---
title: "Algebraic Geometry::Birational Geometry"
---

::: {.front card-id="card-8c26bb201aefe21c" tags="definition"}
What is: crepant resolutions
:::

::: {.back card-id="card-8c26bb201aefe21c"}
A resolution $f:Y\to X$ of a normal $\mathbb Q$-Gorenstein variety is crepant if $K_Y=f^*K_X$ as $\mathbb Q$-divisors, equivalently if all exceptional discrepancies are zero.
:::

::: {.front card-id="card-21139fdf3f221644"}
What is **Kodaira dimension**?
:::

::: {.back card-id="card-21139fdf3f221644"}
For$X$ normal projective and $D\in {\mathbf{Q}}{\hbox{-}}\operatorname{Div}(X)$,
$$\kappa(X, D)\coloneqq\limsup _{m \in {\mathbf{Z}}_{\geq 0}} \frac{\log \left(h^0\left(\mathcal{O}_X(m D)\right)\right)}{\log m}$$
Equivalently, the Iitaka dimension of the canonical
$$\kappa(X) \coloneqq\kappa(X; \omega_X)$$
Interpret as $P_m(X) \sim m^{\kappa(x)}$ (bounded above and below by constant multiples).
:::

::: {.front card-id="card-0996fd4a0ee4d958"}
What is a general type variety?
:::

::: {.back card-id="card-0996fd4a0ee4d958"}
$\kappa(X) = \dim(X)$ is maximal, i.e. $\omega_X$ is big.
:::

::: {.front card-id="card-67f625f64dc3c847"}
What is a big line bundle?
:::

::: {.back card-id="card-67f625f64dc3c847"}
${\mathcal{L}}\in \operatorname{Pic}(X)$ is big iff $\kappa(X; {\mathcal{L}}) = \dim(X)$ is maximal, i.e. $\dim \operatorname{im}\phi_{{\left\lvert {m} \right\rvert} {\mathcal{L}}} = \dim(X)$ for $n\gg 1$.
:::

::: {.front card-id="card-a54e2a90c7831a3d"}
What is Iitaka dimension?
:::

::: {.back card-id="card-a54e2a90c7831a3d"}
For ${\mathcal{L}}\in \operatorname{Pic}(X)$, define the *Iitaka dimension* of ${\mathcal{L}}\in \operatorname{Pic}(X)$ as the maximal embedding dimension:
$$\kappa(X; {\mathcal{L}}) \coloneqq\sup_{m\in {\mathbf{Z}}_{\geq 0}} \left\{{\dim \phi_{{\left\lvert {m{\mathcal{L}}} \right\rvert}}(X)}\right\},\qquad \phi_{{\left\lvert {m{\mathcal{L}}} \right\rvert}}:X\to {\mathbf{P}}^n$$
Always have $\kappa(X; {\mathcal{L}}) \in \left\{{-\infty, 0, 1,\cdots, \dim(X)}\right\}$.

If ${\mathcal{L}}$ is not effective, define $\kappa(X; {\mathcal{L}})= -\infty$.

Fact:
$$\kappa(X; {\mathcal{L}}) + 1 = {\mathrm{trdeg}}_k \operatorname{ff}(R(X; L))$$
where $R(X; L)$ is the section ring.
:::

::: {.front card-id="card-e9e007319ee4649c"}
What is the section ring?
:::

::: {.back card-id="card-e9e007319ee4649c"}
$$R(X, L) \coloneqq\bigoplus_{n\geq 0} H^0(X; {\mathcal{L}}{ {}^{ \scriptstyle\otimes_{{\mathcal{O}}_X}^{n} }  })$$
:::

::: {.front card-id="card-e5cda52b3ce32ece"}
Classify curves by Kodaira dimension.
:::

::: {.back card-id="card-e5cda52b3ce32ece"}
$\kappa(X) = -\infty \iff g=0$, positive curvature.

$\implies X\cong {\mathbf{P}}^1 \implies P_{\gt 0}(X) = 0$.

$\kappa(X) = 0 \iff g=1$, flat.

$\implies X\cong E$ an elliptic curve

$\implies K_X$ trivial.

