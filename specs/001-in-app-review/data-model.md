# Data Model: In-App Review

This model fixes the vocabulary, the states, and the typed values before any task is
ordered. The core declares the study types as Pydantic models in
`desktop/study/values.py`, and the analysis package declares the analysis types in
`desktop/analysis/__init__.py`; the frontend declares the same shapes as Zod schemas in
`desktop/src/bridge.ts`.

## Vocabulary

| Term | Meaning | Not to be confused with |
| --- | --- | --- |
| Study | The spaced-repetition function of this feature, and its name in the interface and in code (`study-*` actions, `study.tsx`). | **Review changes**, the existing comparison of a deck with its package (`review` action, `review.tsx`). |
| Card | One front and back pair in a deck file, identified by `card-id`. | An Anki card row. This model has one Anki card for each note. |
| Deck | One Markdown file in the workspace. | An Anki deck in the store, which also exists for each folder. |
| Store | The Anki collection, its media folder, and the learning record for one workspace. | The cache databases `builds.sqlite3` and `derived.sqlite3`. |
| Learning record | The append-only database `record.sqlite3` of everything the app observes about the user's learning. | Anki's `revlog` table, which the scheduler owns and which holds less. |
| Presentation | One showing of one card to the user, graded or not. | A grade. A presentation with no grade is still recorded. |
| Host | The long-lived bridge process that holds the store open. | A request process, which serves one request and exits. |
| Scope | What a session studies: the workspace, a folder, or a deck. | |
| Grade | The user's rating of one recall: Again, Hard, Good, or Easy. | |

## Identifiers

| Type | Raw type | Rule |
| --- | --- | --- |
| `CardId` | string | Not empty. Unique in the workspace. Equal to the note GUID in the store. The app creates it with `crypto.randomUUID()`; earlier IDs keep their form. |
| `DeckPath` | string | The existing bridge type: a path relative to the workspace that ends in `.md`, with no `.` or `..` part. |
| `Scope` | `{kind: "workspace"}` \| `{kind: "folder", path}` \| `{kind: "deck", path: DeckPath}` | Maps to one Anki deck name by R5 in `research.md`. |
| `Grade` | `"again"` \| `"hard"` \| `"good"` \| `"easy"` | Maps to Anki's `CardAnswer` ratings in that order. |
| `StoreId` | string | A UUID made when the store is created. Names the store directory. Independent of the workspace path. |
| `SessionId` | integer | The row ID of a `session` row. Returned by `study-begin`. |
| `PresentationId` | integer | The row ID of a `presentation` row. Returned with each card and sent back with its grade. |
| `ContentDigest` | `Digest` | The existing digest type, applied to a card's rendered front and back. |

## Entities

### Card in the store (Anki note and card)

| Field | Source | Rule |
| --- | --- | --- |
| GUID | `CardId` | Never changes for a note. |
| `Front`, `Back` | Rendered HTML of the card sides | Equal to the package render of the saved deck. |
| Tags | Deck tags and card tags | Set on each sync. Tags that Anki's scheduler set (`leech`) are kept. |
| Deck | From `DeckPath` | `Workspace::…` while the card is in a deck; `Removed` after removal. |
| Schedule | Anki | Written only by Anki's scheduler and undo. Sync never writes it. |

### Deck record

One record for each synced deck, in the collection's config.

| Field | Rule |
| --- | --- |
| `path` | `DeckPath` |
| `inputs` | Map from absolute input path to digest: the deck source, each media file, and the renderer asset identity, as `input_hashes()` gives them. |

A deck is current when every recorded input has its recorded digest. A deck with no
record is not current.

### Scheduling settings

