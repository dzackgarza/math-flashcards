# Data Model: In-App Review

This model fixes the vocabulary, the states, and the typed values before any task is
ordered. The bridge declares the types as Pydantic models in `desktop/backend.py`; the
frontend declares the same shapes as Zod schemas in `desktop/src/bridge.ts`.

## Vocabulary

| Term | Meaning | Not to be confused with |
| --- | --- | --- |
| Study | The spaced-repetition function of this feature, and its name in the interface and in code (`study-*` actions, `study.tsx`). | **Review changes**, the existing comparison of a deck with its package (`review` action, `review.tsx`). |
| Card | One front and back pair in a deck file, identified by `card-id`. | An Anki card row. This model has one Anki card for each note. |
| Deck | One Markdown file in the workspace. | An Anki deck in the store, which also exists for each folder. |
| Store | The Anki collection and its media folder for one workspace path. | The cache databases `builds.sqlite3` and `derived.sqlite3`. |
| Host | The long-lived bridge process that holds the store open. | A request process, which serves one request and exits. |
| Scope | What a session studies: the workspace, a folder, or a deck. | |
| Grade | The user's rating of one recall: Again, Hard, Good, or Easy. | |

## Identifiers

| Type | Raw type | Rule |
| --- | --- | --- |
| `CardId` | string | Not empty. Unique in the workspace. Equal to the note GUID in the store. The app creates it with `crypto.randomUUID()`; earlier IDs keep their form. |
| `DeckPath` | string | The existing bridge type: a path relative to the workspace that ends in `.md`, with no `.` or `..` part. |
| `Scope` | `{kind: "workspace"}` \| `{kind: "folder", path}` \| `{kind: "deck", path: DeckPath}` | Maps to one Anki deck name by R5 in `research.md`. |
| `Grade` | `"again"` \| `"hard"` \| `"good"` \| `"easy"` | Maps to Anki's `CardAnswer` ratings in that order. |
| `StoreKey` | `Digest` | The existing digest type, applied to the workspace path. |

## Entities

### Card in the store (Anki note and card)

| Field | Source | Rule |
| --- | --- | --- |
| GUID | `CardId` | Never changes for a note. |
| `Front`, `Back` | Rendered HTML of the card sides | Equal to the package render of the saved deck. |
| Tags | Deck tags and card tags | Replaced on each sync. |
| Deck | From `DeckPath` | `Workspace::…` while the card is in a deck; `Removed` after removal. |
| Schedule | Anki | Written only by Anki's scheduler and undo. Sync never writes it. |

### Deck record

One record for each synced deck, in the collection's config.

| Field | Rule |
| --- | --- |
| `path` | `DeckPath` |
| `inputs` | Map from absolute input path to digest: the deck source, each media file, and the renderer asset identity, as `input_hashes()` gives them. |

A deck is current when every recorded input has its recorded digest. A deck with no
record is not current.

### Scheduling settings

