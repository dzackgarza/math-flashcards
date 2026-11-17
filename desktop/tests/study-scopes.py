# /// script
# requires-python = ">=3.12"
# dependencies = ["anki", "playwright", "psutil"]
# ///
"""Study native deck and folder scopes with their visible scheduler counts."""

import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

import psutil
from anki.collection import Collection
from evidence import evidence
from playwright.sync_api import expect, sync_playwright


def main(artifacts: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="flashcards-study-scopes-") as directory:
        workspace = Path(directory)
        decks = {
            "Algebra/Groups.md": ["g1", "g2", "g3"],
            "Algebra/Rings.md": ["r1"],
            "Analysis/Real.md": ["a1"],
            "Algebra.md": ["standalone"],
        }
        for path, identities in decks.items():
            target = workspace / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(
                "".join(
                    f'::: {{.front card-id="{identity}"}}\nRecall {identity}.\n:::\n\n'
                    f'::: {{.back card-id="{identity}"}}\nAnswer {identity}.\n:::\n\n'
                    for identity in identities
                )
            )
        with sync_playwright() as playwright:
            api = playwright.request.new_context(
                base_url="http://127.0.0.1:1420",
                extra_http_headers={"x-flashcards": "1"},
            )

            def request(action: str, **values):
                response = api.post(
                    "/api/request",
                    data={
                        "action": action,
                        "workspace": str(workspace),
                        **values,
                    },
                )
                assert response.ok, response.text()
                return response.json()

            def open_window():
                browser = playwright.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto("http://127.0.0.1:1420")
                page.get_by_role("button", name="Workspace", exact=True).click()
                page.get_by_label("Workspace folder").fill(str(workspace))
                page.get_by_role("button", name="Open workspace", exact=True).click()
                expect(page.get_by_role("status", name="Study")).to_have_text(
                    "Study cards ready"
                )
                return browser, page

            browser, page = open_window()
            try:
                opened = request("study-open")
                cached = request("cache-manifest", generation=1)
                assert cached["state"] == "cached", cached
                assert request("cached-manifest", generation=1) == cached
                root = opened["counts"]
                assert root["counts"] == {"new": 6, "learning": 0, "review": 0}, root
                assert {
                    (child["kind"], child["path"]) for child in root["children"]
                } == {
                    ("folder", "Algebra"),
                    ("folder", "Analysis"),
                    ("deck", "Algebra.md"),
                }, root
                assert request("study-counts") == root
                begun = request(
                    "study-begin", scope={"kind": "deck", "path": "Algebra/Groups.md"}
                )
                current = begun["next"]
                for grade in ("again", "easy"):
                    assert current["card_id"] in decks["Algebra/Groups.md"], current
                    current = request(
                        "study-answer",
                        session=begun["session"],
                        presentation=current["presentation"],
                        grade=grade,
                        timing={"reveal_ms": 2000, "grade_ms": 1000, "unfocused_ms": 0},
                    )
                request("study-end", session=begun["session"])
            finally:
                browser.close()
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
            collection = Collection(str(Path(opened["store"]) / "collection.anki2"))
            try:
                review = collection.find_cards("is:review")
                assert len(review) == 1
                collection.sched.set_due_date(review, "0")
            finally:
                collection.close()
            browser, page = open_window()
            try:

                def tree_row(path: str):
                    return page.locator(".tree-row").filter(
                        has=page.get_by_label(f"Study counts for {path}", exact=True)
                    )

                tree_row("Algebra").click()
                tree_row("Analysis").click()
                for path, text in {
                    "workspace": "New: 4 Learning: 1 Review: 1",
                    "Algebra": "New: 2 Learning: 1 Review: 1",
                    "Algebra/Groups.md": "New: 1 Learning: 1 Review: 1",
                    "Algebra/Rings.md": "New: 1 Learning: 0 Review: 0",
                    "Algebra.md": "New: 1 Learning: 0 Review: 0",
                    "Analysis": "New: 1 Learning: 0 Review: 0",
                }.items():
                    expect(
                        page.get_by_label(f"Study counts for {path}", exact=True)
                    ).to_have_text(text, timeout=2000)

                def study_scope(kind: str, path: str, expected: set[str]):
                    tree_row(path).click(button="right")
                    page.get_by_role("menuitem", name="Study", exact=True).click()
                    study = page.get_by_role("region", name="Study session")
                    seen = set()
                    for _ in expected:
                        show = study.get_by_role(
                            "button", name="Show answer", exact=False
                        )
                        expect(show).to_be_visible()
                        with closing(sqlite3.connect(opened["record"])) as record:
                            identity = record.execute(
                                "select card_id from presentation order by id desc limit 1"
                            ).fetchone()[0]
                        assert identity in expected and identity not in seen, identity
                        seen.add(identity)
                        show.click()
                        study.get_by_role("button", name="Easy", exact=False).click()
                    expect(
                        study.get_by_role("heading", name="Study complete for now")
                    ).to_be_visible()
                    assert seen == expected
                    with closing(sqlite3.connect(opened["record"])) as record:
                        assert record.execute(
                            "select scope_kind,scope_path from session order by id desc limit 1"
                        ).fetchone() == (kind, path)
                    study.get_by_role(
                        "button", name="Return to editor", exact=False
                    ).click()

                study_scope("deck", "Algebra.md", {"standalone"})
                expect(
                    page.get_by_label("Study counts for workspace", exact=True)
                ).to_have_text("New: 3 Learning: 1 Review: 1")
                study_scope("deck", "Algebra/Rings.md", {"r1"})
                expect(
                    page.get_by_label("Study counts for Algebra", exact=True)
                ).to_have_text("New: 1 Learning: 1 Review: 1")
                study_scope("folder", "Algebra", set(decks["Algebra/Groups.md"]))
                expect(
                    page.get_by_label("Study counts for Algebra", exact=True)
                ).to_have_text("New: 0 Learning: 0 Review: 0")
                expect(
                    page.get_by_label("Study counts for workspace", exact=True)
                ).to_have_text("New: 1 Learning: 0 Review: 0")
                expect(
                    page.get_by_label("Study counts for Analysis", exact=True)
                ).to_have_text("New: 1 Learning: 0 Review: 0")
                page.screenshot(path=str(artifacts / "scoped-counts.png"))
                response = api.post(
                    "/api/request",
                    data={
                        "action": "study-begin",
                        "workspace": str(workspace),
                        "scope": {"kind": "deck", "path": "Missing.md"},
                    },
                )
                assert not response.ok and "UnknownScope" in response.text(), (
                    response.text()
                )
            finally:
                (artifacts / "window.txt").write_text(page.locator("body").inner_text())
                browser.close()
                api.dispose()


if __name__ == "__main__":
    with evidence(
        "study-scopes", Path(__file__).parent / "fixtures/study"
    ) as artifacts:
        main(artifacts)
