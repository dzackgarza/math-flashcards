---
title: "Orals::Morphisms"
---

- How does a morphism of rings induce an algebra structure?

    $ f:R\to S $ induces $ S\in   {}_{R}{\mathsf{Mod}} $ via $ r.s \coloneqq f(r)s $.

- What is an **open immersion** of schemes?

    $ f:X\to Y $ inducing $ X\cong U \subseteq Y $ with $ U $ an open subscheme, where $ U\subseteq Y $ is an open scheme iff $ {\left\lvert {U} \right\rvert} \subseteq {\left\lvert {Y} \right\rvert} $ and $ {\mathcal{O}}_U \cong { \left.{{{\mathcal{O}}_Y}} \right|_{{U}} } $.

- What is a **closed immersion** of schemes?

    $ f:X\to Y $ inducing a homeomorphism $ \tilde f: {\left\lvert {X} \right\rvert} \to {\left\lvert {V} \right\rvert} $ for $ {\left\lvert {V} \right\rvert} \subseteq {\left\lvert {Y} \right\rvert} $ a closed subspace of the underlying topological spaces, such that $ f^\sharp: {\mathcal{O}}_Y \twoheadrightarrow f_* {\mathcal{O}}_X $ is a surjective map of sheaves.

    Equivalently, separates points and tangent vectors, i.e. $ p\neq q $ closed points in $ X \implies \exists s\in {\mathfrak{m}}_p {\mathcal{L}}_p \setminus{\mathfrak{m}}_q {\mathcal{L}}_q $, and $ \left\{{s\in V {~\mathrel{\Big\vert}~}s_p\in {\mathfrak{m}}_p {\mathcal{L}}_p}\right\} $ spans $ {\mathfrak{m}}_p {\mathcal{L}}_p/{\mathfrak{m}}_p^2 {\mathcal{L}}_p $, where $ \phi: X\to {\mathbf{P}}^n_{/ {k}} $ corresponds to $ {\mathcal{L}} $ and $ \left\{{s_0, \cdots, s_n}\right\}\in H^0(X; {\mathcal{L}}) $.

- What is a **closed subscheme**?

    An equivalence class of closed immersions, where $ f\sim g $ if they fit into a commuting triangle.

- What is the fiber of a morphism $ f:X\to Y $?

    $ f_y \coloneqq X \underset{\scriptscriptstyle {Y} }{\times} \operatorname{Spec}\kappa(y) $

- What is a **smooth morphism**?

    Locally of finite presentation, flat, and regular geometric fibers. (LFP: open cover where $ R\to A $ is fp, so $ \exists\, R[x_1, \cdots, x_n] \twoheadrightarrow A $).

    Smooth implies regular.

    For ring maps: $ f:R\to A $ of finite presentation with $ \tau_{\leq 1}{\mathbb{L}}_{A/R} \cong M[0] $ with $ M\in   {}_{A}{\mathsf{Mod}} $ some finite projective (i.e. the naive cotangent complex is quasi-isomorphic to a projective module in degree zero). For schemes: smooth at $ x \iff \exists U = \operatorname{Spec}A \ni x $ and $ V = \operatorname{Spec}R \supseteq f(U) $ such that the induced ring map $ R\to A $ is a smooth ring map.

    Sufficient condition: flat, locally of finite presentation, smooth fibers (i.e. for all $ a\in A $, the fiber $ R \underset{\scriptscriptstyle {A} }{\times}\kappa(a) $ is a smooth scheme over $ \kappa(a) $).

    Equivalently, $ \Omega_{R/A} $ is locally free of finite rank equal to $ \operatorname{reldim}R/A $ (roughly: $ \dim f^{-1}(a) $).

- What is a smooth morphism of relative dimension $ n $?

    $ f: X\to Y $ flat with $ \dim C_X = \dim C_Y + n $ for any irreducible components $ C_Y \subseteq f(C_X) $, and $ \dim_{\kappa(x)}(\Omega_{X/k}\otimes\kappa(x)) = n $.

    Condition 2 means every irreducible component of every fiber $ X_y $ of $ f $ has dimension $ n $.

    For $ X $ integral, flat + irreducible component dimension condition + $ \Omega_{X/Y} $ is locally free of rank $ n $.

    Closed under base change, composition, fiber products.

