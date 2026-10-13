# ankdown-for-math is fetched from GitHub via uvx — no local checkout required.
ANKDOWN_REF := "git+https://github.com/dzackgarza/ankdown-for-math"

[private]
default:
    @just --list

# Compile every deck under decks/ into apkg/
build:
    uvx --from "{{ANKDOWN_REF}}" ankdown build decks --output-dir apkg

# Sanity-check that every deck is well-formed new-format Markdown
test:
    python3 .agents/check-decks.py

# CI entry point (used by the pre-push hook)
test-ci: test

# Commit gate entry point
test-commit: test desktop-frontend desktop-source-test desktop-test

# Install the desktop dependencies
desktop-install:
    cd desktop && bun install --frozen-lockfile

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

# Exercise the editor against its real backend with an isolated server
desktop-test:
    cd desktop && bunx start-server-and-test 'just -f ../justfile desktop-web' http-get://127.0.0.1:1420 'uv run tests/workbench.py'

# Verify source preservation and card boundaries against Pandoc
desktop-source-test:
    cd desktop && bun test tests/source-roundtrip.test.ts

# Capture and exercise the built native window on an isolated display
desktop-native-test:
    xvfb-run -a -s '-screen 0 1600x1200x24' uv run desktop/tests/native.py

# Apply the canonical formatters to desktop sources
desktop-format:
    uvx ruff check --fix desktop/backend.py desktop/tests
    uvx ruff format desktop/backend.py desktop/tests
    cd desktop && bunx prettier --write src tests/*.ts vite.config.ts index.html
    cd desktop/src-tauri && cargo fmt
