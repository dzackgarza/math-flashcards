# /// script
# requires-python = ">=3.12"
# ///
"""Check installation and update with real build files and desktop tools."""

import configparser
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path


def main() -> None:
    desktop = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="flashcards-install-") as directory:
        root = Path(directory)
        data = root / "data with spaces 100%"
        commands = root / "bin with spaces 100%"
        arguments = [
            "uv",
            "run",
            "--upgrade",
            str(desktop / "linux" / "install.py"),
            str(desktop / "src-tauri" / "target" / "release"),
            "--data-dir",
            str(data),
            "--bin-dir",
            str(commands),
        ]
        subprocess.run(arguments, check=True)
        entry_path = data / "applications" / "dev.math.flashcards.desktop"
        entry = configparser.ConfigParser(interpolation=None)
        entry.read(entry_path)
        assert entry["Desktop Entry"]["Name"] == "Math Flashcards"
        subprocess.run(["desktop-file-validate", str(entry_path)], check=True)
        for name in ("backend.py", "paired-cards.lua", "assets.json"):
            assert (
                data / "math-flashcards" / "lib" / "Math Flashcards" / name
            ).read_bytes() == (
                desktop / "src-tauri" / "target" / "release" / name
            ).read_bytes()
        resources = data / "math-flashcards" / "lib" / "Math Flashcards"
        python = (resources / "runtime.txt").read_text().strip()
        workspace = root / "offline workspace"
        workspace.mkdir()
        source = (desktop.parent / "decks" / "Analysis" / "Precalculus.md").read_text()
        deck = workspace / "Study.md"
        deck.write_text(source)
        # Linux network namespaces deny all remote access, including requests
        # hidden inside dependencies: https://man7.org/linux/man-pages/man1/unshare.1.html
        offline = [
            "unshare",
            "--user",
            "--map-root-user",
            "--net",
            python,
            str(resources / "backend.py"),
        ]
        environment = os.environ | {
            "XDG_CACHE_HOME": str(root / "fresh cache"),
            "UV_OFFLINE": "1",
        }
        listed = subprocess.run(
            offline,
            input=json.dumps({"action": "list", "workspace": str(workspace)}),
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        listing = json.loads(listed.stdout)
        assert [item["path"] for item in listing["decks"]] == ["Study.md"]
        assert listing["decks"][0]["source"] == source
        assert (
            listing["macros"]
            == json.loads((resources / "assets.json").read_text())["macros"]
        )
        loaded = subprocess.run(
            offline,
            input=json.dumps(
                {
                    "action": "load",
                    "workspace": str(workspace),
                    "path": "Study.md",
                    "generation": 0,
                }
            ),
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        document = json.loads(loaded.stdout)
        assert document["source"] == source
        assert document["hash"] == hashlib.sha256(source.encode()).hexdigest()
        edited = source.replace("Precalculus", "Offline study")
        subprocess.run(
            offline,
            input=json.dumps(
                {
                    "action": "save",
                    "generation": 0,
                    "workspace": str(workspace),
                    "path": "Study.md",
                    "source": edited,
                    "expected": document["hash"],
                }
            ),
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        assert deck.read_text() == edited
        assets = json.loads((resources / "assets.json").read_text())
        assert (
            resources / "asset-sets" / (assets["identity"] + ".json")
        ).read_bytes() == (resources / "assets.json").read_bytes()
        generated = subprocess.run(
            offline,
            input=json.dumps(
                {
                    "action": "generate",
                    "workspace": str(workspace),
                    "path": "Study.md",
                    "assets": assets["identity"],
                }
            ),
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        result = json.loads(generated.stdout)
        assert result["status"] == "Up to date"
        with zipfile.ZipFile(result["package"]) as package:
            media = json.loads(package.read("media"))
            macro_file = next(
                name for name, value in media.items() if value == "_ankdown_macros.js"
            )
            stmaryrd, assignment = (
                package.read(macro_file).decode().split("\nwindow.ANKDOWN_MACROS = ")
            )
            assert stmaryrd == assets["stmaryrd"]
            assert json.loads(assignment.removesuffix(";")) == assets["macros"]
        command = commands / "math-flashcards"
        assert command.is_symlink()
        assert command.resolve() == data / "math-flashcards" / "launch"
        original_entry = entry_path.read_bytes()
        entry_path.write_text(
            "[Desktop Entry]\nType=Application\nName=Old installation\nExec=false\n"
        )
        subprocess.run(arguments, check=True)
        assert entry_path.read_bytes() == original_entry
        assert (data / "math-flashcards" / "bin" / "desktop").read_bytes() == (
            desktop / "src-tauri" / "target" / "release" / "desktop"
        ).read_bytes()
        original_assets = (resources / "assets.json").read_bytes()
        candidate = root / "next build"
        candidate.mkdir()
        build = desktop / "src-tauri" / "target" / "release"
        for name in ("desktop", "backend.py", "paired-cards.lua", "assets.json"):
            shutil.copy2(build / name, candidate / name)
        shutil.copytree(build / "asset-sets", candidate / "asset-sets")
        subprocess.run(
            [
                python,
                "-c",
                "from pathlib import Path; import backend, sys; old=backend.installed_assets(); macros=old.macros | {'maintenanceProof': r'\\mathrm{updated}'}; assets=backend.AssetSet(identity=backend.asset_identity(macros, old.stmaryrd, old.renderer), macros=macros, stmaryrd=old.stmaryrd, renderer=old.renderer); candidate=Path(sys.argv[1]); (candidate / 'assets.json').write_text(assets.model_dump_json()); (candidate / 'asset-sets' / (assets.identity + '.json')).write_text(assets.model_dump_json())",
                str(candidate),
            ],
            cwd=resources,
            check=True,
        )
        installer = desktop / "linux" / "install.py"
        installer_python = subprocess.check_output(
            ["uv", "python", "find", "--script", str(installer)], text=True
        ).strip()
        failed_environment = os.environ.copy()
        failed_environment.pop("UV_OFFLINE", None)
        failed_environment.update(
            {"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
        )
        failed = subprocess.run(
            [
                "unshare",
                "--user",
                "--map-root-user",
                "--net",
                installer_python,
                str(installer),
                str(candidate),
                "--data-dir",
                str(data),
                "--bin-dir",
                str(commands),
            ],
            text=True,
            capture_output=True,
            env=failed_environment,
            check=False,
        )
        assert failed.returncode != 0, (
            "The disconnected dependency update unexpectedly succeeded."
        )
        assert (resources / "assets.json").read_bytes() == original_assets, (
            failed.stderr
        )
        retained = subprocess.run(
            offline,
            input=json.dumps({"action": "list", "workspace": str(workspace)}),
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        assert json.loads(retained.stdout)["macros"] == assets["macros"]
        assert deck.read_text() == edited
        assert entry_path.read_bytes() == original_entry
    print(
        "Installation and update preserve the native build and refresh the validated desktop entry."
    )


if __name__ == "__main__":
    main()
