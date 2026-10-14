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

$V(x^2+y^2-z^2)$ the double cone along the $z{\hbox{-}}$axis.

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
$(X, {\mathcal{O}}_X)$ where $X\in {\mathsf{Top}}$ and a **structure sheaf** ${\mathcal{O}}_X\in {\mathsf{Sh}}(X, \mathsf{CRing})$. This is locally ringed if all stalks ${\mathcal{O}}_{X, x}$ have unique maximal ideals.
:::

::: {.front card-id="card-645aa342d2f0ce7b"}
What is a morphism of ringed spaces? Locally ringed spaces?
:::

::: {.back card-id="card-645aa342d2f0ce7b"}
Pairs $(f, f^\sharp)$ where $f\in {\mathsf{Top}}(X, Y)$ and $f^\sharp: {\mathcal{O}}_{Y} \to f_* {\mathcal{O}}_X$ is a map of sheaves of rings on $Y$. This is a morphism of locally ringed spaces iff for each $x\in X$ the induced stalk map $f^\sharp_x: {\mathcal{O}}_{Y, f(x)} \to {\mathcal{O}}_{X, x}$ is a local homomorphism, i.e. $f^\sharp_x( {\mathfrak{m}}_{f(x)} ) \subseteq {\mathfrak{m}}_x$.

Here a local homomorphism $\phi: (A, {\mathfrak{m}}_A)\to (B, {\mathfrak{m}}_B)$ is a ring map with $\phi({\mathfrak{m}}_A) \subseteq {\mathfrak{m}}_B$; these are the morphisms of $\mathsf{Loc}\mathsf{Ring}$.
:::

::: {.front card-id="card-f5a08ee1e016720b"}
What is the definition of a scheme?
:::

::: {.back card-id="card-f5a08ee1e016720b"}
A locally ringed space $(X, {\mathcal{O}}_X)$ locally isomorphic to an affine scheme: every point $x$ admits an open neighborhood $U\ni x$ with $(U, { \left.{{{\mathcal{O}}_X}} \right|_{{U}} }) \cong (\operatorname{Spec}A, {\mathcal{O}}_{\operatorname{Spec}A})$ as locally ringed spaces for some ring $A$. Equivalently, $\exists {\mathcal{U}}\rightrightarrows X$ an open cover by such $U$.
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
Sections: ${\mathcal{O}}(U)$ is the set of functions $s: U\to {\textstyle\coprod}_{{\mathfrak{p}}\in U} A_{\mathfrak{p}}$ with $s({\mathfrak{p}}) \in A_{\mathfrak{p}}$ which are locally fractions: $\forall {\mathfrak{p}}\in U, \exists V$ open with ${\mathfrak{p}}\in V \subseteq U$ and $\exists a, f\in A$ such that for each ${\mathfrak{q}}\in V$, $f\not\in {\mathfrak{q}}$ and $s({\mathfrak{q}}) = a/f$ in $A_{\mathfrak{q}}$.

Stalks: ${\mathcal{O}}_{\operatorname{Spec}A, {\mathfrak{p}}} = A_{\mathfrak{p}}\coloneqq S^{-1}A, S\coloneqq A\setminus{\mathfrak{p}}$.

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

For $X = \operatorname{Spec}A$: set ${\mathfrak{a}}\coloneqq\bigcap_{{\mathfrak{p}}\in Z}{\mathfrak{p}}$, the intersection of all prime ideals in $Z$ (the radical ideal of functions vanishing on $Z$). Then $V({\mathfrak{a}}) = Z$, and $A/{\mathfrak{a}}$ is reduced since ${\mathfrak{a}}$ is radical, so $\operatorname{Spec}(A/{\mathfrak{a}})$ is the reduced closed subscheme on $Z$. Intersecting only the maximal ideals in $Z$ is wrong in general: for $A$ a DVR and $Z = \operatorname{Spec}A$ it gives the closed point.

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
$$\dim_{\kappa(x)} {\mathbf{T}}_{X, x} = \operatorname{krulldim}R, R\coloneqq{\mathcal{O}}_{X, x} \qquad\forall x\in X, k \coloneqq R/{\mathfrak{m}}_R$$
:::

::: {.front card-id="card-3a870899611e5f04"}
What does it mean to be **regular in codimension 1**?
:::