- How is smoothness related to regularity?

    Over $ k = { \overline{k} } $, $ X $ is smooth of relative dimension $ n $ over $ \operatorname{Spec}k $ $ \iff X $ is regular of dimension $ n $.

- What is generic smoothness?

    For $ f:X\to Y\in {\mathsf{Var}}_{/ {k}}, \operatorname{ch}k = 0 $ with $ X $ smooth, then there is a nonempty open $ V\subseteq Y $ such that $ { \left.{{f}} \right|_{{f^{-1}(V)}} } $ is a smooth morphism.

- Give an example a morphism that is not smooth.

    Let $ \operatorname{ch}k = p, k={ \overline{k} } $ and take the Frobenius morphism $ f:X\to Y $ to $ X=Y={\mathbf{P}}^n_{/ {k}} $.

    Since $ d(t^p)=0 $, the map $ f^*\Omega_{Y/k}\to \Omega_{X/k} $ is zero and $ \Omega_{X/Y} \cong \Omega_{X/k} $ is locally free of rank 1 but but $ \operatorname{reldim}f = 0 $, so $ f $ is nowhere smooth.

- What is a consequence of smoothness?

    Smooth morphisms are flat, and smooth fibers implies this is a flat family of smooth schemes.

- What is a **proper morphism**?

    Separated, finite type, and universally closed.

    Equivalently, use the valuative criterion ($ =1 $ lift).

- How is it related to **completeness**?

    A variety $ X $ is complete if $ X\to \operatorname{Spec}k $ is proper, i.e. a proper variety (integral separated scheme of finite type over a field) is complete.

- How is this related to Hausdorff + compactness properties?

    $ X/{\mathbf{C}} $ is complete iff $ X $ is compact in the analytic topology

- What is an **etale** morphism $ f:X\to Y\in {\mathsf{Sch}}_{/ {k}} $?

    Fully general: flat, finite type, unramified.

    Smooth of relative dimension 0.

    Flat and $ \Omega_{X/ Y} = 0 $.

    For varieties: flat and unramified.

- What is an **unramified** morphism?

    For every $ x\in X $, $ f^\sharp({\mathfrak{m}}_{f(x)}) \cdot {\mathcal{O}}_{X, x} \cong{\mathfrak{m}}_x $ where $ f^\sharp: {\mathcal{O}}_{Y, f(x)}\to {\mathcal{O}}_{X, x} $, and $ \kappa(x)/\kappa(y) $ is a separable algebraic extension.

    Equivalently, $ f:X\to Y $ with $ \Omega_{X/Y} = 0 $.

    Equivalently, $ f $ locally of finite presentation and the diagonal is an open immersion.

    For curves: $ \exists e_p\in {\mathbf{Z}}_{\geq 0} $ such that $ f^\sharp({\mathfrak{m}}_{f(p)}) {\mathcal{O}}_{X, x} = {\mathfrak{m}}_{x}^{e_p} $, and unramified iff $ e_p = 1 $ for all $ p\in X $.

    Flat + unramified = etale.

- What is a **flat** morphism?

    For projective varieties: the induced maps on stalks are flat ring maps.

    $ f: X\to S $ is flat at $ x $ iff $ {\mathcal{O}}_{X, x} \in   {}_{{\mathcal{O}}_{S, f(x) } }{\mathsf{Mod}}^\flat $ (i.e. the module structure induced by $ f $ yields a flat module.)

    Hartshorne's definition: for $ f:X\to Y $ and $ {\mathcal{F}}\in  {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $, $ {\mathcal{F}} $ is flat over $ Y $ at $ x\in X $ if $ {\mathcal{F}}_x \in   {}_{{\mathcal{O}}_{Y, f(x)}}{\mathsf{Mod}}^\flat $; flat if flat at every $ x\in S $, and $ X $ is flat over $ Y $ if $ {\mathcal{F}}\coloneqq{\mathcal{O}}_X $ is flat.

    $ f\in \mathsf{CRing}(A, B) $ is a flat map iff $ B\in   {}_{A}{\mathsf{Mod}}^\flat $, and a morphism $ f\in {\mathsf{Sch}}(X, Y) $ is flat iff flat on local rings, i.e. $ f_x: {\mathcal{O}}_{Y, f(x)}\to {\mathcal{O}}_{X, x} $ is flat.

