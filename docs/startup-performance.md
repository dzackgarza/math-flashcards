# Startup measurements

Measure the populated tree, editable deck, mathematical rendering, and completed
background checks separately. A displayed window alone does not prove usable startup.
Release acceptance needs repeated measurements in both cache conditions and the
installed native app. Development measurements below are baseline observations.

## Baseline

Recorded on 2026-10-25, before switching the frontend from the combined list request.
The checkout had the new local discovery operations and reserved request capacity;
the frontend still used the original listing and document operations.

| Environment | Value |
| --- | --- |
| Source base | `0647d603338e275e28bb2775c5401110b0f46cd7` |
| CPU | Intel Core i7-1355U |
| Architecture | x86_64 |
| Logical processors | 12 |
| Kernel | Linux 7.2.7-zen1-1-zen |
| Workspace decks | 41 |
| Source bytes returned by list | 823879 |
| Repository packages on disk | 19 MiB, rounded by `du -sh` |
| Browser selected fixture | `decks/Analysis/Precalculus.md` |
| Fixture source bytes | 7650 |
| Fixture SHA-256 | `c966a97dd02f89214e14675c5c3cb9cec1e63c8a7fc938fc388cfa65def8375f` |
| Disposable browser workspace package bytes | 0 |

| Development endpoint | Seconds, single observation |
| --- | ---: |
| Browser navigation to default tree | 13.871 |
| Open disposable workspace to tree | 13.304 |
| Deck selection to editable fields | 4.158 |
| Deck selection to rendered equations | 4.272 |
| Direct Python list of repository decks under strace | 2.510 |

The browser measurements use `time.monotonic()` in
`desktop/tests/workbench.py`. The selected fixture is copied into a disposable
workspace. The script records its exact source digest, source size, source
revision, host identity, and separate endpoints in
`desktop/test-artifacts/startup.json`.

The direct list trace is `desktop/test-artifacts/baseline-list.trace`, captured
with `strace -f -e trace=process,network`. It shows DNS and HTTPS connections
before the list response. The adapters also run `uv sync --upgrade` for the
combined list operation. The direct Python timing excludes that upgrade.

Before the commit gate rebuilt the app, the release binary and the installed
binary had the same SHA-256:
`66aaff7d135718ca6e087e13afe02655056a40a712ee3a6250e7e96b2d9c8b35`.
This identifies the compared binaries; it does not attribute native performance
to the current checkout. Native launch distributions, warm-cache distributions,
input latency, and background-completion distributions remain to be measured.

## Request capacity

The focused browser startup scenario copies the complete source corpus into a
disposable workspace. It requires selection, editing, and a saved disk change
while check coverage is incomplete, then waits for completed source, package,
and Problems coverage. Its screenshots and trace use the `startup-` prefix in
`desktop/test-artifacts/`. The populated editor and final coverage screenshots
were inspected.

| Progressive development endpoint | Seconds, single observation |
| --- | ---: |
| Open workspace to tree | 1.628 |
| Select deck to editable fields | 3.375 |
| Fill field and observe its text through Playwright | 0.896 |
| Open workspace to complete background checks | 76.572 |

The field-fill interval includes browser automation and assertions. It is not
the keyboard-event latency acceptance measurement. Release distributions remain
required. The selection observation exceeds the proposed release target and
needs critical-path profiling.

An import profile of a manifest request is saved in
`desktop/test-artifacts/startup-imports.log`. Importing `ankdown.cli` took
622 ms cumulatively in that observation; its imports include Cyclopts, Pydantic,
and Genanki. Foreground reads can avoid exporter and CLI imports.

Foreground requests now import the lightweight Ankdown package rather than its
export CLI. Maintenance loads Cyclopts and the exporter explicitly. Document
reads obtain bytes and a digest; package checks own build-record access.
The renderer loads one asset set per app session and starts independently of
directory discovery.

| After import separation | Seconds, single observation |
| --- | ---: |
| Direct manifest request under import profiling | 0.250 |
| Direct selected-document request | 0.190 |
| Browser workspace to tree | 0.361 |
| Browser deck selection to editable fields | 1.806 |
| Browser field fill and text assertion | 0.565 |
| Browser complete background checks | 42.909 |

