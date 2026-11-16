import { useCallback, useEffect, useRef, useState } from "react";
import { z } from "zod";
import { parseDocument } from "yaml";
import { decodeString } from "micromark-util-decode-string";
import { basename } from "pathe";
import { cards, deckParser } from "./cards";
import {
  request,
  studyOpenSchema,
  syncResultSchema,
  manifestSchema,
  sourcesSchema,
  type StudyOpen,
  type StudyDeck,
  type SourceResult,
  type Entry,
} from "./bridge";

const metadataSchema = z.object({
  title: z.string().optional(),
  tags: z.union([z.string(), z.array(z.string())]).default([]),
});

// Lezer owns Markdown syntax; YAML and micromark decode its metadata and URLs.
// https://eemeli.org/yaml/#parsing-documents
// https://github.com/micromark/micromark/tree/main/packages/micromark-util-decode-string
function nativeDeck(
  source: Extract<SourceResult, { state: "ready" }>,
): StudyDeck {
  const tree = deckParser.parse(source.source);
  let title = basename(source.path, ".md");
  const tags: string[] = [];
  const references = new Map<string, string>();
  const images: { from: number; url: string | null; label: string }[] = [];
  const label = (value: string) =>
    decodeString(value).trim().replace(/\s+/g, " ").toUpperCase();
  const url = (value: string) =>
    decodeString(value.startsWith("<") ? value.slice(1, -1) : value);
  tree.iterate({
    enter(ref) {
      const node = ref.node;
      if (node.name === "YAMLFrontmatter") {
        const body = node.getChild("CodeText");
        if (!body) return;
        const parsed = parseDocument(source.source.slice(body.from, body.to));
        if (parsed.errors.length) throw parsed.errors[0];
        const metadata = metadataSchema.parse(parsed.toJS());
        if (metadata.title !== undefined) title = metadata.title;
        tags.push(
          ...(typeof metadata.tags === "string"
            ? metadata.tags.split(/\s+/).filter(Boolean)
            : metadata.tags),
        );
      }
      if (node.name === "LinkReference") {
        const name = node.getChild("LinkLabel");
        const target = node.getChild("URL");
        if (name && target)
          references.set(
            label(source.source.slice(name.from + 1, name.to - 1)),
            url(source.source.slice(target.from, target.to)),
          );
      }
      if (node.name === "Image") {
        const target = node.getChild("URL");
        const reference = node.getChild("LinkLabel");
        const marks = node.getChildren("LinkMark");
        const name =
          reference && reference.to > reference.from + 2
            ? source.source.slice(reference.from + 1, reference.to - 1)
            : source.source.slice(marks[0].to, marks[1].from);
        images.push({
          from: node.from,
          url: target ? url(source.source.slice(target.from, target.to)) : null,
          label: label(name),
        });
      }
    },
  });
  return {
    path: source.path,
    source_hash: source.revision,
    title,
    tags,
    cards: cards(source.source).map((card) => ({
      id: card.id,
      front: card.front.value,
      back: card.back.value,
      tags: card.tags.split(/\s+/).filter(Boolean),
      media: [
        ...new Set(
          images
            .filter(
              (image) =>
                (image.from >= card.front.contentFrom &&
                  image.from < card.front.contentTo) ||
                (image.from >= card.back.contentFrom &&
                  image.from < card.back.contentTo),
            )
            .map((image) => {
              const resolved = image.url ?? references.get(image.label);
              if (resolved === undefined)
                throw new Error(`Unresolved image reference: ${image.label}`);
              return resolved;
            }),
        ),
      ],
    })),
  };
}

// A session starts from disk after the editor has saved. Background preparation
// may still be publishing its final React state when the user selects Study.
export async function syncSavedStudy(
  workspace: string,
  assets: string,
  generation: number,
) {
  const manifest = await request(
    { action: "manifest", workspace, generation },
    manifestSchema,
  );
  const paths = manifest.entries.map((entry) => entry.path);
  for (let offset = 0; offset < paths.length; offset += 8) {
    const batch = await request(
      {
        action: "sources",
        workspace,
        generation,
        paths: paths.slice(offset, offset + 8),
      },
      sourcesSchema,
    );
    const decks = batch.results.map((source) => {
      if (source.state === "failed") throw new Error(source.message);
      return nativeDeck(source);
    });
    const synced = await request(
      { action: "study-sync", workspace, assets, paths, decks },
      syncResultSchema,
    );
    if (synced.failed.length || synced.duplicates.length)
      throw new Error(
        [
          ...synced.failed.map((item) => `${item.path}: ${item.message}`),
          ...synced.duplicates.map(
            (item) =>
              `Duplicate card ${item.card_id}: ${item.paths.join(", ")}`,
          ),
        ].join("\n"),
      );
    if (offset + 8 >= paths.length && synced.pending)
      throw new Error(
        "The workspace changed while preparing Study. Start Study again to load the saved cards.",
      );
  }
}

