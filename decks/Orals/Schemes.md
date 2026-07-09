---
title: "Orals::Schemes"
---

- Give several concrete examples of schemes

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

- Give several concrete examples of morphisms of schemes.

    The normalization of the cuspidal curve $ \eta:{\mathbf{A}}^1\to C $ where $ t\mapsto (t^2, t^3) $.

    $ (x, y)\mapsto (x, xy) $ on $ {\mathbf{A}}^2 $

    $ x\mapsto x^n $ on $ {\mathbf{G}}_m $

    $ V(xy-c) \to {\mathbf{A}}^1 $ given by coordinate projection

- Give an example of a morphism of ringed spaces which is not induced by any ring morphism.

    Take $ R $ a DVR, then $ \operatorname{Spec}\operatorname{ff}(R) \to \operatorname{Spec}R $ sending the unique point to the closed point. This is not induced by any morphism $ R\to \operatorname{ff}(R) $ since it is not a morphism of *locally* ringed spaces.

- What is a ringed space? Locally ringed spaces?

    $ (X, {\mathcal{O}}_X) $ where $ X\in {\mathsf{Top}} $ and a **structure sheaf** $ {\mathcal{O}}_X\in {\mathsf{Sh}}(X, \mathsf{CRing}) $. This is locally ringed if all stalks $ {\mathcal{O}}_{X, x} $ have unique maximal ideals.

- What is a morphism of ringed spaces? Locally ringed spaces?

    Pairs $ (f, f^\sharp) $ where $ f\in {\mathsf{Top}}(X, Y) $ and $ f^\sharp: {\mathcal{O}}_{Y} \to f_* {\mathcal{O}}_X $. This is a morphism of locally ringed spaces iff $ f^\sharp_x: {\mathcal{O}}_{Y, f(x)} \to f_* {\mathcal{O}}_{X, x} $ is a morphism of local rings, i.e. $ f^\sharp_x( {\mathfrak{m}}_{f(x)} ) \subseteq {\mathfrak{m}}_x $.

- What is the definition of a scheme?

    A locally ringed space $ (X, {\mathcal{O}}_X) $ locally isomorphic to an affine scheme, i.e. $ \exists {\mathcal{U}}\rightrightarrows X $ such that $ (U, { \left.{{{\mathcal{O}}_X}} \right|_{{U}} }) \cong (\operatorname{Spec}A, {\mathcal{O}}_{\operatorname{Spec}A}) $ for each $ U $.

- What is the dimension of a scheme?

    Supremum of lengths of chains of irreducible closed subsets, where the length is the number of *links* in a chain $ Z_0 \subseteq Z_1 \subseteq \cdots \subseteq Z_n $.

- What is the Krull dimension of a ring?

    Supremum of all lengths of chains of primes ideals.

- What is a variety in scheme-theoretic terms?

    A separated integral scheme of finite type over a field.

- What is an **affine scheme**? What are their morphisms?

    A locally ringed space $ (X, {\mathcal{O}}_X) $ which is isomorphic to $ (R, {\mathcal{O}}_{\operatorname{Spec}R}) $ for some $ R\in \mathsf{CRing} $. Morphisms are morphisms of *locally* ringed spaces, and maps $ \operatorname{Spec}A\to \operatorname{Spec}B $ biject with ring maps $ B\to A $.

- Describe $ (\operatorname{Spec}A, {\mathcal{O}}_{\operatorname{Spec}A}) $.

    Stalks $ {\mathcal{O}}_{\operatorname{Spec}A, {\mathfrak{p}}} = A_{\mathfrak{p}}\coloneqq S^{-1}A, S\coloneqq A\setminus{\mathfrak{p}} $.

    Sections: $ {\mathcal{O}}(U) = s: U\to {\textstyle\coprod}_{p\in U} A_p $ where $ s(p) \in A_p $ and locally a fraction: $ \forall p\in U, \exists V $ with $ p\in V \subseteq U $ and $ \exists a, f\in A $ such that for each $ q\in V $ with $ f\not\in q $, $ s(q) = a/f $.

    Global sections: $ A $.

