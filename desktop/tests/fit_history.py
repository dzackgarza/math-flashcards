# /// script
# requires-python = ">=3.12"
# dependencies = ["anki"]
# ///
"""Measure the smallest dated history accepted by the installed Anki fit (R14)."""

import json
import tempfile
import time
from pathlib import Path

from anki.collection import Collection
from anki.decks import DeckConfigId
from evidence import evidence


def add_history(collection: Collection, card_id: int, count: int) -> None:
    # Anki revlog schema and training-item conversion:
    # https://github.com/ankitects/anki/blob/main/rslib/src/scheduler/fsrs/params.rs
    start = (int(time.time()) - (count + 10) * 86400) * 1000
    for index in range(count):
        collection.db.execute(
            "insert into revlog values (?,?,?,?,?,?,?,?,?)",
            start + index * 86400000,
            card_id,
            -1,
            3,
            1,
            1,
            2500,
            1000,
            0 if index == 0 else 1,
        )


def main(artifacts: Path) -> None:
    results = []
    with tempfile.TemporaryDirectory(prefix="flashcards-fit-history-") as directory:
        for count in range(17):
            collection = Collection(str(Path(directory) / f"history-{count}.anki2"))
            try:
                model = collection.models.by_name("Basic")
                assert model is not None
                note = collection.new_note(model)
                note.fields = ["Recall", "Answer"]
                collection.add_note(note, collection.decks.id("Default"))
                add_history(collection, note.cards()[0].id, count)
                preset = collection.decks.get_config(DeckConfigId(1))
                assert preset is not None
                params = list(
                    collection._backend.get_deck_configs_for_update(
                        1
                    ).defaults.config.fsrs_params_6
                )
                started = time.perf_counter()
                fit = collection._backend.compute_fsrs_params(
                    search="",
                    current_params=params,
                    ignore_revlogs_before_ms=0,
                    num_of_relearning_steps=len(preset["lapse"]["delays"]),
                    health_check=False,
                )
                result = {
                    "revlog_rows": count,
                    "training_items": fit.fsrs_items,
                    "fit_seconds": time.perf_counter() - started,
                }
                if fit.fsrs_items:
                    for key, parameters in (
                        ("current", params),
                        ("fitted", fit.params),
                    ):
                        started = time.perf_counter()
                        evaluation = collection._backend.evaluate_params_legacy(
                            params=parameters, search="", ignore_revlogs_before_ms=0
                        )
                        result[key] = {
                            "parameters": list(parameters),
                            "log_loss": evaluation.log_loss,
                            "rmse_bins": evaluation.rmse_bins,
                            "seconds": time.perf_counter() - started,
                        }
                results.append(result)
                (artifacts / "fits.json").write_text(json.dumps(results, indent=2))
                if fit.fsrs_items:
                    break
            finally:
                collection.close()
    assert results[-1]["training_items"] > 0, results


if __name__ == "__main__":
    with evidence("fit-history", Path(__file__).parent / "fixtures/study") as artifacts:
        main(artifacts)
