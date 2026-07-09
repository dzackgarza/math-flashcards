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
