# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Preserve learning through backups, cache rebuilds, and a leech review."""

import json
import os
import shutil
import sqlite3
import subprocess
import tempfile
import time
from contextlib import closing
from pathlib import Path

import psutil
from anki.cards_pb2 import FsrsMemoryState
from anki.collection import Collection
from anki.decks import DeckConfigId
from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def rows(path: Path):
    with closing(sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)) as record:
        tables = record.execute(
            "select name from sqlite_master where type='table' order by name"
        ).fetchall()
        return {
            name: record.execute(f'select * from "{name}" order by id').fetchall()
            for (name,) in tables
        }


def paired(store: Path) -> Path:
    with closing(sqlite3.connect(store / "record.sqlite3")) as record:
        event = record.execute(
            "select path from store_event where kind='backed-up' order by id desc limit 1"
        ).fetchone()
    assert event is not None, "Opening or closing Study must record an Anki backup."
    package = Path(event[0])
    assert package.is_file(), package
    snapshot = package.with_suffix(".sqlite3")
    assert rows(snapshot) == rows(store / "record.sqlite3")
    return package


def main(artifacts: Path) -> None:
    desktop = Path(__file__).resolve().parents[1]
    runtime = subprocess.check_output(
        ["uv", "python", "find", "--script", str(desktop / "backend.py")], text=True
    ).strip()
    with tempfile.TemporaryDirectory(prefix="flashcards-preservation-") as directory:
        workspace = Path(directory)
        (workspace / "Leech.md").write_text(
            '::: {.front card-id="leech-card"}\nRecall this.\n:::\n\n'
            '::: {.back card-id="leech-card"}\nAnswer.\n:::\n'
        )
        with sync_playwright() as playwright:
            api = playwright.request.new_context(
                base_url="http://127.0.0.1:1420",
                extra_http_headers={"x-flashcards": "1"},
            )

            def request(action: str, **values):
                response = api.post(
                    "/api/request",
                    data={"action": action, "workspace": str(workspace), **values},
                )
                assert response.ok, response.text()
                return response.json()

            opened = request("study-open")
            store = Path(opened["store"])
            first_backup = paired(store)
            original = rows(store / "record.sqlite3")
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            try:
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready", timeout=30000
                )
                before = rows(store / "record.sqlite3")
                collection_files = {
                    path: path.read_bytes() for path in store.glob("collection.anki2*")
                }
                request("rebuild-cache", generation=1)
                assert rows(store / "record.sqlite3") == before
                assert all(
                    path.read_bytes() == data for path, data in collection_files.items()
                )
                assert first_backup.is_file()
                assert first_backup.with_suffix(".sqlite3").is_file()
            finally:
                browser.close()
                api.dispose()

        # Prepare a due review at Anki's leech threshold with the isolated host stopped.
        hosts = [
            p
            for p in psutil.process_iter(["cmdline"])
            if p.info["cmdline"]
            and "study-host" in p.info["cmdline"]
            and p.environ().get("XDG_DATA_HOME") == os.environ["XDG_DATA_HOME"]
        ]
        assert len(hosts) == 1
        hosts[0].terminate()
        hosts[0].wait(timeout=10)
        # Seed an expired pair, then let Anki's real retention policy remove it.
        expired = store / "backups/backup-2000-01-01-00.00.00.colpkg"
        shutil.copy2(first_backup, expired)
        shutil.copy2(
            first_backup.with_suffix(".sqlite3"), expired.with_suffix(".sqlite3")
        )
        collection = Collection(str(store / "collection.anki2"))
        try:
            preferences = collection._backend.get_preferences()
            preferences.backups.minimum_interval_mins = 0
            preferences.backups.daily = 0
            preferences.backups.weekly = 0
            preferences.backups.monthly = 0
            collection._backend.set_preferences(preferences)
            preset = collection.decks.get_config(DeckConfigId(1))
            card = collection.get_card(collection.find_cards("")[0])
            card.type = card.queue = 2
            card.ivl = 10
            card.due = collection.sched.today
            card.reps = 10
            card.lapses = preset["lapse"]["leechFails"] - 1
            card.memory_state = FsrsMemoryState(stability=10, difficulty=5)
            card.last_review_time = int(time.time()) - 10 * 86400
            collection.update_card(card)
            identity = card.id
        finally:
            collection.close()

        with (artifacts / "host.log").open("w") as log:
            host = subprocess.Popen(
                [
                    runtime,
                    str(desktop / "backend.py"),
                    "study-host",
                    "--release",
                    "preservation-test",
                ],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=log,
                text=True,
            )
            try:

                def send(action: str, **values):
                    host.stdin.write(
                        json.dumps(
                            {"action": action, "workspace": str(workspace), **values}
                        )
                        + "\n"
                    )
                    host.stdin.flush()
                    line = host.stdout.readline()
                    assert line, "Study host exited without a response; see host.log."
                    reply = json.loads(line)
                    assert reply["ok"], reply
                    return reply["result"]

                send("study-open")
                paired(store)
                assert not expired.exists()
                assert not expired.with_suffix(".sqlite3").exists()
                assert first_backup.is_file()
                assert first_backup.with_suffix(".sqlite3").is_file()
                begun = send("study-begin", scope={"kind": "workspace"})
                offered = begun["next"]
                assert offered["card_id"] == "leech-card"
                following = send(
                    "study-answer",
                    session=begun["session"],
                    presentation=offered["presentation"],
                    grade="again",
                    timing={"reveal_ms": 1000, "grade_ms": 2000, "unfocused_ms": 0},
                )
                assert following["card_id"] == "leech-card", following
            finally:
                # Native shutdown closes stdin. SIGTERM is not an exit-backup test.
                host.stdin.close()
                assert host.wait(timeout=30) == 0
                host.stdout.close()
        paired(store)
        final = rows(store / "record.sqlite3")
        for name, earlier in original.items():
            assert final[name][: len(earlier)] == earlier, name
        for name, earlier in before.items():
            assert final[name][: len(earlier)] == earlier, name
        collection = Collection(str(store / "collection.anki2"))
        try:
            card = collection.get_card(identity)
            assert card.queue >= 0
            assert "leech" in card.note().tags
            assert card.lapses == preset["lapse"]["leechFails"]
            message, ok = collection.fix_integrity()
            assert ok, message
        finally:
            collection.close()

        # The record holds the tag that Anki's scheduler added (FR-045).
        def leech_changes():
            with closing(sqlite3.connect(store / "record.sqlite3")) as record:
                return record.execute(
                    "select kind, tags from card_change where card_id='leech-card' order by id"
                ).fetchall()

        changes = leech_changes()
        assert changes[-1][0] == "tags", changes
        assert "leech" in json.loads(changes[-1][1]), changes
        with closing(sqlite3.connect(store / "record.sqlite3")) as record:
            (shown,) = record.execute(
                "select tags from presentation where id=?",
                (following["presentation"],),
            ).fetchone()
        assert "leech" in json.loads(shown), shown

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            try:

                def open_workspace():
                    page.goto("http://127.0.0.1:1420")
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_label("Workspace folder").fill(str(workspace))
                    page.get_by_role(
                        "button", name="Open workspace", exact=True
                    ).click()
                    expect(page.get_by_role("status", name="Study")).to_have_text(
                        "Study cards ready", timeout=30000
                    )

                # A sync of unchanged decks adds no tag change for the leech.
                open_workspace()
                assert leech_changes() == changes
                # A later card change of the leech keeps the tag.
                (workspace / "Leech.md").write_text(
                    '::: {.front card-id="leech-card"}\nRecall this.\n:::\n\n'
                    '::: {.back card-id="leech-card"}\nA corrected answer.\n:::\n'
                )
                open_workspace()
                later = leech_changes()
                assert [kind for kind, _ in later[len(changes) :]] == ["content"]
                assert "leech" in json.loads(later[-1][1]), later
            finally:
                browser.close()


if __name__ == "__main__":
    with evidence(
        "study-preservation", Path(__file__).parent / "fixtures/study"
    ) as artifacts:
        main(artifacts)
