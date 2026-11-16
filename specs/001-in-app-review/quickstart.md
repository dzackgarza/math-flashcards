# Quickstart: Validate In-App Review

These scenarios prove the feature through the real window, the real bridge, and a real
store. Values and actions are defined in [data-model.md](./data-model.md),
[contracts/study-bridge.md](./contracts/study-bridge.md),
[contracts/learning-record.md](./contracts/learning-record.md), and
[contracts/analysis.md](./contracts/analysis.md). The scenario reads the
learning record with Python's `sqlite3`, with no part of the app and no part of Anki.

## Prerequisites

- `just desktop-dependencies` has run. It installs the bridge environment, which includes
  the `anki` wheel after this feature.
- Every command below uses a temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME` and a copy of
  deck files in a temporary workspace. A run without the data override writes to the
  real review history.

## Automated scenario

```bash
just desktop-study-test
```

The recipe starts `just desktop-web` and runs `desktop/tests/study.py` against it in a
browser. `just test-commit` includes it.

| Step | Expected result |
| --- | --- |
| Open a workspace of fixture decks that was never studied | The tree shows a new count on each deck and folder; no learning or review count. The store directory has `store.json` and `record.sqlite3`. The record has a `card_change` row and a `content` row for each card. |
| Select **Study** on the workspace | The front of one card shows. The back and the grades are hidden. The record has one `session` row and one `presentation` row. |
| Wait 2 s, then press Space | The back shows. Four grades show, each with an interval label. |
| Wait 1 s, then press 3 | The next card shows. The store has one review log row. The card's stored interval agrees with the label that Good showed. |
| Read the `review` view | The first row has every field of FR-028: time and offset, card ID, deck path, folder, deck title, tags, the front and back shown, session and position, kind, scheduler day, `reveal_ms` within 100 ms of 2000, `grade_ms` within 100 ms of 1000, grade, four offered intervals, state before and after, target recall, parameter set, and writer. Its `revlog_*` values equal the store's review log row. |
| Read the record with a second `sqlite3` connection while the app runs, then grade a card | The connection reads every row. The grade succeeds. |
| Press Ctrl-Z | The first card returns. The store has no review log row. The record still has the `response` row, has an `undo` row that refers to it, and has a new `presentation` row for the returned card. |
| With a card on screen, take the focus from the window for 2 s, then reveal and grade | `unfocused_ms` is within 100 ms of 2000. |
| Advance the page clock by 3 hours between the reveal and the grade | `grade_ms` is the full time. `revlog_time_ms` is Anki's limited value. |
| Press Escape with a card on screen | The `presentation` row has no `response` row. The session has a `session_end` row with cause `left`. |
| Run the four queries of `contracts/learning-record.md` | Each gives the numbers that the grades of the scenario imply. |
| Compare the record's schema with `docs/study-record.md` | The document names every table and every column. |
| Grade a card, then end the bridge host with `SIGKILL` | After the window's next request, the grade is in the store and in the record. The session that had no end has a `session_end` row with cause `recovered`. |
| Grade a card Again and wait for its learning delay | The same card returns in the session. |
| Study a card with a macro equation and a TikZ-cd diagram | The equation and the diagram render. A screenshot goes to `desktop/test-artifacts/`. |
| Stop the app; set several cards due today with the `anki` library; start the app | The tree shows review counts for their decks and folders. The record has one `response` row, with `recovered` set and empty times, for each review log row that the library wrote. |
| Study three due cards whose estimated recall differs | The session offers them in ascending order of `before_retrievability`. |
| Edit the back of a reviewed card in the editor and save | The store shows the new back within 10 seconds, with the same due date. The record has a `card_change` row of kind `content` and a new `content` row. |
| Study the edited card | Its two `review` rows give the earlier back and the later back. |
| Move a reviewed card to another deck by editing the files on disk | The card's Anki deck changes; its due date and review log stay. The record has a `card_change` row of kind `moved`; earlier `presentation` rows keep the earlier deck path. |
| Give a note the tag `leech` with the `anki` library, then change the card's tags in its deck | The note has the new tags and `leech`. |
| Rename a deck with reviewed cards | Each card keeps its due date. |
| Delete a reviewed card from its deck, then paste it back | The card leaves the counts, then returns with the same due date. |
| Put one `card-id` in two decks | The sync result names both decks. The note stays with the first deck. |
| Set new cards per day to 3 and study the workspace | Exactly 3 new cards are offered. The record has a `setting_change` row with the earlier and the later value. |
| Set target recall to 1.0 | The field shows its bound; the stored setting is unchanged. |
| Open a card in the editor for 2 s, then select another card | The record has one `editor_view` row for the first card with `shown_ms` within 100 ms of 2000. |
| Open **Statistics** | The two analyses are listed with their titles and summaries. |
| Run each analysis | `recall_by_folder` gives the numbers that the grades imply. The numbers of grades in the bands of `calibration` sum to the number of review grades that were not undone. |
| Dump every record row, run each analysis, and dump again | The two dumps are equal. |
| Run an analysis with a session in progress, then grade a card | The result shows. The grade is recorded. |
| With a session in progress, select **Save a copy** with a temporary directory | The directory holds a store with `store.json`, the collection, and the record. The record has a `store_event` row of kind `copied`. The next grade succeeds. |
| Stop the app; start it with an empty data directory that holds the copy; attach it | The counts and every record row equal those of the copy. |
| Replace `collection.anki2` with an unreadable file and open the workspace | The window shows the error with the store path. The file is unchanged. |
| Select **Rebuild cached data** | The store, its review log, and the record are unchanged. |
| Open the Study settings | The path of the learning record shows and is the file that the scenario reads. |
| Stop the app; rename the workspace folder; open it | The window lists the existing store with its earlier path, last use, and numbers of cards and grades. No store is created. |
| Attach the listed store | The counts and the review history are as before the rename. `store.json` lists both paths. The record has a `store_event` row of kind `attached`. |
| Open a second workspace and select a new store | A second store directory exists. The first store is unchanged. |
| Run the fit on a store with no review | The window states that the history is too small. Nothing changes. |
| Stop the app; add a dated review history with the `anki` library; start the app; run the fit | The window shows the fitted parameters and Anki's two measures for the fitted and the current set. |
| Accept the fit | The preset holds the fitted parameters. The record has a `parameter_set` row with source `fit`; a later `presentation` row refers to it. |
| Stop the app and read `backups/` | Each `.colpkg` has a copy of the record with the same time in its name; `sqlite3` opens the copy and finds the same number of rows in each table. |
| Compare every record row that the scenario read at an earlier step with the same row at the end | Each row is equal. No row is missing. |
| Open a store that holds `desktop/tests/fixtures/study/record-v1.sqlite3` | Every row equals the committed dump, and the `review` view reads it. |
| Run each analysis on `desktop/tests/fixtures/study/record-v1.sqlite3` | Each returns a table. |
| List every file that the bridge processes wrote outside the workspace | Each is under the temporary data directory or the temporary cache directory. |
| Run Anki's database check on the store | No problem is reported. |
| Generate a package for a studied deck | The package and its status are as before this feature. |

## Analysis catalog

```bash
just desktop-analysis-test
```

The recipe runs `desktop/tests/analysis.py`. The test works on a temporary copy of the
entry script and the two packages, and calls the entry script as the bridge does.

| Step | Expected result |
| --- | --- |
| List the catalog | The analyses, in the order of their titles. |
| Add one module to the temporary catalog | The list holds it. Its result is the table that it returns. The results of the earlier analyses are equal to those before. |
| Add a module that raises | Its run gives `AnalysisFailed` with the error text. The other analyses run. |
| Add a module that executes an `INSERT` | Its run gives `AnalysisFailed` that names a read-only database. Every record row is equal afterward. |
| Add a module that does not import | The list holds it with its `failure`. The other analyses are listed. |
| Run a name that the catalog does not hold | `UnknownAnalysis`. |
| Give a path outside the study data directory | `RecordUnreadable`. |

## Part boundaries

```bash
just desktop-boundaries
```

The recipe runs `desktop/tests/boundaries.py`, which runs Import Linter on `desktop/`.

| Step | Expected result |
| --- | --- |
| Check the repository | Three contracts are kept. |
| In a temporary copy, an analysis imports `study`, `anki`, or `backend` | The check fails and names the import. |
| In a temporary copy, the core imports `analysis` | The check fails and names the import. |
| In a temporary copy, one analysis imports another | The check fails and names the import. |

## Manual check on the full workspace

```bash
XDG_DATA_HOME="$(mktemp -d)" just desktop-web
```

Open `http://127.0.0.1:1420` and the repository's `decks/` folder.

