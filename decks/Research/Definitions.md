---
title: "Research::Definitions"
---

::: {.front card-id="card-9d8b2fab7bf814ba"}
What is a rational map?
:::

::: {.back card-id="card-9d8b2fab7bf814ba"}
A rational map $ f: V \rightarrow W $ between two varieties with $ V $ irreducible is an equivalence class of pairs $ \left(f_U, U\right) $ in which $ f_U $ is a morphism of varieties from a non-empty open set $ U \subset V $ to $ W $, and two such pairs $ \left(f_U, U\right) $ and $ \left(f_{U^{\prime}}^{\prime}, U^{\prime}\right) $ are considered equivalent if $ f_U $ and $ f_{U^{\prime}}^{\prime} $ coincide on the intersection $ U \cap U^{\prime} $.
:::

::: {.front card-id="card-21139fdf3f221644"}
What is **Kodaira dimension**?
:::

::: {.back card-id="card-21139fdf3f221644"}
For$ X $ normal projective and $ D\in {\mathbf{Q}}{\hbox{-}}\operatorname{Div}(X) $,

$$\kappa(X, D)\coloneqq\limsup _{m \in {\mathbf{Z}}_{\geq 0}} \frac{\log \left(h^0\left(\mathcal{O}_X(m D)\right)\right)}{\log m}$$

Equivalently, the Iitaka dimension of the canonical

$$\kappa(X) \coloneqq\kappa(X; \omega_X)$$

Interpret as $ P_m(X) \sim m^{\kappa(x)} $ (bounded above and below by constant multiples).
:::

::: {.front card-id="card-0996fd4a0ee4d958"}
What is a general type variety?
:::

::: {.back card-id="card-0996fd4a0ee4d958"}
$ \kappa(X) = \dim(X) $ is maximal, i.e. $ \omega_X $ is big.
:::

::: {.front card-id="card-67f625f64dc3c847"}
What is a big line bundle?
:::

::: {.back card-id="card-67f625f64dc3c847"}
$ {\mathcal{L}}\in \operatorname{Pic}(X) $ is big iff $ \kappa(X; {\mathcal{L}}) = \dim(X) $ is maximal, i.e. $ \dim \operatorname{im}\phi_{{\left\lvert {m} \right\rvert} {\mathcal{L}}} = \dim(X) $ for $ n\gg 1 $.
:::

::: {.front card-id="card-a54e2a90c7831a3d"}
What is Iitaka dimension?
:::

::: {.back card-id="card-a54e2a90c7831a3d"}
For $ {\mathcal{L}}\in \operatorname{Pic}(X) $, define the *Iitaka dimension* of $ {\mathcal{L}}\in \operatorname{Pic}(X) $ as the maximal embedding dimension:

$$\kappa(X; {\mathcal{L}}) \coloneqq\sup_{m\in {\mathbf{Z}}_{\geq 0}} \left\{{\dim \phi_{{\left\lvert {m{\mathcal{L}}} \right\rvert}}(X)}\right\},\qquad \phi_{{\left\lvert {m{\mathcal{L}}} \right\rvert}}:X\to {\mathbf{P}}^n$$

Always have $ \kappa(X; {\mathcal{L}}) \in \left\{{-\infty, 0, 1,\cdots, \dim(X)}\right\} $.

If $ {\mathcal{L}} $ is not effective, define $ \kappa(X; {\mathcal{L}})= -\infty $.

Fact:

$$\kappa(X; {\mathcal{L}}) + 1 = {\mathrm{trdeg}}_k \operatorname{ff}(R(X; L))$$

where $ R(X; L) $ is the section ring.
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
$ \kappa(X) = -\infty \iff g=0 $, positive curvature.

$ \implies X\cong {\mathbf{P}}^1 \implies P_{\gt 0}(X) = 0 $.

$ \kappa(X) = 0 \iff g=1 $, flat.

$ \implies X\cong E $ an elliptic curve

$ \implies K_X $ trivial.

$ \kappa(X) = 1 \iff g\geq 2 $, negative curvature.

$ \implies $ general type.

$ \implies K_X $ ample.
:::

::: {.front card-id="card-b361751d37669bf3"}
Classify surfaces by Kodaira dimension.
:::

::: {.back card-id="card-b361751d37669bf3"}
For a minimal smooth projective surface $ X $,

$ \kappa(X) = -\infty \iff $Ruled, rational.

