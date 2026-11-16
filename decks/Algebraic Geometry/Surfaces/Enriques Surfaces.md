---
title: "Algebraic Geometry::Surfaces::Enriques Surfaces"
---

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
