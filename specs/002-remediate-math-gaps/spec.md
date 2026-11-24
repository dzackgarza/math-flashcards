# Feature Specification: Remediate Mathematical Coverage Gaps

**Feature Branch**: `main`

**Created**: 2026-11-23

**Status**: Draft

**Input**: User description: "Remediate all gaps with new cards"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Recover commutative-algebra foundations (Priority: P1)

The researcher can define and compute with syzygies, module length, and the local invariants in Atiyah–Macdonald dimension theory. The researcher can connect these foundations to resolutions, Castelnuovo–Mumford regularity, and Koszul complexes.

**Why this priority**: The existing geometric applications use these operations, but several definitions and computational links are absent.

**Independent Test**: Give the researcher generators of an ideal, a finite-length module, or a graded module over a polynomial ring. The researcher can construct the relevant syzygy or Koszul object, compute length, and read dimension or regularity from the appropriate data.

**Acceptance Scenarios**:

1. **Given** generators of an ideal, **When** asked for their relations, **Then** the researcher can define the first syzygy module and explain higher syzygies through free resolutions.
2. **Given** a short exact sequence of finite-length modules, **When** asked for the lengths, **Then** the researcher can apply additivity and identify simple composition factors.
3. **Given** a Noetherian local ring, **When** asked for the dimension theorem, **Then** the researcher can state the equality of Krull dimension, Hilbert–Samuel degree, and the parameter number with the required hypotheses.
4. **Given** a graded minimal free resolution, **When** asked for Castelnuovo–Mumford regularity, **Then** the researcher can compute it from the graded Betti numbers.

---

### User Story 2 - Use the arithmetic functions behind the prime number theorem (Priority: P1)

The researcher can define the standard arithmetic functions, form their Dirichlet series, use convolution and partial summation, and convert between the standard asymptotic forms of the prime number theorem.

**Why this priority**: This study subject has no current retrieval coverage.

**Independent Test**: Ask the researcher to recover the identities relating the Möbius and von Mangoldt functions, Chebyshev's functions, and the prime-counting function, and to state the prime number theorem in equivalent forms.

**Acceptance Scenarios**:

1. **Given** a multiplicative arithmetic identity, **When** Dirichlet convolution is required, **Then** the researcher can define convolution and use Möbius inversion correctly.
2. **Given** the logarithmic derivative of the Riemann zeta function, **When** asked for its coefficients, **Then** the researcher can recover the von Mangoldt function and Chebyshev's psi function.
3. **Given** one standard asymptotic statement of the prime number theorem, **When** asked for another, **Then** the researcher can derive the equivalence using partial summation and elementary estimates.

---

### User Story 3 - Apply graded and birational constructions (Priority: P2)

The researcher can use Castelnuovo–Mumford regularity, algebraic Koszul complexes, Rees algebras, and Cox rings in explicit calculations. The researcher can distinguish the toric Cox construction from the general class-group-graded construction.

**Why this priority**: Basic geometric constructions exist, but their algebraic definitions and computational uses are incomplete.

**Independent Test**: Give the researcher a complete intersection, an ideal blowup, or a toric surface. The researcher can construct the relevant complex or graded ring and compute the requested invariant or quotient data.

**Acceptance Scenarios**:

1. **Given** a sequence in a ring, **When** asked for its Koszul complex, **Then** the researcher can give the terms, differential, homology, and the regular-sequence exactness statement.
2. **Given** an ideal in a Noetherian ring, **When** asked for its Rees and associated graded algebras, **Then** the researcher can construct both and relate them to the blowup and exceptional fiber.
3. **Given** a toric surface obtained by blowing up the plane, **When** asked for its Cox ring, **Then** the researcher can give generators, gradings, and the irrelevant ideal.

---

### User Story 4 - Work with arithmetic schemes and cohomological invariants (Priority: P2)

The researcher can pass between projective varieties over the rationals and their integral models, state the Weil conjectures through point counts and cohomology, perform descent, use general valuations, and state local and global duality. The researcher can distinguish established semistable-reduction theorems from more general alteration statements.

**Why this priority**: Existing cards provide many ingredients but do not join them into the required operations.

**Independent Test**: Present an explicit projective equation, a finite-field variety, an elliptic-curve descent, or a valuation extension. The researcher can carry out the construction or state the theorem with correct hypotheses and limits.

**Acceptance Scenarios**:

1. **Given** a projective scheme over the rationals, **When** an integral model is requested, **Then** the researcher can clear denominators, take a flat projective closure, and identify generic and special fibers.
2. **Given** projective space over a finite field, **When** its zeta function is requested, **Then** the researcher can compute it from point counts and verify the Weil statements, including Betti degrees.
3. **Given** an elliptic curve amenable to explicit descent, **When** a Selmer computation is requested, **Then** the researcher can construct the descent maps and determine the stated Selmer group.
4. **Given** a field with a valuation, **When** the valuation is extended or classified, **Then** the researcher can apply the relevant valuation-ring, extension, or Ostrowski statement.

---

### User Story 5 - Complete birational and toric worked examples (Priority: P3)

The researcher can run an explicit higher-dimensional minimal model program, distinguish an Atiyah flop from a flip, and classify normal complete toric surfaces through their fans and cyclic-quotient singularities.

**Why this priority**: The general algorithms and classifications are already strong; the remaining need is computational and global scope.

**Independent Test**: Ask the researcher to perform the stated fan or contraction operations and identify the resulting models, exceptional loci, and endpoints.