$ \implies X\cong {\mathbf{P}}^{2} $ or a minimal ruled surface.

$ \implies \left|12 K_{X}\right|=\emptyset $.

$ \kappa(X) = 0\iff $ abelian, hyperelliptic, K3s, Enriques.

$ \implies \left|12 K_{X}\right|=\{0\} $.

$ \kappa(X) = 1\iff $ elliptic

$ \kappa(X) = 2 \iff $ general type.
:::

::: {.front card-id="card-edd9ac6f0fa2d3e8"}
What is **plurigenera**?
:::

::: {.back card-id="card-edd9ac6f0fa2d3e8"}
$$P_m(X)= h^0(\omega_X^m) = h^0(\mathcal{O}_X(m K_X))$$

Measures the size of a canonical model of $ X $, $ \mathop{\mathrm{Proj}}(\bigoplus_{m\geq 0} H^0(K_X^m)) $.

Can prove a variety is not rational by showing $ P_m(X) > 0 $ for some $ m>0 $.
:::

::: {.front card-id="card-241e5ed95b035be5"}
What is a variety of general type?
:::

::: {.back card-id="card-241e5ed95b035be5"}
Maximal possible Kodaira dimension: $ \kappa(X) = \dim(X) $, e.g. any variety with ample canonical.
:::

::: {.front card-id="card-cd129aadf37058b3"}
What is **irregularity**?
:::

::: {.back card-id="card-cd129aadf37058b3"}
$$q(X) \coloneqq h^{0, 1} = h^1({\mathcal{O}}_X)$$

For a smooth complex projective surface, $ q(X)=h^0(\Omega_X^1) $.

Measures the difference $ p_g(X) - p_a(X) $ between geometric and arithmetic genus.
:::

::: {.front card-id="card-66ce9a474b7f4659"}
What is a **rational** variety?
:::

::: {.back card-id="card-66ce9a474b7f4659"}
Normal and birational $ X\overset{\sim}{\dashrightarrow}{\mathbf{P}}^N $ for some $ N $.
:::

::: {.front card-id="card-887ac50e6202d5f9"}
What is a **unirational** variety?
:::

::: {.back card-id="card-887ac50e6202d5f9"}
Idea: Luroth shows that if $ k \subsetneq L \subseteq k(x) $ then $ L = k(x) $ and asks the same for subfields $ L \subseteq k(x_1,\cdots, x_n) $. If $ L = k(X) $ for a variety, this induces $ {\mathbf{P}}^n \dashrightarrow X $ with dense image; call such $ X $ unirational.

Normal and admits a dominant rational map $ {\mathbf{P}}^N\dashrightarrow X $ for some $ N $, or dominated by a rational variety so that $ k({\mathbf{P}}^n)/k(X) $ is a purely transcendental (separable) extension of finite type.

Idea: similar to rational, e.g. $ h^0(\Omega^{\geq 1}_X) = 0 $, Luroth asks if unirational implies rational. True for curves, false for 3-folds and higher.
:::

::: {.front card-id="card-c99c177d102ccfce"}
What is a **uniruled** variety?
:::

::: {.back card-id="card-c99c177d102ccfce"}
Idea: covered by rational curves, for every $ x\in X $ there is a nonconstant morphism $ {\mathbf{P}}^1\to X $ with $ f(0) =x $, i.e. for every point one can find a rational curve containing it.

More precisely, $ \exists Y $ and a dominant rational morphism $ Y\times {\mathbf{P}}^1\dashrightarrow X $ which does not factor through the projection to $ Y $, i.e. dominated by a ruled variety.
:::

::: {.front card-id="card-749c097614ea7db3"}
What is a **ruled** variety?
:::

::: {.back card-id="card-749c097614ea7db3"}
Birational to $ Y\times {\mathbf{P}}^1 $ for some $ Y $.
:::

::: {.front card-id="card-15b64175339c625d"}
What is a minimal model?
:::

::: {.back card-id="card-15b64175339c625d"}
For $ \kappa(X) \geq 0 $, a birational $ \tilde X\to X $ with $ K_{\tilde X} $ nef and $ \tilde X $ terminal.
:::

::: {.front card-id="card-704cc7c711f84485"}
What is a terminal singularity? Canonical singularity? Log-terminal singularity?
:::

::: {.back card-id="card-704cc7c711f84485"}
For a resolution $ \pi: \tilde X\to X $, write $ K_{\tilde X} \equiv_{\mathbf{Q}}\pi^* K_{X} + \sum a_i E_i $ with $ a_i\in {\mathbf{Q}} $, then

