"""Study actions that append to the learning record (research.md R12 and R13)."""

from pathlib import PurePosixPath

import anki.collection  # noqa: F401 -- initialize Anki before its cyclic card imports
from anki.cards import CardId as AnkiCardId
from anki.scheduler.v3 import CardAnswer, SchedulingState
from pydantic import TypeAdapter

from study.record import Presentation, Response
from study.store import Store, Stores, deck_name
from study.sync import DeckState
from study.values import (
    AnswerRequest,
    Begun,
    Counts,
    GradeLabels,
    Scope,
    StudyCard,
    StudyError,
    StudyFailure,
    StudyFinished,
    StudyNext,
    Value,
    ViewedRequest,
)


def stale() -> StudyFailure:
    return StudyFailure(
        StudyError(
            kind="StaleCard",
            message="This presentation is no longer current. Fetch the current card.",
        )
    )


def select_scope(store: Store, kind: str, path: str | None) -> None:
    name = deck_name(path or "")
    paths = store.collection.get_config("native_decks", {})
    known = kind == "workspace" or (
        path in paths
        if kind == "deck"
        else any(p.startswith(path + "/") for p in paths)
    )
    deck = store.collection.decks.by_name(name)
    if deck is None or not known:
        raise StudyFailure(
            StudyError(
                kind="UnknownScope",
                message=f"No study cards in {path or 'this workspace'}.",
            )
        )
    store.collection.decks.select(deck["id"])


def select_session(store: Store, session: int) -> None:
    scope = store.record.connection.execute(
        "select scope_kind, scope_path from session where id=? and id not in (select session from session_end)",
        (session,),
    ).fetchone()
    if scope is None:
        raise stale()
    select_scope(store, *scope)


def interval(state: SchedulingState) -> int:
    # Anki's scheduling_states.proto owns the units and the state variants.
    # https://github.com/ankitects/anki/blob/main/proto/anki/scheduler.proto
    normal = state.normal
    match normal.WhichOneof("kind"):
        case "learning":
            return normal.learning.scheduled_secs
        case "relearning":
            return normal.relearning.learning.scheduled_secs
        case "review":
            return normal.review.scheduled_days * 86400
        case _:
            raise ValueError("Anki offered a state without a review interval.")


def begin(store: Store, scope: Scope) -> Begun:
    path = None if scope.kind == "workspace" else scope.path
    select_scope(store, scope.kind, path)
    session = store.record.session(scope.kind, path)
    return Begun(session=session, next=next_card(store, session))


def next_card(store: Store, session: int) -> StudyNext:
    select_session(store, session)
    collection = store.collection
    queue = collection.sched.get_queued_cards(fetch_limit=1)
    counts = Counts(
        new=queue.new_count, learning=queue.learning_count, review=queue.review_count
    )
    if not queue.cards:
        info = collection.sched.congratulations_info()
        graded = collection.db.scalar(
            "select count(*) from revlog where id>=? and ease>0",
            (collection.sched.day_cutoff - 86400) * 1000,
        )
        return StudyFinished(
            graded_today=graded,
            next_learning_seconds=info.secs_until_next_learn
            if info.learn_remaining
            else None,
            counts=counts,
            undoable=False,
        )
    queued = queue.cards[0]
    card = collection.get_card(AnkiCardId(queued.card.id))
    card_id = card.note().guid
    decks = TypeAdapter(dict[str, DeckState]).validate_python(
        collection.get_config("native_decks", {})
    )
    path, deck = next(
        (path, deck) for path, deck in decks.items() if card_id in deck.cards
    )
    content, tags = store.record.connection.execute(
        "select content, tags from card_change where card_id=? order by id desc limit 1",
        (card_id,),
    ).fetchone()
    front, back, assets = store.record.connection.execute(
        "select front, back, assets from content where id=?", (content,)
    ).fetchone()
    media = {
        name: str(store.directory / "record-media" / digest)
        for name, digest in store.record.connection.execute(
            "select name, digest from media where content=?", (content,)
        )
    }
    labels = GradeLabels(
        **dict(
            zip(
                ("again", "hard", "good", "easy"),
                collection.sched.describe_next_states(queued.states),
                strict=True,
            )
        )
    )
    position = store.record.connection.execute(
        "select count(*) + 1 from presentation where session=?", (session,)
    ).fetchone()[0]
    kind = queued.states.current.normal.WhichOneof("kind")
    assert kind is not None
    memory = card.memory_state
    stats = collection.card_stats_data(card.id)
    settings = store.opened().settings
    parameters = store.record.connection.execute(
        "select max(id) from parameter_set"
    ).fetchone()[0]
    facts = Presentation(
        session=session,
        position=position,
        card_id=card_id,
        content=content,
        deck_path=path,
        folder=str(PurePosixPath(path).parent) if "/" in path else "",
        deck_title=deck.title,
        tags=tags,
        kind=kind,
        scheduler_day=collection.sched.today,
        before_interval_days=card.ivl,
        before_due=card.due,
        before_reps=card.reps,
        before_lapses=card.lapses,
        before_stability=memory.stability if memory else None,
        before_difficulty=memory.difficulty if memory else None,
        before_retrievability=stats.fsrs_retrievability
        if stats.HasField("fsrs_retrievability")
        else None,
        offer_again_s=interval(queued.states.again),
        offer_hard_s=interval(queued.states.hard),
        offer_good_s=interval(queued.states.good),
        offer_easy_s=interval(queued.states.easy),
        labels=labels.model_dump_json(),
        desired_retention=settings.desired_retention,
        parameter_set=parameters,
        new_per_day=settings.new_per_day,
        reviews_per_day=settings.reviews_per_day,
    )
    presentation = store.record.presentation(facts)
    return StudyCard(
        presentation=presentation,
        card_id=card_id,
        deck=path,
        front=front,
        back=back,
        assets=assets,
        media=media,
        references=dict(
            store.record.connection.execute(
                "select label, name from image_reference where content=?", (content,)
            )
        ),
        labels=labels,
        counts=counts,
        undoable=False,
    )


