---
title: "Algebraic Geometry::Surfaces::Enriques Surfaces"
---

::: {.front card-id="enriques-quotient-dual-complex" tags="construction comparison"}
How do the involution on a Kulikov dual complex and its action on components determine the topology and singularities of an Enriques quotient degeneration?
:::

::: {.back card-id="enriques-quotient-dual-complex"}
Use a regular involution on the model, with an equivariant subdivision when needed.

| K3 dual complex and action | Quotient complex | Component behavior |
| --- | --- | --- |
| Type III: $S^2$, antipodal | $\mathbb{RP}^2$ | Components exchanged in pairs |
| Type III: $S^2$, reflection | Disk | Exchanged pairs off the fixed equator; preserved components on it |
| Type II: interval, reversal | Interval | Components paired, possibly a preserved middle component or double curve |
| Type II: interval, identity | Interval | Every component preserved |

For an exchanged pair, the normalization of its quotient is one of the components. In the AEGS type III reflection models, a preserved component has four isolated fixed points, lying in pairs on two boundary curves; its quotient has four $A_1$ points.

A nontrivial involution of $\mathbb P^1$ is conjugate to $t\mapsto-t$ and has two fixed points. On an elliptic double curve, preserving its one-form gives translation by nonzero two-torsion; negating the form gives $p\mapsto a-p$ with four fixed points. Opposite residues on the two branches determine which action is compatible with a nonsymplectic involution that exchanges, or preserves, the adjacent components.

The quotient complex records incidence, not the gluing isomorphisms or the singularities on each normalized component; retain those separately.

Reference: AEGS, Proposition 4.8 and §7.3.
:::

::: {.front card-id="enriques-affine-to-stable-example" tags="application calculation"}
Recover the stable Enriques limit from the following divisor-model construction: the mirror polygon has successive edge vectors $(2,0),(-1,1),(-1,0),(0,-1)$, with a unit Symington surgery on the diagonal edge. The doubled sphere yields four invariant components with ramification squares $(0,8,4,4)$; the first is ruled, the others are a $D_8$ pair and two $D_4$ pairs. Determine the surviving quotient components and polarization degree.
:::

::: {.back card-id="enriques-affine-to-stable-example"}
Putting the edge vectors end to end gives vertices
$$ (0,0),\ (2,0),\ (1,1),\ (0,1).$$
Perform the unit shear surgery on $(2,0)\!\to\!(1,1)$, then double the resulting affine disk with opposite orientation. In this construction the Enriques and del Pezzo reflections have the same equator. Choose the equivariant triangulation and component gluings giving the stated divisor model.

Each component is preserved, so each component map to the quotient has degree two. With $q^*R_i=\widetilde R_i$:

| Component | $\widetilde R_i^2$ upstairs | $R_i^2$ downstairs | Stable-model map |
| --- | --- | --- | --- |
| Ruled component | $0$ | $0$ | Contracts along its ruling |
| $D_8$ anticanonical pair | $8$ | $4$ | Survives as its index-two folded quotient |
| Each $D_4$ anticanonical pair | $4$ | $2$ | Survives as its index-two folded quotient |

The surviving shapes are $D_8:2={}_2'B_4^-$ and two copies of $D_4:2={}_2'B_2^-$. The global ramification degree is
$$R_Z^2=4+2+2=8,$$
as required for the square of the degree-two numerical polarization. On each surviving component, contract any remaining $R_i$-orthogonal curves and retain the induced conductor gluing.

Square zero alone would not specify the contraction: here the restricted polarization is nontrivial and semiample with one-dimensional image. A numerically trivial restriction would instead contract the component to a point.

Reference: AEGS, Example 4.14, Corollary 4.9, and §6.5.
:::

::: {.front card-id="enriques-degree-two-projective-model" tags="construction comparison formula"}
For an ADE Enriques surface with an ample numerical polarization of square two, which line bundle defines its quartic del Pezzo model? Distinguish the ordinary and special cases.
:::

::: {.back card-id="enriques-degree-two-projective-model"}
Over $\mathbb C$, let $[L]\in\operatorname{Pic}(Z)/\langle K_Z\rangle$, $L^2=2$. The lifts $L$ and $L\otimes K_Z$ have the same square
$$M=L^{\otimes2},\qquad M^2=8,\qquad h^0(Z,M)=5.$$
The complete system $|M|$ is basepoint-free and gives a degree-two map to a quartic del Pezzo surface $W\subset\mathbb P^4$. Degree check: $8=2\cdot4$.

| Case | Intermediate surface $Y$ in the K3 covering diagram | Singularities of $W$ |
| --- | --- | --- |
| Ordinary | $\mathbb P^1\times\mathbb P^1$ | $4A_1$ |
| Special Heegner locus | $\mathbb P(1,1,2)$ | $A_3+2A_1$ |

