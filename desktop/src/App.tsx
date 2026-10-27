import {
  lazy,
  Suspense,
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  type MouseEvent,
} from "react";
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
  IconAlertTriangle,
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
import type { Side } from "./editor";
import { replaceDiagram, type DiagramTarget } from "./diagrams";
import { loadMathJax, previewHtml, type MathJaxRuntime } from "./math";
import {
  CardRow,
  type CardPreview,
  DeckNameForm,
  NewDeckForm,
  TreeRow,
  deckName,
  dragSchema,
  targetSchema,
} from "./organize";
import { ReviewChanges } from "./review";
import { ProblemDrawer, useProblems } from "./problem-drawer";
import { useSearch } from "./search";
import { previousPackage, refreshTargets } from "./packages";
import { backgroundTurn, noteForegroundInput } from "./background";
import {
  request,
  watchWorkspace,
  manifestSchema,
  cachedManifestSchema,
  sourcesSchema,
  checksSchema,
  cachedChecksSchema,
  assetVersionSchema,
  cacheRebuiltSchema,
  documentSchema,
  generatedSchema,
  organizedSchema,
  reviewSchema,
  type Change,
  type Document,
  type Pending,
  type Entry,
  type Manifest,
  type SourceResult,
  type PackageCheck,
} from "./bridge";

type Task = "Idle" | "Loading" | "Generating" | "Organizing";
type Notice = { label: string; undo: Change[] | null };
// `scope` is one deck path, or null for every deck.
type Review = { scope: string | null; decks: Pending[] | null };

const STALE = /changed on disk|changed during|changed before/;

// Loading the CodeMirror/MathJax field editor is only required after a deck is
// selected. Keep its extensions out of the initial navigation bundle; Tauri
// serves this chunk locally, without an installer or network dependency.
const SideEditor = lazy(() =>
  import("./editor").then(({ SideEditor }) => ({ default: SideEditor })),
);
const QuiverEditor = lazy(() =>
  import("./quiver").then(({ QuiverEditor }) => ({ default: QuiverEditor })),
);

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