- What are some consequences of flatness?

    Numerical invariants remain constant in flat families, e.g. the dimensions of fibers and their hilbert polynomials.

    Defining $ \dim_x X \coloneqq\dim {\mathcal{O}}_{X, x} $, if $ f:X\to Y $ is flat then $ \dim_x X_{f(x)} = \dim_x X - \dim_{f(x)} Y $.

    If $ B $ is smooth 1-dimensional affine, $ X\to B $ is a family, and $ 0\in B $ is a closed point, $ \lim_{b\to 0} X_b = X_0 $ where $ \lim_{b\to 0} X_b \coloneqq\overline{X_0} $, the fiber over $ 0 $.

- Given an example of a non-flat morphism.

    $ \operatorname{Bl}_0 {\mathbf{A}}^2 \xrightarrow{\pi} {\mathbf{A}}^2 $, since $ {\sharp}\pi^{-1}(p) = 1 $ for all $ p\neq 0 $ and $ \pi^{-1}(0)\cong {\mathbf{P}}^1 $, contradicting equidimensionality.

    Take a nodal curve $ X $ and $ f:\tilde X\to X $ its normalization -- if this were flat, $ f_* {\mathcal{O}}_{\tilde X} $ would be a flat sheaf of $ {\mathcal{O}}_X{\hbox{-}} $modules, which is coherent and thus locally free, and rank 1 and thus univertible; however the node $ q $ has two preimages $ p_1, p_2 $, so $ (f_* {\mathcal{O}}_{\tilde X})_q $ needs two generators as an $ {\mathcal{O}}_X{\hbox{-}} $module.

    Any nontrivial normalization.

    A ramified map of curves:

- What are some examples of flat morphisms?

    Smooth morphisms, elliptic fibrations.

    Miracle flatness: any proper morphism between smooth varieties with equidimensional fibers.

- What is a **finite ring morphism**?

    A finite ring morphism $ f:R\to A $ is one that makes $ A\in   {}_{R}{\mathsf{Mod}}^{\mathrm{fg}} $.

- What is a **finite morphism**?

    Hartshorne: $ f:X\to Y $ where $ \operatorname{Spec}B_i\rightrightarrows Y $ with $ \operatorname{Spec}A_i \coloneqq f^{-1}(B_i) $ with each $ A_i\in { {}_{B_i}  \mathsf{Alg}} $ such that $ A_i \in   {}_{B_i}{\mathsf{Mod}}^{\mathrm{fg}} $.

    Note that being fg as a **module** is **stronger** than being fg as an **algebra**: $ k[x] \in  {}_{k}  \mathsf{Alg} $ has one algebra generator but infinite rank in $   {}_{k}{\mathsf{Mod}} $.

    Thus **finite** implies **finite type** but not conversely.

    Proper and locally quasifinite.

    Equivalently, admits an open cover where it restricts to finite ring morphisms.

- What is a consequence of a morphism being finite?

    Closed with finite fibers.

    Finite implies projective, and finite fibers + projective implies proper (not conversely!)

- What is a sufficient criterion for a morphism to be finite?

    Proper, locally of finite presentation, finite fibers.

    For locally Noetherian schemes, finite $ \iff $ proper + finite fibers.

- Give an example of a non-finite morphism.

    The hyperbola projection $ V(xy-c)\to {\mathbf{G}}_m $, which has finite fibers but is not finite.

