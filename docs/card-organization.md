# Card organization

## Design

Organization happens in the editor's deck tree and card list. Decks in the tree
and cards in the list are drag sources; decks are drop targets for cards and other
decks, and cards are drop targets for reordering.

[Atlassian's drag-and-drop design guidelines](https://atlassian.design/components/pragmatic-drag-and-drop/design-guidelines/)
recommend hover feedback, a lifted drag preview, and an indicator of the destination.
Deck targets show a highlighted outline; card targets show a before/after
insertion line. Folders expand while a drag hovers over them, and the tree and
card list scroll near their edges. Announcements report each completed change.

| Dependency | Fit |
| --- | --- |
| Atlassian Pragmatic drag and drop | Native drag preview, drop targets, insertion markers, auto-scroll, and live announcements; works with Mantine's tree |
| dnd kit | React sortable collections and keyboard sensors; its multiple-container guide supplies the same board pattern |

Selected: Atlassian Pragmatic drag and drop, its hitbox and indicator packages,
and Mantine's `Tree`.

The window sets `dragDropEnabled: false` so the webview handles HTML drag events.
[Tauri's window configuration](https://v2.tauri.app/reference/config/#dragdropenabled)
documents the native handler switch.

## Operations

Drag a card in the list to reorder it. Drop it on a deck in the tree to move it to
the end of that deck. Ctrl-click toggles a card in the selection; Shift-click
selects a range. Dragging a selected card moves the whole selection.

Drag a deck onto another deck to merge them. Confirmation names the source and
destination. The merge moves every card and sends the source file to the desktop
trash. **New deck** creates an empty deck; empty decks remain valid and can
receive cards. Splitting a deck is a new deck followed by a move.

Organization saves immediately. **Undo** reverses the last operation. The open
deck must have no unsaved edits. Both sides, card IDs, tags, and deck metadata
remain authored Markdown. The open deck contributes the hash it was loaded with,
so a disk edit after loading rejects the change, as it does for a save. Every
destination is validated before writes; files are staged, destinations precede
sources, and write errors restore published files. A generated Anki package
becomes Unsynced when its source changes.
