# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Change Study settings through the window and inspect the resulting schedule."""

import json
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

            def open_window(*, new_store: bool = False):
                browser = playwright.chromium.launch(headless=False)
                page = browser.new_page(viewport={"width": 900, "height": 700})
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                if new_store:
                    page.get_by_role("button", name="Start new", exact=True).click()
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
                page.screenshot(path=str(artifacts / "settings-form.png"))
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
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert record.execute(
                        "select count(*) from response"
                    ).fetchone() == (3,)
                    settings = record.execute(
                        'select key,"before","after" from setting_change order by id'
                    ).fetchall()
                    assert [
                        (key, json.loads(before), json.loads(after))
                        for key, before, after in settings
                    ] == [("new_per_day", 20, 3), ("desired_retention", 0.9, 0.95)], (
                        settings
                    )
                    assert record.execute(
                        "select distinct new_per_day,reviews_per_day,desired_retention from review where grade is not null"
                    ).fetchall() == [(3, 200, 0.95)]
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()

            def stop_host():
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

            stop_host()
            assert request("study-open")["settings"] == {
                "new_per_day": 3,
                "reviews_per_day": 200,
                "desired_retention": 0.95,
            }
            # A separate workspace has no new cards introduced today. Anki's
            # review limit includes those introductions unless configured otherwise.
            source = (workspace / "Settings.md").read_text()
            workspace = workspace / "Reviews"
            workspace.mkdir()
            (workspace / "Settings.md").write_text(source)
            browser, page = open_window(new_store=True)
            opened = request("study-open")
            browser.close()
            stop_host()
            # Dated review states belong to Anki. Prepare five due cards through
            # its library, then exercise queue order and limits through the UI.
            collection = Collection(str(Path(opened["store"]) / "collection.anki2"))
            try:
                cards = collection.find_cards("")[:5]
                for identity, stability in zip(cards, (40, 5, 80, 10, 20), strict=True):
                    card = collection.get_card(identity)
                    card.type = card.queue = 2
                    card.ivl = 30
                    card.due = collection.sched.today - 10
                    card.reps = 10
                    card.memory_state = FsrsMemoryState(
                        stability=stability, difficulty=5
                    )
                    card.last_review_time = int(time.time()) - 40 * 86400
                    collection.update_card(card)
            finally:
                collection.close()
            browser, page = open_window()
            try:
                study = page.get_by_role("region", name="Study session")

                def settings(new: str, reviews: str, retention: str):
                    study.get_by_role(
                        "button", name="Study settings", exact=True
                    ).click()
                    dialog = page.get_by_role("dialog", name="Study settings")
                    dialog.get_by_label("New cards per day", exact=True).fill(new)
                    dialog.get_by_label("Reviews per day", exact=True).fill(reviews)
                    dialog.get_by_label("Target recall", exact=True).fill(retention)
                    dialog.get_by_label("Target recall", exact=True).press("End")
                    dialog.get_by_label("Target recall", exact=True).press("1")
                    dialog.get_by_label("Target recall", exact=True).press("Backspace")
                    dialog.get_by_role(
                        "button", name="Save settings", exact=True
                    ).click()
                    expect(dialog).not_to_be_visible()

                def current():
                    with closing(sqlite3.connect(opened["record"])) as record:
                        return record.execute(
                            "select card_id,before_interval_days,before_due,before_reps,before_lapses,before_stability,before_difficulty,offer_good_s from presentation order by id desc limit 1"
                        ).fetchone()

                settings("0", "2", "0.80")
                expect(study.get_by_label("Remaining cards")).to_have_text(
                    "New: 0Learning: 0Review: 2"
                )
                lower = current()
                settings("0", "2", "0.98")
                higher = current()
                assert lower[:-1] == higher[:-1], (lower, higher)
                assert higher[-1] < lower[-1], (lower, higher)
                study.get_by_role("button", name="Show answer", exact=False).click()
                # Numeric edits must not grade the card behind the modal.
                settings("0", "2", "0.98")
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert record.execute(
                        "select count(*) from response"
                    ).fetchone() == (0,)
                    before = record.execute(
                        "select count(*) from setting_change"
                    ).fetchone()
                for key, value in (
                    ("new_per_day", -1),
                    ("reviews_per_day", 10000),
                    ("desired_retention", 1.0),
                ):
                    invalid = {
                        "new_per_day": 0,
                        "reviews_per_day": 2,
                        "desired_retention": 0.98,
                        key: value,
                    }
                    response = api.post(
                        "/api/request",
                        data={
                            "action": "study-set-settings",
                            "workspace": str(workspace),
                            "settings": invalid,
                        },
                    )
                    assert response.status == 422, response.text()
                    assert response.json()["kind"] == "InvalidSettings", response.text()
                assert request("study-open")["settings"] == {
                    "new_per_day": 0,
                    "reviews_per_day": 2,
                    "desired_retention": 0.98,
                }
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert (
                        record.execute("select count(*) from setting_change").fetchone()
                        == before
                    )
                for _ in range(2):
                    study.get_by_role("button", name="Show answer", exact=False).click()
                    study.get_by_role("button", name="Good", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                settings("0", "5", "0.98")
                expect(study.get_by_label("Remaining cards")).to_contain_text(
                    "Review: 3"
                )
                for _ in range(3):
                    study.get_by_role("button", name="Show answer", exact=False).click()
                    study.get_by_role("button", name="Good", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                with closing(sqlite3.connect(opened["record"])) as record:
                    reviews = record.execute(
                        "select before_retrievability,reviews_per_day,desired_retention from review where grade is not null and kind='review' order by id"
                    ).fetchall()
                    assert len(reviews) == 5, reviews
                    probabilities = [row[0] for row in reviews]
                    assert len(set(probabilities)) == 5 and probabilities == sorted(
                        probabilities
                    ), reviews
                    assert [row[1:] for row in reviews] == [(2, 0.98)] * 2 + [
                        (5, 0.98)
                    ] * 3, reviews
                    (artifacts / "review-order.json").write_text(
                        json.dumps(reviews, indent=2)
                    )
                page.screenshot(path=str(artifacts / "review-limit.png"))
            finally:
                (artifacts / "review-window.txt").write_text(
                    page.locator("body").inner_text()
                )
                browser.close()
            api.dispose()


if __name__ == "__main__":
    with evidence(
        "study-settings", Path(__file__).parent / "fixtures/study"
    ) as artifacts:
        main(artifacts)