- What is a **quasifinite ring morphism**?

    **Discrete finite fibers**: for $ R\to S $ *finite type* and $ {\mathfrak{q}}\in \operatorname{Spec}S $, the point in the fiber $ \overline{{\mathfrak{q}}}\in F \coloneqq\operatorname{Spec}(S\otimes_R \kappa({\mathfrak{p}})) $ is isolated, i.e. the fiber above that point is zero-dimensional.

- What is a **quasifinite** morphism?

    Locally quasifinite and quasicompact. Equivalently, covered my opens where the induced ring maps are finite type and quasifinite at the prime $ {\mathfrak{q}} $ associated to $ x\in X $.

- What is a consequence of a morphism of affine schemes being finite?

    If $ R\to A $ is finite the $ \operatorname{Spec}A\to \operatorname{Spec}R $ has finite fibers.

- What is a **finite type morphism**?

    Locally of finite type and quasicompact.

    Equivalently, on an open cover, inducing finitely generated *algebras* and covered by finitely many: $ f:X\to Y $ where $ \operatorname{Spec}B_i\rightrightarrows Y $ with $ \operatorname{Spec}A_i \coloneqq f^{-1}(B_i) $ with each $ A_i\in { {}_{B_i}  \mathsf{Alg}}^{\mathrm{fg}} $.

    Note that being fg as a module is **stronger** than being fg as an algebra: $ k[x] \in  {}_{k}  \mathsf{Alg} $ has one algebra generator but infinite rank in $   {}_{k}{\mathsf{Mod}} $. Thus finite implies finite type but not conversely.

- What is a morphism locally of finite type?

    $ f:X\to Y $ with open covers $ \operatorname{Spec}B_i, U_i\coloneqq f^{-1}(\operatorname{Spec}B_i) $ where $ \operatorname{Spec}A_{ij}\rightrightarrows U_i $ making $ A_{ij}\in { {}_{B_i}  \mathsf{Alg}}^{\mathrm{fg}} $.

    Additionally **is of finite type** if each $ U_i $ can be covered by finitely many $ A_{ij} $.

    A ring map $ R\to A $ is of finite type $ A $ admits a surjection from $ R[x_1, \cdots, x_n] $ for some $ n $. Equivalently, $ A\in  {}_{R}  \mathsf{Alg}^{\mathrm{fg}} $. Being **locally of finite type** means every $ x $ admitting a neighborhood $ \operatorname{Spec}A_i\ni x $ where $ f(\operatorname{Spec}A_i) \subseteq \operatorname{Spec}R_i\ni f(x) $ so that the induced ring map $ R\to A $ is finite type.

- What is a finitely presented morphism?

    Locally of finite presentation, quasicompact, quasiseparated.

- What is a locally finitely presented morphism?

    On open covers, the induced rings maps $ R_i\to A_i $ are finite presentation, i.e. $ R_i[x_1,\cdots, x_n] \twoheadrightarrow A_i $ with fg kernel for some $ n $.

- A universally closed morphism?

    $ f:X\to Y $ closed and every base change $ Y'\to Y \leadsto X \underset{\scriptscriptstyle {Y} }{\times} Y' \to Y' $ is closed, where maps are closed when images of closed sets are closed.

- What is an example of a closed morphism?

    Any finite map of rings, the structure map of any proper scheme.

- What is an example of a non-closed morphism?

    Use that $ {\mathbf{A}}^n $ is not proper: $ X \underset{\scriptscriptstyle {k} }{\times} X \to X $ is not closed for $ X\coloneqq{\mathbf{A}}^1 $ since it is the coordinate projection, and $ V(xy-c) \mapsto {\mathbf{G}}_m $ which is not closed.

- What is a a **projective morphism**?

    $ f:X\to Y $ which factors as $ X\hookrightarrow{\mathbf{P}}^N_{/ {Y}} \twoheadrightarrow Y $, a closed immersion followed by the natural projection, where $ {\mathbf{P}}^N_{/ {Y}} \coloneqq{\mathbf{P}}^N_{/ {{\mathbf{Z}}}} \underset{\scriptscriptstyle {\operatorname{Spec}{\mathbf{Z}}} }{\times} Y $.

