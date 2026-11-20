"""Check the live import contracts and prove that each forbidden dependency fails."""

import json
import os
import re
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

    # The window writes learning data only through bridge requests (FR-057):
    # its Tauri capabilities grant no file write, and its sources import no
    # file-system call but the deck watcher.
    capabilities = json.loads(
        (DESKTOP / "src-tauri/capabilities/default.json").read_text()
    )["permissions"]
    sources = {
        path: path.read_text()
        for path in (DESKTOP / "src").rglob("*")
        if path.suffix in {".ts", ".tsx"}
    }
    assert not frontend_writes(capabilities, sources), frontend_writes(
        capabilities, sources
    )
    probe = Path("src/probe.ts")
    assert frontend_writes(
        [*capabilities, "fs:allow-write-file"],
        sources | {probe: 'import { writeFile } from "@tauri-apps/plugin-fs";\n'},
    ) == ["fs:allow-write-file", f"{probe}: writeFile"]
    print("The window has no file write outside the bridge.")


# https://v2.tauri.app/reference/javascript/fs/ and its permission table.
WINDOW_FILE_ACCESS = {"fs:allow-watch", "fs:allow-unwatch"}
FILE_SYSTEM_IMPORT = re.compile(
    r"import\s*\{([^}]*)\}\s*from\s*\"@tauri-apps/plugin-fs\""
)


def frontend_writes(capabilities: list[str], sources: dict[Path, str]) -> list[str]:
    granted = [
        permission
        for permission in capabilities
        if permission.split(":")[0] in {"fs", "shell", "sql"}
        and permission not in WINDOW_FILE_ACCESS
    ]
    imported = [
        f"{path}: {name.strip()}"
        for path, text in sources.items()
        for match in FILE_SYSTEM_IMPORT.finditer(text)
        for name in match.group(1).split(",")
        if name.strip() and name.strip() != "watch"
    ]
    return granted + imported


if __name__ == "__main__":
    main()
