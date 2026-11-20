[private]
default:
    @just --list

# Compile every deck under decks/ into decks/apkg/
build: desktop-dependencies
    "$(uv python find --script desktop/backend.py)" desktop/backend.py build decks

# Compile every TikZ-cd diagram of a workspace into the app's diagram cache; the app need not run
compile-diagrams workspace="decks":
    "$(uv python find --script desktop/backend.py)" desktop/backend.py diagrams "{{workspace}}"

# Sanity-check that every deck is well-formed new-format Markdown
test: check-math
    uv run --upgrade scripts/check-decks.py

# Reject TeX that MathJax cannot render, such as an undefined macro
check-math:
    cd desktop && bun scripts/check-math.ts ../decks

# Check that every card citation key names an item in the running Zotero library
check-citations:
    uv run --upgrade scripts/check-citations.py

# List card lines that may cite a source in prose. A shortlist to read, not a proof
lint-prose-citations:
    uv run --upgrade scripts/lint-prose-citations.py

# Push gate entry point
test-push: test

# Commit gate entry point using prepared dependencies
test-commit: test desktop-boundaries desktop-frontend desktop-source-test desktop-editor-test desktop-test desktop-study-test desktop-analysis-test desktop-diagram-test desktop-organization-test

# Install the Chromium build of the current Playwright release. Each browser
# scenario runs with `uv run --upgrade`, so a new Playwright release needs its
# own browser build before the scenario starts.
[private]
desktop-browser:
    uv run --upgrade --no-project --with playwright playwright install chromium

# Install the desktop build dependencies
desktop-dependencies:
    [ -d desktop/.parser ] || env -u GIT_INDEX_FILE git clone --quiet --filter=tree:0 --sparse --branch develop https://github.com/dzackgarza/Zettlr-pandoc-mathjax desktop/.parser
    env -u GIT_INDEX_FILE git -C desktop/.parser sparse-checkout set vendor/lezer-markdown-pandoc
    env -u GIT_INDEX_FILE git -C desktop/.parser pull --quiet --ff-only --no-recurse-submodules
    [ -d desktop/.renderer ] || env -u GIT_INDEX_FILE git clone --quiet --filter=tree:0 --sparse --branch main https://github.com/dzackgarza/pandoc-config desktop/.renderer
    env -u GIT_INDEX_FILE git -C desktop/.renderer sparse-checkout set styles filters templates
    env -u GIT_INDEX_FILE git -C desktop/.renderer pull --quiet --ff-only --no-recurse-submodules
    cd desktop && bun update
    cd desktop/src-tauri && cargo update --quiet
    uv run --upgrade desktop/backend.py prepare
    uv run --upgrade desktop/scripts/prepare-diagrams.py

# Build and install the app in XDG user directories
desktop-install: desktop-dependencies desktop-build desktop-deploy

# Rebuild the checkout and update the installed app and desktop entry
desktop-update: desktop-install

# Install the current native build and refresh its desktop entry
desktop-deploy:
    uv run --upgrade desktop/linux/install.py desktop/src-tauri/target/release

# Verify installation and update in temporary XDG directories
desktop-install-test:
    uv run --upgrade desktop/tests/installation.py

# Check the installed Study runtime and preservation of learning data on update
desktop-install-study-test:
    uv run --upgrade desktop/tests/installation.py --study

# Run the native desktop app
desktop-dev:
    cd desktop && bunx tauri dev

# Open the built native app
desktop-run:
    desktop/src-tauri/target/release/desktop

# Serve the editor with its real backend for browser inspection
desktop-web:
    cd desktop && bunx vite --host 127.0.0.1

# Build the frontend and native executable
desktop-build:
    cd desktop && bunx tsc --noEmit
    cd desktop && bunx tauri build --no-bundle

# Compile the desktop frontend
desktop-frontend:
    cd desktop && bunx tsc --noEmit
    cd desktop && bunx vite build

# Verify the shared editor's rendering, wrapping, and source edits
desktop-editor-test: (desktop-test "editor")

# Graphical Quiver import/creation and offline SVG export through real backend
desktop-diagram-test: (desktop-test "quiver")

