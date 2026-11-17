# Contract: Study Bridge

The study bridge is the interface between the window and the core: the review store and
the writer of the learning record. It extends the existing bridge (`request()` in
`desktop/src/bridge.ts`). The core is the Python package `desktop/study/`; the entry
script `desktop/backend.py` starts its host. Value types are defined in
[data-model.md](../data-model.md). The learning record that these actions write is
defined in [learning-record.md](./learning-record.md). Analyses have their own
contract, [analysis.md](./analysis.md); no analysis action reaches the host.

## Transport

| Rule | Detail |
| --- | --- |
| Entry | The window calls the existing `request` command with an action that starts with `study-`. |
| Routing | The native shell (`lib.rs`) and the Vite middleware (`vite.config.ts`) send every `study-*` action to the host. No other action reaches the host. |
| Host start | `backend.py study-host`, with the release's Python and `-I`, on the first `study-*` request. The app runs as one copy (FR-047), so one host exists. |
| Framing | One JSON request on one line of the host's standard input. One JSON response on one line of its standard output. Diagnostics go to standard error. |
| Order | One request at a time, in arrival order. |
| Response | `{"ok": true, "result": …}` or `{"ok": false, "error": StudyError}`. The shell returns the result as the command's value and the error as its rejection, as JSON. |
| End | The host ends each open session in the record, closes the store, and exits when its standard input closes. A host that exits early makes the pending request fail with the host's diagnostics; the next request starts a new host. |
| Workspace | Each request names its workspace. The host opens the store of a workspace at its first request and holds it until exit. |
| Network | The host opens no network connection (FR-043). |

## Actions

Every request has `action` and `workspace`. Unknown fields are rejected.

| Action | Further request fields | Result | Collection | Learning record |
| --- | --- | --- | --- | --- |
| `study-open` | | `StudyOpen` | Created when no store exists | `store_event`; recovered rows |
| `study-attach` | `choice: { kind: "existing", store: StoreId }` \| `{ kind: "new" }` | `StudyOpen` with state `Open` | Created for `new` | `store_event` |
| `study-sync` | `assets: Digest`, `decks: StudyDeck[]` (at most 8), `paths: DeckPath[]` (complete workspace inventory) | `SyncResult` | Scheduling identities, decks, tags | `card_change`, `content`, `media` |
| `study-counts` | | `DeckCounts` | No | No |
| `study-begin` | `scope: Scope` | `{ session: SessionId, next: StudyNext }` | No | `session`; `presentation` |
| `study-next` | `session: SessionId` | `StudyNext` | No | `presentation` |
| `study-answer` | `session: SessionId`, `presentation: PresentationId`, `grade: Grade`, `timing: Timing` | `StudyNext` for the card after the grade | Grade | `response`; `presentation` |
| `study-undo` | `session: SessionId` | `StudyNext` for the restored card | Undo | `undo`; `presentation` |
| `study-end` | `session: SessionId` | `{}` | No | `session_end` |
| `study-set-settings` | `settings: Settings` | `Settings` | Preset | `setting_change` |
| `study-fit` | | `Fit` | No | No |
| `study-apply-fit` | `parameters: float[]` | `Settings` | Preset parameters | `parameter_set`, `setting_change` |
| `study-copy` | `directory: str` | `StoreCopy` | Closed, copied, opened again | `store_event` |
| `study-viewed` | `card_id: CardId`, `deck: DeckPath`, `shown_ms: int`, `unfocused_ms: int` | `{}` | No | `editor_view` |

No action updates or deletes a row of the learning record.

## Behaviour

### `study-open`

- Finds the store whose current attached path is the workspace path (R4 of
  `research.md`).
- With a store for the path, or with no store on disk, it returns `Open` with the
  absolute paths of the store directory, `record-media/`, and the learning record. The
  native shell adds `record-media/` and `record-assets/` to the asset scope, as it adds
  the workspace for `list`.
- The browser server grants the same scope after an `Open` result from either open or
  attach. `GET /api/study-media?path=<absolute retained file>&name=<authored filename>`
  returns the retained bytes and the authored filename's media type. Paths outside the
  opened stores' media and asset directories return 403, missing files return 404, and
  unknown media types return 415. Real paths determine scope, including symbolic links.
- With stores on disk and none for the path, it returns `Unattached` with a summary of
  each store. It creates nothing.
- A new store gets the settings in R9 before its first queue is built, and the first
  `parameter_set` row with source `anki-default`.
