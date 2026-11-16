"""Native Study values and bridge contract (specs/001-in-app-review/data-model.md)."""

from pathlib import PurePosixPath
from typing import Annotated, Literal

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, FiniteFloat


class Value(BaseModel):
    model_config = ConfigDict(extra="forbid")


def deck_path(value: str) -> str:
    parts = value.split("/")
    if (
        not value.endswith(".md")
        or PurePosixPath(value).is_absolute()
        or "\\" in value
        or any(part in {"", ".", ".."} for part in parts)
        or parts[0] == "apkg"
    ):
        raise ValueError("Use a relative Markdown deck path.")
    return value


type CardId = Annotated[str, Field(min_length=1)]
type DeckPath = Annotated[str, AfterValidator(deck_path)]
type Digest = Annotated[str, Field(pattern=r"^[a-f0-9]{64}$")]
type RowId = Annotated[int, Field(gt=0)]
type Milliseconds = Annotated[int, Field(ge=0)]
type Grade = Literal["again", "hard", "good", "easy"]


class Card(Value):
    id: CardId
    front: str
    back: str
    tags: list[str]
    media: list[str]


class StudyDeck(Value):
    path: DeckPath
    source_hash: Digest
    title: str
    tags: list[str]
    cards: list[Card]


class WorkspaceScope(Value):
    kind: Literal["workspace"]


class FolderScope(Value):
    kind: Literal["folder"]
    path: str


class DeckScope(Value):
    kind: Literal["deck"]
    path: DeckPath


type Scope = Annotated[
    WorkspaceScope | FolderScope | DeckScope, Field(discriminator="kind")
]


class Timing(Value):
    reveal_ms: Milliseconds
    grade_ms: Milliseconds
    unfocused_ms: Milliseconds


class Settings(Value):
    new_per_day: Annotated[int, Field(ge=0, le=9999)]
    reviews_per_day: Annotated[int, Field(ge=0, le=9999)]
    desired_retention: Annotated[FiniteFloat, Field(ge=0.70, le=0.99)]


class Counts(Value):
    new: int
    learning: int
    review: int


class DeckCounts(Value):
    path: str
    kind: Literal["workspace", "folder", "deck"]
    counts: Counts
    children: list["DeckCounts"]


class GradeLabels(Value):
    again: str
    hard: str
    good: str
    easy: str


class StudyCard(Value):
    state: Literal["Card"] = "Card"
    presentation: RowId
    card_id: CardId
    deck: DeckPath
    front: str
    back: str
    labels: GradeLabels
    counts: Counts
    undoable: bool


class StudyFinished(Value):
    state: Literal["Finished"] = "Finished"
    graded_today: int
    next_learning_seconds: int | None
    counts: Counts
    undoable: bool


type StudyNext = Annotated[StudyCard | StudyFinished, Field(discriminator="state")]


class FailedDeck(Value):
    path: DeckPath
    message: str


class Duplicate(Value):
    card_id: CardId
    paths: list[DeckPath]


class SyncResult(Value):
    added: int
    updated: int
    moved: int
    removed: int
    restored: int
    failed: list[FailedDeck]
    duplicates: list[Duplicate]
    pending: int


class StoreSummary(Value):
    store: str
    paths: list[str]
    path_exists: bool
    created: str
    last_used: str
    cards: int
    responses: int


class Open(Value):
    state: Literal["Open"] = "Open"
    store: str
    media: str
    record: str
    settings: Settings
    counts: DeckCounts


class Unattached(Value):
    state: Literal["Unattached"] = "Unattached"
    stores: list[StoreSummary]


type StudyOpen = Annotated[Open | Unattached, Field(discriminator="state")]


class Fit(Value):
    parameters: list[FiniteFloat]
    current: list[FiniteFloat]
    reviews: int
    log_loss: FiniteFloat
    rmse_bins: FiniteFloat
    current_log_loss: FiniteFloat
    current_rmse_bins: FiniteFloat


class StoreCopy(Value):
    path: str


class StudyError(Value):
    kind: Literal[
        "StoreUnreadable",
        "StaleCard",
        "InvalidSettings",
        "UnknownScope",
        "UnknownStore",
        "NotEnoughHistory",
        "CopyFailed",
    ]
    message: str


class StudyFailure(Exception):
    def __init__(self, error: StudyError):
        super().__init__(error.message)
        self.error = error


class WorkspaceRequest(Value):
    action: Literal["study-open", "study-counts", "study-fit"]
    workspace: str


class Existing(Value):
    kind: Literal["existing"]
    store: str


class New(Value):
    kind: Literal["new"]


class AttachRequest(Value):
    action: Literal["study-attach"]
    workspace: str
    choice: Annotated[Existing | New, Field(discriminator="kind")]


class SyncRequest(Value):
    action: Literal["study-sync"]
    workspace: str
    assets: Digest
    decks: Annotated[list[StudyDeck], Field(max_length=8)]
    paths: list[DeckPath]


class BeginRequest(Value):
    action: Literal["study-begin"]
    workspace: str
    scope: Scope


class SessionRequest(Value):
    action: Literal["study-next", "study-undo", "study-end"]
    workspace: str
    session: RowId


class AnswerRequest(Value):
    action: Literal["study-answer"]
    workspace: str
    session: RowId
    presentation: RowId
    grade: Grade
    timing: Timing


class SettingsRequest(Value):
    action: Literal["study-set-settings"]
    workspace: str
    settings: Settings


class ApplyFitRequest(Value):
    action: Literal["study-apply-fit"]
    workspace: str
    parameters: list[FiniteFloat]


class CopyRequest(Value):
    action: Literal["study-copy"]
    workspace: str
    directory: str


class ViewedRequest(Value):
    action: Literal["study-viewed"]
    workspace: str
    card_id: CardId
    deck: DeckPath
    shown_ms: Milliseconds
    unfocused_ms: Milliseconds


type Request = Annotated[
    WorkspaceRequest
    | AttachRequest
    | SyncRequest
    | BeginRequest
    | SessionRequest
    | AnswerRequest
    | SettingsRequest
    | ApplyFitRequest
    | CopyRequest
    | ViewedRequest,
    Field(discriminator="action"),
]
