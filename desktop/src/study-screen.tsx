import { useEffect, useLayoutEffect, useRef, useState } from "react";
import { Alert, Button, Group, Kbd, Stack, Text, Title } from "@mantine/core";
import { request, studyNextSchema, type StudyNext } from "./bridge";
import { SideEditor } from "./editor";
import type { MathJaxRuntime } from "./math";

type Grade = "again" | "hard" | "good" | "easy";
const grades: Grade[] = ["again", "hard", "good", "easy"];

function Presentation({
  workspace,
  session,
  card,
  mathjax,
  onNext,
  onClose,
}: {
  workspace: string;
  session: number;
  card: Extract<StudyNext, { state: "Card" }>;
  mathjax: MathJaxRuntime | null;
  onNext: (next: StudyNext) => void;
  onClose: () => void;
}) {
  const clock = useRef({
    started: 0,
    revealed: null as number | null,
    away: null as number | null,
    unfocused: 0,
  });
  const sending = useRef(false);
  const [revealed, setRevealed] = useState(false);
  const [pending, setPending] = useState(false);
  const [error, setError] = useState("");
  useLayoutEffect(() => {
    const started = performance.now();
    clock.current = {
      started,
      revealed: null,
      away: document.hidden || !document.hasFocus() ? started : null,
      unfocused: 0,
    };
    function focus(event: Event) {
      const timing = clock.current;
      const now = Math.max(timing.started, event.timeStamp);
      if (document.hidden || !document.hasFocus()) timing.away ??= now;
      else if (timing.away !== null) {
        timing.unfocused += now - timing.away;
        timing.away = null;
      }
    }
    window.addEventListener("focus", focus);
    window.addEventListener("blur", focus);
    document.addEventListener("visibilitychange", focus);
    return () => {
      window.removeEventListener("focus", focus);
      window.removeEventListener("blur", focus);
      document.removeEventListener("visibilitychange", focus);
    };
  }, []);
  function reveal(at: number) {
    if (clock.current.revealed !== null || sending.current) return;
    clock.current.revealed = Math.max(clock.current.started, at);
    setRevealed(true);
  }
  async function grade(value: Grade, at: number) {
    const timing = clock.current;
    if (timing.revealed === null || sending.current) return;
    sending.current = true;
    setPending(true);
    setError("");
    try {
      const next = await request(
        {
          action: "study-answer",
          workspace,
          session,
          presentation: card.presentation,
          grade: value,
          timing: {
            reveal_ms: Math.round(timing.revealed - timing.started),
            grade_ms: Math.round(
              Math.max(timing.revealed, at) - timing.revealed,
            ),
            unfocused_ms: Math.round(
              timing.unfocused + (timing.away === null ? 0 : at - timing.away),
            ),
          },
        },
        studyNextSchema,
      );
      onNext(next);
    } catch (failure) {
      if (String(failure).includes("StaleCard")) {
        try {
          onNext(
            await request(
              { action: "study-next", workspace, session },
              studyNextSchema,
            ),
          );
        } catch (currentFailure) {
          setError(String(currentFailure));
        }
      } else setError(String(failure));
    } finally {
      sending.current = false;
      setPending(false);
    }
  }
  useEffect(() => {
    function key(event: KeyboardEvent) {
      if (
        event.repeat ||
        event.altKey ||
        event.ctrlKey ||
        event.metaKey ||
        sending.current
      )
        return;
      if (event.key === "Escape") {
        event.preventDefault();
        onClose();
      } else if (event.code === "Space") {
        event.preventDefault();
        reveal(event.timeStamp);
      } else if (
        ["1", "2", "3", "4"].includes(event.key) &&
        clock.current.revealed !== null
      ) {
        event.preventDefault();
        void grade(grades[Number(event.key) - 1], event.timeStamp);
      }
    }
    window.addEventListener("keydown", key);
    return () => window.removeEventListener("keydown", key);
  });
  return (
    <>
      {error && (
        <Alert color="red" title="Study could not continue">
          {error}
        </Alert>
      )}
      <Text c="dimmed" size="sm">
        {card.deck}
      </Text>
      <SideEditor
        key={card.presentation + "front"}
        minHeight="0"
        side="front"
        value={card.front}
        mathjax={mathjax}
        editable={false}
        onChange={() => {}}
        workspace={workspace}
        path={card.deck}
      />
      {revealed && (
        <SideEditor
          key={card.presentation + "back"}
          minHeight="0"
          side="back"
          value={card.back}
          mathjax={mathjax}
          editable={false}
          onChange={() => {}}
          workspace={workspace}
          path={card.deck}
        />
      )}
      <Group className="study-grades" justify="center" grow>
        {revealed ? (
          grades.map((value, index) => (
            <Button
              key={value}
              variant="default"
              size="md"
              disabled={pending}
              onClick={(event) => void grade(value, event.timeStamp)}
            >
              <Stack gap={2} align="center">
                <span>
                  {value[0].toUpperCase() + value.slice(1)}{" "}
                  <Kbd>{index + 1}</Kbd>
                </span>
                <Text size="sm">{card.labels[value]}</Text>
              </Stack>
            </Button>
          ))
        ) : (
          <Button size="md" onClick={(event) => reveal(event.timeStamp)}>
            Show answer <Kbd ml="sm">Space</Kbd>
          </Button>
        )}
      </Group>
    </>
  );
}

export function StudyScreen({
  workspace,
  session,
  next,
  mathjax,
  record,
  onNext,
  onClose,
}: {
  workspace: string;
  session: number;
  next: StudyNext;
  mathjax: MathJaxRuntime | null;
  record: string;
  onNext: (next: StudyNext) => void;
  onClose: () => void;
}) {
  useEffect(() => {
    if (next.state !== "Finished") return;
    function key(event: KeyboardEvent) {
      if (event.key === "Escape") {
        event.preventDefault();
        onClose();
      }
    }
    window.addEventListener("keydown", key);
    return () => window.removeEventListener("keydown", key);
  }, [next.state, onClose]);
  return (
    <Stack
      component="section"
      aria-label="Study session"
      className="study-screen"
      gap="lg"
    >
      <Group justify="space-between">
        <Title order={2}>Study</Title>
        <Button variant="default" onClick={onClose}>
          Return to editor <Kbd ml="sm">Esc</Kbd>
        </Button>
      </Group>
      <Group gap="lg" aria-label="Remaining cards">
        <Text>New: {next.counts.new}</Text>
        <Text>Learning: {next.counts.learning}</Text>
        <Text>Review: {next.counts.review}</Text>
      </Group>
      {next.state === "Card" ? (
        <Presentation
          key={next.presentation}
          workspace={workspace}
          session={session}
          card={next}
          mathjax={mathjax}
          onNext={onNext}
          onClose={onClose}
        />
      ) : (
        <Stack align="center" py="xl">
          <Title order={3}>Study complete for now</Title>
          <Text>Graded today: {next.graded_today}</Text>
          {next.next_learning_seconds !== null && (
            <Text>
              Next learning card in {Math.ceil(next.next_learning_seconds / 60)}{" "}
              minutes.
            </Text>
          )}
        </Stack>
      )}
      <Text size="sm" c="dimmed" className="study-record">
        Learning record: {record}
      </Text>
    </Stack>
  );
}
