---
title: "Algebraic Geometry::Surfaces::K3 Surfaces"
---

::: {.front card-id="k3-pseudoelliptic-contraction" tags="definition construction example" cite="[@ABE22, §2C]"}
What is a pseudoelliptic surface? For an elliptic K3 with section $S$ and fiber $F$, explain the contraction using $S+2F$ and its effect on a ramification polarization.
:::

::: {.back card-id="k3-pseudoelliptic-contraction"}
A pseudoelliptic surface is obtained by contracting the section of an elliptic surface. The fiber curves survive, but their images meet at the contraction point; they do not define a morphism to the original base. This differs from a genus-one fibration without a section.

For an elliptic K3,
$$S^2=-2,\qquad SF=1,\qquad F^2=0,\qquad
L=S+2F,\quad L^2=2,\quad LS=0.$$
$L$ is nef and big. Its section ring contracts $S$ and the fiber components disjoint from $S$, giving a degree-two polarized surface with du Val singularities. Use a sufficiently divisible multiple of $L$: the degree-one linear system $|S+2F|$ itself has fixed component $S$.

The elliptic involution fixes $S$ and the closure $R'$ of the nonzero two-torsion points. On the minimal elliptic K3 with no reducible fibers, $R'\sim3(S+2F)$. Thus $S+R'$ is not nef, since $(S+R')S=-2$. After contracting $S$, the image of $R'$ is ample. With reducible fibers, first pass to the Weierstrass model by contracting the components disjoint from $S$.
:::

::: {.front card-id="k3-eight-points-order-four" tags="construction example" cite="[@MS18, §2.1]"}
Construct a K3 surface with a purely nonsymplectic order-four automorphism from eight distinct points of $\mathbb P^1$, partitioned into two sets of four.
:::

::: {.back card-id="k3-eight-points-order-four"}
Let $f_4(x_0,x_1)$ and $g_4(x_0,x_1)$ vanish at the two sets. On $\mathbb P^1_x\times\mathbb P^1_y$, set
$$C=(y_0^2f_4+y_1^2g_4=0),\qquad B=C+(y_0=0)+(y_1=0).$$
$B$ has bidegree $(4,4)$. Its eight transverse crossings give eight $A_1$ singularities on the double cover
$$w^2=y_0y_1(y_0^2f_4+y_1^2g_4).$$
Resolve them to obtain a K3: the covering line bundle is $\mathcal O(2,2)=-K_{\mathbb P^1\times\mathbb P^1}$ and the singularities are crepant.

The lift $(y_0,y_1,w)\mapsto(y_0,-y_1,iw)$ has order four; its square is the deck involution. On an affine chart $\omega=dx\wedge dy/w$, it acts by $i$, so every nontrivial power is nonsymplectic.

Relabeling preserves the unordered partition into two blocks: the group is $(S_4\times S_4)\rtimes S_2$, not all of $S_8$. The eight points modulo $\operatorname{PGL}_2$ give dimension five.
:::

::: {.front card-id="k3-even-eight-nikulin-cover" tags="definition construction formula" cite="[@Sch17c, §2.4]"}
Define an even set of disjoint rational curves on a complex K3 surface. Construct the double cover from an even eight and relate it to a Nikulin involution.
:::

::: {.back card-id="k3-even-eight-nikulin-cover"}
For disjoint smooth rational curves $R_i$, an even set means
$$B=\sum_{i=1}^mR_i\sim2L\quad\text{in }\operatorname{Pic}(X)=\operatorname{NS}(X).$$
A nonempty even set has $m=8$ or $16$; an even eight has $m=8$. Divisibility in $\operatorname{NS}(X)\otimes\mathbb Q$ would impose no condition and is insufficient.

For an even eight, a section with zero divisor $B$ gives
$$\pi:\widetilde Y=\operatorname{Spec}_X(\mathcal O_X\oplus\mathcal O_X(-L))\to X.$$
Locally $z^2=s_B$; disjoint smooth branch curves make $\widetilde Y$ smooth. If $E_i$ is the ramification curve, $\pi^*R_i=2E_i$ and
$$4E_i^2=2R_i^2=-4,\qquad K_{\widetilde Y}=\pi^*L=\sum_iE_i.$$
Contract the eight $(-1)$-curves $E_i$: the result $Y$ is K3. The deck involution descends to a symplectic involution on $Y$ with eight isolated fixed points, a **Nikulin involution**. Conversely its quotient has eight $A_1$ points; resolving produces the even eight on $X$.
:::

::: {.front card-id="k3-constant-cycle-beauville-voisin" tags="definition theorem example" cite="[@AE23a, §2; @BV04]"}
Define a constant-cycle curve on a complex K3 surface and the Beauville–Voisin zero-cycle. What does a rational curve supply?
:::

::: {.back card-id="k3-constant-cycle-beauville-voisin"}
A curve $C\subset X$ is **constant-cycle** if all its closed points have the same class in $\operatorname{CH}_0(X)$. Equivalently, the pushforward from $\operatorname{Pic}^0(\widetilde C)$ to $\operatorname{CH}_0(X)$ is zero, for the normalization $\widetilde C$.

For projective K3 $X$, the Beauville–Voisin class $o_X\in\operatorname{CH}_0(X)$ is the degree-one class of a point on any rational curve. The theorem makes it independent of the point and rational curve, and gives
$$D\cdot E=\deg(D\cdot E)o_X,\qquad c_2(X)=24o_X.$$
A rational curve is constant-cycle because its normalization is $\mathbb P^1$ and any two points there are rationally equivalent. Positive-genus constant-cycle curves also exist; constant-cycle does not mean rational.
:::

::: {.front card-id="k3-flex-point-divisor" tags="definition construction example" cite="[@AE23a, §1 and Definitions 2.2 and 2.8]"}
Define a flex point for a polarized K3 surface. On smooth surfaces for which no pencil in $|L|$ has a base curve, construct the flex divisor with its multiplicities. What is its role in stable-pair compactifications?
:::

::: {.back card-id="k3-flex-point-divisor"}
For a polarized K3 $(X,L)$, a point $x$ is **flex** if a pencil $V\subset|L|$ has set-theoretic base locus $\{x\}$. It need not be a reduced basepoint: when $L^2=2d$, the intersection is a length-$2d$ zero-dimensional scheme supported at $x$.

Assume $X$ is smooth over $\mathbb C$, $L$ is primitive and ample, and no pencil in $|L|$ has a base curve. Set $G=\operatorname{Gr}(2,H^0(X,L))$. Taking the scheme-theoretic base locus gives a closed immersion $i:G\hookrightarrow X^{[2d]}$ into the Hilbert scheme. For the Hilbert–Chow map $HC:X^{[2d]}\to X^{(2d)}$, put
$$\Delta=\{2d[x]:x\in X\},\qquad P_{2d}=HC^{-1}(\Delta),\qquad R_{\mathrm{flex}}=\operatorname{supp}_*[P_{2d}\cap i(G)].$$
The inverse image and intersection are scheme-theoretic; $\operatorname{supp}:P_{2d}\to X$ sends a punctual subscheme to its support. The intersection is pure one-dimensional and finite over its image in $X$. Its fundamental cycle supplies the multiplicities of the flex divisor.

Example: two members of the pencil may meet only at $x$, with total intersection multiplicity $2d$. Replacing this by “they meet transversely at $x$” would contradict $L^2=2d$.

Use: an algebraically varying canonical polarizing divisor gives pairs $(X,\epsilon R_{\mathrm{flex}})$ whose closure defines a stable-pair compactification. Identifying its normalization as semitoroidal requires recognizability as an additional theorem; the cited paper constructs the divisor and investigates this question.
:::

::: {.front card-id="construction-k3-complete-intersections" tags="construction application"}
Construct K3 surfaces as smooth complete intersections in ordinary complex projective space. After removing linear equations, which multidegrees work? How do you ensure smoothness and verify the K3 conditions?
:::

::: {.back card-id="construction-k3-complete-intersections"}
For a surface $S\subset\mathbb P^{r+2}$ of multidegree $(d_1,\ldots,d_r)$ with $d_i\ge2$, adjunction gives
$$\omega_S=\mathcal O_S\left(\sum_i d_i-r-3\right).$$
Thus $\sum_i(d_i-1)=3$, giving $(4)$, $(2,3)$, or $(2,2,2)$. Choose general equations: successive Bertini applications give smooth intersections. Weak Lefschetz gives $H^1(S,\mathbb C)=0$, hence $q(S)=0$. The hyperplane polarizations have squares $4$, $6$, and $8$, respectively.
:::

::: {.front card-id="construction-k3-kummer-resolution" tags="construction application"}
Starting with a complex abelian surface $A$, construct a smooth K3 surface. What happens to the holomorphic two-form, irregularity, and exceptional curves?
:::

::: {.back card-id="construction-k3-kummer-resolution"}
Resolve the quotient $A/\langle-1\rangle$ minimally. Its $A_1$ singularities are du Val, so the resolution is crepant and their exceptional curves are disjoint smooth rational $(-2)$-curves. Inversion preserves the nowhere-vanishing two-form on $A$, which descends and extends without zeros. Since $[-1]^*|_{H^1(A,\mathcal O_A)}=-\mathrm{id}$, $H^1(A,\mathcal O_A)^{\langle-1\rangle}=0$. Finite-quotient cohomology and rationality of the singularities give $q(\operatorname{Km}(A))=0$.
:::

::: {.front card-id="construction-k3-product-kummer-equation" tags="construction application"}
Let $E_i$ be complex elliptic curves with affine equations $y_i^2=f_i(x_i)$, where $f_i$ is a squarefree cubic. Give a birational equation for $\operatorname{Km}(E_1\times E_2)$ and describe its branch divisor.
:::

::: {.back card-id="construction-k3-product-kummer-equation"}
The invariant $z=y_1y_2$ gives
$$z^2=f_1(x_1)f_2(x_2).$$
Compactify as a double cover of $\mathbb P^1\times\mathbb P^1$. The branch divisor consists of the four vertical and four horizontal fibers over the branch points of the elliptic double covers, including infinity. Their crossings give $A_1$ singularities; the minimal resolution is the Kummer K3. Thus a reducible $(4,4)$ branch divisor can produce a K3 after resolution, although the double cover is not smooth.
:::

::: {.front card-id="construction-k3-weierstrass" tags="construction application" cite="[@SS10]"}
Construct a complex elliptic K3 surface with section by a Weierstrass equation over $\mathbb P^1$. Specify the coefficient bundles and the conditions to check, including at infinity.
:::

::: {.back card-id="construction-k3-weierstrass"}
Take $L=\mathcal O_{\mathbb P^1}(2)$ and the relative Weierstrass equation
$$y^2z=x^3+a_4xz^2+a_6z^3,\qquad a_4\in H^0(\mathcal O(8)),\quad a_6\in H^0(\mathcal O(12)).$$
Require $\Delta=-16(4a_4^3+27a_6^2)\not\equiv0$ and minimality: at no point are both $\operatorname{ord}(a_4)\ge4$ and $\operatorname{ord}(a_6)\ge6$. Check this in local trivializations also at infinity. Resolve the Weierstrass model to its smooth relatively minimal elliptic surface $f:S\to\mathbb P^1$. The canonical bundle formula gives $\omega_S=f^*(\omega_{\mathbb P^1}\otimes L)\cong\mathcal O_S$; Leray gives $q(S)=0$ since $H^1(\mathcal O_{\mathbb P^1})=H^0(L^{-1})=0$. The discriminant is a section of $\mathcal O(24)$.
:::

