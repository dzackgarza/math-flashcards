# Reading the learning record

Study keeps permanent learning facts in `record.sqlite3`. The Study screen shows
its full path. **Open learning folder** in the native app selects the file in the
file manager. The store is under the XDG data directory, normally
`~/.local/share/math-flashcards/study/<store-id>/` on Linux. The app resolves this
location through `platformdirs`.

Open the record read-only. The app can continue studying while a reader holds a
connection. For example, replace the path below with the path shown in Study:

```sh
sqlite3 -readonly '/path/to/store/record.sqlite3'
```

```sql
.headers on
.mode column
SELECT card_id, grade, front, back FROM review ORDER BY id DESC LIMIT 10;
```

The record uses SQLite's write-ahead log. Copying only the main database file
while the app runs can omit committed data still in its WAL. Use SQLite's backup
API for a live database snapshot, or close the app before copying the complete
store directory. A database snapshot alone does not contain retained media.

The core appends facts. It does not update or delete an earlier row. A correction
refers to the earlier fact; an undo does not erase the grade. A schema extension
adds tables or nullable columns and records the addition in `schema`. An analysis
reads the record and stores no permanent result here. These rules are specified in
the [learning-record contract](../specs/001-in-app-review/contracts/learning-record.md).

## Common columns

The immutable `desktop/tests/fixtures/study/record-v1.sqlite3` fixture and its
`record-v1.json` row dump were produced through the public Study host from the
native build at `98c28602f409071be8bbece5cbe21abee03126aa`. The companion
`collection-v1.anki2` holds the matching scheduling state. The fixture includes
a completed Easy review and an editor view. Never regenerate these files. The
Study scenario opens a copy through the current host, compares every historical
row with the dump, and reads the historical grade through `review`.

Every table below has these columns. Row IDs belong to their own table. Unless a
row below states otherwise, a field is required and cannot be `NULL`.

| Column | Meaning and unit |
| --- | --- |
| `id` | Integer primary key in this table. It is not a timestamp. |
| `at_ms` | Host wall-clock time when the row was inserted, milliseconds since the Unix epoch. For recovered facts this is the recovery time; `revlog_id` retains Anki's original time. |
| `utc_offset_min` | Host local UTC offset at insertion, in minutes east of UTC. |
| `writer` | Foreign key to `writer.id`, identifying the code that inserted this row. |

Times measured in the window are durations from its monotonic clock. They do not
change when the wall clock changes. Time without focus is part of the total
duration, not an amount already subtracted from it. Exposure is not proof of
attention or learning.

## Writer, schema, and store events

| Table.column | Meaning and coding |
| --- | --- |
| `writer.app_release` | Application release string. |
| `writer.anki_version` | Version of the Anki Python distribution used by this writer. |
| `writer.schema_version` | Record schema version understood by this writer. The current schema is version 2. A writer row's common `writer` column refers to itself. |
| `schema.version` | Unique integer schema version. |
| `schema.added` | Text describing the additions. Version 1 stores a JSON object from table names to their SQL field definitions. |
| `store_event.kind` | Store event name: `created`, `attached`, `backed-up`, or `copied`, as applicable to the operation. |
| `store_event.path` | Absolute workspace or destination path associated with the event. |

`store.json` beside the database contains the store UUID, creation time, and
ordered workspace attachment history. It is current store metadata, distinct
from the append-only learning record.

Version 2 adds `image_reference`. Opening a version 1 record creates this table
and appends a schema row. Existing rows remain unchanged. Reference mappings are
recorded on the next synchronization as new content versions; an empty mapping
on an older version means that context was not recorded.

## Editor views and sessions

| Table.column | Meaning, unit, and empty case |
| --- | --- |
| `editor_view.card_id` | Native `card-id` of the card displayed in the editor. |
| `editor_view.deck_path` | Markdown path relative to the workspace at that time. |
| `editor_view.shown_ms` | Total time the card remained selected, in milliseconds. |
| `editor_view.unfocused_ms` | Milliseconds during that view with the window unfocused or the document hidden. |
| `session.scope_kind` | `workspace`, `folder`, or `deck`. |
| `session.scope_path` | Relative folder or deck path. `NULL` for a workspace session. |
| `session_end.session` | Foreign key to the session that ended. |
| `session_end.cause` | `left` for leaving a session with queued cards; `finished` for an empty queue; `host-stopped` for a normal host shutdown; `recovered` when store open finds a session without an end row. |

