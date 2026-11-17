"""Permanent learning facts; see R12 and contracts/learning-record.md.

The xAPI statement model supplies permanence and correction semantics. SQLite owns
transactions, concurrent reads, and backups: https://www.sqlite.org/wal.html
"""

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from time import time_ns
from typing import Literal

from study.values import Value

type RecordScalar = str | int | float | None

COMMON = "id integer primary key, at_ms integer not null, utc_offset_min integer not null, writer integer not null references writer(id)"
TABLES = {
    "writer": "app_release text not null, anki_version text not null, schema_version integer not null",
    "schema": "version integer not null unique, added text not null",
    "store_event": "kind text not null, path text not null",
    "editor_view": "card_id text not null, deck_path text not null, shown_ms integer not null, unfocused_ms integer not null",
    "session": "scope_kind text not null, scope_path text",
    "session_end": "session integer not null references session(id), cause text not null",
    "content": "digest text not null unique, front text not null, back text not null, assets text not null",
    "media": "content integer not null references content(id), name text not null, digest text not null",
    "card_change": "card_id text not null, kind text not null, from_deck text, to_deck text, content integer references content(id), tags text not null",
    "presentation": """session integer not null references session(id), position integer not null,
        card_id text not null, content integer not null references content(id), deck_path text not null,
        folder text not null, deck_title text not null, tags text not null, kind text not null,
        scheduler_day integer not null, before_interval_days integer not null, before_due integer not null,
        before_reps integer not null, before_lapses integer not null, before_stability real,
        before_difficulty real, before_retrievability real, offer_again_s integer not null,
        offer_hard_s integer not null, offer_good_s integer not null, offer_easy_s integer not null,
        labels text not null, desired_retention real not null,
        parameter_set integer not null references parameter_set(id),
        new_per_day integer not null, reviews_per_day integer not null""",
    "response": """presentation integer references presentation(id), card_id text not null,
        grade text, reveal_ms integer, grade_ms integer, unfocused_ms integer,
        after_interval_days integer, after_due integer, after_stability real, after_difficulty real,
        recovered integer not null, revlog_id integer not null unique,
        revlog_cid integer not null, revlog_usn integer not null, revlog_ease integer not null,
        revlog_ivl integer not null, revlog_last_ivl integer not null, revlog_factor integer not null,
        revlog_time_ms integer not null, revlog_type integer not null""",
    "undo": "response integer not null references response(id)",
    "setting_change": 'key text not null, "before" text not null, "after" text not null',
    "parameter_set": "parameters text not null, source text not null, reviews integer, log_loss real, rmse_bins real",
}

IMAGE_REFERENCE = "content integer not null references content(id), label text not null, name text not null"


class Presentation(Value):
    session: int
    position: int
    card_id: str
    content: int
    deck_path: str
    folder: str
    deck_title: str
    tags: str
    kind: Literal["new", "learning", "review", "relearning"]
    scheduler_day: int
    before_interval_days: int
    before_due: int
    before_reps: int
    before_lapses: int
    before_stability: float | None
    before_difficulty: float | None
    before_retrievability: float | None
    offer_again_s: int
    offer_hard_s: int
    offer_good_s: int
    offer_easy_s: int
    labels: str
    desired_retention: float
    parameter_set: int
    new_per_day: int
    reviews_per_day: int


class Response(Value):
    presentation: int | None
    card_id: str
    grade: Literal["again", "hard", "good", "easy"] | None
    reveal_ms: int | None
    grade_ms: int | None
    unfocused_ms: int | None
    after_interval_days: int | None
    after_due: int | None
    after_stability: float | None
    after_difficulty: float | None
    recovered: bool
    revlog_id: int
    revlog_cid: int
    revlog_usn: int
    revlog_ease: int
    revlog_ivl: int
    revlog_last_ivl: int
    revlog_factor: int
    revlog_time_ms: int
    revlog_type: int


def instant() -> tuple[int, int]:
    offset = datetime.now().astimezone().utcoffset()
    assert offset is not None
    return time_ns() // 1_000_000, int(offset.total_seconds() // 60)


