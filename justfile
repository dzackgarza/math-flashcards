[private]
default:
    @just --list

# Compile every deck under decks/ into decks/apkg/
build: desktop-dependencies
    "$(uv python find --script desktop/backend.py)" desktop/backend.py build decks

# Sanity-check that every deck is well-formed new-format Markdown
test: check-math
    uv run --upgrade .agents/check-decks.py

# Reject TeX that MathJax cannot render, such as an undefined macro
check-math: desktop-dependencies
    cd desktop && bun scripts/check-math.ts ../decks

# Push gate entry point
test-push: test

# Commit gate entry point; installs the verified build so the menu app matches the commit
test-commit: test desktop-frontend desktop-source-test desktop-editor-test desktop-test desktop-organization-test desktop-update

# Install the desktop build dependencies
desktop-dependencies:
    [ -d desktop/.parser ] || env -u GIT_INDEX_FILE git clone --quiet --filter=tree:0 --sparse --branch develop https://github.com/dzackgarza/Zettlr-pandoc-mathjax desktop/.parser
    env -u GIT_INDEX_FILE git -C desktop/.parser sparse-checkout set vendor/lezer-markdown-pandoc
    env -u GIT_INDEX_FILE git -C desktop/.parser pull --quiet --ff-only
    cd desktop && bun update
    cd desktop/src-tauri && cargo update --quiet
    uv run --upgrade desktop/backend.py prepare

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
desktop-editor-test:
    cd desktop && bunx start-server-and-test 'just -f ../justfile desktop-web' http-get://127.0.0.1:1420 'uv run --upgrade tests/editor.py'

# Exercise the editor against its real backend with an isolated server
desktop-test scenario="full":
    #!/usr/bin/env python3
    import os
    import subprocess
    import tempfile
    from pathlib import Path
    flags = {"full": "", "startup": " --startup"}
    environment = os.environ.copy()
    environment.setdefault("UV_CACHE_DIR", subprocess.check_output(["uv", "cache", "dir"], text=True).strip())
    environment.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(Path(os.environ.get("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "ms-playwright"))
    with tempfile.TemporaryDirectory(prefix="flashcards-browser-cache-") as directory:
        environment["XDG_CACHE_HOME"] = directory
        subprocess.run(
            ["bunx", "start-server-and-test", "just -f ../justfile desktop-web", "http-get://127.0.0.1:1420", "uv run --upgrade tests/workbench.py" + flags["{{scenario}}"]],
            cwd="desktop", check=True,
            env=environment,
        )

# Exercise card organization and real multi-deck file changes
desktop-organization-test:
    uv run --upgrade desktop/tests/organization.py

# Verify source preservation and card boundaries against Pandoc
desktop-source-test:
    cd desktop && bun test tests/source-roundtrip.test.ts tests/paired-cards.test.ts tests/organization.test.ts tests/workspace.test.ts

# Capture and exercise the built native window on an isolated display
desktop-native-test *arguments:
    xvfb-run -a -s '-screen 0 1600x1200x24' uv run --upgrade desktop/tests/native.py {{arguments}}

# Launch the installed desktop entry and exercise its native export
desktop-installed-test *arguments:
    xvfb-run -a -s '-screen 0 1600x1200x24' uv run --upgrade desktop/tests/native.py --entry '{{env_var_or_default("XDG_DATA_HOME", env_var("HOME") / ".local/share")}}/applications/dev.math.flashcards.desktop' {{arguments}}

# Update a running temporary installation and verify both native sessions offline
desktop-update-test:
    xvfb-run -a -s '-screen 0 1600x1200x24' dbus-run-session -- uv run --upgrade desktop/tests/native.py --updates --offline

# Apply the canonical formatters to desktop sources
desktop-format:
    uvx ruff check --fix desktop/backend.py desktop/tests desktop/linux/install.py
    uvx ruff format desktop/backend.py desktop/tests desktop/linux/install.py
    cd desktop && bunx prettier --write src tests/*.ts vite.config.ts index.html
    cd desktop/src-tauri && cargo fmt
