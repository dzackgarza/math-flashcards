---
title: "Algebraic Geometry::Schemes"
---

::: {.front card-id="card-e01d6cc90a3752e3" tags="definition"}
What is specialization/generization?
:::

::: {.back card-id="card-e01d6cc90a3752e3"}
For points $x,\tilde x$ of a scheme $X$, $x$ is a **specialization** of $\tilde x$ if $x\in\overline{\{\tilde x\}}$; write $\tilde x \leadsto x$ and say $\tilde x$ specializes to $x$. Equivalently, $\tilde x$ is a **generization** of $x$. In $\operatorname{Spec}R$, $\mathfrak p$ specializes to $\mathfrak q$ exactly when $\mathfrak p\subseteq\mathfrak q$.
:::

::: {.front card-id="card-11777c341e4d7e90"}
Give several concrete examples of schemes
:::

::: {.back card-id="card-11777c341e4d7e90"}
$V(xy)$ the union of axes, which is not irreducible.

$V(y^2-x^3)$ the cuspidal curve.

$V(x^2-y^2)$, the X-shaped space.

$V(y^2-x^3-x)$ the nodal curve

$V(y^2-ax^3-bx)$ a general elliptic curve.

The rational normal curves ${\mathbf{P}}^1\to {\mathbf{P}}^N$ given by the Veronese embedding $[x:y]\mapsto$ monomials of degree $d$, so $N = {n+d\choose d}$.

The twisted cubic $\operatorname{im}\qty{{\left[ {x:y} \right]} \to {\left[ {x^3: x^2 y : xy^2 : y^3} \right]} }$, cut out as $V(xz-y^2, yw-z^2, xw-yz)\subseteq {\mathbf{P}}^3$ (i.e. the image of Veronese ${\mathbf{P}}^1\to {\mathbf{P}}^3$). Equivalently the $d=3$ rational normal curve.

The dual numbers $\operatorname{Spec}k[{\varepsilon}]/{\varepsilon}^2$.

${\mathbf{A}}^1$ with a doubled origin (not separated)

The quadric surface $V(xy-zw) \subseteq {\mathbf{P}}^3$

$V(x^2+y^2-z^2)$ the double cone along the $z\dash$axis.

$\operatorname{Spec}R$ for any ring (obviously!)

$\operatorname{Spec}k$ is a point

$\operatorname{Spec}R$ for $R\in \mathsf{DVR}$ is 2 points: a closed point and a generic point.

The Whitney umbrella $V(x^2-y^2z)$.
:::

::: {.front card-id="card-a8ecd677d4355b6c"}
Give several concrete examples of morphisms of schemes.
:::

::: {.back card-id="card-a8ecd677d4355b6c"}
The normalization of the cuspidal curve $\eta:{\mathbf{A}}^1\to C$ where $t\mapsto (t^2, t^3)$.

$(x, y)\mapsto (x, xy)$ on ${\mathbf{A}}^2$

$x\mapsto x^n$ on ${\mathbf{G}}_m$

$V(xy-c) \to {\mathbf{A}}^1$ given by coordinate projection
:::

::: {.front card-id="card-6cd6fec72ba5a191"}
Give an example of a morphism of ringed spaces which is not induced by any ring morphism.
:::

::: {.back card-id="card-6cd6fec72ba5a191"}
Take $R$ a DVR, then $\operatorname{Spec}\operatorname{ff}(R) \to \operatorname{Spec}R$ sending the unique point to the closed point. This is not induced by any morphism $R\to \operatorname{ff}(R)$ since it is not a morphism of *locally* ringed spaces.
:::

::: {.front card-id="card-680201bc520b8457"}
What is a ringed space? Locally ringed spaces?
:::

::: {.back card-id="card-680201bc520b8457"}
$(X, {\mathcal{O}}_X)$ where $X\in \Top$ and a **structure sheaf** ${\mathcal{O}}_X\in \Sh(X, \mathsf{CRing})$. This is locally ringed if all stalks ${\mathcal{O}}_{X, x}$ have unique maximal ideals.
:::

::: {.front card-id="card-645aa342d2f0ce7b"}
What is a morphism of ringed spaces? Locally ringed spaces?
:::

::: {.back card-id="card-645aa342d2f0ce7b"}
Pairs $(f, f^\sharp)$ where $f\in \Top(X, Y)$ and $f^\sharp: {\mathcal{O}}_{Y} \to f_* {\mathcal{O}}_X$ is a map of sheaves of rings on $Y$. This is a morphism of locally ringed spaces iff for each $x\in X$ the induced stalk map $f^\sharp_x: {\mathcal{O}}_{Y, f(x)} \to {\mathcal{O}}_{X, x}$ is a local homomorphism, i.e. $f^\sharp_x( \mfm_{f(x)} ) \subseteq \mfm_x$.

Here a local homomorphism $\phi: (A, \mfm_A)\to (B, \mfm_B)$ is a ring map with $\phi(\mfm_A) \subseteq \mfm_B$; these are the morphisms of $\mathsf{Loc}\mathsf{Ring}$.
:::

::: {.front card-id="card-f5a08ee1e016720b"}
What is the definition of a scheme?
:::

::: {.back card-id="card-f5a08ee1e016720b"}
A locally ringed space $(X, {\mathcal{O}}_X)$ locally isomorphic to an affine scheme: every point $x$ admits an open neighborhood $U\ni x$ with $(U, { \left.{{{\mathcal{O}}_X}} \right|_{{U}} }) \cong (\operatorname{Spec}A, {\mathcal{O}}_{\operatorname{Spec}A})$ as locally ringed spaces for some ring $A$. Equivalently, $\exists \mcu\rightrightarrows X$ an open cover by such $U$.
:::

::: {.front card-id="card-93ee15a42cf7782e" tags="definition"}
What is the dimension of a scheme?
:::

::: {.back card-id="card-93ee15a42cf7782e"}
Supremum of lengths of chains $Z_0 \subsetneq Z_1 \subsetneq \cdots \subsetneq Z_n$ of distinct irreducible closed subsets of $X$, where the length is the number of *links* $n$. For $X=\operatorname{Spec}A$, this is the Krull dimension of $A$.
:::

::: {.front card-id="card-98f87625dc32d705" tags="definition"}
What is the Krull dimension of a ring?
:::

::: {.back card-id="card-98f87625dc32d705"}
Supremum of all lengths $n$ of chains of prime ideals $\mathfrak p_0\subsetneq\cdots\subsetneq\mathfrak p_n$ in $A$.
:::

::: {.front card-id="card-d706ceb0a1e4d9f3"}
What is an **affine scheme**? What are their morphisms?
:::

::: {.back card-id="card-d706ceb0a1e4d9f3"}
A locally ringed space $(X, {\mathcal{O}}_X)$ which is isomorphic to $(\operatorname{Spec}R, {\mathcal{O}}_{\operatorname{Spec}R})$ for some $R\in \mathsf{CRing}$. Morphisms are morphisms of *locally* ringed spaces, and maps $\operatorname{Spec}A\to \operatorname{Spec}B$ biject with ring maps $B\to A$.
:::

::: {.front card-id="card-3c2e2b84953088f7"}
How is ${\mathcal{O}}_X$ defined for an *affine scheme* $\operatorname{Spec}A$?
:::

::: {.back card-id="card-3c2e2b84953088f7"}
Sections: ${\mathcal{O}}(U)$ is the set of functions $s: U\to {\textstyle\coprod}_{\mfp\in U} A_\mfp$ with $s(\mfp) \in A_\mfp$ which are locally fractions: $\forall \mfp\in U, \exists V$ open with $\mfp\in V \subseteq U$ and $\exists a, f\in A$ such that for each $\mfq\in V$, $f\not\in \mfq$ and $s(\mfq) = a/f$ in $A_\mfq$.

Stalks: ${\mathcal{O}}_{\operatorname{Spec}A, \mfp} = A_\mfp\coloneqq S^{-1}A, S\coloneqq A\setminus\mfp$.

Global sections: $A$.
:::

::: {.front card-id="card-41b68915a379f240"}
What is a (quasi)projective scheme?
:::

::: {.back card-id="card-41b68915a379f240"}
Projective morphisms: $f:X\to Y$ factoring through a closed immersion $X\to {\mathbf{P}}^n_{/ {Y}}$

Quasiprojective morphisms: factoring through an *open* immersion.

(quasi)projective iff structure morphism is.
:::

::: {.front card-id="card-f95579b2ccf96d41"}
What is a **normal scheme**?
:::

::: {.back card-id="card-f95579b2ccf96d41"}
$X$ is normal iff irreducible and ${\mathcal{O}}_{X, x}$ is a normal ring at each point, i.e. reduced and integrally closed in its field of fractions.

A ring $R$ is integrally closed if every $s\in S \coloneqq\operatorname{ff}(R)$ is integral over $R$, i.e. $\exists f\in R[x]$ with $f(s) = 0$..
:::