- What is a (quasi)projective scheme?

    Projective morphisms: $ f:X\to Y $ factoring through a closed immersion $ X\to {\mathbf{P}}^n_{/ {Y}} $

    Quasiprojective morphisms: factoring through an *open* immersion.

    (quasi)projective iff structure morphism is.

- How is a non-affine **scheme** defined?

    A locally ringed space in which every point $ x $ admits a neighborhood which is isomorphic to an affine scheme.

- What is a **normal scheme**?

    $ X $ is normal iff irreducible and $ {\mathcal{O}}_{X, x} $ is a normal ring at each point, i.e. reduced and integrally closed in its field of fractions.

    A ring $ R $ is integrally closed if every $ s\in S \coloneqq\operatorname{ff}(R) $ is integral over $ R $, i.e. $ \exists f\in R[x] $ with $ f(s) = 0 $..

- What is the **normalization** of a scheme?

    Cover $ \operatorname{Spec}A_i\rightrightarrows X $, let $ K_i $ be the integral closure of $ A_i $ in its fraction field, and glue $ \operatorname{Spec}K_i $ together to get $ \tilde X \to X $.

- Discuss the normalization.

    Exists for any reduced scheme, yields $ f: \tilde X\to X $ an integral birational morphism (finite for varieties), always regular in codimension 1 so yields regular (thus smooth) curves and surfaces with only isolated singularities. Makes every finite birational morphism into $ \tilde X $ an isomorphism.

- Give an example of a non-normal scheme.

    The cuspidal curve $ V(y^2-x^3) $, since there is a finite birational morphism

    $$\begin{align*}{\mathbf{A}}^1&\to X \\ t&\mapsto (t^2, t^3)\end{align*}$$

    which is not an isomorphism. Similarly, the nodal cubic $ V(y^2-x(x+1)) $ is not normal since its parameterization $ t\mapsto (f_1(t), f_2(t)) $ which is not an isomorphism (2-to-1 at the node).

- What is the universal property of normalization?

    Every dominant $ f:Z\to X $ factors through $ \tilde X\to X $.

- What is the **reduced scheme structure** on a closed subset of a scheme?

    For affines $ Y \subseteq X = \operatorname{Spec}A $: set $ {\mathfrak{a}}\coloneqq\bigcap_{{\mathfrak{p}}\in Y}{\mathfrak{p}} $ the intersection of all prime ideals in $ Y $, then $ \operatorname{Spec}(A/{\mathfrak{a}}) \cong Y $ maximally, and $ A/{\mathfrak{a}} $ is reduced since $ {\mathfrak{a}} $ is radical, this defines a reduced scheme. Alternatively take $ V({\mathfrak{a}}) $ which has coordinate ring $ A/{\mathfrak{a}} $.

    For arbitrary schemes $ Y\subseteq X $, cover by affines $ U_i $, intersect with $ Y $ to get $ Y_i $, put above reduced structure on them. These agree on triple overlaps and so one can glue the sheaves on $ Y_i $ to one on $ Y $.

- What is an **integral scheme**?

    Covered by spectra $ \operatorname{Spec}R_i $ with each $ R_i $ an integral domain, so no nonzero zero divisors.

    Equivalently, $ X $ is reduced and irreducible.

    $ {\mathcal{O}}_X(U) $ is an integral domain for all $ U $.

- What is a consequence of a scheme being integral?

    There is only one generic point, as opposed to many associated points. A section of a line bundle over a nonempty open is determined by its stalk at its generic point.

- What is a **regular scheme**?

    For $ X $ locally Noetherian, the rings $ {\mathcal{O}}_{X, x} $ at closed points are all regular rings.

    $$\dim_{\kappa(x)} {\mathbf{T}}_{X, x} = \operatorname{krulldim}R, R\coloneqq{\mathcal{O}}_{X, x} \qquad\forall x\in X, k \coloneqq R/{\mathfrak{m}}_R$$

- What does it mean to be **regular in codimension 1**?

    Every local ring $ {\mathcal{O}}_{X, x} $ of dimension 1 is regular.

    More generally for local rings, for every prime ideal $ {\mathfrak{p}}\in \operatorname{Spec}A $ of height 1, the localization $ A_{\mathfrak{p}} $ is regular and hence a field or DVR.

