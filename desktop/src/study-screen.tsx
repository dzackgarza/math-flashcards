import { useEffect, useLayoutEffect, useRef, useState } from "react";
import {
  Alert,
  Button,
  Group,
  Kbd,
  Modal,
  Stack,
  Table,
  Text,
  TextInput,
  Title,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { useHotkeys } from "@mantine/hooks";
import {
  request,
  studyNextSchema,
  studyOpenSchema,
  studySettingsSchema,
  studyFitSchema,
  storeCopySchema,
  type StudyFit,
  type StudyNext,
  type StudyOpen,
} from "./bridge";
import { SideEditor } from "./editor";
import type { MathJaxRuntime } from "./math";
import { isTauri } from "@tauri-apps/api/core";
import { revealItemInDir } from "@tauri-apps/plugin-opener";
import { dirname } from "pathe";
import { open } from "@tauri-apps/plugin-dialog";

type Grade = "again" | "hard" | "good" | "easy";
const grades: Grade[] = ["again", "hard", "good", "easy"];

function StudySettings({
  workspace,
  onSaved,
  onClose,
  onCopied,
}: {
  workspace: string;
  onSaved: () => Promise<void>;
  onClose: () => void;
  onCopied: () => Promise<void>;
}) {
  const form = useForm({
    initialValues: {
      new_per_day: "",
      reviews_per_day: "",
      desired_retention: "",
    },
  });
  const [ready, setReady] = useState(false);
  const [fit, setFit] = useState<StudyFit | null>(null);
  const [fitting, setFitting] = useState(false);
  const [destination, setDestination] = useState("");
  const [copying, setCopying] = useState(false);
  const [copied, setCopied] = useState("");
  const copyStatus = useRef<HTMLParagraphElement>(null);
  useEffect(() => {
    if (copied && !copying)
      copyStatus.current?.scrollIntoView({ block: "nearest" });
  }, [copied, copying]);
  const [pending, setPending] = useState(false);
  const [error, setError] = useState("");
  useHotkeys(
    [
      [
        "Escape",
        (event) => {
          event.stopPropagation();
          if (!pending) onClose();
        },
      ],
    ],
    [],
    true,
  );
  useEffect(() => {
    let active = true;
    request({ action: "study-open", workspace }, studyOpenSchema)
      .then((opened) => {
        if (!active) return;
        if (opened.state !== "Open")
          throw new Error("Attach a study store before changing settings.");
        const values = {
          new_per_day: String(opened.settings.new_per_day),
          reviews_per_day: String(opened.settings.reviews_per_day),
          desired_retention: String(opened.settings.desired_retention),
        };
        form.setValues(values);
        form.resetDirty(values);
        setReady(true);
      })
      .catch((failure) => {
        if (active) setError(String(failure));
      });
    return () => {
      active = false;
    };
  }, [workspace]);
  async function save(values: typeof form.values) {
    const parsed = studySettingsSchema.safeParse({
      new_per_day: values.new_per_day.trim() ? Number(values.new_per_day) : NaN,
      reviews_per_day: values.reviews_per_day.trim()
        ? Number(values.reviews_per_day)
        : NaN,
      desired_retention: values.desired_retention.trim()
        ? Number(values.desired_retention)
        : NaN,
    });
    if (!parsed.success) {
      form.setErrors(
        Object.fromEntries(
          parsed.error.issues.map((issue) => [
            issue.path[0],
            issue.path[0] === "desired_retention"
              ? "Enter a target from 0.70 to 0.99."
              : "Enter a whole number from 0 to 9999.",
          ]),
        ),
      );
      return;
    }
    setPending(true);
    setError("");
    try {
      await request(
        { action: "study-set-settings", workspace, settings: parsed.data },
        studySettingsSchema,
      );
      await onSaved();
      onClose();
    } catch (failure) {
      setError(String(failure));
    } finally {
      setPending(false);
    }
  }

  async function fitScheduler() {
    setPending(true);
    setFitting(true);
    setFit(null);
    setError("");
    try {
      setFit(await request({ action: "study-fit", workspace }, studyFitSchema));
    } catch (failure) {
      setError(String(failure));
    } finally {
      setPending(false);
      setFitting(false);
    }
  }

  async function applyFit() {
    if (!fit) return;
    setPending(true);
    setError("");
    try {
      await request(
        { action: "study-apply-fit", workspace, parameters: fit.parameters },
        studySettingsSchema,
      );
      await onSaved();
      onClose();
    } catch (failure) {
      setError(String(failure));
    } finally {
      setPending(false);
    }
  }

  async function saveCopy() {
    setPending(true);
    setCopying(true);
    setCopied("");
    setError("");
    try {
      const result = await request(
        { action: "study-copy", workspace, directory: destination },
        storeCopySchema,
      );
      setCopied(result.path);
      await onCopied();
    } catch (failure) {
      setError(String(failure));
    } finally {
      setPending(false);
      setCopying(false);
    }
  }
  return (
    <Modal
      opened
      title="Study settings"
      onClose={onClose}
      closeOnEscape={false}
      closeOnClickOutside={!pending}
      withCloseButton={!pending}
    >
      <form onSubmit={form.onSubmit(save)}>
        <Stack>
          <Text size="sm">
            These settings apply to the whole workspace. Initial values are Anki
            defaults.
          </Text>
          {error && <Alert color="red">{error}</Alert>}
          <TextInput
            label="New cards per day"
            description="Whole number from 0 to 9999"
            inputMode="numeric"
            disabled={!ready || pending}
            {...form.getInputProps("new_per_day")}
          />
          <TextInput
            label="Reviews per day"
            description="Whole number from 0 to 9999"
            inputMode="numeric"
            disabled={!ready || pending}
            {...form.getInputProps("reviews_per_day")}
          />
          <TextInput
            label="Target recall"
            description="0.70 to 0.99. A higher target schedules reviews sooner."
            inputMode="decimal"
            disabled={!ready || pending}
            {...form.getInputProps("desired_retention")}
          />
          <Button type="submit" disabled={!ready || pending}>
            Save settings
          </Button>
          {form.isDirty() && (
            <Text size="sm">Save changed settings before fitting.</Text>
          )}
          <Button
            variant="default"
            disabled={!ready || pending || form.isDirty()}
            loading={fitting}
            onClick={() => void fitScheduler()}
          >
            Fit scheduler
          </Button>
          {fitting && (
            <Text role="status">Fitting scheduler to stored reviews…</Text>
          )}
          {fit && (
            <Stack component="section" aria-label="Scheduler fit">
              <Title order={3}>Scheduler fit</Title>
              <Text size="sm">Review observations used: {fit.reviews}</Text>
              <Text size="sm">
                Lower log loss and RMSE mean closer predictions of the stored
                self-graded recall. These measures describe the history used for
                fitting.
              </Text>
              <Table>
                <Table.Thead>
                  <Table.Tr>
                    <Table.Th>Measure</Table.Th>
                    <Table.Th>Current</Table.Th>
                    <Table.Th>Fitted</Table.Th>
                  </Table.Tr>
                </Table.Thead>
                <Table.Tbody>
                  <Table.Tr>
                    <Table.Th>Log loss</Table.Th>
                    <Table.Td>{fit.current_log_loss.toPrecision(6)}</Table.Td>
                    <Table.Td>{fit.log_loss.toPrecision(6)}</Table.Td>
                  </Table.Tr>
                  <Table.Tr>
                    <Table.Th>RMSE</Table.Th>
                    <Table.Td>{fit.current_rmse_bins.toPrecision(6)}</Table.Td>
                    <Table.Td>{fit.rmse_bins.toPrecision(6)}</Table.Td>
                  </Table.Tr>
                </Table.Tbody>
              </Table>
              {fit.parameters.every(
                (value, index) => value === Math.fround(fit.current[index]),
              ) && <Text size="sm">Anki retained the current parameters.</Text>}
              <details>
                <summary>Current parameters</summary>
                <Text size="xs" style={{ overflowWrap: "anywhere" }}>
                  {fit.current.join(", ")}
                </Text>
              </details>
              <details>
                <summary>Fitted parameters</summary>
                <Text size="xs" style={{ overflowWrap: "anywhere" }}>
                  {fit.parameters.join(", ")}
                </Text>
              </details>
              <Group>
                <Button
                  disabled={pending || form.isDirty()}
                  onClick={() => void applyFit()}
                >
                  Apply fit
                </Button>
                <Button
                  variant="default"
                  disabled={pending}
                  onClick={() => setFit(null)}
                >
                  Close fit
                </Button>
              </Group>
            </Stack>
          )}
          <Title order={3}>Save a copy</Title>
          <Text size="sm">
            Copy the complete learning store to a chosen folder. This includes
            scheduling, recorded history, and retained images.
          </Text>
          <TextInput
            label="Copy destination"
            value={destination}
            onChange={(event) => setDestination(event.currentTarget.value)}
            disabled={pending}
          />
          {isTauri() && (
            <Button
              variant="default"
              disabled={pending}
              onClick={async () => {
                try {
                  const directory = await open({
                    directory: true,
                    multiple: false,
                    title: "Choose a destination for the learning store",
                  });
                  if (directory) setDestination(directory);
                } catch (failure) {
                  setError(String(failure));
                }
              }}
            >
              Choose copy folder
            </Button>
          )}
          <Button
            disabled={pending || !destination.trim()}
            loading={copying}
            onClick={() => void saveCopy()}
          >
            Save a copy
          </Button>
          {copying && <Text role="status">Saving the learning store…</Text>}
          {copied && !copying && (
            <Text
              ref={copyStatus}
              role="status"
              size="sm"
              style={{ overflowWrap: "anywhere" }}
            >
              Copy saved: {copied}
            </Text>
          )}
        </Stack>
      </form>
    </Modal>
  );
}

export function StudyStoreChoice({
  workspace,
  stores,
  onAttached,
  onClose,
}: {
  workspace: string;
  stores: Extract<StudyOpen, { state: "Unattached" }>["stores"];
  onAttached: () => void;
  onClose: () => void;
}) {
  const [pending, setPending] = useState(false);
  const [error, setError] = useState("");
  async function attach(store: string | null) {
    if (pending) return;
    setPending(true);
    setError("");
    try {
      const opened = await request(
        {
          action: "study-attach",
          workspace,
          choice:
            store === null ? { kind: "new" } : { kind: "existing", store },
        },
        studyOpenSchema,
      );
      if (opened.state !== "Open")
        throw new Error("The study store did not attach.");
      onAttached();
    } catch (failure) {
      setError(String(failure));
    } finally {
      setPending(false);
    }
  }
  return (
    <Modal
      opened
      title="Choose a study store"
      onClose={onClose}
      size="lg"
      closeOnClickOutside={!pending}
      closeOnEscape={!pending}
      withCloseButton={!pending}
    >
      <Stack>
        <Text>
          Attach the learning history for this workspace, or start a new store.
        </Text>
        {error && <Alert color="red">{error}</Alert>}
        {stores.map((store) => (
          <Stack
            key={store.store}
            gap="xs"
            component="section"
            aria-label={store.paths.at(-1)}
          >
            <Text fw={600} style={{ overflowWrap: "anywhere" }}>
              {store.paths.at(-1)}
            </Text>
            <Text size="sm">
              {store.path_exists
                ? "Folder exists"
                : "Folder moved or unavailable"}
            </Text>
            <Text size="sm">
              Last used: {new Date(store.last_used).toLocaleString()}
            </Text>
            <Group>
              <Text>Cards: {store.cards}</Text>
              <Text>Grades: {store.responses}</Text>
            </Group>
            {store.paths.length > 1 && (
              <Text size="sm" c="dimmed">
                Earlier paths: {store.paths.slice(0, -1).join(", ")}
              </Text>
            )}
            <Button
              variant="default"
              aria-label={`Attach ${store.paths.at(-1)}`}
              disabled={pending}
              onClick={() => void attach(store.store)}
            >
              Attach
            </Button>
          </Stack>
        ))}
        <Group justify="space-between">
          <Button variant="subtle" disabled={pending} onClick={onClose}>
            Keep editing
          </Button>
          <Button disabled={pending} onClick={() => void attach(null)}>
            Start new
          </Button>
        </Group>
      </Stack>
    </Modal>
  );
}

function Presentation({
  workspace,
  session,
  card,
  mathjax,
  onNext,
  onClose,
  shortcuts,
}: {
  workspace: string;
  session: number;
  card: Extract<StudyNext, { state: "Card" }>;
  mathjax: MathJaxRuntime | null;
  onNext: (next: StudyNext) => void;
  onClose: () => void;
  shortcuts: boolean;
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
        !shortcuts ||
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
        media={card.media}
        references={card.references}
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
          media={card.media}
          references={card.references}
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
          <Button autoFocus size="md" onClick={(event) => reveal(event.timeStamp)}>
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
  onUndo,
  onEdit,
  undoReason,
  onSettings,
  onCopied,
  shortcuts,
}: {
  workspace: string;
  session: number;
  next: StudyNext;
  mathjax: MathJaxRuntime | null;
  record: string;
  onNext: (next: StudyNext) => void;
  onClose: () => void;
  onUndo: () => Promise<void>;
  onEdit: () => Promise<void>;
  undoReason: string;
  onSettings: () => Promise<void>;
  onCopied: () => Promise<void>;
  shortcuts: boolean;
}) {
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [folderError, setFolderError] = useState("");
  const [actionError, setActionError] = useState("");
  const [pending, setPending] = useState(false);
  const running = useRef(false);
  async function act(action: () => Promise<void>) {
    if (running.current) return;
    running.current = true;
    setPending(true);
    setActionError("");
    try {
      await action();
    } catch (failure) {
      setActionError(String(failure));
    } finally {
      running.current = false;
      setPending(false);
    }
  }
  useEffect(() => {
    function key(event: KeyboardEvent) {
      if (!shortcuts || settingsOpen || event.repeat || event.altKey) return;
      if (
        (event.ctrlKey || event.metaKey) &&
        event.key.toLowerCase() === "z" &&
        !event.shiftKey &&
        next.undoable
      ) {
        event.preventDefault();
        void act(onUndo);
      } else if (
        !event.ctrlKey &&
        !event.metaKey &&
        event.key.toLowerCase() === "e" &&
        next.state === "Card"
      ) {
        event.preventDefault();
        void act(onEdit);
      }
    }
    window.addEventListener("keydown", key);
    return () => window.removeEventListener("keydown", key);
  }, [next, onUndo, onEdit, settingsOpen, shortcuts]);
  useEffect(() => {
    if (next.state !== "Finished" || settingsOpen || !shortcuts) return;
    function key(event: KeyboardEvent) {
      if (event.key === "Escape") {
        event.preventDefault();
        onClose();
      }
    }
    window.addEventListener("keydown", key);
    return () => window.removeEventListener("keydown", key);
  }, [next.state, onClose, settingsOpen, shortcuts]);
  return (
    <Stack
      component="section"
      aria-label="Study session"
      className="study-screen"
      gap="lg"
    >
      <Group justify="space-between">
        <Title order={2}>Study</Title>
        <Group gap="xs">
          <Button
            variant="default"
            disabled={pending}
            onClick={() => setSettingsOpen(true)}
          >
            Study settings
          </Button>
          <Button
            variant="default"
            aria-label="Undo"
            title={next.undoable ? "Undo the last grade" : undoReason}
            disabled={pending || !next.undoable}
            onClick={() => void act(onUndo)}
          >
            Undo <Kbd ml="sm">Ctrl Z</Kbd>
          </Button>
          {next.state === "Card" && (
            <Button
              variant="default"
              disabled={pending}
              onClick={() => void act(onEdit)}
            >
              Edit <Kbd ml="sm">E</Kbd>
            </Button>
          )}
          <Button variant="default" onClick={onClose}>
            Return to editor <Kbd ml="sm">Esc</Kbd>
          </Button>
        </Group>
      </Group>
      {actionError && <Alert color="red">{actionError}</Alert>}
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
          shortcuts={!settingsOpen && shortcuts}
        />
      ) : (
        <Stack align="center" py="xl">
          <Title order={3}>Study complete for now</Title>
          <Text>{next.studied_today}</Text>
          {next.next_learning_seconds !== null && (
            <Text>
              Next learning card in {Math.ceil(next.next_learning_seconds / 60)}{" "}
              minutes.
            </Text>
          )}
        </Stack>
      )}
      <Stack gap="xs" className="study-record">
        <Text size="sm" c="dimmed">
          Study store: {dirname(record)}
        </Text>
        <Text size="sm" c="dimmed">
          Learning record: {record}
        </Text>
        {isTauri() && (
          <Button
            variant="subtle"
            onClick={() =>
              void revealItemInDir(record).catch((failure) =>
                setFolderError(String(failure)),
              )
            }
          >
            Open learning folder
          </Button>
        )}
        {folderError && <Alert color="red">{folderError}</Alert>}
      </Stack>
      {settingsOpen && (
        <StudySettings
          workspace={workspace}
          onSaved={onSettings}
          onCopied={onCopied}
          onClose={() => setSettingsOpen(false)}
        />
      )}
    </Stack>
  );
}
