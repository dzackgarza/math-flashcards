# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "ankdown @ git+https://github.com/dzackgarza/ankdown-for-math@5878dff3082334d33609b0999eb849d8c6db6812",
#   "cyclopts==4.15.0",
#   "filelock==3.20.3",
#   "platformdirs==4.5.1",
#   "pydantic==2.12.5",
#   "send2trash==1.8.3",
# ]
# ///
"""Typed desktop bridge to the existing Pandoc and Ankdown pipeline."""

from __future__ import annotations

import hashlib
import os
import sqlite3
import subprocess
import sys
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Annotated, Literal

import ankdown.cli
import cyclopts
from filelock import FileLock
from platformdirs import user_cache_path
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter
from send2trash import send2trash

EXPORTER = Path(ankdown.cli.__file__).parent
PAIR_FILTER = Path(__file__).with_name("paired-cards.lua")
REVISION = "5878dff3082334d33609b0999eb849d8c6db6812"
type MacroDefinition = str | list[str | int]


class Input(BaseModel):
    model_config = ConfigDict(extra="forbid")
    workspace: str


class ListInput(Input):
    action: Literal["list"]


class DeckInput(Input):
    path: str


class LoadInput(DeckInput):
    action: Literal["load"]


class SaveInput(DeckInput):
    action: Literal["save"]
    source: str
    expected: str


class GenerateInput(DeckInput):
    action: Literal["generate"]


class ReviewInput(Input):
    action: Literal["review"]


class Change(BaseModel):
    path: str
    source: str | None
    expected: str | None


class OrganizeInput(Input):
    action: Literal["organize"]
    changes: list[Change] = Field(min_length=1)


class ChangedDeck(BaseModel):
    path: str
    hash: str | None


class Organized(BaseModel):
    changed: list[ChangedDeck]


type Request = Annotated[
    ListInput | LoadInput | SaveInput | GenerateInput | OrganizeInput | ReviewInput,
    Field(discriminator="action"),
]


class Card(BaseModel):
    front: str
    back: str
    tags: list[str] = Field(default_factory=list)


class Metadata(BaseModel):
    title: str
    model: str
    tags: list[str] = Field(default_factory=list)


class RenderedDeck(BaseModel):
    meta: Metadata
    cards: list[Card]
    media: list[str] = Field(default_factory=list)


class BuildRecord(BaseModel):
    inputs: dict[str, str]
    package: str
    source: str


type Status = Literal["Up to date", "Unsynced", "Empty"]


class Sync(BaseModel):
    """Package state, the reasons it is unsynced, and the deck source it was built from."""

    status: Status
    reasons: list[str]
    built: str | None


class Summary(BaseModel):
    path: str
    status: Status
    reasons: list[str]


class Pending(Summary):
    source: str
    built: str | None


class Review(BaseModel):
    decks: list[Pending]


class Workspace(BaseModel):
    root: str
    decks: list[Summary]
    macros: dict[str, MacroDefinition]


class Document(BaseModel):
    source: str
    hash: str
    cards: int
    status: Status
    reasons: list[str]
    built: str | None
    package: str


class Generated(BaseModel):
    status: Status
    package: str
    log: str


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def workspace_path(value: str) -> Path:
    root = Path(value).expanduser().resolve(strict=True)
    if not (root / "decks").is_dir():
        raise ValueError("Select a workspace that contains a decks folder.")
    return root


def deck_path(root: Path, value: str) -> Path:
    path = (root / "decks" / value).resolve(strict=True)
    if not path.is_relative_to(root / "decks") or path.suffix != ".md":
        raise ValueError("The deck must be a Markdown file inside the decks folder.")
    return path


def package_path(root: Path, path: Path) -> Path:
    name = "__".join(path.relative_to(root / "decks").with_suffix("").parts)
    output = root / "apkg" / (name + ".apkg")
    if not output.resolve().is_relative_to(root):
        raise ValueError("The package destination must stay inside the workspace.")
    return output