::: {.front card-id="construction-k3-quadratic-base-change" tags="construction application" cite="[@SS10, quadratic base change]"}
Let $f:R\to\mathbb P^1_{\mathbb C}$ be a relatively minimal rational elliptic surface with section. How can a quadratic base change produce a K3? Choose branch points that make the construction straightforward and describe the singular fibers afterward.
:::

::: {.back card-id="construction-k3-quadratic-base-change"}
Choose a double cover $g:\mathbb P^1\to\mathbb P^1$ branched over two distinct smooth fibers of $f$, and form $S=R\times_{\mathbb P^1}\mathbb P^1$. The surface is smooth: over singular fibers the base change is étale, and over branch points $f$ is smooth. The section pulls back. The fundamental line bundle changes from $\mathcal O(1)$ to $g^*\mathcal O(1)=\mathcal O(2)$, so the canonical bundle formula and Leray give $\omega_S\cong\mathcal O_S$ and $q(S)=0$. Each singular fiber of $R$ occurs twice with the same Kodaira type; the branch fibers remain smooth.
:::

::: {.front card-id="construction-k3-anticanonical" tags="construction application" cite="[@Bea02]"}
Let $V$ be a smooth complex Fano threefold and $S\in|-K_V|$ smooth. Determine whether $S$ is K3. Use this construction to give examples in $\mathbb P^1\times\mathbb P^2$ and $(\mathbb P^1)^3$.
:::

::: {.back card-id="construction-k3-anticanonical"}
Adjunction gives $\omega_S\cong\mathcal O_S$. Kodaira vanishing gives $H^i(V,\mathcal O_V)=0$ for $i>0$; Serre duality gives $H^2(V,K_V)=0$. The sequence
$$0\longrightarrow\mathcal O_V(K_V)\longrightarrow\mathcal O_V\longrightarrow\mathcal O_S\longrightarrow0$$
then gives $H^0(S,\mathcal O_S)=\mathbb C$ and $H^1(S,\mathcal O_S)=0$. Thus $S$ is K3. In the products, take a general equation of bidegree $(2,3)$ or tridegree $(2,2,2)$, respectively. These anticanonical systems are base-point-free, so Bertini supplies smooth members.
:::

::: {.front card-id="construction-k3-enriques-cover" tags="construction application"}
Given a complex Enriques surface $Y$, construct its canonical cover and determine its degree, ramification, and surface type.
:::

::: {.back card-id="construction-k3-enriques-cover"}
The nontrivial line bundle $\omega_Y$ has order two. Choose $\omega_Y^{\otimes2}\cong\mathcal O_Y$ and form
$$X=\operatorname{Spec}_Y(\mathcal O_Y\oplus\omega_Y^{-1}).$$
The multiplication uses this trivialization. The cover is connected and étale of degree two, and $\omega_X=\pi^*\omega_Y\cong\mathcal O_X$. Since $H^1(Y,\mathcal O_Y)=H^1(Y,\omega_Y)=0$, one has $q(X)=0$. Thus $X$ is K3 and its deck involution is fixed-point-free.
:::

::: {.front card-id="card-cd4f095b6e904394"}
What is a primitively polarized K3 of genus $g$?
:::

::: {.back card-id="card-cd4f095b6e904394"}
$(X, \eta)$ where $\eta\in H^{1,1}(X; {\mathbf{R}})$ is a Kahler class.

Torelli: iso type of $(X, \eta)$ completely determined by $(H^2(X;\ZZ), \cap)$, $\eta$, and the HS on $H^2(X;\CC)$.

Primitive: not a proper multiple of an integral class.

$g\coloneqq 1+{1\over 2}(\eta.\eta)$; the linear system $\eta$ defines contains curves of arithmetic genus $g$.
:::

::: {.front card-id="card-34fab36bd27bc9e8" tags="theorem"}
State global Torelli for complex K3 surfaces, its polarized form, and the resulting description of the automorphism group.
:::

::: {.back card-id="card-34fab36bd27bc9e8"}
Isomorphisms $\sigma: X^{\prime} \rightarrow X$ are in bijection with the isometries $\sigma^*: H^2(X, \mathbb{Z}) \rightarrow H^2\left(X^{\prime}, \mathbb{Z}\right)$ satisfying $\sigma^*\left(H^{2,0}(X)\right)=H^{2,0}\left(X^{\prime}\right)$ and $\sigma^*\left(\mathcal{K}_X\right)=\mathcal{K}_{X^{\prime}}$.

So a Hodge isometry is induced by an isomorphism exactly when it is effective, i.e. maps the Kahler cone to the Kahler cone; e.g. $-\operatorname{id}$ is a Hodge isometry that is not induced by an automorphism.

Strong Torelli for polarized K3s: if $(X, L)$ and $(X', L')$ are polarized K3s and $\varphi: H^2(X;\ZZ) { \, \xrightarrow{\sim}\, }H^2(X';\ZZ)$ is a Hodge isometry with $\varphi(c_1(L)) = c_1(L')$, then $\varphi = f^*$ for a unique isomorphism $f:X' { \, \xrightarrow{\sim}\, }X$.

In particular, two complex K3 surfaces are isomorphic if and only if their integral second cohomology groups admit a Hodge isometry. For one surface,
$$\operatorname{Aut}(X)\cong\{g\in O_{\mathrm{Hdg}}(H^2(X,\mathbb Z)):g(\mathcal K_X)=\mathcal K_X\},$$
as groups via $f\mapsto(f^{-1})^*$.
:::

::: {.front card-id="card-5bb9c6a0085b74b6"}
Discuss the number of fixed points of a symplectic automorphism with finite order $n$.
:::

::: {.back card-id="card-5bb9c6a0085b74b6"}
Computed by Mukai using the Lefschetz fixed point formula: $n\leq 8$, and ${\sharp} \mathrm{Fix}(\sigma) = 8, 6, 4, 4, 2, 3, 2$ for $n = 2, 3, 4, 5, 6, 7, 8$.

Sketch for $n = p$ prime: take $X\twoheadrightarrow X/\sigma$ and resolve its $A_{p-1}$ singularities to get $Y$.

Write $X' \coloneqq X\setminus \mathrm{Fix}(\sigma)$ and $Y' \coloneqq Y\setminus\widetilde{ \mathrm{Fix}}(\sigma)$, where $\widetilde{ \mathrm{Fix}}(\sigma)$ are the corresponding rational curves. Then $X'\to Y'$ is an unramified $p\dash$to-$1$ cover, so $\chi(X') = p\chi(Y')$.

Each fixed point gives a chain of $p-1$ copies of ${\mathbf{P}}^1$ meeting at $p-2$ points, with $\chi = 2(p-1) - (p-2) = p$.

Combine these to get
$$\chi(X) - {\sharp} \mathrm{Fix}(\sigma) = p\cdot \chi(Y)- p^2\cdot {\sharp} \mathrm{Fix}(\sigma) \implies {\sharp} \mathrm{Fix}(\sigma) = {24\over p+1}$$
since $Y$ is also a K3 and thus $\chi(X) = \chi(Y) = 24$.
:::

::: {.front card-id="card-ae6984def8dbe005"}
Discuss the classification of symplectic actions.
:::

::: {.back card-id="card-ae6984def8dbe005"}
Abelian $G\curvearrowright X$ symplectically (Nikulin), 14 possibilities:

$C_n$ where $n=2,\cdots, 8$.

$C_n^2$ where $n=2,3,4$.

$C_2\times C_n$ where $n=4,6$.

$C_2^3$

$C_2^4$.

Arbitrary finite $G\curvearrowright X$ symplectically (Mukai): $G$ is a subgroup of the Mathieu group $M_{23}$ with at least 5 orbits on $\left\{{1, \cdots, 24}\right\}$, so ${\sharp}G \leq 960$, with equality if $G = M_{20}$.

Xiao: 80 possible groups, maximal size of 960.
:::

::: {.front card-id="card-4c8504ee4f1a1bdb"}
Why does every K3 contain a rational curve?
:::

::: {.back card-id="card-4c8504ee4f1a1bdb"}
Bogomolov-Mumford: degenerate to a Kummer which is a product of two special elliptic curves

Construct a configuration of rational curves there

Use irreducibility of $F_{2d}$ to deform to the general K3, possibly making it reducible, but has at least one irreducible.

Use one of the irreducible curves, then specialize to any K3 in $F_{2d}$, the curve can only break into rational curves.
:::

::: {.front card-id="card-303566e8177e0ec5"}
Discuss rational curves on K3s.
:::

::: {.back card-id="card-303566e8177e0ec5"}
Always has at least one.

Any nonzero $D\in \operatorname{Pic}(X)^\mathsf{eff}$ satisfies $D\sim \sum R_i$ for some rational curves.

Over $k=\CC$ $X$ is never uniruled, i.e. no rational curves move.

Conjecture: $X/\overline{k}$ has infinitely many rational curves.
:::

::: {.front card-id="card-d6ef2e2a6407833d"}
What is a Kummer surface?
:::

::: {.back card-id="card-d6ef2e2a6407833d"}
The minimal resolution $\operatorname{Km}(A)$ of $A/\langle-1\rangle$, where $A$ is a complex two-dimensional torus. The quotient has an $A_1$ singularity at the image of each point of $A[2]$. The resolution is a K3 surface; it is projective when $A$ is an abelian surface.
:::

::: {.front card-id="card-e0924526d2ecf9d1"}
Classify surfaces by $\kappa(S)$.
:::

::: {.back card-id="card-e0924526d2ecf9d1"}
$-\infty$: Rational or ruled.

$0$: Four types; abelian, K3s, Enriques, bielliptic.

$1:$ Proper elliptic.

$2$: General type.
:::

::: {.front card-id="card-db418b0ec438a9a3"}
What's the etymology of K3?
:::

::: {.back card-id="card-db418b0ec438a9a3"}
Named after K2 mountains

Or Kummer, Kahler, Kodaira.
:::

::: {.front card-id="card-a0c53897863d4619"}
Let $X_4\subset\mathbb P^3_{\mathbb C}$ be the Fermat quartic surface. What is $K_{X_4}$?
:::

::: {.back card-id="card-a0c53897863d4619"}
By adjunction, $K_{X_4} = (K_{{\mathbf{P}}^3} + X_4)\mathrel{\Big|}_{X_4} = (-4H + 4H)\mathrel{\Big|}_{X_4} = 0$.
:::

::: {.front card-id="card-a974a6a357f3c50a"}
What is the fundamental group of the complex Fermat quartic surface $X_4\subset\mathbb P^3$?
:::

