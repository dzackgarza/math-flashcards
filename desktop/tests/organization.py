# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright==1.58.0", "cyclopts==4.15.0"]
# ///
"""Exercise visual organization with real files, trash, and Anki export."""

import json
import os
import shlex
import shutil
import sqlite3
import subprocess
import tempfile
import zipfile
from pathlib import Path

import cyclopts
from playwright.sync_api import expect, sync_playwright

DESKTOP = Path(__file__).resolve().parents[1]
ARTIFACTS = DESKTOP / "test-artifacts"
SOURCE = "Algebra/Original.md"
TARGET = "Analysis/Target.md"
ABSORBED = "Algebra/Absorb.md"


def card(identifier: str, front: str, back: str) -> str:
    return f'::: {{.front card-id="{identifier}" tags="math"}}\n{front}\n:::\n\n::: {{.back card-id="{identifier}"}}\n{back}\n:::\n'


def deck(title: str, content: str) -> str:
    return f"---\ntitle: {json.dumps(title)}\n---\n\n{content}"


def identifiers(path: Path) -> list[str]:
    # IDs from the saved Pandoc document, independent of the visual list.
    parsed = json.loads(
        subprocess.check_output(
            ["pandoc", "-f", "markdown", "-t", "json", str(path)], text=True
        )
    )
    return [
        dict(block["c"][0][2])["card-id"]
        for block in parsed["blocks"]
        if "front" in block["c"][0][1]
    ]


