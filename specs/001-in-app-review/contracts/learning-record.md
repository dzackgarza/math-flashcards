# Contract: Learning Record

The learning record is the interface between the core, which writes it, and everything
that analyses it. The reader is the user, with SQL, pandas, R, or DuckDB, and the
analysis part of this app ([analysis.md](./analysis.md)). The
tables and fields are defined in [data-model.md](../data-model.md). The field reference
for the user is `docs/study-record.md`.

## Location and access

| Rule | Detail |
| --- | --- |
| File | `record.sqlite3` in the store directory. The app shows the path in the Study settings (FR-042). |
| Format | SQLite 3, with the write-ahead log. No extension, no encryption, no compression. |
| Reader | Any SQLite client. A reader opens the file read-only. A reader needs no part of this app and no part of Anki (FR-037). |
| While the app runs | A reader sees every committed row. The app keeps working. |
| Writer | The study host only. It inserts rows. It has no statement that updates or deletes a row (FR-031). |
| Copy | **Save a copy** in the Study settings writes a complete copy of the store, with the record, to a directory that the user chose, while the app runs (FR-050). A copy of the store directory made while the app is stopped is also complete. The backups in `backups/` are complete copies of the record made while the app runs (FR-040). |
| Facts, not results | The record holds what the app observed. It holds no result of an analysis. A change to an analysis changes no row and no table (FR-054). |
| Network | No part of the record leaves the machine through the app (FR-043). |

## Guarantees to a reader

1. **Complete.** Each card that the window showed is one `presentation` row. Each grade
   is one `response` row. Each grade in Anki's review log has a `response` row with
   Anki's nine values (FR-036). Each time a card was open in the editor is one
   `editor_view` row (FR-058).
2. **Permanent.** A row, once committed, never changes and never disappears. An undo is
   an `undo` row; the undone `response` row stays.
3. **Self-contained.** Each `presentation` row holds the deck path, folder, deck title,
   and tags of that moment as values (the union of the deck tags, the card tags, and
   the tags that the scheduler set, such as `leech`), and refers to a `content` row with the front and
   back source shown, the retained rendering assets, and the recorded media mapping.
   A later edit, move, or removal of the card does not change them.
4. **Empty means not observed.** A field that the app could not observe is `NULL`, never
   zero and never a default. `docs/study-record.md` states, for each field, when it is
   empty.
5. **Measured times.** `reveal_ms`, `grade_ms`, and `unfocused_ms` are the measured
   values. `revlog_time_ms` is Anki's value, which Anki limits.
6. **Stable schema.** A later release adds tables and nullable columns. It does not
   remove, rename, or change the meaning or the unit of a table or column. The `schema`
   table lists each version and what it added. A query written against one release gives
   the same result for the same rows under each later release (FR-039).
7. **Attributed.** Each row names the `writer`: the app release, the Anki version, and
   the schema version (FR-035).

## The `review` view

One row for each presentation, for the common case of analysis. Columns: every column of
`presentation`; the columns of its `response`, empty when the card was not graded;
`undone_at_ms`, empty when the grade was not undone; `front` and `back` of its content.

A recovered `response` row has no presentation and is not in the view. It is in the
`response` table with `recovered` set.

## Research format

The record derives the columns of the public research data set
`open-spaced-repetition/anki-revlogs-10k`. `docs/study-record.md` owns the mapping.

| Data set column | From the record |
| --- | --- |
| `card_id` | `card_id` |
| `rating` (1 to 4) | `grade` (again, hard, good, easy) |
| `state` (0 to 3) | `kind` (new, learning, review, relearning) |
| `duration` | `reveal_ms + grade_ms`, with no limit |
| `day_offset` | `scheduler_day` minus the first `scheduler_day` of the record |
| `elapsed_days`, `elapsed_seconds` | Difference to the earlier graded presentation of the card, in `scheduler_day` and in `at_ms` |

## Queries that the record must answer

Each is checked by the test scenario with Python's `sqlite3` (SC-011, SC-012, SC-014).

```sql
-- Presentations, share graded Again, and mean time to reveal, by folder and month.
SELECT folder,
       strftime('%Y-%m', at_ms / 1000, 'unixepoch') AS month,
       count(*) AS presentations,
       avg(grade = 'again') AS share_again,
       avg(reveal_ms) AS mean_reveal_ms
FROM review
WHERE undone_at_ms IS NULL
GROUP BY folder, month;

-- The same by tag.
SELECT tag.value AS tag, count(*), avg(grade = 'again'), avg(reveal_ms)
FROM review, json_each(review.tags) AS tag
WHERE undone_at_ms IS NULL
GROUP BY tag.value;

-- What one card showed at each of its reviews.
SELECT at_ms, grade, front, back FROM review WHERE card_id = ? ORDER BY at_ms;

-- The scheduler's prediction against the result, for calibration.
SELECT before_retrievability, grade != 'again' AS recalled
FROM review
WHERE kind = 'review' AND grade IS NOT NULL AND undone_at_ms IS NULL;
```
