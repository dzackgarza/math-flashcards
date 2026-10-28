# Update publication

Design: immutable releases with atomic activation.
`desktop/linux/install.py` implements it. `just desktop-install`,
`just desktop-update`, and `just desktop-deploy` run the installer.

## Requirements

An update prepares its complete candidate before publication. A failed
candidate leaves the active installation usable. Running sessions keep their
renderer set and a matching bridge and runtime until restart.

## Installed layout

The installer writes under `$XDG_DATA_HOME/math-flashcards`:

| Path | Contents |
| --- | --- |
| `releases/release-*/bin/desktop` | The native executable |
| `releases/release-*/lib/Math Flashcards/` | The bridge, Lua filter, renderer asset sets, TikZ assets, and `runtime.txt` |
| `releases/release-*/environment/` | The Python environment for the bridge |
| `releases/release-*/launch` | The release launcher, with the runtime command path |
| `active` | A relative symbolic link to the active release |
| `launch` | A dispatcher that runs `active/launch` |

The user command `math-flashcards` links to `launch`. The desktop entry runs
the user command. The icon links to `active/icon.png`.

## Preparation and activation

1. Check the runtime commands: `uv`, `pandoc`, `trash`, `lualatex`, and
   `pdf2svg`.
2. Copy the executable and resources into a new release directory.
3. Create the release environment with `uv venv`. Install the bridge
   dependencies with `uv sync --active --script` at the final installed script
   path.
4. Import the exporter and ask the installed bridge for its renderer asset
   identity. The identity and the archived renderer set must match the prepared
   release.
5. Write the launchers, validate the desktop entry, and publish the stable
   entry points.
6. Replace the `active` link atomically.

A failure before activation sends the release directory to the trash. The
previous release stays active. Activation performs no network work.

## Running sessions

Each release has its own renderer assets. Its `active-assets.json` links to the
asset descriptor of the active release. A running window compares that
descriptor with its own assets. When they differ, the window shows
**Renderer update ready** and continues to export with its original assets. The
next launch uses the new release.

## Acceptance

`just desktop-install-test` and `just desktop-update-test` verify these
conditions:

- A failed real dependency fetch preserves the active executable, bridge,
  renderer inputs, interpreter, launcher, and desktop entry.
- The existing installation still opens, edits, saves, and exports offline.
- A running session keeps its original assets after a successful update and
  shows a restart notice; a new session adopts the complete new set.
- Publication and cleanup preserve authored data, preferences, packages, and
  build provenance.
- The installed entry points and both request adapters use the prepared runtime.
