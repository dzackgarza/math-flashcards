---
title: "Orals::Schemes"
---

::: {.front card-id="card-11777c341e4d7e90"}
Give several concrete examples of schemes
:::

::: {.back card-id="card-11777c341e4d7e90"}
$ V(xy) $ the union of axes, which is not irreducible.

$ V(y^2-x^3) $ the cuspidal curve.

$ V(x^2-y^2) $, the X-shaped space.

$ V(y^2-x^3-x) $ the nodal curve

$ V(y^2-ax^3-bx) $ a general elliptic curve.

The rational normal curves $ {\mathbf{P}}^1\to {\mathbf{P}}^N $ given by the Veronese embedding $ [x:y]\mapsto $ monomials of degree $ d $, so $ N = {n+d\choose d} $.

The twisted cubic $ \operatorname{im}\qty{{\left[ {x:y} \right]} \to {\left[ {x^3: x^2 y : xy^2 : y^3} \right]} } $, cut out as $ V(xz-y^2, yw-z^2, xw-yz)\subseteq {\mathbf{P}}^3 $ (i.e. the image of Veronese $ {\mathbf{P}}^1\to {\mathbf{P}}^3 $). Equivalently the $ d=3 $ rational normal curve.

The dual numbers $ \operatorname{Spec}k[{\varepsilon}]/{\varepsilon}^2 $.

$ {\mathbf{A}}^1 $ with a doubled origin (not separated)

The quadric surface $ V(xy-zw) \subseteq {\mathbf{P}}^3 $

$ V(x^2+y^2-z^2) $ the double cone along the $ z{\hbox{-}} $axis.

$ \operatorname{Spec}R $ for any ring (obviously!)

$ \operatorname{Spec}k $ is a point

$ \operatorname{Spec}R $ for $ R\in \mathsf{DVR} $ is 2 points: a closed point and a generic point.

The Whitney umbrella $ V(x^2-y^2z) $.
:::

::: {.front card-id="card-a8ecd677d4355b6c"}
Give several concrete examples of morphisms of schemes.
:::

::: {.back card-id="card-a8ecd677d4355b6c"}
The normalization of the cuspidal curve $ \eta:{\mathbf{A}}^1\to C $ where $ t\mapsto (t^2, t^3) $.

$ (x, y)\mapsto (x, xy) $ on $ {\mathbf{A}}^2 $

$ x\mapsto x^n $ on $ {\mathbf{G}}_m $

$ V(xy-c) \to {\mathbf{A}}^1 $ given by coordinate projection
:::

::: {.front card-id="card-6cd6fec72ba5a191"}
Give an example of a morphism of ringed spaces which is not induced by any ring morphism.
:::

::: {.back card-id="card-6cd6fec72ba5a191"}
Take $ R $ a DVR, then $ \operatorname{Spec}\operatorname{ff}(R) \to \operatorname{Spec}R $ sending the unique point to the closed point. This is not induced by any morphism $ R\to \operatorname{ff}(R) $ since it is not a morphism of *locally* ringed spaces.
:::

::: {.front card-id="card-680201bc520b8457"}
What is a ringed space? Locally ringed spaces?
:::

::: {.back card-id="card-680201bc520b8457"}
$ (X, {\mathcal{O}}_X) $ where $ X\in {\mathsf{Top}} $ and a **structure sheaf** $ {\mathcal{O}}_X\in {\mathsf{Sh}}(X, \mathsf{CRing}) $. This is locally ringed if all stalks $ {\mathcal{O}}_{X, x} $ have unique maximal ideals.
:::

::: {.front card-id="card-645aa342d2f0ce7b"}
What is a morphism of ringed spaces? Locally ringed spaces?
:::

::: {.back card-id="card-645aa342d2f0ce7b"}
Pairs $ (f, f^\sharp) $ where $ f\in {\mathsf{Top}}(X, Y) $ and $ f^\sharp: {\mathcal{O}}_{Y} \to f_* {\mathcal{O}}_X $. This is a morphism of locally ringed spaces iff $ f^\sharp_x: {\mathcal{O}}_{Y, f(x)} \to f_* {\mathcal{O}}_{X, x} $ is a morphism of local rings, i.e. $ f^\sharp_x( {\mathfrak{m}}_{f(x)} ) \subseteq {\mathfrak{m}}_x $.
:::

