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

::: {.front card-id="card-b361751d37669bf3" tags="theorem"}
Classify smooth minimal complex projective surfaces by Kodaira dimension.
:::

::: {.back card-id="card-b361751d37669bf3"}
Define $\kappa(X) \coloneqq\operatorname{trdeg}_k \left( \bigoplus_{n\geq 0} H^0({\mathcal{O}}_X(nK_X)) \right) - 1$, or $-\infty$ if all $H^0(nK_X) = 0$ for $n > 0$. For a minimal smooth complex projective surface $X$,

$\kappa(X) = -\infty \iff$Ruled, rational.

$\implies X\cong {\mathbf{P}}^{2}$ or a minimal ruled surface.

$\implies \left|12 K_{X}\right|=\emptyset$.

$\kappa(X)=0$ if and only if $X$ is abelian, bielliptic (also called hyperelliptic), K3, or Enriques.

$\implies \left|12 K_{X}\right|=\{0\}$.

$\kappa(X)=1$ implies that $X$ is elliptic; these are the properly elliptic surfaces.

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

::: {.front card-id="card-41bf32b10f9d0aae" tags="theorem"}
State Castelnuovo's rationality criterion for a smooth complex projective surface $S$. Does vanishing of $q$ and $P_1$ suffice?
:::

::: {.back card-id="card-41bf32b10f9d0aae"}
One has
$$S\text{ rational}\iff q(S)=0\text{ and }P_2(S)=0.$$
Vanishing of $q$ and $P_1$ does not suffice, as Enriques surfaces show. The criterion also implies that unirational complex surfaces are rational.
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

::: {.front card-id="card-3cb9dc2bc3da922a" tags="theorem"}
Let $(X,\Delta)$ be a complex projective klt pair and $D$ a nef Cartier divisor. State the Kawamata–Shokurov base-point-free theorem.
:::

::: {.back card-id="card-3cb9dc2bc3da922a"}
If $aD-(K_X+\Delta)$ is nef and big for some $a>0$, then $\lvert mD\rvert$ is base-point-free for every sufficiently large integer $m$. In particular, for smooth projective $X$, a nef line bundle $L$ with $L\otimes\omega_X^{-1}$ nef and big is semiample.
:::

::: {.front card-id="card-719758760811ef26" tags="theorem"}
State the Zariski–Fujita decomposition of a pseudo-effective $\mathbb Q$-divisor $D$ on a smooth complex projective surface. Include uniqueness, sections, and the volume when $D$ is big.
:::

::: {.back card-id="card-719758760811ef26"}
There is a unique decomposition $D=P+N$ with $P$ nef, $N=\sum_i a_iC_i$ effective, $PC_i=0$, and $(C_iC_j)$ negative definite when $N\ne0$; the nonzero coefficients $a_i$ are positive rational numbers. For all sufficiently divisible $m$, multiplication by the section of $mN$ gives
$$H^0(S,\mathcal O_S(mP))\xrightarrow{\sim}H^0(S,\mathcal O_S(mD)).$$
If $D$ is big, then $\operatorname{vol}(D)=P^2$.
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

::: {.front card-id="theorem-iitaka-sections" tags="theorem"}
Let $D$ be a Cartier divisor on a smooth complex projective variety with $\kappa(X,D)\ge0$. State the asymptotic growth of sections and the stabilization of the maps given by sufficiently divisible multiples.
:::

::: {.back card-id="theorem-iitaka-sections"}
For all sufficiently large divisible $m$,
$$h^0(X,mD)\asymp m^{\kappa(X,D)}.$$
The maps $\varphi_{\lvert mD\rvert}$ have image of dimension $\kappa(X,D)$ and are birationally equivalent to a fixed Iitaka fibration.
:::

::: {.front card-id="theorem-iitaka-easy-addition" tags="theorem"}
Let $f:X\to Y$ be a surjective morphism of smooth complex projective varieties with connected fibers and general fiber $F$. State Iitaka's easy addition inequality and its consequence when $\kappa(F)=-\infty$.
:::

