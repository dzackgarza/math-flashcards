---
title: "Orals::Looijenga IAS"
---

- What is a cusp singularity?

    Any singularity such the the exceptional divisor of the minimal resolution is a cycle of rational curves.

- What does it mean for a singularity to be **smoothable**, i.e. what is a **smoothing**?

    For $ X $ with isolated singularities, a flat family $ {\mathcal{X}}\to \mathbb{D} $ with $ {\mathcal{X}}_0 \cong X $ and all nearby fibers $ {\mathcal{X}}_t $ smooth. E.g. most plane curves are smoothable, not automatic for surfaces. Hypersurface singularities are always smoothable. There is no general criterion. There exists non-smoothable varieties: e.g. a cone over a 2-dimensional abelian variety which can't be a limit of smooth projective varieties. Alternatively, quotient singularities in dimension $ \geq 3 $, since these are rigid. Du val singularities are smoothable, since they are hypersurface type, replace $ F(x,y,z)= 0 $ with $ F(x,y,z) = t $.

- What is a **rational surface**?

    A 2-dimensional projective variety birationally equivalent to $ {\mathbf{P}}^2 $; simplest in the Enriques-Kodaira classification. Always a repeated blowup of a minimal rational surface, one of $ {\mathbf{P}}^2 $ or $ { \mathbf{F} }_n $ (the Hirzebruch surface). Suffices to show irregularity $ q=0 $ and plurigenus $ p_2 = 0 $.

- What is a **contraction**?

    A surjective proper morphism $ f:X\to Y $ between normal projective schemes where $ f_* {\mathcal{O}}_X \cong {\mathcal{O}}_Y $, or equivalently the geometric fibers are connected.

- What is a **contractible curve**?

    E.g. if starting with a proper normal algebraic surface $ X $ and a curve $ C $ in $ X $, a contraction morphism $ \pi: X\to Y $ where $ \pi(C) $ is a point.

- What is an **anticanonical pair**?

    A pair $ (Y, D) $ where $ Y $ is a rational surface and $ D $ is a cycle of rational curves $ D = \sum D_i $.

- What is a negative definite pair?

    An ACP where $ M_{ij} \coloneqq D_i \cdot D_j $ is negative definite, i.e. $ {\left\langle {z},~{Mz} \right\rangle} < 0 $ for all $ z \in {\mathbf{R}}^n\setminus\left\{{0}\right\} $.

- What is a **toric pair**?

    An ACP $ (Y, D) $ where $ Y $ is a toric variety and $ D $ is its toric boundary.

- What is an exceptional curve of the first kind?

    Rational curves $ C $ isomorphic to $ {\mathbf{P}}^1 $ with $ C^2 = -1 $.

- What is a **resolution**?

    For $ X $ singular, a proper morphism $ \pi: W\to X $ where $ W $ is smooth, $ \pi^{-1}(X^{\mathsf{sm}}) \subseteq W $ is dense and $ \pi $ induces an isomorphism on the smooth locus.

- What is a **minimal resolution**?

    Minimal $ W $ is minimal iff whenever $ W'\to V $ is another resolution, it factors as $ W'\to W\to V $.

    Exist uniquely in dimensions 1 and 2, but may not in higher dimensions. For a surface with an isolated singularity at 0: $ \pi: W\to V $ is minimal iff $ \pi^{-1}(0) $ does not contain any exceptional curves of the first kind. Any non-minimal resolution must contain a -1 curve.

- What is the hyperbolic Inoue surface?

    From type $ \rm{VII}_0 $ in the classification of complex analytic surfaces, those $ V $ with Betti number $ b_1 = 1 $ and Kodaira dimension $ \kappa = -\infty $. Every curve $ C_i $ in $ X $ is a component of one of two cycles $ D $ or $ \widehat{D} $ where $ D+\widehat{D} \in {\left\lvert {-K_X} \right\rvert} $. Blow $ D $ and $ \widehat{D} $ down to get $ \overline{V} $ with two dual cusps $ p, \widehat{p} $, tracked by the germ $ (\overline{V}, p, \widehat{p} $).

