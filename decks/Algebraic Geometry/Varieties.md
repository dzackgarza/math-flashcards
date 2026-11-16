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
Fano of dimension 2: in the smooth convention, a smooth projective surface $X$ with ample anticanonical divisor $-K_X$. Its degree is $K_X^2$. A weak del Pezzo has $-K_X$ nef and big instead; singular del Pezzo variants must specify the allowed singularities and whether $K_X$ is Cartier or only $\mathbb Q$-Cartier.
:::

::: {.front card-id="card-72e647f121eed544"}
Give several examples of Fano varieties.
:::

::: {.back card-id="card-72e647f121eed544"}
For $n\ge1$, $-K_{\mathbb P^n}=\mathcal O(n+1)$, which is very ample.

Any smooth hypersurface $D\subset\mathbb P^n_{\mathbb C}$ with $n\ge2$ and $1\le\deg D<n+1$, since adjunction yields
$$K_D=(K_{\mathbb P^n}+D)|_D
=\bigl(-(n+1)H+\deg(D)H\bigr)|_D,$$
so $-K_D=(n+1-\deg D)H|_D$ is ample. For example, a smooth cubic surface in $\mathbb P^3$ is Fano.
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
Smooth hypersurfaces $D\subset\mathbb P^n_{\mathbb C}$ of degree $n+1$, with $n\ge3$, since adjunction yields
$$K_D=(K_{\mathbb P^n}+D)|_D
=\bigl(-(n+1)H+\deg(D)H\bigr)|_D=0.$$
Use the Lefschetz hyperplane theorem and Hodge decomposition to show $h^q(\mathcal O_D)=0$ for $0<q<n-1$; Lefschetz also gives $\pi_1(D)=1$. The top group has $h^{n-1}(\mathcal O_D)=1$ by Serre duality. Examples are quartic K3 surfaces in $\mathbb P^3$ and quintic threefolds in $\mathbb P^4$.
:::

::: {.front card-id="card-06bc339afe07854e"}
What is the **dimension** of an affine variety?
:::

::: {.back card-id="card-06bc339afe07854e"}
Supremum over all $n$ of lengths of strict chains $C_0\subsetneq\cdots\subsetneq C_n$ of irreducible closed subsets. The length is the number of inclusions. For an integral affine variety over $k$, it equals $\operatorname{trdeg}_k K(X)$.
:::

::: {.front card-id="card-c647f3d346591b35"}
What is the **degree** of a variety?
:::

::: {.back card-id="card-c647f3d346591b35"}
For an $n$-dimensional projective variety with a fixed embedding, the length of its intersection with $n$ general hyperplanes, counted with scheme-theoretic multiplicity. With $H=c_1(\mathcal O_X(1))$, this is $\deg_H X=H^n$, equivalently $n!$ times the leading coefficient of its Hilbert polynomial. The degree depends on the embedding; replacing $H$ by $aH$ multiplies it by $a^n$.
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
For an integral curve over a perfect field (in particular $\mathbb C$), the normalization is normal, hence regular in codimension 1, hence regular, hence smooth. The normalization map is finite and birational and is an isomorphism over the regular locus, so it is a resolution. The perfect-field hypothesis justifies the step from regular to smooth.
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

::: {.front card-id="card-10b63f4aeb034057" tags="theorem"}
For a proper complex scheme $X$, state GAGA for coherent sheaves, their cohomology, and the Picard group.
:::

::: {.back card-id="card-10b63f4aeb034057"}
Analytification gives an equivalence and natural cohomology isomorphisms
$$\operatorname{Coh}(X)\simeq\operatorname{Coh}(X^{\mathrm{an}}),\qquad H^i(X,\mathcal F)\cong H^i(X^{\mathrm{an}},\mathcal F^{\mathrm{an}}).$$
In particular,
$$\operatorname{Pic}(X)\cong\operatorname{Pic}(X^{\mathrm{an}}).$$
:::

::: {.front card-id="card-ded86dc8399712bb"}
What is a projectively normal morphism?
:::

