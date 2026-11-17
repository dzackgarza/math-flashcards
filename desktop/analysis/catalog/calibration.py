"""Compare scheduler predictions with self-graded recall; research.md R17."""

import sqlite3

from analysis import Analysis, AnalysisTable, Column

title = "Calibration"
summary = "Predicted recall and self-graded recall from review grades, grouped in probability bands."


def run(connection: sqlite3.Connection) -> AnalysisTable:
    rows = connection.execute("""
        with observations as (
            select min(9, cast(before_retrievability * 10 as integer)) as band,
                   before_retrievability, grade
            from review
            where kind = 'review' and grade is not null and undone_at_ms is null
        )
        select case when band is null then 'Not recorded'
                    else printf('%.1f–%.1f', band / 10.0, (band + 1) / 10.0) end,
               count(*), avg(before_retrievability), avg(grade != 'again')
        from observations group by band order by band
    """).fetchall()
    return AnalysisTable(
        analysis=Analysis(name="calibration", title=title, summary=summary),
        columns=[
            Column(name="Predicted recall band"),
            Column(name="Self-graded reviews"),
            Column(name="Mean predicted recall", unit="probability"),
            Column(name="Self-graded recall", unit="proportion"),
        ],
        rows=[list(row) for row in rows],
    )
