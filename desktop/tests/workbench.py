# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright==1.58.0"]
# ///
"""Exercise the editor and real export pipeline in a disposable workspace."""

import json
import shutil
import sqlite3
import tempfile
import zipfile
from pathlib import Path

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
        deck_path = root / "decks" / "Qual Basics" / "Special Angles.md"
        authored_source = deck_path.read_bytes()
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            console: list[str] = []
            page.on("pageerror", lambda error: console.append(str(error)))
            page.goto("http://127.0.0.1:1420")
            expect(
                page.get_by_role("heading", name="Math Flashcards", exact=True)
            ).to_be_visible()
            expect(page.get_by_label("Workspace folder")).to_have_value(
                str(repo.parent), timeout=30000
            )
            expect(
                page.get_by_role("button", name="Refresh workspace", exact=True)
            ).to_be_enabled(timeout=30000)
            page.screenshot(path=str(artifacts / "empty.png"))
            page.get_by_label("Workspace folder").fill(str(root))
            page.get_by_role("button", name="Open workspace", exact=True).click()
            expect(
                page.get_by_role("button", name="Open workspace", exact=True)
            ).to_be_enabled(timeout=30000)
            page.get_by_text("Qual Basics", exact=True).click()
            page.get_by_text("Special Angles", exact=True).click()
            expect(page.get_by_text("Unsynced", exact=True).first).to_be_visible()
            expect(page.locator(".side-editor.front .cm-editor")).to_be_visible()
            expect(page.locator(".side-editor.back .cm-editor")).to_be_visible()
            front_math = page.locator(".side-editor.front .cm-content mjx-container")
            back_math = page.locator(".side-editor.back .cm-content mjx-container")
            expect(front_math).to_contain_text("π/6", timeout=30000)
            expect(back_math.first).to_be_visible()
            expect(page.get_by_text("Unsaved changes", exact=True)).not_to_be_visible()
            page.screenshot(path=str(artifacts / "rendered.png"))
            front_math.click()
            expect(front_math).to_have_count(0)
            expect(page.locator(".side-editor.front .cm-content")).to_have_text(
                r"$\sin(\pi/6) = \cdots$"
            )
            expect(page.get_by_text("Unsaved changes", exact=True)).not_to_be_visible()
            page.screenshot(path=str(artifacts / "source.png"))
            page.get_by_role("button", name="Add card", exact=True).click()
            front_editor = page.locator(".side-editor.front .cm-content")
            back_editor = page.locator(".side-editor.back .cm-content")
            front_editor.fill("Added question\n\nSecond question paragraph with $x^2$")
            back_editor.fill(
                "Added answer\n\n$$\\frac{1}{2}$$\n\n- First fact\n- Second fact"
            )
            page.get_by_role("combobox", name="Tags", exact=True).fill("edited")
            page.get_by_role("combobox", name="Tags", exact=True).press("Enter")
            expect(front_editor).to_contain_text("Second question paragraph")
            expect(back_editor).to_contain_text("Second fact")
            expect(page.get_by_text("Unsaved changes", exact=True)).to_be_visible()
            page.screenshot(path=str(artifacts / "editing.png"))
            page.get_by_role("button", name="Save deck", exact=True).click()
            expect(page.get_by_text("Saved", exact=True).first).to_be_visible(
                timeout=30000
            )
            assert (
                "Added question"
                in (root / "decks" / "Qual Basics" / "Special Angles.md").read_text()
            )
            assert deck_path.read_bytes().startswith(authored_source)
            page.get_by_role("button", name="Reload deck", exact=True).click()
            expect(front_math).to_contain_text("π/6", timeout=30000)
            expect(
                page.get_by_role("button", name="Added question", exact=True)
            ).to_be_visible(timeout=30000)
            page.get_by_role("button", name="Added question", exact=True).click()
            expect(front_editor).to_contain_text("Second question paragraph")
            expect(back_editor).to_contain_text("Second fact")
            page.get_by_role("button", name="Generate Anki deck", exact=True).click()
            expect(page.get_by_text("Up to date", exact=True).first).to_be_visible(
                timeout=60000
            )
            page.screenshot(path=str(artifacts / "generated.png"))
            package = root / "apkg" / "Qual Basics__Special Angles.apkg"
            with zipfile.ZipFile(package) as archive:
                archive.extract("collection.anki2", root)
            with sqlite3.connect(root / "collection.anki2") as database:
                notes = list(database.execute("SELECT flds, tags FROM notes"))
                fields = [row[0] for row in notes]
            assert any(
                "Added question" in value and "Added answer" in value
                for value in fields
            )
            assert any(
                "Added question" in field and "edited" in tags for field, tags in notes
            )
            page.get_by_role("button", name="Delete card", exact=True).click()
            page.get_by_role("button", name="Delete", exact=True).click()
            page.get_by_role("button", name="Save deck", exact=True).click()
            expect(page.get_by_text("Saved", exact=True).first).to_be_visible(
                timeout=30000
            )
            page.screenshot(path=str(artifacts / "deleted.png"))
            expect(page.get_by_text("Unsynced", exact=True).first).to_be_visible()
            assert (
                "Added question"
                not in (
                    root / "decks" / "Qual Basics" / "Special Angles.md"
                ).read_text()
            )
            page.get_by_role("button", name="Generate Anki deck", exact=True).click()
            expect(page.get_by_text("Up to date", exact=True).first).to_be_visible(
                timeout=60000
            )
            package.write_bytes(b"changed package")
            page.get_by_role("button", name="Refresh workspace", exact=True).click()
            expect(page.get_by_text("Unsynced", exact=True).first).to_be_visible()
            page.screenshot(path=str(artifacts / "changed-package.png"))
            page.get_by_role("button", name="Generate Anki deck", exact=True).click()
            expect(page.get_by_text("Up to date", exact=True).first).to_be_visible(
                timeout=60000
            )
            good_package = package.read_bytes()
            with zipfile.ZipFile(package) as archive:
                archive.extract("collection.anki2", root)
            with sqlite3.connect(root / "collection.anki2") as database:
                assert all(
                    "Added question" not in row[0]
                    for row in database.execute("SELECT flds FROM notes")
                )
            page.get_by_role("button", name="Add card", exact=True).click()
            external_source = (
                deck_path.read_text()
                + '\n\n::: {.front card-id="external"}\nExternal question\n:::\n\n::: {.back card-id="external"}\nExternal answer\n:::\n'
            )
            deck_path.write_text(external_source)
            page.get_by_role("button", name="Save deck", exact=True).click()
            expect(page.get_by_text("Action failed", exact=True)).to_be_visible(
                timeout=30000
            )
            assert deck_path.read_text() == external_source
            page.screenshot(path=str(artifacts / "save-conflict.png"), full_page=True)
            page.get_by_role("button", name="Reload deck", exact=True).click()
            page.get_by_role("button", name="Discard changes", exact=True).click()
            expect(page.get_by_text("Saved", exact=True).first).to_be_visible(
                timeout=30000
            )
            for side in ("front", "back"):
                deck_path.write_text(
                    f'---\ntitle: "Unpaired deck"\n---\n\n::: {{.{side} card-id="unpaired"}}\nContent\n:::\n'
                )
                page.get_by_role("button", name="Reload deck", exact=True).click()
                expect(page.get_by_text("Action failed", exact=True)).to_be_visible(
                    timeout=30000
                )
                page.get_by_role(
                    "button", name="Generate Anki deck", exact=True
                ).click()
                expect(page.get_by_text("Failed", exact=True)).to_be_visible(
                    timeout=30000
                )
                assert package.read_bytes() == good_package
            deck_path.write_text(
                '---\ntitle: "Failure deck"\n---\n\n::: {.front card-id="failure"}\nMissing answer\n:::\n\n::: {.back card-id="failure"}\n\n:::\n'
            )
            page.get_by_role("button", name="Reload deck", exact=True).click()
            expect(
                page.get_by_role("button", name="Missing answer", exact=True)
            ).to_be_visible(timeout=30000)
            page.get_by_role("button", name="Generate Anki deck", exact=True).click()
            expect(page.get_by_text("Action failed", exact=True)).to_be_visible(
                timeout=30000
            )
            expect(page.get_by_text("Failed", exact=True)).to_be_visible()
            assert package.read_bytes() == good_package
            page.screenshot(
                path=str(artifacts / "generation-failed.png"), full_page=True
            )
            for width in (768, 1024):
                page.set_viewport_size({"width": width, "height": 1000})
                page.screenshot(
                    path=str(artifacts / f"layout-{width}.png"), full_page=True
                )
            assert not console, console
            context.tracing.stop(path=str(artifacts / "trace.zip"))
            (artifacts / "browser-errors.json").write_text(json.dumps(console))
            browser.close()
    print(
        "Editor changes persist; APKG includes saved cards; package status tracks edits and output changes."
    )


if __name__ == "__main__":
    main()
