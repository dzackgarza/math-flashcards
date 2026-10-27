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

## Historical package checks

The package-history API returns Pending with the prior checked value. It reads
the derived database without hashing packages or reading deck sources.
Fresh checks compute a digest over the current input hashes, package bytes,
and build-record identity. Their check time is metadata, not a validity key.

The offline backend case changes actual package bytes between requests. A
history read still returns Pending; fresh verification detects the edit and
changes the input identity while retaining the source revision.
The browser warm-start scenario observes real tree attributes with a DOM
MutationObserver. It verifies that prior statuses appear as Pending or Checking
before the row becomes Ready. Cache failures remain separate from verified
package results, with an explicit rebuild action.
The backend case also moves the bridge resources and changes the copied Lua
filter while retaining the old resource. Verification detects producer paths
absent from the build record. The damaged-cache browser case rebuilds package
history together with search and Problems data.

## Watcher invalidation

Fresh package results include their file dependencies. The watcher coalesces
paths and derives separate source-read and package-check sets. Pending source
reads survive superseding refreshes; failed paths wait for a relevant change or
manual retry. Unchanged document reads retain build history while checks run.

The real browser scenario edits one deck and verifies that source and package
requests name only that deck. It then exports two decks with a shared image
symlink, changes the link target, and verifies that only the dependent packages
are checked. Their sources are not reread. Media resolution validates the target
inside the workspace and records the referenced path so link changes remain
visible to hashing and watches. `media-invalidation.png` records the result.

The bridge reports missing runtime modules as an incomplete installation and
names `just desktop-install`. A focused case executes the real bridge with site
packages disabled and checks that diagnostic.

## Versioned installation

The installer prepares and validates each release at its final path. Its Python
environment belongs to that release. One active symlink selects the executable,
resources, and environment together. A separate asset-version descriptor lets
an older process detect an update while retaining its own assets.

The installation scenario verifies a failed real dependency fetch with networking
disabled. The active pointer, launcher, runtime marker, renderer file, and desktop
entry remain unchanged; the candidate directory is removed through trash. The
active installation still opens its workspace offline. Reinstalling identical
producer content preserves package freshness across different release paths.

A successful update then supplies a changed validated macro set. The old runtime
reports the new active version while its own asset request retains the original
set. Offline exports through the old and new runtimes contain their respective
exact macro and stmaryrd contents.

`just desktop-update-test` passes with the release frontend at `f8131d1`. It
launches a temporary installation through its desktop entry with networking
disabled. The running window renders the restart notice after activation of a
changed asset set. It still edits, saves, and exports with its original complete
macro/stmaryrd pair. The restarted window exports the new complete pair.
`native-update-notice.png` and `native-updated-session.png` record the inspected
states. The trace covers each launch and contains no updater execution or remote
connection. These observations do not establish the timing budgets.

The native input scenario waits for a rendered package status before invoking
export. Tesseract reads the actual window pixels. The package assertions compare
the complete macro set and stmaryrd contents with the expected release resources.

## Response ownership

The browser scenario delays delivery of real backend responses. A late review
cannot replace a newer review of the same deck. A build-all review delivered
after a workspace switch starts no export. A missing-file response for a deleted
previous deck cannot close the newer editor. Review, generation, action errors,
and disk-follow errors retain their originating session or document identity.

## Release timing baseline

The release frontend at `f8131d1` has a complete repeated baseline on the
workstation's isolated X11 display. The fixture copies the repository workspace,
including its packages. Warm launches follow a completed analysis. Cold launches
rebuild only the derived cache. Every keyboard sample runs during incomplete
workspace checks.

| Cache | Samples | Tree publication p95 / worst (s) | Selection p95 / worst (s) | Key command to glyph p95 / worst (s) |
| --- | --- | --- | --- | --- |
| Warm | 20 | 1.326 / 1.385 | 2.041 / 2.136 | 0.124 / 0.128 |
| Cold | 20 | 1.893 / 2.319 | 1.987 / 2.360 | 0.133 / 0.142 |

The initial complete analysis takes 44.659 seconds. The p95 calculation uses the
nearest rank. Raw samples are in `desktop/test-artifacts/native-timings-baseline.json`.

WebKitWebDriver controls the real release WebView through Tauri's supported
automation interface. Tree publication and selection durations include driver command and
observation time. Selection ends when the selected field is editable and its
MathJax content exists. The keyboard duration starts before native key command
submission and ends when the glyph interior changes in an X11 screen capture.
The test also checks that the editor contains the expected character and restores
the original source. This keyboard upper bound includes input-tool overhead.

The baseline tree endpoint observes populated rows; the final usable-tree
measurement must also require navigation to be enabled. The timing harness now
checks that the loading indicator has cleared before selecting a deck.

The warm tree publication, selection, and keyboard observations exceed the plan's budgets.
Profile application work and measurement overhead before changing the critical
path. The current installed revision and final rendering endpoint still need
their acceptance distributions. These baseline values do not close task F.