::: {.back card-id="card-a974a6a357f3c50a"}
By Lefschetz, $\pi_1(X_4) = \pi_1({\mathbf{P}}^3) = 1$.
:::

::: {.front card-id="card-4dbd0152fa065638"}
Compute the irregularity $q(X_4)$ of the complex Fermat quartic surface.
:::

::: {.back card-id="card-4dbd0152fa065638"}
For the complex Fermat quartic, simple connectivity gives $H_1(X_4,\mathbb Z)=0$. Hence
$$0=H^1(X_4,\mathbb C)=H^{1,0}(X_4)\oplus H^{0,1}(X_4),$$
so $q(X_4)=h^{0,1}(X_4)=0$.
:::

::: {.front card-id="card-a83a6fcf30b32ed7"}
What conditions define a complex K3 surface? Does blowing up a point preserve those conditions?
:::

::: {.back card-id="card-a83a6fcf30b32ed7"}
A smooth connected compact complex surface $S$ with $\omega_S\cong\mathcal O_S$ and $H^1(S,\mathcal O_S)=0$. For a point blowup $\pi:\widetilde S\to S$ with exceptional curve $E$,
$$K_{\widetilde S}=\pi^*K_S+E=E.$$
Thus $\widetilde S$ is birational to a K3 but is not itself a K3.
:::

::: {.front card-id="card-d8dece29c26816e2"}
For a smooth connected complex projective surface $S$ given by equations or a finite cover, which invariants establish that it is K3? Which tools commonly compute them?
:::

::: {.back card-id="card-d8dece29c26816e2"}
Establish $\omega_S\cong\mathcal O_S$ and $H^1(S,\mathcal O_S)=0$. Use adjunction for complete intersections and the canonical bundle formula for covers or elliptic fibrations. Compute $H^1$ by Lefschetz and Hodge decomposition, a finite-cover pushforward, a defining exact sequence, or Leray, as appropriate. The numerical equality $K_S^2=0$ alone does not establish triviality of $\omega_S$.
:::

::: {.front card-id="card-d4ca0d9726924b5c"}
Give several examples of K3s.
:::

::: {.back card-id="card-d4ca0d9726924b5c"}
Any smooth quartic in $\mathbb P^3$, for example $V(x_0^4+\cdots+x_3^4)$ over $\mathbb C$.

A smooth complete intersection of type $(d_1,\cdots, d_n) \subset {\mathbf{P}}^{n+2}$ with all $d_i\geq 2$ and $\sum d_i = n+3$: the quartic and the types $(2,3)$ and $(2,2,2)$.

Kummer surfaces: the quotient of an abelian surface by the involution $x\mapsto -x$ after resolving 16 singular points.

A double plane: a double cover $X\to {\mathbf{P}}^2$ branched along a smooth curve $C$ of degree 6, using $\pi_* {\mathcal{O}}_X \cong {\mathcal{O}}_{{\mathbf{P}}^2} \oplus {\mathcal{O}}(-3) \implies H^1({\mathcal{O}}_X) = 0$ and $\omega_X \cong \pi^*(\omega_{{\mathbf{P}}^2} \otimes{\mathcal{O}}(3)) \cong {\mathcal{O}}_X$.
:::

::: {.front card-id="card-c9537c6e8b69fd2a"}
Let $\pi:S\to\mathbb P^2_{\mathbb C}$ be the double cover branched over a smooth sextic. Compute $\omega_S$, $q(S)$, and $e(S)$, and decide whether $S$ is K3.
:::

::: {.back card-id="card-c9537c6e8b69fd2a"}
The cover is defined by $L=\mathcal O_{\mathbb P^2}(3)$ and a section of $L^2$ with smooth zero divisor $B$. The double-cover formulas give
$$\pi_*\mathcal O_S=\mathcal O_{\mathbb P^2}\oplus\mathcal O_{\mathbb P^2}(-3),\qquad
\omega_S=\pi^*(\omega_{\mathbb P^2}\otimes L)\cong\mathcal O_S.$$
Both summands have vanishing $H^1$, so $q(S)=0$ and $S$ is K3. Since $g(B)=10$,
$$e(S)=2e(\mathbb P^2)-e(B)=6-(2-20)=24.$$
:::

::: {.front card-id="card-87f15ed99f31bbce"}
Give an equation for the double plane.
:::

::: {.back card-id="card-87f15ed99f31bbce"}
$S: t^2 = f_6(x_0, x_1, x_2) \subseteq {\mathbf{P}}(3,1,1,1)$ where $C_6 = V(f_6)$.
:::

::: {.front card-id="card-96d7a76cd22ee066"}
Which involution on a complex abelian surface gives the Kummer construction? Identify its fixed points and the local quotient singularities.
:::

::: {.back card-id="card-96d7a76cd22ee066"}
Use inversion $\iota(a)=-a$. For $A=\mathbb C^2/\Lambda$,
$$\operatorname{Fix}(\iota)=A[2]\cong(\mathbb Z/2\mathbb Z)^4.$$
At a fixed point the action is $(x,y)\mapsto(-x,-y)$. The invariant coordinates $u=x^2$, $v=y^2$, $w=xy$ satisfy $uv=w^2$, so each image is an $A_1$ singularity. Each resolves to a smooth rational curve of square $-2$.
:::

::: {.front card-id="card-bc593360b0b42e7f"}
In the Kummer construction over $\mathbb C$, blow up the fixed points of inversion on an abelian surface. Describe the lifted involution in a blowup chart and check that its quotient is smooth there.
:::

::: {.back card-id="card-bc593360b0b42e7f"}
At a fixed point inversion acts by $(x,y)\mapsto(-x,-y)$. In the blowup chart $y=xu$, it acts by $(x,u)\mapsto(-x,u)$. The invariant ring is $\mathbb C[x^2,u]$, so the quotient is smooth in this chart; the other chart is analogous. The exceptional $\mathbb P^1$ is fixed pointwise. Its image is the exceptional $(-2)$-curve resolving the quotient node.
:::

::: {.front card-id="card-af30b3367d559ae0"}
What is $\chi({\mathsf{K}}3)$?
:::

::: {.back card-id="card-af30b3367d559ae0"}
$\chi({\mathsf{K}}3) = 24$, all diffeomorphic to the Fermat quartic.
:::

::: {.front card-id="card-941b89a280b25084"}
Describe the lattice $\Lambda_{{\mathsf{K}}3}$.
:::

::: {.back card-id="card-941b89a280b25084"}
The lattice associated to a K3 $X$ is $H^2(X; \ZZ)$ with the intersection pairing
$$\begin{align*}H^2(X; \ZZ){ {}^{ \scriptstyle\otimes_{\ZZ}^{2} }  } &\to \ZZ\\ \alpha\otimes\beta &\mapsto \int_X \alpha\wedge \beta\end{align*}$$
which is nondegenerate and unimodular by Poincare duality. $\Lambda_{{\mathsf{K}}3}$ denotes this lattice structure on (all of) $H^2({\mathsf{K}}3; \ZZ)$:

Rank $22$

Signature $(3, 19)$

Even, unimodular

Isometric to $U{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  }$ where

$U = H = \qty{\ZZ^2, \left(\begin{array}{ll}0 & 1 \\1 & 0\end{array}\right)}$ is the hyperbolic plane,

$E_8(-1) =$ unique even unimodular negative-definite lattice of rank 8.
:::

::: {.front card-id="card-e198deda38cb0b29"}
What is the rank of $\Lambda_{{\mathsf{K}}3}$? Proof?
:::

::: {.back card-id="card-e198deda38cb0b29"}
$\chi({\mathsf{K}}3) = 24$ and $p_{{\mathsf{K}}3}(t) = 1 + b_2 t^2 + t^4$ since $b_1 = b_3 = 0$ from $\pi_1({\mathsf{K}}3) = 1$ and $b_0 = b_4 = 1$ from connectedness, thus $\beta_2 = 22$.
:::

::: {.front card-id="card-4f61f550123f13e4"}
Why is $H^2({\mathsf{K}}3; \ZZ)$ torsionfree?
:::

::: {.back card-id="card-4f61f550123f13e4"}
By UCT, $H^2({\mathsf{K}}3;\ZZ)_\tors\cong H_2({\mathsf{K}}3; \ZZ)_\tors$. If $m\tau = 0$ in the latter, construct an unramified cover $i: \tilde S\to S$ with $\chi(\tilde S) = m\chi(S) = 24m$.

Since $i$ is unramified, pulling back a top form yields $K_{\tilde S} \sim 0$.

Noether formula: $\chi({\mathcal{O}}_{\tilde S}) = {1\over 12} (K_{\tilde S}^2 + \chi(\tilde S)) = 2m$.

The LHS is $2-h^1({\mathcal{O}}_{\tilde S}) \leq 2$, the RHS is $\geq 2$, so $m=1$.
:::

::: {.front card-id="card-f64f587ee4649484"}
What is $\operatorname{sgn}\Lambda_{\mathrm{K3}}$?
:::

::: {.back card-id="card-f64f587ee4649484"}
$\operatorname{sgn}\Lambda_{\mathrm{K3}} = \operatorname{sgn}H^2(X; \ZZ) = (3, 19)$.

Proof: write $\operatorname{sgn}\Lambda_{{\mathsf{K}}3} = (s_+, s_-)$, where $s_+ + s_- = b_2(X) = 22$. By the Thom-Hirzebruch index theorem,
$$s_+- s_- = {1\over 3}p_1(X) = {1\over 3}(c_1^2  -2c_2) = {1\over 3}(0-2\cdot24)= -16$$
where $c_1 = c_1({\mathbf{T}}X) = -K_X = 0$ and $c_2 = \chi(X) = 24$.

Combine $s_+ + s_- = 22$ and $s_+ - s_- = -16$ to solve for $(s_+, s_-) = (3, 19)$.
:::

::: {.front card-id="card-6098bf6e2115e6a2"}
Why is $\Lambda_{\mathrm{K3}}$ even?
:::

::: {.back card-id="card-6098bf6e2115e6a2"}
Take an irreducible curve $C\subseteq X$ and use the genus formula:
$$g(C) = 1 + {1\over 2}\qty{C.K_X + C^2} \implies C^2 = 2g-2 \in 2\ZZ$$
:::

::: {.front card-id="card-2dce7321f873d95b"}
Discuss positivity of $\beta_{{\mathsf{K}}3}({-}, {-})$ on $\omega_X$.
:::

::: {.back card-id="card-2dce7321f873d95b"}
$$\beta(\omega_X, \overline{\omega}_X)=\int_S \omega_X \wedge \overline{\omega}_X = \int_X {\left\lvert {f} \right\rvert}\,dz_1\wedge\,dz_2 \wedge\overline{\,dz_1} \wedge \overline{\,dz_2} > 0$$
Similarly $\beta(\omega_X, \omega_X) = 0$.

If $\beta(\omega_X, H^{1, 1}) = 0$ so $H^{1, 1} \perp_\beta (H^{2, 0} \oplus H^{0,2})$
:::

::: {.front card-id="card-cae2e5effcd67939"}
What is the degree of a projective K3?
:::

