# /// script
# requires-python = ">=3.12"
# dependencies = ["mss", "cyclopts", "psutil", "selenium"]
# ///
"""Capture the built native WebKit app in an isolated X11 display."""

import configparser
import difflib
import json
import math
import os
import re
import shlex
import shutil
import subprocess
import tempfile
import time
import zipfile
from contextlib import suppress
from dataclasses import asdict, dataclass
from pathlib import Path

import cyclopts
import mss
import mss.tools
import psutil
from installation import prepare_asset_update
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.webkitgtk.options import Options
from selenium.webdriver.webkitgtk.service import Service


@dataclass
class StartupSample:
    condition: str
    # Actual release-process launch to usable painted tree, native click to
    # painted editor, and native keydown to glyph pixels. These exclude the
    # automation driver's session, command dispatch and xdotool startup.
    tree_seconds: float
    selection_seconds: float
    input_paint_seconds: float
    background_running: bool
    # Diagnostics and conservative end-to-end automation upper bounds.
    driver_tree_seconds: float
    driver_selection_seconds: float
    driver_input_seconds: float
    # In-page components: WebView navigation start to published navigation,
    # and keydown dispatch to the second following animation frame.
    page_tree_seconds: float
    page_input_seconds: float
    page_start_seconds: float


@dataclass
class MathProfile:
    condition: str
    stack: str
    calls: int
    seconds: float


