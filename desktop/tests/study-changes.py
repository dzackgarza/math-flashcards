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
from hashlib import sha256
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
        workspace = Path(directory) / "workspace"
        workspace.mkdir()
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

            def snapshot():
                with closing(sqlite3.connect(record_path)) as record:
                    return {
                        name: record.execute(
                            f'select * from "{name}" order by id'
                        ).fetchall()
                        for (name,) in record.execute(
                            "select name from sqlite_master where type='table'"
                        ).fetchall()
                    }

            retained_snapshots = [snapshot()]

            def open_window(attach_from: Path | None = None):
                browser = playwright.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                if attach_from is not None:
                    page.get_by_role("dialog", name="Choose a study store").get_by_role(
                        "button", name=f"Attach {attach_from}", exact=True
                    ).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready", timeout=30000
                )
                return browser, page

            def start_study(page):
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_role("button", name="Study", exact=True).click()
                return page.get_by_role("region", name="Study session")

            browser, page = open_window()
            try:
                study = start_study(page)
                front = study.locator(".side-editor.front .cm-content").inner_text()
                study.get_by_role("button", name="Show answer", exact=False).click()
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    study.get_by_role("button", name="Undo", exact=True)
                ).to_be_enabled()
                retained_snapshots.append(snapshot())
                study.get_by_role("button", name="Undo", exact=True).click()
                expect(study.locator(".side-editor.front .cm-content")).to_have_text(
                    front
                )
                retained_snapshots.append(snapshot())
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
                        "select back from review where card_id='moving' and undone_at_ms is null"
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
                    retained_snapshots.append(rows_before)
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
                assert collection.find_cards("deck:Workspace::412e6d64 CardId:moving")
                assert collection.find_cards("deck:Removed CardId:new")
                assert collection.find_cards("deck:Workspace::412e6d64 CardId:other")
                collection.sched.set_due_date(
                    collection.find_cards("CardId:moving"), "0"
                )
                scheduled = collection.get_card(
                    collection.find_cards("CardId:moving")[0]
                )
                schedule_before_edit = (
                    scheduled.ivl,
                    scheduled.due,
                    scheduled.reps,
                    scheduled.lapses,
                )
            finally:
                collection.close()
            with closing(sqlite3.connect(record_path)) as record:
                retained_rows = {
                    table: record.execute(
                        f'SELECT * FROM "{table}" ORDER BY id'
                    ).fetchall()
                    for table in tables
                }
                retained_snapshots.append(retained_rows)
            original_image = (
                Path(__file__).parent / "fixtures/study/triangle.svg"
            ).read_bytes()
            revised_image = original_image.replace(b"#dbeafe", b"#fee2e2").replace(
                b"#1e40af", b"#b91c1c"
            )
            assert original_image != revised_image
            picture = workspace / "shape.svg"
            picture.write_bytes(original_image)
            edited_back = "M edited in the editor.\n\n![Recorded shape](shape.svg)"
            browser, page = open_window()
            try:
                page.get_by_text("A", exact=True).click()
                page.locator(".card-row-label").filter(
                    has_text="Recall moving."
                ).click()
                back = page.locator(".side-editor.back .cm-content")
                with page.expect_response(
                    lambda response: (
                        response.url.endswith("/api/request")
                        and response.request.post_data_json.get("action")
                        == "study-sync"
                        and response.ok
                        and "moving" in response.json()["changed_cards"]
                    ),
                    timeout=10000,
                ):
                    back.click()
                    page.keyboard.press("Control+a")
                    page.keyboard.insert_text("M autosaved")
                with closing(sqlite3.connect(record_path)) as record:
                    assert record.execute(
                        "select c.back from content c join card_change a on a.content=c.id where a.card_id='moving' order by a.id desc limit 1"
                    ).fetchone() == ("M autosaved",)
                back.click()
                page.keyboard.press("Control+a")
                page.keyboard.insert_text(edited_back)
                expect(back).to_contain_text("M edited in the editor.")
                # Starting Study must flush this editor input before it reads source.
                study = start_study(page)
                expect(study).to_contain_text("Recall moving.")
                with closing(sqlite3.connect(record_path)) as record:
                    assert (
                        record.execute(
                            "select before_interval_days,before_due,before_reps,before_lapses from presentation where card_id='moving' order by id desc limit 1"
                        ).fetchone()
                        == schedule_before_edit
                    )
                study.get_by_role("button", name="Show answer", exact=False).click()
                expect(study).to_contain_text("M edited in the editor.")
                image = study.get_by_role("img", name="Recorded shape")
                expect(image).to_be_visible()
                expect(image).to_have_js_property("complete", True)
                assert image.evaluate("image => image.naturalWidth > 0")
                study.get_by_role("button", name="Good", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
            finally:
                browser.close()
            stop_host()
            collection = Collection(str(store / "collection.anki2"))
            try:
                collection.sched.set_due_date(
                    collection.find_cards("CardId:moving"), "0"
                )
            finally:
                collection.close()
            picture.write_bytes(revised_image)
            browser, page = open_window()
            try:
                study = start_study(page)
                expect(study).to_contain_text("Recall moving.")
                study.get_by_role("button", name="Show answer", exact=False).click()
                image = study.get_by_role("img", name="Recorded shape")
                expect(image).to_be_visible()
                expect(image).to_have_js_property("complete", True)
                assert image.evaluate("image => image.naturalWidth > 0")
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                with closing(sqlite3.connect(record_path)) as record:
                    reviews = record.execute(
                        "select back,content from review where card_id='moving' and response is not null and undone_at_ms is null order by id"
                    ).fetchall()
                    assert [row[0] for row in reviews] == [
                        "M",
                        edited_back,
                        edited_back,
                    ], reviews
                    media = [
                        record.execute(
                            "select digest from media where content=?", (content,)
                        ).fetchall()
                        for _, content in reviews
                    ]
                    assert media == [
                        [],
                        [(sha256(original_image).hexdigest(),)],
                        [(sha256(revised_image).hexdigest(),)],
                    ], media
                    for table, rows in retained_rows.items():
                        assert (
                            record.execute(
                                f'SELECT * FROM "{table}" ORDER BY id'
                            ).fetchall()[: len(rows)]
                            == rows
                        ), table
                assert (
                    store / "record-media" / sha256(original_image).hexdigest()
                ).read_bytes() == original_image
                assert (
                    store / "record-media" / sha256(revised_image).hexdigest()
                ).read_bytes() == revised_image
                study.get_by_role(
                    "button", name="Return to editor", exact=False
                ).click()
                a.rename(workspace / "A.retired")
                study = start_study(page)
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                expect(study.get_by_label("Remaining cards")).to_have_text(
                    "New: 0Learning: 0Review: 0"
                )
                with closing(sqlite3.connect(record_path)) as record:
                    for identity in ("kept", "moving", "other", "new"):
                        assert record.execute(
                            "select kind,to_deck from card_change where card_id=? order by id desc limit 1",
                            (identity,),
                        ).fetchone() == ("removed", None)
            finally:
                browser.close()
            stop_host()
            # Anki owns its SQL collations, including unicase. Use its reader
            # for complete table snapshots after the host releases the store.
            collection = Collection(str(store / "collection.anki2"))
            try:
                collection_tables = collection.db.list(
                    "select name from sqlite_master where type='table'"
                )
                collection_before = {
                    table: collection.db.all(f'SELECT * FROM "{table}"')
                    for table in collection_tables
                }
            finally:
                collection.close()
            request("study-open")
            noop = request("study-sync", assets=assets, paths=[], decks=[])
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
            stop_host()
            collection = Collection(str(store / "collection.anki2"))
            try:
                assert {
                    table: collection.db.all(f'SELECT * FROM "{table}"')
                    for table in collection_tables
                } == collection_before
            finally:
                collection.close()
            retained_snapshots.append(snapshot())
            old_workspace = workspace
            workspace = Path(directory) / "moved-workspace"
            old_workspace.rename(workspace)
            browser, page = open_window(attach_from=old_workspace)
            try:
                assert request("study-open")["store"] == str(store)
                before_rebuild = snapshot()
                retained_snapshots.append(before_rebuild)
                request("rebuild-cache", generation=100)
                assert snapshot() == before_rebuild
                final_rows = snapshot()
                for earlier in retained_snapshots:
                    for table, previous in earlier.items():
                        assert final_rows[table][: len(previous)] == previous, table
            finally:
                browser.close()
            api.dispose()


if __name__ == "__main__":
    with evidence(
        "study-changes", Path(__file__).parent / "fixtures" / "study"
    ) as artifacts:
        main(artifacts)
