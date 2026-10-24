---
title: "Algebraic Geometry::Hodge Theory"
---

::: {.front card-id="card-e0262b52c2d6df11"}
What is the Albanese variety of $Z$? Its corresponding embedding?
:::

::: {.back card-id="card-e0262b52c2d6df11"}
$\operatorname{Alb}(Z)=H^0\left(Z, \Omega_Z^1\right)^* / H_1(Z, \mathbf{Z})$

$\Phi: Z\to \mathrm{Alb}(Z)$ sends a base point $p\in Z$ to the origin and $\Phi(z)(\eta) \coloneqq\int_p^z \eta$.
:::

::: {.front card-id="card-1473584e4048a634"}
What is the Lefschetz decomposition?
:::

::: {.back card-id="card-1473584e4048a634"}
$$H^k(X; \CC) = \bigoplus_{2r\leq k}L^r H^{k-2r}_\prim(X)$$
:::

::: {.front card-id="card-6c5784cabdbc59b9"}
Draw a picture of 3-dimensional vanishing cycles.
:::

::: {.back card-id="card-6c5784cabdbc59b9"}
For the smoothing $X_t=\{z_1^2+z_2^2+z_3^2+z_4^2=t\}\subset\mathbb C^4$ with $t>0$, the real locus $\{(x_1,\ldots,x_4)\in\mathbb R^4:\sum x_i^2=t\}$ is a three-sphere $S^3\subset X_t$. It shrinks to the node as $t\to0$; this is the vanishing cycle.
:::

::: {.front card-id="card-49cc848db9c8f1bf"}
What is the hard Lefschetz theorem?
:::

::: {.back card-id="card-49cc848db9c8f1bf"}
For $X$ compact Kahler, for $k\leq n\coloneqq\dim X$,

$L^{n-k}: H^k(X; {\mathbf{R}}) { \, \xrightarrow{\sim}\, }H^{2n-k}(X; {\mathbf{R}})$

$H^k(X; {\mathbf{R}}) = \bigoplus_{i\geq 0} L^i H^{k-2i}(X; {\mathbf{R}})_\prim$

$H^k(X; {\mathbf{R}})_\prim\otimes_{\mathbf{R}}\CC=\bigoplus_{p+q=k} H^{p, q}(X)_\prim$.
:::

::: {.front card-id="card-e035601038997a30"}
What is the Hodge index theorem?
:::

::: {.back card-id="card-e035601038997a30"}
For $X$ a compact Kahler surface, the intersection form satisfies
$$\operatorname{sgn}H^2(X; \ZZ) = (2h^{2, 0} + 1,\, h^{1,1} -1), \qquad \operatorname{sgn}H^{1,1}(X) = (1,\, h^{1,1}-1)$$
Equivalently, if $L\in \NS(X)^\amp$ (or even $L^2 \gt 0$) then the intersection form is negative definite on $L^\perp$.
:::

::: {.front card-id="card-32d30066fccb982b"}
What is nonabelian Hodge theory?
:::

::: {.back card-id="card-32d30066fccb982b"}
$\mcm_B$ is the moduli of irreducible reps of $\pi_1(X)$, $\mcm_{\mathrm{Dol}}$ of stable Higgs bundles, and $\mcm_{\mathrm{dR}}$ of stable flat connections:
:::

::: {.front card-id="card-af845a3fa43df735"}
What is a rigid representation?
:::

::: {.back card-id="card-af845a3fa43df735"}
Only trivial deformations, isolated point in character variety.

Conjecture: rigid representations are "motivic", of geometric origin.

E.g. irreducible rigid flat connections are subquotients of the Gauss-Manin connection on a family of smooth projective varieties over an open dense subvariety of $X$.

The underlying local system is a summand of ${\mathbf{R}}^if_* \underline{\CC}$ for $f:Y\to U$ a smooth projective morphism to a dense subvariety.
:::

::: {.front card-id="card-8de617f146e6c753"}
What is a QHS?
:::

::: {.back card-id="card-8de617f146e6c753"}
For $V\in  {}_{\QQ}\Mod^\fd$, a decomposition $V = \bigoplus_{p, q} V^{p, q}$ with $\overline{V^{p, q}} = V^{q, p}$ where $V_m \coloneqq\bigoplus_{p+q=m} V^{p, q}$ is defined over $\QQ$.
:::

::: {.front card-id="card-1d9900cc275457c7"}
What is a ZHS?
:::

::: {.back card-id="card-1d9900cc275457c7"}
A QHS $V$ with a lattice $V(\ZZ) \subset V(\QQ)$.
:::

::: {.front card-id="card-44dd1b29350dfaaf"}
What is the Weil element of a QHS?
:::