::: {.back card-id="theorem-iitaka-easy-addition"}
One has
$$\kappa(X)\le\kappa(F)+\dim Y.$$
In particular, $\kappa(F)=-\infty$ implies $\kappa(X)=-\infty$.
:::

::: {.front card-id="theorem-rational-singularities" tags="theorem"}
Let $Y$ be a complex variety with rational singularities and $f:X\to Y$ a resolution. State the direct-image identities. What do klt singularities imply?
:::

::: {.back card-id="theorem-rational-singularities"}
One has
$$f_*\mathcal O_X=\mathcal O_Y,\qquad R^if_*\mathcal O_X=0\quad(i>0).$$
A normal complex variety with klt singularities has rational singularities. Rational singularities are Cohen–Macaulay, so klt varieties are Cohen–Macaulay.
:::

::: {.front card-id="theorem-inversion-adjunction" tags="theorem"}
Let $X$ be smooth over $\mathbb C$, $S\subset X$ a smooth divisor, and $\Delta\ge0$ an effective $\mathbb Q$-divisor not containing $S$. State adjunction and inversion of adjunction.
:::

::: {.back card-id="theorem-inversion-adjunction"}
One has
$$(K_X+S+\Delta)|_S=K_S+\Delta|_S,$$
and
$$(X,S+\Delta)\text{ is plt near }S\iff(S,\Delta|_S)\text{ is klt}.$$
For a normal ambient pair with reduced boundary component $S$ and $K_X+S+\Delta$ $\mathbb Q$-Cartier, the normalized adjunction boundary is the different on $S^\nu$: the pullback of $(K_X+S+\Delta)|_S$ is $K_{S^\nu}+\operatorname{Diff}_{S^\nu}(\Delta)$.
:::

::: {.front card-id="theorem-hironaka-resolution" tags="theorem"}
State resolution of singularities for a reduced variety over a field of characteristic zero, including the behavior over the regular locus and the exceptional divisor.
:::

::: {.back card-id="theorem-hironaka-resolution"}
There is a proper birational morphism $\pi:\widetilde X\to X$ with $\widetilde X$ smooth, which is an isomorphism over the regular locus of $X$. It can be chosen so that the exceptional locus is a divisor with simple normal crossings.
:::

::: {.front card-id="theorem-eliminate-indeterminacy" tags="theorem"}
For a rational map $f:X\dashrightarrow Y$ between smooth projective varieties in characteristic zero, state elimination of indeterminacies.
:::

::: {.back card-id="theorem-eliminate-indeterminacy"}
There is a sequence of blowups along smooth centers
$$X'=X_r\to X_{r-1}\to\cdots\to X_0=X$$
such that the composite rational map $X'\dashrightarrow Y$ extends to a morphism $X'\to Y$. The centers can be chosen over the locus where $f$ is undefined.
:::

::: {.front card-id="theorem-weak-factorization" tags="theorem"}
State weak factorization for a birational map between smooth complete varieties in characteristic zero, including the constraint on an open set where the map is an isomorphism.
:::

::: {.back card-id="theorem-weak-factorization"}
The map factors through smooth complete varieties as a finite sequence of blowups and blowdowns along smooth centers. All centers can be chosen disjoint from a common open set on which the original map is an isomorphism.
:::

::: {.front card-id="theorem-surface-morphism-factorization" tags="theorem"}
How does a proper birational morphism $f:S\to T$ between smooth complex projective surfaces factor?
:::

::: {.back card-id="theorem-surface-morphism-factorization"}
It is a composite of point blowups:
$$S=S_r\longrightarrow S_{r-1}\longrightarrow\cdots\longrightarrow S_0=T,$$
where each $S_i\to S_{i-1}$ is the blowup of a smooth point.
:::

::: {.front card-id="theorem-castelnuovo-contraction" tags="theorem"}
Let $E$ be a smooth rational curve with $E^2=-1$ on a smooth complex projective surface $S$. State Castelnuovo contraction, including the properties of the target and the inverse construction.
:::

