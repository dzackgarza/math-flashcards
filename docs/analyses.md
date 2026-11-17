# Analyses of the learning record

An analysis computes a result from recorded learning. It reads `record.sqlite3`
and returns a table for **Statistics**. It has no permanent data and changes no
stored row. The [field reference](study-record.md) gives the meaning, unit, and
empty case of each field. The [analysis contract](../specs/001-in-app-review/contracts/analysis.md)
defines the interface and its errors.

Each analysis is one module under `desktop/analysis/catalog/`. It declares
`title`, `summary`, and `run(connection)`. The package discovers modules with
Python's `pkgutil`; adding an analysis needs its module and test, with no change
to the core, schema, catalog list, or window renderer.

For example, `presentation_count.py` can contain:

```python
import sqlite3

from analysis import Analysis, AnalysisTable, Column

title = "Presentation count"
summary = "The number of retained card presentations."


def run(connection: sqlite3.Connection) -> AnalysisTable:
    count = connection.execute("select count(*) from presentation").fetchone()[0]
    return AnalysisTable(
        analysis=Analysis(name="presentation_count", title=title, summary=summary),
        columns=[Column(name="Presentations")],
        rows=[[count]],
    )
```

The analysis name is its module name. Column units are optional. Cells contain
text, integers, finite numbers, or `None` for an unobserved value. Each row has one
cell per column. Statistics displays missing values as a dash, not zero.

The input connection is opened with SQLite's `mode=ro`. A read transaction gives
the analysis a consistent snapshot while the Study host writes later learning
events. The accepted path is a file named `record.sqlite3` inside the app's XDG
data directory under `math-flashcards/study/`; resolved paths outside it fail.
These rules govern access through the supplied connection. Analysis modules are
trusted local code, not a sandbox for arbitrary programs.

An analysis imports neither `study`, `anki`, the backend entry script, nor another
catalog module. It reads neither the workspace nor Anki's collection. Import Linter
checks these module boundaries. A missing fact calls for a core change that starts
recording that fact in an added table or nullable column. It never calls for an
analysis that writes or invents historical values.

Measures derived from grades must say **self-graded** in their summaries and
column labels. Results grouped by subject describe recall of those cards. They
do not establish mastery of that subject. Explain the population and observation
limits of any further learning claim in the maintained research register.

The folder analysis includes ungraded presentations in its presentation count.
SQLite excludes their missing grades and times from the averages. Undone grades
are excluded. Calibration groups review grades in probability bands of width 0.1;
the last band includes 1.0. A missing prediction remains in a **Not recorded**
band, with a missing mean prediction. This keeps its observed grade count without
inventing a probability.

Test through `analysis-list` and `analysis-run` at `desktop/backend.py`, using a
temporary XDG data directory. Check the mathematical result against the record,
unchanged record rows, and the retained first-version fixture. The
`desktop/tests/analysis.py` scenario also demonstrates that adding a module leaves
earlier results unchanged and that import, calculation, and write failures remain
isolated. `just desktop-analysis-test` runs this focused interface check.

Each bridge analysis request retains a diagnostic log and nested Python timing
profile under the app's XDG state directory. Its context records source hashes,
Python and Anki versions, and the input digest. The one-process entry does not
receive an application release identifier, so that field is empty. These files
are diagnostics and may be removed without losing learning data.
