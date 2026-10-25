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
