---
title: "Orals::Morphisms"
---

::: {.front card-id="card-63efc03dbb2b7a94"}
How does a morphism of rings induce an algebra structure?
:::

::: {.back card-id="card-63efc03dbb2b7a94"}
$ f:R\to S $ induces $ S\in   {}_{R}{\mathsf{Mod}} $ via $ r.s \coloneqq f(r)s $.
:::

::: {.front card-id="card-7f48b0ac525a085c"}
What is an **open immersion** of schemes?
:::

::: {.back card-id="card-7f48b0ac525a085c"}
$ f:X\to Y $ inducing $ X\cong U \subseteq Y $ with $ U $ an open subscheme, where $ U\subseteq Y $ is an open scheme iff $ {\left\lvert {U} \right\rvert} \subseteq {\left\lvert {Y} \right\rvert} $ and $ {\mathcal{O}}_U \cong { \left.{{{\mathcal{O}}_Y}} \right|_{{U}} } $.
:::

::: {.front card-id="card-86f3fc66ea0fc489"}
What is a **closed immersion** of schemes?
:::

::: {.back card-id="card-86f3fc66ea0fc489"}
$ f:X\to Y $ inducing a homeomorphism $ \tilde f: {\left\lvert {X} \right\rvert} \to {\left\lvert {V} \right\rvert} $ for $ {\left\lvert {V} \right\rvert} \subseteq {\left\lvert {Y} \right\rvert} $ a closed subspace of the underlying topological spaces, such that $ f^\sharp: {\mathcal{O}}_Y \twoheadrightarrow f_* {\mathcal{O}}_X $ is a surjective map of sheaves.

Equivalently, separates points and tangent vectors, i.e. $ p\neq q $ closed points in $ X \implies \exists s\in {\mathfrak{m}}_p {\mathcal{L}}_p \setminus{\mathfrak{m}}_q {\mathcal{L}}_q $, and $ \left\{{s\in V {~\mathrel{\Big\vert}~}s_p\in {\mathfrak{m}}_p {\mathcal{L}}_p}\right\} $ spans $ {\mathfrak{m}}_p {\mathcal{L}}_p/{\mathfrak{m}}_p^2 {\mathcal{L}}_p $, where $ \phi: X\to {\mathbf{P}}^n_{/ {k}} $ corresponds to $ {\mathcal{L}} $ and $ \left\{{s_0, \cdots, s_n}\right\}\in H^0(X; {\mathcal{L}}) $.
:::

::: {.front card-id="card-fa8d17dce5d4f805"}
What is a **closed subscheme**?
:::

::: {.back card-id="card-fa8d17dce5d4f805"}
An equivalence class of closed immersions, where $ f\sim g $ if they fit into a commuting triangle.
:::

::: {.front card-id="card-478d4dd2b52b290a"}
What is the fiber of a morphism $ f:X\to Y $?
:::

::: {.back card-id="card-478d4dd2b52b290a"}
$ f_y \coloneqq X \underset{\scriptscriptstyle {Y} }{\times} \operatorname{Spec}\kappa(y) $
:::

::: {.front card-id="card-8313983abf999469"}
What is a **smooth morphism**?
:::

::: {.back card-id="card-8313983abf999469"}
Locally of finite presentation, flat, and regular geometric fibers. (LFP: open cover where $ R\to A $ is fp, so $ \exists\, R[x_1, \cdots, x_n] \twoheadrightarrow A $).

Smooth implies regular.

For ring maps: $ f:R\to A $ of finite presentation with $ \tau_{\leq 1}{\mathbb{L}}_{A/R} \cong M[0] $ with $ M\in   {}_{A}{\mathsf{Mod}} $ some finite projective (i.e. the naive cotangent complex is quasi-isomorphic to a projective module in degree zero). For schemes: smooth at $ x \iff \exists U = \operatorname{Spec}A \ni x $ and $ V = \operatorname{Spec}R \supseteq f(U) $ such that the induced ring map $ R\to A $ is a smooth ring map.

