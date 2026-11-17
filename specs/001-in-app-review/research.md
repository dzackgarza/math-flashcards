# Research: In-App Review

Sources: Anki source at commit `827f4aa4` (version 26.09.4), the PyPI `anki` 26.9.4 wheel,
and probes run against that wheel on 2026-11-16. Each fact below is marked **probed**
(a script ran against the wheel), **read** (found in the source), or **inferred**.

## R1. Scheduler source

**Decision**: Add the PyPI `anki` wheel to the bridge dependencies in `desktop/backend.py`.
The bridge drives Anki's `Collection` and its v3 scheduler with FSRS.

**Rationale**:

- The wheel contains Anki's compiled Rust core. It needs no Rust build, no `protoc`, and
  no submodules. It resolves beside the current bridge dependencies on Python 3.14
  (probed).
- The measured costs fit the spec: `import anki` 0.115 s; process start, import, open,
  and queue fetch together 0.20 to 0.24 s; reopening a collection 0.002 s; adding 3,300
  notes in one batch 0.06 s (probed).
- The wheel does not load the parts the request excludes. Sync, add-ons, the editor, and
  Anki's Qt interface are in the wheel or in the separate `aqt` package, but nothing
  calls them.

**Alternatives considered**:

| Alternative | Result |
| --- | --- |
| Link Anki's `rslib` crate into the Tauri binary, as AnkiDroid does | Rejected for now. It removes Python from the review path but needs Anki's pinned Rust toolchain, `protoc`, the translation submodules, and a second bridge. `rslib` has `publish = false`; the crates.io `anki` crate is a stub. Reconsider only if SC-002 fails. |
| Fork `rslib` and remove sync, import/export, and media code | Rejected. About 77,000 Rust lines to keep in step with upstream, against the rule that vendored code is not modified. |
| A standalone FSRS library (`fsrs` crate, `fsrs` on PyPI, `ts-fsrs`) | Rejected. FSRS gives intervals only. Queues, learning steps, daily limits, the day boundary, undo, and the history store would be hand-written copies of Anki behaviour (FR-005). |
| Embed Anki's web reviewer pages | Rejected. They post to `/_anki/*` endpoints of Anki's Qt media server and render with Anki's card templates. |

**Constraints**:

- Anki is AGPL-3.0-or-later. This repository has no licence file and the app runs on one
  machine. If the app is distributed, the combined work comes under AGPL terms (inferred
  from the licence text; not legal advice).
- Dependencies track latest, so an update can install a newer `anki` that upgrades the
  collection format. An earlier release that stays on disk for a running window can then
  fail to open the store (inferred). R3 makes that failure visible.

## R2. Card identity

**Decision**: One scheduling note for each native card. Its GUID and sole `CardId`
field hold the native `card-id`; one template gives Anki one schedulable card.
The app owns front and back source, rendering, and content history.

**Rationale**: Anki accepts an arbitrary string as a GUID and finds the note by it
(probed). The 3,278 front `card-id` values in 68 decks have no duplicate. Updating a
note's fields after a review keeps the interval and the FSRS memory state (probed).
Native IDs preserve identity across edits, moves, and reorders.

**Alternatives considered**: Content-derived identity resets history on each edit.
Identity by deck path and position resets history on moves and reorders.

**Consequence**: Study takes `id`, `front.value`, `back.value`, and tags from the
editor's existing `cards()` parser. The front and back remain native Markdown.
Anki supplies the scheduling identity and state; the learning record holds each
content version and the latest `card_change` selects the current version.

## R3. Process model

**Decision**: One long-lived study process. The app runs as one copy (R15), so the app
has one host. The native shell starts `backend.py study-host` on the first study request
and keeps it. The process holds the collection open and answers one JSON request per
line. It is the only process that opens the collection or writes the record. All other
bridge requests keep the current model: one new process for each request.

**Rationale**:

- Anki keeps undo steps in memory (`UndoManager`, read). After close and reopen,
  `undo_status()` is empty while the review log row remains (probed). Undo (FR-021)
  therefore needs the collection to stay open between the grade and the undo.
- Anki rejects an answer for a card that is not at the top of its in-memory queue
  ("not at top of queue", read). A held collection keeps one queue for the session.
- The FSRS switch is read when a queue is built. It must be set before the first queue
  build (probed). The host sets it when it creates the store.
- Anki opens its collection with SQLite's exclusive locking mode
  (`rslib/src/storage/sqlite.rs`, read). While the host runs, no other process reads the
  collection. Every reader outside the host therefore reads the learning record (R12),
  not the collection.
- A grade is durable when `answer_card()` returns: after `SIGKILL` with no `close()`,
  the review log row and the new card state are in the store (probed, SC-005).

**Alternatives considered**:

| Alternative | Result |
| --- | --- |
| One process for each request, as today | Rejected. Undo is lost between requests. A hand-written undo would copy Anki behaviour. |
| Open the store for a session only and release it when idle | Rejected. Undo would end at a time the user cannot see, and deck counts would need a second access path. |
| A Tauri sidecar binary | Rejected. The bridge is a Python script in a prepared environment; the installer already owns that runtime. |

**Consequences**:

- `desktop/src-tauri/src/lib.rs` and `desktop/vite.config.ts` both route requests. Each
  gets one study route that owns the host process. Study requests run one at a time.
- A release update leaves the running host on its own release environment, as for the
  renderer assets. The next launch uses the new release.
- When the store cannot be opened, each study request fails with a message that names
  the store path and the cause.

## R4. Store location and backups

**Decision**: `platformdirs.user_data_path("math-flashcards") / "study" / <store ID>`.
The store ID is a UUID made when the store is created. The directory holds
`collection.anki2`, Anki's `collection.media`, the learning record (R12),
`record-media/` for retained media, `record-assets/` for retained shared editor assets,
a `store.json` with the store ID and every workspace path the store was attached to, and
`backups/`.

**Store identity**: A store belongs to a workspace, not to a path (FR-041). At open, the
host looks for the store whose current attached path is the workspace path.

| Stores on disk | A store has this path | Result |
| --- | --- | --- |
| None | | A new store is created. |
| One or more | Yes | That store opens. |
| One or more | No | The host returns the list of stores. The user attaches one to this path or starts a new one. |

A store keyed by a digest of the path, the first design, starts an empty history when
the folder is renamed or the data moves to another machine. Over decades both occur.

**Rationale**:

- All current app state is in `user_cache_path("math-flashcards")`. **Rebuild cached
  data** sends cache files to the trash. Review history is not a cache (FR-018).
- The installer owns `$XDG_DATA_HOME/math-flashcards/` and writes `releases/`, `active`,
  and `launch` there. It creates a new release directory and does not remove other
  entries (read in `desktop/linux/install.py`).
