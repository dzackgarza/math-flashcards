#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""List card lines whose text, outside cite attributes, may cite a source.

The list is a shortlist for a reader. A match can be mathematics (a theorem
named after its authors), and prose can cite a source in a form no pattern
here matches, so an empty list does not show that the cards cite nothing in
prose. Read the cards to establish that.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECKS = ROOT / "decks"
NAME = r"[A-Z][\w'’-]+"
NAMES = rf"{NAME}(?:[–-]{NAME})*"
SIGNS = {
    "reference label": re.compile(r"\bReferences?:"),
    "bibliographic link": re.compile(
        r"arxiv\.org|doi\.org|stacks\.math|mathscinet|zbmath|numdam|projecteuclid"
    ),
    "author with italic title": re.compile(rf"\b{NAMES}, \*[^*]+\*"),
    "author with year": re.compile(rf"\b{NAMES},? \(?(?:1[89]|20)\d\d\)?"),
    "author with locator": re.compile(
        rf"\b{NAMES},? (?:§|Chapter|Theorem|Lemma|Proposition|Corollary|Definition|Example|Remark)"
    ),
    "parenthetical authors": re.compile(rf"\((?:[^()]*: )?{NAMES}(?:, {NAMES})*\)"),
    "see an author": re.compile(rf"\b[Ss]ee {NAMES}\b"),
}
CITE = re.compile(r' cite="[^"]*"')
MATH = re.compile(r"\$\$.*?\$\$|\$[^$]*\$")

count = 0
for path in sorted(DECKS.rglob("*.md")):
    if path.is_relative_to(DECKS / "apkg"):
        continue
    for number, line in enumerate(path.read_text().split("\n"), 1):
        text = MATH.sub("$…$", CITE.sub("", line))
        for sign, pattern in SIGNS.items():
            match = pattern.search(text)
            if match:
                count += 1
                start = max(0, match.start() - 60)
                print(f"{path.relative_to(ROOT)}:{number}: {sign}: …{text[start : match.end() + 60]}…")
print(f"{count} candidate line(s); this list is not exhaustive", file=sys.stderr)
