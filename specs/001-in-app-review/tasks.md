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
the copy, and the analyses. A task ID does not give the order of work. An open task
blocks a later task only when the later task uses its result. T079 blocks no code, but
a learning decision of R19 is accepted only after T079 (constitution X). The tier
classification of T081 comes before T059. T083 comes before the other tasks of
Phase 12, and T085 to T088 complete T016, T018, T019, and T078. The test steps that a task puts in `desktop/tests/study.py` can be in a
`desktop/tests/study-*.py` scenario or in `desktop/tests/native-study.py`.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependency on an incomplete task)
- **[Story]**: The user story the task belongs to (US1 to US8)
- Paths are relative to the repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Dependencies, test isolation, and fixtures

- [X] T080 Open the owning GitHub issue of this feature, with the purpose of `specs/001-in-app-review/spec.md` in the repository's own words and a link to this directory. Each failing test commit that the commit hook rejects goes through the sanctioned route for red commits with this issue's number, and each issue that a later task opens refers to it. Owner: [issue #2](https://github.com/dzackgarza/math-flashcards/issues/2).
- [X] T001 Add `anki` with no version pin to the PEP 723 dependency block of `desktop/backend.py`, and confirm that `just desktop-dependencies` prepares an environment in which `import anki` succeeds
- [X] T003 In `justfile`, make the `desktop-test` recipe set `XDG_DATA_HOME` to a temporary directory beside its `XDG_CACHE_HOME` override, and add a `desktop-study-test` recipe that runs `desktop/tests/study.py` against `just desktop-web` with temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME`
- [X] T060 Create `desktop/tests/boundaries.py` and a `desktop-boundaries` recipe in `justfile` that runs it and is part of `test-commit`: the test runs `uvx --from import-linter lint-imports` on `desktop/` and requires status 0; then, in a temporary copy of `desktop/study/` and `desktop/analysis/` with `desktop/.importlinter`, it adds one violating import at a time (an analysis imports `study`; an analysis imports `anki`; an analysis imports `backend`; the core imports `analysis`; one analysis imports another) and requires status 1 with the import named in the report for each. The test fails first because the packages and the contract file do not exist
- [X] T061 Create the packages `desktop/study/` and `desktop/analysis/` with `desktop/analysis/catalog/`, and `desktop/.importlinter` with `root_packages` `study` and `analysis`, `include_external_packages = True`, and three contracts (R17 of `specs/001-in-app-review/research.md`): forbidden `analysis` to `study`, `anki`, `backend`; forbidden `study` to `analysis`; independence of `analysis.catalog.*`. Make `desktop/backend.py` add its own directory to `sys.path` before it imports either package; T060 passes
- [ ] T079 [P] Read the full text of each source that R19 of `specs/001-in-app-review/research.md` cites. Take each text from the Zotero library, or from an open-access copy found by its DOI; give the user the DOIs that have neither, to add to the library. A source whose full text is not obtained keeps the depth Abstract, and R19 gives each decision that depends on it alone the status Open. In `docs/learning-research.md`, set the depth of each to Full and correct its population, material, design, retention interval, and effect size from the paper, and remove an entry whose participants are school children; search for sources on the three decisions that R19 labels as defaults (target recall, learning steps, review order) and on spaced retrieval of advanced mathematics, and add what is found; correct the statuses of R19; open an issue for each learning decision whose status changes
- [X] T004 [P] Add study fixture decks in `desktop/tests/fixtures/study/`: two decks in one folder and one deck at the top level, with a macro equation, a TikZ-cd diagram, an image, deck tags, card tags, and at least twelve cards in total

---

## Phase 2: Foundational

**Purpose**: One running copy, native card identities and source, typed study values, the store with its identity, the record database, and the host route

Story work follows its actual code and data dependencies. Logging accompanies each
operation. Whole-run timing classification does not block a missing user capability.

- [ ] T081 Apply constitution XII to the test runners and application operations: retain test context, logs, setup and nested timings in `test-history/`; write detailed application logs and operation timings under the XDG state directory; include child-process work and the source, runtime, and input context needed for comparisons. Use the existing Study evidence capture as the first caller. Classify the real user-story scenarios into tier 1 and milestone tiers, measure the complete tier 1 loop, and use a cost triage table at the owning design before optimizing any slow operation.

- [X] T062 Add a failing step to `desktop/tests/native.py`: with the built app running, a second launch of the same executable exits, one window exists afterward, and that window has the focus (FR-047, SC-015). Measure whether the test's display session has a D-Bus session bus; when it has none, start one for the test in the `desktop-native-test` recipe of `justfile`, and replace the matching entry of the Unmeasured section of `specs/001-in-app-review/research.md` with the result
- [X] T063 Add `tauri-plugin-single-instance` with version `*` to `desktop/src-tauri/Cargo.toml` and register it as the first plugin in `desktop/src-tauri/src/lib.rs`, with a callback that shows the main window and gives it the focus (R15); T062 passes
- [X] T007 Add `desktop-study-test` to `test-commit` in `justfile`, and create `desktop/tests/study.py` with the scenario harness (temporary workspace copied from `desktop/tests/fixtures/study/`, temporary data and cache directories, store inspection with the `anki` library, record inspection with Python's `sqlite3` alone) and failing steps for `study-open` through the bridge route: with no store on disk, a workspace gets a store directory named by a store ID with a `store.json` that lists the workspace path; the R9 settings hold (FSRS on, `applyAllParentLimits` on, `leechAction` 1, `reviewOrder` 7, `maxTaken` 9999); `record.sqlite3` uses the write-ahead log and has the tables and the `review` view of `specs/001-in-app-review/data-model.md`, a `schema` row, a `writer` row with the app release and the Anki version, a `store_event` row of kind `created`, and a `parameter_set` row with source `anki-default`; an unreadable `collection.anki2` gives `StoreUnreadable` with the path and stays unchanged; a store directory with `store.json` and no `collection.anki2` gives `StoreUnreadable` and gets no new collection; a store directory with `store.json` and no `record.sqlite3` gives `StoreUnreadable` and gets no new record (FR-019)
- [X] T008 Add failing steps to `desktop/tests/study.py` for store identity through the bridge route: with one store on disk, `study-open` for a workspace at another path returns `Unattached` with that store's paths, last use, and numbers of cards and grades, and creates nothing; `study-attach` with `existing` opens that store, adds the path to `store.json`, and writes a `store_event` row of kind `attached`; `study-attach` with `new` creates a second store and leaves the first unchanged; an unknown store ID gives `UnknownStore`
- [X] T009 [P] Declare the study values and the fourteen study requests of `specs/001-in-app-review/data-model.md` and `contracts/study-bridge.md` as Pydantic models in `desktop/study/values.py`, with `extra="forbid"`, native deck batches of at most eight, each `Timing` field 0 or more with no upper bound, `new_per_day` 0 to 9999, `reviews_per_day` 0 to 9999, and `desired_retention` 0.70 to 0.99
- [X] T010 [P] Declare the same values and requests as Zod schemas and inferred types in `desktop/src/bridge.ts`, with a typed `StudyError` and the two states of `StudyOpen`; `bunx tsc --noEmit` passes with no `any` or `unknown`
- [X] T011 Implement the store in `desktop/study/store.py`: directory `user_data_path("math-flashcards")/study/<store ID>`, `store.json` with the store ID and the attached paths, lookup of the store whose current path is the workspace path, creation only when no store exists or on `study-attach` with `new`, creation of `collection.anki2` and `record.sqlite3` only in the call that creates the store directory, the R9 settings before the first queue build, and the `StoreUnreadable` and `UnknownStore` errors
- [X] T012 Implement the learning record database in `desktop/study/record.py` with Python's `sqlite3`: creation of `record.sqlite3` with the tables and the `review` view of `specs/001-in-app-review/data-model.md`, the write-ahead log, the `schema` row, one `writer` row for each host start, the common columns (`at_ms`, `utc_offset_min`, `writer`), and one insert function for each table as the only write path; cite R12 of `specs/001-in-app-review/research.md` in the module comment as the reference
- [X] T013 Implement the host loop in `desktop/study/host.py` and the `study-host` command in `desktop/backend.py`: accept native study values; one JSON request per input line, one `{"ok": …}` response per output line, store held until input closes, and the `study-open` and `study-attach` actions with the count tree from `deck_due_tree()`; keep command-specific dependencies local to their commands
- [X] T014 Add the study route to `desktop/src-tauri/src/lib.rs`: every `study-*` action goes to one host process that starts on first use, serves one request at a time, restarts after an early exit, and stops at app exit; add the store's media folder to the asset scope from the `study-open` result and enable the asset protocol in `desktop/src-tauri/tauri.conf.json`
- [X] T015 [P] Add the same study route and a media route to the middleware in `desktop/vite.config.ts`; the T007 and T008 steps pass

**Checkpoint**: `just desktop-study-test` opens a real store with its record through the real bridge route

---

## Phase 3: User Stories 1 and 6 - Review due cards with a complete record (Priority: P1) 🎯 MVP

**Goal**: The user starts a study session of the workspace, sees a front, reveals the back, grades, and continues until study for today is complete. Every showing of a card is in the learning record with its content, subject, measured times, grade, and scheduler state, and the user reads the record with standard tools

**Independent Test (US1)**: On a workspace that was never studied, grade several cards, restart the app, and confirm that the graded cards keep their schedule and the others are still offered

**Independent Test (US6)**: Study several cards and leave one ungraded. Open the record with `sqlite3` while the app runs. Each presentation is present with its fields, and the record gives the text of each card as the user saw it

### Tests for User Stories 1 and 6 ⚠️

- [X] T016 [US1] Add failing steps to `desktop/tests/study.py`: every fixture card is a new note whose GUID is its `card-id` after the window opens the workspace; the first card is reached from the open workspace in at most two actions (SC-001); **Study** shows a front with the back and grades hidden; Space reveals the back and four labelled grades; key 3 records one review log row and the stored interval agrees with the Good label; on later cards the keys 1, 2, and 4 each record their grade, and the stored interval agrees with the label of that grade (FR-007, SC-008); with an unsaved edit in the editor, **Study** saves the deck first and the session shows the saved text; the next card shows within 0.5 s; counts decrease; a card graded Again returns after its learning delay; after the last card the screen states that study is complete and gives the number graded; a restart keeps every grade
- [X] T017 [US1] Add failing steps to `desktop/tests/study.py`: after a grade, `SIGKILL` of the host loses no review log row and no committed record row, and the next request starts a new host; a card with a macro equation, a TikZ-cd diagram, and an image renders all three through the shared editor renderer, with a screenshot in the run's directory under `test-history/`; each studied side uses the same native source as the editor (SC-007); the content record holds the exact saved front and back source, while the Anki note's GUID and sole `CardId` field equal the native card ID (FR-025); an equation with an undefined macro shows the TeX error
- [X] T018 [US6] Add failing steps to `desktop/tests/study.py` for the record of a presentation (FR-028, SC-009): after the first sync the record has a `card_change` row of kind `added` and a `content` row for each card; a session start writes a `session` row with its scope; after a wait of 2 s, a reveal, a wait of 1 s, and a grade, the `review` row has the time and offset, card ID, deck path, folder, deck title, deck tags and card tags, the front and back shown, session and position, kind, scheduler day, `reveal_ms` within 100 ms of 2000, `grade_ms` within 100 ms of 1000, the grade, four offered intervals of which the selected one agrees with the interval after, empty memory state before the first grade of a new card and a set memory state after it, target recall, parameter set, the daily limits, and the writer; its `revlog_*` values equal the store's review log row; with the focus away from the window for 2 s, `unfocused_ms` is within 100 ms of 2000; with the page clock advanced by 3 hours between reveal and grade, `grade_ms` is the full time and `revlog_time_ms` is Anki's limited value (SC-014); Escape with a card on screen leaves a `presentation` row with no `response` row and writes a `session_end` row with cause `left`
- [X] T019 [US6] Add failing steps to `desktop/tests/study.py` for the record as an independent source: a second read-only `sqlite3` connection reads every row while the app runs, and the next grade succeeds (FR-037); the four queries of `specs/001-in-app-review/contracts/learning-record.md` give the numbers that the scenario's grades imply (SC-011, SC-012); with the app stopped, grades and due-date changes made with the `anki` library appear after the next open as `response` rows with `recovered` set and empty times, and every review log row has a `response` row with the same nine values (FR-036); a session that a `SIGKILL` left open gets a `session_end` row with cause `recovered`; every table and column of the record's schema is named in `docs/study-record.md` (FR-038); the Study screen shows the path of the record, and it is the file that the scenario reads (FR-042)
- [X] T020 [US6] Add failing steps to `desktop/tests/study.py` for a moved workspace through the window (FR-041): after the workspace folder is renamed and opened, the window lists the existing store with its earlier path, last use, and numbers of cards and grades, no store directory is created, and the editor works; after the user attaches the store, the counts and every record row are as before the rename; in a second workspace the user selects a new store and the first store is unchanged
- [X] T064 [US6] Add failing steps to `desktop/tests/study.py` for editor views (FR-058): a card that is open in the editor for 2 s, until another card is selected, has one `editor_view` row with its card ID, its deck path, and `shown_ms` within 100 ms of 2000; with the focus away from the window for 1 s of that time, `unfocused_ms` is within 100 ms of 1000; the card that is open when a study session starts has a row; a workspace in the `Unattached` state writes no row

### Implementation for User Stories 1 and 6

The invalid-draft edge case is exercised by `desktop/tests/study-draft.py`: Study
reads saved content, Problems opens the retained draft, and a repaired draft saves
before Study resumes. Both session start and the in-session editor return use this path.

- [X] T021 [US1] Implement the add path of `study-sync` in `desktop/study/sync.py`: validate each native deck batch against its saved-source digest; create the Anki deck using the native path encoding in R5; add scheduling notes in one `add_notes` call with GUID and sole field `CardId` equal to the native ID; record source and media digests; write a `card_change` row of kind `added` and a `content` row holding native front and back source, retained `record-assets/` identity, media rows, and retained `record-media/` files; return `SyncResult` with `pending` against the full workspace inventory
- [X] T022 [US6] Implement in `desktop/study/session.py` the pure conversion of R13 from Anki's values (queued card, current and next states, card statistics, card after the answer, review log row) and the window's `Timing` to the `presentation` and `response` values of `specs/001-in-app-review/data-model.md`, with an empty value for each fact that was not observed
- [X] T023 [US1] Implement `study-begin`, `study-next`, `study-answer`, and `study-end` in `desktop/study/session.py` by the R10 call sequence: a `session` row at begin; the top card of the scope's queue with a `presentation` row written before the response; Anki's four labels; the three counts; `Finished` with `next_learning_seconds` from `congratulations_info()`; `StaleCard` when `presentation` is not the session's last presentation or its card is not the top card; `reveal_ms + grade_ms` as Anki's answer time; the `response` row after `answer_card()` returns; a `session_end` row at end and for each open session when the host's input closes
- [X] T024 [US6] Implement recovery at store open in `desktop/study/store.py`: one `response` row with `recovered` set for each review log row that has none, and one `session_end` row with cause `recovered` for each session that has none, by the pure comparison of review log IDs with `response` rows
- [x] T025 [P] [US1] Share the native card face from `desktop/src/editor.tsx` with Study: read-only presentation of authored source, the existing MathJax configuration and diagram renderer, and image resolution through each content version's media mapping
- [X] T026 [P] [US1] Create `desktop/src/study.ts`: the session state (unattached, front, revealed, finished, error); the timing of each card with `performance.now()` for the time to reveal and the time to grade, and with the window's visibility and focus events for the time without focus; native deck batches from saved source, `cards()`, source digests, and existing deck metadata; the sync loop that calls `study-sync` until `pending` is zero and reports progress; and the handling of `StaleCard` by fetching the current card
- [X] T027 [US1] Create `desktop/src/study-screen.tsx` and its styles in `desktop/src/App.css`: native front and back from the content record through the shared card face, four grade buttons with Anki's labels, session counts, the finished state, the store error states, the keys Space, 1 to 4, and Escape, and `study-end` when the user leaves and when the queue is finished
- [X] T028 [US1] Connect the screen in `desktop/src/App.tsx`: call `study-open` and run the sync loop at workspace open without blocking the editor, show sync progress, add **Study** to the workspace menu and the Ctrl-K commands, save pending edits before a session starts, and name the function **Study** everywhere (FR-027)
- [X] T029 [US6] Add to `desktop/src/study-screen.tsx` and `desktop/src/App.tsx` the attach list for the `Unattached` state (each store with its paths, whether its current path exists, last use, and numbers of cards and grades; **Attach** and **Start new**), and the paths of the learning record and the store with a command that opens the folder
- [X] T030 [P] [US6] Write `docs/study-record.md`: the location of the record and how to open it read-only; for each table and each column its meaning, unit, value coding, and the case in which it is empty; the `review` view; the guarantees of `specs/001-in-app-review/contracts/learning-record.md`; the mapping to the columns of the `anki-revlogs-10k` research data set; and the example queries
- [X] T065 [US6] Implement `study-viewed` in `desktop/study/session.py` with its insert function for `editor_view` in `desktop/study/record.py`
- [X] T066 [US6] Measure editor views in `desktop/src/study.ts` (the time a card is open and the time without focus, with `performance.now()` and the window's visibility and focus events) and send `study-viewed` from `desktop/src/App.tsx` when the card leaves the editor: another card is selected, the deck closes, a study session starts, or the window closes

**Checkpoint**: The T016 to T020 and T064 steps pass; the workspace can be studied end to end and each showing of a card is in the record. Use on the real data directory starts after this checkpoint, not before

---

## Phase 4: User Story 2 - Deck changes reach review and keep history (Priority: P1)

**Goal**: A saved or external deck change reaches the store with no user action, and a card keeps its history through edits, moves, renames, merges, removal, and return

**Independent Test**: Give a card an interval, edit its text, move it to another deck, and rename that deck; the card keeps its due date, shows the new text, and belongs to the renamed deck

### Tests for User Story 2 ⚠️

- [x] T031 [US2] Add failing steps to `desktop/tests/study-changes.py`, each on a card that has a review log row and a due date set with `sched.set_due_date()`: an edit of the back in the editor reaches the store within 10 s with the same due date; a move to another deck by a file edit on disk changes the Anki deck and keeps the review log; a deck rename, a deck merge, and a reorder of the cards in a deck keep each due date and review log (SC-004); a card deleted from its deck leaves the counts and is suspended in `Removed`; the same card pasted back has its due date; a new card appears as new; one `card-id` in two decks is named with both paths in the Problems list and its note stays with the first deck; a deck with invalid structure keeps its last synced cards; with a session open, a file edit on disk of the card on screen shows the new text of that card, and the removal on disk of the card on screen shows the next card
- [x] T032 [US2] Add failing steps to `desktop/tests/study-changes.py` for the record of deck changes: each content change, tag change, move, removal, and restore has one `card_change` row of its kind (FR-033); a card that is reviewed, edited, and reviewed again has two `review` rows with the earlier and the later back, and the earlier `content` row is unchanged (FR-030); an image replaced under the same file name leaves the earlier bytes in `record-media/`; `presentation` rows written before a move keep the earlier deck path; a note that has the tag `leech` keeps it when its card's tags change in the deck (FR-045)
- [x] T033 [US2] Add a failing step to `desktop/tests/study-changes.py`: `study-sync` on an unchanged workspace returns zero counts, changes no row of the collection, and writes no record row, and no sync step changes a schedule or a review log row (invariant 3)

### Implementation for User Story 2

- [x] T034 [US2] Implement the sync plan in `desktop/study/sync.py` as one function of native decks and a store snapshot (GUID to deck, content digest, deck and card tags, scheduler tags, suspended): adds, content and tag updates, moves, removals, restores, and duplicates, by the R6 rules for current and not-current decks
- [x] T035 [US2] Apply the plan in `study-sync` in `desktop/study/sync.py`: `update_notes(skip_undo_entry=True)` with the scheduler's tags kept, `set_deck`, suspend then move to `Removed`, move back then unsuspend, removal of an Anki deck under `Workspace` only after its cards have left it, removal of the deck record of a deleted file, one `card_change` row for each applied change, one `content` row with its media for each new front and back pair, and `failed` and `duplicates` in the result
- [x] T036 [US2] Trigger the sync loop in `desktop/src/App.tsx` after each successful save, after each file-watch refresh, and before a session starts; when the card on screen changed or left, show the current card
- [x] T037 [P] [US2] Show each duplicate `card-id` as a problem that names both decks in `desktop/src/problems.ts` and `desktop/src/problem-drawer.tsx`

**Checkpoint**: The T031 to T033 steps pass; editing and studying can alternate

---

## Phase 5: User Story 3 - See what is due and choose what to review (Priority: P2)

**Goal**: The tree shows new, learning, and due counts for each deck and folder, and a session can cover one deck, one folder, or the workspace

**Independent Test**: Grade cards in two decks of one folder; the counts of each deck and of the folder change to match, and a session started on one deck offers only its cards

### Tests for User Story 3 ⚠️

- [x] T038 [US3] Add failing public-path steps in `desktop/tests/study-scopes.py`: workspace, folder, and deck counts preserve the native path hierarchy, including a file and folder with the same stem
- [x] T039 [US3] Add failing steps to `desktop/tests/study-scopes.py`: with cards made due through the `anki` library while the app is stopped, the tree shows the new, learning, and review counts on each deck and folder within 2 s of opening; a grade updates the deck and every folder above it; **Study** on a deck offers only its cards; **Study** on a folder offers the cards of every deck below it; the `session` row of each holds its scope

### Implementation for User Story 3

- [x] T040 [US3] Implement `study-counts` and the `UnknownScope` error in `desktop/study/store.py` and `desktop/study/session.py`, and the pure mapping from `Scope` and `DeckPath` to Anki deck names
- [x] T041 [US3] Show the three counts on each deck and folder of the tree in `desktop/src/App.tsx`, refresh them after each grade and each sync, and add **Study** to the deck and folder context menus with the matching scope

**Checkpoint**: The T038 and T039 cases pass

---

## Phase 6: User Story 4 - Correct a grade or a card during review (Priority: P2)

**Goal**: The user undoes the last grade, and opens the card on screen in the editor and returns

**Independent Test**: Grade a card and undo; the card returns with its earlier schedule, and the record keeps the grade with the time of the undo. Open the card in the editor from the session, change it, return; the session shows the new text

### Tests for User Story 4 ⚠️

- [x] T042 [US4] Add failing steps to `desktop/tests/study-corrections.py`: Ctrl-Z after a grade removes the review log row and returns the card with its earlier state; the record still has the `response` row, has an `undo` row that refers to it, shows `undone_at_ms` in the `review` view, and has a new `presentation` row for the returned card (FR-031); key E opens that card in its deck in the editor; after an edit and a return the same card shows the new text; after that sync Undo is disabled and its tooltip gives the reason, and it is enabled again after the next grade; Undo also works after completion and on successive grades

### Implementation for User Story 4

- [x] T043 [US4] Implement `study-undo` and the `undoable` value in `desktop/study/session.py` from Anki's undo status: undo only when the last undo step is a grade, an `undo` row for the undone `response` row, `StaleCard` otherwise
- [x] T044 [US4] Add Undo (button and Ctrl-Z, with the disabled reason) and Edit (button and key E, with the return to the session) to `desktop/src/study-screen.tsx`, and the editor round trip to `desktop/src/App.tsx`

**Checkpoint**: The T042 steps pass

---

## Phase 7: User Story 5 - Control the daily load (Priority: P3)

**Goal**: The user sets new cards per day, reviews per day, and target recall

**Independent Test**: Set the new-card limit to a small number and confirm that a session offers exactly that many new cards

### Tests for User Story 5 ⚠️

- [X] T045 [US5] Add failing steps to `desktop/tests/study-settings.py`: with new cards per day set to 3, a workspace session offers exactly 3 new cards and the root count shows 3; with reviews per day set to 2 and five cards made due through the `anki` library, a workspace session offers exactly 2 review cards; a higher target recall gives a shorter Good interval for a card in the same state; a target recall of 1.0 shows its bound and leaves the stored value; the settings remain after a restart; each change has a `setting_change` row with the earlier and the later value, and later `presentation` rows hold the later values (FR-034); three due review cards whose estimated recall differs are offered in ascending order of `before_retrievability` (FR-044); replace the `reviewOrder` entry of the Unmeasured section of `specs/001-in-app-review/research.md` with the result

### Implementation for User Story 5

- [X] T046 [US5] Implement `study-set-settings` in `desktop/study/settings.py`: `new_per_day` 0 to 9999, `reviews_per_day` 0 to 9999, `desired_retention` 0.70 to 0.99, `InvalidSettings` outside a bound, the one preset that all decks share, and one `setting_change` row for each value that changed
- [X] T047 [US5] Add the settings form to `desktop/src/study-screen.tsx` with the three fields, their bounds, and the count refresh after a change

**Checkpoint**: The T045 steps pass

---

## Phase 8: User Story 7 - Fit the scheduler to my own history (Priority: P3)

**Goal**: The user fits the scheduler's parameters to their own history with Anki's fitting code, sees Anki's measures of the fit, and accepts or rejects it

**Independent Test**: With a prepared history of sufficient size, run the fit, accept it, and confirm that the preset holds the fitted parameters and that the record holds the earlier and the later parameter sets with their times

### Tests for User Story 7 ⚠️

- [X] T048 [US7] Call `compute_fsrs_params` and `evaluate_params_legacy` of the `anki` wheel on a collection in a temporary directory with dated review log rows written through the `anki` library's database handle, find the smallest history that Anki's fit accepts and the time the fit takes, and replace the two fit entries of the Unmeasured section of `specs/001-in-app-review/research.md` with the results
- [X] T049 [US7] Add failing steps to `desktop/tests/study-fit.py`: the fit on a store with no review states that the history is too small and changes nothing; with the history of T048 added while the app is stopped, the fit shows the fitted parameters, the number of reviews used, and Anki's two measures for the fitted and the current set; closing the fit without accepting changes nothing; accepting sets the preset's parameters, writes a `parameter_set` row with source `fit` and its measures and a `setting_change` row, and later `presentation` rows refer to the new set (FR-046)

### Implementation for User Story 7

- [X] T050 [US7] Implement `study-fit` and `study-apply-fit` in `desktop/study/settings.py` by R14: Anki's fit on the whole store, `evaluate_params_legacy` for both parameter sets, `NotEnoughHistory` for Anki's insufficient-data error and for a fit that used no review, the preset's `fsrsParams6` on apply, and the `parameter_set` and `setting_change` rows
- [X] T051 [US7] Add the fit command to the settings of `desktop/src/study-screen.tsx`: progress while the fit runs, both sets of measures, **Apply** and **Close**, and the `NotEnoughHistory` statement

**Checkpoint**: The T049 steps pass

---

## Phase 9: User Story 8 - See statistics from my record and add new ones safely (Priority: P2)

**Goal**: The user opens **Statistics**, selects an analysis, and sees its result from the learning record. An analysis only reads the record, and a new analysis is one new module that changes no core file and no stored data

**Independent Test**: Study several cards. Open Statistics and run each analysis; the numbers agree with the grades given. Add a new analysis; no part of study or of the record changes, and the earlier analyses give the same results

### Tests for User Story 8 ⚠️

- [X] T067 [US8] Add failing steps to `desktop/tests/study-statistics.py`: **Statistics** in the workspace menu lists the two analyses of `specs/001-in-app-review/contracts/analysis.md` with their titles and summaries, each summary and each column of a measure from grades has the words "self-graded" (FR-059), and the summary of `recall_by_folder` states that its result is about recall of the cards of the folder (FR-060); `recall_by_folder` shows, for each folder and month, the number of presentations, the share graded Again, and the mean time to reveal that the scenario's grades imply, equal to the first query of `contracts/learning-record.md`; `calibration` shows bands whose numbers of grades sum to the number of review grades that were not undone; with a session in progress, an analysis runs and the next grade is recorded; a dump of every record row is equal before and after each analysis runs (SC-019)
- [X] T068 [US8] Create `desktop/tests/analysis.py` and a `desktop-analysis-test` recipe in `justfile` that is part of `test-commit`. The test copies `desktop/backend.py`, `desktop/study/`, and `desktop/analysis/` to a temporary directory, calls the entry script there as the bridge does (one process and one JSON request for each action), and uses a record under a temporary `XDG_DATA_HOME`. Failing steps: `analysis-list` gives the catalog in the order of the titles; after one module is added to the temporary catalog, the list holds it, its result is the table that it returns, and the results of the earlier analyses are equal to those before (SC-018); a module that raises gives `AnalysisFailed` with its text, and the other analyses run; a module that executes an `INSERT` gives `AnalysisFailed` that names a read-only database, and every record row is equal afterward; a module that does not import is in the list with its `failure`; an unknown name gives `UnknownAnalysis`; a path outside the study data directory gives `RecordUnreadable`

### Implementation for User Story 8

- [X] T069 [US8] Implement `desktop/analysis/__init__.py`: the `Analysis`, `Column`, `AnalysisTable`, and `AnalysisError` values of `specs/001-in-app-review/data-model.md` as Pydantic models; the path rule and the read-only connection of `contracts/analysis.md`; the list of the catalog with `pkgutil.iter_modules`, with a `failure` for a module that does not import; and the run of one analysis. Cite the `sqlite3` URI documentation and R17 in the module comment
- [X] T070 [P] [US8] Implement `desktop/analysis/catalog/recall_by_folder.py`: title, summary, and one function from a read-only connection to the table of FR-056 for folders and months; the column label and the summary name the share as self-graded and the result as recall of the cards (FR-059, FR-060)
- [X] T071 [P] [US8] Implement `desktop/analysis/catalog/calibration.py`: title, summary, and one function from a read-only connection to the table of FR-056 for predicted against observed recall, in bands of `before_retrievability`; the column label and the summary name the observed recall as self-graded (FR-059)
- [X] T072 [US8] Add the `analysis-list` and `analysis-run` requests to the entry script `desktop/backend.py` and their Zod schemas to `desktop/src/bridge.ts`; both use the existing route of one process for each request, and neither reaches the study host; the T068 steps pass
- [X] T073 [US8] Create `desktop/src/statistics.tsx` and its styles in `desktop/src/App.css`: the list of analyses, the run of the selected one, one table renderer for every `AnalysisTable` with column names and units, and the failure of an analysis in place of its table; add **Statistics** to the workspace menu and the Ctrl-K commands in `desktop/src/App.tsx`; the T067 steps pass
- [X] T074 [P] [US8] Write `docs/analyses.md`: what an analysis is; the rules of `specs/001-in-app-review/contracts/analysis.md`; how to add one (one module and its test, and no other file); where the field reference of the record is (`docs/study-record.md`); and what to do when the record does not hold a needed fact (a core change that adds a table or a nullable column, never an analysis that writes)

**Checkpoint**: The T067 and T068 steps pass; `just desktop-boundaries` passes

---

## Phase 10: Keeping the data (FR-049, FR-050)

**Goal**: The user writes a complete copy of a store to a directory of their choice from inside the running app, and a copy attaches on any machine

**Independent Test**: Save a copy during a session. Start the app on an empty data directory, place the copy there, and attach it; the counts and every record row are those of the store at the time of the copy

### Tests for the copy ⚠️

- [X] T075 Add failing steps to `desktop/tests/study-copy.py`: with a session in progress, **Save a copy** in the Study settings, with a temporary directory, writes `math-flashcards-study-<time>/<store ID>/` with `store.json`, `collection.anki2`, `record.sqlite3`, `record-media/`, and `record-assets/`; `sqlite3` opens the copy's record and finds every row that was committed before the copy, and every retained media and rendering asset matches its recorded digest; the store's record has a `store_event` row of kind `copied` with that path; the next grade succeeds, and Undo is unavailable until it; a directory that does not exist gives `CopyFailed` with the cause, and the store is unchanged; after the app is stopped and started with an empty `XDG_DATA_HOME` in which the copy is placed under `math-flashcards/study/`, the window lists the copy, and after the user attaches it the counts and every record row equal those of the copy (SC-017)

### Implementation for the copy

- [X] T076 Implement `study-copy` in `desktop/study/store.py` by R18: close the collection and the record, copy the store directory with `shutil.copytree`, open both again, write the `store_event` row, and return `CopyFailed` with the store open and unchanged when the copy cannot be written
- [X] T077 Add **Save a copy** to the Study settings in `desktop/src/study-screen.tsx`, with the folder picker of the dialog plugin, progress while the copy runs, and the path of the finished copy

**Checkpoint**: The T075 steps pass

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Backups, permanence across the whole scenario, file placement, the native path, installation, documentation, and measurements

- [X] T078 Add a step to `desktop/tests/native.py`: the built app runs the study step with an empty directory as `HOME` and with `XDG_DATA_HOME`, `XDG_CONFIG_HOME`, `XDG_STATE_HOME`, and `XDG_CACHE_HOME` set to four directories inside it; afterward every file under that `HOME` is under one of the four directories; after the cache and state directories are removed and the app starts again, every record row is equal and the counts are as before (FR-048, SC-016). Add the same assertion for the bridge processes at the end of `desktop/tests/study.py`
- [X] T082 Create the main window in `desktop/src-tauri/src/lib.rs` with its webview data directory at `webview/` under the XDG cache directory, and set `"create": false` for the window in `desktop/src-tauri/tauri.conf.json`; `desktop/tests/native-study.py` finds no web cache file under the data directory (FR-048, R16 of `research.md`)
- [X] T052 Add failing steps to `desktop/tests/study-preservation.py`, then make them pass in `desktop/study/store.py`: the host writes an Anki backup to the store's `backups/` folder at open and at exit when Anki's backup interval allows, with a copy of the record made by `sqlite3.Connection.backup` under the same time, which `sqlite3` opens with the same rows in each table (FR-040); a record copy stays while the `.colpkg` of the same time stays and follows Anki's retention; **Rebuild cached data** leaves the store, its review log, and the record unchanged; a review card whose lapse count is one below Anki's leech threshold, graded Again, stays unsuspended, returns in the session, and has the tag `leech` (FR-024, FR-045); Anki's database check (`fix_integrity()`) reports no problem at the end of the scenario
- [X] T053 Extend `desktop/tests/study-changes.py`: every record row captured at the initial open and subsequent action boundaries is equal at the end, and no row is missing, across undo, edits, moves, removals, **Rebuild cached data**, and attachment after changing the workspace path (SC-010)
- [X] T054 Save the record that the scenario produces as `desktop/tests/fixtures/study/record-v1.sqlite3` with a dump of its rows beside it, and add a step to `desktop/tests/study.py`: the host opens a store that holds this record, every row equals the dump, and the `review` view reads it (FR-039, SC-013); add a step to `desktop/tests/analysis.py`: each analysis of the catalog runs on this record and returns a table; document in `docs/study-record.md` that this fixture is never regenerated
- [x] T055 [P] Exercise Study in `desktop/tests/native-study.py`: in the built window, start a session, grade cards, and confirm the review log rows and the `review` rows in the isolated store, with an image card visible through the asset protocol
- [x] T056 [P] Make `desktop/linux/install.py` copy `desktop/study/` and `desktop/analysis/` into the release beside the entry script, and make the release validation import `anki`, `study`, and `analysis` in the release environment and fail the candidate release when an import fails; extend `desktop/tests/installation.py` for it, and assert there that a store under the data directory, with its record, is unchanged by the installation of a new release (FR-017)
- [X] T057 [P] Document Study and Statistics in `desktop/README.md` (use, keys, settings, the fit, store and record location, saving a copy, attaching a store after a move or on a new machine, backups, the one running copy, where each kind of file is placed, test recipes) and record the `anki`, `tauri-plugin-single-instance`, and Import Linter dependencies and the three parts in `docs/desktop-dependency-survey.md`
- [ ] T058 Run the manual table of `specs/001-in-app-review/quickstart.md` on the repository's `decks/` folder with a temporary `XDG_DATA_HOME`; replace the entries of the Unmeasured section of `specs/001-in-app-review/research.md` for the first-sync time, the save-to-review time, the copy time, and the record size with the measured values, and add the measured count time and the time to the next card for 20 grades (SC-002, SC-006); the entry on a retained earlier release stays until an `anki` release changes the collection format; open an issue for each criterion that fails
- [ ] T059 Run the tier 1 loop that T081 names, through `just test-commit`, and confirm that it stays under five minutes with its setup (constitution V)

---

## Requirement coverage

The task texts above do not name these requirements. This table gives the tasks that
implement and test each one.

| Requirement | Tasks |
| --- | --- |
| FR-001 | T028, T041 (test T039) |
| FR-002 | T027 (test T016) |
| FR-003 | T023, T027 (test T016) |
| FR-004 | T023 (tests T016, T018) |
| FR-005 | T011, T023 |
| FR-006 | T023, T027 (test T016), T093 |
| FR-008 | T023, T027 (test T016) |
| FR-009 | T025 (test T017) |
| FR-010 | T021 (test T016) |
| FR-011 | T036 (test T031) |
| FR-012 | T021, T089 |
| FR-013 | T021 (tests T016, T017) |
| FR-014 | T034, T035 (test T031) |
| FR-015 | T034, T037 (test T031) |
| FR-016 | T035 (test T031) |
| FR-018 | T011, T052 |
| FR-020 | T041 (test T039) |
| FR-021 | T043, T044 (test T042) |
| FR-022 | T044 (test T042) |
| FR-023 | T045, T046, T047, T092 |
| FR-026 | T021 (test T016) |
| FR-029 | T023 (test T018) |
| FR-032 | T023, T024 (test T018) |
| FR-035 | T012 (test T018) |
| FR-043 | T090 |
| FR-051 | T008, T018, T032, T042, T046, T050, T064, T065, T066, T075 |
| FR-052 | T012, T060, T061 |
| FR-053 | T068, T069, T074, T091 |
| FR-054 | T068, T073, T074 |
| FR-055 | T067, T072, T073 |
| FR-057 | T060, T061, T083 |
| SC-003 | T036 (test T031) |
| SC-005 | T024 (test T017) |

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T060 comes before T061, and T061 comes before every task that names a file in `desktop/study/` or `desktop/analysis/`. T079 supplies research for the learning decisions that consume it. Read the full sources for each such decision before implementing that decision; unrelated unread sources do not block native card synchronization, rendering, or recording. Keep unsupported choices explicitly labelled as defaults in R19. A changed learning-decision status is reported before implementing the affected behaviour.
- **Foundational (Phase 2)**: T062 and T063 precede store operations: the store's design depends on one running copy. The typed values, store, record, and host route supply the inputs for story implementation. T081 adds logging with each operation; tier classification and performance work follow the required functionality.
- **US1 and US6 (Phase 3)**: Depends on the native values, store, record, and host route in Foundational. Implement the native sync path, shared card presentation, and window entry point together with the scheduler and record operations they use.
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
Then T027 (study-screen.tsx), T028 (App.tsx), T029 (attach list and record location), T065 and T066 (editor views).
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

## Phase 12: Convergence

- [ ] T083 Run the `desktop-boundaries` check at each commit of this repository, not only in `just test-commit`, and add a check that no file under `desktop/src/` writes learning data except through the bridge requests per FR-057 (partial)
- [X] T084 After an answer that makes Anki add the `leech` tag, write a `card_change` row of kind `tags` whose `tags` include `leech` in `desktop/study/session.py`, keep `leech` in the `tags` of each later `card_change` and `presentation` row of the card in `desktop/study/sync.py`, add the failing step to `desktop/tests/study-preservation.py` first, and describe the value in `docs/study-record.md` per FR-045, `data-model.md` (partial)
- [X] T085 Add steps to `desktop/tests/study.py`: a card graded Again is shown again in the same session after its learning delay, and the next card is readable within 0.5 s of a grade per T016, SC-002 (missing)
- [X] T086 Add steps to `desktop/tests/study.py`: the `review` row of a grade has the expected time zone offset, deck path, folder, deck title, tags, session, position, kind, scheduler day, target recall, parameter set, daily limits, and writer; Escape with a card on screen leaves its `presentation` row with no `response` row per T018, FR-028 (partial)
- [X] T087 Add steps to `desktop/tests/study.py` and, for the queries, `desktop/tests/study-timing.py`: every table and column of the record's schema is named in `docs/study-record.md`; the Study screen shows the path of the record and it is the file that the scenario reads; the calibration query and a query by deck of `contracts/learning-record.md` give the numbers that the grades imply per T019, FR-038, FR-042, SC-011 (missing)
- [X] T088 Add the file placement assertion of `desktop/tests/native-study.py` to the end of `desktop/tests/study.py` for the bridge processes per T078, SC-016 (missing)
- [X] T089 Add a scenario: a new store that is synchronized from the same decks has the same notes, deck placement, and content records as the first store per FR-012 (missing)
- [X] T090 Add a step to the offline native scenario: with Study open and a card graded, no process of the app opens a network connection per FR-043 (missing)
- [X] T091 Add a step to `desktop/tests/analysis.py`: a run of each analysis leaves the data, state, and cache directories with no new file other than logs, and a write to the record from an analysis fails per FR-053 (partial)
- [X] T092 Add a step to `desktop/tests/study-settings.py`: a session of one deck obeys the daily limits per FR-023 (partial)
- [X] T093 Make the finished screen show Anki's own statement of the cards studied today, from `Collection.studied_today()`, in place of the count that `desktop/study/session.py` computes with its own query; add the failing step to `desktop/tests/study.py` first per FR-006, Clarifications 2026-11-20 (partial)
- [ ] T094 Find the cause of the intermittent failure of `just desktop-test study-timing` (the Study screen did not open; 1 failure in 6 runs at revision 720f869, evidence in `test-history/20261120T075735.992939Z-study-timing/`) and correct it with a failing test first per T018, SC-014 (partial)
- [X] T095 Compile each diagram of the saved decks before a card shows it: create one script job, runnable from a `just` recipe with the app closed, that finds the diagrams of a workspace with no current SVG in the cache and compiles them through the shared TikZ filter; make the app start that job at its start, on the user's request, and after the edit of a card ends (debounced), with no compile logic of its own; Study and the editor then show the cached SVG. Add the failing step to `desktop/tests/study.py` first: after the start pass ends, the diagram card is readable within 0.5 s, and the 120 s wait for the diagram is gone per SC-002, Clarifications 2026-11-20 (contradicts)
- [X] T096 Write the design in `research.md`, with alternatives and a recommendation for the user, for one owner of diagram files: the figures tree and TikZ filter of the Pandoc configuration hold and compile the diagrams, and a card refers to its diagram; state the effect on constitution I (Markdown decks are the only authored source) per Clarifications 2026-11-20 (missing)
