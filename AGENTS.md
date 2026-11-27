> **Planning migration — Spec Kit and itree**
>
> Select the work-unit issue with itree. Use Spec Kit to plan and execute the work.
> The issue body and comments hold the current plan, tasks, progress and evidence.
> Earlier instructions that assign this work to vault cards or a separate task list
> identify records to migrate. Match each obligation to its owning issue. Preserve
> task IDs, order, prerequisites, acceptance criteria and evidence. Verify the transfer
> on the issue before retiring the old tracker. An open obligation stays open.

Use the [shared math container](https://github.com/dzackgarza/ai-review-ci/blob/main/SAGE-CONTAINER.md#use-the-image)
(`ghcr.io/dzackgarza/sage:develop`) for Lean/elan, Sage with mypy, GAP,
Julia/Oscar, Macaulay2, and Singular. The guide covers image pull/run commands,
CI use, and the host launchers.

# Content work

`CONTRIBUTING.md` owns the teaching remit and the method for establishing
research relevance from current sources.
Use its "Understand the research before evaluating coverage" and "Evaluate
usefulness through a mathematical task" sections before judging coverage or
scope. Reconstruct the relevant arguments, including implicit operations and
their hypotheses, before identifying prerequisites. Establish a candidate's mathematical role,
then assess coverage and personal familiarity separately. The existing
independent study subjects remain part of the collection.
Do not substitute a generic graduate curriculum or a cited author's complete
research output for this remit.

A request to correct the editorial process targets these governing documents.
Repair the method that produced the judgment. Verify the instructions require
mathematical understanding of the current work, rather than a fixed inventory
of topics from an earlier assessment. Keep card changes out of a process-only
correction.

# Durable documentation

Repository documentation should explain maintained behavior, mathematical
reference material, authoring conventions, or decisions that govern future
work. A request for an assessment or explanation normally calls for an answer
in chat, not a new repository file.

Do not create durable documents for:

- Point-in-time coverage assessments, gap lists, or inventories of which cards
  currently contain a topic. These become stale as cards change.
- Ad hoc audit reports, review findings, or proposed remediation lists produced
  to answer a conversational question.
- Session status, progress reports, completion summaries, validation logs, or
  accounts of attempts and failures. Git history and tool output already record
  changes and checks.
- Apologies, explanations of agent mistakes, or transcripts of user corrections.
  Apply the correction to the owning material. When instructed to change a
  policy, write the operative rule rather than the conversation that led to it.
- Duplicate plans, handoffs, or tracking files that compete with an existing
  source of task state.
- A file created solely to satisfy an assumed requirement to return an artifact
  path. The requested deliverable determines whether a file is needed.

Give assessments in chat with their substantive findings, supporting examples,
and limits. Do not replace that answer with a link to a newly created report or
compress away findings that determine the scope of the work. When remediation
is requested, edit the cards or other owning source directly.

An explicit request for a saved report, audit artifact, or handoff authorizes
that deliverable within the requested scope. Otherwise, before adding a document,
identify its continuing purpose and how it will remain accurate as the repository
changes. If its only purpose is to record the answer to the current conversation,
keep the answer in chat. Extend an existing owning document when a durable rule
or explanation belongs there.

# Application architecture

`.specify/memory/constitution.md` states these rules in full (principles II and VI to X). They
apply to every change of the desktop app.

- **One person, one running copy.** The app is a singleton for one user. Do not add a
  lock, conflict handling, or an error state for a second running copy or a second user.
- **XDG placement.** Each file the app writes outside the workspace is under the XDG
  base directory for its kind, resolved by a library. Learning data is under
  `XDG_DATA_HOME`. Removal of the cache and state directories loses no learning data.
- **Learning data is permanent.** No change deletes or rewrites a record of the user's
  learning, and its format only grows. Each action that bears on the user's learning is
  recoverable from the git history of the workspace or from the learning record.
- **Diagrams are compiled before display.** The TikZ filter of the Pandoc configuration
  owns diagram compilation, its cache, recompilation, and macros. Compilation is one
  script job that runs without the app. The app only starts it: at its start, on
  request, and after a card edit ends (debounced). A card shows a cached SVG and never waits for a compile.
- **Anki's interface settles open interface questions.** When a specification does not
  say what a Study screen counts, shows, or names, read Anki's source and do what Anki
  does. Do not ask the user and do not invent a rule.
- **Three parts.** The core (scheduling, Anki-based logic, the review store, every write
  of learning data) changes rarely. Analyses (everything computed from recorded history)
  and the interface change often. An analysis reads learning data and cannot change it,
  keeps no permanent data, and is one unit that depends on no other analysis. A new
  analysis or view needs no change to the core, to the record's format, or to stored
  data. When an analysis needs a fact that the record does not hold, the core starts to
  record that fact; no existing entry is rewritten.

# Learning research

The app is the user's own learning management system. Card review is its first form of
study; quizzes, oral examinations generated by an AI component, and other forms can
follow. Constitution principle X governs each of them.

- **Published research decides.** Each decision about how the user studies (the task,
  its timing and order, the feedback, the conclusion of an analysis) cites real papers
  from `docs/learning-research.md`. Retrieve each paper's record by DOI and read the
  paper. Do not cite from memory.
- **Adults only.** The user is an adult who learns research-level mathematics. Use
  research on university students and older, on undergraduate and higher mathematics
  education, and on general principles shown to hold for adults. Research on school
  children is not a basis for a decision.
- **State the limits.** Give the population, material, design, retention interval,
  effect size, and reading depth of each source. Label a conclusion that goes from
  simple material and short delays to advanced mathematics and years as an inference.
  Report contrary evidence.
- **No evidence is a result.** Label a decision without research as a default and name
  its true source. Do not present it as a finding.

<!-- agent-memory:start -->
# Agent memory

This repository uses the central agent memory vault at `/home/dzack/.agent-memory-vault`.

Project memory key: `projects/github.com__dzackgarza__math-flashcards/index`.

Repository `.agents` and `.hermes` paths are symlinks to the same vault-owned project directory.

Before changing architecture, search both project and global memory:

```bash
agent-memory search --scope both "<task or subsystem>"
```

Record durable repo-specific lessons with:

```bash
agent-memory add --scope project --type decision --title <title> --content <content>
agent-memory add --scope project --type trap --title <title> --content <content>
agent-memory add --scope project --type advice --title <title> --content <content>
agent-memory add --scope project --type context --title <title> --content <content>
agent-memory add --scope project --type reference --title <title> --content <content>
```

Use Spec Kit to plan each itree work unit. Its GitHub issue owns the current plan, tasks and progress.

Use `agent-memory retrieve <key>`, `agent-memory update <key>`, and `agent-memory delete <key>` for memory CRUD.

The vault should be committed at all times. Treat staged or unstaged vault changes as an ephemeral error state. Before normal memory work resumes, load the bundled vault-maintenance skill with `agent-memory maintain skill vault-maintenance` and follow its referenced check, repair, and commit workflows.

Move reusable lessons during maintenance with:

```bash
agent-memory maintain move <key> --to global/advice
```
<!-- agent-memory:end -->
