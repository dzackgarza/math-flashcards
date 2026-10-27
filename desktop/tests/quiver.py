# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright"]
# ///
"""Exercise the locally packaged Quiver editor and real offline Anki export."""

import json
import re
import sqlite3
import tempfile
import time
import zipfile
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import expect, sync_playwright


def main() -> None:
    desktop = Path(__file__).resolve().parents[1]
    artifacts = desktop / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    legacy = (desktop / "tests/fixtures/quiver-limit-url.txt").read_text().strip()
    with tempfile.TemporaryDirectory(prefix="flashcards-quiver-") as directory:
        root = Path(directory)
        deck = root / "Diagrams.md"
        deck.write_text(
            '---\ntitle: "Diagrams"\n---\n\n'
            '::: {.front card-id="limits"}\nWhat is a limit?\n:::\n\n'
            '::: {.back card-id="limits"}\nRemember: '
            + legacy
            + "\n\n~~~tex\n\\begin{tikzcd}\n\\undefinedLiteralExample\n"
            + "\\end{tikzcd}\n~~~\n:::\n"
        )
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 1000})
            errors: list[str] = []
            outside: list[str] = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.on(
                "request",
                lambda request: (
                    outside.append(request.url)
                    if urlparse(request.url).scheme in ("http", "https")
                    and urlparse(request.url).hostname not in ("127.0.0.1", "localhost")
                    else None
                ),
            )
            try:
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(root))
                page.get_by_role("button", name="Open workspace").click()
                page.get_by_text("Diagrams", exact=True).last.click()

                # The actual legacy link is decoded by the vendored Quiver
                # importer and presented as a diagram, never fetched remotely.
                back = page.locator(".side-editor.back")
                edit = back.get_by_role("button", name="Edit in Quiver")
                expect(edit).to_be_visible(timeout=30000)
                preview = back.frame_locator(
                    'iframe[title="Rendered commutative diagram"]'
                )
                expect(preview.locator(".vertex")).to_have_count(15, timeout=30000)
                # Rendering 15 vertices without fitting the diagram is still
                # unusable: the preview must show the entire graph, not a crop.
                expect(preview.locator(".canvas")).to_have_attribute(
                    "style", re.compile(r"scale\(0\.[0-9]+\)"), timeout=30000
                )
                geometry = preview.locator("body").evaluate(
                    """body => {
                      const width = body.clientWidth, height = body.clientHeight;
                      const points = [...body.querySelectorAll('.vertex')].map(vertex => {
                        const r = vertex.getBoundingClientRect();
                        return [r.left, r.top, r.right, r.bottom];
                      });
                      return { width, height, points };
                    }"""
                )
                assert all(
                    left >= -10
                    and top >= -10
                    and right <= geometry["width"] + 10
                    and bottom <= geometry["height"] + 10
                    for left, top, right, bottom in geometry["points"]
                ), geometry
                x_span = max(point[2] for point in geometry["points"]) - min(
                    point[0] for point in geometry["points"]
                )
                y_span = max(point[3] for point in geometry["points"]) - min(
                    point[1] for point in geometry["points"]
                )
                assert (
                    x_span > geometry["width"] * 0.5
                    and y_span > geometry["height"] * 0.35
                ), ("The diagram is too small to read.", geometry)
                page.screenshot(path=str(artifacts / "quiver-card-preview.png"))
                back.get_by_role("button", name="View larger").click()
                enlarged = page.get_by_role("dialog", name="Commutative diagram")
                expect(enlarged).to_be_visible()
                expect(
                    enlarged.frame_locator(
                        'iframe[title="Rendered commutative diagram"]'
                    ).locator(".vertex")
                ).to_have_count(15, timeout=30000)
                page.screenshot(path=str(artifacts / "quiver-card-enlarged.png"))
                page.keyboard.press("Escape")
                expect(enlarged).not_to_be_visible()
                # Normal card view shows the diagram, not the opaque link.
                assert all(
                    "q.uiver.app" not in text
                    for text in back.locator(".cm-content").all_inner_texts()
                )
                back.get_by_role("button", name="Edit source").click()
                expect(back.locator(".cm-content")).to_contain_text("q.uiver.app")
                back.get_by_role("button", name="Visual view").click()
                back.locator(".cm-content").first.fill("Remember: categorical limits.")
                expect(back.locator(".cm-content").first).to_contain_text(
                    "categorical limits"
                )
                edit.click()
                frame = page.frame_locator('iframe[title="Quiver diagram editor"]')
                expect(frame.locator(".vertex")).to_have_count(15, timeout=30000)
                page.screenshot(path=str(artifacts / "quiver-diagram-editor.png"))
                apply = page.get_by_role("button", name="Use diagram")
                expect(apply).to_be_enabled(timeout=30000)
                apply.click()

                deadline = time.monotonic() + 75
                while time.monotonic() < deadline:
                    saved = deck.read_text()
                    if r"\begin{tikzcd}" in saved and "q.uiver.app" not in saved:
                        break
                    time.sleep(0.1)
                else:
                    raise AssertionError("The Quiver import was not saved in the deck.")
                assert r"\arrow[" in saved and "nfold" in saved
                assert "Remember: categorical limits." in saved
                # One authored diagram and one *literal* TeX code example.
                assert saved.count(r"\begin{tikzcd}") == 2
                expect(back.get_by_role("button", name="Edit in Quiver")).to_have_count(
                    1
                )

                # Reimport the canonical TikZ-cd, including its higher-cell
                # styles, and verify cancelling leaves the authored file alone.
                edit = back.get_by_role("button", name="Edit in Quiver")
                edit.click()
                expect(frame.locator(".vertex")).to_have_count(15, timeout=30000)
                expect(page.get_by_role("button", name="Use diagram")).to_be_enabled()
                page.get_by_role("button", name="Cancel", exact=True).click()
                assert deck.read_text() == saved

                # Create a new diagram with the *actual* Quiver grid gestures.
                page.locator(".side-editor.front").get_by_role(
                    "button", name="New diagram"
                ).click()
                expect(apply).to_be_enabled(timeout=30000)
                expect(frame.locator(".vertex")).to_have_count(0)
                frame.locator("body").click(position={"x": 330, "y": 300})
                frame.locator(".focus-point").click(force=True)
                expect(frame.locator(".vertex")).to_have_count(1)
                apply.click()
                deadline = time.monotonic() + 75
                while time.monotonic() < deadline:
                    saved = deck.read_text()
                    if saved.count(r"\begin{tikzcd}") == 3:
                        break
                    time.sleep(0.1)
                else:
                    raise AssertionError("The new Quiver diagram was not saved.")

                # Export through the real Python/Pandoc/Ankdown backend. Both
                # diagrams must be embedded as offline SVG in the Anki note.
                def backend(payload: dict[str, object]) -> dict[str, object]:
                    response = page.request.post(
                        "http://127.0.0.1:1420/api/request",
                        headers={
                            "x-flashcards": "1",
                            "content-type": "application/json",
                        },
                        data=json.dumps(payload),
                        timeout=120000,
                    )
                    assert response.ok, response.text()
                    return response.json()

                assets = backend({"action": "assets"})["identity"]
                exported = backend(
                    {
                        "action": "generate",
                        "workspace": str(root),
                        "path": "Diagrams.md",
                        "assets": assets,
                    }
                )
                assert exported["status"] == "Up to date"
                with zipfile.ZipFile(exported["package"]) as archive:
                    collection = archive.read("collection.anki2")
                sqlite = root / "collection-verify.sqlite3"
                sqlite.write_bytes(collection)
                with sqlite3.connect(sqlite) as database:
                    fields = [
                        record[0]
                        for record in database.execute("SELECT flds FROM notes")
                    ]
                assert len(fields) == 1 and fields[0].count("<svg") == 2
                assert "undefinedLiteralExample" in fields[0]
                assert "q.uiver.app" not in fields[0]
                assert not outside, outside
                assert not errors, errors
            finally:
                browser.close()
    print(
        "Quiver legacy import, editing, graphical creation, save, offline Anki SVG: passed."
    )


if __name__ == "__main__":
    main()
