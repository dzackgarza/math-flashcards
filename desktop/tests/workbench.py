# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright"]
# ///
"""Exercise the editor and real export pipeline in a disposable workspace."""

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import zipfile
from pathlib import Path

from playwright.sync_api import (
    APIResponse,
    Request,
    Route,
    WebSocketRoute,
    expect,
    sync_playwright,
)


def startup() -> None:
    """Edit and save a current deck while workspace checks have partial coverage."""
    desktop = Path(__file__).resolve().parents[1]
    artifacts = desktop / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="flashcards-startup-") as directory:
        workspace = Path(directory) / "workspace"
        shutil.copytree(
            desktop.parent / "decks", workspace, ignore=shutil.ignore_patterns("apkg")
        )
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            errors: list[str] = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            try:
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                expect(page.get_by_label("Workspace folder")).to_have_value(
                    str(desktop.parent / "decks"), timeout=30000
                )
                page.get_by_label("Workspace folder").fill(str(workspace))
                opened = time.monotonic()
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(
                    page.get_by_role("button", name="Workspace", exact=True)
                ).to_have_text(workspace.name)
                tree_seconds = time.monotonic() - opened
                page.screenshot(path=str(artifacts / "startup-tree.png"))
                progress = page.locator(".workspace-progress")
                expect(progress).to_contain_text("Checking")
                page.get_by_role("button", name="Search Ctrl K", exact=True).click()
                page.get_by_placeholder("Search decks, cards, and commands").fill(
                    "__not_a_card__"
                )
                expect(
                    page.get_by_text(
                        "Search is incomplete while workspace cards load.", exact=True
                    )
                ).to_be_visible()
                page.screenshot(path=str(artifacts / "startup-search.png"))
                page.keyboard.press("Escape")
                page.get_by_text("Analysis", exact=True).click()
                selected = time.monotonic()
                page.get_by_text("Precalculus", exact=True).click()
                front = page.locator(".side-editor.front .cm-content")
                expect(front).to_be_visible()
                editable_seconds = time.monotonic() - selected
                expect(progress).to_contain_text("Checking")
                typed = time.monotonic()
                front.fill("Startup input $x^2$")
                expect(front).to_contain_text("Startup input")
                input_seconds = time.monotonic() - typed
                # Send two CodeMirror input transactions in one browser task.
                # React can batch both state updates, so the second must not
                # rebuild the deck from the draft captured before the first.
                inserted = page.evaluate("""() => {
                  const front = document.querySelector('.side-editor.front .cm-content');
                  const back = document.querySelector('.side-editor.back .cm-content');
                  front.focus();
                  const first = document.execCommand('insertText', false, ' rapid-front');
                  back.focus();
                  const second = document.execCommand('insertText', false, 'rapid-back ');
                  return [first, second];
                }""")
                assert inserted == [True, True], inserted
                expect(front).to_contain_text("rapid-front")
                expect(page.locator(".side-editor.back .cm-content")).to_contain_text(
                    "rapid-back"
                )
                deck = workspace / "Analysis" / "Precalculus.md"
                for _ in range(300):
                    if "Startup input $x^2$" in deck.read_text():
                        break
                    page.wait_for_timeout(100)
                saved = deck.read_text()
                assert "Startup input $x^2$" in saved
                assert "rapid-front" in saved and "rapid-back" in saved
                page.screenshot(path=str(artifacts / "startup-editing.png"))
                expect(progress).to_have_text(
                    "Workspace checks complete", timeout=120000
                )
                assert not errors, errors
                (artifacts / "startup-progressive.json").write_text(
                    json.dumps(
                        {
                            "tree_seconds": tree_seconds,
                            "editable_seconds": editable_seconds,
                            "input_seconds": input_seconds,
                            "background_seconds": time.monotonic() - opened,
                        },
                        indent=2,
                    )
                    + "\n"
                )
            finally:
                page.screenshot(path=str(artifacts / "startup-last.png"))
                context.tracing.stop(path=str(artifacts / "startup-trace.zip"))
                (artifacts / "startup-errors.json").write_text(json.dumps(errors))
                browser.close()