Sufficient condition: flat, locally of finite presentation, smooth fibers (i.e. for all $ a\in A $, the fiber $ R \underset{\scriptscriptstyle {A} }{\times}\kappa(a) $ is a smooth scheme over $ \kappa(a) $).

Equivalently, $ \Omega_{R/A} $ is locally free of finite rank equal to $ \operatorname{reldim}R/A $ (roughly: $ \dim f^{-1}(a) $).
:::

::: {.front card-id="card-e504a4da2d4624f3"}
What is a smooth morphism of relative dimension $ n $?
:::

::: {.back card-id="card-e504a4da2d4624f3"}
$ f: X\to Y $ flat with $ \dim C_X = \dim C_Y + n $ for any irreducible components $ C_Y \subseteq f(C_X) $, and $ \dim_{\kappa(x)}(\Omega_{X/k}\otimes\kappa(x)) = n $.

Condition 2 means every irreducible component of every fiber $ X_y $ of $ f $ has dimension $ n $.

For $ X $ integral, flat + irreducible component dimension condition + $ \Omega_{X/Y} $ is locally free of rank $ n $.

Closed under base change, composition, fiber products.
:::

::: {.front card-id="card-c018f8b2b38ac42f"}
How is smoothness related to regularity?
:::

::: {.back card-id="card-c018f8b2b38ac42f"}
Over $ k = { \overline{k} } $, $ X $ is smooth of relative dimension $ n $ over $ \operatorname{Spec}k $ $ \iff X $ is regular of dimension $ n $.
:::

::: {.front card-id="card-4956b7d16253f682"}
What is generic smoothness?
:::

::: {.back card-id="card-4956b7d16253f682"}
For $ f:X\to Y\in {\mathsf{Var}}_{/ {k}}, \operatorname{ch}k = 0 $ with $ X $ smooth, then there is a nonempty open $ V\subseteq Y $ such that $ { \left.{{f}} \right|_{{f^{-1}(V)}} } $ is a smooth morphism.
:::

::: {.front card-id="card-5706d972b05f5073"}
Give an example a morphism that is not smooth.
:::

::: {.back card-id="card-5706d972b05f5073"}
Let $ \operatorname{ch}k = p, k={ \overline{k} } $ and take the Frobenius morphism $ f:X\to Y $ to $ X=Y={\mathbf{P}}^n_{/ {k}} $.

Since $ d(t^p)=0 $, the map $ f^*\Omega_{Y/k}\to \Omega_{X/k} $ is zero and $ \Omega_{X/Y} \cong \Omega_{X/k} $ is locally free of rank 1 but $ \operatorname{reldim}f = 0 $, so $ f $ is nowhere smooth.
:::

::: {.front card-id="card-7cf150912ca6e3c0"}
What is a consequence of smoothness?
:::

::: {.back card-id="card-7cf150912ca6e3c0"}
Smooth morphisms are flat, and smooth fibers implies this is a flat family of smooth schemes.
:::

::: {.front card-id="card-525d10c2757e41de"}
What is a **proper morphism**?
:::

::: {.back card-id="card-525d10c2757e41de"}
Separated, finite type, and universally closed.

Equivalently, use the valuative criterion ($ =1 $ lift).
:::

::: {.front card-id="card-07e3a111761ae76e"}
How is it related to **completeness**?
:::

::: {.back card-id="card-07e3a111761ae76e"}
A variety $ X $ is complete if $ X\to \operatorname{Spec}k $ is proper, i.e. a proper variety (integral separated scheme of finite type over a field) is complete.
:::

::: {.front card-id="card-40289dd013dd96ec"}
How is this related to Hausdorff + compactness properties?
:::

::: {.back card-id="card-40289dd013dd96ec"}
$ X/{\mathbf{C}} $ is complete iff $ X $ is compact in the analytic topology
:::