::: {.back card-id="card-cae2e5effcd67939"}
$L^2 = 2d$ for $L$ a hyperplane section of its projective embedding.

Even since $L = \phi(S) \cap H \in H^2(S; \ZZ) \cap H^{1, 1}(S)$ which is an even lattice.
:::

::: {.front card-id="card-d298f04cbf91b770"}
Describe $[\omega_S]$.
:::

::: {.back card-id="card-d298f04cbf91b770"}
$$[\omega_S]\in \left\{{[\omega] \in {\mathbf{P}}(L^\perp\otimes\CC) \st{\left\lvert {\omega} \right\rvert} > 0,\, \omega^2 = 0 }\right\}$$
Here $\dim L = 1$ so $\dim L^\perp = 20-1 = 19$.
:::

::: {.front card-id="card-4bd67f251195c762"}
What is the degree of $F_4$?
:::

::: {.back card-id="card-4bd67f251195c762"}
Embed $F_4\hookrightarrow{\mathbf{P}}^3$ and slice by a hyperplane to get 4 points, so $L^2 = 4$ and $d=2$.
:::

::: {.front card-id="card-dc1fb84c7694aa1f"}
Describe $c_1(L)$ for a K3 and its relation to $\operatorname{Pic}$ and $\NS$.
:::

::: {.back card-id="card-dc1fb84c7694aa1f"}
Take the exponential SES $\ZZ\hookrightarrow{\mathcal{O}}_S \twoheadrightarrow{\mathcal{O}}_S^{\times}$ to get $\delta^1: H^1(S; {\mathcal{O}}_S^{\times}) \to H^2(S; \ZZ)$, identify $H^1$ with $\operatorname{Pic}$ and $c_1 = \delta^1$.

Get $\operatorname{Pic}^0(S) = \ker c_1$ and $\operatorname{Pic}(S)/\operatorname{Pic}^0(S)\cong \operatorname{im}c_1 = \NS(X)$.
:::

::: {.front card-id="card-8a1535e682e731af"}
Discuss $\NS(X)$ for $X$ a K3.
:::

::: {.back card-id="card-8a1535e682e731af"}
$\operatorname{Pic}^0(X) = 0$ so $\operatorname{Pic}(X) \cong \NS(X)$, the sublattice of $H^{2}(X; \ZZ)$ generated by algebraic cycles. By Lefschetz $(1, 1)$,
$$\operatorname{Pic}(X) = \NS(X) = H^{2, 0}(X)^\perp \cap H^2(X; \ZZ) \subseteq H^2(X; \CC)$$
$\NS(X)\hookrightarrow H^2(X; \ZZ)$ is an even primitive sublattice of $\Lambda_{\mathrm{K3}}$, of rank $\rho(X)$, the Picard number.

If $X$ is projective, $\NS(X)$ is nondegenerate of signature $(1, \rho(X) - 1)$.

$T_X \coloneqq\NS(X)^\perp$ is also a lattice (transcendental).
:::

::: {.front card-id="card-4a998156627e92cf"}
How is the Lefschetz 1-1 theorem used for K3s?
:::

::: {.back card-id="card-4a998156627e92cf"}
$\NS(X) = \operatorname{Pic}(X) = H^{1, 1}(X) \cap H^2(X; \ZZ) = \omega_S^\perp \cap H^2(X;\ZZ)$.
:::

::: {.front card-id="card-4179669dbcacc189"}
Discuss $\operatorname{sgn}\NS(X)$ and $\operatorname{sgn}T_X$.
:::

::: {.back card-id="card-4179669dbcacc189"}
$\operatorname{sgn}\NS(X) = (a, b)$ where $a\leq 1$: $\operatorname{sgn}H^2(X;\ZZ) = (3, 19)$, and $H^{2, 0} \oplus H^{0, 2} = \CC\omega_X \oplus \CC\overline{\omega_X}$ gives a real 2-dimensional space $V = \left\langle{\omega_X + \overline{\omega}_X, i(\omega_X - \overline{\omega}_X)}\right\rangle$ where both generators have positive square, and $V\subseteq (H^{1,1})^\perp$.

For $X$ projective, an ample class $L$ with $L^2 > 0$ yields
$$\operatorname{sgn}S_X = \operatorname{sgn}\NS(X) = (1, \rho(X) - 1) \implies \operatorname{sgn}T_X = (2, 20-\rho(X))$$
since they must add up to $(3, 19)$.
:::

::: {.front card-id="card-c4ebdb920576685f"}
What is the transcendental lattice? Its signature?
:::

::: {.back card-id="card-c4ebdb920576685f"}
$T(X) = T_X \coloneqq\NS(X)^\perp \subseteq H^2(X; \ZZ)$, the orthogonal complement of Neron-Severi, where $\NS(X) \simeq \operatorname{Pic}(X) \simeq H^{1,1}(X) \cap H^2(X, \mathbf{Z})$. It is usually considered as an integral Hodge structure.

$T_X \otimes\CC\supseteq H^{2, 0} \oplus H^{0, 2}$, so the periods move in $T_X$: for a polarization $L$, $[\omega_X] \in \left\{{ {\mathbf{P}}(T_X^L\otimes\CC) \st\omega^2 = 0, \omega.\overline{\omega} > 0}\right\}$ where $T_X^L = L^\perp$.

If $X$ is projective:

$\NS(X)$ is nondegenerate, and $T(X)$ is the smallest primitive sublattice of $H^2(X; \ZZ)$ whose complexification contains $H^{2, 0}(X)$.

Signature $(2, 20-\rho(X))$.

$T(X)$ is a polarizable irreducible Hodge structure.

For nonprojective K3s, $T(X) + \NS(X) \subseteq H^2(X; \ZZ)$ need not be direct and $T(X)$ need not be irreducible nor polarizable.
:::

::: {.front card-id="card-9bab5774b88b5564"}
Discuss $\operatorname{Pic}(X)$ for a generic projective K3.
:::

::: {.back card-id="card-9bab5774b88b5564"}
Generically $\operatorname{Pic}(X) = \left\langle{L}\right\rangle_\ZZ$ for $L$ associated to the hyperplane section.
:::

::: {.front card-id="card-cf4969638484b2a6" cite="[@Mor88a, projective models]"}
Let $L$ be a base-point-free line bundle with $L^2>0$ on a complex projective K3 surface. What is the dimension of $|L|$, and when can its morphism fail to be an embedding? Describe the very ample models of degrees four, six, and eight.
:::

::: {.back card-id="card-cf4969638484b2a6"}
Riemann–Roch and vanishing give $h^0(L)=2+L^2/2$, so $|L|$ maps to $\mathbb P^{1+L^2/2}$. The morphism can have degree two onto a surface of degree $L^2/2$, or be birational onto a surface of degree $L^2$. It contracts precisely the curves $C$ with $L\cdot C=0$.

For $L$ very ample, degree four gives a quartic in $\mathbb P^3$, and degree six gives a $(2,3)$ complete intersection in $\mathbb P^4$. In degree eight, the model in $\mathbb P^5$ is an intersection of three quadrics exactly when its general hyperplane section is not trigonal. Equivalently, the trigonal exception has an elliptic pencil $E$ with $L\cdot E=3$.
:::

::: {.front card-id="card-dfe46593dd91df51"}
Discuss $\mathop{\mathrm{Aut}}(X)$.
:::

::: {.back card-id="card-dfe46593dd91df51"}
Torelli induces $\mathop{\mathrm{Aut}}(X) \hookrightarrow{\operatorname{O}}(H^2(X; \ZZ))$

Image is effective Hodge isometries: preserves 2-forms and Kahler cones.

Discrete and finitely generated.

Generically trivial when $\operatorname{Pic}(X) = \left\langle{L}\right\rangle_\ZZ$ for $d\neq 1$.

If $\sigma$ preserves an ample class then it must have finite order.
:::

::: {.front card-id="card-9689dd1d644fe056"}
What is a symplectic automorphism?
:::

::: {.back card-id="card-9689dd1d644fe056"}
$\sigma^* \omega_X = \omega_X$, i.e. preserves the symplectic form.

If $\sigma$ has finite order $n > 1$, the coinvariant lattice $(H^2(X;\mathbf{Z})^{\sigma})^\perp$ is negative definite of rank at least $8$ and lies in $\operatorname{NS}(X)$ (Nikulin). For an involution it is $E_8(-2)$. So $\rho(X) \geq 8$, and $\rho(X) \geq 9$ if $X$ is projective, since an invariant ample class is orthogonal to it.
:::

::: {.front card-id="card-bdae5781e53151dc"}
What is the SES involving the symplectic automorphisms of $G\leq \mathop{\mathrm{Aut}}(X)$ a finite subgroup?
:::

::: {.back card-id="card-bdae5781e53151dc"}
$G\curvearrowright H^{2, 0}(X) = \CC\omega_X$ gives $\alpha: G\to \CC^{\times}$, $f\mapsto \alpha(f)$, where $f^* \omega_X = \alpha(f)\omega_X$.

Restrict to its image $\mu_m \subseteq {\CC^{\times}}$ to get a SES
$$G_0 \hookrightarrow G\twoheadrightarrow\mu_m, \qquad G_0 \coloneqq\left\{{f\in G\st f^*\omega_X = \omega_X}\right\}$$
and $G$ is nonsymplectic if $G\ne G_0$.
:::

::: {.front card-id="card-536dcb7d2a4f75ae"}
What are symplectic, non-symplectic, and purely non-symplectic automorphisms?
:::

::: {.back card-id="card-536dcb7d2a4f75ae"}
Let $\omega_X \in H^{2, 0}(X)$ be a nonzero 2-form. An automorphism $g$ of finite order acts by $g^*\omega_X = \alpha(g)\omega_X$ for a root of unity $\alpha(g)$.

Symplectic: $g^*\omega_X = \omega_X$

Non-symplectic: $g^*\omega_X = \alpha(g)\omega_X$ where $\alpha(g)\neq 1$.

Purely non-symplectic: $g^* \omega_X = \alpha(g)\omega_X$ where $\alpha(g) = \zeta_m$ is a *primitive* root of unity of order $m={\left\lvert {g} \right\rvert}$. Some authors call such $\sigma$ of order $n > 1$, with $\sigma^*(\omega_X) = \zeta_n \omega_X$ for a primitive root of unity $\zeta_n$, a non-symplectic automorphism of order $n$.
:::

::: {.front card-id="card-1d14a89c5a2ec472"}
Why are non-symplectic automorphisms important? (Proof sketch)
:::

::: {.back card-id="card-1d14a89c5a2ec472"}
If $X$ admits a finite order non-symplectic automorphism, $X$ is automatically projective.

Proof idea: use Kodaira embedding, find a rational Kahler class.

Use that $H^2(X;\QQ)\hookrightarrow H^2(X;{\mathbf{R}})$ is dense and $\mck$ is open in $H^{1, 1}\otimes{\mathbf{R}}$.

