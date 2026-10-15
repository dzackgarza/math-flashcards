# /// script
# requires-python = ">=3.12"
# ///
"""Check installation and update with real build files and desktop tools."""

import configparser
import subprocess
import tempfile
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
        for name in ("backend.py", "paired-cards.lua"):
            assert (
                data / "math-flashcards" / "lib" / "Math Flashcards" / name
            ).read_bytes() == (
                desktop / "src-tauri" / "target" / "release" / name
            ).read_bytes()
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
    print(
        "Installation and update preserve the native build and refresh the validated desktop entry."
    )


if __name__ == "__main__":
    main()
