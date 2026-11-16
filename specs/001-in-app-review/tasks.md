---

description: "Task list for in-app review"
---

# Tasks: In-App Review

**Input**: Design documents from `/specs/001-in-app-review/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/study-bridge.md, contracts/learning-record.md, contracts/analysis.md, quickstart.md

**Tests**: Included. Constitution principle V requires proof through the real application
path, and each story's test is committed before its implementation and must fail for the
stated reason first.

**Organization**: Tasks are grouped by user story. User Stories 1 and 6 are one phase: a
grade is identified by its row in the learning record, and a review that is not recorded
in full is lost for all later analysis. Each later story writes its own record rows.

**Record rule for every task**: The host only inserts rows into `record.sqlite3`. No task
adds a statement that updates or deletes a record row, and no task removes or renames a
table or column of the record.

**Part rule for every task** (constitution, principle IX): Core code is in
`desktop/study/`. Analysis code is in `desktop/analysis/`. Interface code is in
`desktop/src/`. `desktop/backend.py` is the entry script. A task of the core changes no
analysis file, and a task of an analysis changes no core file. Task IDs are permanent;
T060 and later were added with the requirements for one running copy, file placement,
the copy, and the analyses, and each phase lists its tasks in the order of work.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependency on an incomplete task)
- **[Story]**: The user story the task belongs to (US1 to US8)
- Paths are relative to the repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Dependencies, test isolation, and fixtures

- [X] T080 Open the owning GitHub issue of this feature, with the purpose of `specs/001-in-app-review/spec.md` in the repository's own words and a link to this directory. Each failing test commit that the commit hook rejects goes through the sanctioned route for red commits with this issue's number, and each issue that a later task opens refers to it. Owner: [issue #2](https://github.com/dzackgarza/math-flashcards/issues/2).
- [X] T001 Add `anki` with no version pin to the PEP 723 dependency block of `desktop/backend.py`, and confirm that `just desktop-dependencies` prepares an environment in which `import anki` and `import ankdown` both succeed
- [ ] T002 In the `ankdown-for-math` repository, add an `id` field to the card model in `ankdown/cli.py` and emit it from `ankdown/ankdown.lua` for each card that supplies one; the package build ignores `id` and package GUIDs stay `simple_hash(front + back)`; prove it with a test in that repository and commit there
- [ ] T003 In `justfile`, make the `desktop-test` recipe set `XDG_DATA_HOME` to a temporary directory beside its `XDG_CACHE_HOME` override, and add a `desktop-study-test` recipe that runs `desktop/tests/study.py` against `just desktop-web` with temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME`
- [ ] T060 Create `desktop/tests/boundaries.py` and a `desktop-boundaries` recipe in `justfile` that runs it and is part of `test-commit`: the test runs `uvx --from import-linter lint-imports` on `desktop/` and requires status 0; then, in a temporary copy of `desktop/study/` and `desktop/analysis/` with `desktop/.importlinter`, it adds one violating import at a time (an analysis imports `study`; an analysis imports `anki`; an analysis imports `backend`; the core imports `analysis`; one analysis imports another) and requires status 1 with the import named in the report for each. The test fails first because the packages and the contract file do not exist
- [ ] T061 Create the packages `desktop/study/` and `desktop/analysis/` with `desktop/analysis/catalog/`, and `desktop/.importlinter` with `root_packages` `study` and `analysis`, `include_external_packages = True`, and three contracts (R17 of `specs/001-in-app-review/research.md`): forbidden `analysis` to `study`, `anki`, `backend`; forbidden `study` to `analysis`; independence of `analysis.catalog.*`. Make `desktop/backend.py` add its own directory to `sys.path` before it imports either package; T060 passes
- [ ] T079 [P] Read the full text of each source that R19 of `specs/001-in-app-review/research.md` cites. Take each text from the Zotero library, or from an open-access copy found by its DOI; give the user the DOIs that have neither, to add to the library. A source whose full text is not obtained keeps the depth Abstract, and R19 gives each decision that depends on it alone the status Open. In `docs/learning-research.md`, set the depth of each to Full and correct its population, material, design, retention interval, and effect size from the paper, and remove an entry whose participants are school children; search for sources on the three decisions that R19 labels as defaults (target recall, learning steps, review order) and on spaced retrieval of advanced mathematics, and add what is found; correct the statuses of R19; open an issue for each learning decision whose status changes
- [X] T004 [P] Add study fixture decks in `desktop/tests/fixtures/study/`: two decks in one folder and one deck at the top level, with a macro equation, a TikZ-cd diagram, an image, deck tags, card tags, and at least twelve cards in total

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: One running copy, the card ID in the render output, the typed study values, the store with its identity, the record database, and the host route

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T062 Add a failing step to `desktop/tests/native.py`: with the built app running, a second launch of the same executable exits, one window exists afterward, and that window has the focus (FR-047, SC-015). Measure whether the test's display session has a D-Bus session bus; when it has none, start one for the test in the `desktop-native-test` recipe of `justfile`, and replace the matching entry of the Unmeasured section of `specs/001-in-app-review/research.md` with the result
- [ ] T063 Add `tauri-plugin-single-instance` with version `*` to `desktop/src-tauri/Cargo.toml` and register it as the first plugin in `desktop/src-tauri/src/lib.rs`, with a callback that shows the main window and gives it the focus (R15); T062 passes
- [ ] T005 Add a failing case to `desktop/tests/paired-cards.test.ts`: the rendered deck of a paired-card source has, for each card, an `id` equal to its `card-id`, in front order
- [ ] T006 Pass each `card-id` from `desktop/paired-cards.lua` to the exporter filter and make `id` a required, non-empty field of `Card` in `desktop/backend.py` (contract: Render output); T005 passes and `just desktop-test` still produces the same packages
- [ ] T007 Add `desktop-study-test` to `test-commit` in `justfile`, and create `desktop/tests/study.py` with the scenario harness (temporary workspace copied from `desktop/tests/fixtures/study/`, temporary data and cache directories, store inspection with the `anki` library, record inspection with Python's `sqlite3` alone) and failing steps for `study-open` through the bridge route: with no store on disk, a workspace gets a store directory named by a store ID with a `store.json` that lists the workspace path; the R9 settings hold (FSRS on, `applyAllParentLimits` on, `leechAction` 1, `reviewOrder` 7, `maxTaken` 9999); `record.sqlite3` uses the write-ahead log and has the tables and the `review` view of `specs/001-in-app-review/data-model.md`, a `schema` row, a `writer` row with the app release and the Anki version, a `store_event` row of kind `created`, and a `parameter_set` row with source `anki-default`; an unreadable `collection.anki2` gives `StoreUnreadable` with the path and stays unchanged; a store directory with `store.json` and no `collection.anki2` gives `StoreUnreadable` and gets no new collection; a store directory with `store.json` and no `record.sqlite3` gives `StoreUnreadable` and gets no new record (FR-019)
- [ ] T008 Add failing steps to `desktop/tests/study.py` for store identity through the bridge route: with one store on disk, `study-open` for a workspace at another path returns `Unattached` with that store's paths, last use, and numbers of cards and grades, and creates nothing; `study-attach` with `existing` opens that store, adds the path to `store.json`, and writes a `store_event` row of kind `attached`; `study-attach` with `new` creates a second store and leaves the first unchanged; an unknown store ID gives `UnknownStore`
- [ ] T009 [P] Declare the study values and the fourteen study requests of `specs/001-in-app-review/data-model.md` and `contracts/study-bridge.md` as Pydantic models in `desktop/study/values.py`, with `extra="forbid"`, `limit` 1 to 8, each `Timing` field 0 or more with no upper bound, `new_per_day` 0 to 9999, `reviews_per_day` 0 to 9999, and `desired_retention` 0.70 to 0.99
- [ ] T010 [P] Declare the same values and requests as Zod schemas and inferred types in `desktop/src/bridge.ts`, with a typed `StudyError` and the two states of `StudyOpen`; `bunx tsc --noEmit` passes with no `any` or `unknown`
- [ ] T011 Implement the store in `desktop/study/store.py`: directory `user_data_path("math-flashcards")/study/<store ID>`, `store.json` with the store ID and the attached paths, lookup of the store whose current path is the workspace path, creation only when no store exists or on `study-attach` with `new`, creation of `collection.anki2` and `record.sqlite3` only in the call that creates the store directory, the R9 settings before the first queue build, and the `StoreUnreadable` and `UnknownStore` errors
- [ ] T012 Implement the learning record database in `desktop/study/record.py` with Python's `sqlite3`: creation of `record.sqlite3` with the tables and the `review` view of `specs/001-in-app-review/data-model.md`, the write-ahead log, the `schema` row, one `writer` row for each host start, the common columns (`at_ms`, `utc_offset_min`, `writer`), and one insert function for each table as the only write path; cite R12 of `specs/001-in-app-review/research.md` in the module comment as the reference
- [ ] T013 Implement the host loop in `desktop/study/host.py` and the `study-host` command in `desktop/backend.py` that starts it and gives it the deck render function: one JSON request per input line, one `{"ok": …}` response per output line, store held until input closes, and the `study-open` and `study-attach` actions with the count tree from `deck_due_tree()`
- [ ] T014 Add the study route to `desktop/src-tauri/src/lib.rs`: every `study-*` action goes to one host process that starts on first use, serves one request at a time, restarts after an early exit, and stops at app exit; add the store's media folder to the asset scope from the `study-open` result and enable the asset protocol in `desktop/src-tauri/tauri.conf.json`
- [ ] T015 [P] Add the same study route and a media route to the middleware in `desktop/vite.config.ts`; the T007 and T008 steps pass

**Checkpoint**: `just desktop-study-test` opens a real store with its record through the real bridge route

---

## Phase 3: User Stories 1 and 6 - Review due cards with a complete record (Priority: P1) 🎯 MVP

**Goal**: The user starts a study session of the workspace, sees a front, reveals the back, grades, and continues until study for today is complete. Every showing of a card is in the learning record with its content, subject, measured times, grade, and scheduler state, and the user reads the record with standard tools

**Independent Test (US1)**: On a workspace that was never studied, grade several cards, restart the app, and confirm that the graded cards keep their schedule and the others are still offered

**Independent Test (US6)**: Study several cards and leave one ungraded. Open the record with `sqlite3` while the app runs. Each presentation is present with its fields, and the record gives the text of each card as the user saw it

### Tests for User Stories 1 and 6 ⚠️

- [ ] T016 [US1] Add failing steps to `desktop/tests/study.py`: every fixture card is a new note whose GUID is its `card-id` after the window opens the workspace; the first card is reached from the open workspace in at most two actions (SC-001); **Study** shows a front with the back and grades hidden; Space reveals the back and four labelled grades; key 3 records one review log row and the stored interval agrees with the Good label; on later cards the keys 1, 2, and 4 each record their grade, and the stored interval agrees with the label of that grade (FR-007, SC-008); with an unsaved edit in the editor, **Study** saves the deck first and the session shows the saved text; the next card shows within 0.5 s; counts decrease; a card graded Again returns after its learning delay; after the last card the screen states that study is complete and gives the number graded; a restart keeps every grade
- [ ] T017 [US1] Add failing steps to `desktop/tests/study.py`: after a grade, `SIGKILL` of the host loses no review log row and no committed record row, and the next request starts a new host; a card with a macro equation, a TikZ-cd diagram, and an image renders all three, with a screenshot in `desktop/test-artifacts/`; the `Front` and `Back` of each studied note equal the fields of the same card in the package that the app generates for its deck (SC-007); an equation with an undefined macro shows the TeX error
- [ ] T018 [US6] Add failing steps to `desktop/tests/study.py` for the record of a presentation (FR-028, SC-009): after the first sync the record has a `card_change` row of kind `added` and a `content` row for each card; a session start writes a `session` row with its scope; after a wait of 2 s, a reveal, a wait of 1 s, and a grade, the `review` row has the time and offset, card ID, deck path, folder, deck title, deck tags and card tags, the front and back shown, session and position, kind, scheduler day, `reveal_ms` within 100 ms of 2000, `grade_ms` within 100 ms of 1000, the grade, four offered intervals of which the selected one agrees with the interval after, empty memory state before the first grade of a new card and a set memory state after it, target recall, parameter set, the daily limits, and the writer; its `revlog_*` values equal the store's review log row; with the focus away from the window for 2 s, `unfocused_ms` is within 100 ms of 2000; with the page clock advanced by 3 hours between reveal and grade, `grade_ms` is the full time and `revlog_time_ms` is Anki's limited value (SC-014); Escape with a card on screen leaves a `presentation` row with no `response` row and writes a `session_end` row with cause `left`
- [ ] T019 [US6] Add failing steps to `desktop/tests/study.py` for the record as an independent source: a second read-only `sqlite3` connection reads every row while the app runs, and the next grade succeeds (FR-037); the four queries of `specs/001-in-app-review/contracts/learning-record.md` give the numbers that the scenario's grades imply (SC-011, SC-012); with the app stopped, grades and due-date changes made with the `anki` library appear after the next open as `response` rows with `recovered` set and empty times, and every review log row has a `response` row with the same nine values (FR-036); a session that a `SIGKILL` left open gets a `session_end` row with cause `recovered`; every table and column of the record's schema is named in `docs/study-record.md` (FR-038); the Study screen shows the path of the record, and it is the file that the scenario reads (FR-042)
- [ ] T020 [US6] Add failing steps to `desktop/tests/study.py` for a moved workspace through the window (FR-041): after the workspace folder is renamed and opened, the window lists the existing store with its earlier path, last use, and numbers of cards and grades, no store directory is created, and the editor works; after the user attaches the store, the counts and every record row are as before the rename; in a second workspace the user selects a new store and the first store is unchanged
- [ ] T064 [US6] Add failing steps to `desktop/tests/study.py` for editor views (FR-058): a card that is open in the editor for 2 s, until another card is selected, has one `editor_view` row with its card ID, its deck path, and `shown_ms` within 100 ms of 2000; with the focus away from the window for 1 s of that time, `unfocused_ms` is within 100 ms of 1000; the card that is open when a study session starts has a row; a workspace in the `Unattached` state writes no row

### Implementation for User Stories 1 and 6

- [ ] T021 [US1] Implement the add path of `study-sync` in `desktop/study/sync.py`: for at most `limit` decks that are not current, render with the render function that the entry script gave, create the Anki deck `Workspace::<folders>::<file stem>`, add the notes in one `add_notes` call with GUID `card-id` and the rendered `Front` and `Back`, copy media through `col.media`, write the deck record of `input_hashes()` to the collection config, write a `card_change` row of kind `added` for each note and a `content` row with its `media` rows and `record-media/` files for each new front and back pair, and return `SyncResult` with `pending`
- [ ] T022 [US6] Implement in `desktop/study/session.py` the pure conversion of R13 from Anki's values (queued card, current and next states, card statistics, card after the answer, review log row) and the window's `Timing` to the `presentation` and `response` values of `specs/001-in-app-review/data-model.md`, with an empty value for each fact that was not observed
- [ ] T023 [US1] Implement `study-begin`, `study-next`, `study-answer`, and `study-end` in `desktop/study/session.py` by the R10 call sequence: a `session` row at begin; the top card of the scope's queue with a `presentation` row written before the response; Anki's four labels; the three counts; `Finished` with `next_learning_seconds` from `congratulations_info()`; `StaleCard` when `presentation` is not the session's last presentation or its card is not the top card; `reveal_ms + grade_ms` as Anki's answer time; the `response` row after `answer_card()` returns; a `session_end` row at end and for each open session when the host's input closes
- [ ] T024 [US6] Implement recovery at store open in `desktop/study/store.py`: one `response` row with `recovered` set for each review log row that has none, and one `session_end` row with cause `recovered` for each session that has none, by the pure comparison of review log IDs with `response` rows
- [ ] T025 [P] [US1] Add element typesetting for rendered card HTML to `desktop/src/math.ts`, using the loaded MathJax and `texOptions(macros)` of the active asset set
- [ ] T026 [P] [US1] Create `desktop/src/study.ts`: the session state (unattached, front, revealed, finished, error); the timing of each card with `performance.now()` for the time to reveal and the time to grade, and with the window's visibility and focus events for the time without focus; the sync loop that calls `study-sync` until `pending` is zero and reports progress; and the handling of `StaleCard` by fetching the current card
- [ ] T027 [US1] Create `desktop/src/study.tsx` and its styles in `desktop/src/App.css`: card front and back from the note HTML, image sources resolved against `media`, four grade buttons with Anki's labels, session counts, the finished state, the store error states, the keys Space, 1 to 4, and Escape, and `study-end` when the user leaves and when the queue is finished
- [ ] T028 [US1] Connect the screen in `desktop/src/App.tsx`: call `study-open` and run the sync loop at workspace open without blocking the editor, show sync progress, add **Study** to the workspace menu and the Ctrl-K commands, save pending edits before a session starts, and name the function **Study** everywhere (FR-027)
- [ ] T029 [US6] Add to `desktop/src/study.tsx` and `desktop/src/App.tsx` the attach list for the `Unattached` state (each store with its paths, whether its current path exists, last use, and numbers of cards and grades; **Attach** and **Start new**), and the paths of the learning record and the store with a command that opens the folder
- [ ] T030 [P] [US6] Write `docs/study-record.md`: the location of the record and how to open it read-only; for each table and each column its meaning, unit, value coding, and the case in which it is empty; the `review` view; the guarantees of `specs/001-in-app-review/contracts/learning-record.md`; the mapping to the columns of the `anki-revlogs-10k` research data set; and the example queries
- [ ] T065 [US6] Implement `study-viewed` in `desktop/study/session.py` with its insert function for `editor_view` in `desktop/study/record.py`
- [ ] T066 [US6] Measure editor views in `desktop/src/study.ts` (the time a card is open and the time without focus, with `performance.now()` and the window's visibility and focus events) and send `study-viewed` from `desktop/src/App.tsx` when the card leaves the editor: another card is selected, the deck closes, a study session starts, or the window closes

**Checkpoint**: The T016 to T020 and T064 steps pass; the workspace can be studied end to end and each showing of a card is in the record. Use on the real data directory starts after this checkpoint, not before

---

## Phase 4: User Story 2 - Deck changes reach review and keep history (Priority: P1)

**Goal**: A saved or external deck change reaches the store with no user action, and a card keeps its history through edits, moves, renames, merges, removal, and return

**Independent Test**: Give a card an interval, edit its text, move it to another deck, and rename that deck; the card keeps its due date, shows the new text, and belongs to the renamed deck

### Tests for User Story 2 ⚠️

- [ ] T031 [US2] Add failing steps to `desktop/tests/study.py`, each on a card that has a review log row and a due date set with `sched.set_due_date()`: an edit of the back in the editor reaches the store within 10 s with the same due date; a move to another deck by a file edit on disk changes the Anki deck and keeps the review log; a deck rename, a deck merge, and a reorder of the cards in a deck keep each due date and review log (SC-004); a card deleted from its deck leaves the counts and is suspended in `Removed`; the same card pasted back has its due date; a new card appears as new; one `card-id` in two decks is named with both paths in the Problems list and its note stays with the first deck; a deck with invalid structure keeps its last synced cards; with a session open, a file edit on disk of the card on screen shows the new text of that card, and the removal on disk of the card on screen shows the next card
- [ ] T032 [US2] Add failing steps to `desktop/tests/study.py` for the record of deck changes: each content change, tag change, move, removal, and restore has one `card_change` row of its kind (FR-033); a card that is reviewed, edited, and reviewed again has two `review` rows with the earlier and the later back, and the earlier `content` row is unchanged (FR-030); an image replaced under the same file name leaves the earlier bytes in `record-media/`; `presentation` rows written before a move keep the earlier deck path; a note that has the tag `leech` keeps it when its card's tags change in the deck (FR-045)
- [ ] T033 [US2] Add a failing step to `desktop/tests/study.py`: `study-sync` on an unchanged workspace returns zero counts, changes no row of the collection, and writes no record row, and no sync step changes a schedule or a review log row (invariant 3)

### Implementation for User Story 2

- [ ] T034 [US2] Implement the sync plan in `desktop/study/sync.py` as one function of the rendered decks and a store snapshot (GUID to deck, sides, deck and card tags, scheduler tags, suspended): adds, field and tag updates, moves, removals, restores, and duplicates, by the R6 rules for current and not-current decks
- [ ] T035 [US2] Apply the plan in `study-sync` in `desktop/study/sync.py`: `update_notes(skip_undo_entry=True)` with the scheduler's tags kept, `set_deck`, suspend then move to `Removed`, move back then unsuspend, removal of an Anki deck under `Workspace` only after its cards have left it, removal of the deck record of a deleted file, one `card_change` row for each applied change, one `content` row with its media for each new front and back pair, and `failed` and `duplicates` in the result
- [ ] T036 [US2] Trigger the sync loop in `desktop/src/App.tsx` after each successful save, after each file-watch refresh, and before a session starts; when the card on screen changed or left, show the current card
- [ ] T037 [P] [US2] Show each duplicate `card-id` as a problem that names both decks in `desktop/src/problems.ts` and `desktop/src/problem-drawer.tsx`

**Checkpoint**: The T031 to T033 steps pass; editing and studying can alternate

---

## Phase 5: User Story 3 - See what is due and choose what to review (Priority: P2)

**Goal**: The tree shows new, learning, and due counts for each deck and folder, and a session can cover one deck, one folder, or the workspace

**Independent Test**: Grade cards in two decks of one folder; the counts of each deck and of the folder change to match, and a session started on one deck offers only its cards

### Tests for User Story 3 ⚠️

- [ ] T038 [P] [US3] Add failing units in `desktop/tests/study.test.ts`: a workspace, folder, or deck scope maps to its entry of the count tree, and a deck path with nested folders maps to nested entries
- [ ] T039 [US3] Add failing steps to `desktop/tests/study.py`: with cards made due through the `anki` library while the app is stopped, the tree shows the new, learning, and review counts on each deck and folder within 2 s of opening; a grade updates the deck and every folder above it; **Study** on a deck offers only its cards; **Study** on a folder offers the cards of every deck below it; the `session` row of each holds its scope

### Implementation for User Story 3

- [ ] T040 [US3] Implement `study-counts` and the `UnknownScope` error in `desktop/study/store.py`, and the pure mapping from `Scope` and `DeckPath` to Anki deck names
- [ ] T041 [US3] Show the three counts on each deck and folder of the tree in `desktop/src/App.tsx`, refresh them after each grade and each sync, and add **Study** to the deck and folder context menus with the matching scope, using the mapping in `desktop/src/study.ts`

**Checkpoint**: The T038 and T039 cases pass

---

## Phase 6: User Story 4 - Correct a grade or a card during review (Priority: P2)

**Goal**: The user undoes the last grade, and opens the card on screen in the editor and returns

**Independent Test**: Grade a card and undo; the card returns with its earlier schedule, and the record keeps the grade with the time of the undo. Open the card in the editor from the session, change it, return; the session shows the new text

### Tests for User Story 4 ⚠️

- [ ] T042 [US4] Add failing steps to `desktop/tests/study.py`: Ctrl-Z after a grade removes the review log row and returns the card with its earlier state; the record still has the `response` row, has an `undo` row that refers to it, shows `undone_at_ms` in the `review` view, and has a new `presentation` row for the returned card (FR-031); key E opens that card in its deck in the editor; after an edit and a return the same card shows the new text; after that sync Undo is disabled and its tooltip gives the reason, and it is enabled again after the next grade

### Implementation for User Story 4

- [ ] T043 [US4] Implement `study-undo` and the `undoable` value in `desktop/study/session.py` from Anki's undo status: undo only when the last undo step is a grade, an `undo` row for the undone `response` row, `StaleCard` otherwise
- [ ] T044 [US4] Add Undo (button and Ctrl-Z, with the disabled reason) and Edit (button and key E, with the return to the session) to `desktop/src/study.tsx`, and the editor round trip to `desktop/src/App.tsx`

**Checkpoint**: The T042 steps pass

---

## Phase 7: User Story 5 - Control the daily load (Priority: P3)

**Goal**: The user sets new cards per day, reviews per day, and target recall

**Independent Test**: Set the new-card limit to a small number and confirm that a session offers exactly that many new cards

### Tests for User Story 5 ⚠️

- [ ] T045 [US5] Add failing steps to `desktop/tests/study.py`: with new cards per day set to 3, a workspace session offers exactly 3 new cards and the root count shows 3; with reviews per day set to 2 and five cards made due through the `anki` library, a workspace session offers exactly 2 review cards; a higher target recall gives a shorter Good interval for a card in the same state; a target recall of 1.0 shows its bound and leaves the stored value; the settings remain after a restart; each change has a `setting_change` row with the earlier and the later value, and later `presentation` rows hold the later values (FR-034); three due review cards whose estimated recall differs are offered in ascending order of `before_retrievability` (FR-044); replace the `reviewOrder` entry of the Unmeasured section of `specs/001-in-app-review/research.md` with the result

### Implementation for User Story 5

- [ ] T046 [US5] Implement `study-set-settings` in `desktop/study/settings.py`: `new_per_day` 0 to 9999, `reviews_per_day` 0 to 9999, `desired_retention` 0.70 to 0.99, `InvalidSettings` outside a bound, the one preset that all decks share, and one `setting_change` row for each value that changed
- [ ] T047 [US5] Add the settings form to `desktop/src/study.tsx` with the three fields, their bounds, and the count refresh after a change

**Checkpoint**: The T045 steps pass

---

## Phase 8: User Story 7 - Fit the scheduler to my own history (Priority: P3)

**Goal**: The user fits the scheduler's parameters to their own history with Anki's fitting code, sees Anki's measures of the fit, and accepts or rejects it

**Independent Test**: With a prepared history of sufficient size, run the fit, accept it, and confirm that the preset holds the fitted parameters and that the record holds the earlier and the later parameter sets with their times

### Tests for User Story 7 ⚠️

- [ ] T048 [US7] Call `compute_fsrs_params` and `evaluate_params_legacy` of the `anki` wheel on a collection in a temporary directory with dated review log rows written through the `anki` library's database handle, find the smallest history that Anki's fit accepts and the time the fit takes, and replace the two fit entries of the Unmeasured section of `specs/001-in-app-review/research.md` with the results
- [ ] T049 [US7] Add failing steps to `desktop/tests/study.py`: the fit on a store with no review states that the history is too small and changes nothing; with the history of T048 added while the app is stopped, the fit shows the fitted parameters, the number of reviews used, and Anki's two measures for the fitted and the current set; closing the fit without accepting changes nothing; accepting sets the preset's parameters, writes a `parameter_set` row with source `fit` and its measures and a `setting_change` row, and later `presentation` rows refer to the new set (FR-046)

### Implementation for User Story 7

- [ ] T050 [US7] Implement `study-fit` and `study-apply-fit` in `desktop/study/settings.py` by R14: Anki's fit on the whole store, `evaluate_params_legacy` for both parameter sets, `NotEnoughHistory` for Anki's insufficient-data error and for a fit that used no review, the preset's `fsrsParams6` on apply, and the `parameter_set` and `setting_change` rows
- [ ] T051 [US7] Add the fit command to the settings of `desktop/src/study.tsx`: progress while the fit runs, both sets of measures, **Apply** and **Close**, and the `NotEnoughHistory` statement

**Checkpoint**: The T049 steps pass

---

## Phase 9: User Story 8 - See statistics from my record and add new ones safely (Priority: P2)

**Goal**: The user opens **Statistics**, selects an analysis, and sees its result from the learning record. An analysis only reads the record, and a new analysis is one new module that changes no core file and no stored data

**Independent Test**: Study several cards. Open Statistics and run each analysis; the numbers agree with the grades given. Add a new analysis; no part of study or of the record changes, and the earlier analyses give the same results

### Tests for User Story 8 ⚠️

- [ ] T067 [US8] Add failing steps to `desktop/tests/study.py`: **Statistics** in the workspace menu lists the two analyses of `specs/001-in-app-review/contracts/analysis.md` with their titles and summaries, each summary and each column of a measure from grades has the words "self-graded" (FR-059), and the summary of `recall_by_folder` states that its result is about recall of the cards of the folder (FR-060); `recall_by_folder` shows, for each folder and month, the number of presentations, the share graded Again, and the mean time to reveal that the scenario's grades imply, equal to the first query of `contracts/learning-record.md`; `calibration` shows bands whose numbers of grades sum to the number of review grades that were not undone; with a session in progress, an analysis runs and the next grade is recorded; a dump of every record row is equal before and after each analysis runs (SC-019)
- [ ] T068 [US8] Create `desktop/tests/analysis.py` and a `desktop-analysis-test` recipe in `justfile` that is part of `test-commit`. The test copies `desktop/backend.py`, `desktop/study/`, and `desktop/analysis/` to a temporary directory, calls the entry script there as the bridge does (one process and one JSON request for each action), and uses a record under a temporary `XDG_DATA_HOME`. Failing steps: `analysis-list` gives the catalog in the order of the titles; after one module is added to the temporary catalog, the list holds it, its result is the table that it returns, and the results of the earlier analyses are equal to those before (SC-018); a module that raises gives `AnalysisFailed` with its text, and the other analyses run; a module that executes an `INSERT` gives `AnalysisFailed` that names a read-only database, and every record row is equal afterward; a module that does not import is in the list with its `failure`; an unknown name gives `UnknownAnalysis`; a path outside the study data directory gives `RecordUnreadable`

### Implementation for User Story 8

- [ ] T069 [US8] Implement `desktop/analysis/__init__.py`: the `Analysis`, `Column`, `AnalysisTable`, and `AnalysisError` values of `specs/001-in-app-review/data-model.md` as Pydantic models; the path rule and the read-only connection of `contracts/analysis.md`; the list of the catalog with `pkgutil.iter_modules`, with a `failure` for a module that does not import; and the run of one analysis. Cite the `sqlite3` URI documentation and R17 in the module comment
- [ ] T070 [P] [US8] Implement `desktop/analysis/catalog/recall_by_folder.py`: title, summary, and one function from the read-only connection to the table of FR-056 for folders and months; the column label and the summary name the share as self-graded and the result as recall of the cards (FR-059, FR-060)
- [ ] T071 [P] [US8] Implement `desktop/analysis/catalog/calibration.py`: title, summary, and one function from the read-only connection to the table of FR-056 for predicted against observed recall, in bands of `before_retrievability`; the column label and the summary name the observed recall as self-graded (FR-059)
- [ ] T072 [US8] Add the `analysis-list` and `analysis-run` requests to the entry script `desktop/backend.py` and their Zod schemas to `desktop/src/bridge.ts`; both use the existing route of one process for each request, and neither reaches the study host; the T068 steps pass
- [ ] T073 [US8] Create `desktop/src/statistics.tsx` and its styles in `desktop/src/App.css`: the list of analyses, the run of the selected one, one table renderer for every `AnalysisTable` with column names and units, and the failure of an analysis in place of its table; add **Statistics** to the workspace menu and the Ctrl-K commands in `desktop/src/App.tsx`; the T067 steps pass
- [ ] T074 [P] [US8] Write `docs/analyses.md`: what an analysis is; the rules of `specs/001-in-app-review/contracts/analysis.md`; how to add one (one module and its test, and no other file); where the field reference of the record is (`docs/study-record.md`); and what to do when the record does not hold a needed fact (a core change that adds a table or a nullable column, never an analysis that writes)

**Checkpoint**: The T067 and T068 steps pass; `just desktop-boundaries` passes

---

## Phase 10: Keeping the data (FR-049, FR-050)

**Goal**: The user writes a complete copy of a store to a directory of their choice from inside the running app, and a copy attaches on any machine

**Independent Test**: Save a copy during a session. Start the app on an empty data directory, place the copy there, and attach it; the counts and every record row are those of the store at the time of the copy

### Tests for the copy ⚠️

- [ ] T075 Add failing steps to `desktop/tests/study.py`: with a session in progress, **Save a copy** in the Study settings, with a temporary directory, writes `math-flashcards-study-<time>/<store ID>/` with `store.json`, `collection.anki2`, `record.sqlite3`, and `record-media/`; `sqlite3` opens the copy's record and finds every row that was committed before the copy; the store's record has a `store_event` row of kind `copied` with that path; the next grade succeeds, and Undo is unavailable until it; a directory that does not exist gives `CopyFailed` with the cause, and the store is unchanged; after the app is stopped and started with an empty `XDG_DATA_HOME` in which the copy is placed under `math-flashcards/study/`, the window lists the copy, and after the user attaches it the counts and every record row equal those of the copy (SC-017)

### Implementation for the copy

- [ ] T076 Implement `study-copy` in `desktop/study/store.py` by R18: close the collection and the record, copy the store directory with `shutil.copytree`, open both again, write the `store_event` row, and return `CopyFailed` with the store open and unchanged when the copy cannot be written
- [ ] T077 Add **Save a copy** to the Study settings in `desktop/src/study.tsx`, with the folder picker of the dialog plugin, progress while the copy runs, and the path of the finished copy

**Checkpoint**: The T075 steps pass

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Backups, permanence across the whole scenario, file placement, the native path, installation, documentation, and measurements

- [ ] T078 Add a step to `desktop/tests/native.py`: the built app runs the study step with an empty directory as `HOME` and with `XDG_DATA_HOME`, `XDG_CONFIG_HOME`, `XDG_STATE_HOME`, and `XDG_CACHE_HOME` set to four directories inside it; afterward every file under that `HOME` is under one of the four directories; after the cache and state directories are removed and the app starts again, every record row is equal and the counts are as before (FR-048, SC-016). Add the same assertion for the bridge processes at the end of `desktop/tests/study.py`
- [ ] T052 Add failing steps to `desktop/tests/study.py`, then make them pass in `desktop/study/store.py`: the host writes an Anki backup to the store's `backups/` folder at open and at exit when Anki's backup interval allows, with a copy of the record made by `sqlite3.Connection.backup` under the same time, which `sqlite3` opens with the same number of rows in each table (FR-040); a record copy stays while the `.colpkg` of the same time stays; **Rebuild cached data** leaves the store, its review log, and the record unchanged; a review card whose lapse count is one below Anki's leech threshold, graded Again, stays unsuspended, returns in the session, and has the tag `leech` (FR-024, FR-045); Anki's database check (`fix_integrity()`) reports no problem at the end of the scenario; a package generated for a studied deck has the same content and status as before
- [ ] T053 Add a step at the end of `desktop/tests/study.py`: every record row that the scenario read at an earlier step is equal at the end, and no row is missing, across undo, edits, moves, removals, **Rebuild cached data**, and the change of the workspace path (SC-010)
- [ ] T054 Save the record that the scenario produces as `desktop/tests/fixtures/study/record-v1.sqlite3` with a dump of its rows beside it, and add a step to `desktop/tests/study.py`: the host opens a store that holds this record, every row equals the dump, and the `review` view reads it (FR-039, SC-013); add a step to `desktop/tests/analysis.py`: each analysis of the catalog runs on this record and returns a table; document in `docs/study-record.md` that this fixture is never regenerated
- [ ] T055 [P] Add one study step to `desktop/tests/native.py`: in the built window, start a session, grade a card, and confirm the review log row and the `review` row in the isolated store, with an image card visible through the asset protocol
- [ ] T056 [P] Make `desktop/linux/install.py` copy `desktop/study/` and `desktop/analysis/` into the release beside the entry script, and make the release validation import `anki`, `study`, and `analysis` in the release environment and fail the candidate release when an import fails; extend `desktop/tests/installation.py` for it, and assert there that a store under the data directory, with its record, is unchanged by the installation of a new release (FR-017)
- [ ] T057 [P] Document Study and Statistics in `desktop/README.md` (use, keys, settings, the fit, store and record location, saving a copy, attaching a store after a move or on a new machine, backups, the one running copy, where each kind of file is placed, test recipes) and record the `anki`, `tauri-plugin-single-instance`, and Import Linter dependencies and the three parts in `docs/desktop-dependency-survey.md`
- [ ] T058 Run the manual table of `specs/001-in-app-review/quickstart.md` on the repository's `decks/` folder with a temporary `XDG_DATA_HOME`; replace the entries of the Unmeasured section of `specs/001-in-app-review/research.md` for the first-sync time, the save-to-review time, the copy time, and the record size with the measured values, and add the measured count time and the time to the next card for 20 grades (SC-002, SC-006); the entry on a retained earlier release stays until an `anki` release changes the collection format; open an issue for each criterion that fails
- [ ] T059 Run `just test-commit` and confirm that the whole suite stays under five minutes

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies. T002 is in another repository and must be pushed before T006. T060 comes before T061, and T061 comes before every task that names a file in `desktop/study/` or `desktop/analysis/`. T080 comes first. T079 changes no code and blocks no task of Phases 1 and 2, which hold no learning decision. It is complete before Phase 3 starts: principle X requires the full text for a decision that depends on one paper, and Phase 3 builds such decisions. A status that it changes in R19 goes to the user before the story that it affects starts.
- **Foundational (Phase 2)**: Depends on Setup. Blocks every story. T062 and T063 come first: the store's design depends on one running copy.
- **US1 and US6 (Phase 3)**: Depends on Foundational.
- **US2 to US5 and US7 (Phases 4 to 8)**: Each depends on Phase 3. None depends on another.
- **US8 (Phase 9)**: Depends on Phase 3 for a record with rows. It depends on no other story and changes no file of `desktop/study/`.
- **Keeping the data (Phase 10)**: Depends on Phase 3.
- **Polish (Phase 11)**: Depends on the stories that are in the release. T053 and T054 need US2 and US4; the analysis step of T054 needs US8; T055 and T078 need Phase 3; T058 needs US1 to US3 and Phase 10.

### Within Each Phase

- A test task is committed and fails for its stated reason before the implementation tasks of its phase start.
- Bridge values before bridge actions; bridge actions before window code that calls them.
- `desktop/tests/study.py`, the modules of `desktop/study/`, and `desktop/src/App.tsx` are each changed by many tasks; tasks on the same file run in order.
- In Phase 3, T022 comes before T023, which writes the rows that T022 builds.
- T048 comes before T049: the fit test needs the measured history size.

### Parallel Opportunities

- T004 beside T001 to T003.
- T009 and T010; T015 beside T014.
- T025, T026, and T030 beside T021 to T024.
- T037 beside T034 to T036; T038 beside T039.
- T070, T071, and T074 beside T069.
- T055, T056, and T057.
- After Phase 3, the phases US2 to US5 and US7 can proceed in parallel when their changes to `desktop/study/` and `desktop/src/App.tsx` are merged in order.
- US8 proceeds in parallel with every core phase: it shares no Python file with them.

## Parallel Example: User Stories 1 and 6

```text
After T016 to T020 are committed and failing:
  Task: "T021 add path of study-sync in desktop/study/sync.py"
  Task: "T022 conversion in desktop/study/session.py"          then T023 (same file), T024
  Task: "T025 element typesetting in desktop/src/math.ts"
  Task: "T026 session state, timing, and sync loop in desktop/src/study.ts"
  Task: "T030 field reference in docs/study-record.md"
Then T027 (study.tsx), T028 (App.tsx), T029 (attach list and record location), T065 and T066 (editor views).
```

## Implementation Strategy

### MVP First (User Stories 1 and 6)

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3.
3. Validate with `just desktop-study-test`.

The record is complete from the first real grade: the app is used on the real data
directory only after Phase 3. After Phase 3 alone, a saved edit reaches the store only as
a new card ID; edits to existing cards need US2. Daily use with continued editing
therefore needs Phase 3 and US2.

### Incremental Delivery

1. Setup and Foundational: the three parts with their checked boundaries; one running copy; a real store with its record opens through the real bridge route.
2. US1 and US6: the workspace can be studied, and every showing of a card is recorded.
3. US2: editing and studying can alternate; the record holds each card change.
4. US3: counts and deck or folder sessions.
5. US4: Undo and Edit.
6. US5: load settings.
7. US7: fit to the user's own history.
8. US8: Statistics with the first two analyses. Every later analysis is one module.
9. Keeping the data: a complete copy to a chosen directory.
10. Polish: backups, permanence checks, the first-version record fixture, file placement, native proof, installation, documentation, measurements.

## Notes

- Every test run uses temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME`. The real review history and the real learning record are never a test target.
- The store is user data. No task deletes a store, and no task adds a migration or an import of earlier history.
- A change to the record's schema after T054 adds tables or nullable columns and a `schema` row. The T054 step is the proof that earlier rows stay readable.
- An analysis that is added after this feature needs no task here: one module in `desktop/analysis/catalog/`, its test in `desktop/tests/analysis.py`, and `docs/analyses.md` as the guide.
- Commit after each task. A failing test commit that a hook rejects uses the repository's sanctioned route for red commits.