Find $c\in H^2(X; \QQ)$, decompose into $c_{2,0} + c_{1,1} + c_{0, 2}$ in $H^2(X;\CC)$ where $c_{1,1}$ is a real Kahler form, and kill $c_{2,0}, c_{0, 2}$ using the automorphism:

Average to define $h \coloneqq\sum_{i=0}^{{\left\lvert {g} \right\rvert} - 1}(g^*)^i c$ which is $g\dash$invariant.

Use that $g$ respects the Hodge decomposition, and $h_{1,1} = h\in H^2(X;\QQ)$ since $H^{2,0}, H^{0, 2}$ does not contain $g\dash$invariant elements.

By Kodaira embedding, some multiple of $h$ gives the embedding.
:::

::: {.front card-id="card-dff409395fc9e167"}
Give examples of automorphisms of K3s.
:::

::: {.back card-id="card-dff409395fc9e167"}
$\iota: F_4\to F_4$ where ${\left[ {x_0:x_1:x_2:x_3} \right]}\mapsto {\left[ {x_0:x_1:-x_2:-x_3} \right]}$, symplectic, $\mathrm{Fix}(\iota)$ is 8 points.

$\iota: F_4\to F_4$ where ${\left[ {x_0:x_1:x_2:x_3} \right]}\mapsto {\left[ {x_0:x_1:\zeta_4 x_2: \zeta_4 x_3} \right]}$.

Set $\omega\coloneqq({\partial}_0 f_4)^{-1}\,dx_2 \wedge \,dx_3$, then $\omega\mapsto -\omega$, so non-symplectic but not purely non-symplectic.
:::

::: {.front card-id="card-6ebe9be6d49b919e"}
Describe symplectic automorphisms locally.
:::

::: {.back card-id="card-6ebe9be6d49b919e"}
Can find local coordinates where $\sigma \in \operatorname{GL}_2(\CC)$ is of the form ${ \begin{bmatrix} {\lambda } & {0}  \\ {0} & {\overline{\lambda}} \end{bmatrix} }$ with $\lambda$ an $n$th root of unity where $n={\left\lvert {\sigma} \right\rvert}$.

Has only isolated fixed points, at most 8.

Nikulin counts ${\sharp} \mathrm{Fix}(\sigma)$ when ${\left\lvert {\sigma} \right\rvert}$ has small prime order.

Quotient has only type $A$ singularities.
:::

::: {.front card-id="card-a464f8a5173c47ca"}
Describe the Lefschetz number of a symplectic automorphism.
:::

::: {.back card-id="card-a464f8a5173c47ca"}
$L(\sigma) \coloneqq\sum (-1)^i \operatorname{Tr}(\sigma^* \curvearrowright H^i({\mathcal{O}}_S) )$.

$L(\sigma)\neq 0 \implies  \mathrm{Fix}(\sigma)\neq\emptyset$

$L(\sigma) = 2$ for a symplectic automorphism.
:::

::: {.front card-id="card-f12fcae19855ecbf"}
For a complex K3 surface $X$ and a finite group $G$ of symplectic automorphisms, which surface obtained from $X/G$ is again K3?
:::

::: {.back card-id="card-f12fcae19855ecbf"}
The minimal resolution of $X/G$ is K3. The quotient has only du Val singularities, and the invariant holomorphic two-form extends without zeros across their crepant resolution. The quotient itself can be singular.
:::

::: {.front card-id="card-67d5703c9df61496"}
Give an example of how having too many rational curves can be used in a proof.
:::

::: {.back card-id="card-67d5703c9df61496"}
If ${\left\lvert {\sigma} \right\rvert} = p = 11$ then ${\sharp} \mathrm{Fix}(\sigma) = 2$ yields 2 $A_{10}$ singularities, thus 20 independent $(-2)\dash$curves in $H^2(X; \ZZ)$ which generate a sublattice of signature $(0, 20)$.

This contradicts $\operatorname{sgn}H^2 = (3, 19)$.
:::

::: {.front card-id="card-d03dc5ca2d69bd48"}
Discuss $G\in \Fin\Grp\curvearrowright X$ not necessarily symplectically.
:::

::: {.back card-id="card-d03dc5ca2d69bd48"}
Kondo: ${\sharp}G \leq 3840$, proved using isometries of lattices.

Equality if $M_{20}\hookrightarrow G\twoheadrightarrow C_4$.
:::

::: {.front card-id="card-0c2e9f05f3de4898"}
Define the invariant lattice.
:::

::: {.back card-id="card-0c2e9f05f3de4898"}
$$H^2(X; \ZZ)^\sigma \coloneqq\left\{{x\in H^2(X;\ZZ) \st\sigma.x = x}\right\}$$
:::

::: {.front card-id="card-7c60a27942fbbd02"}
Give an example of a K3 with maximal Picard rank.
:::

::: {.back card-id="card-7c60a27942fbbd02"}
$X = \mathrm{Kummer}(E_3{ {}^{ \scriptscriptstyle\times^{2} }  })$ where $E_3$ is an elliptic curve with CM by $\zeta_3$.

Satisfies $\rho(X) = 20$.

Given by $X\hookrightarrow{\mathbf{P}}^3$ by $\sum x_i^4 - 12\prod x_i$.
:::

::: {.front card-id="card-4213492c4d415591"}
Discuss $(H^2(X; \ZZ)^\sigma)^\perp$.
:::

::: {.back card-id="card-4213492c4d415591"}
$$(H^2(X; \ZZ)^\sigma)^\perp \subseteq \NS(X) \implies H^2(X;\ZZ)^\sigma \subseteq T_X$$
Nikulin shows $(H^2(X;\ZZ)^\sigma)^\perp$ is a negative definite lattice.
:::

::: {.front card-id="card-764bc15a3a2a3fc6"}
Compute $\operatorname{rank}_\ZZ(H^2(X; \ZZ)^\sigma)^\perp$.
:::

::: {.back card-id="card-764bc15a3a2a3fc6"}
Start with $\operatorname{rank}_\ZZ(H^2(X;\ZZ))^\perp = m(p-1)$.
$$\begin{align*}{\sharp} \mathrm{Fix}(\sigma) &= \chi( \mathrm{Fix}(\sigma)) \\ &= \sum_{i=0}^4 (-1)^i \operatorname{Tr}(\sigma \curvearrowright H^i(X;\ZZ)) \\ &= 2 + \operatorname{Tr}(\sigma \curvearrowright H^2(X;\ZZ)^\sigma) + \operatorname{Tr}(\sigma \curvearrowright( H^2(X;\ZZ)^\sigma) ^\perp) \\ &= 2 + (22 - m(p-1)) - m \\&\implies m = {24\over p+1}\end{align*}$$
using that $\sum_{i=1}^{m-1}\zeta_m^i = -1$.
:::

::: {.front card-id="card-7f7b0e69e329f6b1"}
Give lower bounds on $\rho(X)$ when $\zeta_p\curvearrowright X$.
:::

::: {.back card-id="card-7f7b0e69e329f6b1"}
For a complex projective K3 surface with a symplectic automorphism of prime order $p$, the coinvariant lattice lies in $\operatorname{NS}(X)$, and averaging an ample class gives an additional invariant algebraic class. Hence $\rho(X)\geq1+\operatorname{rank}(H^2(X,\mathbb Z)^{\sigma})^\perp$: for $p=2,3,5,7$, the respective bounds are $9,13,17,19$.
:::

::: {.front card-id="card-ff30a885bc572a3d"}
Why are K3s with automorphisms special?
:::

::: {.back card-id="card-ff30a885bc572a3d"}
Gives a lower bound on $\rho(X)$.
:::

::: {.front card-id="card-f729e40766440d54"}
Discuss $\NS(X)$ when $X$ has an order 3 automorphism.
:::

::: {.back card-id="card-f729e40766440d54"}
Always get the Coxeter-Todd lattice, whose points give highest density sphere packing in dimension 12.
:::

::: {.front card-id="card-dec2dfa1d9efa061"}
What is an **algebraic** K3 surface?
:::

::: {.back card-id="card-dec2dfa1d9efa061"}
Smooth complete variety $X$ over a field $k$, $\dim X = 2$, where $\omega_{X/k}\cong {\mathcal{O}}_X$ and $H^1({\mathcal{O}}_X) = 0$.

Interpret $q(X) \coloneqq h^{0, 1}(X) = h^1({\mathcal{O}}_X)$ as the irregularity, so the last condition is $q(X) = 0$.
:::

::: {.front card-id="card-b314c9e25a945fe6"}
Discuss the cotangent sheaf of a K3.
:::

::: {.back card-id="card-b314c9e25a945fe6"}
Locally free of rank 2, $\Omega_X^2 = \operatorname{det}\Omega_X = \omega_X \cong {\mathcal{O}}_X$.

Carries an algebraic symplectic structure $(\Omega_X){ {}^{ \scriptscriptstyle\times^{2} }  } \to {\mathcal{O}}_X$ inducing an isomorphism ${\mathbf{T}}_X\cong \Omega_X {}^{ \vee }\coloneqq\mathop{\mathcal{H}\! \mathit{om}}(\Omega_X, {\mathcal{O}}_X) \cong \Omega_X$.
:::

::: {.front card-id="card-6f292d586b8e981e"}
When is a K3 surface projective?
:::

::: {.back card-id="card-6f292d586b8e981e"}
Always: any smooth complete surface is projective.
:::

::: {.front card-id="card-e3ada979046f3479"}
Why is a smooth quartic a K3?
:::

::: {.back card-id="card-e3ada979046f3479"}
If $X \subseteq {\mathbf{P}}^3$ then take the LES for ${\mathcal{O}}_{{\mathbf{P}}^3}(-4) \hookrightarrow{\mathcal{O}}_{{\mathbf{P}}^3} \twoheadrightarrow{\mathcal{O}}_X$ and use that $H^1({\mathcal{O}}_{{\mathbf{P}}^3}) = H^2({\mathcal{O}}_{{\mathbf{P}}^3}(-4)) = 0$ to conclude $H^1({\mathcal{O}}_X) = 0$.

The adjunction formula yields $\omega_X = \omega_{{\mathbf{P}}^3}\otimes{\mathcal{O}}(4)\mathrel{\Big|}_X \cong {\mathcal{O}}_X$.
:::

::: {.front card-id="card-788afed38cc8d30e"}
What is $\chi({\mathcal{O}}_X)$ for a K3?
:::

::: {.back card-id="card-788afed38cc8d30e"}
2: $h^0({\mathcal{O}}_X) = h^1({\mathcal{O}}_X) = 0$ by definition, and by Serre duality $h^2({\mathcal{O}}_X) = h^0(\omega_X) = 1$.
:::

::: {.front card-id="card-91364e66978ac689"}
What is $\pi_1^\text{ét}(X)$ for a K3?
:::

::: {.back card-id="card-91364e66978ac689"}
Trivial: if $Y\to X$ is an irreducible finite etale cover of degree $d$ then $Y$ is a smooth complete surface, $\omega_Y \cong{\mathcal{O}}_Y$, and $\chi({\mathcal{O}}_Y) = d\chi({\mathcal{O}}_X) =2d$ with $h^0({\mathcal{O}}_Y) = h^2({\mathcal{O}}_Y) = 1$.

