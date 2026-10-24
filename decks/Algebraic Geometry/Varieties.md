---
title: "Algebraic Geometry::Varieties"
---

::: {.front card-id="card-155c7a1001d2816c" tags="algebraic-geometry"}
What is a variety in scheme-theoretic terms?
:::

::: {.back card-id="card-155c7a1001d2816c"}
A separated integral scheme of finite type over a field $k$ (Hartshorne's convention). Some authors drop integrality and call any separated scheme of finite type over $k$ a variety.

Another convention requires geometric integrality over $k$.
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
For ${\mathbf{A}}^1$ (and any irreducible curve), the Zariski topology on the closed points is the cofinite topology. For ${\mathbf{A}}^n$, not cofinite, just take the usual basis $V(I)$ for $I\normal k[x_1, \cdots, x_{n}]$.
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
$K_X \sim_\QQ0$. Sometimes require $\omega_X\cong {\mathcal{O}}_X$ instead, with $h^j({\mathcal{O}}_X) = 0$ for $1\leq j\leq n-1$.
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

Jacobian criterion: for $Y\subseteq{\mathbf{A}}^n$ an affine variety of dimension $d$, let $I(Y) = \left\langle{f_1,\cdots, f_r}\right\rangle \normal k[x_1, \cdots, x_{n}]$ and $J_Y \coloneqq\left[ {\frac{\partial f_i}{\partial x_j}\,} \right]$ the corresponding Jacobian matrix, then $Y$ is smooth at $p$ iff $\operatorname{rank}J_Y(p) = n-d$ (maximal rank), otherwise if $\operatorname{rank}J_Y(p) < n-d$ it is a singular point.

Alternatively, at a closed point $p$, $\dim {\mathbf{T}}_p X = \dim X$ if smooth and $\dim {\mathbf{T}}_p X > \dim X$ if singular, where ${\mathbf{T}}_p X \coloneqq(\mfm_p /\mfm_p^2) {}^{ \vee }\coloneqq\mathop{\mathrm{Hom}}_{  {}_{k}\Mod}(\mfm_p/\mfm_p^2, k)$.
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

::: {.front card-id="card-46208803000099ea" tags="formula"}
For the blowup $\pi:\widetilde X\to X$ of a smooth complex variety along a smooth center of codimension $c\ge2$, compute $K_{\widetilde X}$ using the exceptional divisor $E$.
:::

::: {.back card-id="card-46208803000099ea"}
$$K_{\widetilde X}=\pi^*K_X+(c-1)E.$$
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

::: {.front card-id="card-24176e569cb28a19"}
Give $\dim {\mathbf{P}}(V)$ in terms of $\dim V$.
:::

::: {.back card-id="card-24176e569cb28a19"}
$\dim {\mathbf{P}}(V) = \dim V - 1$.
:::

::: {.front card-id="card-2f94dbd7c0c5c56e"}
What is $\dim {\mathbf{P}}^n$.
:::

::: {.back card-id="card-2f94dbd7c0c5c56e"}
$\dim {\mathbf{P}}^n = n$, locally $n$ degrees of freedom: $p \sim {\left[ {1: x_1/x_0:\cdots :x_n/x_0} \right]}$.
:::

::: {.front card-id="card-3c62ffad76035cd6"}
What is the Kodaira embedding theorem?
:::

::: {.back card-id="card-3c62ffad76035cd6"}
If $X$ is compact Kahler and $\mcl\in \operatorname{Pic}(X)$ then $\mcl> 0 \iff \mcl\in \operatorname{Pic}(X)^\amp$.

$\impliedby$: if $\mcl{ {}^{ \scriptstyle\otimes_{}^{n} }  } = {\mathcal{O}}_{{\mathbf{P}}^N}(1)\mathrel{\Big|}_X$, the hyperplane bundle is positive since its curvature is the Fubini-Study form.

Positive: $\mcl> 0 \iff \mcl$ admits a metric $h$ such that the associated curvature $\sqrt{-1}\Theta(\mcl, h)$ is a positive 1-1 form.

Comes from the Chern connection induced by ${ \overline{{\partial}}}:\mcl\to \mcl\otimes H^{0, 1}(M)$, namely $\nabla^{0, 1} = { \overline{{\partial}}}$.
:::

::: {.front card-id="card-26a43a92a834b431"}
When is a variety smooth?
:::

::: {.back card-id="card-26a43a92a834b431"}
If $\Omega_{X}$ is locally free of rank $\dim X$

Equivalently, $X \underset{\scriptscriptstyle {k} }{\times}\kbar$ is a regular scheme.
:::

::: {.front card-id="card-10b63f4aeb034057"}
Discuss GAGA
:::

::: {.back card-id="card-10b63f4aeb034057"}
To any $X\in\Sch^{\mathrm{ft}}_{/ {\CC}}$ there exist $X^\an\to X$ a morphism of ringed spaces from an analytic space where the points of $X^\an$ correspond to the closed points of $X$ and there is an induced equivalence $\Coh(X) { \, \xrightarrow{\sim}\, }\Coh(X^\an)$.
:::

::: {.front card-id="card-ded86dc8399712bb"}
What is a projectively normal morphism?
:::

::: {.back card-id="card-ded86dc8399712bb"}
The restriction $H^0\left(\mathbf{P}^{g-1}, \mathcal{O}(k)\right) \longrightarrow H^0\left(C, \omega_C^k\right)$ is surjective for all $k$.
:::

::: {.front card-id="formula-cyclic-cover-pushforward-canonical" tags="formula"}
For the smooth cyclic cover $f:X\to Y$ of degree $n$ defined by a smooth branch divisor $B\in\lvert L^n\rvert$ on smooth projective $Y/\mathbb C$, compute $f_*\mathcal O_X$ and $\omega_X$.
:::

::: {.back card-id="formula-cyclic-cover-pushforward-canonical"}
$$f_*\mathcal O_X=\bigoplus_{i=0}^{n-1}L^{-i},\qquad \omega_X\cong f^*(\omega_Y\otimes L^{n-1}).$$
:::

::: {.front card-id="formula-cyclic-cover-euler" tags="formula"}
For a smooth degree-$n$ cyclic cover $X\to Y$ of smooth projective complex varieties branched along smooth $B\in\lvert L^n\rvert$, compute the topological and holomorphic Euler characteristics of $X$.
:::

::: {.back card-id="formula-cyclic-cover-euler"}
$$e(X)=ne(Y)-(n-1)e(B),\qquad \chi(\mathcal O_X)=\sum_{i=0}^{n-1}\chi(Y,L^{-i}).$$
:::

::: {.front card-id="formula-double-cover-pushforward-canonical" tags="formula"}
For a smooth double cover $f:X\to Y$ of smooth projective complex varieties defined by a smooth branch divisor in $\lvert L^2\rvert$, compute $f_*\mathcal O_X$ and $\omega_X$.
:::

::: {.back card-id="formula-double-cover-pushforward-canonical"}
$$f_*\mathcal O_X=\mathcal O_Y\oplus L^{-1},\qquad \omega_X\cong f^*(\omega_Y\otimes L).$$
:::

::: {.front card-id="formula-stable-map-virtual-dimension" tags="formula"}
For a smooth projective complex $m$-fold $X$, compute the virtual dimension of $\overline M_{g,n}(X,\beta)$.
:::

::: {.back card-id="formula-stable-map-virtual-dimension"}
$$\operatorname{vdim}\overline M_{g,n}(X,\beta)=(1-g)(m-3)-K_X\beta+n.$$
:::

::: {.front card-id="formula-hypersurface-threefold-invariants" tags="formula"}
For a smooth degree-$d$ hypersurface $X\subset\mathbb P^4_{\mathbb C}$, compute $H^3,K_X,c_2(X),c_3(X)$ and $e(X)$.
:::

::: {.back card-id="formula-hypersurface-threefold-invariants"}
$$\begin{aligned}H^3&=d,\qquad K_X=(d-5)H,\\c_2(X)&=(d^2-5d+10)H^2,\\c_3(X)&=(-d^3+5d^2-10d+10)H^3,\\e(X)&=d(-d^3+5d^2-10d+10).\end{aligned}$$
:::

::: {.front card-id="formula-quintic-threefold-invariants" tags="formula"}
For a smooth quintic threefold $X\subset\mathbb P^4_{\mathbb C}$, compute $K_X,H^3,c_2(X)H,e(X)$ and $\chi(\mathcal O_X(mH))$.
:::

::: {.back card-id="formula-quintic-threefold-invariants"}
$$K_X\sim0,\quad H^3=5,\quad c_2(X)H=50,\quad e(X)=-200,\quad \chi(\mathcal O_X(mH))=\frac{5m^3+25m}{6}.$$
:::

::: {.front card-id="formula-veronese-degree" tags="formula"}
Compute the degree of the image of $\mathbb P^n_{\mathbb C}$ under the $d$-uple Veronese embedding, $d\ge1$.
:::

::: {.back card-id="formula-veronese-degree"}
$$\deg\nu_d(\mathbb P^n)=d^n.$$
:::

::: {.front card-id="formula-segre-degree" tags="formula"}
Compute the degree of $\mathbb P^m_{\mathbb C}\times\mathbb P^n_{\mathbb C}$ in its Segre embedding.
:::

::: {.back card-id="formula-segre-degree"}
$$\deg\operatorname{Seg}(\mathbb P^m\times\mathbb P^n)=\binom{m+n}{m}.$$
:::

::: {.front card-id="formula-grassmannian-degree" tags="formula"}
Compute the Plücker degree of $\operatorname{Gr}(k,n)$, parametrizing $k$-dimensional subspaces of $\mathbb C^n$, for $1\le k<n$.
:::

::: {.back card-id="formula-grassmannian-degree"}
$$\deg\operatorname{Gr}(k,n)=\frac{(k(n-k))!\prod_{i=0}^{k-1}i!}{\prod_{i=0}^{k-1}(n-k+i)!}.$$
:::

::: {.front card-id="formula-grassmannian-two-planes-degree" tags="formula"}
Compute the Plücker degree of $\operatorname{Gr}(2,n)$ and its values for $n=4,5,6$.
:::

::: {.back card-id="formula-grassmannian-two-planes-degree"}
$$\deg\operatorname{Gr}(2,n)=\frac1{n-1}\binom{2n-4}{n-2},\qquad \deg\operatorname{Gr}(2,4)=2,\quad \deg\operatorname{Gr}(2,5)=5,\quad \deg\operatorname{Gr}(2,6)=14.$$
:::

::: {.front card-id="formula-hypersurface-discriminant-degree" tags="formula"}
For $n\ge1,d\ge2$, compute the degree of the discriminant hypersurface of singular degree-$d$ hypersurfaces in $\mathbb P^n_{\mathbb C}$.
:::

::: {.back card-id="formula-hypersurface-discriminant-degree"}
$$\deg\Delta_{n,d}=(n+1)(d-1)^n.$$
:::
