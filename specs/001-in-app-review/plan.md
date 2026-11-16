# Implementation Plan: In-App Review

**Branch**: `master` (no feature branch; feature directory `specs/001-in-app-review`) | **Date**: 2026-11-16 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-in-app-review/spec.md`

**Plan card**: `PLAN-in-app-review` under `FEATURE-in-app-review` in the agent-memory vault. The card points to this directory, which owns the plan.

## Summary

The desktop app gains a **Study** function: spaced-repetition review of the cards in the
saved Markdown decks, scheduled by Anki's own code. The bridge adds the PyPI `anki` wheel
and one long-lived host process that holds an Anki collection for the workspace. A
state-based sync keeps one Anki note for each `card-id`, so edits, moves, and renames keep
review history. A new React screen shows the card, the four grades with Anki's interval
labels, counts, and Undo. Package export does not change.

## Technical Context

**Language/Version**: Python ≥ 3.12 (bridge; the prepared runtime is 3.14), TypeScript with React (window), Rust (Tauri 2 shell), Lua (Pandoc filters)

**Primary Dependencies**: `anki` (PyPI wheel, new), `ankdown` from `ankdown-for-math`, Pydantic, filelock, platformdirs, Pandoc, MathJax 4, Mantine, Zod, Tauri 2

**Storage**: One Anki collection (SQLite) with its media folder for each workspace path, under `user_data_path("math-flashcards")/study/`; Anki `.colpkg` backups beside it

**Testing**: Playwright scenarios in Python against `just desktop-web` with the real bridge; `bun test` for TypeScript units; the native scenario under Xvfb; all run from `just test-commit`

**Target Platform**: Linux desktop (Tauri/WebKitGTK), one user, one machine

**Project Type**: Desktop app

**Performance Goals**: Next card readable within 0.5 s of a grade (SC-002); changed cards in review within 10 s of a save (SC-003); tree counts within 2 s of opening a prepared workspace (SC-006)

**Constraints**: No network at run time; installed releases are immutable; no version pins or lock files; the whole test suite under five minutes; Anki is AGPL-3.0-or-later

**Scale/Scope**: About 3,300 cards in 68 decks; one new screen; seven bridge actions; one new process type

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Result |
| --- | --- | --- |
| I. Markdown decks are the only authored source | The store's notes are regenerated from the decks by `study-sync`. Review history is user data: it lives in the user data directory (R4), has Anki backups, and is outside **Rebuild cached data**. | Pass |
| II. Shared rendering sources | Notes hold the package render (`render()` with both filters). The study screen typesets with the app's MathJax and the active macro set. No new parser, macro, or renderer. | Pass |
| III. Dependencies before hand-written code | Scheduling, queues, undo, counts, backups, and the database check are Anki calls. The one new algorithm is the sync plan (deck render against store snapshot); its reference is Anki's own import-by-GUID update behaviour and the existing `sync()` input comparison. The `id` field is added in the exporter's repository, not in a vendored copy. `anki` has no version pin. | Pass |
| IV. Fail loudly | Store in use, unreadable store, stale card, invalid settings, and render failures each reach the window with their cause. No empty store replaces an unreadable one. No import path for earlier history. | Pass |
| V. Proof through the real application path | `desktop/tests/study.py` drives the real window and bridge and reads the real store. The native scenario proves the host route. Each story's test is committed before its implementation. | Pass |
| Technical constraints | `uv` and `bun` only; no run-time network; releases stay immutable, and a running window keeps its host on its own release. | Pass |

**Post-design check**: The design in `research.md`, `data-model.md`, and `contracts/`
adds no violation. One risk stays open and is not a violation: a retained earlier release
may fail to open a store that a newer `anki` upgraded (R1). The failure is visible
(`StoreUnreadable`).

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
│   └── study-bridge.md
├── checklists/
│   └── requirements.md
└── tasks.md
```

### Source Code (repository root)

```text
desktop/
├── backend.py               # anki dependency; study models, store, sync plan, host loop, study-host command
├── paired-cards.lua         # passes each card-id to the exporter filter
├── src/
│   ├── bridge.ts            # Zod schemas and request types for the study actions
│   ├── study.tsx            # new: study screen, settings, finished state
│   ├── study.ts             # new: session state, sync loop, count tree mapping
│   ├── math.ts              # element typesetting for rendered card HTML
│   ├── App.tsx              # entry points, tree counts, sync triggers, editor round trip
│   └── App.css
├── src-tauri/
│   ├── src/lib.rs           # study route: one host process, one request at a time, media scope
│   └── tauri.conf.json      # asset protocol for the store's media folder
├── vite.config.ts           # the same study route and a media route for the browser build
├── tests/
│   ├── study.py             # new: browser scenario with a real store
│   ├── study.test.ts        # new: scope and count mapping units
│   ├── native.py            # one study step in the built window
│   └── fixtures/            # study fixture decks
├── linux/install.py         # release validation imports anki
└── README.md                # Study section; store location

justfile                     # desktop-study-test; test-commit includes it; desktop-test isolates XDG_DATA_HOME
docs/desktop-dependency-survey.md   # anki entry and the study boundary

(ankdown-for-math repository)        # Card.id in the model and in ankdown.lua
```

**Structure Decision**: The feature extends the existing desktop app in place. The bridge
stays one script (`desktop/backend.py`); the window gains two modules. The exporter change
is made in its own repository and reaches this one through the unpinned dependency.

## Phases

| Phase | Content | Proof |
| --- | --- | --- |
| Foundation | Card ID in the render output; `anki` dependency; typed study values on both sides; store open, lock, and settings; host process and its two routes; test isolation | `study-open` on a temporary data directory returns counts from a real collection through the real window |
| US1 Review | `study-next`, `study-answer`, study screen, typesetting, media, first sync of all decks | Quickstart steps for a session, durability, and rendering |
| US2 Deck changes | Sync plan for update, move, rename, remove, restore, duplicate; triggers | Quickstart steps for edits and file changes |
| US3 Counts and scope | Count tree in the deck tree; Study entry points on folder and deck | Quickstart steps for counts and scope |
| US4 Correction | `study-undo`; editor round trip | Quickstart steps for Undo and Edit |
| US5 Load | Settings screen and bounds | Quickstart steps for limits and target recall |
| Finish | Backups, native step, installer validation, documentation, full-workspace measurements | `just test-commit`; the manual table in `quickstart.md` |

US1 depends on the Foundation and on the add path of sync. US2 to US5 each depend on US1
and not on each other.

## Risks

| Risk | Evidence | Handling |
| --- | --- | --- |
| First sync time for 68 decks is unknown | Not measured | Batched sync with progress; measure in the Finish phase; SC-006 exempts first preparation |
| A long-lived process is new to the shell | `lib.rs` starts one process for each request | The route owns start, restart after exit, and stop at app exit; the native scenario proves it |
| A newer `anki` changes the collection format | Inferred | `StoreUnreadable` names the cause; Anki backups allow recovery |
| Tests write to the real history | `desktop-test` isolates the cache directory only | The Foundation changes the recipe before the window opens any store |
| Suite time | The suite limit is five minutes | The study scenario uses small fixture decks; the full workspace is a manual check |

## Complexity Tracking

No constitution violation needs justification.