::: {.front card-id="card-a484edc8e6016938"}
What is an **etale** morphism $ f:X\to Y\in {\mathsf{Sch}}_{/ {k}} $?
:::

::: {.back card-id="card-a484edc8e6016938"}
Fully general: flat, finite type, unramified.

Smooth of relative dimension 0.

Flat and $ \Omega_{X/ Y} = 0 $.

For varieties: flat and unramified.
:::

::: {.front card-id="card-e9ced257a3fb0b70"}
What is an **unramified** morphism?
:::

::: {.back card-id="card-e9ced257a3fb0b70"}
For every $ x\in X $, $ f^\sharp({\mathfrak{m}}_{f(x)}) \cdot {\mathcal{O}}_{X, x} \cong{\mathfrak{m}}_x $ where $ f^\sharp: {\mathcal{O}}_{Y, f(x)}\to {\mathcal{O}}_{X, x} $, and $ \kappa(x)/\kappa(y) $ is a separable algebraic extension.

Equivalently, $ f:X\to Y $ with $ \Omega_{X/Y} = 0 $.

Equivalently, $ f $ locally of finite presentation and the diagonal is an open immersion.

For curves: $ \exists e_p\in {\mathbf{Z}}_{\geq 0} $ such that $ f^\sharp({\mathfrak{m}}_{f(p)}) {\mathcal{O}}_{X, x} = {\mathfrak{m}}_{x}^{e_p} $, and unramified iff $ e_p = 1 $ for all $ p\in X $.

Flat + unramified = etale.
:::

::: {.front card-id="card-b00d12404bc086fb"}
What is a **flat** morphism?
:::

::: {.back card-id="card-b00d12404bc086fb"}
For projective varieties: the induced maps on stalks are flat ring maps.

$ f: X\to S $ is flat at $ x $ iff $ {\mathcal{O}}_{X, x} \in   {}_{{\mathcal{O}}_{S, f(x) } }{\mathsf{Mod}}^\flat $ (i.e. the module structure induced by $ f $ yields a flat module.)

Hartshorne's definition: for $ f:X\to Y $ and $ {\mathcal{F}}\in  {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $, $ {\mathcal{F}} $ is flat over $ Y $ at $ x\in X $ if $ {\mathcal{F}}_x \in   {}_{{\mathcal{O}}_{Y, f(x)}}{\mathsf{Mod}}^\flat $; flat if flat at every $ x\in S $, and $ X $ is flat over $ Y $ if $ {\mathcal{F}}\coloneqq{\mathcal{O}}_X $ is flat.

$ f\in \mathsf{CRing}(A, B) $ is a flat map iff $ B\in   {}_{A}{\mathsf{Mod}}^\flat $, and a morphism $ f\in {\mathsf{Sch}}(X, Y) $ is flat iff flat on local rings, i.e. $ f_x: {\mathcal{O}}_{Y, f(x)}\to {\mathcal{O}}_{X, x} $ is flat.
:::

::: {.front card-id="card-da88a614473cf4db"}
What are some consequences of flatness?
:::

::: {.back card-id="card-da88a614473cf4db"}
Numerical invariants remain constant in flat families, e.g. the dimensions of fibers and their hilbert polynomials.

Defining $ \dim_x X \coloneqq\dim {\mathcal{O}}_{X, x} $, if $ f:X\to Y $ is flat then $ \dim_x X_{f(x)} = \dim_x X - \dim_{f(x)} Y $.

If $ B $ is smooth 1-dimensional affine, $ X\to B $ is a family, and $ 0\in B $ is a closed point, $ \lim_{b\to 0} X_b = X_0 $ where $ \lim_{b\to 0} X_b \coloneqq\overline{X_0} $, the fiber over $ 0 $.
:::

::: {.front card-id="card-7eb3cab7d1016342"}
Given an example of a non-flat morphism.
:::