def measure_quiver_native(entry: Path | None) -> None:
    """Verify Quiver's local iframe bridge inside the installed WebKit app."""
    desktop = Path(__file__).resolve().parents[1]
    binary = desktop / "src-tauri" / "target" / "release" / "desktop"
    if entry is not None:
        configuration = configparser.ConfigParser(interpolation=None)
        configuration.read(entry)
        binary = Path(
            shlex.split(configuration["Desktop Entry"]["Exec"])[0].replace("%%", "%")
        )
    artifacts = desktop / "test-artifacts"
    artifacts.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="flashcards-native-quiver-") as temporary:
        root = Path(temporary)
        workspace = root / "workspace"
        workspace.mkdir()
        deck = workspace / "Category Theory.md"
        deck.write_bytes((desktop.parent / "decks" / "Category Theory.md").read_bytes())
        before = deck.read_bytes()
        environment = os.environ | {
            "TAURI_WEBVIEW_AUTOMATION": "true",
            "GDK_BACKEND": "x11",
            "XDG_CONFIG_HOME": str(root / "config"),
            "XDG_CACHE_HOME": str(root / "cache"),
            "XDG_DATA_HOME": str(root / "data"),
            "UV_OFFLINE": "1",
        }
        options = Options()
        options.capabilities.pop("browserName")
        options.binary_location = str(binary)
        with (artifacts / "native-quiver.log").open("w") as log:
            service = Service(
                executable_path="/bin/WebKitWebDriver", env=environment, log_output=log
            )
            service.start()
            driver: webdriver.Remote | None = None
            try:
                driver = webdriver.Remote(
                    command_executor=service.service_url, options=options
                )
                wait = WebDriverWait(driver, 120, poll_frequency=0.05)
                wait.until(
                    lambda browser: (
                        browser.find_element(By.CSS_SELECTOR, ".workspace-name")
                        .get_attribute("textContent")
                        .strip()
                        != "Choose a workspace"
                    )
                )
                driver.find_element(By.CSS_SELECTOR, '[aria-label="Workspace"]').click()
                field = wait.until(
                    lambda browser: browser.find_element(
                        By.CSS_SELECTOR,
                        'input[placeholder="Folder containing your Markdown decks"]',
                    )
                )
                from selenium.webdriver.common.keys import Keys

                field.send_keys(Keys.CONTROL, "a")
                field.send_keys(str(workspace))
                wait.until(
                    lambda browser: (
                        browser.find_element(
                            By.CSS_SELECTOR,
                            'input[placeholder="Folder containing your Markdown decks"]',
                        ).get_attribute("value")
                        == str(workspace)
                    )
                )
                wait.until(
                    lambda browser: browser.find_element(
                        By.XPATH, "//button[normalize-space()='Open workspace']"
                    ).is_enabled()
                )
                driver.find_element(
                    By.XPATH, "//button[normalize-space()='Open workspace']"
                ).click()
                try:
                    WebDriverWait(driver, 25, poll_frequency=0.05).until(
                        lambda browser: (
                            browser.execute_script(
                                "return document.querySelector('.workspace-name')?.textContent?.trim()"
                            )
                            == workspace.name
                        )
                    )
                except TimeoutException:
                    driver.save_screenshot(
                        str(artifacts / "native-quiver-workspace-failure.png")
                    )
                    print(
                        json.dumps(
                            {
                                "requested": str(workspace),
                                "field": driver.execute_script(
                                    "return document.querySelector('input[placeholder*=\"Folder containing\"]')?.value"
                                ),
                                "displayed": driver.execute_script(
                                    "return document.querySelector('.workspace-name')?.textContent"
                                ),
                                "tree": driver.execute_script(
                                    "return [...document.querySelectorAll('[data-deck]')].map(n=>n.dataset.deck)"
                                ),
                                "errors": driver.execute_script(
                                    "return document.body.innerText.slice(0, 1000)"
                                ),
                            }
                        ),
                        flush=True,
                    )
                    raise
                wait.until(
                    lambda browser: browser.find_element(
                        By.CSS_SELECTOR, '[data-deck="Category Theory.md"]'
                    )
                ).click()
                wait.until(
                    lambda browser: browser.find_elements(
                        By.CSS_SELECTOR, ".side-editor.front .cm-content"
                    )
                )
                # The diagram is on the limit/colimit card, not the first
                # card selected when this deck opens.
                wait.until(
                    lambda browser: (
                        browser.find_element(
                            By.CSS_SELECTOR,
                            '[data-card="card-d87ef906950bd548"] .card-row-label',
                        )
                        if browser.find_element(
                            By.CSS_SELECTOR,
                            '[data-card="card-d87ef906950bd548"] .card-row-label',
                        ).is_enabled()
                        else False
                    )
                ).click()
                try:
                    wait.until(
                        lambda browser: browser.find_elements(
                            By.CSS_SELECTOR, ".side-editor.back .diagram-field-entry"
                        )
                    )
                except TimeoutException:
                    driver.save_screenshot(
                        str(artifacts / "native-quiver-selection-failure.png")
                    )
                    print(
                        "Native diagram selection diagnostic:",
                        driver.execute_script("""return {
                          active: document.querySelector('.card-row.active')?.dataset.card,
                          selected: [...document.querySelectorAll('.card-row-label')].filter(n=>n.getAttribute('aria-pressed')==='true').map(n=>n.textContent.slice(0,100)),
                          status: document.querySelector('.toolbar .status')?.textContent,
                          heading: document.querySelector('.card-stage')?.innerText.slice(0,250),
                          error: document.querySelector('[role="alert"]')?.textContent,
                        }"""),
                        flush=True,
                    )
                    raise
                # The side editor presents the diagram instead of 1,889 bytes
                # of opaque URL or 1,076 bytes of LaTeX.
                assert not any(
                    r"\begin{tikzcd}" in editor.text
                    for editor in driver.find_elements(
                        By.CSS_SELECTOR, ".side-editor.back .cm-content"
                    )
                )
                preview = wait.until(
                    lambda browser: browser.find_element(
                        By.CSS_SELECTOR,
                        '.side-editor.back iframe[title="Rendered commutative diagram"]',
                    )
                )
                driver.switch_to.frame(preview)
                try:
                    WebDriverWait(driver, 25, poll_frequency=0.1).until(
                        lambda browser: (
                            len(browser.find_elements(By.CSS_SELECTOR, ".vertex")) == 15
                        )
                    )
                except TimeoutException:
                    print(
                        "Native Quiver iframe diagnostic:",
                        driver.execute_script(
                            "return {href:location.href,origin:location.origin,referrer:document.referrer,ready:document.readyState,body:document.body?.innerText.slice(0,1000),vertices:document.querySelectorAll('.vertex').length,html:document.documentElement.outerHTML.slice(0,800)}"
                        ),
                        flush=True,
                    )
                    driver.switch_to.default_content()
                    driver.save_screenshot(str(artifacts / "native-quiver-failure.png"))
                    print(
                        "Native parent diagnostic:",
                        driver.execute_script(
                            "return {href:location.href,origin:location.origin,body:document.body.innerText.slice(-1800)}"
                        ),
                        flush=True,
                    )
                    raise
                geometry_script = """return {
                      viewport: [document.documentElement.clientWidth, document.documentElement.clientHeight],
                      transform: document.querySelector('.canvas')?.style.transform,
                      bodyClass: document.body.className,
                      fonts: document.fonts.status,
                      points: [...document.querySelectorAll('.vertex')].map(vertex => {
                        const r = vertex.getBoundingClientRect();
                        return [r.left, r.top, r.right, r.bottom];
                      }),
                    }"""
                try:
                    WebDriverWait(driver, 20, poll_frequency=0.05).until(
                        lambda browser: (
                            "scale(1)"
                            not in browser.execute_script(geometry_script)["transform"]
                        )
                    )
                except TimeoutException:
                    print(
                        "Native Quiver did not fit its preview:",
                        driver.execute_script(geometry_script),
                        flush=True,
                    )
                    raise
                geometry = driver.execute_script(geometry_script)
                width, height = geometry["viewport"]
                assert all(
                    left >= -10
                    and top >= -10
                    and right <= width + 10
                    and bottom <= height + 10
                    for left, top, right, bottom in geometry["points"]
                ), "The native card preview clips diagram objects."
                x_span = max(point[2] for point in geometry["points"]) - min(
                    point[0] for point in geometry["points"]
                )
                y_span = max(point[3] for point in geometry["points"]) - min(
                    point[1] for point in geometry["points"]
                )
                assert x_span > width * 0.5 and y_span > height * 0.35, (
                    "The native diagram was over-shrunk and is unreadable.",
                    geometry,
                )
                driver.switch_to.default_content()
                driver.save_screenshot(str(artifacts / "native-quiver-card.png"))
                driver.find_element(
                    By.XPATH, "//button[normalize-space()='Edit in Quiver']"
                ).click()
                editable = wait.until(
                    lambda browser: browser.find_element(
                        By.CSS_SELECTOR, 'iframe[title="Quiver diagram editor"]'
                    )
                )
                driver.switch_to.frame(editable)
                wait.until(
                    lambda browser: (
                        len(browser.find_elements(By.CSS_SELECTOR, ".vertex")) == 15
                    )
                )
                driver.switch_to.default_content()
                wait.until(
                    lambda browser: browser.find_element(
                        By.XPATH, "//button[normalize-space()='Use diagram']"
                    ).is_enabled()
                )
                driver.save_screenshot(str(artifacts / "native-quiver-editor.png"))
                driver.find_element(
                    By.XPATH, "//button[normalize-space()='Cancel']"
                ).click()
                assert deck.read_bytes() == before
                print("Installed WebKit renders and edits Quiver diagrams offline.")
            finally:
                if driver is not None:
                    children = psutil.Process(service.process.pid).children(
                        recursive=True
                    )
                    driver.quit()
                    _, alive = psutil.wait_procs(children, timeout=10)
                    for child in alive:
                        with suppress(psutil.NoSuchProcess):
                            if child.status() != psutil.STATUS_ZOMBIE:
                                child.terminate()
                    psutil.wait_procs(alive, timeout=10)
                service.stop()


