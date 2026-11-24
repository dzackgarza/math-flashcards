# Research and Source Decisions

## Mathematical source verification

**Decision**: Verify each new theorem, formula, and computation against a mathematical source before adding it. Reuse the collection's existing Zotero works where they contain the statement. Add a missing work to Zotero before citing it. Use precise section, theorem, or chapter locators in the front-div `cite` attribute.

**Rationale**: The prior coverage audit establishes absence, not the correctness of proposed new material. The cards must support research use, so hypotheses and exceptional cases matter.

**Alternatives considered**: Writing from notation familiarity alone was rejected. Copying source passages without a retrieval task was also rejected.

## Owner and source map

| Content | Owning subject | Primary references to verify |
| --- | --- | --- |
| Syzygies, Betti numbers, Koszul complexes, regularity, Rees algebras | Commutative Algebra; Homological Algebra; Cohomology for sheaf regularity | Atiyah–Macdonald; Eisenbud; Bruns–Herzog; Stacks Project |
| Length, dimension theorem, height, Artinian rings, catenarity | Commutative Algebra; Modules and Linear Algebra; Schemes for geometric formulations | Atiyah–Macdonald; Matsumura; Stacks Project |
| Arithmetic functions and the prime number theorem | Analytic Number Theory | Apostol or Davenport for the elementary identities and equivalent asymptotic forms |
| Integral models and generic fibers | Schemes; Arithmetic Geometry | Stacks Project; Liu for models and base change |
| Weil conjectures and finite-field zeta computations | Etale Cohomology; Arithmetic Geometry | Deligne; Milne; existing finite-field elliptic-curve conventions |
| Selmer groups and descent | Arithmetic Geometry | Silverman for elliptic descent; Bloch–Kato or Neukirch–Schmidt–Wingberg for general local conditions |
| Galois duality | Class Field Theory | Neukirch–Schmidt–Wingberg or Milne for Tate and Poitou–Tate statements |
| General valuations and extensions | Algebraic Number Theory | Neukirch; Engler–Prestel; Stacks Project valuation rings |
| Abelian-variety and mixed-characteristic reduction | Arithmetic Geometry; Curves and Surfaces | Grothendieck semistable reduction; Néron-model references; de Jong and Abramovich–Karu for alteration-level statements |
| MMP examples and Atiyah flop | Birational Geometry | Kollár–Mori; Reid for the conifold and surface/threefold contractions |
| Normal complete toric surfaces and Cox rings | Toric Varieties; Birational Geometry | Cox–Little–Schenck; Hu–Keel for Cox rings and Mori dream spaces |

## Computation checks

**Decision**: Check algebraic examples through an independent operation in the shared mathematical container where practical. Use Macaulay2 for resolutions, Betti numbers, Koszul homology, and Rees presentations. Use direct fan and point-count calculations for toric and finite-field examples. Keep the checked input and output in the commit rationale when it settles a mathematical choice.

**Rationale**: A rendered formula proves only rendering. Independent computation tests the mathematical assertion at the operation's owner.

**Alternatives considered**: Visual inspection alone was rejected for graded algebra and descent computations. Adding application tests for mathematical content was rejected because the content is the deliverable.

## Citation and presentation decisions

**Decision**: Use compact composite cards for connected theorem packages and separate focused cards for computations. Put the requested result first, retain hypotheses beside the statement, and use tables for classifications and comparisons.

**Rationale**: This follows `CONTRIBUTING.md` and avoids splitting a connected argument into isolated fragments.

**Alternatives considered**: One card per minor fact was rejected as the default. Long source summaries were rejected because they do not supply a clear retrieval task.

## Resolved scope decisions

- The scope is exactly FR-001 through FR-016; strong topics without a stated gap need no duplicate cards.
- An explicit elliptic-curve descent must identify which Selmer group it computes and distinguish a full \(2\)-descent from a \(2\)-isogeny descent.
- General semistable reduction in mixed characteristic must not be asserted. The new material must state the established abelian-variety theorem separately from alteration results.
- The spectrum of the rationals maps to the generic point of the spectrum of the integers. It is not an open immersion.
- The Cox-ring computation for the plane blown up at a point must give compatible fan, divisor-class, grading, and irrelevant-ideal conventions.

## Verified source inventory

The following works are present in Zotero with PDF attachments and readable text. These are the citation keys to use; no source is cited solely from the coverage audit.