| Field | Type | Constraint |
| --- | --- | --- |
| `new_per_day` | integer | 0 to 9999 (Anki's bound) |
| `reviews_per_day` | integer | 0 to 9999 (Anki's bound) |
| `desired_retention` | number | 0.70 to 0.99 (Anki's bound) |

The settings are one Anki preset shared by every deck. A value outside its bound is
rejected at the bridge boundary with an error; Anki's silent reset to the default is
never reached.

### Store

| Part | Rule |
| --- | --- |
| Directory | `user_data_path("math-flashcards") / "study" / StoreId` |
| `store.json` | The `StoreId`, the creation time, and each workspace path the store was attached to, with the time. The last entry is the current path. |
| `record.sqlite3` | The learning record. Created with the store. Rows are only inserted. |
| `record-media/` | Files that content versions refer to, each named by its digest. |
| `collection.anki2` | Created only when the directory does not exist. An existing directory without a readable collection is an error (FR-019). |
| `collection.media/` | Anki's media folder. |
| `backups/` | Anki `.colpkg` backups, each with a copy of `record.sqlite3` beside it. |

The directory is the whole of the learning data of one workspace (FR-049). A copy of it
is a store.

### Learning record (`record.sqlite3`)

Every table has `id` (integer row ID), `at_ms` (UTC time in milliseconds),
`utc_offset_min` (the local offset at that time), and `writer` (a `writer` row). Rows
are only inserted. `docs/study-record.md` is the field reference for the user.

| Table | Fields beyond the common ones |
| --- | --- |
| `writer` | `app_release`, `anki_version`, `schema_version` |
| `schema` | `version`, `added` (the tables and columns that the version added) |
| `store_event` | `kind` (created, attached, backed-up, copied), `path` |
| `editor_view` | `card_id`, `deck_path`, `shown_ms`, `unfocused_ms` (one row for each time a card was open in the editor, written when it leaves the editor) |
| `session` | `scope_kind`, `scope_path` |
| `session_end` | `session`, `cause` (left, finished, host-stopped, recovered) |
| `content` | `digest` (`ContentDigest`, unique), `front`, `back` |
| `media` | `content` (the `content` row that refers to the file), `name` (the file name in the card), `digest` (the file is `record-media/<digest>`, stored once for all rows with that digest) |
| `card_change` | `card_id`, `kind` (added, content, tags, moved, removed, restored), `from_deck`, `to_deck`, `content`, `tags` |
| `presentation` | `session`, `position`, `card_id`, `content`, `deck_path`, `folder`, `deck_title`, `tags`, `kind` (new, learning, review, relearning), `scheduler_day`, `before_interval_days`, `before_due`, `before_reps`, `before_lapses`, `before_stability`, `before_difficulty`, `before_retrievability`, `offer_again_s`, `offer_hard_s`, `offer_good_s`, `offer_easy_s`, `labels`, `desired_retention`, `parameter_set`, `new_per_day`, `reviews_per_day` |
| `response` | `presentation` (empty for a recovered row), `card_id`, `grade`, `reveal_ms`, `grade_ms`, `unfocused_ms`, `after_interval_days`, `after_due`, `after_stability`, `after_difficulty`, `recovered`, and Anki's row: `revlog_id`, `revlog_ease`, `revlog_ivl`, `revlog_last_ivl`, `revlog_factor`, `revlog_time_ms`, `revlog_type` |
| `undo` | `response` |
| `setting_change` | `key`, `before`, `after` |
| `parameter_set` | `parameters`, `source` (anki-default, fit), `reviews`, `log_loss`, `rmse_bins` |

| View | Content |
| --- | --- |
| `review` | One row for each `presentation`, with the fields of its `response` and the time of its `undo` (`undone_at_ms`), empty where there is none, and the `front` and `back` of its `content`. |

Rules for fields:

- A field that the app could not observe is empty (SQL `NULL`), never zero. A recovered
  `response` row has empty `presentation`, `reveal_ms`, `grade_ms`, and `unfocused_ms`.
- `before_stability`, `before_difficulty`, and `before_retrievability` are empty for a
  card that has no memory state yet (a new card).
- `tags`, `labels`, and `parameters` are JSON text. Times are integers in the unit that
  the field name gives.

## Card lifecycle

```text
            add to a deck                 first grade            graduate
(no note) ───────────────▶ New ───────────────────▶ Learning ───────────▶ Review
                            ▲                          ▲    ◀───────────    │
                            │                          └──── lapse (Again) ─┘
                            │ ID returns                    (Relearning)
                            │ (schedule restored)
   any state ── removed from the decks ──▶ Removed (suspended, deck `Removed`)
```

| Transition | Owner | Rule |
| --- | --- | --- |
| Add | Sync | A new `CardId` becomes a new note in its deck. |
| Grade | Anki scheduler | Only for the card at the top of the queue. |
| Undo | Anki undo | Only when the last undo step is a grade. The record keeps the grade and adds an `undo` row. |
| Edit, retag | Sync | Fields and tags change; the schedule stays. |
| Move | Sync | The Anki deck changes; the schedule stays. |
| Remove | Sync | Suspend, then move to `Removed`. The schedule stays. |
| Restore | Sync | Move to the deck, then unsuspend. The schedule stays. |

## Invariants

1. For each `CardId` in a current deck, the store has exactly one note with that GUID,
   in that deck's Anki deck, not suspended, with the rendered sides of the saved deck.
2. A note whose `CardId` is in no deck is suspended and in `Removed`.
3. Sync never changes a schedule or a review log row.
4. No operation deletes a note that has a review log row.
5. The host is the only process that opens the collection, and the only process that
   writes the record. Every other reader of the record opens it read-only.
6. An Anki deck under `Workspace` exists for each deck file and each folder, and for
   nothing else.
7. The package build and its records are unchanged by study operations.
8. No row of the learning record is updated or deleted.
9. Each card that the window shows has one `presentation` row, written before the
   user can grade it.
10. Each `revlog` row in the collection has one `response` row with the same nine
    values. Each `response` row whose grade was not undone has its `revlog` row.
11. Each `presentation` row refers to a `content` row that holds the front and back
    shown.
12. A store is created only when no store exists, or when the user chose a new one.
13. The schema of the learning record gains tables and nullable columns and loses
    nothing.
14. An analysis changes no data of a store. Every row of the record is equal before and
    after an analysis runs. The one file that a read-only connection can create is
    SQLite's shared-memory file for the write-ahead log, which holds no data
    (https://www.sqlite.org/wal.html, "Read-Only Databases").
15. The analysis package imports neither the core package, nor `anki`, nor the entry
    script. The core package does not import the analysis package. No analysis imports
    another analysis.
16. Every file that the app writes outside the workspace is under the XDG base directory
    for its kind (R16).
17. One copy of the app runs.

## Valid and invalid examples

| Case | Result |
| --- | --- |
| A card's back text changes | Valid. Same note, new `Back`, same due date. |
| A card moves from `A.md` to `B/C.md` and both decks are in one sync call | Valid. One move; no removal. |
| The same move, with the two decks in different sync calls | Valid. Removed and restored, or moved, by the order of the calls; the schedule is the same at the end. |
| `A.md` is renamed to `D.md` | Valid. Each card moves to the Anki deck of `D.md`; the Anki deck of `A.md` is removed when empty. |
| A card is deleted, then pasted back with the same ID | Valid. Removed, then restored with its schedule. |
| The same `card-id` is in `A.md` and `B.md` | Invalid. The sync result names both paths; the note stays with the deck that had it first. |
| A grade arrives for a card that is not at the top of the queue | Invalid. `StaleCard` error; the screen fetches the current card. |
| A deck fails to render | Its cards keep their last synced content; the sync result lists the deck. |
| The store directory exists but the collection does not open | Invalid. `StoreUnreadable` error with the path; nothing is created. |
| The user starts the app while it runs | Valid. The running window gets the focus. No second copy and no second host start. |
| An analysis runs while a session is open | Valid. The analysis reads the rows committed so far. The next grade is recorded. |
| An analysis tries to write to the record | Invalid. Its connection is read-only; SQLite rejects the statement, and the analysis fails alone. |
| The user saves a copy of the store during a session | Valid. The copy holds every row committed before it. Undo is unavailable until the next grade. |
| A card is open in the editor for 40 s | Valid. One `editor_view` row with `shown_ms` near 40000, written when the card leaves the editor. |
| `desired_retention` of 1.0 | Invalid. Rejected at the boundary. |
| The user takes 200 s to grade | Valid. The record holds 200 s; Anki's `revlog` holds its own limited value. |
| The user undoes a grade | Valid. Anki deletes its `revlog` row. The `response` row stays, and an `undo` row refers to it. |
| The user leaves a session with a card on screen | Valid. The `presentation` row has no `response` row. |
| The host stops after Anki stored a grade and before the `response` row | Valid at the next open: the host writes the `response` row from `revlog`, marked recovered, with the unobserved fields empty. |
| A card is reviewed, edited, and reviewed again | Valid. Two `presentation` rows refer to two `content` rows. |
| The workspace folder is renamed and opened | No store has the new path and one store exists: the host returns `Unattached`. Nothing is created. |
| A request tries to change or delete a record row | Invalid. The host has no such operation. |

## Values that cross the bridge

```text
Counts        = { new: int, learning: int, review: int }
GradeLabels   = { again: str, hard: str, good: str, easy: str }     # Anki's text, shown as given
StudyCard     = { presentation: PresentationId, card_id: CardId, deck: DeckPath,
                  front: str, back: str, labels: GradeLabels, counts: Counts,
                  undoable: bool }
Timing        = { reveal_ms: int, grade_ms: int, unfocused_ms: int }   # measured by the window
StudyFinished = { graded_today: int, next_learning_seconds: int | null,
                  counts: Counts, undoable: bool }
StudyNext     = { state: "Card", ...StudyCard } | { state: "Finished", ...StudyFinished }

DeckCounts    = { path: str, kind: "workspace" | "folder" | "deck",
                  counts: Counts, children: DeckCounts[] }

SyncResult    = { added: int, updated: int, moved: int, removed: int, restored: int,
                  failed: { path: DeckPath, message: str }[],
                  duplicates: { card_id: CardId, paths: DeckPath[] }[],
                  pending: int }                                    # decks not yet current

Settings      = { new_per_day: int, reviews_per_day: int, desired_retention: float }

StoreSummary  = { store: StoreId, paths: str[], path_exists: bool,   # the current path is a folder
                  created: str, last_used: str, cards: int, responses: int }
StudyOpen     = { state: "Open", store: str, media: str, record: str,
                  settings: Settings, counts: DeckCounts }
              | { state: "Unattached", stores: StoreSummary[] }

Fit           = { parameters: float[], current: float[], reviews: int,
                  log_loss: float, rmse_bins: float,          # Anki's evaluation of the fitted set
                  current_log_loss: float, current_rmse_bins: float }

StoreCopy     = { path: str }                                 # the directory of the copy

StudyError    = { kind: "StoreUnreadable" | "StaleCard" | "InvalidSettings"
                        | "UnknownScope" | "UnknownStore" | "NotEnoughHistory"
                        | "CopyFailed",
                  message: str }

# Analysis (contracts/analysis.md). These values do not pass through the study host.
Analysis      = { name: str, title: str, summary: str,       # name is the module name
                  failure: str | null }                       # set when the module does not import
Column        = { name: str, unit: str | null }
Cell          = str | int | float | null
AnalysisTable = { analysis: Analysis, columns: Column[], rows: Cell[][] }
AnalysisError = { kind: "UnknownAnalysis" | "AnalysisFailed" | "RecordUnreadable",
                  message: str }
```

`Counts` come from Anki's queue (`new_count`, `learning_count`, `review_count`) and from
`deck_due_tree()`. `undoable` is true when Anki's undo status names the answer operation.

## Pure and effectful parts

| Part | Kind | Input → output |
| --- | --- | --- |
| Scope to Anki deck name | Pure | `Scope` → deck name |
| Deck path to Anki deck name | Pure | `DeckPath` → deck name |
| Sync plan | Pure | rendered decks, store snapshot (GUID → deck, sides, tags, suspended) → adds, updates, moves, removals, restores, duplicates |
| Render a deck | Effect (Pandoc, LuaLaTeX) | `DeckPath` → rendered cards with IDs, media |
| Apply a sync plan | Effect (store) | plan → `SyncResult` |
| Queue, answer, undo, counts, settings | Effect (store, clock) | Anki calls in R10 |
| Measure reveal, grade, and unfocused time | Effect (window clock and focus events) | card on screen → `Timing` |
| Find the store of a workspace | Effect (files) | workspace path → `StoreId`, or the list of stores, or none |
| Open the store, backup, copy | Effect (files) | `StoreId` → open collection and record, or `StudyError` |
| List the analyses | Effect (files, read-only) | the catalog directory → `Analysis[]` |
| Run an analysis | Effect (record, read-only) | read-only connection to the record → `AnalysisTable` |
| Measure the time a card is open in the editor | Effect (window clock and focus events) | card in the editor → `shown_ms`, `unfocused_ms` |
| Record row from Anki values | Pure | queued card, states, card after the answer, `revlog` row, `Timing` → `presentation` and `response` values |
| Rows missing from the record | Pure | `revlog` IDs, `response` IDs → the `revlog` rows to recover |
| Write a record row | Effect (record) | values → inserted row |
| Fit and evaluate parameters | Effect (store, CPU) | Anki calls in R14 |

The sync plan and the conversion of Anki values to record rows are the only new logic
that is not an Anki call or an existing bridge function. Each is a function of values
and is tested with real rendered decks and a real store.

## Parts

| Part | Code | Holds | Must not hold |
| --- | --- | --- | --- |
| Core | `desktop/study/` | Store identity, the record's schema and its insert functions, the sync plan, sessions, settings, the fit, the host loop | Statistics over the record; text or layout for the window beyond error messages; an import of the analysis package |
| Analysis | `desktop/analysis/`, one module for each analysis in `desktop/analysis/catalog/` | Queries and computations over the record; the `AnalysisTable` value | A write to any file of a store; an import of the core, of `anki`, or of another analysis; permanent data |
| Interface | `desktop/src/` | The study screen, the Statistics screen, timing of what the user does | A scheduling rule; a query over the record |

An analysis is a module with a title, a summary, and one function from a read-only
record connection to an `AnalysisTable`. The catalog is the set of modules in the
directory; no list names them.

## Boundary rules

- Each study request is validated by its Pydantic model with `extra="forbid"`, as the
  current requests are. Each response is parsed by its Zod schema.
- Paths go through the existing `workspace_path()` and `deck_path()` checks.
- The host never returns Anki protobuf values. It converts them to the values above.
- The frontend types have no `any` and no `unknown`. The bridge has no `Any`.

## Policies

| Policy | Rule |
| --- | --- |
| Ordering | Anki's queue decides card order. Requests to the host run one at a time, in arrival order. |
| Idempotency | `study-sync` on an unchanged workspace changes nothing and returns zero counts. A repeated `study-answer` for an answered card returns `StaleCard`. |
| Clock | Anki reads the system clock and its own day rollover. The app adds no clock. |
| Time taken | The screen measures the time from showing the front to the grade and sends it with the grade. |
| Conflict | A duplicate ID is reported, never merged. |
| Concurrency | One copy of the app, one host, one request at a time. The record has one writer and any number of read-only readers. |
| Retry | No automatic retry. An error reaches the screen with its cause. |