- Discuss the **dual divisors** $ D $ and $ \widehat{D} $.

    For $ (\overline{V}, p) $ the germ of a cusp, the exceptional divisor $ D $ of a minimal resolution forms (by definition) a cycle of smooth rational transversely intersecting curves with $ D_{i\operatorname{mod}n}\cdot D_{i+1 \operatorname{mod}n} = 1 $, which is characterized by the diagonal of the intersection matrix $ \mathbf{d} = {\left[ {d_1,\cdots, d_n} \right]} $. The hyperbolic Innoue surface has two cycles $ D, \widehat{D} $ which blow down to dual cusps $ p, \widehat{p} $.

- What is **Looijenga's conjecture**?

    Known: If $ \widehat{D} $ contracts to a smoothable cusp singularity $ \widehat{p} $, then $ D $ is the anticanonical divisor of some rational surface. Conjecture: the converse, i.e. if $ D $ is the anticanonical divisor of some rational surface, then the cusp singularity associated to $ \widehat{D} $ is smoothable.

- Why is the converse to Looijenga's conjecture true?

    Statement: If $ \widehat{D} $ contracts to a smoothable cusp singularity $ \widehat{p} $, then $ D $ is the anticanonical divisor for some rational surface. Suppose $ \widehat{p} $ is smoothable, then Loojienga shows $ \overline{V} $ has a universal deformation which is semi-universal for the germ $ (\overline{V}, p, \widehat{p}) $, so one gets a deformation $ \pi: {\mathcal{V}}\to \mathbb{D} $ with $ {\mathcal{V}}_0 = \overline{V} $ where $ (\overline{V}, p) $ is constant and $ (\overline{V}, \widehat{p}) $ is smoothed. The general fiber $ {\mathcal{V}}_t $ is a surface with a cusp singularity $ p_t $ (basically $ p $); simultaneously smooth all $ p_t $ to get $ {\mathcal{Y}}\to \mathbb{D} $ where $ {\mathcal{Y}}_t $ is smooth and $ {\mathcal{Y}}_0 $ is a partially contracted $ V $ with a cusp $ \widehat{p} $. The general fibers $ {\mathcal{Y}}_t $ are the desired rational surfaces with anticanonical divisor $ D $.

- What is a **pseudofan**?

    For $ (V, D) $ an ACP where $ D = \sum_{i=1}^nD_i $ is a cycle, the pseudofanof $ (V, D) $ is the triangulated IAS whose underlying triangulated surface is $ { \mathrm{Cone} }(\Gamma(D)) $, the cone over the dual complex of $ D $.

- What are the two main **surgeries** on pseudofans?

    Internal blowups and node smoothing.

    Pics:

- What is an **almost toric fibration**?

    A Lagrangian fibration $ \mu: (X, \omega) \to S $ whose general fiber is a smooth $ T^2 $ which undergoes symplectic reduction at $ {{\partial}}S $ where fibers in $ S^\circ $ degenerate to wedges of $ S^2 $ at finitely many specified points. The **almost toric base** generalizes the moment polytope and has an IA structure with $ v\in S^{\mathrm{sing}}\iff \mu^{-1}(v) $ is singular. $ \mu^{-1}({{\partial}}S) $ is an anticanonical divisor on $ X $.

- Disuss almost toric fibrations over a disc.

    Represented by $ \mu: (Y, D, \omega)\to S $ a symplectic anticanonical pair where components of $ D $ map to $ {{\partial}}S $. Doing internal blowups on aboundary component $ P_i\subseteq {{\partial}}S $ corresponds to an internal blowup on $ D_i $ in $ Y $, similarly for node smoothing.

- What is a **stratified space**?

    A topological space $ B $ with a filtration $ \emptyset = B_{-1} \subseteq B_0 \subseteq \cdots $ where each $ B_k $ is closed and the sections $ S_d(B) \coloneqq B_d\setminus B_{d-1} $ are smooth $ d{\hbox{-}} $dimensional manifolds and $ B = \bigcup_{d\geq 0} B_d $. Say $ B $ is dimension $ n $ if $ n $ is maximal such that $ S_n(B) \neq \emptyset $, in which case $ S_n(B) $ is the **top stratum**.