- What are some examples of schemes that are regular in codimension 1?

    Smooth varieties over a field: the local rings of closed points are regular, hence of all points, since they are localizations of the former.

    Any Noetherian normal scheme: any local ring of dimension 1 is an integrally closed domain and hence regular.

- What is a **reduced scheme**?

    $ X $ is reduced iff $ {\mathcal{O}}_X(U) $ is a reduced ring for every $ U $, or equivalently every local ring $ {\mathcal{O}}_{X, x} $ is reduced, where a ring $ R $ is reduced iff no nonzero nilpotents.

- What is a **quasicompact morphism**? A quasicompact scheme?

    $ f:Y\to X $ is quasicompact iff $ \exists {\mathcal{V}}\rightrightarrows Y $ by open affine subschemes such that each $ f^{-1}(V_i) $ is quasicompact as a space (i.e. every open cover admits a finite subcover).

- What is a **locally Noetherian scheme**?

    A scheme is **locally** Noetherian iff every $ x\in X $ admits an open neighborhood $ U_x\ni x $ such that $ U_x = \operatorname{Spec}R_i $ with $ R_i $ a Noetherian ring (ACC)

- What is a **Noetherian** scheme?

    A scheme is Noetherian iff locally Noetherian and quasicompact.

- What is a **separated scheme**?

    $ X $ is separated iff its structure morphism $ X\to \operatorname{Spec}{\mathbf{Z}} $ is a separated morphism, i.e. the diagonal $ \Delta_{X/\operatorname{Spec}{\mathbf{Z}}}: X\to X \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} X $ is a **closed immersion**.

- What is a **quasiseparated** scheme?

    $ X $ is quasiseparated iff $ X\to \operatorname{Spec}{\mathbf{Z}} $ is a quasiseparated morphisms, where $ f:X\to Y $ is quasiseparated iff $ \Delta_{X/Y}: X\to X \underset{\scriptscriptstyle {Y} }{\times} X $ is a quasicompact morphism.

- What is a **locally factorial** scheme? (Equivalently, **factorial**)

    All local rings are UFDs. Implies that every Weil divisor is Cartier.

- What is a **formal scheme**?

    A locally ringed space locally isomorphic to $ (\operatorname{Spf}A, {\mathcal{O}}_{\operatorname{Spf}A}) $ where $ \operatorname{Spf}A $ is the formal spectrum of a ring -- roughly the completion of a Noetherian scheme $ X_i $ along a closed subscheme $ Y_i $, where one takes $ Y $ as the space and $ \varprojlim_n {\mathcal{O}}_X/{\mathcal{I}}_Y^n $.

- What is a **smooth scheme** of relative dimension $ n $?

    $ f:X\to Y $ flat, $ \dim(X')= \dim Y' + n $ whenever $ X', Y_i $ are irreducible with $ f(X')\subseteq Y' $, and $ \dim_{\kappa(x)} (\Omega_{X/Y}\otimes\kappa(x)) = n $ for all closed and generic points.

    For $ X $ integral, the last condition can be replaced with $ \Omega_{X/Y} $ is locally free of rank $ n $.

- What are some examples of smooth schemes?

    $ {\mathbf{A}}^n/S, {\mathbf{P}}^n/S $ are smooth of relative dimension $ n $.

    Over a field $ k={ \overline{k} } $, smooth iff regular of dimension $ n $.

    For an irreducible separated scheme over a field $ k ={ \overline{k} } $, smooth iff nonsingular as a variety.

- What is an example of a non-smooth scheme?

    $ V(x^2)\subseteq {\mathbf{A}}^1_{/ {k}} $,

    $ \operatorname{Spec}E $ over $ \operatorname{Spec}k $ where $ E $ is a nonseparable extension e.g. $ { \mathbf{F} }_p(t^{1\over p}) $ over $ { \mathbf{F} }_p(t) $,

    the cuspidal curve $ V(y^2-x^3) $.