::: {.back card-id="card-ded86dc8399712bb"}
For an integral projective embedding $X\hookrightarrow\mathbb P^N$, projectively normal means its homogeneous coordinate ring is integrally closed. Equivalently, $X$ is normal and
$$H^0(\mathbb P^N,\mathcal O(k))\longrightarrow H^0(X,\mathcal O_X(k))$$
is surjective for every integer $k\ge0$.

For a smooth non-hyperelliptic curve in its canonical embedding, this is the restriction
$$H^0\left(\mathbf{P}^{g-1},\mathcal O(k)\right)\longrightarrow H^0(C,\omega_C^k),$$
surjective for every $k\ge0$ by Max Noether's theorem. Normality of $C$ is automatic here.

$d$-normality asks for just the degree-$d$ restriction to be surjective. Linear normality is $1$-normality. For $d\ge0$, $d$-normality is equivalent to $H^1(\mathbb P^N,I_X(d))=0$. Normality of the variety alone does not imply normality of its homogeneous coordinate ring.

Reference: Caminata–Moon–Schaffler, *On a theorem of L. G. Roberts*, Appendix A.
:::

::: {.front card-id="formula-cyclic-cover-pushforward-canonical" tags="formula"}
For the smooth cyclic cover $f:X\to Y$ of degree $n$ defined by a smooth branch divisor $B\in\lvert L^n\rvert$ on smooth projective $Y/\mathbb C$, compute $f_*\mathcal O_X$ and $\omega_X$.
:::

::: {.back card-id="formula-cyclic-cover-pushforward-canonical"}
$$f_*\mathcal O_X=\bigoplus_{i=0}^{n-1}L^{-i},\qquad \omega_X\cong f^*(\omega_Y\otimes L^{n-1}).$$
:::


::: {.front card-id="formula-double-cover-pushforward-canonical" tags="formula"}
For a smooth double cover $f:X\to Y$ of smooth projective complex varieties defined by a smooth branch divisor in $\lvert L^2\rvert$, compute $f_*\mathcal O_X$ and $\omega_X$.
:::

::: {.back card-id="formula-double-cover-pushforward-canonical"}
$$f_*\mathcal O_X=\mathcal O_Y\oplus L^{-1},\qquad \omega_X\cong f^*(\omega_Y\otimes L).$$
:::







::: {.front card-id="application-gaga-proper-bundles" tags="application"}
Let $X/\mathbb C$ be projective. An analytic vector bundle on $X^{an}$ and a holomorphic morphism between two such bundles are given. Can both be recovered algebraically, and will analytic and algebraic cohomology agree? Identify the theorem.
:::

::: {.back card-id="application-gaga-proper-bundles"}
GAGA is an equivalence of coherent-sheaf categories, so the bundle algebraizes and the morphism comes from a unique algebraic morphism. Local freeness is preserved under this correspondence. GAGA also identifies the analytic cohomology with the algebraic cohomology of the algebraized bundle.
:::

::: {.front card-id="application-gaga-nonproper-counterexample" tags="application"}
Is the holomorphic map $\mathbb A^1_{\mathbb C}{}^{an}\to\mathbb A^1_{\mathbb C}{}^{an}$ given by $z\mapsto e^z$ algebraic? Why does GAGA not force an algebraic map in this case?
:::

::: {.back card-id="application-gaga-nonproper-counterexample"}
An algebraic endomorphism of $\mathbb A^1_{\mathbb C}$ is a polynomial, whereas $e^z$ is not a polynomial. The affine line is not proper, so the properness hypothesis of GAGA is absent. Analytification need not preserve the algebraic space of global sections on a nonproper variety.
:::

::: {.front card-id="card-cda4ef39c2d129e2" tags="definition"}
What is the definition of Affine space?
:::

::: {.back card-id="card-cda4ef39c2d129e2"}
$\mathbb A^n_k=\operatorname{Spec}k[x_1,\dots,x_n]$ is affine $n$-space over $k$, with $k$-points $k^n$. It is a smooth affine variety of dimension $n$, and $\mathbb A^n_k\cong\mathbb P^n_k\setminus V(x_0)$.
:::

::: {.front card-id="card-80713ef54baa2818" tags="definition"}
What is the definition of Affine variety?
:::