- At each open the host writes the rows that the record lacks: a recovered `response`
  row for each review log row with none, and a `session_end` row with cause `recovered`
  for each session with none.
- An existing directory whose collection or record does not open returns
  `StoreUnreadable`. The host creates nothing in it.

### `study-attach`

- `existing` adds the workspace path to the store's `store.json` as its current path and
  opens the store. A store ID that is not on disk returns `UnknownStore`.
- `new` creates a store for the path. It is the only way to create a store while another
  store exists.
- Neither choice changes or removes another store.

### `study-sync`

- Takes native card values parsed from saved source by `cards()` in
  `desktop/src/cards.ts`. Each deck includes its saved-source digest. The host checks
  that digest against the file before accepting the batch. `pending` is the number
  of paths whose saved source differs from the last accepted version.
- Each native card includes its local image references in `media: string[]`. The shared
  Lezer parser identifies images and reference definitions; the window resolves those
  definitions before sending the batch. The core retains the referenced bytes and their
  authored names. YAML metadata uses the same parser's metadata boundaries and the
  `yaml` library for values.
- With no deck out of date, it changes nothing and returns zero counts.
- `changed_cards` lists the native IDs changed by this call. The window fetches a
  new presentation when this list contains the card on screen. A completed sync
  still delivers this list when another source refresh has begun; changing the
  workspace prevents it from affecting the new workspace's session.
- Records native front and back source with the asset identity named by `assets`.
  Anki notes carry the `card-id`; the app's content record supplies presentation.
- Never changes a schedule or a review log row (invariant 3).
- Sets deck tags and card tags and keeps the tags that Anki's scheduler set (FR-045).
- Writes one `card_change` row for each add, content change, tag change, move, removal,
  and restore, and one `content` row for each front and back pair that the record does
  not hold yet, with its media files.
- A deck whose source, media, or rendering assets cannot be validated or retained is
  listed in `failed` and counts as not current, with the cause shown in the window.

### `study-counts`

- Returns the workspace root with nested folder and deck entries, keyed by native paths.
- Reads each entry's new, learning, and review counts from Anki's due tree. The window
  refreshes them after synchronization and grading.
- A file and folder with the same stem are separate scopes. Internal scheduling names
  follow the path encoding in R5; the window and record retain the native names.

### `study-begin`, `study-next`, `study-end`

- `study-begin` writes a `session` row and returns the first card of the scope, or
  `Finished`. An unknown folder or deck returns `UnknownScope`.
- `study-next` returns the card at the top of Anki's queue for the session's scope, or
  `Finished`.
- Each returned card is one new `presentation` row, written before the response. The row
  holds every field of FR-028 that exists before a grade. A card that is fetched again is
  a new presentation; the earlier row stays with no response.
- `labels` are Anki's interval texts for the four grades of that card.
- `counts` are the remaining new, learning, and review counts of the scope.
- `Finished.next_learning_seconds` is the time until a learning card returns, or null.
- `study-end` writes a `session_end` row with cause `left` or `finished`. A session that
  is not open returns `StaleCard`.

### `study-answer`

- Applies the grade only when `presentation` is the last presentation of the session and
  its card is at the top of the queue. Otherwise it returns `StaleCard` and records
  nothing.
- `timing` is measured by the window. The host sends `reveal_ms + grade_ms` to Anki as
  the answer time and writes the three values, with no limit, to the `response` row
  (FR-029).
- The grade is durable in the collection, and the `response` row is durable in the
  record, when the response is written.
- The result is the next card, as `study-next` would give it.

### `study-undo`

The window starts a new session with the same scope before undoing from an ended
session's finished screen. The completed session remains in the record.

- Reverses the last grade in the collection when Anki's last undo step is a grade,
  writes an `undo` row that refers to the `response` row, and returns the restored card.
  The `response` row stays (FR-031). Otherwise it returns `StaleCard` and changes
  nothing.

### `study-set-settings`

- Rejects a value outside its bound with `InvalidSettings`.
- Applies the values to the one preset that all decks share.
- Writes one `setting_change` row for each value that changed, with the earlier and the
  later value.
- An unchanged value writes nothing. The next presentation reads the updated preset;
  the window refreshes its queue and counts after saving. Changes invalidate grade Undo.

### `study-fit`, `study-apply-fit`

- `study-fit` runs Anki's fit on the whole store and returns the fitted parameters, the
  current parameters, the number of reviews used, and Anki's two accuracy measures for
  each set (R14). It changes nothing.
