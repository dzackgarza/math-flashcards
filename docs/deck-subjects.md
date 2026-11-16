# Deck subjects

`decks/` is the workspace folder. Its Markdown files are the flashcard sources;
its `apkg/` subfolder holds generated packages. The directory hierarchy
follows the subject branches of the local Zotero library. Zotero's `Textbooks`
collection supplies the main branches; `Logic` supplies Set Theory.

| Zotero collection | Deck location |
| --- | --- |
| Textbooks / Algebra | Algebra |
| Textbooks / Category Theory | Category Theory.md |
| Textbooks / Analysis | Analysis |
| Textbooks / Geometry / Differential Geometry | Geometry / Manifolds.md |
| Textbooks / Topology | Topology |
| Textbooks / Number Theory / Algebraic | Number Theory / Algebraic Number Theory.md; Class Field Theory.md; Function Fields.md; Lattices and Quadratic Forms.md |
| Textbooks / Algebraic Geometry / Arithmetic Geometry | Algebraic Geometry / Arithmetic Geometry.md |
| Textbooks / Algebraic Geometry / Schemes | Algebraic Geometry / Schemes.md; Sheaves and Vector Bundles.md |
| Textbooks / Algebraic Geometry / Cohomology | Algebraic Geometry / Cohomology.md; Etale Cohomology.md |
| Textbooks / Algebraic Geometry / Hodge Theory | Algebraic Geometry / Hodge Theory.md |
| Textbooks / Algebraic Geometry / Curves; Surfaces | Algebraic Geometry / Curves and Surfaces.md |
| Textbooks / Algebraic Geometry / Surfaces | Algebraic Geometry / Surfaces / K3 Surfaces.md |
| Textbooks / Algebraic Geometry / Moduli | Algebraic Geometry / Moduli / K3 Moduli.md |
| Textbooks / Algebraic Geometry / Mirror Symmetry | Algebraic Geometry / Mirror Symmetry / Integral Affine Structures.md |
| Textbooks / Algebraic Geometry / Birational Geometry; Toric; Varieties | Algebraic Geometry / Birational Geometry.md; Toric Varieties.md; Varieties.md |
| Textbooks / Mathematical Physics | Mathematical Physics.md |
| Logic / Set Theory | Logic / Set Theory.md |

The deck tree adapts the collection tree to study subjects. Integral lattices
and quadratic forms have a Number Theory deck. Divisors has its own Algebraic
Geometry deck. Vocabulary is a separate study subject.

## Subject boundaries