::: {.back card-id="card-80713ef54baa2818"}
A variety that is a closed subvariety of affine space $\mathbb A^n_k$; equivalently, $\operatorname{Spec}A$ for a finitely generated integral $k$-algebra $A$.
:::

::: {.front card-id="card-7288765221fc915e" tags="definition"}
What is the definition of Algebraic set?
:::

::: {.back card-id="card-7288765221fc915e"}
A subset $Y\subseteq\mathbb A^n$ (respectively $Y\subseteq\mathbb P^n$) is algebraic if it is the common zero locus $V(T)$ of a set of polynomials (respectively homogeneous polynomials). Equivalently, $Y$ is Zariski closed. An affine or projective variety is an irreducible algebraic set.
:::

::: {.front card-id="card-028eba576c31c295" tags="definition"}
What is the definition of Analytification?
:::

::: {.back card-id="card-028eba576c31c295"}
For a $\mathbb C$-scheme $X$ locally of finite type, the analytification $X^{\mathrm{an}}$ is the complex analytic space with underlying set $X(\mathbb C)$, the analytic topology, and the sheaf of holomorphic functions locally obtained from algebraic functions. A coherent sheaf $\mathcal F$ has an analytification $\mathcal F^{\mathrm{an}}$; for $X$ proper, GAGA gives $\operatorname{Coh}(X)\simeq\operatorname{Coh}(X^{\mathrm{an}})$ and $H^i(X,\mathcal F)\cong H^i(X^{\mathrm{an}},\mathcal F^{\mathrm{an}})$.
:::

::: {.front card-id="card-a923b40b24ddb82d" tags="definition"}
What is the definition of Chern connection?
:::

::: {.back card-id="card-a923b40b24ddb82d"}
For a Hermitian holomorphic vector bundle $(E,h)$ on a complex manifold, the Chern connection is the unique connection compatible with $h$ whose $(0,1)$-part is the holomorphic structure operator $\bar\partial_E$. In a holomorphic frame its connection matrix is $\theta=h^{-1}\partial h$, and its curvature is $\Theta=\bar\partial(h^{-1}\partial h)$.
:::

::: {.front card-id="card-5a5a7328d999ae9d" tags="definition"}
What is the definition of Curvature form?
:::

::: {.back card-id="card-5a5a7328d999ae9d"}
For a Hermitian vector bundle $(E,h)$ with Chern connection $\nabla$, the curvature is $F_\nabla=\nabla^2$, a $2$-form with values in $\operatorname{End}(E)$; locally $F_\nabla=d\theta+\theta\wedge\theta$ for the connection matrix $\theta$. For a line bundle $L$, $\frac{\sqrt{-1}}{2\pi}F_\nabla$ represents $c_1(L)$.
:::

::: {.front card-id="card-35a1ab1ac682520a" tags="definition"}
What is the definition of Fubini-study form?
:::

::: {.back card-id="card-35a1ab1ac682520a"}
The Fubini–Study form on $\mathbb P^n$ is the Kähler form $\omega_{\mathrm{FS}}=\frac{\sqrt{-1}}{2\pi}\partial\bar\partial\log(\sum_{i=0}^n|z_i|^2)$ in homogeneous coordinates. Its cohomology class is the hyperplane class, and it is the curvature of the standard Hermitian metric on $\mathcal O(1)$.
:::

::: {.front card-id="card-2e33a1b484322f31" tags="definition"}
What is the definition of Jacobian criterion?
:::

::: {.back card-id="card-2e33a1b484322f31"}
Let $Y=V(f_1,\dots,f_r)\subseteq\mathbb A^n$ be an affine variety of dimension $d$ over a field, with Jacobian matrix $J=(\partial f_i/\partial x_j)$. Then $Y$ is smooth at $p$ if and only if $\operatorname{rank}J(p)=n-d$; if the rank is less than $n-d$, then $p$ is singular.
:::

::: {.front card-id="card-4ec1c402e82f4a78" tags="definition"}
What is the definition of Morphism of varieties?
:::

::: {.back card-id="card-4ec1c402e82f4a78"}
A morphism of locally ringed spaces over $k$. In the affine case it corresponds to a $k$-algebra homomorphism $k[Y]\to k[X]$, i.e. a map whose coordinate functions are regular (polynomial).
:::

