# Shared Zettlr rendering in the flashcard editors

Make every rendering behavior in the Zettlr fork available in the flashcard
editors through the same implementation.

Derive the scope from the fork's actual code. Include its renderers,
decorations, widgets, styles, nested editors, and the selection and editing
behavior that controls rendered content.

## Completion conditions

- [ ] Inspect every rendering entry point and its dependencies. Account for
  each in the shared implementation.
- [ ] Make both apps use that implementation. Neither app may retain a separate
  rendering implementation or supply one through an override.
- [ ] Limit app adapters to external services. Adapters cannot omit, replace,
  or disable rendering to make integration easier.
- [ ] Implement all services required by the flashcard app. A missing service
  is unfinished work.
- [ ] Verify every rendering behavior in the actual card editors against the
  fork, including editing and source reveal. Selected examples and passing
  tests do not establish complete coverage.
- [ ] Preserve the fork's behavior, then rebuild and verify the installed
  flashcard app.

Extraction is an intermediate step. Any rendering behavior still exclusive to
Zettlr means the task remains incomplete.

# Definition-card coverage

Every technical term used in a card must have a definition card. The collection
does not meet this requirement, and no complete inventory of missing terms
exists.

## Completion conditions

- [ ] Read every card and extract every technical term it uses.
- [ ] Check whether each extracted term has a definition card.
- [ ] Add one definition card for each term without one: the term on the front,
  its definition on the back.
- [ ] Preserve existing card IDs, tags, and deck placement.
- [ ] Run `just test`.
