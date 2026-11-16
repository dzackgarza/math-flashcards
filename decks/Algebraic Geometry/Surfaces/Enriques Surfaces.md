---
title: "Algebraic Geometry::Surfaces::Enriques Surfaces"
---

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