::: {.back card-id="card-44dd1b29350dfaaf"}
$C\in \operatorname{GL}(V)$ which acts as $i^{p-q}$ in $V^{p, q}$.
:::

::: {.front card-id="card-b9b109d2565bf9e1"}
What is a pure rational Hodge structure of weight $m$?
:::

::: {.back card-id="card-b9b109d2565bf9e1"}
A finite-dimensional rational vector space $V$ with a decomposition
$$V_\CC=\bigoplus_{p+q=m}V^{p,q},\qquad \overline{V^{p,q}}=V^{q,p}.$$
Thus $V^{p,q}=0$ when $p+q\ne m$.
:::

::: {.front card-id="card-50d0923ee164ff53"}
What is the colevel of a HS?
:::

::: {.back card-id="card-50d0923ee164ff53"}
$\min\left\{{p\st h^{p, m-p} \neq 0}\right\}$.
:::

::: {.front card-id="card-5ee6faf8e21ba056"}
What are the filtrations on a HS?
:::

::: {.back card-id="card-5ee6faf8e21ba056"}
Decreasing Hodge filtration: $\operatorname{Fil}^n V \coloneqq\sum_{p \geq n, q} V^{p, q}$

Increasing weight filtration: $\operatorname{Fil}_n V \coloneqq\sum_{p+q \leq n} V^{p, q}$.
:::

::: {.front card-id="card-b5b2ef0bd90811ea"}
What are the Weil and Griffiths intermediate Jacobians?
:::

::: {.back card-id="card-b5b2ef0bd90811ea"}
Define $V_W$ the Weil complex structure $V_W^{1, 0}$ and Griffiths complex structure $V_G^{1 ,0} = F^{k+1}V$

Then
$$J_W(V)=V /\left(V(\mathbb{Z})+V_W^{1,0}\right) \text { and } J_G(V)=V /\left(V(\mathbb{Z})+F^{k+1} V\right)$$
:::

::: {.front card-id="card-a19566b1c063201e"}
What is the Serre-Deligne torus $S$? Why is it important?
:::

::: {.back card-id="card-a19566b1c063201e"}
$S({\mathbf{R}}) =\CC^{\times}$, so $S = \mathrm{Res}^{\CC}_{{\mathbf{R}}} {\mathbf{G}}_m$.

Alternatively ${ \begin{bmatrix} {a} & {-b}  \\ {b} & {a} \end{bmatrix} } \in \operatorname{GL}_2({\mathbf{R}})$.

There is a cocharacter $w: {\mathbf{G}}_m\to S$ which on real points is ${\mathbf{R}}^{\times}\hookrightarrow\CC^{\times}$, a QHS on $V$ is the same as an action $S\curvearrowright V$ defined over ${\mathbf{R}}$ with $w$ defined over $\QQ$, so $V^{p, q}$ are eigenspaces with characters $z^p\overline{z}^q$.

For a real algebra $A$, $S(A)=(A\otimes_{\mathbf R}\CC)^{\times}$.
:::

::: {.front card-id="card-890de6962a64c40d"}
What are $\ZZ(m)$ and the Tate twist $V(m)$?
:::

::: {.back card-id="card-890de6962a64c40d"}
The rank-one integral Hodge structure $\ZZ(m)$ has underlying lattice $(2\pi i)^m\ZZ$ and type $(-m,-m)$. In particular, $\ZZ(0)$ has weight zero and $\ZZ(-1)=\ZZ(1)^\vee$.

For an integral Hodge structure $V$, set $V(m)=V\otimes_\ZZ\ZZ(m)$; for a rational Hodge structure, use $V\otimes_\QQ\QQ(m)$. If $V$ has weight $n$, then $V(m)$ has weight $n-2m$ and $V(m)^{p,q}=V^{p+m,q+m}$.
:::

::: {.front card-id="card-fc3f20e8b96f267b"}
What is a polarization of a (pure) Hodge structure?
:::

::: {.back card-id="card-fc3f20e8b96f267b"}
For a pure HS of weight $m$, $Q:V{ {}^{ \scriptstyle\otimes_{}^{2} }  }\to \ZZ(-m)$ defined over $\QQ$, $(-1)^m$-symmetric, such that the form $(v,w)\mapsto (2\pi i)^m Q(Cv, \overline{w})$ is Hermitian and positive-definite, where $C$ is the Weil element ($C = i^{p-q}$ on $V^{p, q}$).

