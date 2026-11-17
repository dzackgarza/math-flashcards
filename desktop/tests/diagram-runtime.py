"""Render a Study diagram through the real bridge with an empty home."""

import json
import os
import subprocess
import tempfile
from pathlib import Path
from xml.etree import ElementTree

from evidence import evidence


def main(artifacts: Path) -> None:
    desktop = Path(__file__).resolve().parents[1]
    runtime = (desktop / "runtime.txt").read_text().strip()
    with tempfile.TemporaryDirectory(prefix="flashcards-diagram-runtime-") as directory:
        root = Path(directory)
        home = root / "home"
        home.mkdir()
        workspace = root / "workspace"
        workspace.mkdir()
        diagram = r"\begin{tikzcd} A \arrow[r] & B \end{tikzcd}"
        source = (
            '::: {.front card-id="diagram"}\nDiagram.\n:::\n\n'
            '::: {.back card-id="diagram"}\n' + diagram + '\n:::\n'
        )
        deck = workspace / "Diagram.md"
        deck.write_text(source)
        environment = os.environ | {
            "HOME": str(home),
            "XDG_DATA_HOME": str(home / "data"),
            "XDG_CACHE_HOME": str(home / "cache"),
            "XDG_CONFIG_HOME": str(home / "config"),
            "XDG_STATE_HOME": str(home / "state"),
        }
        result = subprocess.run(
            [runtime, "-I", str(desktop / "backend.py")],
            input=json.dumps({
                "action": "render-diagram", "workspace": str(workspace),
                "path": "Diagram.md", "source": diagram,
            }) + "\n",
            text=True, capture_output=True, env=environment,
        )
        (artifacts / "bridge.log").write_text(result.stderr)
        assert result.returncode == 0, result.stderr
        svg = json.loads(result.stdout)["svg"]
        tree = ElementTree.fromstring(svg)
        assert tree.tag == "{http://www.w3.org/2000/svg}svg"
        assert tree.findall(".//{http://www.w3.org/2000/svg}path")
        (artifacts / "diagram.svg").write_text(svg)
        assert deck.read_text() == source
        misplaced = [
            str(path.relative_to(home)) for path in home.rglob("*")
            if path.is_file() and path.relative_to(home).parts[0]
            not in {"data", "cache", "config", "state"}
        ]
        assert not misplaced, misplaced


if __name__ == "__main__":
    with evidence("diagram-runtime", Path(__file__).parent / "fixtures/study") as artifacts:
        main(artifacts)
