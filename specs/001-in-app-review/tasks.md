---

description: "Task list for in-app review"
---

# Tasks: In-App Review

**Input**: Design documents from `/specs/001-in-app-review/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/study-bridge.md, quickstart.md

**Tests**: Included. Constitution principle V requires proof through the real application
path, and each story's test is committed before its implementation and must fail for the
stated reason first.

**Organization**: Tasks are grouped by user story. Each story is a complete increment
that `desktop/tests/study.py` proves on its own.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependency on an incomplete task)
- **[Story]**: The user story the task belongs to (US1 to US5)
- Paths are relative to the repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Dependencies, test isolation, and fixtures

- [ ] T001 Add `anki` with no version pin to the PEP 723 dependency block of `desktop/backend.py`, and confirm that `just desktop-dependencies` prepares an environment in which `import anki` and `import ankdown` both succeed
- [ ] T002 In the `ankdown-for-math` repository, add an `id` field to the card model in `ankdown/cli.py` and emit it from `ankdown/ankdown.lua` for each card that supplies one; the package build ignores `id` and package GUIDs stay `simple_hash(front + back)`; prove it with a test in that repository and commit there
- [ ] T003 In `justfile`, make the `desktop-test` recipe set `XDG_DATA_HOME` to a temporary directory beside its `XDG_CACHE_HOME` override, add a `desktop-study-test` recipe that runs `desktop/tests/study.py` against `just desktop-web` with temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME`, and add `desktop-study-test` to `test-commit`
- [ ] T004 [P] Add study fixture decks in `desktop/tests/fixtures/study/`: two decks in one folder and one deck at the top level, with a macro equation, a TikZ-cd diagram, an image, tags, and at least twelve cards in total

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: The card ID in the render output, the typed study values, the store, and the host route

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Add a failing case to `desktop/tests/paired-cards.test.ts`: the rendered deck of a paired-card source has, for each card, an `id` equal to its `card-id`, in front order
- [ ] T006 Pass each `card-id` from `desktop/paired-cards.lua` to the exporter filter and make `id` a required, non-empty field of `Card` in `desktop/backend.py` (contract: Render output); T005 passes and `just desktop-test` still produces the same packages
- [ ] T007 Create `desktop/tests/study.py` with the scenario harness (temporary workspace copied from `desktop/tests/fixtures/study/`, temporary data and cache directories, store inspection with the `anki` library) and failing steps for `study-open`: a new workspace gets a store under the temporary data directory with `workspace.txt`, FSRS on, `applyAllParentLimits` on, and leech action tag only; a second workspace path gets a second store; a second host on the same store gets `StoreInUse`; an unreadable `collection.anki2` gives `StoreUnreadable` with the path and stays unchanged
- [ ] T008 [P] Declare the study values and the seven study requests of `specs/001-in-app-review/data-model.md` and `contracts/study-bridge.md` as Pydantic models in `desktop/backend.py`, with `extra="forbid"`, `limit` 1 to 8, `elapsed_ms` 0 or more, `new_per_day` 0 to 9999, `reviews_per_day` 0 to 9999, and `desired_retention` 0.70 to 0.99
- [ ] T009 [P] Declare the same values and requests as Zod schemas and inferred types in `desktop/src/bridge.ts`, with a typed `StudyError`; `bunx tsc --noEmit` passes with no `any` or `unknown`
- [ ] T010 Implement the store in `desktop/backend.py`: directory `user_data_path("math-flashcards")/study/<digest of the workspace path>`, creation only when the directory is absent, `workspace.txt` check, exclusive lock, the R9 settings before the first queue build, and the `StoreInUse` and `StoreUnreadable` errors
- [ ] T011 Implement the `study-host` command in `desktop/backend.py`: one JSON request per input line, one `{"ok": …}` response per output line, store held until input closes, and the `study-open` action with the count tree from `deck_due_tree()`
- [ ] T012 Add the study route to `desktop/src-tauri/src/lib.rs`: every `study-*` action goes to one host process that starts on first use, serves one request at a time, restarts after an early exit, and stops at app exit; add the store's media folder to the asset scope from the `study-open` result and enable the asset protocol in `desktop/src-tauri/tauri.conf.json`
- [ ] T013 [P] Add the same study route and a media route to the middleware in `desktop/vite.config.ts`; the T007 steps pass through the browser window

**Checkpoint**: `just desktop-study-test` opens a real store through the real window

---

