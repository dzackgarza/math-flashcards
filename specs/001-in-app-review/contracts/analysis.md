# Contract: Analysis

An analysis is one computation over the learning record that gives the user a result
about their learning. Analyses are the part of the app that changes most often: the user
and their agents add, change, and remove them for the whole life of the project. This
contract keeps each such change away from the core and from the learning data
(constitution, principle IX; R17 of `research.md`). Value types are defined in
[data-model.md](../data-model.md). The input of every analysis is defined in
[learning-record.md](./learning-record.md).

## One analysis

| Rule | Detail |
| --- | --- |
| Unit | One Python module in `desktop/analysis/catalog/`. The module name is the analysis name. |
| Declares | A title and a summary for the list, and one function from a read-only connection to the record to an `AnalysisTable`. |
| Input | The learning record, and nothing else. An analysis does not read Anki's collection, the workspace, or another analysis. |
| Output | An `AnalysisTable`: named columns, each with a unit or none, and rows of text, numbers, and empty cells. |
| Computes from history | Each result is computed from the rows of the record at the time of the run. An analysis keeps no permanent data. |
| Stands alone | An analysis imports no other analysis, no part of the core (`desktop/study/`), no `anki`, and not the entry script. |
| Added by | One new module and its test. No list, no core file, no schema, and no interface file changes. |
| Removed by | Removal of its module and its test. |

## Access to the record

| Rule | Detail |
| --- | --- |
| Connection | The analysis package opens the record with `sqlite3.connect("file:<path>?mode=ro", uri=True)` and gives that connection to the analysis. |
| Path | The window sends the record path that `study-open` returned. The package accepts a file named `record.sqlite3` under `user_data_path("math-flashcards")/study/` and rejects every other path. |
| While the host writes | The analysis reads the rows committed before its read. The host is not blocked. |
| Missing fact | When the record does not hold a fact that an analysis needs, the analysis is not written against a guess. The core starts to record the fact (an added table or nullable column), and the analysis covers the time from then on. |

## Actions

Each action runs in a new process, as the bridge actions of the editor. No action
reaches the study host.

| Action | Request fields | Result | Learning record |
| --- | --- | --- | --- |
| `analysis-list` | | `Analysis[]`, in the order of their titles | Not read |
| `analysis-run` | `record: str`, `name: str` | `AnalysisTable` | Read-only |

## Errors

| Kind | Meaning | What the window shows |
| --- | --- | --- |
| `UnknownAnalysis` | The catalog has no module of that name. | The error; the list refreshes. |
| `AnalysisFailed` | The analysis raised an error. | The error text, for that analysis. Study and the other analyses work. |
| `RecordUnreadable` | The path is not a record of this app, or the file does not open. | The error, with the path. |

A module of the catalog that fails to import is in the list with its name and its
`failure`. The other analyses are listed and run.

## The first analyses

| Name | Result |
| --- | --- |
| `recall_by_folder` | For each folder and month: the number of presentations, the share graded Again, and the mean time to reveal, without undone grades. |
| `calibration` | For review presentations, in bands of the scheduler's predicted recall: the number of grades, the mean predicted recall, and the share recalled. |

## Window

| Element | Contract |
| --- | --- |
| Entry | **Statistics** in the workspace menu and in the Ctrl-K commands. |
| List | Each analysis with its title and summary. |
| Result | The table of the selected analysis, with its column names and units. One renderer shows every `AnalysisTable`. |
| During study | Statistics opens while a session is in progress. The session continues. |
| Failure | The failure of an analysis shows in place of its table. |

## Boundary checks

| Check | Where |
| --- | --- |
| The analysis package imports neither the core, nor `anki`, nor the entry script; the core does not import the analysis package; no module of the catalog imports another | Import Linter contracts in `desktop/.importlinter`, run by `just test-commit` |
| Every row of the record is equal before and after each analysis of the catalog runs | The study scenario |
| A statement that writes, sent through the connection of an analysis, fails | The study scenario |
| Each analysis of the catalog runs on the committed first-version record | The fixture step of the study scenario |
