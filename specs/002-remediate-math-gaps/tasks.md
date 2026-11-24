---

description: "Tasks for mathematical coverage remediation"

---

# Tasks: Remediate Mathematical Coverage Gaps

**Input**: Design documents from `specs/002-remediate-math-gaps/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md

**Tests**: No application tests are requested. Mathematical assertions and worked examples are verified at their owners; repository content checks run at the batch milestone.

**Organization**: Tasks are grouped by user story and can be completed independently after the shared setup.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Different files and no dependency on an incomplete task
- **[Story]**: The user story that the task implements
- Every task adds new cards while preserving existing card IDs and authored questions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish source, citation, and computational support

- [x] T001 Inventory usable Zotero citation keys and supporting sources for every reference family in `specs/002-remediate-math-gaps/research.md`; record unresolved source needs in that file
- [x] T002 Verify the available Sage-container Macaulay2 and direct-computation workflows for the graded-algebra, toric, finite-field, and descent examples in `specs/002-remediate-math-gaps/research.md`
- [x] T003 Create `decks/Number Theory/Analytic Number Theory.md` with the repository's required title frontmatter and register the new subject in `docs/deck-subjects.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish shared mathematical and card-authoring conventions

- [x] T004 Resolve the fan, divisor-class, and grading conventions for the plane blown up at a point and the conventions for the explicit elliptic-curve descent; record the verified inputs in `specs/002-remediate-math-gaps/research.md`
- [x] T005 Verify the exact theorem scope for general valuations, Poitou–Tate duality, abelian-variety semistable reduction, and mixed-characteristic alterations against the sources mapped in `specs/002-remediate-math-gaps/research.md`

**Checkpoint**: Sources, computations, and theorem boundaries are ready; story implementation can begin

---

## Phase 3: User Story 1 - Recover commutative-algebra foundations (Priority: P1) 🎯 MVP

**Goal**: Make syzygies, length, dimension theory, regularity, and Koszul homology directly retrievable and computable

**Independent Test**: Construct resolutions and Koszul complexes, compute length and regularity, and state the local dimension theorem with correct hypotheses

### Implementation for User Story 1

- [x] T006 [US1] Add syzygy modules, higher syzygies, minimal graded resolutions, Betti numbers, Hilbert syzygy, Auslander–Buchsbaum, Hilbert–Burch, and explicit ideal computations to `decks/Algebra/Homological Algebra.md` and `decks/Algebra/Commutative Algebra.md`
- [x] T007 [US1] Add module length, composition series, additivity, Artinian modules, and dimension-zero Noetherian rings to `decks/Algebra/Modules and Linear Algebra.md` and `decks/Algebra/Commutative Algebra.md`
- [x] T008 [US1] Add the Noetherian local dimension theorem, Krull's general height theorem, catenarity in the geometric setting, and connecting examples to `decks/Algebra/Commutative Algebra.md` and `decks/Algebraic Geometry/Schemes.md`
- [x] T009 [US1] Add numerical Castelnuovo–Mumford regularity, the graded Betti formula, and named ideal/sheaf computations to `decks/Algebraic Geometry/Cohomology.md`
- [x] T010 [US1] Add the algebraic Koszul complex, differential, homology, regular-sequence exactness, and the correctly hypothesized Tor connection to `decks/Algebra/Homological Algebra.md` and `decks/Algebraic Geometry/Sheaves and Vector Bundles.md`

**Checkpoint**: FR-001 through FR-005 are complete and all computations are independently checked

---

## Phase 4: User Story 2 - Use arithmetic functions behind the prime number theorem (Priority: P1)

**Goal**: Establish a working analytic-number-theory toolkit

**Independent Test**: Use convolution, Dirichlet series, and partial summation to convert among the standard forms of the prime number theorem

### Implementation for User Story 2

- [x] T011 [US2] Add arithmetic functions, Dirichlet convolution, Möbius inversion, von Mangoldt and Chebyshev functions, and Dirichlet-series identities to `decks/Number Theory/Analytic Number Theory.md`
- [x] T012 [US2] Add partial summation, the elementary relations among prime-counting and Chebyshev functions, equivalent asymptotic forms of the prime number theorem, and the zeta nonvanishing input to `decks/Number Theory/Analytic Number Theory.md`

**Checkpoint**: FR-008 is complete and every identity has correct summation ranges and asymptotic hypotheses

---

## Phase 5: User Story 3 - Apply graded and birational constructions (Priority: P2)

**Goal**: Complete the algebraic theory and computations for Rees and Cox rings

**Independent Test**: Construct Rees and associated graded algebras and compute the Cox quotient data for the plane blown up at a point

### Implementation for User Story 3

- [x] T013 [US3] Add general Rees algebras, associated graded algebras, special fibers, finite generation, and the Hilbert–Samuel connection with an explicit example to `decks/Algebra/Commutative Algebra.md` and `decks/Algebraic Geometry/Birational Geometry.md`
- [x] T014 [US3] Add class-group-graded Cox rings with torsion and choices, plus the graded Cox ring and irrelevant ideal of the plane blown up at a point, to `decks/Algebraic Geometry/Toric Varieties.md` and `decks/Algebraic Geometry/Birational Geometry.md`