- Mathematical Physics owns GW, ideal-sheaf DT, and PT curve counting and their
  comparison, as well as gauge equations and ASD moduli. Deformation Theory owns
  perfect obstruction theories and virtual classes. Hodge Theory owns Betti,
  de Rham, Dolbeault, Hodge, and Deligne–Hitchin moduli and representation
  quotients; Mathematical Physics retains the Hitchin-system applications.
  PT sheaf-section pairs differ from the KSBA pairs in Moduli / Stable Pairs.
  [Fulton–Pandharipande](https://arxiv.org/abs/alg-geom/9608011),
  [Pandharipande–Thomas](https://people.math.ethz.ch/~rahul/pt.pdf), and
  [Simpson](https://arxiv.org/abs/alg-geom/9604005) supply the moduli conventions.

- Topology / Four-Manifolds owns intersection forms as topological invariants,
  handles, smooth structures, spin and spin-c structures, and Seiberg–Witten
  invariants. Lattices and Quadratic Forms keeps the algebra of forms; surface
  decks retain their complex-geometric applications. Use complex orientation
  on complex surfaces, positive-definite E8, scalar signature as the difference
  of inertia indices, and the torsion-free quotient of integral cohomology for
  an intersection lattice.
  [Manolescu's course notes](https://web.stanford.edu/~cm5/4Mnotes.pdf),
  Donaldson–Kronheimer, *The Geometry of Four-Manifolds*, and Morgan,
  *The Seiberg–Witten Equations and Applications to the Topology of Smooth
  Four-Manifolds*, supply the topology and gauge-theory conventions.

- Deformation Theory owns marked Artinian lifting problems, obstruction classes,
  torsors of lifts, hulls, and deformation calculations for schemes, sheaves,
  maps, and pairs. Spectral Sequences supplies local-to-global machinery;
  specialized moduli decks keep the global spaces and compactifications.
  Hartshorne, *Deformation Theory*, and the
  [Stacks Project's formal deformation theory](https://stacks.math.columbia.edu/tag/06G8)
  supply the conventions. Small extensions here have one-dimensional kernel
  annihilated by the maximal ideal. Use the cotangent complex for singular
  schemes, and distinguish a complete obstruction space from the obstruction
  class of a specified lifting problem.

- Sheaves and Vector Bundles owns exact sequences of sheaves and the local
  operations that construct them. Cohomology owns their derived functors,
  vanishing theorems, duality, and global calculations. Spectral Sequences owns
  page conventions, convergence, edge maps, and degeneration tests;
  Hodge Theory keeps the geometric Hodge structures.
  Hartshorne, *Algebraic Geometry*, Chapters II–III, and the
  [Stacks Project](https://stacks.math.columbia.edu/) supply the algebraic conventions.

- Geometry / Manifolds owns smooth differential geometry, Riemannian curvature,
  and the differential-geometric foundations of complex and Kähler geometry.
  Its curvature convention is
  `R(X,Y)Z = ∇_X∇_Y Z − ∇_Y∇_X Z − ∇_[X,Y] Z`, with positive sectional
  curvature on the round sphere. Its Kähler form is `ω(X,Y) = g(JX,Y)`.
  [Joyce's differential geometry course](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/IntroDiffGeom.html)
  and [complex and Kähler geometry course](https://people.maths.ox.ac.uk/joyce/KahlerGeom2022/index.html)
  supply reference material. Keep metric-dependent statements distinct from
  assertions about the complex manifold admitting such a metric.

- Combinatorics / Matroids owns independence, rank, circuits, flats, matroid
  polytopes, and regular subdivisions. Toric Varieties owns the varieties and
  degenerations constructed from lattice polytopes.

- Moduli / Stable Pairs owns KSBA stability, families, weight changes, and the
  characteristic classes of their universal families. GIT and Weighted
  Configurations owns quotients, linearizations, and weighted pointed curves;
  Hyperplane Arrangements owns weighted arrangements and their toric models.
  Hurwitz and Prym owns cover moduli and the abelian varieties constructed from
  curve correspondences. Conformal Blocks owns coinvariants, fusion, and the
  bundles they define on moduli of curves.

- Covers owns the general construction of finite abelian covers. Surfaces /
  Abelian Cover Surfaces owns Campedelli and Burniat constructions; ADE Pairs
  owns the index-two surface–boundary shapes and priming used in double-cover
  compactifications. These global shapes differ from the local ADE germs in
  Surface Singularities. Alexeev–Pardini's papers on abelian covers and
  Alexeev–Thompson's *ADE surfaces and their moduli* fix these conventions.

- Abelian Varieties owns polarizations, period spaces, and semiabelic
  compactifications. Symplectic Varieties owns symplectic singularities,
  Hilbert schemes of points, and generalized Kummer varieties. Derived
  Categories owns semiorthogonal decompositions, exceptional collections, and
  admissible subcategories. Specialized surface constructions remain in the
  surface decks.

- Algebraic Geometry / Intersection Theory owns cycle equivalences, intersection
  operations, moving and excess intersection, and enumerative constructions.
  Numerical Invariants keeps standard ring presentations and numerical formulas;
  a worked enumerative problem belongs with the intersection method it exercises.
  The [Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/tag/0AZ7)
  develops the operations, and Eisenbud–Harris, *3264 and All That*, develops
  their enumerative applications.

- Arithmetic Geometry includes elliptic curves over finite, local, and number
  fields, their group laws and isogenies, and modular curves. Curves and Surfaces
  owns geometric curve theory and elliptic surfaces; Kodaira fiber configurations
  belong there. Silverman, *The Arithmetic of Elliptic Curves*, supplies the
  arithmetic conventions; [Sutherland's lectures](https://math.mit.edu/classes/18.783/2023/lectures.html)
  connect models, isogenies, finite fields, and modular curves.

- Toric Varieties owns fan and polytope constructions together with their worked
  calculations. Its figures live in `decks/Algebraic Geometry/assets/toric/` as
  editable SVG sources. Ray labels are primitive lattice generators; polygons
  show lattice points in the specified lattice. Normal fans use inward normals.
  [Cox–Little–Schenck, Toric Varieties](https://dacox.people.amherst.edu/toric.html)
  supplies the fan, divisor, and homogeneous-coordinate conventions.

- Algebraic Geometry / Moduli / Tautological Classes studies classes constructed
  from the universal curve. Its intersection formulas use the moduli stack;
  each comparison with topological MMM classes states the sign convention.
  [Schmitt, Section 6](https://johannesschmitt.gitlab.io/ModCurves/Script.pdf)
  develops the tautological ring.
  [Kock, Part I](https://mat.uab.es/~kock/GW/notes/psi-notes.pdf) supplies the
  descendant calculus, and
  [Wahl, Lecture 1](https://web.math.ku.dk/~wahl/PCMIlec.pdf) treats MMM classes.

- Algebraic Geometry / Singularities identifies local germs from their equations
  and resolutions. Plane Curves studies branches; Surface Singularities studies
  exceptional curves on resolutions. Birational Classes classifies pairs by
  discrepancies. Numerical invariant formulas belong in Numerical Invariants.
  [Reid](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf) gives the Du Val
  classification; [Kollár](https://web.math.princeton.edu/~kollar/book/chap3.pdf)
  defines semi-log-canonical pairs through normalization.

- Algebraic Geometry / Numerical Invariants collects computations for standard
  varieties. A dimension card identifies the space being measured and states
  whether the dimension is expected or actual. A group or ring computation gives
  its structure, rather than only its rank. Each card supplies the hypotheses
  needed to interpret its answer. Structural theorems belong in the subject decks.

  The [Stacks Project](https://stacks.math.columbia.edu/tag/02P3) gives the Chow
  operations used in these computations.
  [Grassmannians and their Chow rings](https://ravif.web.illinois.edu/exposition/seminar_talks/Grassmannians%20and%20their%20Chow%20rings.pdf)
  develops the Schubert presentation.
  [Givental](https://math.berkeley.edu/~giventh/ln/l15-16.pdf) computes the quintic
  Hodge diamond.

- Algebraic Geometry / Examples collects explicit equations, parametrizations,
  and projective constructions of curves and varieties, including rational normal
  curves, scrolls, and Segre and Veronese embeddings.
  References for scroll constructions and determinantal equations are
  [Reid, Rational Scrolls](https://mreid.warwick.ac.uk/surf/Reid_Park_City_chapters.pdf)
  and [Eisenbud, Commutative Algebra](https://www.math.ens.psl.eu/~benoist/refs/Eisenbud.pdf).

- Complex Analysis holds definitions, formulas, examples, statements, and proof
  prompts together. Tags identify the kind of card.
- Algebraic Geometry / Definitions holds definition cards that several subject
  decks use. Its Morphisms deck defines properties of morphisms, including
  separated, quasicompact, finite presentation, proper, affine, finite, flat,
  smooth, unramified, etale, immersion, and closed immersion.
- Schemes includes schemes and their constructions. Sheaves and Vector Bundles
  includes sheaves of modules, differentials, and normal bundles. Cohomology
  holds cohomology constructions and computations; Homological Algebra holds
  their general algebraic prerequisites.
- K3 Surfaces holds results specific to K3 surfaces. K3 Moduli holds markings,
  periods, families, degenerations, and compactifications. General Hodge theory,
  divisor theory, surface theory, and lattice theory belong in their respective
  subject decks.
- Integral Affine Structures holds integral affine geometry and its applications
  to anticanonical pairs and mirror symmetry.
- Manifolds, Lie Algebras, Algebraic Groups, and Functional Analysis each have an
  independent subject scope. Their current size does not change that scope.

## Adding and moving cards

Choose a card's deck from the mathematical question it asks. A definition used
in several subjects has one home. A specialized application can have a separate
card when its question and hypotheses differ. Preserve the card ID when moving
a card, and keep its Front and Back together.

Before adding a card, search the existing sources for the concept and its
common names. Compare the answers as well as the prompts. Incorporate additional
equivalent formulations into the existing card. State a proof task explicitly
in its prompt so that it remains distinct from recalling the theorem.

A new deck needs a distinct mathematical subject. Extend an existing subject
deck when the new material belongs to its scope. Use tags for card type and
source context.