An ungraded presentation remains in the record. A session end does not imply that
every card was graded. An unattached workspace has no store in which to record
editor views.

## Content, media, and card changes

| Table.column | Meaning and empty case |
| --- | --- |
| `content.digest` | Unique SHA-256 identity of the native front and back, rendering identity, retained media mapping, and image reference mapping. |
| `content.front` | Exact saved Markdown source of the front div body. |
| `content.back` | Exact saved Markdown source of the back div body. |
| `content.assets` | Rendering descriptor identity. Its retained file is `record-assets/<identity>.json`. |
| `media.content` | Foreign key to the content version that uses this file. |
| `media.name` | Authored image URL resolved relative to that version's source deck. |
| `media.digest` | SHA-256 of the retained bytes, stored as `record-media/<digest>`. |
| `image_reference.content` | Foreign key to the content version that uses the reference. |
| `image_reference.label` | Normalized Markdown reference label. |
| `image_reference.name` | Authored URL of the reference definition; names a `media` row for this content. |
| `card_change.card_id` | Native card identity; content edits do not change it. |
| `card_change.kind` | Change name: `added`, `content`, `tags`, `moved`, `removed`, or `restored`. |
| `card_change.from_deck` | Earlier relative deck path; `NULL` for a newly added card. |
| `card_change.to_deck` | Later relative deck path; `NULL` when removed from the workspace. |
| `card_change.content` | Foreign key to the applicable content version; nullable when no version was observed. |
| `card_change.tags` | JSON array of the tags associated with the card at the change. |

Anki notes hold scheduling identity in their GUID and sole `CardId` field. The
record holds authored source. Retained media bytes and rendering descriptors
must be copied with the record to preserve its presentation inputs. A later file
replacement or card edit does not replace an earlier content row or media file.

## Presentations

The host inserts a presentation before returning the card to the window. Each
fetch is a new presentation, including fetching the same card again. The fields
describe the offer at that moment, not the card's current mutable Anki state.

| Column in `presentation` | Meaning, unit, and empty case |
| --- | --- |
| `session` | Foreign key to the study session. |
| `position` | One-based presentation position in that session. |
| `card_id` | Native card identity. |
| `content` | Foreign key to the content version offered. |
| `deck_path` | Relative Markdown path at presentation. |
| `folder` | Relative parent folder, or the empty string for a root-level deck. |
| `deck_title` | Deck title at presentation. |
| `tags` | JSON array of the deck and card tags in effect. |
| `kind` | Anki state: `new`, `learning`, `review`, or `relearning`. |
| `scheduler_day` | Anki's integer day number, using its own day boundary. It is not a Unix day or a local calendar date. |
| `before_interval_days` | Card interval before the answer, in days. |
| `before_due` | Anki's raw due value before the answer. Its unit depends on state: new-card position, intraday learning Unix seconds, or scheduler day. |
| `before_reps` | Number of prior answers recorded on the Anki card. |
| `before_lapses` | Anki lapse count before the answer. |
| `before_stability` | FSRS stability in days; `NULL` when no memory state exists. |
| `before_difficulty` | FSRS dimensionless difficulty; `NULL` when no memory state exists. |
| `before_retrievability` | Anki's estimated recall probability from 0 to 1; `NULL` when Anki supplies none. |
| `offer_again_s` | Offered interval for Again, in seconds. |
| `offer_hard_s` | Offered interval for Hard, in seconds. |
| `offer_good_s` | Offered interval for Good, in seconds. |
| `offer_easy_s` | Offered interval for Easy, in seconds. |
| `labels` | JSON object with `again`, `hard`, `good`, and `easy` labels supplied by Anki, including its display formatting. |
| `desired_retention` | Target recall probability in effect. |
| `parameter_set` | Foreign key to the FSRS parameter set in effect. |
| `new_per_day` | Daily new-card limit in effect. |
| `reviews_per_day` | Daily review limit in effect. |