**Checkpoint**: FR-015 and FR-016 are complete; the fan, grading, and irrelevant ideal agree

---

## Phase 6: User Story 4 - Work with arithmetic schemes and cohomological invariants (Priority: P2)

**Goal**: Connect arithmetic-scheme operations, Weil statements, descent, duality, valuations, and reduction theorems

**Independent Test**: Build an integral model, compute finite-field zeta functions, perform a named descent, and state general valuation, duality, and reduction theorems with correct limits

### Implementation for User Story 4

- [x] T015 [US4] Add generic-point base change, flat projective integral models, spreading out, special fibers, projectivity under base change, and a worked equation to `decks/Algebraic Geometry/Schemes.md` and `decks/Algebraic Geometry/Arithmetic Geometry.md`
- [x] T016 [P] [US4] Add the point-count definition of finite-field zeta functions, the complete Weil statement including Betti degrees, the trace-formula connection, and projective-space and product computations to `decks/Algebraic Geometry/Etale Cohomology.md`
- [x] T017 [US4] Add abelian-variety and Galois-representation Selmer groups with local conditions and a verified explicit elliptic-curve descent to `decks/Algebraic Geometry/Arithmetic Geometry.md`
- [x] T018 [P] [US4] Add Tate local duality and the Poitou–Tate sequence with finite-set, dual-module, and cohomological hypotheses to `decks/Number Theory/Class Field Theory.md`
- [x] T019 [P] [US4] Add general valuations, valuation rings, equivalence and places, Ostrowski's theorem, and finite-extension valuation formulas to `decks/Number Theory/Algebraic Number Theory.md`
- [x] T020 [US4] Add abelian-variety semistable reduction and Néron–Ogg–Shafarevich, plus a precise comparison with mixed-characteristic alteration results, to `decks/Algebraic Geometry/Arithmetic Geometry.md` and `decks/Algebraic Geometry/Curves and Surfaces.md`

**Checkpoint**: FR-006, FR-007, and FR-009 through FR-012 are complete; no general mixed-characteristic semistable-reduction claim is overstated

---

## Phase 7: User Story 5 - Complete birational and toric worked examples (Priority: P3)

**Goal**: Add the missing higher-dimensional MMP computation and global singular-toric description

**Independent Test**: Run the stated threefold MMP, identify an Atiyah flop, and reconstruct a normal complete toric surface from its fan

### Implementation for User Story 5

- [x] T021 [US5] Add the higher-dimensional MMP run for the point blowup of projective three-space and a worked Atiyah flop to `decks/Algebraic Geometry/Birational Geometry.md`
- [x] T022 [P] [US5] Add the global complete-fan description of normal toric surfaces, cyclic-quotient singularities, minimal resolutions, projectivity, and weighted-projective-plane examples to `decks/Algebraic Geometry/Toric Varieties.md`

**Checkpoint**: FR-013 and FR-014 are complete and the smooth classification is not applied to singular surfaces

---

## Phase 8: Cross-Cutting Mathematical and Repository Review

**Purpose**: Check the whole remediation against the specification and the real card pipeline

- [x] T023 Review every new card against FR-001 through FR-018 and the edge cases in `specs/002-remediate-math-gaps/spec.md`; repair missing hypotheses, ambiguous retrieval tasks, and unsupported claims in the owning `decks/**/*.md` file
- [x] T024 Recheck every explicit syzygy, regularity, descent, zeta, Rees, Cox, MMP, and toric computation against its source or independent computation and record the decisive verification in `specs/002-remediate-math-gaps/research.md`
- [ ] T025 Run `just check-math`, `just check-citations`, `just lint-prose-citations`, and the milestone `just test`; repair all content failures in the owning files
  - `just check-math` and `just test` pass. The prose-citation shortlist was reviewed. `just check-citations` still rejects 45 pre-existing cited works without PDF attachments; no source introduced by T006–T022 is among them. The remaining work belongs to those older citation records and is tracked by issue #6.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup**: No dependencies
- **Foundational**: Depends on Setup and blocks all story work
- **User Stories 1–5**: Depend on Foundational; different-file tasks can run in parallel
- **Cross-Cutting Review**: Depends on all story tasks

### User Story Dependencies

- **US1**: Independent
- **US2**: Independent
- **US3**: Uses the verified Cox conventions from T004
- **US4**: Uses the verified descent conventions from T004 and theorem boundaries from T005
- **US5**: Independent

### Parallel Opportunities

- T013 and T014 can run in parallel
- T015 through T020 can run in parallel by owning file, except tasks sharing `Arithmetic Geometry.md` or `Curves and Surfaces.md` must coordinate their edits
- US1, US2, US3, and US5 can proceed independently after T004 and T005

## Implementation Strategy

1. Complete source and convention verification before authoring.
2. Complete US1 and US2 first because they supply absent foundations.
3. Add the remaining independent batches without changing existing cards.
4. Perform one cross-requirement mathematical review before the repository milestone checks.
5. Complete only when every requirement has usable retrieval coverage and all content checks pass.
