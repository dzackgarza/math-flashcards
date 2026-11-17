"""Folder/month query in contracts/learning-record.md; no subject-mastery inference."""

import sqlite3

from analysis import Analysis, AnalysisTable, Column

title = "Recall by folder"
summary = "Presentations, self-graded Again share, and reveal time for recall of the cards in each folder and month."


def run(connection: sqlite3.Connection) -> AnalysisTable:
    rows = connection.execute("""
        select folder, strftime('%Y-%m', at_ms / 1000, 'unixepoch') as month,
               count(*), avg(grade = 'again'), avg(reveal_ms)
        from review where undone_at_ms is null
        group by folder, month order by folder, month
    """).fetchall()
    return AnalysisTable(
        analysis=Analysis(name="recall_by_folder", title=title, summary=summary),
        columns=[
            Column(name="Folder"),
            Column(name="Month", unit="UTC"),
            Column(name="Presentations"),
            Column(name="Self-graded Again share", unit="proportion"),
            Column(name="Mean time to reveal", unit="ms"),
        ],
        rows=[list(row) for row in rows],
    )
