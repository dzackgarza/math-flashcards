# Math Flashcards Constitution

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

## Technical Constraints

- Python runs through `uv`; JavaScript tooling runs through `bun`. `npm` and `pip` are not used.
- The installed app works from prepared local resources. Ordinary editing, review, and
  export do not fetch from the network.
- An installed release is immutable. Earlier releases stay on disk for running windows.
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

**Version**: 1.0.0 | **Ratified**: 2026-11-16 | **Last Amended**: 2026-11-16
