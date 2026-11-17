"""One shared Anki preset; every changed setting remains in the learning record."""

import json

from anki.decks import DeckConfigId

from study.store import Store
from study.values import Settings


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
