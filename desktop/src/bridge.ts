import { invoke, isTauri } from "@tauri-apps/api/core";
import { watch } from "@tauri-apps/plugin-fs";
import { z } from "zod";

export type Request =
  | { action: "list" | "review"; workspace: string }
  | { action: "load" | "generate"; workspace: string; path: string }
  | { action: "organize"; workspace: string; changes: Change[] }
  | {
      action: "save";
      workspace: string;
      path: string;
      source: string;
      expected: string;
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
const summarySchema = z.object({
  path: z.string(),
  status: statusSchema,
  reasons: z.array(z.string()),
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
});
export const documentSchema = z.object({
  source: z.string(),
  hash: z.string(),
  cards: z.number(),
  status: statusSchema,
  reasons: z.array(z.string()),
  built: z.string().nullable(),
  package: z.string(),
});
export const reviewSchema = z.object({
  decks: z.array(
    summarySchema.extend({ source: z.string(), built: z.string().nullable() }),
  ),
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
