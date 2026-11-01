---
title: "Algebraic Geometry::Mirror Symmetry::Integral Affine Structures"
---

::: {.front card-id="card-dcd1e437d41fbead"}
What is a cusp singularity?
:::

::: {.back card-id="card-dcd1e437d41fbead"}
Any singularity such that the exceptional divisor of the minimal resolution is a cycle of rational curves.
:::

::: {.front card-id="card-d5ec173bf75ab3ce"}
What does it mean for a singularity to be **smoothable**, i.e. what is a **smoothing**?
:::

::: {.back card-id="card-d5ec173bf75ab3ce"}
For $X$ with isolated singularities, a flat family $\mcx\to \mathbb{D}$ with $\mcx_0 \cong X$ and all nearby fibers $\mcx_t$ smooth. E.g. most plane curves are smoothable, not automatic for surfaces. Hypersurface singularities are always smoothable. There is no general criterion. There exists non-smoothable varieties: e.g. a cone over a 2-dimensional abelian variety which can't be a limit of smooth projective varieties. Alternatively, quotient singularities in dimension $\geq 3$, since these are rigid. Du Val singularities are smoothable, since they are hypersurface type, replace $F(x,y,z)= 0$ with $F(x,y,z) = t$.
:::

::: {.front card-id="card-1e60c609baa1e7af"}
What is an **anticanonical pair**?
:::

::: {.back card-id="card-1e60c609baa1e7af"}
A pair $(Y, D)$ where $Y$ is a rational surface and $D$ is a cycle of rational curves $D = \sum D_i$.
:::

::: {.front card-id="card-8f58666bb53a9709"}
What is a negative definite pair?
:::

::: {.back card-id="card-8f58666bb53a9709"}
An ACP where $M_{ij} \coloneqq D_i \cdot D_j$ is negative definite, i.e. ${\left\langle {z},~{Mz} \right\rangle} < 0$ for all $z \in {\mathbf{R}}^n\setminus\left\{{0}\right\}$.
:::

::: {.front card-id="card-f64cc783f07e304d"}
What is a **toric pair**?
:::

::: {.back card-id="card-f64cc783f07e304d"}
An ACP $(Y, D)$ where $Y$ is a toric variety and $D$ is its toric boundary.
:::

::: {.front card-id="card-89fdc8b480c546ee"}
What is the hyperbolic Inoue surface?
:::

::: {.back card-id="card-89fdc8b480c546ee"}
From type $\rm{VII}_0$ in the classification of complex analytic surfaces, those $V$ with Betti number $b_1 = 1$ and Kodaira dimension $\kappa = -\infty$. Every curve $C_i$ in $X$ is a component of one of two cycles $D$ or $\widehat{D}$ where $D+\widehat{D} \in {\left\lvert {-K_X} \right\rvert}$. Blow $D$ and $\widehat{D}$ down to get $\overline{V}$ with two dual cusps $p, \widehat{p}$, tracked by the germ $(\overline{V}, p, \widehat{p}$).
:::

::: {.front card-id="card-aa75df981fa1d916"}
Discuss the **dual divisors** $D$ and $\widehat{D}$.
:::

::: {.back card-id="card-aa75df981fa1d916"}
For $(\overline{V}, p)$ the germ of a cusp, the exceptional divisor $D$ of a minimal resolution forms (by definition) a cycle of smooth rational transversely intersecting curves with $D_{i\operatorname{mod}n}\cdot D_{i+1 \operatorname{mod}n} = 1$, which is characterized by the diagonal of the intersection matrix $\mathbf{d} = {\left[ {d_1,\cdots, d_n} \right]}$. The hyperbolic Inoue surface has two cycles $D, \widehat{D}$ which blow down to dual cusps $p, \widehat{p}$.
:::

::: {.front card-id="card-e1f9c6c06a356657"}
What is **Looijenga's conjecture**?
:::

::: {.back card-id="card-e1f9c6c06a356657"}
Known: If $\widehat{D}$ contracts to a smoothable cusp singularity $\widehat{p}$, then $D$ is the anticanonical divisor of some rational surface. Conjecture: the converse, i.e. if $D$ is the anticanonical divisor of some rational surface, then the cusp singularity associated to $\widehat{D}$ is smoothable.
:::

::: {.front card-id="card-428498c896e7e4e6"}
Why is the converse to Looijenga's conjecture true?
:::