The native selection profile identifies synchronous card summaries as a major
part of the selection path. The captured stack maps to `previewHtml` in
`src/math.ts`, called for every card by `App.tsx` before the editor is published.
The shared field editor has a separate stack.

Card summaries now render one card per task after the selected deck is
published. The tree keeps its data identity while membership is unchanged, so
a folder opened between cached and reconciled publication stays open. The
release built from `3833e78`'s frontend, measured on an otherwise idle
workstation, gives this distribution:

| Cache | Samples | Tree publication p95 / worst (s) | Selection p95 / worst (s) | Key command to glyph p95 / worst (s) |
| --- | --- | --- | --- | --- |
| Warm | 20 | 1.161 / 1.282 | 0.870 / 0.896 | 0.156 / 0.161 |
| Cold | 20 | 1.476 / 1.589 | 0.899 / 0.930 | 0.169 / 0.182 |

Selection meets its budget. Warm tree publication and keyboard paint do not.
The timing run also reads an in-page `flashcards:tree-published` mark and the
interval from keydown to the second following animation frame, to separate page
work from driver and input-tool overhead. A run under external load (load
average above 14) is not an acceptance sample.

| Conversion owner | Warm calls | Warm CPU (s) | Cold calls | Cold CPU (s) |
| --- | --- | --- | --- | --- |
| Card summaries | 106 | 0.736 | 106 | 0.849 |
| Selected field editor | 2 | 0.013 | 2 | 0.013 |

These durations cover actual MathJax conversion calls and exclude Markdown
parsing, stylesheet updates, backend time, and driver overhead. Raw stacks are
in `desktop/test-artifacts/native-profile.json`. Summary conversion must yield
outside the selected editor's initial render; complete summaries remain required.

## Completed release timing verification (2026-10-27)

The release under test has the shared CodeMirror editor in a local on-demand
chunk. The tree publishes before that chunk is imported, and it requests the
chunk after the tree paints. Search, Problems, and mathematical card summaries
retain complete coverage and run on cooperative idle turns; typing briefly
defers those computations instead of cancelling them. Fast navigation does not
stand in for completed background work.

The native test now separates application time from test-driver overhead:

- Launch-to-tree is measured from the OS native process creation to a mark
  after the populated, enabled tree's second animation frame. Reconciliation
  with unchanged manifest membership cannot cancel that mark.
- Selection starts on the actual deck click event and ends after the editor is
  contenteditable, a MathJax container exists, and two animation frames pass.
- Keyboard latency starts on the actual `keydown` event and ends on the
  observed pixel change in the isolated native window. The harness separately
  records command-submission and WebDriver observation upper bounds.
- Each condition has 20 release launches, with the actual corpus and packages.
  Keyboard samples occur while workspace checks remain incomplete. The test
  verifies undo and byte-for-byte restoration after every keystroke.

| Condition | Usable tree p95 / worst | Selected editor p95 / worst | Key paint p95 / worst |
| --- | --- | --- | --- |
| Warm derived cache | 0.988 / 1.075 s | 0.660 / 0.748 s | 95.8 / 96.5 ms |
| Cold derived cache | 1.363 / 1.607 s | 0.815 / 0.868 s | 93.9 / 95.2 ms |

All release p95 targets in the responsive-startup plan pass, including the
100 ms keyboard target. The load average recorded at completion was
3.54 / 2.52 / 2.36; the initial complete background analysis required
65.342 s. The time to complete analysis is not substituted for tree usability.
Raw samples, p95 calculations, worst cases, and separate driver/page timings
are in `desktop/test-artifacts/native-timings.json`. Those artifacts are
generated by the native test and are not a substitute for rerunning it on a
changed installed binary.

## Final release startup and native input acceptance (2026-10-27)

The current release was rebuilt after resolving dropped rapid edits, stale
response ownership, and main-thread competition from mathematical summaries,
search parsing, and Problems checking. Background computations now yield to
foreground input and resume during idle periods.

Twenty warm and twenty cold launches of the real Tauri release were observed
with the full deck corpus and package fixture; every sampled input occurred
while background checks were incomplete. Durations measure the native process
start to a usable painted navigation tree, the real deck click to an editable
rendered field, and the real keydown to visible glyph pixels. Driver command
round trips remain separately recorded and are not substituted for product
latency. Nearest-rank p95 values are seconds.

| Cache | Runs | Tree p95 / worst | Selection p95 / worst | Input paint p95 / worst | Driver tree p95 | Driver input p95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Warm | 20 | 0.988 / 1.075 | 0.660 / 0.748 | 0.096 / 0.096 | 0.994 | 0.110 |
| Cold | 20 | 1.363 / 1.607 | 0.815 / 0.868 | 0.094 / 0.095 | 1.423 | 0.097 |

These measurements satisfy the startup plan's p95 budgets: warm tree at
most 1 s, cold tree at most 2 s, selection at most 1 s and native input paint
at most 0.100 s. Raw individual observations, page markers, and load average
are retained in `desktop/test-artifacts/native-timings.json`. The measurement
assertion continues to fail on any missed budget.
