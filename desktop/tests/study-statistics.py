# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Read Statistics during Study without changing the learning record."""

import math
import os
import sqlite3
import tempfile
import time
from contextlib import closing
from pathlib import Path

import psutil
from anki.cards_pb2 import FsrsMemoryState
from anki.collection import Collection
from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="flashcards-statistics-") as directory:
        workspace = Path(directory)
        (workspace / "Algebra").mkdir()
        (workspace / "Algebra/Recall.md").write_text(
            "".join(
                f'::: {{.front card-id="recall-{i}"}}\nRecall {i}.\n:::\n\n'
                f'::: {{.back card-id="recall-{i}"}}\nAnswer {i}.\n:::\n\n'
                for i in range(3)
            )
        )
        with sync_playwright() as playwright:
            api = playwright.request.new_context(
                base_url="http://127.0.0.1:1420",
                extra_http_headers={"x-flashcards": "1"},
            )

            def request(action: str, **values):
                response = api.post("/api/request", data={"action": action, **values})
                assert response.ok, response.text()
                return response.json()

            def window():
                browser = playwright.chromium.launch(headless=False)
                page = browser.new_page(viewport={"width": 900, "height": 700})
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready", timeout=30000
                )
                return browser, page

            browser, page = window()
            opened = request("study-open", workspace=str(workspace))
            browser.close()
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
            collection = Collection(str(Path(opened["store"]) / "collection.anki2"))
            try:
                for identity in collection.find_cards(""):
                    card = collection.get_card(identity)
                    card.type = card.queue = 2
                    card.ivl = 10
                    card.due = collection.sched.today
                    card.reps = 5
                    card.memory_state = FsrsMemoryState(stability=10, difficulty=5)
                    card.last_review_time = int(time.time()) - 10 * 86400
                    collection.update_card(card)
            finally:
                collection.close()
            browser, page = window()
            try:
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_role("button", name="Study", exact=True).click()
                study = page.get_by_role("region", name="Study session")
                for undo in (True, False, False):
                    study.get_by_role("button", name="Show answer", exact=False).click()
                    shown = study.locator(".side-editor.front .cm-content").inner_text()
                    study.get_by_role("button", name="Easy", exact=False).click()
                    expect(
                        study.get_by_role("button", name="Show answer", exact=False)
                    ).to_be_visible()
                    if undo:
                        page.keyboard.press("Control+z")
                        expect(
                            study.locator(".side-editor.front .cm-content")
                        ).to_have_text(shown)
                        expect(
                            study.get_by_role("button", name="Show answer", exact=False)
                        ).to_be_visible()
                        expect(
                            study.get_by_role("button", name="Undo", exact=True)
                        ).to_be_disabled()
                # The remaining card is revealed: Statistics must own its keys.
                study.get_by_role("button", name="Show answer", exact=False).click()
                with closing(sqlite3.connect(opened["record"])) as record:
                    before = list(record.iterdump())
                    recall = [
                        list(row)
                        for row in record.execute(
                            "select folder,strftime('%Y-%m',at_ms / 1000,'unixepoch') as month,count(*),avg(grade='again'),avg(reveal_ms) from review where undone_at_ms is null group by folder,month order by folder,month"
                        )
                    ]
                    reviews = record.execute(
                        "select count(*) from review where kind='review' and grade is not null and undone_at_ms is null"
                    ).fetchone()[0]
                assert reviews == 2
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_role("button", name="Statistics", exact=True).click()
                dialog = page.get_by_role("dialog", name="Statistics")
                catalog = request("analysis-list")
                for item in catalog:
                    expect(dialog).to_contain_text(item["summary"])
                    assert "self-graded" in item["summary"]
                    dialog.get_by_role("button", name=item["title"], exact=True).click()
                    table = dialog.get_by_role("table", name=item["title"], exact=True)
                    expect(table).to_be_visible()
                    result = request(
                        "analysis-run", record=opened["record"], name=item["name"]
                    )
                    if item["name"] == "recall_by_folder":
                        assert result["rows"] == recall
                        assert "recall of the cards" in item["summary"]
                    else:
                        assert sum(row[1] for row in result["rows"]) == reviews
                    rows = table.locator("tbody tr")
                    expect(rows).to_have_count(len(result["rows"]))
                    for index, expected in enumerate(result["rows"]):
                        cells = rows.nth(index).locator("td").all_text_contents()
                        for actual, value in zip(cells, expected, strict=True):
                            if isinstance(value, (float, int)):
                                assert math.isclose(
                                    float(actual.replace(",", "")),
                                    value,
                                    rel_tol=1e-5,
                                    abs_tol=1e-5,
                                ), (actual, value)
                            else:
                                assert actual == ("—" if value is None else value)
                    with closing(sqlite3.connect(opened["record"])) as record:
                        assert list(record.iterdump()) == before
                    page.screenshot(path=str(artifacts / f"{item['name']}.png"))
                page.keyboard.press("1")
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert list(record.iterdump()) == before
                page.keyboard.press("Escape")
                expect(dialog).not_to_be_visible()
                expect(study).to_be_visible()
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert record.execute(
                        "select count(*) from response"
                    ).fetchone() == (4,)
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
                api.dispose()


if __name__ == "__main__":
    with evidence(
        "study-statistics", Path(__file__).parent / "fixtures/study"
    ) as artifacts:
        main(artifacts)
