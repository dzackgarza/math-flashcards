"""Workspace stores using Anki's collection API and the app's permanent record."""

import shutil
import sqlite3
from contextlib import closing
from datetime import UTC, datetime
from importlib.metadata import version
from pathlib import Path, PurePosixPath
from uuid import uuid4

from anki.collection import Collection
from anki.decks import DeckConfigId
from anki.decks_pb2 import DeckTreeNode
from anki.errors import BackendIOError, DBError
from platformdirs import user_data_path
from pydantic import ValidationError
from send2trash import send2trash

from study.record import TABLES, Record, Response
from study.values import (
    Counts,
    DeckCounts,
    Fit,
    Open,
    Settings,
    StoreCopy,
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


def deck_name(path: str) -> str:
    # Encode complete UTF-8 components with Python's reversible bytes.hex().
    # Anki normalizes names and splits "::": research.md R5.
    return "::".join(
        ["Workspace", *(part.encode().hex() for part in path.split("/") if part)]
    )


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
        self.grade_responses: dict[int, int] = {}
        self.pending_fit: Fit | None = None
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
            recorded = {
                row[0]
                for row in self.record.connection.execute(
                    "select revlog_id from response"
                )
            }
            for row in self.collection.db.all(
                "select r.id,r.cid,r.usn,r.ease,r.ivl,r.lastIvl,r.factor,r.time,r.type,n.guid "
                "from revlog r join cards c on c.id=r.cid join notes n on n.id=c.nid order by r.id"
            ):
                if row[0] in recorded:
                    continue
                # A later card state is not evidence for the state after an old
                # review. Recover only the facts in Anki's durable review row.
                self.record.response(
                    Response(
                        presentation=None,
                        card_id=row[9],
                        grade={1: "again", 2: "hard", 3: "good", 4: "easy"}.get(row[3]),
                        reveal_ms=None,
                        grade_ms=None,
                        unfocused_ms=None,
                        after_interval_days=None,
                        after_due=None,
                        after_stability=None,
                        after_difficulty=None,
                        recovered=True,
                        revlog_id=row[0],
                        revlog_cid=row[1],
                        revlog_usn=row[2],
                        revlog_ease=row[3],
                        revlog_ivl=row[4],
                        revlog_last_ivl=row[5],
                        revlog_factor=row[6],
                        revlog_time_ms=row[7],
                        revlog_type=row[8],
                    )
                )
            unfinished = self.record.connection.execute(
                "select id from session where id not in (select session from session_end)"
            ).fetchall()
            for (session,) in unfinished:
                self.record.session_end(session, "recovered")
        try:
            self.backup()
        except Exception:
            self.collection.close()
            self.record.close()
            raise

    def opened(self) -> Open:
        preset = self.collection.decks.get_config(DeckConfigId(1))
        assert preset is not None
        return Open(
            store=str(self.directory),
            media=str(self.directory / "record-media"),
            record=str(self.directory / "record.sqlite3"),
            settings=Settings(
                new_per_day=preset["new"]["perDay"],
                reviews_per_day=preset["rev"]["perDay"],
                desired_retention=preset["desiredRetention"],
            ),
            counts=self.counts(),
        )

    def counts(self) -> DeckCounts:
        paths = set(self.collection.get_config("native_decks", {}))
        folders = {
            str(parent)
            for path in paths
            for parent in PurePosixPath(path).parents
            if str(parent) != "."
        }
        names = {deck_name(path): path for path in paths | folders | {""}}

        def visit(node: DeckTreeNode, name: str) -> DeckCounts | None:
            path = names.get(name)
            if path is None:
                return None
            return DeckCounts(
                path=path,
                kind="workspace" if not path else "deck" if path in paths else "folder",
                counts=Counts(
                    new=node.new_count,
                    learning=node.learn_count,
                    review=node.review_count,
                ),
                children=[
                    result
                    for child in node.children
                    if (result := visit(child, name + "::" + child.name)) is not None
                ],
            )

        tree = self.collection.sched.deck_due_tree()
        workspace = next(child for child in tree.children if child.name == "Workspace")
        result = visit(workspace, "Workspace")
        assert result is not None
        return result

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

    def copy(self, directory: str) -> StoreCopy:
        try:
            destination = Path(directory).resolve(strict=True)
            if not destination.is_dir():
                raise NotADirectoryError(f"Not a directory: {destination}")
            if destination.is_relative_to(self.directory.parent.resolve()):
                raise ValueError(
                    "Choose a copy destination outside the live Study data directory."
                )
            parent = destination / datetime.now(UTC).strftime(
                "math-flashcards-study-%Y%m%dT%H%M%S.%fZ"
            )
            parent.mkdir()
        except (OSError, ValueError) as error:
            raise StudyFailure(
                StudyError(kind="CopyFailed", message=str(error))
            ) from error
        copied = parent / self.metadata.id
        # Closing both SQLite owners checkpoints their WALs. Reopen the same
        # objects to preserve the active session and writer (research.md R18).
        self.collection.close()
        self.record.close()
        try:
            try:
                shutil.copytree(self.directory, copied)
            finally:
                self.collection.reopen()
                self.record.reopen()
                self.grade_responses.clear()
        except OSError as error:
            send2trash(str(parent))
            raise StudyFailure(
                StudyError(kind="CopyFailed", message=str(error))
            ) from error
        self.record.store_event("copied", str(copied))
        return StoreCopy(path=str(copied))

    def backup(self) -> None:
        directory = self.directory / "backups"
        before = {path: path.stat() for path in directory.glob("backup-*.colpkg")}
        if self.collection.create_backup(
            backup_folder=str(directory), force=False, wait_for_completion=True
        ):
            # Anki owns filenames and may replace a same-second backup. Compare
            # file metadata rather than reconstructing its local timestamp (R4).
            changed = [
                path
                for path in directory.glob("backup-*.colpkg")
                if path not in before or path.stat() != before[path]
            ]
            if len(changed) != 1:
                raise RuntimeError(
                    f"Cannot identify the completed Anki backup: {changed}"
                )
            package = changed[0]
            self.record.store_event("backed-up", str(package))
            temporary = package.with_suffix(".sqlite3.tmp")
            with closing(sqlite3.connect(temporary)) as snapshot:
                self.record.connection.backup(snapshot)
            temporary.replace(package.with_suffix(".sqlite3"))
        # Anki's retention policy removes collection backups. Keep each record
        # snapshot for exactly as long as its matching collection backup remains.
        for snapshot in directory.glob("backup-*.sqlite3"):
            if not snapshot.with_suffix(".colpkg").exists():
                send2trash(str(snapshot))

    def close(self) -> None:
        sessions = self.record.connection.execute(
            "select id from session where id not in (select session from session_end)"
        ).fetchall()
        for (session,) in sessions:
            self.record.session_end(session, "host-stopped")
        try:
            self.backup()
        finally:
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
