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
        (root / "decks" / "Basics").mkdir(parents=True)
        shutil.copyfile(
            repo.parent / "decks" / "Basics" / "Precalculus.md",
            root / "decks" / "Basics" / "Precalculus.md",
        )
        deck_path = root / "decks" / "Basics" / "Precalculus.md"
        authored_source = deck_path.read_bytes()
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            console: list[str] = []
            page.on("pageerror", lambda error: console.append(str(error)))
            page.goto("http://127.0.0.1:1420")
            status = page.locator(".toolbar .status")
            expect(
                page.get_by_role("heading", name="Math Flashcards", exact=True)
            ).to_be_visible()
            page.get_by_role("button", name="Workspace", exact=True).click()
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
                page.get_by_role("button", name="Workspace", exact=True)
            ).to_have_text(root.name, timeout=30000)
            page.get_by_text("Basics", exact=True).click()
            page.get_by_text("Precalculus", exact=True).click()
            expect(status).to_contain_text("not in the Anki package")
            expect(page.locator(".side-editor.front .cm-editor")).to_be_visible()
            expect(page.locator(".side-editor.back .cm-editor")).to_be_visible()
            front_math = page.locator(".side-editor.front .cm-content mjx-container")
            back_math = page.locator(".side-editor.back .cm-content mjx-container")
            # MathJax 4 sets \pi as the mathematical italic letter U+1D70B.
            expect(front_math).to_contain_text("\U0001d70b/6", timeout=30000)
            expect(back_math.first).to_be_visible()
            page.screenshot(path=str(artifacts / "rendered.png"))
            front_math.click()
            expect(front_math).to_have_count(0)
            expect(page.locator(".side-editor.front .cm-content")).to_have_text(
                r"$\sin(\pi/6) = \cdots$"
            )
            assert deck_path.read_bytes() == authored_source
            page.screenshot(path=str(artifacts / "source.png"))

            def deck_action(name: str) -> None:
                page.get_by_role("button", name="Deck actions", exact=True).click()
                page.get_by_role("menuitem", name=name, exact=True).click()

            def saved(predicate) -> None:
                for _ in range(100):
                    if predicate(deck_path.read_text()):
                        return
                    page.wait_for_timeout(100)
                raise AssertionError("The deck file did not receive the edit.")

            # Edits save without a command.
            page.get_by_role("button", name="Add card", exact=True).click()
            front_editor = page.locator(".side-editor.front .cm-content")
            back_editor = page.locator(".side-editor.back .cm-content")
            front_editor.fill(
                "Added question\n\nSecond question paragraph with $x^2$ in $k\\fps{t}$"
            )
            back_editor.fill(
                "Added answer"
                + " that runs well past the width of the editor" * 6
                + "\n$$\\frac{1}{2}$$\n\n- First fact\n- Second fact"
            )
            for side in ("front", "back"):
                assert page.locator(f".side-editor.{side} .cm-scroller").evaluate(
                    "scroller => scroller.scrollWidth <= scroller.clientWidth"
                ), f"{side} editor scrolls horizontally"
            page.get_by_role("combobox", name="Tags", exact=True).fill("edited")
            page.get_by_role("combobox", name="Tags", exact=True).press("Enter")
            expect(front_editor).to_contain_text("Second question paragraph")
            # \fps sets t in the stmaryrd double brackets of pandoc-config.
            expect(front_editor.locator("mjx-container")).to_have_count(2)
            expect(front_editor.locator("mjx-merror")).to_have_count(0)
            expect(back_editor).to_contain_text("Second fact")
            saved(lambda text: "Added question" in text and "edited" in text)
            assert deck_path.read_bytes().startswith(authored_source)
            expect(page.locator('.card-row[data-change="added"]').last).to_contain_text(
                "Added question"
            )
            expect(status).to_contain_text("not in the Anki package", timeout=30000)
            page.screenshot(path=str(artifacts / "editing.png"))
            page.keyboard.press("Control+k")
            expect(page.get_by_placeholder("Search")).to_be_visible()
            page.keyboard.type("Added")
            page.screenshot(path=str(artifacts / "command-menu.png"))
            page.keyboard.press("Escape")
            expect(page.get_by_placeholder("Search")).not_to_be_visible()

            # The status opens the review of changes that the package lacks.
            status.click()
            review = page.get_by_role(
                "dialog", name="Changes not in the Anki packages", exact=True
            )
            expect(review.get_by_text("New", exact=True).first).to_be_visible(
                timeout=30000
            )
            expect(review).to_contain_text("Added question")
            page.screenshot(path=str(artifacts / "review.png"))
            review.get_by_role(
                "button", name="Update the Anki package", exact=True
            ).click()
            expect(review).not_to_be_visible()
            expect(status).to_have_text("Anki package up to date", timeout=60000)
            expect(page.locator(".card-row[data-change]")).to_have_count(0)
            page.screenshot(path=str(artifacts / "generated.png"))
            package = root / "apkg" / "Basics__Precalculus.apkg"
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
            page.get_by_role("button", name="Deck actions", exact=True).click()
            expect(
                page.get_by_role("menuitem", name="Update Anki package", exact=True)
            ).to_be_disabled()
            page.wait_for_timeout(300)
            page.screenshot(path=str(artifacts / "deck-actions.png"))
            page.keyboard.press("Escape")

            page.get_by_role("button", name="Delete card", exact=True).click()
            page.get_by_role("button", name="Delete", exact=True).click()
            saved(lambda text: "Added question" not in text)
            expect(status).to_have_text(
                "1 change not in the Anki package", timeout=30000
            )
            page.screenshot(path=str(artifacts / "deleted.png"))
            deck_action("Update Anki package")
            expect(status).to_have_text("Anki package up to date", timeout=60000)

            # A package changed outside the app is out of date without a refresh.
            package.write_bytes(b"changed package")
            expect(status).to_have_text(
                "The Anki package file changed after generation.", timeout=30000
            )
            page.screenshot(path=str(artifacts / "changed-package.png"))
            deck_action("Update Anki package")
            expect(status).to_have_text("Anki package up to date", timeout=60000)
            good_package = package.read_bytes()
            with zipfile.ZipFile(package) as archive:
                archive.extract("collection.anki2", root)
            with sqlite3.connect(root / "collection.anki2") as database:
                assert all(
                    "Added question" not in row[0]
                    for row in database.execute("SELECT flds FROM notes")
                )

            # A disk change during an edit asks which version to keep.
            page.get_by_role("button", name="Add card", exact=True).click()
            external_source = (
                deck_path.read_text()
                + '\n\n::: {.front card-id="external"}\nExternal question\n:::\n\n::: {.back card-id="external"}\nExternal answer\n:::\n'
            )
            deck_path.write_text(external_source)
            expect(
                page.get_by_text(
                    "The deck changed on disk while you edited it", exact=True
                )
            ).to_be_visible(timeout=30000)
            assert deck_path.read_text() == external_source
            page.screenshot(path=str(artifacts / "save-conflict.png"), full_page=True)
            page.get_by_role("button", name="Use the disk version", exact=True).click()
            expect(
                page.get_by_role("button", name="External question", exact=True)
            ).to_be_visible(timeout=30000)
            assert deck_path.read_text() == external_source

            # The open deck follows its file.
            for side in ("front", "back"):
                deck_path.write_text(
                    f'---\ntitle: "Unpaired deck"\n---\n\n::: {{.{side} card-id="unpaired"}}\nContent\n:::\n'
                )
                expect(page.get_by_text("Action failed", exact=True)).to_be_visible(
                    timeout=30000
                )
                page.get_by_role("button", name="Dismiss error", exact=True).click()
                deck_action("Update Anki package")
                expect(status).to_have_text("Generation failed", timeout=30000)
                assert package.read_bytes() == good_package
                page.get_by_role("button", name="Dismiss error", exact=True).click()
            deck_path.write_text(
                '---\ntitle: "Failure deck"\n---\n\n::: {.front card-id="failure"}\nMissing answer\n:::\n\n::: {.back card-id="failure"}\n\n:::\n'
            )
            expect(
                page.get_by_role("button", name="Missing answer", exact=True)
            ).to_be_visible(timeout=30000)
            deck_action("Update Anki package")
            expect(page.get_by_text("Action failed", exact=True)).to_be_visible(
                timeout=30000
            )
            expect(status).to_have_text("Generation failed")
            assert package.read_bytes() == good_package
            page.screenshot(
                path=str(artifacts / "generation-failed.png"), full_page=True
            )

            # The Problems drawer lists every equation that does not render and
            # every card without an answer, in all decks.
            (root / "decks" / "Basics" / "Broken.md").write_text(
                '---\ntitle: "Broken"\n---\n\n::: {.front card-id="macro"}\nUnknown $\\undefinedmacro x$\n:::\n\n::: {.back card-id="macro"}\n$$\\left{ x \\right}$$\n:::\n'
            )
            problems_button = page.get_by_role(
                "button", name="Show problems", exact=True
            )
            expect(problems_button).to_contain_text("3", timeout=30000)
            expect(page.locator(".tree-dot.problem")).to_have_count(2)
            problem_row = page.locator(".card-row[data-problem]")
            expect(problem_row).to_contain_text("Missing answer")
            expect(problem_row).to_contain_text("Problem")
            problems_button.click()
            drawer = page.get_by_role("dialog", name="3 problems", exact=True)
            expect(drawer).to_contain_text(
                "Undefined control sequence \\undefinedmacro"
            )
            expect(drawer).to_contain_text(
                "Missing or unrecognized delimiter for \\left"
            )
            expect(drawer).to_contain_text(
                "The exporter rejects a card without an answer."
            )
            page.wait_for_timeout(300)
            page.screenshot(path=str(artifacts / "problems.png"))
            drawer.locator(
                ".problem-message", has_text="Undefined control sequence"
            ).click()
            expect(drawer).not_to_be_visible()
            expect(page.locator(".deck-title")).to_have_text("Broken", timeout=30000)
            expect(page.locator(".card-row.active[data-problem]")).to_be_visible()
            expect(
                page.locator(".side-editor.front .cm-content mjx-merror")
            ).to_be_visible(timeout=30000)
            page.screenshot(path=str(artifacts / "problem-card.png"))
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
        "Edits save automatically; the open deck follows its file; the review lists changes; APKG includes saved cards."
    )


if __name__ == "__main__":
    main()