::: {.back card-id="card-428498c896e7e4e6"}
Statement: If $\widehat{D}$ contracts to a smoothable cusp singularity $\widehat{p}$, then $D$ is the anticanonical divisor for some rational surface. Suppose $\widehat{p}$ is smoothable, then Looijenga shows $\overline{V}$ has a universal deformation which is semi-universal for the germ $(\overline{V}, p, \widehat{p})$, so one gets a deformation $\pi: \mcv\to \mathbb{D}$ with $\mcv_0 = \overline{V}$ where $(\overline{V}, p)$ is constant and $(\overline{V}, \widehat{p})$ is smoothed. The general fiber $\mcv_t$ is a surface with a cusp singularity $p_t$ (basically $p$); simultaneously smooth all $p_t$ to get $\mcy\to \mathbb{D}$ where $\mcy_t$ is smooth and $\mcy_0$ is a partially contracted $V$ with a cusp $\widehat{p}$. The general fibers $\mcy_t$ are the desired rational surfaces with anticanonical divisor $D$.
:::

::: {.front card-id="card-20dcddff332cb1eb"}
What is a **pseudofan**?
:::

::: {.back card-id="card-20dcddff332cb1eb"}
For $(V, D)$ an ACP where $D = \sum_{i=1}^nD_i$ is a cycle, the pseudofan of $(V, D)$ is the triangulated IAS whose underlying triangulated surface is $\Cone(\Gamma(D))$, the cone over the dual complex of $D$.
:::

::: {.front card-id="card-f270c4dc468b873e"}
What are the two main **surgeries** on pseudofans?
:::

::: {.back card-id="card-f270c4dc468b873e"}
Internal blowups and node smoothing.

An internal blowup inserts an interior exceptional curve and changes one boundary self-intersection $D_i^2\mapsto D_i^2-1$. Smoothing a node between $D_i$ and $D_{i+1}$ replaces those components by one with self-intersection $D_i^2+D_{i+1}^2+2$.
:::

::: {.front card-id="card-a45da020a729aa8b"}
What is an **almost toric fibration**?
:::

::: {.back card-id="card-a45da020a729aa8b"}
A Lagrangian fibration $\mu: (X, \omega) \to S$ whose general fiber is a smooth $T^2$ which undergoes symplectic reduction at ${{\partial}}S$ where fibers in $S^\circ$ degenerate to wedges of $S^2$ at finitely many specified points. The **almost toric base** generalizes the moment polytope and has an IA structure with $v\in S^\sing\iff \mu^{-1}(v)$ is singular. $\mu^{-1}({{\partial}}S)$ is an anticanonical divisor on $X$.
:::

::: {.front card-id="card-f4f2a1127c580098"}
Discuss almost toric fibrations over a disc.
:::

::: {.back card-id="card-f4f2a1127c580098"}
Represented by $\mu: (Y, D, \omega)\to S$ a symplectic anticanonical pair where components of $D$ map to ${{\partial}}S$. Doing internal blowups on a boundary component $P_i\subseteq {{\partial}}S$ corresponds to an internal blowup on $D_i$ in $Y$, similarly for node smoothing.
:::

::: {.front card-id="card-36d6504007dcd5d9"}
What is a **stratified space**?
:::

::: {.back card-id="card-36d6504007dcd5d9"}
A topological space $B$ with a filtration $\emptyset = B_{-1} \subseteq B_0 \subseteq \cdots$ where each $B_k$ is closed and the sections $S_d(B) \coloneqq B_d\setminus B_{d-1}$ are smooth $d\dash$dimensional manifolds and $B = \bigcup_{d\geq 0} B_d$. Say $B$ is dimension $n$ if $n$ is maximal such that $S_n(B) \neq \emptyset$, in which case $S_n(B)$ is the **top stratum**.
:::

::: {.front card-id="card-f7d3c07e867f37fd"}
What is a **Lagrangian torus fibration**?
:::

::: {.back card-id="card-f7d3c07e867f37fd"}
A fibration $f: (X^{2n}, \omega) \to B$ which is a proper continuous map where $B$ is an $n\dash$dimensional stratified space and $f$ is a smooth submersion over the top stratum of $B$ with connected Lagrangian fibers, where the remaining fibers are connected stratified spaces with isotropic strata.
:::

::: {.front card-id="card-bc08b869a67e268a"}
What is an order $k$ **refinement** of an IAS?
:::

::: {.back card-id="card-bc08b869a67e268a"}
For $S$ an IAS, the new IAS $S[k]$ gotten by post-composing the charts on $S$ with multiplication by $k$.
:::

::: {.front card-id="card-f5f851cb3bb46914"}
What is a **corner blowup**?
:::

::: {.back card-id="card-f5f851cb3bb46914"}
For $(Y, D)$ an ACP, a blowup at a node of $D$. Yields anticanonical $\pi^* D - E$
:::

::: {.front card-id="card-7cb45956de5022ad"}
What is an internal blowup?
:::

::: {.back card-id="card-7cb45956de5022ad"}
For $(Y, D)$ an ACP, a blowup at $p\in D^\sing$. Yields anticanonical $\pi^* D - E$
:::