::: {.back card-id="card-7eb3cab7d1016342"}
$ \operatorname{Bl}_0 {\mathbf{A}}^2 \xrightarrow{\pi} {\mathbf{A}}^2 $, since $ {\sharp}\pi^{-1}(p) = 1 $ for all $ p\neq 0 $ and $ \pi^{-1}(0)\cong {\mathbf{P}}^1 $, contradicting equidimensionality.

Take a nodal curve $ X $ and $ f:\tilde X\to X $ its normalization -- if this were flat, $ f_* {\mathcal{O}}_{\tilde X} $ would be a flat sheaf of $ {\mathcal{O}}_X{\hbox{-}} $modules, which is coherent and thus locally free, and rank 1 and thus invertible; however the node $ q $ has two preimages $ p_1, p_2 $, so $ (f_* {\mathcal{O}}_{\tilde X})_q $ needs two generators as an $ {\mathcal{O}}_X{\hbox{-}} $module.

Any nontrivial normalization.

A ramified map of curves:
:::

::: {.front card-id="card-9b485a1d353a0607"}
What are some examples of flat morphisms?
:::

::: {.back card-id="card-9b485a1d353a0607"}
Smooth morphisms, elliptic fibrations.

Miracle flatness: any proper morphism between smooth varieties with equidimensional fibers.
:::

::: {.front card-id="card-872922cda061b5c3"}
What is a **finite ring morphism**?
:::

::: {.back card-id="card-872922cda061b5c3"}
A finite ring morphism $ f:R\to A $ is one that makes $ A\in   {}_{R}{\mathsf{Mod}}^{\mathrm{fg}} $.
:::

::: {.front card-id="card-50c3a5b5a43dbd56"}
What is a **finite morphism**?
:::

::: {.back card-id="card-50c3a5b5a43dbd56"}
Hartshorne: $ f:X\to Y $ where $ \operatorname{Spec}B_i\rightrightarrows Y $ with $ \operatorname{Spec}A_i \coloneqq f^{-1}(B_i) $ with each $ A_i\in { {}_{B_i}  \mathsf{Alg}} $ such that $ A_i \in   {}_{B_i}{\mathsf{Mod}}^{\mathrm{fg}} $.

Note that being fg as a **module** is **stronger** than being fg as an **algebra**: $ k[x] \in  {}_{k}  \mathsf{Alg} $ has one algebra generator but infinite rank in $   {}_{k}{\mathsf{Mod}} $.

Thus **finite** implies **finite type** but not conversely.

Proper and locally quasifinite.

Equivalently, admits an open cover where it restricts to finite ring morphisms.
:::

::: {.front card-id="card-a33f381a0acf3855"}
What is a consequence of a morphism being finite?
:::

::: {.back card-id="card-a33f381a0acf3855"}
Closed with finite fibers.

Finite implies projective, and finite fibers + projective implies proper (not conversely!)
:::

::: {.front card-id="card-b43d97bd1c06ebbc"}
What is a sufficient criterion for a morphism to be finite?
:::

::: {.back card-id="card-b43d97bd1c06ebbc"}
Proper, locally of finite presentation, finite fibers.

For locally Noetherian schemes, finite $ \iff $ proper + finite fibers.
:::

::: {.front card-id="card-f6ad9d9bdd3e651a"}
Give an example of a non-finite morphism.
:::

::: {.back card-id="card-f6ad9d9bdd3e651a"}
The hyperbola projection $ V(xy-c)\to {\mathbf{G}}_m $, which has finite fibers but is not finite.
:::

::: {.front card-id="card-80a1e9e416914d0f"}
What is a **quasifinite ring morphism**?
:::

::: {.back card-id="card-80a1e9e416914d0f"}
**Discrete finite fibers**: for $ R\to S $ *finite type* and $ {\mathfrak{q}}\in \operatorname{Spec}S $, the point in the fiber $ \overline{{\mathfrak{q}}}\in F \coloneqq\operatorname{Spec}(S\otimes_R \kappa({\mathfrak{p}})) $ is isolated, i.e. the fiber above that point is zero-dimensional.
:::

