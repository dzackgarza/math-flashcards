"""Study actions that append to the learning record (research.md R12 and R13)."""

from study.store import Stores
from study.values import Value, ViewedRequest


def viewed(stores: Stores, request: ViewedRequest, workspace: str) -> Value:
    store = stores.attached(workspace)
    if store is not None:
        store.record.editor_view(
            request.card_id,
            request.deck,
            request.shown_ms,
            request.unfocused_ms,
        )
    return Value()
