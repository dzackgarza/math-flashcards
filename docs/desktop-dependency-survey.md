# Desktop dependency survey

Date: 2026-10-14. Selected architecture: separate CodeMirror Front and Back fields.

## Recommendation

Use Tauri 2, React, TypeScript, Vite, Mantine, and CodeMirror 6.
Keep Markdown files as the authored source. Use the existing ankdown Pandoc
filter for deck validation and ankdown for package generation. The exporter and
the macro set track the main branches of ankdown-for-math and pandoc-config.

## Dependency owners

| Behaviour | Dependency | Integration |
| --- | --- | --- |
| Desktop window and frontend build | [Tauri with Vite](https://v2.tauri.app/start/frontend/vite/) | Official React/TypeScript scaffold |
| Deck navigation | [Mantine Tree](https://mantine.dev/core/tree/) | Folder hierarchy and selectable deck nodes |
| App layout | CSS grid columns with Mantine components | Deck tree, card list, Front and Back editors |
| Command menu | [Mantine Spotlight](https://mantine.dev/x/spotlight/) | Ctrl-K search over decks, cards, and actions |
| Card and deck organization | [Atlassian Pragmatic drag and drop](https://atlassian.design/components/pragmatic-drag-and-drop/) | Drag sources, drop targets, insertion markers, auto-scroll, and announcements; see `card-organization.md` |
| Commutative diagrams | Quiver from the sibling `visual-tikz-editor` checkout; `quiver.sty` and the TikZ Lua filter from pandoc-config | Graphical diagram editing; TikZ-cd source renders to SVG offline |
| Editing | Zettlr's `@dzack/pandoc-editor`, mounted with [React CodeMirror](https://github.com/uiwjs/react-codemirror) | Shared Pandoc editing and live rendering in separate Front and Back fields |
| Source ranges and syntax | Zettlr-Pandoc's Lezer fork | Pandoc fenced divs, attributes, math, and source positions; shared parser for both editors and deck pairing |
| External changes | [Tauri filesystem plugin](https://v2.tauri.app/plugin/file-system/) | Watch the selected workspace |
| Process execution and output | [Tauri commands](https://v2.tauri.app/develop/calling-rust/) and Python subprocess | A typed bridge request; exporter completion and diagnostics |
| Native diagnostics | [Tauri logging plugin](https://v2.tauri.app/plugin/logging/), `log`, and [`dirs::state_dir()`](https://docs.rs/dirs/latest/dirs/fn.state_dir.html) | Request outcomes, elapsed times, and process lifecycle in XDG state; retain rotated files |
| Workspace selection | [Tauri dialog plugin](https://v2.tauri.app/plugin/dialog/) | Native folder picker |
| Preferences | [Tauri store plugin](https://v2.tauri.app/plugin/store/) | Workspace path |
| Generation records | Python SQLite and [platformdirs](https://platformdirs.readthedocs.io/) | Successful build fingerprints in the platform cache |
| Card HTML and APKG | [ankdown-for-math](https://github.com/dzackgarza/ankdown-for-math), [Pandoc Lua filters](https://pandoc.org/lua-filters.html) | Reuse the filter's front/back JSON and exporter CLI |
| Math rendering | Zettlr's shared equation renderer and [MathJax 4](https://docs.mathjax.org/en/v4.0/web/typeset.html) | The host supplies MathJax and the exporter's macros; the shared editor owns widgets and source selection |
| Status controls | Mantine Badge, Button, Alert, Loader, Drawer | Visible build state and the Problems drawer |
| Native scheduling and collection backups | [Anki's Python library](https://github.com/ankitects/anki/tree/main/pylib/anki), PyPI `anki` | One persistent host owns the collection; native card identities enter its scheduling API directly |
| One running desktop copy | [Tauri single-instance plugin](https://v2.tauri.app/plugin/single-instance/) | First shell plugin; activates the existing window |
| Core and analysis boundaries | [Import Linter](https://import-linter.readthedocs.io/) | `.importlinter` forbids core imports from analyses and imports between analysis modules; `desktop-boundaries` tests both accepted and rejected imports |

## Study ownership

The Study integration has three parts. `desktop/study/` owns Anki scheduling and
every learning-data write in one persistent process. `desktop/analysis/` computes
each analysis independently in a fresh bridge process with a read-only record
connection. `desktop/src/` renders the interface and sends typed requests. A new
analysis module or view requires no core schema change. The source and alternative
survey, API measurements, and boundary probes are maintained in
[Study research](../specs/001-in-app-review/research.md), especially R1, R3, and R17.

The Anki wheel supplies its Rust scheduling implementation through Python bindings.
The persistent host preserves its queue and undo state across requests. SQLite's
online backup API snapshots the separate permanent learning record beside each
Anki collection backup. These stores belong to XDG data; removing cache or logs
must not remove a learning fact.

## Alternatives

| Choice | Fit | Recommendation |
| --- | --- | --- |
| Mantine | Supplies the tree, layout, forms, dialogs, and status containers together | Use |
| Individually assembled headless components | Requires additional styling and composition for the same surface | Prefer the complete component library |
| CodeMirror source editing | Retains LaTeX and Markdown as text; exposes source positions | Use |
| [Tiptap Markdown](https://tiptap.dev/docs/editor/markdown) | Converts Markdown through an editor document model; its documented Markdown extension is beta and has preservation limits | Use only if rich text authoring is chosen |
| [remark/mdast](https://github.com/remarkjs/remark) | Mature parsing and transformation ecosystem; useful for source ranges | Zettlr's Lezer fork supplies Pandoc syntax and ranges in CodeMirror |
| Browser Markdown renderer plus KaTeX | Adds a second rendering interpretation and macro configuration | Reuse exporter MathJax and macros |
| New Rust APKG implementation | Duplicates package generation, media and model ownership | Reuse ankdown |

## Source and export contracts

Local evidence: `README.md`, `justfile`, `desktop/backend.py`, and the installed
`ankdown` package's `ankdown.lua`, `cli.py`, `mathjax.html`, and `card.css`.

The paired-card filter validates `.front` and `.back` divs linked by `card-id`.
It supplies each complete side to Ankdown's filter as a block container.
Ankdown handles math, images, generated media, and card HTML.
The editor renders math with the same macros as export.

The CLI accepts an individual Markdown file with an explicit output path.
Directory builds map relative deck paths to filenames by replacing separators
with `__`. Regeneration uses the whole saved deck, including its metadata and media.
Process events can show a running indicator and real diagnostics. The current
CLI provides completion output rather than a percentage progress stream.

Each CodeMirror field edits only one div body. Keep the authored document around
that body. Zettlr's Lezer fork owns Pandoc syntax recognition and attribute
parsing. The app pairs sides by ID. Pandoc validates the same pairs for loading,
saving, and export. Saves compare disk content to detect external edits.

## Generation state

Show separate indicators for an unsaved draft and the saved deck's package state.
The bridge reports Up to date, Unsynced, or Empty for a saved deck. The editor
also shows a checking state while the bridge status is pending, Generating
during a build, and Failed after a failed build.

A successful generation record contains hashes of the source, resolved media,
exporter assets, the macro set, and resulting APKG bytes.
Use a standard SHA-256 implementation. Up to date requires the current inputs
and package to match the successful record. An existing package with no verified
record starts as Unsynced. Modification times alone cannot prove equivalence.

Generate to a temporary package beside the destination. Publish the package and
record only after successful completion. Recheck inputs after generation so an
edit during the build leaves the deck Unsynced. Errors retain their diagnostic
output and the previous package. Scope filesystem and shell capabilities to
the chosen workspace and declared commands.

## Anki import boundary

The inspected exporter computes note GUIDs from front plus back content.
Editing content therefore changes note identity. The app's Up to date badge
describes the generated APKG. Anki collection state is a separate operation.
[Anki packaged deck documentation](https://docs.ankiweb.net/manual/importing/packaged-decks)
describes import behaviour. Replacement of edited notes and deletion from a live
collection require a separate identity/import design if requested.

## Architecture decision

### Native Study

The Study function uses the `anki` Python library directly for scheduling. Native
card IDs become Anki scheduling identities; retained Markdown and the shared editor
renderer own the presentation. The choices and source API references are maintained
in [the Study research](../specs/001-in-app-review/research.md).

The [Tauri opener plugin](https://v2.tauri.app/plugin/opener/) supplies
`revealItemInDir` for the learning-record location. It opens the platform file
manager and selects the record. This replaces the need to write a Linux process
launcher or choose a file-manager executable. The shell grants the reveal command;
the interface passes the record path returned by the opened store. Browser
development shows the paths without a native folder command.

### Authoring and package generation

Selected: side-by-side Front and Back editors with math rendered in place, built
under `desktop/` in this repository for the personal flashcard collection.

Alternative: a rich text editor using Tiptap, with additional extensions and
Markdown round-trip verification for the mathematical source corpus.

The desktop editor stores paired fenced divs linked by card ID. A native command
runs the Python exporter bridge. The filesystem plugin watches the
selected workspace; the bridge owns file reads, saves and generation.
