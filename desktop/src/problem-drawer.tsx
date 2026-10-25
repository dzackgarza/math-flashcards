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
import {
  request,
  problemCacheSchema,
  problemStoredSchema,
  type CheckErrorKind,
} from "./bridge";

const colors = {
  LaTeX: "red",
  "Card structure": "red",
  "Empty answer": "orange",
} as const;

// Completed deck checks are valid for their source and asset identity.
// Yield between cards and report coverage separately from problem counts.
export function useProblems(
  mathjax: MathJaxRuntime | null,
  decks: { path: string; source: string; revision: string }[],
  assetIdentity: string,
  root: string,
  generation: number,
  cacheEpoch: number,
): {
  problems: Problem[];
  checked: number;
  error: string;
  cacheFailure: boolean;
} {
  const checked = useRef(
    new Map<
      string,
      {
        root: string;
        source: string;
        assetIdentity: string;
        cacheEpoch: number;
        problems: Problem[];
      }
    >(),
  );
  const [, publish] = useState(0);
  const [failure, setFailure] = useState<{
    root: string;
    kind: CheckErrorKind;
    message: string;
  } | null>(null);
  useEffect(() => {
    if (!mathjax || !root || !assetIdentity) return;
    let cancelled = false;
    setFailure(null);
    const current = (deck: { path: string; source: string }) => {
      const result = checked.current.get(deck.path);
      return (
        result?.root === root &&
        result.source === deck.source &&
        result.assetIdentity === assetIdentity &&
        result.cacheEpoch === cacheEpoch
      );
    };
    const input = {
      workspace: root,
      generation,
      producer: __CHECKER_IDENTITY__,
      assets: assetIdentity,
    };
    (async () => {
      let cacheHealthy = true;
      for (let offset = 0; offset < decks.length; offset += 8) {
        const pending = decks
          .slice(offset, offset + 8)
          .filter((deck) => !current(deck));
        if (!pending.length) continue;
        const unavailable = new Set<string>();
        if (cacheHealthy) {
          const response = await request(
            {
              ...input,
              action: "problems",
              entries: pending.map(({ path, revision }) => ({
                path,
                revision,
              })),
            },
            problemCacheSchema,
          );
          if (cancelled) return;
          if (
            response.session.root !== root ||
            response.session.generation !== generation
          )
            throw new Error(
              "The problem cache belongs to another workspace session.",
            );
          for (const result of response.results) {
            const deck = pending.find((deck) => deck.path === result.path);
            if (!deck)
              throw new Error(
                "The problem cache returned a deck outside its request.",
              );
            if (result.state === "ready") {
              if (
                result.revision !== deck.revision ||
                result.producer !== input.producer ||
                result.assets !== assetIdentity
              )
                throw new Error(
                  "The saved Problems result has a different input identity.",
                );
              checked.current.set(deck.path, {
                root,
                source: deck.source,
                assetIdentity,
                cacheEpoch,
                problems: result.problems,
              });
              continue;
            }
            if (result.state === "superseded") unavailable.add(result.path);
            if (result.state === "failed") {
              setFailure({
                root,
                kind: result.kind,
                message: result.path + ": " + result.message,
              });
              if (result.kind === "CacheFailure") cacheHealthy = false;
              else unavailable.add(result.path);
            }
          }
          publish((version) => version + 1);
        }
        for (const deck of pending) {
          if (current(deck) || unavailable.has(deck.path)) continue;
          const problems: Problem[] = [];
          for (const batch of problemBatches(mathjax, deck.path, deck.source)) {
            problems.push(...batch);
            await new Promise((resolve) => setTimeout(resolve));
            if (cancelled) return;
          }
          if (cacheHealthy) {
            const response = await request(
              {
                ...input,
                action: "store-problems",
                entries: [
                  { path: deck.path, revision: deck.revision, problems },
                ],
              },
              problemStoredSchema,
            );
            if (cancelled) return;
            if (
              response.session.root !== root ||
              response.session.generation !== generation
            )
              throw new Error(
                "The saved Problems response belongs to another session.",
              );
            const result = response.results[0];
            if (!result || result.path !== deck.path)
              throw new Error(
                "The Problems publication did not identify its deck.",
              );
            if (result.state === "superseded") continue;
            if (result.state === "failed") {
              setFailure({
                root,
                kind: result.kind,
                message: result.path + ": " + result.message,
              });
              if (result.kind !== "CacheFailure") continue;
              cacheHealthy = false;
            }
          }
          checked.current.set(deck.path, {
            root,
            source: deck.source,
            assetIdentity,
            cacheEpoch,
            problems,
          });
          publish((version) => version + 1);
        }
      }
    })().catch((error) => {
      if (!cancelled)
        setFailure({ root, kind: "BackendFailure", message: String(error) });
    });
    return () => {
      cancelled = true;
    };
  }, [mathjax, decks, assetIdentity, root, generation, cacheEpoch]);
  const valid = decks.flatMap((deck) => {
    const result = checked.current.get(deck.path);
    return result?.root === root &&
      result.source === deck.source &&
      result.assetIdentity === assetIdentity &&
      result.cacheEpoch === cacheEpoch
      ? [result]
      : [];
  });
  return {
    problems: valid.flatMap((result) => result.problems),
    checked: valid.length,
    error: failure?.root === root ? failure.message : "",
    cacheFailure: failure?.root === root && failure.kind === "CacheFailure",
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
  manifestReady,
  mathjax,
  opened,
  close,
  open,
}: {
  problems: Problem[] | null;
  decks: number;
  checked: number;
  manifestReady: boolean;
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
      {manifestReady && checked < decks && (
        <Text c="dimmed" mb="sm">
          Checking decks: {checked} of {decks}. Results are incomplete.
        </Text>
      )}
      {!manifestReady ? (
        <Text c="dimmed">Refreshing workspace membership…</Text>
      ) : problems === null || (checked < decks && problems.length === 0) ? (
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
