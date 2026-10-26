import { invoke, isTauri } from "@tauri-apps/api/core";
import { watch } from "@tauri-apps/plugin-fs";
import { z } from "zod";

const generationSchema = z.number().int().nonnegative();
export const digestSchema = z.string().regex(/^[a-f0-9]{64}$/);
export const deckPathSchema = z
  .string()
  .refine(
    (path) =>
      path.endsWith(".md") &&
      !path.startsWith("/") &&
      !path.includes("\\") &&
      path
        .split("/")
        .every((part) => part !== ".." && part !== "." && part !== "") &&
      path.split("/")[0] !== "apkg",
    "Use a relative Markdown deck path outside apkg/.",
  );
export const sessionSchema = z.object({
  root: z.string().startsWith("/"),
  generation: generationSchema,
});
const batchSchema = z.object({
  workspace: z.string(),
  generation: generationSchema,
  paths: z.array(deckPathSchema).min(1).max(8),
});
export const discoveryRequestSchema = z.discriminatedUnion("action", [
  z.object({
    action: z.literal("manifest"),
    workspace: z.string(),
    generation: generationSchema,
  }),
  batchSchema.extend({ action: z.literal("sources") }),
  batchSchema.extend({ action: z.literal("checks"), assets: digestSchema }),
  batchSchema.extend({
    action: z.literal("cached-checks"),
    assets: digestSchema,
  }),
]);
export const manifestSchema = z.object({
  session: sessionSchema,
  entries: z.array(z.object({ path: deckPathSchema })),
});
export const manifestCacheRequestSchema = z.object({
  action: z.enum(["cached-manifest", "cache-manifest"]),
  workspace: z.string(),
  generation: generationSchema,
});
export const cachedManifestSchema = z.discriminatedUnion("state", [
  manifestSchema.extend({ state: z.literal("cached") }),
  z.object({ session: sessionSchema, state: z.literal("pending") }),
  z.object({
    session: sessionSchema,
    state: z.literal("failed"),
    kind: z.literal("CacheFailure"),
    message: z.string(),
  }),
]);
export const sourceSchema = z.object({
  path: deckPathSchema,
  source: z.string(),
  revision: digestSchema,
});
const pathFailureSchema = z.object({
  state: z.literal("failed"),
  path: deckPathSchema,
  kind: z.enum([
    "UnreadablePath",
    "InvalidDeck",
    "InvalidAssets",
    "BackendFailure",
    "CacheFailure",
  ]),
  message: z.string(),
});
export type CheckErrorKind = z.infer<typeof pathFailureSchema>["kind"];
export const sourcesSchema = z.object({
  session: sessionSchema,
  results: z.array(
    z.discriminatedUnion("state", [
      sourceSchema.extend({ state: z.literal("ready") }),
      pathFailureSchema,
    ]),
  ),
});

export const packageOperationRequestSchema = z.discriminatedUnion("action", [
  z.object({
    action: z.literal("generate"),
    workspace: z.string(),
    path: deckPathSchema,
    assets: digestSchema,
  }),
  z.object({
    action: z.literal("review"),
    workspace: z.string(),
    assets: digestSchema,
  }),
]);

export type Request =
  | z.infer<typeof packageOperationRequestSchema>
  | z.infer<typeof discoveryRequestSchema>
  | z.infer<typeof problemCacheRequestSchema>
  | z.infer<typeof manifestCacheRequestSchema>
  | z.infer<typeof searchCacheRequestSchema>
  | { action: "assets" | "asset-version" }
  | { action: "rebuild-cache"; workspace: string; generation: number }
  | { action: "list"; workspace: string }
  | {
      action: "load" | "validate";
      workspace: string;
      path: string;
      generation: number;
    }
  | { action: "organize"; workspace: string; changes: Change[] }
  | {
      action: "save";
      workspace: string;
      path: string;
      source: string;
      expected: string;
      generation: number;
    };

export interface Change {
  path: string;
  source: string | null;
  expected: string | null;
}

export const organizedSchema = z.object({
  changed: z.array(z.object({ path: z.string(), hash: z.string().nullable() })),
});

