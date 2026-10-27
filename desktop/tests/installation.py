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


def prepare_asset_update(build: Path, candidate: Path, resources: Path) -> None:
    """Prepare a changed renderer set with the real bridge's asset model."""
    candidate.mkdir()
    for name in ("desktop", "backend.py", "paired-cards.lua", "assets.json"):
        shutil.copy2(build / name, candidate / name)
    shutil.copytree(build / "asset-sets", candidate / "asset-sets")
    # A test update must be a *complete* candidate. Omitting the newly
    # prepared TikZ renderer would make its failure an installation-input
    # failure instead of exercising the intended disconnected upgrade.
    shutil.copytree(build / "tikz-assets", candidate / "tikz-assets")
    python = (resources / "runtime.txt").read_text().strip()
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
        resources = (
            data / "math-flashcards" / "active" / "lib" / "Math Flashcards"
        ).resolve(strict=True)
        for name in ("backend.py", "paired-cards.lua", "assets.json"):
            assert (resources / name).read_bytes() == (
                desktop / "src-tauri" / "target" / "release" / name
            ).read_bytes()
        tikz_files = sorted(
            file.relative_to(resources / "tikz-assets")
            for file in (resources / "tikz-assets").rglob("*")
            if file.is_file()
        )
        assert tikz_files
        for name in tikz_files:
            assert (resources / "tikz-assets" / name).read_bytes() == (
                desktop / "src-tauri" / "target" / "release" / "tikz-assets" / name
            ).read_bytes()
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
        assert (
            data / "math-flashcards" / "active" / "bin" / "desktop"
        ).read_bytes() == (
            desktop / "src-tauri" / "target" / "release" / "desktop"
        ).read_bytes()
        application = data / "math-flashcards"
        active_release = (application / "active").resolve(strict=True)
        current_resources = active_release / "lib" / "Math Flashcards"
        assert current_resources != resources
        current_python = (current_resources / "runtime.txt").read_text().strip()
        current_offline = [
            *offline[:4],
            current_python,
            str(current_resources / "backend.py"),
        ]
        original_assets = (current_resources / "assets.json").read_bytes()
        original_launcher = (application / "launch").read_bytes()
        original_runtime = (current_resources / "runtime.txt").read_bytes()
        original_releases = sorted(
            path.name for path in (application / "releases").iterdir()
        )
        candidate = root / "next build"
        build = desktop / "src-tauri" / "target" / "release"
        prepare_asset_update(build, candidate, resources)
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
        assert (application / "active").resolve(strict=True) == active_release
        assert (
            sorted(path.name for path in (application / "releases").iterdir())
            == original_releases
        )
        assert (current_resources / "assets.json").read_bytes() == original_assets, (
            failed.stderr
        )
        assert (application / "launch").read_bytes() == original_launcher
        assert (current_resources / "runtime.txt").read_bytes() == original_runtime
        retained = subprocess.run(
            current_offline,
            input=json.dumps({"action": "list", "workspace": str(workspace)}),
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        assert json.loads(retained.stdout)["macros"] == assets["macros"]
        assert json.loads(retained.stdout)["decks"][0]["status"] == "Up to date"
        assert deck.read_text() == edited
        assert entry_path.read_bytes() == original_entry
        subprocess.run(
            [
                installer_python,
                str(installer),
                str(candidate),
                "--data-dir",
                str(data),
                "--bin-dir",
                str(commands),
            ],
            check=True,
        )
        updated_resources = (
            application / "active" / "lib" / "Math Flashcards"
        ).resolve(strict=True)
        updated_python = (updated_resources / "runtime.txt").read_text().strip()
        updated_offline = [
            *offline[:4],
            updated_python,
            str(updated_resources / "backend.py"),
        ]
        original = subprocess.run(
            current_offline,
            input='{"action":"assets"}',
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        original_set = json.loads(original.stdout)
        adopted = subprocess.run(
            updated_offline,
            input='{"action":"assets"}',
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        adopted_set = json.loads(adopted.stdout)
        assert original_set["identity"] == assets["identity"]
        assert adopted_set["identity"] != original_set["identity"]
        version = subprocess.run(
            current_offline,
            input='{"action":"asset-version"}',
            text=True,
            capture_output=True,
            check=True,
            env=environment,
        )
        assert json.loads(version.stdout)["identity"] == adopted_set["identity"]
        for runtime, renderer in (
            (current_offline, original_set),
            (updated_offline, adopted_set),
        ):
            generated = subprocess.run(
                runtime,
                input=json.dumps(
                    {
                        "action": "generate",
                        "workspace": str(workspace),
                        "path": "Study.md",
                        "assets": renderer["identity"],
                    }
                ),
                text=True,
                capture_output=True,
                check=True,
                env=environment,
            )
            exported = json.loads(generated.stdout)
            assert exported["status"] == "Up to date"
            with zipfile.ZipFile(exported["package"]) as package:
                media = json.loads(package.read("media"))
                macro_file = next(
                    name
                    for name, value in media.items()
                    if value == "_ankdown_macros.js"
                )
                script, assignment = (
                    package.read(macro_file)
                    .decode()
                    .split("\nwindow.ANKDOWN_MACROS = ")
                )
                assert script == renderer["stmaryrd"]
                assert json.loads(assignment.removesuffix(";")) == renderer["macros"]
    print(
        "Installation and update preserve the native build and refresh the validated desktop entry."
    )


if __name__ == "__main__":
    main()
