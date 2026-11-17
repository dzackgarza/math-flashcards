# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright"]
# ///
"""Study the saved card while an invalid native draft remains editable."""

import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="flashcards-study-draft-") as directory:
        workspace = Path(directory)
        deck = workspace / "Draft.md"
        deck.write_text(
            '::: {.front card-id="draft"}\nSaved question.\n:::\n\n::: {.back card-id="draft"}\nSaved answer.\n:::\n'
        )
        saved = deck.read_text()
        invalid = "Unfinished draft.\n:::\nUnpaired text."
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
                page.locator('[data-deck="Draft.md"]').click()
                front = page.locator(".side-editor.front .cm-content")
                expect(front).to_have_text("Saved question.")

                def edit(text: str):
                    front.click()
                    page.keyboard.press("Control+a")
                    page.keyboard.insert_text(text)

                def start():
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.get_by_role("button", name="Study", exact=True).click()
                    study = page.get_by_role("region", name="Study session")
                    expect(
                        study.get_by_role("button", name="Show answer", exact=False)
                    ).to_be_visible()
                    return study

                edit(invalid)
                expect(
                    page.get_by_role("alert").filter(has_text="Invalid card")
                ).to_be_visible()
                study = start()
                expect(study).to_contain_text("Saved question.")
                assert deck.read_text() == saved
                page.get_by_role("button", name="Show problems").click()
                drawer = page.get_by_role("dialog")
                expect(drawer).to_contain_text("Card structure")
                expect(drawer).to_contain_text("Draft")
                drawer.get_by_role("button").filter(has_text="Card structure").click()
                expect(front).to_contain_text("Unpaired text.")
                edit("Corrected question.")
                study = start()
                expect(study).to_contain_text("Corrected question.")
                saved = deck.read_text()
                assert "Corrected question." in saved
                page.keyboard.press("e")
                expect(front).to_have_text("Corrected question.")
                edit(invalid)
                expect(
                    page.get_by_role("alert").filter(has_text="Invalid card")
                ).to_be_visible()
                page.get_by_role("button", name="Return to Study", exact=True).click()
                expect(
                    study.get_by_role("button", name="Show answer", exact=False)
                ).to_be_visible()
                expect(study).to_contain_text("Corrected question.")
                assert deck.read_text() == saved
                page.keyboard.press("Escape")
                expect(front).to_contain_text("Unpaired text.")
                edit("Final question.")
                study = start()
                expect(study).to_contain_text("Final question.")
                study.get_by_role("button", name="Show answer", exact=False).click()
                expect(study).to_contain_text("Saved answer.")
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                response = api.post(
                    "/api/request",
                    data={"action": "study-open", "workspace": str(workspace)},
                )
                assert response.ok, response.text()
                with closing(sqlite3.connect(response.json()["record"])) as record:
                    fronts = record.execute(
                        "select distinct front from review"
                    ).fetchall()
                    assert set(fronts) == {
                        ("Saved question.",),
                        ("Corrected question.",),
                        ("Final question.",),
                    }, fronts
                    assert record.execute(
                        "select count(*) from response"
                    ).fetchone() == (1,)
                expect(page.get_by_role("alert")).to_have_count(0)
                page.screenshot(path=str(artifacts / "draft-study.png"))
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
                api.dispose()


if __name__ == "__main__":
    with evidence("study-draft", Path(__file__).parent / "fixtures/study") as artifacts:
        main(artifacts)
