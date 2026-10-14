# UI references

The editor has three panes: a deck tree, a card list, and a card editor. The
references below have the same structure or the same object (a two-sided card),
and each one sets the quality bar for one part of the editor.

## Same structure: library, list, editor

| Reference | What to take |
| --- | --- |
| [Bear](https://bear.app) (Apple Design Award 2017) | Sidebar, note list, and editor share one surface and use hairline separators, not boxed panels. Markdown renders in place while the source stays editable. The note list shows a title and a two-line preview of the body. |
| [Things 3](https://culturedcode.com/things/) (Apple Design Award 2017) | Hierarchy from type weight and white space only. Calm neutral palette with one accent. Short, physical motion when an item moves or completes. |
| [Craft](https://www.craft.do) (Mac App of the Year 2021) | Content blocks read as pages, not form fields. Toolbar actions stay hidden until the cursor is in the block. |
| [Ulysses](https://ulysses.app) | Library, sheet list, and editor are three columns with a direct match to deck tree, card list, and card. Each column collapses with one keystroke. |
| [Linear](https://linear.app) | A desktop tool with high density that still reads as premium: command menu (Ctrl-K), keyboard selection in lists, and one quiet state indicator in place of colored badges. |

## Same object: the two-sided card

| Reference | What to take |
| --- | --- |
| [Mochi](https://mochi.cards) | Markdown flashcards on desktop, iOS, and the web. The card is the central object on screen, and the edit form is secondary. |
| [Orbit](https://withorbit.com) (Andy Matuschak) | Review prompts set as large, centered type on a calm field. This is the model for a card preview. |
| [Noji](https://noji.io) | iOS flashcards with a polished deck list and review flow. Use its deck covers and progress treatment as a model. |

## Platform specifications

- [Apple Human Interface Guidelines: sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)
  and [split views](https://developer.apple.com/design/human-interface-guidelines/split-views):
  the specification for the three-pane layout.
- [GNOME Human Interface Guidelines: boxed lists and sidebars](https://developer.gnome.org/hig/):
  the same pattern on the Linux desktop where the editor runs.
- [Mobbin](https://mobbin.com): screenshot library of production iOS and web
  apps. Search "flashcards" and "notes" to find flows.

## How the editor applies the references

1. The deck tree is a full-height sidebar with a tinted background. The card
   list and the editor are plain columns separated by one hairline.
2. The workspace path is in a menu under the workspace name in the sidebar.
3. The card list shows rendered math: the front on the first line and the back
   in muted text on the second line.
4. The selected card shows its Front and Back as two raised card faces with
   math rendered in place. Click an equation to edit its source.
5. The toolbar shows one status: the save state first, then how the package
   differs from the deck. The status opens a review of the changed cards. Deck
   actions are in one menu at the right of the toolbar and in the deck's
   context menu in the tree.
6. A command menu (Ctrl-K) finds decks, cards, and actions. Edits save
   automatically.
7. Problems in all decks are in a drawer at the right, opened from the sidebar
   footer. Dots in the tree and labels in the card list mark where they are.
8. The type scale has four sizes: 12, 14, 16, and 20 px, set in Inter.
