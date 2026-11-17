"""Operational logs and nested timings, separate from permanent learning evidence.

References: https://docs.python.org/3/library/logging.html#logging.FileHandler
and https://docs.python.org/3/library/profile.html#profile.Profile.dump_stats.
"""

import cProfile
import json
import logging
import os
import platform
import sys
import traceback
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path
from time import perf_counter
from uuid import uuid4

from platformdirs import user_state_path

type LogScalar = str | int | float | bool | None


class Diagnostics:
    def __init__(self, label: str, release: str | None):
        root = Path(__file__).parent
        self.directory = (
            user_state_path("math-flashcards") / "diagnostics" / str(uuid4())
        )
        self.directory.mkdir(parents=True)
        sources = [
            *root.glob("*.py"),
            *root.joinpath("study").rglob("*.py"),
            *root.joinpath("analysis").rglob("*.py"),
        ]
        (self.directory / "context.json").write_text(
            json.dumps(
                {
                    "label": label,
                    "started_at": datetime.now(UTC).isoformat(),
                    "pid": os.getpid(),
                    "parent_pid": os.getppid(),
                    "app_release": release,
                    "python": sys.version,
                    "platform": platform.platform(),
                    "anki_version": version("anki"),
                    "sources": {
                        str(path.relative_to(root)): sha256(
                            path.read_bytes()
                        ).hexdigest()
                        for path in sorted(sources)
                    },
                },
                indent=2,
            )
            + "\n"
        )
        self.handler = logging.FileHandler(self.directory / "events.jsonl")
        self.handler.setFormatter(logging.Formatter("%(message)s"))
        self.logger = logging.getLogger(f"{label}.{self.directory.name}")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        self.logger.addHandler(self.handler)

    @contextmanager
    def operation(self, name: str, inputs: str = "") -> Iterator[dict[str, LogScalar]]:
        identity = str(uuid4())
        details: dict[str, LogScalar] = {
            "id": identity,
            "operation": name,
            "input_sha256": sha256(inputs.encode()).hexdigest(),
        }
        self.logger.info(
            json.dumps(
                {
                    **details,
                    "event": "started",
                    "at": datetime.now(UTC).isoformat(),
                }
            )
        )
        profile = cProfile.Profile()
        started = perf_counter()
        outcome = "ok"
        profile.enable()
        try:
            yield details
        except BaseException as error:
            outcome = "error"
            details["error_type"] = type(error).__name__
            details["error_message"] = str(error)
            details["traceback"] = traceback.format_exc()
            raise
        finally:
            profile.disable()
            elapsed = perf_counter() - started
            filename = identity + ".pstats"
            profile.dump_stats(str(self.directory / filename))
            self.logger.info(
                json.dumps(
                    {
                        **details,
                        "event": "completed",
                        "at": datetime.now(UTC).isoformat(),
                        "outcome": outcome,
                        "elapsed_seconds": elapsed,
                        "profile": filename,
                    }
                )
            )

    def close(self) -> None:
        self.logger.removeHandler(self.handler)
        self.handler.close()
