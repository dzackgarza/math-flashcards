# Update publication

Decision: immutable releases with atomic activation. Owner: the runtime lifecycle
in the startup plan. The user approved this design on 2026-10-26.

## Failure to correct

The installation scenario prepares a real installation, then attempts an update
with a different validated renderer set inside a network namespace. The
dependency fetch fails because GitHub cannot resolve. The installed asset file
has already changed. The installer publishes executable/resources before it
prepares the installed Python environment.

An update must prepare its complete candidate before publication. A failed
candidate must leave the active installation usable. Running sessions must keep
their renderer set and a matching bridge/runtime until restart.

## Alternatives

| Design | Publication | Running sessions | Cost |
| --- | --- | --- | --- |
| Immutable releases, recommended | Prepare the binary, resources, and Python environment at their final release paths; switch one active pointer after verification | Keep their own release and archived renderer set; read a separate active-asset descriptor for the restart notice | Changes the internal installed layout and requires release retention |
| Existing paths with a transaction | Prepare dependencies before changing active files; save and restore the existing files on activation failure | Needs an additional activation protocol so a running frontend cannot receive a different bridge contract or partially replaced resources | Keeps paths but requires coordination across the installer, launchers, and request adapters |

The recommendation keeps `just desktop-install`, `just desktop-update`, the
desktop entry, and the user command as maintenance and launch entry points.
Each release owns its bridge, renderer resources, and prepared environment.
Python dependencies can be installed into an explicit release environment with
`uv sync --active --script`, using the final installed script as the metadata
owner. Activation performs no network work.

The active-asset descriptor is separate from the session's immutable assets.
An existing window can announce an update while exporting with its original
asset identity. The next launch uses the newly activated release.

## Acceptance

- A failed real dependency fetch preserves the active executable, bridge,
  renderer inputs, interpreter, launcher, and desktop entry.
- The existing installation still opens, edits, saves, and exports offline.
- A running session keeps its original assets after a successful update and
  shows a restart notice; a new session adopts the complete new set.
- Publication and cleanup preserve authored data, preferences, packages, and
  build provenance.
- The installed entry points and both request adapters use the prepared runtime.
