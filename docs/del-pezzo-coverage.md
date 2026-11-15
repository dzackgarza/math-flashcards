# Del Pezzo coverage and the boundary of plane blowups

## Remediation

The findings below are addressed by the delpezzo-* and blowup-* cards in
[Curves and Surfaces](../decks/Algebraic%20Geometry/Curves%20and%20Surfaces.md),
the construction-delpezzo-weighted-low-degree card in
[Examples](../decks/Algebraic%20Geometry/Examples.md), and the clarified
definition in [Varieties](../decks/Algebraic%20Geometry/Varieties.md).

Coverage now includes degree classification, weak and singular variants,
Picard lattices, roots and Cremona reflections, exceptional-class enumeration,
weighted constructions, and contrasting point configurations at and beyond
nine blowups. The existing numerical and construction cards remain in place.

The remaining sections preserve the baseline assessment before remediation.

Coverage is useful for numerical calculations, but incomplete as a working
theory. The admissible degrees and blowup constructions are present, sometimes
inside answers to other questions. The lattice interpretation and the change
at and beyond nine points need dedicated cards.

This assessment concerns smooth projective surfaces over $\mathbb C$.
Over other fields, distinguish the geometric Picard lattice from line bundles
defined over the ground field. Singular del Pezzo surfaces require separate
hypotheses.

## Current cards

| Topic | Coverage |
| --- | --- |
| Definition | Varieties: card-0324110ee3d3217f says “Fano of dimension 2”; smooth versus weak versus singular versions need separation |
| Degrees and classification | Numerical Invariants/Surfaces: numerical-del-pezzo-exceptional-counts lists all degrees and both degree-eight cases; Toric Varieties includes the general blowup classification |
| General position | numerical-del-pezzo-general-position gives the line, conic, and singular-cubic obstructions |
| Constructions | Examples has cubic surfaces, intersections of quadrics, and cubic pencils; Numerical Invariants/Surfaces has degree-two double covers and degree-one anticanonical maps |
| Exceptional curves | Counts by degree and the explicit cubic-surface classes are present |
| Picard group and intersection pairing | Numerical Invariants/Picard Groups gives blowup generators; Numerical Invariants/Surfaces gives the intersection matrix, canonical class, and self-intersection formulas |
| Root lattices and Weyl action | No dedicated del Pezzo treatment found in the inspected cards |
| Nine points | A cubic-pencil construction is present; the distinction from very general points is missing |
| More than nine points | No dedicated treatment found of anticanonical positivity, configuration dependence, or infinite exceptional curves |

## Degrees and constructions to make directly retrievable

A smooth del Pezzo surface has ample $-K_X$ and degree $d=K_X^2$.

| Degree | Construction over $\mathbb C$ |
| --- | --- |
| 9 | $\mathbb P^2$ |
| 8 | $\mathbb P^1\times\mathbb P^1$ or $\operatorname{Bl}_p\mathbb P^2$ |
| 1 through 7 | Blow up $9-d$ plane points in del Pezzo general position |
| 3 | Smooth cubic in $\mathbb P^3$ |
| 4 | Smooth intersection of two quadrics in $\mathbb P^4$ |
| 2 | Double cover of $\mathbb P^2$ branched over a smooth quartic; weighted quartic model in $\mathbb P(1,1,1,2)$ |
| 1 | Smooth degree-six model in $\mathbb P(1,1,2,3)$; anticanonical pencil with a base point |