- What is a **Lagrangian torus fibration**?

    A fibration $ f: (X^{2n}, \omega) \to B $ which is a proper continuous map where $ B $ is an $ n{\hbox{-}} $dimensional stratified space and $ f $ is a smooth submersion over the top stratum of $ B $ with connected Lagrangian fibers, where the remaining fibers are connected stratified spaces with isotropic strata.

- What is an order $ k $ **refinment** of an IAS?

    For $ S $ an IAS, the new IAS $ S[k] $ gotten by post-composing the charts on $ S $ with multiplication by $ k $.

- What is a **corner blowup**?

    For $ (Y, D) $ an ACP, a blowup at a node of $ D $. Yields anticanonical $ \pi^* D - E $

- What is an internal blowup?

    For $ (Y, D) $ an ACP, a blowup at $ p\in D^{\mathrm{sing}} $. Yields anticanonical $ \pi^* D - E $

- How do IAS surgeries affect **charge**?

    **Internal blowup** on $ D_i: d_i\mapsto d_{i} + 1 $, no other changes. $ Q(D) \mapsto Q(D) + 1 $. **$ +1 $ charge**.

    **Corner blowup** on $ D_i \cap D_{i+1} $: $ (\cdots, d_i, d_{i+1},\cdots)\mapsto (\cdots, d_i+1, 1, d_{i+1} +1,\cdots) $ and $ Q(D) \mapsto Q(D) $ **$ +0 $ charge**.

    **Node smoothing** on $ D_{i} \cap D_{i+1} $: $ (\cdots, d_i, d_{i+1}, \cdots)\mapsto (\cdots, d_{i} + d_{i+1} - 2,\cdots) $. **$ +1 $ charge.**

- What is a **type III anticanonical pair** $ ({\mathcal{X}}_0, D) $?

    A surface $ {\mathcal{X}}_0 $ with a decomposition $ {\mathcal{X}}_0 = \bigcup_{i=0}^n V_i $ such that...

    **Central HIS and normality**: $ V_0 $ is the hyperbolic Inoue surface with cycles $ D, \widehat{D} $ and for $ i > 0 $ the normalizations $ \tilde V_i\to V_i $ are smooth rational surfaces.

    **ACP Double Curves**: For $ D_{ij} $ an irreducible double curve of $ {\mathcal{X}}_0 $ lying on $ V_{i} \cap V_j $, let $ D_i $ be the union of the double curves $ D_{ij} $ contained in $ V_i $ and let $ \tilde D_i $ be its inverse image under normalization; then require $ (\tilde V_i, \tilde D_i) $ to be an ACP.

    **Triple point formula**: For $ D_{ij} $ a double curve joining $ V_i $ and $ V_j $, then

    $$\qty{{ \left.{{D_{ij}}} \right|_{{\tilde V_i}} }}^2 + \qty{{ \left.{{D_{ij}}} \right|_{{\tilde V_j}} }}^2 = \begin{cases}-2 & D_{ij} \text{ smooth} \\0 & D_{ij} \text{ nodal} \end{cases}$$

    The dual complex $ \Gamma({\mathcal{X}}_0) $ is a triangulation of $ S^2 $.

- What is **$ d{\hbox{-}} $semistability**?

    $  \operatorname{Ext}_{{\mathcal{O}}_{{\mathcal{X}}_0}}( \Omega_{{\mathcal{X}}_0}^1, {\mathcal{O}}_{{\mathcal{X}}_0}) \cong {\mathcal{O}}_{{\mathcal{X}}_0^{\mathrm{sing}}} $

- What is the **Friedman-Miranda criterion**?

    The cusp singularity associated to $ \widehat{D} $ is smoothable iff there exists a type III ACP $ ({\mathcal{X}}_0, D) $.

- What is a **nodal curve**?

    A complete algebraic curve such that every point is either smooth or a node, where $ p $ is a node iff it admits a neighborhood which is complex analytically isomorphic to $ V(xy) $.

- What is the **dual complex** of a type III anticanonical pair?

    For $ ({\mathcal{X}}_0, D) $ an ACP, the triangulation of $ S^2 $ with vertices are the components of $ V_i $, directed edges $ e_{ij} $ for double curves $ D_{ij} $, triangular faces are triiple points $ T_{ijk} $.

