// Reports the problems that the editor's Problems drawer shows, for every deck
// in a workspace, and fails when there is one.
import { createRequire } from "node:module";
import { join } from "node:path";
import { workspaceSchema } from "../src/bridge";
import { texOptions } from "../src/math";
import { deckProblems } from "../src/problems";

const root = process.argv[2];
if (!root) throw new Error("Usage: bun scripts/check-math.ts <workspace>");
const backend = Bun.spawnSync(
  [
    "uv",
    "run",
    "--refresh-package",
    "ankdown",
    join(import.meta.dir, "..", "backend.py"),
  ],
  {
    stdin: new TextEncoder().encode(
      JSON.stringify({ action: "list", workspace: root }) + "\n",
    ),
  },
);
if (backend.exitCode !== 0) throw new Error(backend.stderr.toString());
const workspace = workspaceSchema.parse(JSON.parse(backend.stdout.toString()));
// MathJax's Node entry point loads the same TeX input component as the editor:
// https://docs.mathjax.org/en/v3.2/server/components.html
const mathjax = await createRequire(import.meta.url)("mathjax").init({
  loader: { load: ["input/tex", "[tex]/mathtools"] },
  tex: texOptions(workspace.macros),
});
const problems = workspace.decks.flatMap((deck) =>
  deckProblems(mathjax, deck.path, deck.source),
);
for (const problem of problems)
  console.log(
    [
      problem.path,
      problem.label && `"${problem.label}"`,
      problem.side,
      problem.kind + ": " + problem.message,
      problem.source,
    ]
      .filter(Boolean)
      .join(" | "),
  );
console.log(`${problems.length} problems in ${workspace.decks.length} decks.`);
process.exit(problems.length ? 1 : 0);
