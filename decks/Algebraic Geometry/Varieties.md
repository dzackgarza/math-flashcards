---
title: "Algebraic Geometry::Varieties"
---

::: {.front card-id="card-155c7a1001d2816c" tags="algebraic-geometry"}
What is a variety in scheme-theoretic terms?
:::

::: {.back card-id="card-155c7a1001d2816c"}
A separated integral scheme of finite type over a field $k$ (Hartshorne's convention). Some authors drop integrality and call any separated scheme of finite type over $k$ a variety.
:::

::: {.front card-id="card-73187788340331e8"}
For $V$ a affine variety, what is $k[V]$? What is $A(V)$? What is $k(V)$?
:::

::: {.back card-id="card-73187788340331e8"}
For $V\subseteq {\mathbf{A}}^n$, these are polynomial functions $f\in k[x_1,\cdots, x_n]$ restricted to $V$, i.e. $k[V] = k[x_1,\cdots, x_n]\mathrel{\Big|}_V$. This can be written as $k[V] = k[x_0,\cdots, x_n]/I(V)$, and is sometimes written $A(V) \coloneqq k[V]$. Then $k(V)$ are rational such functions.
:::

::: {.front card-id="card-caab136d7899b1d0"}
What is a **Noetherian** space?
:::

::: {.back card-id="card-caab136d7899b1d0"}
DCC on closed subsets (not necessarily irreducible)
:::

::: {.front card-id="card-7a231e87b8e29bea"}
What is ${\mathcal{O}}_X$ for an affine variety?
:::

::: {.back card-id="card-7a231e87b8e29bea"}
The sheaf of regular functions: sections over $U$ are functions $\phi: U\to k$ where for every $p\in U$ there exists an open neighborhood $U_p\ni p$ and polynomials $f, g\in k[X]$ with ${ \left.{{\phi(x)}} \right|_{{U_p}} } = {f(x)\over g(x)}$.
:::

::: {.front card-id="card-227d4c4c1f0a7f98"}
What are the **Zariski closed** subsets of ${\mathbb{A}}^n$?
:::

::: {.back card-id="card-227d4c4c1f0a7f98"}
For ${\mathbf{A}}^1$ (and any irreducible curve), the Zariski topology on the closed points is the cofinite topology. For ${\mathbf{A}}^n$, not cofinite, just take the usual basis $V(I)$ for $I{~\trianglelefteq~}k[x_1, \cdots, x_{n}]$.
:::

::: {.front card-id="card-b03c437dbfefd2df"}
Is the Zariski topology on ${\mathbf{A}}^2$ the product topology?
:::

::: {.back card-id="card-b03c437dbfefd2df"}
No: $V(x-y) \subseteq {\mathbf{A}}^2$ is clearly closed in the Zariski topology but not closed in the product topology. If it were, ${\mathbf{A}}^2\setminus\Delta$ would be open, so find $U\times V\subset {\mathbf{A}}^2\setminus\Delta$ an open box. Then $U,V$ have finite complements since ${\mathbf{A}}^1$ has the cofinite topology, $U = {\mathbf{A}}^1\setminus\left\{{p_i}\right\}_{i\leq n_1}$ and $V = {\mathbf{A}}^1\setminus\left\{{ q_i }\right\}_{i\leq n_2}$. Pick any $z\neq p_i, q_i$, then $(z,z)\in U\times V \cap\Delta$.
:::

::: {.front card-id="card-52a5e4c5cd50dd0a"}
What is a distinguished open set?
:::

::: {.back card-id="card-52a5e4c5cd50dd0a"}
$D_f \coloneqq X\setminus V(f)$.
:::

::: {.front card-id="card-29a61aa31ebdcf41"}
What is an **affine variety**? A **projective variety**?
:::

::: {.back card-id="card-29a61aa31ebdcf41"}
Affine: an irreducible closed subset of ${\mathbf{A}}^n$. Projective: an irreducible algebraic subset of ${\mathbf{P}}^n$, where $Y$ is an algebraic subset if $Y = V(T)$ for $T$ a collection of homogeneous elements in $k[x_0,\cdots, x_n]$.
:::

::: {.front card-id="card-88228e68e566d9cd"}
What is an **irreducible** subset of an affine variety?
:::

::: {.back card-id="card-88228e68e566d9cd"}
Can't be expressed as the union of proper closed subsets.
:::

::: {.front card-id="card-fa9b1f48dff20ea3"}
What is a **proper** variety?
:::

::: {.back card-id="card-fa9b1f48dff20ea3"}
Separated, finite type, universally closed. Can leave out finite type, since all varieties are.
:::

::: {.front card-id="card-5b346fda33bf8915"}
Give an example of a non-proper variety.
:::

::: {.back card-id="card-5b346fda33bf8915"}
${\mathbf{A}}^n$: separated and finite type over $k$, but not universally closed: take $X = {\mathbf{A}}^1, Y= {\mathbf{A}}^1$, then $X \underset{\scriptscriptstyle {k} }{\times} Y$ is the projection ${\mathbf{A}}^2\to {\mathbf{A}}^1$ onto the coordinate axis, but e.g. $V(xy-c)\mapsto {\mathbf{G}}_m$ which is not closed.
:::

::: {.front card-id="card-d95b4982ca0a7f51"}
What is a complete variety?
:::

::: {.back card-id="card-d95b4982ca0a7f51"}
Integral separated scheme of finite type over a field $k$, where $X\to \operatorname{Spec}k$ is proper.
:::

::: {.front card-id="card-292b553d5ddc68d3"}
What is a normal affine variety?
:::

::: {.back card-id="card-292b553d5ddc68d3"}
Irreducible and local rings are integrally closed.
:::

::: {.front card-id="card-c4182aeda64227f7"}
What is a Fano variety?
:::

::: {.back card-id="card-c4182aeda64227f7"}
A complete variety with ample anticanonical $-K_X$. Note: always projective.
:::

::: {.front card-id="card-0324110ee3d3217f"}
What is a del Pezzo surface?
:::

::: {.back card-id="card-0324110ee3d3217f"}
Fano of dimension 2.
:::

::: {.front card-id="card-72e647f121eed544"}
Give several examples of Fano varieties.
:::

::: {.back card-id="card-72e647f121eed544"}
$-K_{{\mathbf{P}}^n} = {\mathcal{O}}(n+1)$ which is very ample.

Any $D\in \operatorname{Div}({\mathbf{P}}^n)$ when $\deg D < n+1$, since adjunction yields
$$K_D = (K_{{\mathbf{P}}^n} + D)\mathrel{\Big|}_D = \qty{-(n+1)H + \deg(D)\cdot H}\mathrel{\Big|}_D > 0$$
:::

::: {.front card-id="card-c3dc4c2d611a350b"}
What is a Calabi-Yau variety?
:::

::: {.back card-id="card-c3dc4c2d611a350b"}
$K_X \sim_{\mathbf{Q}}0$. Sometimes require $\omega_X\cong {\mathcal{O}}_X$ instead, with $h^j({\mathcal{O}}_X) = 0$ for $1\leq j\leq n-1$.
:::

::: {.front card-id="card-2957b6e954c7da3c"}
Give examples of Calabi-Yau varieties.
:::

::: {.back card-id="card-2957b6e954c7da3c"}
Hypersurfaces $D$ of $\deg D = n+1$, since adjunction yields
$$K_D = (K_{{\mathbf{P}}^n} + D)\mathrel{\Big|}_D = \qty{-(n+1)H + \deg(D)\cdot H}\mathrel{\Big|}_D = 0H\mathrel{\Big|}_D = 0,$$
using the Lefschetz hyperplane theorem to show that the $h^i$ vanish.
:::

::: {.front card-id="card-06bc339afe07854e"}
What is the **dimension** of an affine variety?
:::

::: {.back card-id="card-06bc339afe07854e"}
Supremum over all $n$ of lengths of chains $C_0 \subseteq \cdots C_n$ of irreducible closed subsets.
:::

::: {.front card-id="card-c647f3d346591b35"}
What is the **degree** of a variety?
:::

::: {.back card-id="card-c647f3d346591b35"}
For $\dim X = n$, the number of points in $X$ intersected with $n$ general hyperplanes.
:::

::: {.front card-id="card-7892e4e293c4f44e" tags="definition"}
What is a **smooth point** of a variety? A **singular point**?
:::

::: {.back card-id="card-7892e4e293c4f44e"}
$X$ is nonsingular (smooth) at $x$ if its local ring $\mathcal O_{X,x}$ is regular: the minimal number of generators of its maximal ideal equals $\dim\mathcal O_{X,x}$. Otherwise $x$ is a singular point. $X$ is nonsingular if this holds at every point.

Jacobian criterion: for $Y\subseteq{\mathbf{A}}^n$ an affine variety of dimension $d$, let $I(Y) = \left\langle{f_1,\cdots, f_r}\right\rangle {~\trianglelefteq~}k[x_1, \cdots, x_{n}]$ and $J_Y \coloneqq\left[ {\frac{\partial f_i}{\partial x_j}\,} \right]$ the corresponding Jacobian matrix, then $Y$ is smooth at $p$ iff $\operatorname{rank}J_Y(p) = n-d$ (maximal rank), otherwise if $\operatorname{rank}J_Y(p) < n-d$ it is a singular point.

Alternatively, at a closed point $p$, $\dim {\mathbf{T}}_p X = \dim X$ if smooth and $\dim {\mathbf{T}}_p X > \dim X$ if singular, where ${\mathbf{T}}_p X \coloneqq({\mathfrak{m}}_p /{\mathfrak{m}}_p^2) {}^{ \vee }\coloneqq\mathop{\mathrm{Hom}}_{  {}_{k}{\mathsf{Mod}}}({\mathfrak{m}}_p/{\mathfrak{m}}_p^2, k)$.
:::

::: {.front card-id="card-5d527bea8b6d3b5f"}
What is a separated variety?
:::

::: {.back card-id="card-5d527bea8b6d3b5f"}
Separated iff diagonal is closed iff at $\leq 1$ lift exists for the valuative criterion (to exclude double points).
:::

::: {.front card-id="card-58457551e4c299e3"}
What is the tautological bundle on ${\mathbf{P}}^n$?
:::

::: {.back card-id="card-58457551e4c299e3"}
${\mathcal{O}}_{{\mathbf{P}}^n}(-1)$, the bundle whose fiber above $p\in {\mathbf{P}}^n$ is the line in ${\mathbf{A}}^{n+1}$ defined by $p$.
:::

::: {.front card-id="card-eb835339ede48526"}
What is the **Serre twisting line bundle**?
:::

::: {.back card-id="card-eb835339ede48526"}
The dual of the tautological, ${\mathcal{O}}(-1) {}^{ \vee }= {\mathcal{O}}(1)$.
:::

::: {.front card-id="card-aa5dec0abf747e0e"}
How can you check if $X = V(I)$ is irreducible?
:::

::: {.back card-id="card-aa5dec0abf747e0e"}
Iff $I$ is prime in $k[x_1, \cdots, x_{n}]$.
:::

::: {.front card-id="card-625357df5fd8ef86"}
Why does the exceptional curve $E$ in $\operatorname{Bl}_p(X)$ satisfy $E^2=-1$?
:::

::: {.back card-id="card-625357df5fd8ef86"}
Take $\pi:\operatorname{Bl}_0 {\mathbf{P}}^2\to {\mathbf{P}}^2$. Take two lines $L_1, L_2$ intersecting transversally away from 0 in ${\mathbf{P}}^2$, then $\pi^* L_1.\pi^* L_2 = L_1.L_2 = 1$ since $\pi$ is an isomorphism away from zero. Now move them to $L_1', L_2'$ intersecting at 0; then $\pi^* L_1' = \tilde L_1' + E$ and $\pi^* L_2' = \tilde L_2' + E$, and
$$1 = (\pi^*L_1' . \pi^* L_2') = (\tilde L_1' + E).(\tilde L_2' + E) = \tilde L_1'.\tilde L_2' + \tilde L_1'.E + E.\tilde L_2' + E^2 = 0 + 1 + 1 + E^2 \implies E^2=-1$$
.

Use the following theorem:  For $\pi: \operatorname{Bl}_p X\to X$, let $C$ be a curve in $X$, smooth at $p$. Then the proper transform $\tilde C$ intersects $E$ transversely at one point $q$, and $\pi^* C = \tilde C + E$. Intersect both sides with $E$ to get $\pi^* C . E = (\tilde C + E).E$. The LHS is zero since $\pi^* A.E = 0$ for any divisor $A\in X$. The RHS is $\tilde C.E + E^2 = q + E^2$; taking degrees yields $0 = 1 + E^2 \implies E^2 = -1$.
:::

::: {.front card-id="card-09997a605600bdd5"}
Why is the normalization a resolution of singularities in dimension 1?
:::

::: {.back card-id="card-09997a605600bdd5"}
The normalization is normal, hence regular in codimension 1, hence regular hence smooth.
:::

::: {.front card-id="card-46208803000099ea"}
What is the canonical class of a blowup?
:::

::: {.back card-id="card-46208803000099ea"}
For $\pi: \tilde X\to X$, $K_{\tilde X} = \pi^* K_X + E$.
:::

::: {.front card-id="card-d88dc079b7f19264" tags="definition"}
What is the scheme-theoretic definition of an **affine variety**?
:::

::: {.back card-id="card-d88dc079b7f19264"}
An affine variety over $k$ is an integral separated scheme of finite type over $k$ which is affine, i.e. isomorphic to $\operatorname{Spec}A$ for a finitely generated $k$-domain $A$. Such a scheme is automatically Noetherian, and every affine scheme is separated. Over an algebraically closed field, writing $A = k[x_1,\cdots,x_n]/\mathfrak p$, its closed points form the common zero locus $V(\mathfrak p)\subseteq\mathbb A_k^n$.
:::

::: {.front card-id="card-1d238038a4983580" tags="definition"}
What is: Projective varieties
:::

::: {.back card-id="card-1d238038a4983580"}
A projective variety over $k$ is an integral closed subscheme of $\mathbb P_k^n$ for some $n$. Equivalently, it is $\operatorname{Proj}S$ for a suitable finitely generated graded $k$-domain generated in degree one.
:::

::: {.front card-id="card-c2dcd4397ae86227" tags="definition"}
What is: Morphisms
:::

::: {.back card-id="card-c2dcd4397ae86227"}
A morphism of schemes $f:X\to Y$ consists of a continuous map and a map of sheaves $f^\#:\mathcal O_Y\to f_*\mathcal O_X$ such that each induced map on stalks $\mathcal O_{Y,f(x)}\to\mathcal O_{X,x}$ is local. For varieties over $k$, the morphism also respects the maps to $\operatorname{Spec}k$.
:::

::: {.front card-id="card-3b757b5adf06e626" tags="definition"}
What is a rational map?
:::

::: {.back card-id="card-3b757b5adf06e626"}
For varieties $X,Y$ with $X$ irreducible, a rational map $f: X\dashrightarrow Y$ is an equivalence class of pairs $(U, f_U)$ in which $U\subseteq X$ is a nonempty (hence dense) open subset and $f_U: U\to Y$ is a morphism. Two pairs $(U, f_U)$ and $(U', f'_{U'})$ are equivalent if $f_U$ and $f'_{U'}$ coincide on $U\cap U'$; since $X$ is reduced and $Y$ is separated, agreement on any nonempty open subset of $U\cap U'$ already forces this. It is dominant if the image of some (equivalently every) representative is dense in $Y$.
:::

::: {.front card-id="card-b7fee6cc99998ad4" tags="definition"}
What is: Nonsingular varieties
:::

::: {.back card-id="card-b7fee6cc99998ad4"}
A variety $X$ is nonsingular at $x$ if its local ring $\mathcal O_{X,x}$ is regular: the minimal number of generators of its maximal ideal equals $\dim\mathcal O_{X,x}$. It is nonsingular if this holds at every point.
:::

::: {.front card-id="card-aeb31f26f04430b2" tags="definition"}
What is the scheme-theoretic definition of a (smooth) **curve**?
:::

::: {.back card-id="card-aeb31f26f04430b2"}
A curve over a field $k$ is an integral separated scheme of finite type over $k$ of dimension 1. It is nonsingular iff all its local rings are regular; over a perfect field (e.g. $k=\overline{k}$) this is equivalent to $C$ being smooth over $k$. At every closed point of a nonsingular curve, the local ring is a discrete valuation ring; Weil divisors are then formal sums of closed points.
:::

::: {.front card-id="card-693a53dc1f51c51e"}
What is a hyperplane section? Give an example.
:::

::: {.back card-id="card-693a53dc1f51c51e"}
$Y \subseteq X$ of the form $Y = X\cap H$ for $X\hookrightarrow{\mathbf{P}}^N$ and $H\subseteq {\mathbf{P}}^N$ a hyperplane.

Any hypersurface is an example.
:::

::: {.front card-id="card-5bd745bf9fb39e79"}
What is Chow's theorem for complex projective varieties?
:::

::: {.back card-id="card-5bd745bf9fb39e79"}
Chow 1949: The functor $X \rightsquigarrow X(\mathbb{C})$ from nonsingular projective algebraic varieties to projective complex manifolds is an equivalence of categories. This remains true when singularities are allowed.
:::
