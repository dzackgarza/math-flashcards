"""Native card synchronization through Anki's collection API (research.md R6/R7).

Reference: https://github.com/ankitects/anki/blob/main/pylib/anki/collection.py
"""

import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from anki.collection import AddNoteRequest
from pydantic import TypeAdapter
from rendering import InvalidAssetsError, asset_set, digest

from study.store import Store
from study.values import Duplicate, FailedDeck, SyncRequest, SyncResult, Value


class DeckState(Value):
    inputs: dict[str, str]
    assets: str
    title: str
    tags: list[str]
    cards: list[str]


def current(state: DeckState, assets: str) -> bool:
    if state.assets != assets:
        return False
    try:
        return all(
            digest(Path(path).read_bytes()) == value
            for path, value in state.inputs.items()
        )
    except OSError:
        return False


def retain(path: Path, data: bytes) -> None:
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"Retained content is damaged: {path}")
        return
    with path.open("xb") as stream:
        stream.write(data)


def sync(store: Store, workspace: Path, request: SyncRequest) -> SyncResult:
    result = SyncResult(
        added=0,
        updated=0,
        moved=0,
        removed=0,
        restored=0,
        failed=[],
        duplicates=[],
        pending=0,
    )
    collection = store.collection
    states = TypeAdapter(dict[str, DeckState]).validate_python(
        collection.get_config("native_decks", {})
    )
    try:
        assets = asset_set(request.assets)
        retain(
            store.directory / "record-assets" / (request.assets + ".json"),
            assets.model_dump_json().encode(),
        )
    except (OSError, ValueError, InvalidAssetsError) as error:
        result.failed = [
            FailedDeck(path=deck.path, message=str(error)) for deck in request.decks
        ]
        result.pending = len(request.paths)
        return result

    model = collection.models.by_name("Native card identity")
    if model is None:
        model = collection.models.new("Native card identity")
        collection.models.add_field(model, collection.models.new_field("CardId"))
        template = collection.models.new_template("Card")
        template["qfmt"] = "{{CardId}}"
        template["afmt"] = "{{CardId}}"
        collection.models.add_template(model, template)
        model = collection.models.get(collection.models.add_dict(model).id)
        assert model is not None

    owners = {
        identity: path for path, state in states.items() for identity in state.cards
    }
    for deck in request.decks:
        previous = states.get(deck.path)
        try:
            source_path = (workspace / deck.path).resolve(strict=True)
            if digest(source_path.read_bytes()) != deck.source_hash:
                raise ValueError(f"The saved source changed: {deck.path}")
            references_current = all(
                dict(
                    store.record.connection.execute(
                        "select label, name from image_reference where content=(select content from card_change where card_id=? order by id desc limit 1)",
                        (card.id,),
                    )
                )
                == card.references
                for card in deck.cards
            )
            if (
                previous is not None
                and current(previous, request.assets)
                and references_current
            ):
                continue
            inputs = {str(source_path): deck.source_hash}
            media: dict[str, tuple[str, bytes]] = {}
            for card in deck.cards:
                if not set(card.references.values()) <= set(card.media):
                    raise ValueError(
                        f"Image references must name retained media: {card.id}"
                    )
                for name in card.media:
                    target = urlsplit(name)
                    if target.scheme or target.netloc:
                        raise ValueError(f"Study media must be a local file: {name}")
                    path = (source_path.parent / unquote(target.path)).resolve(
                        strict=True
                    )
                    data = path.read_bytes()
                    identity = digest(data)
                    inputs[str(path)] = identity
                    media[name] = (identity, data)
            seen: set[str] = set()
            duplicates = []
            for card in deck.cards:
                owner = owners.get(card.id)
                if card.id in seen or (owner is not None and owner != deck.path):
                    duplicates.append(
                        Duplicate(
                            card_id=card.id,
                            paths=sorted({deck.path, owner or deck.path}),
                        )
                    )
                seen.add(card.id)
            if duplicates:
                result.duplicates.extend(duplicates)
                continue
            for identity, data in media.values():
                retain(store.directory / "record-media" / identity, data)

            deck_id = collection.decks.id(
                "Workspace::" + deck.path[:-3].replace("/", "::")
            )
            additions = []
            changed = []
            versions = []
            for card in deck.cards:
                retained = {name: media[name][0] for name in card.media}
                identity = digest(
                    json.dumps(
                        [
                            card.front,
                            card.back,
                            request.assets,
                            retained,
                            card.references,
                        ],
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode()
                )
                content = store.record.connection.execute(
                    "select id from content where digest=?", (identity,)
                ).fetchone()
                if content is None:
                    content_id = store.record.content(
                        identity, card.front, card.back, request.assets
                    )
                    for name, media_digest in retained.items():
                        store.record.media(content_id, name, media_digest)
                    for label, name in card.references.items():
                        store.record.image_reference(content_id, label, name)
                else:
                    content_id = content[0]
                tags = sorted(set(deck.tags + card.tags))
                latest = store.record.connection.execute(
                    "select content, tags from card_change where card_id=? order by id desc limit 1",
                    (card.id,),
                ).fetchone()
                kinds = []
                if latest is None:
                    kinds.append("added")
                else:
                    if latest[0] != content_id:
                        kinds.append("content")
                    if json.loads(latest[1]) != tags:
                        kinds.append("tags")
                if not kinds:
                    continue
                notes = collection.find_notes("CardId:" + json.dumps(card.id))
                if notes:
                    note = collection.get_note(notes[0])
                    note.tags = sorted(
                        set(tags + [tag for tag in note.tags if tag == "leech"])
                    )
                    changed.append(note)
                else:
                    note = collection.new_note(model)
                    note.guid = card.id
                    note["CardId"] = card.id
                    note.tags = tags
                    additions.append(AddNoteRequest(note=note, deck_id=deck_id))
                versions.append((card.id, kinds, content_id, tags))
            if additions:
                collection.add_notes(additions)
            if changed:
                collection.update_notes(changed, skip_undo_entry=True)
            for identity, kinds, content, tags in versions:
                for kind in kinds:
                    store.record.card_change(
                        identity,
                        kind,
                        None if kind == "added" else deck.path,
                        deck.path,
                        content,
                        tags,
                    )
                owners[identity] = deck.path
            result.added += sum("added" in kinds for _, kinds, _, _ in versions)
            result.updated += sum("added" not in kinds for _, kinds, _, _ in versions)
            states[deck.path] = DeckState(
                inputs=inputs,
                assets=request.assets,
                title=deck.title,
                tags=deck.tags,
                cards=[card.id for card in deck.cards],
            )
            collection.set_config(
                "native_decks",
                {path: state.model_dump() for path, state in states.items()},
            )
        except (OSError, ValueError) as error:
            result.failed.append(FailedDeck(path=deck.path, message=str(error)))
    result.pending = sum(
        path not in states or not current(states[path], request.assets)
        for path in request.paths
    )
    return result
