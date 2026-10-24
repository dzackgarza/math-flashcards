# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright"]
# ///
"""Check the card field's live Markdown presentation and authored source."""

from pathlib import Path

from playwright.sync_api import expect, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page(viewport={"width": 900, "height": 900})
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.on(
        "console",
        lambda message: (
            errors.append(message.text) if message.type == "error" else None
        ),
    )
    page.goto("http://127.0.0.1:1420/tests/editor.html")
    editor = page.locator(".cm-content")
    expect(editor).to_be_visible()
    original = page.locator("output").text_content()
    page.get_by_role("button", name="Outside the editor").click()
    expect(editor.locator(".cm-list").first).to_be_visible()
    expect(editor.locator(".cm-strong").first).to_have_css("font-weight", "700")
    expect(editor.locator(".cm-emphasis").first).to_have_css("font-style", "italic")
    expect(editor.locator(".blockquote-wrapper")).to_be_visible()
    item = editor.locator(".cm-line").filter(has_text="A group has an identity")
    expect(item).to_have_count(1)
    assert item.evaluate("line => parseFloat(getComputedStyle(line).textIndent) < 0")
    assert item.evaluate("line => line.getBoundingClientRect().height > 40")
    assert page.locator("output").text_content() == original
    artifacts = Path(__file__).resolve().parents[1] / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    page.screenshot(path=str(artifacts / "markdown-editor.png"))
    editor.click()
    page.keyboard.press("Control+End")
    page.keyboard.type(" Appended.")
    expect(page.locator("output")).to_have_text(original + " Appended.")
    assert errors == [], errors
    browser.close()
