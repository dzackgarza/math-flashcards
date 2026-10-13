# /// script
# requires-python = ">=3.12"
# dependencies = ["mss==10.1.0"]
# ///
"""Capture the built native WebKit app in an isolated X11 display."""

import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import mss
import mss.tools


def main() -> None:
    desktop = Path(__file__).resolve().parents[1]
    artifacts = desktop / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="flashcards-native-") as directory:
        root = Path(directory)
        (root / "decks" / "Qual Basics").mkdir(parents=True)
        shutil.copyfile(
            desktop.parent / "decks" / "Qual Basics" / "Special Angles.md",
            root / "decks" / "Qual Basics" / "Special Angles.md",
        )
        with (artifacts / "native.log").open("w") as log:
            process = subprocess.Popen(
                [str(desktop / "src-tauri" / "target" / "release" / "desktop")],
                stdout=log,
                stderr=log,
                env=os.environ
                | {
                    "XDG_CONFIG_HOME": str(root / "config"),
                    "XDG_CACHE_HOME": str(root / "cache"),
                    "XDG_DATA_HOME": str(root / "data"),
                },
            )
            try:
                window = subprocess.check_output(
                    [
                        "xdotool",
                        "search",
                        "--sync",
                        "--onlyvisible",
                        "--pid",
                        str(process.pid),
                        "--name",
                        "Math Flashcards",
                    ],
                    text=True,
                ).splitlines()[0]
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
                assert package.is_file(), (artifacts / "native.log").read_text()
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
                print("Native app opened, rendered a deck, and generated its APKG.")
            finally:
                process.terminate()
                process.wait(timeout=10)


if __name__ == "__main__":
    main()
