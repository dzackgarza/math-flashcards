"""Run independent analysis modules through the real one-process bridge."""

import json
import os
import shutil
import sqlite3
import subprocess
import tempfile
from contextlib import ExitStack, closing
from pathlib import Path

from evidence import evidence


def main(artifacts: Path) -> None:
    desktop = Path(__file__).resolve().parents[1]
    runtime = (desktop / "runtime.txt").read_text().strip()
    with (
        tempfile.TemporaryDirectory(prefix="flashcards-analyses-") as directory,
        ExitStack() as cleanup,
    ):
        root = Path(directory)
        (root / "state").mkdir()
        cleanup.callback(
            shutil.copytree, root / "state", artifacts / "application-state"
        )
        for name in ("backend.py", "rendering.py", "diagnostics.py"):
            shutil.copy2(desktop / name, root / name)
        for name in ("study", "analysis"):
            shutil.copytree(
                desktop / name,
                root / name,
                ignore=shutil.ignore_patterns("__pycache__"),
            )
        record = root / "data/math-flashcards/study/fixture/record.sqlite3"
        record.parent.mkdir(parents=True)
        shutil.copy2(desktop / "tests/fixtures/study/record-v1.sqlite3", record)
        environment = os.environ | {
            "XDG_DATA_HOME": str(root / "data"),
            "XDG_STATE_HOME": str(root / "state"),
        }

        def request(action: str, **values):
            result = subprocess.run(
                [runtime, "-I", str(root / "backend.py")],
                input=json.dumps({"action": action, **values}) + "\n",
                text=True,
                capture_output=True,
                env=environment,
                check=False,
            )
            with (artifacts / "bridge.log").open("a") as log:
                log.write(result.stdout + result.stderr)
            assert result.returncode == 0, result.stderr
            return json.loads(result.stdout)

        def snapshot():
            with closing(sqlite3.connect(record)) as connection:
                return list(connection.iterdump())

        before = snapshot()
        catalog = request("analysis-list")
        assert [item["name"] for item in catalog] == [
            "calibration",
            "recall_by_folder",
        ], catalog
        assert [item["title"] for item in catalog] == sorted(
            item["title"] for item in catalog
        )
        assert all("self-graded" in item["summary"] for item in catalog)
        baseline = {
            item["name"]: request("analysis-run", record=str(record), name=item["name"])
            for item in catalog
        }
        assert snapshot() == before
        for name, result in baseline.items():
            assert result["analysis"]["name"] == name and "rows" in result, result
        extra = root / "analysis/catalog/extra.py"
        extra.write_text("""from analysis import Analysis, AnalysisTable, Column
title = "Extra analysis"
summary = "Count retained presentations."
def run(connection):
    return AnalysisTable(analysis=Analysis(name="extra", title=title, summary=summary, failure=None), columns=[Column(name="Presentations", unit=None)], rows=[list(connection.execute("select count(*) from presentation").fetchone())])
""")
        expanded = request("analysis-list")
        assert [item["title"] for item in expanded] == sorted(
            item["title"] for item in expanded
        )
        assert {item["name"] for item in expanded} == {
            "calibration",
            "recall_by_folder",
            "extra",
        }
        with closing(sqlite3.connect(record)) as connection:
            count = connection.execute("select count(*) from presentation").fetchone()[
                0
            ]
        assert request("analysis-run", record=str(record), name="extra")["rows"] == [
            [count]
        ]
        for name, result in baseline.items():
            assert request("analysis-run", record=str(record), name=name) == result
        (root / "analysis/catalog/broken.py").write_text(
            'title="Broken"\nsummary="Raises a calculation error."\ndef run(connection):\n    raise ValueError("Broken calculation")\n'
        )
        failure = request("analysis-run", record=str(record), name="broken")
        assert (
            failure["kind"] == "AnalysisFailed"
            and "Broken calculation" in failure["message"]
        ), failure
        (root / "analysis/catalog/writing.py").write_text(
            'title="Writing"\nsummary="Attempts a write."\ndef run(connection):\n    connection.execute("insert into setting_change select * from setting_change")\n'
        )
        failure = request("analysis-run", record=str(record), name="writing")
        assert (
            failure["kind"] == "AnalysisFailed" and "readonly" in failure["message"]
        ), failure
        assert snapshot() == before
        (root / "analysis/catalog/unavailable.py").write_text(
            'raise RuntimeError("Unavailable analysis")\n'
        )
        unavailable = next(
            item for item in request("analysis-list") if item["name"] == "unavailable"
        )
        assert "Unavailable analysis" in unavailable["failure"]
        assert (
            request("analysis-run", record=str(record), name="absent")["kind"]
            == "UnknownAnalysis"
        )
        outside = root / "record.sqlite3"
        shutil.copy2(record, outside)
        assert (
            request("analysis-run", record=str(outside), name="calibration")["kind"]
            == "RecordUnreadable"
        )
        for name, result in baseline.items():
            assert request("analysis-run", record=str(record), name=name) == result
        assert snapshot() == before


if __name__ == "__main__":
    with evidence("analysis", Path(__file__).parent / "fixtures/study") as artifacts:
        main(artifacts)