- What is a quasiprojective morphism?

    $ f:X\to Y $ which factors as $ X\hookrightarrow X'\to Y' $, a closed immersion followed by a projective morphism.

- Give examples and counterexamples of projective morphisms.

    For $ A $ any ring and $ S $ any graded ring with $ S_0 = A $, $ \mathop{\mathrm{Proj}}S\to \operatorname{Spec}A $ is projective.

- Give some consequences of projective morphisms.

    For Noetherian schemes, projective $ \implies $ proper.

- What is a faithfully flat morphism?

    Flat and surjective.

- What is a rational morphism?

    An equivalence class of pairs $ (U, { \left.{{f}} \right|_{{U}} }) $ where $ U\subseteq X $ is open dense and $ { \left.{{f}} \right|_{{U}} }: U\to Y $ is a morphism, which are identified if they coincide on intersections.

- What is a birational map?

    A rational map with a rational inverse.

- What is the degree of a morphism?

    $ f:X\to S $ with $ f_*{\mathcal{O}}_X\in   {}_{{\mathcal{O}}_s}{\mathsf{Mod}} $ finite and locally free, take its degree as a Coherent sheaf, where $ \deg {\mathcal{F}}\coloneqq\deg \operatorname{det}{\mathcal{F}} $ since $ \operatorname{det}{\mathcal{F}}\in \operatorname{Pic}(X) $, where the degree is the degree of the associated divisor.

- What is a **separated morphism**?

    A morphism $ f:X\to S $ of schemes is **separated** iff $ \Delta_{X/S}: X\to X \underset{\scriptscriptstyle {S} }{\times} X $ is a **closed immersion**.

- How is this separatedness related to Hausdorffness?

    $ X\in {\mathsf{Top}} $ is **Hausdorff** iff the diagonal $ \Delta \subseteq X\times X $ is a closed subset.

- What is a quasiseparated morphism?

    - $ f:X\to S $ is quasiseparated iff the diagonal is quasicompact.

- What is qcqs? (Quasi-compact and quaiseparated)

    Quasicompact: inverse images of quasicompact sets are quasicompact. Quasiseparated: the diagonal is quasicompact.

- What is an affine morphism?

    Inverse images of affines are affine.

- What are some examples of affine morphisms?

    Any morphism between affine schemes, closed immersions.

- What are some consequences of a morphism being affine?

    Separated and quasicompact.

- What is a quasiaffine morphism?

    Inverse images of quasiaffines are quasiaffine.

- What is a quasiaffine scheme?

    Quasicompact and isomorphic to an open subscheme of an affine scheme.

- What is a normal morphism?

    $ f:X\to Y $ with $ f $ flat at $ x $ and the fiber $ X_{f(x)} $ *geometrically normal*, i.e. for every field extension $ L/k $ and every $ \ell $ over $ x $ in $ X \underset{\scriptscriptstyle {k} }{\times} L $ has a normal local ring, i.e. integrally closed in its field of fractions.

- What is a regular morphism?

    Flat at $ x $ and *geometrically regular* at $ x $, i.e. for every fg field extension $ L/k $ and $ \ell $ over $ x $ in $ X \underset{\scriptscriptstyle {k} }{\times} L $, the local ring at $ \ell $ is regular, i.e. the minimal number of generators of its maximal ideal equals its Krull dimension.

- What is the cotangent complex?

    The nonabelian left-derived functor $ {\mathbb{L}}_{{-}/A}: \mathsf{CRing}_A\to \mathbf{D}{  {}_{A}{\mathsf{Mod}}} $ of the functor $ \Omega^1_{{-}/A}[0] $

- When is a morphism of schemes an immersion?

    $ \iota: X\to Z $ making $ X $ isomorphic to an open subscheme *of a closed subscheme* of $ Z $.

- Name some properties preserved by base change.

    Open/closed immersions, affine, finite, integral, locally of ft, qc, ft, quasi-finite, flat, surjective.
