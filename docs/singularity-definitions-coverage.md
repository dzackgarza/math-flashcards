# Singularity definitions: coverage assessment

The basic definitions have useful coverage. Their relationships and recognition
tests remain fragmented, and the plt definition contains a mathematical error.
The highest priority is a composite comparison card with separating examples,
followed by a practical discrepancy-computation card.

This assessment concerns complex varieties and effective rational boundaries.
It inspects the Singularities decks, Birational Geometry, Schemes, the numerical
surface discrepancy cards, and uses of singularity classes elsewhere in the decks.

## Existing coverage

| Topic | Evidence and assessment |
| --- | --- |
| Discrepancy, log discrepancy, klt, lc | Birational Classes, singularity-pair-discrepancies: normality, effectiveness, the rational Cartier hypothesis, both discrepancy conventions, and strict transforms are explicit. Good foundation. |
| Terminal and canonical | Birational Classes, card-704cc7c711f84485: correct exceptional-divisor inequalities for varieties with zero boundary. |
| dlt | Birational Classes, singularity-dlt-definition: the existence of a suitable log resolution and the boundary coefficient bound are present. The distinction between one suitable resolution and every resolution needs an example. |
| plt | Birational Geometry, card-9972162b653b2027: present, but incorrect; see below. |
| slc | Birational Classes, card-e65c8bbc605edf10: the reducedness, codimension-one, depth, boundary, and normalization conditions are present. The nodal-curve example supplies a useful contrast with normal lc varieties. |
| Rational singularities | Definition and higher-direct-image criterion are present, together with klt implying rational and rational implying Cohen–Macaulay. |
| lc centers | Definition and identification of their union with the non-klt locus are present. A concrete computation of all centers is not supplied by that card. |
| Thresholds | A definition and resolution formula for lct, with node, cusp, and monomial examples, are present. |
| Surface examples | Du Val equations and quotients, cyclic quotients, simple elliptic singularities, and surface cusps are represented. The A1 and 1/3(1,1) examples explicitly distinguish canonical from terminal and klt from canonical. |
| Research applications | Cone, contraction, base-point-free, and vanishing cards use klt hypotheses. Inversion of adjunction includes the smooth-divisor plt/klt equivalence. K3 moduli uses slc pairs. |
| Local algebra | Schemes contains normality, factoriality, Gorenstein, and Cohen–Macaulay definitions. Their relationship to the birational classes needs a compact comparison. |

Decks: [Birational Classes](../decks/Algebraic%20Geometry/Singularities/Birational%20Classes.md),
[Surface Singularities](../decks/Algebraic%20Geometry/Singularities/Surface%20Singularities.md),
[Local Models and Resolutions](../decks/Algebraic%20Geometry/Singularities/Local%20Models%20and%20Resolutions.md),
[Birational Geometry](../decks/Algebraic%20Geometry/Birational%20Geometry.md),
[Schemes](../decks/Algebraic%20Geometry/Schemes.md).

## Correction required: plt

The current answer additionally requires every divisor of nonpositive discrepancy
to have center in the integral part of the boundary. That condition is false.

The existing A1 example supplies a counterexample: with zero boundary it is klt,
hence plt, but its exceptional curve has discrepancy zero and center at the vertex.
The integral part of the boundary is empty. Thus the current definition contradicts
an example already taught in the collection.

For an effective boundary with coefficients at most one, on a normal variety with
K_X + Delta rational Cartier, plt requires discrepancy greater than minus one
for every exceptional divisor over X. State these hypotheses explicitly.
[Reference: Kollár, Canonical Models, Definition 13](https://web.math.princeton.edu/~kollar/book/chap2.pdf).

## Highest-priority composite cards

### Class hierarchy with simple separating examples

For boundary pairs, organize klt implies plt implies dlt implies lc, and compare
their quantifiers and coefficient conditions in one table. For varieties with
zero boundary, organize terminal implies canonical implies klt implies lc;
explicitly note that klt, plt, and dlt coincide in this case.
[Reference: Kollár, Definition 13 and discussion 13(3)](https://web.math.princeton.edu/~kollar/book/chap2.pdf).

Reuse the existing repertoire:

- A smooth surface with one smooth coefficient-one boundary component separates
  plt from klt.
- The coordinate axes with coefficient one separate dlt from plt: blowing up
  their intersection gives discrepancy minus one. This also explains why the
  dlt definition asks for a suitable resolution rather than every resolution.
- The cone over a smooth plane cubic supplies an lc, non-klt variety, hence
  an lc, non-dlt pair with zero boundary. Its exceptional elliptic curve has
  discrepancy minus one.
- The existing A1 and cyclic quotient examples separate the remaining
  zero-boundary classes.

The cards currently give several ingredients, but the inspected decks do not
assemble this comparison or make all these separations directly retrievable.

### How to test a pair

Combine the definition of a log resolution, the discrepancy equation, the
coefficient of a strict transform, and the finite klt/lc test on a log resolution.
Include the blowup calculation for a smooth center of codimension c:
the exceptional discrepancy is c - 1 minus the boundary multiplicity along
the center. The existing coordinate-axis calculation is the simplest model.
Distinguish discrepancies a from log discrepancies A = a + 1 throughout.

Embedded resolution and simple normal crossings already have cards. A general
log-resolution definition for a pair was not found in the inspected decks.

### Boundary strata, adjunction, and normalization

Extend the same coordinate-axis example to list its lc centers: both axes and
their intersection. Compare with a single smooth coefficient-one component.
Connect these examples to the different and inversion of adjunction.

Then compare a nodal curve as a nonnormal variety with that curve as a boundary
inside a smooth surface. The slc normalization test and the lc pair test answer
different questions. Existing cards contain both examples but do not explicitly
test this distinction.

### Cohomological and local-algebra comparisons

Connect the existing rational-singularity implications with Gorenstein,
rational Cartier, and rational factorial conditions. State which hypotheses
concern canonical divisors and which concern all Weil divisors. Include
counterexamples to invalid converses using the surface repertoire.

Du Bois singularities and epsilon-lc singularities were not found by the
deck-wide terminology search. Add their definitions and research roles after
the core comparisons; give epsilon-lc higher priority when boundedness is in
scope. These omissions do not justify delaying the main composite cards.

## Remediation scope

Correct the plt answer while preserving its card ID. Add the composite
comparisons and extend the existing examples by synthesis. Keep useful authored
derivations and the focused definition cards: they support later diagnosis and
targeted practice. Routine proofs are lower priority than recognizing a class,
checking a theorem's hypotheses, and computing an example.
