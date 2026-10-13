import { expect, test } from "bun:test";
import { Glob } from "bun";
import { resolve } from "node:path";
import { cards, replaceCard } from "../src/cards";
import { previewSchema } from "../src/bridge";

test("repository card ranges preserve source and agree with Pandoc export", async () => {
  const workspace = resolve(import.meta.dir, "../..");
  for await (const path of new Glob("**/*.md").scan(
    resolve(workspace, "decks"),
  )) {
    const source = await Bun.file(resolve(workspace, "decks", path)).text();
    const ranges = cards(source);
    for (const range of ranges) {
      expect(
        replaceCard(source, range, source.slice(range.from, range.to)),
      ).toBe(source);
    }
    const process = Bun.spawn(
      [
        "uv",
        "run",
        "--locked",
        "--script",
        resolve(import.meta.dir, "../backend.py"),
      ],
      {
        stdin: new Blob([
          JSON.stringify({ action: "preview", workspace, path, source }) + "\n",
        ]),
        stdout: "pipe",
        stderr: "pipe",
      },
    );
    const output = await new Response(process.stdout).text();
    const diagnostics = await new Response(process.stderr).text();
    expect(await process.exited, path + ": " + diagnostics).toBe(0);
    const deck = previewSchema.parse(JSON.parse(output));
    expect(ranges.length, path).toBe(deck.cards.length);
  }
}, 120000);
