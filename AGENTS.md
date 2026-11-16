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

<!-- agent-memory:start -->
# Application architecture

`.specify/memory/constitution.md` states these rules in full (principles VI to IX). They
apply to every change of the desktop app.

- **One person, one running copy.** The app is a singleton for one user. Do not add a
  lock, conflict handling, or an error state for a second running copy or a second user.
- **XDG placement.** Each file the app writes outside the workspace is under the XDG
  base directory for its kind, resolved by a library. Learning data is under
  `XDG_DATA_HOME`. Removal of the cache and state directories loses no learning data.
- **Learning data is permanent.** No change deletes or rewrites a record of the user's
  learning, and its format only grows. Each action that bears on the user's learning is
  recoverable from the git history of the workspace or from the learning record.
- **Three parts.** The core (scheduling, Anki-based logic, the review store, every write
  of learning data) changes rarely. Analyses (everything computed from recorded history)
  and the interface change often. An analysis reads learning data and cannot change it,
  keeps no permanent data, and is one unit that depends on no other analysis. A new
  analysis or view needs no change to the core, to the record's format, or to stored
  data. When an analysis needs a fact that the record does not hold, the core starts to
  record that fact; no existing entry is rewritten.

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

Plan work is card-backed. Create and update plan cards with `agent-memory plan add` and `agent-memory plan update`, not `agent-memory add --type plan`.

Use `agent-memory retrieve <key>`, `agent-memory update <key>`, and `agent-memory delete <key>` for memory CRUD.

The vault should be committed at all times. Treat staged or unstaged vault changes as an ephemeral error state. Before normal memory work resumes, load the bundled vault-maintenance skill with `agent-memory maintain skill vault-maintenance` and follow its referenced check, repair, and commit workflows.

Move reusable lessons during maintenance with:

```bash
agent-memory maintain move <key> --to global/advice
```
<!-- agent-memory:end -->