The later import profile is `startup-imports-local.log`. The remaining editor
and input timing observations still need release profiling and event-to-paint
measurements before comparison with acceptance budgets.

The native bridge uses independent Tokio semaphores for foreground requests and
background batches. The browser adapter uses independent
[p-limit queues](https://github.com/sindresorhus/p-limit#usage) with the same
capacity. A background operation cannot take the foreground permit. Each source
or package-check batch accepts at most eight deck paths.

Dependency maintenance clears `GIT_INDEX_FILE` before accessing the parser's
Git repository. A partial commit supplies a temporary index for the application
repository; nested Git commands must use the parser repository's own index.
Git documents the environment boundary in its
[hook guidance](https://git-scm.com/docs/githooks#_description).

## Persistent Problems verification

The browser scenario uses an isolated application cache while retaining the
tool and browser download caches. It verifies cached Problems after a fresh
page launch, then changes a macro without changing file size or nanosecond
modification time. The new undefined-macro diagnostic replaces the cached one.

The scenario damages a stored problem record, observes the rebuild action,
and rebuilds the cache. It checks that fresh Problems records return and that
authored source, the prior package bytes, and successful build provenance
remain unchanged. Cache screenshots use the `cache-` prefix; the replayable
trace is `desktop/test-artifacts/trace.zip`.

Checker validity includes the card parser, problem checker, math adapter,
bridge schema, resolved Pandoc parser code, and dependency lock data. The
backend also keys records by their Pydantic storage schema. Source identity
uses SHA-256 of file bytes, independently of filesystem timestamps.

## Session renderer assets

The offline generation case uses a copied bridge and real prepared resources.
It publishes a second validated macro set while retaining the first archive.
Exports requested with the first identity retain its exact macro and stmaryrd
contents. Checks with the second identity detect the changed input; a new
export includes the second set. An unavailable identity returns `InvalidAssets`.
Every backend request in this case runs in a network namespace.

The installation scenario also opens, saves, and exports through the installed
interpreter with a fresh derived cache and networking disabled. It checks the
installed archive and reads the exported package to compare both renderer inputs.
These bridge checks do not establish native rendering or release timing budgets.

The release installed at the desktop entry also passes the native scenario with
`--entry ~/.local/share/applications/dev.math.flashcards.desktop --offline`.
The app and its children run inside the network namespace. Native keyboard input
changes a card answer and saves it to the disposable workspace. The scenario
exports an APKG, moves a card, and restores the saved workspace after restart.
`native-front.png` shows rendered mathematics; the `native-` screenshots record
the remaining states. This scenario uses a fresh cache but does not measure the
release timing distributions or prove input latency during full-corpus checks.
Offline native runs also write `native-offline.trace` across the initial launch
and restart. The scenario checks that the app starts the prepared interpreter,
attempts neither `uv` nor Git, and makes no remote connection. The inspected
trace contains local Python and Pandoc execution and no Internet socket family.

## Workspace search

The browser scenario creates an unopened deck and finds it by text present only
in its answer. Changing the card ID before selecting that result produces a
specific stale-card error. After the watcher publishes the current source,
the search result opens the current card without modifying its file.
`workspace-search.png` records the selected result.

The progressive startup scenario opens search before the corpus reads finish.
An unmatched query reports incomplete search coverage. It then selects, edits,
and saves a deck while workspace checks remain incomplete.

Search summaries and their exact source text persist in the derived database.
The parser key covers the card parser, search producer, resolved Pandoc parser,
and dependency data; the backend also keys stored records by their schema.
Reads and publication both compare current file bytes with the requested digest.
The focused backend case verifies reuse in another process, changed producer
keys, a damaged row, and a same-size source edit with preserved nanosecond mtime.
The browser warm-start case verifies a `ready` search response for the stored
source. The shared rebuild case regenerates search and Problems data while
retaining authored files, package bytes, and successful build provenance.
Manifest publication prunes search and Problems rows for paths that are no
longer members of the workspace. A real organization-and-reconciliation case
verifies removal of the old path from both tables after a deck rename.
