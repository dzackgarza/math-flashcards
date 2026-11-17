# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright", "psutil"]
# ///
"""Correct a Study grade and edit a card without losing recorded history."""

import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

import psutil
from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(
        prefix="flashcards-study-corrections-"
    ) as directory:
        workspace = Path(directory)
        (workspace / "Corrections.md").write_text(
            "".join(
                f'::: {{.front card-id="{identity}"}}\nRecall {identity}.\n:::\n\n'
                f'::: {{.back card-id="{identity}"}}\nOriginal {identity}.\n:::\n\n'
                for identity in ("first", "second")
            )
        )
        with sync_playwright() as playwright:
            api = playwright.request.new_context(
                base_url="http://127.0.0.1:1420",
                extra_http_headers={"x-flashcards": "1"},
            )
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page(viewport={"width": 900, "height": 700})
            errors: list[str] = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            try:
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready", timeout=30000
                )
                opened = api.post(
                    "/api/request",
                    data={"action": "study-open", "workspace": str(workspace)},
                )
                assert opened.ok, opened.text()
                store = opened.json()
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_role("button", name="Study", exact=True).click()
                study = page.get_by_role("region", name="Study session")
                show = study.get_by_role("button", name="Show answer", exact=False)
                expect(show).to_be_visible()
                undo = study.get_by_role("button", name="Undo", exact=True)
                expect(undo).to_be_disabled()
                with closing(sqlite3.connect(store["record"])) as record:
                    first = record.execute(
                        "select card_id from presentation order by id desc limit 1"
                    ).fetchone()[0]

                def schedule(identity: str):
                    with closing(
                        sqlite3.connect(f"file:{store['record']}?mode=ro", uri=True)
                    ) as record:
                        return record.execute(
                            "select before_interval_days,before_due,before_reps,before_lapses,before_stability,before_difficulty from presentation where card_id=? order by id desc limit 1",
                            (identity,),
                        ).fetchone()

                before = schedule(first)
                show.click()
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(show).to_be_visible()
                expect(undo).to_be_enabled()
                page.keyboard.press("Control+z")
                expect(study).to_contain_text(f"Recall {first}.")
                expect(show).to_be_visible()
                assert schedule(first) == before
                with closing(sqlite3.connect(store["record"])) as record:
                    reviews = record.execute(
                        "select card_id,grade,undone_at_ms from review where grade is not null order by id"
                    ).fetchall()
                    assert (
                        len(reviews) == 1
                        and reviews[0][:2] == (first, "easy")
                        and reviews[0][2] is not None
                    ), reviews
                    assert record.execute(
                        "select count(*) from undo u join response r on r.id=u.response where r.card_id=?",
                        (first,),
                    ).fetchone() == (1,)
                    assert (
                        record.execute(
                            "select count(*) from presentation where card_id=?",
                            (first,),
                        ).fetchone()[0]
                        >= 2
                    )
                page.keyboard.press("e")
                back = page.locator(".side-editor.back .cm-content")
                expect(back).to_have_text(f"Original {first}.")
                back.click()
                page.keyboard.press("Control+a")
                page.keyboard.insert_text(f"Corrected {first}.")
                page.screenshot(path=str(artifacts / "editor-return.png"))
                page.get_by_role("button", name="Return to Study", exact=True).click()
                expect(show).to_be_visible()
                expect(undo).to_be_disabled()
                expect(undo).to_have_attribute(
                    "title", "A card changed. Grade a card to enable Undo."
                )
                show.click()
                expect(study).to_contain_text(f"Corrected {first}.")
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(show).to_be_visible()
                expect(undo).to_be_enabled()
                with closing(sqlite3.connect(store["record"])) as record:
                    second = record.execute(
                        "select card_id from presentation order by id desc limit 1"
                    ).fetchone()[0]
                assert second != first
                second_before = schedule(second)
                show.click()
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                expect(undo).to_be_enabled()
                page.keyboard.press("Control+z")
                expect(show).to_be_visible()
                expect(study).to_contain_text(f"Recall {second}.")
                assert schedule(second) == second_before
                with closing(sqlite3.connect(store["record"])) as record:
                    rows = record.execute(
                        "select card_id,back,undone_at_ms from review where grade is not null order by id"
                    ).fetchall()
                    assert [(row[0], row[1], row[2] is not None) for row in rows] == [
                        (first, f"Original {first}.", True),
                        (first, f"Corrected {first}.", False),
                        (second, f"Original {second}.", True),
                    ], rows
                    assert record.execute(
                        "select count(*) from session_end where cause='finished'"
                    ).fetchone() == (1,)
                    assert record.execute(
                        "select count(*) from session"
                    ).fetchone() == (2,)
                    kept = record.execute(
                        "select revlog_id from review where undone_at_ms is null and revlog_id is not null"
                    ).fetchall()
                page.screenshot(path=str(artifacts / "corrected-study.png"))
                # Successive undos use Anki's returned operation counter, not
                # UndoStatus.last_step, which is a sequence counter.
                page.keyboard.press("Control+z")
                expect(study).to_contain_text(f"Recall {first}.")
                expect(undo).to_be_disabled()
                assert schedule(first) == before
                with closing(sqlite3.connect(store["record"])) as record:
                    assert record.execute("select count(*) from undo").fetchone() == (
                        3,
                    )
                    kept = record.execute(
                        "select revlog_id from review where undone_at_ms is null and revlog_id is not null"
                    ).fetchall()
                    assert kept == []
                expect(page.get_by_role("alert")).to_have_count(0)
                assert not errors, errors
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
                api.dispose()
            hosts = [
                p
                for p in psutil.process_iter(["cmdline"])
                if p.info["cmdline"] is not None
                and "study-host" in p.info["cmdline"]
                and p.environ().get("XDG_DATA_HOME") == os.environ["XDG_DATA_HOME"]
            ]
            assert len(hosts) == 1
            hosts[0].terminate()
            hosts[0].wait(timeout=10)
            with closing(
                sqlite3.connect(
                    f"file:{store['store']}/collection.anki2?mode=ro", uri=True
                )
            ) as collection:
                assert (
                    collection.execute("select id from revlog order by id").fetchall()
                    == kept
                )


if __name__ == "__main__":
    with evidence(
        "study-corrections", Path(__file__).parent / "fixtures/study"
    ) as artifacts:
        main(artifacts)