Equivalently, on $V_\CC = \bigoplus V^{p, q}$: the $V^{p, q}$ are mutually orthogonal for the sesquilinear form $Q(v, \overline{w})$, and $i^{p-q} Q(v, \overline{v}) > 0$ for $0\neq v\in V^{p, q}$. Since $i^{p-q} = (-1)^p i^{-m}$, this says $i^{-m}(-1)^p Q(v, \overline{v}) > 0$ on $V^{p, q}$ (for even $m$, $i^{-m} = \pm 1$ is a sign), giving a positive definite Hermitian product ${\left\langle {v},~{w} \right\rangle} \coloneqq i^{-m}\sum_{p, q} (-1)^p Q(v^{p, q}, \overline{w^{p, q}})$.

Alternatively a morphism $V\to V {}^{ \vee }(-m)$, motivated by Poincare duality.
:::

::: {.front card-id="card-8c6c5dcc6ef06e82"}
What is the Hodge–Frölicher spectral sequence?
:::

::: {.back card-id="card-8c6c5dcc6ef06e82"}
$E_1^{p, q} = H^q(M; \Omega_M^p) \Rightarrow H^{p+q}(M; \CC)$.
:::

::: {.front card-id="card-f1aac53fbedc8116"}
What is primitive cohomology?
:::

::: {.back card-id="card-f1aac53fbedc8116"}
Let $(X, g)$ be a compact Kahler manifold of complex dimension $n$ with Lefschetz operator $L$ (cup product with the Kahler class) and its adjoint $\Lambda$. Then
$$H_\prim^{n-k}(X) \coloneqq\ker\qty{H^{n-k} \xrightarrow{L^{k+1}} H^{n+k+2} },$$
equivalently
$$H^m(X, \mathbb{R})_{\prim}:=\operatorname{Ker}\left(\Lambda: H^m(X, \mathbb{R}) \longrightarrow H^{m-2}(X, \mathbb{R})\right)$$
and
$$H^{p, q}(X)_{\prim}:=\operatorname{Ker}\left(\Lambda: H^{p, q}(X) \longrightarrow H^{p-1, q-1}(X)\right)$$
The Kahler class induces a representation of ${\mathfrak{sl}}_2(\CC)$ on $H^*(X; {\mathbf{R}})$ via $L, \Lambda$, and primitive classes are its lowest weight vectors.

For a rational Kähler class, the Hodge–Riemann pairing polarizes the primitive rational cohomology of a smooth complex projective variety.
:::

::: {.front card-id="card-e405e246f75e260c"}
Discuss the Hodge spectral sequence for $M$ connected and projective (or more generally compact Kahler).
:::

::: {.back card-id="card-e405e246f75e260c"}
Degenerates at $E_1$, yielding a decreasing filtration $\operatorname{Fil}^* H^d(M;\CC)$ with ${\mathsf{gr}\,}^p H^d(M; \CC) \cong H^{d-p}(M; \Omega_M^p)$.

Puts a HS of pure weight $d$ on $H^d(M; \CC)$ with Hodge filtration $\operatorname{Fil}^*$.

$H^{2n}(M; \CC)= \ZZ(-n)$.

For $\eta\in H^2(M; \QQ)$ a hyperplane class, $\eta$ is type $(1,1)$ and defines a Lefschetz operator $L({-}) \coloneqq\eta\cup({-})$.

Hard Lefschetz holds: $L^k: H^{n-k}(M; \QQ) { \, \xrightarrow{\sim}\, }H^{n+k}(M; \QQ)$ for all $n$.
$$\bigoplus_{k=0}^n H_\prim^{n-k}(M; \QQ)\otimes_{\mathbf{R}}{\CC[L] \over \left\langle{L^{k+1}}\right\rangle} { \, \xrightarrow{\sim}\, }H^*(M; \CC)$$
There is a polarization
$$\begin{align}I: H_\prim^{n-k}(M; \QQ){ {}^{ \scriptstyle\otimes_{}^{2} }  } &\to \QQ\\ a\otimes b &\mapsto(-1)^{(n-k)(n-k-1)\over 2} \int_M L^k(a\wedge b)\end{align}$$
:::

::: {.front card-id="card-37366038babffe54"}
What is a VHS?
:::

::: {.back card-id="card-37366038babffe54"}
Over a smooth variety $S$, a local system $V$ on $S$ of ${}_{ \CC}\Mod^\fd$ defined over $\QQ$

With an increasing weight filtration by sub-local systems

With a decreasing Hodge filtration on the underlying vector bundle $\mcv\coloneqq{\mathcal{O}}_S \otimes{\CC_S} V$ by sub-bundles satisfying

Having a HS on every fiber

The covariant derivative maps $\operatorname{Fil}^p \mcv\to \operatorname{Fil}^{p-1}\mcv$.
:::