@contextmanager
def database() -> Iterator[sqlite3.Connection]:
    cache = user_cache_path("math-flashcards")
    cache.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(cache / "builds.sqlite3") as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS deck_builds (path TEXT PRIMARY KEY, record TEXT NOT NULL)"
        )
        yield connection


def input_hashes(path: Path, media: list[Path]) -> dict[str, str]:
    files = [
        path,
        PAIR_FILTER,
        *media,
        *(
            EXPORTER / name
            for name in (
                "ankdown.lua",
                "cli.py",
                "mathjax.html",
                "mathjax-macros.json",
                "card.css",
            )
        ),
    ]
    hashes = {str(file): digest(file.read_bytes()) for file in files}
    hashes["exporter"] = REVISION
    hashes["pandoc"] = digest(
        subprocess.run(["pandoc", "--version"], check=True, capture_output=True).stdout
    )
    return hashes


def has_cards(path: Path) -> bool:
    # A card side is a `.front` or `.back` div, so a deck without either class
    # has no cards; a lone side goes to the exporter, which rejects it. Listing
    # runs this per deck, so it reads text instead of running Pandoc.
    source = path.read_text(encoding="utf-8")
    return ".front" in source or ".back" in source


EMPTY = "The deck has no cards, so it has no Anki package."


def sync(path: Path, output: Path) -> Sync:
    with database() as connection:
        row = connection.execute(
            "SELECT record FROM deck_builds WHERE path = ?", (str(path),)
        ).fetchone()
    if row is None:
        if not has_cards(path):
            return Sync(status="Empty", reasons=[EMPTY], built=None)
        return Sync(
            status="Unsynced",
            reasons=["No Anki package has been generated from this deck."],
            built=None,
        )
    record = BuildRecord.model_validate_json(row[0])
    reasons: list[str] = []
    if not output.is_file():
        reasons.append("The Anki package file is missing.")
    elif digest(output.read_bytes()) != record.package:
        reasons.append("The Anki package file changed after generation.")
    current = input_hashes(path, [])
    for name, expected in record.inputs.items():
        if name in current:
            if current[name] == expected:
                continue
            reason = (
                "The deck changed." if name == str(path) else "The exporter changed."
            )
        else:
            file = Path(name)
            if file.is_file() and digest(file.read_bytes()) == expected:
                continue
            reason = "Media changed: " + file.name
        if reason not in reasons:
            reasons.append(reason)
    if "The deck changed." in reasons and not has_cards(path):
        reasons.append("The deck has no cards. An update removes its Anki package.")
    return Sync(
        status="Unsynced" if reasons else "Up to date",
        reasons=reasons,
        built=record.source,
    )


@contextmanager
def render(path: Path, source: str, scratch: Path) -> Iterator[RenderedDeck]:
    # Pandoc owns card parsing: https://pandoc.org/lua-filters.html
    # Keeping the input beside its deck preserves the exporter's image resolution.
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".tmp",
        prefix=".flashcards-",
        dir=path.parent,
        encoding="utf-8",
    ) as temporary:
        temporary.write(source)
        temporary.flush()
        process = subprocess.run(
            [
                "pandoc",
                "-f",
                "markdown",
                "--lua-filter",
                str(PAIR_FILTER),
                "--lua-filter",
                str(EXPORTER / "ankdown.lua"),
                temporary.name,
                "-t",
                "plain",
            ],
            cwd=scratch,
            env=os.environ | {"PWD": str(scratch)},
            capture_output=True,
            text=True,
            check=True,
        )
        if process.stderr:
            print(process.stderr, file=sys.stderr, end="")
        yield RenderedDeck.model_validate_json(process.stdout)


def media_paths(deck: RenderedDeck, root: Path, scratch: Path) -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for entry in deck.media:
        source, name = entry.split(":", 1)
        path = Path(source).resolve(strict=True)
        if not path.is_relative_to(root) and not path.is_relative_to(scratch):
            raise ValueError("Referenced media must stay inside the workspace.")
        mapping[name] = path
    return mapping