::: {.front card-id="card-f5a08ee1e016720b"}
What is the definition of a scheme?
:::

::: {.back card-id="card-f5a08ee1e016720b"}
A locally ringed space $ (X, {\mathcal{O}}_X) $ locally isomorphic to an affine scheme, i.e. $ \exists {\mathcal{U}}\rightrightarrows X $ such that $ (U, { \left.{{{\mathcal{O}}_X}} \right|_{{U}} }) \cong (\operatorname{Spec}A, {\mathcal{O}}_{\operatorname{Spec}A}) $ for each $ U $.
:::

::: {.front card-id="card-93ee15a42cf7782e"}
What is the dimension of a scheme?
:::

::: {.back card-id="card-93ee15a42cf7782e"}
Supremum of lengths of chains of irreducible closed subsets, where the length is the number of *links* in a chain $ Z_0 \subseteq Z_1 \subseteq \cdots \subseteq Z_n $.
:::

::: {.front card-id="card-98f87625dc32d705"}
What is the Krull dimension of a ring?
:::

::: {.back card-id="card-98f87625dc32d705"}
Supremum of all lengths of chains of primes ideals.
:::

::: {.front card-id="card-b0c0714e38749bce"}
What is a variety in scheme-theoretic terms?
:::

::: {.back card-id="card-b0c0714e38749bce"}
A separated integral scheme of finite type over a field.
:::

::: {.front card-id="card-d706ceb0a1e4d9f3"}
What is an **affine scheme**? What are their morphisms?
:::

::: {.back card-id="card-d706ceb0a1e4d9f3"}
A locally ringed space $ (X, {\mathcal{O}}_X) $ which is isomorphic to $ (R, {\mathcal{O}}_{\operatorname{Spec}R}) $ for some $ R\in \mathsf{CRing} $. Morphisms are morphisms of *locally* ringed spaces, and maps $ \operatorname{Spec}A\to \operatorname{Spec}B $ biject with ring maps $ B\to A $.
:::

::: {.front card-id="card-3c2e2b84953088f7"}
Describe $ (\operatorname{Spec}A, {\mathcal{O}}_{\operatorname{Spec}A}) $.
:::

::: {.back card-id="card-3c2e2b84953088f7"}
Stalks $ {\mathcal{O}}_{\operatorname{Spec}A, {\mathfrak{p}}} = A_{\mathfrak{p}}\coloneqq S^{-1}A, S\coloneqq A\setminus{\mathfrak{p}} $.

Sections: $ {\mathcal{O}}(U) = s: U\to {\textstyle\coprod}_{p\in U} A_p $ where $ s(p) \in A_p $ and locally a fraction: $ \forall p\in U, \exists V $ with $ p\in V \subseteq U $ and $ \exists a, f\in A $ such that for each $ q\in V $ with $ f\not\in q $, $ s(q) = a/f $.

Global sections: $ A $.
:::

::: {.front card-id="card-41b68915a379f240"}
What is a (quasi)projective scheme?
:::

::: {.back card-id="card-41b68915a379f240"}
Projective morphisms: $ f:X\to Y $ factoring through a closed immersion $ X\to {\mathbf{P}}^n_{/ {Y}} $

Quasiprojective morphisms: factoring through an *open* immersion.

(quasi)projective iff structure morphism is.
:::

::: {.front card-id="card-a6f91c7c60717e89"}
How is a non-affine **scheme** defined?
:::

::: {.back card-id="card-a6f91c7c60717e89"}
A locally ringed space in which every point $ x $ admits a neighborhood which is isomorphic to an affine scheme.
:::

::: {.front card-id="card-f95579b2ccf96d41"}
What is a **normal scheme**?
:::

::: {.back card-id="card-f95579b2ccf96d41"}
$ X $ is normal iff irreducible and $ {\mathcal{O}}_{X, x} $ is a normal ring at each point, i.e. reduced and integrally closed in its field of fractions.

A ring $ R $ is integrally closed if every $ s\in S \coloneqq\operatorname{ff}(R) $ is integral over $ R $, i.e. $ \exists f\in R[x] $ with $ f(s) = 0 $..
:::

::: {.front card-id="card-e4bb12b1e53ef9aa"}
What is the **normalization** of a scheme?
:::

