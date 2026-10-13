---
title: "Orals::Misc Schemes"
---

::: {.front card-id="card-134f85a8c9a41dbd"}
What is the **fiber product** of schemes?
:::

::: {.back card-id="card-134f85a8c9a41dbd"}
*(Answer was a figure; image not recovered.)*
:::

::: {.front card-id="card-a82b6f5d3938ff3c"}
What is the **residue field** of a point?
:::

::: {.back card-id="card-a82b6f5d3938ff3c"}
$ \kappa(x) \coloneqq{\mathcal{O}}_{X, x}/{\mathfrak{m}}_x $.
:::

::: {.front card-id="card-8291e7f9a2f63d07"}
What does it mean to *evaluate* a prime ideal $ {\mathfrak{p}}{~\trianglelefteq~}R $ at an element $ f\in R $?
:::

::: {.back card-id="card-8291e7f9a2f63d07"}
Take the image of $ f $ under the natural map $ R \to R/p \to \kappa(p) $ where $ \kappa(p) $ is the residue field of the local ring $ R/p $.
:::

::: {.front card-id="card-caff831dd2a6d615"}
What is a dominant morphism of schemes?
:::

::: {.back card-id="card-caff831dd2a6d615"}
$ f:X\to S $ where $ f(X) \subseteq S $ is dense. For integral schemes: maps generic points to generic points, or the ring maps on sections are injective, or the local ring morphisms at all local rings is injective.
:::

::: {.front card-id="card-0f8f55d06116c7b8"}
Characterize maps $ \operatorname{Spec}L \to X $ for $ L $ a field.
:::

::: {.back card-id="card-0f8f55d06116c7b8"}
Equivalent to giving a point $ x\in X $ and an inclusion $ \kappa(x) \hookrightarrow L $ of the residue field into $ L $.
:::

::: {.front card-id="card-eb9cd3c92698f1bf"}
Characterize maps $ \operatorname{Spec}k[{\varepsilon}]/{\varepsilon}^2\to X $.
:::

::: {.back card-id="card-eb9cd3c92698f1bf"}
Giving a rational point $ x\in X $, so $ \kappa(x) = k $, and an element of $ {\mathbf{T}}_x \coloneqq({\mathfrak{m}}_x/{\mathfrak{m}}_x)^2 $.
:::

::: {.front card-id="card-49d5cc8e3c490ffa"}
What is a **morphism of locally ringed spaces**?
:::

::: {.back card-id="card-49d5cc8e3c490ffa"}
A morphism $ X\to Y $ in $ \mathsf{Loc}\mathsf{Ring} $ is a morphism $ \phi $ in $ \mathsf{CRing} $ where $ \phi({\mathfrak{m}}_X) \subseteq {\mathfrak{m}}_Y $. A morphism of ringed spaces is a pair $ (f, f^\sharp): (X, {\mathcal{O}}_X) \to (Y, {\mathcal{O}}_Y) $ where $ f: {\left\lvert {X} \right\rvert}\to {\left\lvert {Y} \right\rvert}\in {\mathsf{Top}} $ and $ f^\sharp: {\mathcal{O}}_Y\to f_* {\mathcal{O}}_X $. A morphism of *locally* ringed spaces is a morphism as above where $ f_x: {\mathcal{O}}_{X, x}\to {\mathcal{O}}_{y, f(x)} $ is a morphism of local rings for each $ x\in X $.
:::

::: {.front card-id="card-618a12ae0264b25f"}
For $ X\to S $ a scheme, what is a $ T{\hbox{-}} $valued point of $ X $ for $ T $ a scheme?
:::

::: {.back card-id="card-618a12ae0264b25f"}
A scheme morphism $ T\to X $.
:::

::: {.front card-id="card-fdb0e1a6a993fc2f"}
What is a **generic point**?
:::

::: {.back card-id="card-fdb0e1a6a993fc2f"}
A point $ \eta \in X $ such that $ { \operatorname{cl}}_X \eta = X $.
:::