def validate(root: Path, path: Path, source: str) -> int:
    """Render a deck through the exporter's filters, check its media, and count its cards."""
    with tempfile.TemporaryDirectory(prefix="flashcards-check-") as directory:
        scratch = Path(directory)
        with render(path, source, scratch) as deck:
            media_paths(deck, root, scratch)
            return len(deck.cards)


def remove_package(root: Path, path: Path) -> None:
    package = package_path(root, path)
    if package.is_file():
        send2trash(package)
    with database() as connection:
        connection.execute("DELETE FROM deck_builds WHERE path = ?", (str(path),))


def generate(root: Path, path: Path) -> Generated:
    output = package_path(root, path)
    if not has_cards(path):
        remove_package(root, path)
        return Generated(status="Empty", package=str(output), log=EMPTY)
    output.parent.mkdir(parents=True, exist_ok=True)
    cache = user_cache_path("math-flashcards")
    cache.mkdir(parents=True, exist_ok=True)
    with FileLock(cache / (digest(str(path).encode()) + ".lock")):
        source = path.read_bytes().decode("utf-8")
        with tempfile.TemporaryDirectory(
            prefix=".flashcards-build-", dir=output.parent
        ) as directory:
            scratch = Path(directory)
            with render(path, source, scratch) as deck:
                media = [
                    file
                    for file in media_paths(deck, root, scratch).values()
                    if not file.is_relative_to(scratch)
                ]
                inputs = input_hashes(path, media)
                if inputs[str(path)] != digest(source.encode()):
                    raise ValueError(
                        "The deck changed before generation. Generate it again."
                    )
                temporary = scratch / output.name
                process = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "ankdown.cli",
                        "compile",
                        "--output",
                        str(temporary),
                    ],
                    input=deck.model_dump_json(),
                    cwd=scratch,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                record = BuildRecord(
                    inputs=inputs,
                    package=digest(temporary.read_bytes()),
                    source=source,
                )
                temporary.replace(output)
                with database() as connection:
                    connection.execute(
                        "INSERT OR REPLACE INTO deck_builds VALUES (?, ?)",
                        (str(path), record.model_dump_json()),
                    )
                return Generated(
                    status=sync(path, output).status,
                    package=str(output),
                    log=process.stdout + process.stderr,
                )


def publish_changes(root: Path, changes: list[Change]) -> Organized:
    cache = user_cache_path("math-flashcards")
    cache.mkdir(parents=True, exist_ok=True)
    with FileLock(cache / (digest(str(root).encode()) + ".workspace.lock")):
        paths = [(root / "decks" / change.path).resolve() for change in changes]
        if len(set(paths)) != len(paths):
            raise ValueError("Each deck can change only once in an operation.")
        originals: dict[Path, bytes | None] = {}
        for change, path in zip(changes, paths, strict=True):
            if not path.is_relative_to(root / "decks") or path.suffix != ".md":
                raise ValueError(
                    "The deck must stay inside the workspace decks folder."
                )
            original = path.read_bytes() if path.is_file() else None
            actual = digest(original) if original is not None else None
            if actual != change.expected:
                raise ValueError("A deck changed on disk. Reload it before organizing.")
            if change.source is None and original is None:
                raise ValueError("The deck to absorb is missing.")
            if change.source is not None:
                path.parent.mkdir(parents=True, exist_ok=True)
                validate(root, path, change.source)
            originals[path] = original
        # Stage every file before publishing; restore published files on failure.
        # tempfile + atomic replace: https://docs.python.org/3/library/tempfile.html
        with tempfile.TemporaryDirectory(
            prefix=".flashcards-organize-", dir=root
        ) as directory:
            scratch = Path(directory)
            staged: dict[Path, Path] = {}
            backups: dict[Path, Path] = {}
            for index, (change, path) in enumerate(zip(changes, paths, strict=True)):
                original = originals[path]
                if original is not None:
                    backup = scratch / f"{index}.original"
                    backup.write_bytes(original)
                    backups[path] = backup
                if change.source is not None:
                    temporary = scratch / f"{index}.updated"
                    with temporary.open("w", encoding="utf-8") as handle:
                        handle.write(change.source)
                        handle.flush()
                        os.fsync(handle.fileno())
                    staged[path] = temporary
            for change, path in zip(changes, paths, strict=True):
                actual = digest(path.read_bytes()) if path.is_file() else None
                if actual != change.expected:
                    raise ValueError("A deck changed during organization. Reload it.")
            published: list[Path] = []
            try:
                # Destinations precede sources; a process interruption retains card content.
                for change, path in zip(changes, paths, strict=True):
                    path.parent.mkdir(parents=True, exist_ok=True)
                    if change.source is None:
                        send2trash(path)
                    else:
                        staged[path].replace(path)
                    published.append(path)
            except OSError:
                for path in reversed(published):
                    if path in backups:
                        backups[path].replace(path)
                    else:
                        send2trash(path)
                raise
        # A removed deck's package and build record describe a deck that no longer exists.
        for change, path in zip(changes, paths, strict=True):
            if change.source is None:
                remove_package(root, path)
        return Organized(
            changed=[
                ChangedDeck(
                    path=change.path,
                    hash=digest(change.source.encode())
                    if change.source is not None
                    else None,
                )
                for change in changes
            ]
        )


