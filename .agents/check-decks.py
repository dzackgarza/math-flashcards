#!/usr/bin/env python3
"""Validate paired card decks with Pandoc and the app's pairing filter."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECKS = ROOT / "decks"

errors = []
deck_count = card_count = 0
for p in sorted(DECKS.rglob("*.md")):
    deck_count += 1
    rel = p.relative_to(ROOT)
    text = p.read_text(encoding="utf-8")
    if not re.match(r'^---\ntitle: "[^"]+"\n---\n', text):
        errors.append(f"{rel}: missing/!malformed title frontmatter")
    process = subprocess.run(
        ['pandoc', '-f', 'markdown', '--lua-filter', str(ROOT / 'desktop' / 'paired-cards.lua'), '-t', 'json', str(p)],
        capture_output=True, text=True,
    )
    if process.returncode != 0:
        errors.append(f"{rel}: {process.stderr.strip()}")
        continue
    items = json.loads(process.stdout)['blocks'][0]['c']
    if not items:
        errors.append(f"{rel}: no cards")
    card_count += len(items)
    for img in re.findall(r'!\[[^\]]*\]\((?!https?://)[^)]*\)', text):
        errors.append(f"{rel}: reference to missing local figure: {img}")

if errors:
    print(f"deck check FAILED ({len(errors)} problem(s)):", file=sys.stderr)
    for e in errors:
        print("  " + e, file=sys.stderr)
    sys.exit(1)
print(f"deck check OK: {deck_count} decks, {card_count} cards, all well-formed")