Thus $2-h^1({\mathcal{O}}_Y) = 2d \implies d=1$.
:::

::: {.front card-id="card-04741fc87ffccbcc"}
What is the statement of RR for $L\in \operatorname{Pic}(X)$ for $X$ a K3? How does this change if $L$ is ample?
:::

::: {.back card-id="card-04741fc87ffccbcc"}
$\chi(L) = {1\over 2}L^2 + 2$.

If $L$ is ample then $H^1(L) = 0$ so the LHS is $h^0(L)$.
:::

::: {.front card-id="card-8416a0db82d96015"}
What is $c_2(X)$ for a K3?
:::

::: {.back card-id="card-8416a0db82d96015"}
24 by the Noether formula.
:::


::: {.front card-id="card-758927d12fcaa059"}
Discuss $h^0({\mathbf{T}}_X)$ for $X$ a K3.
:::

::: {.back card-id="card-758927d12fcaa059"}
$h^0({\mathbf{T}}_X) = h^0(\Omega_X)= 0$ using the isomorphism ${\mathbf{T}}_X\cong \Omega_X$. So no global vector fields.
:::

::: {.front card-id="card-cadd5037b23ac4b9"}
What is a **complex** K3 surface?
:::

::: {.back card-id="card-cadd5037b23ac4b9"}
A compact connected complex manifold, $\dim X = 2$, with $\Omega^2_X \cong {\mathcal{O}}_X$ and $h^1({\mathcal{O}}_X) = 0$.

If $X$ is an algebraic K3 then $X^\an$ is a (projective) complex K3.
:::

::: {.front card-id="card-8d81d919296f7a7a"}
Why is $X^\an$ projective when $X$ is an algebraic K3?
:::

::: {.back card-id="card-8d81d919296f7a7a"}
GAGA: the ideal sheaf $I$ of $X\subseteq {\mathbf{P}}^n$ is coherent analytic and thus isomorphic to an algebraic ideal sheaf.
:::

::: {.front card-id="card-ed2a3b29ee9828a1"}
Are all complex K3s projective?
:::

::: {.back card-id="card-ed2a3b29ee9828a1"}
No: most complex tori $X=\CC^2/\Gamma$ are not.
:::

::: {.front card-id="card-f863478d0d916b41"}
Discuss $H^*_\sing(X)$ for a K3.
:::

::: {.back card-id="card-f863478d0d916b41"}
Take the LES $H^1(X;\ZZ) \to H^1(X;{\mathcal{O}})\to H^1(X;{\mathcal{O}}^{\times})$ to show $H^1(X;\ZZ) = H^3(X;\ZZ) = 0$ mod torsion and $H^0(X;\ZZ) = H^4(X;\ZZ) = \ZZ$. The only other nontrivial group is $H^2(X; \ZZ)$.
:::

::: {.front card-id="card-c9d0de8eb14f950a"}
Discuss $H^2(X; \ZZ)$
:::

::: {.back card-id="card-c9d0de8eb14f950a"}
Torsionfree, since $0\to \operatorname{Pic}(X) \to H^2(X;\ZZ) \to H^2(X; {\mathcal{O}})$ using $\operatorname{Pic}(X)\cong H^1(X; {\mathcal{O}}^{\times})$; since $H^2(X;{\mathcal{O}})\cong \CC$ and $\operatorname{Pic}(X)$ are torsionfree, so is $H^2$. The intersection form on $\operatorname{Pic}(X)$ corresponds to the intersection form on $H^2$ under this embedding.

$\operatorname{rank}_\ZZ H^2 = 22$ since $e(X) = c_2(X) = 24$ and $b_2(X) = 22$, and this defines a unimodular lattice ${\mathbf{E}}_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  } \oplus U{ {}^{ \scriptscriptstyle\oplus^{3} }  }$.
:::

::: {.front card-id="card-e9df1180e0586b98"}
How is $\rho(X)\leq 22$ proved for K3s over positive characteristic fields?
:::

::: {.back card-id="card-e9df1180e0586b98"}
Take the LES in $H^*_\text{ét}$ for the Kummer sequence $\mu_n\hookrightarrow{\mathbf{G}}_m\twoheadrightarrow{\mathbf{G}}_m$ for $n$ prime to $p$, use $\operatorname{Pic}(X) \cong H^1(X;{\mathbf{G}}_m)$ to show $H^1_\text{ét}(X; \mu_n) = k^{\times}/(k^{\times})^n$.

Use $k$ separably closed and duality to get $H^1_\text{ét}(X; { \ZZ_{\widehat{\ell}} }) = H^3(X;{ \ZZ_{\widehat{\ell}} }) = 0$.

Use $c_2(X) = 24$ to conclude $\operatorname{rank}_\ZZ H^2_\text{ét}(X; { \ZZ_{\widehat{\ell}} }) = 22$.
:::

::: {.front card-id="card-8a3313b45abc3005"}
What is a hyperelliptic curve in the context of K3s?
:::

::: {.back card-id="card-8a3313b45abc3005"}
$C$ with a degree 2 morphism $C\to {\mathbf{P}}^1$.

Usually $g(C) \geq 2$, $\omega_C$ is bpf, and the canonical embedding $\phi_{\omega_C}$ is non-constant.
:::

::: {.front card-id="card-696f61d1ecfeb96a"}
Give a lower bound for $C^2$ for an integral curve on a K3.
:::

::: {.back card-id="card-696f61d1ecfeb96a"}
$C^2 \geq -2$, using
$$2 p_a(C)-2=\left(C . \omega_X \otimes \mathcal{O}(C)\right)\implies 2 p_a(C)-2=(C)^2$$
and $p_a(C) \geq 0$.
:::

::: {.front card-id="card-d659e54d9492db61"}
Discuss curves on a K3.
:::

::: {.back card-id="card-d659e54d9492db61"}
By adjunction, $C^2\geq -2$. Automatically smooth, since $g(C) \leq p_a(G)$ with equality iff $C$ is smooth, and here $p_a(C) = p_g(C) = 0$. Any $(-2)\dash$curve is integral.
:::

::: {.front card-id="card-ee039062cee28f38"}
When is a line bundle on a K3 ample?
:::

::: {.back card-id="card-ee039062cee28f38"}
$L$ is ample iff $L\in \mcc_X \subset \NS(X)_{\mathbf{R}}$ (the positive cone) and $(L.C) > 0$ for every smooth rational curve $C\cong {\mathbf{P}}^1 \subseteq X$.
:::

::: {.front card-id="card-38e09a8919b928e1"}
Discuss $L^2$ and $h^0(L)$ for $L = {\mathcal{O}}_X(C)$, $C$ a curve on a K3 $X$.
:::

::: {.back card-id="card-38e09a8919b928e1"}
Let $L= {\mathcal{O}}_X(C)$ for $C\subseteq X$ a smooth irreducible curve of genus $g$ on a K3 $X$, then
$$L^2 = 2g-2,\qquad h^0(L) = g+1$$
Use adjunction to prove the first, and RR + Serre duality + $H^0({ \left.{{L}} \right|_{{C}} }) \cong H^0(\omega_C)$ and the SES $H^0(X; {\mathcal{O}}_X) \hookrightarrow H^0(X; L)\twoheadrightarrow H^0(C; { \left.{{L}} \right|_{{C}} })$.
:::

::: {.front card-id="card-f155d869dc3cff26"}
Discuss projective embeddings of curves in K3s.
:::

::: {.back card-id="card-f155d869dc3cff26"}
For $C\subseteq X$ smooth irreducible with $g(C) \geq 1$, $L\coloneqq{\mathcal{O}}(C)$ is bpf and $\phi_L: X\to {\mathbf{P}}^g$ restricts to the canonical embedding $C\to {\mathbf{P}}^{g-1}$.

For $g=2$, $C$ is hyperelliptic so $C\to {\mathbf{P}}^1$ is degree 2. Since $L^2 = 2$ and $L = \phi_L^* {\mathcal{O}}(1)$, $\phi_L$ is degree 2, so $X$ is a double cover of ${\mathbf{P}}^2$ over a degree 6 curve.
:::

::: {.front card-id="card-a289e10e50b64ad3"}
Discuss the analog of Noether's theorem on projective normality of non-hyperelliptic curves.
:::

::: {.back card-id="card-a289e10e50b64ad3"}
For $C\subseteq X$ irreducible smooth non-hyperelliptic with $g(C) > 2$ on a K3 $X$, $L\coloneqq{\mathcal{O}}(C)$ is projectively normal, so $\phi_L^*$ defines surjections $H^0({\mathbf{P}}^g; {\mathcal{O}}(k)) \twoheadrightarrow H^0(X; L^k)$ for all $k$.
:::

::: {.front card-id="card-6c6d0f89580f2dfc"}
Discuss projective embeddings of K3s in arbitrary characteristic.
:::

::: {.back card-id="card-6c6d0f89580f2dfc"}
If $C\subseteq X$ is smooth irreducible and $L\coloneqq{\mathcal{O}}(C)$, then for $k\geq 2, g>2$ or $k\geq 3, g=2$ the induced embedding $\phi_{L^k}:X\to {\mathbf{P}}^n, n= k^2(g-1)+1$ is birational onto its image.
:::

::: {.front card-id="card-504dac3b1ca18677" cite="[@Huy16, Chapter 2, Remark 2.8; @Mum70, Theorem 3]"}
Discuss $\operatorname{Pic}(X)^\vamp$ for $X$ a K3.
:::

::: {.back card-id="card-504dac3b1ca18677"}
If $L$ is ample and bpf, the $L^k$ is very ample for $k\geq 3$.

Consequence of a general result of Mumford.
:::

::: {.front card-id="card-b2f808dcef295d55"}
Discuss big and nef line bundles $L$ on a K3.
:::

::: {.back card-id="card-b2f808dcef295d55"}
$H^1(L) = 0$ by the Kodaira-Ramanujam vanishing theorem.

If $C$ is an irreducible curve with $C^2 > 0$, then ${\mathcal{O}}(C)$ is big and nef.

Decompose $L = M + F$ into its mobile and fixed parts. If $M$ is big, then $L$ is bpf and $F$ is trivial.

If $L$ is not bpf then $L = {\mathcal{O}}(mE + C)$ with $E$ smooth elliptic, $C\cong{\mathbf{P}}^1$, $E.C = 1$, and $m\geq 2$.
:::

::: {.front card-id="card-7eed0c440c3acc28"}
What is Ramanujam's lemma?
:::

::: {.back card-id="card-7eed0c440c3acc28"}
If $C$ is 1-connected and $H^1({\mathcal{O}}_X) = 0$, then $H^1({\mathcal{O}}_X(-C)) =0$.

In characteristic zero, can drop $H^1({\mathcal{O}}_X) = 0$ assumption.
:::

::: {.front card-id="card-b87e35a4eb78f2b0"}
Let $L\in \operatorname{Pic}(X)$ be big and nef. Show that ${\left\lvert {L} \right\rvert}$ is bpf.
:::

