# Location of the ankdown-for-math checkout (override with ANKDOWN_DIR).
ANKDOWN := env_var_or_default("ANKDOWN_DIR", home_dir() / "gitclones/ankdown-for-math")

[private]
default:
    @just --list

# Compile every deck under decks/ into apkg/
build:
    #!/usr/bin/env bash
    set -euo pipefail
    mkdir -p apkg
    while IFS= read -r d; do
      name=$(printf '%s' "$d" | sed 's#^decks/##; s#/#__#g; s#\.md$##')
      pandoc --lua-filter "{{ANKDOWN}}/ankdown/ankdown.lua" "$d" -t plain \
        | python3 "{{ANKDOWN}}/ankdown/cli.py" compile --output "apkg/$name.apkg"
    done < <(find decks -name '*.md')

# Sanity-check that every deck is well-formed new-format Markdown
test:
    python3 .agents/check-decks.py

# CI entry point (used by the pre-push hook)
test-ci: test
