# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Inspect, reject, and accept an Anki parameter fit through Study settings."""

import json
import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

import psutil
from anki.collection import Collection
from anki.decks import DeckConfigId
from evidence import evidence
from fit_history import add_history
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="flashcards-study-fit-") as directory:
        workspace = Path(directory)
        (workspace / "Fit.md").write_text(
            '::: {.front card-id="fit-card"}\nRecall.\n:::\n\n'
            '::: {.back card-id="fit-card"}\nAnswer.\n:::\n'
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
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_role("button", name="Study", exact=True).click()
                page.get_by_role("button", name="Study settings", exact=True).click()
                return browser, page

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

            browser, page = window()
            opened = request("study-open")

            def record_dump():
                with closing(
                    sqlite3.connect(f"file:{opened['record']}?mode=ro", uri=True)
                ) as record:
                    return list(record.iterdump())

            try:
                before = record_dump()
                page.get_by_role("button", name="Fit scheduler", exact=True).click()
                expect(page.get_by_role("alert")).to_contain_text(
                    "Insufficient review history"
                )
                assert record_dump() == before
                page.screenshot(path=str(artifacts / "empty-history.png"))
            finally:
                (artifacts / "empty-window.txt").write_text(
                    page.locator("body").inner_text()
                )
                browser.close()
            stop_host()
            collection = Collection(str(Path(opened["store"]) / "collection.anki2"))
            try:
                add_history(collection, collection.find_cards("")[0], 2)
                preset = collection.decks.get_config(DeckConfigId(1))
                original = preset["fsrsParams6"]
            finally:
                collection.close()
            browser, page = window()
            try:
                before = record_dump()
                fit = request("study-fit")
                assert fit["reviews"] == 1, fit
                page.get_by_role("button", name="Fit scheduler", exact=True).click()
                result = page.get_by_role("region", name="Scheduler fit")
                expect(result).to_be_visible()
                expect(result).to_contain_text("Review observations used: 1")
                for value in ("Current", "Fitted", "Log loss", "RMSE", "parameters"):
                    expect(result).to_contain_text(value)
                assert record_dump() == before
                page.screenshot(path=str(artifacts / "fit.png"))
                result.get_by_role("button", name="Close fit", exact=True).click()
                expect(result).not_to_be_visible()
                assert record_dump() == before
                page.get_by_role("button", name="Fit scheduler", exact=True).click()
                expect(result).to_be_visible()
                result.get_by_role("button", name="Apply fit", exact=True).click()
                expect(
                    page.get_by_role("dialog", name="Study settings")
                ).not_to_be_visible()
                expect(
                    page.get_by_role("button", name="Show answer", exact=False)
                ).to_be_visible()
                with closing(sqlite3.connect(opened["record"])) as record:
                    rows = record.execute(
                        "select id,parameters,source,reviews,log_loss,rmse_bins from parameter_set order by id"
                    ).fetchall()
                    assert len(rows) == 2, rows
                    assert (
                        json.loads(rows[0][1]) == original
                        and rows[0][2] == "anki-default"
                    )
                    assert json.loads(rows[1][1]) == fit["parameters"]
                    assert rows[1][2:] == (
                        "fit",
                        fit["reviews"],
                        fit["log_loss"],
                        fit["rmse_bins"],
                    ), rows
                    change = record.execute(
                        'select key,"before","after" from setting_change'
                    ).fetchall()
                    assert len(change) == 1 and change[0][0] == "fsrsParams6", change
                    assert (
                        json.loads(change[0][1]) == original
                        and json.loads(change[0][2]) == fit["parameters"]
                    )
                    assert record.execute(
                        "select parameter_set from presentation order by id desc limit 1"
                    ).fetchone() == (rows[1][0],)
                page.get_by_role("button", name="Show answer", exact=False).click()
                page.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    page.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
            finally:
                (artifacts / "fit-window.txt").write_text(
                    page.locator("body").inner_text()
                )
                browser.close()
            stop_host()
            collection = Collection(str(Path(opened["store"]) / "collection.anki2"))
            try:
                assert (
                    collection.decks.get_config(DeckConfigId(1))["fsrsParams6"]
                    == fit["parameters"]
                )
            finally:
                collection.close()
            api.dispose()


if __name__ == "__main__":
    with evidence("study-fit", Path(__file__).parent / "fixtures/study") as artifacts:
        main(artifacts)