::: {.back card-id="card-e4bb12b1e53ef9aa"}
Cover $ \operatorname{Spec}A_i\rightrightarrows X $, let $ K_i $ be the integral closure of $ A_i $ in its fraction field, and glue $ \operatorname{Spec}K_i $ together to get $ \tilde X \to X $.
:::

::: {.front card-id="card-eee331be6492de45"}
Discuss the normalization.
:::

::: {.back card-id="card-eee331be6492de45"}
Exists for any reduced scheme, yields $ f: \tilde X\to X $ an integral birational morphism (finite for varieties), always regular in codimension 1 so yields regular (thus smooth) curves and surfaces with only isolated singularities. Makes every finite birational morphism into $ \tilde X $ an isomorphism.
:::

::: {.front card-id="card-571f6dddb3e98505"}
Give an example of a non-normal scheme.
:::

::: {.back card-id="card-571f6dddb3e98505"}
The cuspidal curve $ V(y^2-x^3) $, since there is a finite birational morphism

$$\begin{align*}{\mathbf{A}}^1&\to X \\ t&\mapsto (t^2, t^3)\end{align*}$$

which is not an isomorphism. Similarly, the nodal cubic $ V(y^2-x(x+1)) $ is not normal since its parameterization $ t\mapsto (f_1(t), f_2(t)) $ which is not an isomorphism (2-to-1 at the node).
:::

::: {.front card-id="card-9b3ba2e73259c05c"}
What is the universal property of normalization?
:::

::: {.back card-id="card-9b3ba2e73259c05c"}
Every dominant $ f:Z\to X $ factors through $ \tilde X\to X $.
:::

::: {.front card-id="card-1a4004ebf4e453ee"}
What is the **reduced scheme structure** on a closed subset of a scheme?
:::

::: {.back card-id="card-1a4004ebf4e453ee"}
For affines $ Y \subseteq X = \operatorname{Spec}A $: set $ {\mathfrak{a}}\coloneqq\bigcap_{{\mathfrak{p}}\in Y}{\mathfrak{p}} $ the intersection of all prime ideals in $ Y $, then $ \operatorname{Spec}(A/{\mathfrak{a}}) \cong Y $ maximally, and $ A/{\mathfrak{a}} $ is reduced since $ {\mathfrak{a}} $ is radical, this defines a reduced scheme. Alternatively take $ V({\mathfrak{a}}) $ which has coordinate ring $ A/{\mathfrak{a}} $.

For arbitrary schemes $ Y\subseteq X $, cover by affines $ U_i $, intersect with $ Y $ to get $ Y_i $, put above reduced structure on them. These agree on triple overlaps and so one can glue the sheaves on $ Y_i $ to one on $ Y $.
:::

::: {.front card-id="card-83ac8aa1cdbd2198"}
What is an **integral scheme**?
:::

::: {.back card-id="card-83ac8aa1cdbd2198"}
Covered by spectra $ \operatorname{Spec}R_i $ with each $ R_i $ an integral domain, so no nonzero zero divisors.

Equivalently, $ X $ is reduced and irreducible.

$ {\mathcal{O}}_X(U) $ is an integral domain for all $ U $.
:::

::: {.front card-id="card-916ff2f19bad03f2"}
What is a consequence of a scheme being integral?
:::

::: {.back card-id="card-916ff2f19bad03f2"}
There is only one generic point, as opposed to many associated points. A section of a line bundle over a nonempty open is determined by its stalk at its generic point.
:::

::: {.front card-id="card-3e5a7802b44048bf"}
What is a **regular scheme**?
:::

::: {.back card-id="card-3e5a7802b44048bf"}
For $ X $ locally Noetherian, the rings $ {\mathcal{O}}_{X, x} $ at closed points are all regular rings.

$$\dim_{\kappa(x)} {\mathbf{T}}_{X, x} = \operatorname{krulldim}R, R\coloneqq{\mathcal{O}}_{X, x} \qquad\forall x\in X, k \coloneqq R/{\mathfrak{m}}_R$$
:::

::: {.front card-id="card-3a870899611e5f04"}
What does it mean to be **regular in codimension 1**?
:::

::: {.back card-id="card-3a870899611e5f04"}
Every local ring $ {\mathcal{O}}_{X, x} $ of dimension 1 is regular.