Every integer degree from one through nine occurs. No other degree occurs for
smooth del Pezzo surfaces. The existing cards should connect the classification
to this conclusion, rather than rely on recall from an exceptional-curve table.
Weak del Pezzo means $-K$ nef and big; its anticanonical model contracts
$(-2)$-curves to Du Val singularities. These notions should be compared explicitly.
[Reference: Van Luijk, Del Pezzo Surfaces](https://samirsiksek.github.io/siksek.github.io/arith/notes/delpezzo.pdf).

## Picard lattice and its uses

For $X_r=\operatorname{Bl}_{p_1,\ldots,p_r}\mathbb P^2$,

$$
\operatorname{Pic}(X_r)=\operatorname{NS}(X_r)
=\mathbb ZH\oplus\bigoplus_i\mathbb ZE_i,\qquad
H^2=1,\quad H E_i=0,\quad E_iE_j=-\delta_{ij}.
$$

Thus it is the odd unimodular lattice $I_{1,r}$, with
$K=-3H+\sum E_i$ and $K^2=9-r$. For infinitely near centers use total
transforms for this diagonal basis. The other degree-eight surface has the
even hyperbolic lattice $U$, with ruling classes of square zero and mutual
intersection one. This distinguishes the surfaces even though their degrees
and Picard ranks agree.

For $3\le r\le8$, the negative-definite lattice $K^\perp$ has root type

| $r$ | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- |
| Type | $A_2\oplus A_1$ | $A_4$ | $D_5$ | $E_6$ | $E_7$ | $E_8$ |

Use roots $E_i-E_{i+1}$ and $H-E_1-E_2-E_3$, reflections
$s_\alpha(D)=D+(D\cdot\alpha)\alpha$, and the quadratic Cremona transformation
to connect the lattice to changes of blowdown marking. A lattice root is not
automatically an effective curve: on a smooth del Pezzo, an effective
$(-2)$-curve orthogonal to $K$ would contradict ampleness.
Likewise, Weyl symmetries of markings are not all automorphisms of a fixed surface.
[Reference: Dolgachev–Iskovskikh](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/manin09.pdf).

The practical cards should enumerate exceptional classes using
$E^2=K\cdot E=-1$, recover the cubic-surface lines, test intersections,
and use these curves to determine nef inequalities. Distinguish numerical
conditions on a class from the effectivity and irreducibility arguments.

## What changes at nine points?

The formula $K^2=0$ alone does not give an elliptic fibration.

| Configuration | Anticanonical behavior |
| --- | --- |
| Distinct base points of a general cubic pencil | $|-K|$ is a base-point-free pencil on the blowup; it gives a rational elliptic surface with sections |
| Very general plane points | There is a unique smooth cubic $C$ through them; its strict transform is nef of square zero, but $-K$ is not semiample |

In the second case, the degree-zero normal bundle
$\mathcal O_C(3)(-p_1-\cdots-p_9)$ is nontorsion. The restriction sequence
then gives $h^0(X,-mK)=1$ for every positive $m$: every system consists
of the corresponding multiple of the same cubic. This supplies a concrete
nef-but-not-semiample surface example.
[Reference: nef nonsemiample rational surface example, Example 3.6](https://aif.centre-mersenne.org/item/10.5802/aif.3620.pdf).

The lattice also records the transition: $K^\perp$ is negative semidefinite
with radical $\mathbb ZK$, and $K^\perp/\mathbb ZK\cong E_8(-1)$.
This is the affine-root boundary of the finite del Pezzo picture.

## What happens after more than nine blowups?

The surface remains rational, with $\kappa=-\infty$, $p_g=q=0$, and
Picard lattice $I_{1,r}$. It does not become a surface of general type.
But $K^2=9-r<0$, so $-K$ cannot be nef, hence cannot be ample.
It is neither del Pezzo nor weak del Pezzo.

The number of points does not determine anticanonical effectivity or bigness:

| Configuration, $r\ge10$ | Consequence |
| --- | --- |
| Very general points | No cubic passes through all of them, so $|-K|$ is empty |
| Points on a smooth cubic | Its strict transform is effective anticanonical with negative square |
| Points on a line | Writing $L'=H-\sum E_i$, one has $-K=2H+L'$; this is big because $H$ is big and $L'$ effective, despite $(-K)^2<0$ |

Thus negative self-intersection does not imply non-bigness for a nonnef divisor.
The last example can be checked directly from
$H^0(2mH)\hookrightarrow H^0(-mK)$ by multiplication with the section of $mL'$.

For very general point configurations with $r\ge9$, infinitely many
$(-1)$-curves replace the finite del Pezzo lists, and the curve cone is
not rational polyhedral. Special configurations behave differently.
The orthogonal complement of $K$ for $r\ge10$ has signature $(1,r-1)$,
so the finite negative-definite root-lattice picture also ends.
[Reference: de Fernex, On the Mori cone of blow-ups of the plane](https://arxiv.org/abs/1001.5243).

Remediation should retain the existing computations and add the classification
as a direct retrieval task, weighted low-degree constructions, the lattice and
Weyl interpretation, weak del Pezzo comparisons, and explicit contrasting
examples at and beyond nine points. These additions also supply examples for
the [convex-geometry coverage gaps](convex-geometry-coverage.md).