| Subject | Citation keys and verified locations |
| --- | --- |
| Dimension, length, Artinian rings | `@AM18`, Chapters 6, 8, 11 |
| Resolutions, Koszul complexes, depth, Castelnuovo–Mumford regularity, Rees algebras | `@Eis95`, Chapters 1, 17, 18, 20 and Appendix 3; `@BH98`, Chapters 1–2 and 4 |
| Analytic number theory | `@Apo98`, Chapters 2, 4, 11 and the prime-number-theorem chapter |
| Arithmetic models | `@Liu10`, Chapters 3–4; `@The25`, Limits of Schemes and More on Morphisms |
| Weil conjectures | `@Del74`, Théorème 1.6; `@Mil25`, zeta-function and Weil-conjecture sections |
| Elliptic descent | `@Sil09`, X.4 and X.6, especially Proposition 6.2 |
| General Selmer local conditions | `@BK07`, Definitions 3.7 and 5.1 |
| Tate and Poitou–Tate duality | `@Mil06`, I.2, Corollary 2.3 and I.4, Theorem 4.10 |
| General valuations and extensions | `@The25`, Algebra, §10.50; `@Neu99`, II.3–4 and II.8 |
| Abelian-variety reduction | `@Gro72`, I.6 and IX.3; `@BLR90`, Part 4 |
| Alterations in arithmetic and mixed characteristic | `@De96`, Theorems 6.5 and 8.2 |
| Toric surfaces and Cox quotients | `@CLS11`, Chapters 2, 5, 10–11 |
| MMP and the conifold | `@KM98`, `@Bir07`, and `@Rei80` for the surrounding conventions |

`@BK07`, `@Mil06`, and `@De96` were added to Zotero with their full PDFs for this remediation. The readable source text comes from Zotero's indexed full text or the existing extracted-Markdown attachments.

## Verified computational conventions

Sage and Singular are available for independent checks. Singular's `syz` computation was verified on \((x^2,y^2)\), and Sage finite-field and lattice computations are available. Macaulay2 is not required for the planned checks.

For \(X=\operatorname{Bl}_p\mathbf P^2\cong\mathbf F_1\), use the smooth complete fan with rays
\[
\rho_1=(1,0),\quad \rho_2=(0,1),\quad \rho_3=(-1,-1),\quad \rho_4=(0,-1).
\]
Let \(D_i=D_{\rho_i}\), \(A=[D_1]=[D_3]=H-E\), and \(B=[D_2]=H\). Then \([D_4]=B-A=E\). Thus
\[
\operatorname{Cox}(X)=\mathbf C[x_1,x_2,x_3,x_4],\qquad
\deg(x_1)=\deg(x_3)=H-E,\quad \deg(x_2)=H,\quad \deg(x_4)=E.
\]
The maximal cones are \(12,23,34,41\), so
\[
B=(x_3x_4,x_1x_4,x_1x_2,x_2x_3)=(x_1,x_3)(x_2,x_4).
\]
These relations follow directly from the two characters of the fan and will be checked again when the card is authored.

For the explicit descent, use \(E:\,y^2=x^3+7x\) and \(E':\,Y^2=X^3-28X\) with the degree-two isogeny from Silverman X.6. The homogeneous spaces are
\[
C_d:\ d w^2=d^2-28z^4,\qquad C'_d:\ d W^2=d^2+7Z^4,
\]
with \(d\in\{\pm1,\pm2,\pm7,\pm14\}\). Silverman's Proposition 6.2 gives \(S^{(\phi)}(E/\mathbf Q)\cong\mathbf Z/2\mathbf Z\) and \(S^{(\hat\phi)}(E'/\mathbf Q)\cong\mathbf Z/2\mathbf Z\). The card must show the local tests, not merely quote the result. This is a two-isogeny descent, not a claim to compute the full \(2\)-Selmer group.

## Theorem boundaries verified before authoring

- **Tate local duality**: use a nonarchimedean local field with finite residue field and a finite Galois module whose order is prime to the characteristic of the field; use the dual \(M^\vee(1)\). Archimedean places require Tate cohomology and are not silently included in that statement.
- **Poitou–Tate**: use a finite set \(S\) containing the archimedean places, the places of bad reduction or ramification, and places dividing the module order; \(G_S\) is the group of the maximal extension unramified outside \(S\). The sequence uses restricted products \(P_S^r\) and the dual module.
- **Valuations**: a general value group is totally ordered abelian, not necessarily cyclic. Existence of extensions follows by embedding into a completed algebraic closure; the fundamental identity is stated only under its standard finite-extension hypotheses.
- **Abelian varieties**: after a finite separable extension, the identity component of the special fiber of the Néron model is an extension of an abelian variety by a torus. The \(\ell\)-adic criterion requires \(\ell\) different from the residue characteristic.
- **Mixed characteristic**: de Jong's Theorem 6.5 permits an alteration of the total space and a finite extension of the trait. It does not assert that every variety has a strict semistable model with unchanged generic fiber. The arithmetic statement in Theorem 8.2 likewise uses an alteration over a ring of integers.
