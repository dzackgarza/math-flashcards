# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright"]
# ///
"""Measure Study events through the window with Playwright's browser clock."""

import sqlite3
import subprocess
import tempfile
import time
from contextlib import closing
from datetime import UTC, datetime
from pathlib import Path

from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="flashcards-study-timing-") as directory:
        workspace = Path(directory)
        folder = workspace / "Timing"
        folder.mkdir()
        faces = {
            "elapsed": ("Measure elapsed time.", "Elapsed answer."),
            "focus": ("Measure time without focus.", "Focus answer."),
            "long": (r"Unknown $\undefinedmacro x$.", "Long answer."),
        }
        source = "---\ntitle: Timing\ntags: [timing]\n---\n\n" + "".join(
            f'::: {{.front card-id="{identity}" tags="elapsed"}}\n{front}\n:::\n\n'
            f'::: {{.back card-id="{identity}"}}\n{back}\n:::\n\n'
            for identity, (front, back) in faces.items()
        )
        (folder / "Checks.md").write_text(source)
        with sync_playwright() as playwright:
            api = playwright.request.new_context(
                base_url="http://127.0.0.1:1420",
                extra_http_headers={"x-flashcards": "1"},
            )
            response = api.post(
                "/api/request",
                data={"action": "study-open", "workspace": str(workspace)},
            )
            assert response.ok, response.text()
            record_path = Path(response.json()["record"])
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            # Clock virtualizes performance.now and Event.timeStamp together.
            # It changes browser elapsed time, not Anki's backend wall clock:
            # https://playwright.dev/python/docs/clock
            page.clock.install(time="2030-01-01T00:00:00Z")
            try:
                page.goto("http://127.0.0.1:1420")
                page.context.new_cdp_session(page).send(
                    "Emulation.setFocusEmulationEnabled", {"enabled": False}
                )
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready"
                )
                expect(page.get_by_role("button", name="Show problems")).to_have_text(
                    "Problems1"
                )
                page.get_by_text("Timing", exact=True).click()
                page.get_by_text("Checks", exact=True).click()
                editor = page.locator(".editor-column .side-editor.front .cm-content")
                expect(editor).to_contain_text("Measure elapsed time.")
                page.clock.pause_at(
                    page.evaluate("new Date(Date.now() + 10).toISOString()")
                )
                page.locator(".card-row-label").filter(
                    has_text="Measure time without focus."
                ).click()
                page.clock.run_for(16)
                expect(editor).to_contain_text("Measure time without focus.")
                page.clock.fast_forward(1000)
                focused = subprocess.check_output(
                    ["xdotool", "getwindowfocus"], text=True
                ).strip()
                subprocess.run(["xdotool", "windowfocus", "0"], check=True)
                assert not page.evaluate("document.hasFocus()")
                page.clock.fast_forward(1000)
                subprocess.run(["xdotool", "windowfocus", focused], check=True)
                with page.expect_response(
                    lambda response: (
                        response.url.endswith("/api/request")
                        and response.request.post_data_json.get("action")
                        == "study-viewed"
                        and response.request.post_data_json.get("card_id") == "focus"
                    )
                ) as viewed:
                    page.locator(".card-row-label").filter(has_text="Unknown").click()
                    page.clock.run_for(16)
                assert viewed.value.ok, viewed.value.text()
                with closing(sqlite3.connect(record_path)) as record:
                    editor_view = record.execute(
                        "select card_id,deck_path,shown_ms,unfocused_ms from editor_view order by id desc limit 1"
                    ).fetchone()
                assert editor_view[:2] == ("focus", "Timing/Checks.md"), editor_view
                assert abs(editor_view[2] - 2000) <= 100, editor_view
                assert abs(editor_view[3] - 1000) <= 100, editor_view
                # Keep an actual read-only transaction open throughout the grades.
                with closing(
                    sqlite3.connect(f"file:{record_path}?mode=ro", uri=True)
                ) as reader:
                    reader.execute("begin")
                    tables = [
                        row[0]
                        for row in reader.execute(
                            "select name from sqlite_master where type='table'"
                        )
                    ]
                    for table in tables:
                        reader.execute(f'SELECT * FROM "{table}"').fetchall()
                    assert reader.execute(
                        "select count(*) from response"
                    ).fetchone() == (0,)
                    page.get_by_role("button", name="Workspace", exact=True).click()
                    page.clock.run_for(250)
                    page.get_by_role("button", name="Study", exact=True).click()
                    study = page.get_by_role("region", name="Study session")
                    seen = set()
                    for _ in faces:
                        show = study.get_by_role(
                            "button", name="Show answer", exact=False
                        )
                        deadline = time.monotonic() + 10
                        while not show.is_visible() and time.monotonic() < deadline:
                            page.clock.run_for(16)
                        expect(show).to_be_visible()
                        with closing(sqlite3.connect(record_path)) as record:
                            identity = record.execute(
                                "select card_id from presentation order by id desc limit 1"
                            ).fetchone()[0]
                        assert identity not in seen, identity
                        seen.add(identity)
                        if identity == "long":
                            expect(study.locator("mjx-merror")).to_be_visible()
                            page.screenshot(path=str(artifacts / "study-tex-error.png"))
                        if identity == "focus":
                            focused = subprocess.check_output(
                                ["xdotool", "getwindowfocus"], text=True
                            ).strip()
                            subprocess.run(["xdotool", "windowfocus", "0"], check=True)
                            assert page.evaluate("document.hasFocus()") is False
                            page.clock.fast_forward(2000)
                            subprocess.run(
                                ["xdotool", "windowfocus", focused], check=True
                            )
                            assert page.evaluate("document.hasFocus()") is True
                        else:
                            page.clock.fast_forward(2000)
                        page.keyboard.press("Space")
                        page.clock.run_for(16)
                        expect(
                            study.get_by_role("button", name="Easy", exact=False)
                        ).to_be_visible()
                        page.clock.fast_forward(
                            10800000 if identity == "long" else 1000
                        )
                        page.keyboard.press("4")
                        page.clock.run_for(16)
                    page.clock.resume()
                    expect(
                        study.get_by_role("heading", name="Study complete for now")
                    ).to_be_visible()
                    assert seen == set(faces)
                    with closing(sqlite3.connect(record_path)) as record:
                        assert record.execute(
                            "select card_id from editor_view order by id desc limit 1"
                        ).fetchone() == ("long",)
                    assert reader.execute(
                        "select count(*) from response"
                    ).fetchone() == (0,)
                    reader.execute("commit")
                    rows = reader.execute(
                        "select card_id,reveal_ms,grade_ms,unfocused_ms,revlog_time_ms,front,back from review order by id"
                    ).fetchall()
                    assert len(rows) == 3, rows
                    for identity, reveal, grade, away, limited, front, back in rows:
                        assert abs(reveal - 2000) <= 100, (identity, reveal)
                        expected_grade = 10800000 if identity == "long" else 1000
                        assert abs(grade - expected_grade) <= 100, (identity, grade)
                        assert (
                            abs(away - (2000 if identity == "focus" else 0)) <= 100
                        ), (identity, away)
                        assert limited == min(reveal + grade, 9999000), (
                            identity,
                            limited,
                        )
                        assert (front, back) == faces[identity]
                    folder_rows = reader.execute(
                        "SELECT folder,strftime('%Y-%m',at_ms/1000,'unixepoch'),count(*),avg(grade='again'),avg(reveal_ms) FROM review WHERE undone_at_ms IS NULL GROUP BY folder,2"
                    ).fetchall()
                    assert len(folder_rows) == 1
                    assert folder_rows[0][:4] == (
                        "Timing",
                        datetime.now(UTC).strftime("%Y-%m"),
                        3,
                        0.0,
                    ), folder_rows
                    assert abs(folder_rows[0][4] - 2000) <= 100, folder_rows
                    tag_rows = reader.execute(
                        "SELECT tag.value,count(*),avg(grade='again'),avg(reveal_ms) FROM review,json_each(review.tags) AS tag WHERE undone_at_ms IS NULL GROUP BY tag.value"
                    ).fetchall()
                    assert [(row[0], row[1], row[2]) for row in tag_rows] == [
                        ("elapsed", 3, 0.0),
                        ("timing", 3, 0.0),
                    ], tag_rows
                    assert all(abs(row[3] - 2000) <= 100 for row in tag_rows), tag_rows
                    history = reader.execute(
                        "SELECT at_ms,grade,front,back FROM review WHERE card_id=? ORDER BY at_ms",
                        ("long",),
                    ).fetchall()
                    assert len(history) == 1 and history[0][1:] == (
                        "easy",
                        *faces["long"],
                    ), history
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
                api.dispose()


if __name__ == "__main__":
    with evidence(
        "study-timing", Path(__file__).parent / "fixtures/study"
    ) as artifacts:
        main(artifacts)
