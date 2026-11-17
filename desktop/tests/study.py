# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Exercise Study through the real bridge with disposable learning data."""

import json
import os
import pstats
import re
import shutil
import sqlite3
import subprocess
import tempfile
from contextlib import closing
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlencode
from uuid import UUID, uuid4

import psutil
from anki.collection import Collection
from anki.scheduler.v3 import CardAnswer
from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
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
                diagnostics = (
                    Path(os.environ["XDG_STATE_HOME"])
                    / "math-flashcards"
                    / "diagnostics"
                )
                logs = list(diagnostics.glob("*/events.jsonl"))
                assert logs, "Opening Study must retain its operation log in XDG state."
                events = [json.loads(line) for line in logs[0].read_text().splitlines()]
                completed = [event for event in events if event["event"] == "completed"]
                opened_event = next(
                    event for event in completed if event.get("action") == "study-open"
                )
                assert opened_event["outcome"] == "ok", opened_event
                assert opened_event["workspace"] == str(workspace)
                assert opened_event["elapsed_seconds"] > 0
                context = json.loads((logs[0].parent / "context.json").read_text())
                assert (
                    context["app_release"]
                    == json.loads((desktop / "package.json").read_text())["version"]
                )
                assert (
                    context["sources"]["study/host.py"]
                    == sha256((desktop / "study" / "host.py").read_bytes()).hexdigest()
                )
                pstats.Stats(str(logs[0].parent / opened_event["profile"]))
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
                forbidden = api.get(
                    "/api/study-media?"
                    + urlencode(
                        {"path": str(store / "store.json"), "name": "store.json"}
                    )
                )
                assert forbidden.status == 403, forbidden.text()
                missing = api.get(
                    "/api/study-media?"
                    + urlencode(
                        {
                            "path": str(retained.parent / ("0" * 64)),
                            "name": "missing.svg",
                        }
                    )
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
                        column[1]
                        for column in record.execute("pragma table_info(response)")
                    }
                    assert {"revlog_cid", "revlog_usn"} <= response_columns, (
                        response_columns
                    )
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

                browser = playwright.chromium.launch(headless=False)
                context = browser.new_context()
                page = context.new_page()
                page.add_init_script("""
                    window.observedFocus = [];
                    for (const kind of ['focus', 'blur', 'visibilitychange']) {
                      const target = kind === 'visibilitychange' ? document : window;
                      target.addEventListener(kind, event => window.observedFocus.push({
                        kind, at: event.timeStamp, handled: performance.now(),
                        focused: document.hasFocus(), hidden: document.hidden
                      }));
                    }
                """)
                try:
                    page.goto("http://127.0.0.1:1420")
                    # Disable Playwright's focus emulation on the loaded page;
                    # native window focus must exercise the app's focus handling.
                    # https://chromedevtools.github.io/devtools-protocol/tot/Emulation/#method-setFocusEmulationEnabled
                    page.context.new_cdp_session(page).send(
                        "Emulation.setFocusEmulationEnabled", {"enabled": False}
                    )
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_label("Workspace folder").fill(str(workspace))
                    page.get_by_role(
                        "button", name="Open workspace", exact=True
                    ).click()
                    expect(
                        page.get_by_role("button", name="Workspace", exact=True)
                    ).to_have_text(workspace.name)
                    expect(page.get_by_role("status", name="Study")).to_have_text(
                        "Study cards ready"
                    )
                    media = api.get(
                        "/api/study-media?"
                        + urlencode({"path": str(retained), "name": "triangle.svg"})
                    )
                    assert media.ok, media.text()
                    assert media.headers["content-type"] == "image/svg+xml", (
                        media.headers
                    )
                    assert media.body() == image
                    with closing(sqlite3.connect(record_path)) as record:
                        added = record.execute(
                            "select card_id, to_deck, kind from card_change order by id"
                        ).fetchall()
                        assert len(added) == 12 and all(
                            row[2] == "added" for row in added
                        ), added
                        assert ("study-absolute-value", "Basics.md", "added") in added
                        content = record.execute(
                            "select c.front, c.back, c.assets from content c join card_change a on a.content=c.id where a.card_id='study-absolute-value'"
                        ).fetchone()
                        assert content[:2] == (
                            r"Evaluate $\abs{-2}$.",
                            r"$\abs{-2}=2$.",
                        ), content
                        assert (
                            store / "record-assets" / (content[2] + ".json")
                        ).is_file()
                        retained_image = record.execute(
                            "select m.name, m.digest from media m join card_change a on a.content=m.content where a.card_id='study-image'"
                        ).fetchone()
                        assert retained_image == (
                            "triangle.svg",
                            sha256(image).hexdigest(),
                        ), retained_image
                        assert (
                            store / "record-media" / retained_image[1]
                        ).read_bytes() == image
                    page.get_by_text("Basics", exact=True).click()
                    front = page.locator(".side-editor.front .cm-content")
                    expect(front).to_contain_text("Evaluate")
                    page.screenshot(path=str(artifacts / "study-ready.png"))
                    page.wait_for_timeout(2000)
                    page.locator(".card-row-label").nth(1).click()
                    expect(front).to_contain_text("Which shape")
                    # Inspect committed history after the window's navigation.
                    response = api.post(
                        "/api/request",
                        data={"action": "study-open", "workspace": str(workspace)},
                    )
                    assert response.ok, response.text()
                    with closing(sqlite3.connect(record_path)) as record:
                        views = record.execute(
                            "select card_id, deck_path, shown_ms, unfocused_ms from editor_view"
                        ).fetchall()
                    assert len(views) == 1, (
                        f"Leaving a card in the editor must record its view: {views}"
                    )
                    assert views[0][:2] == ("study-absolute-value", "Basics.md"), views
                    assert views[0][2] >= 2000, views
                    assert 0 <= views[0][3] <= views[0][2], views
                    focused = subprocess.check_output(
                        ["xdotool", "getwindowfocus"], text=True
                    ).strip()
                    assert page.evaluate("document.hasFocus()")
                    # One native command owns the timed interval; browser-driver
                    # round trips must not extend the time without focus.
                    subprocess.run(
                        [
                            "xdotool",
                            "windowfocus",
                            "0",
                            "sleep",
                            "1",
                            "windowfocus",
                            focused,
                        ],
                        check=True,
                    )
                    assert page.evaluate("document.hasFocus()")
                    page.locator(".card-row-label").nth(2).click()
                    expect(
                        front.get_by_role("img", name="3 squared, math", exact=True)
                    ).to_be_visible()
                    response = api.post(
                        "/api/request",
                        data={"action": "study-open", "workspace": str(workspace)},
                    )
                    assert response.ok, response.text()
                    with closing(sqlite3.connect(record_path)) as record:
                        assert record.execute(
                            "select count(*) from card_change"
                        ).fetchone() == (12,)
                        views = record.execute(
                            "select card_id, deck_path, shown_ms, unfocused_ms from editor_view order by id"
                        ).fetchall()
                    assert len(views) == 2, views
                    assert views[1][:2] == ("study-image", "Basics.md"), views
                    (artifacts / "focus-events.json").write_text(
                        json.dumps(page.evaluate("window.observedFocus"), indent=2)
                        + "\n"
                    )
                    assert abs(views[1][3] - 1000) <= 100, views
                    (artifacts / "editor-views.json").write_text(
                        json.dumps(views, indent=2) + "\n"
                    )

                    unattached_workspace = root / "unattached-workspace"
                    shutil.copytree(workspace, unattached_workspace)
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_label("Workspace folder").fill(
                        str(unattached_workspace)
                    )
                    page.get_by_role(
                        "button", name="Open workspace", exact=True
                    ).click()
                    expect(
                        page.get_by_role("button", name="Workspace", exact=True)
                    ).to_have_text(unattached_workspace.name)
                    response = api.post(
                        "/api/request",
                        data={
                            "action": "study-open",
                            "workspace": str(unattached_workspace),
                        },
                    )
                    assert response.ok and response.json()["state"] == "Unattached", (
                        response.text()
                    )
                    with closing(sqlite3.connect(record_path)) as record:
                        before_views = record.execute(
                            "select * from editor_view order by id"
                        ).fetchall()
                    assert len(before_views) == 3, before_views
                    chooser = page.get_by_role("dialog", name="Choose a study store")
                    expect(chooser).to_be_visible()
                    expect(chooser).to_contain_text(str(workspace))
                    page.screenshot(path=str(artifacts / "study-store-choice.png"))
                    chooser.get_by_role(
                        "button", name="Keep editing", exact=True
                    ).click()
                    page.get_by_text("Basics", exact=True).click()
                    expect(front).to_contain_text("Evaluate")
                    page.locator(".card-row-label").nth(1).click()
                    expect(front).to_contain_text("Which shape")
                    response = api.post(
                        "/api/request",
                        data={
                            "action": "study-open",
                            "workspace": str(unattached_workspace),
                        },
                    )
                    assert response.ok, response.text()
                    with closing(sqlite3.connect(record_path)) as record:
                        assert (
                            record.execute(
                                "select * from editor_view order by id"
                            ).fetchall()
                            == before_views
                        )
                    assert list(stores.iterdir()) == [store]
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_label("Workspace folder").fill(str(workspace))
                    page.get_by_role(
                        "button", name="Open workspace", exact=True
                    ).click()
                    expect(page.get_by_role("status", name="Study")).to_have_text(
                        "Study cards ready"
                    )
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_role("button", name="Study", exact=True).click()
                    study = page.get_by_role("region", name="Study session")
                    expect(study.locator(".side-editor.front")).to_be_visible()
                    expect(study.locator(".side-editor.back")).to_have_count(0)
                    expect(
                        study.get_by_role("button", name="Good", exact=False)
                    ).to_have_count(0)
                    page.screenshot(path=str(artifacts / "study-front.png"))
                    page.wait_for_timeout(2000)
                    page.keyboard.press("Space")
                    expect(study.locator(".side-editor.back")).to_be_visible()
                    expect(
                        study.get_by_role("button", name="Good", exact=False)
                    ).to_be_visible()
                    page.screenshot(path=str(artifacts / "study-answer.png"))
                    page.wait_for_timeout(1000)
                    page.keyboard.press("3")
                    expect(
                        study.get_by_role("button", name="Show answer", exact=False)
                    ).to_be_visible()
                    with closing(sqlite3.connect(record_path)) as record:
                        response_row = record.execute(
                            "select grade, reveal_ms, grade_ms, recovered from response"
                        ).fetchone()
                        assert response_row[0] == "good" and response_row[3] == 0, (
                            response_row
                        )
                        assert response_row[1] >= 2000 and response_row[2] >= 1000, (
                            response_row
                        )
                    page.keyboard.press("Escape")
                    expect(study).to_have_count(0)
                finally:
                    (artifacts / "initial-window.txt").write_text(page.locator("body").inner_text())
                    browser.close()

                response = api.post(
                    "/api/request",
                    data={
                        "action": "study-begin",
                        "workspace": str(workspace),
                        "scope": {"kind": "workspace"},
                    },
                )
                assert response.ok, response.text()
                session = response.json()["session"]
                offered = response.json()["next"]
                assert offered["state"] == "Card", offered
                first_presentation = offered["presentation"]
                for grade in ("good", "again", "hard", "easy"):
                    assert offered["state"] == "Card", offered
                    assert set(offered["labels"]) == {"again", "hard", "good", "easy"}
                    response = api.post(
                        "/api/request",
                        data={
                            "action": "study-answer",
                            "workspace": str(workspace),
                            "session": session,
                            "presentation": offered["presentation"],
                            "grade": grade,
                            "timing": {
                                "reveal_ms": 2000,
                                "grade_ms": 1000,
                                "unfocused_ms": 0,
                            },
                        },
                    )
                    assert response.ok, response.text()
                    with closing(sqlite3.connect(record_path)) as record:
                        record.row_factory = sqlite3.Row
                        review = record.execute(
                            "select * from review where id=?",
                            (offered["presentation"],),
                        ).fetchone()
                        assert review["card_id"] == offered["card_id"]
                        assert (review["front"], review["back"]) == (
                            offered["front"],
                            offered["back"],
                        )
                        assert review["grade"] == grade
                        assert (
                            review["reveal_ms"],
                            review["grade_ms"],
                            review["unfocused_ms"],
                        ) == (2000, 1000, 0)
                        assert review["before_stability"] is None
                        assert review["after_stability"] > 0
                        interval = review["revlog_ivl"]
                        assert review["offer_" + grade + "_s"] == (
                            interval * 86400 if interval > 0 else -interval
                        )
                        assert review["revlog_time_ms"] == 3000
                    offered = response.json()
                stale = api.post(
                    "/api/request",
                    data={
                        "action": "study-answer",
                        "workspace": str(workspace),
                        "session": session,
                        "presentation": first_presentation,
                        "grade": "easy",
                        "timing": {"reveal_ms": 0, "grade_ms": 0, "unfocused_ms": 0},
                    },
                )
                assert not stale.ok and "StaleCard" in stale.text(), stale.text()
                response = api.post(
                    "/api/request",
                    data={
                        "action": "study-end",
                        "workspace": str(workspace),
                        "session": session,
                    },
                )
                assert response.ok, response.text()
                with closing(sqlite3.connect(record_path)) as record:
                    assert record.execute(
                        "select count(*) from response"
                    ).fetchone() == (5,)
                    assert record.execute(
                        "select cause from session_end where session=?", (session,)
                    ).fetchone() == ("left",)

                # Anki owns the collection exclusively. Stop this isolated test host
                # before inspecting its committed state with Anki's own library.
                response = api.post(
                    "/api/request",
                    data={
                        "action": "study-begin",
                        "workspace": str(workspace),
                        "scope": {"kind": "workspace"},
                    },
                )
                assert response.ok, response.text()
                interrupted_session = response.json()["session"]
                hosts = [
                    process
                    for process in psutil.process_iter(["cmdline"])
                    if process.info["cmdline"] is not None
                    and "study-host" in process.info["cmdline"]
                    and process.environ().get("XDG_DATA_HOME")
                    == os.environ["XDG_DATA_HOME"]
                ]
                assert len(hosts) == 1, hosts
                hosts[0].kill()
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
                    identities = collection.db.all("select guid, flds from notes")
                    assert len(identities) == 12 and all(
                        guid == fields for guid, fields in identities
                    ), identities
                    assert [
                        field["name"]
                        for field in collection.get_note(
                            collection.find_notes("CardId:study-absolute-value")[0]
                        ).note_type()["flds"]
                    ] == ["CardId"]
                    assert collection.get_config("fsrs") is True
                    assert collection.get_config("applyAllParentLimits") is True
                    preset = collection.decks.get_config(1)
                    assert preset["lapse"]["leechAction"] == 1
                    assert preset["reviewOrder"] == 7
                    assert preset["maxTaken"] == 9999
                finally:
                    collection.close()

                collection = Collection(str(store / "collection.anki2"))
                try:
                    queued = collection.sched.get_queued_cards(fetch_limit=1).cards[0]
                    card = collection.get_card(queued.card.id)
                    card.start_timer()
                    collection.sched.answer_card(
                        collection.sched.build_answer(
                            card=card, states=queued.states, rating=CardAnswer.EASY
                        )
                    )
                    collection.sched.set_due_date([card.id], "7")
                    revlogs = [
                        tuple(row)
                        for row in collection.db.all(
                            "select id,cid,usn,ease,ivl,lastIvl,factor,time,type from revlog order by id"
                        )
                    ]
                    assert len(revlogs) == 7, revlogs
                finally:
                    collection.close()
                response = api.post(
                    "/api/request",
                    data={"action": "study-open", "workspace": str(workspace)},
                )
                assert response.ok, response.text()
                with closing(sqlite3.connect(record_path)) as record:
                    recorded = record.execute(
                        "select revlog_id,revlog_cid,revlog_usn,revlog_ease,revlog_ivl,revlog_last_ivl,revlog_factor,revlog_time_ms,revlog_type from response order by revlog_id"
                    ).fetchall()
                    assert recorded == revlogs, (recorded, revlogs)
                    recovered = record.execute(
                        "select presentation,reveal_ms,grade_ms,unfocused_ms,after_interval_days,after_due,after_stability,after_difficulty from response where recovered=1"
                    ).fetchall()
                    assert recovered == [(None,) * 8, (None,) * 8], recovered
                    assert record.execute(
                        "select cause from session_end where session=?",
                        (interrupted_session,),
                    ).fetchone() == ("recovered",)

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
                assert summary[0]["cards"] == 12 and summary[0]["responses"] == 7
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
                browser = playwright.chromium.launch(headless=False)
                page = browser.new_page()
                try:
                    page.goto("http://127.0.0.1:1420")
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_label("Workspace folder").fill(str(workspace))
                    page.get_by_role(
                        "button", name="Open workspace", exact=True
                    ).click()
                    chooser = page.get_by_role("dialog", name="Choose a study store")
                    expect(chooser).to_be_visible()
                    chooser.get_by_role("button", name="Start new", exact=True).click()
                    expect(chooser).to_have_count(0)
                    expect(page.get_by_role("status", name="Study")).to_have_text(
                        "Study cards ready"
                    )
                finally:
                    browser.close()
                response = api.post(
                    "/api/request",
                    data={"action": "study-open", "workspace": str(workspace)},
                )
                assert response.ok, response.text()
                assert response.json()["store"] != str(store)
                fresh_record = Path(response.json()["record"])
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
                unknown = response.json()
                assert unknown["kind"] == "UnknownStore", response.text()
                assert set(stores.iterdir()) == before

                browser = playwright.chromium.launch(headless=False)
                page = browser.new_page()
                try:
                    page.goto("http://127.0.0.1:1420")
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_label("Workspace folder").fill(str(workspace))
                    page.get_by_role(
                        "button", name="Open workspace", exact=True
                    ).click()
                    expect(page.get_by_role("status", name="Study")).to_have_text(
                        "Study cards ready"
                    )
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_role("button", name="Study", exact=True).click()
                    study = page.get_by_role("region", name="Study session")
                    seen = set()
                    for remaining in range(12, 0, -1):
                        expect(study.get_by_label("Remaining cards")).to_contain_text(
                            f"New: {remaining}"
                        )
                        expect(
                            study.get_by_role("button", name="Show answer", exact=False)
                        ).to_be_visible()
                        with closing(sqlite3.connect(fresh_record)) as record:
                            identity = record.execute(
                                "select card_id from presentation order by id desc limit 1"
                            ).fetchone()[0]
                        seen.add(identity)
                        if identity == "study-image":
                            picture = study.get_by_role(
                                "img", name="A triangle", exact=True
                            )
                            expect(picture).to_be_visible()
                            expect(picture).to_have_attribute(
                                "src", re.compile("^blob:")
                            )
                            expect(picture).to_have_js_property("complete", True)
                            assert picture.evaluate(
                                "image => image.complete && image.naturalWidth > 0"
                            )
                            page.screenshot(path=str(artifacts / "study-image.png"))
                            page.set_viewport_size({"width": 760, "height": 620})
                            expect(picture).to_be_in_viewport()
                            expect(
                                study.get_by_role(
                                    "button", name="Show answer", exact=False
                                )
                            ).to_be_in_viewport()
                            page.screenshot(
                                path=str(artifacts / "study-image-small.png")
                            )
                            page.set_viewport_size({"width": 1280, "height": 720})
                        if identity == "study-diagram":
                            expect(
                                study.get_by_role(
                                    "img", name="Rendered commutative diagram"
                                )
                            ).to_be_visible(timeout=15000)
                            page.screenshot(path=str(artifacts / "study-diagram.png"))
                        if identity == "study-absolute-value":
                            expect(study.locator("mjx-container")).to_have_count(1)
                            page.screenshot(path=str(artifacts / "study-macro.png"))
                        page.keyboard.press("Space")
                        if identity == "study-image":
                            referenced = study.get_by_role("img", name="Collapsed triangle", exact=True)
                            expect(referenced).to_be_visible()
                            expect(referenced).to_have_js_property("complete", True)
                            assert referenced.evaluate("image => image.naturalWidth > 0")
                        expect(
                            study.get_by_role("button", name="Easy", exact=False)
                        ).to_be_visible()
                        page.keyboard.press("4")
                    expect(
                        study.get_by_role("heading", name="Study complete for now")
                    ).to_be_visible()
                    expect(study).to_contain_text("Graded today: 12")
                    assert {
                        "study-image",
                        "study-diagram",
                        "study-absolute-value",
                    } <= seen
                    page.screenshot(path=str(artifacts / "study-finished.png"))
                    with closing(sqlite3.connect(fresh_record)) as record:
                        assert record.execute(
                            "select count(*) from response"
                        ).fetchone() == (12,)
                        assert record.execute(
                            "select cause from session_end"
                        ).fetchall() == [("finished",)]
                    page.keyboard.press("Escape")
                    expect(study).to_have_count(0)
                    with closing(sqlite3.connect(fresh_record)) as record:
                        tables = [
                            row[0]
                            for row in record.execute(
                                "select name from sqlite_master where type='table'"
                            )
                        ]
                        before_rows = {
                            table: record.execute(
                                f'select * from "{table}" order by id'
                            ).fetchall()
                            for table in tables
                        }
                    moved_workspace = root / "moved-workspace"
                    workspace.rename(moved_workspace)
                    before_stores = set(stores.iterdir())
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_label("Workspace folder").fill(str(moved_workspace))
                    page.get_by_role(
                        "button", name="Open workspace", exact=True
                    ).click()
                    chooser = page.get_by_role("dialog", name="Choose a study store")
                    expect(chooser).to_be_visible()
                    expect(chooser).to_contain_text("Grades: 12")
                    page.screenshot(path=str(artifacts / "study-store-moved.png"))
                    chooser.get_by_role(
                        "button", name=f"Attach {workspace}", exact=True
                    ).click()
                    expect(chooser).to_have_count(0)
                    expect(page.get_by_role("status", name="Study")).to_have_text(
                        "Study cards ready"
                    )
                    assert set(stores.iterdir()) == before_stores
                    metadata = json.loads(
                        (fresh_record.parent / "store.json").read_text()
                    )
                    assert metadata["paths"][-1]["path"] == str(moved_workspace)
                    with closing(sqlite3.connect(fresh_record)) as record:
                        for table, rows in before_rows.items():
                            after = record.execute(
                                f'select * from "{table}" order by id'
                            ).fetchall()
                            assert after[: len(rows)] == rows, table
                finally:
                    browser.close()

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
                failures = [
                    json.loads(line)
                    for log in diagnostics.glob("*/events.jsonl")
                    for line in log.read_text().splitlines()
                    if json.loads(line).get("outcome") == "error"
                ]
                assert any(
                    event["error_message"] == unknown["message"] and event["traceback"]
                    for event in failures
                ), failures
            finally:
                api.dispose()
                diagnostics = (
                    Path(os.environ["XDG_STATE_HOME"])
                    / "math-flashcards"
                    / "diagnostics"
                )
                if diagnostics.is_dir():
                    shutil.copytree(diagnostics, artifacts / "application")


if __name__ == "__main__":
    with evidence("study", Path(__file__).parent / "fixtures" / "study") as artifacts:
        main(artifacts)
