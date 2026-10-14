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


def display_math(inline):
    return inline.get("t") == "Math" and inline["c"][0]["t"] == "DisplayMath"


def check_math(node, rel):
    # Pandoc math needs no space inside $ delimiters: https://pandoc.org/MANUAL.html#math
    if isinstance(node, list):
        blocks = [child for child in node if isinstance(child, dict)]
        for before, after in zip(blocks, blocks[1:]):
            if before.get("t") != "Para" or after.get("t") != "Para":
                continue
            ends = [i for i in before["c"] if i["t"] not in ("Space", "SoftBreak")]
            if display_math(ends[-1]) or display_math(after["c"][0]):
                math = ends[-1] if display_math(ends[-1]) else after["c"][0]
                errors.append(
                    f"{rel}: blank line beside display math: {math['c'][1][:50]!r}"
                )
        for child in node:
            check_math(child, rel)
    if isinstance(node, dict):
        if node.get("t") == "Str" and "$" in node["c"]:
            errors.append(f"{rel}: $ outside math: {node['c']!r}")
        for child in node.values():
            check_math(child, rel)


for p in sorted(DECKS.rglob("*.md")):
    deck_count += 1
    rel = p.relative_to(ROOT)
    for number, line in enumerate(p.read_text().split("\n"), 1):
        if line != line.rstrip():
            errors.append(f"{rel}:{number}: trailing whitespace")
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
    check_math(document["blocks"], rel)

if errors:
    print(f"deck check FAILED ({len(errors)} problem(s)):", file=sys.stderr)
    for e in errors:
        print("  " + e, file=sys.stderr)
    sys.exit(1)
print(f"deck check OK: {deck_count} decks, {card_count} cards, all well-formed")
