"""One shared Anki preset; every changed setting remains in the learning record."""

import json

from anki.decks import DeckConfigId
from anki.errors import BackendError

from study.store import Store
from study.values import Fit, Settings, StudyError, StudyFailure


def set_settings(store: Store, settings: Settings) -> Settings:
    previous = store.opened().settings.model_dump()
    changes = {
        key: value
        for key, value in settings.model_dump().items()
        if previous[key] != value
    }
    if not changes:
        return settings
    preset = store.collection.decks.get_config(DeckConfigId(1))
    assert preset is not None
    preset["new"]["perDay"] = settings.new_per_day
    preset["rev"]["perDay"] = settings.reviews_per_day
    preset["desiredRetention"] = settings.desired_retention
    # Anki invalidates the queue when deck configuration changes; R9.
    store.collection.decks.update_config(preset)
    for key, value in changes.items():
        store.record.setting_change(key, json.dumps(previous[key]), json.dumps(value))
    store.grade_responses.clear()
    return store.opened().settings


def fit(store: Store) -> Fit:
    collection = store.collection
    store.pending_fit = None
    preset = collection.decks.get_config(DeckConfigId(1))
    assert preset is not None
    current = preset["fsrsParams6"]
    try:
        candidate = collection._backend.compute_fsrs_params(
            search="",
            current_params=current,
            ignore_revlogs_before_ms=0,
            num_of_relearning_steps=len(preset["lapse"]["delays"]),
            health_check=False,
        )
        if not candidate.fsrs_items:
            raise StudyFailure(
                StudyError(
                    kind="NotEnoughHistory",
                    message=collection.tr.deck_config_not_enough_history(),
                )
            )
        fitted = collection._backend.evaluate_params_legacy(
            params=candidate.params,
            search="",
            ignore_revlogs_before_ms=0,
        )
        earlier = collection._backend.evaluate_params_legacy(
            params=current,
            search="",
            ignore_revlogs_before_ms=0,
        )
    except BackendError as error:
        # Anki's Python layer has no distinct insufficient-data exception.
        # rslib/src/error/mod.rs translates it through this same fluent key (R14).
        if str(error) == collection.tr.deck_config_not_enough_history():
            raise StudyFailure(
                StudyError(kind="NotEnoughHistory", message=str(error))
            ) from error
        raise
    result = Fit(
        parameters=list(candidate.params),
        current=current,
        reviews=candidate.fsrs_items,
        log_loss=fitted.log_loss,
        rmse_bins=fitted.rmse_bins,
        current_log_loss=earlier.log_loss,
        current_rmse_bins=earlier.rmse_bins,
    )
    store.pending_fit = result
    return result


def apply_fit(store: Store, parameters: list[float]) -> Settings:
    candidate = store.pending_fit
    if candidate is None or candidate.parameters != parameters:
        raise StudyFailure(
            StudyError(
                kind="InvalidSettings",
                message="Run the fit before applying its parameters.",
            )
        )
    preset = store.collection.decks.get_config(DeckConfigId(1))
    assert preset is not None
    before = preset["fsrsParams6"]
    preset["fsrsParams6"] = parameters
    store.collection.decks.update_config(preset)
    store.record.parameter_set(
        parameters, "fit", candidate.reviews, candidate.log_loss, candidate.rmse_bins
    )
    store.record.setting_change(
        "fsrsParams6", json.dumps(before), json.dumps(parameters)
    )
    store.grade_responses.clear()
    store.pending_fit = None
    return store.opened().settings