::: {.front card-id="card-e4bb12b1e53ef9aa"}
What is the **normalization** of a scheme?
:::

::: {.back card-id="card-e4bb12b1e53ef9aa"}
Cover $\operatorname{Spec}A_i\rightrightarrows X$, let $K_i$ be the integral closure of $A_i$ in its fraction field, and glue $\operatorname{Spec}K_i$ together to get $\tilde X \to X$.
:::

::: {.front card-id="card-eee331be6492de45"}
Discuss the normalization.
:::

::: {.back card-id="card-eee331be6492de45"}
Exists for any reduced scheme, yields $f: \tilde X\to X$ an integral birational morphism (finite for varieties), always regular in codimension 1 so yields regular (thus smooth) curves and surfaces with only isolated singularities. Makes every finite birational morphism into $\tilde X$ an isomorphism.
:::

::: {.front card-id="card-571f6dddb3e98505"}
Give an example of a non-normal scheme.
:::

::: {.back card-id="card-571f6dddb3e98505"}
The cuspidal curve $V(y^2-x^3)$, since there is a finite birational morphism
$$\begin{align*}{\mathbf{A}}^1&\to X \\ t&\mapsto (t^2, t^3)\end{align*}$$
which is not an isomorphism. Similarly, the nodal cubic $V(y^2-x(x+1))$ is not normal since its parameterization $t\mapsto (f_1(t), f_2(t))$ which is not an isomorphism (2-to-1 at the node).
:::

::: {.front card-id="card-9b3ba2e73259c05c"}
What is the universal property of normalization?
:::

::: {.back card-id="card-9b3ba2e73259c05c"}
Every dominant $f:Z\to X$ factors through $\tilde X\to X$.
:::

::: {.front card-id="card-1a4004ebf4e453ee" tags="definition"}
What is the **reduced induced scheme structure** on a closed subset of a scheme?
:::

::: {.back card-id="card-1a4004ebf4e453ee"}
For a closed subset $Z\subseteq X$, there is a unique reduced closed subscheme $Z_{\mathrm{red}}\hookrightarrow X$ with underlying space $Z$.

For $X = \operatorname{Spec}A$: set $\mfa\coloneqq\bigcap_{\mfp\in Z}\mfp$, the intersection of all prime ideals in $Z$ (the radical ideal of functions vanishing on $Z$). Then $V(\mfa) = Z$, and $A/\mfa$ is reduced since $\mfa$ is radical, so $\operatorname{Spec}(A/\mfa)$ is the reduced closed subscheme on $Z$. Intersecting only the maximal ideals in $Z$ is wrong in general: for $A$ a DVR and $Z = \operatorname{Spec}A$ it gives the closed point.

For arbitrary schemes, cover $X$ by affines $U_i$ and put the above structure on $Z\cap U_i$. By uniqueness these agree on overlaps, so they glue to a closed subscheme of $X$ with underlying space $Z$.
:::

::: {.front card-id="card-83ac8aa1cdbd2198" tags="definition"}
What is an **integral scheme**?
:::

::: {.back card-id="card-83ac8aa1cdbd2198"}
$X$ is integral iff it is nonempty and ${\mathcal{O}}_X(U)$ is an integral domain for every nonempty open $U$.

Equivalently, $X$ is reduced and irreducible.

Equivalently, $X$ is nonempty and every nonempty affine open $\operatorname{Spec}R \subseteq X$ has $R$ an integral domain. A cover by spectra of domains is not enough: $\operatorname{Spec}k \amalg \operatorname{Spec}k$ has such a cover but is not irreducible.
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
For $X$ locally Noetherian, the rings ${\mathcal{O}}_{X, x}$ at closed points are all regular rings.
$$\dim_{\kappa(x)} {\mathbf{T}}_{X, x} = \operatorname{krulldim}R, R\coloneqq{\mathcal{O}}_{X, x} \qquad\forall x\in X, k \coloneqq R/\mfm_R$$
:::

::: {.front card-id="card-3a870899611e5f04"}
What does it mean to be **regular in codimension 1**?
:::

::: {.back card-id="card-3a870899611e5f04"}
Every local ring ${\mathcal{O}}_{X, x}$ of dimension 1 is regular, hence a DVR.

For rings: for every prime ideal $\mfp\in \operatorname{Spec}A$ of height 1, the localization $A_\mfp$ is regular, hence a DVR.
:::

::: {.front card-id="card-5e3188dbef9fc5a0"}
What are some examples of schemes that are regular in codimension 1?
:::

::: {.back card-id="card-5e3188dbef9fc5a0"}
Smooth varieties over a field: the local rings of closed points are regular, hence of all points, since they are localizations of the former.

Any Noetherian normal scheme: any local ring of dimension 1 is an integrally closed domain and hence regular.
:::

::: {.front card-id="card-c64f65eef56890b2" tags="definition"}
What is a **reduced scheme**?
:::

::: {.back card-id="card-c64f65eef56890b2"}
$X$ is reduced iff ${\mathcal{O}}_X(U)$ is a reduced ring for every open $U \subseteq X$, or equivalently every local ring ${\mathcal{O}}_{X, x}$ is reduced, where a ring $R$ is reduced iff it has no nonzero nilpotents.
:::

::: {.front card-id="card-17e3b6dd4ac0258d"}
What is a **quasicompact morphism**? A quasicompact scheme?
:::

::: {.back card-id="card-17e3b6dd4ac0258d"}
$f:Y\to X$ is quasicompact iff $\exists \mcv\rightrightarrows Y$ by open affine subschemes such that each $f^{-1}(V_i)$ is quasicompact as a space (i.e. every open cover admits a finite subcover).
:::

::: {.front card-id="card-041ea23b72922e69"}
What is a **locally Noetherian scheme**?
:::

::: {.back card-id="card-041ea23b72922e69"}
A scheme is **locally** Noetherian iff every $x\in X$ admits an open neighborhood $U_x\ni x$ such that $U_x = \operatorname{Spec}R_i$ with $R_i$ a Noetherian ring (ACC)
:::

::: {.front card-id="card-fb850108ac7bd9c3" tags="definition"}
What is a **Noetherian** scheme?
:::

::: {.back card-id="card-fb850108ac7bd9c3"}
A scheme is Noetherian iff locally Noetherian and quasicompact. Equivalently, it has a finite cover by open affines $\operatorname{Spec}A_i$ with each $A_i$ a Noetherian ring.
:::

::: {.front card-id="card-eeddc4ca51429133"}
What is a **separated scheme**?
:::

::: {.back card-id="card-eeddc4ca51429133"}
$X$ is separated iff its structure morphism $X\to \operatorname{Spec}\ZZ$ is a separated morphism, i.e. the diagonal $\Delta_{X/\operatorname{Spec}\ZZ}: X\to X \underset{\scriptscriptstyle {\ZZ} }{\times} X$ is a **closed immersion**.
:::

::: {.front card-id="card-d5feac6218f5093e"}
What is a **quasiseparated** scheme?
:::

::: {.back card-id="card-d5feac6218f5093e"}
$X$ is quasiseparated iff $X\to \operatorname{Spec}\ZZ$ is a quasiseparated morphisms, where $f:X\to Y$ is quasiseparated iff $\Delta_{X/Y}: X\to X \underset{\scriptscriptstyle {Y} }{\times} X$ is a quasicompact morphism.
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
A locally ringed space locally isomorphic to $(\operatorname{Spf}A, {\mathcal{O}}_{\operatorname{Spf}A})$ where $\operatorname{Spf}A$ is the formal spectrum of a ring -- roughly the completion of a Noetherian scheme $X_i$ along a closed subscheme $Y_i$, where one takes $Y$ as the space and $\projectivelim_n {\mathcal{O}}_X/\mci_Y^n$.
:::

::: {.front card-id="card-289455ed6aa37e98"}
What are some examples of smooth schemes?
:::

::: {.back card-id="card-289455ed6aa37e98"}
${\mathbf{A}}^n/S, {\mathbf{P}}^n/S$ are smooth of relative dimension $n$.

Over a field $k=\kbar$, smooth iff regular of dimension $n$.

For an irreducible separated scheme over a field $k =\kbar$, smooth iff nonsingular as a variety.
:::

::: {.front card-id="card-8c4813bcb8326a81"}
What is an example of a non-smooth scheme?
:::

::: {.back card-id="card-8c4813bcb8326a81"}
$V(x^2)\subseteq {\mathbf{A}}^1_{/ {k}}$,

$\operatorname{Spec}E$ over $\operatorname{Spec}k$ where $E$ is a nonseparable extension e.g. ${ \mathbf{F} }_p(t^{1\over p})$ over ${ \mathbf{F} }_p(t)$,

the cuspidal curve $V(y^2-x^3)$.
:::

::: {.front card-id="card-fb0795cc9324cabf"}
What is a **Gorenstein** scheme?
:::