::: {.back card-id="card-3a870899611e5f04"}
Every local ring ${\mathcal{O}}_{X, x}$ of dimension 1 is regular, hence a DVR.

For rings: for every prime ideal ${\mathfrak{p}}\in \operatorname{Spec}A$ of height 1, the localization $A_{\mathfrak{p}}$ is regular, hence a DVR.
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
$f:Y\to X$ is quasicompact iff $\exists {\mathcal{V}}\rightrightarrows Y$ by open affine subschemes such that each $f^{-1}(V_i)$ is quasicompact as a space (i.e. every open cover admits a finite subcover).
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
$X$ is separated iff its structure morphism $X\to \operatorname{Spec}{\mathbf{Z}}$ is a separated morphism, i.e. the diagonal $\Delta_{X/\operatorname{Spec}{\mathbf{Z}}}: X\to X \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} X$ is a **closed immersion**.
:::

::: {.front card-id="card-d5feac6218f5093e"}
What is a **quasiseparated** scheme?
:::

::: {.back card-id="card-d5feac6218f5093e"}
$X$ is quasiseparated iff $X\to \operatorname{Spec}{\mathbf{Z}}$ is a quasiseparated morphisms, where $f:X\to Y$ is quasiseparated iff $\Delta_{X/Y}: X\to X \underset{\scriptscriptstyle {Y} }{\times} X$ is a quasicompact morphism.
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
A locally ringed space locally isomorphic to $(\operatorname{Spf}A, {\mathcal{O}}_{\operatorname{Spf}A})$ where $\operatorname{Spf}A$ is the formal spectrum of a ring -- roughly the completion of a Noetherian scheme $X_i$ along a closed subscheme $Y_i$, where one takes $Y$ as the space and $\projectivelim_n {\mathcal{O}}_X/{\mathcal{I}}_Y^n$.
:::

::: {.front card-id="card-289455ed6aa37e98"}
What are some examples of smooth schemes?
:::

::: {.back card-id="card-289455ed6aa37e98"}
${\mathbf{A}}^n/S, {\mathbf{P}}^n/S$ are smooth of relative dimension $n$.

Over a field $k={ \overline{k} }$, smooth iff regular of dimension $n$.

For an irreducible separated scheme over a field $k ={ \overline{k} }$, smooth iff nonsingular as a variety.
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
Locally Noetherian whose local rings are Gorenstein ($R$ such that $R$ has finite injective dimension in ${}_{R}{\mathsf{Mod}}$).
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
For a closed subscheme $Y$ of ${\mathbf{P}}^n/k$: the ideal $I$ of $Y$ in $k[x_0,\cdots, x_n]$ can be generated by $r\coloneqq\operatorname{codim}_{{\mathbf{P}}^n}(Y)$ elements. Equivalent to $Y = \bigcap_{i=1}^r H_i$ for some hypersurfaces $H_i$ and thus ${\mathcal{I}}_Y = \sum_{i=1}^r {\mathcal{I}}_{H_i}$.

For an arbitrary closed subscheme $Y\leq X$ of a smooth variety: $Y$ is lci in $X$ iff ${\mathcal{I}}_Y$ can be locally generated by $r\coloneqq\operatorname{codim}_{X}(Y)$ elements at every point $y\in Y$.
:::

::: {.front card-id="card-063a8348047c4935"}
What is a **Cohen-Macaulay** scheme?
:::

::: {.back card-id="card-063a8348047c4935"}
All local rings are Cohen-Macaulay: $A$ where $\mathrm{depth} A = \dim A$, where the depth is the maximal length of a regular sequence whose generates are in ${\mathfrak{m}}_A$, and $\left\{{x_1,\cdots, x_n}\right\}$ is a regular sequence for $M\in   {}_{A}{\mathsf{Mod}}$ is $x_1$ is not a zero divisor in $M$ and $x_{i+1}$ is not a zero divisor in $M/I_iM$ where $I_i \coloneqq\left\langle{x_1,\cdots, x_i}\right\rangle$.
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
$\kappa(x) \coloneqq{\mathcal{O}}_{X, x}/{\mathfrak{m}}_x$. If $U = \operatorname{Spec}A \ni x$ and ${\mathfrak{p}}\in \operatorname{Spec}A$ corresponds to $x$, then $\kappa(x) = A_{\mathfrak{p}}/ {\mathfrak{p}}A_{\mathfrak{p}}$, the fraction field of $A/{\mathfrak{p}}$.
:::