class Record:
    def __init__(self, path: Path, *, create: bool, release: str, anki_version: str):
        self.path = path
        self.reopen(create=create)
        if create:
            self.connection.execute("pragma journal_mode=wal")
            for table, fields in TABLES.items():
                self.connection.execute(f'create table "{table}" ({COMMON}, {fields})')
            self.connection.execute("""create view review as
                select p.*, c.front, c.back, c.assets,
                    r.id as response, r.at_ms as responded_at_ms,
                    r.utc_offset_min as response_utc_offset_min, r.writer as response_writer, r.grade,
                    r.reveal_ms, r.grade_ms, r.unfocused_ms,
                    r.after_interval_days, r.after_due, r.after_stability, r.after_difficulty,
                    r.recovered, r.revlog_id, r.revlog_cid, r.revlog_usn, r.revlog_ease, r.revlog_ivl, r.revlog_last_ivl,
                    r.revlog_factor, r.revlog_time_ms, r.revlog_type, u.at_ms as undone_at_ms
                from presentation p join content c on c.id=p.content
                left join response r on r.presentation=p.id
                left join undo u on u.response=r.id""")
        self.writer = self.add_writer(release, anki_version)
        if create:
            self.schema(1, json.dumps(TABLES))
        if (
            self.connection.execute('select 1 from "schema" where version=2').fetchone()
            is None
        ):
            with self.connection:
                self.connection.execute(
                    f"create table image_reference ({COMMON}, {IMAGE_REFERENCE})"
                )
                self.schema(2, json.dumps({"image_reference": IMAGE_REFERENCE}))

    def add_writer(self, release: str, anki_version: str) -> int:
        writer = self.connection.execute(
            "select coalesce(max(id), 0) + 1 from writer"
        ).fetchone()[0]
        at_ms, offset = instant()
        with self.connection:
            self.connection.execute(
                "insert into writer values (?, ?, ?, ?, ?, ?, ?)",
                (writer, at_ms, offset, writer, release, anki_version, 2),
            )
        return writer

    def schema(self, version: int, added: str) -> int:
        return self.insert(
            'insert into "schema" (at_ms, utc_offset_min, writer, version, added) values (?, ?, ?, ?, ?)',
            (version, added),
        )

    def store_event(self, kind: str, path: str) -> int:
        return self.insert(
            "insert into store_event (at_ms, utc_offset_min, writer, kind, path) values (?, ?, ?, ?, ?)",
            (kind, path),
        )

    def parameter_set(
        self,
        parameters: list[float],
        source: str,
        reviews: int | None = None,
        log_loss: float | None = None,
        rmse_bins: float | None = None,
    ) -> int:
        return self.insert(
            "insert into parameter_set (at_ms, utc_offset_min, writer, parameters, source, reviews, log_loss, rmse_bins) values (?, ?, ?, ?, ?, ?, ?, ?)",
            (json.dumps(parameters), source, reviews, log_loss, rmse_bins),
        )

    def session_end(self, session: int, cause: str) -> int:
        return self.insert(
            "insert into session_end (at_ms, utc_offset_min, writer, session, cause) values (?, ?, ?, ?, ?)",
            (session, cause),
        )

    def editor_view(
        self, card_id: str, deck_path: str, shown_ms: int, unfocused_ms: int
    ) -> int:
        return self.insert(
            "insert into editor_view (at_ms, utc_offset_min, writer, card_id, deck_path, shown_ms, unfocused_ms) values (?, ?, ?, ?, ?, ?, ?)",
            (card_id, deck_path, shown_ms, unfocused_ms),
        )

    def session(self, kind: str, path: str | None) -> int:
        return self.insert(
            "insert into session (at_ms, utc_offset_min, writer, scope_kind, scope_path) values (?, ?, ?, ?, ?)",
            (kind, path),
        )

    def content(self, digest: str, front: str, back: str, assets: str) -> int:
        return self.insert(
            "insert into content (at_ms, utc_offset_min, writer, digest, front, back, assets) values (?, ?, ?, ?, ?, ?, ?)",
            (digest, front, back, assets),
        )

    def media(self, content: int, name: str, digest: str) -> int:
        return self.insert(
            "insert into media (at_ms, utc_offset_min, writer, content, name, digest) values (?, ?, ?, ?, ?, ?)",
            (content, name, digest),
        )

    def image_reference(self, content: int, label: str, name: str) -> int:
        return self.insert(
            "insert into image_reference (at_ms, utc_offset_min, writer, content, label, name) values (?, ?, ?, ?, ?, ?)",
            (content, label, name),
        )

    def card_change(
        self,
        card_id: str,
        kind: str,
        from_deck: str | None,
        to_deck: str | None,
        content: int | None,
        tags: list[str],
    ) -> int:
        return self.insert(
            "insert into card_change (at_ms, utc_offset_min, writer, card_id, kind, from_deck, to_deck, content, tags) values (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (card_id, kind, from_deck, to_deck, content, json.dumps(tags)),
        )

    def presentation(self, facts: Presentation) -> int:
        fields = facts.model_dump()
        return self.insert(
            "insert into presentation (at_ms, utc_offset_min, writer, "
            + ", ".join(fields)
            + ") values (?, ?, ?, "
            + ", ".join("?" for _ in fields)
            + ")",
            tuple(fields.values()),
        )

    def response(self, facts: Response) -> int:
        fields = facts.model_dump()
        return self.insert(
            "insert into response (at_ms, utc_offset_min, writer, "
            + ", ".join(fields)
            + ") values (?, ?, ?, "
            + ", ".join("?" for _ in fields)
            + ")",
            tuple(fields.values()),
        )

    def undo(self, response: int) -> int:
        return self.insert(
            "insert into undo (at_ms, utc_offset_min, writer, response) values (?, ?, ?, ?)",
            (response,),
        )

    def setting_change(self, key: str, before: str, after: str) -> int:
        return self.insert(
            'insert into setting_change (at_ms, utc_offset_min, writer, key, "before", "after") values (?, ?, ?, ?, ?, ?)',
            (key, before, after),
        )

    def insert(self, sql: str, values: tuple[RecordScalar, ...]) -> int:
        at_ms, offset = instant()
        with self.connection:
            cursor = self.connection.execute(sql, (at_ms, offset, self.writer, *values))
        assert cursor.lastrowid is not None
        return cursor.lastrowid

    def close(self) -> None:
        self.connection.close()

    def reopen(self, *, create: bool = False) -> None:
        self.connection = sqlite3.connect(
            self.path if create else self.path.resolve().as_uri() + "?mode=rw",
            uri=not create,
        )
        self.connection.execute("pragma foreign_keys=on")
