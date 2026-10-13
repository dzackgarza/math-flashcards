import { useEffect, useRef, useState } from "react";
import {
  ActionIcon,
  Alert,
  Badge,
  Box,
  Breadcrumbs,
  Button,
  Checkbox,
  Group,
  Loader,
  Menu,
  Modal,
  Paper,
  Select,
  Stack,
  Text,
  TextInput,
  Title,
  UnstyledButton,
} from "@mantine/core";
import { useMediaQuery } from "@mantine/hooks";
import {
  IconArrowDown,
  IconArrowUp,
  IconCards,
  IconDots,
  IconGripVertical,
  IconPlus,
  IconScissors,
  IconTransfer,
  IconArrowBackUp,
} from "@tabler/icons-react";
import {
  draggable,
  dropTargetForElements,
  monitorForElements,
  type ElementEventPayloadMap,
} from "@atlaskit/pragmatic-drag-and-drop/element/adapter";
import { combine } from "@atlaskit/pragmatic-drag-and-drop/combine";
import { attachClosestEdge } from "@atlaskit/pragmatic-drag-and-drop-hitbox/closest-edge/attach-closest-edge";
import { extractClosestEdge } from "@atlaskit/pragmatic-drag-and-drop-hitbox/closest-edge/extract-closest-edge";
import type { Edge } from "@atlaskit/pragmatic-drag-and-drop-hitbox/types";
import DropIndicator from "@atlaskit/pragmatic-drag-and-drop-react-drop-indicator/box";
import {
  autoScrollForElements,
  autoScrollWindowForElements,
} from "@atlaskit/pragmatic-drag-and-drop-auto-scroll/element";
import { announce } from "@atlaskit/pragmatic-drag-and-drop-live-region";
import { MathJax, MathJaxContext } from "better-react-mathjax";
import DOMPurify from "dompurify";
import { z } from "zod";
import { cards, reorderCards, transferCards, type CardRange } from "./cards";
import {
  documentSchema,
  previewSchema,
  organizedSchema,
  request,
  type Change,
  type Document,
  type Preview,
  type Summary,
} from "./bridge";

const dragSchema = z.discriminatedUnion("kind", [
  z.object({
    kind: z.literal("cards"),
    path: z.string(),
    ids: z.array(z.string()),
  }),
  z.object({ kind: z.literal("deck"), path: z.string() }),
]);
const targetSchema = z.object({
  path: z.string(),
  card: z.string().optional(),
});
type Dialog = {
  kind: "new" | "split" | "move" | "absorb";
  path: string;
} | null;
type Undo = { changes: Change[]; focus: string | null };
const deckName = (path: string) =>
  path.split("/").slice(-1)[0].replace(/\.md$/, "");