More generally for local rings, for every prime ideal $ {\mathfrak{p}}\in \operatorname{Spec}A $ of height 1, the localization $ A_{\mathfrak{p}} $ is regular and hence a field or DVR.
:::

::: {.front card-id="card-5e3188dbef9fc5a0"}
What are some examples of schemes that are regular in codimension 1?
:::

::: {.back card-id="card-5e3188dbef9fc5a0"}
Smooth varieties over a field: the local rings of closed points are regular, hence of all points, since they are localizations of the former.

Any Noetherian normal scheme: any local ring of dimension 1 is an integrally closed domain and hence regular.
:::

::: {.front card-id="card-c64f65eef56890b2"}
What is a **reduced scheme**?
:::

::: {.back card-id="card-c64f65eef56890b2"}
$ X $ is reduced iff $ {\mathcal{O}}_X(U) $ is a reduced ring for every $ U $, or equivalently every local ring $ {\mathcal{O}}_{X, x} $ is reduced, where a ring $ R $ is reduced iff no nonzero nilpotents.
:::

::: {.front card-id="card-17e3b6dd4ac0258d"}
What is a **quasicompact morphism**? A quasicompact scheme?
:::

::: {.back card-id="card-17e3b6dd4ac0258d"}
$ f:Y\to X $ is quasicompact iff $ \exists {\mathcal{V}}\rightrightarrows Y $ by open affine subschemes such that each $ f^{-1}(V_i) $ is quasicompact as a space (i.e. every open cover admits a finite subcover).
:::

::: {.front card-id="card-041ea23b72922e69"}
What is a **locally Noetherian scheme**?
:::

::: {.back card-id="card-041ea23b72922e69"}
A scheme is **locally** Noetherian iff every $ x\in X $ admits an open neighborhood $ U_x\ni x $ such that $ U_x = \operatorname{Spec}R_i $ with $ R_i $ a Noetherian ring (ACC)
:::

::: {.front card-id="card-fb850108ac7bd9c3"}
What is a **Noetherian** scheme?
:::

::: {.back card-id="card-fb850108ac7bd9c3"}
A scheme is Noetherian iff locally Noetherian and quasicompact.
:::

::: {.front card-id="card-eeddc4ca51429133"}
What is a **separated scheme**?
:::

::: {.back card-id="card-eeddc4ca51429133"}
$ X $ is separated iff its structure morphism $ X\to \operatorname{Spec}{\mathbf{Z}} $ is a separated morphism, i.e. the diagonal $ \Delta_{X/\operatorname{Spec}{\mathbf{Z}}}: X\to X \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} X $ is a **closed immersion**.
:::

::: {.front card-id="card-d5feac6218f5093e"}
What is a **quasiseparated** scheme?
:::

::: {.back card-id="card-d5feac6218f5093e"}
$ X $ is quasiseparated iff $ X\to \operatorname{Spec}{\mathbf{Z}} $ is a quasiseparated morphisms, where $ f:X\to Y $ is quasiseparated iff $ \Delta_{X/Y}: X\to X \underset{\scriptscriptstyle {Y} }{\times} X $ is a quasicompact morphism.
:::

::: {.front card-id="card-314acbfef34305d8"}
What is a **locally factorial** scheme? (Equivalently, **factorial**)
:::

::: {.back card-id="card-314acbfef34305d8"}
All local rings are UFDs. Implies that every Weil divisor is Cartier.
:::

::: {.front card-id="card-57df6bd719dcbcca"}
What is a **formal scheme**?
:::

::: {.back card-id="card-57df6bd719dcbcca"}
A locally ringed space locally isomorphic to $ (\operatorname{Spf}A, {\mathcal{O}}_{\operatorname{Spf}A}) $ where $ \operatorname{Spf}A $ is the formal spectrum of a ring -- roughly the completion of a Noetherian scheme $ X_i $ along a closed subscheme $ Y_i $, where one takes $ Y $ as the space and $ \varprojlim_n {\mathcal{O}}_X/{\mathcal{I}}_Y^n $.
:::

::: {.front card-id="card-18bbf10d6992deac"}
What is a **smooth scheme** of relative dimension $ n $?
:::

::: {.back card-id="card-18bbf10d6992deac"}
$ f:X\to Y $ flat, $ \dim(X')= \dim Y' + n $ whenever $ X', Y_i $ are irreducible with $ f(X')\subseteq Y' $, and $ \dim_{\kappa(x)} (\Omega_{X/Y}\otimes\kappa(x)) = n $ for all closed and generic points.