export const statusSchema = z.enum(["Up to date", "Unsynced", "Empty"]);
export const packageResultSchema = z.object({
  path: deckPathSchema,
  assets: digestSchema,
  revision: digestSchema,
  input_identity: digestSchema,
  checked_at: z.string().datetime({ offset: true }),
  dependencies: z.array(z.string().startsWith("/")),
  status: statusSchema,
  reasons: z.array(z.string()),
  built: z.string().nullable(),
});
const readyPackageSchema = packageResultSchema.extend({
  state: z.literal("ready"),
});
const pendingPackageSchema = z.object({
  state: z.enum(["pending", "checking"]),
  path: deckPathSchema,
  previous: readyPackageSchema.nullable(),
});
const failedPackageSchema = pathFailureSchema.extend({
  previous: readyPackageSchema.nullable(),
});
export const packageCheckSchema = z.discriminatedUnion("state", [
  readyPackageSchema,
  pendingPackageSchema,
  failedPackageSchema,
]);
export type PackageCheck = z.infer<typeof packageCheckSchema>;
export const cachedChecksSchema = z.object({
  session: sessionSchema,
  results: z.array(
    z.discriminatedUnion("state", [
      pendingPackageSchema.extend({ state: z.literal("pending") }),
      failedPackageSchema,
    ]),
  ),
});
export const checksSchema = z.object({
  session: sessionSchema,
  cache_errors: z.array(pathFailureSchema),
  results: z.array(
    z.discriminatedUnion("state", [readyPackageSchema, pathFailureSchema]),
  ),
});
export const problemSchema = z.object({
  path: deckPathSchema,
  card: z.string().nullable(),
  label: z.string().nullable(),
  side: z.enum(["front", "back"]).nullable(),
  kind: z.enum(["LaTeX", "Card structure", "Empty answer"]),
  message: z.string(),
  source: z.string().nullable(),
});
const problemKeySchema = z.object({
  path: deckPathSchema,
  revision: digestSchema,
});
const problemCacheInputSchema = z.object({
  workspace: z.string(),
  generation: generationSchema,
  producer: digestSchema,
  assets: digestSchema,
});
export const problemCacheRequestSchema = z.discriminatedUnion("action", [
  problemCacheInputSchema.extend({
    action: z.literal("problems"),
    entries: z.array(problemKeySchema).min(1).max(8),
  }),
  problemCacheInputSchema.extend({
    action: z.literal("store-problems"),
    entries: z
      .array(problemKeySchema.extend({ problems: z.array(problemSchema) }))
      .min(1)
      .max(8),
  }),
]);
export const problemCacheSchema = z.object({
  session: sessionSchema,
  results: z.array(
    z.discriminatedUnion("state", [
      problemKeySchema.extend({
        state: z.literal("ready"),
        producer: digestSchema,
        assets: digestSchema,
        problems: z.array(problemSchema),
      }),
      z.object({ state: z.literal("pending"), path: deckPathSchema }),
      z.object({ state: z.literal("superseded"), path: deckPathSchema }),
      pathFailureSchema,
    ]),
  ),
});
export const problemStoredSchema = z.object({
  session: sessionSchema,
  results: z.array(
    z.discriminatedUnion("state", [
      z.object({ state: z.literal("stored"), path: deckPathSchema }),
      z.object({ state: z.literal("superseded"), path: deckPathSchema }),
      pathFailureSchema,
    ]),
  ),
});
export const searchCardSchema = z.object({
  id: z.string().min(1),
  label: z.string(),
  front: z.string(),
  back: z.string(),
  tags: z.string(),
});
const searchKeySchema = sourceSchema.pick({ path: true, revision: true });
const searchCacheInputSchema = z.object({
  workspace: z.string(),
  generation: generationSchema,
  producer: digestSchema,
});
export const searchCacheRequestSchema = z.discriminatedUnion("action", [
  searchCacheInputSchema.extend({
    action: z.literal("search"),
    entries: z.array(searchKeySchema).min(1).max(8),
  }),
  searchCacheInputSchema.extend({
    action: z.literal("store-search"),
    entries: z
      .array(searchKeySchema.extend({ cards: z.array(searchCardSchema) }))
      .min(1)
      .max(8),
  }),
]);
export const searchCacheSchema = z.object({
  session: sessionSchema,
  results: z.array(
    z.discriminatedUnion("state", [
      sourceSchema.extend({
        state: z.literal("ready"),
        producer: digestSchema,
        cards: z.array(searchCardSchema),
      }),
      z.object({
        state: z.enum(["pending", "superseded"]),
        path: deckPathSchema,
      }),
      pathFailureSchema,
    ]),
  ),
});
export type SearchCard = z.infer<typeof searchCardSchema>;
export type Problem = z.infer<typeof problemSchema>;
export const cacheRebuiltSchema = z.object({
  session: sessionSchema,
  rebuilt: z.literal(true),
});
const summarySchema = z.object({
  path: z.string(),
  status: statusSchema,
  reasons: z.array(z.string()),
  source: z.string(),
});
export const workspaceSchema = z.object({
  root: z.string(),
  decks: z.array(summarySchema),
  macros: z.record(
    z.string(),
    z.union([
      z.string(),
      z.tuple([z.string(), z.number()]),
      z.tuple([z.string(), z.number(), z.string()]),
    ]),
  ),
  stmaryrd: z.string(),
});
export const documentSchema = z.object({
  session: sessionSchema,
  path: deckPathSchema,
  source: z.string(),
  hash: digestSchema,
  cards: z.number().int().nonnegative().nullable(),
  status: statusSchema.nullable(),
  reasons: z.array(z.string()),
  built: z.string().nullable(),
  package: z.string(),
});
export const assetsSchema = workspaceSchema
  .pick({ macros: true, stmaryrd: true })
  .extend({
    identity: digestSchema,
    renderer: z.string().min(1),
  });
