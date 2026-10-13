#!/usr/bin/env python3
"""Validate paired card decks with Pandoc and the app's pairing filter."""

import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DECKS = ROOT / "decks"

errors = []
deck_count = card_count = 0


def check_images(node, directory):
    # Pandoc owns image syntax and URLs: https://pandoc.org/lua-filters.html#type-image
    if isinstance(node, list):
        for child in node:
            check_images(child, directory)
    if isinstance(node, dict):
        if node.get("t") == "Image":
            url = urlsplit(node["c"][-1][0])
            if (
                url.scheme not in ("http", "https")
                and not (directory / unquote(url.path)).is_file()
            ):
                errors.append(f"{directory}: missing local figure: {url.path}")
        for child in node.values():
            check_images(child, directory)


for p in sorted(DECKS.rglob("*.md")):
    deck_count += 1
    rel = p.relative_to(ROOT)
    process = subprocess.run(
        [
            "pandoc",
            "-f",
            "markdown",
            "--lua-filter",
            str(ROOT / "desktop" / "paired-cards.lua"),
            "-t",
            "json",
            str(p),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if process.returncode != 0:
        errors.append(f"{rel}: {process.stderr.strip()}")
        continue
    document = json.loads(process.stdout)
    if "title" not in document["meta"] or not document["meta"]["title"]["c"]:
        errors.append(f"{rel}: missing deck title")
    items = document["blocks"][0]["c"]
    card_count += len(items)
    check_images(document["blocks"], p.parent)

if errors:
    print(f"deck check FAILED ({len(errors)} problem(s)):", file=sys.stderr)
    for e in errors:
        print("  " + e, file=sys.stderr)
    sys.exit(1)
print(f"deck check OK: {deck_count} decks, {card_count} cards, all well-formed")