function treeData(paths: string[]): TreeNodeData[] {
  const roots: TreeNodeData[] = [];
  for (const path of paths) {
    let children = roots;
    let value = "";
    const parts = path.split("/");
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
  const [decks, setDecks] = useState<Entry[]>([]);
  const [sourceRecords, setSourceRecords] = useState(
    new Map<string, SourceResult>(),
  );
  const [searchCoverage, setSearchCoverage] = useState(new Set<string>());
  const [packageRecords, setPackageRecords] = useState(
    new Map<string, PackageCheck>(),
  );
  const [packageCacheIssue, setPackageCacheIssue] = useState<{
    root: string;
    message: string;
    kind: "CacheFailure" | "BackendFailure";
  } | null>(null);
  const [coverage, setCoverage] = useState({
    state: "idle",
    checked: 0,
    total: 0,
    error: "",
  });
  const [assetIdentity, setAssetIdentity] = useState("");
  const [cacheEpoch, setCacheEpoch] = useState(0);
  const [navigationCacheFailure, setNavigationCacheFailure] = useState<{
    root: string;
    message: string;
  } | null>(null);
  const [document, setDocument] = useState<Document | null>(null);
  const [mathjax, setMathjax] = useState<MathJaxRuntime | null>(null);
  const [index, setIndex] = useState(0);
  const [draft, setDraft] = useState<{
    source: string;
    card: CardRange;
    front: string;
    back: string;
  } | null>(null);
  const [diagramSession, setDiagramSession] = useState<{
    root: string;
    generation: number;
    navigationToken: number;
    path: string;
    cardId: string;
    side: Side;
    source: string;
    target: DiagramTarget | null;
  } | null>(null);
  const latestDraft = useRef<typeof draft>(null);
  const [task, setTask] = useState<Task>("Idle");
  const [progress, setProgress] = useState("");
  const [buildResult, setBuildResult] = useState<"Ready" | "Failed">("Ready");
  const [error, setError] = useState("");
  const [restartRequired, setRestartRequired] = useState(false);
  const [conflict, setConflict] = useState(false);
  const [log, setLog] = useState("");
  const [workspaceMenu, setWorkspaceMenu] = useState(false);
  const [cardFilter, setCardFilter] = useState("");
  const [selection, setSelection] = useState<string[]>([]);
  const [notice, setNotice] = useState<Notice | null>(null);
  const [review, setReview] = useState<Review | null>(null);
  const [problemsOpen, setProblemsOpen] = useState(false);
  // The latest document for asynchronous saves and disk events.
  const current = useRef<Document | null>(null);
  const saving = useRef<Promise<void>>(Promise.resolve());
  const savingPreferences = useRef<Promise<void>>(Promise.resolve());
  const navigation = useRef(0);
  const workspaceNavigation = useRef(0);
  const reviewRequest = useRef(0);
  const generationRequest = useRef(0);
  const reconciliation = useRef(0);
  const workspaceRoot = useRef<string | null>(null);
  const changedPaths = useRef(new Set<string>());
  const pendingSources = useRef(new Set<string>());
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
  // Mantine's Tree reinitializes its expansion state from a stale closure
  // whenever `data` changes identity, which can drop a folder the user has just
  // expanded. Republishing unchanged membership therefore keeps the same data.
  const membership = decks.map((deck) => deck.path).join("\n");
  const data = useMemo(
    () => treeData(membership ? membership.split("\n") : []),
    [membership],
  );
  // The publication mark precedes React's DOM commit. Release measurements
  // also need the first usable, painted tree (with navigation enabled).
  useEffect(() => {
    if (
      !workspace ||
      busy ||
      !decks.length ||
      performance.getEntriesByName("flashcards:tree-usable").length
    )
      return;
    let frame = requestAnimationFrame(() => {
      frame = requestAnimationFrame(() => {
        if (
          window.document.querySelector("[data-deck]") &&
          !window.document.querySelector('.sidebar-head [aria-label="Loading"]')
        ) {
          performance.mark("flashcards:tree-usable");
          // Request the local editor chunk only after navigation has painted.
          // Its JavaScript compilation must not delay the initial deck tree.
          void import("./editor");
        }
      });
    });
    return () => cancelAnimationFrame(frame);
    // Cached navigation and the reconciled manifest can have identical
    // membership but distinct array identities. Do not cancel the first
    // painted-tree measurement (or its editor prefetch) for that refetch.
  }, [workspace, busy, membership]);
  // Pandoc counts the saved deck's cards; the editor parser must agree.
  const mismatch = useMemo(
    () =>
      document !== null &&
      document.cards !== null &&
      document.cards !== cards(document.saved).length,
    [document?.cards, document?.saved],
  );
  const packageHistory = document
    ? previousPackage(packageRecords.get(document.path))
    : null;
  const changes = useMemo<CardChange[]>(() => {
    if (
      !document ||
      (document.status === null && !packageHistory) ||
      parsed.error
    )
      return [];
    try {
      return cardChanges(
        packageHistory ? packageHistory.built : document.built,
        document.source,
      );
    } catch {
      return [];
    }
  }, [
    document?.built,
    document?.source,
    document?.status,
    packageHistory?.built,
    packageHistory?.input_identity,
    parsed.error,
  ]);
  const changed = useMemo(
    () => new Map(changes.map((change) => [change.id, change.kind])),
    [changes],
  );
  // The open deck is checked as saved; the others as listed.
  const sources = useMemo(
    () =>
      decks.flatMap((deck) => {
        if (!searchCoverage.has(deck.path)) return [];
        if (deck.path === document?.path && !conflict)
          return [
            {
              path: deck.path,
              source: document.saved,
              revision: document.hash,
            },
          ];
        const result = sourceRecords.get(deck.path);
        return result?.state === "ready"
          ? [
              {
                path: deck.path,
                source: result.source,
                revision: result.revision,
              },
            ]
          : [];
      }),
    [
      decks,
      sourceRecords,
      searchCoverage,
      conflict,
      document?.path,
      document?.saved,
      document?.hash,
    ],
  );
  const {
    index: searchIndex,
    invalid: searchInvalid,
    error: searchCacheError,
    cacheFailure: searchCacheFailure,
  } = useSearch(sources, workspace, reconciliation.current, cacheEpoch);
  const searchPending =
    coverage.state === "discovering" ||
    searchCoverage.size < decks.length ||
    sources.some(
      (deck) => !searchIndex.has(deck.path) && !searchInvalid.has(deck.path),
    );
  const searchFailed =
    searchInvalid.size > 0 ||
    decks.some((deck) => sourceRecords.get(deck.path)?.state === "failed");
  const {
    problems,
    checked: problemCoverage,
    error: problemCacheError,
    cacheFailure: problemCacheFailure,
  } = useProblems(
    mathjax,
    sources,
    assetIdentity,
    workspace,
    reconciliation.current,
    cacheEpoch,
  );
  const derivedCacheError =
    navigationCacheFailure?.root === workspace
      ? navigationCacheFailure.message
      : problemCacheError ||
        searchCacheError ||
        (packageCacheIssue?.root === workspace
          ? packageCacheIssue.message
          : "");
  const derivedCacheFailure =
    navigationCacheFailure?.root === workspace ||
    problemCacheFailure ||
    searchCacheFailure ||
    (packageCacheIssue?.root === workspace &&
      packageCacheIssue.kind === "CacheFailure");
  const problemDecks = useMemo(
    () => new Set((problems ?? []).map((problem) => problem.path)),
    [problems],
  );
  const problemCards = useMemo(
    () =>
      new Set(
        (problems ?? [])
          .filter((problem) => problem.path === document?.path)
          .map((problem) => problem.card),
      ),
    [problems, document?.path],
  );

  function updateDocument(
    next: (document: Document | null) => Document | null,
  ) {
    current.current = next(current.current);
    setDocument(current.current);
  }

  function updateDraft(next: typeof draft) {
    latestDraft.current = next;
    setDraft(next);
  }

  async function refresh(root = workspace, changes: string[] | null = null) {
    if (!root || root !== workspaceRoot.current) return;
    const targets = refreshTargets(
      root,
      decks,
      sourceRecords,
      packageRecords,
      pendingSources.current,
      changes,
    );
    for (const path of targets.read) pendingSources.current.add(path);
    updateDocument((open) =>
      open && (changes === null || targets.verify.has(open.path))
        ? { ...open, status: null }
        : open,
    );
    setSearchCoverage((previous) =>
      changes === null
        ? new Set()
        : new Set([...previous].filter((path) => !targets.read.has(path))),
    );
    setPackageRecords((previous) => {
      const next = new Map(previous);
      for (const [path, check] of previous)
        if (changes === null || targets.verify.has(path))
          next.set(path, {
            state: "pending",
            path,
            previous: previousPackage(check),
          });
      return next;
    });
    const token = workspaceNavigation.current;
    const generation = ++reconciliation.current;
    if (changes === null) void checkAssetUpdate();
    const result = await request(
      { action: "manifest", workspace: root, generation },
      manifestSchema,
    );
    if (
      token !== workspaceNavigation.current ||
      generation !== reconciliation.current
    )
      return;
    setDecks(result.entries);
    const members = new Set(result.entries.map((entry) => entry.path));
    setSourceRecords(
      (previous) =>
        new Map([...previous].filter(([path]) => members.has(path))),
    );
    setPackageRecords(
      (previous) =>
        new Map([...previous].filter(([path]) => members.has(path))),
    );
    void cacheManifest(result.session.root, generation, token);
    void fillWorkspace(result, token, changes);
  }

  async function checkAssetUpdate() {
    try {
      const session = await loadMathJax();
      const active = await request(
        { action: "asset-version" },
        assetVersionSchema,
      );
      setRestartRequired(active.identity !== session.identity);
    } catch (failure) {
      setError(String(failure));
    }
  }

  async function cacheManifest(
    root: string,
    generation: number,
    token: number,
  ) {
    try {
      const result = await request(
        { action: "cache-manifest", workspace: root, generation },
        cachedManifestSchema,
      );
      if (
        token !== workspaceNavigation.current ||
        generation !== reconciliation.current
      )
        return;
      if (
        result.session.root !== root ||
        result.session.generation !== generation
      )
        throw new Error(
          "The navigation cache belongs to another workspace session.",
        );
      if (result.state === "failed")
        setNavigationCacheFailure({ root, message: result.message });
      else
        setNavigationCacheFailure((current) =>
          current?.root === root ? null : current,
        );
    } catch (failure) {
      if (
        token === workspaceNavigation.current &&
        generation === reconciliation.current
      )
        setNavigationCacheFailure({ root, message: String(failure) });
    }
  }

  async function checkPaths(
    root: string,
    generation: number,
    paths: string[],
    token: number,
  ) {
    const assets = (await loadMathJax()).identity;
    if (
      token !== workspaceNavigation.current ||
      generation !== reconciliation.current ||
      root !== workspaceRoot.current
    )
      return;
    setPackageRecords((previous) => {
      const next = new Map(previous);
      for (const path of paths)
        next.set(path, {
          state: "checking",
          path,
          previous: previousPackage(previous.get(path)),
        });
      return next;
    });
    const response = await request(
      { action: "checks", workspace: root, generation, paths, assets },
      checksSchema,
    ).catch((failure) => {
      if (
        token === workspaceNavigation.current &&
        generation === reconciliation.current
      )
        setPackageRecords((previous) => {
          const next = new Map(previous);
          for (const path of paths)
            next.set(path, {
              state: "failed",
              path,
              kind: "BackendFailure",
              message: String(failure),
              previous: previousPackage(previous.get(path)),
            });
          return next;
        });
      throw failure;
    });
    if (
      token !== workspaceNavigation.current ||
      generation !== reconciliation.current ||
      root !== workspaceRoot.current
    )
      return;
    if (
      response.session.root !== root ||
      response.session.generation !== generation
    )
      throw new Error(
        "The package response belongs to another workspace session.",
      );
    if (
      response.results.some(
        (result) => result.state === "ready" && result.assets !== assets,
      )
    )
      throw new Error("The package response uses another renderer asset set.");
    setPackageRecords((previous) => {
      const next = new Map(previous);
      for (const result of response.results)
        next.set(
          result.path,
          result.state === "ready"
            ? result
            : {
                ...result,
                previous: previousPackage(previous.get(result.path)),
              },
        );
      return next;
    });
    if (response.cache_errors.length)
      setPackageCacheIssue({
        root,
        kind: "CacheFailure",
        message: response.cache_errors
          .map((error) => error.path + ": " + error.message)
          .join("\n"),
      });
    for (const result of response.results) {
      if (result.state === "failed") continue;
      updateDocument((open) =>
        open?.path === result.path && open.hash === result.revision
          ? {
              ...open,
              status: result.status,
              reasons: result.reasons,
              built: result.built,
            }
          : open,
      );
    }
    return response.results
      .filter((result) => result.state === "failed")
      .map((result) => result.path + ": " + result.message);
  }

  async function fillWorkspace(
    manifest: Manifest,
    token: number,
    changes: string[] | null,
  ) {
    const { root, generation } = manifest.session;
    if (
      token !== workspaceNavigation.current ||
      generation !== reconciliation.current ||
      root !== workspaceRoot.current
    )
      return;
    const targets = refreshTargets(
      root,
      manifest.entries,
      sourceRecords,
      packageRecords,
      pendingSources.current,
      changes,
    );
    const work = new Set([...targets.read, ...targets.verify]);
    const workPaths = manifest.entries
      .map((entry) => entry.path)
      .filter((path) => work.has(path));
    const members = new Set(manifest.entries.map((entry) => entry.path));
    for (const path of pendingSources.current)
      if (!members.has(path)) pendingSources.current.delete(path);
    for (const path of targets.read) pendingSources.current.add(path);
    setSearchCoverage(
      (previous) =>
        new Set(
          [...previous].filter(
            (path) => members.has(path) && !targets.read.has(path),
          ),
        ),
    );
    const errors: string[] = manifest.entries.flatMap(({ path }) => {
      if (work.has(path)) return [];
      const source = sourceRecords.get(path);
      const check = packageRecords.get(path);
      return [
        ...(source?.state === "failed" ? [path + ": " + source.message] : []),
        ...(check?.state === "failed" ? [path + ": " + check.message] : []),
      ];
    });
    const skipped = manifest.entries.length - workPaths.length;
    setCoverage({
      state: "running",
      checked: skipped,
      total: manifest.entries.length,
      error: [...new Set(errors)].join("\n"),
    });
    try {
      for (let offset = 0; offset < workPaths.length; offset += 8) {
        if (
          token !== workspaceNavigation.current ||
          generation !== reconciliation.current
        )
          return;
        const paths = workPaths.slice(offset, offset + 8);
        const verifyPaths = paths.filter((path) => targets.verify.has(path));
        const readPaths = paths.filter((path) => targets.read.has(path));
        if (verifyPaths.length) {
          const assets = (await loadMathJax()).identity;
          try {
            const history = await request(
              {
                action: "cached-checks",
                workspace: root,
                generation,
                paths: verifyPaths,
                assets,
              },
              cachedChecksSchema,
            );
            if (
              token !== workspaceNavigation.current ||
              generation !== reconciliation.current
            )
              return;
            if (
              history.session.root !== root ||
              history.session.generation !== generation
            )
              throw new Error(
                "The package history belongs to another workspace session.",
              );
            setPackageRecords((previous) => {
              const next = new Map(previous);
              for (const result of history.results) {
                const current = previous.get(result.path);
                if (current?.state === "ready") continue;
                next.set(
                  result.path,
                  result.state === "pending"
                    ? {
                        ...result,
                        state:
                          current?.state === "checking"
                            ? "checking"
                            : "pending",
                        previous: previousPackage(current) ?? result.previous,
                      }
                    : { ...result, previous: previousPackage(current) },
                );
              }
              return next;
            });
            for (const result of history.results) {
              if (result.state !== "failed") continue;
              if (result.kind === "CacheFailure")
                setPackageCacheIssue({
                  root,
                  kind: "CacheFailure",
                  message: result.message,
                });
              else errors.push(result.path + ": " + result.message);
            }
            setPackageCacheIssue((current) =>
              current?.root === root && current.kind === "BackendFailure"
                ? null
                : current,
            );
          } catch (failure) {
            if (
              token !== workspaceNavigation.current ||
              generation !== reconciliation.current
            )
              return;
            setPackageCacheIssue({
              root,
              kind: "BackendFailure",
              message: String(failure),
            });
          }
        }
        if (readPaths.length) {
          const response = await request(
            {
              action: "sources",
              workspace: root,
              generation,
              paths: readPaths,
            },
            sourcesSchema,
          );
          if (
            token !== workspaceNavigation.current ||
            generation !== reconciliation.current
          )
            return;
          if (
            response.session.root !== root ||
            response.session.generation !== generation
          )
            throw new Error(
              "The source response belongs to another workspace session.",
            );
          setSourceRecords((previous) => {
            const next = new Map(previous);
            for (const result of response.results)
              next.set(result.path, result);
            return next;
          });
          for (const result of response.results) {
            pendingSources.current.delete(result.path);
            const previous = packageRecords.get(result.path);
            if (
              (result.state === "failed" ||
                (previous?.state === "ready" &&
                  previous.revision !== result.revision)) &&
              !verifyPaths.includes(result.path)
            )
              verifyPaths.push(result.path);
            if (result.state === "ready")
              updateDocument((open) =>
                open?.path === result.path && open.hash !== result.revision
                  ? { ...open, status: null }
                  : open,
              );
          }
          setSearchCoverage(
            (previous) =>
              new Set([
                ...previous,
                ...response.results.map((result) => result.path),
              ]),
          );
          for (const result of response.results)
            if (result.state === "failed")
              errors.push(result.path + ": " + result.message);
        }
        const failures = verifyPaths.length
          ? await checkPaths(root, generation, verifyPaths, token)
          : [];
        if (
          token !== workspaceNavigation.current ||
          generation !== reconciliation.current
        )
          return;
        errors.push(...(failures ?? []));
        setCoverage({
          state: "running",
          checked: skipped + offset + paths.length,
          total: manifest.entries.length,
          error: [...new Set(errors)].join("\n"),
        });
      }
      if (
        token === workspaceNavigation.current &&
        generation === reconciliation.current
      )
        setCoverage({
          state: errors.length ? "failed" : "complete",
          checked: manifest.entries.length,
          total: manifest.entries.length,
          error: [...new Set(errors)].join("\n"),
        });
    } catch (failure) {
      if (
        token === workspaceNavigation.current &&
        generation === reconciliation.current
      )
        setCoverage((current) => ({
          ...current,
          state: "failed",
          error: String(failure),
        }));
    }
  }

  const refreshOnChange = useDebouncedCallback(() => {
    const paths = [...changedPaths.current].filter(
      (path) => path === workspace || path.startsWith(workspace + "/"),
    );
    changedPaths.current.clear();
    if (paths.length)
      refresh(workspace, paths).catch((failure) => setError(String(failure)));
  }, 500);

  // Saves queue behind each other, so each one sends the hash the previous
  // save returned. A deck with invalid card structure stays unsaved.
  function persist(): Promise<void> {
    saving.current = saving.current.then(async () => {
      const open = current.current;
      if (!open || open.source === open.saved) return;
      const selectionToken = navigation.current;
      const stillOpen = (latest: Document | null): latest is Document =>
        selectionToken === navigation.current &&
        latest?.path === open.path &&
        latest.session.root === open.session.root &&
        latest.session.generation === open.session.generation &&
        latest.hash === open.hash &&
        latest.saved === open.saved;
      try {
        cards(open.source);
      } catch {
        return;
      }
      try {
        const result = await request(
          {
            action: "save",
            generation: reconciliation.current,
            workspace: open.session.root,
            path: open.path,
            source: open.source,
            expected: open.hash,
          },
          documentSchema,
        );
        if (stillOpen(current.current)) {
          updateDocument((document) =>
            stillOpen(document)
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
        }
        void checkPaths(
          open.session.root,
          reconciliation.current,
          [open.path],
          workspaceNavigation.current,
        ).catch((failure) => setError(String(failure)));
      } catch (failure) {
        if (!stillOpen(current.current)) return;
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
    const token = workspaceNavigation.current;
    flush()
      .then(() => {
        if (token === workspaceNavigation.current) return action();
      })
      .catch((failure) => {
        if (token === workspaceNavigation.current) setError(String(failure));
      });
  }

  const publishedField = useRef("");
  async function chooseWorkspace(root: string) {
    const token = ++workspaceNavigation.current;
    reviewRequest.current++;
    generationRequest.current++;
    setReview(null);
    setProgress("");
    const previousRoot = workspaceRoot.current ?? workspace;
    workspaceRoot.current = null;
    changedPaths.current.clear();
    pendingSources.current.clear();
    const navigationToken = ++navigation.current;
    const generation = ++reconciliation.current;
    setTask("Loading");
    setError("");
    loadMathJax().then(
      (loaded) => {
        if (token !== workspaceNavigation.current) return;
        setAssetIdentity(loaded.identity);
        setMathjax(loaded.mathjax);
      },
      (failure) => {
        if (token === workspaceNavigation.current) setError(String(failure));
      },
    );
    let published = false;
    const publish = (result: Manifest) => {
      workspaceRoot.current = result.session.root;
      setWorkspace(result.session.root);
      setDecks(result.entries);
      if (published) return;
      published = true;
      // Release timing reads this mark to separate page work from launch.
      if (!performance.getEntriesByName("flashcards:tree-published").length)
        performance.mark("flashcards:tree-published");
      if (isTauri())
        savingPreferences.current = savingPreferences.current
          .then(async () => {
            if (token !== workspaceNavigation.current) return;
            const store = await preferences();
            if (token !== workspaceNavigation.current) return;
            await store.set("workspace", result.session.root);
            await store.save();
          })
          .catch((failure) => {
            if (token === workspaceNavigation.current)
              setError(String(failure));
          });
      // A path the user is typing for the next workspace takes precedence.
      const typed = workspaceForm.getValues().workspace;
      if (!typed || typed === publishedField.current)
        workspaceForm.setFieldValue("workspace", result.session.root);
      publishedField.current = result.session.root;
      setSourceRecords(new Map());
      setSearchCoverage(new Set());
      setPackageRecords(new Map());
      setPackageCacheIssue(null);
      updateDocument(() => null);
      setSelection([]);
      setNotice(null);
      updateDraft(null);
      setLog("");
      setConflict(false);
      setBuildResult("Ready");
    };
    try {
      const cached = await request(
        { action: "cached-manifest", workspace: root, generation },
        cachedManifestSchema,
      );
      if (token !== workspaceNavigation.current) return;
      if (cached.session.generation !== generation)
        throw new Error(
          "The cached navigation belongs to another workspace session.",
        );
      if (cached.state === "cached") {
        await flush();
        if (token !== workspaceNavigation.current) return;
        publish(cached);
        setCoverage({ state: "discovering", checked: 0, total: 0, error: "" });
        if (navigationToken === navigation.current) setTask("Idle");
      }
      if (cached.state === "failed")
        setNavigationCacheFailure({
          root: cached.session.root,
          message: cached.message,
        });
      const result = await request(
        { action: "manifest", workspace: root, generation },
        manifestSchema,
      );
      if (token !== workspaceNavigation.current) return;
      if (
        result.session.root !== cached.session.root ||
        result.session.generation !== generation
      )
        throw new Error(
          "The discovered navigation belongs to another workspace session.",
        );
      if (!published) await flush();
      if (
        token !== workspaceNavigation.current ||
        generation !== reconciliation.current
      )
        return;
      publish(result);
      if (cached.state !== "failed")
        void cacheManifest(result.session.root, generation, token);
      void fillWorkspace(result, token, null);
    } catch (failure) {
      if (token === workspaceNavigation.current) {
        if (!published) workspaceRoot.current = previousRoot;
        setError(String(failure));
      }
    } finally {
      if (
        token === workspaceNavigation.current &&
        navigationToken === navigation.current
      )
        setTask("Idle");
    }
  }

  function showDocument(
    path: string,
    result: Omit<Document, "path" | "saved">,
    cardId?: string,
  ) {
    const parsed = cards(result.source);
    const target =
      cardId === undefined ? 0 : parsed.findIndex((card) => card.id === cardId);
    updateDocument(() => ({ ...result, path, saved: result.source }));
    const folders = path.split("/").slice(0, -1);
    folders.forEach((_, depth) =>
      tree.expand("/" + folders.slice(0, depth + 1).join("/")),
    );
    selectCard(Math.max(0, target), result.source);
    setConflict(false);
  }

  async function chooseDeck(
    path: string,
    cardId?: string,
    selection: "required" | "preferred" = "required",
  ) {
    const token = ++navigation.current;
    const workspaceToken = workspaceNavigation.current;
    setTask("Loading");
    setError("");
    try {
      const result = await request(
        { action: "load", workspace, path, generation: reconciliation.current },
        documentSchema,
      );
      if (
        token !== navigation.current ||
        workspaceToken !== workspaceNavigation.current
      )
        return;
      if (result.session.root !== workspace)
        throw new Error("The document belongs to another workspace session.");
      if (
        selection === "required" &&
        cardId !== undefined &&
        !cards(result.source).some((card) => card.id === cardId)
      )
        throw new Error(
          "This card changed on disk. Search again for its current version.",
        );
      showDocument(path, result, cardId);
      void checkPaths(
        workspace,
        reconciliation.current,
        [path],
        workspaceNavigation.current,
      ).catch((failure) => setError(String(failure)));
      setSelection([]);
      setLog("");
      setBuildResult("Ready");
      setCardFilter("");
    } catch (failure) {
      if (
        token === navigation.current &&
        workspaceToken === workspaceNavigation.current
      )
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
      {
        action: "load",
        workspace: open.session.root,
        path: open.path,
        generation: reconciliation.current,
      },
      documentSchema,
    );
    const latest = current.current;
    if (
      token !== navigation.current ||
      latest?.path !== open.path ||
      latest.session.root !== open.session.root ||
      latest.source !== latest.saved
    )
      return;
    if (result.session.root !== open.session.root)
      throw new Error("The document belongs to another workspace session.");
    if (result.hash === latest.hash) return;
    showDocument(open.path, result, ranges[index]?.id);
  }

  const followOnChange = useDebouncedCallback(() => {
    const open = current.current;
    const token = navigation.current;
    followDisk().catch((failure) => {
      const latest = current.current;
      if (
        token !== navigation.current ||
        latest?.path !== open?.path ||
        latest?.session.root !== open?.session.root
      )
        return;
      // A deck removed outside the app closes.
      if (/No such file|does not exist/.test(String(failure))) {
        updateDocument(() => null);
        updateDraft(null);
        return;
      }
      setError(String(failure));
    });
  }, 300);

  useEffect(() => {
    window.addEventListener("keydown", noteForegroundInput, true);
    window.addEventListener("input", noteForegroundInput, true);
    window.addEventListener("pointerdown", noteForegroundInput, true);
    return () => {
      window.removeEventListener("keydown", noteForegroundInput, true);
      window.removeEventListener("input", noteForegroundInput, true);
      window.removeEventListener("pointerdown", noteForegroundInput, true);
    };
  }, []);

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
    const token = workspaceNavigation.current;
    const reconcileOnFocus = () => {
      if (disposed || token !== workspaceNavigation.current) return;
      refresh().catch((failure) => setError(String(failure)));
      followOnChange();
    };
    window.addEventListener("focus", reconcileOnFocus);
    let stop: (() => void) | undefined;
    watchWorkspace(workspace, (paths) => {
      if (disposed || token !== workspaceNavigation.current) return;
      const relevant = paths
        .map((path) => path.replace(/\\/g, "/"))
        .filter(
          (path) =>
            !/(?:^|\/)(?:\.git|node_modules|src-tauri|test-artifacts)(?:\/|$)/.test(
              path,
            ) && !path.includes(".flashcards-"),
        );
      if (!relevant.length) return;
      for (const path of relevant) changedPaths.current.add(path);
      refreshOnChange();
      const open = current.current;
      if (open && relevant.includes(workspace + "/" + open.path))
        followOnChange();
    })
      .then((unwatch) => {
        if (disposed) unwatch();
        else stop = unwatch;
      })
      .catch((failure) => setError(String(failure)));
    return () => {
      disposed = true;
      window.removeEventListener("focus", reconcileOnFocus);
      stop?.();
    };
  }, [workspace, refreshOnChange, followOnChange]);

  function edit(source: string) {
    noteForegroundInput();
    // The ref holds the latest text; a render-time copy can predate the
    // previous keystroke, which would drop an edit that restores it.
    const open = current.current;
    if (!open || open.source === source) return;
    updateDocument((open) => (open ? { ...open, source } : open));
    autosave();
  }

  function selectCard(cardIndex: number, source: string) {
    setIndex(cardIndex);
    const card = cards(source)[cardIndex];
    updateDraft(
      card
        ? { source, card, front: card.front.value, back: card.back.value }
        : null,
    );
  }

  function editCard(field: Side, value: string) {
    const previous = latestDraft.current;
    if (!current.current || !previous) return;
    const next = { ...previous, [field]: value };
    let source = previous.source;
    const sides: Side[] = ["front", "back"];
    for (const side of sides.sort(
      (a, b) => previous.card[b].from - previous.card[a].from,
    )) {
      source = replaceField(source, previous.card[side], next[side]);
    }
    updateDraft(next);
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
    void chooseDeck(open.path, selected?.id, "preferred");
  }

  // The edits replace the disk version.
  async function keepMyVersion() {
    const open = current.current;
    if (!open) return;
    const token = navigation.current;
    const disk = await request(
      {
        action: "load",
        workspace: open.session.root,
        path: open.path,
        generation: reconciliation.current,
      },
      documentSchema,
    );
    if (
      token !== navigation.current ||
      current.current?.path !== open.path ||
      current.current.session.root !== open.session.root ||
      current.current.session.generation !== open.session.generation ||
      current.current.hash !== open.hash
    )
      return;
    updateDocument((document) =>
      document && document.path === open.path
        ? { ...document, hash: disk.hash }
        : document,
    );
    await persist();
  }

  async function generate(paths: string[]) {
    const root = workspace;
    const workspaceToken = workspaceNavigation.current;
    const token = ++generationRequest.current;
    const active = () =>
      token === generationRequest.current &&
      workspaceToken === workspaceNavigation.current &&
      root === workspaceRoot.current;
    await flush();
    if (!active()) return;
    const assets = (await loadMathJax()).identity;
    if (!active()) return;
    setTask("Generating");
    setBuildResult("Ready");
    setError("");
    const logs: string[] = [];
    const failures: string[] = [];
    for (const [position, path] of paths.entries()) {
      if (!active()) return;
      setProgress(
        paths.length === 1
          ? "Updating the Anki package…"
          : `Updating Anki package ${position + 1} of ${paths.length}…`,
      );
      try {
        const result = await request(
          { action: "generate", workspace: root, path, assets },
          generatedSchema,
        );
        if (!active()) return;
        logs.push(deckName(path) + "\n" + result.log);
      } catch (failure) {
        if (!active()) return;
        failures.push(deckName(path) + ": " + String(failure));
        if (path === current.current?.path) setBuildResult("Failed");
      }
    }
    if (!active()) return;
    setLog([...logs, ...failures].join("\n\n"));
    if (failures.length) setError(failures.join("\n\n"));
    setProgress("");
    setTask("Idle");
    await refresh();
    if (!active()) return;
    await followDisk();
  }

  async function generateAll() {
    const root = workspace;
    const workspaceToken = workspaceNavigation.current;
    const token = ++generationRequest.current;
    const active = () =>
      token === generationRequest.current &&
      workspaceToken === workspaceNavigation.current &&
      root === workspaceRoot.current;
    await flush();
    if (!active()) return;
    const assets = (await loadMathJax()).identity;
    if (!active()) return;
    try {
      const result = await request(
        { action: "review", workspace: root, assets },
        reviewSchema,
      );
      if (active()) await generate(result.decks.map((deck) => deck.path));
    } catch (failure) {
      if (active()) setError(String(failure));
    }
  }

  async function openReview(scope: string | null) {
    const root = workspace;
    const workspaceToken = workspaceNavigation.current;
    const token = ++reviewRequest.current;
    const active = () =>
      token === reviewRequest.current &&
      workspaceToken === workspaceNavigation.current &&
      root === workspaceRoot.current;
    setReview({ scope, decks: null });
    try {
      await flush();
      if (!active()) return;
      const assets = (await loadMathJax()).identity;
      if (!active()) return;
      const result = await request(
        { action: "review", workspace: root, assets },
        reviewSchema,
      );
      if (!active()) return;
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
      if (!active()) return;
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
    return request(
      { action: "load", workspace, path, generation: reconciliation.current },
      documentSchema,
    );
  }

  // Changes publish immediately; the open deck reloads, or follows `focus`.
  // Without `originals` the change has no Undo.
  async function organize(
    changes: Change[],
    originals: Record<string, string | null> | null,
    label: string,
    focus?: string,
  ) {
    const root = workspace;
    const workspaceToken = workspaceNavigation.current;
    const navigationToken = navigation.current;
    const active = () =>
      workspaceToken === workspaceNavigation.current &&
      root === workspaceRoot.current;
    const ownsSelection = () =>
      active() && navigationToken === navigation.current;
    // The caller may have awaited a file read in an older workspace before
    // invoking organize. Do not write its edits to that obsolete root.
    if (!active()) return;
    const open = current.current?.path;
    const touched = changes.some((change) => change.path === open);
    setTask("Organizing");
    setError("");
    try {
      const result = await request(
        { action: "organize", workspace: root, changes },
        organizedSchema,
      );
      if (!active()) return;
      await refresh(root);
      if (!active()) return;
      const removed = changes
        .filter((change) => change.source === null)
        .map((change) => change.path);
      const next = focus ?? (touched ? open : undefined);
      if (ownsSelection()) {
        if (next && !removed.includes(next))
          await chooseDeck(next, selected?.id, "preferred");
        else if (touched) {
          navigation.current++;
          updateDocument(() => null);
          updateDraft(null);
          setSelection([]);
          setTask("Idle");
        }
      }
      if (!active()) return;
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
    } catch (failure) {
      if (active()) throw failure;
    } finally {
      // A superseding deck load or workspace change owns the task indicator.
      if (ownsSelection()) setTask("Idle");
    }
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

  // Rows receive one stable handler that calls the current chooseRow.
  const chooseRowRef = useRef(chooseRow);
  chooseRowRef.current = chooseRow;
  const chooseCard = useCallback(
    (id: string, event: MouseEvent) => chooseRowRef.current(id, event),
    [],
  );
  const selectedGroup = useMemo(
    () => ranges.map((card) => card.id).filter((id) => selection.includes(id)),
    [ranges, selection],
  );
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

  const pendingDecks = decks.filter((deck) => {
    const result = packageRecords.get(deck.path);
    return result?.state === "ready" && result.status === "Unsynced";
  });
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
              : document?.status === null
                ? "Checking Anki package…"
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
  // Summaries are keyed by renderer and TeX source, so an edit renders only
  // the changed field. Unrendered fields show no summary until their turn.
  const previewCache = useRef<{
    renderer: MathJaxRuntime | null;
    html: Map<string, string>;
  }>({ renderer: null, html: new Map() });
  const [previewVersion, setPreviewVersion] = useState(0);
  useEffect(() => {
    if (!mathjax) return;
    const cache = previewCache.current;
    if (cache.renderer !== mathjax) {
      cache.renderer = mathjax;
      cache.html = new Map();
    }
    const missing = [
      ...new Set(
        ranges.flatMap((range) => [
          range.front.value,
          range.back.value.split(/\n\s*\n/)[0],
        ]),
      ),
    ].filter((source) => !cache.html.has(source));
    if (!missing.length) return;
    let cancelled = false;
    async function renderPreviews(renderer: MathJaxRuntime) {
      let published = performance.now();
      for (const source of missing) {
        // Each MathJax conversion is synchronous and can outlast a frame.
        // Yielding through a zero-delay timer immediately queues more main-
        // thread work, competing with typing. Render one summary at a time
        // only when the browser has an idle turn (with a finite fallback).
        await backgroundTurn();
        if (cancelled) return;
        cache.html.set(source, previewHtml(renderer, source));
        // The cache is mutable; publish at bounded intervals rather than
        // triggering one whole-editor React render for every card summary.
        if (performance.now() - published > 50) {
          setPreviewVersion((version) => version + 1);
          published = performance.now();
        }
      }
      if (!cancelled) setPreviewVersion((version) => version + 1);
    }
    void renderPreviews(mathjax).catch((failure) => {
      if (!cancelled) setError(String(failure));
    });
    return () => {
      cancelled = true;
    };
  }, [mathjax, ranges]);
  const previews = useMemo((): (CardPreview | null)[] => {
    const html = previewCache.current.html;
    return ranges.map((range) => {
      const front = html.get(range.front.value);
      const back = html.get(range.back.value.split(/\n\s*\n/)[0]);
      return front !== undefined && back !== undefined ? { front, back } : null;
    });
    // previewVersion publishes insertions into the mutable cache.
  }, [ranges, previewVersion, mathjax]);
  const statuses = useMemo(
    () =>
      new Map(
        [...packageRecords].flatMap(([path, result]) =>
          result.state === "ready" ? [[path, result.status] as const] : [],
        ),
      ),
    [packageRecords],
  );

  useHotkeys([["mod+S", () => guard(() => {})]], [], true);

  function openWorkspace() {
    if (workspaceForm.validate().hasErrors) return;
    const root = workspaceForm.getValues().workspace;
    setWorkspaceMenu(false);
    guard(() => chooseWorkspace(root));
  }

  function refreshWorkspace() {
    refresh().catch((failure) => setError(String(failure)));
  }

  async function rebuildCache() {
    try {
      await request(
        {
          action: "rebuild-cache",
          workspace,
          generation: reconciliation.current,
        },
        cacheRebuiltSchema,
      );
      setCacheEpoch((epoch) => epoch + 1);
      setNavigationCacheFailure(null);
      setPackageCacheIssue(null);
      await refresh();
    } catch (failure) {
      setError(String(failure));
    }
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
                id: "problems",
                label: "Show problems",
                onClick: () => setProblemsOpen(true),
              },
              {
                id: "generate-all",
                label: "Update all Anki packages",
                disabled: busy,
                onClick: () => guard(generateAll),
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
      actions: decks.flatMap((deck) => {
        const entries =
          deck.path === document?.path
            ? ranges.map((card) => ({
                id: card.id,
                label: card.label,
                front: card.front.value,
                back: card.back.value,
                tags: card.tags,
              }))
            : (searchIndex.get(deck.path) ?? []);
        return entries.map((range, cardIndex) => ({
          id: "card:" + deck.path + ":" + range.id,
          label: range.label,
          description: deckName(deck.path),
          keywords: [range.front, range.back, range.tags],
          onClick: () => {
            if (document?.path === deck.path) {
              setSelection([range.id]);
              selectCard(cardIndex, document.source);
            } else guard(() => chooseDeck(deck.path, range.id));
          },
        }));
      }),
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
                placeholder="Folder containing your Markdown decks"
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
                {/* A pending load is superseded by its navigation token, so a
                    stalled workspace never prevents opening another. */}
                <Button
                  disabled={busy && task !== "Loading"}
                  onClick={openWorkspace}
                >
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
              const check = packageRecords.get(path);
              const previous = previousPackage(check);
              const checkTitle =
                check?.state === "failed"
                  ? check.message +
                    (previous
                      ? " Previous package status: " + previous.status + "."
                      : "")
                  : previous
                    ? "Previous package status: " +
                      previous.status +
                      ". Checking current inputs."
                    : "Checking Anki package inputs.";
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
                      data-package-state={
                        hasChildren ? undefined : (check?.state ?? "pending")
                      }
                      data-previous-package-status={
                        hasChildren || check?.state === "ready"
                          ? undefined
                          : previous?.status
                      }
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
                      {!hasChildren && problemDecks.has(path) && (
                        <span
                          className="tree-dot problem"
                          title="The deck has problems"
                        />
                      )}
                      {!hasChildren && statuses.get(path) === "Unsynced" && (
                        <span
                          className="tree-dot"
                          title="The Anki package is out of date"
                        />
                      )}
                      {!hasChildren && check?.state !== "ready" && (
                        <span
                          className={
                            "tree-dot " +
                            (check?.state === "failed" ? "failed" : "pending")
                          }
                          title={checkTitle}
                          role="img"
                          aria-label={checkTitle}
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
          {workspace &&
            decks.length === 0 &&
            coverage.state !== "discovering" && (
              <Text c="dimmed" size="sm" px="xs">
                This workspace has no Markdown decks.
              </Text>
            )}
        </div>
        <Stack gap={4}>
          {workspace && (
            <Text
              size="xs"
              c="dimmed"
              px="xs"
              className="workspace-progress"
              role="status"
            >
              {coverage.state === "complete" &&
              !derivedCacheError &&
              !searchPending &&
              !searchFailed &&
              problemCoverage === decks.length
                ? "Workspace checks complete"
                : coverage.state === "failed" ||
                    derivedCacheError ||
                    searchFailed
                  ? "Workspace checks need attention"
                  : coverage.state === "discovering"
                    ? "Refreshing workspace membership…"
                    : `Checking ${coverage.checked} of ${coverage.total} decks…`}
            </Text>
          )}
          {coverage.error && (
            <Text size="xs" c="red" px="xs">
              {coverage.error}
              <Button variant="subtle" size="xs" onClick={refreshWorkspace}>
                Retry checks
              </Button>
            </Text>
          )}
          {derivedCacheError && (
            <Text size="xs" c="red" px="xs">
              {derivedCacheError}
              <Button
                variant="subtle"
                size="xs"
                onClick={() =>
                  derivedCacheFailure ? void rebuildCache() : refreshWorkspace()
                }
              >
                {derivedCacheFailure ? "Rebuild cached data" : "Retry checks"}
              </Button>
            </Text>
          )}
          {workspace && (
            <Button
              variant="subtle"
              color={problems?.length ? "red" : "gray"}
              justify="space-between"
              aria-label="Show problems"
              styles={{ label: { flex: 1 } }}
              leftSection={<IconAlertTriangle size={16} />}
              rightSection={
                problems?.length ? (
                  <Badge size="sm" variant="filled" color="red">
                    {problems.length}
                  </Badge>
                ) : null
              }
              onClick={() => setProblemsOpen(true)}
            >
              Problems
              {coverage.state === "discovering"
                ? " (refreshing)"
                : problemCoverage < decks.length &&
                  ` (${problemCoverage}/${decks.length} checked)`}
            </Button>
          )}
          {workspace && decks.length > 0 && (
            <Button
              variant="light"
              justify="space-between"
              aria-label="Review and update Anki packages"
              rightSection={
                pendingDecks.length > 0 &&
                decks.every(
                  (deck) => packageRecords.get(deck.path)?.state === "ready",
                ) ? (
                  <Badge size="sm" variant="filled" color="orange">
                    {pendingDecks.length}
                  </Badge>
                ) : null
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
        {restartRequired && (
          <Alert className="banner" color="blue" title="Renderer update ready">
            Restart the app to use the updated renderer assets.
          </Alert>
        )}
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
                : "Choose the folder containing your Markdown decks."}
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
                        problem={problemCards.has(range.id)}
                        active={index === cardIndex}
                        selected={selection.includes(range.id)}
                        group={selectedGroup}
                        disabled={busy || !!parsed.error || conflict}
                        choose={chooseCard}
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
                      disabled={busy}
                      onClick={() => guard(() => generateAll())}
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
                      <Suspense fallback={<Text>Loading card editors…</Text>}>
                        <div className="side-editors">
                          {(["front", "back"] as const).map((side) => (
                            <SideEditor
                              key={
                                document.path + ":" + draft.card.id + ":" + side
                              }
                              side={side}
                              workspace={document.session.root}
                              path={document.path}
                              value={draft[side]}
                              mathjax={mathjax}
                              editable={!busy}
                              onChange={(value) => editCard(side, value)}
                              onNewDiagram={() => {
                                const active = latestDraft.current;
                                if (!active || !current.current) return;
                                setDiagramSession({
                                  root: current.current.session.root,
                                  generation:
                                    current.current.session.generation,
                                  navigationToken: navigation.current,
                                  path: current.current.path,
                                  cardId: active.card.id,
                                  side,
                                  source: active[side],
                                  target: null,
                                });
                              }}
                              onEditDiagram={(target) => {
                                const active = latestDraft.current;
                                if (!active || !current.current) return;
                                setDiagramSession({
                                  root: current.current.session.root,
                                  generation:
                                    current.current.session.generation,
                                  navigationToken: navigation.current,
                                  path: current.current.path,
                                  cardId: active.card.id,
                                  side,
                                  source: active[side],
                                  target,
                                });
                              }}
                            />
                          ))}
                        </div>
                      </Suspense>
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
                          updateDraft({
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
        close={() => {
          reviewRequest.current++;
          setReview(null);
        }}
        openCard={(path, id) => {
          setReview(null);
          guard(() => chooseDeck(path, id));
        }}
        update={(paths) => {
          setReview(null);
          guard(() => generate(paths));
        }}
      />
      <ProblemDrawer
        problems={problems}
        decks={decks.length}
        checked={problemCoverage}
        manifestReady={coverage.state !== "discovering"}
        mathjax={mathjax}
        opened={problemsOpen}
        close={() => setProblemsOpen(false)}
        open={(problem) => {
          setProblemsOpen(false);
          guard(() => chooseDeck(problem.path, problem.card ?? undefined));
        }}
      />
      {diagramSession && (
        <Suspense fallback={<Text>Loading Quiver…</Text>}>
          <QuiverEditor
            initial={diagramSession.target}
            onClose={() => setDiagramSession(null)}
            onApply={(source) => {
              const active = latestDraft.current;
              const doc = current.current;
              if (
                !active ||
                !doc ||
                doc.session.root !== diagramSession.root ||
                doc.session.generation !== diagramSession.generation ||
                navigation.current !== diagramSession.navigationToken ||
                doc.path !== diagramSession.path ||
                active.card.id !== diagramSession.cardId ||
                active[diagramSession.side] !== diagramSession.source
              ) {
                setError(
                  "The card changed while Quiver was open. Reopen its current diagram.",
                );
                setDiagramSession(null);
                return;
              }
              try {
                editCard(
                  diagramSession.side,
                  replaceDiagram(
                    diagramSession.source,
                    diagramSession.target,
                    source,
                  ),
                );
                setDiagramSession(null);
              } catch (failure) {
                setError(String(failure));
              }
            }}
          />
        </Suspense>
      )}
      <Spotlight
        actions={commands}
        limit={40}
        highlightQuery
        nothingFound={
          searchFailed
            ? "Some decks could not be searched. See Problems."
            : searchPending
              ? "Search is incomplete while workspace cards load."
              : "Nothing found"
        }
        shortcut="mod + K"
        tagsToIgnore={[]}
        triggerOnContentEditable
        searchProps={{
          leftSection: <IconSearch size={18} />,
          placeholder: "Search decks, cards, and commands",
          rightSectionWidth: searchPending || searchFailed ? 170 : undefined,
          rightSection:
            searchPending || searchFailed ? (
              <Text size="xs" c="dimmed" role="status">
                {searchFailed
                  ? "Some decks unavailable"
                  : "Loading workspace cards…"}
              </Text>
            ) : undefined,
        }}
      />
    </div>
  );
}