$\kappa(X) = 1 \iff g\geq 2$, negative curvature.

$\implies$ general type.

$\implies K_X$ ample.
:::

::: {.front card-id="card-b361751d37669bf3"}
Classify surfaces by Kodaira dimension.
:::

::: {.back card-id="card-b361751d37669bf3"}
For a minimal smooth projective surface $X$,

$\kappa(X) = -\infty \iff$Ruled, rational.

$\implies X\cong {\mathbf{P}}^{2}$ or a minimal ruled surface.

$\implies \left|12 K_{X}\right|=\emptyset$.

$\kappa(X) = 0\iff$ abelian, hyperelliptic, K3s, Enriques.

$\implies \left|12 K_{X}\right|=\{0\}$.

$\kappa(X) = 1\iff$ elliptic

$\kappa(X) = 2 \iff$ general type.
:::

::: {.front card-id="card-edd9ac6f0fa2d3e8"}
What is **plurigenera**?
:::

::: {.back card-id="card-edd9ac6f0fa2d3e8"}
$$P_m(X)= h^0(\omega_X^m) = h^0(\mathcal{O}_X(m K_X))$$
Measures the size of a canonical model of $X$, $\mathop{\mathrm{Proj}}(\bigoplus_{m\geq 0} H^0(K_X^m))$.

Can prove a variety is not rational by showing $P_m(X) > 0$ for some $m>0$.
:::

::: {.front card-id="card-241e5ed95b035be5"}
What is a variety of general type?
:::

::: {.back card-id="card-241e5ed95b035be5"}
Maximal possible Kodaira dimension: $\kappa(X) = \dim(X)$, e.g. any variety with ample canonical.
:::

::: {.front card-id="card-cd129aadf37058b3"}
What is **irregularity**?
:::

::: {.back card-id="card-cd129aadf37058b3"}
$$q(X) \coloneqq h^{0, 1} = h^1({\mathcal{O}}_X)$$
For a smooth complex projective surface, $q(X)=h^0(\Omega_X^1)$.

Measures the difference $p_g(X) - p_a(X)$ between geometric and arithmetic genus.
:::

::: {.front card-id="card-66ce9a474b7f4659"}
What is a **rational** variety?
:::

::: {.back card-id="card-66ce9a474b7f4659"}
Normal and birational $X\overset{\sim}{\dashrightarrow}{\mathbf{P}}^N$ for some $N$.
:::

::: {.front card-id="card-887ac50e6202d5f9"}
What is a **unirational** variety?
:::

::: {.back card-id="card-887ac50e6202d5f9"}
Idea: Luroth shows that if $k \subsetneq L \subseteq k(x)$ then $L = k(x)$ and asks the same for subfields $L \subseteq k(x_1,\cdots, x_n)$. If $L = k(X)$ for a variety, this induces ${\mathbf{P}}^n \dashrightarrow X$ with dense image; call such $X$ unirational.

Normal and admits a dominant rational map ${\mathbf{P}}^N\dashrightarrow X$ for some $N$, or dominated by a rational variety so that $k({\mathbf{P}}^n)/k(X)$ is a purely transcendental (separable) extension of finite type.

Idea: similar to rational, e.g. $h^0(\Omega^{\geq 1}_X) = 0$, Luroth asks if unirational implies rational. True for curves, false for 3-folds and higher.
:::

::: {.front card-id="card-c99c177d102ccfce"}
What is a **uniruled** variety?
:::

::: {.back card-id="card-c99c177d102ccfce"}
Idea: covered by rational curves, for every $x\in X$ there is a nonconstant morphism ${\mathbf{P}}^1\to X$ with $f(0) =x$, i.e. for every point one can find a rational curve containing it.

More precisely, $\exists Y$ and a dominant rational morphism $Y\times {\mathbf{P}}^1\dashrightarrow X$ which does not factor through the projection to $Y$, i.e. dominated by a ruled variety.
:::

::: {.front card-id="card-749c097614ea7db3"}
What is a **ruled** variety?
:::

::: {.back card-id="card-749c097614ea7db3"}
Birational to $Y\times {\mathbf{P}}^1$ for some $Y$.
:::