::: {.front card-id="card-9f5ea1864394028d" tags="definition"}
What is the definition of Nonsingular?
:::

::: {.back card-id="card-9f5ea1864394028d"}
A scheme or variety $X$ is nonsingular (smooth) at a point $x$ if the local ring $\mathcal O_{X,x}$ is regular, i.e. $\dim_{\kappa(x)}\mathfrak m_x/\mathfrak m_x^2=\dim\mathcal O_{X,x}$. It is nonsingular if this holds at every point; over a perfect field this agrees with smoothness over $k$.
:::

::: {.front card-id="card-00a61fe475367c6f" tags="definition"}
What is the definition of Positive (1,1)-form?
:::

::: {.back card-id="card-00a61fe475367c6f"}
A real $(1,1)$-form $\omega=\frac{\sqrt{-1}}2\sum h_{j\bar k}\,dz_j\wedge d\bar z_k$ on a complex manifold is positive if the Hermitian matrix $(h_{j\bar k})$ is positive definite at every point. Positivity of a line-bundle curvature $\sqrt{-1}\Theta(L,h)$ is defined by this condition.
:::

::: {.front card-id="card-035a00f28e2c48c8" tags="definition"}
What is the definition of Positive line bundle?
:::

::: {.back card-id="card-035a00f28e2c48c8"}
A line bundle $L$ on a compact complex manifold $X$ is positive if it admits a Hermitian metric $h$ whose Chern curvature $\sqrt{-1}\Theta(L,h)$ is a positive $(1,1)$-form. By the Kodaira embedding theorem, a compact Kähler manifold is projective if and only if it admits a positive line bundle; on a projective variety, $L$ is positive if and only if $L$ is ample.
:::

::: {.front card-id="card-c8c50d3d9fb6620f" tags="definition"}
What is the definition of Projective variety?
:::

::: {.back card-id="card-c8c50d3d9fb6620f"}
A variety that is a closed subvariety of projective space $\mathbb P^n_k$; equivalently, an integral separated scheme of finite type over $k$ admitting a closed immersion into $\mathbb P^n_k$.
:::

::: {.front card-id="card-1fa6363d969b462c" tags="definition"}
What is the definition of Singular point?
:::

::: {.back card-id="card-1fa6363d969b462c"}
A point $x\in X$ at which $\mathcal O_{X,x}$ is not a regular local ring, i.e. $\dim_{\kappa(x)}\mathfrak m_x/\mathfrak m_x^2>\dim\mathcal O_{X,x}$. For an affine variety $V(f_1,\dots,f_r)\subseteq\mathbb A^n$, these are the points where the Jacobian matrix has rank $<n-\dim X$.
:::

::: {.front card-id="card-5346ba4ab0a420de" tags="definition"}
What is the definition of Stable map?
:::

::: {.back card-id="card-5346ba4ab0a420de"}
For a smooth projective complex variety $X$ and $\beta\in H_2(X;\mathbb Z)$, an $n$-pointed stable map of genus $g$ is a map $f:C\to X$ with $f_*[C]=\beta$, where $C$ is connected, nodal, projective, of arithmetic genus $g$, with $n$ distinct marked smooth points. Automorphisms commute with $f$ and fix the marks; their group must be finite.

Equivalently, each contracted rational component has at least three special points, and each contracted genus-one component at least one; special points are markings and branches of nodes. Nonconstant rational components need not have three special points.

The proper Deligne–Mumford stack $\overline{\mathcal M}_{g,n}(X,\beta)$ has complex virtual dimension $(1-g)(\dim X-3)-K_X\cdot\beta+n$. The source need not be stable after forgetting $f$.
:::

::: {.front card-id="card-2b5c1c6d230a4fab" tags="definition"}
What is the definition of Variety?
:::

::: {.back card-id="card-2b5c1c6d230a4fab"}
A separated integral scheme of finite type over a field $k$ (Hartshorne's convention); classically, an irreducible algebraic subset of $\mathbb A^n$ or $\mathbb P^n$ over an algebraically closed field, with its sheaf of regular functions.
:::