The reduced ramification divisor $R_Z\in|M|$ supplies the stable-pair polarization. On a smooth resolution with only big and nef polarization, first contract the orthogonal $(-2)$-curves to obtain the ADE polarized model. Numerical equivalence does not select one of the two lifts $L$, but it does select $M$.

Reference: AEGS, Introduction and §§2.1–2.2; Cossec's classification of Enriques linear systems cited there.
:::

::: {.front card-id="enriques-horikawa-involutions-residue" tags="construction calculation"}
Construct a smooth Enriques surface from an invariant $(4,4)$ curve on $\mathbb P^1\times\mathbb P^1$. Identify all three involutions of its K3 covering diagram, their fixed loci, and their actions on the two-form.
:::

::: {.back card-id="enriques-horikawa-involutions-residue"}
Take $Y=\mathbb P^1\times\mathbb P^1$, $\tau(x,y)=(-x,-y)$, and a smooth invariant branch curve $B=(f=0)$ avoiding the four fixed points of $\tau$. The double cover $X$ has local equation $z^2+f(x,y)=0$, with $z$ a fiber coordinate of $\mathcal O_Y(2,2)$.

| Involution | Formula | Action on $\omega$ | Fixed locus |
| --- | --- | --- | --- |
| $d$ | $(x,y,-z)$ | $-1$ | Ramification curve |
| $a$ | $(-x,-y,-z)$ | $-1$ | Empty |
| $b=da$ | $(-x,-y,z)$ | $+1$ | Eight points |

Use the residue $\omega=\operatorname{Res}(dx\wedge dy\wedge dz/(z^2+f))=dx\wedge dy/(2z)$. The product of the coordinate signs gives the character. The equation is invariant under each map. At a fixed point of $\tau$, $f\ne0$, so the two points above it have $z\ne0$: $a$ exchanges them and $b$ fixes them.

Thus $Z=X/a$ is Enriques, $X/b$ has eight $A_1$ singularities and K3 minimal resolution, and $W=Y/\tau=X/\langle d,a\rangle$. The invariant monomials have $i+j$ even. In bidegree $(4,4)$ there are $3^2+2^2=13$ of them; projectivizing and dividing by the two-dimensional connected coordinate torus gives dimension $12-2=10$.

Reference: AEGS, §2.1.
:::

::: {.front card-id="enriques-half-fibers" tags="definition construction example"}
For a complex Enriques surface $S$, relate primitive nef isotropic classes, half-fibers, and genus-one pencils. Why need the pencil have no section?
:::

::: {.back card-id="enriques-half-fibers"}
$\operatorname{Num}(S)=\operatorname{Pic}(S)/\langle K_S\rangle\simeq U\oplus E_8(-1)$.

- A primitive nef class $f\ne0$ with $f^2=0$ is represented by a half-fiber $F$; $|2F|$ defines a genus-one fibration $S\to\mathbb P^1$.
- Its two multiple fibers are $2F$ and $2F'$, with $F'\sim F+K_S$. Thus $F\equiv F'$ but $F\not\sim F'$.
- “Half” means division of the fiber divisor by two. Over $\mathbb C$, half-fibers are reduced: smooth genus-one curves or multiplicative Kodaira fibers. General reducible fibers must still be read with their Kodaira component multiplicities.
- A section $C$ would satisfy $C\cdot(2F)=1$, impossible since $C\cdot F\in\mathbb Z$. “Genus-one fibration” does not assume a section; the associated Jacobian fibration has one.

Reference: [Moschetti–Rota–Schaffler, §2.2](https://arxiv.org/abs/2202.01775).
:::

::: {.front card-id="enriques-isotropic-sequences-nd" tags="definition comparison formula"}
Define isotropic and non-degenerate isotropic sequences on a complex Enriques surface. Define $\mathrm{nd}(S)$ and distinguish lattice existence from nef realization.
:::

::: {.back card-id="enriques-isotropic-sequences-nd"}
An isotropic sequence consists of primitive isotropic classes $f_1,\ldots,f_n\in\operatorname{Num}(S)$ with
$$f_i\cdot f_j=1-\delta_{ij}.$$
Non-degenerate: every $f_i$ is nef, hence represented by a half-fiber. Then
$$\mathrm{nd}(S)=\max\{n:\text{a non-degenerate isotropic sequence of length }n\text{ exists}\}.$$
The Gram matrix is $J_n-I_n$: eigenvalues $n-1,-1,\ldots,-1$ for $n>1$. The signature $(1,9)$ gives $n\le10$.

The abstract Enriques lattice admits length-ten sequences. On a specified surface, intersections with effective $(-2)$-curves can obstruct nefness. Unnodal surfaces have $\mathrm{nd}(S)=10$; the numerical lattice alone does not determine the non-degeneracy invariant.

Reference: [Moschetti–Rota–Schaffler, Definitions 2.6–2.11](https://arxiv.org/abs/2202.01775).
:::
