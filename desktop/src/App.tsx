import { useEffect, useMemo, useRef, useState, type MouseEvent } from "react";
import {
  Alert,
  AppShell,
  Badge,
  Box,
  Button,
  Divider,
  Group,
  Loader,
  Paper,
  Stack,
  Text,
  TextInput,
  TagsInput,
  Title,
  Tree,
  useTree,
  type TreeNodeData,
} from "@mantine/core";
import { useDebouncedCallback } from "@mantine/hooks";
import { IconArrowBackUp, IconPlus } from "@tabler/icons-react";
import {
  monitorForElements,
  type ElementEventPayloadMap,
} from "@atlaskit/pragmatic-drag-and-drop/element/adapter";
import { combine } from "@atlaskit/pragmatic-drag-and-drop/combine";
import { extractClosestEdge } from "@atlaskit/pragmatic-drag-and-drop-hitbox/closest-edge/extract-closest-edge";
import {
  autoScrollForElements,
  autoScrollWindowForElements,
} from "@atlaskit/pragmatic-drag-and-drop-auto-scroll/element";
import { announce } from "@atlaskit/pragmatic-drag-and-drop-live-region";
import { modals } from "@mantine/modals";
import { useForm } from "@mantine/form";
import { isTauri } from "@tauri-apps/api/core";
import { getCurrentWindow } from "@tauri-apps/api/window";
import { appConfigDir, join } from "@tauri-apps/api/path";
import { open } from "@tauri-apps/plugin-dialog";
import { load } from "@tauri-apps/plugin-store";
import { watch } from "@tauri-apps/plugin-fs";
import {
  cards,
  replaceField,
  replaceTags,
  removeCard,
  newCard,
  reorderCards,
  transferCards,
  type CardRange,
} from "./cards";
import { type Side, SideEditor } from "./editor";
import { loadMathJax, type MathJaxRuntime } from "./math";
import {
  CardRow,
  NewDeckForm,
  TreeRow,
  deckName,
  dragSchema,
  targetSchema,
} from "./organize";
import {
  request,
  workspaceSchema,
  documentSchema,
  generatedSchema,
  organizedSchema,
  type Change,
  type Document,
  type Summary,
} from "./bridge";