::: {.back card-id="theorem-castelnuovo-contraction"}
There is a birational morphism $S\to T$ to a smooth projective surface that contracts exactly $E$ to a smooth point $p$. The surface $S$ is the blowup $\operatorname{Bl}_pT$, and the contraction is the blowup morphism.
:::

::: {.front card-id="theorem-exceptional-negative-definite" tags="theorem"}
Let $f:S\to T$ be a projective birational morphism of normal complex projective surfaces, with $S$ smooth. What can be said about the intersection matrix of the exceptional curves above a fixed point of $T$?
:::

::: {.back card-id="theorem-exceptional-negative-definite"}
The matrix is negative definite:
$$\sum_{i,j}a_i a_j(E_iE_j)<0\qquad\text{for every nonzero real vector }(a_i).$$
:::

::: {.front card-id="theorem-negativity-lemma" tags="theorem"}
Let $f:Y\to X$ be projective and birational between normal varieties, and let $D$ be an $\mathbb R$-Cartier divisor with $-D$ relatively nef. What does $f_*D\ge0$ imply? State the exceptional-divisor case.
:::

::: {.back card-id="theorem-negativity-lemma"}
One has $D\ge0$. In particular, if $E$ is $f$-exceptional and $-E$ is $f$-nef, then $E\ge0$.
:::

::: {.front card-id="theorem-cone-klt" tags="theorem"}
For a complex projective klt pair $(X,\Delta)$, state the cone theorem, including the generators, length bound, and local finiteness.
:::

::: {.back card-id="theorem-cone-klt"}
There are rational curves $C_i$ spanning $(K_X+\Delta)$-negative extremal rays such that
$$\overline{\operatorname{NE}}(X)=\overline{\operatorname{NE}}(X)_{K_X+\Delta\ge0}+\sum_i\mathbb R_{\ge0}[C_i],\qquad 0<-(K_X+\Delta)C_i\le2\dim X.$$
These rays are locally finite in the open half-space where $K_X+\Delta$ is negative.
:::

::: {.front card-id="theorem-extremal-contraction" tags="theorem"}
Let $F$ be a $(K_X+\Delta)$-negative extremal face for a complex projective klt pair. State the contraction theorem.
:::

::: {.back card-id="theorem-extremal-contraction"}
There is a projective morphism $\varphi_F:X\to Y$ to a normal projective variety with connected fibers such that, for every integral curve $C$,
$$\varphi_F(C)\text{ is a point}\iff[C]\in F,\qquad(\varphi_F)_*\mathcal O_X=\mathcal O_Y.$$
:::

::: {.front card-id="theorem-surface-abundance" tags="theorem"}
For a smooth minimal complex projective surface $S$ with $\kappa(S)\ge0$, what does abundance say about the canonical divisor?
:::

::: {.back card-id="theorem-surface-abundance"}
The canonical divisor $K_S$ is semiample: $\lvert mK_S\rvert$ is base-point-free for every sufficiently large divisible positive integer $m$.
:::

::: {.front card-id="theorem-canonical-finite-generation" tags="theorem"}
State finite generation of the canonical ring for a smooth projective variety in characteristic zero. What follows in general type?
:::

::: {.back card-id="theorem-canonical-finite-generation"}
The graded ring
$$R(X,K_X)=\bigoplus_{m\ge0}H^0(X,mK_X)$$
is finitely generated. If $X$ is of general type, its canonical model
$$X_{\mathrm{can}}=\operatorname{Proj}R(X,K_X)$$
is projective and birational to $X$.
:::

::: {.front card-id="theorem-surface-minimal-uniqueness" tags="theorem"}
What existence and uniqueness statement holds for the smooth minimal model of a smooth complex projective surface $S$ with $\kappa(S)\ge0$?
:::

::: {.back card-id="theorem-surface-minimal-uniqueness"}
The surface has a smooth minimal model, and any two such models are isomorphic. More strongly, a birational map between smooth minimal projective surfaces of nonnegative Kodaira dimension is an isomorphism.
:::

