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
test-commit: test

# Install the desktop dependencies
desktop-install:
    cd desktop && bun install --frozen-lockfile

# Run the native desktop app
desktop-dev:
    cd desktop && bunx tauri dev

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

# Exercise the editor against its real backend; serve desktop-web first
desktop-test:
    uv run desktop/tests/workbench.py

# Apply the canonical formatters to desktop sources
desktop-format:
    uvx ruff check --fix desktop/backend.py desktop/tests/workbench.py
    uvx ruff format desktop/backend.py desktop/tests/workbench.py
    cd desktop && bunx prettier --write src vite.config.ts index.html
    cd desktop/src-tauri && cargo fmt