## Phase 3: User Story 1 - Review due cards in the app (Priority: P1) 🎯 MVP

**Goal**: The user starts a study session of the workspace, sees a front, reveals the back, grades, and continues until study for today is complete

**Independent Test**: On a workspace that was never studied, grade several cards, restart the app, and confirm that the graded cards keep their schedule and the others are still offered

### Tests for User Story 1 ⚠️

- [ ] T014 [US1] Add failing steps to `desktop/tests/study.py`: every fixture card is a new note whose GUID is its `card-id` after the window opens the workspace; the first card is reached from the open workspace in at most two actions (SC-001); **Study** shows a front with the back and grades hidden; Space reveals the back and four labelled grades; key 3 records one review log row and the stored interval agrees with the Good label; the next card shows within 0.5 s; counts decrease; a card graded Again returns after its learning delay; after the last card the screen states that study is complete and gives the number graded; a restart keeps every grade
- [ ] T015 [US1] Add failing steps to `desktop/tests/study.py`: after a grade, `SIGKILL` of the host loses no review log row and the next request starts a new host; a card with a macro equation, a TikZ-cd diagram, and an image renders all three, with a screenshot in `desktop/test-artifacts/`; the `Front` and `Back` of each studied note equal the fields of the same card in the package that the app generates for its deck (SC-007); an equation with an undefined macro shows the TeX error

### Implementation for User Story 1

- [ ] T016 [US1] Implement the add path of `study-sync` in `desktop/backend.py`: for at most `limit` decks that are not current, render with `render()`, create the Anki deck `Workspace::<folders>::<file stem>`, add the notes in one `add_notes` call with GUID `card-id` and the rendered `Front` and `Back`, copy media through `col.media`, write the deck record of `input_hashes()` to the collection config, and return `SyncResult` with `pending`
- [ ] T017 [US1] Implement `study-next` and `study-answer` in `desktop/backend.py` by the R10 call sequence: the top card of the scope's queue, Anki's four labels, the three counts, `Finished` with `next_learning_seconds` from `congratulations_info()`, `StaleCard` when `card_id` is not the top card, and `elapsed_ms` as the answer time
- [ ] T018 [P] [US1] Add element typesetting for rendered card HTML to `desktop/src/math.ts`, using the loaded MathJax and `texOptions(macros)` of the active asset set
- [ ] T019 [P] [US1] Create `desktop/src/study.ts`: the session state (front, revealed, finished, error), the answer timer, the sync loop that calls `study-sync` until `pending` is zero and reports progress, and the handling of `StaleCard` by fetching the current card
- [ ] T020 [US1] Create `desktop/src/study.tsx` and its styles in `desktop/src/App.css`: card front and back from the note HTML, image sources resolved against `media`, four grade buttons with Anki's labels, session counts, the finished state, the store error states, and the keys Space, 1 to 4, and Escape
- [ ] T021 [US1] Connect the screen in `desktop/src/App.tsx`: call `study-open` and run the sync loop at workspace open without blocking the editor, show sync progress, add **Study** to the workspace menu and the Ctrl-K commands, save pending edits before a session starts, and name the function **Study** everywhere (FR-027)

**Checkpoint**: The T014 and T015 steps pass; the workspace can be studied end to end

---

## Phase 4: User Story 2 - Deck changes reach review and keep history (Priority: P1)

**Goal**: A saved or external deck change reaches the store with no user action, and a card keeps its history through edits, moves, renames, merges, removal, and return

**Independent Test**: Give a card an interval, edit its text, move it to another deck, and rename that deck; the card keeps its due date, shows the new text, and belongs to the renamed deck

### Tests for User Story 2 ⚠️

- [ ] T022 [US2] Add failing steps to `desktop/tests/study.py`, each on a card that has a review log row and a due date set with `sched.set_due_date()`: an edit of the back in the editor reaches the store within 10 s with the same due date; a move to another deck by a file edit on disk changes the Anki deck and keeps the review log; a deck rename, a deck merge, and a reorder of the cards in a deck keep each due date and review log (SC-004); a card deleted from its deck leaves the counts and is suspended in `Removed`; the same card pasted back has its due date; a new card appears as new; one `card-id` in two decks is named with both paths in the Problems list and its note stays with the first deck; a deck with invalid structure keeps its last synced cards
- [ ] T023 [US2] Add a failing step to `desktop/tests/study.py`: `study-sync` on an unchanged workspace returns zero counts and changes no row, and no sync step changes a schedule or a review log row (invariant 3)

