# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "ankdown @ git+https://github.com/dzackgarza/ankdown-for-math",
#   "cyclopts",
#   "filelock",
#   "platformdirs",
#   "pydantic",
#   "send2trash",
# ]
# ///
"""Typed desktop bridge to the existing Pandoc and Ankdown pipeline."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
from collections.abc import Iterator
from contextlib import closing, contextmanager
from datetime import UTC, datetime
from functools import cache
from pathlib import Path
from typing import Annotated, Literal
from xml.etree import ElementTree

try:
    import ankdown
    from filelock import FileLock, Timeout
    from platformdirs import user_cache_path
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        TypeAdapter,
        ValidationError,
        field_validator,
        model_validator,
    )
    from send2trash import send2trash
except ModuleNotFoundError as error:
    raise SystemExit(
        f"The installed Python runtime is incomplete. Run just desktop-install. {error}"
    ) from error

EXPORTER = Path(ankdown.__file__).parent
PAIR_FILTER = Path(__file__).with_name("paired-cards.lua")
TIKZ_ASSETS = Path(__file__).with_name("tikz-assets")
TIKZ_ENVIRONMENT = re.compile(
    r"\\begin\{tikzcd\}(?:\[[^\n]*\])?[\s\S]*?\\end\{tikzcd\}"
)
type MacroDefinition = str | tuple[str, int] | tuple[str, int, str]
type Digest = Annotated[str, Field(pattern=r"^[a-f0-9]{64}$")]


class AssetsInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    action: Literal["assets"]


class AssetVersionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    action: Literal["asset-version"]


class Input(BaseModel):
    model_config = ConfigDict(extra="forbid")
    workspace: str


class ListInput(Input):
    action: Literal["list"]


class DiscoveryInput(Input):
    generation: int = Field(ge=0, strict=True)


class ManifestInput(DiscoveryInput):
    action: Literal["manifest"]


class ManifestCacheInput(DiscoveryInput):
    action: Literal["cached-manifest", "cache-manifest"]


class BatchInput(DiscoveryInput):
    paths: list[str] = Field(min_length=1, max_length=8)

    @field_validator("paths")
    @classmethod
    def relative_decks(cls, values: list[str]) -> list[str]:
        for value in values:
            parts = value.split("/")
            if (
                not value.endswith(".md")
                or "\\" in value
                or parts[0] == "apkg"
                or any(part in ("", ".", "..") for part in parts)
            ):
                raise ValueError("Use a relative Markdown deck path outside apkg/.")
        return values


class SourcesInput(BatchInput):
    action: Literal["sources"]


class ChecksInput(BatchInput):
    action: Literal["checks"]
    assets: Digest


class CachedChecksInput(BatchInput):
    action: Literal["cached-checks"]
    assets: Digest


class Problem(BaseModel):
    path: str
    card: str | None
    label: str | None
    side: Literal["front", "back"] | None
    kind: Literal["LaTeX", "Card structure", "Empty answer"]
    message: str
    source: str | None


class ProblemKey(BaseModel):
    model_config = ConfigDict(extra="forbid")
    path: str
    revision: Digest

    @field_validator("path")
    @classmethod
    def relative_path(cls, value: str) -> str:
        return BatchInput.relative_decks([value])[0]


class ProblemEntry(ProblemKey):
    problems: list[Problem]

    @model_validator(mode="after")
    def matching_paths(self) -> ProblemEntry:
        if any(problem.path != self.path for problem in self.problems):
            raise ValueError("Each problem must belong to its deck.")
        return self


class ProblemCacheInput(DiscoveryInput):
    producer: Digest
    assets: Digest


class ReadProblemsInput(ProblemCacheInput):
    action: Literal["problems"]
    entries: list[ProblemKey] = Field(min_length=1, max_length=8)


class StoreProblemsInput(ProblemCacheInput):
    action: Literal["store-problems"]
    entries: list[ProblemEntry] = Field(min_length=1, max_length=8)


class RebuildCacheInput(DiscoveryInput):
    action: Literal["rebuild-cache"]


class SearchCard(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str = Field(min_length=1)
    label: str
    front: str
    back: str
    tags: str


class SearchKey(BaseModel):
    model_config = ConfigDict(extra="forbid")
    path: str
    revision: Digest

    @field_validator("path")
    @classmethod
    def relative_path(cls, value: str) -> str:
        return BatchInput.relative_decks([value])[0]


class SearchEntry(SearchKey):
    cards: list[SearchCard]

    @field_validator("cards")
    @classmethod
    def distinct_cards(cls, cards: list[SearchCard]) -> list[SearchCard]:
        if len({card.id for card in cards}) != len(cards):
            raise ValueError("Search cards must have distinct IDs within a deck.")
        return cards


class ReadSearchInput(DiscoveryInput):
    action: Literal["search"]
    producer: Digest
    entries: list[SearchKey] = Field(min_length=1, max_length=8)


class StoreSearchInput(DiscoveryInput):
    action: Literal["store-search"]
    producer: Digest
    entries: list[SearchEntry] = Field(min_length=1, max_length=8)


class DeckInput(Input):
    path: str


class LoadInput(DeckInput):
    action: Literal["load", "validate"]
    generation: int = Field(ge=0, strict=True)


class SaveInput(DeckInput):
    action: Literal["save"]
    source: str
    expected: Digest
    generation: int = Field(ge=0, strict=True)


class GenerateInput(DeckInput):
    action: Literal["generate"]
    assets: Digest


class DiagramPreviewInput(DeckInput):
    action: Literal["render-diagram"]
    source: str = Field(min_length=27, max_length=100_000)


class ReviewInput(Input):
    action: Literal["review"]
    assets: Digest


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
    AssetsInput
    | AssetVersionInput
    | ListInput
    | LoadInput
    | SaveInput
    | GenerateInput
    | DiagramPreviewInput
    | OrganizeInput
    | ReviewInput
    | ManifestInput
    | ManifestCacheInput
    | SourcesInput
    | ChecksInput
    | CachedChecksInput
    | ReadProblemsInput
    | StoreProblemsInput
    | ReadSearchInput
    | StoreSearchInput
    | RebuildCacheInput,
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


class RenderedDiagram(BaseModel):
    path: str
    source: str
    svg: str


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


class Verification(Sync):
    input_identity: Digest
    checked_at: datetime
    dependencies: list[str]

    @field_validator("dependencies")
    @classmethod
    def absolute_dependencies(cls, values: list[str]) -> list[str]:
        if values != sorted(set(values)) or any(
            not Path(value).is_absolute() for value in values
        ):
            raise ValueError(
                "Package dependencies must be distinct absolute paths in sorted order."
            )
        return values


class Session(BaseModel):
    root: str
    generation: int = Field(ge=0, strict=True)


class Entry(BaseModel):
    path: str


class Manifest(BaseModel):
    session: Session
    entries: list[Entry]


class ManifestRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")
    entries: list[Entry]

    @model_validator(mode="after")
    def valid_membership(self) -> ManifestRecord:
        paths = BatchInput.relative_decks([entry.path for entry in self.entries])
        if paths != sorted(set(paths)):
            raise ValueError(
                "Saved navigation has invalid ordering or duplicate decks."
            )
        return self


class CachedManifest(Manifest):
    state: Literal["cached"] = "cached"


class MissingManifest(BaseModel):
    session: Session
    state: Literal["pending"] = "pending"


class FailedManifest(BaseModel):
    session: Session
    state: Literal["failed"] = "failed"
    kind: Literal["CacheFailure"] = "CacheFailure"
    message: str


type ManifestCache = Annotated[
    CachedManifest | MissingManifest | FailedManifest, Field(discriminator="state")
]


class AssetSet(BaseModel):
    identity: Digest
    macros: dict[str, MacroDefinition]
    stmaryrd: str = Field(min_length=1)
    renderer: str = Field(min_length=1)

    @model_validator(mode="after")
    def verify_identity(self) -> AssetSet:
        if self.identity != asset_identity(self.macros, self.stmaryrd, self.renderer):
            raise ValueError(
                "The installed renderer assets are damaged. Run just desktop-install."
            )
        return self


class InvalidAssetsError(ValueError):
    """The requested installed renderer set cannot be used."""


class InstallationError(ValueError):
    """A prepared runtime component cannot be used."""


class AssetVersion(BaseModel):
    identity: Digest


class MathJaxPackage(BaseModel):
    version: str


class SourceResult(BaseModel):
    state: Literal["ready"] = "ready"
    path: str
    source: str
    revision: Digest


class PathFailure(BaseModel):
    state: Literal["failed"] = "failed"
    path: str
    kind: Literal[
        "UnreadablePath",
        "InvalidDeck",
        "InvalidAssets",
        "BackendFailure",
        "CacheFailure",
    ]
    message: str


class Sources(BaseModel):
    session: Session
    results: list[Annotated[SourceResult | PathFailure, Field(discriminator="state")]]


class PackageResult(Verification):
    state: Literal["ready"] = "ready"
    path: str
    revision: Digest
    assets: Digest


class Checks(BaseModel):
    session: Session
    results: list[Annotated[PackageResult | PathFailure, Field(discriminator="state")]]
    cache_errors: list[PathFailure] = Field(default_factory=list)


class PendingPackage(BaseModel):
    state: Literal["pending"] = "pending"
    path: str
    previous: PackageResult | None


class FailedPackage(PathFailure):
    previous: PackageResult | None = None


class CachedChecks(BaseModel):
    session: Session
    results: list[
        Annotated[PendingPackage | FailedPackage, Field(discriminator="state")]
    ]


class CachedProblems(ProblemEntry):
    state: Literal["ready"] = "ready"
    producer: Digest
    assets: Digest


class PendingProblems(BaseModel):
    state: Literal["pending", "superseded"] = "pending"
    path: str


class StoredProblems(BaseModel):
    state: Literal["stored", "superseded"]
    path: str


class ProblemCache(BaseModel):
    session: Session
    results: list[
        Annotated[
            CachedProblems | PendingProblems | PathFailure, Field(discriminator="state")
        ]
    ]


class ProblemStored(BaseModel):
    session: Session
    results: list[Annotated[StoredProblems | PathFailure, Field(discriminator="state")]]


class CacheRebuilt(BaseModel):
    session: Session
    rebuilt: Literal[True] = True


class CachedSearch(SearchEntry):
    state: Literal["ready"] = "ready"
    source: str
    producer: Digest

    @model_validator(mode="after")
    def source_identity(self) -> CachedSearch:
        if digest(self.source.encode()) != self.revision:
            raise ValueError("The saved search source does not match its revision.")
        return self


class PendingSearch(BaseModel):
    state: Literal["pending", "superseded"]
    path: str


class SearchCache(BaseModel):
    session: Session
    results: list[
        Annotated[
            CachedSearch | PendingSearch | PathFailure, Field(discriminator="state")
        ]
    ]


class Summary(BaseModel):
    path: str
    status: Status
    reasons: list[str]
    source: str


class Pending(Summary):
    built: str | None


class Review(BaseModel):
    decks: list[Pending]


class Workspace(BaseModel):
    root: str
    decks: list[Summary]
    macros: dict[str, MacroDefinition]
    # The script that defines registerStmaryrd, MathJax's TeX package for
    # stmaryrd's \llbracket and \rrbracket.
    stmaryrd: str


class Document(BaseModel):
    session: Session
    path: str
    source: str
    hash: Digest
    cards: int | None
    status: Status | None
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
    if not root.is_dir():
        raise ValueError("Select the folder containing your Markdown decks.")
    return root


def deck_path(root: Path, value: str) -> Path:
    candidate = root / value
    path = candidate.resolve()
    if (
        not path.is_relative_to(root)
        or candidate.is_relative_to(root / "apkg")
        or path.is_relative_to(root / "apkg")
        or path.suffix != ".md"
    ):
        raise ValueError(
            "A deck must be a Markdown file in the workspace, outside apkg/."
        )
    return path


def deck_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    # Path.walk supports pruning generated output before descending into it.
    # https://docs.python.org/3/library/pathlib.html#pathlib.Path.walk
    for directory, folders, files in root.walk():
        if directory == root:
            folders[:] = [name for name in folders if name != "apkg"]
        for name in files:
            path = directory / name
            resolved = path.resolve()
            if (
                path.suffix == ".md"
                and resolved.is_relative_to(root)
                and not resolved.is_relative_to(root / "apkg")
            ):
                paths.append(path)
    return sorted(paths)


def package_path(root: Path, path: Path) -> Path:
    name = "__".join(path.relative_to(root).with_suffix("").parts)
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
        connection.execute(
            "CREATE TABLE IF NOT EXISTS macros (id INTEGER PRIMARY KEY CHECK (id = 0), digest TEXT NOT NULL)"
        )
        yield connection


def refresh_macros() -> tuple[str, str]:
    """Fetch both renderer inputs during software maintenance."""
    from ankdown.cli import fetch_macros, fetch_stmaryrd

    macros = fetch_macros()
    stmaryrd = fetch_stmaryrd()
    return macros, stmaryrd


@contextmanager
def derived_database() -> Iterator[sqlite3.Connection]:
    """Disposable records use a separate SQLite file from build provenance."""
    directory = user_cache_path("math-flashcards")
    directory.mkdir(parents=True, exist_ok=True)
    with (
        FileLock(directory / "derived.lock", timeout=0.1),
        closing(
            sqlite3.connect(directory / "derived.sqlite3", timeout=0.1)
        ) as connection,
        connection,
    ):
        connection.execute(
            "CREATE TABLE IF NOT EXISTS problem_checks ("
            "root TEXT NOT NULL, path TEXT NOT NULL, revision TEXT NOT NULL, "
            "producer TEXT NOT NULL, assets TEXT NOT NULL, record TEXT NOT NULL, "
            "PRIMARY KEY (root, path))"
        )
        connection.execute(
            "CREATE TABLE IF NOT EXISTS manifests (root TEXT PRIMARY KEY, producer TEXT NOT NULL, record TEXT NOT NULL)"
        )
        connection.execute(
            "CREATE TABLE IF NOT EXISTS search_summaries (root TEXT NOT NULL, path TEXT NOT NULL, revision TEXT NOT NULL, producer TEXT NOT NULL, record TEXT NOT NULL, PRIMARY KEY (root, path))"
        )
        connection.execute(
            "CREATE TABLE IF NOT EXISTS package_checks (root TEXT NOT NULL, path TEXT NOT NULL, producer TEXT NOT NULL, record TEXT NOT NULL, PRIMARY KEY (root, path))"
        )
        yield connection


@cache
def package_producer() -> str:
    return digest(
        Path(__file__).read_bytes()
        + json.dumps(PackageResult.model_json_schema(), sort_keys=True).encode()
    )


def package_history(root: Path, request: CachedChecksInput) -> CachedChecks:
    for path in request.paths:
        deck_path(root, path)
    results: list[PendingPackage | FailedPackage] = []
    for path in request.paths:
        try:
            asset_set(request.assets)
            with derived_database() as connection:
                row = connection.execute(
                    "SELECT record FROM package_checks WHERE root = ? AND path = ? AND producer = ?",
                    (str(root), path, package_producer()),
                ).fetchone()
            previous = PackageResult.model_validate_json(row[0]) if row else None
            if previous is not None and previous.path != path:
                raise ValueError(
                    "The saved package identity is damaged. Rebuild cached data."
                )
            results.append(PendingPackage(path=path, previous=previous))
        except InvalidAssetsError as error:
            results.append(
                FailedPackage(path=path, kind="InvalidAssets", message=str(error))
            )
        except (sqlite3.Error, ValidationError, OSError, Timeout, ValueError) as error:
            results.append(
                FailedPackage(
                    path=path,
                    kind="CacheFailure",
                    message="Saved package checks are damaged. Rebuild cached data."
                    if isinstance(error, ValidationError)
                    else str(error),
                )
            )
    return CachedChecks(
        session=Session(root=str(root), generation=request.generation), results=results
    )


def store_package_check(root: Path, result: PackageResult) -> None:
    with derived_database() as connection:
        connection.execute(
            "INSERT OR REPLACE INTO package_checks VALUES (?, ?, ?, ?)",
            (str(root), result.path, package_producer(), result.model_dump_json()),
        )


def search_cache(
    root: Path, request: ReadSearchInput | StoreSearchInput
) -> SearchCache:
    producer_key = digest(
        (
            request.producer
            + json.dumps(CachedSearch.model_json_schema(), sort_keys=True)
        ).encode()
    )
    paths = [deck_path(root, entry.path) for entry in request.entries]
    results: list[CachedSearch | PendingSearch | PathFailure] = []
    for entry, path in zip(request.entries, paths, strict=True):
        try:
            raw = path.read_bytes()
            source = raw.decode("utf-8")
        except (OSError, UnicodeError) as error:
            results.append(
                PathFailure(path=entry.path, kind="UnreadablePath", message=str(error))
            )
            continue
        if digest(raw) != entry.revision:
            results.append(PendingSearch(path=entry.path, state="superseded"))
            continue
        try:
            if isinstance(entry, SearchEntry):
                record = CachedSearch(
                    path=entry.path,
                    revision=entry.revision,
                    source=source,
                    producer=request.producer,
                    cards=entry.cards,
                )
                with derived_database() as connection:
                    connection.execute(
                        "INSERT OR REPLACE INTO search_summaries VALUES (?, ?, ?, ?, ?)",
                        (
                            str(root),
                            entry.path,
                            entry.revision,
                            producer_key,
                            record.model_dump_json(),
                        ),
                    )
                results.append(record)
                continue
            with derived_database() as connection:
                row = connection.execute(
                    "SELECT record FROM search_summaries WHERE root = ? AND path = ? AND revision = ? AND producer = ?",
                    (str(root), entry.path, entry.revision, producer_key),
                ).fetchone()
            if row is None:
                results.append(PendingSearch(path=entry.path, state="pending"))
                continue
            record = CachedSearch.model_validate_json(row[0])
            if (
                record.path != entry.path
                or record.revision != entry.revision
                or record.producer != request.producer
            ):
                raise ValueError(
                    "The saved search identity is damaged. Rebuild cached data."
                )
            results.append(record)
        except (sqlite3.Error, ValidationError, OSError, Timeout, ValueError) as error:
            results.append(
                PathFailure(
                    path=entry.path,
                    kind="CacheFailure",
                    message="Saved search data is damaged. Rebuild cached data."
                    if isinstance(error, ValidationError)
                    else str(error),
                )
            )
    return SearchCache(
        session=Session(root=str(root), generation=request.generation), results=results
    )


def manifest_cache(root: Path, request: ManifestCacheInput) -> ManifestCache:
    session = Session(root=str(root), generation=request.generation)
    producer = digest(
        Path(__file__).read_bytes()
        + json.dumps(ManifestRecord.model_json_schema(), sort_keys=True).encode()
    )
    try:
        if request.action == "cache-manifest":
            record = ManifestRecord(
                entries=[
                    Entry(path=str(path.relative_to(root))) for path in deck_paths(root)
                ]
            )
            with derived_database() as connection:
                connection.execute(
                    "INSERT OR REPLACE INTO manifests VALUES (?, ?, ?)",
                    (str(root), producer, record.model_dump_json()),
                )
                members = {entry.path for entry in record.entries}
                for table in ("problem_checks", "search_summaries", "package_checks"):
                    previous = connection.execute(
                        f"SELECT path FROM {table} WHERE root = ?", (str(root),)
                    ).fetchall()
                    connection.executemany(
                        f"DELETE FROM {table} WHERE root = ? AND path = ?",
                        [
                            (str(root), path)
                            for (path,) in previous
                            if path not in members
                        ],
                    )
            return CachedManifest(session=session, entries=record.entries)
        with derived_database() as connection:
            row = connection.execute(
                "SELECT record FROM manifests WHERE root = ? AND producer = ?",
                (str(root), producer),
            ).fetchone()
        if row is None:
            return MissingManifest(session=session)
        record = ManifestRecord.model_validate_json(row[0])
        return CachedManifest(session=session, entries=record.entries)
    except (sqlite3.Error, ValidationError, OSError, Timeout) as error:
        return FailedManifest(
            session=session,
            message="Saved navigation is damaged. Rebuild cached data."
            if isinstance(error, ValidationError)
            else str(error),
        )


def problem_cache(
    root: Path, request: ReadProblemsInput | StoreProblemsInput
) -> ProblemCache | ProblemStored:
    producer_key = digest(
        (
            request.producer
            + json.dumps(CachedProblems.model_json_schema(), sort_keys=True)
        ).encode()
    )
    paths = [deck_path(root, entry.path) for entry in request.entries]
    read: list[CachedProblems | PendingProblems | PathFailure] = []
    stored: list[StoredProblems | PathFailure] = []
    for position, (entry, path) in enumerate(zip(request.entries, paths, strict=True)):
        try:
            revision = digest(path.read_bytes())
        except OSError as error:
            failure = PathFailure(
                path=entry.path, kind="UnreadablePath", message=str(error)
            )
            read.append(failure)
            stored.append(failure)
            continue
        if revision != entry.revision:
            read.append(PendingProblems(path=entry.path, state="superseded"))
            stored.append(StoredProblems(path=entry.path, state="superseded"))
            continue
        try:
            if isinstance(request, StoreProblemsInput):
                record = CachedProblems(
                    path=entry.path,
                    revision=entry.revision,
                    producer=request.producer,
                    assets=request.assets,
                    problems=request.entries[position].problems,
                )
                with derived_database() as connection:
                    connection.execute(
                        "INSERT OR REPLACE INTO problem_checks VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            str(root),
                            entry.path,
                            entry.revision,
                            producer_key,
                            request.assets,
                            record.model_dump_json(),
                        ),
                    )
                stored.append(StoredProblems(path=entry.path, state="stored"))
                continue
            with derived_database() as connection:
                row = connection.execute(
                    "SELECT record FROM problem_checks WHERE root = ? AND path = ? "
                    "AND revision = ? AND producer = ? AND assets = ?",
                    (
                        str(root),
                        entry.path,
                        entry.revision,
                        producer_key,
                        request.assets,
                    ),
                ).fetchone()
            if row is None:
                read.append(PendingProblems(path=entry.path))
                continue
            record = CachedProblems.model_validate_json(row[0])
            if (record.path, record.revision, record.producer, record.assets) != (
                entry.path,
                entry.revision,
                request.producer,
                request.assets,
            ):
                read.append(
                    PathFailure(
                        path=entry.path,
                        kind="CacheFailure",
                        message="The saved problem identity is damaged. Rebuild cached data.",
                    )
                )
                continue
            read.append(record)
        except (sqlite3.Error, ValidationError, OSError, Timeout) as error:
            failure = PathFailure(
                path=entry.path,
                kind="CacheFailure",
                message="Saved Problems data is damaged. Rebuild cached data."
                if isinstance(error, ValidationError)
                else str(error),
            )
            read.append(failure)
            stored.append(failure)
    session = Session(root=str(root), generation=request.generation)
    if isinstance(request, StoreProblemsInput):
        return ProblemStored(session=session, results=stored)
    return ProblemCache(session=session, results=read)


def asset_identity(
    macros: dict[str, MacroDefinition], stmaryrd: str, renderer: str
) -> str:
    return digest(
        json.dumps(
            [macros, stmaryrd, renderer], sort_keys=True, separators=(",", ":")
        ).encode()
    )


@cache
def installed_assets() -> AssetSet:
    path = Path(__file__).with_name("assets.json")
    if not path.is_file():
        raise ValueError("The renderer assets are missing. Run just desktop-install.")
    return AssetSet.model_validate_json(path.read_bytes())


def active_asset_version() -> AssetVersion:
    try:
        active = AssetSet.model_validate_json(
            Path(__file__).with_name("active-assets.json").read_bytes()
        )
    except (OSError, ValidationError) as error:
        raise InstallationError(
            "The active renderer descriptor is unavailable. Run just desktop-install."
        ) from error
    return AssetVersion(identity=active.identity)


@cache
def asset_set(identity: Digest) -> AssetSet:
    path = Path(__file__).with_name("asset-sets") / (identity + ".json")
    try:
        result = AssetSet.model_validate_json(path.read_bytes())
    except (OSError, ValidationError) as error:
        raise InvalidAssetsError(
            "The requested renderer assets are unavailable. Run just desktop-install."
        ) from error
    if result.identity != identity:
        raise InvalidAssetsError(
            "The renderer asset identity is damaged. Run just desktop-install."
        )
    return result


@cache
def pandoc_digest() -> str:
    # Each bridge process handles one request; its decks share the same Pandoc.
    # https://docs.python.org/3/library/functools.html#functools.cache
    return digest(
        subprocess.run(["pandoc", "--version"], check=True, capture_output=True).stdout
    )


def producer_files() -> dict[str, Path]:
    return {
        "bridge": Path(__file__),
        "pair-filter": PAIR_FILTER,
        **{
            "ankdown/" + name: EXPORTER / name
            for name in ("ankdown.lua", "cli.py", "mathjax.html", "card.css")
        },
        **{
            "tikz-assets/" + str(file.relative_to(TIKZ_ASSETS)): file
            for file in sorted(TIKZ_ASSETS.rglob("*"))
            if file.is_file()
        },
    }


@cache
def tikz_renderer_identity() -> str:
    files = sorted(file for file in TIKZ_ASSETS.rglob("*") if file.is_file())
    if not files or not (TIKZ_ASSETS / "tikzcd.lua").is_file():
        raise InstallationError(
            "The prepared TikZ-cd renderer is missing. Run just desktop-install."
        )
    return digest(
        b"".join(
            str(file.relative_to(TIKZ_ASSETS)).encode()
            + b"\0"
            + digest(file.read_bytes()).encode()
            + b"\0"
            for file in files
        )
    )


def render_tikzcd_svg(source: str, path: Path) -> str:
    """Compile the authored diagram with the *same* renderer as Anki export.

    The Quiver UI paints many independently transformed SVG layers. Its CSS
    zoom produces seams and nonuniform-looking strokes, particularly on nfold
    curved arrows. The read-only preview uses the authoritative TikZ-cd SVG
    instead; this does not change the original TeX or the graphical editor.
    """
    if not TIKZ_ENVIRONMENT.fullmatch(source.strip()):
        raise ValueError(
            "A diagram preview must contain exactly one TikZ-cd environment."
        )
    identity = tikz_renderer_identity()
    output_dir = user_cache_path("math-flashcards") / "tikz-images"
    output_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ | {
        "FIGURE_STYLES_DIR": str(TIKZ_ASSETS / "styles"),
        "FIGURE_TEMPLATE_FILE": str(TIKZ_ASSETS / "standalone-tikz.tex"),
        "FIGURES_SOURCE_DIR": str(path.parent),
        "PANDOC_DOC_PATH": str(path),
        "SVG_DIR": str(output_dir),
        "TIKZ_RENDER_CONTEXT_HASH": identity,
    }

    process = subprocess.run(
        [
            "pandoc",
            "-f",
            "markdown",
            "-t",
            "html",
            "--lua-filter",
            str(TIKZ_ASSETS / "tikzcd.lua"),
        ],
        input=source,
        text=True,
        cwd=path.parent,
        env=env,
        capture_output=True,
        check=False,
    )
    image = re.search(r"<svg\b[\s\S]*?</svg>", process.stdout)
    if process.returncode or image is None:
        raise ValueError(
            "The commutative diagram did not compile through the shared "
            "TikZ-cd renderer. " + process.stderr[-5000:]
        )
    svg = image.group()
    if ElementTree.fromstring(svg).tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("The TikZ-cd renderer did not produce an SVG image.")
    return svg


def render_diagrams(source: str, path: Path) -> tuple[str, str]:
    """Prepare the temporary Pandoc/Anki input without modifying authored text."""
    if not TIKZ_ENVIRONMENT.search(source):
        return "markdown", source
    # Work on Pandoc's actual RawBlock nodes: a code fence illustrating
    # TikZ-cd, or a quotation containing it, must not become a diagram.
    parsed = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "json"],
        input=source,
        text=True,
        capture_output=True,
        check=True,
    )
    document = json.loads(parsed.stdout)

    pending: list[object] = [document]
    converted = 0
    while pending:
        node = pending.pop()
        if isinstance(node, dict):
            content = node.get("c")
            if (
                node.get("t") == "RawBlock"
                and isinstance(content, list)
                and len(content) == 2
                and content[0] in ("tex", "latex")
                and isinstance(content[1], str)
                and TIKZ_ENVIRONMENT.fullmatch(content[1].strip())
            ):
                node["c"] = [
                    "html",
                    '<div class="anki-commutative-diagram">\n'
                    + render_tikzcd_svg(content[1], path)
                    + "\n</div>",
                ]
                converted += 1
            else:
                pending.extend(node.values())
        elif isinstance(node, list):
            pending.extend(node)
    return (
        ("json", json.dumps(document, ensure_ascii=False))
        if converted
        else ("markdown", source)
    )


@cache
def environment_identity() -> str:
    # Installed distribution metadata supplies producer versions and VCS identities:
    # https://docs.python.org/3/library/importlib.metadata.html
    from importlib.metadata import distributions

    packages: dict[str, tuple[str, str | None]] = {}
    for package in distributions():
        name = package.metadata["Name"]
        if not name or name in packages:
            raise InstallationError(
                "The installed dependency metadata is incomplete. Run just desktop-install."
            )
        packages[name] = (package.version, package.read_text("direct_url.json"))
    return digest(
        json.dumps(
            [sys.version, packages], sort_keys=True, separators=(",", ":")
        ).encode()
    )


def input_hashes(path: Path, media: list[Path], assets: AssetSet) -> dict[str, str]:
    hashes = {str(file): digest(file.read_bytes()) for file in [path, *media]}
    hashes.update(
        {name: digest(file.read_bytes()) for name, file in producer_files().items()}
    )
    hashes["macros"] = assets.identity
    hashes["pandoc"] = pandoc_digest()
    hashes["environment"] = environment_identity()
    return hashes


def has_cards(path: Path) -> bool:
    # A card side is a `.front` or `.back` div, so a deck without either class
    # has no cards; a lone side goes to the exporter, which rejects it. Listing
    # runs this per deck, so it reads text instead of running Pandoc.
    source = path.read_text(encoding="utf-8")
    return ".front" in source or ".back" in source


EMPTY = "The deck has no cards, so it has no Anki package."


def sync(path: Path, output: Path, assets: AssetSet) -> Verification:
    with database() as connection:
        row = connection.execute(
            "SELECT record FROM deck_builds WHERE path = ?", (str(path),)
        ).fetchone()
    current: dict[str, str | None] = dict(input_hashes(path, [], assets))
    package = digest(output.read_bytes()) if output.is_file() else None
    build = digest(row[0].encode()) if row else None
    if row is None:
        state = (
            Sync(
                status="Unsynced",
                reasons=["No Anki package has been generated from this deck."],
                built=None,
            )
            if has_cards(path)
            else Sync(status="Empty", reasons=[EMPTY], built=None)
        )
    else:
        record = BuildRecord.model_validate_json(row[0])
        reasons: list[str] = []
        if current.keys() - record.inputs.keys():
            reasons.append("The exporter changed.")
        if package is None:
            reasons.append("The Anki package file is missing.")
        elif package != record.package:
            reasons.append("The Anki package file changed after generation.")
        for name, expected in record.inputs.items():
            if name in current:
                if current[name] == expected:
                    continue
                reason = (
                    "The deck changed."
                    if name == str(path)
                    else "The renderer assets changed."
                    if name == "macros"
                    else "The exporter changed."
                )
            else:
                file = Path(name)
                current[name] = digest(file.read_bytes()) if file.is_file() else None
                if current[name] == expected:
                    continue
                reason = "Media changed: " + file.name
            if reason not in reasons:
                reasons.append(reason)
        if "The deck changed." in reasons and not has_cards(path):
            reasons.append("The deck has no cards. An update removes its Anki package.")
        state = Sync(
            status="Unsynced" if reasons else "Up to date",
            reasons=reasons,
            built=record.source,
        )
    return Verification(
        status=state.status,
        reasons=state.reasons,
        built=state.built,
        input_identity=digest(
            json.dumps(
                [current, package, build], sort_keys=True, separators=(",", ":")
            ).encode()
        ),
        checked_at=datetime.now(UTC),
        dependencies=sorted(
            {name for name in current if Path(name).is_absolute()}
            | {str(file) for file in producer_files().values()}
            | {str(output)}
        ),
    )


@contextmanager
def render(path: Path, source: str, scratch: Path) -> Iterator[RenderedDeck]:
    # Pandoc owns card parsing: https://pandoc.org/lua-filters.html
    # Keeping the input beside its deck preserves the exporter's image resolution.
    format, prepared = render_diagrams(source, path)
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".tmp",
        prefix=".flashcards-",
        dir=path.parent,
        encoding="utf-8",
    ) as temporary:
        temporary.write(prepared)
        temporary.flush()
        process = subprocess.run(
            [
                "pandoc",
                "-f",
                format,
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
        path = Path(os.path.abspath(source))
        resolved = path.resolve(strict=True)
        if not resolved.is_relative_to(root) and not resolved.is_relative_to(scratch):
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


def generate(root: Path, path: Path, assets: AssetSet) -> Generated:
    from ankdown.cli import RendererAssets

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
                inputs = input_hashes(path, media, assets)
                if inputs[str(path)] != digest(source.encode()):
                    raise ValueError(
                        "The deck changed before generation. Generate it again."
                    )
                temporary = scratch / output.name
                renderer = scratch / "renderer-assets.json"
                renderer.write_text(
                    RendererAssets(
                        macros=assets.macros, stmaryrd=assets.stmaryrd
                    ).model_dump_json()
                )
                process = subprocess.run(
                    [
                        sys.executable,
                        "-I",
                        "-m",
                        "ankdown.cli",
                        "compile",
                        "--output",
                        str(temporary),
                        "--renderer-assets",
                        str(renderer),
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
                    status=sync(path, output, assets).status,
                    package=str(output),
                    log=process.stdout + process.stderr,
                )


def publish_changes(root: Path, changes: list[Change]) -> Organized:
    cache = user_cache_path("math-flashcards")
    cache.mkdir(parents=True, exist_ok=True)
    with FileLock(cache / (digest(str(root).encode()) + ".workspace.lock")):
        paths = [deck_path(root, change.path) for change in changes]
        if len(set(paths)) != len(paths):
            raise ValueError("Each deck can change only once in an operation.")
        originals: dict[Path, bytes | None] = {}
        for change, path in zip(changes, paths, strict=True):
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
) -> (
    Workspace
    | Document
    | Generated
    | RenderedDiagram
    | Organized
    | Review
    | Manifest
    | Sources
    | Checks
    | AssetSet
    | AssetVersion
    | ProblemCache
    | ProblemStored
    | CacheRebuilt
    | ManifestCache
    | SearchCache
    | CachedChecks
):
    if isinstance(request, AssetsInput):
        return installed_assets()
    if isinstance(request, AssetVersionInput):
        return active_asset_version()
    root = workspace_path(request.workspace)
    if isinstance(request, DiagramPreviewInput):
        path = deck_path(root, request.path)
        if not path.is_file():
            raise FileNotFoundError("The diagram's deck is no longer in the workspace.")
        return RenderedDiagram(
            path=request.path,
            source=request.source,
            svg=render_tikzcd_svg(request.source, path),
        )
    if isinstance(request, ManifestCacheInput):
        return manifest_cache(root, request)
    if isinstance(request, RebuildCacheInput):
        directory = user_cache_path("math-flashcards")
        directory.mkdir(parents=True, exist_ok=True)
        with FileLock(directory / "derived.lock", timeout=0.1):
            for name in (
                "derived.sqlite3",
                "derived.sqlite3-wal",
                "derived.sqlite3-shm",
                "derived.sqlite3-journal",
            ):
                path = directory / name
                if path.is_file():
                    send2trash(path)
        return CacheRebuilt(
            session=Session(root=str(root), generation=request.generation)
        )
    if isinstance(request, ReadProblemsInput | StoreProblemsInput):
        return problem_cache(root, request)
    if isinstance(request, ReadSearchInput | StoreSearchInput):
        return search_cache(root, request)
    if isinstance(request, CachedChecksInput):
        return package_history(root, request)
    if isinstance(request, ManifestInput):
        return Manifest(
            session=Session(root=str(root), generation=request.generation),
            entries=[
                Entry(path=str(path.relative_to(root))) for path in deck_paths(root)
            ],
        )
    if isinstance(request, SourcesInput | ChecksInput):
        # Resolve the complete batch before reading anything. A path outside
        # the workspace rejects the request, including symlink escapes.
        paths = [deck_path(root, name) for name in request.paths]
        sources: list[SourceResult | PathFailure] = []
        checks: list[PackageResult | PathFailure] = []
        cache_errors: list[PathFailure] = []
        for name, path in zip(request.paths, paths, strict=True):
            try:
                raw = path.read_bytes()
                source = raw.decode("utf-8")
                revision = digest(raw)
                if isinstance(request, SourcesInput):
                    sources.append(
                        SourceResult(path=name, source=source, revision=revision)
                    )
                    continue
                state = sync(path, package_path(root, path), asset_set(request.assets))
                if digest(path.read_bytes()) != revision:
                    raise ValueError(
                        "The deck changed during verification. Check it again."
                    )
                result = PackageResult(
                    path=name,
                    revision=revision,
                    assets=request.assets,
                    input_identity=state.input_identity,
                    checked_at=state.checked_at,
                    dependencies=state.dependencies,
                    status=state.status,
                    reasons=state.reasons,
                    built=state.built,
                )
                checks.append(result)
                try:
                    store_package_check(root, result)
                except (sqlite3.Error, ValidationError, OSError, Timeout) as error:
                    cache_errors.append(
                        PathFailure(path=name, kind="CacheFailure", message=str(error))
                    )
            except InstallationError as error:
                checks.append(
                    PathFailure(path=name, kind="BackendFailure", message=str(error))
                )
            except InvalidAssetsError as error:
                checks.append(
                    PathFailure(path=name, kind="InvalidAssets", message=str(error))
                )
            except (OSError, UnicodeError) as error:
                failure = PathFailure(
                    path=name, kind="UnreadablePath", message=str(error)
                )
                sources.append(failure)
                checks.append(failure)
            except ValueError as error:
                checks.append(
                    PathFailure(path=name, kind="InvalidDeck", message=str(error))
                )
        session = Session(root=str(root), generation=request.generation)
        if isinstance(request, SourcesInput):
            return Sources(session=session, results=sources)
        return Checks(session=session, results=checks, cache_errors=cache_errors)
    if isinstance(request, OrganizeInput):
        return publish_changes(root, request.changes)
    if isinstance(request, ReviewInput):
        assets = asset_set(request.assets)
        pending: list[Pending] = []
        for path in deck_paths(root):
            state = sync(path, package_path(root, path), assets)
            if state.status == "Unsynced":
                pending.append(
                    Pending(
                        path=str(path.relative_to(root)),
                        status=state.status,
                        reasons=state.reasons,
                        source=path.read_text(encoding="utf-8"),
                        built=state.built,
                    )
                )
        return Review(decks=pending)
    if isinstance(request, ListInput):
        assets = installed_assets()
        summaries: list[Summary] = []
        for path in deck_paths(root):
            state = sync(path, package_path(root, path), assets)
            summaries.append(
                Summary(
                    path=str(path.relative_to(root)),
                    status=state.status,
                    reasons=state.reasons,
                    source=path.read_text(encoding="utf-8"),
                )
            )
        return Workspace(
            root=str(root),
            decks=summaries,
            macros=assets.macros,
            stmaryrd=assets.stmaryrd,
        )
    path = deck_path(root, request.path)
    output = package_path(root, path)
    match request:
        case GenerateInput():
            return generate(root, path, asset_set(request.assets))
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
    return Document(
        session=Session(root=str(root), generation=request.generation),
        path=request.path,
        source=source,
        hash=digest(source.encode()),
        cards=validate(root, path, source)
        if isinstance(request, SaveInput) or request.action == "validate"
        else None,
        status=None,
        reasons=[],
        built=None,
        package=str(output),
    )


def prepare() -> None:
    """Prepare local renderer assets and the interpreter before app launch."""
    directory = Path(__file__).resolve().parent
    renderer = MathJaxPackage.model_validate_json(
        (directory / "node_modules" / "mathjax" / "package.json").read_bytes()
    ).version
    raw, stmaryrd = refresh_macros()
    macros = TypeAdapter(dict[str, MacroDefinition]).validate_json(raw)
    assets = AssetSet(
        identity=asset_identity(macros, stmaryrd, renderer),
        macros=macros,
        stmaryrd=stmaryrd,
        renderer=renderer,
    )
    with tempfile.TemporaryDirectory(
        prefix=".flashcards-runtime-", dir=directory
    ) as temporary:
        staged = Path(temporary)
        (staged / "assets.json").write_text(assets.model_dump_json())
        (staged / "active-assets.json").write_text(assets.model_dump_json())
        (staged / "runtime.txt").write_text(sys.executable + "\n")
        archive = directory / "asset-sets"
        archive.mkdir(exist_ok=True)
        archived = staged / (assets.identity + ".json")
        archived.write_text(assets.model_dump_json())
        destination = archive / archived.name
        if (
            not destination.is_file()
            or destination.read_bytes() != archived.read_bytes()
        ):
            archived.replace(destination)
        for name in ("assets.json", "active-assets.json", "runtime.txt"):
            destination = directory / name
            if (
                destination.is_file()
                and destination.read_bytes() == (staged / name).read_bytes()
            ):
                continue
            (staged / name).replace(destination)
    print(assets.identity)


def build(workspace: Path) -> None:
    """Generate every paired-card deck in a workspace."""
    root = workspace_path(str(workspace))
    assets = installed_assets()
    for path in deck_paths(root):
        result = generate(root, deck_path(root, str(path.relative_to(root))), assets)
        print(result.package)


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
    if len(sys.argv) == 1:
        main()
    else:
        import cyclopts

        app = cyclopts.App()
        app.command(prepare)
        app.command(build)
        app()
