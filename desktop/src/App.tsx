import { useEffect, useMemo, useRef, useState } from "react";
import {
  Alert,
  AppShell,
  Badge,
  Box,
  Button,
  Card,
  Divider,
  Group,
  Loader,
  Paper,
  ScrollArea,
  SegmentedControl,
  Stack,
  Text,
  TextInput,
  TagsInput,
  Title,
  Tree,
  type TreeNodeData,
} from "@mantine/core";
import { useDebouncedCallback, useDebouncedValue } from "@mantine/hooks";
import { modals } from "@mantine/modals";
import { useForm } from "@mantine/form";
import CodeMirror from "@uiw/react-codemirror";
import { isTauri } from "@tauri-apps/api/core";
import { getCurrentWindow } from "@tauri-apps/api/window";
import { appConfigDir, join } from "@tauri-apps/api/path";
import { open } from "@tauri-apps/plugin-dialog";
import { load } from "@tauri-apps/plugin-store";
import { watch } from "@tauri-apps/plugin-fs";
import { MathJax, MathJaxContext } from "better-react-mathjax";
import DOMPurify from "dompurify";
import {
  cards,
  replaceField,
  replaceTags,
  removeCard,
  newCard,
  type CardRange,
} from "./cards";
import { cardLanguage } from "./editor";
import Organizer from "./Organizer";
import {
  request,
  workspaceSchema,
  documentSchema,
  previewSchema,
  generatedSchema,
  type Document,
  type Preview,
  type Summary,
} from "./bridge";

type Task = "Idle" | "Loading" | "Saving" | "Generating";
type Side = "Front" | "Back";

function preferences() {
  return appConfigDir()
    .then((directory) => join(directory, "preferences.json"))
    .then((path) =>
      load(path, {
        defaults: { workspace: __DEFAULT_WORKSPACE__ },
        autoSave: false,
      }),
    );
}

function treeData(decks: Summary[], filter: string): TreeNodeData[] {
  const roots: TreeNodeData[] = [];
  for (const deck of decks.filter((item) =>
    item.path.toLowerCase().includes(filter.toLowerCase()),
  )) {
    let children = roots;
    let value = "";
    const parts = deck.path.split("/");
    for (const [index, part] of parts.entries()) {
      value += "/" + part;
      let node = children.find((item) => item.value === value);
      if (!node) {
        node = { value, label: part.replace(/\.md$/, "") };
        if (index < parts.length - 1) node.children = [];
        children.push(node);
      }
      if (node.children) children = node.children;
    }
  }
  return roots;
}

