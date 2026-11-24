# Validation Guide

## Content review

For each requirement FR-001 through FR-016:

1. Locate the new cards in the owning deck.
2. Read the front without the back and produce the requested definition, construction, theorem, or computation.
3. Check the answer for hypotheses, quantifiers, sign and indexing conventions, and exceptional cases.
4. Check the worked examples against the cited source or an independent computation.
5. Confirm that each edge case in the specification is explicitly distinguished.

## Repository validation

Run the fast content checks while each batch is completed:

```bash
just check-math
just check-citations
```

Run the complete Markdown and rendering gate after the full content batch:

```bash
just test
```

Inspect prose-citation candidates and retain mathematical source locators in the `cite` attribute:

```bash
just lint-prose-citations
```

Expected outcomes:

- The parser finds one front and one back for every new card ID.
- Mathematics rendering accepts every new expression.
- Every citation key resolves in the running Zotero library.
- The named computations and theorem statements satisfy the acceptance scenarios in `spec.md`.
