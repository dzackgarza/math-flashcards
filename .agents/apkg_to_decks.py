#!/usr/bin/env python3
"""Reconcile apkg-only cards into decks/ as nested-list Markdown (issue #1).

For every note in apkg/*.apkg whose normalized front is NOT already present in
decks/, emit it into a Markdown deck under decks/, mirroring the note's Anki deck
name (`A::B` -> decks/A/B.md, title "A::B"). Existing decks are never overwritten:
if a target file already exists, only genuinely-new cards are appended (semantic
merge — existing Markdown stays authoritative). Cards already covered in decks/ are
skipped, so this adds exactly the missing set the diff reports.

Media is unrecoverable (no apkg bundles any; all <img src="attachments/..."> are
dangling), so <img> tags are dropped, keeping surrounding text.

Run:  python3 .agents/apkg_to_decks.py
Then: python3 .agents/apkg_diff.py   (expect 0 missing)  &&  just build
"""
import html
import json
import re
import sqlite3
import sys
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APKG = ROOT / "apkg"
DECKS = ROOT / "decks"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from apkg_diff import normalize_front, deck_fronts  # noqa: E402


def html_to_md(s: str, indent: str = "") -> str:
    """Convert an Anki HTML field to Markdown paragraphs/lists at the given indent."""
    s = s.replace("\r", "")
    # latex delimiters -> markdown math; forbid $ inside a match so a conversion
    # can never span across an already-converted block (guards against malformed
    # source where a stray \( lives inside a \[ ... \] display block)
    s = re.sub(r"\\\[([^$]+?)\\\]", lambda m: f"$${m.group(1)}$$", s, flags=re.S)
    s = re.sub(r"\\\(([^$]+?)\\\)", lambda m: f"${m.group(1)}$", s, flags=re.S)
    # drop dangling images (no media exists), keep alt text if any
    s = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*>', lambda m: m.group(1), s)
    s = re.sub(r"<img[^>]*>", "", s)
    # inline emphasis / code / links
    s = re.sub(r"</?strong>", "**", s)
    s = re.sub(r"</?b>", "**", s)
    s = re.sub(r"</?em>", "*", s)
    s = re.sub(r"</?i>", "*", s)
    s = re.sub(r"<code>(.*?)</code>", lambda m: f"`{m.group(1)}`", s, flags=re.S)
    # external links -> markdown; dead local/wiki links (no scheme) -> plain text
    def _a(m):
        href, text = m.group(1), m.group(2)
        return f"[{text}]({href})" if re.match(r"https?://", href) else text
    s = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', _a, s, flags=re.S)
    s = re.sub(r"<h[1-6]>(.*?)</h[1-6]>", lambda m: f"**{m.group(1).strip()}**", s, flags=re.S)
    s = re.sub(r"<hr\s*/?>", "", s)  # avoid old-format '---' separator

    blocks = []

    def emit_list(ul_html):
        out = []
        for it in re.findall(r"<li>(.*?)</li>", ul_html, flags=re.S):
            it = html.unescape(re.sub(r"<[^>]+>", "", it)).strip()
            it = re.sub(r"\$\$\s*\$\$|\$\s*\$", "", it).strip()  # drop empty math
            if it:
                out.append(f"{indent}- {it}")
        return "\n".join(out)

    # split into <ul> blocks and <p> blocks in order
    for chunk in re.split(r"(<ul>.*?</ul>)", s, flags=re.S):
        chunk = chunk.strip()
        if not chunk:
            continue
        if chunk.startswith("<ul>"):
            blocks.append(emit_list(chunk))
        else:
            for para in re.split(r"</p>\s*<p>|</p>|<p>", chunk):
                para = re.sub(r"<[^>]+>", "", para)
                para = html.unescape(para).strip()
                if para:
                    blocks.append("\n".join(indent + ln for ln in para.splitlines()))
    return "\n\n".join(b for b in blocks if b.strip())


def front_to_md(s: str) -> str:
    """Front becomes a single top-level list item; flatten to one line."""
    md = html_to_md(s)
    md = re.sub(r"\s+", " ", md).strip()
    md = re.sub(r"^-\s+", "", md)  # front is never itself a list item
    return md


def deck_path(name: str) -> Path:
    """`A::B::C` -> decks/A/B/C.md, sanitized."""
    parts = [re.sub(r"[^\w .+-]", "_", p).strip() for p in name.split("::")]
    parts = [p for p in parts if p] or ["Recovered"]
    return DECKS.joinpath(*parts[:-1], parts[-1] + ".md")


def apkg_notes_with_deck(path: Path):
    with zipfile.ZipFile(path) as z:
        if "collection.anki2" not in z.namelist():
            return
        with tempfile.TemporaryDirectory() as d:
            z.extract("collection.anki2", d)
            con = sqlite3.connect(Path(d) / "collection.anki2")
            names = {str(k): v["name"] for k, v in json.loads(
                con.execute("select decks from col").fetchone()[0]).items()}
            q = ("select n.flds, c.did from notes n join cards c on c.nid=n.id "
                 "group by n.id")
            for flds, did in con.execute(q):
                parts = flds.split("\x1f")
                yield parts[0], (parts[1] if len(parts) > 1 else ""), names.get(str(did), "Recovered")
            con.close()


def render_card(front_raw: str, back_raw: str) -> str:
    front = front_to_md(front_raw)
    back = html_to_md(back_raw, indent="    ")
    if not back.strip():
        # original answer was an image; no apkg bundles media, so it is unrecoverable
        back = "    *(Answer was a figure; image not recovered.)*"
    return f"- {front}\n\n{back}\n"


def main():
    have = deck_fronts()
    # collect missing cards grouped by anki deck name; dedup by normalized front
    by_deck = defaultdict(dict)  # deck_name -> {key: (front,back)}
    seen_global = set()
    for path in sorted(APKG.glob("*.apkg")):
        for front, back, deck in apkg_notes_with_deck(path):
            key = normalize_front(front)
            if not key or key in have or key in seen_global:
                continue
            seen_global.add(key)
            by_deck[deck].setdefault(key, (front, back))

    written = added = 0
    for deck, cards in sorted(by_deck.items()):
        target = deck_path(deck)
        target.parent.mkdir(parents=True, exist_ok=True)
        rendered = [render_card(f, b) for f, b in cards.values()]
        if target.exists():
            # semantic merge: append only cards whose front is not already in this file
            existing = target.read_text(encoding="utf-8")
            body_keys = {normalize_front(m.group(1))
                         for m in re.finditer(r"(?m)^- (\S.*)$", existing)}
            new = [r for f, b in cards.values()
                   if normalize_front(f) not in body_keys
                   for r in [render_card(f, b)]]
            if not new:
                continue
            sep = "" if existing.endswith("\n\n") else ("\n" if existing.endswith("\n") else "\n\n")
            target.write_text(existing + sep + "\n".join(new), encoding="utf-8")
            added += len(new)
        else:
            header = f'---\ntitle: "{deck}"\n---\n\n'
            target.write_text(header + "\n".join(rendered), encoding="utf-8")
            added += len(rendered)
            written += 1
    print(f"wrote {written} new deck files, added {added} cards across {len(by_deck)} decks")


if __name__ == "__main__":
    main()