::: {.front card-id="card-c07bc2f98b5d8923"}
What is a PVHS over $S$?
:::

::: {.back card-id="card-c07bc2f98b5d8923"}
For a VHS of pure weight $m$, a polarization $V\otimes_{\CC_S}V\to \ZZ_S(-m)$.
:::

::: {.front card-id="card-e6544d5bd9f4a789"}
What is the Gysin sequence?
:::

::: {.back card-id="card-e6544d5bd9f4a789"}
$$\cdots \rightarrow \mathrm{H}_{\mathrm{Y}}^{\mathrm{d}}(\mathrm{X}) \rightarrow \mathrm{H}^{\mathrm{d}}(\mathrm{X}) \rightarrow \mathrm{H}^{\mathrm{d}}(\mathrm{X}-\mathrm{Y}) \rightarrow \mathrm{H}_{\mathrm{Y}}^{\mathrm{d}+1}(\mathrm{X}) \rightarrow \cdots$$
:::

::: {.front card-id="card-b8012eac51298054"}
What is an MHS?
:::

::: {.back card-id="card-b8012eac51298054"}
A decreasing Hodge filtration $\operatorname{Fil}_H V$ and an increasing weight filtration $\operatorname{Fil}^W V$ such that the filtration on ${\mathsf{gr}\,}_\ell^W$ induced by $\operatorname{Fil}_H$ gives a HS of pure weight $\ell$.
:::

::: {.front card-id="card-374386fcc6e36a35"}
Discuss MHSs.
:::

::: {.back card-id="card-374386fcc6e36a35"}
For $X\in \Sch_{/ {\CC}}^\mathrm{ft}$ a variety, $H^d(X)$ carries a MHS with weights in $\left\{{0,1,\cdots, 2d}\right\}$.

If $X$ is smooth, the weights are $\geq d$.

If $X$ is complete, the weights are $\leq d$.

This extends the functor $\Mfd_\CC\to \mathsf{HS}$ to $\Var_{/ {\CC}}^\mathrm{ft}\to \mathsf{MHS}$.
:::

::: {.front card-id="card-7c05866113c85a06"}
What is the polarization on $H^1(X)$ for $X$ smooth Kahler?
:::

::: {.back card-id="card-7c05866113c85a06"}
$(\alpha, \beta)\mapsto \int_M \alpha\wedge\beta\wedge \omega^{\dim M - 1} \in {\mathbf{R}}$.
:::

::: {.front card-id="card-e8e75131312213a6"}
Where do MHSs appear?
:::

::: {.back card-id="card-e8e75131312213a6"}
Cohomology of noncompact $\CC\dash$varieties.

Limits of PVHS

$\pi_1(X) \otimes{\mathbf{R}}$ for $X\in \mathsf{Alg}\Var_{/ {\CC}}$.

$\pi_*(X)\otimes{\mathbf{R}}$ for $X\in  \mathsf{Alg}\Var_{/ {\CC}}$ with $\pi_1(X) = 1$.
:::

::: {.front card-id="card-079445b64b54e7dd"}
What is a polarized VHS for $(E, d: A^0(E) \to A^1(E))$ a flat bundle on $X$?
:::

::: {.back card-id="card-079445b64b54e7dd"}
Puts a Hermitian metric on a vector bundle!

$E = \bigoplus_{p+q=k} E^{p, q}$ as sub-bundles such that
$$d(A^0\left(E^{p, q}\right)) \subseteq A^{1,0}\left(E^{p, q}\right) \oplus A^{1,0}\left(E^{p-1, q+1}\right) \oplus A^{0,1}\left(E^{p, q}\right) \oplus A^{0,1}\left(E^{p+1, q-1}\right)$$
Each fiber $E_x$ is a Hodge structure of weight $k$.

Polarization: $Q: A^0(E) \otimes_{A^0}\overline{A^0(E)} \to A^0$ which satisfies the Leibniz rule wrt $d$ and induces polarizations on every fiber.

Yields a positive definite Hermitian metric $h(u, w)\coloneqq\sum_{p+q=k} (-1)^p Q(v^{p, q}, w^{p, q})$.
:::

::: {.front card-id="card-d4a5c94c94971cbf"}
What is Griffiths transversality?
:::

::: {.back card-id="card-d4a5c94c94971cbf"}
$$\nabla(\mcf^p)\subseteq \mcf^{p-1} \otimes\Omega^1$$
Needed since the Hodge filtration on the fibers are not necessarily preserved by differentiation.
:::

::: {.front card-id="card-749702f361b7071a"}
What is a connection?
:::

