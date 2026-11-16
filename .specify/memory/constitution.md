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

The system is the person's own learning management system. Review of cards is its first
form of study. Other forms can follow, for example quizzes, or oral examinations that an
AI component generates. Published research on learning decides what each form of study
does (principle X).

## Core Principles

### I. Markdown decks are the only authored source

Card content is authored in the Markdown files under `decks/`. The app reads those files
directly into its native card model. Current-content caches and search records can be
regenerated from them. Historical content shown during learning is permanent evidence
under principle VI. A feature MUST NOT make a generated store the only copy of card
content, and MUST NOT require an edit outside the Markdown source to
change a card. Data that the user produces by using the app and that cannot be regenerated
(review history, preferences) is user data: a feature MUST name where it lives and how it
survives an update of the app.

### II. Native cards, shared rendering, direct Anki integration

A card looks the same wherever it appears. The app's existing card parser owns card
structure and supplies native Markdown source to editing and study. Both use the Pandoc
editor renderer shared with Zettlr. MathJax with the macro set that pandoc-config generates
owns equations. The pandoc-config LuaLaTeX renderer owns TikZ-cd diagrams. A feature MUST
NOT add a second parser of card structure, define a macro by hand, or add a second equation
or diagram renderer.

The core MUST call Anki's library directly for scheduling, queues, grades, undo, and
scheduler history. Stable native card IDs connect that scheduling state to the app's
cards. Anki's scheduling notes hold those identities; the app owns content, presentation,
and the permanent content record. Saving and studying a native card MUST work directly
through these boundaries, from Markdown source to the shared renderer and scheduler.

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
evidence. Tests follow `test-guidelines` and the applicable code style skills; recheck
them against those rules throughout development. Each acceptance test comes from a real
user story in the specification. Replace internal-unit assertions and manipulation of
internal state with actions and observable results through that story's real path,
preserving the intended coverage. Mathematical library tests assert mathematics through
public operations at the owner of each operation.

Tests have named tiers. Tier 1 is the smallest set that establishes implementation
correctness through happy paths and meaningful branches. Its total feedback time,
including setup, MUST stay under five minutes. Higher tiers add evidence; the highest
tier covers the long tail of examples, permutations, edge cases, and combinations.

The local edit-and-check loop MUST return useful feedback in seconds or a few minutes
at most. Use targeted checks and incremental builds for routine changes. Long-running
checks and full builds belong at planned integration or release milestones. A plan MUST
name those milestones and their checks before implementation. A slow local loop is a
defect to fix; it does not justify weakening the checks or substituting a different path.
When a push starts long checks, push at milestones and use fast commit checks for the
ordinary feedback loop.

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

### X. Learning decisions rest on published research

A learning decision is a decision about how the person studies: what the app asks the
person to do, when, in what order, with what feedback, and what an analysis concludes
about the person's learning. Each learning decision of a feature rests on published
research on learning and retention. This applies to the review of cards and to each
later form of study.

- **Real papers.** The basis is a peer-reviewed study, a meta-analysis, or a systematic
  review, identified by its DOI. A blog, the documentation of a product, a popular book,
  and an agent's general knowledge are not a basis. An agent retrieves the record of a
  paper and reads the paper; it does not cite from memory.
- **The person's population.** The person is an adult who learns research-level
  mathematics alone. Admissible evidence is research on adults: university students and
  older, mathematics education at the undergraduate level and above, and general
  principles of learning that reviews show to hold for adults. A study of school children
  is not a basis for a decision. Where a finding exists only for children, the plan says
  so and the decision has no evidence.
- **Stated for each source.** The population, the material, the design, the outcome with
  its retention interval, the size of the effect, and how much of the paper was read
  (abstract or full text). A decision that depends on one paper needs the full text.
- **Applicability is argued.** Most experiments use simple material and delays of days
  or weeks. The plan states the distance between the study and the person's case
  (definitions, theorems, and proofs; delays of years) and labels a conclusion across
  that distance as an inference.
- **Contrary evidence is stated.** A dispute or a null result that bears on a decision
  is in the plan with the evidence for the decision.
- **No evidence is a result.** A decision for which no research was found is labelled a
  default, with its true source (for example, a default of Anki). It is not presented as
  a finding.
- **The record tests the decision.** Where it is possible, the plan names how the
  person's own record (principle VI) will show whether the decision works for this
  person.

`docs/learning-research.md` is the register of sources. A plan cites entries of the
register for each learning decision and adds the entries that it needs.

### XI. Research becomes durable repository knowledge

Every research activity MUST produce a synthesis in the repository's maintained
documentation before dependent work is accepted. This applies to learning research,
architecture, dependencies, APIs, experiments, and technical investigations.

The synthesis states the question, the supported findings, their sources, relevant
alternatives and contrary evidence, the limits of the evidence, and the resulting
decision or unresolved question. Extend the document that owns the topic: the research
register, feature design, dependency survey, or maintained technical documentation.
Keep source references precise enough for a later reader to verify the conclusions.
Chat, tool output, source lists, and copied passages do not replace this synthesis.
Use durable conclusions and their reasons; compute changing inventories from their
sources, as `AGENTS.md` requires.

### XII. Durable logs, timing history, and measured optimization

Detailed application logging is part of each feature from its first implementation.
Test runs also produce durable logs for historical review. Operational app logs use
the XDG state directory; learning evidence belongs in the permanent record under
principle VI.

Record timings for every test and computation, including setup, fixtures, construction,
and nested work. Retain those measurements and test logs with the repository from the
first run. Each run identifies its revision, environment, inputs, result, and enclosing
operations so later measurements can be compared. Plans name the record format and
repository location; raw measurement records are evidence, not session reports.

Before optimizing a timing issue, maintain a triage table at its owning design document.
Include the operation, measured cost per call, actual multipliers (calls, examples,
fixtures, repetitions), aggregate cost, priority, proposed remedy, and remaining measured
cost. Select work from those costs. Small costs that compound and large individual costs
take priority over unmeasured micro-optimizations.

Construction of mathematical objects MUST be close to instant. Defer expensive work
until it is queried unless an explicit option requests eager computation. Measure
construction and internal setup separately and apply timing triage when they dominate.

## Technical Constraints

- Linux is the supported platform. Support for another platform requires an explicit
  user request.
- Python runs through `uv`; JavaScript tooling runs through `bun`. `npm` and `pip` are not used.
- The installed app works from prepared local resources. Ordinary editing, review, and
  export do not fetch from the network.
- An installed release is immutable. An earlier release stays on disk for the copy that runs it.
- Deletion of user files goes through the system trash.
- JSON and YAML files are changed with `jq`, `yq`, or a script.

## Development Workflow

- Use the corresponding Spec Kit workflow for constitutions, specifications,
  clarification, plans, tasks, analysis, implementation, and convergence. Instruction
  and policy edits are verified by their source semantics and diff.
- Maintain contribution lessons in `CONTRIBUTING.md`. Give each policy a stable
  alphanumeric ID grouped by category. State the general class of contributions it
  governs and, when possible, show a concrete bad contribution and its good replacement.
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

**Version**: 2.2.0 | **Ratified**: 2026-11-16 | **Last Amended**: 2026-11-16
