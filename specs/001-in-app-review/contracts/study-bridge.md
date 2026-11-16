# Contract: Study Bridge

The study bridge is the interface between the window and the review store. It extends the
existing bridge (`request()` in `desktop/src/bridge.ts`, the `Request` union in
`desktop/backend.py`). Value types are defined in [data-model.md](../data-model.md).

## Transport

| Rule | Detail |
| --- | --- |
| Entry | The window calls the existing `request` command with an action that starts with `study-`. |
| Routing | The native shell (`lib.rs`) and the Vite middleware (`vite.config.ts`) send every `study-*` action to the host. No other action reaches the host. |
| Host start | `backend.py study-host`, with the release's Python and `-I`, on the first `study-*` request. One host for each running copy of the app. |
| Framing | One JSON request on one line of the host's standard input. One JSON response on one line of its standard output. Diagnostics go to standard error. |
| Order | One request at a time, in arrival order. |
| Response | `{"ok": true, "result": …}` or `{"ok": false, "error": StudyError}`. The shell returns the result as the command's value and the error as its rejection, as JSON. |
| End | The host closes the store and exits when its standard input closes. A host that exits early makes the pending request fail with the host's diagnostics; the next request starts a new host. |
| Workspace | Each request names its workspace. The host opens the store of a workspace at its first request and holds it until exit. |

## Actions

Every request has `action` and `workspace`. Unknown fields are rejected.

| Action | Further request fields | Result | Changes the store |
| --- | --- | --- | --- |
| `study-open` | | `{ store: str, media: str, settings: Settings, counts: DeckCounts }` | Creates the store when its directory does not exist |
| `study-sync` | `assets: Digest`, `limit: int` (1 to 8) | `SyncResult` | Yes |
| `study-counts` | | `DeckCounts` | No |
| `study-next` | `scope: Scope` | `StudyNext` | No |
| `study-answer` | `scope: Scope`, `card_id: CardId`, `grade: Grade`, `elapsed_ms: int` (0 or more) | `StudyNext` for the card after the grade | Yes |
| `study-undo` | `scope: Scope` | `StudyNext` for the restored card | Yes |
| `study-set-settings` | `settings: Settings` | `Settings` | Yes |

## Behaviour

### `study-open`

- Returns the absolute paths of the store directory and its media folder. The native
  shell adds the media folder to the asset scope, as it adds the workspace for `list`.
- A new store gets the settings in R9 of `research.md` before its first queue is built.
- An existing directory whose collection does not open returns `StoreUnreadable`. The
  host creates nothing in it.
- A store that another process holds returns `StoreInUse`.
- A store whose `workspace.txt` names another path returns `StoreUnreadable`.

### `study-sync`

- Brings at most `limit` decks that are not current into agreement with their saved
  files, then returns. `pending` is the number of decks still not current.
- With no deck out of date, it changes nothing and returns zero counts.
- Renders with the asset set named by `assets`, by the package render path.
- Never changes a schedule or a review log row (invariant 3).
- A deck that fails to render is listed in `failed` and counts as not current.

### `study-next`

- Returns the card at the top of Anki's queue for the scope, or `Finished`.
- `labels` are Anki's interval texts for the four grades of that card.
- `counts` are the remaining new, learning, and review counts of the scope.
- `Finished.next_learning_seconds` is the time until a learning card returns, or null.
- An unknown folder or deck returns `UnknownScope`.

### `study-answer`

- Applies the grade only when `card_id` is the card at the top of the queue. Otherwise
  it returns `StaleCard` and records nothing.
- The grade is durable when the response is written.
- The result is the next card, as `study-next` would give it.

### `study-undo`

- Reverses the last grade when Anki's last undo step is a grade, and returns the
  restored card. Otherwise it returns `StaleCard` and changes nothing.

### `study-set-settings`

- Rejects a value outside its bound with `InvalidSettings`.
- Applies the values to the one preset that all decks share.

## Errors

| Kind | Meaning | What the window shows |
| --- | --- | --- |
| `StoreInUse` | Another process holds the store. | Study of this workspace is in use by another window. |
| `StoreUnreadable` | The store exists and cannot be opened, or belongs to another path. | The error, with the store path. |
| `StaleCard` | The request names a card or an undo that is no longer current. | The current card, fetched again. |
| `InvalidSettings` | A setting is outside its bound. | The bound, beside the field. |
| `UnknownScope` | The folder or deck is not in the store. | The error; the tree refreshes. |

Failures outside these kinds (a missing runtime, a Pandoc error, an Anki exception) keep
the existing form: the request is rejected with the diagnostic text.

## Render output

The rendered deck that `render()` returns gains the card ID:

```text
Card = { id: CardId, front: str, back: str, tags: str[] }
```

`id` is required and not empty in this app. The exporter fork (`ankdown-for-math`) owns
the model and its Pandoc filter; `desktop/paired-cards.lua` supplies the ID. The package
build ignores `id`, and package GUIDs do not change.

## Window

| Element | Contract |
| --- | --- |
| Entry points | **Study** on the workspace, on each folder, and on each deck in the tree; a **Study** command in the Ctrl-K menu. |
| Keys | Space reveals the answer. 1, 2, 3, 4 select Again, Hard, Good, Easy. Ctrl-Z undoes. E opens the card in the editor. Escape leaves the session. |
| Card | The `front` HTML; after reveal, the `back` HTML below it. Both are typeset by the app's MathJax with the active macro set. Image sources resolve against `media`. |
| Grades | Four buttons, each with its `labels` text. Hidden until reveal. |
| Counts | New, learning, and review counts of the scope, during the session and in the tree. |
| Undo | Enabled when `undoable` is true. When false, its tooltip gives the reason. |
| Finished | States that study for today is complete, the number graded today, and the time until a learning card returns when there is one. |
| Settings | New cards per day, reviews per day, and target recall, with their bounds. |
