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
collection for the workspace. A state-based sync keeps one Anki note for each `card-id`,
so edits, moves, and renames keep review history. A new React screen shows the card, the
four grades with Anki's interval labels, counts, and Undo. Package export does not
change.

Beside the collection, the host writes the learning record: an append-only SQLite
database that the app owns. It holds each showing of a card with its content, subject,
measured times, grade, and scheduler state, and each session, card change, undo, and
settings change. The user reads it with standard data tools while the app runs. A store
belongs to a workspace and attaches to a new path on the user's choice. The user fits
the scheduler's parameters to this history with Anki's own fitting code.

## Technical Context

**Language/Version**: Python ≥ 3.12 (bridge; the prepared runtime is 3.14), TypeScript with React (window), Rust (Tauri 2 shell), Lua (Pandoc filters)

**Primary Dependencies**: `anki` (PyPI wheel, new), Python's `sqlite3` (standard library, for the learning record), `ankdown` from `ankdown-for-math`, Pydantic, filelock, platformdirs, Pandoc, MathJax 4, Mantine, Zod, Tauri 2

**Storage**: One store for each workspace under `user_data_path("math-flashcards")/study/<store ID>/`: an Anki collection (SQLite) with its media folder, the learning record `record.sqlite3` (SQLite, schema owned by the app, rows only inserted) with `record-media/`, `store.json`, and `backups/` with Anki `.colpkg` files and record copies

**Testing**: Playwright scenarios in Python against `just desktop-web` with the real bridge; `bun test` for TypeScript units; the native scenario under Xvfb; all run from `just test-commit`

**Target Platform**: Linux desktop (Tauri/WebKitGTK), one user, one machine

**Project Type**: Desktop app

**Performance Goals**: Next card readable within 0.5 s of a grade (SC-002); changed cards in review within 10 s of a save (SC-003); tree counts within 2 s of opening a prepared workspace (SC-006)

**Constraints**: No network at run time; the learning record never leaves the machine; no row of the record is updated or deleted; the record's schema only grows; installed releases are immutable; no version pins or lock files; the whole test suite under five minutes; Anki is AGPL-3.0-or-later

**Scale/Scope**: About 3,300 cards in 68 decks; a record that grows for decades (an estimate of 1 kB for each presentation, not measured); one new screen; twelve bridge actions; one new process type

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Result |
| --- | --- | --- |
| Purpose | The feature is built for one person's learning over a career. It records more than Anki records, changes Anki's review order and answer-time limit for that purpose (R9), and omits Anki's sync, editor, add-ons, and sharing. | Pass |
| I. Markdown decks are the only authored source | The store's notes are regenerated from the decks by `study-sync`. Review history and the learning record are user data: they live in the user data directory (R4), have backups, and are outside **Rebuild cached data**. The record keeps the content of each card as shown; it is a history of what the user saw, not a source of cards. | Pass |
| II. Shared rendering sources | Notes hold the package render (`render()` with both filters). The study screen typesets with the app's MathJax and the active macro set. No new parser, macro, or renderer. | Pass |
| III. Dependencies before hand-written code | Scheduling, queues, undo, counts, backups, the database check, and parameter fitting are Anki calls. Two parts are new code. The sync plan (deck render against store snapshot) has Anki's import-by-GUID update behaviour and the existing `sync()` input comparison as its reference. The learning record's schema is hand-written; SQLite owns storage, concurrent reads, and backup; the reference for its rules is the xAPI statement model (never changed, undone by a new statement), and the reference for its fields is Anki's review log and the public research data set (R12). No surveyed library stores this record. The `id` field is added in the exporter's repository, not in a vendored copy. `anki` has no version pin. | Pass, with the record schema for the user's approval |
| IV. Fail loudly | Store in use, unreadable store, unknown store, stale card, invalid settings, too little history, and render failures each reach the window with their cause. No empty store replaces an unreadable one or an unattached one. No import path for earlier history. The record has no migration: its schema only grows, as principle VI requires. | Pass |
| V. Proof through the real application path | `desktop/tests/study.py` drives the real window and bridge, reads the real store, and reads the real record with `sqlite3` alone. The native scenario proves the host route. Each story's test is committed before its implementation. | Pass |
| VI. The learning record is complete, permanent, and open to analysis | Complete: each presentation, response, undo, session, card change, and settings change is a row (FR-028 to FR-035); rows that Anki has and the record lacks are recovered at open (FR-036). Permanent: the host has no update or delete statement; a store attaches to a new path (FR-041); backups include the record. Independent: a second database in a documented format, readable without the app and without Anki. Additive: a `schema` table and a committed first-version fixture that every later release must read. Open: SQLite, a `review` view, `docs/study-record.md`, and the mapping to the research data set. Private: no study action calls Anki's sync or opens a connection; this is established by inspection, not by a test. Scheduling: ascending retrievability and tag-only leeches (R9). | Pass |
| Technical constraints | `uv` and `bun` only; no run-time network; releases stay immutable, and a running window keeps its host on its own release. | Pass |

