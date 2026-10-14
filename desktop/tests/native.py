# /// script
# requires-python = ">=3.12"
# dependencies = ["mss==10.1.0", "cyclopts==4.15.0"]
# ///
"""Capture the built native WebKit app in an isolated X11 display."""

import json
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
        (root / "decks" / "Basics").mkdir(parents=True)
        shutil.copyfile(
            desktop.parent / "decks" / "Basics" / "Precalculus.md",
            root / "decks" / "Basics" / "Precalculus.md",
        )
        with (artifacts / "native.log").open("w") as log:
            uv_cache = subprocess.check_output(
                ["uv", "cache", "dir"], text=True
            ).strip()
            command = [str(desktop / "src-tauri" / "target" / "release" / "desktop")]
            if entry is not None:
                command = ["gio", "launch", str(entry.resolve(strict=True))]
            # GTK prefers WAYLAND_DISPLAY over Xvfb's DISPLAY; GDK_BACKEND selects X11:
            # https://docs.gtk.org/gtk3/running.html#gdk_backend
            runtime_environment = os.environ | {
                "GDK_BACKEND": "x11",
                "XDG_CONFIG_HOME": str(environment / "config"),
                "XDG_CACHE_HOME": str(environment / "cache"),
                "XDG_DATA_HOME": str(environment / "data"),
                "UV_CACHE_DIR": uv_cache,
            }
            process = subprocess.Popen(
                command,
                stdout=log,
                stderr=log,
                env=runtime_environment,
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
                preferences_path = (
                    environment / "config" / "dev.math.flashcards" / "preferences.json"
                )
                for _ in range(120):
                    if preferences_path.is_file():
                        break
                    time.sleep(0.25)
                assert json.loads(preferences_path.read_text())["workspace"] == str(
                    desktop.parent
                )
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
                        "127",
                        "60",
                        "click",
                        "1",
                        "sleep",
                        "0.5",
                        "mousemove",
                        "--window",
                        window,
                        "230",
                        "140",
                        "click",
                        "1",
                        "key",
                        "ctrl+a",
                        "type",
                        "--clearmodifiers",
                        "--delay",
                        "50",
                        str(root),
                    ],
                    check=True,
                )
                time.sleep(0.5)
                subprocess.run(["xdotool", "key", "Return"], check=True)
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
                        "59",
                        "147",
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
                        "80",
                        "177",
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
                        "1403",
                        "28",
                        "click",
                        "1",
                        "sleep",
                        "0.5",
                        "mousemove",
                        "--window",
                        window,
                        "1280",
                        "74",
                        "click",
                        "1",
                    ],
                    check=True,
                )
                package = root / "apkg" / "Basics__Precalculus.apkg"
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
                assert json.loads(preferences_path.read_text())["workspace"] == str(
                    root
                )
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
                # Bursts of build writes must leave the app responsive and bounded.
                # xdotool owns window PID lookup; ps observes actual native children.
                app_pid = subprocess.check_output(
                    ["xdotool", "getwindowpid", window], text=True
                ).strip()
                build_directory = root / "desktop" / "src-tauri" / "target"
                build_directory.mkdir(parents=True)
                for index in range(40):
                    (build_directory / f"artifact-{index}").write_text("build output")
                    processes = subprocess.check_output(
                        ["ps", "-eo", "ppid=,comm="], text=True
                    )
                    backend_children = [
                        line
                        for line in processes.splitlines()
                        if line.split()[0] == app_pid
                        and line.split()[1].startswith(("uv", "python"))
                    ]
                    assert len(backend_children) <= 2
                    time.sleep(0.05)
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
                target = root / "decks" / "Native Target.md"
                target.write_text('---\ntitle: "Native::Target"\n---\n\n')
                time.sleep(2)
                time.sleep(4)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb,
                        shot.size,
                        output=str(artifacts / "native-organization-before.png"),
                    )
                subprocess.run(
                    [
                        "xdotool",
                        "mousemove",
                        "--window",
                        window,
                        "423",
                        "153",
                        "mousedown",
                        "1",
                    ],
                    check=True,
                )
                time.sleep(0.2)
                subprocess.run(
                    ["xdotool", "mousemove", "--window", window, "440", "170"],
                    check=True,
                )
                time.sleep(0.2)
                subprocess.run(
                    ["xdotool", "mousemove", "--window", window, "105", "204"],
                    check=True,
                )
                time.sleep(0.5)
                subprocess.run(
                    ["xdotool", "mousemove", "--window", window, "100", "208"],
                    check=True,
                )
                time.sleep(0.5)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb, shot.size, output=str(artifacts / "native-drag.png")
                    )
                subprocess.run(["xdotool", "mouseup", "1"], check=True)
                for _ in range(120):
                    if "card-id" in target.read_text():
                        break
                    time.sleep(0.25)
                assert r"$\sin(\pi/6) = \cdots$" in target.read_text(), (
                    artifacts / "native.log"
                ).read_text()
                assert (
                    r"$\sin(\pi/6) = \cdots$"
                    not in (root / "decks" / "Basics" / "Precalculus.md").read_text()
                )
                time.sleep(2)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb,
                        shot.size,
                        output=str(artifacts / "native-organized.png"),
                    )
                subprocess.run(["xdotool", "windowclose", window], check=True)
                window = None
                process.wait(timeout=10)
                log.write("\nWorkspace restart\n")
                log.flush()
                process = subprocess.Popen(
                    command, stdout=log, stderr=log, env=runtime_environment
                )
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
                for _ in range(120):
                    restarted_log = (
                        (artifacts / "native.log")
                        .read_text()
                        .split("Workspace restart\n")[-1]
                    )
                    if "Backend result: list exit status: 0" in restarted_log:
                        break
                    time.sleep(0.25)
                assert "Backend result: list exit status: 0" in restarted_log
                time.sleep(1)
                with mss.mss() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb,
                        shot.size,
                        output=str(artifacts / "native-restored-workspace.png"),
                    )
                print(
                    "Native app opens the default workspace, saves workspace changes, and restores them after restart."
                )
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