def dispatch(
    request: Request,
) -> Workspace | Document | Generated | Organized | Review:
    root = workspace_path(request.workspace)
    if isinstance(request, OrganizeInput):
        return publish_changes(root, request.changes)
    paths = [
        path
        for path in sorted((root / "decks").rglob("*.md"))
        if path.resolve().is_relative_to(root / "decks")
    ]
    if isinstance(request, ReviewInput):
        pending: list[Pending] = []
        for path in paths:
            state = sync(path, package_path(root, path))
            if state.status == "Unsynced":
                pending.append(
                    Pending(
                        path=str(path.relative_to(root / "decks")),
                        status=state.status,
                        reasons=state.reasons,
                        source=path.read_text(encoding="utf-8"),
                        built=state.built,
                    )
                )
        return Review(decks=pending)
    if isinstance(request, ListInput):
        summaries: list[Summary] = []
        for path in paths:
            state = sync(path, package_path(root, path))
            summaries.append(
                Summary(
                    path=str(path.relative_to(root / "decks")),
                    status=state.status,
                    reasons=state.reasons,
                )
            )
        return Workspace(
            root=str(root),
            decks=summaries,
            macros=TypeAdapter(dict[str, MacroDefinition]).validate_json(
                (EXPORTER / "mathjax-macros.json").read_text()
            ),
        )
    path = deck_path(root, request.path)
    output = package_path(root, path)
    match request:
        case GenerateInput():
            return generate(root, path)
        case SaveInput():
            publish_changes(
                root,
                [
                    Change(
                        path=request.path,
                        source=request.source,
                        expected=request.expected,
                    )
                ],
            )
    source = path.read_bytes().decode("utf-8")
    state = sync(path, output)
    return Document(
        source=source,
        hash=digest(source.encode()),
        cards=validate(root, path, source),
        status=state.status,
        reasons=state.reasons,
        built=state.built,
        package=str(output),
    )


app = cyclopts.App()


@app.command
def build(workspace: Path) -> None:
    """Generate every paired-card deck in a workspace."""
    root = workspace_path(str(workspace))
    for path in sorted((root / "decks").rglob("*.md")):
        result = generate(root, deck_path(root, str(path.relative_to(root / "decks"))))
        print(result.package)


@app.default
def main() -> None:
    """Read one typed request from stdin and write its result as JSON."""
    request = TypeAdapter(Request).validate_json(sys.stdin.readline())
    try:
        result = dispatch(request)
    except subprocess.CalledProcessError as error:
        print(error.stderr, file=sys.stderr)
        sys.exit(error.returncode)
    except (ValueError, FileNotFoundError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
    print(result.model_dump_json())


if __name__ == "__main__":
    app()