Terminal: $ a_i > 0 $.

Canonical: $ a_i \geq 0 $

Log-terminal: $ a_i > -1 $.
:::

::: {.front card-id="card-3c64e95c0377e039"}
What is Luroth's problem?
:::

::: {.back card-id="card-3c64e95c0377e039"}
Rational $ \implies $ unirational, is the converse true? Equivalently, is every subfield of a purely transcendental field extension again purely transcendental? True in dimension 1 by Galois theory.
:::

::: {.front card-id="card-41bf32b10f9d0aae"}
What is Castelnuovo's theorem on complex surfaces?
:::

::: {.back card-id="card-41bf32b10f9d0aae"}
If $ q(X), P_2(X) $ vanish then $ X $ is rational. This implies that unirational surfaces are rational. Note that $ P_1(X) $ vanishing is not enough, viz. the Enriques surfaces.
:::

::: {.front card-id="card-a52d9643c2df5f41"}
What is a **rationally connected** variety?
:::

::: {.back card-id="card-a52d9643c2df5f41"}
Any pair $ p,q\in X $ can be connected by a chain of rational curves, or equivalently there is a morphism $ f: {\mathbf{P}}^1\to X $ with $ f({\left[ {0: 1} \right]}) = p $ and $ f({\left[ {1: 0} \right]}) = q $.
:::

::: {.front card-id="card-70053316f342a559"}
What is a $ {\mathbf{Q}}{\hbox{-}} $Gorenstein variety?
:::

::: {.back card-id="card-70053316f342a559"}
$ K_X \in {\mathbf{Q}}{\hbox{-}}\operatorname{CDiv}(X) $.
:::

::: {.front card-id="card-2a84e95c52e5f1c9"}
Define the order of a nonzero meromorphic differential $ \omega $ at a point $ p\in C $ a curve.
:::

::: {.back card-id="card-2a84e95c52e5f1c9"}
Let $ X $ be a smooth integral curve over $ k $, let $ \omega $ be a non-zero meromorphic differential on $ X $, and let $ x $ be a closed point of $ X $. The order or valuation of $ \omega $ at $ x $, denoted by $ \operatorname{ord}_x \omega $, is the unique $ n \in \mathbf{Z} $ such that

$$\mathcal{O}_{X, x} \omega=\mathfrak{m}_{X, x}^n \Omega_{X / k, x}$$

as $ \mathcal{O}_{X, x} $-submodules of $ \Omega_{K(X) / k} $.
:::

::: {.front card-id="card-cca847cafa46591c"}
What is $ \operatorname{Div}(\omega) $ for $ \omega $ a meromorphic differential on a curve?
:::

::: {.back card-id="card-cca847cafa46591c"}
$$\operatorname{div} \omega=\sum_{x \in X} \operatorname{ord}_x(\omega) x$$
:::

::: {.front card-id="card-f14aa846a595fa7d"}
What is $ \operatorname{div}(\,dt) $ for $ t $ a coordinate on $ {\mathbf{P}}^1 $?
:::

::: {.back card-id="card-f14aa846a595fa7d"}
$ \operatorname{div}(\,dt) = -2[\infty] $.
:::

::: {.front card-id="card-96f73b263cc4891c"}
Describe the canonical sheaf of a curve explicitly.
:::

::: {.back card-id="card-96f73b263cc4891c"}
$$\Omega_{X / k}(U)= \begin{cases}\left\{\omega \in \Omega_{K(X) / k} \mathrel{\Big|}\operatorname{ord}_x(\omega) \geq 0 \text { for all closed points } x \in U\right\} & \text { if } U \neq \emptyset, \\ 0 & \text { if } U=\emptyset\end{cases}$$
:::

::: {.front card-id="card-5dfcf94c23a1dd43"}
What is RR for a curve?
:::

::: {.back card-id="card-5dfcf94c23a1dd43"}
Theorem $ 2.3 $ (Riemann-Roch). Let $ X $ be a smooth, projective, geometrically integral curve of genus $ g $ over $ k $, and let $ \mathcal{K} $ be a canonical divisor on $ X $. For every divisor $ D $ on $ X $, we have

$$\operatorname{dim}_k L(X, D)-\operatorname{dim}_k L(X, \mathcal{K}-D)=1-g+\operatorname{deg} D$$
:::

