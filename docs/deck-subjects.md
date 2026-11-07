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