::: {.front card-id="card-ee5d9c2421aa732c"}
What is specialization/generization?
:::

::: {.back card-id="card-ee5d9c2421aa732c"}
For $ x, \tilde x\in X $, say $ x $ is a **specialization** of $ \tilde x $ if $ x\in { \operatorname{cl}}_X(\tilde x) $; write $ \tilde x \leadsto x $ and say $ \tilde x $ specializes to $ x $ or $ x $ generizes to $ \tilde x $.
:::

::: {.front card-id="card-1e31ab8314d3ee54"}
What is a **special point**?
:::

::: {.back card-id="card-1e31ab8314d3ee54"}
For a DVR, the unique closed point.
:::

::: {.front card-id="card-1600fe622733e541"}
What is a **closed point**?
:::

::: {.back card-id="card-1600fe622733e541"}
For an affine scheme $ \operatorname{Spec}A $, a point corresponding to a maximal ideal $ m\in \operatorname{mSpec}A $.
:::

::: {.front card-id="card-1b1f50cd7d0bfd9e"}
What is a **rational point**?
:::

::: {.back card-id="card-1b1f50cd7d0bfd9e"}
For a scheme defined over $ k $, any point $ x\in X $ with $ \kappa(x) { \, \xrightarrow{\sim}\, }k $.
:::

::: {.front card-id="card-dd6a17b3b5ccabe1"}
What are the **singular points** of the scheme?
:::

::: {.back card-id="card-dd6a17b3b5ccabe1"}
Points $ x $ at which $ {\mathcal{O}}_{X, x} $ is not a regular local ring, where $ (A, {\mathfrak{m}}_A) $ is regular iff $ \dim_{\kappa(A)} {\mathfrak{m}}_A/{\mathfrak{m}}_A^2 = \dim A $ where $ \kappa(A) $ is the residue field of $ A $.
:::

::: {.front card-id="card-dc477b6237cb1cc7"}
What is **base change**?
:::

::: {.back card-id="card-dc477b6237cb1cc7"}
For $ X\in{\mathsf{Sch}}_{/ {S}} $ and $ T\to S $ a morphism of schemes, the pullback $ X  \underset{\scriptscriptstyle {S} }{\times} T $.
:::

::: {.front card-id="card-fa0b786697fe09b6"}
What does it mean to be **stable under base change**?
:::

::: {.back card-id="card-fa0b786697fe09b6"}
If $ f:X\to S $ has property $ P $ and $ \phi: T\to S $ then $ \tilde f: X \underset{\scriptscriptstyle {S} }{\times}T\to T $ again has property $ P $.
:::

::: {.front card-id="card-d190eb30a79c7d19"}
What does it mean to be **local on the base**?
:::

::: {.back card-id="card-d190eb30a79c7d19"}
For $ f:X\to Y $, property $ P $ is local on the base iff $ \exists V_i\rightrightarrows Y $ with $ f^{-1}(V_i)\to V_i $ having property $ P $.
:::

::: {.front card-id="card-39d50a1666910f3f"}
What is **smooth base change**?
:::

