#!/usr/bin/env python3
"""Extract every note from apkg/*.apkg, normalize fronts, and diff against decks/.

Acceptance-criterion tool for issue #1: proves whether every note in every committed
.apkg has a corresponding card in decks/ (normalized-front match).

Usage:
    python3 .agents/apkg_diff.py            # summary + missing-card report
    python3 .agents/apkg_diff.py --dump-missing PATH   # write missing cards as JSON
"""
import argparse
import html
import json
import re
import sqlite3
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path

# unify unicode punctuation that varies between apkg export and hand-authored decks
_PUNCT = {"’": "'", "‘": "'", "“": '"', "”": '"',
          "–": "-", "—": "-", "−": "-", " ": " "}

ROOT = Path(__file__).resolve().parent.parent
APKG = ROOT / "apkg"
DECKS = ROOT / "decks"


def strip_html(s: str) -> str:
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"</p>\s*<p>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s)


def normalize_front(s: str) -> str:
    """Collapse a front to a comparison key: strip HTML/markdown, LaTeX delims, whitespace, case."""
    s = strip_html(s)
    s = unicodedata.normalize("NFKC", s)
    for a, b in _PUNCT.items():
        s = s.replace(a, b)
    # unify latex delimiters \( \) \[ \] $ $$ -> nothing, keep the math text
    s = s.replace("\\(", " ").replace("\\)", " ").replace("\\[", " ").replace("\\]", " ")
    s = s.replace("$$", " ").replace("$", " ")
    # flatten markdown links [text](url) -> text
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    # drop markdown emphasis / code ticks
    s = re.sub(r"[*_`]", "", s)
    # collapse all whitespace and latex spacing commands
    s = s.replace("\\,", " ").replace("\\;", " ").replace("\\ ", " ").replace("~", " ")
    s = re.sub(r"\s+", " ", s)
    # strip trailing punctuation that varies (?, ., :)
    return s.strip().rstrip("?.:").strip().casefold()


def apkg_notes(path: Path):
    """Yield (front_raw, back_raw, tags) for each note in an apkg."""
    with zipfile.ZipFile(path) as z:
        if "collection.anki2" not in z.namelist():
            return
        with tempfile.TemporaryDirectory() as d:
            z.extract("collection.anki2", d)
            con = sqlite3.connect(Path(d) / "collection.anki2")
            for flds, tags in con.execute("select flds, tags from notes"):
                parts = flds.split("\x1f")
                front = parts[0] if parts else ""
                back = parts[1] if len(parts) > 1 else ""
                yield front, back, (tags or "").strip()
            con.close()


def deck_fronts():
    """Return set of normalized fronts present in decks/ (top-level '- ' items)."""
    keys = set()
    for p in sorted(DECKS.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
        for ln in body.splitlines():
            m = re.match(r"^- (\S.*)$", ln)
            if m:
                keys.add(normalize_front(m.group(1)))
    return keys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump-missing", metavar="PATH", help="write missing cards to JSON")
    args = ap.parse_args()

    have = deck_fronts()
    apkgs = sorted(APKG.glob("*.apkg"))

    total_notes = 0
    # unique-by-normalized-front across all apkgs; keep first raw + list of source apkgs
    uniq = {}
    for path in apkgs:
        for front, back, tags in apkg_notes(path):
            total_notes += 1
            key = normalize_front(front)
            if not key:
                continue
            rec = uniq.setdefault(key, {"front": front, "back": back, "tags": tags, "sources": []})
            rec["sources"].append(path.name)

    missing = {k: v for k, v in uniq.items() if k not in have}
    present = len(uniq) - len(missing)

    print(f"apkgs:                {len(apkgs)}")
    print(f"total notes (raw):    {total_notes}")
    print(f"unique fronts (apkg): {len(uniq)}")
    print(f"decks/ fronts:        {len(have)}")
    print(f"  covered in decks/:  {present}")
    print(f"  MISSING from decks: {len(missing)}")

    if args.dump_missing:
        out = [
            {"front": v["front"], "back": v["back"], "tags": v["tags"],
             "sources": sorted(set(v["sources"])), "key": k}
            for k, v in sorted(missing.items())
        ]
        Path(args.dump_missing).write_text(json.dumps(out, indent=2, ensure_ascii=False))
        print(f"\nwrote {len(out)} missing cards -> {args.dump_missing}")

    return 0 if not missing else 2


if __name__ == "__main__":
    sys.exit(main())
