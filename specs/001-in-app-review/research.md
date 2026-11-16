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

**Decision**: One Anki note for each card. The note GUID is the `card-id`. One notetype
with fields `Front` and `Back` and one card template.

**Rationale**: Anki accepts an arbitrary string as a GUID and finds the note by it
(probed). The 3,278 front `card-id` values in 68 decks have no duplicate. Updating a
note's fields after a review keeps the interval and the FSRS memory state (probed). The
exporter's content hash (`simple_hash(front + back)`) changes on every edit and cannot
carry history.

**Alternatives considered**: Content-derived identity, as the package uses: rejected,
it resets history on each edit. Identity by deck path and position: rejected, moves and
reorders would reset history.

**Consequence**: The render output must carry the `card-id`. `desktop/paired-cards.lua`
reads it and drops it; `ankdown.lua` emits `front`, `back`, `tags` by position. The card
model of the exporter (`ankdown-for-math`, the user's fork) gains an `id` field, and the
pairing filter passes the ID to it. Package GUIDs stay as they are (FR-025).

## R3. Process model

**Decision**: One long-lived study process for each running copy of the app. The native
shell starts `backend.py study-host` on the first study request and keeps it. The process
holds the collection open, holds an exclusive file lock on the store, and answers one
JSON request per line. All other bridge requests keep the current model: one new process
for each request.

**Rationale**:

- Anki keeps undo steps in memory (`UndoManager`, read). After close and reopen,
  `undo_status()` is empty while the review log row remains (probed). Undo (FR-021)
  therefore needs the collection to stay open between the grade and the undo.
- Anki rejects an answer for a card that is not at the top of its in-memory queue
  ("not at top of queue", read). A held collection keeps one queue for the session.
- The FSRS switch is read when a queue is built. It must be set before the first queue
  build (probed). The host sets it when it creates the store.
- An exclusive lock gives the second running copy a clear error (spec edge case) in
  place of a SQLite lock failure.
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
  renderer assets.
- When the store is in use or cannot be opened, each study request fails with a message
  that names the store path and the cause.

## R4. Store location and backups

**Decision**: `platformdirs.user_data_path("math-flashcards") / "study" / <store ID>`.
The store ID is a UUID made when the store is created. The directory holds
`collection.anki2`, Anki's `collection.media`, the learning record (R12), the lock file,
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

**Alternatives considered**: A folder inside the workspace: rejected, it puts a binary
database in the deck repository and in deck discovery. `XDG_STATE_HOME`: rejected, the
XDG specification describes it for data that is less important than user data.

**Test rule**: Every test that starts the bridge sets `XDG_DATA_HOME` to a temporary
directory. `desktop/tests/organization.py` and `desktop/tests/native.py` already do. The
`desktop-test` recipe isolates `XDG_CACHE_HOME` only; once the window opens the store at
workspace open, that scenario would write to the real history.

## R5. Deck mapping

**Decision**: Each deck file maps to one Anki deck named from its workspace path:
`Workspace::<folder>::…::<file stem>`. Folders are parent decks. `Workspace` is the root
deck; studying the workspace selects it.

**Rationale**: The app's tree shows folders and files, and the spec's scopes are deck,
folder, and workspace. `deck_due_tree()` returns nested new, learning, and review counts
for `A::B` names (probed). Anki has no command that studies every deck; a root deck
gives one. The collection is internal, so its deck names need not equal the deck titles
in the packages.

**Alternatives considered**: Names from the `title` metadata: rejected, titles need not
follow the folder tree that the user selects from.

## R6. Deck changes to the store

**Decision**: One operation, `study-sync`, makes the store agree with the saved decks.
It is state-based: it compares each deck's inputs with the inputs recorded at its last
sync and renders only the decks that differ. The frontend calls it at workspace open,
after a save, after a file-watch event, and before a session starts.

**Rationale**:

- The bridge already has this shape for packages: `input_hashes()` records the deck
  source, its media, and the renderer assets, and `sync()` compares them. The store
  keeps the same record for each deck in the collection's config, so the record and the
  notes change together.
- A state comparison needs no event history. A missed file notification or a store that
  was in use is corrected by the next call.
- The Anki operations exist: `add_notes` (batch), `update_notes(skip_undo_entry=True)`,
  `set_deck`, `suspend_cards`, `unsuspend_cards`, `decks.remove` (read and probed).

**Rules**:

- The render is the package render: `render()` with the pairing filter and the exporter
  filter. The note fields hold the same HTML that the package holds (FR-009, SC-007).
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
- A card ID in two decks is reported with both paths. The note stays with the deck that
  had it first.

**Alternatives considered**: Import the generated `.apkg` into the collection: rejected,
the package GUID is a content hash and review would depend on a current package
(FR-025). Sync from frontend edit events: rejected, external edits bypass them.

## R7. Media

**Decision**: Images go to Anki's media folder of the store through `col.media`. The
native shell serves the store's media folder through Tauri's asset protocol, and the
Vite middleware serves it on a route. The study screen resolves each `img` source
against that folder.

**Rationale**: The exporter rewrites each image source to a mangled file name and lists
`source:name` pairs; `media_paths()` validates them. Five decks contain image links.
TikZ-cd diagrams reach the card as SVG from the shared renderer.

**Alternatives considered**: Data URIs inside the note fields: rejected, the exporter
filter treats a non-HTTP source as a file path and mangles it.

## R8. Card display

**Decision**: The study screen inserts the note's `Front` and `Back` HTML and typesets
the element with the app's local MathJax, configured by `texOptions(macros)` from the
active asset set.

**Rationale**: The exporter emits math as `\(…\)` and `\[…\]` in HTML. The package
template typesets the same HTML with MathJax 4 and the same macro set. The editor's
`previewHtml()` is a summary renderer for card lists and does not render lists, tables,
or nested divs.

**Note**: Card HTML is the user's own authored content and is inserted without
sanitizing, as Anki does.

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
  `reviewOrder` is the preset key and 7 the proto value (probed key, read value; the
  effect on the queue is not probed).
- Anki limits the answer time it records to `maxTaken`, 60 s by default: an answer of
  200 s was stored as 60 s (probed). The manual states that the time does not affect
  scheduling. Anki accepts 1 to 9999 (read). The store sets 9999 so that Anki's own log
  loses less; the learning record keeps the measured time with no limit (R13).
- The 100-year maximum interval fits the time scale of the purpose and stays.

## R10. Session behaviour

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

**Undo rule**: Undo is offered when Anki's `undo_status().undo` names the answer
operation. Deck sync writes notes with `skip_undo_entry=True` where Anki offers it; other
sync operations add undo steps, so Undo is unavailable after a sync until the next grade
(FR-021).

## R11. Test method

**Decision**: A Playwright scenario, `desktop/tests/study.py`, drives the real window
served by `just desktop-web` with the real bridge, real deck files in a temporary
workspace, and temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME`. It is a recipe in
`just test-commit`. The scenario reads the store with the `anki` library to check
results, reads the learning record with Python's `sqlite3`, and prepares due cards with
`sched.set_due_date()` while the app is stopped. `set_due_date()` writes a `revlog` row
of type 4 (probed); the host records it at the next open as a recovered row (R12).

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
| `store_event` | Store created, attached to a path, backed up |
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
| Content version | A digest of the note's `Front` and `Back` |
| Subject | Deck path, folder, deck title, and tags from the sync |
| Scheduler day | `sched.today`, Anki's day number with its day boundary |

The time sent to Anki is the sum of the two measured times. The record keeps both parts.

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
amount of history that Anki needs is decided by Anki's code and is not measured here.

## Unmeasured

- The smallest review history that Anki's fit (`compute_fsrs_params`) accepts in the
  wheel.
- The time that the fit takes.
- The effect of `reviewOrder` 7 on the queue (R9).
- The size of the learning record over years. An estimate from the row contents is about
  1 kB for each presentation.
- The time to render all 68 decks for the first sync. It bounds SC-006's first
  preparation and the progress display.
- The time from a save to the changed card in review (SC-003) for the largest deck.
- Whether a retained earlier release opens a store that a newer `anki` upgraded (R1).