::: {.back card-id="card-b87e35a4eb78f2b0"}
Decompose $L = M + F$.

Mobile $\implies$ effective $\implies$ nef, so $M^2 \geq 0$.

If $M^2 > 0$, then $M$ is big and nef so $L$ has at most isolated base points.

Check $H^1(X; M) = 0 = H^1(X; L)$ so $\chi(M) = h^0(M) = h^0(L) = \chi(L)$.

By RR, $M^2 = L^2$, so $2(M.F) + F^2 = 0$

$L$ nef $\implies (M.F) + F^2 = L.F\geq 0 \implies M.F = F^2 = 0$

By RR on $F\neq 0$, reach a contradiction $1 = h^0(F) \geq \chi(F)$, so $F=0$.|
:::

::: {.front card-id="card-e0bfd516a3578177"}
Discuss when $L\in \operatorname{Pic}(X)$ for $X$ a K3 is bpf.
:::

::: {.back card-id="card-e0bfd516a3578177"}
Sufficient condition: $L^2 > 0$ and ${\left\lvert {L} \right\rvert}$ contains an irreducible curve.
:::

::: {.front card-id="card-53e67332f7d85a65"}
Discuss irreducible curves on a K3 in $\operatorname{ch}k \neq 2$.
:::

::: {.back card-id="card-53e67332f7d85a65"}
Always have $C^2 > 0$, ${\left\lvert {{\mathcal{O}}_X(C)} \right\rvert}$ is bpf, its generic member $C'$ is smooth.

Either $C'$ is hyperelliptic (so $\deg \phi = 2$) or not (then $\deg \phi = 1$ is birational)
:::

::: {.front card-id="card-7de6f6849a5d455d"}
Discuss curves with $C^2 = 0$ on a K3.
:::

::: {.back card-id="card-7de6f6849a5d455d"}
If $L \in \operatorname{Pic}(X)^\mathrm{nef}$ is nontrivial and $L^2=0$ then $L$ is bpf.

Away from characteristics 2 and 3, $\exists E$ a smooth irreducible elliptic curve with $mE \in {\left\lvert {L} \right\rvert}$ for some $m$.

If $L.C \geq 0$ for all $C\cong {\mathbf{P}}^1$ then $L\cong {\mathcal{O}}(m E)$ for some $m$.
:::

::: {.front card-id="card-4490be94e7ce9bad"}
Does the Fermat quartic contain any lines?
:::

::: {.back card-id="card-4490be94e7ce9bad"}
Yes: ${\left[ {x_0, \zeta_8 x_0, x_2, \zeta_8 x_2} \right]}$.
:::

::: {.front card-id="card-324108ea57273d0b"}
When does a complex projective K3 surface admit a genus-one fibration? How does an isotropic divisor class produce the fibration, and what extra condition gives a section?
:::

::: {.back card-id="card-324108ea57273d0b"}
The criterion is a nonzero integral class $L\in\operatorname{NS}(X)$ with $L^2=0$. Choose its effective sign, then use reflections $L\mapsto L+(L\cdot C)C$ in $(-2)$-curves with $L\cdot C<0$ to obtain a nef class. Its primitive generator $F$ has a base-point-free pencil $|F|$ defining $X\to\mathbb P^1$ with smooth genus-one general fiber. A section exists exactly when there is an integral curve $D$ with $F\cdot D=1$. A genus-one fibration need not have a section.
:::

::: {.front card-id="card-a772d749c355f1fe"}
Discuss base points of complete linear systems on a K3.
:::

::: {.back card-id="card-a772d749c355f1fe"}
$\operatorname{Bs}{\left\lvert {L} \right\rvert} = F$, i.e. ${\left\lvert {L} \right\rvert}$ has no base points outside of its fixed part.
:::

::: {.front card-id="card-7a25c38d96ac8312"}
What is a polarized K3 of degree $2d$?
:::

::: {.back card-id="card-7a25c38d96ac8312"}
A pair $(X, L)$ with $X$ a projective K3 and $L\in \operatorname{Pic}(X)^\amp = \NS(X)^\amp$ primitive with $L^2 = 2d$.
:::

::: {.front card-id="card-045aecc61162ab8a"}
What is the genus of a polarized K3?
:::

::: {.back card-id="card-045aecc61162ab8a"}
Write $2d = 2g-2$, then $g = g(C)$ for any $C\in {\left\lvert {L} \right\rvert}$, we say $(X, L)$ is a polarized K3 of genus $g$.
:::

::: {.front card-id="card-63450e6157a4c6bd"}
Do there exist K3s of arbitrary degree over $k=\kbar$?
:::

::: {.back card-id="card-63450e6157a4c6bd"}
Yes, for $g\geq 3$ over $k=\kbar$ there exists K3s of degree $2g-2$ in ${\mathbf{P}}^g$.

Idea: for $g=3k$, take a generic quartic $X$ in ${\mathbf{P}}^3$ containing a line $\ell$.

Let $H$ be the hyperplane section and consider ${\left\lvert {H-\ell} \right\rvert}$

This defines an elliptic pencil ${\left\lvert {E} \right\rvert}$.

Consider $L_k \coloneqq H + (k-1)E \in \operatorname{Pic}(X)^\vamp$, for generic $X$ it is primitive.

Yields a polarized K3 of degree $L_k^2 = 6k-2$.
:::

::: {.front card-id="card-920ffb5ecda68daf"}
Do there exist K3s of arbitrary degree over $k\neq \kbar$?
:::

::: {.back card-id="card-920ffb5ecda68daf"}
No: for $k={ \mathbf{F} }_q$, the degree of a polarized K3 defined over $k$ is bounded.

Related to questions about rational points on the moduli of K3s.
:::

::: {.front card-id="card-7f793df47dd67483"}
Discuss $\operatorname{Pic}(X)^\amp\subseteq \operatorname{Pic}(X)$.
:::

::: {.back card-id="card-7f793df47dd67483"}
An open subspace, i.e. ampleness is an open property.
:::

::: {.front card-id="card-76f5190528e2c617"}
What does the Kummer construction do?
:::

::: {.back card-id="card-76f5190528e2c617"}
The Kummer construction allows one to pass from Hodge structures of weight one of a two-dimensional torus to the Hodge structure of weight two of its associated Kummer surface.
:::

::: {.front card-id="card-e7187787287eaf85"}
What is a Hodge structure of K3 type?
:::

::: {.back card-id="card-e7187787287eaf85"}
Weight 2 with
$$\operatorname{dim}_\CC\left(V^{2,0}\right)=1 \text { and } V^{p, q}=0 \text { for }|p-q|>2$$
:::

::: {.front card-id="card-2532873a2539c45d"}
Is the Hodge structure on a K3 polarizable?
:::

::: {.back card-id="card-2532873a2539c45d"}
If algebraic, always. If not, there are counterexamples.
:::

::: {.front card-id="card-a75c71cf2709c1cd" cite="[@GPSZ22, §6.2]"}
What is the transcendental part of a Hodge structure of K3 type?
:::

::: {.back card-id="card-a75c71cf2709c1cd"}
For an integral or rational Hodge structure of K3 type $V$ one defines the transcendental lattice or transcendental part $T$ as the minimal primitive sub-Hodge structure
$$\begin{align}T \subset V \text { with } V^{2,0}=T^{2,0} \subset T_\CC\end{align}$$
The primitivity, i.e. the condition that $V / T$ is torsion free, has to be added for integral Hodge structures, as otherwise minimality cannot be achieved.

More generally, for a polarizable rational Hodge structure $A$ of weight two with $F^3A=0$, let $T[A]$ be its smallest rational sub-Hodge structure containing $F^2A$. This also applies when $h^{2,0}>1$ and satisfies
$$T[A\oplus B]=T[A]\oplus T[B].$$
For a projective surface, it is the orthogonal complement of the rational $(1,1)$-classes under a polarization. In an integral lattice take the primitive intersection with this rational subspace. This is the version used to split the transcendental parts of components in a finite-monodromy surface limit.
:::

::: {.front card-id="card-14234c9dd775e812"}
What is the lattice for $H^1(\CC^2/\Gamma; \ZZ)$?
:::

::: {.back card-id="card-14234c9dd775e812"}
$U{ {}^{ \scriptscriptstyle\oplus^{3} }  }$; always has a Hodge structure of K3 type.
:::

::: {.front card-id="card-7df71f32322ce16a"}
What is the Kummer lattice?
:::

::: {.back card-id="card-7df71f32322ce16a"}
The unique even negative definite rank 16 lattice of discriminant $2^{16}$.
:::

::: {.front card-id="card-5113f1d6f8452d78"}
Describe the Hodge isometries of $T(X)$ for a K3.
:::

::: {.back card-id="card-5113f1d6f8452d78"}
Finite cyclic; any $\alpha: T(X) { \, \xrightarrow{\sim}\, }T(X)$ satisfies $\alpha^n=\operatorname{id}$ for some $n$.

If $\rho(X)$ is odd, then $T(X) = \left\{{\pm \operatorname{id}}\right\} \cong C_2$.
:::

::: {.front card-id="card-e809a4d4414318c1"}
Discuss $K\coloneqq K(T) \coloneqq{ \operatorname{End} }_{\mathbf{Q}\kern-0.5pt\operatorname{HS}}(T)$ for a K3.
:::

::: {.back card-id="card-e809a4d4414318c1"}
Always a number field. If $T\in \mathbf{Q}\kern-0.5pt\operatorname{HS}$ is polarized irreducible of K3 type, the $K$ is either totally real or a CM field.

If CM, $K = \QQ(\eta)$ for some Hodge isometry $\eta$.

Any totally real field is realized as $K(T)$ for $T\in \mathbf{Q}\kern-0.5pt\operatorname{HS}$ polarized of K3 type.
:::

::: {.front card-id="card-3b4ed3689f8e94d9"}
What is $\kappa(X)$ for $X$ a K3?
:::

::: {.back card-id="card-3b4ed3689f8e94d9"}
$\kappa(X) = 0$, one of four such classes of minimal surfaces.
:::

::: {.front card-id="card-277ec0b2ed591534"}
Where do K3s fit into the classification of surfaces?
:::

::: {.back card-id="card-277ec0b2ed591534"}
Positively curved: del Pezzo

Flat: K3s (generally CYs and hyperkahlers)

Negatively curved: general type.
:::

::: {.front card-id="card-8ace99975d2c209d" tags="formula"}
For a complex K3 surface $S$, compute $q,p_g,\chi(\mathcal O_S),K_S^2,c_2(S),b_2,h^{1,1},b_2^+,b_2^-$.
:::

::: {.back card-id="card-8ace99975d2c209d"}
$$\begin{aligned}q&=0,&p_g&=1,&\chi(\mathcal O_S)&=2,\\K_S^2&=0,&c_2(S)&=24,&b_2&=22,\\h^{1,1}&=20,&b_2^+&=3,&b_2^-&=19.\end{aligned}$$
:::

::: {.front card-id="card-b4c7696af026d814"}
Construct a K3 surface as a double cover of $\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}$. Determine the branch bidegree and the genus of the general fiber over either factor.
:::

