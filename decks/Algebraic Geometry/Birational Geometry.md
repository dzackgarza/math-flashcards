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
For$X$ normal projective and $D\in \QQ\dash\operatorname{Div}(X)$,
$$\kappa(X, D)\coloneqq\limsup _{m \in \ZZ_{\geq 0}} \frac{\log \left(h^0\left(\mathcal{O}_X(m D)\right)\right)}{\log m}$$
Equivalently, the Iitaka dimension of the canonical
$$\kappa(X) \coloneqq\kappa(X; \omega_X)$$
Concretely: $\kappa(X) \coloneqq-\infty$ if $P_d(X) = 0$ for all $d>0$, otherwise $\kappa(X) = \min \left\{{k \in \ZZ\st{P_d\over d^k} \leq { \mathsf{O}}(1) }\right\}$ (i.e. the minimal $k$ so that $P_d(X) \in { \mathsf{O}}(d^k)$). Interpret as $P_m(X) \sim m^{\kappa(x)}$ (bounded above and below by constant multiples, for $m$ sufficiently divisible). Generally $\kappa(X) \in \left\{{-\infty}\right\}\cup\left\{{0, 1, \cdots, \dim X}\right\}$.
:::

::: {.front card-id="card-0996fd4a0ee4d958"}
What is a variety of general type?
:::

::: {.back card-id="card-0996fd4a0ee4d958"}
Maximal possible Kodaira dimension: $\kappa(X) = \dim(X)$, i.e. $\omega_X$ is big. E.g. any variety with ample canonical.
:::

::: {.front card-id="card-67f625f64dc3c847"}
What is a big line bundle (big divisor)?
:::

::: {.back card-id="card-67f625f64dc3c847"}
$\mcl\in \operatorname{Pic}(X)$ is big iff $\kappa(X; \mcl) = \dim(X)$ is maximal, i.e. $\dim \operatorname{im}\phi_{{\left\lvert {m\mcl} \right\rvert}} = \dim(X)$ for some $m\gg 0$.

Equivalently, sections grow maximally: there is $c > 0$ with $h^0({\mathcal{O}}(mD)) \geq c\cdot m^{\dim X}$ for all sufficiently large and divisible $m$.
:::

::: {.front card-id="card-a54e2a90c7831a3d"}
What is Iitaka dimension?
:::

::: {.back card-id="card-a54e2a90c7831a3d"}
For $\mcl\in \operatorname{Pic}(X)$, define the *Iitaka dimension* of $\mcl\in \operatorname{Pic}(X)$ as the maximal embedding dimension:
$$\kappa(X; \mcl) \coloneqq\sup_{m\in \ZZ_{\geq 0}} \left\{{\dim \phi_{{\left\lvert {m\mcl} \right\rvert}}(X)}\right\},\qquad \phi_{{\left\lvert {m\mcl} \right\rvert}}:X\to {\mathbf{P}}^n$$
Always have $\kappa(X; \mcl) \in \left\{{-\infty, 0, 1,\cdots, \dim(X)}\right\}$.

If $\mcl$ is not effective, define $\kappa(X; \mcl)= -\infty$.

Fact:
$$\kappa(X; \mcl) + 1 = \trdeg_k \operatorname{ff}(R(X; L))$$
where $R(X; L)$ is the section ring.
:::

::: {.front card-id="card-e9e007319ee4649c"}
What is the section ring?
:::

::: {.back card-id="card-e9e007319ee4649c"}
$$R(X, L) \coloneqq\bigoplus_{n\geq 0} H^0(X; \mcl{ {}^{ \scriptstyle\otimes_{{\mathcal{O}}_X}^{n} }  })$$
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
Define $\kappa(X) \coloneqq\operatorname{trdeg}_k \left( \bigoplus_{n\geq 0} H^0({\mathcal{O}}_X(nK_X)) \right) - 1$, or $-\infty$ if all $H^0(nK_X) = 0$ for $n > 0$. For a minimal smooth projective surface $X$,

$\kappa(X) = -\infty \iff$Ruled, rational.