type Task = "Idle" | "Loading" | "Saving" | "Generating" | "Organizing";
type Notice = { label: string; undo: Change[] | null };

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
  const [mathjax, setMathjax] = useState<MathJaxRuntime | null>(null);
  const [index, setIndex] = useState(0);
  const [draft, setDraft] = useState<{
    source: string;
    card: CardRange;
    front: string;
    back: string;
  } | null>(null);
  const [task, setTask] = useState<Task>("Idle");
  const [buildResult, setBuildResult] = useState<"Ready" | "Failed">("Ready");
  const [error, setError] = useState("");
  const [log, setLog] = useState("");
  const [filter, setFilter] = useState("");
  const [cardFilter, setCardFilter] = useState("");
  const [selection, setSelection] = useState<string[]>([]);
  const [notice, setNotice] = useState<Notice | null>(null);
  const navigation = useRef(0);
  const anchor = useRef<string | null>(null);
  const deckViewport = useRef<HTMLDivElement>(null);
  const cardViewport = useRef<HTMLDivElement>(null);
  const tree = useTree();
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
  const data = useMemo(() => treeData(decks, filter), [decks, filter]);
  // Pandoc counts the saved deck's cards; the editor parser must agree.
  const mismatch = useMemo(
    () => document !== null && document.cards !== cards(document.saved).length,
    [document?.cards, document?.saved],
  );

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
      setSelection([]);
      setNotice(null);
      setDraft(null);
      setLog("");
      loadMathJax(result.macros).then(setMathjax, (failure) =>
        setError(String(failure)),
      );
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
      setSelection([]);
      const folders = path.split("/").slice(0, -1);
      folders.forEach((_, depth) =>
        tree.expand("/" + folders.slice(0, depth + 1).join("/")),
      );
      selectCard(
        Math.max(
          0,
          cards(result.source).findIndex((card) => card.id === cardId),
        ),
        result.source,
      );
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
  }

  function selectCard(cardIndex: number, source: string) {
    setIndex(cardIndex);
    const card = cards(source)[cardIndex];
    setDraft(
      card
        ? { source, card, front: card.front.value, back: card.back.value }
        : null,
    );
  }

  function editCard(field: Side, value: string) {
    if (!document || !draft) return;
    const next = { ...draft, [field]: value };
    let source = draft.source;
    const sides: Side[] = ["front", "back"];
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
              cards: result.cards,
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

  // The open deck supplies the hash it was loaded with, so a disk edit after
  // loading rejects the change, as it does for a save.
  async function loadDeck(path: string) {
    if (document?.path === path) return document;
    return request({ action: "load", workspace, path }, documentSchema);
  }

  // Changes publish immediately; the open deck reloads, or follows `focus`.
  // Without `originals` the change has no Undo.
  async function organize(
    changes: Change[],
    originals: Record<string, string | null> | null,
    label: string,
    focus?: string,
  ) {
    const open = document?.path;
    const touched = changes.some((change) => change.path === open);
    if (dirty && touched)
      throw new Error("Save or reload " + deckName(open!) + " first.");
    setTask("Organizing");
    setError("");
    const result = await request(
      { action: "organize", workspace, changes },
      organizedSchema,
    ).finally(() => setTask("Idle"));
    await refresh();
    const removed = changes
      .filter((change) => change.source === null)
      .map((change) => change.path);
    const next = focus ?? (touched ? open : undefined);
    if (next && !removed.includes(next)) await chooseDeck(next, selected?.id);
    else if (touched) {
      navigation.current++;
      setDocument(null);
      setDraft(null);
      setSelection([]);
    }
    setNotice({
      label,
      undo:
        originals &&
        result.changed.map((deck) => ({
          path: deck.path,
          source: originals[deck.path],
          expected: deck.hash,
        })),
    });
    announce(label);
  }

  async function moveCards(
    path: string,
    ids: string[],
    target: string,
    before?: string,
  ) {
    const origin = await loadDeck(path);
    if (path === target) {
      const order = cards(origin.source).map((card) => card.id);
      const remaining = order.filter((id) => !ids.includes(id));
      remaining.splice(
        before ? remaining.indexOf(before) : remaining.length,
        0,
        ...order.filter((id) => ids.includes(id)),
      );
      await organize(
        [
          {
            path,
            source: reorderCards(origin.source, remaining),
            expected: origin.hash,
          },
        ],
        { [path]: origin.source },
        "Card order saved.",
      );
      return;
    }
    const receiver = await loadDeck(target);
    const result = transferCards(origin.source, receiver.source, ids, before, {
      source: path,
      destination: target,
    });
    await organize(
      [
        { path: target, source: result.destination, expected: receiver.hash },
        { path, source: result.source, expected: origin.hash },
      ],
      { [path]: origin.source, [target]: receiver.source },
      (ids.length === 1 ? "Card" : ids.length + " cards") +
        " moved to " +
        deckName(target) +
        ".",
    );
  }

  async function mergeDecks(path: string, target: string) {
    const origin = await loadDeck(path);
    const receiver = await loadDeck(target);
    const ids = cards(origin.source).map((card) => card.id);
    await organize(
      [
        {
          path: target,
          source: ids.length
            ? transferCards(origin.source, receiver.source, ids, undefined, {
                source: path,
                destination: target,
              }).destination
            : receiver.source,
          expected: receiver.hash,
        },
        { path, source: null, expected: origin.hash },
      ],
      { [path]: origin.source, [target]: receiver.source },
      deckName(path) + " merged into " + deckName(target) + ".",
      document?.path === path ? target : undefined,
    );
  }

  function createDeck() {
    const folder = document?.path.split("/").slice(0, -1).join("/") ?? "";
    const id = modals.open({
      title: "New deck",
      children: (
        <NewDeckForm
          folder={folder}
          submit={(path) => {
            modals.close(id);
            const source =
              "---\ntitle: " +
              JSON.stringify(path.replace(/\.md$/, "").replace(/\//g, "::")) +
              "\n---\n\n";
            confirmNavigation(() => {
              organize(
                [{ path, source, expected: null }],
                { [path]: null },
                deckName(path) + " created.",
                path,
              ).catch((failure) => setError(String(failure)));
            });
          }}
        />
      ),
    });
  }

  function chooseRow(id: string, event: MouseEvent) {
    if (!document) return;
    if (event.shiftKey && anchor.current) {
      const order = ranges.map((card) => card.id);
      const [a, b] = [order.indexOf(anchor.current), order.indexOf(id)].sort(
        (x, y) => x - y,
      );
      setSelection([...new Set([...selection, ...order.slice(a, b + 1)])]);
      return;
    }
    anchor.current = id;
    if (event.ctrlKey || event.metaKey) {
      setSelection(
        selection.includes(id)
          ? selection.filter((value) => value !== id)
          : [...selection, id],
      );
      return;
    }
    setSelection([id]);
    selectCard(
      ranges.findIndex((card) => card.id === id),
      document.source,
    );
  }

  async function drop(event: ElementEventPayloadMap["onDrop"]) {
    const location = event.location.current.dropTargets[0];
    if (!location) return;
    const data = dragSchema.parse(event.source.data);
    const target = targetSchema.parse(location.data);
    if (target.kind === "folder") return;
    if (data.kind === "deck") {
      if (target.kind !== "deck") return;
      modals.openConfirmModal({
        title: "Merge decks",
        children: (
          <Text>
            Move every card from {deckName(data.path)} into{" "}
            {deckName(target.path)}, then send {deckName(data.path)} to the
            trash?
          </Text>
        ),
        labels: { confirm: "Merge decks", cancel: "Cancel" },
        onConfirm: () => {
          mergeDecks(data.path, target.path).catch((failure) =>
            setError(String(failure)),
          );
        },
      });
      return;
    }
    if (target.kind === "deck") {
      await moveCards(data.path, data.ids, target.path);
      return;
    }
    const order = ranges
      .map((card) => card.id)
      .filter((id) => !data.ids.includes(id));
    const before =
      extractClosestEdge(location.data) === "bottom"
        ? order[order.indexOf(target.card) + 1]
        : target.card;
    await moveCards(data.path, data.ids, target.path, before);
  }

  const dropHandler = useRef(drop);
  useEffect(() => {
    dropHandler.current = drop;
  });
  useEffect(
    () =>
      combine(
        monitorForElements({
          onDrop: (event) => {
            dropHandler
              .current(event)
              .catch((failure) => setError(String(failure)));
          },
        }),
        autoScrollWindowForElements(),
        ...[deckViewport.current, cardViewport.current]
          .filter((element) => element !== null)
          .map((element) => autoScrollForElements({ element })),
      ),
    [document !== null],
  );

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
          {notice && (
            <Alert color="teal" withCloseButton onClose={() => setNotice(null)}>
              <Group justify="space-between">
                <Text size="sm" role="status">
                  {notice.label}
                </Text>
                {notice.undo && (
                  <Button
                    variant="subtle"
                    size="compact-sm"
                    leftSection={<IconArrowBackUp size={16} />}
                    disabled={busy}
                    onClick={() =>
                      organize(notice.undo!, null, "Undo complete.").catch(
                        (failure) => setError(String(failure)),
                      )
                    }
                  >
                    Undo
                  </Button>
                )}
              </Group>
            </Alert>
          )}
          <div className="workbench">
            <Paper withBorder p="md" className="deck-panel">
              <Stack gap="sm">
                <Group justify="space-between">
                  <Title order={2} size="h5">
                    Decks
                  </Title>
                  <Button
                    size="compact-sm"
                    variant="light"
                    leftSection={<IconPlus size={14} />}
                    disabled={!workspace || busy}
                    onClick={createDeck}
                  >
                    New deck
                  </Button>
                </Group>
                <TextInput
                  aria-label="Find a deck"
                  placeholder="Find a deck…"
                  value={filter}
                  onChange={(event) => setFilter(event.currentTarget.value)}
                />
                <div ref={deckViewport} className="deck-scroll">
                  <Tree
                    data={data}
                    tree={tree}
                    renderNode={({
                      node,
                      expanded,
                      hasChildren,
                      elementProps,
                    }) => (
                      <TreeRow
                        {...elementProps}
                        path={node.value.slice(1)}
                        folder={hasChildren}
                        disabled={busy}
                        expand={() => tree.expand(node.value)}
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
                      </TreeRow>
                    )}
                  />
                  {workspace && decks.length === 0 && (
                    <Text c="dimmed" size="sm">
                      This workspace has no Markdown decks.
                    </Text>
                  )}
                </div>
              </Stack>
            </Paper>
            {!document ? (
              <Paper withBorder p="xl">
                <Stack align="center" justify="center" h={420}>
                  <Title order={2}>Your decks, in one place</Title>
                  <Text c="dimmed" ta="center">
                    Open a workspace, then select a deck to edit and review its
                    cards.
                  </Text>
                </Stack>
              </Paper>
            ) : (
              <Stack gap="md" className="document-panel">
                <Paper withBorder p="md">
                  <Group justify="space-between" align="start">
                    <Box>
                      <Title order={2} size="h4">
                        {document.path.replace(/\.md$/, "")}
                      </Title>
                      <Text size="sm" c="dimmed">
                        {document.path}
                      </Text>
                    </Box>
                    <Group gap="xs">
                      <Badge color={dirty ? "orange" : "gray"} variant="light">
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
                      <div ref={cardViewport} className="card-scroll">
                        <Stack gap={4}>
                          {ranges.map(
                            (range, cardIndex) =>
                              range.label
                                .toLowerCase()
                                .includes(cardFilter.toLowerCase()) && (
                                <CardRow
                                  key={range.id}
                                  id={range.id}
                                  path={document.path}
                                  label={range.label}
                                  active={index === cardIndex}
                                  selected={selection.includes(range.id)}
                                  group={ranges
                                    .map((card) => card.id)
                                    .filter((id) => selection.includes(id))}
                                  disabled={busy || dirty || !!parsed.error}
                                  choose={(event) => chooseRow(range.id, event)}
                                />
                              ),
                          )}
                        </Stack>
                      </div>
                      <Text size="xs" c="dimmed">
                        {dirty
                          ? "Save the deck to move its cards."
                          : "Drag cards to reorder them, or onto a deck to move them. Ctrl-click or Shift-click selects several."}
                      </Text>
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
                          <div className="side-editors">
                            {(["front", "back"] as const).map((side) => (
                              <SideEditor
                                key={
                                  document.path +
                                  ":" +
                                  draft.card.id +
                                  ":" +
                                  side
                                }
                                side={side}
                                value={draft[side]}
                                mathjax={mathjax}
                                editable={!busy}
                                onChange={(value) => editCard(side, value)}
                              />
                            ))}
                          </div>
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
                      {mismatch && (
                        <Alert color="red" title="Card structure differs">
                          The editor and exporter found different card pairs.
                          Reload the deck before saving.
                        </Alert>
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
        </Stack>
      </AppShell.Main>
    </AppShell>
  );
}