::: {.back card-id="card-fb0795cc9324cabf"}
Locally Noetherian whose local rings are Gorenstein ($R$ such that $R$ has finite injective dimension in ${}_{R}\Mod$).
:::

::: {.front card-id="card-1259f228e463095e"}
What are some consequences of being Gorenstein?
:::

::: {.back card-id="card-1259f228e463095e"}
The canonical line bundle $K_X$ exists.
:::

::: {.front card-id="card-08f6008be740f673"}
What is a **local complete intersection**?
:::

::: {.back card-id="card-08f6008be740f673"}
For a closed subscheme $Y$ of ${\mathbf{P}}^n/k$: the ideal $I$ of $Y$ in $k[x_0,\cdots, x_n]$ can be generated by $r\coloneqq\operatorname{codim}_{{\mathbf{P}}^n}(Y)$ elements. Equivalent to $Y = \bigcap_{i=1}^r H_i$ for some hypersurfaces $H_i$ and thus $\mci_Y = \sum_{i=1}^r \mci_{H_i}$.

For an arbitrary closed subscheme $Y\leq X$ of a smooth variety: $Y$ is lci in $X$ iff $\mci_Y$ can be locally generated by $r\coloneqq\operatorname{codim}_{X}(Y)$ elements at every point $y\in Y$.
:::

::: {.front card-id="card-063a8348047c4935"}
What is a **Cohen-Macaulay** scheme?
:::

::: {.back card-id="card-063a8348047c4935"}
All local rings are Cohen-Macaulay: $A$ where $\mathrm{depth} A = \dim A$, where the depth is the maximal length of a regular sequence whose generates are in $\mfm_A$, and $\left\{{x_1,\cdots, x_n}\right\}$ is a regular sequence for $M\in   {}_{A}\Mod$ is $x_1$ is not a zero divisor in $M$ and $x_{i+1}$ is not a zero divisor in $M/I_iM$ where $I_i \coloneqq\left\langle{x_1,\cdots, x_i}\right\rangle$.
:::

::: {.front card-id="card-b1773b17df4126bf"}
What is a **scheme-theoretic intersection**?
:::

::: {.back card-id="card-b1773b17df4126bf"}
For relative schemes $X_i\to Y$, the intersection of $X_1$ and $X_2$ is the fiber product $X_1 { \underset{\scriptscriptstyle {Y} }{\times} } X_2$. For affines $X_1 = R/J_1$ and $X_2 = R/J_2$, this is realized by
$$\operatorname{Spec}(R/J_1 \otimes_R R/J_2) \cong \operatorname{Spec}R/(J_1 + J_2).$$
If $X_i \hookrightarrow Y$ are closed subschemes, then the intersection is again a closed subscheme of $Y$..
:::

::: {.front card-id="card-f6688f63a2714f98"}
What is an **open subscheme**?
:::

::: {.back card-id="card-f6688f63a2714f98"}
A scheme $U$ with ${\left\lvert {U} \right\rvert} \subseteq {\left\lvert {X} \right\rvert}$ is an open subspace where ${\mathcal{O}}_{U} \cong { \left.{{{\mathcal{O}}_X}} \right|_{{U}} }$.
:::

::: {.front card-id="card-4c3df89f2859bc57" tags="definition"}
What is the **residue field** at a point $x\in X$?
:::

::: {.back card-id="card-4c3df89f2859bc57"}
$\kappa(x) \coloneqq{\mathcal{O}}_{X, x}/\mfm_x$. If $U = \operatorname{Spec}A \ni x$ and $\mfp\in \operatorname{Spec}A$ corresponds to $x$, then $\kappa(x) = A_\mfp/ \mfp A_\mfp$, the fraction field of $A/\mfp$.
:::

::: {.front card-id="card-d78d46215a60b1cb"}
What is the **scheme associated to a variety**?
:::

::: {.back card-id="card-d78d46215a60b1cb"}
Use the functor $t: \Var_{/ {k}}\to \Sch_{/ {k}}$, then $V$ is homeomorphic to the closed points in ${\left\lvert {t(V)} \right\rvert}$ and ${\mathcal{O}}_V \cong { \left.{{ {\mathcal{O}}_{t(V)}}} \right|_{{t(V)^\cl}} }$, i.e. the regular functions on $V$ are restrictions to closed points of the structure sheaf of $t(V)$.

Generally $t(V)$ is the set of nonempty irreducible closed subsets of $V$, define the images of such sets to be closed sets to form a topology.
:::

::: {.front card-id="card-93365011b44724e2" tags="definition"}
What is the **Proj construction**?
:::

::: {.back card-id="card-93365011b44724e2"}
For $S = \bigoplus_{d\geq 0} S_d$ a graded ring, write $S_+ \coloneqq\bigoplus_{d\geq 1} S_d$ and let $\mathop{\mathrm{Proj}}S$ be the set of homogeneous prime ideals of $S$ which do not contain $S_+$. The closed sets are $V(\mfa) \coloneqq\left\{{P\in \mathop{\mathrm{Proj}}S \st P \supseteq\mfa}\right\}$ for $\mfa$ a homogeneous ideal.

For the structure sheaf, for each $p\in \mathop{\mathrm{Proj}}S$ define $S_{(p)}$ to be the elements of degree zero in the localization $S[T^{-1}]$ where $T$ is the set of all homogeneous elements of $S$ which are not in $p$, and define ${\mathcal{O}}(U)$ to be functions $s: U\to \amalg_{p\in U} S_{(p)}$ with $s(p) \in S_{(p)}$ and $s$ locally a fraction: $s(q) = a/f$ with $a,f\in S$ homogeneous of the same degree and $f\not\in q$.

The basic opens $D_+(f)$, for $f$ homogeneous of positive degree, satisfy $D_+(f)\cong\operatorname{Spec}(S_f)_0$.
:::

::: {.front card-id="card-6cdb91f28276b7cc"}
What is ${\mathbf{A}}^n_{/ {R}}$ as a scheme?
:::

::: {.back card-id="card-6cdb91f28276b7cc"}
$\operatorname{Spec}R[x_1,\cdots, x_n]$ or ${\mathbf{A}}^n_{/ {\ZZ}} \underset{\scriptscriptstyle {\ZZ} }{\times} \operatorname{Spec}R$.
:::

::: {.front card-id="card-0fa32d3a60ede40b"}
How are morphisms $X\to {\mathbf{A}}^n_{/ {S}}$ characterized?
:::

::: {.back card-id="card-0fa32d3a60ede40b"}
A choice of $n$ sections $h_1,\cdots,h_n \in H^0(X; {\mathcal{O}}_X)$.
:::

::: {.front card-id="card-acdb021d5d026890" tags="unsorted"}
How is ${\mathbf{P}}^n/S$ defined for $S$ a scheme?
:::

::: {.back card-id="card-acdb021d5d026890"}
Define $\PP^n/\ZZ \definedas \Proj \ZZ[x_0, \cdots, x_n]$ and $\PP^n/S \definedas \fiberprod{\PP^n/\ZZ}{\ZZ}{S}$.
:::

::: {.front card-id="card-98c1f9a1ecd625ba"}
What is the **reduced scheme** associated to a scheme?
:::

::: {.back card-id="card-98c1f9a1ecd625ba"}
For $(X, {\mathcal{O}}_X)\in \Sch$, sheafify $U\mapsto {\mathcal{O}}_X(U)^{ \text{red} }$ where $R^{ \text{red} }\coloneqq R/{\sqrt{0_{R}} }$ is the quotient by the ideal of nilpotent elements to get ${\mathcal{O}}_{X}^{ \text{red} }$.
:::

::: {.front card-id="card-a193384cad51473e" tags="definition"}
What is an **irreducible** scheme?
:::

::: {.back card-id="card-a193384cad51473e"}
Irreducible as a topological space: nonempty and not the union of two proper closed subsets. Equivalently, any two nonempty open subsets meet.
:::

::: {.front card-id="card-1f9ebf5ac271403c"}
What is an $n\dash$fold point over $k$?
:::

::: {.back card-id="card-1f9ebf5ac271403c"}
A scheme $\operatorname{Spec}R\to \operatorname{Spec}k$ with one point such that $R$ is a $k\dash$algebra of dimension $n$.
:::

::: {.front card-id="card-a2844b113bfce411"}
What is a **dominant morphism**?
:::

::: {.back card-id="card-a2844b113bfce411"}
$f:X\to S$ with $f(X) \subseteq S$ dense. For integral schemes, equivalently: $f$ maps the generic point of $X$ to the generic point of $S$; or the maps on sections ${\mathcal{O}}_S(V)\to{\mathcal{O}}_X(f^{-1}(V))$ are injective for all open $V$; or the maps of local rings ${\mathcal{O}}_{S, f(x)}\to{\mathcal{O}}_{X, x}$ are injective for all $x\in X$.
:::

::: {.front card-id="card-134f85a8c9a41dbd" tags="definition"}
What is the **fiber product** of schemes?
:::