::: {.front card-id="card-0f10ef5a77d3c549"}
What is the Mori cone?
:::

::: {.back card-id="card-0f10ef5a77d3c549"}
The Mori cone $\overline{\operatorname{NE}}(X)\subset N_1(X)_{\mathbb R}$ is the closure of the convex cone generated by numerical classes of effective curves on a projective variety $X$. Its dual cone in $N^1(X)_{\mathbb R}$ is the nef cone.
:::

::: {.front card-id="card-9f872aa511b4cde9"}
What is a rational polyhedral cone?
:::

::: {.back card-id="card-9f872aa511b4cde9"}
Generated by a finite subset of $ \Lambda_{\mathbf{Q}} $.
:::

::: {.front card-id="card-ee210ddebc16c66b"}
What is K-stability?
:::

::: {.back card-id="card-ee210ddebc16c66b"}
Modern version of GIT, since GIT doesn't work well for varieties of $ \dim \geq 2 $.

For Fanos, equivalent to admitting a constant scalar curvature metric.
:::

::: {.front card-id="card-ee3d073c81750457"}
When is $ M\in { {}_{k} \mathsf{Alg}} $?
:::

::: {.back card-id="card-ee3d073c81750457"}
Algebras are like "covers" of schemes:

Noncommutative case: $ M\in { {}_{k}  \mathsf{Alg}} $ when $ \exists f\in \mathsf{CRing}(k \to Z(M)) $, so $ f^*: \operatorname{Spec}Z(M) \to \operatorname{Spec}k $ where $ Z(M) $ is the ring-theoretic center of $ M $. This induces an action $ \lambda . m \coloneqq f(\lambda)m $ using the ring multiplication in $ M $.

Commutative case: $ \exists f\in \mathsf{CRing}(k\to M) $ so $ \operatorname{Spec}M\to \operatorname{Spec}k $.

In particular, $ M\in   {}_{k}{\mathsf{Mod}} $ so there should be an action by "scalars" $ k\curvearrowright M $.
:::

::: {.front card-id="card-c5cef00e4330d7da"}
What is a geometric vector bundle over a scheme?
:::

::: {.back card-id="card-c5cef00e4330d7da"}
A geometric vector bundle of rank $ n $ over $ X $ is a scheme $ f: Z \rightarrow X $ together with an open cover $ \left\{U_i\right\} $ of $ X $ and isomorphisms $ \psi_i: f^{-1}\left(U_i\right) \rightarrow \mathbf{A}_{U_i}^n \coloneqq U\times {\mathbf{A}}^n_L $ such that, for any $ i, j $ and any open affine $ V=\operatorname{Spec}(R) \subseteq U_i \cap U_j $, the automorphism $ \psi=\psi_j \circ \psi_i^{-1} $ of $ \mathbf{A}_V^n $ is in $ \operatorname{GL}_n(R) $.
:::

::: {.front card-id="card-6c2dffdf1565979a"}
What is a locally free sheaf $ {\mathcal{E}} $?
:::

::: {.back card-id="card-6c2dffdf1565979a"}
A locally free sheaf $ \mathcal{E} $ of rank $ n $ is an $ \mathcal{O}_X $-module $ \mathcal{E} $ together with a covering $ \left\{U_i\right\} $ of $ X $ such that there exist $ \mathcal{O}_{U_i} $-module isomorphisms

$$\rho_i:\left.\mathcal{E}\right|_{U_i} \simeq \mathcal{O}_{U_i}^n .$$
:::

::: {.front card-id="card-013129f0821e1e9e"}
What is the geometric vector bundle associated to a locally free sheaf?
:::

::: {.back card-id="card-013129f0821e1e9e"}
$ V({\mathcal{E}}) \coloneqq\operatorname{Spec}\operatorname{Sym}{\mathcal{E}} $, where $ \operatorname{Sym}{\mathcal{E}} $ is the sheafy symmetric algebra so $ { \left.{{\qty{\operatorname{Sym}{\mathcal{E}}}}} \right|_{{U_i}} } \cong \operatorname{Sym}\qty{{ \left.{{{\mathcal{E}}}} \right|_{{U_i}} }} $ over $ {\mathcal{O}}_{U_i} $, and where one takes the sheaf-theoretic spectrum.
:::

::: {.front card-id="card-0fdea74c19b58248"}
What is $ \mathop{\mathrm{Proj}}(R) $?
:::