export function useStudySync(
  workspace: string,
  entries: Entry[],
  sources: Map<string, SourceResult>,
  assets: string,
  reportError: (message: string) => void,
) {
  const [status, setStatus] = useState("Preparing study cards");
  useEffect(() => {
    if (!workspace || !assets) return;
    let cancelled = false;
    setStatus("Preparing study cards");
    async function prepare() {
      const opened = await request(
        { action: "study-open", workspace },
        studyOpenSchema,
      );
      if (cancelled) return;
      if (opened.state === "Unattached") {
        setStatus("Choose a study store");
        return;
      }
      const paths = entries.map((entry) => entry.path);
      const decks = paths.flatMap((path) => {
        const source = sources.get(path);
        if (source === undefined) return [];
        if (source.state === "failed") throw new Error(source.message);
        return [nativeDeck(source)];
      });
      let pending = paths.length;
      for (let offset = 0; offset < decks.length; offset += 8) {
        if (cancelled) return;
        const result = await request(
          {
            action: "study-sync",
            workspace,
            assets,
            decks: decks.slice(offset, offset + 8),
            paths,
          },
          syncResultSchema,
        );
        if (result.failed.length)
          throw new Error(
            result.failed
              .map((item) => `${item.path}: ${item.message}`)
              .join("\n"),
          );
        if (result.duplicates.length)
          throw new Error(
            result.duplicates
              .map(
                (item) =>
                  `Duplicate card ${item.card_id}: ${item.paths.join(", ")}`,
              )
              .join("\n"),
          );
        pending = result.pending;
      }
      if (!cancelled && pending === 0) setStatus("Study cards ready");
    }
    void prepare().catch((failure) => {
      if (cancelled) return;
      setStatus("Study preparation failed");
      reportError(String(failure));
    });
    return () => {
      cancelled = true;
    };
  }, [workspace, entries, sources, assets, reportError]);
  return status;
}

// React effect cleanup closes the previous view before the next one starts:
// https://react.dev/reference/react/useEffect
export function useEditorViews(
  workspace: string,
  deck: string | null,
  cardId: string | null,
  reportError: (message: string) => void,
) {
  const opening = useRef<Promise<StudyOpen> | null>(null);
  const writing = useRef<Promise<void>>(Promise.resolve());
  const finish = useRef<(() => void) | null>(null);

  useEffect(() => {
    opening.current = workspace
      ? request({ action: "study-open", workspace }, studyOpenSchema)
      : null;
    void opening.current?.catch((failure) => reportError(String(failure)));
  }, [workspace, reportError]);

  useEffect(() => {
    const ready = opening.current;
    if (!workspace || !deck || !cardId || !ready) return;
    // Monotonic duration, independent of wall-clock changes:
    // https://developer.mozilla.org/en-US/docs/Web/API/Performance/now
    const started = performance.now();
    let unfocused = 0;
    let away = document.hidden || !document.hasFocus() ? started : null;
    const focus = (event: Event) => {
      // Event timestamps share performance.now()'s origin and precede slow
      // listeners. Measure the transition, not when its handler gets CPU time.
      // https://developer.mozilla.org/en-US/docs/Web/API/Event/timeStamp
      const now = Math.max(started, event.timeStamp);
      if (document.hidden || !document.hasFocus()) {
        away ??= now;
      } else if (away !== null) {
        unfocused += now - away;
        away = null;
      }
    };
    window.addEventListener("focus", focus);
    window.addEventListener("blur", focus);
    document.addEventListener("visibilitychange", focus);
    let ended = false;
    const end = () => {
      if (ended) return;
      ended = true;
      window.removeEventListener("focus", focus);
      window.removeEventListener("blur", focus);
      document.removeEventListener("visibilitychange", focus);
      const now = performance.now();
      if (away !== null) unfocused += now - away;
      const shown_ms = Math.round(now - started);
      const unfocused_ms = Math.round(unfocused);
      writing.current = writing.current.then(async () => {
        if ((await ready).state === "Unattached") return;
        await request(
          {
            action: "study-viewed",
            workspace,
            deck,
            card_id: cardId,
            shown_ms,
            unfocused_ms,
          },
          z.strictObject({}),
        );
      });
      void writing.current.catch((failure) => reportError(String(failure)));
    };
    finish.current = end;
    return end;
  }, [workspace, deck, cardId, reportError]);

  return useCallback(() => {
    finish.current?.();
    return writing.current;
  }, []);
}