::: {.front card-id="card-15b64175339c625d"}
What is a minimal model?
:::

::: {.back card-id="card-15b64175339c625d"}
For $\kappa(X) \geq 0$, a birational $\tilde X\to X$ with $K_{\tilde X}$ nef and $\tilde X$ terminal.
:::

::: {.front card-id="card-704cc7c711f84485"}
What is a terminal singularity? Canonical singularity? Log-terminal singularity?
:::

::: {.back card-id="card-704cc7c711f84485"}
For a resolution $\pi: \tilde X\to X$, write $K_{\tilde X} \equiv_{\mathbf{Q}}\pi^* K_{X} + \sum a_i E_i$ with $a_i\in {\mathbf{Q}}$, then

Terminal: $a_i > 0$.

Canonical: $a_i \geq 0$

Log-terminal: $a_i > -1$.
:::

::: {.front card-id="card-3c64e95c0377e039"}
What is Luroth's problem?
:::

::: {.back card-id="card-3c64e95c0377e039"}
Rational $\implies$ unirational, is the converse true? Equivalently, is every subfield of a purely transcendental field extension again purely transcendental? True in dimension 1 by Galois theory.
:::

::: {.front card-id="card-41bf32b10f9d0aae"}
What is Castelnuovo's theorem on complex surfaces?
:::

::: {.back card-id="card-41bf32b10f9d0aae"}
If $q(X), P_2(X)$ vanish then $X$ is rational. This implies that unirational surfaces are rational. Note that $P_1(X)$ vanishing is not enough, viz. the Enriques surfaces.
:::

::: {.front card-id="card-a52d9643c2df5f41"}
What is a **rationally connected** variety?
:::

::: {.back card-id="card-a52d9643c2df5f41"}
Any pair $p,q\in X$ can be connected by a chain of rational curves, or equivalently there is a morphism $f: {\mathbf{P}}^1\to X$ with $f({\left[ {0: 1} \right]}) = p$ and $f({\left[ {1: 0} \right]}) = q$.
:::

::: {.front card-id="card-70053316f342a559"}
What is a ${\mathbf{Q}}{\hbox{-}}$Gorenstein variety?
:::

::: {.back card-id="card-70053316f342a559"}
$K_X \in {\mathbf{Q}}{\hbox{-}}\operatorname{CDiv}(X)$.
:::

::: {.front card-id="card-0f10ef5a77d3c549"}
What is the Mori cone?
:::

::: {.back card-id="card-0f10ef5a77d3c549"}
The Mori cone $\overline{\operatorname{NE}}(X)\subset N_1(X)_{\mathbb R}$ is the closure of the convex cone generated by numerical classes of effective curves on a projective variety $X$. Its dual cone in $N^1(X)_{\mathbb R}$ is the nef cone.
:::

::: {.front card-id="card-ee210ddebc16c66b"}
What is K-stability?
:::

::: {.back card-id="card-ee210ddebc16c66b"}
Modern version of GIT, since GIT doesn't work well for varieties of $\dim \geq 2$.

For Fanos, equivalent to admitting a constant scalar curvature metric.
:::

::: {.front card-id="card-fb89ad30738ffe16"}
How are plurigenera related to the arithmetic or geometric genus?
:::

::: {.back card-id="card-fb89ad30738ffe16"}
$P_1(X) = g(X)$ for smooth projective curves.
:::

::: {.front card-id="card-97356860c51b279d"}
What is $P_m(X)$ for $X$ a smooth complete curve, in terms of $g(X)$?
:::

::: {.back card-id="card-97356860c51b279d"}
$g=0 \implies X \cong {\mathbf{P}}^1 \implies \omega_X \cong {\mathcal{O}}_{{\mathbf{P}}^1}(-2) \implies P_{\geq 0}(X) = 0$.

$g=1 \implies \omega_X\cong {\mathcal{O}}_X \implies P_{\geq 0}(X) = 1$.

$g\geq 2 \implies \deg \omega_X^m = m(2g-2)\implies P_{\geq 2}(X) = m(2g-2) - (g-1)$
:::