# Exercise the editor against its real backend with an isolated server
desktop-test scenario="full": desktop-browser
    #!/usr/bin/env -S uv run --no-project --script
    import os
    import shutil
    import subprocess
    import sys
    import tempfile
    from pathlib import Path
    sys.path.insert(0, str(Path("desktop/tests").resolve()))
    from evidence import evidence
    scenarios = {"full": "uv run --upgrade tests/workbench.py", "startup": "uv run --upgrade tests/workbench.py --startup", "study": "xvfb-run -a uv run --upgrade tests/study.py", "study-changes": "xvfb-run -a uv run --upgrade tests/study-changes.py", "study-timing": "xvfb-run -a uv run --upgrade tests/study-timing.py", "study-scopes": "xvfb-run -a uv run --upgrade tests/study-scopes.py", "study-corrections": "xvfb-run -a uv run --upgrade tests/study-corrections.py", "study-draft": "xvfb-run -a uv run --upgrade tests/study-draft.py", "study-settings": "xvfb-run -a uv run --upgrade tests/study-settings.py"}
    environment = os.environ.copy()
    # A window must open on the display that xvfb-run supplies. Chromium and GTK
    # use the caller's Wayland session when this variable is set.
    environment.pop("WAYLAND_DISPLAY", None)
    scenarios["study-fit"] = "xvfb-run -a uv run --upgrade tests/study-fit.py"
    scenarios["study-statistics"] = "xvfb-run -a uv run --upgrade tests/study-statistics.py"
    scenarios["study-copy"] = "xvfb-run -a uv run --upgrade tests/study-copy.py"
    scenarios["study-preservation"] = "xvfb-run -a uv run --upgrade tests/study-preservation.py"
    scenarios["study-keys"] = "xvfb-run -a uv run --upgrade tests/study-keys.py"
    scenarios["editor"] = "uv run --upgrade tests/editor.py"
    scenarios["quiver"] = "uv run --upgrade tests/quiver.py"
    environment.setdefault("UV_CACHE_DIR", subprocess.check_output(["uv", "cache", "dir"], text=True).strip())
    environment.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(Path(os.environ.get("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "ms-playwright"))
    with evidence("browser-{{scenario}}", Path("desktop/tests/fixtures")) as artifacts, tempfile.TemporaryDirectory(prefix="flashcards-browser-cache-") as directory:
        environment["XDG_CACHE_HOME"] = str(Path(directory) / "cache")
        environment["XDG_DATA_HOME"] = str(Path(directory) / "data")
        environment["XDG_STATE_HOME"] = str(Path(directory) / "state")
        try:
            with (artifacts / "server.log").open("w") as log:
                subprocess.run(
                    ["bunx", "start-server-and-test", "just -f ../justfile desktop-web", "http-get://127.0.0.1:1420", scenarios["{{scenario}}"]],
                    cwd="desktop", check=True, env=environment,
                    stdout=log, stderr=subprocess.STDOUT,
                )
        finally:
            state = Path(environment["XDG_STATE_HOME"])
            if state.is_dir():
                shutil.copytree(state, artifacts / "application-state")

# Exercise Study with isolated learning data and cache directories
desktop-study-test: (desktop-test "study")

# Run independent analyses through the public backend process
desktop-analysis-test:
    uv run --no-project python desktop/tests/analysis.py

# Verify isolation of scheduling, analyses, and individual analysis modules
desktop-boundaries:
    uv run --no-project desktop/tests/boundaries.py

# Exercise card organization and real multi-deck file changes
desktop-organization-test: desktop-browser
    uv run --upgrade desktop/tests/organization.py

# Verify source preservation and card boundaries against Pandoc
desktop-source-test:
    cd desktop && bun test tests/source-roundtrip.test.ts tests/paired-cards.test.ts tests/organization.test.ts tests/workspace.test.ts

# Capture and exercise the built native window on an isolated display
desktop-native-test *arguments:
    env -u WAYLAND_DISPLAY xvfb-run -a -s '-screen 0 1600x1200x24' dbus-run-session -- uv run --upgrade desktop/tests/native.py {{arguments}}

# Verify the Study host lifecycle through the built native bridge
desktop-native-study-test:
    env -u WAYLAND_DISPLAY xvfb-run -a -s '-screen 0 1600x1200x24' dbus-run-session -- uv run desktop/tests/native-study.py

# Launch the installed desktop entry and exercise its native export
desktop-installed-test *arguments:
    env -u WAYLAND_DISPLAY xvfb-run -a -s '-screen 0 1600x1200x24' uv run --upgrade desktop/tests/native.py --entry '{{env_var_or_default("XDG_DATA_HOME", env_var("HOME") / ".local/share")}}/applications/dev.math.flashcards.desktop' {{arguments}}

# Update a running temporary installation and verify both native sessions offline
desktop-update-test:
    env -u WAYLAND_DISPLAY xvfb-run -a -s '-screen 0 1600x1200x24' dbus-run-session -- uv run --upgrade desktop/tests/native.py --updates --offline

# Apply the canonical formatters to desktop sources
desktop-format:
    uvx ruff check --fix desktop/backend.py desktop/tests desktop/linux/install.py
    uvx ruff format desktop/backend.py desktop/tests desktop/linux/install.py
    cd desktop && bunx prettier --write src tests/*.ts vite.config.ts index.html
    cd desktop/src-tauri && cargo fmt