$\implies X\cong {\mathbf{P}}^{2}$ or a minimal ruled surface.

$\implies \left|12 K_{X}\right|=\emptyset$.

$\kappa(X) = 0\iff$ abelian, hyperelliptic, K3s, Enriques.

$\implies \left|12 K_{X}\right|=\{0\}$.

$\kappa(X) = 1\iff$ elliptic

$\kappa(X) = 2 \iff$ general type.
:::

::: {.front card-id="card-edd9ac6f0fa2d3e8"}
What are the **plurigenera** of a smooth projective variety?
:::

::: {.back card-id="card-edd9ac6f0fa2d3e8"}
$$P_m(X)= h^0(\omega_X^m) = h^0(\mathcal{O}_X(m K_X)) = h^0( (\operatorname{det}\Omega_{X/k})^{\otimes m} )$$
This is a birational invariant. Measures the size of a canonical model of $X$, $\mathop{\mathrm{Proj}}(\bigoplus_{m\geq 0} H^0(K_X^m))$.

Can prove a variety is not rational by showing $P_m(X) > 0$ for some $m>0$.
:::

::: {.front card-id="card-cd129aadf37058b3"}
What is the **irregularity** of a smooth projective variety?
:::

::: {.back card-id="card-cd129aadf37058b3"}
The Hodge number
$$q(X) \coloneqq h^{0, 1} = h^1({\mathcal{O}}_X)$$
For a smooth complex projective variety, $q(X)=h^0(\Omega_X^1)$ by Hodge symmetry.

For a surface, it measures the difference $q = p_g(X) - p_a(X)$ between geometric and arithmetic genus.
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
For a resolution $\pi: \tilde X\to X$, write $K_{\tilde X} \equiv_\QQ\pi^* K_{X} + \sum a_i E_i$ with $a_i\in \QQ$, then

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
What is a $\QQ\dash$Gorenstein variety?
:::

::: {.back card-id="card-70053316f342a559"}
$K_X \in \QQ\dash\operatorname{CDiv}(X)$.
:::

::: {.front card-id="card-0f10ef5a77d3c549"}
What is the Mori cone?
:::

::: {.back card-id="card-0f10ef5a77d3c549"}
The Mori cone $\overline\NE(X)\subset N_1(X)_{\mathbb R}$ is the closure of the convex cone generated by numerical classes of effective curves on a projective variety $X$. Its dual cone in $N^1(X)_{\mathbb R}$ is the nef cone.
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

$d < n + 1 \implies P_{\geq 1}(X) = 0$

$d = n +1 \implies \omega_X \cong {\mathcal{O}}_X \implies P_{\geq 1}(X) = 1$

$d > n+1 \implies \omega_X \in \operatorname{Pic}(X)^{\vamp} \implies \cdots$
$$P_{m \gg 0}(X) = {d(d-n-1)^{n-1} \over(n-1)! }\cdot m^{n-1} + { \mathsf{O}}(m^{n-2})$$
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
A weak CY with $H^i({\mathcal{O}}_X) = 0$ for $0 \lt i \lt \dim(X)$ and $\pi_1(X(\CC)) = 1$.
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
Classify smooth hypersurfaces $X\subseteq {\mathbf{P}}^n$ of degree $d$ by Kodaira dimension.
:::

::: {.back card-id="card-72941d8b176edf02"}
$\kappa(X) = -\infty \iff d\leq n$.

$\kappa(X) = 0 \iff d= n+1$.

$\kappa(X) = \dim(X) \iff d\geq n+2$.
:::

::: {.front card-id="card-79afba969c884033"}
What is a nef line bundle (nef divisor)?
:::

::: {.back card-id="card-79afba969c884033"}
$D$ is nef iff $D\cdot C \geq 0$ for all irreducible curves $C$ iff $L\coloneqq{\mathcal{O}}(D)$ has non-negative degree on every irreducible curve $C$.

Degree: $\deg \operatorname{div}(s)$ for $s$ any rational section of $L|_C$.