| Field | Type | Constraint |
| --- | --- | --- |
| `new_per_day` | integer | 0 to 9999 (Anki's bound) |
| `reviews_per_day` | integer | 0 to 9999 (Anki's bound) |
| `desired_retention` | number | 0.70 to 0.99 (Anki's bound) |

The settings are one Anki preset shared by every deck. A value outside its bound is
rejected at the bridge boundary with an error; Anki's silent reset to the default is
never reached.

### Store

| Part | Rule |
| --- | --- |
| Directory | `user_data_path("math-flashcards") / "study" / StoreKey` |
| `workspace.txt` | The workspace path that the key came from. Written at creation, checked at open. |
| `collection.anki2` | Created only when the directory does not exist. An existing directory without a readable collection is an error (FR-019). |
| `collection.media/` | Anki's media folder. |
| `backups/` | Anki `.colpkg` backups. |
| Lock file | Held by the host for its lifetime. |

## Card lifecycle

```text
            add to a deck                 first grade            graduate
(no note) ───────────────▶ New ───────────────────▶ Learning ───────────▶ Review
                            ▲                          ▲    ◀───────────    │
                            │                          └──── lapse (Again) ─┘
                            │ ID returns                    (Relearning)
                            │ (schedule restored)
   any state ── removed from the decks ──▶ Removed (suspended, deck `Removed`)
```

| Transition | Owner | Rule |
| --- | --- | --- |
| Add | Sync | A new `CardId` becomes a new note in its deck. |
| Grade | Anki scheduler | Only for the card at the top of the queue. |
| Undo | Anki undo | Only when the last undo step is a grade. |
| Edit, retag | Sync | Fields and tags change; the schedule stays. |
| Move | Sync | The Anki deck changes; the schedule stays. |
| Remove | Sync | Suspend, then move to `Removed`. The schedule stays. |
| Restore | Sync | Move to the deck, then unsuspend. The schedule stays. |

## Invariants

1. For each `CardId` in a current deck, the store has exactly one note with that GUID,
   in that deck's Anki deck, not suspended, with the rendered sides of the saved deck.
2. A note whose `CardId` is in no deck is suspended and in `Removed`.
3. Sync never changes a schedule or a review log row.
4. No operation deletes a note that has a review log row.
5. The store is opened by one process at a time.
6. An Anki deck under `Workspace` exists for each deck file and each folder, and for
   nothing else.
7. The package build and its records are unchanged by study operations.

## Valid and invalid examples

| Case | Result |
| --- | --- |
| A card's back text changes | Valid. Same note, new `Back`, same due date. |
| A card moves from `A.md` to `B/C.md` and both decks are in one sync call | Valid. One move; no removal. |
| The same move, with the two decks in different sync calls | Valid. Removed and restored, or moved, by the order of the calls; the schedule is the same at the end. |
| `A.md` is renamed to `D.md` | Valid. Each card moves to the Anki deck of `D.md`; the Anki deck of `A.md` is removed when empty. |
| A card is deleted, then pasted back with the same ID | Valid. Removed, then restored with its schedule. |
| The same `card-id` is in `A.md` and `B.md` | Invalid. The sync result names both paths; the note stays with the deck that had it first. |
| A grade arrives for a card that is not at the top of the queue | Invalid. `StaleCard` error; the screen fetches the current card. |
| A deck fails to render | Its cards keep their last synced content; the sync result lists the deck. |
| The store directory exists but the collection does not open | Invalid. `StoreUnreadable` error with the path; nothing is created. |
| A second running copy asks for the store | Invalid. `StoreInUse` error. |
| `desired_retention` of 1.0 | Invalid. Rejected at the boundary. |

## Values that cross the bridge

```text
Counts        = { new: int, learning: int, review: int }
GradeLabels   = { again: str, hard: str, good: str, easy: str }     # Anki's text, shown as given
StudyCard     = { card_id: CardId, deck: DeckPath, front: str, back: str,
                  labels: GradeLabels, counts: Counts, undoable: bool }
StudyFinished = { graded_today: int, next_learning_seconds: int | null,
                  counts: Counts, undoable: bool }
StudyNext     = { state: "Card", ...StudyCard } | { state: "Finished", ...StudyFinished }

DeckCounts    = { path: str, kind: "workspace" | "folder" | "deck",
                  counts: Counts, children: DeckCounts[] }

SyncResult    = { added: int, updated: int, moved: int, removed: int, restored: int,
                  failed: { path: DeckPath, message: str }[],
                  duplicates: { card_id: CardId, paths: DeckPath[] }[],
                  pending: int }                                    # decks not yet current

Settings      = { new_per_day: int, reviews_per_day: int, desired_retention: float }

StudyError    = { kind: "StoreInUse" | "StoreUnreadable" | "StaleCard" | "InvalidSettings"
                        | "UnknownScope", message: str }
```

`Counts` come from Anki's queue (`new_count`, `learning_count`, `review_count`) and from
`deck_due_tree()`. `undoable` is true when Anki's undo status names the answer operation.

## Pure and effectful parts

| Part | Kind | Input → output |
| --- | --- | --- |
| Scope to Anki deck name | Pure | `Scope` → deck name |
| Deck path to Anki deck name | Pure | `DeckPath` → deck name |
| Sync plan | Pure | rendered decks, store snapshot (GUID → deck, sides, tags, suspended) → adds, updates, moves, removals, restores, duplicates |
| Render a deck | Effect (Pandoc, LuaLaTeX) | `DeckPath` → rendered cards with IDs, media |
| Apply a sync plan | Effect (store) | plan → `SyncResult` |
| Queue, answer, undo, counts, settings | Effect (store, clock) | Anki calls in R10 |
| Open the store, lock, backup | Effect (files) | `StoreKey` → open collection or `StudyError` |

The sync plan is the only new logic that is not an Anki call or an existing bridge
function. It is a function of two values and is tested with real rendered decks and a
real store.

## Boundary rules

- Each study request is validated by its Pydantic model with `extra="forbid"`, as the
  current requests are. Each response is parsed by its Zod schema.
- Paths go through the existing `workspace_path()` and `deck_path()` checks.
- The host never returns Anki protobuf values. It converts them to the values above.
- The frontend types have no `any` and no `unknown`. The bridge has no `Any`.

## Policies

| Policy | Rule |
| --- | --- |
| Ordering | Anki's queue decides card order. Requests to the host run one at a time, in arrival order. |
| Idempotency | `study-sync` on an unchanged workspace changes nothing and returns zero counts. A repeated `study-answer` for an answered card returns `StaleCard`. |
| Clock | Anki reads the system clock and its own day rollover. The app adds no clock. |
| Time taken | The screen measures the time from showing the front to the grade and sends it with the grade. |
| Conflict | A duplicate ID is reported, never merged. The store lock decides which running copy studies. |
| Retry | No automatic retry. An error reaches the screen with its cause. |