::: {.front card-id="card-fa113b1d45d9bca3"}
What is $P_m(X)$ for $X \subseteq {\mathbf{P}}^n$ a smooth hypersurface of degree $d$?
:::

::: {.back card-id="card-fa113b1d45d9bca3"}
Write ${\mathcal{O}}_X(1) = { \left.{{{\mathcal{O}}_{{\mathbf{P}}^n}(1)}} \right|_{{X}} }$, then $\omega_X \cong {\mathcal{O}}_X(d - (n+1) )$.

$d < n + 1 \implies P_{\geq 0}(X) = 0$

$d = n +1 \implies \omega_X \cong {\mathcal{O}}_X \implies P_{\geq 1}(X) = 1$

$d > n+1 \implies \omega_X \in \operatorname{Pic}(X)^{{\mathrm{v.amp}}} \implies \cdots$
$$P_{m \gg 0}(X) = {d(d-n-1) \over(n-1)! }\cdot m^{n-1} + { \mathsf{O}}(m^{n-2})$$
:::

::: {.front card-id="card-bff7d57e6cbbd0e0"}
What is $\omega_X$ for $X \subseteq {\mathbf{P}}^{n+1}$ a smooth complete intersection of hypersurfaces of degrees $d_1,\cdots, d_k$?
:::

::: {.back card-id="card-bff7d57e6cbbd0e0"}
$\omega_X \cong {\mathcal{O}}_X(\sum d_i - (n+1))$.
:::

::: {.front card-id="card-da0dd170d4c7b84f"}
What is a weak CY?
:::

::: {.back card-id="card-da0dd170d4c7b84f"}
$X$ smooth projective with $\omega_X \cong {\mathcal{O}}_X$.
:::

::: {.front card-id="card-a75e698385fb2a5e"}
What is a (strong) CY?
:::

::: {.back card-id="card-a75e698385fb2a5e"}
A weak CY with $H^i({\mathcal{O}}_X) = 0$ for $0 \lt i \lt \dim(X)$ and $\pi_1(X({\mathbf{C}})) = 1$.
:::

::: {.front card-id="card-185cc0d094d576b5"}
Give an example of a weak but not strong CY.
:::

::: {.back card-id="card-185cc0d094d576b5"}
An abelian variety.
:::

::: {.front card-id="card-b2137074eb0b0864"}
Give examples of strong CYs.
:::

::: {.back card-id="card-b2137074eb0b0864"}
K3s, since $\omega_X\cong {\mathcal{O}}_X$ and $H^1({\mathcal{O}}_X) = 0$, e.g.

A quartic in ${\mathbf{P}}^3$ (hypersurface of degree 4)

A complete intersection of type $(2, 3)$ in ${\mathbf{P}}^4$.

A complete intersection of type $(2,2,2$) in ${\mathbf{P}}^5$.

Hypersurfaces of degree $n+1$ in ${\mathbf{P}}^n$.
:::

::: {.front card-id="card-72941d8b176edf02"}
Classify hypersurfaces $X\subseteq {\mathbf{P}}^n$ by Kodaira dimension.
:::

::: {.back card-id="card-72941d8b176edf02"}
$\kappa(X) = -\infty \iff d\leq n$.

$\kappa(X) = 0 \iff d= n$.

$\kappa(X) = \dim(X) \iff d\geq n+2$.
:::

::: {.front card-id="card-70ffac49f824101f"}
What is a big bundle?
:::

::: {.back card-id="card-70ffac49f824101f"}
Sections grow maximally: $h^0(L^k)\geq { \mathsf{O}}( k^{\dim X} )$.
:::

::: {.front card-id="card-79afba969c884033"}
What is a nef bundle?
:::

::: {.back card-id="card-79afba969c884033"}
$L$ has non-negative degree on every irreducible curve $C$

Degree: $\deg \operatorname{div}(s)$ for $s$ any rational section of $L$.
:::

::: {.front card-id="card-ea9654ae52152e47"}
What is a big and nef bundle?
:::

::: {.back card-id="card-ea9654ae52152e47"}
$L^2 > 0$ and $L$ is nef.
:::
