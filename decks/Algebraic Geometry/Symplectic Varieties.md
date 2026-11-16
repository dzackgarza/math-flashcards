---
title: "Algebraic Geometry::Symplectic Varieties"
---

::: {.front card-id="hilbert-tautological-bundle" tags="definition construction example"}
Define the tautological bundle $E^{[n]}$ on the Hilbert scheme of points of a smooth surface. Give its rank and fibers.
:::

::: {.back card-id="hilbert-tautological-bundle"}
For a smooth surface $S$ and a vector bundle $E$ of rank $r$, let $\mathcal Z\subset S\times S^{[n]}$ be the universal length-$n$ subscheme, with projections $q:\mathcal Z\to S$, $p:\mathcal Z\to S^{[n]}$. Define
$$E^{[n]}=p_*q^*E.$$
The map $p$ is finite flat of degree $n$, so $E^{[n]}$ is locally free of rank $nr$, with fiber $H^0(Z,E|_Z)$ at $[Z]$.

For distinct points, this fiber is $\bigoplus_{i=1}^n E_{x_i}$. At a nonreduced length-two point it retains the infinitesimal direction; it is not two unrelated copies of $E_x$.

Reference: Alexeev–Engel, *The flex divisor of a K3 surface*, §3.
:::

::: {.front card-id="symplectic-singularity-resolution" tags="definition comparison example"}
Define a symplectic singularity and a symplectic resolution. What condition distinguishes extension of a form from a symplectic resolution?
:::

::: {.back card-id="symplectic-singularity-resolution"}
A normal complex variety $X$ has symplectic singularities if $X_{\mathrm{reg}}$ carries a closed nondegenerate holomorphic two-form $\sigma$ whose pullback extends to a holomorphic two-form on a resolution (equivalently, every resolution).

A symplectic resolution is a resolution $f:Y\to X$ for which that extension is **nondegenerate everywhere** on $Y$. Extension alone may have degeneracy along exceptional divisors.

Example: $\mathbb A^2/\{\pm1\}=\{xy=z^2\}$ is symplectic singular. Its minimal resolution is symplectic; a further blowup at a point is not, since the pulled-back two-form vanishes along the new exceptional curve.

Reference: Beauville, *Symplectic singularities*; Alexeev, *Root systems and hyperkähler varieties*.
:::

::: {.front card-id="symplectic-generalized-kummer" tags="definition construction example"}
Construct a generalized Kummer variety from an abelian surface. Distinguish it from the singular symmetric-product fiber.
:::

::: {.back card-id="symplectic-generalized-kummer"}
For an abelian surface $A/\mathbb C$ and $n\ge1$, compose Hilbert–Chow with addition:
$$s:A^{[n+1]}\longrightarrow\operatorname{Sym}^{n+1}(A)
\xrightarrow{\ \sum\ }A,\qquad K_n(A)=s^{-1}(0).$$
$K_n(A)$ is smooth irreducible holomorphic symplectic of dimension $2n$. The fiber of $\operatorname{Sym}^{n+1}(A)\to A$ can be singular; Hilbert–Chow resolves it.

For $n=1$, unordered pairs $\{a,-a\}$ give $A/\{\pm1\}$, and $K_1(A)$ is its Kummer K3 resolution.

If $\Lambda=A_n=\{(a_i)\in\mathbb Z^{n+1}:\sum a_i=0\}$, then
$$ (\Lambda\otimes A)/W(A_n)
\cong\ker(\operatorname{Sym}^{n+1}(A)\to A),\qquad W(A_n)=S_{n+1}.$$
This is the root-lattice construction of the singular model.

Reference: Alexeev, *Root systems and hyperkähler varieties*, Example 1.
:::
