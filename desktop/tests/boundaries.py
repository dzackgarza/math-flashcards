"""Check the live import contracts and prove that each forbidden dependency fails."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile


DESKTOP = Path(__file__).resolve().parents[1]


def lint(directory: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["uvx", "--from", "import-linter", "lint-imports", "--no-cache"],
        cwd=directory,
        env=os.environ | {"PYTHONPATH": str(directory)},
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> None:
    baseline = lint(DESKTOP)
    assert baseline.returncode == 0, baseline.stdout + baseline.stderr
    violations = (
        ("analysis.catalog.boundary_probe", "study"),
        ("analysis.catalog.boundary_probe", "anki"),
        ("analysis.catalog.boundary_probe", "backend"),
        ("study.boundary_probe", "analysis"),
        ("analysis.catalog.boundary_probe", "analysis.catalog.boundary_peer"),
    )
    for importer, imported in violations:
        with tempfile.TemporaryDirectory(prefix="flashcards-imports-") as temporary:
            directory = Path(temporary)
            for package in ("study", "analysis"):
                shutil.copytree(
                    DESKTOP / package,
                    directory / package,
                    ignore=shutil.ignore_patterns("__pycache__"),
                )
            shutil.copy2(DESKTOP / ".importlinter", directory)
            shutil.copy2(DESKTOP / "backend.py", directory)
            (directory / "analysis/catalog/boundary_peer.py").write_text("")
            target = directory / (importer.replace(".", "/") + ".py")
            target.write_text(f"import {imported}\n")
            result = lint(directory)
            report = result.stdout + result.stderr
            assert result.returncode == 1, report
            assert f"{importer} -> {imported}" in report, report
    print("Import contracts reject every forbidden dependency.")


if __name__ == "__main__":
    main()
