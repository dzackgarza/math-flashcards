# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Change Study settings through the window and inspect the resulting schedule."""

import json
import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

import psutil
from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="flashcards-study-settings-") as directory:
        workspace = Path(directory)
        (workspace / "Settings.md").write_text(
            "".join(
                f'::: {{.front card-id="card-{i}"}}\nRecall {i}.\n:::\n\n'
                f'::: {{.back card-id="card-{i}"}}\nAnswer {i}.\n:::\n\n'
                for i in range(6)
            )
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

            def open_window():
                browser = playwright.chromium.launch(headless=False)
                page = browser.new_page(viewport={"width": 900, "height": 700})
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready", timeout=30000
                )
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_role("button", name="Study", exact=True).click()
                expect(page.get_by_role("region", name="Study session")).to_be_visible()
                return browser, page

            browser, page = open_window()
            try:
                opened = request("study-open")
                study = page.get_by_role("region", name="Study session")
                study.get_by_role("button", name="Study settings", exact=True).click()
                dialog = page.get_by_role("dialog", name="Study settings")
                dialog.get_by_label("New cards per day", exact=True).fill("3")
                dialog.get_by_label("Target recall", exact=True).fill("1.0")
                dialog.get_by_role("button", name="Save settings", exact=True).click()
                expect(dialog).to_contain_text("0.70 to 0.99")
                assert request("study-open")["settings"] == opened["settings"]
                dialog.get_by_label("Target recall", exact=True).fill("0.95")
                dialog.get_by_role("button", name="Save settings", exact=True).click()
                expect(dialog).not_to_be_visible()
                expect(study.get_by_label("Remaining cards")).to_contain_text("New: 3")
                assert request("study-counts")["counts"]["new"] == 3
                page.screenshot(path=str(artifacts / "settings-counts.png"))
                for _ in range(3):
                    study.get_by_role("button", name="Show answer", exact=False).click()
                    study.get_by_role("button", name="Easy", exact=False).click()
                expect(study.get_by_role("heading", name="Study complete for now")).to_be_visible()
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert record.execute("select count(*) from response").fetchone() == (3,)
                    settings = record.execute(
                        'select key,"before","after" from setting_change order by id'
                    ).fetchall()
                    assert [(key, json.loads(before), json.loads(after)) for key, before, after in settings] == [
                        ("new_per_day", 20, 3), ("desired_retention", 0.9, 0.95)
                    ], settings
                    assert record.execute(
                        "select distinct new_per_day,reviews_per_day,desired_retention from review where grade is not null"
                    ).fetchall() == [(3, 200, 0.95)]
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
            hosts = [
                p for p in psutil.process_iter(["cmdline"])
                if p.info["cmdline"] is not None and "study-host" in p.info["cmdline"]
                and p.environ().get("XDG_DATA_HOME") == os.environ["XDG_DATA_HOME"]
            ]
            assert len(hosts) == 1
            hosts[0].terminate()
            hosts[0].wait(timeout=10)
            assert request("study-open")["settings"] == {
                "new_per_day": 3, "reviews_per_day": 200, "desired_retention": 0.95
            }
            api.dispose()


if __name__ == "__main__":
    with evidence("study-settings", Path(__file__).parent / "fixtures/study") as artifacts:
        main(artifacts)
