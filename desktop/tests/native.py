# /// script
# requires-python = ">=3.12"
# dependencies = ["mss", "cyclopts", "psutil"]
# ///
"""Capture the built native WebKit app in an isolated X11 display."""

import json
import os
import re
import shutil
import subprocess
import tempfile
import time
import zipfile
from contextlib import suppress
from pathlib import Path

import cyclopts
import mss
import mss.tools
import psutil
from installation import prepare_asset_update


def wait_for_text(text: str) -> None:
    """Wait for rendered native state before sending the next input."""
    # Tesseract CLI: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html
    deadline = time.monotonic() + 30
    observed = ""
    with mss.MSS() as screen:
        while time.monotonic() < deadline:
            shot = screen.grab({"left": 250, "top": 0, "width": 1190, "height": 200})
            result = subprocess.run(
                ["tesseract", "stdin", "stdout", "--psm", "6"],
                input=mss.tools.to_png(shot.rgb, shot.size),
                capture_output=True,
                check=True,
            )
            observed = " ".join(result.stdout.decode().split())
            if text in observed:
                return
            time.sleep(0.1)
    raise AssertionError(f"Expected native text {text!r}; observed {observed!r}")


def command_action(label: str) -> None:
    subprocess.run(
        ["xdotool", "key", "ctrl+k", "sleep", "0.3", "type", "--clearmodifiers", label],
        check=True,
    )
    time.sleep(0.5)
    subprocess.run(["xdotool", "mousemove", "600", "190", "click", "1"], check=True)


def assert_package_assets(package: Path, asset_file: Path) -> None:
    expected = json.loads(asset_file.read_text())
    with zipfile.ZipFile(package) as archive:
        media = json.loads(archive.read("media"))
        name = next(
            key for key, value in media.items() if value == "_ankdown_macros.js"
        )
        stmaryrd, assignment = (
            archive.read(name).decode().split("\nwindow.ANKDOWN_MACROS = ")
        )
        assert stmaryrd == expected["stmaryrd"]
        assert json.loads(assignment.removesuffix(";")) == expected["macros"]


def close_native(window: str, launcher: subprocess.Popen[bytes]) -> None:
    """Wait for this window's renderer processes before removing their cache."""
    pid = int(subprocess.check_output(["xdotool", "getwindowpid", window], text=True))
    native = psutil.Process(pid)
    # Capture descendants before closing their parent, as in psutil's recipe:
    # https://psutil.io/recipes/#controlling-processes
    children = native.children(recursive=True)
    subprocess.run(["xdotool", "windowclose", window], check=True)
    _, alive = psutil.wait_procs([native, *children], timeout=10)
    for child in alive:
        with suppress(psutil.NoSuchProcess):
            if child.status() != psutil.STATUS_ZOMBIE:
                child.terminate()
    _, alive = psutil.wait_procs(alive, timeout=10)
    for child in alive:
        with suppress(psutil.NoSuchProcess):
            assert child.status() == psutil.STATUS_ZOMBIE
    launcher.wait(timeout=10)