For $ X $ integral, the last condition can be replaced with $ \Omega_{X/Y} $ is locally free of rank $ n $.
:::

::: {.front card-id="card-289455ed6aa37e98"}
What are some examples of smooth schemes?
:::

::: {.back card-id="card-289455ed6aa37e98"}
$ {\mathbf{A}}^n/S, {\mathbf{P}}^n/S $ are smooth of relative dimension $ n $.

Over a field $ k={ \overline{k} } $, smooth iff regular of dimension $ n $.

For an irreducible separated scheme over a field $ k ={ \overline{k} } $, smooth iff nonsingular as a variety.
:::

::: {.front card-id="card-8c4813bcb8326a81"}
What is an example of a non-smooth scheme?
:::

::: {.back card-id="card-8c4813bcb8326a81"}
$ V(x^2)\subseteq {\mathbf{A}}^1_{/ {k}} $,

$ \operatorname{Spec}E $ over $ \operatorname{Spec}k $ where $ E $ is a nonseparable extension e.g. $ { \mathbf{F} }_p(t^{1\over p}) $ over $ { \mathbf{F} }_p(t) $,

the cuspidal curve $ V(y^2-x^3) $.
:::

::: {.front card-id="card-fb0795cc9324cabf"}
What is a **Gorenstein** scheme?
:::

::: {.back card-id="card-fb0795cc9324cabf"}
Locally Noetherian whose local rings are Gorenstein ($ R $ such that $ R $ has finite injective dimension in $   {}_{R}{\mathsf{Mod}} $).
:::

::: {.front card-id="card-1259f228e463095e"}
What are some consequences of being Gorenstein?
:::

::: {.back card-id="card-1259f228e463095e"}
The canonical line bundle $ K_X $ exists.
:::

::: {.front card-id="card-08f6008be740f673"}
What is a **local complete intersection**?
:::

::: {.back card-id="card-08f6008be740f673"}
For a closed subscheme $ Y $ of $ {\mathbf{P}}^n/k $: the ideal $ I $ of $ Y $ in $ k[x_0,\cdots, x_n] $ can be generated by $ r\coloneqq\operatorname{codim}_{{\mathbf{P}}^n}(Y) $ elements. Equivalent to $ Y = \bigcap_{i=1}^r H_i $ for some hypersurfaces $ H_i $ and thus $ {\mathcal{I}}_Y = \sum_{i=1}^r {\mathcal{I}}_{H_i} $.

For an arbitrary closed subscheme $ Y\leq X $ of a smooth variety: $ Y $ is lci in $ X $ iff $ {\mathcal{I}}_Y $ can be locally generated by $ r\coloneqq\operatorname{codim}_{X}(Y) $ elements at every point $ y\in Y $.
:::

::: {.front card-id="card-063a8348047c4935"}
What is a **Cohen-Macaulay** scheme?
:::

::: {.back card-id="card-063a8348047c4935"}
All local rings are Cohen-Macaulay: $ A $ where $ \mathrm{depth} A = \dim A $, where the depth is the maximal length of a regular sequence whose generates are in $ {\mathfrak{m}}_A $, and $ \left\{{x_1,\cdots, x_n}\right\} $ is a regular sequence for $ M\in   {}_{A}{\mathsf{Mod}} $ is $ x_1 $ is not a zero divisor in $ M $ and $ x_{i+1} $ is not a zero divisor in $ M/I_iM $ where $ I_i \coloneqq\left\langle{x_1,\cdots, x_i}\right\rangle $.
:::

::: {.front card-id="card-b1773b17df4126bf"}
What is a **scheme-theoretic intersection**?
:::

::: {.back card-id="card-b1773b17df4126bf"}
For relative schemes $ X_i\to Y $, the intersection of $ X_1 $ and $ X_2 $ is the fiber product $ X_1 { \underset{\scriptscriptstyle {Y} }{\times} } X_2 $. For affines $ X_1 = R/J_1 $ and $ X_2 = R/J_2 $, this is realized by

$$\operatorname{Spec}(R/J_1 \otimes_R R/J_2) \cong \operatorname{Spec}R/(J_1 + J_2).$$

