# Math Flashcards desktop editor

The editor opens the folder containing the deck Markdown files directly.
Subject subfolders contain decks; the workspace's `apkg/` subfolder holds
generated Anki packages and is excluded from deck discovery.
Markdown files remain the authored source.

## Run

From the repository root:

```bash
just desktop-install
```

Build dependencies: Bun, Rust, Cargo, `just`, and the [Tauri Linux prerequisites](https://v2.tauri.app/start/prerequisites/).
Every build resolves each dependency to its latest version; the repository keeps
no lock files. The editor uses `@dzack/pandoc-editor` from the sibling
`Zettlr-pandoc-mathjax/packages/pandoc-editor` workspace package. Zettlr and
the card fields share its source. Keep that checkout beside this repository.
`just desktop-dependencies` clones Zettlr-Pandoc's Pandoc parser
package (`vendor/lezer-markdown-pandoc` in
[Zettlr-pandoc-mathjax](https://github.com/dzackgarza/Zettlr-pandoc-mathjax)) from
its `develop` branch into `desktop/.parser`, and the npm override makes CodeMirror
use the same parser as card pairing.
Installation needs `uv`, Pandoc, and network access to GitHub. Install/update
prepares the Python environment for the installed bridge path and saves its
interpreter location. It fetches the macro set and MathJax `stmaryrd` package
from pandoc-config main as one checked asset set. Opening, refreshing, loading,
and saving use these local resources. Package generation uses prepared local
renderer inputs through Ankdown. Missing runtime files produce an
installation error; run `just desktop-install` to prepare them.
Checks, review, and exports use the renderer assets loaded by the editor.
Install/update retains earlier asset sets for running sessions. Refresh or
return to the window after an update to see the restart notice. The next app
launch uses the updated set.
The native build includes the
bridge and local MathJax 4 assets, with the New Computer Modern font.
Installation adds **Math Flashcards** to the application menu and installs the
`math-flashcards` command. The commit gate ends with `just desktop-update`, which
rebuilds and installs the app, icon, launcher, and desktop entry. Each commit
that passes the gate therefore updates the app in the menu.

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

Ctrl-K searches deck names, card fronts, card backs, tags, and commands across
the workspace. Cards become searchable as background source reads finish.
The search field shows incomplete coverage until the reads finish, and shows
an error when a deck cannot be searched. Opening a card result reads the
current file and checks that the requested card still exists.
Search summaries and their exact source text are cached on disk by source digest
and parser version. Warm sessions reuse them after a current-file byte check.
The cache rebuild action also replaces these disposable records.
Package checks are cached as history. A gray tree marker means that current
inputs are being checked; its tooltip gives the previous result when available.
Only a completed current check supplies the package status. Review and update
can verify the complete workspace while other background work is incomplete.
File watches refresh the changed deck and packages that use the changed file.
Unrelated checked decks keep their results. Focus and manual refresh recheck
the workspace to cover missed notifications. A shared image change checks its
dependent packages without rereading unchanged deck sources.

The app opens the saved workspace on startup. On first launch it opens the
`decks/` folder in the repository used to build the app. Preferences use the standard Tauri store in
the XDG configuration directory.
Select the workspace name in the sidebar to open the workspace menu. Select
**Browse** or enter a workspace path to change it, then select a deck in the
tree. A dot after a deck name marks a deck whose Anki package is out of date.
Saved navigation can appear while the app reconciles directory membership.
The tree appears before workspace checks finish. A progress line shows the
checked coverage. Deck selection reads current file bytes independently of
package checks, and the package status shows **Checking Anki package…** until
verification finishes. Problems shows its own checked coverage while results
are incomplete. You can edit and save during these checks. Failed background
checks show an error and a retry action. Refresh uses local resources.
The card list shows its cards; select a card to edit its sides. **New** and
**Edited** mark the cards that the package does not contain yet.

Drag a card in the list to reorder it, or drop it on a deck in the tree to move it.
Ctrl-click toggles a card in the selection and Shift-click selects a range; dragging
a selected card moves the whole selection. A folder opens while a drag hovers over it.
Drag a deck onto another deck and confirm to merge them. **New deck** creates an
empty deck that can receive cards. **Undo** reverses the last organization
operation. Right-click a deck to update its package, review its changes, rename
it, or delete it; a folder offers a new deck in that folder. Renaming a deck
whose title comes from its path changes the title too. Deleting a deck sends the
deck file and its package to the trash. See [card organization](../docs/card-organization.md)
for the design sources and file operations. Relative media links follow their
original files across moves.
Ctrl-K opens a command menu that finds decks, cards, and actions. **Find a
card** filters the card list by front and back text. Edit **Front** and **Back** in
side-by-side CodeMirror fields. Both fields use Zettlr's shared Pandoc editor,
including list indentation, emphasis, headings, blockquotes, code, and TeX.
Set tags with **Tags**.
The app creates the card ID and stores the sides as paired fenced divs.
Each side can contain paragraphs, lists, math, and nested divs.

A deck contains `.front` and `.back` divs with a shared `card-id` attribute.
Pairs can appear in any order; fronts set the card order. Missing sides,
duplicate sides, and missing IDs are errors. See the [format](../README.md#card-format).

Math renders in place with MathJax and the exporter's macros, using the shared
editor's equation renderer. Click an equation, or move the cursor into it, to edit its
source. Saves and organization changes check each deck with the exporter's
Pandoc filter and media resolution.

An equation that MathJax cannot render shows the TeX error in red. An undefined
macro is an error, as in LaTeX. **Problems** at the bottom of the sidebar shows
the number of problems in all decks and opens a list of them, grouped by deck:

| Problem | Meaning |
| --- | --- |
| LaTeX | An equation does not render; the list shows the TeX error and the equation source |
| Card structure | The deck has an unpaired side, a duplicate side, or a missing ID |
| Empty answer | A card has no back; the exporter rejects it |

Select a problem to open its card. A red dot in the deck tree marks a deck with
problems, and **Problem** marks each card with problems in the card list. The
list follows the saved decks.

Use **Add card** or **Delete card** to change the deck. Edits save to the deck
file shortly after typing stops. Ctrl-S, switching decks, organization changes,
package updates, and closing the window save at once. A deck with invalid card
structure stays unsaved until it is corrected.

The app owns the deck files but does not lock them. When another program changes
the open deck, the editor shows the file. When the file changes while edits are
waiting to save, the save stops and a banner offers **Use the disk version** or
**Keep my version**.

The menu button at the right of the toolbar holds the deck actions:

| Action | Operation |
| --- | --- |
| Update Anki package | Builds the whole deck and replaces its package after the exporter succeeds; disabled when the package is up to date |
| Review changes | Lists the cards that the package lacks |
| Rename deck… | Renames the deck file and its path-derived title |
| Delete deck… | Sends the deck file and its package to the trash |
| Update all Anki packages | Updates every out-of-date package in the workspace |

**Generation output** shows the exporter result or error.

The toolbar shows one status:

| Status | Meaning |
| --- | --- |
| Saving… | Edits are waiting to be written to the deck file |
| Not saved: … | The edits cannot be saved; the text gives the cause |
| N changes not in the Anki package | Cards were added, edited, or removed after the package was generated |
| A reason, such as "The Anki package file changed after generation." | The package is out of date for a reason other than card changes: no package, missing or changed package file, card order, media, or exporter |
| Anki package up to date | Deck, referenced local media, exporter assets, and package bytes match the last successful build |
| No cards to export | The deck has no cards, so it has no package |
| Updating the Anki package… | The exporter is running |
| Generation failed | The last update failed; the previous package remains |

Select the status to review the changes. The review compares the deck with the
deck source that produced the package. It pairs cards by `card-id` and shows the
old and new text of each changed side. Select a card in the review to open it.
**Update Anki packages** at the bottom of the sidebar shows the number of
out-of-date decks and opens the same review for all of them.

Preferences use Tauri's app configuration directory. Build records, including
the deck source of each build, use the platform cache directory under
`math-flashcards/builds.sqlite3`. A deck without a build record is out of date
until the app generates its package. Filesystem watches refresh the status and
the open deck after workspace changes.

Saved navigation and reusable Problems results use `math-flashcards/derived.sqlite3` in the platform
cache directory. Reuse requires the same source bytes, checker, parser, and
renderer assets. A changed file is checked again even if its size and
modification time stay the same. Cache damage shows **Rebuild cached data**.
This action clears disposable results and checks them again. It preserves deck
files, Anki packages, preferences, and successful build records.

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
| `just desktop-test startup` | Edit and save during incomplete workspace coverage |
| `just desktop-organization-test` | Tree drag, grouped moves, reorder, merge, new decks, rename, delete, Undo, and updating all packages |
| `just desktop-native-test` | Built native window and export on an isolated X11 display |
| `just desktop-format` | Canonical Python, TypeScript, CSS, and Rust formatting |
| `just check-math` | The Problems list for every deck in the repository; fails when it is not empty |

The commit gate runs the deck check, the math check, frontend build, source corpus check, and
browser scenario. The browser checks install the Chromium build of the
Playwright version they resolve.
Native capture requires Xvfb and xdotool. Screenshots, the browser trace, and
diagnostic logs are generated in `desktop/test-artifacts/`.

The browser scenario checks card typing, inline math, source preservation,
automatic saves, the change review, delete, package contents, package status,
disk changes to the open deck, save conflicts, failed export preservation, and
the Problems list. The native scenario runs the built executable with
disposable deck copies and isolated app data.
