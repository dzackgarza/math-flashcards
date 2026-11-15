# Convex geometry coverage

The cards contain useful toric definitions and strong Mori applications, but
the foundations are uneven. Some definitions are wrong, and the relationships
among divisor cones need a connected treatment for research use.

This assessment covers the Toric Varieties, Divisors, and Birational Geometry
decks, with searches across the maintained decks for the foundational terms.

## Existing coverage

| Topic | Assessment |
| --- | --- |
| Convex sets and cones | Present, but definitions need correction |
| Rational polyhedral and dual cones | Present; generator/inequality computations need development |
| Faces, facets, supporting hyperplanes | Present mainly in the polyhedral setting |
| Extremal rays and faces | Used extensively; no standalone general definition found in the inspected cards |
| Fans | Substantial coverage: smoothness, simpliciality, completeness, normal fans, orbit correspondence, subdivisions |
| Nef and ample cones | Curve-cone duality and ample-as-nef-interior are present |
| Effective, pseudoeffective, big, movable cones | No connected definition-and-comparison treatment found |
| Concrete Mori cones | Useful examples on plane blowups, Hirzebruch surfaces, products; Fano and K3 boundary cases |
| General convex tools | Separation, bipolarity, relative interior, lineality, and finite generators versus inequalities need coverage |

## Corrections to existing cards

All card identifiers below belong to Toric Varieties.

| Card | Required correction |
| --- | --- |
| card-364a052db48b5781, convex set | Require $0\le t\le1$ and nonnegative coefficients in convex combinations. The finite-combination criterion works in every dimension. |
| card-58d7494c921916ce, convex cone | Scaling stability alone does not imply convexity. Add closure under addition, equivalently under nonnegative linear combinations. |
| card-ced0d59dc309e7b8, worked cone | The input repeats one vector, while the answer uses a two-dimensional cone, incompatible monomials and equations, and a wrong dimension. Reconcile these while preserving the perpendicular-vector and semigroup calculation route. The displayed rotation is a quarter-turn, not a half-turn. |
| card-0f87c32fe5c35f28, fan | Require intersections to be faces of both cones; state the finiteness convention for finite-type toric varieties. |
| card-06dfd60dc8d94782, normal fan | Its maximum convention must be reconciled with the inward-normal/minimum convention used for divisor polytopes and support functions elsewhere. |
| card-316c2a3bb1f98d47, star subdivision | Do not retain a cone that is being subdivided. Keep unaffected cones and replace affected cones by the appropriate cones over faces. |
| card-e402b717c6505552, smooth Fano polytope | Facet vertices must form a basis of the ambient lattice $N$, not an affine lattice. Distinguish the Fano polytope in $N_{\mathbb R}$ from its polar in $M_{\mathbb R}$. |

Reference: [Cox–Little–Schenck, Toric Varieties](https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf),
especially the cone, fan, and polytope constructions.

## Missing foundations

The following should be recalled and used in computations, rather than learned
chiefly through proof reconstruction:

- Convex and conical hulls; dimension, span, lineality; pointed versus
  full-dimensional cones; closure and relative interior.
- Polyhedra versus polytopes; rationality relative to a lattice; finite
  generators versus finite homogeneous inequalities for polyhedral cones.
- Faces versus exposed faces. A subcone $F\subset C$ is a face when
  $x,y\in C$ and $x+y\in F$ force $x,y\in F$. An extremal ray is a
  one-dimensional face. A nonnegative functional exposes $C\cap u^\perp$.
  Every polyhedral face is exposed; this fails for general closed convex cones.
- Duality and separation: for a convex cone in a finite-dimensional real
  vector space, $C^{\vee\vee}=\overline C$. Use this to convert generators
  to inequalities and detect supporting faces.
- Gordan's lemma and Hilbert bases. Primitive ray generators need not
  generate the lattice-point monoid: the cone on $(1,0),(1,2)$ also needs
  $(1,1)$. This distinction is essential when constructing affine toric rings.
- Fan support, refinements, normal fans, and coherent support functions.
  Completeness does not imply projectivity in general.

## Cone relationships to add

For a smooth complex projective variety, keep divisor classes in
$N^1(X)_{\mathbb R}$ and curve classes in $N_1(X)_{\mathbb R}$, paired by
intersection. The cards already state the first duality and the ample-interior
identity, but should connect them to the other cones:

$$
\operatorname{Nef}(X)=\overline{\operatorname{NE}}(X)^\vee,\qquad
\operatorname{Amp}(X)=\operatorname{Int}\operatorname{Nef}(X),\qquad
\overline{\operatorname{Amp}(X)}=\operatorname{Nef}(X).
$$

$$
\overline{\operatorname{Eff}}(X)
=\overline{\operatorname{Cone}\{[D]:D\text{ effective}\}},\qquad
\operatorname{Big}(X)=\operatorname{Int}\overline{\operatorname{Eff}}(X).
$$

The closed movable divisor cone is generated, then closed, from classes of
divisors with nonempty complete linear systems and no fixed divisorial
components. It satisfies

$$
\operatorname{Nef}(X)\subseteq
\overline{\operatorname{Mov}}^{\,1}(X)\subseteq
\overline{\operatorname{Eff}}(X).
$$

On smooth surfaces the first inclusion is equality; in higher dimension it
can be strict. These positivity relationships belong alongside the definitions,
with examples distinguishing their boundaries.
[Reference: Ein–Lazarsfeld–Mustaţă–Nakamaye–Popa](https://www.math.stonybrook.edu/~roblaz/Reprints/Ein.Laz.Mustata.Nakamaye.Popa.AILB.pdf).

Movable divisors and movable curves belong to different spaces. The
pseudoeffective divisor cone is dual to the closed movable curve cone over
$\mathbb C$, rather than to the whole curve cone.
[Reference: BDPP](https://arxiv.org/abs/math/0405285).

Additional distinctions:

- Strict nefness tests positivity on actual integral curves. Kleiman tests
  every nonzero class in the closed curve cone.
- Nef does not imply semiample. A nontorsion degree-zero line bundle on an
  elliptic curve is nef but no positive power has a section. Semiampleness
  of a particular line bundle is not numerical.
- Pseudoeffectivity does not assert that a specified divisor has a section.
- On complete toric varieties, nef Cartier divisors are globally generated.
  This is a special theorem.
- Relative curve and nef cones test curves contracted by a morphism $X\to S$.

## Applications and priority

First repair the existing definitions and worked cone example. Then add the
extremal-ray and duality foundations, followed by a connected cone dictionary.
Use the existing surface computations as anchors:

- Compute effective, nef, ample, and big cones in the same coordinates on
  $\mathbb P^1\times\mathbb P^1$ and $\operatorname{Bl}_p\mathbb P^2$.
- Use the exceptional divisor for effective but not nef, the line pullback
  for nef and big but not ample, and a fiber for nef but not big.
- Find a supporting nef divisor for a contraction and identify the curves
  it annihilates; explain the role of semiampleness.
- Contrast rational polyhedral toric/Fano examples with nonpolyhedral
  examples. Distinguish infinitely many rays from irrational boundary rays,
  and retain the cone theorem's restriction to the canonical-negative region.
- Compute a dual cone, its lattice-point generators, and its affine toric
  chart; distinguish the real convex calculation from the lattice calculation.
- Follow these with relative cones and explicit wall/chamber examples in
  toric geometry or Mori dream spaces.