- What is a **degeneration**?

    A degeneration of $ X $: a flat proper morphism $ \pi: {\mathcal{X}}\to \mathbb{D} $ of complex analytic spaces such that $ \pi $ is smooth over $ \mathbb{D}^\circ $, the general fibers $ {\mathcal{X}}_t $ are deformation equivalent to $ X $ for all $ t\in \mathbb{D}^\circ $, and the monodromy action on $ H^2({\mathcal{X}}_t; {\mathbf{Z}}) $ is nontrivial and unipotent.

- What is a **maximally unipotent degeneration**?

    Unipotent: $ r-1 $ is nilpotent; for matrices, $ p(t) = (t-1)^n $ for some $ n $, so all eigenvalues are 1. Index of unipotency: the minimal power $ r $ such that $ (M-\operatorname{id})^{r-1}\neq 0 $ but $ (M-\operatorname{id})^r=0 $. Maximal: of maximal possible unipotency index; alternatively the limiting mixed Hodge structure is Hodge-Tate type (extensions of sums of $ {\mathbf{Z}}(n) $). Concretely, the monodromy operator $ T: H^n({\mathcal{X}}_t; {\mathbf{Q}}) {\circlearrowleft} $ satisfies $ (T-I)^{n+1} = 0 $ but $ (T-I)^n\neq 0 $.

- What is a basis triangle?

    A triangle $ \Delta \subseteq {\mathbf{R}}^2 $ such that $ \mathrm{Vert}(\Delta) \subset {\mathbf{Z}}^2 $ and $ \mu(\Delta) = 1/2 $.

- What is a **triangulated integral affine structure with singularities**?

    A real surface with boundary (possibly empty) $ \Sigma_g $ equipped with a triangulation $ T $ such that $ \Sigma_g\setminus\mathrm{Vert}(T) $ admits an atlas $ \left\{{(U_i, \phi_i: U_i\to {\mathbf{R}}^2)}\right\} $ such that $ \phi_i \circ \phi_j^{-1}\in {\operatorname{SL}}_2({\mathbf{Z}})\rtimes{\mathbf{Z}}^2 $ and for each triangle $ \Delta \in T $, the interior $ \Delta^\circ $ admits a chart to a *basis triangle*.

- What is a **nodal trade**?

    Alternative terminology for node smoothing.

- What is the **SYZ conjecture**?

    Gross, 2008: If $ X, X {}^{ \vee } $ are mirror CYs, they admit a common cospanning fibration $ X\to B \leftarrow X {}^{ \vee } $ whose fibers are special Lagrangians and the general fiber is a torus. There should also be a canonical map $ X {}^{ \vee }_t { \, \xrightarrow{\sim}\, }H^1(X_t; {\mathbf{R}}/{\mathbf{Z}}) $ and $ X_t { \, \xrightarrow{\sim}\, }H^1(X {}^{ \vee }_t; {\mathbf{R}}/{\mathbf{Z}}) $ (likely too strong to be true)

- What is the relation to **SYZ mirror symmetry**?

    Generally about boundaries in a CY moduli space, particularly near especially "bad" degenerations: maximally unipotent degenerations (MUD) or large complex structure limits. One can find special Lagrangian tori on CYs near these limit points, and approaching the limit, expect to see a larger portion of the CY filled by tori. Toric degnerations are a special case of MUD. Expect the base $ B $ of a special Lagrangian fibration to be the Gromov-Hausdorff limit of a sequence of CYs near MUD, and GH limit should be the dual intersection complex of the AG degeneration. The base is an affine manifold. If $ \pi:{\mathcal{X}}\to \mathbb{D} $ is such a degeneration of CYs and $ {\mathcal{X}} $ is polarized (equipped with $ {\mathcal{L}}\in \operatorname{Pic}({\mathcal{X}}) $ relatively ample), should exists a dual polarization $ \widehat{{\mathcal{L}}} $ on $ \widehat{{\mathcal{X}}} $.