- What is a **Gorenstein** scheme?

    Locally Noetherian whose local rings are Gorenstein ($ R $ such that $ R $ has finite injective dimension in $   {}_{R}{\mathsf{Mod}} $).

- What are some consequences of being Gorenstein?

    The canonical line bundle $ K_X $ exists.

- What is a **local complete intersection**?

    For a closed subscheme $ Y $ of $ {\mathbf{P}}^n/k $: the ideal $ I $ of $ Y $ in $ k[x_0,\cdots, x_n] $ can be generated by $ r\coloneqq\operatorname{codim}_{{\mathbf{P}}^n}(Y) $ elements. Equivalent to $ Y = \bigcap_{i=1}^r H_i $ for some hypersurfaces $ H_i $ and thus $ {\mathcal{I}}_Y = \sum_{i=1}^r {\mathcal{I}}_{H_i} $.

    For an arbitrary closed subscheme $ Y\leq X $ of a smooth variety: $ Y $ is lci in $ X $ iff $ {\mathcal{I}}_Y $ can be locally generated by $ r\coloneqq\operatorname{codim}_{X}(Y) $ elements at every point $ y\in Y $.

- What is a **Cohen-Macaulay** scheme?

    All local rings are Cohen-Macaulay: $ A $ where $ \mathrm{depth} A = \dim A $, where the depth is the maximal length of a regular sequence whose generates are in $ {\mathfrak{m}}_A $, and $ \left\{{x_1,\cdots, x_n}\right\} $ is a regular sequence for $ M\in   {}_{A}{\mathsf{Mod}} $ is $ x_1 $ is not a zero divisor in $ M $ and $ x_{i+1} $ is not a zero divisor in $ M/I_iM $ where $ I_i \coloneqq\left\langle{x_1,\cdots, x_i}\right\rangle $.

- What is a **scheme-theoretic intersection**?

    For relative schemes $ X_i\to Y $, the intersection of $ X_1 $ and $ X_2 $ is the fiber product $ X_1 { \underset{\scriptscriptstyle {Y} }{\times} } X_2 $. For affines $ X_1 = R/J_1 $ and $ X_2 = R/J_2 $, this is realized by

    $$\operatorname{Spec}(R/J_1 \otimes_R R/J_2) \cong \operatorname{Spec}R/(J_1 + J_2).$$

    If $ X_i \hookrightarrow Y $ are closed subschemes, then the intersection is again a closed subscheme of $ Y $..

- What is an **open subscheme**?

    A scheme $ U $ with $ {\left\lvert {U} \right\rvert} \subseteq {\left\lvert {X} \right\rvert} $ is an open subspace where $ {\mathcal{O}}_{U} \cong { \left.{{{\mathcal{O}}_X}} \right|_{{U}} } $.

- What is the **residue field** at a point $ x\in X $?

    $ \kappa(x) \coloneqq A_{\mathfrak{p}}/ {\mathfrak{p}}A_{\mathfrak{p}} $ where $ U = \operatorname{Spec}A \ni x $ and $ {\mathfrak{p}}\in \operatorname{Spec}A $ corresponds to $ x $.

- What is the scheme-theoretic definition of an **affine variety**?

    Integral noetherian separated schemes of finite type over a field

- What is the **scheme associated to a variety**?

    Use the functor $ t: {\mathsf{Var}}_{/ {k}}\to {\mathsf{Sch}}_{/ {k}} $, then $ V $ is homeomorphic to the closed points in $ {\left\lvert {t(V)} \right\rvert} $ and $ {\mathcal{O}}_V \cong { \left.{{ {\mathcal{O}}_{t(V)}}} \right|_{{t(V)^{ \operatorname{cl}}}} } $, i.e. the regular functions on $ V $ are restrictions to closed points of the structure sheaf of $ t(V) $.

    Generally $ t(V) $ is the set of nonempty irreducible closed subsets of $ V $, define the images of such sets to be closed sets to form a topology.

- What is the scheme-theoretic definition of a (smooth) **curve**?

    An integral separated scheme of dimension 1 of finite type over a field $ k $.

    Smooth iff all local rings are regular.

