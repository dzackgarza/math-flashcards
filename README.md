# Math Flashcards

Personal Anki decks for graduate mathematics — quals (algebra, analysis, topology, complex
analysis), algebraic geometry, K3 surfaces, and lattice theory — authored as plain
Markdown and compiled to `.apkg` with
[ankdown-for-math](https://github.com/dzackgarza/ankdown-for-math).

This repository maintains the personal study collection. Some material was
copied into [new-qual-site](https://github.com/dzackgarza/new-qual-site) to seed
its content. The projects are maintained independently.

## Layout

- `decks/` — the maintained Markdown sources, organized by mathematical subject.
  The [subject guide](docs/deck-subjects.md) relates the deck hierarchy to the
  Zotero collections and defines where new cards belong. Each file is one deck,
  and its path matches its Anki deck name (`decks/Analysis/Complex Analysis.md`
  is `Analysis::Complex Analysis`).
- `decks/apkg/` — generated Anki packages, importable directly into Anki. Git ignores them.
- `desktop/` — the Tauri deck editor. See its [guide](desktop/README.md).

## Desktop editor

```bash
just desktop-install
```

Launch **Math Flashcards** from the application menu or run `math-flashcards`.
Each commit that passes the commit gate rebuilds and installs the app.
Open `decks/` itself from the workspace menu in the sidebar. A workspace is any
folder containing deck Markdown files and subject subfolders. Its `apkg/`
subfolder holds exports and is excluded from deck discovery.
Select a deck in the tree. Ctrl-K opens a command menu that finds decks,
cards, and actions.
The editor supports card search, side-by-side Front and Back editing through
Zettlr's shared Pandoc editor, and adding and deleting cards. Edits save automatically, and
the open deck follows changes that other programs make to its file.

Drag a card in the card list to reorder it, or onto a deck in the tree to move it.
Ctrl-click or Shift-click selects several cards to drag together. Drag a deck onto
another deck to merge them. Right-click a deck to update its package, rename it,
or delete it. **New deck** creates an empty deck, and **Undo** restores the last
organization change.

Each deck's generated Anki package belongs in the workspace's `apkg/` folder.
A package is out of date when
its deck, media, or the exporter changed after generation, or when the package
file changed. The toolbar status tells how the package differs from the deck;
select it to review the new, edited, and removed cards and to go to each one.
**Update Anki packages** in the sidebar reviews and updates every out-of-date
package at once. A failed update keeps the previous package.

**Problems** in the sidebar lists every equation that does not render, every
card without an answer, and every deck with invalid card structure. Select a
problem to open its card.

Use `just desktop-dev` for native development. The [desktop guide](desktop/README.md)
lists dependencies, verification commands, and the Anki import boundary.

## Card format

Each card has a `.front` div and a `.back` div with the same `card-id` attribute.
Each ID needs exactly one side of each type. Pairing uses the ID; fronts set the
card order. Each side accepts normal Pandoc Markdown and LaTeX. Math uses `$…$`
(inline) and `$$…$$` (display), with no space just inside a delimiter. Display
math continues its paragraph, so no blank line separates it from adjacent text.
`just test` rejects a `$` that Pandoc does not read as math, a blank line beside
display math, trailing whitespace, and an equation that MathJax cannot render
with the exporter's macros, such as one with an undefined macro. The front div's optional `tags` attribute
sets Anki tags. The frontmatter `title` is the Anki deck name, with `::` denoting sub-decks.

```markdown
---
title: "Algebra::Groups"
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
just build          # compile every deck in decks/ into decks/apkg/
```

The Python bridge installs Ankdown from its GitHub main branch through `uv`.
Each build and each workspace listing upgrades the script environment to the
latest Ankdown commit and the latest release of every other dependency. Other
requests run the installed script environment and do not read the network.
Pandoc reads and validates the paired divs. The bridge uses Ankdown's existing
math and media filter and package writer to generate `.apkg` files.
Pandoc and `uv` must be on `PATH`.

Math renders via MathJax 4 using the macro set that
[pandoc-config](https://github.com/dzackgarza/pandoc-config) main generates from its
LaTeX sources (`templates/css/mathjax-macros.json`), the same macros as the website.
Each build fetches the current set and bundles it in the package, so `\theset`,
`\abs`, `\normal`, and the rest resolve in Anki. The package also bundles
pandoc-config's MathJax `stmaryrd` package (`templates/js/mathjax-stmaryrd.js`),
which gives `\fps{x}` and `\llbracket x \rrbracket` sized double brackets. Cards use the current macro names;
`just test` rejects a macro that the current set does not define.