::: {.front card-id="card-d78d46215a60b1cb"}
What is the **scheme associated to a variety**?
:::

::: {.back card-id="card-d78d46215a60b1cb"}
Use the functor $t: {\mathsf{Var}}_{/ {k}}\to {\mathsf{Sch}}_{/ {k}}$, then $V$ is homeomorphic to the closed points in ${\left\lvert {t(V)} \right\rvert}$ and ${\mathcal{O}}_V \cong { \left.{{ {\mathcal{O}}_{t(V)}}} \right|_{{t(V)^{ \operatorname{cl}}}} }$, i.e. the regular functions on $V$ are restrictions to closed points of the structure sheaf of $t(V)$.

Generally $t(V)$ is the set of nonempty irreducible closed subsets of $V$, define the images of such sets to be closed sets to form a topology.
:::

::: {.front card-id="card-93365011b44724e2" tags="definition"}
What is the **Proj construction**?
:::

::: {.back card-id="card-93365011b44724e2"}
For $S = \bigoplus_{d\geq 0} S_d$ a graded ring, write $S_+ \coloneqq\bigoplus_{d\geq 1} S_d$ and let $\mathop{\mathrm{Proj}}S$ be the set of homogeneous prime ideals of $S$ which do not contain $S_+$. The closed sets are $V({\mathfrak{a}}) \coloneqq\left\{{P\in \mathop{\mathrm{Proj}}S {~\mathrel{\Big\vert}~}P \supseteq{\mathfrak{a}}}\right\}$ for ${\mathfrak{a}}$ a homogeneous ideal.

For the structure sheaf, for each $p\in \mathop{\mathrm{Proj}}S$ define $S_{(p)}$ to be the elements of degree zero in the localization $S[T^{-1}]$ where $T$ is the set of all homogeneous elements of $S$ which are not in $p$, and define ${\mathcal{O}}(U)$ to be functions $s: U\to \amalg_{p\in U} S_{(p)}$ with $s(p) \in S_{(p)}$ and $s$ locally a fraction: $s(q) = a/f$ with $a,f\in S$ homogeneous of the same degree and $f\not\in q$.

The basic opens $D_+(f)$, for $f$ homogeneous of positive degree, satisfy $D_+(f)\cong\operatorname{Spec}(S_f)_0$.
:::

::: {.front card-id="card-6cdb91f28276b7cc"}
What is ${\mathbf{A}}^n_{/ {R}}$ as a scheme?
:::

::: {.back card-id="card-6cdb91f28276b7cc"}
$\operatorname{Spec}R[x_1,\cdots, x_n]$ or ${\mathbf{A}}^n_{/ {{\mathbf{Z}}}} \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} \operatorname{Spec}R$.
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
For $(X, {\mathcal{O}}_X)\in {\mathsf{Sch}}$, sheafify $U\mapsto {\mathcal{O}}_X(U)^{ \text{red} }$ where $R^{ \text{red} }\coloneqq R/{\sqrt{0_{R}} }$ is the quotient by the ideal of nilpotent elements to get ${\mathcal{O}}_{X}^{ \text{red} }$.
:::

::: {.front card-id="card-a193384cad51473e" tags="definition"}
What is an **irreducible** scheme?
:::

::: {.back card-id="card-a193384cad51473e"}
Irreducible as a topological space: nonempty and not the union of two proper closed subsets. Equivalently, any two nonempty open subsets meet.
:::

::: {.front card-id="card-1f9ebf5ac271403c"}
What is an $n{\hbox{-}}$fold point over $k$?
:::

::: {.back card-id="card-1f9ebf5ac271403c"}
A scheme $\operatorname{Spec}R\to \operatorname{Spec}k$ with one point such that $R$ is a $k{\hbox{-}}$algebra of dimension $n$.
:::

::: {.front card-id="card-6067745a47634f5c"}
What is the **Riemann-Roch theorem**?
:::

::: {.back card-id="card-6067745a47634f5c"}
For $C$ a curve,
$$\chi(C; {\mathcal{L}}) = \deg({\mathcal{L}}) + (1-g)$$
:::

