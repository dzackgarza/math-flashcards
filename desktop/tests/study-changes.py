# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Keep scheduling and recorded history through native deck file changes."""

import json
import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

import psutil
from anki.collection import Collection
from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def card(identity: str, answer: str, tags: str = "") -> str:
    return (
        f'::: {{.front card-id="{identity}" tags="{tags}"}}\nRecall {identity}.\n:::\n\n'
        f'::: {{.back card-id="{identity}"}}\n{answer}\n:::\n\n'
    )


def stop_host() -> None:
    hosts = [
        process
        for process in psutil.process_iter(["cmdline"])
        if process.info["cmdline"] is not None
        and "study-host" in process.info["cmdline"]
        and process.environ().get("XDG_DATA_HOME") == os.environ["XDG_DATA_HOME"]
    ]
    assert len(hosts) == 1, hosts
    hosts[0].terminate()
    hosts[0].wait(timeout=10)


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="flashcards-study-changes-") as directory:
        workspace = Path(directory)
        a, b, c = [workspace / name for name in ("A.md", "B.md", "C.md")]
        kept, moving, other = card("kept", "K"), card("moving", "M"), card("other", "O")
        a.write_text(kept + moving)
        b.write_text(other)
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
            store, record_path = Path(opened["store"]), Path(opened["record"])

            def open_window():
                browser = playwright.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready"
                )
                return browser, page

            def start_study(page):
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_role("button", name="Study", exact=True).click()
                return page.get_by_role("region", name="Study session")

            browser, page = open_window()
            try:
                study = start_study(page)
                for _ in range(3):
                    study.get_by_role("button", name="Show answer", exact=False).click()
                    study.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
            finally:
                browser.close()
            stop_host()
            collection = Collection(str(store / "collection.anki2"))
            try:
                ids = collection.find_cards("")
                collection.sched.set_due_date(ids, "7")
                note = collection.get_note(collection.find_notes("CardId:moving")[0])
                note.tags.append("leech")
                collection.update_note(note)
                before = collection.db.all(
                    "select id,nid,type,queue,due,ivl,factor,reps,lapses,odue,odid from cards order by id"
                )
                revlogs = collection.db.all("select * from revlog order by id")
            finally:
                collection.close()
            browser, page = open_window()
            try:
                # External edits go through the workspace watcher and the same
                # saved-source parser used by an editor save and session start.
                a.write_text(kept)
                b.write_text(other + moving)
                study = start_study(page)
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible(timeout=10000)
                with closing(sqlite3.connect(record_path)) as record:
                    transfer = record.execute(
                        "select kind,from_deck,to_deck from card_change where card_id='moving' and kind!='added' order by id"
                    ).fetchall()
                    assert transfer in (
                        [("moved", "A.md", "B.md")],
                        [("removed", "A.md", None), ("restored", None, "B.md")],
                    ), transfer
                study.get_by_role(
                    "button", name="Return to editor", exact=False
                ).click()
                b.rename(c)
                study = start_study(page)
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                study.get_by_role(
                    "button", name="Return to editor", exact=False
                ).click()
                changed = card("moving", "M revised", "revised")
                c.write_text(changed + other)
                study = start_study(page)
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                study.get_by_role(
                    "button", name="Return to editor", exact=False
                ).click()
                c.write_text(other)
                study = start_study(page)
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                with closing(sqlite3.connect(record_path)) as record:
                    assert record.execute(
                        "select kind from card_change where card_id='moving' order by id desc limit 1"
                    ).fetchone() == ("removed",)
                study.get_by_role(
                    "button", name="Return to editor", exact=False
                ).click()
                a.write_text(kept + changed)
                study = start_study(page)
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                with closing(sqlite3.connect(record_path)) as record:
                    changes = record.execute(
                        "select kind from card_change where card_id='moving' order by id"
                    ).fetchall()
                    # R6 permits removal followed by restoration when the file
                    # watcher delivers the two sides of a move in separate batches.
                    transfers = [[("moved",)], [("removed",), ("restored",)]]
                    assert changes in [
                        [
                            ("added",),
                            *first,
                            *second,
                            ("content",),
                            ("tags",),
                            ("removed",),
                            ("restored",),
                        ]
                        for first in transfers
                        for second in transfers
                    ], changes
                    assert record.execute(
                        "select back from review where card_id='moving'"
                    ).fetchone() == ("M",)
                    assert record.execute(
                        "select c.back from content c join card_change a on a.content=c.id where a.card_id='moving' order by a.id desc limit 1"
                    ).fetchone() == ("M revised",)
                page.screenshot(path=str(artifacts / "restored-study.png"))
                study.get_by_role(
                    "button", name="Return to editor", exact=False
                ).click()
                c.write_text(other + changed)
                page.get_by_role("button", name="Show problems", exact=True).click()
                problems = page.get_by_role("dialog")
                expect(problems).to_contain_text("Duplicate card", timeout=10000)
                expect(problems).to_contain_text("moving")
                expect(problems).to_contain_text("A.md")
                expect(problems).to_contain_text("C.md")
                page.screenshot(path=str(artifacts / "duplicate-card.png"))
                page.keyboard.press("Escape")
                c.write_text("This deck is temporarily incomplete.\n")
                a.write_text(kept + changed + card("new", "New answer"))
                study = start_study(page)
                expect(study).to_contain_text("Recall new.", timeout=10000)
                a.write_text(
                    kept
                    + changed
                    + card("new", "Updated answer").replace(
                        "Recall new.", "Recall updated new."
                    )
                )
                expect(study).to_contain_text("Recall updated new.", timeout=10000)
                study.get_by_role("button", name="Show answer", exact=False).click()
                expect(study).to_contain_text("Updated answer", timeout=10000)
                a.write_text(kept + changed)
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible(timeout=10000)
                study.get_by_role(
                    "button", name="Return to editor", exact=False
                ).click()
                a.write_text(other + changed + kept)
                c.rename(workspace / "C.retired")
                study = start_study(page)
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready"
                )
                with closing(sqlite3.connect(record_path)) as record:
                    tables = [
                        row[0]
                        for row in record.execute(
                            "select name from sqlite_master where type='table'"
                        )
                    ]
                    rows_before = {
                        table: record.execute(
                            f'SELECT * FROM "{table}" ORDER BY id'
                        ).fetchall()
                        for table in tables
                    }
                assets = json.loads(
                    (Path(__file__).resolve().parents[1] / "assets.json").read_text()
                )["identity"]
                noop = request("study-sync", assets=assets, paths=["A.md"], decks=[])
                assert noop == {
                    "added": 0,
                    "updated": 0,
                    "moved": 0,
                    "removed": 0,
                    "restored": 0,
                    "failed": [],
                    "duplicates": [],
                    "pending": 0,
                    "changed_cards": [],
                }, noop
                with closing(sqlite3.connect(record_path)) as record:
                    assert {
                        table: record.execute(
                            f'SELECT * FROM "{table}" ORDER BY id'
                        ).fetchall()
                        for table in tables
                    } == rows_before
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
            stop_host()
            collection = Collection(str(store / "collection.anki2"))
            try:
                assert (
                    collection.db.all(
                        "select id,nid,type,queue,due,ivl,factor,reps,lapses,odue,odid from cards where nid in (select id from notes where guid != 'new') order by id"
                    )
                    == before
                )
                assert collection.db.all("select * from revlog order by id") == revlogs
                assert set(
                    collection.get_note(collection.find_notes("CardId:moving")[0]).tags
                ) == {"leech", "revised"}
                assert collection.find_cards("deck:Workspace::A CardId:moving")
                assert collection.find_cards("deck:Removed CardId:new")
                assert collection.find_cards("deck:Workspace::A CardId:other")
            finally:
                collection.close()
            api.dispose()


if __name__ == "__main__":
    with evidence(
        "study-changes", Path(__file__).parent / "fixtures" / "study"
    ) as artifacts:
        main(artifacts)
