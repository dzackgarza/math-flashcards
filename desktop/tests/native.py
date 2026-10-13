# /// script
# requires-python = ">=3.12"
# dependencies = ["mss==10.1.0", "cyclopts==4.15.0"]
# ///
"""Capture the built native WebKit app in an isolated X11 display."""

import os
import shutil
import subprocess
import tempfile
import time
import zipfile
from pathlib import Path

import cyclopts
import mss
import mss.tools


def main(*, entry: Path | None = None) -> None:
    """Exercise a built app, or launch an installed desktop entry through Gio."""
    desktop = Path(__file__).resolve().parents[1]
    artifacts = desktop / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="flashcards-native-") as directory:
        environment = Path(directory)
        root = environment / "workspace"
        (root / "decks" / "Qual Basics").mkdir(parents=True)
        shutil.copyfile(
            desktop.parent / "decks" / "Qual Basics" / "Special Angles.md",
            root / "decks" / "Qual Basics" / "Special Angles.md",
        )
        with (artifacts / "native.log").open("w") as log:
            uv_cache = subprocess.check_output(
                ["uv", "cache", "dir"], text=True
            ).strip()
            command = [str(desktop / "src-tauri" / "target" / "release" / "desktop")]
            if entry is not None:
                command = ["gio", "launch", str(entry.resolve(strict=True))]
            process = subprocess.Popen(
                command,
                stdout=log,
                stderr=log,
                env=os.environ
                | {
                    "XDG_CONFIG_HOME": str(environment / "config"),
                    "XDG_CACHE_HOME": str(environment / "cache"),
                    "XDG_DATA_HOME": str(environment / "data"),
                    "UV_CACHE_DIR": uv_cache,
                },
            )
            window: str | None = None
            try:
                window = subprocess.check_output(
                    [
                        "xdotool",
                        "search",
                        "--sync",
                        "--onlyvisible",
                        "--name",
                        "Math Flashcards",
                    ],
                    text=True,
                    timeout=30,
                ).splitlines()[0]
                wm_class = subprocess.check_output(
                    ["xprop", "-id", window, "WM_CLASS"], text=True
                )
                print(wm_class, flush=True)
                assert '"desktop"' in wm_class
                print("Native window:", window, flush=True)
                time.sleep(2)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb, shot.size, output=str(artifacts / "native-empty.png")
                    )
                # xdotool is the native input owner: https://www.semicomplete.com/projects/xdotool/
                subprocess.run(
                    [
                        "xdotool",
                        "mousemove",
                        "--window",
                        window,
                        "220",
                        "156",
                        "click",
                        "1",
                        "key",
                        "ctrl+a",
                        "type",
                        "--clearmodifiers",
                        str(root),
                    ],
                    check=True,
                )
                subprocess.run(
                    [
                        "xdotool",
                        "mousemove",
                        "--window",
                        window,
                        "1170",
                        "156",
                        "click",
                        "1",
                    ],
                    check=True,
                )
                time.sleep(3)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb,
                        shot.size,
                        output=str(artifacts / "native-workspace.png"),
                    )
                subprocess.run(
                    [
                        "xdotool",
                        "mousemove",
                        "--window",
                        window,
                        "105",
                        "323",
                        "click",
                        "1",
                    ],
                    check=True,
                )
                subprocess.run(
                    [
                        "xdotool",
                        "mousemove",
                        "--window",
                        window,
                        "120",
                        "354",
                        "click",
                        "1",
                    ],
                    check=True,
                )
                time.sleep(4)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb, shot.size, output=str(artifacts / "native-front.png")
                    )
                subprocess.run(
                    [
                        "xdotool",
                        "mousemove",
                        "--window",
                        window,
                        "830",
                        "900",
                        "click",
                        "1",
                    ],
                    check=True,
                )
                time.sleep(1)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb, shot.size, output=str(artifacts / "native-back.png")
                    )
                subprocess.run(
                    [
                        "xdotool",
                        "mousemove",
                        "--window",
                        window,
                        "658",
                        "304",
                        "click",
                        "1",
                    ],
                    check=True,
                )
                package = root / "apkg" / "Qual Basics__Special Angles.apkg"
                for _ in range(120):
                    if package.is_file():
                        break
                    time.sleep(0.25)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb, shot.size, output=str(artifacts / "native-last.png")
                    )
                assert package.is_file(), (artifacts / "native.log").read_text()
                assert zipfile.is_zipfile(package)
                preferences_path = (
                    environment / "config" / "dev.math.flashcards" / "preferences.json"
                )
                assert preferences_path.is_file()
                time.sleep(1)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb,
                        shot.size,
                        output=str(artifacts / "native-generated.png"),
                    )
                package.write_bytes(b"external package edit")
                time.sleep(2)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb,
                        shot.size,
                        output=str(artifacts / "native-unsynced.png"),
                    )
                print("Native app opened, rendered a deck, and generated its APKG.")
            finally:
                if window is not None:
                    subprocess.run(["xdotool", "windowclose", window], check=True)
                else:
                    process.terminate()
                process.wait(timeout=10)


if __name__ == "__main__":
    app = cyclopts.App()
    app.default(main)
    app()