def answer(store: Store, request: AnswerRequest) -> StudyNext:
    select_session(store, request.session)
    collection = store.collection
    latest = store.record.connection.execute(
        "select id, card_id from presentation where session=? order by id desc limit 1",
        (request.session,),
    ).fetchone()
    queue = collection.sched.get_queued_cards(fetch_limit=1)
    if latest is None or latest[0] != request.presentation or not queue.cards:
        raise stale()
    queued = queue.cards[0]
    card = collection.get_card(AnkiCardId(queued.card.id))
    if (
        card.note().guid != latest[1]
        or store.record.connection.execute(
            "select 1 from response where presentation=?", (request.presentation,)
        ).fetchone()
    ):
        raise stale()
    ratings = {
        "again": CardAnswer.AGAIN,
        "hard": CardAnswer.HARD,
        "good": CardAnswer.GOOD,
        "easy": CardAnswer.EASY,
    }
    card.start_timer()
    answer = collection.sched.build_answer(
        card=card, states=queued.states, rating=ratings[request.grade]
    )
    answer.milliseconds_taken = min(
        request.timing.reveal_ms + request.timing.grade_ms, card.time_limit()
    )
    collection.sched.answer_card(answer)
    after = collection.get_card(card.id)
    row = collection.db.first(
        "select id,cid,usn,ease,ivl,lastIvl,factor,time,type from revlog where cid=? order by id desc limit 1",
        card.id,
    )
    assert row is not None
    memory = after.memory_state
    store.record.response(
        Response(
            presentation=request.presentation,
            card_id=latest[1],
            grade=request.grade,
            reveal_ms=request.timing.reveal_ms,
            grade_ms=request.timing.grade_ms,
            unfocused_ms=request.timing.unfocused_ms,
            after_interval_days=after.ivl,
            after_due=after.due,
            after_stability=memory.stability if memory else None,
            after_difficulty=memory.difficulty if memory else None,
            recovered=False,
            revlog_id=row[0],
            revlog_cid=row[1],
            revlog_usn=row[2],
            revlog_ease=row[3],
            revlog_ivl=row[4],
            revlog_last_ivl=row[5],
            revlog_factor=row[6],
            revlog_time_ms=row[7],
            revlog_type=row[8],
        )
    )
    return next_card(store, request.session)


def end(store: Store, session: int) -> Value:
    select_session(store, session)
    finished = not store.collection.sched.get_queued_cards(fetch_limit=1).cards
    store.record.session_end(session, "finished" if finished else "left")
    return Value()


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
