import { invoke, isTauri } from "@tauri-apps/api/core";
import { z } from "zod";

export type Request =
  | { action: "list"; workspace: string }
  | { action: "load" | "generate"; workspace: string; path: string }
  | { action: "preview"; workspace: string; path: string; source: string }
  | { action: "save"; workspace: string; path: string; source: string; expected: string };

export const statusSchema = z.enum(["Up to date", "Unsynced"]);
export const workspaceSchema = z.object({ decks: z.array(z.object({ path: z.string(), status: statusSchema })) });
export const documentSchema = z.object({ source: z.string(), hash: z.string(), status: statusSchema, package: z.string() });
export const previewSchema = z.object({
  title: z.string(),
  cards: z.array(z.object({ front: z.string(), back: z.string(), tags: z.array(z.string()) })),
  macros: z.record(z.string(), z.union([z.string(), z.tuple([z.string(), z.number()]), z.tuple([z.string(), z.number(), z.string()])])),
  css: z.string(),
});
export const generatedSchema = z.object({ status: statusSchema, package: z.string(), log: z.string() });
export type Summary = z.infer<typeof workspaceSchema>["decks"][number];
export type Document = z.infer<typeof documentSchema> & { path: string; saved: string };
export type Preview = z.infer<typeof previewSchema>;

export async function request<Schema extends z.ZodType>(payload: Request, schema: Schema): Promise<z.output<Schema>> {
  const body = JSON.stringify(payload);
  if (isTauri()) {
    return schema.parse(JSON.parse(await invoke<string>("request", { payload: body })));
  }
  const response = await fetch("/api/request", { method: "POST", headers: { "Content-Type": "application/json", "x-flashcards": "1" }, body });
  if (!response.ok) throw new Error(await response.text());
  return schema.parse(await response.json());
}
