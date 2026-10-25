import { expect, test } from "bun:test";
import { Glob } from "bun";
import { resolve } from "node:path";
import { cards, replaceField } from "../src/cards";
import { documentSchema } from "../src/bridge";

test("repository card ranges preserve source and agree with Pandoc export", async () => {
  const workspace = resolve(import.meta.dir, "../../decks");
  const backend = resolve(import.meta.dir, "../backend.py");
  // `uv run --script` fetches ankdown main from GitHub on every call. One sync
  // upgrades the script environment to the latest versions; each load then runs its interpreter.
  // https://docs.astral.sh/uv/guides/scripts/#locking-dependencies
  const sync = Bun.spawnSync(["uv", "sync", "--upgrade", "--script", backend]);
  expect(sync.exitCode, sync.stderr.toString()).toBe(0);
  const find = Bun.spawnSync(["uv", "python", "find", "--script", backend]);
  expect(find.exitCode, find.stderr.toString()).toBe(0);
  const python = find.stdout.toString().trim();
  for await (const path of new Glob("**/*.md").scan(workspace)) {
    if (path.startsWith("apkg/")) continue;
    const source = await Bun.file(resolve(workspace, path)).text();
    const ranges = cards(source);
    for (const range of ranges) {
      for (const field of [range.front, range.back])
        expect(replaceField(source, field, field.value)).toBe(source);
    }
    const process = Bun.spawn([python, backend], {
      stdin: new Blob([
        JSON.stringify({ action: "validate", workspace, path, generation: 0 }) +
          "\n",
      ]),
      stdout: "pipe",
      stderr: "pipe",
    });
    const output = await new Response(process.stdout).text();
    const diagnostics = await new Response(process.stderr).text();
    expect(await process.exited, path + ": " + diagnostics).toBe(0);
    const deck = documentSchema.parse(JSON.parse(output));
    expect(ranges.length, path).toBe(deck.cards);
  }
}, 120000);
