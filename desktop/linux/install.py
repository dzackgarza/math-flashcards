# /// script
# requires-python = ">=3.12"
# dependencies = ["cyclopts==4.15.0", "pydantic==2.12.5"]
# ///
"""Install the native app and its desktop entry in user directories."""

import configparser
import json
import os
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path

import cyclopts
from pydantic import BaseModel, field_validator

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


class TauriConfiguration(BaseModel):
    productName: str


def data_home() -> Path:
    # The standard defines unset, empty and relative values:
    # https://specifications.freedesktop.org/basedir/latest/
    value = os.environ.get("XDG_DATA_HOME")
    if value and Path(value).is_absolute():
        return Path(value)
    return Path.home() / ".local" / "share"


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
    resources = [spec.build_dir / name for name in ("backend.py", "paired-cards.lua")]
    for source in (binary, *resources):
        if not source.is_file():
            raise FileNotFoundError(f"Build the desktop app first: {source}")
    dependency_directories: list[str] = []
    for name in ("uv", "pandoc"):
        executable = shutil.which(name)
        if executable is None:
            raise FileNotFoundError(f"Required runtime command: {name}")
        dependency_directories.append(str(Path(executable).parent))

    application = spec.data_dir / "math-flashcards"
    # Tauri's Linux resources live beside bin/ in lib/<runtime application name>:
    # https://v2.tauri.app/develop/resources/
    installed_binary = application / "bin" / "desktop"
    configuration = TauriConfiguration.model_validate(
        json.loads((SOURCES.parent / "src-tauri" / "tauri.conf.json").read_text())
    )
    publish(binary, installed_binary)
    for source in resources:
        publish(source, application / "lib" / configuration.productName / source.name)

    application.mkdir(parents=True, exist_ok=True)
    launcher = application / "launch"
    contents = (
        (SOURCES / "launch.sh.in")
        .read_text()
        .replace(
            "@DEPENDENCY_PATH@",
            shlex.quote(":".join(dict.fromkeys(dependency_directories))),
        )
        .replace("@APPLICATION@", shlex.quote(str(installed_binary)))
    )
    with tempfile.TemporaryDirectory(prefix=".launcher-", dir=application) as directory:
        temporary = Path(directory) / "launch"
        temporary.write_text(contents)
        temporary.chmod(0o755)
        temporary.replace(launcher)
    spec.bin_dir.mkdir(parents=True, exist_ok=True)
    command = spec.bin_dir / "math-flashcards"
    with tempfile.TemporaryDirectory(prefix=".command-", dir=spec.bin_dir) as directory:
        temporary = Path(directory) / "math-flashcards"
        temporary.symlink_to(launcher)
        temporary.replace(command)

    entry = configparser.ConfigParser(interpolation=None)
    entry.optionxform = str
    entry.read(SOURCES / f"{APP_ID}.desktop.in")
    entry["Desktop Entry"]["Exec"] = exec_argument(command)
    entry["Desktop Entry"]["TryExec"] = str(command)
    applications = spec.data_dir / "applications"
    applications.mkdir(parents=True, exist_ok=True)
    destination = applications / f"{APP_ID}.desktop"
    with tempfile.TemporaryDirectory(prefix=".entry-", dir=applications) as directory:
        temporary = Path(directory) / destination.name
        with temporary.open("w") as handle:
            entry.write(handle, space_around_delimiters=False)
        subprocess.run(["desktop-file-validate", str(temporary)], check=True)
        temporary.replace(destination)
    icon = SOURCES.parent / "src-tauri" / "icons" / "128x128.png"
    publish(
        icon, spec.data_dir / "icons" / "hicolor" / "128x128" / "apps" / f"{APP_ID}.png"
    )
    subprocess.run(["update-desktop-database", str(applications)], check=True)
    return destination


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
        data_dir=data_home() if data_dir is None else data_dir,
        bin_dir=Path.home() / ".local" / "bin" if bin_dir is None else bin_dir,
    )
    print(install(spec))


if __name__ == "__main__":
    app()