function DeckTile({
  deck,
  compact,
  disabled,
  open,
  absorb,
}: {
  deck: Summary;
  compact?: boolean;
  disabled: boolean;
  open: () => void;
  absorb: () => void;
}) {
  const element = useRef<HTMLDivElement>(null);
  const handle = useRef<HTMLButtonElement>(null);
  const [over, setOver] = useState(false);
  const [dragging, setDragging] = useState(false);
  // Atlassian's handle + target pattern: https://atlassian.design/components/pragmatic-drag-and-drop/design-guidelines/
  useEffect(() => {
    if (!element.current || !handle.current) return;
    return combine(
      draggable({
        element: element.current,
        dragHandle: handle.current,
        canDrag: () => !disabled,
        getInitialData: () => ({ kind: "deck", path: deck.path }),
        onDragStart: () => setDragging(true),
        onDrop: () => setDragging(false),
      }),
      dropTargetForElements({
        element: element.current,
        canDrop: ({ source }) =>
          !disabled && dragSchema.parse(source.data).path !== deck.path,
        getData: () => ({ path: deck.path }),
        onDragEnter: () => setOver(true),
        onDragLeave: () => setOver(false),
        onDrop: () => setOver(false),
      }),
    );
  }, [deck.path, disabled]);
  return (
    <Paper
      ref={element}
      withBorder
      p={compact ? "sm" : "md"}
      className={
        "deck-tile " +
        (over ? "drop-active " : "") +
        (dragging ? "dragging " : "") +
        (compact ? "compact" : "")
      }
      data-deck={deck.path}
    >
      <Group justify="space-between" wrap="nowrap">
        <ActionIcon
          ref={handle}
          disabled={disabled}
          variant="subtle"
          color="gray"
          aria-label={"Drag deck " + deckName(deck.path)}
          className="drag-handle"
        >
          <IconGripVertical size={18} />
        </ActionIcon>
        <IconCards
          size={compact ? 22 : 32}
          color="var(--mantine-color-indigo-5)"
        />
        <Menu position="bottom-end">
          <Menu.Target>
            <ActionIcon
              variant="subtle"
              color="gray"
              aria-label={"Actions for " + deckName(deck.path)}
            >
              <IconDots size={18} />
            </ActionIcon>
          </Menu.Target>
          <Menu.Dropdown>
            <Menu.Item onClick={open}>Open deck</Menu.Item>
            <Menu.Item onClick={absorb} disabled={disabled}>
              Absorb into another deck
            </Menu.Item>
          </Menu.Dropdown>
        </Menu>
      </Group>
      <UnstyledButton
        onClick={open}
        disabled={disabled}
        className="deck-open"
        aria-label={"Open deck " + deckName(deck.path)}
      >
        <Text fw={650} mt="sm">
          {deckName(deck.path)}
        </Text>
        <Text c="dimmed" size="xs" lineClamp={1}>
          {deck.path.split("/").slice(0, -1).join(" / ") || "Workspace"}
        </Text>
      </UnstyledButton>
      <Group justify="space-between" mt="sm">
        <Badge
          size="xs"
          color={deck.status === "Up to date" ? "teal" : "orange"}
          variant="light"
        >
          {deck.status}
        </Badge>
        {over && (
          <Text size="xs" c="indigo" fw={600}>
            Drop here
          </Text>
        )}
      </Group>
    </Paper>
  );
}

function CardTile({
  card,
  html,
  path,
  selected,
  group,
  busy,
  select,
  edit,
}: {
  card: CardRange;
  html: string;
  path: string;
  selected: boolean;
  group: string[];
  busy: boolean;
  select: (id: string, range: boolean) => void;
  edit: () => void;
}) {
  const element = useRef<HTMLDivElement>(null);
  const handle = useRef<HTMLButtonElement>(null);
  const [edge, setEdge] = useState<Edge | null>(null);
  const [dragging, setDragging] = useState(false);
  const narrow = useMediaQuery("(max-width: 48em)");
  const ids = selected ? group : [card.id];
  useEffect(() => {
    if (!element.current || !handle.current) return;
    return combine(
      draggable({
        element: element.current,
        dragHandle: handle.current,
        canDrag: () => !busy,
        getInitialData: () => ({ kind: "cards", path, ids }),
        onDragStart: () => setDragging(true),
        onDrop: () => setDragging(false),
      }),
      dropTargetForElements({
        element: element.current,
        canDrop: ({ source }) => {
          const data = dragSchema.parse(source.data);
          return !busy && data.kind === "cards" && !data.ids.includes(card.id);
        },
        getData: ({ input, element }) =>
          attachClosestEdge(
            { path, card: card.id },
            {
              input,
              element,
              allowedEdges: narrow ? ["top", "bottom"] : ["left", "right"],
            },
          ),
        onDrag: ({ self }) => setEdge(extractClosestEdge(self.data)),
        onDragLeave: () => setEdge(null),
        onDrop: () => setEdge(null),
      }),
    );
  }, [path, card.id, ids.join("|"), busy, narrow]);
  return (
    <Paper
      ref={element}
      withBorder
      className={
        "organizer-card " +
        (selected ? "selected " : "") +
        (dragging ? "dragging" : "")
      }
      data-card={card.id}
    >
      <Group justify="space-between" p="sm">
        <Checkbox
          checked={selected}
          aria-label={"Select card " + card.label}
          disabled={busy}
          onChange={(event) =>
            select(
              card.id,
              event.nativeEvent instanceof MouseEvent &&
                event.nativeEvent.shiftKey,
            )
          }
        />
        <Badge variant="light" size="xs">
          Question
        </Badge>
        <ActionIcon
          ref={handle}
          disabled={busy}
          variant="subtle"
          color="gray"
          aria-label={"Drag card " + card.label}
          className="drag-handle"
        >
          <IconGripVertical size={18} />
        </ActionIcon>
      </Group>
      <UnstyledButton
        className="card-open"
        aria-label={"Open card " + card.label}
        disabled={busy}
        onClick={(event) =>
          event.shiftKey || event.ctrlKey || event.metaKey
            ? select(card.id, event.shiftKey)
            : edit()
        }
      >
        <MathJax dynamic>
          <Box
            className="card-thumbnail math-content"
            dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(html) }}
          />
        </MathJax>
      </UnstyledButton>
      <Group p="sm" gap={4} className="card-tags">
        {card.tags
          .split(",")
          .map((tag) => tag.trim())
          .filter(Boolean)
          .slice(0, 3)
          .map((tag) => (
            <Badge key={tag} size="xs" variant="outline" color="gray">
              {tag}
            </Badge>
          ))}
        {selected && group.length > 1 && (
          <Badge size="xs">{group.length} selected</Badge>
        )}
      </Group>
      {edge && <DropIndicator edge={edge} gap="16px" />}
    </Paper>
  );
}