def measure_startup(entry: Path | None, profile: bool) -> None:
    """Measure real release windows and native keyboard paint during checks."""
    desktop = Path(__file__).resolve().parents[1]
    artifacts = desktop / "test-artifacts"
    if entry is None:
        binary = desktop / "src-tauri" / "target" / "release" / "desktop"
        resources = binary.parent
    else:
        configuration = configparser.ConfigParser(interpolation=None)
        configuration.read(entry)
        # Desktop entry escaping: https://specifications.freedesktop.org/desktop-entry-spec/latest/exec-variables.html
        binary = Path(
            shlex.split(configuration["Desktop Entry"]["Exec"])[0].replace("%%", "%")
        )
        resources = (
            entry.parent.parent
            / "math-flashcards"
            / "active"
            / "lib"
            / "Math Flashcards"
        )
    samples: list[StartupSample] = []
    profiles: list[MathProfile] = []
    repetitions = 1 if profile else 20
    with tempfile.TemporaryDirectory(prefix="flashcards-timings-") as temporary:
        root = Path(temporary)
        workspace = root / "workspace"
        shutil.copytree(desktop.parent / "decks", workspace)
        source = workspace / "Analysis" / "Precalculus.md"
        original = source.read_bytes()
        environment = os.environ | {
            "TAURI_WEBVIEW_AUTOMATION": "true",
            "GDK_BACKEND": "x11",
            "XDG_CONFIG_HOME": str(root / "config"),
            "XDG_CACHE_HOME": str(root / "cache"),
            "XDG_DATA_HOME": str(root / "data"),
        }
        options = Options()
        # Tauri supplies its application identity, rather than MiniBrowser's.
        # https://v2.tauri.app/develop/tests/webdriver/example/selenium/
        options.capabilities.pop("browserName")
        options.binary_location = str(binary)
        with (artifacts / "native-timings.log").open("w") as log:
            service = Service(
                executable_path="/bin/WebKitWebDriver", env=environment, log_output=log
            )
            service.start()

            def launch() -> webdriver.Remote:
                return webdriver.Remote(
                    command_executor=service.service_url, options=options
                )

            def native_start() -> float:
                # The driver launches the real release binary as its child.
                # WebDriver's session handshake is not part of the app launch.
                children = psutil.Process(service.process.pid).children(recursive=True)
                candidates = [
                    child.create_time()
                    for child in children
                    if child.name() == "desktop"
                ]
                assert candidates, "The native release process was not found."
                return min(candidates)

            def finish(driver: webdriver.Remote) -> None:
                children = psutil.Process(service.process.pid).children(recursive=True)
                driver.quit()
                _, alive = psutil.wait_procs(children, timeout=10)
                for child in alive:
                    with suppress(psutil.NoSuchProcess):
                        if child.status() != psutil.STATUS_ZOMBIE:
                            child.terminate()
                _, alive = psutil.wait_procs(alive, timeout=10)
                for child in alive:
                    with suppress(psutil.NoSuchProcess):
                        assert child.status() == psutil.STATUS_ZOMBIE

            try:
                driver = launch()
                try:
                    # The first complete analysis is setup, not a measured endpoint.
                    wait = WebDriverWait(driver, 900, poll_frequency=0.02)
                    wait.until(
                        lambda d: d.find_elements(By.CSS_SELECTOR, "[data-deck]")
                    )
                    driver.find_element(
                        By.CSS_SELECTOR, '[aria-label="Workspace"]'
                    ).click()
                    field = driver.find_element(
                        By.CSS_SELECTOR,
                        'input[placeholder="Folder containing your Markdown decks"]',
                    )
                    from selenium.webdriver.common.keys import Keys

                    field.send_keys(Keys.CONTROL, "a")
                    field.send_keys(str(workspace))
                    wait.until(
                        lambda d: d.find_element(
                            By.XPATH, "//button[normalize-space()='Open workspace']"
                        ).is_enabled()
                    )
                    started = time.monotonic()
                    driver.find_element(
                        By.XPATH, "//button[normalize-space()='Open workspace']"
                    ).click()
                    wait.until(
                        lambda d: (
                            d.find_element(By.CSS_SELECTOR, ".workspace-name")
                            .get_attribute("textContent")
                            .strip()
                            == workspace.name
                        )
                    )
                    wait.until(
                        lambda d: (
                            d.find_element(
                                By.CSS_SELECTOR, ".workspace-progress"
                            ).get_attribute("textContent")
                            == "Workspace checks complete"
                        )
                    )
                    background_seconds = time.monotonic() - started
                finally:
                    finish(driver)
                for condition in ("warm", "cold"):
                    for repetition in range(repetitions):
                        if condition == "cold":
                            python = (resources / "runtime.txt").read_text().strip()
                            subprocess.run(
                                [python, "-I", str(resources / "backend.py")],
                                input=json.dumps(
                                    {
                                        "action": "rebuild-cache",
                                        "workspace": str(workspace),
                                        "generation": 0,
                                    }
                                ),
                                text=True,
                                capture_output=True,
                                check=True,
                                env=environment,
                            )
                        launched = time.monotonic()
                        driver = launch()
                        try:
                            process_started = native_start()
                            wait = WebDriverWait(driver, 30, poll_frequency=0.01)
                            wait.until(
                                lambda d: (
                                    d.find_element(By.CSS_SELECTOR, ".workspace-name")
                                    .get_attribute("textContent")
                                    .strip()
                                    == workspace.name
                                    and d.find_elements(By.CSS_SELECTOR, "[data-deck]")
                                    and not d.find_elements(
                                        By.CSS_SELECTOR,
                                        '.sidebar-head [aria-label="Loading"]',
                                    )
                                    and d.execute_script(
                                        "return performance.getEntriesByName('flashcards:tree-usable').length > 0"
                                    )
                                )
                            )
                            driver_tree_seconds = time.monotonic() - launched
                            tree_clock = driver.execute_script("""
                              const usable = performance.getEntriesByName('flashcards:tree-usable')[0];
                              if (!usable) return null;
                              return (performance.timeOrigin + usable.startTime) / 1000;
                            """)
                            assert tree_clock is not None, (
                                "The usable tree was not marked."
                            )
                            tree_seconds = tree_clock - process_started
                            # WebKit's performance.timeOrigin and psutil's
                            # kernel process creation timestamp are separate
                            # wall-clock estimates. In particular a usable
                            # paint can follow WebDriver's earlier DOM-ready
                            # observation; their measured difference is not
                            # a validity assertion. Retain both measurements.
                            assert tree_seconds > 0
                            page_start_seconds = (
                                tree_clock
                                - driver.execute_script(
                                    "return performance.getEntriesByName('flashcards:tree-usable')[0].startTime"
                                )
                                / 1000
                                - process_started
                            )
                            page_tree_seconds = (
                                driver.execute_script(
                                    "return performance.getEntriesByName('flashcards:tree-published')[0].startTime"
                                )
                                / 1000
                            )
                            driver.find_element(
                                By.XPATH,
                                "//*[@role='treeitem' and normalize-space()='Analysis']",
                            ).click()
                            deck = wait.until(
                                lambda d: d.find_element(
                                    By.CSS_SELECTOR,
                                    '[data-deck="Analysis/Precalculus.md"]',
                                )
                            )
                            if profile:
                                wait.until(
                                    lambda d: d.execute_script(
                                        "return typeof window.MathJax?.tex2chtml === 'function'"
                                    )
                                )
                                driver.execute_script(r"""
                                  window.nativeMathProfile = new Map();
                                  const original = window.MathJax.tex2chtml;
                                  window.MathJax.tex2chtml = function(...args) {
                                    const stack = new Error().stack.split('\n').slice(1, 5).join('\n');
                                    const start = performance.now();
                                    try { return original.apply(this, args); }
                                    finally {
                                      const result = window.nativeMathProfile.get(stack) ?? {stack, calls: 0, seconds: 0};
                                      result.calls++;
                                      result.seconds += (performance.now() - start) / 1000;
                                      window.nativeMathProfile.set(stack, result);
                                    }
                                  };
                                """)
                            # Observe the actual native click and the editor's
                            # second painted frame inside the WebView, not the
                            # Selenium request/response round trip.
                            driver.execute_script("""
                              window.nativeSelection = null;
                              const deck = document.querySelector('[data-deck="Analysis/Precalculus.md"]');
                              deck.addEventListener('click', () => {
                                const start = performance.now();
                                const ready = () => {
                                  const editor = document.querySelector('.side-editor.front .cm-content');
                                  const math = document.querySelector('.side-editor.front mjx-container');
                                  if (editor?.getAttribute('contenteditable') !== 'true' || !math) return;
                                  observer.disconnect();
                                  requestAnimationFrame(() => requestAnimationFrame(() => {
                                    window.nativeSelection = (performance.now() - start) / 1000;
                                  }));
                                };
                                const observer = new MutationObserver(ready);
                                observer.observe(document.body, {childList: true, subtree: true, attributes: true});
                                ready();
                              }, {capture: true, once: true});
                            """)
                            selected = time.monotonic()
                            deck.click()
                            editor = wait.until(
                                lambda d: d.find_element(
                                    By.CSS_SELECTOR, ".side-editor.front .cm-content"
                                )
                            )
                            wait.until(
                                lambda d: (
                                    d.find_elements(
                                        By.CSS_SELECTOR,
                                        ".side-editor.front mjx-container",
                                    )
                                    and d.find_element(
                                        By.CSS_SELECTOR,
                                        ".side-editor.front .cm-content",
                                    ).get_attribute("contenteditable")
                                    == "true"
                                )
                            )
                            driver_selection_seconds = time.monotonic() - selected
                            selection_seconds = wait.until(
                                lambda d: d.execute_script(
                                    "return window.nativeSelection"
                                )
                            )
                            if profile:
                                profiles.extend(
                                    MathProfile(condition=condition, **values)
                                    for values in driver.execute_script(
                                        "return [...window.nativeMathProfile.values()].sort((a,b)=>b.seconds-a.seconds)"
                                    )
                                )
                            background_running = (
                                driver.find_element(
                                    By.CSS_SELECTOR, ".workspace-progress"
                                ).get_attribute("textContent")
                                != "Workspace checks complete"
                            )
                            # innerText alone loses trailing empty lines, so
                            # it can claim Undo restored a field while a new
                            # blank line remains in the saved Markdown.
                            front_text = """return {
                              text: document.querySelector('.side-editor.front .cm-content').innerText,
                              lines: document.querySelectorAll('.side-editor.front .cm-line').length
                            }"""
                            unedited = driver.execute_script(front_text)
                            editor.click()
                            subprocess.run(
                                [
                                    "xdotool",
                                    "key",
                                    "--clearmodifiers",
                                    "ctrl+End",
                                    "Return",
                                ],
                                check=True,
                            )
                            wait.until(
                                lambda d: d.execute_script(
                                    "return document.querySelector('.side-editor.front .cm-line:last-child').textContent.trim() === ''"
                                )
                            )
                            # Math above the new line can still be laying out;
                            # sample the line only once its position holds
                            # across consecutive animation frames.
                            left, top = driver.execute_async_script("""
                              const done = arguments[arguments.length - 1];
                              const place = () => {
                                const line = document.querySelector('.side-editor.front .cm-line:last-child');
                                const r = line.getBoundingClientRect();
                                return [Math.floor(r.left + parseFloat(getComputedStyle(line).paddingLeft)) + 2, Math.floor(r.top) + 4];
                              };
                              let previous = place(), stable = 0;
                              const step = () => requestAnimationFrame(() => {
                                const next = place();
                                stable = next[0] === previous[0] && next[1] === previous[1] ? stable + 1 : 0;
                                previous = next;
                                if (stable >= 3) done(next); else step();
                              });
                              step();
                            """)
                            with mss.MSS() as screen:
                                region = {
                                    "left": left,
                                    "top": top,
                                    "width": 5,
                                    "height": 16,
                                }
                                before = screen.grab(region).rgb
                                dark = lambda pixels: sum(
                                    max(pixels[i : i + 3]) < 160
                                    for i in range(0, len(pixels), 3)
                                )
                                baseline = dark(before)
                                driver.execute_script("""
                                  window.inputFrame = null;
                                  window.nativeKeyEpoch = null;
                                  window.addEventListener('keydown', (event) => {
                                    const start = event.timeStamp;
                                    window.nativeKeyEpoch = (performance.timeOrigin + start) / 1000;
                                    requestAnimationFrame(() => requestAnimationFrame(() => {
                                      window.inputFrame = (performance.now() - start) / 1000;
                                    }));
                                  }, {once: true, capture: true});
                                """)
                                typed = time.monotonic()
                                subprocess.run(
                                    ["xdotool", "key", "--clearmodifiers", "m"],
                                    check=True,
                                )
                                while time.monotonic() - typed < 5:
                                    pixels = screen.grab(region).rgb
                                    if pixels != before and dark(pixels) > baseline + 5:
                                        pixel_seen_epoch = time.time()
                                        break
                                else:
                                    driver.save_screenshot(
                                        str(artifacts / "native-timing-last.png")
                                    )
                                    frame = screen.grab(
                                        {
                                            "left": 0,
                                            "top": 0,
                                            "width": 1440,
                                            "height": 1000,
                                        }
                                    )
                                    mss.tools.to_png(
                                        frame.rgb,
                                        frame.size,
                                        output=str(
                                            artifacts / "native-timing-frame.png"
                                        ),
                                    )
                                    print(
                                        json.dumps(
                                            {
                                                "region": region,
                                                "baseline_dark": baseline,
                                                "observed_dark": dark(pixels),
                                                "line": driver.execute_script(
                                                    "return document.querySelector('.side-editor.front .cm-line:last-child').textContent"
                                                ),
                                            }
                                        ),
                                        flush=True,
                                    )
                                    raise AssertionError(
                                        "The native input glyph did not paint."
                                    )
                                driver_input_seconds = time.monotonic() - typed
                            key_epoch = driver.execute_script(
                                "return window.nativeKeyEpoch"
                            )
                            assert key_epoch is not None, (
                                "The native key event was not received."
                            )
                            input_seconds = pixel_seen_epoch - key_epoch
                            assert 0 < input_seconds <= driver_input_seconds + 0.05
                            page_input_seconds = wait.until(
                                lambda d: d.execute_script("return window.inputFrame")
                            )
                            assert (
                                driver.execute_script(
                                    "return document.querySelector('.side-editor.front .cm-line:last-child').textContent.trim()"
                                )
                                == "m"
                            )
                            # CodeMirror groups history entries by input timing:
                            # https://codemirror.net/docs/ref/#commands.history^config.newGroupDelay
                            for _ in range(4):
                                if driver.execute_script(front_text) == unedited:
                                    break
                                subprocess.run(
                                    ["xdotool", "key", "--clearmodifiers", "ctrl+z"],
                                    check=True,
                                )
                                time.sleep(0.2)
                            assert driver.execute_script(front_text) == unedited
                            subprocess.run(
                                ["xdotool", "key", "--clearmodifiers", "ctrl+s"],
                                check=True,
                            )
                            try:
                                wait.until(
                                    lambda d: (
                                        source.read_bytes() == original
                                        and "Saving"
                                        not in d.find_element(
                                            By.CSS_SELECTOR, ".toolbar .status"
                                        ).get_attribute("textContent")
                                    )
                                )
                            except TimeoutException:
                                raise AssertionError(
                                    json.dumps(
                                        {
                                            "status": driver.find_element(
                                                By.CSS_SELECTOR, ".toolbar .status"
                                            ).get_attribute("textContent"),
                                            "difference": [
                                                line
                                                for line in difflib.unified_diff(
                                                    original.decode().splitlines(),
                                                    source.read_text().splitlines(),
                                                    lineterm="",
                                                )
                                            ][:20],
                                        }
                                    ),
                                )
                            sample = StartupSample(
                                condition,
                                tree_seconds,
                                selection_seconds,
                                input_seconds,
                                background_running,
                                driver_tree_seconds,
                                driver_selection_seconds,
                                driver_input_seconds,
                                page_tree_seconds,
                                page_input_seconds,
                                page_start_seconds,
                            )
                            samples.append(sample)
                            print(json.dumps(asdict(sample)), flush=True)
                            if repetition == 0:
                                driver.save_screenshot(
                                    str(artifacts / f"native-timing-{condition}.png")
                                )
                        except Exception:
                            driver.save_screenshot(
                                str(artifacts / "native-timing-failure.png")
                            )
                            print(
                                driver.execute_script(
                                    "return [...document.querySelectorAll('[role=treeitem]')].map(n=>({text:n.textContent,expanded:n.getAttribute('aria-expanded')}))"
                                ),
                                flush=True,
                            )
                            raise
                        finally:
                            finish(driver)
            finally:
                service.stop()
    report = {
        "binary": str(binary),
        "background_seconds": background_seconds,
        # Samples taken under external CPU load are not acceptance samples.
        "load_average": os.getloadavg(),
        "samples": [asdict(sample) for sample in samples],
        "p95": {
            condition: {
                metric: sorted(
                    getattr(sample, metric)
                    for sample in samples
                    if sample.condition == condition
                )[math.ceil(0.95 * repetitions) - 1]
                for metric in (
                    "tree_seconds",
                    "selection_seconds",
                    "input_paint_seconds",
                )
            }
            for condition in ("warm", "cold")
        },
        "worst": {
            condition: {
                metric: max(
                    getattr(sample, metric)
                    for sample in samples
                    if sample.condition == condition
                )
                for metric in (
                    "tree_seconds",
                    "selection_seconds",
                    "input_paint_seconds",
                )
            }
            for condition in ("warm", "cold")
        },
        "driver_p95": {
            condition: {
                metric: sorted(
                    getattr(sample, metric)
                    for sample in samples
                    if sample.condition == condition
                )[math.ceil(0.95 * repetitions) - 1]
                for metric in (
                    "driver_tree_seconds",
                    "driver_selection_seconds",
                    "driver_input_seconds",
                )
            }
            for condition in ("warm", "cold")
        },
        "page_p95": {
            condition: {
                metric: sorted(
                    getattr(sample, metric)
                    for sample in samples
                    if sample.condition == condition
                )[math.ceil(0.95 * repetitions) - 1]
                for metric in ("page_tree_seconds", "page_input_seconds")
            }
            for condition in ("warm", "cold")
        },
    }
    if profile:
        report.pop("page_p95")
        report.pop("p95")
        report.pop("driver_p95")
        report.pop("worst")
        report["mathjax"] = [asdict(result) for result in profiles]
    (
        artifacts / ("native-profile.json" if profile else "native-timings.json")
    ).write_text(json.dumps(report, indent=2) + "\n")
    if not profile:
        failures = []
        for condition, results in report["p95"].items():
            for metric, value in results.items():
                target = (
                    (1 if condition == "warm" else 2)
                    if metric == "tree_seconds"
                    else (1 if metric == "selection_seconds" else 0.1)
                )
                if value > target:
                    failures.append(
                        f"{condition} {metric}: p95 {value:.3f}s exceeds {target:.3f}s"
                    )
        assert not failures, "\n".join(failures)


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
    *,
    entry: Path | None = None,
    offline: bool = False,
    updates: bool = False,
    timings: bool = False,
    profile: bool = False,
    diagrams: bool = False,
) -> None:
    """Exercise a built app, or launch an installed desktop entry through Gio."""
    if diagrams:
        if offline or updates or timings or profile:
            raise ValueError(
                "The native Quiver scenario uses its own isolated session."
            )
        measure_quiver_native(entry)
        return
    if timings:
        if offline or updates:
            raise ValueError("Timing uses its own release-window scenario.")
        measure_startup(entry, profile)
        return
    if profile:
        raise ValueError("Use --timings with --profile.")
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
