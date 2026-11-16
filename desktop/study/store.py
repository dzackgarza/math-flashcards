"""Workspace stores using Anki's collection API and the app's permanent record."""

import sqlite3
from contextlib import closing
from datetime import UTC, datetime
from importlib.metadata import version
from pathlib import Path
from uuid import uuid4

from anki.collection import Collection
from anki.decks import DeckConfigId
from anki.errors import BackendIOError, DBError
from platformdirs import user_data_path
from pydantic import ValidationError

from study.record import TABLES, Record
from study.values import (
    Counts,
    DeckCounts,
    Open,
    Settings,
    StoreSummary,
    StudyError,
    StudyFailure,
    Unattached,
    Value,
)


class Attachment(Value):
    path: str
    at: str


class Metadata(Value):
    id: str
    created: str
    paths: list[Attachment]


def unreadable(path: Path, cause: str) -> StudyFailure:
    return StudyFailure(
        StudyError(kind="StoreUnreadable", message=f"Cannot open {path}: {cause}")
    )


def check_database(path: Path, tables: set[str]) -> None:
    if not path.is_file():
        raise unreadable(path, "file is missing")
    try:
        with closing(sqlite3.connect(f"file:{path}?mode=ro", uri=True)) as connection:
            names = {
                name
                for (name,) in connection.execute(
                    "select name from sqlite_master where type='table'"
                )
            }
        if missing := tables - names:
            raise unreadable(path, "missing tables: " + ", ".join(sorted(missing)))
    except sqlite3.DatabaseError as error:
        raise unreadable(path, str(error)) from error


class Store:
    def __init__(
        self, directory: Path, metadata: Metadata, *, create: bool, release: str
    ):
        self.directory = directory
        self.metadata = metadata
        collection_path = directory / "collection.anki2"
        record_path = directory / "record.sqlite3"
        if not create:
            for path in (collection_path, record_path):
                if not path.is_file():
                    raise unreadable(path, "file is missing")
            check_database(collection_path, {"col", "notes", "cards", "revlog"})
            check_database(record_path, set(TABLES))
        try:
            self.collection = Collection(str(collection_path))
        except (BackendIOError, DBError) as error:
            raise unreadable(collection_path, str(error)) from error
        if create:
            self.collection.set_config("fsrs", True)
            self.collection.set_config("applyAllParentLimits", True)
            preset = self.collection.decks.get_config(DeckConfigId(1))
            assert preset is not None
            preset["lapse"]["leechAction"] = 1
            preset["reviewOrder"] = 7
            preset["maxTaken"] = 9999
            preset["fsrsParams6"] = list(
                self.collection._backend.get_deck_configs_for_update(
                    1
                ).defaults.config.fsrs_params_6
            )
            self.collection.decks.update_config(preset)
            self.collection.decks.id("Workspace")
            for name in ("record-media", "record-assets", "backups"):
                (directory / name).mkdir()
        try:
            self.record = Record(
                record_path,
                create=create,
                release=release,
                anki_version=version("anki"),
            )
        except sqlite3.DatabaseError as error:
            self.collection.close()
            raise unreadable(record_path, str(error)) from error
        if create:
            self.record.store_event("created", metadata.paths[-1].path)
            self.record.parameter_set(preset["fsrsParams6"], "anki-default")
        else:
            unfinished = self.record.connection.execute(
                "select id from session where id not in (select session from session_end)"
            ).fetchall()
            for (session,) in unfinished:
                self.record.session_end(session, "recovered")

    def opened(self) -> Open:
        preset = self.collection.decks.get_config(DeckConfigId(1))
        assert preset is not None
        tree = self.collection.sched.deck_due_tree()
        workspace = next(child for child in tree.children if child.name == "Workspace")
        return Open(
            store=str(self.directory),
            media=str(self.directory / "record-media"),
            record=str(self.directory / "record.sqlite3"),
            settings=Settings(
                new_per_day=preset["new"]["perDay"],
                reviews_per_day=preset["rev"]["perDay"],
                desired_retention=preset["desiredRetention"],
            ),
            counts=DeckCounts(
                path="",
                kind="workspace",
                counts=Counts(
                    new=workspace.new_count,
                    learning=workspace.learn_count,
                    review=workspace.review_count,
                ),
                children=[],
            ),
        )

    def summary(self) -> StoreSummary:
        used = self.record.connection.execute(
            "select max(at_ms) from writer"
        ).fetchone()[0]
        return StoreSummary(
            store=self.metadata.id,
            paths=[item.path for item in self.metadata.paths],
            path_exists=Path(self.metadata.paths[-1].path).is_dir(),
            created=self.metadata.created,
            last_used=datetime.fromtimestamp(used / 1000, UTC).isoformat(),
            cards=self.collection.card_count(),
            responses=self.record.connection.execute(
                "select count(*) from response"
            ).fetchone()[0],
        )

    def attach(self, workspace: str) -> None:
        self.metadata.paths.append(
            Attachment(path=workspace, at=datetime.now(UTC).isoformat())
        )
        self.save_metadata()
        self.record.store_event("attached", workspace)

    def save_metadata(self) -> None:
        temporary = self.directory / "store.json.tmp"
        temporary.write_text(self.metadata.model_dump_json())
        temporary.replace(self.directory / "store.json")

    def close(self) -> None:
        sessions = self.record.connection.execute(
            "select id from session where id not in (select session from session_end)"
        ).fetchall()
        for (session,) in sessions:
            self.record.session_end(session, "host-stopped")
        self.collection.close()
        self.record.close()


