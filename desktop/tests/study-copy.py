# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright", "psutil"]
# ///
"""Save a complete learning store while Study is active."""

import argparse
import json
import os
import shutil
import sqlite3
import subprocess
import tempfile
from contextlib import closing
from hashlib import sha256
from pathlib import Path

import psutil
from evidence import evidence
from playwright.sync_api import expect, sync_playwright

type RecordCell = str | int | float | None


def rows(path: Path) -> dict[str, list[list[RecordCell]]]:
    with closing(sqlite3.connect(path)) as connection:
        tables = [
            name
            for (name,) in connection.execute(
                "select name from sqlite_master where type='table' order by name"
            )
        ]
        return {
            name: [
                list(row)
                for row in connection.execute(f'select * from "{name}" order by id')
            ]
            for name in tables
        }


def restore(artifacts: Path) -> None:
    manifest = json.loads(Path(os.environ["FLASHCARDS_COPY_MANIFEST"]).read_text())
    workspace = Path(manifest["workspace"])
    record = (
        Path(os.environ["XDG_DATA_HOME"])
        / "math-flashcards/study"
        / manifest["store"]
        / "record.sqlite3"
    )
    assert rows(record) == manifest["rows"]
    with sync_playwright() as playwright:
        api = playwright.request.new_context(
            base_url="http://127.0.0.1:1421", extra_http_headers={"x-flashcards": "1"}
        )
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page(viewport={"width": 900, "height": 700})
        try:
            page.goto("http://127.0.0.1:1421")
            page.get_by_role("button", name="Workspace", exact=True).click()
            page.get_by_label("Workspace folder").fill(str(workspace))
            page.get_by_role("button", name="Open workspace", exact=True).click()
            dialog = page.get_by_role("dialog", name="Choose a study store")
            expect(dialog).to_contain_text("Grades: 1")
            page.screenshot(path=str(artifacts / "attach-copy.png"))
            dialog.get_by_role(
                "button", name=f"Attach {manifest['original_workspace']}", exact=True
            ).click()
            expect(page.get_by_role("status", name="Study")).to_have_text(
                "Study cards ready", timeout=30000
            )
            opened = api.post(
                "/api/request",
                data={"action": "study-open", "workspace": str(workspace)},
            )
            assert opened.ok, opened.text()
            assert opened.json()["counts"]["counts"] == manifest["counts"]
            current = rows(record)
            for table, original in manifest["rows"].items():
                assert current[table][: len(original)] == original, table
            page.get_by_role("button", name="Workspace", exact=True).click()
            page.get_by_role("button", name="Study", exact=True).click()
            study = page.get_by_role("region", name="Study session")
            image = study.get_by_role("img", name="Triangle", exact=True)
            expect(image).to_be_visible()
            expect(image).to_have_js_property("complete", True)
            assert image.evaluate("image => image.naturalWidth") > 0
            study.get_by_role("button", name="Show answer", exact=False).click()
            study.get_by_role("button", name="Easy", exact=False).click()
            expect(
                study.get_by_role("heading", name="Study complete for now")
            ).to_be_visible()
            assert len(rows(record)["response"]) == 2
            page.screenshot(path=str(artifacts / "restored-study.png"))
        finally:
            (artifacts / "window.txt").write_text(page.locator("body").inner_text())
            browser.close()
            api.dispose()


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
                counts_before = request("study-counts")["counts"]
                dialog.get_by_label("Copy destination", exact=True).fill(
                    str(root / "absent")
                )
                with page.expect_response(
                    lambda response: (
                        response.url.endswith("/api/request")
                        and response.request.post_data_json["action"] == "study-copy"
                    )
                ) as failed:
                    dialog.get_by_role("button", name="Save a copy", exact=True).click()
                assert (
                    failed.value.status == 422
                    and failed.value.json()["kind"] == "CopyFailed"
                )
                expect(dialog.get_by_role("alert")).to_contain_text(
                    str(root / "absent")
                )
                assert rows(record) == before
                dialog.get_by_label("Copy destination", exact=True).fill(
                    str(destination)
                )
                dialog.get_by_role("button", name="Save a copy", exact=True).click()
                expect(dialog.get_by_role("status")).to_contain_text("Copy saved:")
                expect(dialog.get_by_role("status")).to_be_in_viewport()
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
        hosts = [
            p
            for p in psutil.process_iter(["cmdline"])
            if p.info["cmdline"] is not None
            and "study-host" in p.info["cmdline"]
            and p.environ().get("XDG_DATA_HOME") == os.environ["XDG_DATA_HOME"]
        ]
        assert len(hosts) == 1
        hosts[0].terminate()
        hosts[0].wait(timeout=10)
        restored_data = root / "restored-data"
        shutil.copytree(copied, restored_data / "math-flashcards/study" / copied.name)
        moved = root / "moved-workspace"
        shutil.copytree(workspace, moved)
        manifest = artifacts / "restore-input.json"
        manifest.write_text(
            json.dumps(
                {
                    "workspace": str(moved),
                    "original_workspace": str(workspace),
                    "store": copied.name,
                    "rows": before,
                    "counts": counts_before,
                },
                indent=2,
            )
        )
        state = root / "restored-state"
        environment = os.environ | {
            "XDG_DATA_HOME": str(restored_data),
            "XDG_STATE_HOME": str(state),
            "XDG_CACHE_HOME": str(root / "restored-cache"),
            "FLASHCARDS_COPY_MANIFEST": str(manifest),
        }
        try:
            with (artifacts / "restore-server.log").open("w") as log:
                subprocess.run(
                    [
                        "bunx",
                        "start-server-and-test",
                        "bunx vite --host 127.0.0.1 --port 1421 --strictPort",
                        "http-get://127.0.0.1:1421",
                        "uv run --upgrade tests/study-copy.py restore",
                    ],
                    cwd=Path(__file__).resolve().parents[1],
                    env=environment,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    check=True,
                )
        finally:
            if state.exists():
                shutil.copytree(state, artifacts / "restored-application-state")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("copy", "restore"), nargs="?", default="copy")
    mode = parser.parse_args().mode
    with evidence(
        "study-copy" if mode == "copy" else "study-copy-restore",
        Path(__file__).parent / "fixtures/study",
    ) as artifacts:
        (main if mode == "copy" else restore)(artifacts)
