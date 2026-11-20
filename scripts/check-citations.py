#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Check that every card citation key names an item in the live Zotero library.

Card sides carry citations in a `cite` attribute in Pandoc citation syntax.
Pandoc parses each deck; its Cite elements give the keys. The running Zotero
desktop's local API supplies the Better BibTeX citation keys.

A cited item with no PDF attachment also fails the check: nobody can have
read the source to verify the cited claim and its locator.
"""

import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECKS = ROOT / "decks"
# Zotero local API: https://www.zotero.org/support/dev/zotero_7_for_developers#local_api
ZOTERO = "http://127.0.0.1:23119/api/users/0/items"


PDF_TYPES = {"application/pdf", "image/vnd.djvu"}


def zotero_keys() -> dict[str, str]:
    """Map each Better BibTeX citation key to its Zotero item key."""
    keys: dict[str, str] = {}
    start = 0
    while True:
        with urllib.request.urlopen(
            # A fixed sort keeps pages disjoint; the default order shifts between pages.
            f"{ZOTERO}/top?limit=100&start={start}&format=json&sort=dateAdded&direction=asc"
        ) as response:
            # Zotero emits raw control characters inside some field strings.
            page = json.loads(response.read().decode(), strict=False)
        if not page:
            return keys
        keys.update(
            (item["data"]["citationKey"], item["key"])
            for item in page
            if item["data"].get("citationKey")
        )
        start += 100


def walk(node, found: list[tuple[str, str]]) -> None:
    if isinstance(node, list):
        for child in node:
            walk(child, found)
    if isinstance(node, dict):
        if node.get("t") == "Div":
            attributes = dict(node["c"][0][2])
            if "cite" in attributes:
                found.append((attributes["card-id"], attributes["cite"]))
        for child in node.values():
            walk(child, found)


def cited_keys(cite: str) -> list[str]:
    process = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "json"],
        input=cite,
        capture_output=True,
        text=True,
        check=True,
    )
    keys: list[str] = []

    def visit(node):
        if isinstance(node, list):
            for child in node:
                visit(child)
        if isinstance(node, dict):
            if node.get("t") == "Cite":
                keys.extend(c["citationId"] for c in node["c"][0])
            for child in node.values():
                visit(child)

    visit(json.loads(process.stdout)["blocks"])
    return keys


def has_pdf(item: str) -> bool:
    # The children endpoint omits trashed attachments.
    with urllib.request.urlopen(f"{ZOTERO}/{item}/children?format=json") as response:
        children = json.loads(response.read().decode(), strict=False)
    return any(child["data"].get("contentType") in PDF_TYPES for child in children)


library = zotero_keys()
unread: dict[str, list[str]] = {}
missing: list[str] = []
count = 0
for path in sorted(DECKS.rglob("*.md")):
    if path.is_relative_to(DECKS / "apkg"):
        continue
    document = json.loads(
        subprocess.run(
            ["pandoc", "-f", "markdown", "-t", "json", str(path)],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    found: list[tuple[str, str]] = []
    walk(document["blocks"], found)
    for card, cite in found:
        for key in cited_keys(cite):
            count += 1
            if key not in library:
                missing.append(f"{path.relative_to(ROOT)}: {card}: @{key}")
                continue
            unread.setdefault(key, []).append(f"{path.relative_to(ROOT)}: {card}")

unread = {key: cards for key, cards in unread.items() if not has_pdf(library[key])}

if missing:
    print(f"citation check FAILED ({len(missing)} unknown key(s)):", file=sys.stderr)
    for line in missing:
        print("  " + line, file=sys.stderr)
if unread:
    print(
        f"citation check FAILED ({len(unread)} cited work(s) with no PDF in Zotero):"
        " these citations may need verification against the source, including"
        " their locators. Attach the PDF to the Zotero item.",
        file=sys.stderr,
    )
    for key, cards in sorted(unread.items()):
        print(f"  @{key}:", file=sys.stderr)
        for line in cards:
            print("    " + line, file=sys.stderr)
if missing or unread:
    sys.exit(1)
print(f"citation check OK: {count} citations resolve in Zotero")