- What is the **Proj construction**?

    For $ S $ a graded ring,write $ S_+ \coloneqq\bigoplus_{d\geq 1} S_d $ and let $ \mathop{\mathrm{Proj}}S $ be the set of homogeneous prime ideals of $ S $ which do not completely contains $ S_+ $. Define $ V({\mathfrak{p}}) \coloneqq\left\{{P\in \mathop{\mathrm{Proj}}S {~\mathrel{\Big\vert}~}P \supseteq{\mathfrak{p}}}\right\} $.

    For the structure sheaf, for each $ p\in \mathop{\mathrm{Proj}}S $ define $ S_p $ to be the elements of degree zero in the localization $ S[T^{-1}] $ where $ T $ is the system of all homogeneous elements of $ S $ which are not in $ p $, and define $ {\mathcal{O}}(U) $ to be functions $ s: U\to \amalg_{p\in U} S_p $ with $ s(p) \in S_p $ and $ s $ is locally a fraction: $ s(q) = a/f $ with $ a,f\in S $ homogeneous of the same degree and $ f\not\in q $.

- What is $ {\mathbf{A}}^n_{/ {R}} $ as a scheme?

    $ \operatorname{Spec}R[x_1,\cdots, x_n] $ or $ {\mathbf{A}}^n_{/ {{\mathbf{Z}}}} \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} \operatorname{Spec}R $.

- How are morphisms $ X\to {\mathbf{A}}^n_{/ {S}} $ characterized?

    A choice of $ n $ sections $ h_1,\cdots,h_n \in H^0(X; {\mathcal{O}}_X) $.

- How is $ {\mathbf{P}}^n/S $ defined for $ S $ a scheme?

    Define $ {\mathbf{P}}^n_{/ {{\mathbf{Z}}}}\coloneqq\mathop{\mathrm{Proj}}{\mathbf{Z}}[x_0,\cdots, x_n] $ and $ {\mathbf{P}}^n_{/ {S}} \coloneqq{\mathbf{P}}^n_{/ {{\mathbf{Z}}}} \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} S $.

- What is the **reduced scheme** associated to a scheme?

    For $ (X, {\mathcal{O}}_X)\in {\mathsf{Sch}} $, sheafify $ U\mapsto {\mathcal{O}}_X(U)^{ \text{red} } $ where $ R^{ \text{red} }\coloneqq R/{\sqrt{0_{R}} } $ is the quotient by the ideal of nilpotent elements to get $ {\mathcal{O}}_{X}^{ \text{red} } $.

- What is an **irreducible** scheme?

    Irreducible as a topological space, i.e. does not admit a cover by two proper nonempty closed subsets.

- What is the **reduced induced scheme structure** on $ Z\subseteq X $ a closed subset?

    For any $ T\subseteq X $ closed, construct a unique closed $ Z\subseteq X $ such that $ {\left\lvert {Z} \right\rvert} = {\left\lvert {T} \right\rvert} $ and $ Z $ s reduced. For affine $ X\subseteq \operatorname{Spec}A $, take $ {\mathcal{I}}\coloneqq\bigcap_{{\mathfrak{m}}\in X}{\mathfrak{m}} $ and the subscheme it defines; for arbitrary schemes do this locally and glue.

- What is the **scheme-theoretic image**?

    For $ f:X\to Y $, the smallest closed subscheme of $ Y $ through which $ f $ factors.

    Can take $ {\mathcal{I}}\coloneqq\ker\qty{{\mathcal{O}}_Y\to f_* {\mathcal{O}}_X} $ if this is qcoh, or if $ X $ is reduced take $ \overline{f(X)} $.

    E.g. if $ f: A\to B $ inducing $ \operatorname{Spec}B\to \operatorname{Spec}A $, take $ \operatorname{Spec}(A/I)\leq \operatorname{Spec}A $ as a closed subscheme.

- What is an $ n{\hbox{-}} $fold point over $ k $?

    A scheme $ \operatorname{Spec}R\to \operatorname{Spec}k $ with one point such that $ R $ is a $ k{\hbox{-}} $algebra of dimension $ n $.