If $ X_i \hookrightarrow Y $ are closed subschemes, then the intersection is again a closed subscheme of $ Y $..
:::

::: {.front card-id="card-f6688f63a2714f98"}
What is an **open subscheme**?
:::

::: {.back card-id="card-f6688f63a2714f98"}
A scheme $ U $ with $ {\left\lvert {U} \right\rvert} \subseteq {\left\lvert {X} \right\rvert} $ is an open subspace where $ {\mathcal{O}}_{U} \cong { \left.{{{\mathcal{O}}_X}} \right|_{{U}} } $.
:::

::: {.front card-id="card-4c3df89f2859bc57"}
What is the **residue field** at a point $ x\in X $?
:::

::: {.back card-id="card-4c3df89f2859bc57"}
$ \kappa(x) \coloneqq A_{\mathfrak{p}}/ {\mathfrak{p}}A_{\mathfrak{p}} $ where $ U = \operatorname{Spec}A \ni x $ and $ {\mathfrak{p}}\in \operatorname{Spec}A $ corresponds to $ x $.
:::

::: {.front card-id="card-8a7983284608870e"}
What is the scheme-theoretic definition of an **affine variety**?
:::

::: {.back card-id="card-8a7983284608870e"}
Integral noetherian separated schemes of finite type over a field
:::

::: {.front card-id="card-d78d46215a60b1cb"}
What is the **scheme associated to a variety**?
:::

::: {.back card-id="card-d78d46215a60b1cb"}
Use the functor $ t: {\mathsf{Var}}_{/ {k}}\to {\mathsf{Sch}}_{/ {k}} $, then $ V $ is homeomorphic to the closed points in $ {\left\lvert {t(V)} \right\rvert} $ and $ {\mathcal{O}}_V \cong { \left.{{ {\mathcal{O}}_{t(V)}}} \right|_{{t(V)^{ \operatorname{cl}}}} } $, i.e. the regular functions on $ V $ are restrictions to closed points of the structure sheaf of $ t(V) $.

Generally $ t(V) $ is the set of nonempty irreducible closed subsets of $ V $, define the images of such sets to be closed sets to form a topology.
:::

::: {.front card-id="card-34901803982172ce"}
What is the scheme-theoretic definition of a (smooth) **curve**?
:::

::: {.back card-id="card-34901803982172ce"}
An integral separated scheme of dimension 1 of finite type over a field $ k $.

Smooth iff all local rings are regular.
:::

::: {.front card-id="card-93365011b44724e2"}
What is the **Proj construction**?
:::

::: {.back card-id="card-93365011b44724e2"}
For $ S $ a graded ring,write $ S_+ \coloneqq\bigoplus_{d\geq 1} S_d $ and let $ \mathop{\mathrm{Proj}}S $ be the set of homogeneous prime ideals of $ S $ which do not completely contains $ S_+ $. Define $ V({\mathfrak{p}}) \coloneqq\left\{{P\in \mathop{\mathrm{Proj}}S {~\mathrel{\Big\vert}~}P \supseteq{\mathfrak{p}}}\right\} $.

For the structure sheaf, for each $ p\in \mathop{\mathrm{Proj}}S $ define $ S_p $ to be the elements of degree zero in the localization $ S[T^{-1}] $ where $ T $ is the system of all homogeneous elements of $ S $ which are not in $ p $, and define $ {\mathcal{O}}(U) $ to be functions $ s: U\to \amalg_{p\in U} S_p $ with $ s(p) \in S_p $ and $ s $ is locally a fraction: $ s(q) = a/f $ with $ a,f\in S $ homogeneous of the same degree and $ f\not\in q $.
:::

::: {.front card-id="card-6cdb91f28276b7cc"}
What is $ {\mathbf{A}}^n_{/ {R}} $ as a scheme?
:::

::: {.back card-id="card-6cdb91f28276b7cc"}
$ \operatorname{Spec}R[x_1,\cdots, x_n] $ or $ {\mathbf{A}}^n_{/ {{\mathbf{Z}}}} \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} \operatorname{Spec}R $.
:::

::: {.front card-id="card-0fa32d3a60ede40b"}
How are morphisms $ X\to {\mathbf{A}}^n_{/ {S}} $ characterized?
:::

