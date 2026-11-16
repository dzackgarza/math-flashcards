# Quickstart: Validate In-App Review

These scenarios prove the feature through the real window, the real bridge, and a real
store. Values and actions are defined in [data-model.md](./data-model.md) and
[contracts/study-bridge.md](./contracts/study-bridge.md).

## Prerequisites

- `just desktop-dependencies` has run. It installs the bridge environment, which includes
  the `anki` wheel after this feature.
- Every command below uses a temporary `XDG_DATA_HOME` and `XDG_CACHE_HOME` and a copy of
  deck files in a temporary workspace. A run without the data override writes to the
  real review history.

## Automated scenario

```bash
just desktop-study-test
```

The recipe starts `just desktop-web` and runs `desktop/tests/study.py` against it in a
browser. `just test-commit` includes it.

| Step | Expected result |
| --- | --- |
| Open a workspace of fixture decks that was never studied | The tree shows a new count on each deck and folder; no learning or review count. |
| Select **Study** on the workspace | The front of one card shows. The back and the grades are hidden. |
| Press Space | The back shows. Four grades show, each with an interval label. |
| Press 3 | The next card shows. The store has one review log row. The card's stored interval agrees with the label that Good showed. |
| Press Ctrl-Z | The first card returns. The store has no review log row. |
| Grade a card, then end the bridge host with `SIGKILL` | After the window's next request, the grade is in the store. |
| Grade a card Again and wait for its learning delay | The same card returns in the session. |
| Study a card with a macro equation and a TikZ-cd diagram | The equation and the diagram render. A screenshot goes to `desktop/test-artifacts/`. |
| Stop the app; set several cards due today with the `anki` library; start the app | The tree shows review counts for their decks and folders. |
| Edit the back of a reviewed card in the editor and save | The store shows the new back within 10 seconds, with the same due date. |
| Move a reviewed card to another deck by editing the files on disk | The card's Anki deck changes; its due date and review log stay. |
| Rename a deck with reviewed cards | Each card keeps its due date. |
| Delete a reviewed card from its deck, then paste it back | The card leaves the counts, then returns with the same due date. |
| Put one `card-id` in two decks | The sync result names both decks. The note stays with the first deck. |
| Set new cards per day to 3 and study the workspace | Exactly 3 new cards are offered. |
| Set target recall to 1.0 | The field shows its bound; the stored setting is unchanged. |
| Start a second bridge host on the same store | Its first request returns `StoreInUse`. |
| Replace `collection.anki2` with an unreadable file and open the workspace | The window shows the error with the store path. The file is unchanged. |
| Select **Rebuild cached data** | The store and its review log are unchanged. |
| Run Anki's database check on the store | No problem is reported. |
| Generate a package for a studied deck | The package and its status are as before this feature. |

## Manual check on the full workspace

```bash
XDG_DATA_HOME="$(mktemp -d)" just desktop-web
```

Open `http://127.0.0.1:1420` and the repository's `decks/` folder.

| Check | Expected result | Criterion |
| --- | --- | --- |
| First preparation of all 68 decks | Progress shows; the editor stays usable. Record the time. | SC-006 |
| Reload after preparation | Counts show within 2 seconds. | SC-006 |
| Grade 20 cards | The next card is readable within 0.5 seconds after each grade. | SC-002 |
| Total of the tree's new counts | Equal to the number of cards in the decks, limited by the daily setting. | SC-006 |

## Native check

```bash
just desktop-native-test
```

The native scenario gains one study step: start a session in the built window, grade a
card, and confirm the review log row. It proves the host route in `lib.rs` and the media
scope, which the browser scenario does not use.