### Implementation for User Story 2

- [ ] T024 [US2] Implement the sync plan in `desktop/backend.py` as one function of the rendered decks and a store snapshot (GUID to deck, sides, tags, suspended): adds, field and tag updates, moves, removals, restores, and duplicates, by the R6 rules for current and not-current decks
- [ ] T025 [US2] Apply the plan in `study-sync` in `desktop/backend.py`: `update_notes(skip_undo_entry=True)`, `set_deck`, suspend then move to `Removed`, move back then unsuspend, removal of an Anki deck under `Workspace` only after its cards have left it, removal of the deck record of a deleted file, and `failed` and `duplicates` in the result
- [ ] T026 [US2] Trigger the sync loop in `desktop/src/App.tsx` after each successful save, after each file-watch refresh, and before a session starts; when the card on screen changed or left, show the current card
- [ ] T027 [P] [US2] Show each duplicate `card-id` as a problem that names both decks in `desktop/src/problems.ts` and `desktop/src/problem-drawer.tsx`

**Checkpoint**: The T022 and T023 steps pass; editing and studying can alternate

---

## Phase 5: User Story 3 - See what is due and choose what to review (Priority: P2)

**Goal**: The tree shows new, learning, and due counts for each deck and folder, and a session can cover one deck, one folder, or the workspace

**Independent Test**: Grade cards in two decks of one folder; the counts of each deck and of the folder change to match, and a session started on one deck offers only its cards

### Tests for User Story 3 ⚠️

- [ ] T028 [P] [US3] Add failing units in `desktop/tests/study.test.ts`: a workspace, folder, or deck scope maps to its entry of the count tree, and a deck path with nested folders maps to nested entries
- [ ] T029 [US3] Add failing steps to `desktop/tests/study.py`: with cards made due through the `anki` library while the app is stopped, the tree shows the new, learning, and review counts on each deck and folder within 2 s of opening; a grade updates the deck and every folder above it; **Study** on a deck offers only its cards; **Study** on a folder offers the cards of every deck below it

### Implementation for User Story 3

- [ ] T030 [US3] Implement `study-counts` and the `UnknownScope` error in `desktop/backend.py`, and the pure mapping from `Scope` and `DeckPath` to Anki deck names
- [ ] T031 [US3] Show the three counts on each deck and folder of the tree in `desktop/src/App.tsx`, refresh them after each grade and each sync, and add **Study** to the deck and folder context menus with the matching scope, using the mapping in `desktop/src/study.ts`

**Checkpoint**: The T028 and T029 cases pass

---

## Phase 6: User Story 4 - Correct a grade or a card during review (Priority: P2)

**Goal**: The user undoes the last grade, and opens the card on screen in the editor and returns

**Independent Test**: Grade a card and undo; the card returns with its earlier schedule. Open the card in the editor from the session, change it, return; the session shows the new text

### Tests for User Story 4 ⚠️

- [ ] T032 [US4] Add failing steps to `desktop/tests/study.py`: Ctrl-Z after a grade removes the review log row and returns the card with its earlier state; key E opens that card in its deck in the editor; after an edit and a return the same card shows the new text; after that sync Undo is disabled and its tooltip gives the reason, and it is enabled again after the next grade

### Implementation for User Story 4

- [ ] T033 [US4] Implement `study-undo` and the `undoable` value in `desktop/backend.py` from Anki's undo status: undo only when the last undo step is a grade, `StaleCard` otherwise
- [ ] T034 [US4] Add Undo (button and Ctrl-Z, with the disabled reason) and Edit (button and key E, with the return to the session) to `desktop/src/study.tsx`, and the editor round trip to `desktop/src/App.tsx`

**Checkpoint**: The T032 steps pass

---

## Phase 7: User Story 5 - Control the daily load (Priority: P3)

**Goal**: The user sets new cards per day, reviews per day, and target recall

**Independent Test**: Set the new-card limit to a small number and confirm that a session offers exactly that many new cards

### Tests for User Story 5 ⚠️

- [ ] T035 [US5] Add failing steps to `desktop/tests/study.py`: with new cards per day set to 3, a workspace session offers exactly 3 new cards and the root count shows 3; with reviews per day set to 2 and five cards made due through the `anki` library, a workspace session offers exactly 2 review cards; a higher target recall gives a shorter Good interval for a card in the same state; a target recall of 1.0 shows its bound and leaves the stored value; the settings remain after a restart