::: {.front card-id="card-fdc3053e059f5adb"}
How do IAS surgeries affect **charge**?
:::

::: {.back card-id="card-fdc3053e059f5adb"}
**Internal blowup** on $D_i: d_i\mapsto d_{i} + 1$, no other changes. $Q(D) \mapsto Q(D) + 1$. **$+1$ charge**.

**Corner blowup** on $D_i \cap D_{i+1}$: $(\cdots, d_i, d_{i+1},\cdots)\mapsto (\cdots, d_i+1, 1, d_{i+1} +1,\cdots)$ and $Q(D) \mapsto Q(D)$ **$+0$ charge**.

**Node smoothing** on $D_{i} \cap D_{i+1}$: $(\cdots, d_i, d_{i+1}, \cdots)\mapsto (\cdots, d_{i} + d_{i+1} - 2,\cdots)$. **$+1$ charge.**
:::

::: {.front card-id="card-d49137a8cee771d1"}
What is a **type III anticanonical pair** $(\mcx_0, D)$?
:::

::: {.back card-id="card-d49137a8cee771d1"}
A surface $\mcx_0$ with a decomposition $\mcx_0 = \bigcup_{i=0}^n V_i$ such that...

**Central HIS and normality**: $V_0$ is the hyperbolic Inoue surface with cycles $D, \widehat{D}$ and for $i > 0$ the normalizations $\tilde V_i\to V_i$ are smooth rational surfaces.

**ACP Double Curves**: For $D_{ij}$ an irreducible double curve of $\mcx_0$ lying on $V_{i} \cap V_j$, let $D_i$ be the union of the double curves $D_{ij}$ contained in $V_i$ and let $\tilde D_i$ be its inverse image under normalization; then require $(\tilde V_i, \tilde D_i)$ to be an ACP.

**Triple point formula**: For $D_{ij}$ a double curve joining $V_i$ and $V_j$, then
$$\qty{{ \left.{{D_{ij}}} \right|_{{\tilde V_i}} }}^2 + \qty{{ \left.{{D_{ij}}} \right|_{{\tilde V_j}} }}^2 = \begin{cases}-2 & D_{ij} \text{ smooth} \\0 & D_{ij} \text{ nodal} \end{cases}$$
The dual complex $\Gamma(\mcx_0)$ is a triangulation of $S^2$.
:::

::: {.front card-id="card-726a9d643dacbb85"}
What is **$d\dash$semistability**?
:::

::: {.back card-id="card-726a9d643dacbb85"}
$\operatorname{Ext}_{{\mathcal{O}}_{\mcx_0}}( \Omega_{\mcx_0}^1, {\mathcal{O}}_{\mcx_0}) \cong {\mathcal{O}}_{\mcx_0^\sing}$
:::

::: {.front card-id="card-34641c38d14db4fa"}
What is the **Friedman-Miranda criterion**?
:::

::: {.back card-id="card-34641c38d14db4fa"}
The cusp singularity associated to $\widehat{D}$ is smoothable iff there exists a type III ACP $(\mcx_0, D)$.
:::

::: {.front card-id="card-eeb1f10b7050ade0"}
What is the **dual complex** of a type III anticanonical pair?
:::

::: {.back card-id="card-eeb1f10b7050ade0"}
For $(\mcx_0, D)$ an ACP, the triangulation of $S^2$ with vertices are the components of $V_i$, directed edges $e_{ij}$ for double curves $D_{ij}$, triangular faces are triple points $T_{ijk}$.
:::

::: {.front card-id="card-eb930237132be4b8"}
What is a **degeneration**?
:::

::: {.back card-id="card-eb930237132be4b8"}
A degeneration of $X$: a flat proper morphism $\pi: \mcx\to \mathbb{D}$ of complex analytic spaces such that $\pi$ is smooth over $\mathbb{D}^\circ$, the general fibers $\mcx_t$ are deformation equivalent to $X$ for all $t\in \mathbb{D}^\circ$, and the monodromy action on $H^2(\mcx_t; \ZZ)$ is nontrivial and unipotent.
:::

::: {.front card-id="card-701904cdad9a4b3c"}
What is a **maximally unipotent degeneration**?
:::

::: {.back card-id="card-701904cdad9a4b3c"}
Unipotent: $r-1$ is nilpotent; for matrices, $p(t) = (t-1)^n$ for some $n$, so all eigenvalues are 1. Index of unipotency: the minimal power $r$ such that $(M-\operatorname{id})^{r-1}\neq 0$ but $(M-\operatorname{id})^r=0$. Maximal: of maximal possible unipotency index; alternatively the limiting mixed Hodge structure is Hodge-Tate type (extensions of sums of $\ZZ(n)$). Concretely, the monodromy operator $T: H^n(\mcx_t; \QQ) {\circlearrowleft}$ satisfies $(T-I)^{n+1} = 0$ but $(T-I)^n\neq 0$.
:::