The offer fields convert Anki's review-day intervals to seconds. Learning and
relearning offers already use seconds. A new card has no prior FSRS memory state;
empty memory fields must not be interpreted as a measured value of zero.

## Responses and undo

A normal response follows Anki's committed answer operation. The two databases
do not share a transaction. On store open, the host copies any Anki review-log
row whose ID has no response. Recovery does not guess the missing presentation,
window timings, or historical after-state from the card's current state.

| Column in `response` | Meaning, unit, and empty case |
| --- | --- |
| `presentation` | Foreign key to the graded presentation; `NULL` for recovery. |
| `card_id` | Native card identity. |
| `grade` | `again`, `hard`, `good`, or `easy`. `NULL` when a recovered Anki operation has no rating, such as setting a due date. |
| `reveal_ms` | Milliseconds from showing the front to revealing the back; `NULL` for recovery. |
| `grade_ms` | Milliseconds from reveal to grade; `NULL` for recovery. |
| `unfocused_ms` | Milliseconds without focus or visibility across both intervals; `NULL` for recovery. |
| `after_interval_days` | Observed interval after Anki applies the answer, in days; `NULL` for recovery. |
| `after_due` | Observed raw Anki due value after the answer, with the state-dependent units above; `NULL` for recovery. |
| `after_stability` | Observed FSRS stability in days after the answer; `NULL` for recovery or an absent memory state. |
| `after_difficulty` | Observed FSRS dimensionless difficulty after the answer; `NULL` for recovery or an absent memory state. |
| `recovered` | Integer boolean: 0 for a normal response, 1 for recovery. |
| `revlog_id` | Unique Anki `revlog.id`, in epoch milliseconds. Anki may adjust it to distinguish operations within a millisecond. |
| `revlog_cid` | Anki numeric card ID (`cid`), distinct from the native string `card_id`. |
| `revlog_usn` | Anki update sequence number (`usn`); -1 identifies an unsynced local row. |
| `revlog_ease` | Anki `ease`: 1 Again, 2 Hard, 3 Good, 4 Easy; 0 for an unrated manual operation. |
| `revlog_ivl` | Anki resulting `ivl`: positive values are days; negative values encode seconds by their absolute value. |
| `revlog_last_ivl` | Anki previous `lastIvl`, with the same signed-unit convention. |
| `revlog_factor` | Raw Anki `factor`. Its interpretation depends on the scheduler and row type; retain it as recorded rather than treating it as an app-defined measure. |
| `revlog_time_ms` | Anki's stored answer time in milliseconds. It can be capped even when the window's duration is longer. |
| `revlog_type` | Raw Anki review kind: 0 learning, 1 review, 2 relearning, 3 filtered, 4 manual, 5 rescheduled. Use the row's recorded Anki version when interpreting it. |
| `undo.response` | Foreign key to the response that was undone. The undo row's common timestamp gives when it was undone. |