**Post-design check**: The design in `research.md`, `data-model.md`, and `contracts/`
adds no violation. One risk stays open and is not a violation: a retained earlier release
may fail to open a store that a newer `anki` upgraded (R1). The failure is visible
(`StoreUnreadable`), and the learning record does not depend on Anki's format.

**Facts the feature observes and does not record** (principle VI requires a reason for
each):

| Fact | Reason |
| --- | --- |
| Pointer movement, scrolling, and keys other than reveal and grade | No analysis in the purpose uses them, and they are not a measure of recall. |
| Editor activity (time spent writing a card) | The editor is outside this feature. A later feature that records it follows principle VI. |
| The rendered pixels of a card | The front and back HTML with their media files reproduce the card. |

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
│   └── learning-record.md
├── checklists/
│   └── requirements.md
└── tasks.md
```

### Source Code (repository root)

```text
desktop/
├── backend.py               # anki dependency; study models, store identity, learning record, sync plan, host loop, fit, study-host command
├── paired-cards.lua         # passes each card-id to the exporter filter
├── src/
│   ├── bridge.ts            # Zod schemas and request types for the study actions
│   ├── study.tsx            # new: study screen, attach list, settings, record location, fit, finished state
│   ├── study.ts             # new: session state, timing of reveal, grade, and focus, sync loop, count tree mapping
│   ├── math.ts              # element typesetting for rendered card HTML
│   ├── App.tsx              # entry points, tree counts, sync triggers, editor round trip
│   └── App.css
├── src-tauri/
│   ├── src/lib.rs           # study route: one host process, one request at a time, media scope
│   └── tauri.conf.json      # asset protocol for the store's media folder
├── vite.config.ts           # the same study route and a media route for the browser build
├── tests/
│   ├── study.py             # new: browser scenario with a real store; reads the record with sqlite3
│   ├── study.test.ts        # new: scope and count mapping units
│   ├── native.py            # one study step in the built window
│   └── fixtures/            # study fixture decks; the first-version record and its row dump
├── linux/install.py         # release validation imports anki
└── README.md                # Study section; store and record location, attach, backups

justfile                     # desktop-study-test; test-commit includes it; desktop-test isolates XDG_DATA_HOME
docs/desktop-dependency-survey.md   # anki entry and the study boundary
docs/study-record.md                # new: every table and field of the learning record; research-format mapping

(ankdown-for-math repository)        # Card.id in the model and in ankdown.lua
```

**Structure Decision**: The feature extends the existing desktop app in place. The bridge
stays one script (`desktop/backend.py`); the window gains two modules. The exporter change
is made in its own repository and reaches this one through the unpinned dependency.

## Phases

| Phase | Content | Proof |
| --- | --- | --- |
| Foundation | Card ID in the render output; `anki` dependency; typed study values on both sides; store identity, open, attach, lock, and settings; the record database and its schema; host process and its two routes; test isolation | `study-open` on a temporary data directory returns counts from a real collection through the real bridge route, and the record exists |
| US1 and US6 Review with a complete record | Sessions, `study-next`, `study-answer`, study screen, typesetting, media, first sync of all decks; every record field of a presentation and a response; measured times; recovery at open; attach list; record location; field reference | Quickstart steps for a session, durability, rendering, record fields, times, external read, queries, and the moved workspace |
| US2 Deck changes | Sync plan for update, move, rename, remove, restore, duplicate; triggers; card-change and content rows; scheduler tags kept | Quickstart steps for edits and file changes |
| US3 Counts and scope | Count tree in the deck tree; Study entry points on folder and deck | Quickstart steps for counts and scope |
| US4 Correction | `study-undo` with its `undo` row; editor round trip | Quickstart steps for Undo and Edit |
| US5 Load | Settings screen and bounds; setting-change rows; review order | Quickstart steps for limits, target recall, and order |
| US7 Fit | `study-fit`, `study-apply-fit`, fit screen, parameter-set rows | Quickstart steps for the fit |
| Finish | Backups with record copies, the first-version record fixture, native step, installer validation, documentation, full-workspace measurements | `just test-commit`; the manual table in `quickstart.md` |

US1 and US6 are one phase: the bridge contract identifies a grade by its presentation
row, and a review that is not recorded in full is lost for all later analysis. The app
is not used on the real data directory before that phase is complete. US2 to US5 and US7
each depend on that phase and not on each other. Each of them writes its own record
rows.

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
| Suite time | The suite limit is five minutes | The study scenario uses small fixture decks; the full workspace is a manual check |

## Complexity Tracking

No constitution violation needs justification.
