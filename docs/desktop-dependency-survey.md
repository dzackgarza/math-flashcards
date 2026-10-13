# Desktop dependency survey

Date: 2026-10-14. Selected architecture: separate CodeMirror Front and Back fields.

## Recommendation

Use Tauri 2, React, TypeScript, Vite, Mantine, and CodeMirror 6.
Keep Markdown files as the authored source. Use the existing ankdown Pandoc
filter for preview HTML and ankdown for package generation. Package dependencies
must be locked to tested releases during implementation.

## Dependency owners

| Behaviour | Dependency | Integration |
| --- | --- | --- |
| Desktop window and frontend build | [Tauri with Vite](https://v2.tauri.app/start/frontend/vite/) | Official React/TypeScript scaffold |
| Deck navigation | [Mantine Tree](https://mantine.dev/core/tree/) | Folder hierarchy and selectable deck nodes |
| App layout | [Mantine AppShell](https://mantine.dev/core/app-shell/), [Splitter](https://mantine.dev/core/splitter/) | Deck tree, card list, editor, preview |
| Editing | [React CodeMirror](https://github.com/uiwjs/react-codemirror), `@codemirror/lang-markdown` | Separate Front and Back fields, history, selection and keyboard commands |
| Source ranges and syntax | Zettlr-Pandoc's Lezer fork | Pandoc fenced divs, attributes, math, and source positions; shared parser for both editors and deck pairing |
| External changes | [Tauri filesystem plugin](https://v2.tauri.app/plugin/file-system/) | Watch the selected workspace |
| Process execution and output | [Tauri commands](https://v2.tauri.app/develop/calling-rust/) and Python subprocess | A typed bridge request; exporter completion and diagnostics |
| Workspace selection | [Tauri dialog plugin](https://v2.tauri.app/plugin/dialog/) | Native folder picker |
| Preferences | [Tauri store plugin](https://v2.tauri.app/plugin/store/) | Workspace path |
| Generation records | Python SQLite and [platformdirs](https://platformdirs.readthedocs.io/) | Successful build fingerprints in the platform cache |
| Card HTML and APKG | [ankdown-for-math](https://github.com/dzackgarza/ankdown-for-math), [Pandoc Lua filters](https://pandoc.org/lua-filters.html) | Reuse the filter's front/back JSON and exporter CLI |
| Math rendering | [MathJax](https://docs.mathjax.org/en/v3.2/web/typeset.html) | Match the exporter's MathJax 3 configuration and macro asset |
| Flip and status controls | Mantine Card, Badge, SegmentedControl, Button, Alert, Loader | Explicit Front/Back state; clickable preview; visible build state |

## Alternatives

| Choice | Fit | Recommendation |
| --- | --- | --- |
| Mantine | Supplies the tree, layout, forms, dialogs, status and preview containers together | Use |
| Individually assembled headless components | Requires additional styling and composition for the same surface | Prefer the complete component library |
| CodeMirror source editing | Retains LaTeX and Markdown as text; exposes source positions | Use |
| [Tiptap Markdown](https://tiptap.dev/docs/editor/markdown) | Converts Markdown through an editor document model; its documented Markdown extension is beta and has preservation limits | Use only if rich text authoring is chosen |
| [remark/mdast](https://github.com/remarkjs/remark) | Mature parsing and transformation ecosystem; useful for source ranges | Zettlr's Lezer fork supplies Pandoc syntax and ranges in CodeMirror |
| Browser Markdown renderer plus KaTeX | Adds a second rendering interpretation and macro configuration | Reuse Pandoc card HTML and exporter MathJax |
| New Rust APKG implementation | Duplicates package generation, media and model ownership | Reuse ankdown |

## Source and export contracts

Local evidence: `README.md`, `justfile`, and the sibling checkout's
`ankdown/ankdown.lua`, `ankdown/cli.py`, and `ankdown/mathjax.html`.
The sibling checkout must be compared with the pinned exporter revision before wiring.

The paired-card filter validates `.front` and `.back` divs linked by `card-id`.
It supplies each complete side to Ankdown's filter as a block container.
Ankdown handles math, images, generated media, and card HTML.
Preview uses the same filter chain and math macros as export.

The CLI accepts an individual Markdown file with an explicit output path.
Directory builds map relative deck paths to filenames by replacing separators
with `__`. Regeneration uses the whole saved deck, including its metadata and media.
Process events can show a running indicator and real diagnostics. The current
CLI provides completion output rather than a percentage progress stream.

Each CodeMirror field edits only one div body. Keep the authored document around
that body. Zettlr's Lezer fork owns Pandoc syntax recognition and attribute
parsing. The app pairs sides by ID. Pandoc validates the same pairs for loading,
saving, preview, and export. Saves compare disk content to detect external edits.

## Generation state

Show separate indicators for an unsaved draft and the saved deck's package state.
Package states are Up to date, Unsynced, Generating and Failed.

A successful generation record contains hashes of the source, resolved media,
exporter revision, filter/model/macro assets, and resulting APKG bytes.
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

Selected: separate Front and Back editors with a card preview, built under `desktop/` in this
repository. The current request establishes a new desktop surface here; the
existing archive notice concerns the content maintenance location.

Alternative: a rich text editor using Tiptap, with additional extensions and
Markdown round-trip verification for the mathematical source corpus.

The desktop editor stores paired fenced divs linked by card ID. A native command
runs the pinned Python exporter bridge. The filesystem plugin watches the
selected workspace; the bridge owns file reads, saves and generation.