::: {.front card-id="card-2392e89f2c4ead0e"}
What is a basis triangle?
:::

::: {.back card-id="card-2392e89f2c4ead0e"}
A triangle $\Delta \subseteq {\mathbf{R}}^2$ such that $\mathrm{Vert}(\Delta) \subset \ZZ^2$ and $\mu(\Delta) = 1/2$.
:::

::: {.front card-id="card-9247748d2ed4dab9"}
What is a **triangulated integral affine structure with singularities**?
:::

::: {.back card-id="card-9247748d2ed4dab9"}
A real surface with boundary (possibly empty) $\Sigma_g$ equipped with a triangulation $T$ such that $\Sigma_g\setminus\mathrm{Vert}(T)$ admits an atlas $\left\{{(U_i, \phi_i: U_i\to {\mathbf{R}}^2)}\right\}$ such that $\phi_i \circ \phi_j^{-1}\in \SL_2(\ZZ)\rtimes\ZZ^2$ and for each triangle $\Delta \in T$, the interior $\Delta^\circ$ admits a chart to a *basis triangle*.
:::

::: {.front card-id="card-8e3344790c13a342"}
What is a **nodal trade**?
:::

::: {.back card-id="card-8e3344790c13a342"}
Alternative terminology for node smoothing.
:::

::: {.front card-id="card-4110e677dd492db8"}
What is the **SYZ conjecture**?
:::

::: {.back card-id="card-4110e677dd492db8"}
Gross, 2008: If $X, X {}^{ \vee }$ are mirror CYs, they admit a common cospanning fibration $X\to B \leftarrow X {}^{ \vee }$ whose fibers are special Lagrangians and the general fiber is a torus. There should also be a canonical map $X {}^{ \vee }_t { \, \xrightarrow{\sim}\, }H^1(X_t; {\mathbf{R}}/\ZZ)$ and $X_t { \, \xrightarrow{\sim}\, }H^1(X {}^{ \vee }_t; {\mathbf{R}}/\ZZ)$ (likely too strong to be true)
:::

::: {.front card-id="card-23688564458dd17f"}
What is the relation to **SYZ mirror symmetry**?
:::

::: {.back card-id="card-23688564458dd17f"}
Generally about boundaries in a CY moduli space, particularly near especially "bad" degenerations: maximally unipotent degenerations (MUD) or large complex structure limits. One can find special Lagrangian tori on CYs near these limit points, and approaching the limit, expect to see a larger portion of the CY filled by tori. Toric degenerations are a special case of MUD. Expect the base $B$ of a special Lagrangian fibration to be the Gromov-Hausdorff limit of a sequence of CYs near MUD, and GH limit should be the dual intersection complex of the AG degeneration. The base is an affine manifold. If $\pi:\mcx\to \mathbb{D}$ is such a degeneration of CYs and $\mcx$ is polarized (equipped with $\mcl\in \operatorname{Pic}(\mcx)$ relatively ample), should exists a dual polarization $\widehat{\mcl}$ on $\widehat{\mcx}$.
:::

::: {.front card-id="card-b3a5d5b512719741"}
What is **charge**?
:::

::: {.back card-id="card-b3a5d5b512719741"}
$Q(Y, D):=12+\sum_{i=1}^n\left(d_i-3\right)=12+\sum_{i=1}^n\left(a_i-b_i\right)$ where $\mathbf{d}=\left(d_1, \ldots, d_n\right)=(a_1+3, \underbrace{2, \ldots, 2}_{b_1}, \ldots, a_k+3, \underbrace{2, \ldots, 2}_{b_k})$ and $a_i, b_i \geq 0$. All toric pairs have charge zero.
:::

::: {.front card-id="card-0d5e3770ce1f2ca9"}
How can one obtain $\widehat{ \mathbf d}$ for $\widehat{D}$ from $\mathbf d$?
:::

::: {.back card-id="card-0d5e3770ce1f2ca9"}
Interchange the $a_i$ and $b_i$: $\widehat{\mathbf{d}}=\left(\widehat{d_1},\cdots, \widehat{d_s} \right)=(b_1+3, \underbrace{2, \ldots, 2}_{a_1}, \ldots, b_k+3, \underbrace{2, \ldots, 2}_{a_k})$
:::

::: {.front card-id="card-e2d5b7767b890517"}
Discuss $Q(D)$ and $Q(\widehat{D})$.
:::

::: {.back card-id="card-e2d5b7767b890517"}
$Q(D) \coloneqq 12 + \sum (d_i - 3)$ and $Q(D) + Q(\widehat{D}) = 24$. This follows from the formula $Q(D) = 12 + \sum(a_i - b_i)$ and that $\widehat{D}$ swaps $a_i$ and $b_i$.
:::

