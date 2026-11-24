# Content Model

## Card

A card consists of one front and one back with the same unique `card-id`.

- **Front**: A retrieval task that asks for a definition, theorem, construction, comparison, or computation. Optional fields are `tags` and `cite`.
- **Back**: The complete checkable answer, including the hypotheses and notation needed to interpret it.
- **Citation**: A Zotero Better BibTeX key with a precise locator in the front-div `cite` attribute.
- **Owner**: The deck whose mathematical subject contains the question.

## Deck

A deck is one Markdown source with a `title` in frontmatter. Its path determines its subject and Anki deck name. The new Analytic Number Theory deck owns the arithmetic-function and prime-number-theorem tasks. Existing decks own all other tasks.

## Requirement-to-content relationship

Each functional requirement maps to one or more cards. A requirement is complete only when its definitions, operations, hypotheses, and named examples are all retrievable. A keyword mention or a citation without an answer does not satisfy a requirement.

## Validation rules

- Every new card ID is unique across the authored sources and has exactly one front and one back.
- Existing card IDs and sound authored tasks remain unchanged.
- Every formula uses the repository's supported mathematics syntax and macros.
- Every citation key resolves in Zotero and identifies a work that supports the statement.
- Every worked example has internally consistent hypotheses, notation, and conclusion.
- Every theorem distinguishes existence from uniqueness, absolute from relative properties, and proved results from conjectures.