::: {.front card-id="card-63642f240775d774"}
What is a **quasifinite** morphism?
:::

::: {.back card-id="card-63642f240775d774"}
Locally quasifinite and quasicompact. Equivalently, covered my opens where the induced ring maps are finite type and quasifinite at the prime $ {\mathfrak{q}} $ associated to $ x\in X $.
:::

::: {.front card-id="card-deaa6d5ac072e40a"}
What is a consequence of a morphism of affine schemes being finite?
:::

::: {.back card-id="card-deaa6d5ac072e40a"}
If $ R\to A $ is finite the $ \operatorname{Spec}A\to \operatorname{Spec}R $ has finite fibers.
:::

::: {.front card-id="card-08935d3d51a49bc7"}
What is a **finite type morphism**?
:::

::: {.back card-id="card-08935d3d51a49bc7"}
Locally of finite type and quasicompact.

Equivalently, on an open cover, inducing finitely generated *algebras* and covered by finitely many: $ f:X\to Y $ where $ \operatorname{Spec}B_i\rightrightarrows Y $ with $ \operatorname{Spec}A_i \coloneqq f^{-1}(B_i) $ with each $ A_i\in { {}_{B_i}  \mathsf{Alg}}^{\mathrm{fg}} $.

Note that being fg as a module is **stronger** than being fg as an algebra: $ k[x] \in  {}_{k}  \mathsf{Alg} $ has one algebra generator but infinite rank in $   {}_{k}{\mathsf{Mod}} $. Thus finite implies finite type but not conversely.
:::

::: {.front card-id="card-50d5401e86f0de21"}
What is a morphism locally of finite type?
:::

::: {.back card-id="card-50d5401e86f0de21"}
$ f:X\to Y $ with open covers $ \operatorname{Spec}B_i, U_i\coloneqq f^{-1}(\operatorname{Spec}B_i) $ where $ \operatorname{Spec}A_{ij}\rightrightarrows U_i $ making $ A_{ij}\in { {}_{B_i}  \mathsf{Alg}}^{\mathrm{fg}} $.

Additionally **is of finite type** if each $ U_i $ can be covered by finitely many $ A_{ij} $.

A ring map $ R\to A $ is of finite type $ A $ admits a surjection from $ R[x_1, \cdots, x_n] $ for some $ n $. Equivalently, $ A\in  {}_{R}  \mathsf{Alg}^{\mathrm{fg}} $. Being **locally of finite type** means every $ x $ admitting a neighborhood $ \operatorname{Spec}A_i\ni x $ where $ f(\operatorname{Spec}A_i) \subseteq \operatorname{Spec}R_i\ni f(x) $ so that the induced ring map $ R\to A $ is finite type.
:::

::: {.front card-id="card-c35dccf24f080a71"}
What is a finitely presented morphism?
:::

::: {.back card-id="card-c35dccf24f080a71"}
Locally of finite presentation, quasicompact, quasiseparated.
:::

::: {.front card-id="card-67acbfbbf098e7b7"}
What is a locally finitely presented morphism?
:::

::: {.back card-id="card-67acbfbbf098e7b7"}
On open covers, the induced rings maps $ R_i\to A_i $ are finite presentation, i.e. $ R_i[x_1,\cdots, x_n] \twoheadrightarrow A_i $ with fg kernel for some $ n $.
:::

::: {.front card-id="card-9b5950fc2403c0f6"}
A universally closed morphism?
:::

::: {.back card-id="card-9b5950fc2403c0f6"}
$ f:X\to Y $ closed and every base change $ Y'\to Y \leadsto X \underset{\scriptscriptstyle {Y} }{\times} Y' \to Y' $ is closed, where maps are closed when images of closed sets are closed.
:::

::: {.front card-id="card-76e5dd778285e576"}
What is an example of a closed morphism?
:::

::: {.back card-id="card-76e5dd778285e576"}
Any finite map of rings, the structure map of any proper scheme.
:::