::: {.front card-id="theorem-siu-plurigenera" tags="theorem"}
Let $f:X\to\Delta$ be a smooth projective family of complex varieties over a connected disk. State invariance of plurigenera.
:::

::: {.back card-id="theorem-siu-plurigenera"}
For every integer $m\ge0$,
$$h^0(X_t,\omega_{X_t}^{\otimes m})$$
is independent of $t\in\Delta$.
:::

::: {.front card-id="application-contraction-minus-one" tags="application"}
Let $E$ be a smooth rational curve with $E^2=-1$ on a smooth complex projective surface $S$. Can it be contracted while keeping the target smooth? Identify the theorem and the inverse construction.
:::

::: {.back card-id="application-contraction-minus-one"}
Castelnuovo contraction gives a morphism $S\to T$ to a smooth projective surface, contracting exactly $E$ to a smooth point $p$. The inverse construction is $S\cong\operatorname{Bl}_pT$.
:::

::: {.front card-id="application-contraction-minus-two" tags="application"}
Let $E$ be a smooth rational curve with $E^2=-2$ on a smooth complex projective surface $S$. Could a birational morphism to a smooth projective surface contract exactly $E$? Which factorization result decides this, and why is negative self-intersection insufficient?
:::

::: {.back card-id="application-contraction-minus-two"}
No. A birational morphism between smooth projective surfaces factors into point blowups. If its exceptional locus consisted of a single irreducible curve, there would be just one blowup and its exceptional curve would have square $-1$. Thus $E^2=-2$ rules out a smooth target for such a contraction. Negative definiteness alone does not give Castelnuovo's smooth-point contraction.
:::

::: {.front card-id="application-zariski-fixed-exceptional" tags="application"}
On $S=\operatorname{Bl}_p\mathbb P^2_{\mathbb C}$, write $H$ for the pullback of a line and $E$ for the exceptional curve. Find the Zariski decomposition of $D=H+E$, its volume, and $h^0(S,mD)$ for $m\ge0$. Explain why $D^2$ is not the volume.
:::

::: {.back card-id="application-zariski-fixed-exceptional"}
The decomposition is $P=H$ and $N=E$: $H$ is nef, $HE=0$, and $E^2=-1$. Zariski decomposition gives $\operatorname{vol}(D)=P^2=1$, whereas $D^2=0$. Multiplication by the section of $mE$ identifies sections of $mH$ and $mD$, so
$$h^0(S,mD)=h^0(\mathbb P^2,\mathcal O(m))=\binom{m+2}{2}.$$
:::

::: {.front card-id="application-extremal-product-contractions" tags="application"}
For $S=\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}$, identify the extremal rays of the curve cone and their contractions. Are these contractions birational?
:::

::: {.back card-id="application-extremal-product-contractions"}
The cone is generated by the two fiber classes, since effective curve classes have nonnegative bidegrees. Each fiber has $K_S$-degree $-2$, so each ray is $K_S$-negative. The associated contraction is the projection that collapses those fibers. Both contractions have one-dimensional target and are of fiber type, not birational.
:::

::: {.front card-id="application-fano-nef-semiample" tags="application"}
Let $X$ be smooth complex projective with $-K_X$ ample, and let $D$ be nef Cartier. Must some positive multiple of $D$ be globally generated? Choose a theorem and check its positivity assumption.
:::

::: {.back card-id="application-fano-nef-semiample"}
Yes. The divisor $D-K_X$ is ample, being the sum of a nef divisor and an ample divisor, so it is nef and big. The base-point-free theorem applies with boundary zero and $a=1$, giving base-point-freeness of $|mD|$ for every sufficiently large $m$.
:::

::: {.front card-id="application-resolve-plane-pencil" tags="application"}
Resolve the rational map $\mathbb P^2_{\mathbb C}\dashrightarrow\mathbb P^1_{\mathbb C}$, $[x:y:z]\mapsto[x:y]$. Give its indeterminacy locus, a smooth resolution, and the fibers of the resulting morphism.
:::

