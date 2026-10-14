# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright==1.58.0", "cyclopts==4.15.0"]
# ///
"""Exercise deck-tree organization with real files, trash, and Anki export."""

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
        page.get_by_text("Algebra", exact=True).click()
        page.get_by_text("Analysis", exact=True).click()
        page.get_by_text("Original", exact=True).click()
        expect(
            page.locator(".side-editor .cm-content mjx-container").first
        ).to_be_visible(timeout=30000)
        page.screenshot(path=str(ARTIFACTS / "organization-tree.png"))

        def deck_row(path: str):
            return page.locator(f'.tree-row[data-deck="{path}"]')

        def card_row(label: str):
            return page.get_by_role("button", name=label, exact=True)

        def undo() -> None:
            page.get_by_role("button", name="Undo", exact=True).click()
            expect(page.get_by_text("Undo complete.", exact=True)).to_be_visible(
                timeout=30000
            )

        card_row("Identity element").click()
        card_row("Inverse").click(modifiers=["Control"])
        card_row("Identity element").drag_to(deck_row(TARGET))
        expect(page.get_by_text("2 cards moved to Target.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert identifiers(source) == ["three"]
        assert identifiers(target) == ["four", "one", "two"]
        assert "../Algebra/assets/plot.png" in target.read_text()
        assert r"$$g e=g$$" in target.read_text()
        expect(card_row("Identity element")).not_to_be_visible()
        page.screenshot(path=str(ARTIFACTS / "organization-moved.png"))
        undo()
        assert source.read_bytes() == original_source
        assert target.read_bytes() == original_target
        expect(card_row("Identity element")).to_be_visible(timeout=30000)

        start = card_row("Identity element").bounding_box()
        finish = card_row("Closure").bounding_box()
        assert start and finish
        page.mouse.move(
            start["x"] + start["width"] / 2, start["y"] + start["height"] / 2
        )
        page.mouse.down()
        page.mouse.move(start["x"] + 30, start["y"] + 10, steps=5)
        page.mouse.move(
            finish["x"] + finish["width"] / 2,
            finish["y"] + finish["height"] - 3,
            steps=12,
        )
        page.wait_for_timeout(300)
        page.screenshot(path=str(ARTIFACTS / "organization-drag-indicator.png"))
        page.mouse.up()
        expect(page.get_by_text("Card order saved.", exact=True)).to_be_visible(
            timeout=30000
        )
        assert identifiers(source) == ["two", "three", "one"]

        deck_row(ABSORBED).drag_to(deck_row(TARGET))
        expect(
            page.get_by_role("dialog", name="Merge decks", exact=True)
        ).to_be_visible()
        page.get_by_role("button", name="Merge decks", exact=True).click()
        expect(
            page.get_by_text("Absorb merged into Target.", exact=True)
        ).to_be_visible(timeout=30000)
        assert not absorbed.exists()
        assert identifiers(target) == ["four", "five"]
        expect(deck_row(ABSORBED)).to_have_count(0)
        page.screenshot(path=str(ARTIFACTS / "organization-merged.png"))
        undo()
        assert absorbed.read_bytes() == original_absorbed
        assert target.read_bytes() == original_target
        expect(deck_row(ABSORBED)).to_be_visible(timeout=30000)

        page.get_by_role("button", name="New deck", exact=True).click()
        page.get_by_label("Deck name", exact=True).fill("Selected")
        page.get_by_label("Folder", exact=True).fill("Geometry")
        page.get_by_role("button", name="Create deck", exact=True).click()
        expect(page.get_by_text("Selected created.", exact=True)).to_be_visible(
            timeout=30000
        )
        split = root / "decks" / "Geometry" / "Selected.md"
        assert identifiers(split) == []
        expect(page.get_by_text("Add a card to begin.", exact=True)).to_be_visible()
        deck_row(SOURCE).click()
        card_row("Closure").click()
        card_row("Identity element").click(modifiers=["Shift"])
        card_row("Closure").drag_to(deck_row("Geometry/Selected.md"))
        expect(
            page.get_by_text("2 cards moved to Selected.", exact=True)
        ).to_be_visible(timeout=30000)
        assert identifiers(split) == ["three", "one"]
        assert identifiers(source) == ["two"]
        page.screenshot(path=str(ARTIFACTS / "organization-split.png"))
        undo()
        assert identifiers(source) == ["two", "three", "one"]

        deck_row(TARGET).click()
        expect(card_row("Continuity")).to_be_visible(timeout=30000)
        page.get_by_role("button", name="Generate Anki deck", exact=True).click()
        expect(page.get_by_text("Up to date", exact=True).first).to_be_visible(
            timeout=60000
        )
        deck_row(SOURCE).click()
        card_row("Closure").drag_to(deck_row(TARGET))
        expect(page.get_by_text("Card moved to Target.", exact=True)).to_be_visible(
            timeout=30000
        )
        deck_row(TARGET).click()
        expect(page.get_by_text("Unsynced", exact=True).first).to_be_visible(
            timeout=30000
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

        deck_row(SOURCE).click()
        expect(card_row("Inverse")).to_be_visible(timeout=30000)
        page.locator(".side-editor.front .cm-content").fill("Edited inverse")
        expect(
            page.get_by_text("Save the deck to move its cards.", exact=True)
        ).to_be_visible()
        before = source.read_bytes()
        card_row("Edited inverse").drag_to(deck_row(TARGET))
        assert source.read_bytes() == before
        page.get_by_role("button", name="Reload deck", exact=True).click()
        page.get_by_role("button", name="Discard changes", exact=True).click()
        expect(card_row("Inverse")).to_be_visible(timeout=30000)

        external = (
            source.read_text() + "\n" + card("six", "External card", "External answer")
        )
        source.write_text(external)
        target_before = target.read_bytes()
        page.mouse.move(0, 0)
        card_row("Inverse").drag_to(deck_row(TARGET))
        expect(page.get_by_text("Action failed", exact=True)).to_be_visible(
            timeout=30000
        )
        assert source.read_text() == external
        assert target.read_bytes() == target_before
        page.get_by_role("button", name="Reload deck", exact=True).click()
        expect(card_row("External card")).to_be_visible(timeout=30000)
        for width in (768, 1024):
            page.set_viewport_size({"width": width, "height": 1000})
            page.screenshot(
                path=str(ARTIFACTS / f"organization-{width}.png"), full_page=True
            )
        assert not errors, errors
        browser.close()
    print(
        "Tree drag merges decks, moves and reorders cards, splits through a new deck, rejects stale and unsaved sources, and exports moved cards."
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