::: {.front card-id="card-fa8cf4bfe010b0a3"}
What is an example of a non-closed morphism?
:::

::: {.back card-id="card-fa8cf4bfe010b0a3"}
Use that $ {\mathbf{A}}^n $ is not proper: $ X \underset{\scriptscriptstyle {k} }{\times} X \to X $ is not closed for $ X\coloneqq{\mathbf{A}}^1 $ since it is the coordinate projection, and $ V(xy-c) \mapsto {\mathbf{G}}_m $ which is not closed.
:::

::: {.front card-id="card-31a64a619e91d37a"}
What is a **projective morphism**?
:::

::: {.back card-id="card-31a64a619e91d37a"}
$ f:X\to Y $ which factors as $ X\hookrightarrow{\mathbf{P}}^N_{/ {Y}} \twoheadrightarrow Y $, a closed immersion followed by the natural projection, where $ {\mathbf{P}}^N_{/ {Y}} \coloneqq{\mathbf{P}}^N_{/ {{\mathbf{Z}}}} \underset{\scriptscriptstyle {\operatorname{Spec}{\mathbf{Z}}} }{\times} Y $.
:::

::: {.front card-id="card-9f9cd83a2a11e95a"}
What is a quasiprojective morphism?
:::

::: {.back card-id="card-9f9cd83a2a11e95a"}
$ f:X\to Y $ which factors as $ X\hookrightarrow X'\to Y' $, a closed immersion followed by a projective morphism.
:::

::: {.front card-id="card-0defb0831c46c847"}
Give examples and counterexamples of projective morphisms.
:::

::: {.back card-id="card-0defb0831c46c847"}
For $ A $ any ring and $ S $ any graded ring with $ S_0 = A $, $ \mathop{\mathrm{Proj}}S\to \operatorname{Spec}A $ is projective.
:::

::: {.front card-id="card-de0aa28404f698be"}
Give some consequences of projective morphisms.
:::

::: {.back card-id="card-de0aa28404f698be"}
For Noetherian schemes, projective $ \implies $ proper.
:::

::: {.front card-id="card-1663965932adfa0b"}
What is a faithfully flat morphism?
:::

::: {.back card-id="card-1663965932adfa0b"}
Flat and surjective.
:::

::: {.front card-id="card-3bc057f937ac3fbd"}
What is a rational morphism?
:::

::: {.back card-id="card-3bc057f937ac3fbd"}
An equivalence class of pairs $ (U, { \left.{{f}} \right|_{{U}} }) $ where $ U\subseteq X $ is open dense and $ { \left.{{f}} \right|_{{U}} }: U\to Y $ is a morphism, which are identified if they coincide on intersections.
:::

::: {.front card-id="card-2672951a3cb0357e"}
What is a birational map?
:::

::: {.back card-id="card-2672951a3cb0357e"}
A rational map with a rational inverse.
:::

::: {.front card-id="card-588fc4423bcb3277"}
What is the degree of a morphism?
:::

::: {.back card-id="card-588fc4423bcb3277"}
$ f:X\to S $ with $ f_*{\mathcal{O}}_X\in   {}_{{\mathcal{O}}_s}{\mathsf{Mod}} $ finite and locally free, take its degree as a Coherent sheaf, where $ \deg {\mathcal{F}}\coloneqq\deg \operatorname{det}{\mathcal{F}} $ since $ \operatorname{det}{\mathcal{F}}\in \operatorname{Pic}(X) $, where the degree is the degree of the associated divisor.
:::

::: {.front card-id="card-2fc77d27d9c19b46"}
What is a **separated morphism**?
:::

::: {.back card-id="card-2fc77d27d9c19b46"}
A morphism $ f:X\to S $ of schemes is **separated** iff $ \Delta_{X/S}: X\to X \underset{\scriptscriptstyle {S} }{\times} X $ is a **closed immersion**.
:::

::: {.front card-id="card-16d44af59a623c18"}
How is this separatedness related to Hausdorffness?
:::