::: {.back card-id="card-0fa32d3a60ede40b"}
A choice of $ n $ sections $ h_1,\cdots,h_n \in H^0(X; {\mathcal{O}}_X) $.
:::

::: {.front card-id="card-acdb021d5d026890"}
How is $ {\mathbf{P}}^n/S $ defined for $ S $ a scheme?
:::

::: {.back card-id="card-acdb021d5d026890"}
Define $ {\mathbf{P}}^n_{/ {{\mathbf{Z}}}}\coloneqq\mathop{\mathrm{Proj}}{\mathbf{Z}}[x_0,\cdots, x_n] $ and $ {\mathbf{P}}^n_{/ {S}} \coloneqq{\mathbf{P}}^n_{/ {{\mathbf{Z}}}} \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} S $.
:::

::: {.front card-id="card-98c1f9a1ecd625ba"}
What is the **reduced scheme** associated to a scheme?
:::

::: {.back card-id="card-98c1f9a1ecd625ba"}
For $ (X, {\mathcal{O}}_X)\in {\mathsf{Sch}} $, sheafify $ U\mapsto {\mathcal{O}}_X(U)^{ \text{red} } $ where $ R^{ \text{red} }\coloneqq R/{\sqrt{0_{R}} } $ is the quotient by the ideal of nilpotent elements to get $ {\mathcal{O}}_{X}^{ \text{red} } $.
:::

::: {.front card-id="card-a193384cad51473e"}
What is an **irreducible** scheme?
:::

::: {.back card-id="card-a193384cad51473e"}
Irreducible as a topological space, i.e. does not admit a cover by two proper nonempty closed subsets.
:::

::: {.front card-id="card-984cea0fe1e067b0"}
What is the **reduced induced scheme structure** on $ Z\subseteq X $ a closed subset?
:::

::: {.back card-id="card-984cea0fe1e067b0"}
For any $ T\subseteq X $ closed, construct a unique closed $ Z\subseteq X $ such that $ {\left\lvert {Z} \right\rvert} = {\left\lvert {T} \right\rvert} $ and $ Z $ is reduced. For affine $ X\subseteq \operatorname{Spec}A $, take $ {\mathcal{I}}\coloneqq\bigcap_{{\mathfrak{m}}\in X}{\mathfrak{m}} $ and the subscheme it defines; for arbitrary schemes do this locally and glue.
:::

::: {.front card-id="card-fee79260e57ce322"}
What is the **scheme-theoretic image**?
:::

::: {.back card-id="card-fee79260e57ce322"}
For $ f:X\to Y $, the smallest closed subscheme of $ Y $ through which $ f $ factors.

Can take $ {\mathcal{I}}\coloneqq\ker\qty{{\mathcal{O}}_Y\to f_* {\mathcal{O}}_X} $ if this is qcoh, or if $ X $ is reduced take $ \overline{f(X)} $.

E.g. if $ f: A\to B $ inducing $ \operatorname{Spec}B\to \operatorname{Spec}A $, take $ \operatorname{Spec}(A/I)\leq \operatorname{Spec}A $ as a closed subscheme.
:::

::: {.front card-id="card-1f9ebf5ac271403c"}
What is an $ n{\hbox{-}} $fold point over $ k $?
:::

::: {.back card-id="card-1f9ebf5ac271403c"}
A scheme $ \operatorname{Spec}R\to \operatorname{Spec}k $ with one point such that $ R $ is a $ k{\hbox{-}} $algebra of dimension $ n $.
:::

::: {.front card-id="card-6067745a47634f5c"}
What is the **Riemann-Roch theorem**?
:::

::: {.back card-id="card-6067745a47634f5c"}
For $ C $ a curve,

$$\chi(C; {\mathcal{L}}) = \deg({\mathcal{L}}) + (1-g)$$
:::

::: {.front card-id="card-6ca7d0c76fa6a201"}
How is the **adjunction formula** derived?
:::

::: {.back card-id="card-6ca7d0c76fa6a201"}
Start with $ f: C\hookrightarrow S $ a curve in a surface over $ \operatorname{Spec}k $ to get