::: {.front card-id="card-2985fd69293c1543"}
Discuss **conservation of charge**.
:::

::: {.back card-id="card-2985fd69293c1543"}
For $(\mcx_0, D)$ a Type III ACP, $\sum Q(V_i, D_i) = 24$.
:::

::: {.front card-id="card-4498d8364f0200a3"}
What is a **nonsingular IAS**?
:::

::: {.back card-id="card-4498d8364f0200a3"}
When the atlas of charts on an IAS for $S\setminus\mathrm{Vert}(T)$ extends to $S$; if not, denote the points where this fails as $S^\sing$.
:::

::: {.front card-id="card-974cd49e9a49cf40"}
What is the **developing map**?
:::

::: {.back card-id="card-974cd49e9a49cf40"}
For $S$ an IAS with singularities, take contractible opens $U \subset S\setminus S^\sing$ with charts $\phi_U: U\to {\mathbf{R}}^2$, uniquely defined up to an element of $\SL_2(\ZZ)\rtimes\ZZ^2$, and define $\Phi: \widetilde{S\setminus S^\sing} \to {\mathbf{R}}^2$ from the universal cover by gluing any charts $\phi_U, \phi_V$ which agree on $U\cap V$. Equivalent to the data of a monodromy representation $\pi_1(S\setminus S^\sing) \to \SL_2(\ZZ) \rtimes\ZZ^2$.
:::

::: {.front card-id="card-3c8695ea7ecde08d"}
How are ACPs related to toric pairs?
:::

::: {.back card-id="card-3c8695ea7ecde08d"}
Prop 5.1: every ACP $(Y, D)$ is a sequence of node smoothings and internal blowups of a toric pair $(\overline{Y}, \overline{D})$.
:::

::: {.front card-id="card-bfda170c1a6d2203"}
What is the negative self-intersection of an edge in an IAS?
:::

::: {.back card-id="card-bfda170c1a6d2203"}
For $e_{ik}$ an edge in $\Delta \subset T$ for an IAS, letting $e_{ij}, e_{il}$ be the edges emanating from $v_i$ clockwise and counterclockwise to $e_{ik}$, define $d_{ik}$ to be the "negative self intersection" of $e_{ik}$ by
$$d_{ik} e_{ik} = e_{ij} + e_{il}$$
The data of $d_{ik}$ for each edge $e_{ik}$ satisfying $d_{ik} + d_{ki} = 2$ for each $i, k$ uniquely determines a triangulated IAS.
:::

::: {.front card-id="card-ad1873dac9f9941a"}
When does a surface $\mcx_0$ smooth to an anticanonical pair in a family $\mcx\to \mathbb{D}$?
:::

::: {.back card-id="card-ad1873dac9f9941a"}
Being a Type III ACP $(\mcx_0, D)$ plus $d\dash$semistability.
:::

::: {.front card-id="card-de8cda450126374b"}
Motivation: singularities.
:::

::: {.back card-id="card-de8cda450126374b"}
- Examples:
- Blowups:
:::

::: {.front card-id="card-3fb785303c85fc6d"}
Discuss dual intersection graphs and cycles associated to minimal resolutions.
:::

::: {.back card-id="card-3fb785303c85fc6d"}
- For $\pi: (\tilde X, E)\to (X, 0)$ a minimal (no -1 curves) resolution, define $\Gamma$ whose vertices are components of $E$, put $e_{ij}\coloneqq E_i \cdot E_j$ edges between $v_i$ and $v_j$, and attach the number $e_{ii} \coloneqq-E_i^2$ to each $v_i$. Note $\Gamma$ has no graph-theoretic cycles. Form a matrix $M_{ij} = e_{ij}$, by a theorem of Grauert-Mumford $M$ is negative definite.
- Example: ?
:::

::: {.front card-id="card-c354b1c7c752e729" tags="definition"}
Affine manifold
:::

::: {.back card-id="card-c354b1c7c752e729"}
An affine manifold is a smooth manifold $B$ with an atlas $\{(U_i,\phi_i)\}$ whose transition maps $\phi_i\circ\phi_j^{-1}$ are affine transformations of $\mathbb R^n$; equivalently $B$ carries a flat torsion-free connection. It is integral if the transitions lie in $\mathrm{Aff}(\mathbb Z^n)=\mathrm{GL}_n(\mathbb Z)\ltimes\mathbb Z^n$.
:::

::: {.front card-id="card-b1cc21ccaddb6e46" tags="definition"}
Almost toric base
:::

::: {.back card-id="card-b1cc21ccaddb6e46"}
The almost toric base of an almost toric fibration $\mu:(X,\omega)\to S$ is the stratified space $S$ with an integral affine structure on $S\setminus S^{\mathrm{sing}}$; it generalizes the moment polytope, and $\mu^{-1}(v)$ is singular exactly at $v\in S^{\mathrm{sing}}$.
:::