::: {.back card-id="card-749702f361b7071a"}
For $L$ a local system on $Y$,parallel transport induces $\nabla_\eta: V_y\to V_y$ for $\eta\in T_y Y$ and $V\coloneqq{\mathcal{O}}_Y\otimes_\CC L$ the associated vector bundle.

Satisfies $\nabla_\eta(fv) = \eta(f)v + f\nabla_\eta(v)$.

View as an operator $\nabla: V\to \Omega^1_Y \otimes V$ satisfying $\nabla(fv) = df\otimes v + f\nabla(v)$.
:::

::: {.front card-id="card-d405c897c5dcf46b"}
When is a connection integrable?
:::

::: {.back card-id="card-d405c897c5dcf46b"}
E.g. if $\nabla^2 = 0$; equivalent to having $\operatorname{rank}V$ solutions to $\nabla v = 0$.
:::

::: {.front card-id="card-13b2ac619d704015"}
What is the Gauss-Manin connection?
:::

::: {.back card-id="card-13b2ac619d704015"}
For $f:X\to Y$, the integrable connection on $V \coloneqq{\mathcal{O}}_Y \otimes_\CC{\mathbf{R}}^i f_* \underline{\CC}$, the vector bundle associated to the local system $L\coloneqq{\mathbf{R}}^1 f_* \underline{\CC}$.

Sections $L$ are precisely solutions to $\nabla v = 0$.
:::

::: {.front card-id="card-7ed36435cd4087ee"}
Motivate perverse sheaves.
:::

::: {.back card-id="card-7ed36435cd4087ee"}
The Leray spectral sequence doesn't degenerate for arbitrary morphisms $f:X\to Y$, nor is there a decomposition ${\mathbf{R}}f_* \QQ= \bigoplus {\mathbf{R}}^q f_* \QQ[-q]$.

Instead ${\mathbf{R}}f_* \QQ$ decomposes (in a weaker sense) into perverse sheaves.

Decomposition theorem: Let $f: X \rightarrow Y$ be a projective map of complex algebraic varieties, with $X$ smooth, then $\mathbb{R} f_* \mathbb{Q}$ decomposes into a sum of translates of simple perverse sheaves.
:::

::: {.front card-id="card-48e8cb4d83d5162d"}
Motivate ${}_\mcd\Mod$.
:::

::: {.back card-id="card-48e8cb4d83d5162d"}
Generalize integrable connections.

Coherent such correspond to a system of PDEs.

A PVHS gives a regular holonomic ${}_\mcd\Mod$.
:::

::: {.front card-id="card-62ce6f1165580cfb"}
Define ${}_\mcd\Mod$.
:::

::: {.back card-id="card-62ce6f1165580cfb"}
For $X$, let $D_X$ be the sheaf of algebras of holomorphic differential operators.

For $X = {\mathbf{A}}^n$, $H^0(D_X) = W^n$ the Weyl algebra: $\left\langle{x_1,\cdots, x_n, {\partial}_1,\cdots, {\partial}_n}\right\rangle/\left\langle{\left[x_i, x_j\right]=\left[\partial_i, \partial_j\right]=0,\left[\partial_i, x_j\right]=\delta_{i j}}\right\rangle$.

$M\in   {}_{\mathcal D_X}\Mod \subset   {}_{{\mathcal{O}}_X}\Mod$ if $M\in \Sh(X; \Ab\Grp)$ where $D_X\curvearrowright M$ from the left.
:::

::: {.front card-id="card-c1fe4aa5951fa4cd"}
Give an example of $M\in {}_\mcd\Mod$.
:::

::: {.back card-id="card-c1fe4aa5951fa4cd"}
$(V, \nabla)$ an integrable vector bundle, with ${\partial}_i .v \coloneqq\nabla_{{\partial}_i}(v)$.

Need integrability to get $[{\partial}_i {\partial}_j] = 0$.
:::

::: {.front card-id="card-bd8193568fce0868"}
What is a perverse sheaf?
:::

::: {.back card-id="card-bd8193568fce0868"}
An object of $D_{{\operatorname{const.}}}^b(X,   {}_{ \CC}\Mod)$ (complexes of sheaves of vector spaces with bounded constructible cohomology) isomorphic to $\mathrm{RH}(M)$ for some $M\in    {}_\mcd\Mod ^{\text{hol}}$ and $\mathrm{RH}({-}) \coloneqq\mathop{\mathrm{\mathbb{R}Hom}}({-}, {\mathcal{O}}_X)$ is the functor inducing the Riemann-Hilbert equivalence.
:::

::: {.front card-id="card-1ac89899346723e1"}
Motivate the sheaves $\mathrm{IC}(L)$ for a local system $L$.
:::

