# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright", "psutil"]
# ///
"""Save a complete learning store while Study is active."""

import json
import sqlite3
import tempfile
from contextlib import closing
from hashlib import sha256
from pathlib import Path

from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def rows(path: Path) -> dict[str, list]:
    with closing(sqlite3.connect(path)) as connection:
        tables = [
            name
            for (name,) in connection.execute(
                "select name from sqlite_master where type='table' order by name"
            )
        ]
        return {
            name: connection.execute(f'select * from "{name}" order by id').fetchall()
            for name in tables
        }


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="flashcards-study-copy-") as directory:
        root = Path(directory)
        workspace = root / "workspace"
        workspace.mkdir()
        (workspace / "triangle.svg").write_bytes(
            (Path(__file__).parent / "fixtures/study/triangle.svg").read_bytes()
        )
        (workspace / "Copy.md").write_text(
            "".join(
                f'::: {{.front card-id="copy-{i}"}}\nRecall {i}.\n![Triangle](triangle.svg)\n:::\n\n'
                f'::: {{.back card-id="copy-{i}"}}\nAnswer {i}.\n:::\n\n'
                for i in range(2)
            )
        )
        destination = root / "copies"
        destination.mkdir()
        with sync_playwright() as playwright:
            api = playwright.request.new_context(
                base_url="http://127.0.0.1:1420",
                extra_http_headers={"x-flashcards": "1"},
            )

            def request(action: str, **values):
                response = api.post(
                    "/api/request",
                    data={"action": action, "workspace": str(workspace), **values},
                )
                assert response.ok, response.text()
                return response.json()

            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page(viewport={"width": 900, "height": 700})
            try:
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready", timeout=30000
                )
                opened = request("study-open")
                record = Path(opened["record"])
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_role("button", name="Study", exact=True).click()
                study = page.get_by_role("region", name="Study session")
                study.get_by_role("button", name="Show answer", exact=False).click()
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    study.get_by_role("button", name="Show answer", exact=False)
                ).to_be_visible()
                expect(
                    study.get_by_role("button", name="Undo", exact=True)
                ).to_be_enabled()
                study.get_by_role("button", name="Study settings", exact=True).click()
                dialog = page.get_by_role("dialog", name="Study settings")
                before = rows(record)
                dialog.get_by_label("Copy destination", exact=True).fill(
                    str(root / "absent")
                )
                dialog.get_by_role("button", name="Save a copy", exact=True).click()
                expect(dialog.get_by_role("alert")).to_contain_text("CopyFailed")
                assert rows(record) == before
                dialog.get_by_label("Copy destination", exact=True).fill(
                    str(destination)
                )
                dialog.get_by_role("button", name="Save a copy", exact=True).click()
                expect(dialog.get_by_role("status")).to_contain_text("Copy saved:")
                copied = list(destination.glob("math-flashcards-study-*/*"))
                assert len(copied) == 1, copied
                copied = copied[0]
                assert copied.name == Path(opened["store"]).name
                assert {
                    "store.json",
                    "collection.anki2",
                    "record.sqlite3",
                    "record-media",
                    "record-assets",
                } <= {path.name for path in copied.iterdir()}
                assert rows(copied / "record.sqlite3") == before
                with closing(sqlite3.connect(copied / "record.sqlite3")) as saved:
                    for (digest,) in saved.execute("select distinct digest from media"):
                        assert (
                            sha256(
                                (copied / "record-media" / digest).read_bytes()
                            ).hexdigest()
                            == digest
                        )
                    for (identity,) in saved.execute(
                        "select distinct assets from content"
                    ):
                        asset = copied / "record-assets" / f"{identity}.json"
                        assert json.loads(asset.read_text())["identity"] == identity
                        assert (
                            asset.read_bytes()
                            == (
                                Path(opened["store"]) / "record-assets" / asset.name
                            ).read_bytes()
                        )
                with closing(
                    sqlite3.connect(copied / "collection.anki2")
                ) as collection:
                    assert collection.execute(
                        "select count(*) from revlog"
                    ).fetchone() == (1,)
                with closing(sqlite3.connect(record)) as saved:
                    assert saved.execute(
                        "select path from store_event where kind='copied'"
                    ).fetchall() == [(str(copied),)]
                page.screenshot(path=str(artifacts / "copy-saved.png"))
                page.keyboard.press("Escape")
                expect(dialog).not_to_be_visible()
                expect(
                    study.get_by_role("button", name="Undo", exact=True)
                ).to_be_disabled()
                study.get_by_role("button", name="Show answer", exact=False).click()
                study.get_by_role("button", name="Easy", exact=False).click()
                expect(
                    study.get_by_role("heading", name="Study complete for now")
                ).to_be_visible()
                expect(
                    study.get_by_role("button", name="Undo", exact=True)
                ).to_be_enabled()
                assert len(rows(record)["response"]) == 2
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
                api.dispose()


if __name__ == "__main__":
    with evidence("study-copy", Path(__file__).parent / "fixtures/study") as artifacts:
        main(artifacts)
