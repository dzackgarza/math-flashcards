# /// script
# requires-python = ">=3.12"
# dependencies = ["cyclopts", "pydantic", "platformdirs"]
# ///
"""Install the native app and its desktop entry in user directories."""

import configparser
import os
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path

import cyclopts
from platformdirs import user_data_path
from pydantic import BaseModel, Field, field_validator

APP_ID = "dev.math.flashcards"
SOURCES = Path(__file__).parent


class Installation(BaseModel):
    build_dir: Path
    data_dir: Path
    bin_dir: Path

    @field_validator("data_dir", "bin_dir")
    @classmethod
    def absolute_directory(cls, value: Path) -> Path:
        if not value.is_absolute():
            raise ValueError("Installation directories must be absolute paths.")
        return value


class Bundle(BaseModel):
    resources: dict[str, str]


class TauriConfiguration(BaseModel):
    productName: str
    bundle: Bundle


class RendererResource(BaseModel):
    identity: str = Field(pattern="^[a-f0-9]{64}$")


def exec_argument(path: Path) -> str:
    # Exec quoting follows both desktop string escaping and argument escaping:
    # https://specifications.freedesktop.org/desktop-entry/latest/exec-variables.html
    escaped = str(path).replace("%", "%%")
    for character in ("\\", '"', "$", "`"):
        escaped = escaped.replace(character, "\\" + character)
    return '"' + escaped.replace("\\", "\\\\") + '"'


def publish(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".install-", dir=destination.parent
    ) as directory:
        temporary = Path(directory) / destination.name
        shutil.copy2(source, temporary)
        temporary.replace(destination)


