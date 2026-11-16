# Math Flashcards Constitution

## Purpose

This project is a personal mathematics learning system for one person, built for that
person alone. Its time scale is a career: knowledge that stays recallable for decades, a
place to put everything the person wants to remember for life, and a record of the
person's own learning that grows for the same decades. The record exists so that the
person can analyse their own performance with statistical methods and with results from
learning research: which subjects are weak and need more study or more sources, and which
are fluent and need little review. The project adapts and reuses Anki for this purpose. It
is not a copy of Anki and has no duty to behave as a general flashcard program for other
people.

## Core Principles

### I. Markdown decks are the only authored source

Card content is authored in the Markdown files under `decks/`. Every other store of card
content is generated from those files and can be regenerated from them: Anki packages,
caches, search records, and any review store. A feature MUST NOT make a generated store the
only copy of card content, and MUST NOT require an edit outside the Markdown source to
change a card. Data that the user produces by using the app and that cannot be regenerated
(review history, preferences) is user data: a feature MUST name where it lives and how it
survives an update of the app.

### II. Shared rendering sources

A card looks the same wherever it appears. Pandoc and the exporter's filters own card
structure. MathJax with the macro set that pandoc-config generates owns equations. The
pandoc-config LuaLaTeX renderer owns TikZ-cd diagrams. The editor fields use the Pandoc
editor package shared with Zettlr. A feature MUST NOT add a second parser of card
structure, define a macro by hand, or add a second equation or diagram renderer.

### III. Dependencies before hand-written code

A maintained library, an existing component, or a reference implementation owns each
behaviour that one exists for. Hand-written code MUST cite a mature reference; with no
reference it needs the user's approval. Vendored code is never modified in place.
Dependencies track their latest versions: no version pins and no lock files.

### IV. Fail loudly

No backward compatibility, fallbacks, compatibility shims, or migrations. A missing file, a
failed check, or an invalid state produces a visible error that names the cause. A feature
MUST NOT hide a failure, substitute a default result, or remove functionality to make an
error disappear.

### V. Proof through the real application path

Tests assert the intended end-to-end behaviour through the path the user takes: the real
backend, real files, and the real rendered window. A bug fix starts with a committed test
that fails for the reported reason. Mocks that supply the behaviour under test are not
evidence. The whole suite stays under five minutes.

### VI. The learning record is complete, permanent, and open to analysis

Every feature in which the person learns, recalls, or reviews MUST record what the person
did, in as much detail as the feature can observe, with the context that gives the record
meaning later: the time, the content that was shown, its subject, the state of the
scheduler, and the settings in effect. A fact that the app can observe and does not record
is lost for all later analysis, so a feature MUST justify each observable fact it omits.

- **Permanent.** No feature deletes or overwrites a record of the person's performance. A
  correction is a new record that refers to the earlier one. A feature MUST NOT lose
  records when a file moves, a deck is reorganized, the app is updated, or the machine
  changes.
- **Independent.** The record is readable without this app and without Anki. Where a
  dependency keeps its own history in its own format, the app keeps a complete copy in a
  documented format that the project owns.
- **Additive format.** The format of the record only grows. A record that any earlier
  release wrote stays readable by every later release. Principle IV does not permit a
  change that makes an earlier record unreadable.
- **Open to analysis.** The person can read the whole record with standard data tools. A
  feature documents each field it records.
- **Private.** The record stays on the person's machine. No feature sends it elsewhere.
- **Easy to keep.** All learning data of a workspace is in one directory. The person
  makes a complete copy of it in one step, and a copy works on any machine.
- **Covers every act of learning.** Each action in the app that bears on the person's
  learning can be extracted and understood later, from the git history of the workspace
  or from the record. A feature states, for each such action, which of the two holds it.

Scheduling serves long-term retention. Material that the record shows to be fluent gets
less of the person's time, and material that it shows to be weak gets more.

### VII. One person, one running copy

One person uses the app, and one copy of the app runs on a machine. A second launch
brings the running copy to the front and starts nothing. A feature MUST NOT add a lock,
a merge rule, conflict handling, or an error state for a second running copy or a second
user. Inside the running copy, each store of user data has one writer.

### VIII. XDG Base Directory placement

Every file that the app writes outside the workspace is under the XDG base directory for
its kind, in a directory named for the app:

| Kind | Base directory |
| --- | --- |
| Learning data and other data that cannot be regenerated | `XDG_DATA_HOME` |
| Preferences | `XDG_CONFIG_HOME` |
| State that persists between runs and is not learning data (logs, window layout) | `XDG_STATE_HOME` |
| Data that the app can regenerate | `XDG_CACHE_HOME` |

A library resolves each directory (`platformdirs` in Python, the Tauri path API in the
shell). No path is fixed relative to the home directory. Removal of the cache and state
directories loses no learning data.

### IX. Three parts with a small blast radius

The app has three parts. Analyses and the interface change often, for the whole life of
the project. The core changes rarely. The boundaries keep a frequent change away from
the learning data and from the scheduling logic.

| Part | Owns | Rule |
| --- | --- | --- |
| Core | Scheduling, the Anki-based logic, the review store, and every write of learning data | The only writer of learning data. It contains no presentation and no statistics. It depends on neither other part. |
| Analysis | Everything computed after the fact from recorded history: statistics, models, findings about the person's learning | It reads learning data and cannot change it. It keeps no permanent data: each result can be computed again from the record. Each analysis is one unit that depends on no other analysis. |
| Interface | What the person sees and does | It shows what the core and the analyses return, and sends the person's input to them. It contains no scheduling rule and no computation over the record. |

- A new or changed analysis, and a new or changed view, MUST NOT need a change to the
  core, to the format of the record, or to stored data.
- When an analysis needs a fact that the record does not hold, the core starts to record
  that fact (principle VI, additive). No existing entry is rewritten.
- A change to the core is deliberate: its plan names the change and the reason, and the
  core's own tests prove that the behaviour it did not mean to change is the same.
- The commit gate checks the boundaries.

## Technical Constraints

- Python runs through `uv`; JavaScript tooling runs through `bun`. `npm` and `pip` are not used.
- The installed app works from prepared local resources. Ordinary editing, review, and
  export do not fetch from the network.
- An installed release is immutable. An earlier release stays on disk for the copy that runs it.
- Deletion of user files goes through the system trash.
- JSON and YAML files are changed with `jq`, `yq`, or a script.

## Development Workflow

- `just test-commit` is the commit gate and `just test-push` is the push gate. The gates run
  from the hooks; a change is complete when the gate passes.
- Git history only moves forward. A correction is a new commit.
- Formatter output is canonical.
- Repository documents describe maintained behaviour, as `AGENTS.md` defines. Status
  reports, audit results, and session accounts are not committed.

## Governance

`AGENTS.md` and the instructions it refers to own project policy. This constitution states
the rules that Spec Kit plan gates check; when the two disagree, `AGENTS.md` governs and
this file is corrected. An amendment is a commit to this file with a semantic version
change: MAJOR for a removed or redefined principle, MINOR for an added principle or
section, PATCH for a clarification. Every plan records its check against these principles,
and each violation it keeps is justified in that plan.

**Version**: 1.2.0 | **Ratified**: 2026-11-16 | **Last Amended**: 2026-11-16