def main(
    *, entry: Path | None = None, offline: bool = False, updates: bool = False
) -> None:
    """Exercise a built app, or launch an installed desktop entry through Gio."""
    desktop = Path(__file__).resolve().parents[1]
    artifacts = desktop / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    trace = artifacts / "native-offline.trace"
    if offline:
        trace.write_text("")
    with tempfile.TemporaryDirectory(prefix="flashcards-native-") as directory:
        environment = Path(directory)
        build = desktop / "src-tauri" / "target" / "release"
        if updates:
            if entry is not None:
                raise ValueError("The update scenario owns its temporary installation.")
            installation = environment / "installation"
            install_arguments = [
                "uv",
                "run",
                "--upgrade",
                str(desktop / "linux" / "install.py"),
                str(build),
                "--data-dir",
                str(installation),
                "--bin-dir",
                str(environment / "commands"),
            ]
            subprocess.run(install_arguments, check=True)
            entry = installation / "applications" / "dev.math.flashcards.desktop"
            resources = (
                installation / "math-flashcards" / "active" / "lib" / "Math Flashcards"
            ).resolve(strict=True)
            candidate = environment / "next build"
            prepare_asset_update(build, candidate, resources)
        root = environment / "workspace"
        (root / "Analysis").mkdir(parents=True)
        shutil.copyfile(
            desktop.parent / "decks" / "Analysis" / "Precalculus.md",
            root / "Analysis" / "Precalculus.md",
        )
        with (artifacts / "native.log").open("w") as log:
            uv_cache = subprocess.check_output(
                ["uv", "cache", "dir"], text=True
            ).strip()
            command = [str(desktop / "src-tauri" / "target" / "release" / "desktop")]
            if entry is not None:
                command = ["gio", "launch", str(entry.resolve(strict=True))]
            if offline:
                command = [
                    "unshare",
                    "--user",
                    "--map-root-user",
                    "--net",
                    "strace",
                    "-f",
                    "-A",
                    "-s",
                    "4096",
                    "-e",
                    "trace=process,network",
                    "-o",
                    str(trace),
                    *command,
                ]
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
                    desktop.parent / "decks"
                )
                with mss.MSS() as screen:
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
                with mss.MSS() as screen:
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
                with mss.MSS() as screen:
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
                        "1110",
                        "190",
                        "click",
                        "1",
                        "key",
                        "ctrl+End",
                        "Return",
                        "type",
                        "--clearmodifiers",
                        "--delay",
                        "10",
                        "Native input $x^2$",
                    ],
                    check=True,
                )
                subprocess.run(["xdotool", "key", "ctrl+s"], check=True)
                source_path = root / "Analysis" / "Precalculus.md"
                for _ in range(120):
                    if "Native input $x^2$" in source_path.read_text():
                        break
                    time.sleep(0.25)
                assert "Native input $x^2$" in source_path.read_text(), (
                    artifacts / "native.log"
                ).read_text()
                wait_for_text("not in the Anki package")
                command_action("Update this Anki package")
                package = root / "apkg" / "Analysis__Precalculus.apkg"
                for _ in range(120):
                    if package.is_file():
                        break
                    time.sleep(0.25)
                with mss.MSS() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb, shot.size, output=str(artifacts / "native-last.png")
                    )
                assert package.is_file(), (artifacts / "native.log").read_text()
                assert zipfile.is_zipfile(package)
                if updates:
                    assert_package_assets(package, resources / "assets.json")
                    update_arguments = install_arguments.copy()
                    update_arguments[4] = str(candidate)
                    subprocess.run(update_arguments, check=True)
                    command_action("Refresh workspace")
                    wait_for_text("Renderer update ready")
                    with mss.MSS() as screen:
                        shot = screen.grab(
                            {"left": 0, "top": 0, "width": 1440, "height": 1000}
                        )
                        mss.tools.to_png(
                            shot.rgb,
                            shot.size,
                            output=str(artifacts / "native-update-notice.png"),
                        )
                    package.write_bytes(b"external package edit")
                    source_path.write_text(
                        source_path.read_text().replace(
                            "Native input $x^2$", "Native input $x^2$ after update"
                        )
                    )
                    wait_for_text("not in the Anki package")
                    command_action("Update this Anki package")
                    for _ in range(120):
                        if zipfile.is_zipfile(package):
                            break
                        time.sleep(0.25)
                    assert zipfile.is_zipfile(package), (
                        artifacts / "native.log"
                    ).read_text()
                    assert_package_assets(package, resources / "assets.json")
                    close_native(window, process)
                    window = None
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
                    time.sleep(3)
                    command_action("Precalculus")
                    time.sleep(3)
                    package.write_bytes(b"external package edit")
                    source_path.write_text(
                        source_path.read_text().replace("after update", "after restart")
                    )
                    wait_for_text("not in the Anki package")
                    command_action("Update this Anki package")
                    for _ in range(120):
                        if zipfile.is_zipfile(package):
                            break
                        time.sleep(0.25)
                    assert zipfile.is_zipfile(package), (
                        artifacts / "native.log"
                    ).read_text()
                    assert_package_assets(package, candidate / "assets.json")
                    with mss.MSS() as screen:
                        shot = screen.grab(
                            {"left": 0, "top": 0, "width": 1440, "height": 1000}
                        )
                        mss.tools.to_png(
                            shot.rgb,
                            shot.size,
                            output=str(artifacts / "native-updated-session.png"),
                        )
                assert json.loads(preferences_path.read_text())["workspace"] == str(
                    root
                )
                time.sleep(1)
                with mss.MSS() as screen:
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
                with mss.MSS() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb,
                        shot.size,
                        output=str(artifacts / "native-unsynced.png"),
                    )
                target = root / "Native Target.md"
                target.write_text('---\ntitle: "Native::Target"\n---\n\n')
                time.sleep(2)
                time.sleep(4)
                with mss.MSS() as screen:
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
                with mss.MSS() as screen:
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
                    not in (root / "Analysis" / "Precalculus.md").read_text()
                )
                time.sleep(2)
                with mss.MSS() as screen:
                    shot = screen.grab(
                        {"left": 0, "top": 0, "width": 1440, "height": 1000}
                    )
                    mss.tools.to_png(
                        shot.rgb,
                        shot.size,
                        output=str(artifacts / "native-organized.png"),
                    )
                close_native(window, process)
                window = None
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
                    if "Backend result: manifest exit status: 0" in restarted_log:
                        break
                    time.sleep(0.25)
                assert "Backend result: manifest exit status: 0" in restarted_log
                time.sleep(1)
                with mss.MSS() as screen:
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
                    close_native(window, process)
                else:
                    process.terminate()
                process.wait(timeout=10)
    if offline:
        events = trace.read_text().splitlines()
        attempted = [
            match.group(1)
            for event in events
            if (match := re.search(r'execve\("([^"]+)"', event))
        ]
        assert any(Path(program).name == "desktop" for program in attempted)
        assert any(Path(program).name == "python3" for program in attempted)
        assert not any(Path(program).name in {"uv", "git"} for program in attempted)
        assert not any(
            "connect(" in event and ("AF_INET," in event or "AF_INET6," in event)
            for event in events
        )


if __name__ == "__main__":
    app = cyclopts.App()
    app.default(main)
    app()
