# /// script
# requires-python = ">=3.12"
# dependencies = ["selenium", "psutil", "send2trash", "python-xlib"]
# ///
"""Open and restart Study through the built app's actual native command."""

import json
import os
import shutil
import sqlite3
import subprocess
import tempfile
from contextlib import closing, suppress
from hashlib import file_digest
from pathlib import Path

import psutil
from evidence import evidence
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.webkitgtk.options import Options
from selenium.webdriver.webkitgtk.service import Service
from send2trash import send2trash
from Xlib import X, display, protocol


def main(artifacts: Path) -> None:
    desktop = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="flashcards-native-study-") as temporary:
        root = Path(temporary) / "home"
        root.mkdir()
        workspace = Path(temporary) / "workspace"
        shutil.copytree(desktop / "tests" / "fixtures" / "study", workspace)
        preferences = root / "config" / "dev.math.flashcards" / "preferences.json"
        preferences.parent.mkdir(parents=True)
        preferences.write_text(json.dumps({"workspace": str(workspace)}))
        environment = os.environ | {
            "HOME": str(root),
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
                wait = WebDriverWait(driver, 30)
                wait.until(
                    conditions.text_to_be_present_in_element(
                        (By.CSS_SELECTOR, '[role="status"][aria-label="Study"]'),
                        "Study cards ready",
                    )
                )
                payload = json.dumps(
                    {"action": "study-open", "workspace": str(workspace)}
                )
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
                native_log = (
                    root
                    / "state"
                    / "math-flashcards"
                    / "diagnostics"
                    / "native"
                    / "native.log"
                )
                assert native_log.is_file(), (
                    "Native request diagnostics were not retained in XDG state"
                )
                events = native_log.read_text()
                assert "event=app-start" in events, events
                assert (
                    "event=request-completed action=study-open outcome=ok" in events
                ), events
                release = json.loads((desktop / "package.json").read_text())["version"]
                assert "elapsed_ms=" in events and f"release={release}" in events, (
                    events
                )
                store = Path(opened["store"])
                assert store.parent == root / "data" / "math-flashcards" / "study"
                with closing(sqlite3.connect(opened["record"])) as record:
                    writers = record.execute("select count(*) from writer").fetchone()[
                        0
                    ]
                assert service.process is not None
                hosts = [
                    child
                    for child in psutil.Process(service.process.pid).children(
                        recursive=True
                    )
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
                    lambda _: (
                        not hosts[0].is_running()
                        or hosts[0].status() == psutil.STATUS_ZOMBIE
                    )
                )
                restarted = driver.execute_async_script(script, payload)
                assert restarted == first, restarted
                assert not hosts[0].is_running()
                failure = driver.execute_async_script(
                    script,
                    json.dumps(
                        {
                            "action": "study-attach",
                            "workspace": str(workspace),
                            "choice": {
                                "kind": "existing",
                                "store": "00000000-0000-0000-0000-000000000000",
                            },
                        }
                    ),
                )
                assert not failure["ok"], failure
                assert "UnknownStore" in failure["error"], failure
                events = native_log.read_text()
                assert "event=study-host-reaped" in events, events
                assert (
                    "event=request-completed action=study-attach outcome=error"
                    in events
                ), events
                assert "UnknownStore" in events, events
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert (
                        record.execute("select count(*) from writer").fetchone()[0]
                        == writers + 1
                    )
                    assert record.execute(
                        "select kind from store_event where kind!='backed-up'"
                    ).fetchall() == [("created",)]
                    backup = record.execute(
                        "select path from store_event where kind='backed-up' order by id limit 1"
                    ).fetchone()
                    assert backup is not None
                    assert Path(backup[0]).is_file()
                    assert Path(backup[0]).with_suffix(".sqlite3").is_file()
                wait.until(
                    conditions.element_to_be_clickable(
                        (By.XPATH, '//span[@class="tree-label" and text()="Basics"]')
                    )
                ).click()
                wait.until(
                    conditions.element_to_be_clickable(
                        (
                            By.XPATH,
                            '//*[contains(@class, "card-row-label") and contains(., "Which shape")]',
                        )
                    )
                ).click()
                picture = wait.until(
                    conditions.visibility_of_element_located(
                        (By.CSS_SELECTOR, '.side-editor.front img[alt="A triangle"]')
                    )
                )
                wait.until(
                    lambda _: driver.execute_script(
                        "return arguments[0].complete && arguments[0].naturalWidth > 0",
                        picture,
                    )
                )
                back_picture = wait.until(
                    conditions.visibility_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            '.side-editor.back img[alt="Collapsed triangle"]',
                        )
                    )
                )
                wait.until(
                    lambda _: driver.execute_script(
                        "return arguments[0].complete && arguments[0].naturalWidth > 0",
                        back_picture,
                    )
                )
                driver.save_screenshot(str(artifacts / "native-editor-image.png"))
                driver.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Workspace"]'
                ).click()
                wait.until(
                    conditions.element_to_be_clickable(
                        (By.XPATH, '//button[normalize-space()="Study"]')
                    )
                ).click()
                seen = set()
                for remaining in range(12, 0, -1):
                    wait.until(
                        lambda window, remaining=remaining: (
                            " ".join(
                                window.find_element(
                                    By.CSS_SELECTOR,
                                    '[aria-label="Study counts for workspace"]',
                                )
                                .get_attribute("textContent")
                                .split()
                            )
                            == f"New: {remaining} Learning: 0 Review: 0"
                        )
                    )
                    wait.until(
                        conditions.text_to_be_present_in_element(
                            (By.CSS_SELECTOR, '[aria-label="Remaining cards"]'),
                            f"New: {remaining}",
                        )
                    )
                    reveal = wait.until(
                        conditions.element_to_be_clickable(
                            (By.XPATH, '//button[contains(., "Show answer")]')
                        )
                    )
                    with closing(sqlite3.connect(opened["record"])) as record:
                        identity = record.execute(
                            "select card_id from presentation order by id desc limit 1"
                        ).fetchone()[0]
                    seen.add(identity)
                    if identity == "study-image":
                        picture = wait.until(
                            conditions.visibility_of_element_located(
                                (
                                    By.CSS_SELECTOR,
                                    'section[aria-label="Study session"] img[alt="A triangle"]',
                                )
                            )
                        )
                        wait.until(
                            lambda _, picture=picture: driver.execute_script(
                                "return arguments[0].complete && arguments[0].naturalWidth > 0",
                                picture,
                            )
                        )
                        assert picture.get_attribute("src").startswith("blob:")
                        driver.save_screenshot(
                            str(artifacts / "native-study-image.png")
                        )
                    if identity == "study-diagram":
                        # A fresh TeX font cache is part of this milestone scenario.
                        diagram_wait = WebDriverWait(driver, 120)
                        diagram = diagram_wait.until(
                            conditions.visibility_of_element_located(
                                (
                                    By.CSS_SELECTOR,
                                    'section[aria-label="Study session"] img[alt="Rendered commutative diagram"]',
                                )
                            )
                        )
                        diagram_wait.until(
                            lambda _: driver.execute_script(
                                "return arguments[0].complete && arguments[0].naturalWidth > 0",
                                diagram,
                            )
                        )
                        driver.save_screenshot(
                            str(artifacts / "native-study-diagram.png")
                        )
                    reveal.click()
                    wait.until(
                        conditions.element_to_be_clickable(
                            (By.XPATH, '//button[contains(., "Easy")]')
                        )
                    ).click()
                wait.until(
                    conditions.visibility_of_element_located(
                        (By.XPATH, '//*[text()="Study complete for now"]')
                    )
                )
                assert "study-image" in seen and len(seen) == 12, seen
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert record.execute(
                        "select count(*) from response"
                    ).fetchone() == (12,)
                    assert record.execute(
                        "select count(*) from review where response is not null"
                    ).fetchone() == (12,)
                    recorded = record.execute(
                        "select revlog_id,revlog_cid,revlog_usn,revlog_ease,revlog_ivl,revlog_last_ivl,revlog_factor,revlog_time_ms,revlog_type from response order by revlog_id"
                    ).fetchall()
                driver.save_screenshot(str(artifacts / "native-study-finished.png"))
                driver.find_element(
                    By.XPATH, '//button[contains(., "Return to editor")]'
                ).click()
                wait.until(
                    conditions.visibility_of_element_located(
                        (By.CSS_SELECTOR, ".editor-column .side-editor.front")
                    )
                )
                with closing(sqlite3.connect(opened["record"])) as record:
                    views_before_close = record.execute(
                        "select count(*) from editor_view"
                    ).fetchone()[0]
                children = psutil.Process(service.process.pid).children(recursive=True)
                # WebDriver session deletion force-exits its browser process.
                # Xvfb has no window manager to route _NET_CLOSE_WINDOW. Send
                # its normal WM_DELETE_WINDOW request to the client instead:
                # https://www.x.org/releases/current/doc/xorg-docs/icccm/icccm.pdf
                # https://github.com/WebKit/WebKit/blob/main/Source/WebDriver/glib/SessionHostGlib.cpp
                app = [
                    child
                    for child in children
                    if child.exe() == options.binary_location
                ]
                assert len(app) == 1, app
                windows = subprocess.check_output(
                    ["xdotool", "search", "--onlyvisible", "--pid", str(app[0].pid)],
                    text=True,
                ).splitlines()
                assert len(windows) == 1, windows
                with closing(display.Display()) as connection:
                    window = connection.create_resource_object(
                        "window", int(windows[0])
                    )
                    delete = connection.intern_atom("WM_DELETE_WINDOW")
                    assert delete in window.get_wm_protocols()
                    window.send_event(
                        protocol.event.ClientMessage(
                            window=window,
                            client_type=connection.intern_atom("WM_PROTOCOLS"),
                            data=(32, [delete, X.CurrentTime, 0, 0, 0]),
                        )
                    )
                    connection.sync()
                WebDriverWait(driver, 10).until(
                    lambda _: "event=app-exit" in native_log.read_text()
                )
                with closing(sqlite3.connect(store / "collection.anki2")) as collection:
                    assert (
                        collection.execute(
                            "select id,cid,usn,ease,ivl,lastIvl,factor,time,type from revlog order by id"
                        ).fetchall()
                        == recorded
                    )
                with closing(sqlite3.connect(opened["record"])) as record:
                    assert (
                        record.execute("select count(*) from editor_view").fetchone()[0]
                        == views_before_close + 1
                    )
                    last_view = record.execute(
                        "select card_id,shown_ms,unfocused_ms from editor_view order by id desc limit 1"
                    ).fetchone()
                    assert last_view[0] == "study-image", last_view
                    assert last_view[1] > 0 and 0 <= last_view[2] <= last_view[1], (
                        last_view
                    )
                driver.quit()
                driver = None
                _, alive = psutil.wait_procs(children, timeout=10)
                assert all(child.status() == psutil.STATUS_ZOMBIE for child in alive), (
                    alive
                )
                assert "event=app-exit" in native_log.read_text()
                with closing(sqlite3.connect(opened["record"])) as record:
                    tables = record.execute(
                        "select name from sqlite_master where type='table'"
                    ).fetchall()
                    retained = {
                        name: record.execute(
                            f'select * from "{name}" order by id'
                        ).fetchall()
                        for (name,) in tables
                    }
                misplaced = [
                    str(path.relative_to(root))
                    for path in root.rglob("*")
                    if path.is_file()
                    and path.relative_to(root).parts[0]
                    not in {"config", "cache", "data", "state"}
                ]
                assert not misplaced, misplaced
                web_cache = [
                    str(path.relative_to(root))
                    for name in ("WebKitCache", "CacheStorage")
                    for directory in (root / "data").rglob(name)
                    for path in directory.rglob("*")
                    if path.is_file()
                ]
                assert not web_cache, web_cache
                shutil.copytree(
                    root / "state", artifacts / "application-state-before-removal"
                )
                send2trash(str(root / "cache"))
                send2trash(str(root / "state"))
                driver = webdriver.Remote(
                    command_executor=service.service_url, options=options
                )
                wait = WebDriverWait(driver, 30)
                wait.until(
                    conditions.text_to_be_present_in_element(
                        (By.CSS_SELECTOR, '[role="status"][aria-label="Study"]'),
                        "Study cards ready",
                    )
                )
                restored = driver.execute_async_script(script, payload)
                assert restored["ok"], restored
                assert restored["result"]["store"] == opened["store"]
                assert restored["result"]["counts"]["counts"] == {
                    "new": 0,
                    "learning": 0,
                    "review": 0,
                }
                with closing(sqlite3.connect(opened["record"])) as record:
                    for name, previous in retained.items():
                        current = record.execute(
                            f'select * from "{name}" order by id'
                        ).fetchall()
                        assert current[: len(previous)] == previous, name
                misplaced = [
                    str(path.relative_to(root))
                    for path in root.rglob("*")
                    if path.is_file()
                    and path.relative_to(root).parts[0]
                    not in {"config", "cache", "data", "state"}
                ]
                assert not misplaced, misplaced
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
    with evidence(
        "native-study", Path(__file__).parent / "fixtures" / "study"
    ) as artifacts:
        main(artifacts)