::: {.back card-id="card-1ac89899346723e1"}
For singular spaces, only allow chains which meet the singular strata with appropriate codimensions.

Always a perverse sheaf.
:::

::: {.front card-id="card-fd276d037dd8cb3f"}
What is Saito's theorem?
:::

::: {.back card-id="card-fd276d037dd8cb3f"}
For $f:X\to Y$ projective, ${\mathbf{R}}f_* K$ decomposes into a sum of IC complexes associated to PVHS when $K$ is in a certain subcategory of regular holonomic ${}_\mcd\Mod$.
:::

::: {.front card-id="card-9fb9b11c6c6eb0ba"}
What is the significance of the weight filtration?
:::

::: {.back card-id="card-9fb9b11c6c6eb0ba"}
${\mathsf{gr}\,}_\ell W_*$ carries a pure HS of weight $\ell$, so looks like $H^\ell$ of a smooth projective variety.
:::

::: {.front card-id="card-37c7477ed34e32d2"}
Discuss VHSs.
:::

::: {.back card-id="card-37c7477ed34e32d2"}
For $f:X\to Y$, suppose $H^k(X_y; \CC)$ carries a filtration

Organize $\left\{{H^k(X_y; \CC)}\right\}_{y\in Y}$ into a local system.

Tensor with functions on the base to get a flat bundle $(V, \nabla)$/

Filtrations organize into sub-bundles.
:::

::: {.front card-id="card-29a78cbc2139cd55"}
What is the monodromy theorem for VHSs?
:::

::: {.back card-id="card-29a78cbc2139cd55"}
For $V$ a PVHS over $\mathbb{D}^\circ$, lift via $\pi: {\mathbb{H}}\to \mathbb{D}$ to get a monodromy morphism $\rho: \pi_1(\mathbb{D}^\circ) \to {\operatorname{O}}(H^0({\mathbb{H}}; \pi^* V))$ with the form $I$.

Theorem: the eigenvalues of $T\coloneqq\rho(1)$ are of the form $\zeta_n$ for some $n$, and in particular ${\left\lvert {\lambda} \right\rvert} = 1$.

$T$ has Jordan blocks of size at most $d\coloneqq\max\left\{{{\left\lvert {p-q} \right\rvert}\st h^{p, q}\neq 0}\right\}$.
:::

::: {.front card-id="card-f71cc370724c36c7"}
What is the Jacobian of a complex manifold?
:::

::: {.back card-id="card-f71cc370724c36c7"}
$$\operatorname{Jac}(X) \coloneqq H^1({\mathcal{O}}_X)/H^1(X; \ZZ)\cong \ker(\operatorname{Pic}(X) \to H^2(X; \ZZ)) \cong \operatorname{Pic}^0(X)$$
The continuous part of $\operatorname{Pic}(X)$.
:::

::: {.front card-id="card-e21fb5304f2bb38b"}
What is the Lefschetz 1-1 theorem?
:::

::: {.back card-id="card-e21fb5304f2bb38b"}
For a compact Kähler manifold $X$, the image of $c_1:\operatorname{Pic}(X)\to H^2(X;\ZZ)$ is the subgroup of integral classes whose images in $H^2(X;\CC)$ have type $(1,1)$.
:::

::: {.front card-id="card-3617dcb5de3156d3"}
How is $c_1$ realized as a morphism:
:::

::: {.back card-id="card-3617dcb5de3156d3"}
$c_1: \operatorname{Pic}(X) \to H^2_\text{ét}(X; { \ZZ_{\widehat{\ell}} }(1))$.
:::

::: {.front card-id="card-26e2d214ce1626dc"}
What are isogenous Hodge structures?
:::

::: {.back card-id="card-26e2d214ce1626dc"}
$V, W$ with integral Hodge structures are isogenous iff $V_\QQ\cong W_\QQ$.
:::

::: {.front card-id="card-49d969d85716f30f"}
What are Hodge classes?
:::

::: {.back card-id="card-49d969d85716f30f"}
For $V$ a Hodge structure of even weight $2k$, the intersection $V\cap V^{k, k}$.
:::

::: {.front card-id="card-caf733a4c2c79137"}
What are $\ZZ(1), \QQ(1)$?
:::

::: {.back card-id="card-caf733a4c2c79137"}
The Tate Hodge structure $\mathbf{Z}(1)$ is the Hodge structure of weight $-2$ given by the free $\mathbf{Z}$-module of rank one $(2 \pi i) \mathbf{Z}$ (as a submodule of $\mathbf{C}$ ) such that $\mathbf{Z}(1)^{-1,-1}$ is one-dimensional. Similarly, one defines the rational Tate Hodge structure $\mathbf{Q}(1)$.
:::