::: {.back card-id="card-134f85a8c9a41dbd"}
For maps $X\to S$ and $Y\to S$, the fiber product $X\times_S Y$ represents pairs of maps to $X$ and $Y$ whose composites to $S$ agree: $\operatorname{Hom}_S(T,X\times_S Y)\cong\operatorname{Hom}_S(T,X)\times\operatorname{Hom}_S(T,Y)$. For affine schemes, $\operatorname{Spec}A\times_{\operatorname{Spec}R}\operatorname{Spec}B\cong\operatorname{Spec}(A\otimes_R B)$.
:::

::: {.front card-id="card-8291e7f9a2f63d07"}
What does it mean to *evaluate* a prime ideal $\mfp\normal R$ at an element $f\in R$?
:::

::: {.back card-id="card-8291e7f9a2f63d07"}
Take the image of $f$ under the natural map $R \to R/\mfp\to \kappa(\mfp)$ where $\kappa(\mfp) \coloneqq\operatorname{ff}(R/\mfp) \cong R_\mfp/\mfp R_\mfp$ is the residue field of the local ring $R_\mfp$.
:::

::: {.front card-id="card-0f8f55d06116c7b8"}
Characterize maps $\operatorname{Spec}L \to X$ for $L$ a field.
:::

::: {.back card-id="card-0f8f55d06116c7b8"}
Equivalent to giving a point $x\in X$ and an inclusion $\kappa(x) \hookrightarrow L$ of the residue field into $L$.
:::

::: {.front card-id="card-eb9cd3c92698f1bf"}
Characterize maps $\operatorname{Spec}k[{\varepsilon}]/{\varepsilon}^2\to X$.
:::

::: {.back card-id="card-eb9cd3c92698f1bf"}
Giving a rational point $x\in X$, so $\kappa(x) = k$, and an element of ${\mathbf{T}}_x \coloneqq(\mfm_x/\mfm_x)^2$.
:::

::: {.front card-id="card-618a12ae0264b25f"}
For $X\to S$ a scheme, what is a $T\dash$valued point of $X$ for $T$ a scheme?
:::

::: {.back card-id="card-618a12ae0264b25f"}
A scheme morphism $T\to X$.
:::

::: {.front card-id="card-fdb0e1a6a993fc2f"}
What is a **generic point**?
:::

::: {.back card-id="card-fdb0e1a6a993fc2f"}
A point $\eta \in X$ such that $\cl_X \eta = X$.
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
For an affine scheme $\operatorname{Spec}A$, a point corresponding to a maximal ideal $m\in \operatorname{mSpec}A$.
:::

::: {.front card-id="card-1b1f50cd7d0bfd9e"}
What is a **rational point**?
:::

::: {.back card-id="card-1b1f50cd7d0bfd9e"}
For a scheme defined over $k$, any point $x\in X$ with $\kappa(x) { \, \xrightarrow{\sim}\, }k$.
:::

::: {.front card-id="card-dd6a17b3b5ccabe1"}
What are the **singular points** of the scheme?
:::

::: {.back card-id="card-dd6a17b3b5ccabe1"}
Points $x$ at which ${\mathcal{O}}_{X, x}$ is not a regular local ring, where $(A, \mfm_A)$ is regular iff $\dim_{\kappa(A)} \mfm_A/\mfm_A^2 = \dim A$ where $\kappa(A)$ is the residue field of $A$.
:::

::: {.front card-id="card-dc477b6237cb1cc7"}
What is **base change**?
:::

::: {.back card-id="card-dc477b6237cb1cc7"}
For $X\in\Sch_{/ {S}}$ and $T\to S$ a morphism of schemes, the pullback $X  \underset{\scriptscriptstyle {S} }{\times} T$.
:::

::: {.front card-id="card-fa0b786697fe09b6"}
What does it mean to be **stable under base change**?
:::

::: {.back card-id="card-fa0b786697fe09b6"}
If $f:X\to S$ has property $P$ and $\phi: T\to S$ then $\tilde f: X \underset{\scriptscriptstyle {S} }{\times}T\to T$ again has property $P$.
:::

::: {.front card-id="card-d190eb30a79c7d19"}
What does it mean to be **local on the base**?
:::

::: {.back card-id="card-d190eb30a79c7d19"}
For $f:X\to Y$, property $P$ is local on the base iff $\exists V_i\rightrightarrows Y$ with $f^{-1}(V_i)\to V_i$ having property $P$.
:::

::: {.front card-id="card-c568a40234fbb420"}
What is the **codimension** of a subset of a scheme?
:::

::: {.back card-id="card-c568a40234fbb420"}
For an irreducible closed $Z\subseteq X$, the supremum over lengths of chains $Z= Z_0 \subseteq Z_1 \subseteq \cdots \subseteq Z_n$ of distinct irreducible closed subsets of $X$. For an arbitrary closed subset $Y$, take the infimum over all irreducibles $Z \subseteq Y$.
:::

::: {.front card-id="card-bc6d4901d6074616"}
What is the **geometric genus** of a scheme?
:::

::: {.back card-id="card-bc6d4901d6074616"}
For $X$ smooth projective, far left side of the Hodge diamond:
$$p_g \coloneqq h^0(X; \Omega_X^n) = h^0(\omega_X) = h^0(K_X) = h^{n, 0}$$
:::

::: {.front card-id="card-a61d8207edb6dea5"}
Discuss the geometric genus.
:::

::: {.back card-id="card-a61d8207edb6dea5"}
For $X$ smooth projective, $p_g(X) = h^{n, 0} = h^0(\operatorname{det}\Omega_X) = h^0(K_X)$; it is a birational invariant. For curves, $p_g(X) = h^{1,0} = h^{0, 1} = h^1({\mathcal{O}}_X)$ and
$$p_a = (-1)^{\dim X}(\chi({\mathcal{O}}_X) - 1) = -1(h^0({\mathcal{O}}_X) - h^1({\mathcal{O}}_X) - 1) = -1(1-p_g(X) - 1) = p_g(X)$$
$p_a(X) \neq p_g(X)$ in general: take $Y$ a cubic plane curve and $X\coloneqq Y\times Y$, then $p_g(X) = 1$ but $p_a(X) = -1$.

For singular curves, define $p_g(C) \coloneqq p_g(\tilde C)$ where $\tilde C$ is the normalization.

For an irreducible plane curve, $g = {1\over 2}(d-1)(d-2) - s$ where $s$ is a count of singularities with multiplicity.
:::

::: {.front card-id="card-48c0d3ff41bea326"}
What is Bertini's theorem? Give a consequence.
:::

::: {.back card-id="card-48c0d3ff41bea326"}
Idea: a generic hyperplane section of a smooth projective variety is again smooth.

For $k = \overline{k}$ and $X\subseteq {\mathbf{P}}^n_{/ {k}}$ a smooth projective variety (closed subvariety of ${\mathbf{P}}^n$), there is a hyperplane $H$ not containing $X$ such that the hyperplane section $H\cap X$ is regular at every point. The set of $H$ with this property is an open dense subset of the complete linear system ${\left\lvert {H} \right\rvert}$ (regarded as a projective space). If $\dim X \geq 2$ then $H\cap X$ is moreover connected, hence irreducible, so it is again a smooth projective variety.

Consequence: iterating, every smooth projective variety of dimension $\geq 2$ contains smooth irreducible curves, cut out by general hyperplane sections.
:::

::: {.front card-id="card-f6e2da3ec9f4c267"}
Let $Y\leq X$ be a smooth codimension $r$ subvariety, discuss $\omega_Y$.
:::

::: {.back card-id="card-f6e2da3ec9f4c267"}
$\omega_Y \cong \omega_X \otimes\bigwedge\nolimits^r \mathbf{N}_{Y/X}$, and if $r=1$ this recovers $\omega_Y\cong \omega_X \otimes{\mathcal{O}}(Y) \otimes{\mathcal{O}}_Y$ where $Y$ is considered a divisor.
:::

::: {.front card-id="card-00224b008d0de86d"}
Compute $\omega_X$ and $p_g$ for $X = {\mathbf{P}}^n_{/ {k}}$.
:::

::: {.back card-id="card-00224b008d0de86d"}
Start with $0\to {\mathcal{O}}_X \to {\mathcal{O}}_X(1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  } \to {\mathbb{T}}_X\to 0$, dualize to get $0 \rightarrow \Omega_{X / Y} \rightarrow \mathcal{O}_X(-1)^{n+1} \rightarrow \mathcal{O}_X \rightarrow 0$, take determinants to get $\omega_X \cong {\mathcal{O}}_X(-n-1)$.

This has not sections if $n\geq 1$ so $p_g = 0$.
:::

::: {.front card-id="card-319a35d07535844b"}
What is a **geometrically connected** scheme?
:::