For $D\in \QQ\dash\operatorname{CDiv}(X)$ and $Z\leq X$ a proper subvariety, $D$ is nef along $Z$ iff $D.C \coloneqq\deg_{\tilde C}(f^* D) \geq 0$ where $f: \tilde C\to C$ is the normalization, for all effective curves $C\subseteq Z$.
:::

::: {.front card-id="card-25b5396645bc9bae"}
What is the **strict transform**?
:::

::: {.back card-id="card-25b5396645bc9bae"}
For a blowup $\pi:\widetilde X\to X$ with center $Z$ and a closed subscheme $Y\subseteq X$, the strict transform is the scheme-theoretic closure of $\pi^{-1}(Y\setminus Z)$ in $\widetilde X$.
:::

::: {.front card-id="card-2672951a3cb0357e"}
What is a birational map?
:::

::: {.back card-id="card-2672951a3cb0357e"}
A rational map with a rational inverse.
:::

::: {.front card-id="card-9db7a801cc266d51"}
What is the **blowup** of a variety?
:::

::: {.back card-id="card-9db7a801cc266d51"}
For $\operatorname{Bl}_0 {\mathbf{A}}^n$: take ${\mathbf{A}}^n\times {\mathbf{P}}^{n-1}$ with coordinates ${\left[ {x_0, \cdots, x_{n-1}} \right]}, {\left[ {y_0:\cdots : y_{n-1}} \right]}$, so the closed subsets are $V(f)$ where $f$ is a polynomial in $x_i, y_i$ which is homogeneous in the $y_i$. Take the blowup to be the subset $\left\{{x_iy_j = x_j y_i \st1\leq i,j\leq n-1}\right\} = \left\{{2\times 2\text{ minors of} \begin{bmatrix}x_0 & x_1 & \cdots & x_n \\ y_0 & y_1 & \cdots & y_n \end{bmatrix}}\right\}$.

Then $\exists \pi: \operatorname{Bl}_0 {\mathbf{A}}^n \to {\mathbf{A}}^n$ where ${\sharp}\pi^{-1}(p) = 1$ for $p\neq 0$ and $\pi^{-1}(0)\cong {\mathbf{P}}^{n-1}$ corresponding to all lines through $0$.

For $\operatorname{Bl}_Y {\mathbf{A}}^n$ with $Y \subseteq {\mathbf{A}}^n$ a closed subvariety: take $\cl_{\operatorname{Bl}_0 {\mathbf{A}}^n}\qty{\pi^{-1}(Y\setminus\left\{{0}\right\})}$.
:::

::: {.front card-id="card-77f1ef48e07e3dc0"}
What is the **blowup of a scheme along a subscheme**? How does this recover blowups for varieties?
:::

::: {.back card-id="card-77f1ef48e07e3dc0"}
Can generally blowup along a coherent sheaf of ideals $\mci$ on $X$: take the sheaf of graded algebras $\tilde \mci\coloneqq\bigoplus_{d\geq 0}\mci^d$ where $\mci^0 \coloneqq{\mathcal{O}}_X$ and set $\tilde X \coloneqq\mathop{\mathrm{Proj}}\tilde \mci$. Can do this with the ideal of sheaf of $Y\hookrightarrow X$ a closed subscheme.

For $X={\mathbf{A}}^n_{/ {k}}$, $p=0$ corresponds to $I = \left\langle{x_0,\cdots,x_n}\right\rangle$ and $\tilde X \coloneqq\mathop{\mathrm{Proj}}S$ where $S\coloneqq\bigoplus_{d\geq 0} I^d$; then setting $X \coloneqq\operatorname{Spec}A, A\coloneqq k[x_1, \cdots, x_{n}]$ there is a surjection $A[y_1,\cdots, y_n]$ where $y_i\mapsto x_i, {\left\lvert {x_i} \right\rvert} = 1$, making $\tilde X$ isomorphic to a closed subscheme of $\mathop{\mathrm{Proj}}A[y_1,\cdots, y_n] \cong {\mathbf{P}}^{n-1}_{/ {A}}$, and the ideal of definition is generated by $\left\{{x_iy_j - x_jy_i}\right\}$.
:::

