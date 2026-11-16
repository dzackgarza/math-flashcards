# Implementation Plan: In-App Review

**Branch**: `master` (no feature branch; feature directory `specs/001-in-app-review`) | **Date**: 2026-11-16 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-in-app-review/spec.md`

**Plan card**: `PLAN-in-app-review` under `FEATURE-in-app-review` in the agent-memory vault. The card points to this directory, which owns the plan.

## Summary

The desktop app gains a **Study** function: spaced-repetition review of the cards in the
saved Markdown decks, scheduled by Anki's own code, with a complete and permanent record
of the user's learning. The purpose is a personal learning system for one person over a
career (constitution, Purpose); Anki is adapted and reused for it, not copied.

The bridge adds the PyPI `anki` wheel and one long-lived host process that holds an Anki
collection for the workspace. A state-based sync keeps one scheduling note for each
native `card-id`, so edits, moves, and renames keep review history. The app's existing
card parser supplies native front and back source. The shared editor renderer displays
it. A new React screen shows four grades with Anki's interval labels, counts, and Undo.

Beside the collection, the host writes the learning record: an append-only SQLite
database that the app owns. It holds each showing of a card with its content, subject,
measured times, grade, and scheduler state, and each session, card change, undo, and
settings change. The user reads it with standard data tools while the app runs. A store
belongs to a workspace and attaches to a new path on the user's choice. The user fits
the scheduler's parameters to this history with Anki's own fitting code.

The app has three parts (constitution, principle IX). The core is the Python package
`desktop/study/`: the host, the store, and the only writer of the record. The analyses
are the Python package `desktop/analysis/`: each is one module that receives a read-only
connection to the record and returns a table, and the **Statistics** screen lists and
shows them. The interface is the window. A new analysis is one new module; it changes no
core file and no stored data. Import contracts in the commit gate check the boundaries.

The app runs as one copy, enforced by the Tauri single-instance plugin, so one host is
the only writer of the store. Every file is placed by the XDG Base Directory
Specification. The user saves a complete copy of a store to a chosen directory from
inside the app.

## Technical Context

**Language/Version**: Python ≥ 3.12 (bridge; the prepared runtime is 3.14), TypeScript with React (window), Rust (Tauri 2 shell), Lua (Pandoc filters)

**Primary Dependencies**: `anki` (PyPI wheel, new), Python's `sqlite3` (standard library, for the learning record and for the read-only connection of the analyses), `tauri-plugin-single-instance` (new), Import Linter (new, commit gate only, through `uvx`), Pydantic, filelock, platformdirs, `@dzack/pandoc-editor`, the existing Lezer Pandoc parser, MathJax 4, Mantine, Zod, Tauri 2

**Storage**: One store for each workspace under `user_data_path("math-flashcards")/study/<store ID>/`: an Anki collection (SQLite) with its media folder, the learning record `record.sqlite3` (SQLite, schema owned by the app, rows only inserted) with `record-media/` and `record-assets/`, `store.json`, and `backups/` with Anki `.colpkg` files and record copies

**Testing**: Tier 1 covers real user stories and meaningful branches through Playwright and the prepared bridge, plus type and boundary checks. Tier 2 covers the built Linux app under Xvfb and broader combinations at milestones. Tests follow `test-guidelines`; internal assertions do not replace real-path evidence.

**Target Platform**: Linux desktop (Tauri/WebKitGTK), one user, one machine, one running copy

**Project Type**: Desktop app

**Performance Goals**: Next card readable within 0.5 s of a grade (SC-002); changed cards in review within 10 s of a save (SC-003); tree counts within 2 s of opening a prepared workspace (SC-006)

**Constraints**: No network at run time; the learning record never leaves the machine; no row of the record is updated or deleted; the record's schema only grows; installed releases are immutable; no version pins or lock files; the complete tier 1 loop under five minutes; Anki is AGPL-3.0-or-later; an analysis has a read-only connection and imports no core code; every file outside the workspace is under its XDG base directory

**Scale/Scope**: About 3,300 cards in 68 decks; a record that grows for decades (an estimate of 1 kB for each presentation, not measured); a catalog of analyses that grows for decades; two new screens (Study, Statistics); fourteen study actions and two analysis actions; one new process type

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Result |
| --- | --- | --- |
| Purpose | The feature is built for one person's learning over a career. It records more than Anki records, changes Anki's review order and answer-time limit for that purpose (R9), and omits Anki's sync, editor, add-ons, and sharing. | Pass |
| I. Markdown decks are the only authored source | `study-sync` derives scheduling identities from native card IDs in the decks. Review history and the learning record are user data: they live in the user data directory (R4), have backups, and are outside **Rebuild cached data**. The record keeps the content of each card as shown; it is a history of what the user saw, not an authored source of cards. | Pass |
| II. Native cards, shared rendering, direct Anki integration | Study uses the native card source returned by `cards()` and the shared editor renderer, with the app's MathJax, active macros, diagrams, and recorded media. The core calls Anki's library directly for scheduling; its notes contain the stable card ID as their sole field. | Pass |
| III. Dependencies before hand-written code | Scheduling, queues, undo, counts, backups, the database check, and parameter fitting are Anki calls. The sync plan compares native card IDs and source versions with the store. SQLite owns record storage, concurrent reads, and backup; the reference for permanence is the xAPI statement model, and the reference for scheduling fields is Anki's review log and the public research data set (R12). The editor's existing parser and renderer own card content. `anki` has no version pin. | Pass, with the record schema for the user's approval |
| IV. Fail loudly | Unreadable store, failed copy, failed analysis, unknown store, stale card, invalid settings, too little history, and render failures each reach the window with their cause. No empty store replaces an unreadable one or an unattached one. No import path for earlier history. The record has no migration: its schema only grows, as principle VI requires. | Pass |
| V. Proof through the real application path | `desktop/tests/study.py` drives the real window and bridge, reads the real store, and reads the real record with `sqlite3` alone. The native scenario proves the host route. Each story's test is committed before its implementation. | Pass |
| VI. The learning record is complete, permanent, and open to analysis | Complete: each presentation, response, undo, session, card change, and settings change is a row (FR-028 to FR-035); rows that Anki has and the record lacks are recovered at open (FR-036). Permanent: the host has no update or delete statement; a store attaches to a new path (FR-041); backups include the record. Independent: a second database in a documented format, readable without the app and without Anki. Additive: a `schema` table and a committed first-version fixture that every later release must read. Open: SQLite, a `review` view, `docs/study-record.md`, and the mapping to the research data set. Private: no study action calls Anki's sync or opens a connection; this is established by inspection, not by a test. Scheduling: ascending retrievability and tag-only leeches (R9). | Pass |
| VI, easy to keep and covers every act of learning | The store directory is the whole of a workspace's learning data. `study-copy` writes a complete copy to a chosen directory, and a copy attaches on any machine (R18). The specification's table names, for each action that bears on learning, the git history or the record row that holds it; a card open in the editor is a new `editor_view` row (FR-058). | Pass |
| VII. One person, one running copy | The single-instance plugin gives the focus to the running window (R15). One host is the only writer of the store for the life of the running copy, and an update takes effect at the next launch. | Pass |
| VIII. XDG Base Directory placement | R16 gives the directory of each file. The feature writes learning data under the data directory and writes no result of an analysis to a file; a result that a later analysis stores is a cache file (R16). One existing defect is outside the feature's own files: the web view writes its cache under the data directory. Tauri's web view library owns that placement and gives no setting for it (R16). | Pass for the feature's files; one existing defect, owned upstream |
| IX. Three parts with a small blast radius | Core in `desktop/study/`, analyses in `desktop/analysis/`, interface in `desktop/src/` (R17). An analysis has a read-only connection, runs outside the host, and returns a generic table that the Statistics screen renders, so a new analysis is one module. Import Linter contracts in the commit gate forbid imports across the boundary. The record holds facts, not results, so an analysis change needs no migration. | Pass |
| X. Learning decisions rest on published research | R19 gives, for each learning decision of the feature, its sources in `docs/learning-research.md` and a status. Supported: recall before reveal, spaced reviews, relearning, no setting aside, the recorded time to reveal. Inference: the adaptive schedule, and mixed subjects in a session. Default with no source: target recall 0.9, the learning steps, and the review order. Contrary evidence: recall in thought with a self-assigned grade, for definition cards; FR-059 and FR-060 state the limit in each analysis. Reading depth is recorded per source in the register. T079 requires full texts and qualifications before dependent learning decisions are accepted. | Open: T079 |
| XI. Research becomes durable repository knowledge | Technical choices and alternatives belong in `research.md`; learning evidence belongs in `docs/learning-research.md`; dependency choices belong in `docs/desktop-dependency-survey.md`. Update the owner before accepting dependent work. | Pass at each decision |\n| XII. Durable logs, timing history, and measured optimization | Study scenarios retain revision, source and fixture digests, elapsed time, nested Python profiles, and diagnostics under `test-history/`. Application operations need XDG state logs and timings; broader test runners need the same durable evidence. | Open: T081 |\n| Technical constraints | `uv` and `bun` only; no run-time network; releases stay immutable, and the running copy keeps its host on its own release. | Pass |

**Post-design check**: The design in `research.md`, `data-model.md`, and `contracts/`
adds no violation. One risk stays open and is not a violation: a retained earlier release
may fail to open a store that a newer `anki` upgraded (R1). The failure is visible
(`StoreUnreadable`), and the learning record does not depend on Anki's format.

One conflict between principles is open for the user's decision. Principle III says that
dependencies track their latest versions. Principle IX says that the core changes
rarely and only on purpose. A newer `anki` changes scheduling behaviour without a change
in this repository. The design records the Anki version on every row and keeps dated
backups; it does not pin `anki`.

**Facts the feature observes and does not record** (principle VI requires a reason for
each):

| Fact | Reason |
| --- | --- |
| Pointer movement, scrolling, and keys other than reveal and grade | No analysis in the purpose uses them, and they are not a measure of recall. |
| Keys and text in the editor between two saves | Each saved state of a card is recorded, and each time a card is open in the editor is recorded with its duration (FR-058). The text between saves is not a state that the user kept. |
| Search text | A search gives a list. The card that the user opens from it is recorded as an editor view. |
| Which analysis the user ran, and when | Reading a statistic is not an act of learning or recall. The analysis part cannot write the record, by design. |
| The rendered pixels of a card | Native front and back source, the asset identity, and retained media describe the presentation. |

## Project Structure

### Documentation (this feature)

```text
specs/001-in-app-review/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── study-bridge.md
│   ├── learning-record.md
│   └── analysis.md
├── checklists/
│   └── requirements.md
└── tasks.md
```

### Source Code (repository root)

```text
desktop/
├── backend.py               # entry script: anki dependency, the study-host command, the analysis-list and analysis-run commands
├── study/                   # new: THE CORE. The only writer of learning data
│   ├── values.py            #   typed study values and requests
│   ├── store.py             #   store identity, open, attach, counts, recovery, backups, copy
│   ├── record.py            #   the record's schema and its insert functions
│   ├── sync.py              #   the sync plan and its application
│   ├── session.py           #   sessions, next card, answer, undo, the conversion to record values
│   ├── settings.py          #   scheduling settings and the fit
│   └── host.py              #   the request loop of the host process
├── analysis/                # new: THE ANALYSES. Read-only
│   ├── __init__.py          #   the table value, the read-only connection, the list, the run
│   └── catalog/             #   one module for each analysis
│       ├── recall_by_folder.py
│       └── calibration.py
├── .importlinter            # new: the import contracts between the parts
├── src/                     # THE INTERFACE
│   ├── bridge.ts            # Zod schemas and request types for the study and analysis actions
│   ├── study.tsx            # new: study screen, attach list, settings, record location, copy, fit, finished state
│   ├── study.ts             # new: session state, timing of reveal, grade, focus, and editor views, sync loop, count tree mapping
│   ├── statistics.tsx       # new: list of analyses and one renderer for every result table
│   ├── editor.tsx           # shared native card face for editing and study
│   ├── App.tsx              # entry points, tree counts, sync triggers, editor round trip, editor views
│   └── App.css
├── src-tauri/
│   ├── Cargo.toml           # tauri-plugin-single-instance
│   ├── src/lib.rs           # single-instance plugin first; study route: one host process, one request at a time, media scope
│   └── tauri.conf.json      # asset protocol for the store's media folder
├── vite.config.ts           # the same study route and a media route for the browser build
├── tests/
│   ├── study.py             # new: browser scenario with a real store; reads the record with sqlite3
│   ├── analysis.py          # new: the catalog through the entry script; an added, a failing, and a broken analysis
│   ├── boundaries.py        # new: each import contract rejects its violation
│   ├── study.test.ts        # new: scope and count mapping units
│   ├── native.py            # one study step and the second-launch step in the built window
│   └── fixtures/            # study fixture decks; the first-version record and its row dump
├── linux/install.py         # the release holds both packages; validation imports them and anki
└── README.md                # Study and Statistics sections; store and record location, attach, copy, backups

