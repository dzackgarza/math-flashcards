# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Grade native cards with each keyboard choice and inspect Anki's review rows."""

import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

import psutil
from anki.collection import Collection
from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
    grades = ("again", "hard", "good", "easy")
    with tempfile.TemporaryDirectory(prefix="flashcards-study-keys-") as directory:
        workspace = Path(directory)
        for grade in grades:
            (workspace / f"{grade}.md").write_text(
                f'::: {{.front card-id="{grade}"}}\nRecall {grade}.\n:::\n\n'
                f'::: {{.back card-id="{grade}"}}\nAnswer {grade}.\n:::\n'
            )
        with sync_playwright() as playwright:
            api = playwright.request.new_context(
                base_url="http://127.0.0.1:1420",
                extra_http_headers={"x-flashcards": "1"},
            )
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
                opened = api.post(
                    "/api/request",
                    data={"action": "study-open", "workspace": str(workspace)},
                )
                assert opened.ok, opened.text()
                store = opened.json()
                for number, grade in enumerate(grades, 1):
                    page.locator(".tree-row").filter(
                        has=page.get_by_label(
                            f"Study counts for {grade}.md", exact=True
                        )
                    ).click(button="right")
                    with page.expect_response(
                        lambda response: (
                            response.url.endswith("/api/request")
                            and response.request.post_data_json.get("action")
                            == "study-begin"
                        )
                    ) as begun:
                        page.get_by_role("menuitem", name="Study", exact=True).click()
                    assert begun.value.ok, begun.value.text()
                    offered = begun.value.json()["next"]
                    assert offered["card_id"] == grade
                    study = page.get_by_role("region", name="Study session")
                    expect(study).to_contain_text(f"Recall {grade}.")
                    expect(study.locator(".side-editor.back")).not_to_be_visible()
                    expect(
                        study.get_by_role("button", name="Easy", exact=False)
                    ).not_to_be_visible()
                    (artifacts / f"focus-before-{grade}.txt").write_text(
                        page.evaluate("document.activeElement.outerHTML")
                    )
                    page.keyboard.press("Space")
                    expect(study).to_contain_text(f"Answer {grade}.")
                    for choice in grades:
                        expect(
                            study.get_by_role(
                                "button", name=choice.title(), exact=False
                            )
                        ).to_contain_text(offered["labels"][choice])
                    with page.expect_response(
                        lambda response: (
                            response.url.endswith("/api/request")
                            and response.request.post_data_json.get("action")
                            == "study-answer"
                        )
                    ) as answered:
                        page.keyboard.press(str(number))
                    assert answered.value.ok, answered.value.text()
                    with closing(sqlite3.connect(store["record"])) as record:
                        record.row_factory = sqlite3.Row
                        review = record.execute(
                            "select * from review where id=?",
                            (offered["presentation"],),
                        ).fetchone()
                        assert review["grade"] == grade
                        interval = review["revlog_ivl"]
                        assert review[f"offer_{grade}_s"] == (
                            interval * 86400 if interval > 0 else -interval
                        )
                        assert (
                            record.execute("select count(*) from response").fetchone()[
                                0
                            ]
                            == number
                        )
                    page.keyboard.press("Escape")
                    expect(study).not_to_be_visible()
                with closing(sqlite3.connect(store["record"])) as record:
                    responses = record.execute(
                        "select revlog_id,revlog_cid,revlog_usn,revlog_ease,revlog_ivl,revlog_last_ivl,revlog_factor,revlog_time_ms,revlog_type from response order by revlog_id"
                    ).fetchall()
                assert [row[3] for row in responses] == [1, 2, 3, 4]
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
                api.dispose()
        hosts = [
            process
            for process in psutil.process_iter(["cmdline"])
            if process.info["cmdline"]
            and "study-host" in process.info["cmdline"]
            and process.environ().get("XDG_DATA_HOME") == os.environ["XDG_DATA_HOME"]
        ]
        assert len(hosts) == 1
        hosts[0].kill()
        hosts[0].wait(timeout=10)
        collection = Collection(str(Path(store["store"]) / "collection.anki2"))
        try:
            assert collection.db.all(
                "select id,cid,usn,ease,ivl,lastIvl,factor,time,type from revlog order by id"
            ) == [list(row) for row in responses]
        finally:
            collection.close()


if __name__ == "__main__":
    with evidence("study-keys", Path(__file__).parent / "fixtures/study") as artifacts:
        main(artifacts)