- Too little history for Anki's fitting code returns `NotEnoughHistory`.
- `study-apply-fit` sets the preset's parameters, writes a `parameter_set` row with
  source `fit` and the measures, and returns the settings. The user rejects a fit by not
  applying it.
- `reviews` is Anki's count of training observations, which excludes an initial
  learning row without a later recall observation. The candidate may equal the
  current parameters. Apply accepts the candidate held by the current host; after
  a host restart, run the fit again. Repeated apply returns `InvalidSettings`.

### `study-copy`

- Writes a complete copy of the store to
  `<directory>/math-flashcards-study-<time>/<store ID>/` (R18): the host closes the
  collection and the record, copies the store directory, and opens both again.
- The copy has the layout of a store. In the `study/` directory of any machine it is in
  the attach list.
- Writes a `store_event` row of kind `copied` with the destination, after the store is
  open again.
- A directory that does not exist or cannot be written returns `CopyFailed` with the
  cause. The store is open and unchanged afterward.
- After a copy, `undoable` is false until the next grade.

### `study-viewed`

- Writes one `editor_view` row for a card that was open in the editor and has left it
  (FR-058). The window measures both times.
- A card ID that the store does not hold is recorded as given: the card can be new and
  not yet saved.

## Errors

| Kind | Meaning | What the window shows |
| --- | --- | --- |
| `CopyFailed` | The copy could not be written. | The cause, with the directory. |
| `StoreUnreadable` | The store exists and its collection or record cannot be opened. | The error, with the store path. |
| `UnknownStore` | The store ID is not on disk. | The error; the list of stores refreshes. |
| `StaleCard` | The request names a presentation, a session, or an undo that is no longer current. | The current card, fetched again. |
| `InvalidSettings` | A setting is outside its bound. | The bound, beside the field. |
| `UnknownScope` | The folder or deck is not in the store. | The error; the tree refreshes. |
| `NotEnoughHistory` | Anki's fitting code needs more reviews. | That statement; nothing changes. |

Failures outside these kinds (a missing runtime, a Pandoc error, an Anki exception) keep
the existing form: the request is rejected with the diagnostic text.

## Native card input

The editor's parser supplies saved card values:

```text
Card = { id: CardId, front: str, back: str, tags: str[] }
StudyDeck = { path: DeckPath, source_hash: Digest, title: str,
              tags: str[], cards: Card[] }
```

`id` is required and not empty. `front` and `back` are the exact Markdown source
slices returned by `cards()`. The host validates paths, saved-source digests, and
workspace-wide identity before applying scheduling changes.

## Window

| Element | Contract |
| --- | --- |
| Entry points | **Study** on the workspace, on each folder, and on each deck in the tree; a **Study** command in the Ctrl-K menu. |
| Keys | Space reveals the answer. 1, 2, 3, 4 select Again, Hard, Good, Easy. Ctrl-Z undoes. E opens the card in the editor. Escape leaves the session. |
| Card | The native `front` source; after reveal, the `back` source below it. Both use the shared editor renderer in read-only mode, with the active macro set and recorded media. |
| Grades | Four buttons, each with its `labels` text. Hidden until reveal. |
| Timing | The window measures, with its monotonic clock, the time from the card on screen to the reveal, the time from the reveal to the grade, and the time in both that the window was hidden or without focus. It sends the three values with the grade. |
| Counts | New, learning, and review counts of the scope, during the session and in the tree. |
| Undo | Enabled when `undoable` is true. When false, its tooltip gives the reason. |
| Finished | States that study for today is complete, the number graded today, and the time until a learning card returns when there is one. |
| Session end | The window sends `study-end` when the user leaves the session and when the queue is finished. |
| Attach | For `Unattached`, the window lists each store with its paths, whether its current path exists, its last use, and its numbers of cards and grades. The user attaches one or starts a new one. Study is unavailable until the choice; the editor keeps working. |
| Settings | New cards per day, reviews per day, and target recall, with their bounds. The path of the learning record and of the store, with a command that opens the folder. A command that runs the fit, shows both sets of measures, and applies the fitted set on the user's choice. **Save a copy** opens the folder picker and writes a copy of the store there. |
| Editor views | When a card leaves the editor (another card is selected, the deck closes, a study session starts, or the window closes), the window sends `study-viewed` with the time the card was open and the time without focus. With no open store, it sends nothing. |
| No scheduling logic | The window shows the labels, counts, and states that the host returns. It computes no interval, no due date, and no order. |