::: {.back card-id="application-resolve-plane-pencil"}
The only indeterminacy point is $p=[0:0:1]$. Blowing up $p$ resolves the pencil of lines through $p$. The resulting morphism $\operatorname{Bl}_p\mathbb P^2\to\mathbb P^1$ has fibers the strict transforms of those lines, each isomorphic to $\mathbb P^1$; the exceptional curve records the direction and is a section.
:::

::: {.front card-id="application-iitaka-elliptic-fibration" tags="application"}
Let $S\to B$ be a surjective morphism with connected fibers from a smooth complex projective surface to a smooth projective curve, with general fiber elliptic. Can $S$ be of general type? Which theorem gives a bound without computing $K_S^2$?
:::

::: {.back card-id="application-iitaka-elliptic-fibration"}
No. The general fiber has Kodaira dimension zero. Iitaka's easy addition theorem gives $\kappa(S)\le0+\dim B=1$, whereas a surface of general type has Kodaira dimension two.
:::

::: {.front card-id="application-iitaka-rational-fibration" tags="application"}
Let $X\to Y$ be a surjective morphism of smooth complex projective varieties with connected fibers and general fiber $\mathbb P^1$. Can $X$ have a nonzero pluricanonical section? Choose the relevant form of the addition theorem.
:::

::: {.back card-id="application-iitaka-rational-fibration"}
No. The general fiber has Kodaira dimension $-\infty$, so Iitaka's easy addition theorem gives $\kappa(X)=-\infty$. Thus $H^0(X,mK_X)=0$ for every $m>0$.
:::

::: {.front card-id="application-canonical-model-general-type" tags="application"}
Let $X$ be a smooth complex projective $n$-fold of general type. Which results give a projective canonical model and show that its dimension is $n$?
:::

::: {.back card-id="application-canonical-model-general-type"}
BCHM gives finite generation of $R(X,K_X)$, hence a projective model $\operatorname{Proj}R(X,K_X)$. General type means $\kappa(X)=n$; Iitaka's section-growth theorem gives $h^0(X,mK_X)\asymp m^n$ for sufficiently divisible $m$. Consequently the canonical model has dimension $n$.
:::

::: {.front card-id="application-rationality-enriques-test" tags="application"}
A smooth complex projective surface has $q=p_g=0$. Is that enough to conclude rationality? Give a counterexample and identify the extra plurigenus test that does decide rationality.
:::

::: {.back card-id="application-rationality-enriques-test"}
An Enriques surface has $q=p_g=0$ but $P_2=1$, and is not rational. Castelnuovo's criterion uses $q=0$ and $P_2=0$, not merely $P_1=p_g=0$. Under these two vanishing conditions the surface is rational.
:::

::: {.front card-id="application-minimal-model-uniqueness-boundary" tags="application"}
Compare minimal-model uniqueness for a smooth complex projective surface with $\kappa\ge0$ and for a rational surface. Why do $\mathbb F_0$ and $\mathbb F_2$ test the hypothesis?
:::

::: {.back card-id="application-minimal-model-uniqueness-boundary"}
A surface with $\kappa\ge0$ has a unique smooth minimal model up to isomorphism. Rational surfaces need not: $\mathbb F_0$ and $\mathbb F_2$ are birational and minimal, but are not isomorphic. The latter has a curve of self-intersection $-2$, whereas all effective curve classes on $\mathbb F_0=\mathbb P^1\times\mathbb P^1$ have nonnegative square.
:::

::: {.front card-id="theorem-indeterminacy-codimension" tags="theorem"}
For a rational map $f:X\dashrightarrow Y$ with $X$ a normal integral variety and $Y$ proper over the base field, bound the codimension of its indeterminacy locus. What follows for a surface?
:::

::: {.back card-id="theorem-indeterminacy-codimension"}
The map is defined at every codimension-one point, so its indeterminacy locus has codimension at least two. On a surface it is a finite set of closed points. At a codimension-one point, normality gives a discrete valuation ring, and properness extends the map by the valuative criterion.
:::

