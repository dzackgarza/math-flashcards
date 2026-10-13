# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright==1.58.0"]
# ///
"""Exercise the editor and real export pipeline in a disposable workspace."""

import json
import os
from pathlib import Path
import shutil
import sqlite3
import tempfile
import zipfile

from playwright.sync_api import expect, sync_playwright


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    artifacts = repo / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="flashcards-test-") as directory:
        root = Path(directory)
        (root / "decks" / "Qual Basics").mkdir(parents=True)
        shutil.copyfile(
            repo.parent / "decks" / "Qual Basics" / "Special Angles.md",
            root / "decks" / "Qual Basics" / "Special Angles.md",
        )
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            console: list[str] = []
            page.on("pageerror", lambda error: console.append(str(error)))
            page.goto("http://127.0.0.1:1420")
            expect(page.get_by_role("heading", name="Math Flashcards", exact=True)).to_be_visible()
            page.screenshot(path=str(artifacts / "empty.png"))
            page.get_by_label("Workspace folder").fill(str(root))
            page.get_by_role("button", name="Open workspace", exact=True).click()
            page.get_by_text("Qual Basics", exact=True).click()
            page.get_by_text("Special Angles", exact=True).click()
            expect(page.get_by_text("Unsynced", exact=True).first).to_be_visible()
            expect(page.locator(".cm-editor")).to_be_visible()
            page.screenshot(path=str(artifacts / "front.png"))
            page.get_by_role("button", name="Flip card").click()
            expect(page.get_by_role("radio", name="Back", exact=True)).to_be_checked()
            page.screenshot(path=str(artifacts / "back.png"))
            page.get_by_role("button", name="Add card", exact=True).click()
            editor = page.locator(".cm-content")
            editor.fill("- Added question\n\n    Added answer\n\n    tags: edited\n")
            expect(page.get_by_text("Unsaved changes", exact=True)).to_be_visible()
            page.screenshot(path=str(artifacts / "editing.png"))
            page.get_by_role("button", name="Save deck", exact=True).click()
            expect(page.get_by_text("Saved", exact=True).first).to_be_visible(timeout=30000)
            assert "Added question" in (root / "decks" / "Qual Basics" / "Special Angles.md").read_text()
            page.get_by_role("button", name="Generate Anki deck", exact=True).click()
            expect(page.get_by_text("Up to date", exact=True).first).to_be_visible(timeout=60000)
            page.screenshot(path=str(artifacts / "generated.png"))
            package = root / "apkg" / "Qual Basics__Special Angles.apkg"
            with zipfile.ZipFile(package) as archive:
                archive.extract("collection.anki2", root)
            with sqlite3.connect(root / "collection.anki2") as database:
                fields = [row[0] for row in database.execute("SELECT flds FROM notes")]
            assert any("Added question" in value and "Added answer" in value for value in fields)
            page.get_by_role("button", name="Delete card", exact=True).click()
            page.get_by_role("button", name="Delete", exact=True).click()
            page.get_by_role("button", name="Save deck", exact=True).click()
            expect(page.get_by_text("Unsynced", exact=True).first).to_be_visible()
            assert "Added question" not in (root / "decks" / "Qual Basics" / "Special Angles.md").read_text()
            page.screenshot(path=str(artifacts / "deleted.png"))
            page.get_by_role("button", name="Generate Anki deck", exact=True).click()
            expect(page.get_by_text("Up to date", exact=True).first).to_be_visible(timeout=60000)
            package.write_bytes(b"changed package")
            page.get_by_role("button", name="Refresh workspace", exact=True).click()
            expect(page.get_by_text("Unsynced", exact=True).first).to_be_visible()
            page.screenshot(path=str(artifacts / "changed-package.png"))
            for width in (768, 1024):
                page.set_viewport_size({"width": width, "height": 1000})
                page.screenshot(path=str(artifacts / f"layout-{width}.png"))
            assert not console, console
            context.tracing.stop(path=str(artifacts / "trace.zip"))
            (artifacts / "browser-errors.json").write_text(json.dumps(console))
            browser.close()
    print("Editor changes persist; APKG includes saved cards; package status tracks edits and output changes.")


if __name__ == "__main__":
    main()
