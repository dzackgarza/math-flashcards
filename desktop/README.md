# Math Flashcards desktop editor

The editor opens a workspace with a `decks/` folder and writes generated Anki
packages to its `apkg/` folder. Markdown files remain the authored source.

## Run

From the repository root:

```bash
just desktop-install
```

Build dependencies: Bun, Rust, Cargo, `just`, and the [Tauri Linux prerequisites](https://v2.tauri.app/start/prerequisites/).
Runtime dependencies: `uv` and Pandoc on `PATH`. The first backend call fetches
the locked Python dependencies, including the pinned Ankdown exporter.
The native build includes the bridge, its dependency lock, and local MathJax assets.
Installation adds **Math Flashcards** to the application menu and installs the
`math-flashcards` command. Run `just desktop-update` from this checkout to rebuild
and update the app, icon, launcher, and desktop entry.

| Installed item | Location |
| --- | --- |
| Desktop entry | `$XDG_DATA_HOME/applications/dev.math.flashcards.desktop` |
| App and resources | `$XDG_DATA_HOME/math-flashcards/` |
| Icon | `$XDG_DATA_HOME/icons/hicolor/128x128/apps/dev.math.flashcards.png` |
| Command | `~/.local/bin/math-flashcards` |
| Preferences | `$XDG_CONFIG_HOME/dev.math.flashcards/preferences.json` |

Unset XDG data and configuration directories use `~/.local/share` and `~/.config`.
The launcher supplies the installed `uv` and Pandoc directories to the app.
The installed app runs independently of the source checkout. `just desktop-deploy`
refreshes the installation from an existing build.

## Use

The app opens the saved workspace on startup. On first launch it opens the
repository used to build the app. Preferences use the standard Tauri store in
the XDG configuration directory.
Select the workspace name in the sidebar to open the workspace menu. Select
**Browse** or enter a workspace path to change it, then select a deck in the
tree. A dot after a deck name marks an unsynced package. The card list shows its cards; select a card to edit its sides.

Drag a card in the list to reorder it, or drop it on a deck in the tree to move it.
Ctrl-click toggles a card in the selection and Shift-click selects a range; dragging
a selected card moves the whole selection. A folder opens while a drag hovers over it.
Drag a deck onto another deck and confirm to merge them. **New deck** creates an
empty deck that can receive cards. **Undo** reverses the last organization
operation. These changes save immediately; save or reload a deck with unsaved
edits before moving its cards. See [card organization](../docs/card-organization.md)
for the design sources and file operations. Relative media links follow their
original files across moves.
Ctrl-K opens a command menu that finds decks, cards, and actions. **Find a
card** filters the card list by front and back text. Ctrl-S saves the deck. Edit **Front** and **Back** in
side-by-side CodeMirror fields. Both fields accept Markdown and LaTeX, with
Pandoc syntax and TeX highlighting from Zettlr's parser. Set tags with **Tags**.
The app creates the card ID and stores the sides as paired fenced divs.
Each side can contain paragraphs, lists, math, and nested divs.

A deck contains `.front` and `.back` divs with a shared `card-id` attribute.
Pairs can appear in any order; fronts set the card order. Missing sides,
duplicate sides, and missing IDs are errors. See the [format](../README.md#card-format).

Math renders in place with MathJax and the exporter's macros, using a renderer
adapted from Zettlr. Click an equation, or move the cursor into it, to edit its
source. Saves and organization changes check each deck with the exporter's
Pandoc filter and media resolution.

Use **Add card** or **Delete card** to change the deck. **Save deck** writes the
complete source file. Switching decks, reopening the workspace, reloading, and
closing the native window ask about unsaved changes. A save rejects a disk edit
made after the document was loaded. Reload the deck to read that external edit.

Select **Generate Anki deck** after saving. It builds the entire selected deck
and publishes the package after the exporter succeeds. Generation output shows
the exporter result or error. An empty answer is an export error.

The toolbar shows **Unsaved changes** while the deck has unsaved edits, and
otherwise the package state:

| State | Meaning |
| --- | --- |
| Up to date | Source, referenced local media, exporter assets, and package bytes match the successful build |
| Unsynced | The draft or saved inputs differ, the package differs, or there is no verified build record |
| Generating | The exporter is running |
| Failed | The last export attempt failed; the previous package remains |

Preferences use Tauri's app configuration directory. Build records use the platform cache
directory under `math-flashcards/builds.sqlite3`. Existing packages start as
Unsynced until the app generates a verified package. Native filesystem watches
refresh saved package status after workspace changes.

## Anki import

Import the generated `.apkg` with Anki's File → Import command.
The exporter derives note IDs from card content. Editing a card changes its ID.
Importing a regenerated package can add a replacement note while retaining the
old note. Removing a source card removes it from the generated package.
The package status describes the file, not the live Anki collection.
See [Anki's packaged deck documentation](https://docs.ankiweb.net/manual/importing/packaged-decks).

## Development and verification

| Command | Operation |
| --- | --- |
| `just desktop-dev` | Native Tauri development window |
| `just desktop-web` | Browser editor with the real backend on localhost |
| `just desktop-frontend` | TypeScript check and frontend build |
| `just desktop-source-test` | Side preservation, pair validation, and agreement with Pandoc |
| `just desktop-test` | Managed browser scenario with real filesystem edits and real APKG generation |
| `just desktop-organization-test` | Tree drag, grouped moves, reorder, merge, new decks, Undo, and conflicts |
| `just desktop-native-test` | Built native window and export on an isolated X11 display |
| `just desktop-format` | Canonical Python, TypeScript, CSS, and Rust formatting |

The commit gate runs the deck check, frontend build, source corpus check, and
browser scenario. Browser checks require Playwright Chromium; provision it with
`uvx --from playwright==1.58.0 playwright install chromium`.
Native capture requires Xvfb and xdotool. Screenshots, the browser trace, and
diagnostic logs are generated in `desktop/test-artifacts/`.

The browser scenario checks card typing, inline math, source preservation, save,
delete, package contents, package status, external save conflicts, and failed
export preservation. The native scenario runs the built executable with
disposable deck copies and isolated app data.