::: {.back card-id="card-0fdea74c19b58248"}
Homogeneous prime ideals of $ R $ **not** completely containing $ R_+ \coloneqq\bigoplus_{d\geq 1} R_d $.
:::

::: {.front card-id="card-62fefa7cee201023"}
Show $ \dim {\mathcal{M}}_g = 3g-3 $.
:::

::: {.back card-id="card-62fefa7cee201023"}
$ \dim {\mathcal{M}}_g = \dim {\mathbf{T}}_{{\mathcal{M}}_g} = h^1({\mathbf{T}}_C) $ where $ C $ is any smooth complete curve of genus $ g $.

Serre duality: $ H^1({\mathbf{T}}_C) = H^0({\mathbf{T}}_C {}^{ \vee }\otimes\omega_C) {}^{ \vee }= H^0(\omega_C{ {}^{ \scriptstyle\otimes_{}^{2} }  }) $.

RR: $ \chi(\omega_C{ {}^{ \scriptstyle\otimes_{}^{2} }  }) = 2(g-2) + (1-g) = 3g-3 $.

For $ g\geq 2 $, $ H^1(\omega_C{ {}^{ \scriptstyle\otimes_{}^{2} }  }) = H^0( (\omega_C{ {}^{ \scriptstyle\otimes_{}^{2} }  }) {}^{ \vee }\otimes\omega_C)=0 $ since this is a line bundle of degree $ 4-4g + 2g-2 = 2-2g < 0 $.
:::

::: {.front card-id="card-fb89ad30738ffe16"}
How are plurigenera related to the arithmetic or geometric genus?
:::

::: {.back card-id="card-fb89ad30738ffe16"}
$ P_1(X) = g(X) $ for smooth projective curves.
:::

::: {.front card-id="card-97356860c51b279d"}
What is $ P_m(X) $ for $ X $ a smooth complete curve, in terms of $ g(X) $?
:::

::: {.back card-id="card-97356860c51b279d"}
$ g=0 \implies X \cong {\mathbf{P}}^1 \implies \omega_X \cong {\mathcal{O}}_{{\mathbf{P}}^1}(-2) \implies P_{\geq 0}(X) = 0 $.

$ g=1 \implies \omega_X\cong {\mathcal{O}}_X \implies P_{\geq 0}(X) = 1 $.

$ g\geq 2 \implies \deg \omega_X^m = m(2g-2)\implies P_{\geq 2}(X) = m(2g-2) - (g-1) $
:::

::: {.front card-id="card-fa113b1d45d9bca3"}
What is $ P_m(X) $ for $ X \subseteq {\mathbf{P}}^n $ a smooth hypersurface of degree $ d $?
:::

::: {.back card-id="card-fa113b1d45d9bca3"}
Write $ {\mathcal{O}}_X(1) = { \left.{{{\mathcal{O}}_{{\mathbf{P}}^n}(1)}} \right|_{{X}} } $, then $ \omega_X \cong {\mathcal{O}}_X(d - (n+1) ) $.

$ d < n + 1 \implies P_{\geq 0}(X) = 0 $

$ d = n +1 \implies \omega_X \cong {\mathcal{O}}_X \implies P_{\geq 1}(X) = 1 $

$ d > n+1 \implies \omega_X \in \operatorname{Pic}(X)^{{\mathrm{v.amp}}} \implies \cdots $

$$P_{m \gg 0}(X) = {d(d-n-1) \over(n-1)! }\cdot m^{n-1} + { \mathsf{O}}(m^{n-2})$$
:::

::: {.front card-id="card-bff7d57e6cbbd0e0"}
What is $ \omega_X $ for $ X \subseteq {\mathbf{P}}^{n+1} $ a smooth complete intersection of hypersurfaces of degrees $ d_1,\cdots, d_k $?
:::

::: {.back card-id="card-bff7d57e6cbbd0e0"}
$ \omega_X \cong {\mathcal{O}}_X(\sum d_i - (n+1)) $.
:::

::: {.front card-id="card-da0dd170d4c7b84f"}
What is a weak CY?
:::

::: {.back card-id="card-da0dd170d4c7b84f"}
$ X $ smooth projective with $ \omega_X \cong {\mathcal{O}}_X $.
:::

::: {.front card-id="card-a75e698385fb2a5e"}
What is a (strong) CY?
:::