::: {.back card-id="card-16d44af59a623c18"}
$ X\in {\mathsf{Top}} $ is **Hausdorff** iff the diagonal $ \Delta \subseteq X\times X $ is a closed subset.
:::

::: {.front card-id="card-e1412ba6beca8d61"}
What is a quasiseparated morphism?
:::

::: {.back card-id="card-e1412ba6beca8d61"}
- $ f:X\to S $ is quasiseparated iff the diagonal is quasicompact.
:::

::: {.front card-id="card-18c0183a85d23dc4"}
What is qcqs? (Quasi-compact and quasiseparated)
:::

::: {.back card-id="card-18c0183a85d23dc4"}
Quasicompact: inverse images of quasicompact sets are quasicompact. Quasiseparated: the diagonal is quasicompact.
:::

::: {.front card-id="card-bf7f67bffb5a2228"}
What is an affine morphism?
:::

::: {.back card-id="card-bf7f67bffb5a2228"}
Inverse images of affines are affine.
:::

::: {.front card-id="card-534d631836eea4d5"}
What are some examples of affine morphisms?
:::

::: {.back card-id="card-534d631836eea4d5"}
Any morphism between affine schemes, closed immersions.
:::

::: {.front card-id="card-034beb5eb0638400"}
What are some consequences of a morphism being affine?
:::

::: {.back card-id="card-034beb5eb0638400"}
Separated and quasicompact.
:::

::: {.front card-id="card-9afecef0329938ff"}
What is a quasiaffine morphism?
:::

::: {.back card-id="card-9afecef0329938ff"}
Inverse images of quasiaffines are quasiaffine.
:::

::: {.front card-id="card-9ddb86c66cf9607a"}
What is a quasiaffine scheme?
:::

::: {.back card-id="card-9ddb86c66cf9607a"}
Quasicompact and isomorphic to an open subscheme of an affine scheme.
:::

::: {.front card-id="card-c347351b419faef3"}
What is a normal morphism?
:::

::: {.back card-id="card-c347351b419faef3"}
$ f:X\to Y $ with $ f $ flat at $ x $ and the fiber $ X_{f(x)} $ *geometrically normal*, i.e. for every field extension $ L/k $ and every $ \ell $ over $ x $ in $ X \underset{\scriptscriptstyle {k} }{\times} L $ has a normal local ring, i.e. integrally closed in its field of fractions.
:::

::: {.front card-id="card-74776a13413b562c"}
What is a regular morphism?
:::

::: {.back card-id="card-74776a13413b562c"}
Flat at $ x $ and *geometrically regular* at $ x $, i.e. for every fg field extension $ L/k $ and $ \ell $ over $ x $ in $ X \underset{\scriptscriptstyle {k} }{\times} L $, the local ring at $ \ell $ is regular, i.e. the minimal number of generators of its maximal ideal equals its Krull dimension.
:::

::: {.front card-id="card-b18d26174d2423d1"}
What is the cotangent complex?
:::

::: {.back card-id="card-b18d26174d2423d1"}
The nonabelian left-derived functor $ {\mathbb{L}}_{{-}/A}: \mathsf{CRing}_A\to \mathbf{D}{  {}_{A}{\mathsf{Mod}}} $ of the functor $ \Omega^1_{{-}/A}[0] $
:::

::: {.front card-id="card-c79260140f5f0dbd"}
When is a morphism of schemes an immersion?
:::

::: {.back card-id="card-c79260140f5f0dbd"}
$ \iota: X\to Z $ making $ X $ isomorphic to an open subscheme *of a closed subscheme* of $ Z $.
:::

::: {.front card-id="card-9129195c6fc4fa3d"}
Name some properties preserved by base change.
:::

::: {.back card-id="card-9129195c6fc4fa3d"}
Open/closed immersions, affine, finite, integral, locally of ft, qc, ft, quasi-finite, flat, surjective.
:::