- What is the **Riemann-Roch theorem**?

    For $ C $ a curve,

    $$\chi(C; {\mathcal{L}}) = \deg({\mathcal{L}}) + (1-g)$$

- How is the **adjunction formula** derived?

    Start with $ f: C\hookrightarrow S $ a curve in a surface over $ \operatorname{Spec}k $ to get

    $$\begin{align*}{\mathbf{T}}_C \hookrightarrow f^* {\mathbf{T}}_S \twoheadrightarrow N_{C/S} \quad &\underset{\text{dualize}}\leadsto\quad N {}^{ \vee }_{C/S} \coloneqq I_C/I_C^2 \hookrightarrow f^* \Omega^1_{S/k} \twoheadrightarrow\Omega^{1}_{C/k} \\ &\implies \operatorname{det}f^* \Omega^1_{S/k} \cong \operatorname{det}\Omega^1_{C/k} \otimes\operatorname{det}N {}^{ \vee }_{C/S} \\&\implies f^* \omega_S \cong \omega_C \otimes\operatorname{det}N {}^{ \vee }_{C/S} \\ &\implies\omega_C = f^*\omega_S \otimes\operatorname{det}N_{C/S} \end{align*}$$

    Now use that $ I_C = {\mathcal{O}}_Y(C)^{-1} $ and $ I_C/I_C^2 = {\mathcal{O}}_Y(C)^{-1}\otimes{\mathcal{O}}_C $ to get

    $$N_{C/S} = (I_C/I_C^2) {}^{ \vee }= ({\mathcal{O}}_S(C)^{-1}\otimes{\mathcal{O}}_C) {}^{ \vee }= {\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C$$

    and so

    $$\omega_C = f^* \omega_S \otimes{\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C  \implies \omega_C = \qty{\omega_S \otimes{\mathcal{O}}_S(C) }\mathrel{\Big|}_C \implies K_C = (K_S + C)\mathrel{\Big|}_S$$

    \

- What is the **adjunction formula**?

    $$\omega_C = \qty{\omega_S \otimes{\mathcal{O}}_S(C) }\mathrel{\Big|}_C \implies K_C = (K_S + C)\mathrel{\Big|}_S$$

    $$f^* \omega_Y = \omega_C \otimes{\mathcal{O}}_Y(C) \otimes{\mathcal{O}}_C\implies K_C = (K_Y + C)\mathrel{\Big|}_C$$

- For a smooth curves $ C $ on a surface $ S $, use the adjunction formula to express the genus in terms of intersection numbers.

    $$2g-2 = C.(C+K_C)$$

    Use $ \omega_C \cong \omega_S \otimes{\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C $, take degrees, and use that $ \deg(\omega_C) = 2g-2 $ and $ \deg_C({\mathcal{O}}_S(D)\otimes{\mathcal{O}}_C) = {\sharp}(C\cap D) $ to get

    $$\deg(\omega_S \otimes{\mathcal{O}}_S(C)\otimes{\mathcal{O}}_C) = \deg({\mathcal{O}}_S(C+K_C)\otimes{\mathcal{O}}_C) = {\sharp}(C \cap(C+K_C)).$$

- For $ C\hookrightarrow S $ a curve in a surface, what is $ \omega_C $?

    Idea: differential forms with (no?) poles along $ C $, and base change to $ {\mathcal{O}}_C $:

    $$\omega_S = (\omega_S \otimes{\mathcal{O}}_S(C))\otimes{\mathcal{O}}_C.$$

- What is the degree formula for a curve of degree $ d $ in $ {\mathbf{P}}^2 $?

    By adjunction,

    $$2g-2 = C.(C+K_C) = d(d-3)\implies g ={1\over 2}(d-1)(d-2).$$

- What is **Serre vanishing**?

    For $ X $ a Noetherian scheme, $ X $ is affine $ \iff H^{i>0}(X; {\mathcal{F}}) = 0 $ for all $ {\mathcal{F}}\in {\mathsf{QCoh}}(X) \iff H^1(X; {\mathcal{I}}) = 0 $ for all coherent sheaves of ideals on $ X $.

- What is a **dominant morphism**?

    For schemes: dense image.