The nine `revlog_*` values preserve Anki's row without conversion. The two window
durations preserve the full observed time. They serve different questions.
Anki defines the raw review kinds in
[`RevlogReviewKind`](https://github.com/ankitects/anki/blob/main/rslib/src/revlog/mod.rs).

## Settings and parameter sets

| Table.column | Meaning and empty case |
| --- | --- |
| `setting_change.key` | Name of the changed setting. |
| `setting_change.before` | JSON text for its earlier value. |
| `setting_change.after` | JSON text for its later value. |
| `parameter_set.parameters` | JSON array of FSRS weights in Anki's order. |
| `parameter_set.source` | `anki-default` for the initial weights or `fit` for an accepted fitted set. |
| `parameter_set.reviews` | Number of reviews used for a fit; `NULL` for initial defaults. |
| `parameter_set.log_loss` | Anki's log-loss fit measure; `NULL` when no fit was evaluated. |
| `parameter_set.rmse_bins` | Anki's binned root-mean-square-error measure; `NULL` when no fit was evaluated. |

## The `review` view

`review` joins each presentation to its content, response, and undo. It retains
all presentation columns, including their common columns. It also exposes:

| View column | Source or empty case |
| --- | --- |
| `front`, `back`, `assets` | The presentation's content row. |
| `response` | Response row ID, or `NULL` when ungraded. |
| `responded_at_ms` | Response insertion time, or `NULL` when ungraded. |
| `response_utc_offset_min` | Response UTC offset, or `NULL` when ungraded. |
| `response_writer` | Response writer ID, or `NULL` when ungraded. |
| `grade`, `reveal_ms`, `grade_ms`, `unfocused_ms` | Response fields, or `NULL` when ungraded. |
| `after_interval_days`, `after_due`, `after_stability`, `after_difficulty` | Response after-state fields, or `NULL` when ungraded or unobserved. |
| `recovered` and every `revlog_*` column | Response values, or `NULL` when ungraded. |
| `undone_at_ms` | Undo insertion time, or `NULL` when no undo refers to the response. |

Recovered responses have no presentation and therefore do not appear in this
view. Query `response` to include them. The view's `id`, `at_ms`,
`utc_offset_min`, and `writer` always refer to the presentation.

## Example queries

These measure self-graded card recall. They do not measure mastery of a subject.
SQLite aggregates ignore `NULL`; an ungraded presentation contributes to the
presentation count but not to the share of grades or mean reveal time.

```sql
-- Presentations, self-graded Again share, and mean reveal time by folder/month.
SELECT folder, strftime('%Y-%m', at_ms / 1000, 'unixepoch') AS month,
       count(*) AS presentations, avg(grade = 'again') AS share_again,
       avg(reveal_ms) AS mean_reveal_ms
FROM review WHERE undone_at_ms IS NULL GROUP BY folder, month;

-- The same measures by tag.
SELECT tag.value AS tag, count(*) AS presentations,
       avg(grade = 'again') AS share_again, avg(reveal_ms) AS mean_reveal_ms
FROM review, json_each(review.tags) AS tag
WHERE undone_at_ms IS NULL GROUP BY tag.value;

-- Historical authored source for one native card ID.
SELECT at_ms, grade, front, back FROM review
WHERE card_id = 'study-absolute-value' ORDER BY at_ms;

-- Predicted recall against the self-assigned grade, for review-state cards.
SELECT before_retrievability, grade != 'again' AS self_graded_recall
FROM review
WHERE kind = 'review' AND grade IS NOT NULL AND undone_at_ms IS NULL;
```

## Relation to the research data format

The [anki-revlogs-10k dataset](https://huggingface.co/datasets/open-spaced-repetition/anki-revlogs-10k)
provides a comparison format for scheduling research. Its duration is capped;
the app's measured durations are not. See the source assessment in
[research R12](../specs/001-in-app-review/research.md#r12-learning-record).

| Dataset field | Derivation from this record |
| --- | --- |
| `card_id` | Native `card_id`; retain a separate mapping if numeric IDs are required. |
| `rating` | `again` → 1, `hard` → 2, `good` → 3, `easy` → 4. |
| `state` | `new` → 0, `learning` → 1, `review` → 2, `relearning` → 3. |
| `duration` | `reveal_ms + grade_ms` for the full measured time, or `revlog_time_ms` when the analysis specifically requires Anki's capped measure. Name the choice. |
| `day_offset` | `scheduler_day` minus the first scheduler day in the selected history. |
| `elapsed_days` | Difference from the preceding non-undone graded presentation of the same card in scheduler days. |
| `elapsed_seconds` | Difference between those presentation `at_ms` values divided by 1000. |
| Card/deck/parent relationships | `card_id`, historical `deck_path`, and `folder` at each presentation. |

A recovered response lacks the presentation facts needed for some of these
derivations. Keep those values empty or define a separate analysis of Anki's raw
rows. Do not silently manufacture a complete presentation from current card data.