::: {.front card-id="card-92769a4b13586c9a" tags="definition"}
Cycle of rational curves
:::

::: {.back card-id="card-92769a4b13586c9a"}
A cycle of rational curves is a reduced connected divisor $D=\sum_{i=1}^n D_i$ on a smooth surface with each $D_i\cong\mathbb P^1$, $D_i\cdot D_{i+1}=1$ for indices modulo $n$, $D_i\cdot D_j=0$ when $|i-j|>1$, and no other intersections. It is the exceptional divisor of the minimal resolution of a cusp singularity.
:::

::: {.front card-id="card-e5ac4665a3c590e7" tags="definition"}
Deformation equivalent
:::

::: {.back card-id="card-e5ac4665a3c590e7"}
Two compact complex varieties $X$ and $Y$ are deformation equivalent if they are fibers of the same proper smooth family $\mathcal X\to S$ over a connected base $S$; equivalently they are joined by a chain of deformations.
:::

::: {.front card-id="card-7ec42e54742410f3" tags="definition"}
Double curve
:::

::: {.back card-id="card-7ec42e54742410f3"}
In a reducible surface $X_0=\bigcup_i V_i$, a double curve is an irreducible curve $D_{ij}\subset V_i\cap V_j$ along which two irreducible components $V_i$ and $V_j$ meet. Locally $X_0$ is $xy=0$ times a curve, and the normalization separates the two branches.
:::

::: {.front card-id="card-5fa52bc6d9e5d4e3" tags="definition"}
Dual cusp
:::

::: {.back card-id="card-5fa52bc6d9e5d4e3"}
For a cusp singularity with cycle $D$ and self-intersection data $\mathbf d=(d_1,\dots,d_n)$, the dual cusp is the cusp whose minimal-resolution cycle $\widehat D$ has data $\widehat{\mathbf d}$ obtained by interchanging the coefficients $a_i$ and $b_i$ in $\mathbf d=(a_1+3,2,\dots,2,\dots,a_k+3,2,\dots,2)$. It satisfies $Q(D)+Q(\widehat D)=24$.
:::

::: {.front card-id="card-57cc973230f7ba94" tags="definition"}
Dual intersection complex
:::

::: {.back card-id="card-57cc973230f7ba94"}
For a semistable degeneration $\pi:\mathcal X\to\Delta$ with central fiber $X_0=\sum_{i\in I}D_i$, the dual intersection complex is the simplicial complex with a vertex for each component $D_i$, an edge for each irreducible component of $D_i\cap D_j$, a triangle for each triple intersection, and so on. It records the incidence pattern of the components and is the base of the SYZ fibration in the large complex structure limit.
:::

::: {.front card-id="card-615708f96cbc7338" tags="definition"}
Grauert-mumford theorem
:::

::: {.back card-id="card-615708f96cbc7338"}
The Grauert-Mumford theorem states that a connected compact divisor $E=\sum E_i$ on a smooth complex surface can be contracted to a normal surface singularity if and only if its intersection matrix $(E_i\cdot E_j)$ is negative definite; the contraction is then unique up to isomorphism.
:::

::: {.front card-id="card-9065f7ad2a1a7ff3" tags="definition"}
Gromov-hausdorff limit
:::

::: {.back card-id="card-9065f7ad2a1a7ff3"}
The Gromov-Hausdorff limit of compact metric spaces $(X_i,d_i)$ is a compact metric space $(X,d)$ with $d_{GH}(X_i,X)\to0$; equivalently the $X_i$ admit $\epsilon_i$-dense $\epsilon_i$-isometric nets into $X$ with $\epsilon_i\to0$.
:::

::: {.front card-id="card-5572b0772967e64e" tags="definition"}
Hodge-tate
:::

::: {.back card-id="card-5572b0772967e64e"}
A mixed Hodge structure is Hodge-Tate if every graded piece $\mathrm{gr}^W_k$ is a direct sum of Tate twists $\mathbb Q(-p)$ of Hodge type $(p,p)$; equivalently it is a successive extension of the $\mathbb Q(n)$.
:::

::: {.front card-id="card-dee2f67fdb8f773a" tags="definition"}
Hypersurface singularity
:::

::: {.back card-id="card-dee2f67fdb8f773a"}
A hypersurface singularity is a germ $(X,p)$ isomorphic to $(V(f),0)\subset(\mathbb A^n,0)$ for a nonzero $f\in k[x_1,\dots,x_n]$ with $f(0)=0$ and $df(0)=0$; equivalently $\mathcal O_{X,p}\cong k[x_1,\dots,x_n]_{(x)}/(f)$.
:::

::: {.front card-id="card-c52d15822bcdec98" tags="definition"}
Integral affine structure
:::