def install(spec: Installation) -> Path:
    binary = spec.build_dir / "desktop"
    configuration = TauriConfiguration.model_validate_json(
        (SOURCES.parent / "src-tauri" / "tauri.conf.json").read_bytes()
    )
    resources: list[Path] = []
    # Tauri's resource map owns the packaged layout. The installer regenerates
    # only its interpreter pointer and active-renderer link for the new release.
    for destination in configuration.bundle.resources.values():
        if destination in {"runtime.txt", "active-assets.json"}:
            continue
        path = spec.build_dir / destination
        if destination.endswith("/"):
            if not path.is_dir():
                raise FileNotFoundError(f"Build the desktop resources first: {path}")
            resources.extend(
                sorted(
                    file
                    for file in path.rglob("*")
                    if file.is_file() and "__pycache__" not in file.parts
                )
            )
        else:
            resources.append(path)
    archive = spec.build_dir / "asset-sets"
    assets = RendererResource.model_validate_json(
        (spec.build_dir / "assets.json").read_bytes()
    )
    archived_assets = archive / (assets.identity + ".json")
    if not archived_assets.is_file():
        raise FileNotFoundError(f"Prepare renderer assets first: {archived_assets}")
    if not any(path.name == "tikzcd.lua" for path in resources):
        raise FileNotFoundError("Prepare the bundled TikZ renderer first.")
    for source in (binary, *resources):
        if not source.is_file():
            raise FileNotFoundError(f"Build the desktop app first: {source}")
    dependency_directories: list[str] = []
    for name in ("uv", "pandoc", "trash", "lualatex", "pdf2svg"):
        executable = shutil.which(name)
        if executable is None:
            raise FileNotFoundError(f"Required runtime command: {name}")
        dependency_directories.append(str(Path(executable).parent))

    application = spec.data_dir / "math-flashcards"
    releases = application / "releases"
    releases.mkdir(parents=True, exist_ok=True)
    release = Path(tempfile.mkdtemp(prefix="release-", dir=releases))
    active = application / "active"
    activated = False
    try:
        # Tauri resolves Linux resources beside the actual executable:
        # https://v2.tauri.app/develop/resources/
        installed_binary = release / "bin" / "desktop"
        publish(binary, installed_binary)
        resource_directory = release / "lib" / configuration.productName
        for source in resources:
            publish(source, resource_directory / source.relative_to(spec.build_dir))
        installed_script = resource_directory / "backend.py"
        python = subprocess.check_output(
            ["uv", "python", "find", "--script", str(installed_script)], text=True
        ).strip()
        environment = release / "environment"
        subprocess.run(["uv", "venv", "--python", python, str(environment)], check=True)
        # Sync at the final installed script path into the release-owned environment:
        # https://docs.astral.sh/uv/reference/cli/#uv-sync--active
        subprocess.run(
            [
                "uv",
                "sync",
                "--upgrade",
                "--active",
                "--compile-bytecode",
                "--script",
                str(installed_script),
            ],
            check=True,
            env=os.environ | {"VIRTUAL_ENV": str(environment)},
        )
        interpreter = environment / "bin" / "python3"
        (resource_directory / "runtime.txt").write_text(str(interpreter) + "\n")
        (resource_directory / "active-assets.json").symlink_to(
            active / "lib" / configuration.productName / "assets.json"
        )
        subprocess.run(
            [str(interpreter), "-I", "-c", "from ankdown.cli import RendererAssets"],
            check=True,
        )
        subprocess.run(
            [
                str(interpreter),
                "-I",
                "-c",
                "import sys; sys.path.insert(0, sys.argv[1]); import anki.collection, study.host, analysis",
                str(resource_directory),
            ],
            check=True,
        )
        validated = RendererResource.model_validate_json(
            subprocess.check_output(
                [str(interpreter), "-I", str(installed_script)],
                input='{"action":"assets"}\n',
                text=True,
            )
        )
        if validated.identity != assets.identity:
            raise ValueError(
                "The installed renderer assets do not match the prepared release."
            )
        if (
            archived_assets.read_bytes()
            != (resource_directory / "assets.json").read_bytes()
        ):
            raise ValueError(
                "The renderer archive does not match the prepared release."
            )

        release_launcher = release / "launch"
        release_launcher.write_text(
            (SOURCES / "launch.sh.in")
            .read_text()
            .replace(
                "@DEPENDENCY_PATH@",
                shlex.quote(":".join(dict.fromkeys(dependency_directories))),
            )
            .replace("@APPLICATION@", shlex.quote(str(installed_binary)))
        )
        release_launcher.chmod(0o755)
        dispatcher = release / "dispatch"
        dispatcher.write_text(
            (SOURCES / "dispatch.sh.in")
            .read_text()
            .replace("@APPLICATION@", shlex.quote(str(active / "launch")))
        )
        dispatcher.chmod(0o755)

        launcher = application / "launch"
        command = spec.bin_dir / "math-flashcards"
        entry = configparser.ConfigParser(interpolation=None)
        entry.optionxform = str
        entry.read(SOURCES / f"{APP_ID}.desktop.in")
        entry["Desktop Entry"]["Exec"] = exec_argument(command)
        entry["Desktop Entry"]["TryExec"] = str(command)
        applications = spec.data_dir / "applications"
        applications.mkdir(parents=True, exist_ok=True)
        destination = applications / f"{APP_ID}.desktop"
        staged_entry = release / destination.name
        with staged_entry.open("w") as handle:
            entry.write(handle, space_around_delimiters=False)
        subprocess.run(["desktop-file-validate", str(staged_entry)], check=True)
        publish(
            SOURCES.parent / "src-tauri" / "icons" / "128x128.png", release / "icon.png"
        )

        # Stable entry points refer to the active release. Candidate preparation
        # and validation complete before any installed entry point changes.
        publish(dispatcher, launcher)
        spec.bin_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            prefix=".command-", dir=spec.bin_dir
        ) as directory:
            temporary = Path(directory) / "math-flashcards"
            temporary.symlink_to(launcher)
            temporary.replace(command)
        publish(staged_entry, destination)
        icon = (
            spec.data_dir / "icons" / "hicolor" / "128x128" / "apps" / f"{APP_ID}.png"
        )
        icon.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".icon-", dir=icon.parent) as directory:
            temporary = Path(directory) / icon.name
            temporary.symlink_to(active / "icon.png")
            temporary.replace(icon)
        subprocess.run(["update-desktop-database", str(applications)], check=True)
        with tempfile.TemporaryDirectory(
            prefix=".activation-", dir=application
        ) as directory:
            pointer = Path(directory) / "active"
            pointer.symlink_to(
                release.relative_to(application), target_is_directory=True
            )
            pointer.replace(active)
            activated = True
        return destination
    finally:
        if not activated:
            subprocess.run(["trash", str(release)], check=True)


app = cyclopts.App()


@app.default
def main(
    build_dir: Path, *, data_dir: Path | None = None, bin_dir: Path | None = None
) -> None:
    """Install or update a built native application and its desktop entry.

    build_dir: Tauri release directory containing the executable and resources.
    data_dir: Override XDG_DATA_HOME for an isolated installation.
    bin_dir: Override the standard ~/.local/bin command directory.
    """
    spec = Installation(
        build_dir=build_dir.resolve(strict=True),
        data_dir=user_data_path() if data_dir is None else data_dir,
        bin_dir=Path.home() / ".local" / "bin" if bin_dir is None else bin_dir,
    )
    print(install(spec))


if __name__ == "__main__":
    app()