::: {.back card-id="card-b4c7696af026d814"}
Take a smooth branch divisor $B\in|\mathcal O(4,4)|$, and form the double cover with $L=\mathcal O(2,2)$. Then
$$\pi_*\mathcal O_X=\mathcal O\oplus\mathcal O(-2,-2),\qquad
\omega_X=\pi^*(\mathcal O(-2,-2)\otimes L)\cong\mathcal O_X.$$
Künneth gives $H^1(\mathcal O_X)=0$, so the smooth cover is K3. Over a general point of either factor, the fiber is a double cover of $\mathbb P^1$ branched at four points, hence has genus one. A section requires an additional condition; this construction alone gives a genus-one fibration.
:::

::: {.front card-id="card-4e90b1d8184c7c0a"}
Why is lattice theory important in the study of K3s?
:::

::: {.back card-id="card-4e90b1d8184c7c0a"}
For $X$ a smooth K3, $H^2(X; \ZZ) \cong L_{{\mathsf{K}}3} \coloneqq H{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8{ {}^{ \scriptscriptstyle\oplus^{2} }  }$.
:::

::: {.front card-id="card-cd0d75cdabdfde40"}
Discuss $H^{2, 0}(X)$ for $X$ a K3.
:::

::: {.back card-id="card-cd0d75cdabdfde40"}
$H^{2, 0}(X) = \CC\omega_X$ for some nowhere vanishing holomorphic 2-form $\omega_X$
:::

::: {.front card-id="card-f366077ef99eafd5"}
What is the Kahler cone $\mck_X$?
:::

::: {.back card-id="card-f366077ef99eafd5"}
$\mck_X \subseteq H^{1, 1}(X; {\mathbf{R}})$ the set of Kahler forms, forms an open convex cone.
:::



::: {.front card-id="application-torelli-sign-isometry" tags="application"}
For a complex K3 surface $X$, the map $-\operatorname{id}$ is an integral Hodge isometry of $H^2(X,\mathbb Z)$. Must it be induced by an automorphism? Which part of global Torelli decides?
:::

::: {.back card-id="application-torelli-sign-isometry"}
No. It sends every Kähler class to its negative, so it does not preserve the Kähler cone. Global Torelli realizes a given Hodge isometry by an automorphism precisely when it preserves that cone. Existence of a Hodge isometry and realization of that particular isometry are different assertions.
:::

::: {.front card-id="application-torelli-polarization" tags="application"}
Let $(X,L)$ and $(Y,M)$ be polarized complex K3 surfaces. An integral Hodge isometry $\varphi:H^2(X,\mathbb Z)\to H^2(Y,\mathbb Z)$ sends $c_1(L)$ to $c_1(M)$. Does it come from an isomorphism, and in which direction? Explain why the ample classes matter.
:::

::: {.back card-id="application-torelli-polarization"}
Yes: polarized Torelli gives a unique isomorphism $f:Y\to X$ with $f^*=\varphi$. Sending an ample class to an ample class selects the corresponding Kähler chambers, so the cone condition is satisfied. The direction reverses because cohomology acts by pullback.
:::

::: {.front card-id="card-7dde87ec9eecba8a" tags="definition"}
What is the definition of Bogomolov–mumford theorem?
:::

::: {.back card-id="card-7dde87ec9eecba8a"}
Let $X$ be a projective K3 surface over an algebraically closed field of characteristic zero. Then every nonzero effective divisor class on $X$ is a nonnegative rational linear combination of classes of rational curves; equivalently, the effective cone of $X$ is generated by rational curves.
:::

::: {.front card-id="card-ac29a60ed7a2e5d5" tags="definition"}
What is the definition of Coinvariant lattice?
:::

::: {.back card-id="card-ac29a60ed7a2e5d5"}
For a finite-order automorphism $\sigma$ of a lattice $L$, the lattice $(L^\sigma)^\perp\subset L$. For a symplectic automorphism of a K3 surface it is negative definite and lies in $\operatorname{NS}(X)$.
:::

::: {.front card-id="card-0864fe38f27357b8" tags="definition"}
What is the definition of Compact complex surface?
:::

::: {.back card-id="card-0864fe38f27357b8"}
A connected compact complex manifold of complex dimension $2$. Examples are $\mathbb P^2$, complex tori $\mathbb C^2/\Lambda$, K3 surfaces, and Enriques surfaces.
:::

::: {.front card-id="card-7c69b521f27aa9a2" tags="definition"}
What is the definition of Effective hodge isometry?
:::

::: {.back card-id="card-7c69b521f27aa9a2"}
A Hodge isometry $g:H^2(X;\mathbb Z)\to H^2(X';\mathbb Z)$ that maps the Kähler cone of $X$ onto the Kähler cone of $X'$. By global Torelli, these are exactly the isometries induced by isomorphisms $X'\to X$.
:::

::: {.front card-id="card-f9d2f48577eecebd" tags="definition"}
What is the definition of Holomorphic 2-form?
:::

::: {.back card-id="card-f9d2f48577eecebd"}
A global section of $\Omega_X^2$. On a K3 surface a holomorphic $2$-form is a nowhere-vanishing form $\omega_X$ generating $H^{2,0}(X)=\mathbb C\omega_X$.
:::

::: {.front card-id="card-e693aac43b035a27" tags="definition"}
What is the definition of Hyperbolic plane?
:::

::: {.back card-id="card-e693aac43b035a27"}
The rank-two even unimodular lattice $U$ with Gram matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$. It is the lattice generated by a fibre and a section on $\mathbb P^1\times\mathbb P^1$.
:::

::: {.front card-id="card-412e012d939e6cff" tags="definition"}
What is the definition of Intersection pairing?
:::

::: {.back card-id="card-412e012d939e6cff"}
The symmetric bilinear form $H^2(X;\mathbb Z)\times H^2(X;\mathbb Z)\to\mathbb Z$, $(\alpha,\beta)\mapsto\int_X\alpha\cup\beta$. On a surface it restricts to the intersection form on divisor classes.
:::

::: {.front card-id="card-60e5ba4948c41e2f" tags="definition"}
What is the definition of Irreducible hodge structure?
:::

::: {.back card-id="card-60e5ba4948c41e2f"}
A Hodge structure $V$ with no nonzero proper sub-Hodge structure. Equivalently, its Mumford–Tate group acts irreducibly on $V$. The transcendental lattice of a projective K3 is polarizable and irreducible.
:::

::: {.front card-id="card-76926cb7ee6be178" tags="definition"}
What is the definition of Kummer sequence?
:::

::: {.back card-id="card-76926cb7ee6be178"}
For $n$ invertible on a scheme $X$, the exact sequence of étale sheaves $0\to\mu_n\to\mathbb G_m\xrightarrow{n}\mathbb G_m\to0$. Its long exact sequence relates $\operatorname{Pic}(X)$ to $H^2_{\text{ét}}(X;\mu_n)$.
:::

::: {.front card-id="card-957550ab4d6f6c37" tags="definition"}
What is the definition of Noether formula?
:::

::: {.back card-id="card-957550ab4d6f6c37"}
For a smooth projective complex surface $S$, $12\chi(\mathcal O_S)=K_S^2+c_2(S)=K_S^2+e(S)$.
:::

::: {.front card-id="card-5b1a9c18abed8bef" tags="definition"}
What is the definition of Poincaré duality?
:::

::: {.back card-id="card-5b1a9c18abed8bef"}
The nondegenerate pairing $H^k(X;\mathbb Z)\times H^{n-k}(X;\mathbb Z)\to\mathbb Z$, $(\alpha,\beta)\mapsto\langle\alpha\cup\beta,[X]\rangle$, for a compact oriented $n$-manifold. It makes $H^2$ of a K3 surface a unimodular lattice.
:::

::: {.front card-id="card-5e489e6c90b31567" tags="definition"}
What is the definition of Pontryagin class?
:::

::: {.back card-id="card-5e489e6c90b31567"}
For a real vector bundle $E$, the class $p_1(E)=c_1(E\otimes\mathbb C)^2-2c_2(E\otimes\mathbb C)\in H^4(X;\mathbb Z)$. For a compact oriented $4$-manifold, $\operatorname{sgn}(X)=\frac13p_1(TX)$.
:::

::: {.front card-id="card-6a43788773bf5191" tags="definition"}
What is the definition of Positive cone?
:::

::: {.back card-id="card-6a43788773bf5191"}
For a real vector space with a quadratic form of signature $(1,n)$, the cone $\{x:x^2>0\}$. In surface theory the positive cone is the component of this cone in $N^1(X)_{\mathbb R}$ containing the ample classes.
:::

::: {.front card-id="card-b9ed3a6a087c1634" tags="definition"}
What is the definition of Separably closed field?
:::

::: {.back card-id="card-b9ed3a6a087c1634"}
A field $k$ with no nontrivial finite separable extension; equivalently, every irreducible polynomial over $k$ has at most one distinct root in an algebraic closure. This is weaker than algebraic closure: over $\mathbb F_p(t)$, the polynomial $x^p-t$ is irreducible and inseparable, so $\mathbb F_p(t)$ is not separably closed.
:::

::: {.front card-id="card-3a139a4f8e33c4bc" tags="definition"}
What is the definition of Sextic double plane?
:::

::: {.back card-id="card-3a139a4f8e33c4bc"}
A double cover $X\to\mathbb P^2$ branched along a smooth plane sextic. It is a K3 surface, with equation $t^2=f_6(x_0,x_1,x_2)$ in $\mathbb P(3,1,1,1)$.
:::

::: {.front card-id="card-2599e5decd6f5d5a" tags="definition"}
What is the definition of Symplectic form?
:::

::: {.back card-id="card-2599e5decd6f5d5a"}
A closed nondegenerate holomorphic $2$-form. On a K3 surface a symplectic form is a nowhere-vanishing section of $\Omega_X^2\cong\mathcal O_X$, unique up to scalar.
:::

::: {.front card-id="card-d63e2330de347174" tags="definition"}
What is the definition of Thom–hirzebruch index theorem?
:::

::: {.back card-id="card-d63e2330de347174"}
For a closed oriented smooth four-manifold,
$$\sigma(X)=b_2^+-b_2^-=\frac13\langle p_1(TX),[X]\rangle.$$
If $TX$ has an almost-complex structure inducing the orientation, $p_1=c_1^2-2c_2$, hence $\sigma=\frac13\langle c_1^2-2c_2,[X]\rangle$.

For a complex K3, $c_1=0$ and $\int_Xc_2=24$, so $\sigma=-16$. Together with $b_2=22$, this gives $(b_2^+,b_2^-)=(3,19)$: the inertia pair, rather than the scalar signature.
:::

::: {.front card-id="card-71e5b09d37500058" tags="definition"}
What is the definition of Totally real field?
:::

::: {.back card-id="card-71e5b09d37500058"}
A number field all of whose embeddings into $\mathbb C$ have image in $\mathbb R$. The field $K(T)=\operatorname{End}_{\mathrm{HS}}(T)$ of a polarized irreducible K3-type Hodge structure is either totally real or CM.
:::
