"""Stage the maintained Pandoc TikZ renderer and Quiver TeX package for release.

This runs during networked installation, never during opening, saving, or
exporting a deck. The source of TikZ rendering remains pandoc-config's Lua
filter and macro set, rather than another LaTeX implementation in this app.
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path
from urllib.request import urlopen

import tomllib


def main() -> None:
    desktop = Path(__file__).resolve().parents[1]
    shared = desktop / ".renderer"
    fork = desktop.parent.parent / "visual-tikz-editor" / "vendor" / "quiver"
    manifest = tomllib.loads((fork / "PROVENANCE.toml").read_text())
    commit = manifest["upstream_commit"]
    assert len(commit) == 40 and all(ch in "0123456789abcdef" for ch in commit)
    # Match the TeX exporter to the *same* Quiver revision as the local editor,
    # including its 2-cell "nfold" and "between" options.
    url = f"https://raw.githubusercontent.com/varkor/quiver/{commit}/package/quiver.sty"
    with urlopen(url, timeout=40) as response:
        package = response.read()
    if not all(
        token in package
        for token in (
            b"\\ProvidesPackage{quiver}",
            b"between/.style",
            b"\\usetikzlibrary{nfold}",
        )
    ):
        raise ValueError(
            "The Quiver package does not support the editor's exported arrows."
        )

    target = desktop / "tikz-assets"
    with tempfile.TemporaryDirectory(prefix=".tikz-stage-", dir=desktop) as temporary:
        stage = Path(temporary) / "tikz-assets"
        stage.mkdir()
        shutil.copytree(shared / "styles", stage / "styles")
        shutil.copy2(shared / "filters" / "tikzcd.lua", stage / "tikzcd.lua")
        shutil.copy2(
            shared / "templates" / "standalone-tikz.tex",
            stage / "standalone-tikz.tex",
        )
        (stage / "styles" / "vendor" / "quiver.sty").write_bytes(package)
        (stage / "provenance.json").write_text(
            json.dumps(
                {"quiver_commit": commit, "source": "pandoc-config/main"},
                sort_keys=True,
            )
            + "\n"
        )
        if target.exists():
            shutil.rmtree(target)
        stage.replace(target)
    print(f"Prepared Quiver {commit} and the shared Pandoc TikZ renderer.")


if __name__ == "__main__":
    main()
