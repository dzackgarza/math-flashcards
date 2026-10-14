import { useEffect, useMemo, useRef, useState, type MouseEvent } from "react";
import {
  ActionIcon,
  Alert,
  Box,
  Button,
  CloseButton,
  Group,
  Kbd,
  Loader,
  Popover,
  Stack,
  Text,
  TextInput,
  TagsInput,
  Title,
  Tooltip,
  Tree,
  UnstyledButton,
  useTree,
  type TreeNodeData,
} from "@mantine/core";
import { useDebouncedCallback, useHotkeys } from "@mantine/hooks";
import {
  Spotlight,
  spotlight,
  type SpotlightActionGroupData,
} from "@mantine/spotlight";
import {
  IconArrowBackUp,
  IconCards,
  IconChevronDown,
  IconChevronRight,
  IconFolder,
  IconFolderOpen,
  IconPlus,
  IconRefresh,
  IconSearch,
  IconTrash,
} from "@tabler/icons-react";
import { basename } from "pathe";
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
import { loadMathJax, previewHtml, type MathJaxRuntime } from "./math";
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

function treeData(decks: Summary[]): TreeNodeData[] {
  const roots: TreeNodeData[] = [];
  for (const deck of decks) {
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
  const [workspaceMenu, setWorkspaceMenu] = useState(false);
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
  const data = useMemo(() => treeData(decks), [decks]);
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
  // One status: unsaved source first, then the package.
  const status = dirty ? "Unsaved changes" : packageState;
  const tone =
    status === "Up to date"
      ? "synced"
      : status === "Failed"
        ? "failed"
        : status === "Generating"
          ? "working"
          : "pending";
  const blocked = busy || mismatch || !!parsed.error;
  const canSave = dirty && !blocked;
  const canGenerate = document !== null && !dirty && !blocked;
  const previews = useMemo(
    () =>
      mathjax
        ? ranges.map((range) => ({
            front: previewHtml(mathjax, range.front.value),
            back: previewHtml(mathjax, range.back.value.split(/\n\s*\n/)[0]),
          }))
        : null,
    [mathjax, ranges],
  );
  const statuses = useMemo(
    () => new Map(decks.map((deck) => [deck.path, deck.status])),
    [decks],
  );

  useHotkeys(
    [
      [
        "mod+S",
        () => {
          if (canSave) void save();
        },
      ],
    ],
    [],
    true,
  );

  function openWorkspace() {
    if (workspaceForm.validate().hasErrors) return;
    setWorkspaceMenu(false);
    confirmNavigation(() => {
      void chooseWorkspace(workspaceForm.getValues().workspace);
    });
  }

  function refreshWorkspace() {
    refresh().catch((failure) => setError(String(failure)));
  }

  const commands: SpotlightActionGroupData[] = [
    {
      group: "Actions",
      actions: [
        ...(document
          ? [
              {
                id: "add-card",
                label: "Add card",
                disabled: blocked,
                onClick: addCard,
              },
              {
                id: "save",
                label: "Save deck",
                disabled: !canSave,
                onClick: () => void save(),
              },
              {
                id: "generate",
                label: "Generate Anki deck",
                disabled: !canGenerate,
                onClick: () => void generate(),
              },
            ]
          : []),
        ...(workspace
          ? [
              {
                id: "new-deck",
                label: "New deck",
                disabled: busy,
                onClick: createDeck,
              },
              {
                id: "refresh",
                label: "Refresh workspace",
                disabled: busy,
                onClick: refreshWorkspace,
              },
            ]
          : []),
      ],
    },
    {
      group: "Decks",
      actions: decks.map((deck) => ({
        id: "deck:" + deck.path,
        label: deckName(deck.path),
        description: deck.path.split("/").slice(0, -1).join(" / "),
        onClick: () =>
          confirmNavigation(() => {
            void chooseDeck(deck.path);
          }),
      })),
    },
    {
      group: "Cards",
      actions: document
        ? ranges.map((range, cardIndex) => ({
            id: "card:" + range.id,
            label: range.label,
            onClick: () => {
              setSelection([range.id]);
              selectCard(cardIndex, document.source);
            },
          }))
        : [],
    },
  ];

  return (
    <div className="app">
      <aside className="sidebar">
        <Group justify="space-between" wrap="nowrap" className="sidebar-head">
          <Title order={1} className="app-title">
            Math Flashcards
          </Title>
          {busy && <Loader size={14} aria-label={task} />}
        </Group>
        <Popover
          opened={workspaceMenu}
          onChange={setWorkspaceMenu}
          width={440}
          position="bottom-start"
          shadow="lg"
        >
          <Popover.Target>
            <UnstyledButton
              className="workspace-button"
              aria-label="Workspace"
              onClick={() => setWorkspaceMenu((value) => !value)}
            >
              <IconFolder size={16} stroke={1.75} />
              <span className="workspace-name">
                {workspace ? basename(workspace) : "Choose a workspace"}
              </span>
              <IconChevronDown size={14} />
            </UnstyledButton>
          </Popover.Target>
          <Popover.Dropdown>
            <Stack gap="sm">
              <TextInput
                label="Workspace folder"
                placeholder="Folder containing decks/"
                key={workspaceForm.key("workspace")}
                {...workspaceForm.getInputProps("workspace")}
                onKeyDown={(event) => {
                  if (event.key === "Enter") openWorkspace();
                }}
              />
              <Group gap="xs" justify="flex-end">
                {isTauri() && (
                  <Button
                    variant="default"
                    leftSection={<IconFolderOpen size={16} />}
                    onClick={async () => {
                      const selectedFolder = await open({
                        directory: true,
                        multiple: false,
                        title: "Choose the deck workspace",
                      });
                      if (!selectedFolder) return;
                      setWorkspaceMenu(false);
                      confirmNavigation(() => {
                        void chooseWorkspace(selectedFolder);
                      });
                    }}
                  >
                    Browse
                  </Button>
                )}
                <Button
                  variant="default"
                  disabled={!workspace || busy}
                  onClick={refreshWorkspace}
                >
                  Refresh workspace
                </Button>
                <Button disabled={busy} onClick={openWorkspace}>
                  Open workspace
                </Button>
              </Group>
            </Stack>
          </Popover.Dropdown>
        </Popover>
        <UnstyledButton
          className="command-button"
          onClick={() => spotlight.open()}
        >
          <IconSearch size={15} stroke={1.75} />
          <span>Search</span>
          <Kbd size="xs">Ctrl K</Kbd>
        </UnstyledButton>
        <div ref={deckViewport} className="deck-scroll">
          <Tree
            data={data}
            tree={tree}
            levelOffset={14}
            renderNode={({ node, expanded, hasChildren, elementProps }) => (
              <TreeRow
                {...elementProps}
                path={node.value.slice(1)}
                folder={hasChildren}
                disabled={busy}
                expand={() => tree.expand(node.value)}
                data-active={
                  document?.path === node.value.slice(1) || undefined
                }
                onClick={(event) => {
                  elementProps.onClick?.(event);
                  if (!hasChildren && !busy)
                    confirmNavigation(() => {
                      void chooseDeck(node.value.slice(1));
                    });
                }}
              >
                {hasChildren ? (
                  <IconChevronRight
                    size={14}
                    className={"tree-chevron" + (expanded ? " open" : "")}
                  />
                ) : (
                  <IconCards size={15} stroke={1.75} className="tree-icon" />
                )}
                <span className="tree-label">{node.label}</span>
                {!hasChildren &&
                  statuses.get(node.value.slice(1)) === "Unsynced" && (
                    <span className="tree-dot" aria-hidden />
                  )}
              </TreeRow>
            )}
          />
          {workspace && decks.length === 0 && (
            <Text c="dimmed" size="sm" px="xs">
              This workspace has no Markdown decks.
            </Text>
          )}
        </div>
        <Button
          variant="subtle"
          color="gray"
          justify="flex-start"
          leftSection={<IconPlus size={16} />}
          disabled={!workspace || busy}
          onClick={createDeck}
        >
          New deck
        </Button>
      </aside>
      <div className="content">
        {error && (
          <Alert
            className="banner"
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
        {!document ? (
          <Stack className="empty-state" align="center" justify="center">
            <IconCards size={40} stroke={1.25} className="empty-icon" />
            <Title order={2} fz={20}>
              Your decks, in one place
            </Title>
            <Text c="dimmed" ta="center" maw={360}>
              {workspace
                ? "Select a deck in the sidebar to edit its cards."
                : "Choose the workspace folder that contains decks/."}
            </Text>
            {!workspace && (
              <Button onClick={() => setWorkspaceMenu(true)}>
                Choose workspace
              </Button>
            )}
          </Stack>
        ) : (
          <div className="panes">
            <section className="card-column">
              <header className="column-head">
                <Group justify="space-between" wrap="nowrap" align="start">
                  <Box miw={0}>
                    <Title order={2} fz={20} className="deck-title">
                      {deckName(document.path)}
                    </Title>
                    <Text size="sm" c="dimmed" truncate>
                      {[
                        ...document.path.split("/").slice(0, -1),
                        ranges.length === 1
                          ? "1 card"
                          : ranges.length + " cards",
                      ].join(" · ")}
                    </Text>
                  </Box>
                  <Tooltip label="Add card" openDelay={400}>
                    <ActionIcon
                      variant="subtle"
                      size="lg"
                      aria-label="Add card"
                      onClick={addCard}
                      disabled={blocked}
                    >
                      <IconPlus size={18} />
                    </ActionIcon>
                  </Tooltip>
                </Group>
                <TextInput
                  mt="sm"
                  variant="filled"
                  aria-label="Find a card"
                  placeholder="Find a card"
                  leftSection={<IconSearch size={15} />}
                  value={cardFilter}
                  onChange={(event) => setCardFilter(event.currentTarget.value)}
                />
              </header>
              <div ref={cardViewport} className="card-scroll">
                {ranges.map(
                  (range, cardIndex) =>
                    (range.label + "\n" + range.back.value)
                      .toLowerCase()
                      .includes(cardFilter.toLowerCase()) && (
                      <CardRow
                        key={range.id}
                        id={range.id}
                        path={document.path}
                        label={range.label}
                        preview={previews?.[cardIndex] ?? null}
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
              </div>
              <Text className="column-foot" size="sm" c="dimmed">
                {dirty
                  ? "Save the deck to move its cards."
                  : "Drag cards to reorder them, or onto a deck to move them. Ctrl-click or Shift-click selects several."}
              </Text>
            </section>
            <main className="editor-column">
              <header className="toolbar">
                <Group
                  gap={8}
                  wrap="nowrap"
                  className="status"
                  title={document.package}
                >
                  <span className={"status-dot " + tone} aria-hidden />
                  <Text size="sm" fw={500}>
                    {status}
                  </Text>
                </Group>
                <Group gap="xs" wrap="nowrap">
                  <Button
                    variant="subtle"
                    color="gray"
                    leftSection={<IconRefresh size={16} />}
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
                    variant="default"
                    onClick={save}
                    disabled={!canSave}
                    loading={task === "Saving"}
                  >
                    Save deck
                  </Button>
                  <Button
                    onClick={generate}
                    disabled={!canGenerate}
                    loading={task === "Generating"}
                  >
                    Generate Anki deck
                  </Button>
                </Group>
              </header>
              <div className="editor-scroll">
                <div className="card-stage">
                  {parsed.error && (
                    <Alert color="red" title="Invalid card">
                      {parsed.error}
                    </Alert>
                  )}
                  {mismatch && (
                    <Alert color="red" title="Card structure differs">
                      The editor and exporter found different card pairs. Reload
                      the deck before saving.
                    </Alert>
                  )}
                  {draft ? (
                    <>
                      <Group justify="space-between">
                        <Text size="sm" c="dimmed">
                          Card {index + 1} of {ranges.length}
                        </Text>
                        <Button
                          color="red"
                          variant="subtle"
                          size="compact-sm"
                          leftSection={<IconTrash size={14} />}
                          onClick={deleteCard}
                          disabled={!selected || blocked}
                        >
                          Delete card
                        </Button>
                      </Group>
                      <div className="side-editors">
                        {(["front", "back"] as const).map((side) => (
                          <SideEditor
                            key={
                              document.path + ":" + draft.card.id + ":" + side
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
                        placeholder="Add a tag"
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
                    </>
                  ) : (
                    <Text c="dimmed" ta="center" py="xl">
                      Add a card to begin.
                    </Text>
                  )}
                  {log && (
                    <details className="generation-log">
                      <summary>Generation output</summary>
                      <pre>{log}</pre>
                    </details>
                  )}
                </div>
              </div>
            </main>
          </div>
        )}
      </div>
      {notice && (
        <div className="snackbar">
          <Text size="sm" role="status">
            {notice.label}
          </Text>
          {notice.undo && (
            <Button
              variant="subtle"
              color="indigo.2"
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
          <CloseButton
            size="sm"
            variant="transparent"
            aria-label="Dismiss"
            className="snackbar-close"
            onClick={() => setNotice(null)}
          />
        </div>
      )}
      <Spotlight
        actions={commands}
        limit={40}
        highlightQuery
        nothingFound="Nothing found"
        shortcut="mod + K"
        tagsToIgnore={[]}
        triggerOnContentEditable
        searchProps={{
          leftSection: <IconSearch size={18} />,
          placeholder: "Search decks, cards, and commands",
        }}
      />
    </div>
  );
}
