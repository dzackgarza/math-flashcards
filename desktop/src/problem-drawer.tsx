import { useEffect, useRef, useState } from "react";
import {
  Badge,
  Code,
  Drawer,
  Group,
  Stack,
  Text,
  UnstyledButton,
} from "@mantine/core";
import { previewHtml, type MathJaxRuntime } from "./math";
import { deckName } from "./organize";
import { problemBatches, type Problem } from "./problems";

const colors = {
  LaTeX: "red",
  "Card structure": "red",
  "Empty answer": "orange",
} as const;

// Completed deck checks are valid for their source and asset identity.
// Yield between cards and report coverage separately from problem counts.
export function useProblems(
  mathjax: MathJaxRuntime | null,
  decks: { path: string; source: string }[],
  assetIdentity: string,
): { problems: Problem[]; checked: number } {
  const checked = useRef(
    new Map<
      string,
      { source: string; assetIdentity: string; problems: Problem[] }
    >(),
  );
  const [, publish] = useState(0);
  useEffect(() => {
    if (!mathjax) return;
    let cancelled = false;
    (async () => {
      for (const deck of decks) {
        const previous = checked.current.get(deck.path);
        if (
          previous?.source === deck.source &&
          previous.assetIdentity === assetIdentity
        )
          continue;
        const problems: Problem[] = [];
        for (const batch of problemBatches(mathjax, deck.path, deck.source)) {
          problems.push(...batch);
          await new Promise((resolve) => setTimeout(resolve));
          if (cancelled) return;
        }
        checked.current.set(deck.path, {
          source: deck.source,
          assetIdentity,
          problems,
        });
        publish((version) => version + 1);
        await new Promise((resolve) => setTimeout(resolve));
        if (cancelled) return;
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [mathjax, decks, assetIdentity]);
  const valid = decks.flatMap((deck) => {
    const result = checked.current.get(deck.path);
    return result?.source === deck.source &&
      result.assetIdentity === assetIdentity
      ? [result]
      : [];
  });
  return {
    problems: valid.flatMap((result) => result.problems),
    checked: valid.length,
  };
}

function ProblemRow({
  problem,
  mathjax,
  open,
}: {
  problem: Problem;
  mathjax: MathJaxRuntime | null;
  open: () => void;
}) {
  return (
    <UnstyledButton className="problem-row" onClick={open}>
      <Group gap="xs" wrap="nowrap" align="start">
        <Badge
          size="sm"
          variant="light"
          color={colors[problem.kind]}
          className="change-kind"
        >
          {problem.kind}
        </Badge>
        {problem.label === null ? (
          <span className="change-front">The whole deck</span>
        ) : mathjax ? (
          <span
            className="change-front"
            dangerouslySetInnerHTML={{
              __html: previewHtml(mathjax, problem.label),
            }}
          />
        ) : (
          <span className="change-front">{problem.label}</span>
        )}
        {problem.side && (
          <Text size="sm" c="dimmed" className="problem-side">
            {problem.side === "front" ? "Front" : "Back"}
          </Text>
        )}
      </Group>
      <Text size="sm" className="problem-message">
        {problem.message}
      </Text>
      {problem.source && (
        <Code block className="problem-source">
          {problem.source}
        </Code>
      )}
    </UnstyledButton>
  );
}

// Lists the problems of every deck, grouped by deck. Selecting a problem opens
// its card.
export function ProblemDrawer({
  problems,
  decks,
  checked,
  mathjax,
  opened,
  close,
  open,
}: {
  problems: Problem[] | null;
  decks: number;
  checked: number;
  mathjax: MathJaxRuntime | null;
  opened: boolean;
  close: () => void;
  open: (problem: Problem) => void;
}) {
  const groups = new Map<string, Problem[]>();
  for (const problem of problems ?? [])
    groups.set(problem.path, [...(groups.get(problem.path) ?? []), problem]);
  return (
    <Drawer
      opened={opened}
      onClose={close}
      position="right"
      size="xl"
      title={
        problems?.length
          ? problems.length === 1
            ? "1 problem"
            : problems.length + " problems"
          : "Problems"
      }
    >
      {checked < decks && (
        <Text c="dimmed" mb="sm">
          Checking decks: {checked} of {decks}. Results are incomplete.
        </Text>
      )}
      {problems === null || (checked < decks && problems.length === 0) ? (
        <Text c="dimmed">Checking the available decks…</Text>
      ) : problems.length === 0 ? (
        <Text c="dimmed">
          Every equation renders and every card has an answer in all {decks}{" "}
          decks.
        </Text>
      ) : (
        <Stack gap="lg">
          {[...groups].map(([path, deckProblems]) => (
            <section key={path} className="review-deck">
              <Group justify="space-between" align="baseline">
                <Text fw={600}>{deckName(path)}</Text>
                <Text size="sm" c="dimmed">
                  {path.split("/").slice(0, -1).join(" / ")}
                </Text>
              </Group>
              <Stack gap={4} mt={6}>
                {deckProblems.map((problem, index) => (
                  <ProblemRow
                    key={index}
                    problem={problem}
                    mathjax={mathjax}
                    open={() => open(problem)}
                  />
                ))}
              </Stack>
            </section>
          ))}
        </Stack>
      )}
    </Drawer>
  );
}