::: {.front card-id="card-93938d5c9783d630"}
Discuss properties of the blowup morphism.
:::

::: {.back card-id="card-93938d5c9783d630"}
It is an isomorphism away from $p$ and $\pi^{-1}(p)$, for varieties $X$ it is birational, proper, and surjective; if $X$ is quasiprojective then $\tilde X$ is too and $\pi$ is projective.
:::

::: {.front card-id="card-3ee6736250e4d3aa"}
What is a **resolution of singularities**?
:::

::: {.back card-id="card-3ee6736250e4d3aa"}
For varieties $X$, a regular irreducible variety $\tilde X$ admitting a proper birational morphism $\pi: \tilde X\to X$ and restricts to an isomorphism on $f^{-1}(X^{\mathrm{reg}})$. For curves, the normalization suffices since it removes all singularities in codimension 1.
:::

::: {.front card-id="card-8ec58f09e82af130" tags="definition"}
What is: Blowups
:::

::: {.back card-id="card-8ec58f09e82af130"}
The blowup of a scheme $X$ along an ideal sheaf $I$ is $\operatorname{Bl}_I X=\operatorname{Proj}_X\bigoplus_{n\geq0}I^n$. It is universal among maps $Y\to X$ for which the pulled-back ideal $I\mathcal O_Y$ is invertible.
:::

::: {.front card-id="card-57d6edcbbc895cf2"}
What is a **contraction**?
:::

::: {.back card-id="card-57d6edcbbc895cf2"}
A surjective proper morphism $f:X\to Y$ between normal projective schemes where $f_* {\mathcal{O}}_X \cong {\mathcal{O}}_Y$, or equivalently the geometric fibers are connected.
:::

::: {.front card-id="card-cdc67f784e52a114"}
What is a **contractible curve**?
:::

::: {.back card-id="card-cdc67f784e52a114"}
E.g. if starting with a proper normal algebraic surface $X$ and a curve $C$ in $X$, a contraction morphism $\pi: X\to Y$ where $\pi(C)$ is a point.
:::

::: {.front card-id="card-28accb71191608ee"}
What is a **resolution**?
:::

::: {.back card-id="card-28accb71191608ee"}
For $X$ singular, a proper morphism $\pi: W\to X$ where $W$ is smooth, $\pi^{-1}(X^{\mathsf{sm}}) \subseteq W$ is dense and $\pi$ induces an isomorphism on the smooth locus.
:::

::: {.front card-id="card-63ead0b6b3f67ab5"}
What is a **minimal resolution**?
:::

::: {.back card-id="card-63ead0b6b3f67ab5"}
Minimal $W$ is minimal iff whenever $W'\to V$ is another resolution, it factors as $W'\to W\to V$.

Exist uniquely in dimensions 1 and 2, but may not in higher dimensions. For a surface with an isolated singularity at 0: $\pi: W\to V$ is minimal iff $\pi^{-1}(0)$ does not contain any exceptional curves of the first kind. Any non-minimal resolution must contain a -1 curve.
:::

::: {.front card-id="card-701972d5f4fef18e"}
What does it mean for a line bundle on a surface to be big and nef? Why care?
:::

::: {.back card-id="card-701972d5f4fef18e"}
$L^2 > 0$ and $L$ is nef.

Weaker than ample, but results for ample often still hold for just big and nef. Note that $L^2 > 0$ is not quite the right definition of "big" alone.

Big and nef on a K3 implies effective.
:::

::: {.front card-id="card-3cb9dc2bc3da922a"}
What is the Base Point Free theorem?
:::

::: {.back card-id="card-3cb9dc2bc3da922a"}
If $L\in \operatorname{Pic}(X)$ is big and nef, then $L^n$ is globally generated for some $n$.

Holds for smooth projective varieties over $\CC$ when $L\otimes\omega_X {}^{ \vee }$ is big and nef.
:::

