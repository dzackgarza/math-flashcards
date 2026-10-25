import { useEffect, useRef, useState } from "react";
import { cards } from "./cards";
import { request, searchCacheSchema, type SearchCard } from "./bridge";

interface SearchSource {
  path: string;
  source: string;
  revision: string;
}

interface CheckedSearch {
  root: string;
  source: string;
  epoch: number;
  cards: SearchCard[];
  error: string;
}

export function useSearch(
  decks: SearchSource[],
  root: string,
  generation: number,
  epoch: number,
) {
  const checked = useRef(new Map<string, CheckedSearch>());
  const [, publish] = useState(0);
  const [failure, setFailure] = useState<{
    root: string;
    message: string;
    cacheFailure: boolean;
    epoch: number;
  } | null>(null);
  const current = (deck: SearchSource) => {
    const record = checked.current.get(deck.path);
    return record?.root === root &&
      record.source === deck.source &&
      record.epoch === epoch
      ? record
      : undefined;
  };
  useEffect(() => {
    if (!root) return;
    let cancelled = false;
    setFailure((previous) =>
      previous?.root === root &&
      previous.epoch === epoch &&
      previous.cacheFailure
        ? previous
        : null,
    );
    const paths = new Set(decks.map((deck) => deck.path));
    for (const [path, record] of checked.current)
      if (record.root !== root || !paths.has(path))
        checked.current.delete(path);
    const run = async () => {
      const pending = decks.filter((deck) => !current(deck));
      for (let offset = 0; offset < pending.length; offset += 8) {
        if (cancelled) return;
        const batch = pending.slice(offset, offset + 8);
        const input = {
          workspace: root,
          generation,
          producer: __PARSER_IDENTITY__,
        };
        const cached = await request(
          {
            ...input,
            action: "search",
            entries: batch.map(({ path, revision }) => ({ path, revision })),
          },
          searchCacheSchema,
        );
        if (cancelled) return;
        if (
          cached.session.root !== root ||
          cached.session.generation !== generation
        )
          throw new Error(
            "The search response belongs to another workspace session.",
          );
        for (const deck of batch) {
          if (cancelled) return;
          const result = cached.results.find(
            (result) => result.path === deck.path,
          );
          if (!result)
            throw new Error("The search response is missing a requested deck.");
          if (result.state === "superseded") continue;
          if (result.state === "ready") {
            if (
              result.revision !== deck.revision ||
              result.producer !== __PARSER_IDENTITY__ ||
              result.source !== deck.source
            )
              throw new Error(
                "The saved search data belongs to another source revision.",
              );
            checked.current.set(deck.path, {
              root,
              source: deck.source,
              epoch,
              cards: result.cards,
              error: "",
            });
            publish((value) => value + 1);
            continue;
          }
          if (result.state === "failed") {
            if (result.kind !== "CacheFailure") {
              checked.current.set(deck.path, {
                root,
                source: deck.source,
                epoch,
                cards: [],
                error: result.message,
              });
              publish((value) => value + 1);
              continue;
            }
            setFailure({
              root,
              epoch,
              message: result.message,
              cacheFailure: true,
            });
          }
          let summaries: SearchCard[];
          try {
            summaries = cards(deck.source).map((card) => ({
              id: card.id,
              label: card.label,
              front: card.front.value,
              back: card.back.value,
              tags: card.tags,
            }));
          } catch (error) {
            checked.current.set(deck.path, {
              root,
              source: deck.source,
              epoch,
              cards: [],
              error: String(error),
            });
            publish((value) => value + 1);
            continue;
          }
          const stored = await request(
            {
              ...input,
              action: "store-search",
              entries: [
                { path: deck.path, revision: deck.revision, cards: summaries },
              ],
            },
            searchCacheSchema,
          );
          if (cancelled) return;
          if (
            stored.session.root !== root ||
            stored.session.generation !== generation
          )
            throw new Error(
              "The saved search response belongs to another workspace session.",
            );
          const state = stored.results[0];
          if (!state)
            throw new Error("The saved search response is missing its deck.");
          if (state.state === "superseded") continue;
          if (state.state === "pending")
            throw new Error("The search cache did not publish its result.");
          if (
            state.state === "ready" &&
            (state.path !== deck.path ||
              state.revision !== deck.revision ||
              state.producer !== __PARSER_IDENTITY__ ||
              state.source !== deck.source)
          )
            throw new Error(
              "The saved search result belongs to another source revision.",
            );
          if (state.state === "failed") {
            if (state.kind !== "CacheFailure") {
              checked.current.set(deck.path, {
                root,
                source: deck.source,
                epoch,
                cards: [],
                error: state.message,
              });
              publish((value) => value + 1);
              continue;
            }
            setFailure({
              root,
              epoch,
              message: state.message,
              cacheFailure: true,
            });
          }
          checked.current.set(deck.path, {
            root,
            source: deck.source,
            epoch,
            cards: summaries,
            error: "",
          });
          publish((value) => value + 1);
          // Yield between decks, as in the existing Problems scheduler.
          await new Promise<void>((resolve) => setTimeout(resolve, 0));
        }
      }
    };
    run().catch((error) => {
      if (!cancelled)
        setFailure({
          root,
          epoch,
          message: String(error),
          cacheFailure: false,
        });
    });
    return () => {
      cancelled = true;
    };
  }, [decks, root, generation, epoch]);
  const index = new Map<string, SearchCard[]>();
  const invalid = new Set<string>();
  for (const deck of decks) {
    const record = current(deck);
    if (!record) continue;
    if (record.error) invalid.add(deck.path);
    else index.set(deck.path, record.cards);
  }
  return {
    index,
    invalid,
    error: failure?.root === root ? failure.message : "",
    cacheFailure: failure?.root === root && failure.cacheFailure,
  };
}