::: {.back card-id="card-c52d15822bcdec98"}
An integral affine structure on an $n$-manifold $B$ is an atlas $\{(U_i,\phi_i:U_i\to\mathbb R^n)\}$ whose transition maps lie in $\mathrm{Aff}(\mathbb Z^n)=\mathrm{GL}_n(\mathbb Z)\ltimes\mathbb Z^n$; equivalently it is a flat torsion-free connection whose holonomy lies in $\mathrm{Aff}(\mathbb Z^n)$.
:::

::: {.front card-id="card-2bfad83d9328a7f6" tags="definition"}
Lagrangian fibration
:::

::: {.back card-id="card-2bfad83d9328a7f6"}
A Lagrangian fibration is a proper surjective map $f:(X^{2n},\omega)\to B$ whose smooth fibers are connected Lagrangian submanifolds of $X$, i.e. $\omega|_{f^{-1}(b)}=0$. A Lagrangian torus fibration has fibers $T^n$; the smooth locus of $B$ carries an integral affine structure.
:::

::: {.front card-id="card-63b5131f7fd0118f" tags="definition"}
Limiting mixed hodge structure
:::

::: {.back card-id="card-63b5131f7fd0118f"}
For a degeneration $\pi:\mathcal X\to\Delta^*$ with unipotent monodromy $T$, the limiting mixed Hodge structure is the mixed Hodge structure on the cohomology of the limiting fiber constructed by Schmid from the variation of Hodge structure and the weight filtration of the nilpotent operator $N=\log T$.
:::

::: {.front card-id="card-02b0355c3650e92b" tags="definition"}
Moment polytope
:::

::: {.back card-id="card-02b0355c3650e92b"}
For a Hamiltonian torus action on a compact symplectic manifold $(X,\omega)$ with moment map $\mu:X\to\mathfrak t^*$, the moment polytope is the convex polytope $\mu(X)\subset\mathfrak t^*$ (Atiyah-Guillemin-Sternberg). For a toric variety it is the polytope $P_D$ of an ample torus-invariant divisor.
:::

::: {.front card-id="card-1fd74048e90db1c2" tags="definition"}
Monodromy operator
:::

::: {.back card-id="card-1fd74048e90db1c2"}
For a degeneration $\pi:\mathcal X\to\Delta^*$, the monodromy operator is the automorphism $T$ of $H^*(\mathcal X_t)$ induced by the positive generator of $\pi_1(\Delta^*)\cong\mathbb Z$. For a semistable degeneration it is unipotent, and $N=\log T$ is nilpotent.
:::

::: {.front card-id="card-795c0ca34a8a8864" tags="definition"}
Monodromy representation
:::

::: {.back card-id="card-795c0ca34a8a8864"}
For a fibration $f:X\to B$ with fiber $F$, the monodromy representation is the homomorphism $\pi_1(B,b_0)\to\operatorname{Aut}(H^*(F;\mathbb Z))$ obtained by transporting cycles around loops in $B$. For a degeneration $\pi:\mathcal X\to\Delta^*$ it is generated by the Picard-Lefschetz transformation $T$.
:::

::: {.front card-id="card-4cb3e1460015c430" tags="definition"}
Nilpotent
:::

::: {.back card-id="card-4cb3e1460015c430"}
An element $N$ of a ring, or an endomorphism of a vector space, is nilpotent if $N^k=0$ for some $k\ge1$; the least such $k$ is its nilpotency index. An endomorphism $T$ is unipotent if $T-I$ is nilpotent.
:::

::: {.front card-id="card-56810efcabc4bf7c" tags="definition"}
Semi-universal deformation
:::

::: {.back card-id="card-56810efcabc4bf7c"}
A semi-universal (miniversal) deformation of $X$ is a deformation $\mathcal X\to S$ such that every deformation of $X$ is induced from it and the induced map on tangent spaces is unique; equivalently the Kodaira-Spencer map $T_0S\to\operatorname{Ext}^1(\Omega_X,\mathcal O_X)$ is an isomorphism.
:::

::: {.front card-id="card-2e3d766f0efeb706" tags="definition"}
Special lagrangian
:::

::: {.back card-id="card-2e3d766f0efeb706"}
A special Lagrangian submanifold of a Calabi-Yau manifold $(X,\omega,\Omega)$ is a Lagrangian submanifold $L\subset X$ (so $\omega|_L=0$ and $\dim_{\mathbb R}L=\dim_{\mathbb C}X$) with $\operatorname{Im}\Omega|_L=0$; equivalently $L$ is calibrated by $\operatorname{Re}\Omega$ and has minimal volume in its homology class.
:::

::: {.front card-id="card-50e0c6eeda83171e" tags="definition"}
Symplectic reduction
:::