$$\begin{align*}{\mathbf{T}}_C \hookrightarrow f^* {\mathbf{T}}_S \twoheadrightarrow N_{C/S} \quad &\underset{\text{dualize}}\leadsto\quad N {}^{ \vee }_{C/S} \coloneqq I_C/I_C^2 \hookrightarrow f^* \Omega^1_{S/k} \twoheadrightarrow\Omega^{1}_{C/k} \\ &\implies \operatorname{det}f^* \Omega^1_{S/k} \cong \operatorname{det}\Omega^1_{C/k} \otimes\operatorname{det}N {}^{ \vee }_{C/S} \\&\implies f^* \omega_S \cong \omega_C \otimes\operatorname{det}N {}^{ \vee }_{C/S} \\ &\implies\omega_C = f^*\omega_S \otimes\operatorname{det}N_{C/S} \end{align*}$$

Now use that $ I_C = {\mathcal{O}}_Y(C)^{-1} $ and $ I_C/I_C^2 = {\mathcal{O}}_Y(C)^{-1}\otimes{\mathcal{O}}_C $ to get

$$N_{C/S} = (I_C/I_C^2) {}^{ \vee }= ({\mathcal{O}}_S(C)^{-1}\otimes{\mathcal{O}}_C) {}^{ \vee }= {\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C$$

and so

$$\omega_C = f^* \omega_S \otimes{\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C  \implies \omega_C = \qty{\omega_S \otimes{\mathcal{O}}_S(C) }\mathrel{\Big|}_C \implies K_C = (K_S + C)\mathrel{\Big|}_S$$

\
:::

::: {.front card-id="card-f8859d1bf94b455d"}
What is the **adjunction formula**?
:::

::: {.back card-id="card-f8859d1bf94b455d"}
$$\omega_C = \qty{\omega_S \otimes{\mathcal{O}}_S(C) }\mathrel{\Big|}_C \implies K_C = (K_S + C)\mathrel{\Big|}_S$$

$$f^* \omega_Y = \omega_C \otimes{\mathcal{O}}_Y(C) \otimes{\mathcal{O}}_C\implies K_C = (K_Y + C)\mathrel{\Big|}_C$$
:::

::: {.front card-id="card-282fc0e81109dc6b"}
For a smooth curves $ C $ on a surface $ S $, use the adjunction formula to express the genus in terms of intersection numbers.
:::

::: {.back card-id="card-282fc0e81109dc6b"}
$$2g-2 = C.(C+K_C)$$

Use $ \omega_C \cong \omega_S \otimes{\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C $, take degrees, and use that $ \deg(\omega_C) = 2g-2 $ and $ \deg_C({\mathcal{O}}_S(D)\otimes{\mathcal{O}}_C) = {\sharp}(C\cap D) $ to get

$$\deg(\omega_S \otimes{\mathcal{O}}_S(C)\otimes{\mathcal{O}}_C) = \deg({\mathcal{O}}_S(C+K_C)\otimes{\mathcal{O}}_C) = {\sharp}(C \cap(C+K_C)).$$
:::

::: {.front card-id="card-624368019a58567d"}
For $ C\hookrightarrow S $ a curve in a surface, what is $ \omega_C $?
:::

::: {.back card-id="card-624368019a58567d"}
Idea: differential forms with (no?) poles along $ C $, and base change to $ {\mathcal{O}}_C $:

$$\omega_S = (\omega_S \otimes{\mathcal{O}}_S(C))\otimes{\mathcal{O}}_C.$$
:::

::: {.front card-id="card-f73cddec8b039beb"}
What is the degree formula for a curve of degree $ d $ in $ {\mathbf{P}}^2 $?
:::

::: {.back card-id="card-f73cddec8b039beb"}
By adjunction,

$$2g-2 = C.(C+K_C) = d(d-3)\implies g ={1\over 2}(d-1)(d-2).$$
:::

::: {.front card-id="card-7a13c1f152bea481"}
What is **Serre vanishing**?
:::

::: {.back card-id="card-7a13c1f152bea481"}
For $ X $ a Noetherian scheme, $ X $ is affine $ \iff H^{i>0}(X; {\mathcal{F}}) = 0 $ for all $ {\mathcal{F}}\in {\mathsf{QCoh}}(X) \iff H^1(X; {\mathcal{I}}) = 0 $ for all coherent sheaves of ideals on $ X $.
:::

::: {.front card-id="card-a2844b113bfce411"}
What is a **dominant morphism**?
:::

::: {.back card-id="card-a2844b113bfce411"}
For schemes: dense image.
:::