export default function App() {
  const [view, setView] = useState<"Organize" | "Edit">("Organize");
  const [organizerDeck, setOrganizerDeck] = useState<string | null>(null);
  const workspaceForm = useForm({
    mode: "uncontrolled",
    initialValues: { workspace: "" },
    validate: {
      workspace: (value) =>
        value.trim() ? null : "Choose a workspace folder.",
    },
  });
  const [workspace, setWorkspace] = useState("");
  const [decks, setDecks] = useState<Summary[]>([]);
  const [document, setDocument] = useState<Document | null>(null);
  const [preview, setPreview] = useState<Preview | null>(null);
  const [previewError, setPreviewError] = useState("");
  const [previewLoading, setPreviewLoading] = useState(false);
  const [index, setIndex] = useState(0);
  const [draft, setDraft] = useState<{
    source: string;
    card: CardRange;
    front: string;
    back: string;
  } | null>(null);
  const [loadRevision, setLoadRevision] = useState(0);
  const [side, setSide] = useState<Side>("Front");
  const [task, setTask] = useState<Task>("Idle");
  const [buildResult, setBuildResult] = useState<"Ready" | "Failed">("Ready");
  const [error, setError] = useState("");
  const [log, setLog] = useState("");
  const [filter, setFilter] = useState("");
  const [cardFilter, setCardFilter] = useState("");
  const [debouncedSource] = useDebouncedValue(document?.source, 400);
  const navigation = useRef(0);
  const parsed = useMemo(() => {
    try {
      return { cards: cards(document?.source ?? ""), error: "" };
    } catch (failure) {
      return { cards: [], error: String(failure) };
    }
  }, [document?.source]);
  const ranges = parsed.cards;
  const dirty = document !== null && document.source !== document.saved;
  const busy = task !== "Idle";
  const selected = ranges[index];
  const rendered = preview?.cards[index];
  const data = useMemo(() => treeData(decks, filter), [decks, filter]);
  const mismatch =
    preview !== null &&
    !previewLoading &&
    preview.cards.length !== ranges.length;

  async function refresh(root = workspace) {
    if (!root) return;
    const result = await request(
      { action: "list", workspace: root },
      workspaceSchema,
    );
    setDecks(result.decks);
    setDocument((current) => {
      if (!current) return current;
      const summary = result.decks.find((item) => item.path === current.path);
      return summary ? { ...current, status: summary.status } : current;
    });
  }

  const refreshOnChange = useDebouncedCallback(() => {
    refresh().catch((failure) => setError(String(failure)));
  }, 700);

  async function chooseWorkspace(root: string) {
    setTask("Loading");
    setError("");
    try {
      const result = await request(
        { action: "list", workspace: root },
        workspaceSchema,
      );
      navigation.current++;
      setWorkspace(result.root);
      workspaceForm.setFieldValue("workspace", result.root);
      setDecks(result.decks);
      setDocument(null);
      setOrganizerDeck(null);
      setDraft(null);
      setPreview(null);
      setLog("");
      setBuildResult("Ready");
      if (isTauri()) {
        const store = await preferences();
        await store.set("workspace", result.root);
        await store.save();
      }
    } catch (failure) {
      setError(String(failure));
    } finally {
      setTask("Idle");
    }
  }

  function confirmNavigation(action: () => void) {
    if (!dirty) {
      action();
      return;
    }
    modals.openConfirmModal({
      title: "Unsaved changes",
      children: (
        <Text>Discard the unsaved changes before leaving this deck?</Text>
      ),
      labels: { confirm: "Discard changes", cancel: "Keep editing" },
      onConfirm: action,
    });
  }

  async function chooseDeck(path: string, cardId?: string) {
    const token = ++navigation.current;
    setTask("Loading");
    setError("");
    try {
      const result = await request(
        { action: "load", workspace, path },
        documentSchema,
      );
      if (token !== navigation.current) return;
      cards(result.source);
      setDocument({ ...result, path, saved: result.source });
      setOrganizerDeck(path);
      setLoadRevision((revision) => revision + 1);
      selectCard(
        Math.max(
          0,
          cards(result.source).findIndex((card) => card.id === cardId),
        ),
        result.source,
      );
      setSide("Front");
      setPreview(null);
      setPreviewError("");
      setLog("");
      setBuildResult("Ready");
      setCardFilter("");
    } catch (failure) {
      setError(String(failure));
    } finally {
      if (token === navigation.current) setTask("Idle");
    }
  }

  useEffect(() => {
    if (!document || debouncedSource !== document.source) return;
    let active = true;
    setPreviewLoading(true);
    setPreviewError("");
    request(
      {
        action: "preview",
        workspace,
        path: document.path,
        source: debouncedSource,
      },
      previewSchema,
    )
      .then((value) => {
        if (active) setPreview(value);
      })
      .catch((failure) => {
        if (active) {
          setPreview(null);
          setPreviewError(String(failure));
        }
      })
      .finally(() => {
        if (active) setPreviewLoading(false);
      });
    return () => {
      active = false;
    };
  }, [
    workspace,
    document?.path,
    document?.source,
    loadRevision,
    debouncedSource,
  ]);

  useEffect(() => {
    if (!isTauri()) {
      void chooseWorkspace(__DEFAULT_WORKSPACE__);
      return;
    }
    preferences()
      .then(async (store) => {
        const saved = await store.get<string>("workspace");
        if (typeof saved !== "string" || !saved)
          throw new Error("The saved workspace must be a folder path.");
        await chooseWorkspace(saved);
      })
      .catch((failure) => setError(String(failure)));
  }, []);

  useEffect(() => {
    const handler = (event: BeforeUnloadEvent) => {
      if (dirty) event.preventDefault();
    };
    window.addEventListener("beforeunload", handler);
    return () => window.removeEventListener("beforeunload", handler);
  }, [dirty]);

  useEffect(() => {
    if (!isTauri()) return;
    const window = getCurrentWindow();
    let disposed = false;
    let stop: (() => void) | undefined;
    window
      .onCloseRequested((event) => {
        if (!dirty) return;
        event.preventDefault();
        confirmNavigation(() => {
          window.destroy().catch((failure) => setError(String(failure)));
        });
      })
      .then((unlisten) => {
        if (disposed) unlisten();
        else stop = unlisten;
      })
      .catch((failure) => setError(String(failure)));
    return () => {
      disposed = true;
      stop?.();
    };
  }, [dirty]);

  useEffect(() => {
    if (!workspace || !isTauri()) return;
    let disposed = false;
    let stop: (() => void) | undefined;
    watch(
      workspace,
      (event) => {
        // Access events describe reads, not changed inputs: https://v2.tauri.app/reference/javascript/fs/#watcheventkind
        if (
          event.type !== "any" &&
          event.type !== "other" &&
          "access" in event.type
        )
          return;
        if (
          !event.paths.some(
            (path) =>
              !/(?:^|\/)(?:\.git|node_modules|src-tauri|test-artifacts)(?:\/|$)/.test(
                path.replace(/\\/g, "/"),
              ) && !path.includes(".flashcards-"),
          )
        )
          return;
        refreshOnChange();
      },
      { recursive: true, delayMs: 700 },
    )
      .then((unwatch) => {
        if (disposed) unwatch();
        else stop = unwatch;
      })
      .catch((failure) => setError(String(failure)));
    return () => {
      disposed = true;
      stop?.();
    };
  }, [workspace, refreshOnChange]);

  function edit(source: string) {
    if (!document || document.source === source) return;
    setDocument((current) => (current ? { ...current, source } : current));
    setPreviewLoading(true);
  }

  function selectCard(cardIndex: number, source: string) {
    setIndex(cardIndex);
    setSide("Front");
    const card = cards(source)[cardIndex];
    setDraft(
      card
        ? { source, card, front: card.front.value, back: card.back.value }
        : null,
    );
  }

  function editCard(field: "front" | "back", value: string) {
    if (!document || !draft) return;
    const next = { ...draft, [field]: value };
    let source = draft.source;
    const sides: ("front" | "back")[] = ["front", "back"];
    for (const side of sides.sort(
      (a, b) => draft.card[b].from - draft.card[a].from,
    )) {
      source = replaceField(source, draft.card[side], next[side]);
    }
    setDraft(next);
    edit(source);
  }

  async function save() {
    if (!document) return;
    const saving = document;
    setTask("Saving");
    setError("");
    try {
      const result = await request(
        {
          action: "save",
          workspace,
          path: saving.path,
          source: saving.source,
          expected: saving.hash,
        },
        documentSchema,
      );
      setDocument((current) =>
        current?.path === saving.path
          ? {
              ...current,
              saved: saving.source,
              hash: result.hash,
              status: result.status,
            }
          : current,
      );
      await refresh();
    } catch (failure) {
      setError(String(failure));
    } finally {
      setTask("Idle");
    }
  }

  async function generate() {
    if (!document || dirty) return;
    setTask("Generating");
    setBuildResult("Ready");
    setError("");
    setLog("Generating the saved deck…");
    try {
      const result = await request(
        { action: "generate", workspace, path: document.path },
        generatedSchema,
      );
      setLog(result.log);
      await refresh();
    } catch (failure) {
      setError(String(failure));
      setLog(String(failure));
      setBuildResult("Failed");
    } finally {
      setTask("Idle");
    }
  }

  function addCard() {
    if (!document) return;
    const source = document.source + "\n\n" + newCard(crypto.randomUUID());
    selectCard(ranges.length, source);
    edit(source);
  }

  function deleteCard() {
    if (!document || !selected) return;
    modals.openConfirmModal({
      title: "Delete card",
      children: <Text>Delete this card from the deck?</Text>,
      labels: { confirm: "Delete", cancel: "Cancel" },
      confirmProps: { color: "red" },
      onConfirm: () => {
        const source = removeCard(document.source, selected);
        selectCard(Math.max(0, index - 1), source);
        edit(source);
      },
    });
  }

  const packageState =
    task === "Generating"
      ? "Generating"
      : buildResult === "Failed"
        ? "Failed"
        : dirty
          ? "Unsynced"
          : document?.status;
  return (
    <AppShell header={{ height: 76 }} padding="lg">
      <AppShell.Header px="lg">
        <Group h="100%" justify="space-between">
          <Box>
            <Title order={1} size="h3">
              Math Flashcards
            </Title>
            <Text size="sm" c="dimmed">
              Write, review, export
            </Text>
          </Box>
          <Group>
            <Text size="sm" c="dimmed">
              {workspace ? "Deck workspace" : "Open a workspace to begin"}
            </Text>
            <SegmentedControl
              aria-label="Workspace view"
              value={view}
              data={["Organize", "Edit"]}
              onChange={(value) =>
                confirmNavigation(() => {
                  setView(value as "Organize" | "Edit");
                  if (value === "Organize") {
                    setDocument(null);
                    setDraft(null);
                    setPreview(null);
                  }
                })
              }
            />
            {busy && <Loader size="sm" aria-label={task} />}
          </Group>
        </Group>
      </AppShell.Header>
      <AppShell.Main>
        <Stack gap="md">
          <Paper withBorder p="md">
            <Group align="end" wrap="wrap">
              <TextInput
                label="Workspace folder"
                placeholder="Folder containing decks/"
                key={workspaceForm.key("workspace")}
                {...workspaceForm.getInputProps("workspace")}
                style={{ flex: 1, minWidth: 220 }}
              />
              {isTauri() && (
                <Button
                  variant="default"
                  onClick={async () => {
                    const selectedFolder = await open({
                      directory: true,
                      multiple: false,
                      title: "Choose the deck workspace",
                    });
                    if (selectedFolder)
                      confirmNavigation(() => {
                        void chooseWorkspace(selectedFolder);
                      });
                  }}
                >
                  Browse
                </Button>
              )}
              <Button
                disabled={busy}
                onClick={() => {
                  if (workspaceForm.validate().hasErrors) return;
                  confirmNavigation(() => {
                    void chooseWorkspace(workspaceForm.getValues().workspace);
                  });
                }}
              >
                Open workspace
              </Button>
              <Button
                variant="default"
                disabled={!workspace || busy}
                onClick={() => {
                  refresh().catch((failure) => setError(String(failure)));
                }}
              >
                Refresh workspace
              </Button>
            </Group>
          </Paper>
          {error && (
            <Alert
              color="red"
              title="Action failed"
              withCloseButton
              onClose={() => setError("")}
            >
              <Text
                size="sm"
                style={{ whiteSpace: "pre-wrap", overflowWrap: "anywhere" }}
              >
                {error}
              </Text>
            </Alert>
          )}
          {view === "Organize" ? (
            <Organizer
              key={workspace}
              workspace={workspace}
              decks={decks}
              onChange={refresh}
              onEdit={(path, id) => {
                setView("Edit");
                void chooseDeck(path, id);
              }}
              initialDeck={organizerDeck}
            />
          ) : (
            <div className="workbench">
              <Paper withBorder p="md" className="deck-panel">
                <Stack gap="sm">
                  <Title order={2} size="h5">
                    Decks
                  </Title>
                  <TextInput
                    aria-label="Find a deck"
                    placeholder="Find a deck…"
                    value={filter}
                    onChange={(event) => setFilter(event.currentTarget.value)}
                  />
                  <ScrollArea h="calc(100vh - 320px)" mih={200}>
                    <Tree
                      data={data}
                      renderNode={({
                        node,
                        expanded,
                        hasChildren,
                        elementProps,
                      }) => (
                        <Group
                          {...elementProps}
                          wrap="nowrap"
                          gap="xs"
                          py={5}
                          onClick={(event) => {
                            elementProps.onClick?.(event);
                            if (!hasChildren && !busy)
                              confirmNavigation(() => {
                                void chooseDeck(node.value.slice(1));
                              });
                          }}
                        >
                          <Text size="sm" c={hasChildren ? "dimmed" : "indigo"}>
                            {hasChildren ? (expanded ? "▾" : "▸") : "▤"}
                          </Text>
                          <Text
                            size="sm"
                            fw={
                              document?.path === node.value.slice(1) ? 700 : 400
                            }
                            style={{ overflowWrap: "anywhere" }}
                          >
                            {node.label}
                          </Text>
                        </Group>
                      )}
                    />
                    {workspace && decks.length === 0 && (
                      <Text c="dimmed" size="sm">
                        This workspace has no Markdown decks.
                      </Text>
                    )}
                  </ScrollArea>
                </Stack>
              </Paper>
              {!document ? (
                <Paper withBorder p="xl">
                  <Stack align="center" justify="center" h={420}>
                    <Title order={2}>Your decks, in one place</Title>
                    <Text c="dimmed" ta="center">
                      Open a workspace, then select a deck to edit and review
                      its cards.
                    </Text>
                  </Stack>
                </Paper>
              ) : (
                <Stack gap="md" className="document-panel">
                  <Paper withBorder p="md">
                    <Group justify="space-between" align="start">
                      <Box>
                        <Title order={2} size="h4">
                          {preview?.title ?? document.path.replace(/\.md$/, "")}
                        </Title>
                        <Text size="sm" c="dimmed">
                          {document.path}
                        </Text>
                      </Box>
                      <Group gap="xs">
                        <Badge
                          color={dirty ? "orange" : "gray"}
                          variant="light"
                        >
                          {dirty ? "Unsaved changes" : "Saved"}
                        </Badge>
                        <Badge
                          color={
                            packageState === "Up to date" ? "teal" : "orange"
                          }
                          variant="light"
                        >
                          {packageState}
                        </Badge>
                      </Group>
                    </Group>
                    <Group mt="md">
                      <Button
                        onClick={save}
                        disabled={!dirty || busy || mismatch || !!parsed.error}
                        loading={task === "Saving"}
                      >
                        Save deck
                      </Button>
                      <Button
                        variant="default"
                        disabled={busy}
                        onClick={() =>
                          confirmNavigation(() => {
                            void chooseDeck(document.path);
                          })
                        }
                      >
                        Reload deck
                      </Button>
                      <Button
                        onClick={generate}
                        disabled={dirty || busy || mismatch || !!parsed.error}
                        loading={task === "Generating"}
                      >
                        Generate Anki deck
                      </Button>
                      <Text size="sm" c="dimmed">
                        {dirty
                          ? "Save your changes before generating."
                          : "Package reflects the saved deck."}
                      </Text>
                    </Group>
                    <Text
                      size="xs"
                      c="dimmed"
                      mt="sm"
                      style={{ overflowWrap: "anywhere" }}
                    >
                      {document.package}
                    </Text>
                  </Paper>
                  <div className="card-workbench">
                    <Paper withBorder p="md">
                      <Stack gap="sm">
                        <Group justify="space-between">
                          <Title order={3} size="h5">
                            Cards
                          </Title>
                          <Button
                            size="compact-sm"
                            variant="light"
                            onClick={addCard}
                            disabled={busy || !!parsed.error}
                          >
                            Add card
                          </Button>
                        </Group>
                        <TextInput
                          aria-label="Find a card"
                          placeholder="Find a card…"
                          value={cardFilter}
                          onChange={(event) =>
                            setCardFilter(event.currentTarget.value)
                          }
                        />
                        <ScrollArea h={420}>
                          <Stack gap={4}>
                            {ranges.map(
                              (range, cardIndex) =>
                                range.label
                                  .toLowerCase()
                                  .includes(cardFilter.toLowerCase()) && (
                                  <Button
                                    key={cardIndex}
                                    variant={
                                      index === cardIndex ? "light" : "subtle"
                                    }
                                    color={
                                      index === cardIndex ? "indigo" : "gray"
                                    }
                                    justify="start"
                                    h="auto"
                                    py="sm"
                                    onClick={() => {
                                      selectCard(cardIndex, document.source);
                                    }}
                                    styles={{
                                      label: {
                                        whiteSpace: "normal",
                                        textAlign: "left",
                                        overflowWrap: "anywhere",
                                      },
                                    }}
                                  >
                                    {range.label}
                                  </Button>
                                ),
                            )}
                          </Stack>
                        </ScrollArea>
                      </Stack>
                    </Paper>
                    <Stack gap="md" className="editor-panel">
                      <Paper withBorder p="md">
                        <Group justify="space-between" mb="sm">
                          <Title order={3} size="h5">
                            Edit card
                          </Title>
                          <Button
                            color="red"
                            variant="subtle"
                            size="compact-sm"
                            onClick={deleteCard}
                            disabled={!selected || busy || !!parsed.error}
                          >
                            Delete card
                          </Button>
                        </Group>
                        {draft ? (
                          <Stack gap="md">
                            {(["front", "back"] as const).map((field) => (
                              <Box
                                key={field}
                                className={"side-editor " + field}
                              >
                                <Title
                                  order={4}
                                  size="h6"
                                  mb="xs"
                                  id={field + "-label"}
                                >
                                  {field === "front" ? "Front" : "Back"}
                                </Title>
                                <CodeMirror
                                  key={
                                    document.path +
                                    ":" +
                                    draft.card.id +
                                    ":" +
                                    field
                                  }
                                  value={draft[field]}
                                  minHeight="100px"
                                  maxHeight="220px"
                                  extensions={[cardLanguage]}
                                  basicSetup={{
                                    lineNumbers: false,
                                    foldGutter: false,
                                  }}
                                  editable={!busy}
                                  onChange={(value) => editCard(field, value)}
                                  aria-label={
                                    field === "front" ? "Front" : "Back"
                                  }
                                />
                              </Box>
                            ))}
                            <TagsInput
                              label="Tags"
                              value={(selected?.tags ?? draft.card.tags)
                                .split(",")
                                .map((tag) => tag.trim())
                                .filter(Boolean)}
                              onChange={(tags) => {
                                if (!selected) return;
                                const source = replaceTags(
                                  document.source,
                                  selected,
                                  tags,
                                );
                                setDraft({
                                  ...draft,
                                  source,
                                  card: cards(source)[index],
                                });
                                edit(source);
                              }}
                              disabled={busy || !!parsed.error}
                            />
                          </Stack>
                        ) : (
                          <Text c="dimmed">Add a card to begin.</Text>
                        )}
                        {parsed.error && (
                          <Alert color="red" title="Invalid card">
                            {parsed.error}
                          </Alert>
                        )}
                      </Paper>
                      <Paper withBorder p="md">
                        <Group justify="space-between" mb="md">
                          <Title order={3} size="h5">
                            Preview
                          </Title>
                          <SegmentedControl
                            aria-label="Card side"
                            value={side}
                            onChange={(value) => setSide(value as Side)}
                            data={["Front", "Back"]}
                          />
                        </Group>
                        {previewLoading ? (
                          <Group justify="center" mih={180}>
                            <Loader size="sm" />
                            <Text c="dimmed">Rendering preview…</Text>
                          </Group>
                        ) : previewError ? (
                          <Alert color="red" title="Preview failed">
                            <Text size="sm" style={{ whiteSpace: "pre-wrap" }}>
                              {previewError}
                            </Text>
                          </Alert>
                        ) : mismatch ? (
                          <Alert color="red" title="Card structure differs">
                            The editor and exporter found different card pairs.
                            Reload the deck before saving.
                          </Alert>
                        ) : preview && rendered ? (
                          <MathJaxContext
                            version={3}
                            src="/mathjax/tex-chtml.js"
                            config={{
                              startup: { typeset: false },
                              tex: {
                                macros: preview.macros,
                                inlineMath: [
                                  ["$", "$"],
                                  ["\\(", "\\)"],
                                ],
                                displayMath: [
                                  ["$$", "$$"],
                                  ["\\[", "\\]"],
                                ],
                                processEscapes: true,
                                packages: { "[+]": ["ams", "color"] },
                              },
                              loader: { load: ["[tex]/ams", "[tex]/color"] },
                            }}
                          >
                            <Card
                              withBorder
                              padding="lg"
                              radius="md"
                              className={"card-preview " + side.toLowerCase()}
                              role="button"
                              tabIndex={0}
                              aria-label="Flip card"
                              onClick={() =>
                                setSide(side === "Front" ? "Back" : "Front")
                              }
                              onKeyDown={(event) => {
                                if (
                                  event.key === "Enter" ||
                                  event.key === " "
                                ) {
                                  event.preventDefault();
                                  setSide(side === "Front" ? "Back" : "Front");
                                }
                              }}
                            >
                              <Group justify="space-between" mb="md">
                                <Badge
                                  variant="light"
                                  color={side === "Front" ? "indigo" : "teal"}
                                >
                                  {side === "Front" ? "Question" : "Answer"}
                                </Badge>
                                <Text size="xs" c="dimmed">
                                  Click or press Space to flip
                                </Text>
                              </Group>
                              <MathJax dynamic hideUntilTypeset="every">
                                <div
                                  className="math-content"
                                  dangerouslySetInnerHTML={{
                                    __html: DOMPurify.sanitize(
                                      side === "Front"
                                        ? rendered.front
                                        : rendered.back,
                                    ),
                                  }}
                                />
                              </MathJax>
                            </Card>
                            <Group mt="sm" gap="xs">
                              {rendered.tags.map((tag) => (
                                <Badge key={tag} variant="outline" color="gray">
                                  {tag}
                                </Badge>
                              ))}
                            </Group>
                          </MathJaxContext>
                        ) : (
                          <Text c="dimmed">Select a card to preview.</Text>
                        )}
                      </Paper>
                      {log && (
                        <Paper withBorder p="md">
                          <Title order={3} size="h5">
                            Generation output
                          </Title>
                          <Divider my="sm" />
                          <Text
                            component="pre"
                            size="sm"
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "anywhere",
                            }}
                          >
                            {log}
                          </Text>
                        </Paper>
                      )}
                    </Stack>
                  </div>
                </Stack>
              )}
            </div>
          )}
        </Stack>
      </AppShell.Main>
    </AppShell>
  );
}