**Acceptance Scenarios**:

1. **Given** the blowup of projective three-space at a point, **When** the minimal model program is run, **Then** the researcher can identify each contraction and the final Mori fiber space.
2. **Given** the conifold and its small resolutions, **When** asked for an Atiyah flop, **Then** the researcher can identify the exceptional curve and explain why the operation is a flop.
3. **Given** a complete two-dimensional normal toric variety, **When** its global structure is requested, **Then** the researcher can describe its complete fan, singular cones, resolutions, and projectivity without imposing a finite smooth classification.

### Edge Cases

- Regular local-ring regularity must remain distinct from Castelnuovo–Mumford regularity.
- The generic point of the spectrum of the integers is not an open subscheme; an integral model need not be smooth at every prime.
- General valuation statements must include arbitrary ordered value groups, not only discrete valuations.
- Semistable reduction for abelian varieties must not be confused with unproved general semistable reduction in mixed characteristic.
- A flop is not a flip, and a nef minimal endpoint need not be semiample.
- A finite global list of smooth complete toric surfaces must not be presented as a finite list of all singular normal toric surfaces.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The collection MUST teach first and higher syzygies, minimal graded free resolutions, graded Betti numbers, the Hilbert syzygy theorem, and the Auslander–Buchsbaum and Hilbert–Burch connections, with explicit ideal examples.
- **FR-002**: The collection MUST teach Castelnuovo–Mumford regularity as a numerical invariant for graded modules and coherent sheaves, including the Betti-number formula and computations for named ideals and sheaves.
- **FR-003**: The collection MUST teach the algebraic Koszul complex, its differential and homology, and exactness for regular sequences, with computations and the connection to Tor under the correct hypotheses.
- **FR-004**: The collection MUST teach module length through composition series, additivity in short exact sequences, simple factors, and the relationship among finite length, Artinian modules, and dimension-zero Noetherian rings.
- **FR-005**: The collection MUST teach the Noetherian local dimension theorem, Krull's general height theorem, catenarity in the standard geometric setting, and dimension-zero Artinian ring theory.
- **FR-006**: The collection MUST teach generic fibers, flat projective integral models, spreading out over a localized integer ring, special fibers, and the distinction between the generic-point morphism and an open immersion, with a worked projective example.
- **FR-007**: The collection MUST teach the Weil conjectures from point counts through rationality, the functional equation, Betti degrees, and the Riemann hypothesis, with projective-space and product computations.
- **FR-008**: The collection MUST teach the Möbius and von Mangoldt functions, prime-counting and Chebyshev functions, Dirichlet convolution and inversion, relevant Dirichlet-series identities, partial summation, and the equivalent asymptotic forms of the prime number theorem.
- **FR-009**: The collection MUST teach Selmer groups for abelian varieties and Galois representations with precise local conditions and MUST include a correct explicit descent computation for a named elliptic curve.
- **FR-010**: The collection MUST teach Tate local duality and the Poitou–Tate global duality sequence with hypotheses, duals, and the role of the chosen finite set of places.
- **FR-011**: The collection MUST teach general valuations and valuation rings, equivalence and places, Ostrowski's theorem, and extension of valuations to finite extensions, including ramification and residue degrees.
- **FR-012**: The collection MUST teach semistable reduction and Néron–Ogg–Shafarevich for abelian varieties and MUST distinguish general mixed-characteristic alteration results from full semistable reduction.
- **FR-013**: The collection MUST include a worked higher-dimensional minimal model program and a worked Atiyah flop, identifying all contractions, exceptional loci, and endpoints.
- **FR-014**: The collection MUST teach the global fan description of normal complete toric surfaces, their cyclic-quotient singularities, minimal resolutions, and projectivity.
- **FR-015**: The collection MUST teach general Rees algebras, associated graded algebras, special fibers, finite generation, and the Hilbert–Samuel connection, with an explicit example.
- **FR-016**: The collection MUST teach class-group-graded Cox rings, including torsion and the required choices, and MUST include the Cox ring and irrelevant ideal of the plane blown up at a point.
- **FR-017**: Each new retrieval task MUST supply the mathematical hypotheses, quantifiers, notation, and answer needed to check an attempted response. A source citation MUST NOT replace the mathematical answer.
- **FR-018**: New material MUST preserve the existing authored cards and MUST place each new task with the mathematical subject that owns it.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Every requirement FR-001 through FR-016 has at least one completed retrieval task with an answer that supports the stated operation.
- **SC-002**: Every named example in the acceptance scenarios has a complete computation or a theorem statement whose hypotheses and conclusions can be checked directly.
- **SC-003**: A reader can distinguish every pair of concepts listed under Edge Cases by answering collection content alone.
- **SC-004**: All new cards satisfy the collection's mathematical-content, citation, and rendering requirements without changing existing card identities.

## Assumptions

- Scope is the set of gaps identified in the coverage assessment immediately preceding this request. It is not an attempt to build complete textbook courses in every named subject.
- New cards target a graduate-level mathematical researcher and prioritize definitions, usable theorem statements, constructions, and computations.
- Existing sound cards remain in place. Related new tasks are added instead of replacing their questions.
- Missing proof-reconstruction cards are not treated as gaps unless a proof technique is itself required for one of the stated operations.
- Advanced generalizations are included only where the preceding assessment named their absence. Statements must distinguish theorems, conjectures, and alteration-level results.