::: {.back card-id="card-319a35d07535844b"}
A scheme that is connected and does not become disconnected after base change: for $X\in \Sch_{/ {k}}$, for every extension $L$ of $k$, require that $X \underset{\scriptscriptstyle {k} }{\times} L$ is connected.
:::

::: {.front card-id="card-fae8e7095295f561" tags="definition"}
What is: Ringed spaces and their morphisms
:::

::: {.back card-id="card-fae8e7095295f561"}
A ringed space is a topological space $X$ with a sheaf of rings $\mathcal O_X$. A morphism $(X,\mathcal O_X)\to(Y,\mathcal O_Y)$ is a continuous map $f$ with a sheaf map $f^\#:\mathcal O_Y\to f_*\mathcal O_X$. It is locally ringed if the stalk maps are local homomorphisms.
:::

::: {.front card-id="card-943a2df5418e9de9" tags="definition"}
What is the **structure sheaf** of a scheme?
:::

::: {.back card-id="card-943a2df5418e9de9"}
Part of the definition of a scheme as a locally ringed space $(X, \mathcal O_X)$: $\mathcal O_X$ is the structure sheaf, a sheaf of rings recording the regular functions locally on $X$. On $X=\operatorname{Spec}A$, $\mathcal O_X(D(f))=A_f$, and the stalk at $\mathfrak p$ is $A_{\mathfrak p}$.
:::

::: {.front card-id="card-8b388f202394fece" tags="definition"}
What is: Generic points and closed points
:::

::: {.back card-id="card-8b388f202394fece"}
A point $\eta$ is generic for a closed subset $Z$ if $\overline{\{\eta\}}=Z$. A point $x$ is closed if $\{x\}$ is closed. In $\operatorname{Spec}A$, $\mathfrak p$ is closed exactly when it is maximal, and the generic point of $V(\mathfrak p)$ is $\mathfrak p$.
:::

::: {.front card-id="card-03a12cd80ccb7400" tags="definition"}
What is: Definitions of affine/projective/general schemes
:::

::: {.back card-id="card-03a12cd80ccb7400"}
An affine scheme is $\operatorname{Spec}A$ for a ring $A$. A scheme is a locally ringed space covered by open affine schemes. A projective scheme over $S$ admits a closed immersion into $\mathbb P_S^n$ for some $n$; the term also has a relative $\operatorname{Proj}$ formulation.
:::

::: {.front card-id="card-870c96f4b6081b54" tags="definition"}
What is: Normal schemes and normalization
:::

::: {.back card-id="card-870c96f4b6081b54"}
A ring $R$ with field of fractions $K$ is **normal** if every element of $K$ which is integral over $R$ (i.e. a root of monic polynomial in $R[x]$ ) is actually in $R$.

A scheme $X$ is **normal** if all its local rings $\mathcal{O}_{X, p}$ are normal domains; a variety $X$ is **normal** if it is irreducible and the local rings $\mathcal{O}_{X, p}$ are normal for all $p \in X$.

The **normalization** of an integral scheme $X$: cover $X$ by affines $\operatorname{Spec}A_i$, let $\tilde A_i$ be the integral closure of $A_i$ in the function field $K(X)$, and glue the $\operatorname{Spec}\tilde A_i$ to get $\nu: \tilde X\to X$. Then $\tilde X$ is normal and integral, $\nu$ is integral and birational (finite for varieties), and every dominant morphism $Z\to X$ from a normal integral scheme $Z$ factors uniquely through $\nu$.
:::

::: {.front card-id="card-7b6fdb224bdd77f2"}
What is a **regular immersion**?
:::

::: {.back card-id="card-7b6fdb224bdd77f2"}
An immersion whose sheaf of ideals is regular, where $\mci\leq {\mathcal{O}}_X$ is regular iff for every $x\in \mathop{\mathrm{supp}}({\mathcal{O}}_X/\mci)$ admits an open neighborhood $U$ and a regular sequence $f_1,\cdots, f_r\in {\mathcal{O}}_X(U)$ generating ${ \left.{{\mci}} \right|_{{U}} }$.
:::

::: {.front card-id="card-f6ef6d64003c7e76"}
What are consequences of a morphism being flat?
:::

::: {.back card-id="card-f6ef6d64003c7e76"}
The Hilbert polynomials of all fibers are the same.

If $f:X\to Y$ with $X,Y$ finite type over a field, $\dim_x X_y = \dim_x X - \dim_y Y$ where $\dim_x X \coloneqq\dim {\mathcal{O}}_{X, x}$.

For $\mcx\to C^\circ$ a flat family of closed subschemes of ${\mathbf{P}}^n$ over a punctured curve $C^\circ$, one can "pass to the limit": given $Y$ regular integral of dimension 1 and $p\in Y$ a closed point, let $Y^\circ \coloneqq Y\setminus\left\{{ p }\right\}$ and $X\subseteq {\mathbf{P}}^n_{Y^\circ}$ be a closed subscheme which is flat over $Y^\circ$; then $\exists ! \tilde X \subseteq {\mathbf{P}}^n_{Y}$ a closed subscheme flat over $Y$ which restricts to $X$.
:::

::: {.front card-id="card-f29f14b3c651a2c2"}
Give an example and a non-example of a flat morphism.
:::

::: {.back card-id="card-f29f14b3c651a2c2"}
Example: any open immersion, $\tilde M$ over $A$ for any $M \in   {}_{A}\Mod^\flat$. Any smooth morphism by miracle flatness Non-example: any blowup, since the fibers jump in dimension.
:::

::: {.front card-id="card-069f1fe38915b1c4"}
What is an **associated point**?
:::

::: {.back card-id="card-069f1fe38915b1c4"}
$x\in X$ where every element of $\mfm_x$ is a zero divisor.
:::

::: {.front card-id="card-1f647ebbef5efd37"}
What is a **flat family**?
:::

::: {.back card-id="card-1f647ebbef5efd37"}
Any morphism $\mcx\to X$ of schemes to $X$ which is flat.
:::

::: {.front card-id="card-3c776a71df041421"}
How can one check if a morphism is flat?
:::

::: {.back card-id="card-3c776a71df041421"}
For $f: X\to Y$ with $Y$ integral and regular of dimension 1, $f$ is flat iff every *associated point* maps to $\eta_Y$. For $X$ reduced, this says every irreducible component of $X$ dominates $Y$.
:::

::: {.front card-id="card-16b1ac8dbea48ede"}
What are some properties not preserved in a flat family?
:::

::: {.back card-id="card-16b1ac8dbea48ede"}
Being irreducible or reduced, Picard numbers, generally most things that aren't related to Hilbert polynomials.
:::

::: {.front card-id="card-d09c4ef4014a45e1"}
Discuss the image of a flat morphism.
:::

::: {.back card-id="card-d09c4ef4014a45e1"}
Always open.
:::

::: {.front card-id="card-63efc03dbb2b7a94"}
How does a morphism of rings induce an algebra structure?
:::

::: {.back card-id="card-63efc03dbb2b7a94"}
$f:R\to S$ induces $S\in   {}_{R}\Mod$ via $r.s \coloneqq f(r)s$.
:::

::: {.front card-id="card-7f48b0ac525a085c"}
What is an **open immersion** of schemes?
:::

::: {.back card-id="card-7f48b0ac525a085c"}
$f:X\to Y$ inducing $X\cong U \subseteq Y$ with $U$ an open subscheme, where $U\subseteq Y$ is an open scheme iff ${\left\lvert {U} \right\rvert} \subseteq {\left\lvert {Y} \right\rvert}$ and ${\mathcal{O}}_U \cong { \left.{{{\mathcal{O}}_Y}} \right|_{{U}} }$.
:::

::: {.front card-id="card-86f3fc66ea0fc489"}
What is a **closed immersion** of schemes?
:::

::: {.back card-id="card-86f3fc66ea0fc489"}
$f:X\to Y$ inducing a homeomorphism $\tilde f: {\left\lvert {X} \right\rvert} \to {\left\lvert {V} \right\rvert}$ for ${\left\lvert {V} \right\rvert} \subseteq {\left\lvert {Y} \right\rvert}$ a closed subspace of the underlying topological spaces, such that $f^\sharp: {\mathcal{O}}_Y \twoheadrightarrow f_* {\mathcal{O}}_X$ is a surjective map of sheaves.

Equivalently, separates points and tangent vectors, i.e. $p\neq q$ closed points in $X \implies \exists s\in \mfm_p \mcl_p \setminus\mfm_q \mcl_q$, and $\left\{{s\in V \st s_p\in \mfm_p \mcl_p}\right\}$ spans $\mfm_p \mcl_p/\mfm_p^2 \mcl_p$, where $\phi: X\to {\mathbf{P}}^n_{/ {k}}$ corresponds to $\mcl$ and $\left\{{s_0, \cdots, s_n}\right\}\in H^0(X; \mcl)$.
:::

::: {.front card-id="card-fa8d17dce5d4f805"}
What is a **closed subscheme**?
:::