class Stores:
    def __init__(self, release: str) -> None:
        self.release = release
        self.directory = user_data_path("math-flashcards") / "study"
        self.directory.mkdir(parents=True, exist_ok=True)
        self.opened: dict[str, Store] = {}

    def metadata(self) -> list[Metadata]:
        records = []
        for directory in sorted(self.directory.iterdir()):
            path = directory / "store.json"
            try:
                record = Metadata.model_validate_json(path.read_bytes())
            except (OSError, ValidationError) as error:
                raise unreadable(path, str(error)) from error
            if record.id != directory.name or not record.paths:
                raise unreadable(
                    path, "store identity or attachment history is invalid"
                )
            records.append(record)
        return records

    def load(self, metadata: Metadata) -> Store:
        if metadata.id not in self.opened:
            self.opened[metadata.id] = Store(
                self.directory / metadata.id,
                metadata,
                create=False,
                release=self.release,
            )
        return self.opened[metadata.id]

    def create(self, workspace: str) -> Store:
        at = datetime.now(UTC).isoformat()
        metadata = Metadata(
            id=str(uuid4()), created=at, paths=[Attachment(path=workspace, at=at)]
        )
        directory = self.directory / metadata.id
        directory.mkdir()
        (directory / "store.json").write_text(metadata.model_dump_json())
        store = Store(directory, metadata, create=True, release=self.release)
        self.opened[metadata.id] = store
        return store

    def open(self, workspace: str) -> Open | Unattached:
        metadata = self.metadata()
        if not metadata:
            return self.create(workspace).opened()
        for item in metadata:
            if item.paths[-1].path == workspace:
                return self.load(item).opened()
        return Unattached(stores=[self.summary(item) for item in metadata])

    def attached(self, workspace: str) -> Store | None:
        for item in self.metadata():
            if item.paths[-1].path == workspace:
                return self.load(item)
        return None

    def summary(self, metadata: Metadata) -> StoreSummary:
        if metadata.id in self.opened:
            return self.opened[metadata.id].summary()
        directory = self.directory / metadata.id
        collection = directory / "collection.anki2"
        record = directory / "record.sqlite3"
        check_database(collection, {"cards"})
        check_database(record, set(TABLES))
        with closing(
            sqlite3.connect(f"file:{collection}?mode=ro", uri=True)
        ) as connection:
            cards = connection.execute("select count(*) from cards").fetchone()[0]
        with closing(sqlite3.connect(f"file:{record}?mode=ro", uri=True)) as connection:
            responses = connection.execute("select count(*) from response").fetchone()[
                0
            ]
            used = connection.execute("select max(at_ms) from writer").fetchone()[0]
        return StoreSummary(
            store=metadata.id,
            paths=[item.path for item in metadata.paths],
            path_exists=Path(metadata.paths[-1].path).is_dir(),
            created=metadata.created,
            last_used=datetime.fromtimestamp(used / 1000, UTC).isoformat(),
            cards=cards,
            responses=responses,
        )

    def attach(self, workspace: str, identity: str) -> Open:
        for item in self.metadata():
            if item.id == identity:
                store = self.load(item)
                store.attach(workspace)
                return store.opened()
        raise StudyFailure(
            StudyError(kind="UnknownStore", message=f"Unknown store: {identity}")
        )

    def close(self) -> None:
        for store in self.opened.values():
            store.close()