| Check | Expected result | Criterion |
| --- | --- | --- |
| First preparation of all 68 decks | Progress shows; the editor stays usable. Record the time. | SC-006 |
| Reload after preparation | Counts show within 2 seconds. | SC-006 |
| Grade 20 cards | The next card is readable within 0.5 seconds after each grade. | SC-002 |
| Total of the tree's new counts | Equal to the number of cards in the decks, limited by the daily setting. | SC-006 |
| Size of `record.sqlite3` after the 20 grades | Record the bytes for each presentation. | Purpose (career time scale) |
| Open `record.sqlite3` with the `sqlite3` shell and with DuckDB while the app runs | Both read the `review` view. | SC-011 |
| **Save a copy** of the store | Progress shows. Record the time. | SC-017 |

## Native check

```bash
just desktop-native-test
```

The native scenario gains three steps. They prove what the browser scenario does not
use: the host route in `lib.rs`, the media scope, the single-instance plugin, and the
files that the web view writes.

| Step | Expected result | Criterion |
| --- | --- | --- |
| Start a session in the built window and grade a card | The store has the review log row, and the record has the `review` row. An image card shows. | SC-002 |
| Start the app a second time while it runs | The second process exits. One window exists, and it has the focus. | SC-015 |
| Run with an empty directory as `HOME` and the four XDG directories inside it; list every file under that `HOME` | Each file is under one of the four directories. | SC-016 |
| Remove the cache and state directories; start the app | Every record row is equal. The counts are as before. | SC-016 |
