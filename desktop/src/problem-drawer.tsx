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
import { deckProblems, type Problem } from "./problems";

const colors = {
  LaTeX: "red",
  "Card structure": "red",
  "Empty answer": "orange",
} as const;

// The problems of every deck, or null until the first check ends. A deck is
// checked again only when its source changes. The check yields between decks
// so that typing stays responsive.
export function useProblems(
  mathjax: MathJaxRuntime | null,
  decks: { path: string; source: string }[],
): Problem[] | null {
  const checked = useRef(
    new Map<string, { source: string; problems: Problem[] }>(),
  );
  const [problems, setProblems] = useState<Problem[] | null>(null);
  useEffect(() => {
    if (!mathjax) return;
    let cancelled = false;
    (async () => {
      for (const deck of decks) {
        if (checked.current.get(deck.path)?.source === deck.source) continue;
        checked.current.set(deck.path, {
          source: deck.source,
          problems: deckProblems(mathjax, deck.path, deck.source),
        });
        await new Promise((resolve) => setTimeout(resolve));
        if (cancelled) return;
      }
      setProblems(
        decks.flatMap((deck) => checked.current.get(deck.path)!.problems),
      );
    })();
    return () => {
      cancelled = true;
    };
  }, [mathjax, decks]);
  return problems;
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
  mathjax,
  opened,
  close,
  open,
}: {
  problems: Problem[] | null;
  decks: number;
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
      {problems === null ? (
        <Text c="dimmed">Checking the decks…</Text>
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
