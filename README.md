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

- `decks/` — paired Front and Back divs, grouped by subject
  (`decks/<Subject>/<Deck>.md`). Each file is one deck.
- `apkg/` — compiled Anki packages, importable directly into Anki.
- `desktop/` — the Tauri deck editor. See its [guide](desktop/README.md).

## Desktop editor

```bash
just desktop-install
```

Launch **Math Flashcards** from the application menu or run `math-flashcards`.
Use `just desktop-update` to rebuild and update the installed app and desktop entry.
Open a workspace folder that contains `decks/`. Select a deck in the tree.
The editor supports card search, separate Front and Back editing, adding and deleting cards,
math preview, and a front/back flip control. Save the deck, then select
**Generate Anki deck** to regenerate its package in `apkg/`.

**Organize** displays deck and card tiles. Drag card handles to reorder or move
cards between decks. Checkboxes select groups. Use the toolbar to move or split
a selection. Drag a deck onto another to absorb it. Menus provide the same
operations without dragging, and **Undo** restores the last organization change.

The package badge shows **Up to date**, **Unsynced**, **Generating**, or **Failed**.
Source and media changes, exporter changes, and changes to the generated package
make it unsynced. A separate badge shows unsaved edits. Failed exports retain
the previous package. Disk changes are checked before a save.

Use `just desktop-dev` for native development. The [desktop guide](desktop/README.md)
lists dependencies, verification commands, and the Anki import boundary.

## Card format

Each card has a `.front` div and a `.back` div with the same `card-id` attribute.
Each ID needs exactly one side of each type. Pairing uses the ID; fronts set the
card order. Each side accepts normal Pandoc Markdown and LaTeX. Math uses `$…$`
(inline) and `$$…$$` (display). The front div's optional `tags` attribute sets Anki
tags. The frontmatter `title` is the Anki deck name, with `::` denoting sub-decks.

```markdown
---
title: "Qual Algebra::QualAlgebraGroups"
---

::: {.front card-id="simple-group" tags="definition"}
Simple group
:::

::: {.back card-id="simple-group"}
No nontrivial normal subgroups.
:::

::: {.front card-id="class-equation" tags="theorem"}
Class Equation
:::

::: {.back card-id="class-equation"}
$$\abs{G} = \abs{Z(G)} + \sum_i [G : C_G(x_i)]$$
:::
```

## Building

```bash
just build          # compile every deck in decks/ into apkg/
```

The locked Python bridge fetches Ankdown from GitHub through `uv`.
Pandoc reads and validates the paired divs. The bridge uses Ankdown's existing
math and media filter and package writer to generate `.apkg` files.
Pandoc and `uv` must be on `PATH`.

Math renders via MathJax using the macro set generated from the LaTeX sources in
[pandoc-config](https://github.com/dzackgarza/pandoc-config)
(`generate-mathjax-config.py`) — the same macros used by the website. The tool bundles
them automatically, so `\theset`, `\abs`, `\normal`, and the rest resolve in Anki.