::: {.front card-id="card-719758760811ef26"}
What is the Zariski decomposition of an effective divisor?
:::

::: {.back card-id="card-719758760811ef26"}
$D = P + N$ where $P, N \in \NS(X)_\QQ$ with $P\in \operatorname{Nef}(X)$ the positive part and $N = \sum a_i C_i$ effective (with $a_i \in \QQ_{\gt 0})$ where $P.C_i = 0$ for all $i$ and the intersection matrix $(C_i . C_j)$ is negative definite.
:::

::: {.front card-id="card-7ee99fa7712a9959"}
Discuss finite generation of the section ring $R(X; L)$ for $L\in \operatorname{Pic}(X)$.
:::

::: {.back card-id="card-7ee99fa7712a9959"}
If $X$ is a smooth surface and $L$ is big, then $R(X; L)$ is finitely generated iff $P$ is semiample.

$R(; L)$ is finitely generated for any $L\in \operatorname{Pic}(X)$ whatsoever for a K3.
:::

::: {.front card-id="formula-smooth-center-blowup-euler" tags="formula"}
For the blowup $\widetilde X\to X$ of a smooth projective complex variety along a smooth center $Z$ of codimension $c\ge2$, compute $e(\widetilde X)$.
:::

::: {.back card-id="formula-smooth-center-blowup-euler"}
$$e(\widetilde X)=e(X)+(c-1)e(Z).$$
:::

::: {.front card-id="formula-point-blowup-exceptional-power" tags="formula"}
For a point blowup of a smooth complex $n$-fold, $n\ge2$, compute the top intersection of the exceptional divisor $E$.
:::

::: {.back card-id="formula-point-blowup-exceptional-power"}
$$E^n=(-1)^{n-1}.$$
:::

::: {.front card-id="formula-cyclic-quotient-resolution" tags="formula"}
For the complex cyclic quotient singularity $\frac1r(1,a)$, with $0<a<r$ and $\gcd(r,a)=1$, write $r/a=[b_1,\ldots,b_s]^-$ with $b_i\ge2$. Compute the exceptional intersection matrix of its minimal resolution.
:::

::: {.back card-id="formula-cyclic-quotient-resolution"}
$$E_i^2=-b_i,\qquad E_iE_{i+1}=1,\qquad E_iE_j=0\quad(|i-j|>1),\qquad \frac ra=b_1-\cfrac1{b_2-\cfrac1{\ddots-\cfrac1{b_s}}}.$$
:::

::: {.front card-id="formula-surface-discrepancy-equations" tags="formula"}
For a resolution $\pi:\widetilde X\to X$ of a normal complex $\mathbb Q$-Gorenstein surface singularity with smooth rational exceptional curves $E_i$, give the canonical discrepancy formula and the linear system for its coefficients.
:::

::: {.back card-id="formula-surface-discrepancy-equations"}
$$K_{\widetilde X}=\pi^*K_X+\sum_i a_iE_i,\qquad \sum_i a_i(E_iE_j)=-2-E_j^2.$$
:::

::: {.front card-id="formula-du-val-resolution-invariants" tags="formula"}
For the minimal resolution $\pi:\widetilde X\to X$ of a complex Du Val surface singularity, compute the exceptional self-intersections, canonical discrepancy, and $R^1\pi_*\mathcal O_{\widetilde X}$.
:::

::: {.back card-id="formula-du-val-resolution-invariants"}
$$E_i^2=-2,\qquad K_{\widetilde X}=\pi^*K_X,\qquad R^1\pi_*\mathcal O_{\widetilde X}=0.$$
:::

::: {.front card-id="formula-normalization-canonical-conductor" tags="formula"}
For a demi-normal complex $\mathbb Q$-Gorenstein surface $X$, with normalization $\nu:X^\nu\to X$ and conductor divisor $D^\nu$, express $\nu^*K_X$.
:::

::: {.back card-id="formula-normalization-canonical-conductor"}
$$\nu^*K_X=K_{X^\nu}+D^\nu.$$
:::