::: {.back card-id="card-50e0c6eeda83171e"}
Symplectic reduction (Marsden-Weinstein quotient) of a symplectic manifold $(X,\omega)$ by a Hamiltonian action of a Lie group $G$ with moment map $\mu:X\to\mathfrak g^*$ is $\mu^{-1}(0)/G$, with the induced symplectic form on the smooth locus; more generally one uses $\mu^{-1}(\xi)/G_\xi$.
:::

::: {.front card-id="card-aa1ee324431e9f74" tags="definition"}
Toric boundary
:::

::: {.back card-id="card-aa1ee324431e9f74"}
The toric boundary of a toric variety $X_\Sigma$ is the reduced divisor $D=\sum_{\rho\in\Sigma(1)}D_\rho$, the complement of the dense torus $T\subset X_\Sigma$. It is a normal-crossing divisor, and $(X_\Sigma,D)$ is a toric pair.
:::

::: {.front card-id="card-d03d58dd6041270c" tags="definition"}
Toric degeneration
:::

::: {.back card-id="card-d03d58dd6041270c"}
A toric degeneration is a flat family $\pi:\mathcal X\to\Delta$ whose general fibers are smooth (often Calabi-Yau) and whose central fiber $X_0$ is a toric variety; equivalently the family is locally toric and its dual intersection complex is a triangulated integral affine manifold.
:::

::: {.front card-id="card-b4e485673235edf3" tags="definition"}
Triple point
:::

::: {.back card-id="card-b4e485673235edf3"}
A triple point of a reducible surface $X_0=\bigcup_i V_i$ is a point at which three irreducible components meet, or at which three double curves meet. In the dual complex it corresponds to a triangular face whose vertices are the components and whose edges are the double curves.
:::

::: {.front card-id="card-356efa2f005e6ec3" tags="definition"}
Type vii_0 surface
:::

::: {.back card-id="card-356efa2f005e6ec3"}
A type $\mathrm{VII}_0$ surface is a compact complex surface with $b_1=1$, $b_2=0$, and Kodaira dimension $\kappa=-\infty$, in Kodaira's classification of compact complex surfaces. The hyperbolic Inoue surfaces are examples.
:::

::: {.front card-id="card-e8b82c81356a6955" tags="definition"}
Unipotency index
:::

::: {.back card-id="card-e8b82c81356a6955"}
For a unipotent endomorphism $T$ (so $T-I$ is nilpotent), the unipotency index is the least integer $r\ge1$ such that $(T-I)^r=0$; equivalently it is the maximal Jordan-block size of $T$. A degeneration is maximally unipotent when this index is as large as possible, namely $r=n+1$ on $H^n$.
:::

::: {.front card-id="card-34e632bf729f4796" tags="definition"}
Universal deformation
:::

::: {.back card-id="card-34e632bf729f4796"}
A deformation $\mathcal X\to S$ of $X$ is universal if every deformation $\mathcal Y\to T$ of $X$ is induced from it by a unique base change $T\to S$. Equivalently the Kodaira-Spencer map is an isomorphism and the family is complete and rigid.
:::

::: {.front card-id="card-8934770be8e9010f" tags="definition"}
Node smoothing
:::

::: {.back card-id="card-8934770be8e9010f"}
The surgery on an anticanonical pair inverse to a corner blowup: contract the exceptional $(-1)$-curve produced by blowing up a node of the boundary divisor, so that the two boundary branches meet again in a node. On the weight data of an integral affine structure it acts by $(\dots,d_i,d_{i+1},\dots)\mapsto(\dots,d_i+d_{i+1}-2,\dots)$ and raises the charge by $1$.
:::

::: {.front card-id="card-d64fe05250d1165d" tags="definition"}
Top stratum
:::

::: {.back card-id="card-d64fe05250d1165d"}
Let $B$ be a stratified space with filtration $\emptyset=B_{-1}\subseteq B_0\subseteq\cdots$ and strata $S_d(B)=B_d\setminus B_{d-1}$. If $n$ is the largest integer with $S_n(B)\neq\emptyset$, the top stratum is $S_n(B)=B_n\setminus B_{n-1}$. It is an open dense $n$-dimensional manifold, and its complement is the union of the lower-dimensional strata.
:::

::: {.front card-id="card-1a1d68d156466368" tags="definition"}
Triple point formula
:::

::: {.back card-id="card-1a1d68d156466368"}
For a double curve $D_{ij}$ joining the components $V_i$ and $V_j$ of a type III anticanonical pair, the self-intersections in the two normalized components satisfy $(D_{ij}|_{\tilde V_i})^2+(D_{ij}|_{\tilde V_j})^2=-2$ when $D_{ij}$ is smooth and $0$ when $D_{ij}$ is nodal, where $\tilde V_i$ is the normalization of $V_i$.
:::
