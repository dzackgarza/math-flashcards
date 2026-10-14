import {
  useEffect,
  useRef,
  useState,
  type HTMLAttributes,
  type MouseEvent,
  type ReactNode,
} from "react";
import { Button, Stack, TextInput, UnstyledButton } from "@mantine/core";
import { useForm } from "@mantine/form";
import {
  draggable,
  dropTargetForElements,
} from "@atlaskit/pragmatic-drag-and-drop/element/adapter";
import { combine } from "@atlaskit/pragmatic-drag-and-drop/combine";
import { attachClosestEdge } from "@atlaskit/pragmatic-drag-and-drop-hitbox/closest-edge/attach-closest-edge";
import { extractClosestEdge } from "@atlaskit/pragmatic-drag-and-drop-hitbox/closest-edge/extract-closest-edge";
import type { Edge } from "@atlaskit/pragmatic-drag-and-drop-hitbox/types";
import DropIndicator from "@atlaskit/pragmatic-drag-and-drop-react-drop-indicator/box";
import { z } from "zod";

export const dragSchema = z.discriminatedUnion("kind", [
  z.object({
    kind: z.literal("cards"),
    path: z.string(),
    ids: z.array(z.string()),
  }),
  z.object({ kind: z.literal("deck"), path: z.string() }),
]);
export const targetSchema = z.discriminatedUnion("kind", [
  z.object({ kind: z.literal("deck"), path: z.string() }),
  z.object({ kind: z.literal("folder") }),
  z.object({ kind: z.literal("card"), path: z.string(), card: z.string() }),
]);

export const deckName = (path: string) =>
  path.split("/").slice(-1)[0].replace(/\.md$/, "");

// Atlassian's drop-target pattern: https://atlassian.design/components/pragmatic-drag-and-drop/design-guidelines/
// Deck rows take dragged decks and cards; folder rows expand while a drag hovers.
export function TreeRow({
  path,
  folder,
  disabled,
  expand,
  children,
  ...props
}: {
  path: string;
  folder: boolean;
  disabled: boolean;
  expand: () => void;
  children: ReactNode;
} & HTMLAttributes<HTMLDivElement>) {
  const element = useRef<HTMLDivElement>(null);
  const [over, setOver] = useState(false);
  const [dragging, setDragging] = useState(false);
  useEffect(() => {
    if (!element.current) return;
    if (folder)
      return dropTargetForElements({
        element: element.current,
        getData: () => ({ kind: "folder" }),
        onDragEnter: expand,
      });
    return combine(
      draggable({
        element: element.current,
        canDrag: () => !disabled,
        getInitialData: () => ({ kind: "deck", path }),
        onDragStart: () => setDragging(true),
        onDrop: () => setDragging(false),
      }),
      dropTargetForElements({
        element: element.current,
        canDrop: ({ source }) =>
          !disabled && dragSchema.parse(source.data).path !== path,
        getData: () => ({ kind: "deck", path }),
        onDragEnter: () => setOver(true),
        onDragLeave: () => setOver(false),
        onDrop: () => setOver(false),
      }),
    );
  }, [path, folder, disabled]);
  return (
    <div
      {...props}
      ref={element}
      data-deck={folder ? undefined : path}
      className={
        props.className +
        " tree-row" +
        (over ? " drop-active" : "") +
        (dragging ? " dragging" : "")
      }
    >
      {children}
    </div>
  );
}

// Dragging a selected card carries the whole selection.
export function CardRow({
  id,
  path,
  label,
  preview,
  active,
  selected,
  group,
  disabled,
  choose,
}: {
  id: string;
  path: string;
  label: string;
  preview: { front: string; back: string } | null;
  active: boolean;
  selected: boolean;
  group: string[];
  disabled: boolean;
  choose: (event: MouseEvent) => void;
}) {
  const element = useRef<HTMLDivElement>(null);
  const [edge, setEdge] = useState<Edge | null>(null);
  const [dragging, setDragging] = useState(false);
  const ids = selected ? group : [id];
  useEffect(() => {
    if (!element.current) return;
    return combine(
      draggable({
        element: element.current,
        canDrag: () => !disabled,
        getInitialData: () => ({ kind: "cards", path, ids }),
        onDragStart: () => setDragging(true),
        onDrop: () => setDragging(false),
      }),
      dropTargetForElements({
        element: element.current,
        canDrop: ({ source }) => {
          const data = dragSchema.parse(source.data);
          return !disabled && data.kind === "cards" && !data.ids.includes(id);
        },
        getData: ({ input, element }) =>
          attachClosestEdge(
            { kind: "card", path, card: id },
            { input, element, allowedEdges: ["top", "bottom"] },
          ),
        onDrag: ({ self }) => setEdge(extractClosestEdge(self.data)),
        onDragLeave: () => setEdge(null),
        onDrop: () => setEdge(null),
      }),
    );
  }, [path, id, ids.join("|"), disabled]);
  return (
    <div
      ref={element}
      data-card={id}
      className={
        "card-row" +
        (active ? " active" : "") +
        (selected ? " selected" : "") +
        (dragging ? " dragging" : "")
      }
    >
      <UnstyledButton
        className="card-row-label"
        aria-label={label}
        aria-pressed={selected}
        onClick={choose}
      >
        {preview ? (
          <>
            <span
              className="card-row-front"
              dangerouslySetInnerHTML={{ __html: preview.front }}
            />
            <span
              className="card-row-back"
              dangerouslySetInnerHTML={{ __html: preview.back }}
            />
          </>
        ) : (
          <span className="card-row-front">{label}</span>
        )}
      </UnstyledButton>
      {edge && <DropIndicator edge={edge} gap="4px" />}
    </div>
  );
}

export function NewDeckForm({
  folder,
  submit,
}: {
  folder: string;
  submit: (path: string) => void;
}) {
  const form = useForm({
    initialValues: { name: "", folder },
    validate: {
      name: (value) =>
        !value.trim()
          ? "Enter a deck name."
          : /[\\/]/.test(value)
            ? "Enter a deck name without path separators."
            : null,
    },
  });
  return (
    <form
      onSubmit={form.onSubmit((values) =>
        submit(
          (values.folder.trim() ? values.folder.trim() + "/" : "") +
            values.name.trim() +
            ".md",
        ),
      )}
    >
      <Stack>
        <TextInput
          label="Deck name"
          data-autofocus
          {...form.getInputProps("name")}
        />
        <TextInput
          label="Folder"
          description="Optional subject folder"
          {...form.getInputProps("folder")}
        />
        <Button type="submit">Create deck</Button>
      </Stack>
    </form>
  );
}