export type Manifest = z.infer<typeof manifestSchema>;
export const assetVersionSchema = assetsSchema.pick({ identity: true });
export type Entry = Manifest["entries"][number];
export type SourceResult = z.infer<typeof sourcesSchema>["results"][number];
export type PackageResult = z.infer<typeof checksSchema>["results"][number];
export const reviewSchema = z.object({
  decks: z.array(summarySchema.extend({ built: z.string().nullable() })),
});
export const generatedSchema = z.object({
  status: statusSchema,
  package: z.string(),
  log: z.string(),
});
export type Summary = z.infer<typeof summarySchema>;
export type Pending = z.infer<typeof reviewSchema>["decks"][number];
export type Document = z.infer<typeof documentSchema> & {
  path: string;
  saved: string;
};
export type Macros = z.infer<typeof workspaceSchema>["macros"];

export async function request<Schema extends z.ZodType>(
  payload: Request,
  schema: Schema,
): Promise<z.output<Schema>> {
  const body = JSON.stringify(payload);
  if (isTauri()) {
    return schema.parse(
      JSON.parse(await invoke<string>("request", { payload: body })),
    );
  }
  const response = await fetch("/api/request", {
    method: "POST",
    headers: { "Content-Type": "application/json", "x-flashcards": "1" },
    body,
  });
  if (!response.ok) throw new Error(await response.text());
  return schema.parse(await response.json());
}

// Calls `changed` after files in the workspace change. The native app uses the
// Tauri file watcher; the development server forwards its chokidar events over
// Vite's HMR socket: https://vite.dev/guide/api-plugin.html#client-server-communication
export async function watchWorkspace(
  root: string,
  changed: (paths: string[]) => void,
): Promise<() => void> {
  if (isTauri())
    return watch(
      root,
      (event) => {
        // Access events describe reads: https://v2.tauri.app/reference/javascript/fs/#watcheventkind
        if (
          event.type !== "any" &&
          event.type !== "other" &&
          "access" in event.type
        )
          return;
        changed(event.paths);
      },
      { recursive: true, delayMs: 300 },
    );
  const hot = import.meta.hot;
  if (!hot) throw new Error("The development server must provide HMR.");
  const listener = (data: { root: string; path: string }) => {
    if (data.root === root) changed([data.path]);
  };
  hot.on("flashcards:changed", listener);
  const response = await fetch("/api/watch", {
    method: "POST",
    headers: { "x-flashcards": "1" },
    body: root,
  });
  if (!response.ok) throw new Error(await response.text());
  return () => hot.off("flashcards:changed", listener);
}
