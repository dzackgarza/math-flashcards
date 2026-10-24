import { expect, test } from "bun:test";
import { mkdtemp, mkdir } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import {
  documentSchema,
  organizedSchema,
  reviewSchema,
  workspaceSchema,
  type Request,
} from "../src/bridge";

test("a deck folder supports discovery, editing, and organization beside its export directory", async () => {
  const directory = await mkdtemp(join(tmpdir(), "flashcards-workspace-"));
  const workspace = join(directory, "study");
  const backend = resolve(import.meta.dir, "../backend.py");
  const find = Bun.spawnSync(["uv", "python", "find", "--script", backend]);
  expect(find.exitCode, find.stderr.toString()).toBe(0);
  const python = find.stdout.toString().trim();
  const request = async (payload: Request) => {
    const process = Bun.spawn([python, backend], {
      stdin: new Blob([JSON.stringify(payload) + "\n"]),
      stdout: "pipe",
      stderr: "pipe",
      env: { ...Bun.env, XDG_CACHE_HOME: join(directory, "cache") },
    });
    const output = await new Response(process.stdout).text();
    const error = await new Response(process.stderr).text();
    return { output, error, code: await process.exited };
  };
  const source =
    '---\ntitle: "Algebra::Groups"\n---\n\n' +
    '::: {.front card-id="identity"}\nIdentity element\n:::\n\n' +
    '::: {.back card-id="identity"}\n$eg=ge=g$\n:::\n';
  try {
    await mkdir(join(workspace, "Algebra"), { recursive: true });
    await mkdir(join(workspace, "apkg"));
    await Bun.write(join(workspace, "Algebra/Groups.md"), source);
    await Bun.write(join(workspace, "apkg/Export notes.md"), "Export metadata");
    await Bun.write(join(directory, "Outside.md"), source);

    const listed = await request({ action: "list", workspace });
    expect(listed.code, listed.error).toBe(0);
    const listing = workspaceSchema.parse(JSON.parse(listed.output));
    expect(listing.root).toBe(workspace);
    expect(listing.decks.map((deck) => deck.path)).toEqual([
      "Algebra/Groups.md",
    ]);

    const loaded = await request({
      action: "load",
      workspace,
      path: "Algebra/Groups.md",
    });
    expect(loaded.code, loaded.error).toBe(0);
    const deck = documentSchema.parse(JSON.parse(loaded.output));
    expect(deck.source).toBe(source);
    expect(deck.cards).toBe(1);
    expect(deck.package).toBe(join(workspace, "apkg/Algebra__Groups.apkg"));

    const edited = source.replace(
      "Identity element",
      "Define an identity element.",
    );
    const saved = await request({
      action: "save",
      workspace,
      path: "Algebra/Groups.md",
      source: edited,
      expected: deck.hash,
    });
    expect(saved.code, saved.error).toBe(0);
    expect(await Bun.file(join(workspace, "Algebra/Groups.md")).text()).toBe(
      edited,
    );
    const savedDeck = documentSchema.parse(JSON.parse(saved.output));
    const moved = await request({
      action: "organize",
      workspace,
      changes: [
        { path: "Groups.md", source: edited, expected: null },
        { path: "Algebra/Groups.md", source: null, expected: savedDeck.hash },
      ],
    });
    expect(moved.code, moved.error).toBe(0);
    expect(
      organizedSchema
        .parse(JSON.parse(moved.output))
        .changed.map((item) => item.path),
    ).toEqual(["Groups.md", "Algebra/Groups.md"]);
    expect(await Bun.file(join(workspace, "Groups.md")).text()).toBe(edited);
    expect(await Bun.file(join(workspace, "Algebra/Groups.md")).exists()).toBe(
      false,
    );
    const reviewed = await request({ action: "review", workspace });
    expect(reviewed.code, reviewed.error).toBe(0);
    expect(
      reviewSchema
        .parse(JSON.parse(reviewed.output))
        .decks.map((item) => item.path),
    ).toEqual(["Groups.md"]);

    for (const path of ["../Outside.md", "apkg/Export notes.md"]) {
      const rejected = await request({ action: "load", workspace, path });
      expect(rejected.code).not.toBe(0);
      expect(rejected.error).toContain("deck");
      const invalidMove = await request({
        action: "organize",
        workspace,
        changes: [{ path, source, expected: null }],
      });
      expect(invalidMove.code).not.toBe(0);
      expect(invalidMove.error).toContain("deck");
    }
    expect(await Bun.file(join(directory, "Outside.md")).text()).toBe(source);
    expect(await Bun.file(join(workspace, "apkg/Export notes.md")).text()).toBe(
      "Export metadata",
    );
  } finally {
    const cleanup = Bun.spawnSync(["trash", directory]);
    expect(cleanup.exitCode, cleanup.stderr.toString()).toBe(0);
  }
}, 60000);