::: {.back card-id="card-fa8d17dce5d4f805"}
An equivalence class of closed immersions, where $f\sim g$ if they fit into a commuting triangle.
:::

::: {.front card-id="card-478d4dd2b52b290a"}
What is the fiber of a morphism $f:X\to Y$?
:::

::: {.back card-id="card-478d4dd2b52b290a"}
$f_y \coloneqq X \underset{\scriptscriptstyle {Y} }{\times} \operatorname{Spec}\kappa(y)$
:::

::: {.front card-id="card-8313983abf999469"}
What is a **smooth morphism**?
:::

::: {.back card-id="card-8313983abf999469"}
Locally of finite presentation, flat, and regular geometric fibers. (LFP: open cover where $R\to A$ is fp, so $\exists\, R[x_1, \cdots, x_n] \twoheadrightarrow A$).

Smooth implies regular.

For ring maps: $f:R\to A$ of finite presentation with $\tau_{\leq 1}{\mathbb{L}}_{A/R} \cong M[0]$ with $M\in   {}_{A}\Mod$ some finite projective (i.e. the naive cotangent complex is quasi-isomorphic to a projective module in degree zero). For schemes: smooth at $x \iff \exists U = \operatorname{Spec}A \ni x$ and $V = \operatorname{Spec}R \supseteq f(U)$ such that the induced ring map $R\to A$ is a smooth ring map.

Sufficient condition: flat, locally of finite presentation, smooth fibers (i.e. for all $a\in A$, the fiber $R \underset{\scriptscriptstyle {A} }{\times}\kappa(a)$ is a smooth scheme over $\kappa(a)$).

Equivalently, $\Omega_{R/A}$ is locally free of finite rank equal to $\operatorname{reldim}R/A$ (roughly: $\dim f^{-1}(a)$).
:::

::: {.front card-id="card-e504a4da2d4624f3"}
What is a **smooth morphism** of relative dimension $n$?
:::

::: {.back card-id="card-e504a4da2d4624f3"}
(Hartshorne, for schemes of finite type over $k$) $f: X\to Y$ such that