::: {.back card-id="card-39d50a1666910f3f"}
For $ f: X\to S $ smooth and $ g: T\to S $ qc and $ {\mathcal{F}}\in {\mathsf{Sh}}(T) $ of $ C_n{\hbox{-}} $modules (torsion), there is an isomorphism $ f^* {\mathbf{R}}^q g_* {\mathcal{F}} { \, \xrightarrow{\sim}\, }{\mathbf{R}}^q \tilde g_* (f')^*{\mathcal{F}} $ where $ \tilde g: X \underset{\scriptscriptstyle {S} }{\times} T \to X $ and $ \tilde f: X \underset{\scriptscriptstyle {S} }{\times} T\to T $.
:::

::: {.front card-id="card-5e0bccfad0df15c7"}
What is **proper base change**?
:::

::: {.back card-id="card-5e0bccfad0df15c7"}
If $ \pi: X\to S $ is proper and $ {\mathcal{F}} $ is a torsion sheaf on $ X $ with $ f: T\to S $, the base change morphism $ f^{-1}{\mathbf{R}}^i \pi_* {\mathcal{F}} { \, \xrightarrow{\sim}\, }{\mathbf{R}}^i \tilde\pi_* \tilde f^{-1}{\mathcal{F}} $.
:::

::: {.front card-id="card-2621a7b4726467d5"}
What does it mean to be **regular in codimension one**?
:::

::: {.back card-id="card-2621a7b4726467d5"}
Every local ring $ {\mathcal{O}}_{X, x} $ of dimension 1 is regular. Implies that local rings are DVRs.
:::

::: {.front card-id="card-c568a40234fbb420"}
What is the **codimension** of a subset of a scheme?
:::

::: {.back card-id="card-c568a40234fbb420"}
For an irreducible closed $ Z\subseteq X $, the supremum over lengths of chains $ Z= Z_0 \subseteq Z_1 \subseteq \cdots \subseteq Z_n $ of distinct irreducible closed subsets of $ X $. For an arbitrary closed subset $ Y $, take the infimum over all irreducibles $ Z \subseteq Y $.
:::

::: {.front card-id="card-de688f4ab8bf69dd"}
What are the exact sequences associated with relative differentials?
:::

::: {.back card-id="card-de688f4ab8bf69dd"}
For $ f:X\to Y $ and $ Z \leq X $ closed with ideal sheaf $ {\mathcal{I}}_Z $, the sequence

$${\mathcal{I}}_Z/{\mathcal{I}}_Z^2\to \Omega_{X/Y}\otimes{\mathcal{O}}_Z \twoheadrightarrow\Omega_{Z/Y}$$

If $ Y=k $, this is exact iff $ Z $ is smooth.

For $ X\xrightarrow{f} Y \xrightarrow{g} Z $,

$$f^* \Omega_{Y / Z} \rightarrow \Omega_{X / Z} \twoheadrightarrow\Omega_{X / Y}$$
:::

::: {.front card-id="card-5473776e9b06e148"}
What is the **canonical sheaf** of a scheme?
:::

::: {.back card-id="card-5473776e9b06e148"}
$ \omega_X \coloneqq\operatorname{det}\Omega_{X/k} $.
:::

::: {.front card-id="card-bc6d4901d6074616"}
What is the **geometric genus** of a scheme?
:::

::: {.back card-id="card-bc6d4901d6074616"}
For $ X $ smooth projective, far left side of the Hodge diamond:

$$p_g \coloneqq h^0(X; \Omega_X^n) = h^0(\omega_X) = h^0(K_X) = h^{n, 0}$$
:::

::: {.front card-id="card-a61d8207edb6dea5"}
Discuss the geometric genus.
:::

::: {.back card-id="card-a61d8207edb6dea5"}
For $ X $ smooth projective, $ p_g(X) = h^{n, 0} = h^0(\operatorname{det}\Omega_X) = h^0(K_X) $; it is a birational invariant. For curves, $ p_g(X) = h^{1,0} = h^{0, 1} = h^1({\mathcal{O}}_X) $ and

$$p_a = (-1)^{\dim X}(\chi({\mathcal{O}}_X) - 1) = -1(h^0({\mathcal{O}}_X) - h^1({\mathcal{O}}_X) - 1) = -1(1-p_g(X) - 1) = p_g(X)$$

$ p_a(X) \neq p_g(X) $ in general: take $ Y $ a cubic plane curve and $ X\coloneqq Y\times Y $, then $ p_g(X) = 1 $ but $ p_a(X) = -1 $.

For singular curves, define $ p_g(C) \coloneqq p_g(\tilde C) $ where $ \tilde C $ is the normalization.

For an irreducible plane curve, $ g = {1\over 2}(d-1)(d-2) - s $ where $ s $ is a count of singularities with multiplicity.
:::

::: {.front card-id="card-d5e412cd78235f30"}
What are the **normal** and **conormal sheaves**?
:::

::: {.back card-id="card-d5e412cd78235f30"}
For $ Y\hookrightarrow X $ a smooth subvariety of a smooth variety, $ \mathbf{N}_{Y/X} {}^{ \vee }= {\mathcal{I}}_Y/{\mathcal{I}}_Y^2 $ is the conormal sheaf and $ \mathbf{N}_{Y/X}\coloneqq\mathop{\mathcal{H}\! \mathit{om}}_{{\mathcal{O}}_Y}({\mathcal{I}}_Y/{\mathcal{I}}_Y^2, {\mathcal{O}}_Y) $ is the normal sheaf.
:::

::: {.front card-id="card-48c0d3ff41bea326"}
What is **Bertini's theorem**?
:::

::: {.back card-id="card-48c0d3ff41bea326"}
Idea: a generic hyperplane section of a smooth projective variety is again smooth.

A hyperplane section of a smooth variety in $ {\mathbf{P}}^n $ is again smooth: for $ X \leq {\mathbf{P}}^n_{/ {k}} $ a smooth closed subvariety, there exists a hyperplane $ H $ such that $ H\cap X $ is regular at every point. The set of such hyperplanes forms an open dense subset of the linear system $ {\left\lvert {H} \right\rvert} $.

For $ X\subseteq {\mathbf{P}}^n_{/ {k}} $ a smooth projective variety (closed subvariety of $ {\mathbf{P}}^n $), there is a hyperplane $ H $ not containing $ X $ such that the hyperplane section $ H\cap X $ is everywhere regular.

The set of $ H $ with this property is an open dense subset of the complete linear system $ {\left\lvert {H} \right\rvert} $ (regarded as a projective space). If $ \dim X \geq 2 $ then $ H\cap X $ can be taken to be smooth.
:::

::: {.front card-id="card-f6e2da3ec9f4c267"}
Let $ Y\leq X $ be a smooth codimension $ r $ subvariety, discuss $ \omega_Y $.
:::

::: {.back card-id="card-f6e2da3ec9f4c267"}
$ \omega_Y \cong \omega_X \otimes\bigwedge\nolimits^r \mathbf{N}_{Y/X} $, and if $ r=1 $ this recovers $ \omega_Y\cong \omega_X \otimes{\mathcal{O}}(Y) \otimes{\mathcal{O}}_Y $ where $ Y $ is considered a divisor.
:::

::: {.front card-id="card-00224b008d0de86d"}
Compute $ \omega_X $ and $ p_g $ for $ X = {\mathbf{P}}^n_{/ {k}} $.
:::

::: {.back card-id="card-00224b008d0de86d"}
Start with $ 0\to {\mathcal{O}}_X \to {\mathcal{O}}_X(1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  } \to {\mathbb{T}}_X\to 0 $, dualize to get $ 0 \rightarrow \Omega_{X / Y} \rightarrow \mathcal{O}_X(-1)^{n+1} \rightarrow \mathcal{O}_X \rightarrow 0 $, take determinants to get $ \omega_X \cong {\mathcal{O}}_X(-n-1) $.

This has not sections if $ n\geq 1 $ so $ p_g = 0 $.
:::

::: {.front card-id="card-60a62c47a2cbe0cc"}
What does it mean for $ {\mathcal{L}}\in \operatorname{Pic}(X) $ to be very ample wrt a scheme $ Y $, where $ X\in {\mathsf{Sch}}_{/ {Y}} $?
:::

::: {.back card-id="card-60a62c47a2cbe0cc"}
There is an immersion $ \iota: X\to {\mathbf{P}}^n_{/ {Y}} $ for some $ n $ where $ {\mathcal{L}}\cong \iota^* {\mathcal{O}}_{{\mathbf{P}}^n}(1) $. For $ Y = \operatorname{Spec}A $, this is equivalent to existence of sections $ \left\{{s_1,\cdots, s_n}\right\}\subseteq H^0(X; {\mathcal{L}}) $ such that $ x\mapsto {\left[ {s_1(x): \cdots : s_n(x)} \right]} $ is an immersion.
:::

::: {.front card-id="card-12cc1c6c9aa5697e"}
What does it mean for $ {\mathcal{L}}\in \operatorname{Pic}(X) $ to be **ample**?
:::

::: {.back card-id="card-12cc1c6c9aa5697e"}
For all $ {\mathcal{F}}\in {\mathsf{Coh}}(X) $, the twist $ {\mathcal{F}}\otimes{\mathcal{L}}^n $ is globally generated for $ n\gg 0 $.
:::

::: {.front card-id="card-600a9b022ee0b85d"}
Discuss ampleness of sheaves of affine schemes.
:::

::: {.back card-id="card-600a9b022ee0b85d"}
Every $ X\in {\mathsf{Coh}}(\operatorname{Spec}A) $ is globally generated, so if $ {\mathcal{F}} $ is invertible then it is necessarily ample.
:::

::: {.front card-id="card-482d5dfab0db0fdf"}
What does it mean for $ {\mathcal{F}}\in {\mathsf{QCoh}}(X) $ to be **globally generated**? $ {\mathcal{L}}\in \operatorname{Pic}(X) $?
:::

::: {.back card-id="card-482d5dfab0db0fdf"}
$ \forall x\in X, {\mathcal{F}}_x $ is generated by $ H^0(X; {\mathcal{F}})_x $, or equivalently there exists a free sheaf $ {\mathcal{G}} $ surjecting $ {\mathcal{G}}\twoheadrightarrow{\mathcal{F}} $.

For $ \operatorname{Pic}(X) $, $ \forall x\in X $ there exists a nonvanishing section $ s\in H^0(X; {\mathcal{L}}) $, i.e. bpf.
:::

::: {.front card-id="card-2629a4068afdc432"}
Discuss $ H^0({\mathbf{P}}^m; {\mathcal{O}}(n)) $ for $ n\in {\mathbf{Z}} $.
:::

::: {.back card-id="card-2629a4068afdc432"}
The section ring is given by $ \bigoplus_{n\geq 0} H^0({\mathbf{P}}^m; {\mathcal{O}}(n)) \cong k[x_0,\cdots, x_m] $ as graded rings. Thus $ H^0({\mathcal{O}}) = k $ and $ H^0({\mathcal{O}}(n)) $ are degree $ n $ polynomials, so is generated by the monomials of total degree $ n $ -- this is a stars and bars argument; the number of monomials in $ R[x_1,\cdots, x_N] $ of degree $ D $ is $ {N+D-1\choose D} $. Here $ N = m+1 $ and $ D = n $, so we get $ {m+d\choose d} $.

How this count goes: represent as $ a^3b^2d^2e \leadsto \bullet \bullet \bullet \mathrel{\Big|}\bullet \bullet \mathrel{\Big|}\mathrel{\Big|}\bullet \bullet \mathrel{\Big|}\bullet $. Note that there are no sections for $ n < 0 $. In general, $ {\mathcal{O}}(n) $ corresponds to the $ n{\hbox{-}} $uple/Veronese embedding $ {\mathbf{P}}^n \to {\mathbf{P}}^N $.
:::

::: {.front card-id="card-979041d2022161e4"}
Discuss ampleness of $ {\mathcal{O}}_{{\mathbf{P}}^m}(n) $.
:::

::: {.back card-id="card-979041d2022161e4"}
$ {\mathcal{O}}(1) $ is very ample: write $ {\mathbf{P}}^n = \mathop{\mathrm{Proj}}k[x_0, \cdots, x_{n}] $, then $ x_0,\cdots, x_n $ induce $ n+1 $ global sections . For $ n\geq 1 $, $ {\mathcal{O}}(n) $ corresponds to the Veronese embedding into $ {\mathbf{P}}^N $, and so is very ample.
:::

::: {.front card-id="card-938f2d52c80bd08e"}
Prove that if $ X $ is a projective variety, $ H^0(X; {\mathcal{O}}_X) = k $
:::

::: {.back card-id="card-938f2d52c80bd08e"}
Since $ {\mathbf{P}}^n $ is proper, $ X\subseteq {\mathbf{P}}^n $ is proper as a closed subvariety. So $ s\in H^0(X; {\mathcal{O}}_X) $ is the same as a regular map $ s: X\to {\mathbf{A}}^1 $.

By properness, $ \operatorname{im}s \subseteq {\mathbf{A}}^1 $ is closed and thus a finite set of points since $ {\mathbf{A}}^1 $ has the cofinite topology.

By irreducibility, it must be one point, so $ s $ is a constant map $ s(x) = \lambda $ for some $ \lambda \in k $, so sections biject with elements of $ k $.
:::

::: {.front card-id="card-610ae6d59c072f6d"}
Discuss $ H^*({\mathbf{P}}^n; {\mathcal{O}}(d)) $.
:::

::: {.back card-id="card-610ae6d59c072f6d"}
$ k[x_0,\cdots, x_n]_d $ for $ *=0 $,

zero for $ *=1,\cdots, n-1 $, and

$ \qty{\prod_{i=1}^n x_i }^{-1}k[x_0^{-1}, \cdots, x_n^{-1}] $ for $ *=n $.
:::

::: {.front card-id="card-9db7a801cc266d51"}
What is the **blowup** of a variety?
:::

::: {.back card-id="card-9db7a801cc266d51"}
For $ \operatorname{Bl}_0 {\mathbf{A}}^n $: take $ {\mathbf{A}}^n\times {\mathbf{P}}^{n-1} $ with coordinates $ {\left[ {x_0, \cdots, x_{n-1}} \right]}, {\left[ {y_0:\cdots : y_{n-1}} \right]} $, so the closed subsets are $ V(f) $ where $ f $ is a polynomial in $ x_i, y_i $ which is homogeneous in the $ y_i $. Take the blowup to be the subset $ \left\{{x_iy_j = x_j y_i {~\mathrel{\Big\vert}~}1\leq i,j\leq n-1}\right\} = \left\{{2\times 2\text{ minors of} \begin{bmatrix}x_0 & x_1 & \cdots & x_n \\ y_0 & y_1 & \cdots & y_n \end{bmatrix}}\right\} $.

Then $ \exists \pi: \operatorname{Bl}_0 {\mathbf{A}}^n \to {\mathbf{A}}^n $ where $ {\sharp}\pi^{-1}(p) = 1 $ for $ p\neq 0 $ and $ \pi^{-1}(0)\cong {\mathbf{P}}^{n-1} $ corresponding to all lines through $ 0 $.

For $ \operatorname{Bl}_Y {\mathbf{A}}^n $ with $ Y \subseteq {\mathbf{A}}^n $ a closed subvariety: take $ { \operatorname{cl}}_{\operatorname{Bl}_0 {\mathbf{A}}^n}\qty{\pi^{-1}(Y\setminus\left\{{0}\right\})} $.
:::

::: {.front card-id="card-77f1ef48e07e3dc0"}
What is the **blowup of a scheme along a subscheme**? How does this recover blowups for varieties?
:::

::: {.back card-id="card-77f1ef48e07e3dc0"}
Can generally blowup along a coherent sheaf of ideals $ {\mathcal{I}} $ on $ X $: take the sheaf of graded algebras $ \tilde {\mathcal{I}}\coloneqq\bigoplus_{d\geq 0}{\mathcal{I}}^d $ where $ {\mathcal{I}}^0 \coloneqq{\mathcal{O}}_X $ and set $ \tilde X \coloneqq\mathop{\mathrm{Proj}}\tilde {\mathcal{I}} $. Can do this with the ideal of sheaf of $ Y\hookrightarrow X $ a closed subscheme.

For $ X={\mathbf{A}}^n_{/ {k}} $, $ p=0 $ corresponds to $ I = \left\langle{x_0,\cdots,x_n}\right\rangle $ and $ \tilde X \coloneqq\mathop{\mathrm{Proj}}S $ where $ S\coloneqq\bigoplus_{d\geq 0} I^d $; then setting $ X \coloneqq\operatorname{Spec}A, A\coloneqq k[x_1, \cdots, x_{n}] $ there is a surjection $ A[y_1,\cdots, y_n] $ where $ y_i\mapsto x_i, {\left\lvert {x_i} \right\rvert} = 1 $, making $ \tilde X $ isomorphic to a closed subscheme of $ \mathop{\mathrm{Proj}}A[y_1,\cdots, y_n] \cong {\mathbf{P}}^{n-1}_{/ {A}} $, and the ideal of definition is generated by $ \left\{{x_iy_j - x_jy_i}\right\} $.
:::

::: {.front card-id="card-f99d3b6a576c782a"}
Discuss ampleness of $ {\mathcal{L}}\in \operatorname{Pic}(C) $ for $ C $ a smooth complete curve.
:::

::: {.back card-id="card-f99d3b6a576c782a"}
$ {\mathcal{L}}= {\mathcal{O}}(D) $ is ample iff $ \deg D > 0 $, using RR.
:::

::: {.front card-id="card-a4380c8c6119e01f"}
What is a **base point** of a linear system?
:::

::: {.back card-id="card-a4380c8c6119e01f"}
For $ p\in X $ and a linear system $ {\left\lvert {D_0} \right\rvert} $, $ p $ is a base point iff $ p\in \mathop{\mathrm{supp}}D $ for all $ D\in {\left\lvert {D_0} \right\rvert} $, where $ \mathop{\mathrm{supp}}D $ is the union of all prime divisors in $ D $.
:::

::: {.front card-id="card-95da29f9068355c0"}
What is a **strict transform**?
:::

::: {.back card-id="card-95da29f9068355c0"}
For $ \pi: \tilde X\to X $ a blowup with center $ Z $ and $ Y\leq X $ a closed subscheme, the closure $ { \operatorname{cl}}_{\tilde X} \pi^{-1}(Y\setminus Z $).
:::

::: {.front card-id="card-93938d5c9783d630"}
Discuss properties of the blowup morphism.
:::

::: {.back card-id="card-93938d5c9783d630"}
It is an isomorphism away from $ p $ and $ \pi^{-1}(p) $, for varieties $ X $ it is birational, proper, and surjective; if $ X $ is quasiprojective then $ \tilde X $ is too and $ \pi $ is projective.
:::

::: {.front card-id="card-3ee6736250e4d3aa"}
What is a **resolution of singularities**?
:::

::: {.back card-id="card-3ee6736250e4d3aa"}
For varieties $ X $, a regular irreducible variety $ \tilde X $ admitting a proper birational morphism $ \pi: \tilde X\to X $ and restricts to an isomorphism on $ f^{-1}(X^{\mathrm{reg}}) $. For curves, the normalization suffices since it removes all singularities in codimension 1.
:::

::: {.front card-id="card-75342d6157a4433d"}
What is a **prime divisor** on a scheme?
:::

::: {.back card-id="card-75342d6157a4433d"}
A closed integral subscheme of dimension 1. Need $ X $ to be a Noetherian integral separated scheme which is regular in codimension 1.
:::

::: {.front card-id="card-319a35d07535844b"}
What is a **geometrically connected** scheme?
:::

::: {.back card-id="card-319a35d07535844b"}
A scheme that is connected and does not become disconnected after base change: for $ X\in {\mathsf{Sch}}_{/ {k}} $, for every extension $ L $ of $ k $, require that $ X \underset{\scriptscriptstyle {k} }{\times} L $ is connected.
:::

::: {.front card-id="card-cf5815d5a2806ef1"}
What is the **degree** of a morphism of curves?
:::

::: {.back card-id="card-cf5815d5a2806ef1"}
For $ f:X\to Y $ finite, the degree of the field extension $ [K(X): K(Y)] $.
:::
