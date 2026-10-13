# Card organization

## Survey and selection

Use rendered card tiles and deck tiles. Open a deck to see its cards; open a card
to edit its separate sides. Selected cards form a group during a move.

[Atlassian's drag-and-drop design guidelines](https://atlassian.design/components/pragmatic-drag-and-drop/design-guidelines/)
recommend visible handles, hover feedback, a lifted drag preview, and an indicator
of the destination. Interactive tiles use a separate handle. Deck targets show
a highlighted border; card targets show a before/after insertion marker.

[Atlassian's accessibility guidelines](https://atlassian.design/components/pragmatic-drag-and-drop/accessibility-guidelines/)
recommend action menus and announcements for the same operations.
[WCAG dragging guidance](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements)
requires an alternative that does not require dragging. Selection controls,
Move, earlier/later buttons, Absorb, and Split provide those alternatives.

| Dependency | Fit |
| --- | --- |
| Atlassian Pragmatic drag and drop | Native drag preview, drop targets, insertion markers, auto-scroll, and live announcements; works with Mantine controls |
| dnd kit | React sortable collections and keyboard sensors; its multiple-container guide supplies the same board pattern |

Selected: Atlassian Pragmatic drag and drop, its hitbox and indicator packages,
and existing Mantine components. This adds organization to the existing editor.

## Operations

Drag a card handle to reorder it. Drag selected cards onto a deck to move the
group. Checkboxes support selection; Shift selects a range. The toolbar provides
the same move and reorder operations. Clear selection keeps the card contents.

Drag a deck handle onto another deck, or use **Absorb into**. Confirmation names
the source and destination. Absorption moves its cards and sends the source file
to the desktop trash. **Split into new deck** creates a deck from selected cards.
**New deck** creates an empty deck. Empty decks remain valid and can receive cards.

Organization saves immediately. **Undo** reverses the last operation. Both sides,
card IDs, tags, and deck metadata remain authored Markdown. File hashes reject
external edits before publication. Every destination is validated before writes;
files are staged, destinations precede sources, and write errors restore published
files. A generated Anki package becomes Unsynced when its source changes.
