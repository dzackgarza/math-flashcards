#!/usr/bin/env python3
"""Sanity-check that every deck under decks/ is well-formed ankdown-for-math Markdown.
Fails (exit 1) on any regression: missing title frontmatter, no cards, leftover
old-format separators, or references to (missing) local figures."""
import re
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
    items = [ln for ln in text.splitlines() if re.match(r'^- \S', ln)]
    if not items:
        errors.append(f"{rel}: no cards (top-level '- ' items)")
    card_count += len(items)
    body = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.S)  # drop frontmatter
    if re.search(r'(?m)^%\s*$', body) or re.search(r'(?m)^---\s*$', body):
        errors.append(f"{rel}: leftover old-format separator (% or ---)")
    for img in re.findall(r'!\[[^\]]*\]\((?!https?://)[^)]*\)', text):
        errors.append(f"{rel}: reference to missing local figure: {img}")

if errors:
    print(f"deck check FAILED ({len(errors)} problem(s)):", file=sys.stderr)
    for e in errors:
        print("  " + e, file=sys.stderr)
    sys.exit(1)
print(f"deck check OK: {deck_count} decks, {card_count} cards, all well-formed")
