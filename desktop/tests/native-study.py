# /// script
# requires-python = ">=3.12"
# dependencies = ["selenium", "psutil"]
# ///
"""Open and restart Study through the built app's actual native command."""

import json
import os
import shutil
import sqlite3
import tempfile
from contextlib import closing, suppress
from hashlib import file_digest
from pathlib import Path

import psutil
from evidence import evidence
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.webkitgtk.options import Options
from selenium.webdriver.webkitgtk.service import Service


def main(artifacts: Path) -> None:
    desktop = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="flashcards-native-study-") as temporary:
        root = Path(temporary)
        workspace = root / "workspace"
        shutil.copytree(desktop / "tests" / "fixtures" / "study", workspace)
        preferences = root / "config" / "dev.math.flashcards" / "preferences.json"
        preferences.parent.mkdir(parents=True)
        preferences.write_text(json.dumps({"workspace": str(workspace)}))
        environment = os.environ | {
            "TAURI_WEBVIEW_AUTOMATION": "true",
            "GDK_BACKEND": "x11",
            "XDG_CONFIG_HOME": str(root / "config"),
            "XDG_CACHE_HOME": str(root / "cache"),
            "XDG_DATA_HOME": str(root / "data"),
            "XDG_STATE_HOME": str(root / "state"),
        }
        options = Options()
        # Tauri's supported WebDriver path launches the release executable:
        # https://v2.tauri.app/develop/tests/webdriver/example/selenium/
        options.capabilities.pop("browserName")
        options.binary_location = str(desktop / "src-tauri/target/release/desktop")
        with Path(options.binary_location).open("rb") as executable:
            (artifacts / "executable.sha256").write_text(
                file_digest(executable, "sha256").hexdigest() + "\n"
            )
        with (artifacts / "webkit.log").open("w") as log:
            service = Service(
                executable_path="/bin/WebKitWebDriver", env=environment, log_output=log
            )
            service.start()
            driver: webdriver.Remote | None = None
            try:
                driver = webdriver.Remote(
                    command_executor=service.service_url, options=options
                )
                driver.set_script_timeout(30)
                WebDriverWait(driver, 30).until(
                    lambda window: window.execute_script(
                        "return typeof window.__TAURI_INTERNALS__?.invoke === 'function'"
                    )
                )
                payload = json.dumps({"action": "study-open", "workspace": str(workspace)})
                script = """
                    const done = arguments[arguments.length - 1];
                    window.__TAURI_INTERNALS__.invoke('request', {payload: arguments[0]})
                      .then(value => done({ok: true, result: JSON.parse(value)}))
                      .catch(error => done({ok: false, error: String(error)}));
                """
                first = driver.execute_async_script(script, payload)
                assert first["ok"], first
                opened = first["result"]
                assert opened["state"] == "Open", opened
                native_log = root / "state" / "math-flashcards" / "diagnostics" / "native" / "native.log"
                assert native_log.is_file(), "Native request diagnostics were not retained in XDG state"
                events = native_log.read_text()
                assert "event=app-start" in events, events
                assert "event=request-completed action=study-open outcome=ok" in events, events
                release = json.loads((desktop / "package.json").read_text())["version"]
                assert "elapsed_ms=" in events and f"release={release}" in events, events
                store = Path(opened["store"])
                assert store.parent == root / "data" / "math-flashcards" / "study"
                with closing(sqlite3.connect(opened["record"])) as record:
                    writers = record.execute("select count(*) from writer").fetchone()[0]
                assert service.process is not None
                hosts = [
                    child
                    for child in psutil.Process(service.process.pid).children(recursive=True)
                    if "study-host" in child.cmdline()
                ]
                assert len(hosts) == 1, hosts
                again = driver.execute_async_script(script, payload)
                assert again == first, again
                assert hosts[0].is_running()
                # A real process exit must restart the native bridge's host and reopen
                # the same store, rather than leaving a dead route or creating data.
                hosts[0].terminate()
                # The native parent reaps the child on the next request. psutil.wait
                # on a non-child waits for disappearance, not merely process exit:
                # https://psutil.io/api/#psutil.Process.wait
                WebDriverWait(driver, 10).until(
                    lambda _: not hosts[0].is_running()
                    or hosts[0].status() == psutil.STATUS_ZOMBIE
                )
                restarted = driver.execute_async_script(script, payload)
                assert restarted == first, restarted
                assert not hosts[0].is_running()
                failure = driver.execute_async_script(script, json.dumps({
                    "action": "study-attach",
                    "workspace": str(workspace),
                    "choice": {"kind": "existing", "store": "00000000-0000-0000-0000-000000000000"},
                }))
                assert not failure["ok"], failure
                assert "UnknownStore" in failure["error"], failure
                events = native_log.read_text()
                assert "event=study-host-reaped" in events, events
                assert "event=request-completed action=study-attach outcome=error" in events, events
                assert "UnknownStore" in events, events
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert record.execute("select count(*) from writer").fetchone()[0] == writers + 1
                    assert record.execute("select kind from store_event").fetchall() == [("created",)]
                children = psutil.Process(service.process.pid).children(recursive=True)
                # WebDriver session deletion force-exits its browser process.
                # Close through Tauri before releasing the automation session:
                # https://github.com/WebKit/WebKit/blob/main/Source/WebDriver/glib/SessionHostGlib.cpp
                driver.execute_script("""
                    setTimeout(() => window.__TAURI_INTERNALS__.invoke(
                        'plugin:window|destroy', {label: 'main'}), 100);
                """)
                WebDriverWait(driver, 10).until(
                    lambda _: "event=app-exit" in native_log.read_text()
                )
                driver.quit()
                driver = None
                _, alive = psutil.wait_procs(children, timeout=10)
                assert all(child.status() == psutil.STATUS_ZOMBIE for child in alive), alive
                assert "event=app-exit" in native_log.read_text()
            finally:
                assert service.process is not None
                children = psutil.Process(service.process.pid).children(recursive=True)
                if driver is not None:
                    driver.quit()
                _, alive = psutil.wait_procs(children, timeout=10)
                for child in alive:
                    with suppress(psutil.NoSuchProcess):
                        if child.status() != psutil.STATUS_ZOMBIE:
                            child.terminate()
                psutil.wait_procs(alive, timeout=10)
                service.stop()
                state = root / "state"
                if state.is_dir():
                    shutil.copytree(state, artifacts / "application-state")


if __name__ == "__main__":
    with evidence("native-study", Path(__file__).parent / "fixtures" / "study") as artifacts:
        main(artifacts)