def main() -> None:
    cache_root = Path(os.environ["XDG_CACHE_HOME"])
    assert cache_root.name.startswith("flashcards-browser-cache-"), (
        "Run this scenario through just desktop-test."
    )
    repo = Path(__file__).resolve().parents[1]
    artifacts = repo / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="flashcards-test-") as directory:
        root = Path(directory)
        (root / "Analysis").mkdir(parents=True)
        shutil.copyfile(
            repo.parent / "decks" / "Analysis" / "Precalculus.md",
            root / "Analysis" / "Precalculus.md",
        )
        deck_path = root / "Analysis" / "Precalculus.md"
        authored_source = deck_path.read_bytes()
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            launched = time.monotonic()
            console: list[str] = []
            page.on("pageerror", lambda error: console.append(str(error)))
            page.goto("http://127.0.0.1:1420")
            status = page.locator(".toolbar .status")
            expect(
                page.get_by_role("heading", name="Math Flashcards", exact=True)
            ).to_be_visible()
            page.get_by_role("button", name="Workspace", exact=True).click()
            expect(page.get_by_label("Workspace folder")).to_have_value(
                str(repo.parent / "decks"), timeout=30000
            )
            expect(
                page.get_by_role("button", name="Refresh workspace", exact=True)
            ).to_be_enabled(timeout=30000)
            initial_tree_seconds = time.monotonic() - launched
            page.screenshot(path=str(artifacts / "empty.png"))
            page.get_by_label("Workspace folder").fill(str(root))
            workspace_started = time.monotonic()
            page.get_by_role("button", name="Open workspace", exact=True).click()
            expect(
                page.get_by_role("button", name="Workspace", exact=True)
            ).to_have_text(root.name, timeout=30000)
            tree_seconds = time.monotonic() - workspace_started
            page.get_by_text("Analysis", exact=True).click()
            selected = time.monotonic()
            page.get_by_text("Precalculus", exact=True).click()
            expect(status).to_contain_text("not in the Anki package", timeout=30000)
            expect(page.locator(".side-editor.front .cm-editor")).to_be_visible()
            expect(page.locator(".side-editor.back .cm-editor")).to_be_visible()
            editable_seconds = time.monotonic() - selected
            front_math = page.locator(".side-editor.front .cm-content mjx-container")
            back_math = page.locator(".side-editor.back .cm-content mjx-container")
            # MathJax 4 sets \pi as the mathematical italic letter U+1D70B.
            expect(front_math).to_contain_text("\U0001d70b/6", timeout=30000)
            expect(back_math.first).to_be_visible()
            renderer_seconds = time.monotonic() - selected
            (artifacts / "startup.json").write_text(
                json.dumps(
                    {
                        "revision": subprocess.check_output(
                            ["git", "rev-parse", "HEAD"], cwd=repo, text=True
                        ).strip(),
                        "machine": platform.uname()._asdict(),
                        "corpus": {
                            "path": "Analysis/Precalculus.md",
                            "sha256": hashlib.sha256(authored_source).hexdigest(),
                            "bytes": len(authored_source),
                            "package_bytes": 0,
                        },
                        "seconds": {
                            "launch_to_default_tree": initial_tree_seconds,
                            "workspace_to_tree": tree_seconds,
                            "selection_to_editable": editable_seconds,
                            "selection_to_rendered": renderer_seconds,
                        },
                    },
                    indent=2,
                )
                + "\n"
            )
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
            delayed: list[tuple[Route, APIResponse]] = []

            def delay_first_review(route: Route) -> None:
                payload = route.request.post_data_json
                if payload.get("action") == "review" and not delayed:
                    # Delay delivery of the real backend response without changing it.
                    delayed.append((route, route.fetch()))
                else:
                    route.continue_()

            page.route("**/api/request", delay_first_review)
            status.click()
            review = page.get_by_role(
                "dialog", name="Changes not in the Anki packages", exact=True
            )
            for _ in range(300):
                if delayed:
                    break
                page.wait_for_timeout(100)
            assert delayed
            review.get_by_role("button", name="Close", exact=True).click()
            front = page.locator(".side-editor.front .cm-content")
            front.fill(front.inner_text() + " Current review")
            saved(lambda text: "Current review" in text)
            status.click()
            expect(review).to_contain_text("Current review", timeout=30000)
            delayed_route, delayed_response = delayed[0]
            delayed_route.fulfill(response=delayed_response)
            page.evaluate(
                "() => new Promise(resolve => requestAnimationFrame(() => "
                "requestAnimationFrame(resolve)))"
            )
            expect(review).to_contain_text("Current review")
            page.unroute("**/api/request", delay_first_review)
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
            package = root / "apkg" / "Analysis__Precalculus.apkg"
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
            (root / "Analysis" / "Broken.md").write_text(
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
            try:
                page.set_viewport_size({"width": 1440, "height": 1000})
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=60000
                )
                derived = cache_root / "math-flashcards" / "derived.sqlite3"
                provenance = cache_root / "math-flashcards" / "builds.sqlite3"
                broken = root / "Analysis" / "Broken.md"
                with sqlite3.connect(provenance) as database:
                    original_build = database.execute(
                        "SELECT record FROM deck_builds WHERE path = ?",
                        (str(deck_path),),
                    ).fetchone()[0]
                with sqlite3.connect(derived) as database:
                    stored = json.loads(
                        database.execute(
                            "SELECT record FROM problem_checks WHERE root = ? AND path = ?",
                            (str(root), "Analysis/Broken.md"),
                        ).fetchone()[0]
                    )
                assert (
                    stored["revision"]
                    == hashlib.sha256(broken.read_bytes()).hexdigest()
                )
                assert len(stored["problems"]) == 2
                page.screenshot(path=str(artifacts / "cache-cold.png"))

                def restore_workspace() -> None:
                    page.on("pageerror", lambda error: console.append(str(error)))
                    page.goto("http://127.0.0.1:1420")
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    expect(page.get_by_label("Workspace folder")).to_have_value(
                        str(repo.parent / "decks"), timeout=30000
                    )
                    page.get_by_label("Workspace folder").fill(str(root))
                    page.get_by_role(
                        "button", name="Open workspace", exact=True
                    ).click()
                    expect(
                        page.get_by_role("button", name="Workspace", exact=True)
                    ).to_have_text(root.name)

                page.close()
                page = context.new_page()
                delayed_checks: list[tuple[Route, APIResponse]] = []

                def delay_package_checks(route: Route) -> None:
                    payload = route.request.post_data_json
                    if (
                        payload.get("action") == "checks"
                        and payload.get("workspace") == str(root)
                        and not delayed_checks
                    ):
                        delayed_checks.append((route, route.fetch()))
                    else:
                        route.continue_()

                page.route("**/api/request", delay_package_checks)
                page.add_init_script(
                    """(expected => {
                      window.packageHistory = [];
                      new MutationObserver(() => {
                        if (document.querySelector('.workspace-name')?.textContent !== expected) return;
                        for (const row of document.querySelectorAll('[data-deck][data-previous-package-status]')) {
                          window.packageHistory.push({path: row.dataset.deck, state: row.dataset.packageState, previous: row.dataset.previousPackageStatus});
                        }
                      }).observe(document, {subtree: true, childList: true, attributes: true, attributeFilter: ['data-package-state', 'data-previous-package-status']});
                    })("""
                    + json.dumps(root.name)
                    + ");"
                )
                with (
                    page.expect_response(
                        lambda response: (
                            response.url.endswith("/api/request")
                            and response.request.post_data_json.get("action")
                            == "cached-checks"
                            and response.request.post_data_json.get("workspace")
                            == str(root)
                        )
                    ) as package_history_response,
                    page.expect_response(
                        lambda response: (
                            response.url.endswith("/api/request")
                            and response.request.post_data_json.get("action")
                            == "search"
                            and response.request.post_data_json.get("workspace")
                            == str(root)
                        )
                    ) as search_response,
                    page.expect_response(
                        lambda response: (
                            response.url.endswith("/api/request")
                            and response.request.post_data_json.get("action")
                            == "problems"
                            and response.request.post_data_json.get("workspace")
                            == str(root)
                        )
                    ) as cached_response,
                ):
                    restore_workspace()
                    page.get_by_text("Analysis", exact=True).click()
                    expect(
                        page.locator('[data-deck="Analysis/Precalculus.md"]')
                    ).to_have_attribute("data-package-state", "checking")
                    for _ in range(300):
                        if delayed_checks:
                            break
                        page.wait_for_timeout(100)
                    assert delayed_checks
                    check_route, check_response = delayed_checks[0]
                    check_route.fulfill(response=check_response)
                    page.unroute("**/api/request", delay_package_checks)
                cached = cached_response.value.json()
                saved_search = search_response.value.json()
                history = package_history_response.value.json()
                assert all(
                    result["state"] == "pending" for result in history["results"]
                )
                assert any(
                    result["path"] == "Analysis/Precalculus.md"
                    and result["previous"] is not None
                    for result in history["results"]
                )
                assert any(
                    result["state"] == "ready"
                    and result["path"] == "Analysis/Broken.md"
                    and result["source"] == broken.read_text()
                    for result in saved_search["results"]
                )
                assert any(
                    result["state"] == "ready"
                    and result["path"] == "Analysis/Broken.md"
                    for result in cached["results"]
                )
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                observed_history = page.evaluate("window.packageHistory")
                assert any(
                    result["path"] == "Analysis/Precalculus.md"
                    and result["state"] in {"pending", "checking"}
                    for result in observed_history
                ), observed_history
                expect(
                    page.locator('[data-deck="Analysis/Precalculus.md"]')
                ).to_have_attribute("data-package-state", "ready")
                page.get_by_role("button", name="Show problems", exact=True).click()
                expect(
                    page.get_by_role("dialog", name="3 problems", exact=True)
                ).to_contain_text("Undefined control sequence \\undefinedmacro")
                page.screenshot(
                    path=str(artifacts / "cache-warm.png"), animations="disabled"
                )

                page.close()
                page = context.new_page()
                original = broken.read_text()
                edited = original.replace(r"\undefinedmacro", r"\undefinedmacrO")
                metadata = broken.stat()
                broken.write_text(edited)
                os.utime(broken, ns=(metadata.st_atime_ns, metadata.st_mtime_ns))
                restore_workspace()
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                page.get_by_role("button", name="Show problems", exact=True).click()
                drawer = page.get_by_role("dialog", name="3 problems", exact=True)
                expect(drawer).to_contain_text(
                    "Undefined control sequence \\undefinedmacrO"
                )
                page.screenshot(
                    path=str(artifacts / "cache-revalidated.png"), animations="disabled"
                )

                page.close()
                page = context.new_page()
                authored_cache_source = deck_path.read_bytes()
                with sqlite3.connect(derived) as database:
                    database.execute(
                        "UPDATE problem_checks SET record = ? WHERE root = ? AND path = ?",
                        ("damaged record", str(root), "Analysis/Broken.md"),
                    )
                    database.execute(
                        "UPDATE package_checks SET record = ? WHERE root = ? AND path = ?",
                        ("damaged record", str(root), "Analysis/Precalculus.md"),
                    )
                restore_workspace()
                rebuild = page.get_by_role(
                    "button", name="Rebuild cached data", exact=True
                )
                expect(rebuild).to_be_visible(timeout=30000)
                page.screenshot(path=str(artifacts / "cache-damaged.png"))
                rebuild.click()
                expect(rebuild).not_to_be_visible(timeout=30000)
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                with sqlite3.connect(derived) as database:
                    rebuilt = json.loads(
                        database.execute(
                            "SELECT record FROM problem_checks WHERE root = ? AND path = ?",
                            (str(root), "Analysis/Broken.md"),
                        ).fetchone()[0]
                    )
                assert (
                    rebuilt["revision"]
                    == hashlib.sha256(broken.read_bytes()).hexdigest()
                )
                assert any(
                    problem["message"] == "Undefined control sequence \\undefinedmacrO"
                    for problem in rebuilt["problems"]
                )
                with sqlite3.connect(provenance) as database:
                    assert (
                        database.execute(
                            "SELECT record FROM deck_builds WHERE path = ?",
                            (str(deck_path),),
                        ).fetchone()[0]
                        == original_build
                    )
                assert package.read_bytes() == good_package
                assert deck_path.read_bytes() == authored_cache_source
                assert broken.read_text() == edited
                page.screenshot(path=str(artifacts / "cache-rebuilt.png"))
                distant = root / "Elsewhere.md"
                distant_source = '---\ntitle: "Elsewhere"\n---\n\n::: {.front card-id="distant"}\nDistant question\n:::\n\n::: {.back card-id="distant"}\nRemote search proof $x^2$\n:::\n'
                distant.write_text(distant_source)
                expect(page.get_by_text("Elsewhere", exact=True)).to_be_visible(
                    timeout=30000
                )
                page.get_by_role("button", name="Search Ctrl K", exact=True).click()
                search = page.get_by_placeholder("Search decks, cards, and commands")
                search.fill("Remote search proof")
                result = page.get_by_text("Distant question", exact=True)
                expect(result).to_be_visible(timeout=30000)
                current_source = distant_source.replace(
                    'card-id="distant"', 'card-id="current"'
                ).replace("Distant question", "Current distant question")
                distant.write_text(current_source)
                result.click()
                expect(
                    page.get_by_text(
                        "Error: This card changed on disk. Search again for its current version.",
                        exact=True,
                    )
                ).to_be_visible(timeout=30000)
                page.get_by_role("button", name="Search Ctrl K", exact=True).click()
                search.fill("Remote search proof")
                current_result = page.get_by_text(
                    "Current distant question", exact=True
                )
                expect(current_result).to_be_visible(timeout=30000)
                current_result.click()
                expect(
                    page.get_by_role("heading", name="Elsewhere", exact=True)
                ).to_be_visible(timeout=30000)
                expect(page.locator(".side-editor.front .cm-content")).to_contain_text(
                    "Current distant question"
                )
                expect(page.locator(".side-editor.back .cm-content")).to_contain_text(
                    "Remote search proof"
                )
                assert distant.read_text() == current_source
                page.screenshot(path=str(artifacts / "workspace-search.png"))
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                expect(page.locator(".toolbar .status")).to_contain_text(
                    "not in the Anki package", timeout=30000
                )
                scopes: list[tuple[str, tuple[str, ...]]] = []

                def record_scope(request: Request) -> None:
                    if not request.url.endswith("/api/request"):
                        return
                    payload = request.post_data_json
                    if payload.get("workspace") == str(root) and payload.get(
                        "action"
                    ) in {"sources", "checks"}:
                        scopes.append((payload["action"], tuple(payload["paths"])))

                page.on("request", record_scope)
                with page.expect_response(
                    lambda response: (
                        response.url.endswith("/api/request")
                        and response.request.post_data_json.get("action") == "checks"
                        and response.request.post_data_json.get("workspace")
                        == str(root)
                        and "Elsewhere.md"
                        in response.request.post_data_json.get("paths", [])
                    )
                ):
                    distant.write_text(
                        current_source.replace(
                            "Current distant question", "Edited distant question"
                        )
                    )
                expect(page.locator(".side-editor.front .cm-content")).to_contain_text(
                    "Edited distant question", timeout=30000
                )
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                assert {path for _, paths in scopes for path in paths} == {
                    "Elsewhere.md"
                }, scopes

                shutil.copyfile(repo / "src-tauri/icons/32x32.png", root / "small.png")
                shutil.copyfile(
                    repo / "src-tauri/icons/128x128.png", root / "large.png"
                )
                diagram = root / "diagram.png"
                diagram.symlink_to("small.png")
                shared = {"Shared One.md", "Shared Two.md"}
                for name in sorted(shared):
                    identity = name.replace(".md", "").replace(" ", "-").lower()
                    (root / name).write_text(
                        f'---\ntitle: "{identity}"\n---\n\n::: {{.front card-id="{identity}"}}\nShared diagram\n:::\n\n::: {{.back card-id="{identity}"}}\n![Diagram](diagram.png)\n:::\n'
                    )
                headers = {"x-flashcards": "1", "content-type": "application/json"}
                asset_response = page.request.post(
                    "http://127.0.0.1:1420/api/request",
                    headers=headers,
                    data=json.dumps({"action": "assets"}),
                )
                assert asset_response.ok, asset_response.text()
                active_assets = asset_response.json()["identity"]
                for name in sorted(shared):
                    generated = page.request.post(
                        "http://127.0.0.1:1420/api/request",
                        headers=headers,
                        data=json.dumps(
                            {
                                "action": "generate",
                                "workspace": str(root),
                                "path": name,
                                "assets": active_assets,
                            }
                        ),
                    )
                    assert generated.ok, generated.text()
                    assert generated.json()["status"] == "Up to date"
                    expect(
                        page.locator(f'[data-deck="{name}"] .tree-dot')
                    ).to_have_count(0, timeout=30000)
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                scopes.clear()
                with page.expect_response(
                    lambda response: (
                        response.url.endswith("/api/request")
                        and response.request.post_data_json.get("action") == "checks"
                        and response.request.post_data_json.get("workspace")
                        == str(root)
                        and shared.issubset(
                            response.request.post_data_json.get("paths", [])
                        )
                    )
                ) as media_response:
                    subprocess.run(["trash", str(diagram)], check=True)
                    diagram.symlink_to("large.png")
                changed_media = media_response.value.json()
                assert {path for _, paths in scopes for path in paths} == shared, scopes
                assert not any(action == "sources" for action, _ in scopes), scopes
                for result in changed_media["results"]:
                    assert result["state"] == "ready" and result["status"] == "Unsynced"
                    assert "Media changed: diagram.png" in result["reasons"]
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                page.screenshot(path=str(artifacts / "media-invalidation.png"))
                delayed_review: list[tuple[Route, APIResponse]] = []
                exports: list[str] = []

                def delay_build_all_review(route: Route) -> None:
                    payload = route.request.post_data_json
                    if payload.get("action") == "review" and not delayed_review:
                        delayed_review.append((route, route.fetch()))
                    else:
                        if payload.get("action") == "generate":
                            exports.append(payload["workspace"])
                        route.continue_()

                page.route("**/api/request", delay_build_all_review)
                page.keyboard.press("Control+k")
                page.get_by_placeholder("Search decks, cards, and commands").fill(
                    "Update all Anki packages"
                )
                page.keyboard.press("Enter")
                for _ in range(300):
                    if delayed_review:
                        break
                    page.wait_for_timeout(100)
                assert delayed_review
                next_workspace = root / "Next workspace"
                next_workspace.mkdir()
                (next_workspace / "Fresh.md").write_text(
                    '---\ntitle: "Fresh"\n---\n\n::: {.front card-id="fresh"}\nNew workspace question\n:::\n\n::: {.back card-id="fresh"}\nNew workspace answer\n:::\n'
                )
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(next_workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(
                    page.get_by_role("button", name="Workspace", exact=True)
                ).to_have_text(next_workspace.name)
                page.get_by_text("Fresh", exact=True).click()
                expect(page.locator(".side-editor.front .cm-content")).to_contain_text(
                    "New workspace question"
                )
                old_route, old_response = delayed_review[0]
                old_route.fulfill(response=old_response)
                page.wait_for_timeout(1000)
                assert not exports, exports
                expect(page.locator(".side-editor.front .cm-content")).to_contain_text(
                    "New workspace question"
                )
                expect(page.locator(".generation-log")).to_have_count(0)
                page.unroute("**/api/request", delay_build_all_review)
                other = next_workspace / "Other.md"
                other.write_text(
                    (next_workspace / "Fresh.md")
                    .read_text()
                    .replace("Fresh", "Other")
                    .replace("fresh", "other")
                    .replace("New workspace", "Other deck")
                )
                expect(page.get_by_text("Other", exact=True)).to_be_visible()
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                deleted_load: list[tuple[Route, APIResponse]] = []

                def delay_deleted_load(route: Route) -> None:
                    payload = route.request.post_data_json
                    if (
                        payload.get("action") == "load"
                        and payload.get("path") == "Fresh.md"
                    ):
                        deleted_load.append((route, route.fetch()))
                    else:
                        route.continue_()

                page.route("**/api/request", delay_deleted_load)
                subprocess.run(["trash", str(next_workspace / "Fresh.md")], check=True)
                for _ in range(300):
                    if deleted_load:
                        break
                    page.wait_for_timeout(100)
                assert deleted_load
                assert not deleted_load[0][1].ok
                page.get_by_text("Other", exact=True).click()
                expect(page.locator(".side-editor.front .cm-content")).to_contain_text(
                    "Other deck question"
                )
                for route, response in deleted_load:
                    route.fulfill(response=response)
                page.wait_for_timeout(1000)
                expect(page.locator(".side-editor.front .cm-content")).to_contain_text(
                    "Other deck question"
                )
                expect(page.get_by_text("Action failed", exact=True)).to_have_count(0)
                page.unroute("**/api/request", delay_deleted_load)

                # A watcher notification that never arrives is recovered by
                # reconciliation when the window regains focus.
                page.close()
                page = context.new_page()
                page.on("pageerror", lambda error: console.append(str(error)))
                dropped: list[str] = []

                def drop_change_events(socket: WebSocketRoute) -> None:
                    server = socket.connect_to_server()

                    def forward(message: str | bytes) -> None:
                        if isinstance(message, str) and "flashcards:changed" in message:
                            dropped.append(message)
                            return
                        socket.send(message)

                    server.on_message(forward)

                page.route_web_socket(re.compile(r".*"), drop_change_events)
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                # The default preference loads into the field before it accepts input.
                expect(page.get_by_label("Workspace folder")).to_have_value(
                    str(repo.parent / "decks"), timeout=30000
                )
                page.get_by_label("Workspace folder").fill(str(next_workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(
                    page.get_by_role("button", name="Workspace", exact=True)
                ).to_have_text(next_workspace.name)
                expect(page.get_by_text("Other", exact=True)).to_be_visible()
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )
                (next_workspace / "Missed.md").write_text(
                    other.read_text()
                    .replace("Other", "Missed")
                    .replace("other", "missed")
                )
                for _ in range(100):
                    if any("Missed.md" in message for message in dropped):
                        break
                    page.wait_for_timeout(100)
                assert any("Missed.md" in message for message in dropped), dropped
                expect(page.get_by_text("Missed", exact=True)).to_have_count(0)
                page.evaluate("window.dispatchEvent(new Event('focus'))")
                expect(page.get_by_text("Missed", exact=True)).to_be_visible()
                expect(page.locator(".workspace-progress")).to_have_text(
                    "Workspace checks complete", timeout=30000
                )

                # Discovery for a superseded workspace cannot publish its tree.
                held_discovery: list[tuple[Route, APIResponse]] = []

                def hold_old_discovery(route: Route) -> None:
                    payload = route.request.post_data_json
                    if payload.get("workspace") == str(root) and payload.get(
                        "action"
                    ) in ("cached-manifest", "manifest"):
                        held_discovery.append((route, route.fetch()))
                    else:
                        route.continue_()

                page.route("**/api/request", hold_old_discovery)
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(root))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                for _ in range(300):
                    if held_discovery:
                        break
                    page.wait_for_timeout(100)
                assert held_discovery
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(next_workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_text("Missed", exact=True)).to_be_visible()
                page.wait_for_timeout(1000)
                for route, response in held_discovery:
                    route.fulfill(response=response)
                page.wait_for_timeout(1500)
                expect(
                    page.get_by_role("button", name="Workspace", exact=True)
                ).to_have_text(next_workspace.name)
                expect(page.get_by_text("Analysis", exact=True)).to_have_count(0)
                expect(page.get_by_text("Missed", exact=True)).to_be_visible()
                page.unroute("**/api/request", hold_old_discovery)
                assert not console, console
            finally:
                page.screenshot(path=str(artifacts / "cache-last.png"))
                context.tracing.stop(path=str(artifacts / "trace.zip"))
                (artifacts / "browser-errors.json").write_text(json.dumps(console))
                browser.close()
    print(
        "Edits save automatically; the open deck follows its file; the review lists changes; APKG includes saved cards."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--startup", action="store_true")
    arguments = parser.parse_args()
    # Install the Chromium build of the resolved Playwright version for every scenario.
    # https://playwright.dev/python/docs/browsers#install-browsers
    subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"], check=True
    )
    if arguments.startup:
        startup()
    else:
        main()