- What is **charge**?

    $ Q(Y, D):=12+\sum_{i=1}^n\left(d_i-3\right)=12+\sum_{i=1}^n\left(a_i-b_i\right) $ where $ \mathbf{d}=\left(d_1, \ldots, d_n\right)=(a_1+3, \underbrace{2, \ldots, 2}_{b_1}, \ldots, a_k+3, \underbrace{2, \ldots, 2}_{b_k}) $ and $ a_i, b_i \geq 0 $. All toric pairs have charge zero.

- How can one obtain $ \widehat{ \mathbf d} $ for $ \widehat{D} $ from $ \mathbf d $?

    Interchange the $ a_i $ and $ b_i $: $ \widehat{\mathbf{d}}=\left(\widehat{d_1},\cdots, \widehat{d_s} \right)=(b_1+3, \underbrace{2, \ldots, 2}_{a_1}, \ldots, b_k+3, \underbrace{2, \ldots, 2}_{a_k}) $

- Discuss $ Q(D) $ and $ Q(\widehat{D}) $.

    $ Q(D) \coloneqq 12 + \sum (d_i - 3) $ and $ Q(D) + Q(\widehat{D}) = 24 $. This follows from the formula $ Q(D) = 12 + \sum(a_i - b_i) $ and that $ \widehat{D} $ swaps $ a_i $ and $ b_i $.

- Discuss **conservation of charge**.

    For $ ({\mathcal{X}}_0, D) $ a Type III ACP, $ \sum Q(V_i, D_i) = 24 $.

- What is a **nonsingular IAS**?

    When the atlas of charts on an IAS for $ S\setminus\mathrm{Vert}(T) $ extends to $ S $; if not, denote the points where this fails as $ S^{\mathrm{sing}} $.

- What is the **developing map**?

    For $ S $ an IAS with singularities, take contractible opens $ U \subset S\setminus S^{\mathrm{sing}} $ with charts $ \phi_U: U\to {\mathbf{R}}^2 $, uniquely defined up to an element of $ {\operatorname{SL}}_2({\mathbf{Z}})\rtimes{\mathbf{Z}}^2 $, and define $ \Phi: \widetilde{S\setminus S^{\mathrm{sing}}} \to {\mathbf{R}}^2 $ from the universal cover by gluing any charts $ \phi_U, \phi_V $ which agree on $ U\cap V $. Equivalet to the data of a monodromy representation $ \pi_1(S\setminus S^{\mathrm{sing}}) \to {\operatorname{SL}}_2({\mathbf{Z}}) \rtimes{\mathbf{Z}}^2 $.

- How are ACPs related to toric pairs?

    Prop 5.1: every ACP $ (Y, D) $ is a sequence of node smoothings and internal blowups of a toric pair $ (\overline{Y}, \overline{D}) $.

- What is the neative self-intersection of an edge in an IAS?

    For $ e_{ik} $ an edge in $ \Delta \subset T $ for an IAS, letting $ e_{ij}, e_{il} $ be the edges emanating from $ v_i $ clockwise and counterclockwise to $ e_{ik} $, define $ d_{ik} $ to be the "negative self intersection" of $ e_{ik} $ by

    $$d_{ik} e_{ik} = e_{ij} + e_{il}$$

    The data of $ d_{ik} $ for each edge $ e_{ik} $ satisfying $ d_{ik} + d_{ki} = 2 $ for each $ i, k $ uniquely determines a triangulated IAS.

- When does a surface $ {\mathcal{X}}_0 $ smooth to an anticanonical pair in a family $ {\mathcal{X}}\to \mathbb{D} $?

    Being a Type III ACP $ ({\mathcal{X}}_0, D) $ plus $ d{\hbox{-}} $semistability.

- Motivation: singularities.

    - Examples:
    - Blowups:

- Discuss dual intersection graphs and cycles associated to minimal resolutions.

    - For $ \pi: (\tilde X, E)\to (X, 0) $ a minimal (no -1 curves) resolution, define $ \Gamma $ whose vertices are components of $ E $, put $ e_{ij}\coloneqq E_i \cdot E_j $ edges between $ v_i $ and $ v_j $, and attach the number $ e_{ii} \coloneqq-E_i^2 $ to each $ v_i $. Note $ \Gamma $ has no graph-theoretic cycles. Form a matrix $ M_{ij} = e_{ij} $, by a theorem of Grauert-Mumford $ M $ is negative definite.
    - Example: ?
