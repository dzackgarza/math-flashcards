# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "ankdown @ git+https://github.com/dzackgarza/ankdown-for-math@5878dff3082334d33609b0999eb849d8c6db6812",
#   "beautifulsoup4==4.14.3",
#   "cyclopts==4.15.0",
#   "filelock==3.20.3",
#   "platformdirs==4.5.1",
#   "pydantic==2.12.5",
# ]
# ///
"""Typed desktop bridge to the existing Pandoc and Ankdown pipeline."""

from __future__ import annotations

import base64
import hashlib
import mimetypes
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
from bs4 import BeautifulSoup
from filelock import FileLock
from platformdirs import user_cache_path
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter

EXPORTER = Path(ankdown.cli.__file__).parent
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


class PreviewInput(DeckInput):
    action: Literal["preview"]
    source: str


class SaveInput(DeckInput):
    action: Literal["save"]
    source: str
    expected: str


class GenerateInput(DeckInput):
    action: Literal["generate"]


type Request = Annotated[
    ListInput | LoadInput | PreviewInput | SaveInput | GenerateInput,
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


class Preview(BaseModel):
    title: str
    cards: list[Card]
    macros: dict[str, MacroDefinition]
    css: str


class BuildRecord(BaseModel):
    inputs: dict[str, str]
    package: str


class Summary(BaseModel):
    path: str
    status: Literal["Up to date", "Unsynced"]


class Workspace(BaseModel):
    decks: list[Summary]


class Document(BaseModel):
    source: str
    hash: str
    status: Literal["Up to date", "Unsynced"]
    package: str


class Generated(BaseModel):
    status: Literal["Up to date", "Unsynced"]
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
            "CREATE TABLE IF NOT EXISTS builds (path TEXT PRIMARY KEY, record TEXT NOT NULL)"
        )
        yield connection


def input_hashes(path: Path, media: list[Path]) -> dict[str, str]:
    files = [
        path,
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


def status(path: Path, output: Path) -> Literal["Up to date", "Unsynced"]:
    with database() as connection:
        row = connection.execute(
            "SELECT record FROM builds WHERE path = ?", (str(path),)
        ).fetchone()
    if row is None or not output.is_file():
        return "Unsynced"
    record = BuildRecord.model_validate_json(row[0])
    for name, expected in record.inputs.items():
        if name in ("exporter", "pandoc"):
            continue
        file = Path(name)
        if not file.is_file() or digest(file.read_bytes()) != expected:
            return "Unsynced"
    current = input_hashes(path, [])
    if any(record.inputs.get(key) != value for key, value in current.items()):
        return "Unsynced"
    if digest(output.read_bytes()) != record.package:
        return "Unsynced"
    return "Up to date"


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


def preview(root: Path, path: Path, source: str) -> Preview:
    with tempfile.TemporaryDirectory(prefix="flashcards-preview-") as directory:
        scratch = Path(directory)
        with render(path, source, scratch) as deck:
            mapping = media_paths(deck, root, scratch)
            for card in deck.cards:
                for field in ("front", "back"):
                    soup = BeautifulSoup(getattr(card, field), "html.parser")
                    for image in soup.find_all("img"):
                        name = str(image["src"])
                        if name in mapping:
                            image_path = mapping[name]
                            mime = mimetypes.guess_type(image_path.name)[0]
                            if mime is None:
                                raise ValueError(
                                    f"Unknown image type: {image_path.name}"
                                )
                            image["src"] = (
                                f"data:{mime};base64,"
                                + base64.b64encode(image_path.read_bytes()).decode()
                            )
                    setattr(card, field, str(soup))
            macros = TypeAdapter(dict[str, MacroDefinition]).validate_json(
                (EXPORTER / "mathjax-macros.json").read_text()
            )
            return Preview(
                title=deck.meta.title,
                cards=deck.cards,
                macros=macros,
                css=(EXPORTER / "card.css").read_text(),
            )


def generate(root: Path, path: Path) -> Generated:
    output = package_path(root, path)
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
                    inputs=inputs, package=digest(temporary.read_bytes())
                )
                temporary.replace(output)
                with database() as connection:
                    connection.execute(
                        "INSERT OR REPLACE INTO builds VALUES (?, ?)",
                        (str(path), record.model_dump_json()),
                    )
                return Generated(
                    status=status(path, output),
                    package=str(output),
                    log=process.stdout + process.stderr,
                )


def dispatch(request: Request) -> Workspace | Document | Preview | Generated:
    root = workspace_path(request.workspace)
    if isinstance(request, ListInput):
        return Workspace(
            decks=[
                Summary(
                    path=str(path.relative_to(root / "decks")),
                    status=status(path, package_path(root, path)),
                )
                for path in sorted((root / "decks").rglob("*.md"))
                if path.resolve().is_relative_to(root / "decks")
            ]
        )
    path = deck_path(root, request.path)
    output = package_path(root, path)
    match request:
        case PreviewInput():
            return preview(root, path, request.source)
        case GenerateInput():
            return generate(root, path)
        case SaveInput():
            if digest(path.read_bytes()) != request.expected:
                raise ValueError("This deck changed on disk. Reload it before saving.")
            # tempfile + atomic replace: https://docs.python.org/3/library/tempfile.html
            with tempfile.NamedTemporaryFile(
                mode="w",
                dir=path.parent,
                prefix=".flashcards-save-",
                encoding="utf-8",
                delete=False,
            ) as temporary:
                temporary.write(request.source)
                temporary.flush()
                os.fsync(temporary.fileno())
            Path(temporary.name).replace(path)
        case LoadInput():
            pass
    source = path.read_bytes().decode("utf-8")
    return Document(
        source=source,
        hash=digest(source.encode()),
        status=status(path, output),
        package=str(output),
    )


app = cyclopts.App()


@app.default
def main() -> None:
    """Read one typed request from stdin and write its result as JSON."""
    request = TypeAdapter(Request).validate_json(sys.stdin.readline())
    try:
        result = dispatch(request)
    except subprocess.CalledProcessError as error:
        print(error.stderr, file=sys.stderr)
        raise
    print(result.model_dump_json())


if __name__ == "__main__":
    app()