### Implementation for User Story 5

- [ ] T036 [US5] Implement `study-set-settings` in `desktop/backend.py`: `new_per_day` 0 to 9999, `reviews_per_day` 0 to 9999, `desired_retention` 0.70 to 0.99, `InvalidSettings` outside a bound, and the one preset that all decks share
- [ ] T037 [US5] Add the settings form to `desktop/src/study.tsx` with the three fields, their bounds, and the count refresh after a change

**Checkpoint**: The T035 steps pass

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Backups, the native path, installation, documentation, and measurements

- [ ] T038 Add failing steps to `desktop/tests/study.py`, then make them pass in `desktop/backend.py`: the host writes an Anki backup to the store's `backups/` folder at open and at exit when Anki's backup interval allows; **Rebuild cached data** leaves the store and its review log unchanged; a review card whose lapse count is one below Anki's leech threshold, graded Again, stays unsuspended and returns in the session (FR-024); Anki's database check (`fix_integrity()`) reports no problem at the end of the scenario; a package generated for a studied deck has the same content and status as before
- [ ] T039 [P] Add one study step to `desktop/tests/native.py`: in the built window, start a session, grade a card, and confirm the review log row in the isolated store, with an image card visible through the asset protocol
- [ ] T040 [P] Make the release validation in `desktop/linux/install.py` import `anki` in the release environment and fail the candidate release when the import fails; extend `desktop/tests/installation.py` for it, and assert there that a store under the data directory is unchanged by the installation of a new release (FR-017)
- [ ] T041 [P] Document Study in `desktop/README.md` (use, keys, settings, store location, backups, the one-window rule, test recipe) and record the `anki` dependency and the study boundary in `docs/desktop-dependency-survey.md`
- [ ] T042 Run the manual table of `specs/001-in-app-review/quickstart.md` on the repository's `decks/` folder with a temporary `XDG_DATA_HOME`; replace the Unmeasured section of `specs/001-in-app-review/research.md` with the measured first-sync time, save-to-review time, and count time; open an issue for each criterion that fails
- [ ] T043 Run `just test-commit` and confirm that the whole suite stays under five minutes

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies. T002 is in another repository and must be pushed before T006.
- **Foundational (Phase 2)**: Depends on Setup. Blocks every story.
- **US1 (Phase 3)**: Depends on Foundational.
- **US2 to US5 (Phases 4 to 7)**: Each depends on US1. None depends on another.
- **Polish (Phase 8)**: Depends on the stories that are in the release. T039 needs US1; T042 needs US1 to US3.

### Within Each Phase

- A test task is committed and fails for its stated reason before the implementation tasks of its phase start.
- Bridge values before bridge actions; bridge actions before window code that calls them.
- `desktop/tests/study.py`, `desktop/backend.py`, and `desktop/src/App.tsx` are each changed by many tasks; tasks on the same file run in order.

### Parallel Opportunities

- T004 beside T001 to T003.
- T008 and T009; T013 beside T012.
- T018 and T019 beside T016 and T017.
- T027 beside T024 to T026; T028 beside T029.
- T039, T040, and T041.
- After US1, the phases US2 to US5 can proceed in parallel when their `desktop/backend.py` and `desktop/src/App.tsx` changes are merged in order.

## Parallel Example: User Story 1

```text
After T014 and T015 are committed and failing:
  Task: "T016 add path of study-sync in desktop/backend.py"   then T017 (same file)
  Task: "T018 element typesetting in desktop/src/math.ts"
  Task: "T019 session state and sync loop in desktop/src/study.ts"
Then T020 (study.tsx) and T021 (App.tsx).
```

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3.
3. Validate with `just desktop-study-test`.

After US1 alone, a saved edit reaches the store only as a new card ID; edits to existing
cards need US2. Daily use with continued editing therefore needs US1 and US2.

### Incremental Delivery

1. Setup and Foundational: a real store opens through the real window.
2. US1: the workspace can be studied.
3. US2: editing and studying can alternate.
4. US3: counts and deck or folder sessions.
5. US4: Undo and Edit.
6. US5: load settings.
7. Polish: backups, native proof, installation, documentation, measurements.

## Notes

- Every test run uses temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME`. The real review history is never a test target.
- The store is user data. No task deletes a store, and no task adds a migration or an import of earlier history.
- Commit after each task. A failing test commit that a hook rejects uses the repository's sanctioned route for red commits.