::: {.front card-id="card-3f0ae58e29b77281"}
What is the Hodge filtration?
:::

::: {.back card-id="card-3f0ae58e29b77281"}
$\Fil^i V_\CC\coloneqq\bigoplus_{p\geq i} V^{p, q}_\CC$, satisfies $\Fil^p V_\CC\oplus\overline{\Fil^q V_\CC} = V_\CC$ for all $p+q=n+1$.
:::

::: {.front card-id="card-9b71bf87ceb9944f"}
What is the Hodge structure associated to an arbitrary Hodge filtration?
:::

::: {.back card-id="card-9b71bf87ceb9944f"}
For $\Fil^* V$ a Hodge filtration, define $V^{p, n-p} \coloneqq\Fil^p V \cap\overline{\Fil^{n-p} V}$.
:::

::: {.front card-id="card-7157bd1d4cfece5d"}
Discuss the Hodge conjecture.
:::

::: {.back card-id="card-7157bd1d4cfece5d"}
The even part $\bigoplus H^{2 k}(X, \mathbf{Q})$ contains all algebraic classes, i.e. classes obtained as fundamental classes $[Z]$ of subvarieties $Z \subset X$. It is not difficult to see that $[Z]$ is an integral class, i.e. that it comes from an element in $H^{2 k}(X, \mathbf{Z})$, and that it is contained in $H^{k, k}(X)$.

The Hodge conjecture asserts that the space spanned by those is determined entirely by the Hodge structure itself.

(Hodge conjecture). For a smooth projective variety $X$ over $\mathbf{C}$ the subspace of $H^{2 k}(X, \mathbf{Q})$ spanned by all algebraic classes $[Z]$ coincides with the space of Hodge classes, i.e.
$$H^{2 k}(X; \mathbf{Q}) \cap H^{k, k}(X)=\left\langle{[Z] \st Z \subset X}\right\rangle_\QQ$$
:::

::: {.front card-id="card-9274e5ea0d527d5d"}
Discuss the status of the Hodge conjecture.
:::

::: {.back card-id="card-9274e5ea0d527d5d"}
Can fail for nonprojective hyperkahlers, integral version known not to hold.

Known for $(1, 1)\dash$classes and $(\dim X-1, \dim X - 1)\dash$classes.

Known for K3s, but not for products of K3s.
:::

::: {.front card-id="card-875031744b580783"}
What is a Hodge isometry?
:::

::: {.back card-id="card-875031744b580783"}
For polarized Hodge structures $(V_1,q_1)$ and $(V_2,q_2)$, a Hodge isometry is an isomorphism $f:V_1\xrightarrow{\sim}V_2$ of Hodge structures such that $q_2(fx,fy)=q_1(x,y)$ for all $x,y\in V_1$.
:::

::: {.front card-id="card-f684c22e4863facf"}
What is the Hodge-Riemann pairing?
:::

::: {.back card-id="card-f684c22e4863facf"}
Consider a rational (or integral) Kahler class $\omega \in H^2(X, \mathbf{Q})$ on a smooth projective manifold $X$. Then define on $H^n(X, \mathbf{Q})$ with $n \leq d=\operatorname{dim}_\CC X$ the following pairing:
$$(v, w) \longmapsto(-1)^{n(n-1) / 2} \int_X v \wedge w \wedge \omega^{d-n}$$
:::

::: {.front card-id="card-6d7de03bbbdaa923"}
How can one interpret Hodge structures as representations of the Deligne torus?
:::

::: {.back card-id="card-6d7de03bbbdaa923"}
Given $V$ a Hodge structure of weight $n$, define
$$\begin{align}
\rho: \CC^{\times}&\to \operatorname{GL}(V_{\mathbf{R}}) \quad \in \Grp\
z &\mapsto (v\mapsto z^p \overline{z}^q\cdot v), \quad v\in V^{p, q}
.\end{align}$$
$\QQ\dash$Hodge structures of weight $n$ biject with algebraic representations $\rho$ with an ${\mathbf{R}}^{\times}$ action defined by $\rho(t).v\coloneqq t^n.v$.

The inverse construction sends $\rho$ to $V^{p, q}:=\left\{v \in V_\CC \mathrel{\Big|}\rho_\CC(z)(v)=\left(z^p \overline{z}^q\right) \cdot v \text { for all } z \in \mathbf{C}^*\right\}$ where $\rho_\CC: \CC^{\times}\to \operatorname{GL}(V_\CC)$ is a $\CC\dash$linear extension.

