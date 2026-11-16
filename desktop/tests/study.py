# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Exercise Study through the real bridge with disposable learning data."""

import json
import os
import shutil
import sqlite3
import tempfile
from contextlib import closing
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlencode
from uuid import UUID, uuid4

import psutil
from anki.collection import Collection
from playwright.sync_api import sync_playwright


def main() -> None:
    desktop = Path(__file__).resolve().parents[1]
    stores = Path(os.environ["XDG_DATA_HOME"]) / "math-flashcards" / "study"
    with tempfile.TemporaryDirectory(prefix="flashcards-study-") as temporary:
        root = Path(temporary)
        workspace = root / "workspace"
        shutil.copytree(desktop / "tests" / "fixtures" / "study", workspace)
        with sync_playwright() as playwright:
            api = playwright.request.new_context(
                base_url="http://127.0.0.1:1420",
                extra_http_headers={"x-flashcards": "1"},
            )
            try:
                response = api.post(
                    "/api/request",
                    data={"action": "study-open", "workspace": str(workspace)},
                )
                assert response.ok, response.text()
                opened = response.json()
                assert opened["state"] == "Open", opened
                store = Path(opened["store"])
                assert store.parent == stores, store
                UUID(store.name)
                metadata = json.loads((store / "store.json").read_text())
                assert metadata["id"] == store.name
                assert metadata["paths"][-1]["path"] == str(workspace)
                record_path = store / "record.sqlite3"
                assert opened["record"] == str(record_path)
                assert opened["media"] == str(store / "record-media")
                # Retained files are content-addressed store input. Serve their bytes
                # with the authored file's type, independent of the current workspace.
                image = (workspace / "triangle.svg").read_bytes()
                retained = store / "record-media" / sha256(image).hexdigest()
                retained.write_bytes(image)
                media = api.get(
                    "/api/study-media?"
                    + urlencode({"path": str(retained), "name": "triangle.svg"})
                )
                assert media.ok, media.text()
                assert media.headers["content-type"] == "image/svg+xml", media.headers
                assert media.body() == image
                forbidden = api.get(
                    "/api/study-media?"
                    + urlencode({"path": str(store / "store.json"), "name": "store.json"})
                )
                assert forbidden.status == 403, forbidden.text()
                missing = api.get(
                    "/api/study-media?"
                    + urlencode({"path": str(retained.parent / ("0" * 64)), "name": "missing.svg"})
                )
                assert missing.status == 404, missing.text()
                assert opened["settings"] == {
                    "new_per_day": 20,
                    "reviews_per_day": 200,
                    "desired_retention": 0.9,
                }
                with closing(sqlite3.connect(record_path)) as record:
                    assert record.execute("pragma journal_mode").fetchone() == ("wal",)
                    tables = {
                        name
                        for (name,) in record.execute(
                            "select name from sqlite_master where type='table'"
                        )
                    }
                    assert {
                        "writer",
                        "schema",
                        "store_event",
                        "editor_view",
                        "session",
                        "session_end",
                        "content",
                        "media",
                        "card_change",
                        "presentation",
                        "response",
                        "undo",
                        "setting_change",
                        "parameter_set",
                    } <= tables, tables
                    response_columns = {
                        column[1] for column in record.execute("pragma table_info(response)")
                    }
                    assert {"revlog_cid", "revlog_usn"} <= response_columns, response_columns
                    assert record.execute(
                        'select version from "schema"'
                    ).fetchall() == [(1,)]
                    writer = record.execute(
                        "select app_release, anki_version, schema_version from writer"
                    ).fetchone()
                    assert writer[0] and writer[1] and writer[2] == 1, writer
                    assert record.execute(
                        "select kind, path from store_event"
                    ).fetchall() == [("created", str(workspace))]
                    assert record.execute(
                        "select source from parameter_set"
                    ).fetchall() == [("anki-default",)]
                    assert record.execute("select * from review").fetchall() == []

                # Anki owns the collection exclusively. Stop this isolated test host
                # before inspecting its committed state with Anki's own library.
                hosts = [
                    process
                    for process in psutil.process_iter(["cmdline"])
                    if "study-host" in process.info["cmdline"]
                    and process.environ().get("XDG_DATA_HOME")
                    == os.environ["XDG_DATA_HOME"]
                ]
                assert len(hosts) == 1, hosts
                hosts[0].terminate()
                hosts[0].wait(timeout=10)
                # SQLite's backup includes committed WAL contents after the stop:
                # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.backup
                snapshot = root / "snapshot.anki2"
                with (
                    closing(
                        sqlite3.connect(
                            f"file:{store / 'collection.anki2'}?mode=ro", uri=True
                        )
                    ) as source,
                    closing(sqlite3.connect(snapshot)) as copy,
                ):
                    source.backup(copy)
                collection = Collection(str(snapshot))
                try:
                    assert collection.get_config("fsrs") is True
                    assert collection.get_config("applyAllParentLimits") is True
                    preset = collection.decks.get_config(1)
                    assert preset["lapse"]["leechAction"] == 1
                    assert preset["reviewOrder"] == 7
                    assert preset["maxTaken"] == 9999
                finally:
                    collection.close()

                other = root / "other"
                other.mkdir()
                before = set(stores.iterdir())
                response = api.post(
                    "/api/request",
                    data={
                        "action": "study-open",
                        "workspace": str(other),
                    },
                )
                assert response.ok, response.text()
                unattached = response.json()
                assert unattached["state"] == "Unattached", unattached
                summary = unattached["stores"]
                assert len(summary) == 1, summary
                assert summary[0]["store"] == store.name
                assert summary[0]["paths"] == [str(workspace)]
                assert summary[0]["last_used"]
                assert summary[0]["cards"] == 0 and summary[0]["responses"] == 0
                assert set(stores.iterdir()) == before

                response = api.post(
                    "/api/request",
                    data={
                        "action": "study-attach",
                        "workspace": str(other),
                        "choice": {"kind": "existing", "store": store.name},
                    },
                )
                assert response.ok, response.text()
                assert response.json()["store"] == str(store)
                metadata = json.loads((store / "store.json").read_text())
                assert [item["path"] for item in metadata["paths"]] == [
                    str(workspace),
                    str(other),
                ]
                with closing(sqlite3.connect(record_path)) as record:
                    assert record.execute(
                        "select kind, path from store_event order by id"
                    ).fetchall() == [
                        ("created", str(workspace)),
                        ("attached", str(other)),
                    ]
                    rows = record.execute(
                        "select * from store_event order by id"
                    ).fetchall()
                metadata_before = (store / "store.json").read_bytes()
                response = api.post(
                    "/api/request",
                    data={
                        "action": "study-attach",
                        "workspace": str(workspace),
                        "choice": {"kind": "new"},
                    },
                )
                assert response.ok, response.text()
                assert response.json()["store"] != str(store)
                assert (store / "store.json").read_bytes() == metadata_before
                with closing(sqlite3.connect(record_path)) as record:
                    assert (
                        record.execute(
                            "select * from store_event order by id"
                        ).fetchall()
                        == rows
                    )
                before = set(stores.iterdir())
                response = api.post(
                    "/api/request",
                    data={
                        "action": "study-attach",
                        "workspace": str(workspace),
                        "choice": {"kind": "existing", "store": str(uuid4())},
                    },
                )
                assert not response.ok
                assert response.json()["kind"] == "UnknownStore", response.text()
                assert set(stores.iterdir()) == before

                for defect in (
                    "corrupt-collection",
                    "absent-collection",
                    "absent-record",
                ):
                    broken_workspace = root / defect
                    broken_workspace.mkdir()
                    broken = stores / str(uuid4())
                    broken.mkdir()
                    (broken / "store.json").write_text(
                        json.dumps(
                            {
                                "id": broken.name,
                                "created": metadata["created"],
                                "paths": [
                                    {
                                        "path": str(broken_workspace),
                                        "at": metadata["created"],
                                    }
                                ],
                            }
                        )
                    )
                    if defect == "corrupt-collection":
                        (broken / "collection.anki2").write_bytes(
                            b"unreadable collection"
                        )
                    if defect == "absent-record":
                        shutil.copyfile(snapshot, broken / "collection.anki2")
                    if defect != "absent-record":
                        with closing(
                            sqlite3.connect(broken / "record.sqlite3")
                        ) as record:
                            record.execute("create table preserved (value text)")
                    files_before = {
                        path.name: path.read_bytes() for path in broken.iterdir()
                    }
                    response = api.post(
                        "/api/request",
                        data={
                            "action": "study-open",
                            "workspace": str(broken_workspace),
                        },
                    )
                    assert not response.ok
                    failure = response.json()
                    assert failure["kind"] == "StoreUnreadable", failure
                    expected = (
                        "record.sqlite3"
                        if defect == "absent-record"
                        else "collection.anki2"
                    )
                    assert str(broken / expected) in failure["message"], failure
                    assert {
                        path.name: path.read_bytes() for path in broken.iterdir()
                    } == files_before, defect
            finally:
                api.dispose()


if __name__ == "__main__":
    main()
