# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright", "cyclopts"]
# ///
"""Exercise deck-tree organization with real files, trash, and Anki export."""

import json
import os
import shlex
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
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
    source = root / SOURCE
    target = root / TARGET
    absorbed = root / ABSORBED
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
        page.get_by_role("button", name="Workspace", exact=True).click()
        expect(
            page.get_by_role("button", name="Refresh workspace", exact=True)
        ).to_be_enabled(timeout=30000)
        page.get_by_label("Workspace folder").fill(str(root))
        page.get_by_role("button", name="Open workspace", exact=True).click()
        expect(page.get_by_role("button", name="Workspace", exact=True)).to_have_text(
            root.name, timeout=30000
        )
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
            expect(
                page.locator(".snackbar").get_by_text("Undo complete.", exact=True)
            ).to_be_visible(timeout=30000)

        card_row("Identity element").click()
        card_row("Inverse").click(modifiers=["Control"])
        card_row("Identity element").drag_to(deck_row(TARGET))
        expect(
            page.locator(".snackbar").get_by_text(
                "2 cards moved to Target.", exact=True
            )
        ).to_be_visible(timeout=30000)
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
        expect(
            page.locator(".snackbar").get_by_text("Card order saved.", exact=True)
        ).to_be_visible(timeout=30000)
        assert identifiers(source) == ["two", "three", "one"]

        deck_row(ABSORBED).drag_to(deck_row(TARGET))
        expect(
            page.get_by_role("dialog", name="Merge decks", exact=True)
        ).to_be_visible()
        page.get_by_role("button", name="Merge decks", exact=True).click()
        expect(
            page.locator(".snackbar").get_by_text(
                "Absorb merged into Target.", exact=True
            )
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
        expect(
            page.locator(".snackbar").get_by_text("Selected created.", exact=True)
        ).to_be_visible(timeout=30000)
        split = root / "Geometry" / "Selected.md"
        assert identifiers(split) == []
        expect(page.get_by_text("Add a card to begin.", exact=True)).to_be_visible()
        deck_row(SOURCE).click()
        card_row("Closure").click()
        card_row("Identity element").click(modifiers=["Shift"])
        card_row("Closure").drag_to(deck_row("Geometry/Selected.md"))
        expect(
            page.locator(".snackbar").get_by_text(
                "2 cards moved to Selected.", exact=True
            )
        ).to_be_visible(timeout=30000)
        assert identifiers(split) == ["three", "one"]
        assert identifiers(source) == ["two"]
        page.screenshot(path=str(ARTIFACTS / "organization-split.png"))
        undo()
        assert identifiers(source) == ["two", "three", "one"]

        def deck_action(path: str, name: str) -> None:
            deck_row(path).click(button="right")
            page.get_by_role("menuitem", name=name, exact=True).click()

        def contents(path: Path) -> list[str]:
            with zipfile.ZipFile(path) as archive:
                archive.extract("collection.anki2", root)
            with sqlite3.connect(root / "collection.anki2") as database:
                return [row[0] for row in database.execute("SELECT flds FROM notes")]

        packages = root / "apkg"
        page.get_by_role(
            "button", name="Review and update Anki packages", exact=True
        ).click()
        review = page.get_by_role(
            "dialog", name="Changes not in the Anki packages", exact=True
        )
        expect(review.get_by_text("Associativity")).to_be_visible(timeout=30000)
        review.get_by_role("button", name="Update 3 Anki packages", exact=True).click()
        expected = {
            "Algebra__Original.apkg",
            "Algebra__Absorb.apkg",
            "Analysis__Target.apkg",
        }
        deadline = time.monotonic() + 120
        while (
            not packages.is_dir()
            or {path.name for path in packages.iterdir()} != expected
        ):
            assert time.monotonic() < deadline, sorted(packages.iterdir())
            page.wait_for_timeout(200)
        # The button stays available; its badge counts out-of-date packages.
        expect(page.locator(".workspace-progress")).to_have_text(
            "Workspace checks complete", timeout=120000
        )
        expect(
            page.get_by_role("button", name="Review and update Anki packages")
        ).to_have_text("Update Anki packages")

        card_row("Closure").drag_to(deck_row(TARGET))
        expect(
            page.locator(".snackbar").get_by_text("Card moved to Target.", exact=True)
        ).to_be_visible(timeout=30000)
        deck_row(TARGET).click()
        status = page.locator(".toolbar .status")
        expect(status).to_have_text("1 change not in the Anki package", timeout=30000)
        expect(page.locator('.card-row[data-change="added"]')).to_contain_text(
            "Closure"
        )
        page.screenshot(path=str(ARTIFACTS / "organization-pending.png"))
        deck_action(TARGET, "Update Anki package")
        expect(status).to_have_text("Anki package up to date", timeout=60000)
        assert any(
            "Closure" in field and "product stays" in field
            for field in contents(packages / "Analysis__Target.apkg")
        )

        # An edited card saves before it moves.
        deck_row(SOURCE).click()
        expect(card_row("Inverse")).to_be_visible(timeout=30000)
        card_row("Inverse").click()
        page.locator(".side-editor.front .cm-content").fill("Edited inverse")
        page.get_by_role("button", name="Dismiss", exact=True).click()
        card_row("Edited inverse").drag_to(deck_row(TARGET))
        expect(
            page.locator(".snackbar").get_by_text("Card moved to Target.", exact=True)
        ).to_be_visible(timeout=30000)
        assert "Edited inverse" in target.read_text()
        assert "Edited inverse" not in source.read_text()
        undo()
        assert "Edited inverse" in source.read_text()

        # The open deck follows its file.
        external = (
            source.read_text() + "\n" + card("six", "External card", "External answer")
        )
        source.write_text(external)
        expect(card_row("External card")).to_be_visible(timeout=30000)

        deck_row(ABSORBED).click(button="right")
        expect(
            page.get_by_role("menuitem", name="Delete deck…", exact=True)
        ).to_be_visible()
        page.wait_for_timeout(300)
        page.screenshot(path=str(ARTIFACTS / "organization-context-menu.png"))
        page.get_by_role("menuitem", name="Rename deck…", exact=True).click()
        page.get_by_label("Deck name", exact=True).fill("Associative")
        page.get_by_role("button", name="Rename deck", exact=True).click()
        expect(
            page.locator(".snackbar").get_by_text(
                "Absorb renamed to Associative.", exact=True
            )
        ).to_be_visible(timeout=30000)
        renamed = root / "Algebra" / "Associative.md"
        assert not absorbed.exists()
        assert renamed.read_text().startswith('---\ntitle: "Algebra::Associative"\n---')
        assert identifiers(renamed) == ["five"]
        assert not (packages / "Algebra__Absorb.apkg").exists()
        undo()
        assert absorbed.read_bytes() == original_absorbed
        assert not renamed.exists()

        deck_action(ABSORBED, "Delete deck…")
        page.get_by_role("button", name="Delete deck", exact=True).click()
        expect(
            page.locator(".snackbar").get_by_text(
                "Absorb sent to the trash.", exact=True
            )
        ).to_be_visible(timeout=30000)
        assert not absorbed.exists()
        expect(deck_row(ABSORBED)).to_have_count(0)
        undo()
        assert absorbed.read_bytes() == original_absorbed
        for width in (768, 1024):
            page.set_viewport_size({"width": width, "height": 1000})
            page.screenshot(
                path=str(ARTIFACTS / f"organization-{width}.png"), full_page=True
            )
        assert not errors, errors
        browser.close()
    print(
        "Tree drag merges decks, moves and reorders cards, and splits through a new deck; the context menu renames and deletes decks; every out-of-date package updates at once."
    )


app = cyclopts.App()


@app.default
def main(*, workspace: Path | None = None) -> None:
    # The Chromium build that the resolved Playwright version drives:
    # https://playwright.dev/python/docs/browsers#install-browsers
    subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"], check=True
    )
    if workspace is not None:
        scenario(workspace)
        return
    with tempfile.TemporaryDirectory(prefix="flashcards-organize-") as directory:
        root = Path(directory) / "workspace"
        (root / "Algebra" / "assets").mkdir(parents=True)
        (root / "Analysis").mkdir(parents=True)
        shutil.copyfile(
            DESKTOP / "src-tauri" / "icons" / "32x32.png",
            root / "Algebra" / "assets" / "plot.png",
        )
        (root / SOURCE).write_text(
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
        (root / TARGET).write_text(
            deck(
                "Analysis::Target",
                card("four", "Continuity", "Nearby inputs give nearby outputs."),
            )
        )
        (root / ABSORBED).write_text(
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