::: {.back card-id="card-a75e698385fb2a5e"}
A weak CY with $ H^i({\mathcal{O}}_X) = 0 $ for $ 0 \lt i \lt \dim(X) $ and $ \pi_1(X({\mathbf{C}})) = 1 $.
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
K3s, since $ \omega_X\cong {\mathcal{O}}_X $ and $ H^1({\mathcal{O}}_X) = 0 $, e.g.

A quartic in $ {\mathbf{P}}^3 $ (hypersurface of degree 4)

A complete intersection of type $ (2, 3) $ in $ {\mathbf{P}}^4 $.

A complete intersection of type $ (2,2,2 $) in $ {\mathbf{P}}^5 $.

Hypersurfaces of degree $ n+1 $ in $ {\mathbf{P}}^n $.
:::

::: {.front card-id="card-72941d8b176edf02"}
Classify hypersurfaces $ X\subseteq {\mathbf{P}}^n $ by Kodaira dimension.
:::

::: {.back card-id="card-72941d8b176edf02"}
$ \kappa(X) = -\infty \iff d\leq n $.

$ \kappa(X) = 0 \iff d= n $.

$ \kappa(X) = \dim(X) \iff d\geq n+2 $.
:::

::: {.front card-id="card-a04854f8fc86df07"}
What is the fundamental SES for a divisor $ D $ on a surface $ X $?
:::

::: {.back card-id="card-a04854f8fc86df07"}
$ {\mathcal{O}}_X(-D) \hookrightarrow{\mathcal{O}}_X \twoheadrightarrow{\mathcal{O}}_D $.
:::

::: {.front card-id="card-4dcbe0afdb38b38d"}
How is $ C.D $ defined for curves on a surface?
:::

::: {.back card-id="card-4dcbe0afdb38b38d"}
$$C.D = \sum_{p\in C\cap D}(C.D)_p, \quad (C.D)_p \coloneqq\dim_k {\mathcal{O}}_{X, p}/\left\langle{f, g}\right\rangle$$

where $ C \pitchfork D \iff {\mathfrak{m}}_x = \left\langle{f, g}\right\rangle $ for $ f,g $ their local equations.
:::

::: {.front card-id="card-092509a94bf42014"}
How is $ D\in \operatorname{Div}(X) $ related to normal bundles?
:::

::: {.back card-id="card-092509a94bf42014"}
$ D^2 = \deg {\mathcal{N}}_{D/X} $.
:::

::: {.front card-id="card-7486d6a8dece697a"}
What is $ C.D $ for $ C, D \subseteq {\mathbf{P}}^2 $?
:::

::: {.back card-id="card-7486d6a8dece697a"}
$ C\sim m H $ and $ D\sim n H $ for $ H $ a hyperplane (here a line), so

$$C.D = (mH).(nH) = mnH^2 = mn$$

where $ H^2 = (H.H') = {\sharp}(H\cap H') =1 $ by moving $ H $ to $ H' $.
:::

::: {.front card-id="card-5b487b04292875b0"}
What is the intersection matrix for $ {\mathbf{P}}^1\times {\mathbf{P}}^1 $?
:::

::: {.back card-id="card-5b487b04292875b0"}
Write $ \operatorname{Pic}({\mathbf{P}}^1\times {\mathbf{P}}^1) = \left\langle{f_1, f_2}\right\rangle_{\mathbf{Z}} $ for $ f_i $ the class of a fiber to get

$${

\begin{bmatrix}

{0} & {1}

\

{1} & {0}

\end{bmatrix}

},\qquad \text{i.e. }f*1 .f*2 = 1,\quad f*1^2 = f*2^2 = 0$$
:::

::: {.front card-id="card-c1f058f6cd2095c9"}
What is the genus formula for a curve on a smooth surface?
:::

::: {.back card-id="card-c1f058f6cd2095c9"}
$$\omega_C \simeq { \left.{{\qty{\omega_X \otimes \mathcal{O}_X(C)}}} \right|_{{ C}} } \underset{\deg}\implies 2g-2=\left(C+K_X\right) \cdot C$$
:::

::: {.front card-id="card-58f42a16f8d57796"}
What is RR for surfaces?
:::

::: {.back card-id="card-58f42a16f8d57796"}
For $ D\in \operatorname{Div}(X) $,

$$\chi({\mathcal{O}}_X(D)) - \chi({\mathcal{O}}_X) = {D\cdot (D-K_X) \over 2}$$
:::
