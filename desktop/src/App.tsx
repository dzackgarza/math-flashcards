import { useEffect, useMemo, useRef, useState, type MouseEvent } from "react";
import {
  ActionIcon,
  Alert,
  Badge,
  Box,
  Button,
  CloseButton,
  Group,
  Kbd,
  Loader,
  Menu,
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
  IconListDetails,
  IconMenu2,
  IconPencil,
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
import {
  cardChanges,
  cards,
  replaceField,
  replaceTags,
  removeCard,
  newCard,
  reorderCards,
  transferCards,
  type CardChange,
  type CardRange,
} from "./cards";
import { type Side, SideEditor } from "./editor";
import { loadMathJax, previewHtml, type MathJaxRuntime } from "./math";
import {
  CardRow,
  DeckNameForm,
  NewDeckForm,
  TreeRow,
  deckName,
  dragSchema,
  targetSchema,
} from "./organize";
import { ReviewChanges } from "./review";
import {
  request,
  watchWorkspace,
  workspaceSchema,
  documentSchema,
  generatedSchema,
  organizedSchema,
  reviewSchema,
  type Change,
  type Document,
  type Pending,
  type Summary,
} from "./bridge";

type Task = "Idle" | "Loading" | "Generating" | "Organizing";
type Notice = { label: string; undo: Change[] | null };
// `scope` is one deck path, or null for every deck.
type Review = { scope: string | null; decks: Pending[] | null };

const STALE = /changed on disk|changed during|changed before/;

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

// The Anki deck name a new deck receives from its path.
const deckTitle = (path: string) =>
  JSON.stringify(path.replace(/\.md$/, "").replace(/\//g, "::"));

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
  const [progress, setProgress] = useState("");
  const [buildResult, setBuildResult] = useState<"Ready" | "Failed">("Ready");
  const [error, setError] = useState("");
  const [conflict, setConflict] = useState(false);
  const [log, setLog] = useState("");
  const [workspaceMenu, setWorkspaceMenu] = useState(false);
  const [cardFilter, setCardFilter] = useState("");
  const [selection, setSelection] = useState<string[]>([]);
  const [notice, setNotice] = useState<Notice | null>(null);
  const [review, setReview] = useState<Review | null>(null);
  // The latest document for asynchronous saves and disk events.
  const current = useRef<Document | null>(null);
  const saving = useRef<Promise<void>>(Promise.resolve());
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
  const changes = useMemo<CardChange[]>(() => {
    if (!document || parsed.error) return [];
    try {
      return cardChanges(document.built, document.source);
    } catch {
      return [];
    }
  }, [document?.built, document?.source, parsed.error]);
  const changed = useMemo(
    () => new Map(changes.map((change) => [change.id, change.kind])),
    [changes],
  );

  function updateDocument(
    next: (document: Document | null) => Document | null,
  ) {
    current.current = next(current.current);
    setDocument(current.current);
  }

  async function refresh(root = workspace) {
    if (!root) return;
    const result = await request(
      { action: "list", workspace: root },
      workspaceSchema,
    );
    setDecks(result.decks);
    updateDocument((open) => {
      if (!open) return open;
      const summary = result.decks.find((item) => item.path === open.path);
      return summary
        ? { ...open, status: summary.status, reasons: summary.reasons }
        : open;
    });
  }

  const refreshOnChange = useDebouncedCallback(() => {
    refresh().catch((failure) => setError(String(failure)));
  }, 500);

  // Saves queue behind each other, so each one sends the hash the previous
  // save returned. A deck with invalid card structure stays unsaved.
  function persist(): Promise<void> {
    saving.current = saving.current.then(async () => {
      const open = current.current;
      if (!open || open.source === open.saved) return;
      try {
        cards(open.source);
      } catch {
        return;
      }
      try {
        const result = await request(
          {
            action: "save",
            workspace,
            path: open.path,
            source: open.source,
            expected: open.hash,
          },
          documentSchema,
        );
        updateDocument((document) =>
          document?.path === open.path
            ? {
                ...document,
                saved: open.source,
                hash: result.hash,
                cards: result.cards,
                status: result.status,
                reasons: result.reasons,
                built: result.built,
              }
            : document,
        );
        setConflict(false);
      } catch (failure) {
        if (STALE.test(String(failure))) setConflict(true);
        else setError(String(failure));
      }
    });
    return saving.current;
  }

  const autosave = useDebouncedCallback(() => void persist(), 600);

  // Every operation that reads the deck from disk first writes pending edits.
  async function flush() {
    autosave.cancel();
    await persist();
    const open = current.current;
    if (open && open.source !== open.saved)
      throw new Error(
        "The open deck has edits that are not saved. Resolve them first.",
      );
  }

  function guard(action: () => void | Promise<void>) {
    flush()
      .then(action)
      .catch((failure) => setError(String(failure)));
  }

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
      updateDocument(() => null);
      setSelection([]);
      setNotice(null);
      setDraft(null);
      setLog("");
      setConflict(false);
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

  function showDocument(
    path: string,
    result: Omit<Document, "path" | "saved">,
    cardId?: string,
  ) {
    cards(result.source);
    updateDocument(() => ({ ...result, path, saved: result.source }));
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
    setConflict(false);
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
      showDocument(path, result, cardId);
      setSelection([]);
      setLog("");
      setBuildResult("Ready");
      setCardFilter("");
    } catch (failure) {
      setError(String(failure));
    } finally {
      if (token === navigation.current) setTask("Idle");
    }
  }

  // The open deck follows its file. Pending edits keep priority; their save
  // reports the conflict.
  async function followDisk() {
    await saving.current;
    const open = current.current;
    if (!open || open.source !== open.saved) return;
    const token = navigation.current;
    const result = await request(
      { action: "load", workspace, path: open.path },
      documentSchema,
    );
    const latest = current.current;
    if (
      token !== navigation.current ||
      latest?.path !== open.path ||
      latest.source !== latest.saved
    )
      return;
    if (result.hash === latest.hash) {
      updateDocument(
        (document) =>
          document && {
            ...document,
            status: result.status,
            reasons: result.reasons,
            built: result.built,
          },
      );
      return;
    }
    showDocument(open.path, result, ranges[index]?.id);
  }

  const followOnChange = useDebouncedCallback(() => {
    followDisk().catch((failure) => {
      // A deck removed outside the app closes.
      if (/No such file|does not exist/.test(String(failure))) {
        updateDocument(() => null);
        setDraft(null);
        return;
      }
      setError(String(failure));
    });
  }, 300);

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
      if (dirty) {
        void persist();
        event.preventDefault();
      }
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
        guard(() =>
          window.destroy().catch((failure) => setError(String(failure))),
        );
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
    if (!workspace) return;
    let disposed = false;
    let stop: (() => void) | undefined;
    watchWorkspace(workspace, (paths) => {
      const relevant = paths
        .map((path) => path.replace(/\\/g, "/"))
        .filter(
          (path) =>
            !/(?:^|\/)(?:\.git|node_modules|src-tauri|test-artifacts)(?:\/|$)/.test(
              path,
            ) && !path.includes(".flashcards-"),
        );
      if (!relevant.length) return;
      refreshOnChange();
      const open = current.current;
      if (open && relevant.includes(workspace + "/decks/" + open.path))
        followOnChange();
    })
      .then((unwatch) => {
        if (disposed) unwatch();
        else stop = unwatch;
      })
      .catch((failure) => setError(String(failure)));
    return () => {
      disposed = true;
      stop?.();
    };
  }, [workspace, refreshOnChange, followOnChange]);

  function edit(source: string) {
    if (!document || document.source === source) return;
    updateDocument((open) => (open ? { ...open, source } : open));
    autosave();
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

  // The disk version replaces the edits that could not be saved.
  function useDiskVersion() {
    const open = current.current;
    if (!open) return;
    updateDocument(
      (document) => document && { ...document, source: document.saved },
    );
    setConflict(false);
    void chooseDeck(open.path, selected?.id);
  }

  // The edits replace the disk version.
  async function keepMyVersion() {
    const open = current.current;
    if (!open) return;
    const disk = await request(
      { action: "load", workspace, path: open.path },
      documentSchema,
    );
    updateDocument((document) => document && { ...document, hash: disk.hash });
    await persist();
  }

  async function generate(paths: string[]) {
    await flush();
    setTask("Generating");
    setBuildResult("Ready");
    setError("");
    const logs: string[] = [];
    const failures: string[] = [];
    for (const [position, path] of paths.entries()) {
      setProgress(
        paths.length === 1
          ? "Updating the Anki package…"
          : `Updating Anki package ${position + 1} of ${paths.length}…`,
      );
      try {
        const result = await request(
          { action: "generate", workspace, path },
          generatedSchema,
        );
        logs.push(deckName(path) + "\n" + result.log);
      } catch (failure) {
        failures.push(deckName(path) + ": " + String(failure));
        if (path === current.current?.path) setBuildResult("Failed");
      }
    }
    setLog([...logs, ...failures].join("\n\n"));
    if (failures.length) setError(failures.join("\n\n"));
    setProgress("");
    setTask("Idle");
    await refresh();
    await followDisk();
  }

  async function openReview(scope: string | null) {
    setReview({ scope, decks: null });
    try {
      await flush();
      const result = await request(
        { action: "review", workspace },
        reviewSchema,
      );
      setReview((open) =>
        open && open.scope === scope
          ? {
              scope,
              decks: result.decks.filter(
                (deck) => scope === null || deck.path === scope,
              ),
            }
          : open,
      );
    } catch (failure) {
      setReview(null);
      setError(String(failure));
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
    const open = current.current;
    if (open?.path === path) return open;
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
    const open = current.current?.path;
    const touched = changes.some((change) => change.path === open);
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
      updateDocument(() => null);
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
    await flush();
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
    await flush();
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
      current.current?.path === path ? target : undefined,
    );
  }

  function createDeck(folder?: string) {
    const id = modals.open({
      title: "New deck",
      children: (
        <NewDeckForm
          folder={
            folder ?? document?.path.split("/").slice(0, -1).join("/") ?? ""
          }
          submit={(path) => {
            modals.close(id);
            guard(() =>
              organize(
                [
                  {
                    path,
                    source: "---\ntitle: " + deckTitle(path) + "\n---\n\n",
                    expected: null,
                  },
                ],
                { [path]: null },
                deckName(path) + " created.",
                path,
              ),
            );
          }}
        />
      ),
    });
  }

  function renameDeck(path: string) {
    const id = modals.open({
      title: "Rename deck",
      children: (
        <DeckNameForm
          name={deckName(path)}
          taken={(name) =>
            decks.some(
              (deck) =>
                deck.path ===
                [...path.split("/").slice(0, -1), name + ".md"].join("/"),
            )
          }
          submit={(name) => {
            modals.close(id);
            const next = [...path.split("/").slice(0, -1), name + ".md"].join(
              "/",
            );
            if (next === path) return;
            guard(async () => {
              const origin = await loadDeck(path);
              // A title derived from the old path follows the new path.
              const header =
                /^---\n[\s\S]*?\n---\n/.exec(origin.source)?.[0] ?? "";
              const source =
                header.replace(
                  "title: " + deckTitle(path) + "\n",
                  "title: " + deckTitle(next) + "\n",
                ) + origin.source.slice(header.length);
              await organize(
                [
                  { path: next, source, expected: null },
                  { path, source: null, expected: origin.hash },
                ],
                { [path]: origin.source, [next]: null },
                deckName(path) + " renamed to " + name + ".",
                current.current?.path === path ? next : undefined,
              );
            });
          }}
        />
      ),
    });
  }

  function deleteDeck(path: string) {
    modals.openConfirmModal({
      title: "Delete deck",
      children: (
        <Text>Send {deckName(path)} and its Anki package to the trash?</Text>
      ),
      labels: { confirm: "Delete deck", cancel: "Cancel" },
      confirmProps: { color: "red" },
      onConfirm: () =>
        guard(async () => {
          const origin = await loadDeck(path);
          await organize(
            [{ path, source: null, expected: origin.hash }],
            { [path]: origin.source },
            deckName(path) + " sent to the trash.",
          );
        }),
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

  const pendingDecks = decks.filter((deck) => deck.status === "Unsynced");
  // One status: the editor's save state first, then the package.
  const status =
    task === "Generating"
      ? progress
      : buildResult === "Failed"
        ? "Generation failed"
        : parsed.error
          ? "Not saved: the card structure is invalid"
          : conflict
            ? "Not saved: the deck changed on disk"
            : dirty
              ? "Saving…"
              : document?.status === "Up to date"
                ? "Anki package up to date"
                : document?.status === "Empty"
                  ? "No cards to export"
                  : changes.length
                    ? changes.length +
                      (changes.length === 1 ? " change" : " changes") +
                      " not in the Anki package"
                    : (document?.reasons[0] ?? "");
  const tone =
    buildResult === "Failed" || parsed.error || conflict
      ? "failed"
      : task === "Generating" || dirty
        ? "working"
        : document?.status === "Up to date"
          ? "synced"
          : document?.status === "Empty"
            ? "empty"
            : "pending";
  const blocked = busy || mismatch || !!parsed.error;
  const canGenerate =
    document !== null &&
    document.status === "Unsynced" &&
    !dirty &&
    !blocked &&
    !conflict;
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

  useHotkeys([["mod+S", () => guard(() => {})]], [], true);

  function openWorkspace() {
    if (workspaceForm.validate().hasErrors) return;
    setWorkspaceMenu(false);
    guard(() => chooseWorkspace(workspaceForm.getValues().workspace));
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
                id: "generate",
                label: "Update this Anki package",
                disabled: !canGenerate,
                onClick: () => guard(() => generate([document.path])),
              },
            ]
          : []),
        ...(workspace
          ? [
              {
                id: "review",
                label: "Review changes not in Anki packages",
                onClick: () => void openReview(null),
              },
              {
                id: "generate-all",
                label: "Update all Anki packages",
                disabled: busy || pendingDecks.length === 0,
                onClick: () =>
                  guard(() => generate(pendingDecks.map((deck) => deck.path))),
              },
              {
                id: "new-deck",
                label: "New deck",
                disabled: busy,
                onClick: () => createDeck(),
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
        onClick: () => guard(() => chooseDeck(deck.path)),
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

  function deckMenuItems(path: string) {
    const unsynced = statuses.get(path) === "Unsynced";
    return (
      <>
        <Menu.Item
          leftSection={<IconRefresh size={16} />}
          disabled={!unsynced || busy}
          onClick={() => guard(() => generate([path]))}
        >
          Update Anki package
        </Menu.Item>
        <Menu.Item
          leftSection={<IconListDetails size={16} />}
          disabled={!unsynced}
          onClick={() => void openReview(path)}
        >
          Review changes
        </Menu.Item>
        <Menu.Divider />
        <Menu.Item
          leftSection={<IconPencil size={16} />}
          disabled={busy}
          onClick={() => renameDeck(path)}
        >
          Rename deck…
        </Menu.Item>
        <Menu.Item
          color="red"
          leftSection={<IconTrash size={16} />}
          disabled={busy}
          onClick={() => deleteDeck(path)}
        >
          Delete deck…
        </Menu.Item>
      </>
    );
  }

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
                      guard(() => chooseWorkspace(selectedFolder));
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
            levelOffset={16}
            renderNode={({ node, expanded, hasChildren, elementProps }) => {
              const path = node.value.slice(1);
              return (
                <Menu position="bottom-start" shadow="md" width={220}>
                  <Menu.ContextMenu>
                    <TreeRow
                      {...elementProps}
                      path={path}
                      folder={hasChildren}
                      disabled={busy}
                      expand={() => tree.expand(node.value)}
                      data-active={document?.path === path || undefined}
                      onClick={(event) => {
                        elementProps.onClick?.(event);
                        if (!hasChildren && !busy)
                          guard(() => chooseDeck(path));
                      }}
                    >
                      {hasChildren ? (
                        <IconChevronRight
                          size={14}
                          className={"tree-chevron" + (expanded ? " open" : "")}
                        />
                      ) : (
                        <IconCards
                          size={15}
                          stroke={1.75}
                          className="tree-icon"
                        />
                      )}
                      <span className="tree-label">{node.label}</span>
                      {!hasChildren && statuses.get(path) === "Unsynced" && (
                        <span
                          className="tree-dot"
                          title="The Anki package is out of date"
                        />
                      )}
                    </TreeRow>
                  </Menu.ContextMenu>
                  <Menu.Dropdown>
                    {hasChildren ? (
                      <Menu.Item
                        leftSection={<IconPlus size={16} />}
                        disabled={busy}
                        onClick={() => createDeck(path)}
                      >
                        New deck in this folder…
                      </Menu.Item>
                    ) : (
                      deckMenuItems(path)
                    )}
                  </Menu.Dropdown>
                </Menu>
              );
            }}
          />
          {workspace && decks.length === 0 && (
            <Text c="dimmed" size="sm" px="xs">
              This workspace has no Markdown decks.
            </Text>
          )}
        </div>
        <Stack gap={4}>
          {pendingDecks.length > 0 && (
            <Button
              variant="light"
              justify="space-between"
              aria-label="Review and update Anki packages"
              rightSection={
                <Badge size="sm" variant="filled" color="orange">
                  {pendingDecks.length}
                </Badge>
              }
              onClick={() => void openReview(null)}
            >
              Update Anki packages
            </Button>
          )}
          <Button
            variant="subtle"
            color="gray"
            justify="flex-start"
            leftSection={<IconPlus size={16} />}
            disabled={!workspace || busy}
            onClick={() => createDeck()}
          >
            New deck
          </Button>
        </Stack>
      </aside>
      <div className="content">
        {error && (
          <Alert
            className="banner"
            color="red"
            title="Action failed"
            withCloseButton
            closeButtonLabel="Dismiss error"
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
        {conflict && (
          <Alert
            className="banner"
            color="orange"
            title="The deck changed on disk while you edited it"
          >
            <Text size="sm">
              Another program changed this deck file, so your latest edits are
              not saved yet.
            </Text>
            <Group gap="xs" mt="sm">
              <Button size="xs" variant="default" onClick={useDiskVersion}>
                Use the disk version
              </Button>
              <Button
                size="xs"
                color="orange"
                onClick={() =>
                  keepMyVersion().catch((failure) => setError(String(failure)))
                }
              >
                Keep my version
              </Button>
            </Group>
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
                        change={changed.get(range.id) ?? null}
                        active={index === cardIndex}
                        selected={selection.includes(range.id)}
                        group={ranges
                          .map((card) => card.id)
                          .filter((id) => selection.includes(id))}
                        disabled={busy || !!parsed.error || conflict}
                        choose={(event) => chooseRow(range.id, event)}
                      />
                    ),
                )}
              </div>
              <Text className="column-foot" size="sm" c="dimmed">
                Drag cards to reorder them, or onto a deck to move them.
                Ctrl-click or Shift-click selects several.
              </Text>
            </section>
            <main className="editor-column">
              <header className="toolbar">
                <UnstyledButton
                  className="status"
                  title={document.reasons.join("\n") || document.package}
                  disabled={document.status !== "Unsynced" || busy}
                  onClick={() => void openReview(document.path)}
                >
                  <span className={"status-dot " + tone} aria-hidden />
                  <Text size="sm" fw={500} component="span">
                    {status}
                  </Text>
                </UnstyledButton>
                <Menu position="bottom-end" shadow="md" width={240}>
                  <Menu.Target>
                    <ActionIcon
                      variant="subtle"
                      color="gray"
                      size="lg"
                      aria-label="Deck actions"
                    >
                      <IconMenu2 size={18} />
                    </ActionIcon>
                  </Menu.Target>
                  <Menu.Dropdown>
                    {deckMenuItems(document.path)}
                    <Menu.Divider />
                    <Menu.Item
                      leftSection={<IconRefresh size={16} />}
                      disabled={busy || pendingDecks.length === 0}
                      onClick={() =>
                        guard(() =>
                          generate(pendingDecks.map((deck) => deck.path)),
                        )
                      }
                    >
                      Update all Anki packages
                    </Menu.Item>
                  </Menu.Dropdown>
                </Menu>
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
                      The editor and exporter found different card pairs.
                      Correct the deck file outside the app.
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
                guard(() => organize(notice.undo!, null, "Undo complete."))
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
      <ReviewChanges
        decks={review?.decks ?? null}
        mathjax={mathjax}
        opened={review !== null}
        busy={busy}
        close={() => setReview(null)}
        openCard={(path, id) => {
          setReview(null);
          guard(() => chooseDeck(path, id));
        }}
        update={(paths) => {
          setReview(null);
          guard(() => generate(paths));
        }}
      />
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