1. $f$ is flat;
2. $\dim X' = \dim Y' + n$ for all irreducible components $X'\subseteq X$ and $Y'\subseteq Y$ with $f(X')\subseteq Y'$;
3. $\dim_{\kappa(x)}(\Omega_{X/Y}\otimes\kappa(x)) = n$ for each point $x\in X$ (closed or not).

For $Y$ irreducible and $f$ flat, condition 2 is equivalent to: every irreducible component of every fiber $X_y$ of $f$ has dimension $n$.

For $X$ integral, condition 3 can be replaced with: $\Omega_{X/Y}$ is locally free of rank $n$.

Closed under base change, composition, fiber products.
:::

::: {.front card-id="card-c018f8b2b38ac42f"}
How is smoothness related to regularity?
:::

::: {.back card-id="card-c018f8b2b38ac42f"}
Over $k = \kbar$, $X$ is smooth of relative dimension $n$ over $\operatorname{Spec}k$ $\iff X$ is regular of dimension $n$.
:::

::: {.front card-id="card-4956b7d16253f682"}
What is generic smoothness?
:::

::: {.back card-id="card-4956b7d16253f682"}
For $f:X\to Y\in \Var_{/ {k}}, \operatorname{ch}k = 0$ with $X$ smooth, then there is a nonempty open $V\subseteq Y$ such that ${ \left.{{f}} \right|_{{f^{-1}(V)}} }$ is a smooth morphism.
:::

::: {.front card-id="card-5706d972b05f5073"}
Give an example a morphism that is not smooth.
:::

::: {.back card-id="card-5706d972b05f5073"}
Let $\operatorname{ch}k = p, k=\kbar$ and take the Frobenius morphism $f:X\to Y$ to $X=Y={\mathbf{P}}^n_{/ {k}}$.

Since $d(t^p)=0$, the map $f^*\Omega_{Y/k}\to \Omega_{X/k}$ is zero and $\Omega_{X/Y} \cong \Omega_{X/k}$ is locally free of rank 1 but $\operatorname{reldim}f = 0$, so $f$ is nowhere smooth.
:::

::: {.front card-id="card-7cf150912ca6e3c0"}
What is a consequence of smoothness?
:::

::: {.back card-id="card-7cf150912ca6e3c0"}
Smooth morphisms are flat, and smooth fibers implies this is a flat family of smooth schemes.
:::

::: {.front card-id="card-525d10c2757e41de" tags="unsorted"}
What is a proper morphism? What are some consequences?
:::

::: {.back card-id="card-525d10c2757e41de"}
A morphism of schemes is proper if it is separated, of finite type, and universally closed. For a morphism of varieties $\phi: X \rightarrow Y$, separated and finite type are automatic, so $\phi$ is proper iff it is universally closed: for all $\psi: Z \rightarrow Y$, the base change $\phi^{\prime}: X \times_Y Z \rightarrow Z$ is a closed map in the Zariski topology.

Equivalently, for $f$ of finite type and quasi-separated, use the valuative criterion ($=1$ lift).

Consequences:

- $X$ is complete iff the structure morphism to a point is proper.
- Fibers of a proper morphism are complete.
- Inverse images of complete subvarieties of $Y$ are complete.
- Any morphism obtained by base change from a proper morphism is proper.
:::

::: {.front card-id="card-07e3a111761ae76e"}
How is it related to **completeness**?
:::

::: {.back card-id="card-07e3a111761ae76e"}
A variety $X$ is complete if $X\to \operatorname{Spec}k$ is proper, i.e. a proper variety (integral separated scheme of finite type over a field) is complete.
:::

::: {.front card-id="card-40289dd013dd96ec"}
How is this related to Hausdorff + compactness properties?
:::

::: {.back card-id="card-40289dd013dd96ec"}
$X/\CC$ is complete iff $X$ is compact in the analytic topology
:::

::: {.front card-id="card-a484edc8e6016938"}
What is an **etale** morphism $f:X\to Y\in \Sch_{/ {k}}$?
:::

::: {.back card-id="card-a484edc8e6016938"}
Fully general: flat, finite type, unramified.

Smooth of relative dimension 0.

Flat and $\Omega_{X/ Y} = 0$.

For varieties: flat and unramified.
:::

::: {.front card-id="card-e9ced257a3fb0b70"}
What is an **unramified** morphism?
:::

::: {.back card-id="card-e9ced257a3fb0b70"}
For every $x\in X$, $f^\sharp(\mfm_{f(x)}) \cdot {\mathcal{O}}_{X, x} \cong\mfm_x$ where $f^\sharp: {\mathcal{O}}_{Y, f(x)}\to {\mathcal{O}}_{X, x}$, and $\kappa(x)/\kappa(y)$ is a separable algebraic extension.

Equivalently, $f:X\to Y$ with $\Omega_{X/Y} = 0$.

Equivalently, $f$ locally of finite presentation and the diagonal is an open immersion.

For curves: $\exists e_p\in \ZZ_{\geq 0}$ such that $f^\sharp(\mfm_{f(p)}) {\mathcal{O}}_{X, x} = \mfm_{x}^{e_p}$, and unramified iff $e_p = 1$ for all $p\in X$.

Flat + unramified = etale.
:::

::: {.front card-id="card-b00d12404bc086fb"}
What is a **flat** morphism?
:::

::: {.back card-id="card-b00d12404bc086fb"}
For projective varieties: the induced maps on stalks are flat ring maps.

$f: X\to S$ is flat at $x$ iff ${\mathcal{O}}_{X, x} \in   {}_{{\mathcal{O}}_{S, f(x) } }\Mod^\flat$ (i.e. the module structure induced by $f$ yields a flat module.)

Hartshorne's definition: for $f:X\to Y$ and $\mcf\in  {}_{{\mathcal{O}}_X}\Mod$, $\mcf$ is flat over $Y$ at $x\in X$ if $\mcf_x \in   {}_{{\mathcal{O}}_{Y, f(x)}}\Mod^\flat$; flat if flat at every $x\in S$, and $X$ is flat over $Y$ if $\mcf\coloneqq{\mathcal{O}}_X$ is flat.

$f\in \mathsf{CRing}(A, B)$ is a flat map iff $B\in   {}_{A}\Mod^\flat$, and a morphism $f\in \Sch(X, Y)$ is flat iff flat on local rings, i.e. $f_x: {\mathcal{O}}_{Y, f(x)}\to {\mathcal{O}}_{X, x}$ is flat.
:::

::: {.front card-id="card-da88a614473cf4db"}
What are some consequences of flatness?
:::

::: {.back card-id="card-da88a614473cf4db"}
Numerical invariants remain constant in flat families, e.g. the dimensions of fibers and their hilbert polynomials.

Defining $\dim_x X \coloneqq\dim {\mathcal{O}}_{X, x}$, if $f:X\to Y$ is flat then $\dim_x X_{f(x)} = \dim_x X - \dim_{f(x)} Y$.

If $B$ is smooth 1-dimensional affine, $X\to B$ is a family, and $0\in B$ is a closed point, $\lim_{b\to 0} X_b = X_0$ where $\lim_{b\to 0} X_b \coloneqq\overline{X_0}$, the fiber over $0$.
:::

::: {.front card-id="card-7eb3cab7d1016342"}
Given an example of a non-flat morphism.
:::

::: {.back card-id="card-7eb3cab7d1016342"}
$\operatorname{Bl}_0 {\mathbf{A}}^2 \xrightarrow{\pi} {\mathbf{A}}^2$, since ${\sharp}\pi^{-1}(p) = 1$ for all $p\neq 0$ and $\pi^{-1}(0)\cong {\mathbf{P}}^1$, contradicting equidimensionality.

Take a nodal curve $X$ and $f:\tilde X\to X$ its normalization -- if this were flat, $f_* {\mathcal{O}}_{\tilde X}$ would be a flat sheaf of ${\mathcal{O}}_X\dash$modules, which is coherent and thus locally free, and rank 1 and thus invertible; however the node $q$ has two preimages $p_1, p_2$, so $(f_* {\mathcal{O}}_{\tilde X})_q$ needs two generators as an ${\mathcal{O}}_X\dash$module.

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
A finite ring morphism $f:R\to A$ is one that makes $A\in   {}_{R}\Mod^\fg$.
:::

::: {.front card-id="card-50c3a5b5a43dbd56" tags="definition"}
What is a **finite morphism**?
:::

::: {.back card-id="card-50c3a5b5a43dbd56"}
Hartshorne: $f:X\to Y$ where $\operatorname{Spec}B_i\rightrightarrows Y$ is an open affine cover with each $f^{-1}(\operatorname{Spec}B_i) = \operatorname{Spec}A_i$ affine and $A_i \in   {}_{B_i}\Mod^\fg$. Equivalently, for every affine open $V=\operatorname{Spec}A\subseteq Y$, $f^{-1}(V)=\operatorname{Spec}B$ with $B$ a finite $A$-module, i.e. $f$ is affine and locally given by finite ring morphisms.

Note that being fg as a **module** is **stronger** than being fg as an **algebra**: $k[x] \in  {}_{k}  \mathsf{Alg}$ has one algebra generator but infinite rank in ${}_{k}\Mod$.

Thus **finite** implies **finite type** but not conversely.

Equivalently, proper and locally quasifinite.
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

For locally Noetherian schemes, finite $\iff$ proper + finite fibers.
:::

::: {.front card-id="card-f6ad9d9bdd3e651a"}
Give an example of a non-finite morphism.
:::

::: {.back card-id="card-f6ad9d9bdd3e651a"}
The hyperbola projection $V(xy-c)\to {\mathbf{G}}_m$, which has finite fibers but is not finite.
:::

::: {.front card-id="card-80a1e9e416914d0f"}
What is a **quasifinite ring morphism**?
:::

::: {.back card-id="card-80a1e9e416914d0f"}
**Discrete finite fibers**: for $R\to S$ *finite type* and $\mfq\in \operatorname{Spec}S$, the point in the fiber $\overline{\mfq}\in F \coloneqq\operatorname{Spec}(S\otimes_R \kappa(\mfp))$ is isolated, i.e. the fiber above that point is zero-dimensional.
:::

::: {.front card-id="card-63642f240775d774"}
What is a **quasifinite** morphism?
:::

::: {.back card-id="card-63642f240775d774"}
Locally quasifinite and quasicompact. Equivalently, covered my opens where the induced ring maps are finite type and quasifinite at the prime $\mfq$ associated to $x\in X$.
:::

::: {.front card-id="card-deaa6d5ac072e40a"}
What is a consequence of a morphism of affine schemes being finite?
:::

::: {.back card-id="card-deaa6d5ac072e40a"}
If $R\to A$ is finite the $\operatorname{Spec}A\to \operatorname{Spec}R$ has finite fibers.
:::

::: {.front card-id="card-08935d3d51a49bc7" tags="definition"}
What is a **finite type morphism**?
:::

::: {.back card-id="card-08935d3d51a49bc7"}
Locally of finite type and quasicompact.

Locally of finite type: every point of $X$ has an affine neighborhood $\operatorname{Spec}A\subseteq f^{-1}(\operatorname{Spec}B)$, with $\operatorname{Spec}B\subseteq Y$ affine open, such that $A$ is a finitely generated $B$-algebra.

Equivalently, there is an open affine cover $\operatorname{Spec}B_i\rightrightarrows Y$ such that each $f^{-1}(\operatorname{Spec}B_i)$ is covered by finitely many $\operatorname{Spec}A_{ij}$ with each $A_{ij}\in { {}_{B_i}  \mathsf{Alg}}^\fg$.

Note that being fg as a module is **stronger** than being fg as an algebra: $k[x] \in  {}_{k}  \mathsf{Alg}$ has one algebra generator but infinite rank in ${}_{k}\Mod$. Thus finite implies finite type but not conversely.
:::

::: {.front card-id="card-50d5401e86f0de21"}
What is a morphism locally of finite type?
:::

::: {.back card-id="card-50d5401e86f0de21"}
$f:X\to Y$ with open covers $\operatorname{Spec}B_i, U_i\coloneqq f^{-1}(\operatorname{Spec}B_i)$ where $\operatorname{Spec}A_{ij}\rightrightarrows U_i$ making $A_{ij}\in { {}_{B_i}  \mathsf{Alg}}^\fg$.

Additionally **is of finite type** if each $U_i$ can be covered by finitely many $A_{ij}$.

A ring map $R\to A$ is of finite type $A$ admits a surjection from $R[x_1, \cdots, x_n]$ for some $n$. Equivalently, $A\in  {}_{R}  \mathsf{Alg}^\fg$. Being **locally of finite type** means every $x$ admitting a neighborhood $\operatorname{Spec}A_i\ni x$ where $f(\operatorname{Spec}A_i) \subseteq \operatorname{Spec}R_i\ni f(x)$ so that the induced ring map $R\to A$ is finite type.
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
On open covers, the induced rings maps $R_i\to A_i$ are finite presentation, i.e. $R_i[x_1,\cdots, x_n] \twoheadrightarrow A_i$ with fg kernel for some $n$.
:::

::: {.front card-id="card-9b5950fc2403c0f6"}
A universally closed morphism?
:::

::: {.back card-id="card-9b5950fc2403c0f6"}
$f:X\to Y$ closed and every base change $Y'\to Y \leadsto X \underset{\scriptscriptstyle {Y} }{\times} Y' \to Y'$ is closed, where maps are closed when images of closed sets are closed.
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
Use that ${\mathbf{A}}^n$ is not proper: $X \underset{\scriptscriptstyle {k} }{\times} X \to X$ is not closed for $X\coloneqq{\mathbf{A}}^1$ since it is the coordinate projection, and $V(xy-c) \mapsto {\mathbf{G}}_m$ which is not closed.
:::

::: {.front card-id="card-31a64a619e91d37a" tags="definition"}
What is a **projective morphism**?
:::

::: {.back card-id="card-31a64a619e91d37a"}
$f:X\to Y$ which factors as $X\hookrightarrow{\mathbf{P}}^N_{/ {Y}} \twoheadrightarrow Y$, a closed immersion followed by the natural projection, where ${\mathbf{P}}^N_{/ {Y}} \coloneqq{\mathbf{P}}^N_{/ {\ZZ}} \underset{\scriptscriptstyle {\operatorname{Spec}\ZZ} }{\times} Y$.
:::

::: {.front card-id="card-9f9cd83a2a11e95a"}
What is a quasiprojective morphism?
:::

::: {.back card-id="card-9f9cd83a2a11e95a"}
$f:X\to Y$ which factors as $X\hookrightarrow X'\to Y$, an open immersion followed by a projective morphism.
:::

::: {.front card-id="card-0defb0831c46c847"}
Give examples and counterexamples of projective morphisms.
:::

::: {.back card-id="card-0defb0831c46c847"}
For $A$ any ring and $S$ any graded ring with $S_0 = A$, $\mathop{\mathrm{Proj}}S\to \operatorname{Spec}A$ is projective.
:::

::: {.front card-id="card-de0aa28404f698be"}
Give some consequences of projective morphisms.
:::

::: {.back card-id="card-de0aa28404f698be"}
For Noetherian schemes, projective $\implies$ proper.
:::

::: {.front card-id="card-1663965932adfa0b"}
What is a faithfully flat morphism?
:::

::: {.back card-id="card-1663965932adfa0b"}
Flat and surjective.
:::

::: {.front card-id="card-588fc4423bcb3277"}
What is the degree of a morphism?
:::

::: {.back card-id="card-588fc4423bcb3277"}
$f:X\to S$ with $f_*{\mathcal{O}}_X\in   {}_{{\mathcal{O}}_s}\Mod$ finite and locally free, take its degree as a Coherent sheaf, where $\deg \mcf\coloneqq\deg \operatorname{det}\mcf$ since $\operatorname{det}\mcf\in \operatorname{Pic}(X)$, where the degree is the degree of the associated divisor.
:::

::: {.front card-id="card-2fc77d27d9c19b46"}
What is a **separated morphism**?
:::

::: {.back card-id="card-2fc77d27d9c19b46"}
A morphism $f:X\to S$ of schemes is **separated** iff $\Delta_{X/S}: X\to X \underset{\scriptscriptstyle {S} }{\times} X$ is a **closed immersion**.
:::

::: {.front card-id="card-16d44af59a623c18"}
How is this separatedness related to Hausdorffness?
:::

::: {.back card-id="card-16d44af59a623c18"}
$X\in \Top$ is **Hausdorff** iff the diagonal $\Delta \subseteq X\times X$ is a closed subset.
:::

::: {.front card-id="card-e1412ba6beca8d61"}
What is a quasiseparated morphism?
:::

::: {.back card-id="card-e1412ba6beca8d61"}
- $f:X\to S$ is quasiseparated iff the diagonal is quasicompact.
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
$f:X\to Y$ with $f$ flat at $x$ and the fiber $X_{f(x)}$ *geometrically normal*, i.e. for every field extension $L/k$ and every $\ell$ over $x$ in $X \underset{\scriptscriptstyle {k} }{\times} L$ has a normal local ring, i.e. integrally closed in its field of fractions.
:::

::: {.front card-id="card-74776a13413b562c"}
What is a regular morphism?
:::

::: {.back card-id="card-74776a13413b562c"}
Flat at $x$ and *geometrically regular* at $x$, i.e. for every fg field extension $L/k$ and $\ell$ over $x$ in $X \underset{\scriptscriptstyle {k} }{\times} L$, the local ring at $\ell$ is regular, i.e. the minimal number of generators of its maximal ideal equals its Krull dimension.
:::

::: {.front card-id="card-b18d26174d2423d1"}
What is the cotangent complex?
:::

::: {.back card-id="card-b18d26174d2423d1"}
The nonabelian left-derived functor ${\mathbb{L}}_{{-}/A}: \mathsf{CRing}_A\to \mathbf{D}{  {}_{A}\Mod}$ of the functor $\Omega^1_{{-}/A}[0]$
:::

::: {.front card-id="card-c79260140f5f0dbd"}
When is a morphism of schemes an immersion?
:::

::: {.back card-id="card-c79260140f5f0dbd"}
$\iota: X\to Z$ making $X$ isomorphic to an open subscheme *of a closed subscheme* of $Z$.
:::

::: {.front card-id="card-9129195c6fc4fa3d"}
Name some properties preserved by base change.
:::

::: {.back card-id="card-9129195c6fc4fa3d"}
Open/closed immersions, affine, finite, integral, locally of ft, qc, ft, quasi-finite, flat, surjective.
:::

::: {.front card-id="card-d0d7557976a8bb37" tags="unsorted"}
Show that $\PP^n$ is proper.
:::

::: {.back card-id="card-d0d7557976a8bb37"}
For a valuation ring $R$ with fraction field $K$, a map $\operatorname{Spec}K\to\mathbb P_R^n$ is given by homogeneous coordinates $[a_0:\cdots:a_n]$ in $K$. Scale them so all $a_i\in R$ and at least one is a unit. They then define an extension $\operatorname{Spec}R\to\mathbb P_R^n$. Separatedness gives uniqueness. The valuative criterion proves $\mathbb P_R^n\to\operatorname{Spec}R$ is proper; hence $\mathbb P_k^n$ is proper over $k$.
:::

::: {.front card-id="card-f8d31bfb2abb0b49" tags="definition"}
What is: open/closed immersions
:::

::: {.back card-id="card-f8d31bfb2abb0b49"}
An open immersion identifies $X$ with an open subscheme of $Y$. A closed immersion identifies $X$ with a closed subscheme of $Y$; locally it comes from a surjection of rings $A\twoheadrightarrow A/I$.
:::

::: {.front card-id="card-0698c886db4b9a7c" tags="definition"}
What is: Affine and projective morphisms
:::

::: {.back card-id="card-0698c886db4b9a7c"}
A morphism $f:X\to Y$ is affine if the inverse image of every affine open in $Y$ is affine. It is projective if it factors as a closed immersion $X\hookrightarrow\mathbb P_Y^n$ followed by projection, for some $n$.
:::

::: {.front card-id="card-24e6d1c8282799dd" tags="definition"}
What is: Definition of separated and proper morphisms,
:::

::: {.back card-id="card-24e6d1c8282799dd"}
A morphism of schemes $f: X\to S$ is **separated** if the diagonal $\Delta_{X/S}: X\to X\times_S X$ is a closed immersion, and **proper** if it is separated, of finite type, and universally closed: every base change $X\times_S T\to T$ is a closed map.

We say a variety $X$ is separated if the image of the diagonal map $\Delta: X \rightarrow X \times X$ is Zariski closed in $X \times X$.

For instance, $\mathbb{C}^n$ is separated because the image of the diagonal in $\mathbb{C}^n \times \mathbb{C}^n=$ $\operatorname{Spec}\left(\mathbb{C}\left[x_1, \ldots, x_n, y_1, \ldots, y_n\right]\right)$ is the affine variety $\mathbf{V}\left(x_1-y_1, \ldots, x_n-y_n\right)$. Similarly, any affine variety is separated.
:::

::: {.front card-id="card-e1b36c9f1c246df3" tags="definition, unsorted"}
What are the three valuative criteria?
:::

::: {.back card-id="card-e1b36c9f1c246df3"}
For $f:X\to Y$, consider every valuation ring $R$ with fraction field $K$ and every commutative square $\operatorname{Spec}K\to X$, $\operatorname{Spec}R\to Y$, and count the lifts $\operatorname{Spec}R\to X$ making both triangles commute.

- Separated ($f$ quasi-separated): $\leq 1$ way to fill.
- Universally closed ($f$ quasi-compact): $\geq 1$ way to fill.
- Proper ($f$ of finite type and quasi-separated): $=1$ way to fill.

Existence tests universal closedness; uniqueness tests separatedness. Hartshorne states these for $X$ Noetherian, where the quasi-separatedness hypothesis is automatic.
:::

::: {.front card-id="card-18782c5a0371defb" tags="definition"}
What is the **scheme-theoretic image**?
:::

::: {.back card-id="card-18782c5a0371defb"}
For $f:X\to Y$, the smallest closed subscheme $Z$ of $Y$ through which $f$ factors.

If $f$ is quasi-compact, $Z$ is cut out by the quasi-coherent ideal $\mci\coloneqq\ker\qty{{\mathcal{O}}_Y\to f_* {\mathcal{O}}_X}$, and its underlying set is $\overline{f(X)}$. If $X$ is reduced, $Z$ is $\overline{f(X)}$ with its reduced induced structure.

E.g. for a ring map $\phi: A\to B$ inducing $\operatorname{Spec}B\to \operatorname{Spec}A$, $Z = \operatorname{Spec}(A/\ker\phi)$.
:::

::: {.front card-id="card-006c2199efa06a65" tags="definition"}
What is: Regular immersions and local complete intersections;
:::

::: {.back card-id="card-006c2199efa06a65"}
A closed immersion $Z\hookrightarrow X$ is regular of codimension $c$ if its ideal is locally generated by a regular sequence of length $c$; then $I/I^2$ is locally free of rank $c$. A local complete intersection morphism factors locally as a regular immersion followed by a smooth morphism.
:::

::: {.front card-id="card-d91e16405fc0a206"}
What is a geometric point?
:::

::: {.back card-id="card-d91e16405fc0a206"}
A morphism $\operatorname{Spec}k \to X$ where $k=\kbar$.
:::

::: {.front card-id="card-3154955e247dbc25"}
What is a geometric fiber?
:::

::: {.back card-id="card-3154955e247dbc25"}
The fiber over a geometric point, i.e. for $f:X\to Y$, the fiber product with $p_i: \operatorname{Spec}k \to Y$ given by $X \underset{\scriptscriptstyle {Y} }{\times}\operatorname{Spec}k$.
:::

::: {.front card-id="card-2290d9ce19976340"}
What is a geometrically integral scheme?
:::

::: {.back card-id="card-2290d9ce19976340"}
Idea: prevents becoming reduced or reducible after a field extension.

The structure morphism $f: X\to \operatorname{Spec}k$ is geometrically integral, i.e.for all geometric points $p_i: \operatorname{Spec}L \to \operatorname{Spec}k$ the fiber $X \underset{\scriptscriptstyle {\operatorname{Spec}k} }{\times} \operatorname{Spec}L$ is integral.

Thm: geometrically integral iff geometrically reduced and geometrically irreducible.
:::