::: {.front card-id="card-6ca7d0c76fa6a201"}
How is the **adjunction formula** derived?
:::

::: {.back card-id="card-6ca7d0c76fa6a201"}
Start with $f: C\hookrightarrow S$ a curve in a surface over $\operatorname{Spec}k$ to get
$$\begin{align*}{\mathbf{T}}_C \hookrightarrow f^* {\mathbf{T}}_S \twoheadrightarrow N_{C/S} \quad &\underset{\text{dualize}}\leadsto\quad N {}^{ \vee }_{C/S} \coloneqq I_C/I_C^2 \hookrightarrow f^* \Omega^1_{S/k} \twoheadrightarrow\Omega^{1}_{C/k} \\ &\implies \operatorname{det}f^* \Omega^1_{S/k} \cong \operatorname{det}\Omega^1_{C/k} \otimes\operatorname{det}N {}^{ \vee }_{C/S} \\&\implies f^* \omega_S \cong \omega_C \otimes\operatorname{det}N {}^{ \vee }_{C/S} \\ &\implies\omega_C = f^*\omega_S \otimes\operatorname{det}N_{C/S} \end{align*}$$
Now use that $I_C = {\mathcal{O}}_S(C)^{-1}$ and $I_C/I_C^2 = {\mathcal{O}}_S(C)^{-1}\otimes{\mathcal{O}}_C$ to get
$$N_{C/S} = (I_C/I_C^2) {}^{ \vee }= ({\mathcal{O}}_S(C)^{-1}\otimes{\mathcal{O}}_C) {}^{ \vee }= {\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C$$
and so
$$\omega_C = f^* \omega_S \otimes{\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C  \implies \omega_C = \qty{\omega_S \otimes{\mathcal{O}}_S(C) }\mathrel{\Big|}_C \implies K_C = (K_S + C)\mathrel{\Big|}_C$$
:::

::: {.front card-id="card-f8859d1bf94b455d"}
What is the **adjunction formula**?
:::

::: {.back card-id="card-f8859d1bf94b455d"}
For $f: C\hookrightarrow S$ a smooth curve in a smooth surface,
$$\omega_C \cong \qty{\omega_S \otimes{\mathcal{O}}_S(C) }\mathrel{\Big|}_C = f^* \omega_S \otimes{\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C \implies K_C = (K_S + C)\mathrel{\Big|}_C$$
The factor $\mathcal O_S(C)$ permits a simple pole along $C$ before taking the residue on $C$.
:::

::: {.front card-id="card-282fc0e81109dc6b"}
For a smooth curve $C$ on a smooth surface $S$, use the adjunction formula to express the genus in terms of intersection numbers.
:::

::: {.back card-id="card-282fc0e81109dc6b"}
$$2g-2 = C.(C+K_S)$$
Use $\omega_C \cong \omega_S \otimes{\mathcal{O}}_S(C) \otimes{\mathcal{O}}_C$, take degrees, and use that $\deg(\omega_C) = 2g-2$ and $\deg_C({\mathcal{O}}_S(D)\otimes{\mathcal{O}}_C) = C.D$ (which is ${\sharp}(C\cap D)$ when $D$ is effective and meets $C$ transversally) to get
$$\deg(\omega_S \otimes{\mathcal{O}}_S(C)\otimes{\mathcal{O}}_C) = \deg({\mathcal{O}}_S(C+K_S)\otimes{\mathcal{O}}_C) = C.(C+K_S).$$
:::

::: {.front card-id="card-f73cddec8b039beb"}
What is the degree formula for a curve of degree $d$ in ${\mathbf{P}}^2$?
:::

::: {.back card-id="card-f73cddec8b039beb"}
By adjunction,
$$2g-2 = C.(C+K_{{\mathbf{P}}^2}) = dH.(d-3)H = d(d-3)\implies g ={1\over 2}(d-1)(d-2).$$
:::

::: {.front card-id="card-7a13c1f152bea481"}
What is **Serre vanishing**?
:::

::: {.back card-id="card-7a13c1f152bea481"}
For $X$ a Noetherian scheme, $X$ is affine $\iff H^{i>0}(X; {\mathcal{F}}) = 0$ for all ${\mathcal{F}}\in {\mathsf{QCoh}}(X) \iff H^1(X; {\mathcal{I}}) = 0$ for all coherent sheaves of ideals on $X$.
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
What does it mean to *evaluate* a prime ideal ${\mathfrak{p}}{~\trianglelefteq~}R$ at an element $f\in R$?
:::

::: {.back card-id="card-8291e7f9a2f63d07"}
Take the image of $f$ under the natural map $R \to R/{\mathfrak{p}}\to \kappa({\mathfrak{p}})$ where $\kappa({\mathfrak{p}}) \coloneqq\operatorname{ff}(R/{\mathfrak{p}}) \cong R_{\mathfrak{p}}/{\mathfrak{p}}R_{\mathfrak{p}}$ is the residue field of the local ring $R_{\mathfrak{p}}$.
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
Giving a rational point $x\in X$, so $\kappa(x) = k$, and an element of ${\mathbf{T}}_x \coloneqq({\mathfrak{m}}_x/{\mathfrak{m}}_x)^2$.
:::

::: {.front card-id="card-618a12ae0264b25f"}
For $X\to S$ a scheme, what is a $T{\hbox{-}}$valued point of $X$ for $T$ a scheme?
:::

::: {.back card-id="card-618a12ae0264b25f"}
A scheme morphism $T\to X$.
:::

::: {.front card-id="card-fdb0e1a6a993fc2f"}
What is a **generic point**?
:::

::: {.back card-id="card-fdb0e1a6a993fc2f"}
A point $\eta \in X$ such that ${ \operatorname{cl}}_X \eta = X$.
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
Points $x$ at which ${\mathcal{O}}_{X, x}$ is not a regular local ring, where $(A, {\mathfrak{m}}_A)$ is regular iff $\dim_{\kappa(A)} {\mathfrak{m}}_A/{\mathfrak{m}}_A^2 = \dim A$ where $\kappa(A)$ is the residue field of $A$.
:::

::: {.front card-id="card-dc477b6237cb1cc7"}
What is **base change**?
:::

::: {.back card-id="card-dc477b6237cb1cc7"}
For $X\in{\mathsf{Sch}}_{/ {S}}$ and $T\to S$ a morphism of schemes, the pullback $X  \underset{\scriptscriptstyle {S} }{\times} T$.
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

::: {.front card-id="card-39d50a1666910f3f"}
What is **smooth base change**?
:::

::: {.back card-id="card-39d50a1666910f3f"}
For $f: X\to S$ smooth and $g: T\to S$ qc and ${\mathcal{F}}\in {\mathsf{Sh}}(T)$ of $C_n{\hbox{-}}$modules (torsion), there is an isomorphism $f^* {\mathbf{R}}^q g_* {\mathcal{F}} { \, \xrightarrow{\sim}\, }{\mathbf{R}}^q \tilde g_* (f')^*{\mathcal{F}}$ where $\tilde g: X \underset{\scriptscriptstyle {S} }{\times} T \to X$ and $\tilde f: X \underset{\scriptscriptstyle {S} }{\times} T\to T$.
:::

::: {.front card-id="card-5e0bccfad0df15c7"}
What is **proper base change**?
:::

::: {.back card-id="card-5e0bccfad0df15c7"}
If $\pi: X\to S$ is proper and ${\mathcal{F}}$ is a torsion sheaf on $X$ with $f: T\to S$, the base change morphism $f^{-1}{\mathbf{R}}^i \pi_* {\mathcal{F}} { \, \xrightarrow{\sim}\, }{\mathbf{R}}^i \tilde\pi_* \tilde f^{-1}{\mathcal{F}}$.
:::

::: {.front card-id="card-c568a40234fbb420"}
What is the **codimension** of a subset of a scheme?
:::

::: {.back card-id="card-c568a40234fbb420"}
For an irreducible closed $Z\subseteq X$, the supremum over lengths of chains $Z= Z_0 \subseteq Z_1 \subseteq \cdots \subseteq Z_n$ of distinct irreducible closed subsets of $X$. For an arbitrary closed subset $Y$, take the infimum over all irreducibles $Z \subseteq Y$.
:::

::: {.front card-id="card-de688f4ab8bf69dd"}
What are the exact sequences associated with relative differentials?
:::

::: {.back card-id="card-de688f4ab8bf69dd"}
For $f:X\to Y$ and $Z \leq X$ closed with ideal sheaf ${\mathcal{I}}_Z$, the sequence
$${\mathcal{I}}_Z/{\mathcal{I}}_Z^2\to \Omega_{X/Y}\otimes{\mathcal{O}}_Z \twoheadrightarrow\Omega_{Z/Y}$$
If $Y=k$, this is exact iff $Z$ is smooth.

For $X\xrightarrow{f} Y \xrightarrow{g} Z$,
$$f^* \Omega_{Y / Z} \rightarrow \Omega_{X / Z} \twoheadrightarrow\Omega_{X / Y}$$
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

::: {.front card-id="card-d5e412cd78235f30"}
What are the **normal** and **conormal sheaves**?
:::

::: {.back card-id="card-d5e412cd78235f30"}
For $Y\hookrightarrow X$ a smooth subvariety of a smooth variety, $\mathbf{N}_{Y/X} {}^{ \vee }= {\mathcal{I}}_Y/{\mathcal{I}}_Y^2$ is the conormal sheaf and $\mathbf{N}_{Y/X}\coloneqq\mathop{\mathcal{H}\! \mathit{om}}_{{\mathcal{O}}_Y}({\mathcal{I}}_Y/{\mathcal{I}}_Y^2, {\mathcal{O}}_Y)$ is the normal sheaf.
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

::: {.front card-id="card-12cc1c6c9aa5697e"}
What does it mean for ${\mathcal{L}}\in \operatorname{Pic}(X)$ to be **ample**?
:::

::: {.back card-id="card-12cc1c6c9aa5697e"}
For all ${\mathcal{F}}\in {\mathsf{Coh}}(X)$, the twist ${\mathcal{F}}\otimes{\mathcal{L}}^n$ is globally generated for $n\gg 0$.
:::

::: {.front card-id="card-600a9b022ee0b85d"}
Discuss ampleness of sheaves of affine schemes.
:::

::: {.back card-id="card-600a9b022ee0b85d"}
Every $X\in {\mathsf{Coh}}(\operatorname{Spec}A)$ is globally generated, so if ${\mathcal{F}}$ is invertible then it is necessarily ample.
:::

::: {.front card-id="card-2629a4068afdc432"}
Discuss $H^0({\mathbf{P}}^m; {\mathcal{O}}(n))$ for $n\in {\mathbf{Z}}$.
:::

::: {.back card-id="card-2629a4068afdc432"}
The section ring is given by $\bigoplus_{n\geq 0} H^0({\mathbf{P}}^m; {\mathcal{O}}(n)) \cong k[x_0,\cdots, x_m]$ as graded rings. Thus $H^0({\mathcal{O}}) = k$ and $H^0({\mathcal{O}}(n))$ are degree $n$ polynomials, so is generated by the monomials of total degree $n$ -- this is a stars and bars argument; the number of monomials in $R[x_1,\cdots, x_N]$ of degree $D$ is ${N+D-1\choose D}$. Here $N = m+1$ and $D = n$, so we get ${m+d\choose d}$.

How this count goes: represent as $a^3b^2d^2e \leadsto \bullet \bullet \bullet \mathrel{\Big|}\bullet \bullet \mathrel{\Big|}\mathrel{\Big|}\bullet \bullet \mathrel{\Big|}\bullet$. Note that there are no sections for $n < 0$. In general, ${\mathcal{O}}(n)$ corresponds to the $n{\hbox{-}}$uple/Veronese embedding ${\mathbf{P}}^n \to {\mathbf{P}}^N$.
:::

::: {.front card-id="card-979041d2022161e4"}
Discuss ampleness of ${\mathcal{O}}_{{\mathbf{P}}^m}(n)$.
:::

::: {.back card-id="card-979041d2022161e4"}
${\mathcal{O}}(1)$ is very ample: write ${\mathbf{P}}^n = \mathop{\mathrm{Proj}}k[x_0, \cdots, x_{n}]$, then $x_0,\cdots, x_n$ induce $n+1$ global sections . For $n\geq 1$, ${\mathcal{O}}(n)$ corresponds to the Veronese embedding into ${\mathbf{P}}^N$, and so is very ample.
:::

::: {.front card-id="card-938f2d52c80bd08e"}
Prove that if $X$ is a projective variety, $H^0(X; {\mathcal{O}}_X) = k$
:::

::: {.back card-id="card-938f2d52c80bd08e"}
Since ${\mathbf{P}}^n$ is proper, $X\subseteq {\mathbf{P}}^n$ is proper as a closed subvariety. So $s\in H^0(X; {\mathcal{O}}_X)$ is the same as a regular map $s: X\to {\mathbf{A}}^1$.

By properness, $\operatorname{im}s \subseteq {\mathbf{A}}^1$ is closed and thus a finite set of points since ${\mathbf{A}}^1$ has the cofinite topology.

By irreducibility, it must be one point, so $s$ is a constant map $s(x) = \lambda$ for some $\lambda \in k$, so sections biject with elements of $k$.
:::

::: {.front card-id="card-610ae6d59c072f6d"}
Discuss $H^*({\mathbf{P}}^n; {\mathcal{O}}(d))$.
:::

::: {.back card-id="card-610ae6d59c072f6d"}
$k[x_0,\cdots, x_n]_d$ for $*=0$,

zero for $*=1,\cdots, n-1$, and

$\qty{\prod_{i=1}^n x_i }^{-1}k[x_0^{-1}, \cdots, x_n^{-1}]$ for $*=n$.
:::

::: {.front card-id="card-9db7a801cc266d51"}
What is the **blowup** of a variety?
:::

::: {.back card-id="card-9db7a801cc266d51"}
For $\operatorname{Bl}_0 {\mathbf{A}}^n$: take ${\mathbf{A}}^n\times {\mathbf{P}}^{n-1}$ with coordinates ${\left[ {x_0, \cdots, x_{n-1}} \right]}, {\left[ {y_0:\cdots : y_{n-1}} \right]}$, so the closed subsets are $V(f)$ where $f$ is a polynomial in $x_i, y_i$ which is homogeneous in the $y_i$. Take the blowup to be the subset $\left\{{x_iy_j = x_j y_i {~\mathrel{\Big\vert}~}1\leq i,j\leq n-1}\right\} = \left\{{2\times 2\text{ minors of} \begin{bmatrix}x_0 & x_1 & \cdots & x_n \\ y_0 & y_1 & \cdots & y_n \end{bmatrix}}\right\}$.

Then $\exists \pi: \operatorname{Bl}_0 {\mathbf{A}}^n \to {\mathbf{A}}^n$ where ${\sharp}\pi^{-1}(p) = 1$ for $p\neq 0$ and $\pi^{-1}(0)\cong {\mathbf{P}}^{n-1}$ corresponding to all lines through $0$.

For $\operatorname{Bl}_Y {\mathbf{A}}^n$ with $Y \subseteq {\mathbf{A}}^n$ a closed subvariety: take ${ \operatorname{cl}}_{\operatorname{Bl}_0 {\mathbf{A}}^n}\qty{\pi^{-1}(Y\setminus\left\{{0}\right\})}$.
:::

::: {.front card-id="card-77f1ef48e07e3dc0"}
What is the **blowup of a scheme along a subscheme**? How does this recover blowups for varieties?
:::

::: {.back card-id="card-77f1ef48e07e3dc0"}
Can generally blowup along a coherent sheaf of ideals ${\mathcal{I}}$ on $X$: take the sheaf of graded algebras $\tilde {\mathcal{I}}\coloneqq\bigoplus_{d\geq 0}{\mathcal{I}}^d$ where ${\mathcal{I}}^0 \coloneqq{\mathcal{O}}_X$ and set $\tilde X \coloneqq\mathop{\mathrm{Proj}}\tilde {\mathcal{I}}$. Can do this with the ideal of sheaf of $Y\hookrightarrow X$ a closed subscheme.

For $X={\mathbf{A}}^n_{/ {k}}$, $p=0$ corresponds to $I = \left\langle{x_0,\cdots,x_n}\right\rangle$ and $\tilde X \coloneqq\mathop{\mathrm{Proj}}S$ where $S\coloneqq\bigoplus_{d\geq 0} I^d$; then setting $X \coloneqq\operatorname{Spec}A, A\coloneqq k[x_1, \cdots, x_{n}]$ there is a surjection $A[y_1,\cdots, y_n]$ where $y_i\mapsto x_i, {\left\lvert {x_i} \right\rvert} = 1$, making $\tilde X$ isomorphic to a closed subscheme of $\mathop{\mathrm{Proj}}A[y_1,\cdots, y_n] \cong {\mathbf{P}}^{n-1}_{/ {A}}$, and the ideal of definition is generated by $\left\{{x_iy_j - x_jy_i}\right\}$.
:::

::: {.front card-id="card-f99d3b6a576c782a"}
Discuss ampleness of ${\mathcal{L}}\in \operatorname{Pic}(C)$ for $C$ a smooth complete curve.
:::

::: {.back card-id="card-f99d3b6a576c782a"}
${\mathcal{L}}= {\mathcal{O}}(D)$ is ample iff $\deg D > 0$, using RR.
:::

::: {.front card-id="card-a4380c8c6119e01f"}
What is a **base point** of a linear system?
:::

::: {.back card-id="card-a4380c8c6119e01f"}
For $p\in X$ and a linear system ${\left\lvert {D_0} \right\rvert}$, $p$ is a base point iff $p\in \mathop{\mathrm{supp}}D$ for all $D\in {\left\lvert {D_0} \right\rvert}$, where $\mathop{\mathrm{supp}}D$ is the union of all prime divisors in $D$.
:::

::: {.front card-id="card-95da29f9068355c0"}
What is a **strict transform**?
:::

::: {.back card-id="card-95da29f9068355c0"}
For $\pi: \tilde X\to X$ a blowup with center $Z$ and $Y\leq X$ a closed subscheme, the closure ${ \operatorname{cl}}_{\tilde X} \pi^{-1}(Y\setminus Z$).
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

::: {.front card-id="card-75342d6157a4433d"}
What is a **prime divisor** on a scheme?
:::

::: {.back card-id="card-75342d6157a4433d"}
A closed integral subscheme of dimension 1. Need $X$ to be a Noetherian integral separated scheme which is regular in codimension 1.
:::

::: {.front card-id="card-319a35d07535844b"}
What is a **geometrically connected** scheme?
:::

::: {.back card-id="card-319a35d07535844b"}
A scheme that is connected and does not become disconnected after base change: for $X\in {\mathsf{Sch}}_{/ {k}}$, for every extension $L$ of $k$, require that $X \underset{\scriptscriptstyle {k} }{\times} L$ is connected.
:::

::: {.front card-id="card-cf5815d5a2806ef1"}
What is the **degree** of a morphism of curves?
:::

::: {.back card-id="card-cf5815d5a2806ef1"}
For $f:X\to Y$ finite, the degree of the field extension $[K(X): K(Y)]$.
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

::: {.front card-id="card-8ec58f09e82af130" tags="definition"}
What is: Blowups
:::

::: {.back card-id="card-8ec58f09e82af130"}
The blowup of a scheme $X$ along an ideal sheaf $I$ is $\operatorname{Bl}_I X=\operatorname{Proj}_X\bigoplus_{n\geq0}I^n$. It is universal among maps $Y\to X$ for which the pulled-back ideal $I\mathcal O_Y$ is invertible.
:::

::: {.front card-id="card-870c96f4b6081b54" tags="definition"}
What is: Normal schemes and normalization
:::

::: {.back card-id="card-870c96f4b6081b54"}
A ring $R$ with field of fractions $K$ is **normal** if every element of $K$ which is integral over $R$ (i.e. a root of monic polynomial in $R[x]$ ) is actually in $R$.

A scheme $X$ is **normal** if all its local rings $\mathcal{O}_{X, p}$ are normal domains; a variety $X$ is **normal** if it is irreducible and the local rings $\mathcal{O}_{X, p}$ are normal for all $p \in X$.

The **normalization** of an integral scheme $X$: cover $X$ by affines $\operatorname{Spec}A_i$, let $\tilde A_i$ be the integral closure of $A_i$ in the function field $K(X)$, and glue the $\operatorname{Spec}\tilde A_i$ to get $\nu: \tilde X\to X$. Then $\tilde X$ is normal and integral, $\nu$ is integral and birational (finite for varieties), and every dominant morphism $Z\to X$ from a normal integral scheme $Z$ factors uniquely through $\nu$.
:::