def scenario(root: Path) -> None:
    source = root / "decks" / SOURCE
    target = root / "decks" / TARGET
    absorbed = root / "decks" / ABSORBED
    original_source, original_target, original_absorbed = (
        source.read_bytes(),
        target.read_bytes(),
        absorbed.read_bytes(),
    )
    ARTIFACTS.mkdir(exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto("http://127.0.0.1:1421")
        expect(
            page.get_by_role("button", name="Refresh workspace", exact=True)
        ).to_be_enabled(timeout=30000)
        page.get_by_label("Workspace folder").fill(str(root))
        page.get_by_role("button", name="Open workspace", exact=True).click()
        expect(
            page.get_by_role("button", name="Open workspace", exact=True)
        ).to_be_enabled(timeout=30000)
        page.screenshot(path=str(ARTIFACTS / "organization-decks.png"))
        page.get_by_role("button", name="Open deck Original", exact=True).click()
        expect(page.locator('[data-card="one"] mjx-container')).to_be_visible(
            timeout=30000
        )
        page.screenshot(path=str(ARTIFACTS / "organization-cards.png"))

        page.get_by_role(
            "checkbox", name="Select card Identity element", exact=True
        ).check()
        page.get_by_role("checkbox", name="Select card Inverse", exact=True).check()
        page.get_by_role(
            "button", name="Drag card Identity element", exact=True
        ).drag_to(page.locator(f'.deck-tile[data-deck="{TARGET}"]'))
        expect(page.get_by_text("Cards moved to Target.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert identifiers(source) == ["three"]
        assert identifiers(target) == ["four", "one", "two"]
        assert "../Algebra/assets/plot.png" in target.read_text()
        assert r"$$g e=g$$" in target.read_text()
        page.screenshot(path=str(ARTIFACTS / "organization-moved.png"))
        page.get_by_role("button", name="Undo", exact=True).click()
        expect(page.get_by_text("Undo complete.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert source.read_bytes() == original_source
        assert target.read_bytes() == original_target

        handle = page.get_by_role(
            "button", name="Drag card Identity element", exact=True
        )
        item = page.locator('[data-card="three"]')
        start = handle.bounding_box()
        finish = item.bounding_box()
        assert start and finish
        page.mouse.move(
            start["x"] + start["width"] / 2, start["y"] + start["height"] / 2
        )
        page.mouse.down()
        page.mouse.move(start["x"] + 30, start["y"] + 30, steps=5)
        page.mouse.move(
            finish["x"] + finish["width"] - 8,
            finish["y"] + finish["height"] / 2,
            steps=12,
        )
        page.wait_for_timeout(300)
        page.screenshot(path=str(ARTIFACTS / "organization-drag-indicator.png"))
        page.mouse.up()
        expect(page.get_by_text("Card order saved.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert identifiers(source) == ["two", "three", "one"]
        reordered_source = source.read_bytes()

        expect(
            page.get_by_role("button", name="Drag deck Absorb", exact=True)
        ).to_be_enabled(timeout=30000)
        page.get_by_role("button", name="Drag deck Absorb", exact=True).drag_to(
            page.locator(f'.deck-tile[data-deck="{TARGET}"]')
        )
        expect(
            page.get_by_role("dialog", name="Absorb deck", exact=True)
        ).to_be_visible()
        page.get_by_role("button", name="Absorb deck", exact=True).click()
        expect(
            page.get_by_text("Deck absorbed into Target.", exact=True)
        ).to_be_visible(timeout=30000)
        assert not absorbed.exists()
        assert identifiers(target) == ["four", "five"]
        page.screenshot(path=str(ARTIFACTS / "organization-absorbed.png"))
        page.get_by_role("button", name="Undo", exact=True).click()
        expect(page.get_by_text("Undo complete.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert absorbed.read_bytes() == original_absorbed
        assert target.read_bytes() == original_target

        page.get_by_role("checkbox", name="Select card Closure", exact=True).check()
        page.get_by_role(
            "checkbox", name="Select card Identity element", exact=True
        ).check()
        page.get_by_role("button", name="Split into new deck", exact=True).click()
        page.get_by_label("Deck name", exact=True).fill("Selected")
        page.get_by_label("Folder", exact=True).fill("Geometry")
        page.get_by_role("button", name="Create deck", exact=True).click()
        expect(
            page.get_by_text("Selection split into Selected.", exact=True)
        ).to_be_visible(timeout=30000)
        split = root / "decks" / "Geometry" / "Selected.md"
        assert identifiers(split) == ["three", "one"]
        assert identifiers(source) == ["two"]
        page.screenshot(path=str(ARTIFACTS / "organization-split.png"))
        page.get_by_role("button", name="Undo", exact=True).click()
        expect(page.get_by_text("Undo complete.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert not split.exists()
        assert source.read_bytes() == reordered_source

        page.get_by_role("button", name="Clear selection", exact=True).click()

        checkbox = page.get_by_role("checkbox", name="Select card Closure", exact=True)
        checkbox.focus()
        checkbox.press("Space")
        page.get_by_role("button", name="Move to deck", exact=True).click()
        page.get_by_role("combobox", name="Destination deck", exact=True).click()
        page.get_by_role("option", name="Analysis / Target", exact=True).click()
        page.get_by_role("button", name="Move cards", exact=True).click()
        expect(page.get_by_text("Cards moved to Target.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert identifiers(source) == ["two", "one"]
        assert identifiers(target) == ["four", "three"]

        page.get_by_role("button", name="Open deck Target", exact=True).click()
        page.get_by_role("button", name="Open card Continuity", exact=True).click()
        expect(page.locator(".side-editor.front .cm-content")).to_contain_text(
            "Continuity", timeout=30000
        )
        page.get_by_role("button", name="Generate Anki deck", exact=True).click()
        expect(page.get_by_text("Up to date", exact=True).first).to_be_visible(
            timeout=60000
        )
        package = root / "apkg" / "Analysis__Target.apkg"
        with zipfile.ZipFile(package) as archive:
            archive.extract("collection.anki2", root)
        with sqlite3.connect(root / "collection.anki2") as database:
            fields = [row[0] for row in database.execute("SELECT flds FROM notes")]
        assert any("Closure" in field and "product stays" in field for field in fields)
        page.get_by_text("Organize", exact=True).click()
        expect(page.locator('[data-card="three"]')).to_be_visible(timeout=30000)
        page.get_by_role("button", name="Open deck Original", exact=True).click()
        page.get_by_role(
            "checkbox", name="Select card Identity element", exact=True
        ).check()
        page.get_by_role(
            "button", name="Drag card Identity element", exact=True
        ).drag_to(page.locator(f'.deck-tile[data-deck="{TARGET}"]'))
        expect(page.get_by_text("Cards moved to Target.", exact=True)).to_be_visible(
            timeout=30000
        )
        expect(
            page.locator(f'.deck-tile[data-deck="{TARGET}"]').get_by_text(
                "Unsynced", exact=True
            )
        ).to_be_visible()
        page.get_by_role("button", name="Undo", exact=True).click()
        expect(page.get_by_text("Undo complete.", exact=True)).to_be_visible(
            timeout=30000
        )

        page.get_by_role("button", name="New deck", exact=True).click()
        page.get_by_label("Deck name", exact=True).fill("Empty")
        page.get_by_role("button", name="Create deck", exact=True).click()
        expect(page.get_by_text("This deck is empty", exact=True)).to_be_visible(
            timeout=30000
        )
        empty = root / "decks" / "Algebra" / "Empty.md"
        assert identifiers(empty) == []
        page.get_by_role("button", name="Open deck Original", exact=True).click()
        page.get_by_role("button", name="Drag card Inverse", exact=True).drag_to(
            page.locator('.deck-tile[data-deck="Algebra/Empty.md"]')
        )
        expect(page.get_by_text("Cards moved to Empty.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert identifiers(empty) == ["two"]
        page.get_by_role("button", name="Undo", exact=True).click()
        expect(page.get_by_text("Undo complete.", exact=True)).to_be_visible(
            timeout=30000
        )

        expect(
            page.get_by_role("button", name="Drag card Identity element", exact=True)
        ).to_be_enabled(timeout=30000)
        external = (
            source.read_text() + "\n" + card("six", "External card", "External answer")
        )
        source.write_text(external)
        target_before = target.read_bytes()
        page.get_by_role(
            "checkbox", name="Select card Identity element", exact=True
        ).check()
        page.get_by_role("button", name="Split into new deck", exact=True).click()
        page.get_by_label("Deck name", exact=True).fill("Conflict")
        page.get_by_role("button", name="Create deck", exact=True).click()
        expect(page.get_by_text("Organization failed", exact=True)).to_be_visible(
            timeout=30000
        )
        assert source.read_text() == external
        assert target.read_bytes() == target_before
        assert not (root / "decks" / "Algebra" / "Conflict.md").exists()
        page.get_by_role("button", name="Cancel", exact=True).click()
        page.get_by_role("button", name="Open deck Original", exact=True).click()
        expect(page.locator('[data-card="six"]')).to_be_visible(timeout=30000)
        for width in (768, 1024):
            page.set_viewport_size({"width": width, "height": 1000})
            page.screenshot(
                path=str(ARTIFACTS / f"organization-{width}.png"), full_page=True
            )
        assert not errors, errors
        browser.close()
    print(
        "Visual drag, grouped moves, reorder, absorb, split, Undo, keyboard alternatives, and Anki contents verified."
    )


app = cyclopts.App()


@app.default
def main(*, workspace: Path | None = None) -> None:
    if workspace is not None:
        scenario(workspace)
        return
    with tempfile.TemporaryDirectory(prefix="flashcards-organize-") as directory:
        root = Path(directory) / "workspace"
        (root / "decks" / "Algebra" / "assets").mkdir(parents=True)
        (root / "decks" / "Analysis").mkdir(parents=True)
        shutil.copyfile(
            DESKTOP / "src-tauri" / "icons" / "32x32.png",
            root / "decks" / "Algebra" / "assets" / "plot.png",
        )
        (root / "decks" / SOURCE).write_text(
            deck(
                "Algebra::Original",
                card(
                    "one",
                    "Identity element\n\n$$e g=g$$\n\n![Plot](assets/plot.png)",
                    "$$g e=g$$",
                )
                + "\n"
                + card("two", "Inverse\n\n$g^{-1}$", "Every element has an inverse.")
                + "\n"
                + card("three", "Closure", "The product stays in the group."),
            )
        )
        (root / "decks" / TARGET).write_text(
            deck(
                "Analysis::Target",
                card("four", "Continuity", "Nearby inputs give nearby outputs."),
            )
        )
        (root / "decks" / ABSORBED).write_text(
            deck("Algebra::Absorb", card("five", "Associativity", "$$a(bc)=(ab)c$$"))
        )
        environment = os.environ | {
            "XDG_DATA_HOME": str(Path(directory) / "data"),
            "XDG_CONFIG_HOME": str(Path(directory) / "config"),
            "XDG_CACHE_HOME": str(Path(directory) / "cache"),
            "UV_CACHE_DIR": subprocess.check_output(
                ["uv", "cache", "dir"], text=True
            ).strip(),
        }
        with sync_playwright() as playwright:
            environment["PLAYWRIGHT_BROWSERS_PATH"] = str(
                Path(playwright.chromium.executable_path).parents[2]
            )
        subprocess.run(
            [
                "bunx",
                "start-server-and-test",
                "bunx vite --host 127.0.0.1 --port 1421",
                "http-get://127.0.0.1:1421",
                "uv run "
                + shlex.quote(str(Path(__file__).resolve()))
                + " --workspace "
                + shlex.quote(str(root)),
            ],
            cwd=DESKTOP,
            env=environment,
            check=True,
        )


if __name__ == "__main__":
    app()
