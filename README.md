> **Deck content archive — this content now lives in [dzackgarza/new-qual-site](https://github.com/dzackgarza/new-qual-site).**
>
> The deck content was migrated into that repository and is maintained there.
>
> Content coverage was checked against this repository at `69cecc4` before archiving.
> The comparisons are in `artifacts/issue-11/source-reviews/content-coverage-verification.md`
> in `new-qual-site`, and they re-run against this pinned revision.

# Math Flashcards

Anki decks for graduate mathematics — quals (algebra, analysis, topology, complex
analysis), algebraic geometry, K3 surfaces, and lattice theory — authored as plain
Markdown and compiled to `.apkg` with
[ankdown-for-math](https://github.com/dzackgarza/ankdown-for-math).

## Layout

- `decks/` — card sources as nested Markdown lists, grouped by subject
  (`decks/<Subject>/<Deck>.md`). Each file is one deck.
- `apkg/` — compiled Anki packages, importable directly into Anki.
- `desktop/` — the Tauri deck editor. See its [guide](desktop/README.md).

## Desktop editor

```bash
just desktop-install
just desktop-build
just desktop-run
```

Open a workspace folder that contains `decks/`. Select a deck in the tree.
The editor supports card search, source editing, adding and deleting cards,
math preview, and a front/back flip control. Save the deck, then select
**Generate Anki deck** to regenerate its package in `apkg/`.

The package badge shows **Up to date**, **Unsynced**, **Generating**, or **Failed**.
Source and media changes, exporter changes, and changes to the generated package
make it unsynced. A separate badge shows unsaved edits. Failed exports retain
the previous package. Disk changes are checked before a save.

Use `just desktop-dev` for native development. The [desktop guide](desktop/README.md)
lists dependencies, verification commands, and the Anki import boundary.

## Card format

Each card is a top-level list item (the **front**); its answer is the indented body
(the **back**). Math uses `$…$` (inline) and `$$…$$` (display). An optional trailing
`tags:` line sets per-card Anki tags. The frontmatter `title` is the Anki deck name,
with `::` denoting sub-decks.

```markdown
---
title: "Qual Algebra::QualAlgebraGroups"
---

- Simple group

    No nontrivial normal subgroups.

    tags: definition

- Class Equation

    $$\abs{G} = \abs{Z(G)} + \sum_i [G : C_G(x_i)]$$

    tags: theorem
```

## Building

```bash
just build          # compile every deck in decks/ into apkg/
```

The tool is fetched from GitHub via `uvx` — no local checkout needed. Under the hood:

```bash
uvx --from git+https://github.com/dzackgarza/ankdown-for-math \
  ankdown build decks --output-dir apkg
```

`ankdown build` runs Pandoc with its own bundled lua filter, so a single command
turns the Markdown decks into `.apkg` packages. (Pandoc must be on `PATH`.)

Math renders via MathJax using the macro set generated from the LaTeX sources in
[pandoc-config](https://github.com/dzackgarza/pandoc-config)
(`generate-mathjax-config.py`) — the same macros used by the website. The tool bundles
them automatically, so `\theset`, `\abs`, `\normal`, and the rest resolve in Anki.