justfile                     # desktop-study-test, desktop-analysis-test, desktop-boundaries; test-commit includes them; desktop-test isolates XDG_DATA_HOME
docs/desktop-dependency-survey.md   # anki, single-instance, and Import Linter entries; the three parts
docs/study-record.md                # new: every table and field of the learning record; research-format mapping
docs/analyses.md                    # new: how to add an analysis, and the rules that it obeys
docs/learning-research.md           # the register of research sources; T079 raises its depth to Full

```

**Structure Decision**: The feature extends the existing desktop app in place, in three
parts (R17). The core is the package `desktop/study/`. The analyses are the package
`desktop/analysis/`. The interface is `desktop/src/`. `desktop/backend.py` stays the
entry script of every bridge process: it adds its own directory to `sys.path`, because
the shell runs it in isolated mode (R17), and it starts the host or runs one analysis.
A later analysis is one new file in `desktop/analysis/catalog/` and its test.
Native card input comes from `desktop/src/cards.ts`, through the saved-source bridge.

## Phases

| Phase | Content | Proof |
| --- | --- | --- |
| Foundation | The two packages and their import contracts; one running copy; native card IDs and source batches; `anki` dependency; typed study values on both sides; store identity, open, attach, and settings; the record database and its schema; host process and its two routes; test isolation | The boundary check rejects each violation; a second launch gives the focus to the first; `study-open` on a temporary data directory returns counts from a real collection through the real bridge route, and the record exists |
| US1 and US6 Review with a complete record | Sessions, `study-next`, `study-answer`, study screen, typesetting, media, first sync of all decks; every record field of a presentation and a response; measured times; editor views; recovery at open; attach list; record location; field reference | Quickstart steps for a session, durability, rendering, record fields, times, editor views, external read, queries, and the moved workspace |
| US2 Deck changes | Sync plan for update, move, rename, remove, restore, duplicate; triggers; card-change and content rows; scheduler tags kept | Quickstart steps for edits and file changes |
| US3 Counts and scope | Count tree in the deck tree; Study entry points on folder and deck | Quickstart steps for counts and scope |
| US4 Correction | `study-undo` with its `undo` row; editor round trip | Quickstart steps for Undo and Edit |
| US5 Load | Settings screen and bounds; setting-change rows; review order | Quickstart steps for limits, target recall, and order |
| US7 Fit | `study-fit`, `study-apply-fit`, fit screen, parameter-set rows | Quickstart steps for the fit |
| US8 Statistics | The analysis package, its two actions, the two first analyses, the Statistics screen, the authoring guide | Quickstart steps for the list, the results, the unchanged record, a failing analysis, and an added analysis |
| Keeping the data | `study-copy`, **Save a copy**, a copy attached on an empty data directory | Quickstart steps for the copy |
| Finish | Backups with record copies, the first-version record fixture read by the host and by every analysis, file placement in an empty home directory, native step, installer validation, documentation, full-workspace measurements | `just test-commit`; the manual table in `quickstart.md` |

US1 and US6 are one phase: the bridge contract identifies a grade by its presentation
row, and a review that is not recorded in full is lost for all later analysis. The app
is not used on the real data directory before that phase is complete. US2 to US5, US7,
US8, and the copy each depend on that phase and not on each other. Each core story
writes its own record rows. US8 writes none.

## Local feedback and milestone checks

Routine edits use the affected scenario, type check, or incremental compile with prepared
dependencies. Each loop must finish in seconds or a few minutes. Dependency refreshes,
full release builds, installation, and full-workspace measurements run at these milestones:

| Milestone | Checks |
| --- | --- |
| Foundation complete | Build the native app and verify one running copy, the host route, store identity, and isolated data placement. |
| First complete Study session with permanent record | Verify the complete native save, study, grade, undo, and recovery path. |
| Feature release | Run `desktop-update`, installer validation, and the full-workspace checks in T058. |

Study test runs retain evidence under `test-history/<UTC timestamp>-<scenario>/`: `run.json`\nrecords the revision, working source hashes, fixture hashes, environment, result, preparation\ntime, and elapsed time; `python.pstats` records nested calls in the test process; `test.log`\nrecords failures; native runs also retain WebKit diagnostics and the executable hash. The\nPython profile includes waits for child processes but not their call stacks. T081 extends\nmeasurement and durable logs to those operations and the other test runners. A timing\noptimization starts with the cost table required by constitution XII, in the design that\nowns the operation.\n\nThe feature's research synthesis belongs in `research.md`, with learning evidence in
`docs/learning-research.md` and dependency choices in `docs/desktop-dependency-survey.md`.
Each implementation decision cites its owning synthesis. New evidence updates that owner
before dependent work is accepted (constitution XI).

## Risks

| Risk | Evidence | Handling |
| --- | --- | --- |
| First sync time for 68 decks is unknown | Not measured | Batched sync with progress; measure in the Finish phase; SC-006 exempts first preparation |
| A long-lived process is new to the shell | `lib.rs` starts one process for each request | The route owns start, restart after exit, and stop at app exit; the native scenario proves it |
| A newer `anki` changes the collection format | Inferred | `StoreUnreadable` names the cause; Anki backups allow recovery; the learning record is a separate database in the app's format |
| The record and the collection have no common transaction | Two SQLite files | The `response` row is written after Anki stores the grade; rows that the record lacks are recovered at each open and marked |
| A later change breaks earlier record rows | Principle VI forbids it | A committed first-version record and its row dump; each later host must read it with every row equal |
| The record's size over decades | Estimated, not measured | Measure in the Finish phase; content and media are stored once for each version, not for each presentation |
| Anki's fit does not run in the wheel, or needs more history than a test can prepare | Presence of the calls probed; no call made | The US7 test task measures it first and records the result in `research.md` |
| No test proves that the record stays on the machine | A negative property | The host calls no sync function and opens no connection; a reviewer checks this by inspection |
| Tests write to the real history | `desktop-test` isolates the cache directory only | The Foundation changes the recipe before the window opens any store |
| Tier 1 feedback time | The complete tier 1 loop must stay under five minutes | Measure setup and nested work, fix repeated costs from a triage table, and run broader evidence at milestones |
| A later agent puts an analysis into the core, or a core call into an analysis | Analyses are added all the time, by agents | The import contracts fail the commit; the analysis connection is read-only; `docs/analyses.md` and the repository `AGENTS.md` state the rule |
| An analysis needs a dependency that conflicts with the core's | One environment for both packages (R17, alternative C) | Not handled now. A separate environment for the analyses is the next step when the first conflict occurs |
| A newer `anki` changes the core's behaviour with no change in this repository | Principle III against principle IX | Open for the user. The record names the Anki version on each row, and the store has dated backups |
| The second-launch step needs a D-Bus session in the native test | Not measured | The task for the step measures it and starts a session bus for the test when one is absent |
| The time of a copy for a large store, during which the host answers no request | Not measured | Measure in the Finish phase; the window shows progress |

## Complexity Tracking

| Principle | State | Reason | Closed by |
| --- | --- | --- | --- |
| VIII | Kept. The web view writes its cache under the data directory (R16). | The web view library of Tauri owns the placement. The cache holds no learning data. | A change in `wry`, or a web view data directory under the cache directory; the user decides (R16) |
| X | Open. Each source has depth Abstract or Secondary, and two decisions rest on one paper each (`kornell2008`, `mettler2016`). | The full texts are not read. | T079, before Phase 3 |
| III and IX | Open. `anki` has no version pin, and a newer `anki` changes the core's behaviour with no change in this repository. | The two principles disagree for this dependency. | The user's decision |