::: {.front card-id="application-rational-map-curve-extension" tags="application"}
Compare rational maps from a smooth projective curve to a proper variety with the rational function $1/t:\mathbb P^1\dashrightarrow\mathbb A^1$. Which maps extend everywhere, and which hypothesis decides?
:::

::: {.back card-id="application-rational-map-curve-extension"}
Every rational map from a smooth projective curve to a proper variety extends uniquely: a curve has no nonempty closed subset of codimension at least two. The function $1/t$ does not extend as a morphism to $\mathbb A^1$ at $t=0$. Its target is not proper; regarded as a map to $\mathbb P^1$, it extends by taking the value infinity there.
:::

::: {.front card-id="theorem-miyaoka-mori-bend-break" tags="theorem"}
Let $X$ be a smooth projective $n$-fold over an algebraically closed field, $C\subset X$ an integral curve with $K_X\cdot C<0$, and $H$ a nef Cartier divisor. State the classical Miyaoka–Mori bend-and-break conclusion through a closed point $x\in C$, with its $H$-degree bound.
:::

::: {.back card-id="theorem-miyaoka-mori-bend-break"}
There is an integral rational curve $R\subset X$ through $x$ with
$$H\cdot R\le 2n\,\frac{H\cdot C}{-K_X\cdot C}.$$
See Miyaoka–Mori, Theorem 5, as recalled in the [introduction to Optimal bounds in Bend-and-Break](https://doi.org/10.1017/fmp.2026.10033).
:::

::: {.front card-id="theorem-deformations-maps-curves" tags="theorem"}
Let $C$ be a smooth projective curve over an algebraically closed field, $X$ a smooth quasi-projective variety, and $f:C\to X$. Identify the tangent and obstruction spaces for deforming $f$ with $C$ fixed. Give a sufficient condition for smoothness of $\operatorname{Hom}(C,X)$ at $[f]$.
:::

::: {.back card-id="theorem-deformations-maps-curves"}
The tangent space is $H^0(C,f^*T_X)$, and obstructions lie in $H^1(C,f^*T_X)$. If the latter vanishes, $\operatorname{Hom}(C,X)$ is smooth at $[f]$, of dimension $h^0(C,f^*T_X)$.
:::

::: {.front card-id="theorem-free-rational-curve-evaluation" tags="theorem"}
For a nonconstant map $f:\mathbb P^1\to X$ to a smooth quasi-projective variety over an algebraically closed field, write $f^*T_X=\bigoplus_i\mathcal O(a_i)$. What condition makes $f$ free, and what does it imply for deformations and evaluation?
:::

::: {.back card-id="theorem-free-rational-curve-evaluation"}
The map is free if every $a_i\ge0$. Then $H^1(f^*T_X)=0$ and $H^1(f^*T_X(-p))=0$ for each $p\in\mathbb P^1$. The Hom scheme is smooth at $[f]$, and evaluation $\operatorname{ev}_p:\operatorname{Hom}(\mathbb P^1,X)\to X$ is smooth there. The universal evaluation $\mathbb P^1\times\operatorname{Hom}(\mathbb P^1,X)\to X$ is smooth at $(p,[f])$ as well.
:::

::: {.front card-id="application-unobstructed-not-free-map" tags="application"}
Suppose $f:\mathbb P^1\to X$ has $f^*T_X\simeq\mathcal O(2)\oplus\mathcal O(-1)$. Is the Hom scheme smooth at $[f]$? Is $f$ free? Is evaluation at a fixed point smooth there?
:::

::: {.back card-id="application-unobstructed-not-free-map"}
$H^1(f^*T_X)=0$, so the Hom scheme is smooth at $[f]$. The negative summand makes $f$ nonfree. Evaluation is not smooth: its tangent map $H^0(f^*T_X)\to(f^*T_X)_p$ misses the $\mathcal O(-1)$ direction, since that summand has no sections.
:::
