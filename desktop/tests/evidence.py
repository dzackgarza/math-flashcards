"""Retain test context and nested Python costs with the standard cProfile format.

Reference: https://docs.python.org/3/library/profile.html#profile.Profile.dump_stats
"""

import cProfile
import json
import platform
import subprocess
import sys
import time
import traceback
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path


@contextmanager
def evidence(label: str, fixtures: Path) -> Iterator[Path]:
    started = time.perf_counter()
    timestamp = datetime.now(UTC)
    repository = Path(__file__).resolve().parents[2]
    directory = repository / "test-history" / f"{timestamp:%Y%m%dT%H%M%S.%fZ}-{label}"
    directory.mkdir(parents=True)
    revision = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()
    changes = subprocess.check_output(
        ["git", "diff", "HEAD", "--", "desktop", "justfile"], cwd=repository
    )
    paths = subprocess.check_output(
        [
            "git",
            "ls-files",
            "-z",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            "desktop",
            "justfile",
        ],
        cwd=repository,
        text=True,
    ).split("\0")
    sources = {
        name: sha256((repository / name).read_bytes()).hexdigest()
        for name in sorted(set(paths))
        if name and (repository / name).is_file()
    }
    inputs = {
        str(path.relative_to(fixtures)): sha256(path.read_bytes()).hexdigest()
        for path in sorted(fixtures.rglob("*"))
        if path.is_file()
    }
    preparation = time.perf_counter() - started
    profile = cProfile.Profile()
    failure: str | None = None
    profile.enable()
    try:
        yield directory
    except BaseException:
        failure = traceback.format_exc()
        raise
    finally:
        profile.disable()
        elapsed = time.perf_counter() - started
        profile.dump_stats(str(directory / "python.pstats"))
        (directory / "test.log").write_text(
            failure if failure is not None else "Scenario completed.\n"
        )
        (directory / "run.json").write_text(
            json.dumps(
                {
                    "schema": 1,
                    "label": label,
                    "started_at": timestamp.isoformat(),
                    "revision": revision,
                    "working_diff_sha256": sha256(changes).hexdigest(),
                    "sources": sources,
                    "command": sys.argv,
                    "python": sys.version,
                    "platform": platform.platform(),
                    "fixtures": inputs,
                    "preparation_seconds": preparation,
                    "elapsed_seconds": elapsed,
                    "result": "failed" if failure is not None else "passed",
                    "profile": "python.pstats",
                    "profile_scope": (
                        "Python test process, including fixture construction and nested calls. "
                        "Child-process waits are measured at their caller; child call stacks "
                        "are outside this profile."
                    ),
                },
                indent=2,
            )
            + "\n"
        )
        print(f"Test evidence: {directory}", flush=True)


def main() -> None:
    """Run one test command in a child process and retain its evidence.

    Usage: evidence.py LABEL FIXTURES -- COMMAND...
    The command's output goes to command.log; its wall time is the run's
    elapsed time, and its exit status is the run's result.
    """
    label, fixtures, separator, *command = sys.argv[1:]
    assert separator == "--" and command, main.__doc__
    with evidence(label, Path(fixtures)) as directory:
        with (directory / "command.log").open("w") as log:
            started = time.perf_counter()
            status = subprocess.run(
                command, stdout=log, stderr=subprocess.STDOUT
            ).returncode
            (directory / "command.json").write_text(
                json.dumps(
                    {
                        "command": command,
                        "status": status,
                        "seconds": time.perf_counter() - started,
                    },
                    indent=2,
                )
                + "\n"
            )
        if status:
            sys.stdout.write((directory / "command.log").read_text()[-4000:])
            raise SystemExit(status)


if __name__ == "__main__":
    main()
