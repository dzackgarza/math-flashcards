# Implementation Plan: Remediate Mathematical Coverage Gaps

**Branch**: `main` | **Date**: 2026-11-23 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/002-remediate-math-gaps/spec.md`

## Summary

Add new, source-cited retrieval cards for every gap in FR-001 through FR-016. Preserve all existing cards and their identities. Organize the work by mathematical owner: commutative-algebra foundations; analytic number theory; arithmetic schemes and cohomology; and birational, Rees, Cox, and toric constructions. Verify each mathematical assertion at its owner and independently check explicit computations. Finish with the collection's parser, mathematics-rendering, and citation checks.

## Technical Context

**Language/Version**: Markdown with the repository's Pandoc and LaTeX mathematics conventions

**Primary Dependencies**: Existing card parser, MathJax macro set, Zotero citation keys, and the shared Sage container for independent computations

**Storage**: Authored Markdown card sources under `decks/`; no learning-data or application-state changes

**Testing**: Targeted mathematical computation checks during authoring; `just test`, `just check-citations`, and `just lint-prose-citations` at the completed content milestone

**Target Platform**: The existing Markdown card collection and its current renderers

**Project Type**: Mathematical content remediation

**Performance Goals**: None; this feature changes mathematical content only

**Constraints**: Add new cards rather than replace sound authored tasks. Use unique stable card IDs. Put citations in front-div `cite` attributes. Keep every hypothesis, quantifier, and convention needed to check the answer. Do not add proof-reconstruction tasks unless the proof technique is a stated requirement.

**Scale/Scope**: Sixteen mathematical requirements, grouped into four independent content batches. Existing strong coverage remains unchanged except where a stated gap requires a new card.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I–II**: PASS. All content is authored in Markdown and uses the existing parser and renderer.
- **III–IV**: PASS. Existing mathematical and rendering infrastructure is reused; no application fallback or migration is introduced.
- **V**: PASS. Acceptance consists of true mathematical assertions and complete retrieval tasks. Repository checks exercise the actual card sources and renderer.
- **VI–X**: PASS. No learning record, scheduling, interface, or study decision changes. Existing retrieval-practice conventions apply; no new learning claim is made.
- **XI**: PASS. Source and verification decisions are recorded in this feature's `research.md`; mathematical content itself belongs in the owning decks.
- **XII**: PASS for this content-only change. Existing repository checks produce their normal retained evidence. No optimization work is proposed.

## Project Structure

### Documentation (this feature)

```text
specs/002-remediate-math-gaps/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── spec.md
├── checklists/requirements.md
└── tasks.md
```

No external interface contracts are needed.

### Source Code (repository root)

```text
decks/
├── Algebra/
│   ├── Commutative Algebra.md
│   ├── Homological Algebra.md
│   └── Modules and Linear Algebra.md
├── Algebraic Geometry/
│   ├── Arithmetic Geometry.md
│   ├── Birational Geometry.md
│   ├── Cohomology.md
│   ├── Etale Cohomology.md
│   ├── Schemes.md
│   ├── Sheaves and Vector Bundles.md
│   └── Toric Varieties.md
└── Number Theory/
    ├── Algebraic Number Theory.md
    ├── Class Field Theory.md
    └── Analytic Number Theory.md
```

**Structure Decision**: Add cards to the subject that owns each question. Create `Number Theory/Analytic Number Theory.md` because analytic number theory is a distinct study subject and no current deck owns it. Use existing decks for all other material. The feature documents describe the remediation contract; the decks own the mathematical content.

## Complexity Tracking

No constitution violations are retained.