- One directory holds everything that cannot be regenerated. A copy of that directory is
  a complete copy of the history, and it attaches to any path on any machine.
- `Collection.create_backup(backup_folder=..., force=..., wait_for_completion=...)`
  writes `backup-YYYY-MM-DD-HH.MM.SS.colpkg` (probed). Anki's backup limits control how
  many are kept.

**Backup lifecycle**: On first load and graceful host shutdown, call
`create_backup(force=False, wait_for_completion=True)`. Anki skips unchanged
collections and enforces its minimum interval. Its
[backup implementation](https://github.com/ankitects/anki/blob/main/rslib/src/collection/backup.rs)
uses local time to name the package and can replace a package within the same second.
Compare file metadata before and after the call to identify its output. Do not
construct a second timestamp. Append the `backed-up` event and use
[SQLite's online backup](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.backup)
to write the record to a temporary file, then replace the matching `.sqlite3` snapshot.
The host processes requests sequentially, so grades cannot interleave with this pair.
Anki thins its packages; send only record snapshots whose matching package is absent
to the trash. Backup failures propagate and remain in the host diagnostics.

`desktop/tests/study-preservation.py` exercises open and EOF shutdown through the
real host, compares every snapshot row, and lets Anki remove an expired pair. It also
checks that cache rebuilding preserves the live store and that a leech review stays
available. A forced process termination is not evidence for graceful exit backups.

**Alternatives considered**: A folder inside the workspace: rejected, it puts a binary
database in the deck repository and in deck discovery. `XDG_STATE_HOME`: rejected, the
XDG specification describes it for data that is less important than user data.

**Test rule**: Every test that starts the bridge sets `XDG_DATA_HOME` to a temporary
directory. `desktop/tests/organization.py` and `desktop/tests/native.py` already do. The
`desktop-test` recipe isolates cache, data, and state directories so tests retain no
learning or diagnostic data in the user's application directories.

## R5. Deck mapping

**Decision**: Each deck file maps to one Anki deck named from its workspace path:
`Workspace::<hex folder>::…::<hex filename>`. Encode each complete path component's
UTF-8 bytes with Python's [bytes.hex()](https://docs.python.org/3/library/stdtypes.html#bytes.hex),
including the filename extension. Folders are parent decks. `Workspace` is the root
deck; studying the workspace selects it. The window and learning record use native
paths, never these internal names.

**Rationale**: The app's tree shows folders and files, and the spec's scopes are deck,
folder, and workspace. `deck_due_tree()` returns nested new, learning, and review counts
for `A::B` names (probed). Anki has no command that studies every deck; a root deck
gives one. The collection is internal, so its deck names need not equal the deck titles
in the packages.

[Anki's name parser](https://github.com/ankitects/anki/blob/main/rslib/src/decks/name.rs)
splits `::`, normalizes Unicode, and trims whitespace and colons. Encoding preserves
the identity of native path components through those operations. Keeping the extension
also distinguishes `Algebra.md` from the folder `Algebra/`. Removing it puts the
standalone deck's cards inside the folder's study scope. Counts use Anki's due tree
and the synchronized native paths to recover the window's folder and file hierarchy.
An unchanged sync checks that its scheduling deck exists; reconciliation moves existing
cards to that deck with `set_deck`, preserving their identity and learning history.

**Alternatives considered**: Names from the `title` metadata: rejected, titles need not
follow the folder tree that the user selects from.

## R6. Deck changes to the store

**Decision**: One operation, `study-sync`, makes the store agree with the saved decks.
It is state-based: it compares each deck's inputs with the inputs recorded at its last
sync and reads only the decks that differ. The frontend calls it at workspace open,
after a save, after a file-watch event, and before a session starts.

**Rationale**:

- The source bridge supplies saved deck text and its digest. The store tracks that
  digest, native media digests, and the shared editor asset identity for each deck.
- A state comparison needs no event history. A missed file notification or a store that
  was in use is corrected by the next call.
- The Anki operations exist: `add_notes` (batch), `update_notes(skip_undo_entry=True)`,
  `set_deck`, `suspend_cards`, `unsuspend_cards`, `decks.remove` (read and probed).

**Rules**:

- The window reads saved source through the existing source bridge and parses cards
  with `desktop/src/cards.ts`. It sends native cards, deck metadata, a source digest,
  and the complete deck inventory. The host checks each source digest against disk
  before accepting the batch. A changed file is read and parsed again.
- Anki's `CardId` field identifies the native card. The learning record holds its
  front and back source and media; the editor's shared renderer displays it.
- One call syncs at most eight decks and reports how many decks remain, as the current
  batch requests do. The host stays free for a grade between calls, and the screen shows
  progress on the first sync.
- A card ID that a synced deck contains and that the store records in a deck that is not
  current is a move. The same ID recorded in a current deck is a duplicate.
- A card that leaves a deck in one call and enters another deck in a later call is
  removed, then restored. Its schedule is the same at the end.
- Sync sets the deck tags and card tags of a note and keeps the tags that Anki's
  scheduler set (`leech`) (FR-045).
- Each add, content change, tag change, move, removal, and restore is one `card_change`
  row in the learning record, and each new front or back is one `content` row (R12).
- A removed card is suspended and moved to the deck `Removed`, outside `Workspace`.
  Removing an Anki deck deletes its cards; suspended cards that were moved out first
  survive the removal (probed). A card ID that returns is moved back and unsuspended.
- A deck that fails to render keeps its last synced cards. The result lists the deck.
- The complete inventory includes paths whose source cannot be parsed. Only valid
  native deck values enter a batch. This distinction preserves a failed deck's
  recorded cards while allowing other decks to sync; an absent inventory path
  means the deck was removed.
- A card ID in two decks is reported with both paths. The note stays with the deck that
  had it first.

Study saves valid pending edits before reading the saved decks. An invalid structural
draft stays in the editor while Study reads the last saved source. The Problems list
includes that live draft error without caching it under the saved file's digest; its
row returns to the existing draft. Other operations that require saving still reject
an unsaved deck. The draft's known card identity continues to identify its editor view.

**Alternatives considered**: Sync from frontend edit events alone misses external edits.
The file watcher and saved-source comparison cover both paths.

Native batches include per-card image references found by the existing Lezer Pandoc
parser. [`yaml`](https://eemeli.org/yaml/#parsing-documents) reads the contents of its
metadata nodes; [`micromark-util-decode-string`](https://github.com/micromark/micromark/tree/main/packages/micromark-util-decode-string)
decodes Markdown URL escapes and character references. The core receives these native
values, verifies the saved-source digest, and reads the referenced local files. Shared
asset descriptor validation lives in `desktop/rendering.py`, used by both the editor
bridge and Study. Its validated descriptor is retained under its identity in
`record-assets/`; media bytes are retained under their digest in `record-media/`.

## R7. Media

**Decision**: The app resolves native image references relative to the saved deck and
retains each referenced file under its digest in `record-media/`. The record maps the
authored reference to those bytes for each content version. The native shell and Vite
serve the recorded media to the shared editor renderer. TikZ-cd source uses the same
diagram renderer as the editor.

**Rationale**: A later file replacement must preserve the media shown in an earlier
review. The content record owns this association (FR-030).

[CommonMark image references](https://spec.commonmark.org/0.31.2/#images) resolve
through definitions in the containing document, including explicit, collapsed,
and shortcut labels. A front can use a definition authored on the back or another
card. Parsing a face alone loses that context. The native deck parser therefore
resolves references before splitting the display into faces; `image_reference`
retains the labels and authored URLs used by each content version. The shared
face receives this mapping alongside the retained file paths. The face text stays
exactly as authored. Schema version 2 adds the mapping table; historical rows
remain intact, and newly resolved context creates a new content version.

The editable face and Study use the same image widget and native reference parser.
The editor resolves authored URLs against its open workspace and deck directory;
Study resolves them through the retained content mapping. Opening a workspace grants
the native asset protocol and the browser media route read access to that workspace.
Browser media routes check both the requested path and its resolved filesystem path.
A source revision in image URLs refreshes previews after a file change. An incomplete
image reference gives an editor diagnostic while its source remains editable.
Image widgets report resolution and decoding errors in their visible content. They
must not throw from the editor's transaction: the transaction runs before `onChange`
can supply the new source and its media mapping. Once that mapping arrives, the shared
renderer replaces the diagnostic with the resolved image.

The browser route uses [`mrmime`](https://github.com/lukeed/mrmime#lookupinput) to resolve
the authored filename's standard MIME type. Its dictionary derives from `mime-db`;
unknown extensions return no type and the route reports 415. A digest filename alone
cannot recover that type. Vite's internal MIME lookup is private, and a second
hand-maintained extension table would duplicate the dependency. Both browser and native
routes grant access only after a store opens, to that store's retained media and assets.

The face fetches retained bytes and creates a Blob with the MIME type resolved from
the authored filename. Tauri's `tauri-utils/src/mime_type.rs` cannot infer SVG from
bytes and uses the path extension; a digest path therefore needs an explicit type.
The image widget releases its object URL on destruction. The shell permits asset
fetches and Blob images in its content security policy. The native Study scenario
exercises SVG through this path and compares the completed grades with both stores.

## R8. Card display

**Decision**: The study screen renders native card source with the shared editor
renderer in read-only mode. It uses the same local MathJax, macros, diagram rendering,
and image handling as the editor, with media resolved from the content record.

**Rationale**: `cards()` already provides the exact authored source of each side, and
`SideEditor` already uses `@dzack/pandoc-editor`. The full card face, rather than the
card-list summary, is the presentation owner (FR-009, SC-007).

The image widget uses the shared editor's `renderBlockWidgets` service and the
`WidgetType` construction of its `render-math.ts`. Source syntax remains owned by
the shared parser. Vite explicitly pre-bundles the lazy face's deep renderer import
and image dependencies: [dependency discovery](https://vite.dev/config/dep-optimization-options#optimizedeps-include)
must not reload a window during a session.

## R9. Scheduling settings

**Decision**: One Anki deck-options preset for all decks, with these values set when the
store is created:

| Setting | Anki key | Value |
| --- | --- | --- |
| FSRS | config `fsrs` | on |
| Limits start from the top deck | config `applyAllParentLimits` | on |
| New cards per day | preset `new.perDay` | Anki default (20), user-set |
| Reviews per day | preset `rev.perDay` | Anki default (200), user-set |
| Target recall | preset `desiredRetention` | Anki default (0.9), user-set |
| Leech action | preset `lapse.leechAction` | 1, tag only |
| Review order | preset `reviewOrder` | 7, ascending retrievability |
| Limit of recorded answer time | preset `maxTaken` | 9999 s, Anki's maximum |
| Maximum interval | preset `rev.maxIvl` | Anki default (36500 days) |

**Rationale**:

- With `applyAllParentLimits` on and a limit of 5, the root deck and each child show at
  most 5 new cards, and one answered card lowers all of them (probed). This makes the
  new-card limit a limit for the workspace (FR-023).
- A suspended leech would leave review, which FR-024 forbids. A new collection's preset
  reports `leechAction` 1 (probed); the store sets it and does not depend on the default.
  The `leech` tag marks a weak card, so deck sync keeps it (FR-045, R6).
- `fsrs` and `applyAllParentLimits` are not in the protobuf `ConfigKey.Bool` enum; they
  are set by their string keys (probed).
- Review order. Anki's default is "Due date, then random", which its manual recommends
  for a collection that is up to date. With FSRS on, the manual gives "Ascending
  retrievability" as the order that shows first the cards the user is most likely to have
  forgotten, and recommends that kind of order for a backlog
  (https://docs.ankiweb.net/deck-options.html, read 2026-11-16). FR-044 asks for that
  order whenever the due reviews exceed the day's study: the cards the user knows best
  wait longest. When the user finishes every due card, the order changes no schedule.
  `reviewOrder` is the preset key and 7 the proto value. The real-window scenario
  `desktop/tests/study-settings.py` prepares five dated review states with distinct
  FSRS stability through Anki's library. Their recorded `before_retrievability`
  values increase strictly in the offered order, including across a daily-limit
  increase. This establishes the queue behaviour for that fixture, not a learning
  outcome for advanced mathematics.
- Anki limits the answer time it records to `maxTaken`, 60 s by default: an answer of
  200 s was stored as 60 s (probed). The manual states that the time does not affect
  scheduling. Anki accepts 1 to 9999 (read). The store sets 9999 so that Anki's own log
  loses less; the learning record keeps the measured time with no limit (R13).
- The 100-year maximum interval fits the time scale of the purpose and stays.

The form updates preset 1 with `decks.update_config`; Anki invalidates its own
queues after the operation (`anki/decks.py`, `anki/scheduler/v3.py`, installed
wheel). It refreshes the current presentation so its offered intervals and recorded
settings agree. A finished session starts a new session when settings make cards
available. Unchanged values create no `setting_change` rows. Invalid values return
`InvalidSettings` without changing the preset or record.

The [Anki deck-options manual](https://docs.ankiweb.net/manual/deck-options)
describes shared presets, daily limits, and target recall. New-card introductions
also consume the review limit with the default configuration; the UI preserves
this rule. The settings scenario isolates due-review limits in a separate store
and proves that increasing target recall shortens the Good interval for an
unchanged card state. These are scheduler semantics, not evidence that the default
limits or target are optimal for this user's learning.

## R10. Session behaviour

The window uses its existing Mantine controls and shared `SideEditor` for the
Study presentation. The workspace menu and command search open the session after
saving and synchronizing the source. Short read-only faces use their content height
so the grading controls remain visible. Following the
[GNOME button guidelines](https://developer.gnome.org/hig/patterns/controls/buttons.html),
the reveal action is prominent and the four grade buttons have equal widths and
equal visual weight. Anki supplies their interval labels; styling does not recommend
a grade.

**Decision**: The host follows Anki's reviewer sequence: `get_queued_cards(fetch_limit=1)`
for the card and the three counts, `describe_next_states()` for the four labels,
`build_answer()` and `answer_card()` for a grade, `undo()` for Undo, and
`congratulations_info()` when the queue is empty.

**Rationale**: All calls work on the wheel (probed, except `congratulations_info`, read).
The labels contain Unicode isolation marks around numbers; the screen shows them as
given. `CongratsInfo.secs_until_next_learn` tells the screen when a learning card
returns (US1 scenario 7).

**Record rule**: The host writes the `presentation` row before it returns a card, and
the `response` row after `answer_card()` returns and before it returns the next card. A
session has explicit `study-begin` and `study-end` requests, so that the record holds
the start, the scope, and the end of each session (FR-032).

The wheel's `anki/scheduler/v3.py` and `scheduler_pb2.pyi` define the call inputs
and state units: learning and relearning offers use seconds; review offers use
days. The host selects the scope's Anki deck before queue access and reads each
grade's committed `revlog` row. Import `anki.collection` before `anki.cards` or
`anki.models`: those modules otherwise enter a circular import through Anki's
generated hooks. These are library integration rules, not learning policies.

**Undo rule**: Undo is offered when Anki's `undo_status().undo` names the answer
operation. Deck sync writes notes with `skip_undo_entry=True` where Anki offers it; other
sync operations add undo steps, so Undo is unavailable after a sync until the next grade
(FR-021).

Anki's [operation labels](https://github.com/ankitects/anki/blob/main/rslib/src/ops.rs)
map the answer operation to `actions_answer_card()`. Compare against that translation,
not a hard-coded English label. Its [undo manager](https://github.com/ankitects/anki/blob/main/rslib/src/undo/mod.rs)
returns the operation's counter from `undo()`. `undo_status().last_step` is the sequence
counter, not the current top entry after an undo. The host associates each newly graded
operation counter with its response row, then uses the returned counter to append the
matching `undo` row. These associations last only for the open host and are cleared
when a sync changes cards. Anki owns the undo stack and the restored schedule.

The finished screen has already ended its session. Undo from that screen begins a new
session with the same scope before restoring the card. Both session boundaries remain
in the record. Editing from an unfinished session keeps that session open; returning
saves the edit, synchronizes native source, and fetches its current presentation.

## R11. Test method

The native shell uses [Tauri's logging plugin](https://v2.tauri.app/plugin/logging/)
with a folder target at `math-flashcards/diagnostics/native` below
[`dirs::state_dir()`](https://docs.rs/dirs/latest/dirs/fn.state_dir.html).
The plugin's default Linux log target uses the data directory; the explicit folder
target applies the constitution's state placement. `KeepAll` retains rotated logs.
Native events record app release, process and platform context, host lifecycle,
request action, elapsed wall time, and failures. Each completed request and app exit
flushes the logger. Request timing includes queue and child-process waits; the Python
host's profiles supply the nested Python costs. Native library internals remain outside
these profiles.

The Study host writes operation events and `cProfile` files under the library-resolved
XDG state directory. Each process records its app and Anki versions, Python and platform,
and source digests. Each operation records an input digest, start and completion times,
outcome, and a profile; errors include their traceback. The record of learning remains
in the data directory. Removing diagnostic files cannot change that record.

Python's standard [logging](https://docs.python.org/3/library/logging.html) and
[profiling](https://docs.python.org/3/library/profile.html) libraries supply this capture.
Profiles include nested Python work and the total time of calls into Anki's native
library; they do not resolve the native library's internal call stacks. This limit must
remain explicit in timing comparisons. Test runners retain the server output and state
directory after server termination, before deleting the isolated directories.

Native host-lifecycle checks wait for a terminated child to reach the exited state
before sending the next bridge request. On Unix,
[`psutil.Process.wait`](https://psutil.io/api/#psutil.Process.wait) waits for a non-child
PID to disappear; the native parent reaps its child when the next request calls
`try_wait`. Waiting for disappearance before that request creates a test dependency
cycle. The test must still verify that the old PID is reaped, the store is unchanged,
and a new writer is recorded after reopening.

Singleton checks move keyboard focus away from the app and require the next launch to
restore it with the same sole window. Direct X window unmapping is not a GTK hide
operation and does not establish the application's visibility state.

Normal-exit checks close the native window before deleting the WebDriver session.
[WebKit's GLib session host](https://github.com/WebKit/WebKit/blob/main/Source/WebDriver/glib/SessionHostGlib.cpp)
force-exits its browser subprocess during session teardown. Deleting that session
cannot establish that Tauri's exit callback closed the Study host and flushed its logs.
The native scenario requires those events before releasing the automation session.

Focus timing uses a headed browser on an isolated X display. Playwright's Chromium
driver enables focus emulation for each page; tests disable that emulation through
[`Emulation.setFocusEmulationEnabled`](https://chromedevtools.github.io/devtools-protocol/tot/Emulation/#method-setFocusEmulationEnabled)
before changing X window focus with `xdotool`. The test observes the document's focus
state before measuring the interval away, then returns focus to the original window.
Synthetic focus events would not establish the window's actual state.

**Decision**: A Playwright scenario, `desktop/tests/study.py`, drives the real window
served by `just desktop-web` with the real bridge, real deck files in a temporary
workspace, and temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME`. It is a recipe in
`just test-commit`. The scenario reads the store with the `anki` library to check
results, reads the learning record with Python's `sqlite3`, and prepares due cards with
`sched.set_due_date()` while the app is stopped. `set_due_date()` writes a `revlog` row
of type 4 (probed); the host records it at the next open as a recovered row (R12).

Anki's open collection holds an exclusive database connection. Inspect its committed
state after stopping the isolated test host, then use SQLite's backup API to include
committed WAL contents in a disposable copy before opening that copy with Anki. The
app's separate record supports concurrent SQL readers throughout the scenario. This
keeps the test on the real storage path without sharing Anki's connection.

The host receives the app version from its launcher: Tauri's package information in the
native shell and the package manifest in Vite. Installed resources need no source-tree
manifest. The study command selects its imports before the other bridge commands load
their dependencies.

**Rationale**: This is how `desktop/tests/workbench.py` proves package generation. Anki
has no supported clock override for other processes (`PYTHON_UNIT_TESTS` only shifts
the day rollover, read), so a test changes due dates, not the clock.

## R12. Learning record

**Decision**: A second SQLite database, `record.sqlite3`, in the store directory. The
app owns its schema. The host is its only writer and only inserts rows. The database
uses SQLite's write-ahead log, so that other programs read it while the host writes.

**Rationale**: The purpose needs a complete, permanent record that is open to analysis.
Anki's review log does not give one:

| Fact | Anki's `revlog` | Evidence |
| --- | --- | --- |
| Columns | `id` (time), `cid`, `usn`, `ease`, `ivl`, `lastIvl`, `factor`, `time`, `type` | read, probed |
| Answer time | Limited to `maxTaken` | probed: 200 s stored as 60 s |
| An undone grade | The row is deleted | probed: 3 rows became 2 |
| Card content, deck, tags at the review | Not stored | read |
| Time to reveal, apart from time to grade | Not stored | read |
| A card shown and not graded | Not stored | read |
| Memory state before and after | Not stored in the row; Anki computes it from the log | read |
| Format | Anki's, upgraded by newer Anki versions | read |

**Tables** (fields in `data-model.md`; every row has a time and a writer):

| Table | One row for each |
| --- | --- |
| `presentation` | Card shown: card, content version, deck, folder, title, tags, session, position, kind, state before, the four offered intervals, settings and parameter set in effect |
| `response` | Grade of a presentation: time to reveal, time to grade, time out of focus, grade, state after, and Anki's nine `revlog` values |
| `undo` | Undone response |
| `session`, `session_end` | Session start with its scope; session end with its cause |
| `content`, `media` | Version of a card's front and back; file that a version refers to |
| `card_change` | Card added, content changed, tags changed, moved, removed, or restored |
| `setting_change`, `parameter_set` | Change of a scheduling setting; set of scheduler parameters with its source |
| `store_event` | Store created, attached to a path, backed up, copied to a directory (R18) |
| `editor_view` | Card open in the editor: the card, how long, and how long without focus (R18) |
| `writer` | App release and Anki version that wrote rows |

A view, `review`, joins each presentation with its response and its undo, so that one
query gives one row for each showing of a card.

**Rules**:

- No row is updated or deleted. A correction is a new row that refers to the earlier
  row. An ungraded presentation is a `presentation` row with no `response` row.
- The `presentation` row is written when the card is shown and the `response` row when
  Anki has stored the grade. Both survive the end of the process.
- The record and Anki's collection are two databases and have no common transaction. At
  each open, the host writes a `response` row, marked as recovered, for each `revlog` row
  that has none (FR-036).
- The schema only grows: new tables and new nullable columns. A `schema` table holds the
  version and the release that added each part (FR-039).
- `docs/study-record.md` documents each field with its meaning, unit, and empty case
  (FR-038).
- Each Anki backup has a copy of the record beside it with the same time in its name,
  made with SQLite's online backup call (`sqlite3.Connection.backup`). Anki removes old
  `.colpkg` files by its backup limits (`thin_backups`, read). A record copy stays while
  the `.colpkg` of the same time stays (FR-040).

**Alternatives considered**:

| Alternative | Result |
| --- | --- |
| Tables added to `collection.anki2` | Rejected. Anki owns that schema; what its database check, format upgrades, and backups do with foreign tables is not specified. |
| Anki's `revlog` alone, with `maxTaken` at 9999 | Rejected. The table above lists what it does not store. |
| An append-only JSON Lines file | Rejected. No index, no transaction, and no safe concurrent read during a write. SQLite is read directly by pandas, R, and DuckDB. |
| xAPI statements in a learning record store | Rejected as the store, kept as the reference for the rules. An xAPI statement is a JSON object (actor, verb, object, result, context) that a learning record store keeps behind an HTTP interface; it is an interchange format between systems. The app has one writer on one machine, and analysis reads tables. The record follows the xAPI rule for permanence: a statement is never changed, and an undo is a new statement that refers to the earlier one (xAPI Data, sections 2.3.1 and 2.3.2, https://github.com/adlnet/xAPI-Spec/blob/IEEE/xAPI-Data.md, read 2026-11-16). An xAPI export can be derived from the record. |

**Research format**: The public data set for spaced-repetition research,
`open-spaced-repetition/anki-revlogs-10k`, has one row for each review with `card_id`,
`day_offset`, `rating` (1 to 4), `state` (0 new, 1 learning, 2 review, 3 relearning),
`duration` (ms, 0 to 60000), `elapsed_days`, and `elapsed_seconds`, and tables that map
cards to decks and decks to parents
(https://huggingface.co/datasets/open-spaced-repetition/anki-revlogs-10k, read
2026-11-16). Its `duration` has Anki's 60 s limit and it has no card content. The record
holds each value that these columns derive from: the grade, the kind, the times, the
scheduler's day number, and the deck path. `docs/study-record.md` gives the mapping, so
that published models run on the user's own history.

## R13. What the record observes

**Decision**: The window measures and the host reads the following for each presentation.

| Fact | Source |
| --- | --- |
| Time to reveal, time to grade | The window's monotonic clock (`performance.now()`), sent with the grade |
| Time out of focus | The window's `visibilitychange` and `blur` events while the card is on screen |
| State before | `QueuedCard.states.current`, which holds the FSRS stability and difficulty (probed), and the card's interval, due value, repetitions, and lapses |
| Estimated recall at the review | `card_stats_data().fsrs_retrievability` (field probed) |
| Offered intervals | The next states of the four grades, as numbers, with Anki's labels |
| State after | The card after `answer_card()`: `memory_state`, interval, due value |
| Anki's row | The `revlog` row that `answer_card()` wrote |
| Content version | A digest of native front and back source, retained media, and shared editor assets |
| Subject | Deck path, folder, deck title, and tags from the sync |
| Scheduler day | `sched.today`, Anki's day number with its day boundary |

The time sent to Anki is the sum of the two measured times. The record keeps both parts.

Editor views use the same [monotonic clock](https://developer.mozilla.org/en-US/docs/Web/API/Performance/now).
Each selected card has one view, closed when its identity, deck, or workspace changes.
[React effect cleanup](https://react.dev/reference/react/useEffect) ends that view before
the next begins. Visibility and [document focus](https://developer.mozilla.org/en-US/docs/Web/API/Document/hasFocus)
determine the intervals without focus. The host appends the measured values only for
the workspace's current store attachment. Native window close waits for the pending
view write before destroying the window. These durations measure exposure, not proof
that the user attended to or learned the content.

Use the focus event's [timestamp](https://developer.mozilla.org/en-US/docs/Web/API/Event/timeStamp)
for each transition. It has the same time origin as `performance.now()` and records
event creation. Reading the clock inside a delayed event handler includes unrelated
work in the measured interval. Clamp a transition to the start of its presentation
when the event was queued before that presentation began.

The focused window scenario uses [Playwright Clock](https://playwright.dev/python/docs/clock)
to advance browser time while keeping the host's wall clock real. Its
[clock API](https://playwright.dev/python/docs/api/class-clock) replaces both
`performance.now()` and `Event.timeStamp`; install it before navigation so the
application uses one clock throughout. Advance rendering timers before operating
an animated menu. `fast_forward` runs each due timer at most once, which permits
the three-hour response case without replaying every periodic callback. This
establishes the window's elapsed-time accounting and Anki's answer-time cap; it
does not represent three hours of physical study. The record retains the full
reveal and grade durations while Anki limits their sum to the preset's `maxTaken`.

## R14. Parameter fitting

**Decision**: The fit (User Story 7) calls Anki's backend: `compute_fsrs_params` to fit,
`evaluate_params_legacy` for Anki's two accuracy measures (`log_loss`, `rmse_bins`) of
the fitted set and of the current set, and the preset's `fsrsParams6` to apply. Each
applied set is a `parameter_set` row. Anki's `FsrsInsufficientData` error, and a fit
that used no review, become `NotEnoughHistory` (read: `compute_params` returns the
current parameters when it has no training item).

**Rationale**: The wheel has `compute_fsrs_params`, `evaluate_params`,
`simulate_fsrs_review`, `get_retention_workload`, `graphs`, and `get_review_logs`
(probed for presence, not called). The Python library has a public wrapper only for
`compute_fsrs_params_from_items`; the search-based call is reached through the
collection's backend object, as Anki's own deck-options page reaches it (read). The
amount of history that Anki needs is decided by Anki's code.

`desktop/tests/fit_history.py` measures a minimal dated history against the installed
wheel. One initial learning row produces no training item. Adding a review on the
next day produces one item; the fit accepts it and both evaluations are finite.
In this fixture Anki retains the current parameters, so acceptance is not evidence
of a useful personal fit. The UI must display the actual candidate and measures,
including equality with the current set.

| Synthetic history | Training items | Fit time |
| --- | ---: | ---: |
| Empty | 0 | 0.002 s |
| Initial learning row | 0 | <0.001 s |
| Initial learning row and next-day review | 1 | 0.104 s |

The reproducible probe retains full parameters, log loss, RMSE, revision,
environment, and timing under `test-history/*-fit-history`. These observations
establish the minimum for this dated fixture, not a universal sufficient sample
for personal scheduling. [Anki's fit implementation](https://github.com/ankitects/anki/blob/main/rslib/src/scheduler/fsrs/params.rs)
returns the current parameters when there are no items and can retain them when
they evaluate at least as well as the candidate. Its `fsrs_items` counts training
observations, not every raw review-log row.

Anki's Python wrapper has no distinct insufficient-data exception. Its
[error mapping](https://github.com/ankitects/anki/blob/main/rslib/src/error/mod.rs)
uses the `deck_config_not_enough_history` translation for `FsrsInsufficientData`.
The app matches that exact translated message; other backend errors remain errors.
The candidate and its evaluation remain in host memory until acceptance. Apply
accepts that candidate, appends its parameters and measures, and records the
previous and applied parameter arrays. Closing the form writes no learning data.
If the host restarts, the user runs the fit again before applying it. The estimates
describe the fitting history, not performance on an independent later sample.

## R15. One running copy

**Decision**: The app is a singleton (constitution, principle VII). The Tauri
single-instance plugin enforces it in the shell. It is the first plugin that the builder
registers. Its callback gives the focus to the main window.

**Source**: https://v2.tauri.app/plugin/single-instance/ (read). On Linux the first copy
owns a D-Bus name made from the app identifier (`org.dev_math_flashcards.SingleInstance`);
a later launch sends its arguments to that name and exits. The plugin needs no
capability and writes no file.

**Consequences**:

- One host process holds the store for the life of the running copy (R3), and it is the
  only writer.
- Two releases never run together. An update takes effect at the next launch.
- The browser build (`just desktop-web`) is a development and test target, not the app.
  The plugin does not cover it.

Concurrency that remains is inside the one copy and has one rule for each resource: the
host answers one request at a time; the record has one writer and any number of
read-only readers (SQLite's write-ahead log, R12).

The native test's Xvfb environment supplies no `DBUS_SESSION_BUS_ADDRESS`.
`dbus-run-session` supplies a working private session bus, verified by querying
`org.freedesktop.DBus.ListNames`. The native recipe uses it so test launches share one
bus and remain separate from the user's running app. The second-launch scenario hides
the first window, requires the new process to exit, and checks that the original window
is the only app window and has the focus.

## R16. File placement by the XDG Base Directory Specification

**Source**: https://specifications.freedesktop.org/basedir/latest/ (read).
`XDG_DATA_HOME` holds "user-specific data files"; `XDG_CONFIG_HOME` holds
"user-specific configuration files"; `XDG_STATE_HOME` holds state "that should persist
between (application) restarts, but that is not important or portable enough" for the
data directory; `XDG_CACHE_HOME` holds "user-specific non-essential data files".

**Decision**: Each file goes to the directory for its kind. Python resolves the
directories with `platformdirs`; the shell resolves them with the Tauri path API.

| File | Kind | Location |
| --- | --- | --- |
| Stores: collection, learning record, record media, `store.json`, backups | Data | `$XDG_DATA_HOME/math-flashcards/study/` |
| Scheduling settings | Data | In the store. Each change is part of the history (FR-034). |
| Installed releases, `active`, `launch` | Data | `$XDG_DATA_HOME/math-flashcards/` (existing) |
| Preferences: the workspace path | Configuration | `$XDG_CONFIG_HOME/dev.math.flashcards/preferences.json` (existing, Tauri store plugin) |
| Render output, check results, search records, results of analyses | Cache | `$XDG_CACHE_HOME/math-flashcards/` |
| Launcher command | Executable | `$HOME/.local/bin`, the directory that the specification names for user executables (existing) |

The feature writes no state file and no runtime file: the host talks through pipes, and
the single-instance plugin uses a D-Bus name.

**Existing state of the app, inspected on this machine**:

| Observation | Conformance |
| --- | --- |
| The Python bridge writes only under `user_cache_path("math-flashcards")`. | Conforms. |
| The installer derives its directories from `XDG_DATA_HOME`, with the specification's default. | Conforms. |
| The app has two directory names: `math-flashcards` (bridge, installer) and `dev.math.flashcards` (Tauri identifier). | Conforms. Both are under the correct base directories. |
| `$XDG_DATA_HOME/dev.math.flashcards/` holds `WebKitCache/` and `CacheStorage/`, written by the web view. `$XDG_CACHE_HOME/dev.math.flashcards/` does not exist. | Does not conform: regenerable web view cache is in the data directory. The web view layer of Tauri owns the placement. |

**Owner of the defect**: The web view library of Tauri (`wry`). Its Linux code sets one
directory for both kinds
(https://github.com/tauri-apps/wry/blob/dev/src/webkitgtk/web_context.rs, read):
`.base_cache_directory(data_directory)` and `.base_data_directory(data_directory)`, with
the comment "TODO: Consider taking a cache_directory so this can be in XDG_CACHE_HOME".
The Tauri window builder has `data_directory` and no cache setting
(https://docs.rs/tauri/latest/tauri/webview/struct.WebviewWindowBuilder.html, read). The
app cannot correct the placement with a setting. The web view cache holds no learning
data. A report to the `wry` project is an action outside this repository; the user
decides it.

## R17. Three parts: interface, core, analysis

**Requirement**: Analyses and views change for the whole life of the project; agents add
them all the time. The learning data and the scheduling logic must be safe from those
changes: a small blast radius, rare data migrations, and a small chance that a later
version changes the core by accident (constitution, principle IX).

**Alternatives considered**:

| Alternative | Protection | Result |
| --- | --- | --- |
| A. Analyses as functions in the study host, in `desktop/backend.py` | None. An analysis shares the file, the process, and the write connection of the core. | Rejected. |
| B. Separate Python packages for the core and the analyses; an analysis runs in a short-lived process with a read-only connection to the record; an import contract in the commit gate | A new analysis touches no core file. It cannot write the record through its connection. The gate rejects an import across the boundary. One prepared environment. | **Chosen.** |
| C. As B, with a separate Python environment for the analyses | As B, and a dependency of an analysis cannot change the versions that the core resolves. | Not chosen now. It needs a second prepared runtime in each release. It becomes necessary when a dependency of an analysis conflicts with a dependency of the core. |

**Decision**:

| Part | Code | Process | Access to learning data |
| --- | --- | --- | --- |
| Core | `desktop/study/` (Python package) | The study host (R3) | The only writer of the store and the record |
| Analysis | `desktop/analysis/` (Python package); one module for each analysis in `desktop/analysis/catalog/` | One new process for each request, as the other bridge actions | The record only, read-only |
| Interface | `desktop/src/` (TypeScript); the study screen and the Statistics screen | The window | None. It calls bridge actions. |

`desktop/backend.py` stays the entry script. It starts the host, which accepts native
card values from the source bridge. The core imports nothing from the entry script.

**Measured on this machine** (a spike with two packages beside an entry script):

| Question | Result |
| --- | --- |
| Does the entry script import a package beside it when Python runs with `-I`, as the shell runs it? | No. Isolated mode leaves the script's directory out of `sys.path`, and the import fails with "No module named". The entry script adds its own directory to `sys.path` before it imports the two packages; with that line the import succeeds. |
| Does Import Linter find the two packages with no project file? | Yes. `uvx --from import-linter lint-imports` in the directory, with `root_packages` `study` and `analysis` and `include_external_packages = True` in `.importlinter`, reports three contracts kept. |
| Does it report each forbidden import? | Yes. An analysis module that imports `study`, `anki`, `backend`, and another analysis breaks two contracts; the report names each import with its line, and the command exits with status 1. |

**Rules that make the blast radius small**:

| Rule | Mechanism | Source |
| --- | --- | --- |
| An analysis cannot change the record | `sqlite3.connect("file:<path>?mode=ro", uri=True)`; the record uses the write-ahead log, which gives readers a consistent view while the host writes | https://docs.python.org/3/library/sqlite3.html#sqlite3-uri-tricks, https://www.sqlite.org/wal.html |
| An analysis cannot read or change Anki's collection | The host holds the collection in exclusive locking mode (R3). The record is complete without it (FR-036). | `rslib/src/storage/sqlite.rs` (read) |
| The analysis package does not import the core, `anki`, or the entry script; the core does not import the analysis package; no analysis imports another | Import Linter contracts of type `forbidden` and `independence`, run by `just test-commit` | https://import-linter.readthedocs.io/en/stable/contract_types/forbidden/, https://import-linter.readthedocs.io/en/stable/contract_types/independence/ |
| A new analysis needs no change to the interface | Each analysis returns one generic value (a table with named columns). The Statistics screen renders any table. The list of analyses is the content of `desktop/analysis/catalog/`. | Design |
| An analysis keeps no permanent data | A result is returned to the window. A stored result is a cache file (R16). | Design |
| A change to an analysis needs no migration | The record holds observed facts, not results. Analyses compute from the facts. | Principle VI |
| A change to the core is visible | The core is one directory. Its tests (the study scenario, the first-version record fixture) are apart from the analysis tests. | Design |

**The first analyses** (FR-056) use the folder/month and calibration queries of
`contracts/learning-record.md`. Two analyses give the catalog its second caller.
The folder count includes ungraded presentations; its averages exclude missing
values. Calibration uses probability bands of width 0.1 and keeps missing
predictions in a named band. These bins summarize recorded predictions and
self-grades; their width is a display default, not a learning intervention.
`docs/analyses.md` owns module authoring and the treatment of missing observations.

**What the alternatives do not solve**: Dependencies track their latest versions
(principle III). A newer `anki` can change scheduling behaviour and upgrade the
collection format without a change in this repository. The record names the Anki version
on every row (`writer`), and the store has dated backups. This is a conflict between
principle III and the stability of the core; the user decides it.

## R18. Keeping the data: one directory, a copy, and what the record covers

**Decision**:

- All learning data of a workspace is the store directory (R4). It holds no file that
  another directory needs, and it needs no file outside itself.
- `study-copy` writes a complete copy of the store to a directory that the user chose.
  The host closes the collection and the record, copies the store directory with
  `shutil.copytree` to `<chosen>/math-flashcards-study-<time>/<store ID>/`, opens both
  again, and writes a `store_event` row of kind `copied` with the destination. The app
  is one copy with one host, so no other writer exists during the copy.
- A copy has the layout of a store. Placed in `$XDG_DATA_HOME/math-flashcards/study/` on
  any machine, it is in the attach list (R4). No restore function exists apart from
  attach.
- The record gains one fact that it did not cover: a card open in the editor (FR-058).
  The window measures the time and sends it to the host when the card leaves the editor.

**Rationale**: The dated backups (R4) are in the store directory, on the same disk as
the store. They protect against a damaged file, not against a lost disk. A copy in a
place that the user chose (another disk, a directory that a backup tool covers) does.

**Alternatives considered**:

| Alternative | Result |
| --- | --- |
| Copy the open collection file | Rejected. The host holds it in exclusive locking mode, and a file copy of an open SQLite database can be inconsistent. |
| An Anki `.colpkg` and a record copy, as the dated backups | Rejected for this purpose. A copy in that form needs a restore function; a copy in the store's layout needs none. |
| A second directory that receives every dated backup with no action by the user | Not chosen now. It is the stronger protection and adds a preference and a failure case (the directory is absent). The user decides. |
| The record inside the workspace, tracked by git | Rejected in R4 and R12: a binary database in the deck repository. |

**Undo after a copy**: Anki keeps undo steps in memory (R3). After the host closes and
opens the collection, the last grade cannot be undone. The window shows Undo as
unavailable, as after a sync (FR-021).

Copy closes and reopens the existing collection and record objects. It does not
call `Store.close`, which ends active sessions, or construct a new `Store`, which
performs interrupted-session recovery. The record keeps its writer identity and
open session. After copying, the window requests a fresh presentation from Anki's
reopened queue before accepting another grade. A finished session stays finished.
The copied record holds exactly the facts committed before copying; the source
then appends the copied event and any later presentations.

The destination must exist and be outside the live Study data directory, so that
copying cannot recurse into the source or create an invalid registry entry. An
incomplete destination created by a failed copy goes to the trash; the original
store reopens. Attaching a completed copy on a fresh data directory preserves all
earlier rows and appends normal writer, recovery, and attachment facts.

## R19. Basis of the learning decisions in published research

Constitution principle X. The keys refer to `docs/learning-research.md`. Each source
there states its reading depth. The statuses remain provisional where the full text
is unread; task T079 checks the papers and corrects this section.

The distance from the studies to this person's case is the same for most rows. The
experiments use word pairs, facts, text passages, definitions of key terms, and
precalculus problems, with final tests after days to months. The person's cards hold
definitions, statements, and proofs of research-level mathematics, and the retention
interval is years. A status of Supported means that the direction of the effect has
evidence for adults. It does not mean that the size of the effect is known for this
material.

| Learning decision | Requirement | Sources | Status |
| --- | --- | --- | --- |
| The person recalls the answer before the app shows it | FR-002 | `roediger2006`, `karpicke2008`, `rowland2014`, `adesope2017`, `dunlosky2013`. Qualification: `soderstrom2015` finds that restudy also improves learning when spacing is controlled. | Supported |
| Reviews of a card are spread over increasing intervals | FR-005 | `cepeda2006`, `cepeda2008`, `bahrick1993`; for mathematics with college students, `rohrer2006`, `hopkins2016`, `lyle2020` | Supported up to 1 year. Beyond that: `bahrick1993` (4 people) and `bahrick1991` (not read) |
| The schedule adapts to each card and to this person, and the person can fit it to their own history | FR-005, FR-046 | `mettler2016` shows the gain of adaptation to item and learner, with a different algorithm. `ye2022` and `su2023` evaluate their scheduler on logs and in simulation, with vocabulary. | Inference. No experiment on learning outcomes with FSRS is in the register |
| A card graded Again comes back in the same session and at short intervals | FR-005, User Story 1 scenario 7 | `rawson2011`, `rawson2013`: relearning to a correct recall in later sessions gives durable retention at small cost. Their first-session criterion (3 correct recalls) is not Anki's default steps. | Supported in direction. The steps are Anki's defaults |
| The app has no action that sets a card aside for the rest of a session | Assumptions | `kornell2008` | Inference from vocabulary experiments with short delays. Effects were not significant in every comparison; the paper does not establish a general prohibition on postponing mathematics cards. |
| The answer is recalled in thought, and the person grades the recall | FR-003, Assumptions | `smith2013` finds no difference between retrieval in thought and a produced response. `tauber2017` finds a produced response better for definitions (d = 0.43), which is the material of many cards. `dunlosky2010` finds that students grade their own recalled definitions too high. | Contrary evidence for definition cards. See the consequences below |
| Target probability of recall of 0.9 | R9 | `ye2022` uses 90% as a comparison policy taken from SuperMemo; its model-based simulation does not establish an optimal target for adult mathematical learning. No learning-outcome evidence for this value is in the register. | Default of Anki |
| Reviews in order of ascending retrievability | FR-044, R9 | None in the register. The source is the Anki manual. | Default, chosen in R9 from the manual |
| A session mixes the cards of all subjects in its scope | FR-005 | `rohrer2007`, `brunmair2019` (g = 0.34 for mathematical tasks). The studies mix types of problem during practice. A review of cards that were learned separately is a different task. | Inference |
| The record holds the time from the front to the reveal | FR-028 | `mettler2016`: response time with accuracy carries enough information about learning strength to set a schedule | Supported |

**Consequences for this feature**

- A grade is the person's own judgement, and the app does not check the answer. Each
  measure that an analysis computes from grades is named as self-graded
  (`contracts/analysis.md`). `dunlosky2010` found overconfidence for incorrect and
  partly correct definitions, even with the correct answer visible. It does not
  establish the magnitude of this person's grading error. Checking separate ideas
  reduced overconfidence but also lowered scores for correct answers.
- Recall of a card is not competence with its content. `pan2018` finds the weakest
  transfer to material that was studied and not tested and to problems with worked
  examples, and `vangog2015` and `karpicke2015` dispute the size of the testing effect
  for complex material. An analysis that calls a subject fluent states that it means
  recall of the cards of that subject.

**Consequences for later forms of study** (outside this feature)

- `muzsnay2025` supplies limited evidence for independent undergraduate problem solving
  with delayed tests. It does not establish the effectiveness of covert flashcard
  review for research-level mathematics or determine its schedule.
- A form of study in which the person produces the answer, and in which the answer is
  checked against the parts of the correct answer, has support from `tauber2017` and
  `dunlosky2010`. The latter measured scoring accuracy immediately, not delayed
  learning gains. Checking one's own answer against separate ideas is still
  self-grading; an independently scored answer is needed to estimate grading error.
- Questions about a proof have a published model of what to ask (`mejiaramos2012`) and
  a tested method of study (`hodds2014`).
- `iannone2014` holds students' views of oral assessment and no measured learning. The
  register has no source on measured learning from oral examination or from generated
  questions; a plan for either feature starts with that search.

**How the record tests the decisions**: the `calibration` analysis compares the
scheduler's predicted recall with the grades. It shows whether the adaptive schedule
predicts this person's self-graded recall. It cannot show an error of the grades
themselves; that needs a checked answer.

## Unmeasured

- The size of the learning record over years. An estimate from the row contents is about
  1 kB for each presentation.
- The time to render all 68 decks for the first sync. It bounds SC-006's first
  preparation and the progress display.
- The time from a save to the changed card in review (SC-003) for the largest deck.
- Whether a retained earlier release opens a store that a newer `anki` upgraded (R1).
- The time that `study-copy` takes for a store of the full workspace (R18).