export default function Organizer({
  workspace,
  decks,
  onChange,
  onEdit,
  initialDeck,
}: {
  workspace: string;
  decks: Summary[];
  onChange: () => Promise<void>;
  onEdit: (path: string, id: string) => void;
  initialDeck: string | null;
}) {
  const [active, setActive] = useState<Document | null>(null);
  const [preview, setPreview] = useState<Preview | null>(null);
  const [selected, setSelected] = useState<string[]>([]);
  const [filter, setFilter] = useState("");
  const [cardFilter, setCardFilter] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [undo, setUndo] = useState<Undo | null>(null);
  const [dialog, setDialog] = useState<Dialog>(null);
  const [destination, setDestination] = useState<string | null>(null);
  const [name, setName] = useState("");
  const [folder, setFolder] = useState("");
  const lastSelected = useRef<string | null>(null);
  const grid = useRef<HTMLDivElement>(null);
  const rail = useRef<HTMLDivElement>(null);
  const ranges = active ? cards(active.source) : [];
  const visibleDecks = decks.filter((deck) =>
    deck.path.toLowerCase().includes(filter.toLowerCase()),
  );

  async function loadDeck(path: string): Promise<Document> {
    const result = await request(
      { action: "load", workspace, path },
      documentSchema,
    );
    return { ...result, path, saved: result.source };
  }
  async function showDeck(path: string) {
    setBusy(true);
    setError("");
    setSelected([]);
    lastSelected.current = null;
    try {
      const document = await loadDeck(path);
      const rendered = await request(
        { action: "preview", workspace, path, source: document.source },
        previewSchema,
      );
      setActive(document);
      setPreview(rendered);
      setCardFilter("");
    } catch (failure) {
      setError(String(failure));
    } finally {
      setBusy(false);
    }
  }
  useEffect(() => {
    if (initialDeck) void showDeck(initialDeck);
  }, [initialDeck, workspace]);
  function openDialog(
    kind: NonNullable<Dialog>["kind"],
    path = active?.path ?? "",
  ) {
    setDialog({ kind, path });
    setDestination(null);
    setName("");
    setFolder(path.includes("/") ? path.split("/").slice(0, -1).join("/") : "");
  }
  function select(id: string, range: boolean) {
    if (range && lastSelected.current) {
      const a = ranges.findIndex((card) => card.id === lastSelected.current);
      const b = ranges.findIndex((card) => card.id === id);
      setSelected((current) => [
        ...new Set([
          ...current,
          ...ranges
            .slice(Math.min(a, b), Math.max(a, b) + 1)
            .map((card) => card.id),
        ]),
      ]);
    } else
      setSelected((current) =>
        current.includes(id)
          ? current.filter((value) => value !== id)
          : [...current, id],
      );
    lastSelected.current = id;
  }
  async function commit(
    changes: Change[],
    originals: Record<string, string | null>,
    label: string,
    focus: string | null,
    reversible = true,
  ) {
    const previousSelection = selected;
    setBusy(true);
    setError("");
    try {
      const result = await request(
        { action: "organize", workspace, changes },
        organizedSchema,
      );
      setUndo(
        reversible
          ? {
              changes: result.changed.map((deck) => ({
                path: deck.path,
                source: originals[deck.path],
                expected: deck.hash,
              })),
              focus: active?.path ?? null,
            }
          : null,
      );
      setNotice(label);
      announce(label);
      setSelected([]);
      setDialog(null);
      await onChange();
      if (focus) {
        const document = await loadDeck(focus);
        const rendered = await request(
          {
            action: "preview",
            workspace,
            path: focus,
            source: document.source,
          },
          previewSchema,
        );
        setActive(document);
        setPreview(rendered);
        setSelected(
          previousSelection.filter((id) =>
            cards(document.source).some((card) => card.id === id),
          ),
        );
      } else {
        setActive(null);
        setPreview(null);
      }
    } catch (failure) {
      setError(String(failure));
    } finally {
      setBusy(false);
    }
  }
  async function move(
    path: string,
    ids: string[],
    target: string,
    before?: string,
  ) {
    setBusy(true);
    try {
      const source = active?.path === path ? active : await loadDeck(path);
      if (path === target) {
        const remaining = cards(source.source)
          .map((card) => card.id)
          .filter((id) => !ids.includes(id));
        const chosen = cards(source.source)
          .map((card) => card.id)
          .filter((id) => ids.includes(id));
        remaining.splice(
          before ? remaining.indexOf(before) : remaining.length,
          0,
          ...chosen,
        );
        await commit(
          [
            {
              path,
              source: reorderCards(source.source, remaining),
              expected: source.hash,
            },
          ],
          { [path]: source.source },
          "Card order saved.",
          path,
        );
        return;
      }
      const receiver = await loadDeck(target);
      const result = transferCards(
        source.source,
        receiver.source,
        ids,
        before,
        {
          source: path,
          destination: target,
        },
      );
      await commit(
        [
          { path: target, source: result.destination, expected: receiver.hash },
          { path, source: result.source, expected: source.hash },
        ],
        { [path]: source.source, [target]: receiver.source },
        "Cards moved to " + deckName(target) + ".",
        path,
      );
    } finally {
      setBusy(false);
    }
  }
  function reorder(direction: "earlier" | "later") {
    if (!active || !selected.length) return;
    const order = ranges.map((card) => card.id);
    const positions = order
      .map((id, index) => (selected.includes(id) ? index : -1))
      .filter((index) => index >= 0);
    const remaining = order.filter((id) => !selected.includes(id));
    const neighbor =
      direction === "earlier"
        ? order[Math.min(...positions) - 1]
        : order[Math.max(...positions) + 1];
    if (!neighbor) return;
    const position =
      remaining.indexOf(neighbor) + (direction === "later" ? 1 : 0);
    const before = remaining[position];
    void move(active.path, selected, active.path, before).catch((failure) =>
      setError(String(failure)),
    );
  }
  async function submitDialog() {
    if (!dialog) return;
    setBusy(true);
    try {
      if (dialog.kind === "move") {
        if (!destination || !active) return;
        await move(active.path, selected, destination);
        return;
      }
      if (dialog.kind === "absorb") {
        if (!destination) return;
        const source = await loadDeck(dialog.path);
        const target = await loadDeck(destination);
        const ids = cards(source.source).map((card) => card.id);
        const moved = ids.length
          ? transferCards(source.source, target.source, ids, undefined, {
              source: dialog.path,
              destination,
            }).destination
          : target.source;
        await commit(
          [
            { path: destination, source: moved, expected: target.hash },
            { path: dialog.path, source: null, expected: source.hash },
          ],
          { [dialog.path]: source.source, [destination]: target.source },
          "Deck absorbed into " + deckName(destination) + ".",
          destination,
        );
        return;
      }
      if (!name.trim() || /[\\/]/.test(name))
        throw new Error("Enter a deck name without path separators.");
      const path =
        (folder.trim() ? folder.trim() + "/" : "") + name.trim() + ".md";
      const empty =
        "---\ntitle: " +
        JSON.stringify(path.replace(/\.md$/, "").replace(/\//g, "::")) +
        "\n---\n\n";
      if (dialog.kind === "new") {
        await commit(
          [{ path, source: empty, expected: null }],
          { [path]: null },
          "Deck created.",
          path,
        );
        return;
      }
      if (!active) return;
      const moved = transferCards(active.source, empty, selected, undefined, {
        source: active.path,
        destination: path,
      });
      await commit(
        [
          { path, source: moved.destination, expected: null },
          { path: active.path, source: moved.source, expected: active.hash },
        ],
        { [path]: null, [active.path]: active.source },
        "Selection split into " + name.trim() + ".",
        path,
      );
    } catch (failure) {
      setError(String(failure));
    } finally {
      setBusy(false);
    }
  }
  async function drop(event: ElementEventPayloadMap["onDrop"]) {
    const target = event.location.current.dropTargets[0];
    if (!target) return;
    try {
      const data = dragSchema.parse(event.source.data);
      const receiver = targetSchema.parse(target.data);
      if (data.kind === "deck") {
        openDialog("absorb", data.path);
        setDestination(receiver.path);
        return;
      }
      let before = receiver.card;
      if (
        before &&
        ["bottom", "right"].includes(extractClosestEdge(target.data) ?? "")
      ) {
        const document =
          active?.path === receiver.path
            ? active
            : await loadDeck(receiver.path);
        const order = cards(document.source)
          .map((card) => card.id)
          .filter((id) => !data.ids.includes(id));
        before = order[order.indexOf(before) + 1];
      }
      await move(data.path, data.ids, receiver.path, before);
    } catch (failure) {
      setError(String(failure));
    }
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
            void dropHandler.current(event);
          },
        }),
        autoScrollWindowForElements(),
      ),
    [workspace],
  );
  useEffect(() => {
    if (!grid.current || !active) return;
    return dropTargetForElements({
      element: grid.current,
      canDrop: ({ source }) =>
        !busy && dragSchema.parse(source.data).kind === "cards",
      getData: () => ({ path: active.path }),
    });
  }, [active?.path, busy]);
  useEffect(() => {
    if (rail.current) return autoScrollForElements({ element: rail.current });
  }, [active?.path]);

  const modalTitle = dialog
    ? {
        new: "New deck",
        split: "New deck from selection",
        move: "Move cards",
        absorb: "Absorb deck",
      }[dialog.kind]
    : "";
  return (
    <Stack gap="md" className="organizer">
      <Group justify="space-between">
        <Breadcrumbs>
          <Button
            variant="subtle"
            onClick={() => {
              setActive(null);
              setPreview(null);
              setSelected([]);
            }}
          >
            Decks
          </Button>
          {active && (
            <Text fw={650}>{preview?.title ?? deckName(active.path)}</Text>
          )}
        </Breadcrumbs>
        <Group>
          {busy && <Loader size="sm" aria-label="Organizing" />}
          <Button
            leftSection={<IconPlus size={16} />}
            disabled={busy || !workspace}
            onClick={() => openDialog("new")}
          >
            New deck
          </Button>
        </Group>
      </Group>
      {error && !dialog && (
        <Alert
          color="red"
          title="Organization failed"
          withCloseButton
          onClose={() => setError("")}
        >
          {error}
        </Alert>
      )}
      {notice && (
        <Alert color="teal">
          <Group justify="space-between">
            <Text size="sm" role="status">
              {notice}
            </Text>
            {undo && (
              <Button
                variant="subtle"
                size="compact-sm"
                leftSection={<IconArrowBackUp size={16} />}
                disabled={busy}
                onClick={() => {
                  const originals = Object.fromEntries(
                    undo.changes.map((change) => [change.path, change.source]),
                  );
                  void commit(
                    undo.changes,
                    originals,
                    "Undo complete.",
                    undo.focus,
                    false,
                  );
                }}
              >
                Undo
              </Button>
            )}
          </Group>
        </Alert>
      )}
      <TextInput
        aria-label="Find decks to organize"
        placeholder="Find a deck…"
        value={filter}
        onChange={(event) => setFilter(event.currentTarget.value)}
      />
      {!active ? (
        <div className="deck-gallery">
          {visibleDecks.map((deck) => (
            <DeckTile
              key={deck.path}
              deck={deck}
              disabled={busy}
              open={() => {
                void showDeck(deck.path);
              }}
              absorb={() => openDialog("absorb", deck.path)}
            />
          ))}
          {decks.length === 0 && (
            <Paper withBorder p="xl">
              <Text>Create a deck to start collecting cards.</Text>
            </Paper>
          )}
        </div>
      ) : (
        <div className="organizer-layout">
          <Paper withBorder p="sm" className="deck-rail">
            <Text fw={650} size="sm" mb="sm">
              Move to a deck
            </Text>
            <Box ref={rail} className="deck-scroll">
              <Stack gap="sm">
                {visibleDecks.map((deck) => (
                  <DeckTile
                    key={deck.path}
                    deck={deck}
                    compact
                    disabled={busy}
                    open={() => {
                      void showDeck(deck.path);
                    }}
                    absorb={() => openDialog("absorb", deck.path)}
                  />
                ))}
              </Stack>
            </Box>
          </Paper>
          <Stack gap="md" className="card-board">
            <Paper withBorder p="md">
              <Group justify="space-between">
                <Group>
                  <Title order={2} size="h4">
                    Cards
                  </Title>
                  <Badge variant="light">{ranges.length}</Badge>
                  {selected.length > 0 && (
                    <Badge>{selected.length} selected</Badge>
                  )}
                </Group>
                <Group gap="xs">
                  <Button
                    size="compact-sm"
                    variant="default"
                    disabled={busy || !ranges.length}
                    onClick={() => setSelected(ranges.map((card) => card.id))}
                  >
                    Select all
                  </Button>
                  <Button
                    size="compact-sm"
                    variant="subtle"
                    disabled={!selected.length || busy}
                    onClick={() => setSelected([])}
                  >
                    Clear selection
                  </Button>
                  <Menu>
                    <Menu.Target>
                      <Button variant="default" size="compact-sm">
                        Deck actions
                      </Button>
                    </Menu.Target>
                    <Menu.Dropdown>
                      <Menu.Item
                        disabled={busy}
                        onClick={() => openDialog("absorb")}
                      >
                        Absorb into another deck
                      </Menu.Item>
                    </Menu.Dropdown>
                  </Menu>
                </Group>
              </Group>
              <Group mt="sm" gap="xs">
                <Button
                  variant="light"
                  leftSection={<IconTransfer size={16} />}
                  disabled={!selected.length || busy}
                  onClick={() => openDialog("move")}
                >
                  Move to deck
                </Button>
                <Button
                  variant="light"
                  leftSection={<IconScissors size={16} />}
                  disabled={!selected.length || busy}
                  onClick={() => openDialog("split")}
                >
                  Split into new deck
                </Button>
                <ActionIcon
                  size="lg"
                  variant="default"
                  aria-label="Move selected cards earlier"
                  disabled={!selected.length || busy}
                  onClick={() => reorder("earlier")}
                >
                  <IconArrowUp size={18} />
                </ActionIcon>
                <ActionIcon
                  size="lg"
                  variant="default"
                  aria-label="Move selected cards later"
                  disabled={!selected.length || busy}
                  onClick={() => reorder("later")}
                >
                  <IconArrowDown size={18} />
                </ActionIcon>
              </Group>
              <TextInput
                mt="sm"
                aria-label="Find cards to organize"
                placeholder="Find a card…"
                value={cardFilter}
                onChange={(event) => setCardFilter(event.currentTarget.value)}
              />
              <Text size="xs" c="dimmed" mt="xs">
                Open a card to edit. Drag handles to rearrange or move. Use
                checkboxes to select a group.
              </Text>
            </Paper>
            {preview && (
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
                <div
                  ref={grid}
                  className="card-gallery"
                  data-card-deck={active.path}
                >
                  {ranges.map(
                    (card, index) =>
                      card.label
                        .toLowerCase()
                        .includes(cardFilter.toLowerCase()) && (
                        <CardTile
                          key={card.id}
                          card={card}
                          path={active.path}
                          html={preview.cards[index].front}
                          selected={selected.includes(card.id)}
                          group={selected}
                          busy={busy}
                          select={select}
                          edit={() => onEdit(active.path, card.id)}
                        />
                      ),
                  )}
                  {ranges.length === 0 && (
                    <Paper p="xl" withBorder className="empty-deck">
                      <IconCards size={36} />
                      <Title order={3} size="h5" mt="sm">
                        This deck is empty
                      </Title>
                      <Text c="dimmed" size="sm" mt="xs">
                        Drop cards here, or open the editor to add a card.
                      </Text>
                      <Button
                        mt="md"
                        variant="light"
                        onClick={() => onEdit(active.path, "")}
                      >
                        Add a card
                      </Button>
                    </Paper>
                  )}
                </div>
              </MathJaxContext>
            )}
          </Stack>
        </div>
      )}
      <Modal
        opened={dialog !== null}
        onClose={() => !busy && setDialog(null)}
        title={modalTitle}
        centered
      >
        <Stack>
          {error && (
            <Alert color="red" title="Organization failed">
              {error}
            </Alert>
          )}
          {dialog && ["new", "split"].includes(dialog.kind) ? (
            <>
              <TextInput
                label="Deck name"
                disabled={busy}
                value={name}
                onChange={(event) => setName(event.currentTarget.value)}
                autoFocus
              />
              <TextInput
                label="Folder"
                disabled={busy}
                description="Optional subject folder"
                value={folder}
                onChange={(event) => setFolder(event.currentTarget.value)}
              />
            </>
          ) : (
            <>
              <Text size="sm">
                {dialog?.kind === "absorb"
                  ? "Move every card from " +
                    deckName(dialog.path) +
                    " into the chosen deck. The source deck goes to the desktop trash."
                  : "Move the selected cards into another deck."}
              </Text>
              <Select
                label="Destination deck"
                disabled={busy}
                searchable
                value={destination}
                onChange={setDestination}
                data={decks
                  .filter((deck) => deck.path !== dialog?.path)
                  .map((deck) => ({
                    value: deck.path,
                    label: deck.path.replace(/\.md$/, "").replace(/\//g, " / "),
                  }))}
              />
            </>
          )}
          <Group justify="end">
            <Button
              variant="default"
              disabled={busy}
              onClick={() => setDialog(null)}
            >
              Cancel
            </Button>
            <Button
              loading={busy}
              onClick={() => {
                void submitDialog();
              }}
              disabled={
                dialog?.kind === "new" || dialog?.kind === "split"
                  ? !name.trim()
                  : !destination
              }
            >
              {dialog?.kind === "absorb"
                ? "Absorb deck"
                : dialog?.kind === "move"
                  ? "Move cards"
                  : "Create deck"}
            </Button>
          </Group>
        </Stack>
      </Modal>
    </Stack>
  );
}