Then $\rho_\CC$ splits into a sum of characters and $V_\CC= \bigoplus V^{p, q}$.
:::

::: {.front card-id="card-dfcbd23d66336108"}
Which representation of the Deligne torus corresponds to $\QQ(1)$?
:::

::: {.back card-id="card-dfcbd23d66336108"}
- $\QQ(1)$ which corresponds to
$$\begin{align}
\CC^{\times}&\to {\mathbf{R}}^{\times}\
z &\mapsto (z\overline{z})^{-1}
.\end{align}$$
:::

::: {.front card-id="card-41bbe9b420b7f0c1"}
Discuss bijections for Hodge structures of weight one.
:::

::: {.back card-id="card-41bbe9b420b7f0c1"}
All of geometric origin, using that projective tori are abelian varieties:
$$\begin{align}
\left\{{T/\CC\text{ tori}}\right\} &\rightleftharpoons\ZZ\operatorname{HS}^1 \\
\left\{{T/\CC\text{ abelian varieties}}\right\} &\rightleftharpoons\left\{{V\in \ZZ\operatorname{HS}^1 \text{ polarizable}}\right\} \\
\left\{{T/\CC\text{ polarized abelian varieties}}\right\} &\rightleftharpoons\left\{{V\in \ZZ\operatorname{HS}^1 \text{ polarized}}\right\}
.\end{align}$$
:::

::: {.front card-id="card-eb58491fe6b0d0bb"}
What are the Hodge and Mumford-Tate groups of $V\in \mathbf{Q}\kern-0.5pt\operatorname{HS}$ polarizable?
:::

::: {.back card-id="card-eb58491fe6b0d0bb"}
Identifying the Hodge structure with a representation $\rho: {\mathbb{S}}\to \operatorname{GL}(V_{\mathbf{R}})$, the smallest algebraic subgroups of $\operatorname{GL}(V)/\QQ$ with
$$\begin{align}
\rho(\mathbb{U}({\mathbf{R}})) \subseteq \Hodge(V)({\mathbf{R}}) \qquad \rho({\mathbb{S}}({\mathbf{R}})) \subseteq \operatorname{MT}(V)({\mathbf{R}})
.\end{align}$$
where $\mathbb{U}\coloneqq\ker\qty{{\mathbb{S}}\xrightarrow{\operatorname{Nm}} {\mathbf{G}}_m({\mathbf{R}})} = \left\{{z\in {\mathbb{S}}({\mathbf{R}}) \st z\overline{z} = 1}\right\}$.

Related by a morphism
$$\begin{align}
\Hodge(V)\times {\mathbf{G}}_m &\to\operatorname{MT}(V) \
(g, \mu) &\mapsto g\mu
.\end{align}$$
What does it mean for a K3 surface to have CM?

$\Hodge(T)$ is commutative, equivalently $\dim_K(T) = 1$. Implies that $K$ is a CM field.
:::

::: {.front card-id="card-c4f19ff090c4318b"}
What is the $\ell\dash$adic algebraic monodromy group?
:::

::: {.back card-id="card-c4f19ff090c4318b"}
For $X\in {\mathsf{sm}}\Var^{\mathop{\mathrm{proj}}}_{/ {k}}$ with $k$ finitely-generated of characteristic zero, the Zariski closure of the image of the Galois representation
$$\begin{align}
\rho*\ell: G*k &\to \operatorname{GL}(V), \qquad V = H^2*\text{ét}(X; { \QQ*\ell }(1))
.\end{align}$$
:::

::: {.front card-id="card-4137a8b3bad51d35"}
What is the Mumford-Tate conjecture?
:::

::: {.back card-id="card-4137a8b3bad51d35"}
Under the isomorphism $H^2_\text{ét}(X; { \QQ_\ell }(1)) { \, \xrightarrow{\sim}\, }H^2(X(\CC); \QQ) \otimes{ \QQ_\ell }(1)$, the identity component of the $\ell\dash$adic monodromy group, $\overline{\operatorname{im}\rho_\ell}^0$, bijects with the Mumford-Tate group $\operatorname{MT}(X)$.

Proved for K3s over number fields.
:::

::: {.front card-id="card-b895e365a3b35d5b"}
What is the Hodge diamond for a surface?
:::

::: {.back card-id="card-b895e365a3b35d5b"}
For a smooth projective complex surface, the Hodge diamond is
$$\begin{matrix}&&1&&\\&q&&q&\\p_g&&h^{1,1}&&p_g\\&q&&q&\\&&1&&\end{matrix}$$
where $q=h^{1,0}=h^1(\mathcal O_X)$ and $p_g=h^{2,0}=h^0(\omega_X)$.
:::
