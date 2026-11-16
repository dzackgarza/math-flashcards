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
