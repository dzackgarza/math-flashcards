---
title: "Algebraic Geometry::Hodge Theory"
---

::: {.front card-id="hodge-clemens-schmid-surface-specialization" tags="theorem comparison example"}
For a projective semistable degeneration of surfaces, how does Clemens–Schmid relate central-fiber cohomology to limiting cohomology? What follows when monodromy is finite?
:::

::: {.back card-id="hodge-clemens-schmid-surface-specialization"}
Let $f:\mathcal X\to\Delta$ be projective, with $\mathcal X$ smooth, $X_0$ a reduced SNC divisor, and smooth fibers over $\Delta^*$. With rational coefficients and $N=\log T$, the exact segment is
$$H_4(X_0)(-3)\longrightarrow H^2(X_0)
\xrightarrow{\mathrm{sp}}H^2_{\lim}
\xrightarrow{N}H^2_{\lim}(-1)
\longrightarrow H_2(X_0)(-3).$$
The first map comes from duality and restriction; $\mathrm{sp}$ is specialization. The displayed Tate twists make these morphisms of mixed Hodge structures.

Thus $\operatorname{im}(\mathrm{sp})=\ker N$. If monodromy is finite, a finite base change kills it; after semistable reduction $N=0$, $H^2_{\lim}$ is pure of weight two, and specialization is surjective. It can still have a kernel from central-fiber component classes.

Simple comparison in degree one: two smooth curves joined at a separating node have trivial monodromy and pure limiting $H^1$. An irreducible one-nodal curve has a nonzero vanishing-cycle monodromy. Reducibility alone does not determine the weight filtration.

Reference: Gallardo–Pearlstein–Schaffler–Zhang, §6; Morrison, *The Clemens–Schmid exact sequence and applications*.
:::

::: {.front card-id="hodge-v-manifold-purity" tags="definition comparison"}
What is a complex V-manifold? What Hodge-theoretic conclusion holds for a projective V-manifold?
:::

::: {.back card-id="hodge-v-manifold-purity"}
A complex analytic space locally isomorphic to $U/G$, where $U$ is smooth and $G$ is finite: a space with finite quotient singularities. It need not be smooth; $\mathbb A^2/\{\pm1\}$ is the $A_1$ example.

For a projective V-manifold, $H^k(X,\mathbb Q)$ carries a pure Hodge structure of weight $k$, with the usual Hodge decomposition. This applies to ordinary rational cohomology of the quotient space; it does not assert smoothness or an integral torsion-free cohomology lattice.

For a reducible stable surface, apply this fact to quotient-singular components where appropriate, then analyze the gluing. Purity of the components alone does not make the whole central fiber's cohomology pure.

Reference: Gallardo–Pearlstein–Schaffler–Zhang, Remark 1.6 and §6; Peters–Steenbrink, *Mixed Hodge Structures*.
:::

::: {.front card-id="hodge-representation-scheme-presentations" tags="definition application"}
Construct a representation scheme from a group presentation. Compute it for a free group, a surface group, and rank-one representations of a closed surface.
:::

::: {.back card-id="hodge-representation-scheme-presentations"}
For $\Gamma=\langle x_1,\ldots,x_m\mid R_1,\ldots,R_s\rangle$ and a complex affine algebraic group $G$,
$$\operatorname{Rep}(\Gamma,G)=\{(g_1,\ldots,g_m)\in G^m:R_j(g_1,\ldots,g_m)=1\ \forall j\}.$$
Use the scheme-theoretic equations. It represents $A\mapsto\operatorname{Hom}(\Gamma,G(A))$ for commutative $\mathbb C$-algebras $A$, independently of the chosen presentation.

| Group | Representation scheme |
| --- | --- |
| Free group $F_m$ | $G^m$ |
| $\pi_1(\Sigma_g)$ | $\{(A_i,B_i)\in G^{2g}:\prod_{i=1}^g[A_i,B_i]=1\}$ |
| $\pi_1(\Sigma_g)$ into $\mathbb G_m$ | $(\mathbb C^*)^{2g}$ |

Here $[A,B]=ABA^{-1}B^{-1}$. In rank one commutators are trivial, and conjugation is trivial, so the coarse character variety is the same torus. For $g=1$ and general $G$, the equation is $AB=BA$, not an unconstrained pair.
:::

::: {.front card-id="hodge-representation-quotients-jordan-example" tags="comparison application"}
Distinguish a representation scheme, conjugacy classes, a character variety, and a quotient stack. Use a nontrivial unipotent representation of $\mathbb Z$ in $\mathrm{SL}_2$.
:::

::: {.back card-id="hodge-representation-quotients-jordan-example"}
For $R=\operatorname{Hom}(\Gamma,G)$:

| Object | Information retained |
| --- | --- |
| $R$ | Representation with chosen frame at the basepoint |
| Set $R(\mathbb C)/G(\mathbb C)$ | Every conjugacy class separately |
| $R/\!/G$ | Closed orbits; identifies each orbit with its closed-orbit limit |
| Stack $[R/G]$ | Representations and their automorphisms; stabilizer at $\rho$ is $Z_G(\rho)$ |

Send the generator of $\mathbb Z$ to $J=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. Then
$$\begin{pmatrix}t&0\\0&t^{-1}\end{pmatrix}
J\begin{pmatrix}t^{-1}&0\\0&t\end{pmatrix}
=\begin{pmatrix}1&t^2\\0&1\end{pmatrix}\longrightarrow I.$$
$J$ and $I$ are not conjugate, but have the same GIT point. Indeed $\mathcal X(\mathbb Z,\mathrm{SL}_2)\cong\mathbb A^1$ via trace; both have trace two. The quotient stack distinguishes them and their different centralizers.
:::

::: {.front card-id="hodge-flat-connections-local-systems" tags="definition construction"}
State the correspondence between flat bundles, local systems, and representations. Give both constructions and explain the role of the basepoint and frame.
:::

::: {.back card-id="hodge-flat-connections-local-systems"}
$X$ connected smooth manifold, basepoint $x$, universal cover $\widetilde X$:
$$\{\text{complex flat bundles }(E,\nabla),\ \nabla^2=0\}
\simeq\{\text{finite-rank complex local systems}\}
\simeq\{\text{representations of }\pi_1(X,x)\}.$$
Maps are connection-preserving maps, local-system maps, and intertwiners, respectively. Horizontal sections give $\ker\nabla$; parallel transport gives monodromy after a frame of $E_x$ is chosen.

Conversely $\rho$ gives $E_\rho=(\widetilde X\times\mathbb C^r)/\pi_1(X,x)$ with its descended trivial connection. Changing the frame conjugates $\rho$; retaining the frame gives the representation space. Taking isomorphism classes without a frame gives conjugacy classes, not automatically their GIT quotient.

On a complex manifold, use holomorphic flat bundles; on a smooth projective complex variety, GAGA identifies these with algebraic integrable connections. For a nonproper algebraic variety, regular singularities at infinity are required for the algebraic Riemann–Hilbert equivalence.
:::

::: {.front card-id="hodge-harmonic-bundles-hitchin-equations" tags="definition construction"}
On a compact Riemann surface, write the harmonic-metric equations that construct the nonabelian Hodge correspondence. Which connection is flat?
:::

::: {.back card-id="hodge-harmonic-bundles-hitchin-equations"}
For a degree-zero polystable Higgs bundle $(E,\bar\partial_E,\theta)$, a Hermitian metric $h$ with Chern connection $D_h$ solves
$$F_{D_h}+[\theta,\theta^{*h}]=0,\qquad
\bar\partial_E\theta=0.$$
The bracket includes wedge product of forms and composition of endomorphisms. On a curve $\theta\wedge\theta=0$ automatically. The associated complex connection
$$D=D_h+\theta+\theta^{*h}$$
is flat. Conversely a semisimple flat connection admits a harmonic metric, whose unitary and self-adjoint parts recover this Higgs bundle.

The unitary connection $D_h$ generally has nonzero curvature; it is $D$ that is flat. For stable objects the harmonic metric is unique up to positive scalar; polystable objects permit rescaling on stable summands. Gauge-equivalent harmonic solutions give the same moduli point.

Reference: Hitchin, *The self-duality equations on a Riemann surface*; Simpson, *Higgs bundles and local systems*.
:::

::: {.front card-id="hodge-unitary-and-rank-one" tags="comparison application"}
Identify the unitary locus in nonabelian Hodge theory. Compute the Betti and Dolbeault moduli spaces in rank one on a genus-$g$ curve.
:::

::: {.back card-id="hodge-unitary-and-rank-one"}
For a smooth projective complex curve $C$,
$$M_B(C,1)=\operatorname{Hom}(\pi_1C,\mathbb C^*)=(\mathbb C^*)^{2g},\qquad
M_{\mathrm{Dol}}(C,1)=\operatorname{Pic}^0(C)\times H^0(C,K_C)=T^*\operatorname{Pic}^0(C).$$
Both have complex dimension $2g$. The Betti space is affine; for $g>0$ the Dolbeault space contains the positive-dimensional projective zero section, so they are not algebraically isomorphic. Nonabelian Hodge gives a homeomorphism.

Unitary representations correspond exactly to $\theta=0$ and polystable degree-zero bundles (Narasimhan–Seshadri). In rank one,
$$\operatorname{Hom}(\pi_1C,U(1))\cong\operatorname{Pic}^0(C)$$
as real tori. Nonunitary monodromy, detected by its absolute values, corresponds to a nonzero Higgs field. For $g=0$, both rank-one moduli spaces are a point.
:::

::: {.front card-id="hodge-moduli-deformation-dimensions" tags="formula comparison"}
Relate the tangent and obstruction theories of Betti, de Rham, and Dolbeault moduli on a smooth projective complex curve of genus $g\ge2$. Compute the dimension at an irreducible rank-$r$ point.
:::

::: {.back card-id="hodge-moduli-deformation-dimensions"}
For a local system $L$, group cohomology uses the adjoint action $\operatorname{Ad}\rho$:

| Description | Deformation complex |
| --- | --- |
| Betti | Group cochains $C^\bullet(\pi_1C,\operatorname{End}L)$ |
| de Rham | $(\Omega^\bullet(C,\operatorname{End}E),d_\nabla)$ |
| Dolbeault | $\operatorname{End}E\xrightarrow{[\theta,-]}\operatorname{End}E\otimes K_C$ and its hypercohomology |

Degree zero gives infinitesimal automorphisms, degree one deformations modulo infinitesimal gauge, and degree two an obstruction space. For the framed representation scheme, the tangent space is $Z^1$; conjugation directions form $B^1$, so $Z^1/B^1=H^1$. At reducible points, $H^1$ is a deformation-space description, not automatically the Zariski tangent of the coarse GIT quotient.

For $g\ge2$ and irreducible $\mathrm{GL}_r$ monodromy, $h^0=h^2=1$ and Euler characteristic is $(2-2g)r^2$:
$$h^1=2r^2(g-1)+2.$$
The scalar obstruction vanishes; the stable locus is smooth of this complex dimension. With determinant connection fixed, use trace-free endomorphisms: dimension $2(r^2-1)(g-1)$. These dimensions agree across the correspondences; the complex tangent spaces are not identified by a holomorphic Dolbeault–Betti map.
:::

::: {.front card-id="hodge-lambda-connections-and-twistor" tags="definition comparison"}
Define a $\lambda$-connection, the Hodge moduli family, and the Deligne–Hitchin moduli space. Identify the special fibers.
:::

::: {.back card-id="hodge-lambda-connections-and-twistor"}
For a holomorphic bundle on a smooth projective complex curve and $\lambda\in\mathbb C$, a $\lambda$-connection is a $\mathbb C$-linear map
$$D_\lambda:E\to E\otimes K_C,\qquad
D_\lambda(fs)=fD_\lambda s+\lambda s\otimes df.$$
In higher dimension impose integrability $D_\lambda^2=0$ using the corresponding extension to forms. On a curve it is automatic.

The degree-zero semistable Hodge moduli family $M_{\mathrm{Hod}}\to\mathbb A^1$ has
$$M_{\mathrm{Hod},0}=M_{\mathrm{Dol}},\qquad
M_{\mathrm{Hod},1}=M_{\mathrm{dR}},\qquad
D_\lambda/\lambda\text{ flat for }\lambda\ne0.$$
The action $t:(\lambda,D_\lambda)\mapsto(t\lambda,tD_\lambda)$ scales the Higgs field at zero.

Glue the analytic Hodge families for $C$ and its conjugate curve $\bar C$ over $\mathbb C^*$, identifying the monodromy of $D_\lambda/\lambda$ and using parameter $\lambda^{-1}$ on the second chart. This gives the Deligne–Hitchin space over $\mathbb P^1$, with Dolbeault fibers for $C$ at zero and $\bar C$ at infinity. On the smooth harmonic-bundle locus it is the twistor space of the hyperkähler moduli metric.
:::

::: {.front card-id="hodge-stable-higgs-unstable-bundle-example" tags="application counterexample"}
Exhibit a stable degree-zero Higgs bundle whose underlying bundle is unstable on a genus-$g\ge2$ curve.
:::

::: {.back card-id="hodge-stable-higgs-unstable-bundle-example"}
Choose a square root $L$ of $K_C$, so $\deg L=g-1>0$. Set
$$E=L\oplus L^{-1},\qquad
\theta=\begin{pmatrix}0&0\\1&0\end{pmatrix}:E\to E\otimes K_C.$$
The lower-left entry uses $L\cong L^{-1}\otimes K_C$. The subbundle $L$ destabilizes $E$ but is not $\theta$-invariant.

Over the function field, this nonzero nilpotent matrix has a unique invariant line: its kernel $L^{-1}$. Every invariant rank-one subsheaf $F$ therefore satisfies $F\subseteq L^{-1}$ and $\deg F\le-(g-1)<0=\mu(E)$. Thus $(E,\theta)$ is stable, with $\operatorname{rk}E=2$, $\det E\cong\mathcal O_C$, and $\operatorname{tr}\theta=0$.
:::

::: {.front card-id="application-lefschetz-calabi-yau-hypersurface" tags="application"}
Let $X\subset\mathbb P^{d+1}_{\mathbb C}$ be a smooth hypersurface of degree $d+2$, with $d\ge2$. Determine $\omega_X$, $\pi_1(X)$, and $H^q(X,\mathcal O_X)$ for $0<q<d$. Which results give the conclusions?
:::

::: {.back card-id="application-lefschetz-calabi-yau-hypersurface"}
Adjunction gives $\omega_X=\mathcal O_X(d+2-d-2)\cong\mathcal O_X$. The homotopy form of weak Lefschetz gives $\pi_1(X)=\pi_1(\mathbb P^{d+1})=1$. For $q<d$, cohomology restriction is an isomorphism compatible with Hodge structures. The ambient space has $H^{0,q}=0$ for $q>0$, so
$$H^q(X,\mathcal O_X)=H^{0,q}(X)=0\qquad(0<q<d).$$
These establish the usual Calabi–Yau conditions. In top degree $h^d(\mathcal O_X)=1$ by Serre duality; it is outside the isomorphism range.
:::

::: {.front card-id="application-lefschetz-curve-monodromy" tags="application"}
Let $X$ be smooth connected complex projective with $\dim X\ge2$, and let $C$ be a smooth curve obtained by successive general hyperplane sections. Can a nontrivial representation $\pi_1(X)\to\operatorname{GL}_r(\mathbb C)$ become trivial on $C$? Must every representation of $\pi_1(C)$ extend to $X$?
:::

::: {.back card-id="application-lefschetz-curve-monodromy"}
Weak Lefschetz gives a surjection $\pi_1(C)\twoheadrightarrow\pi_1(X)$. Therefore restriction to $C$ preserves the image of a representation; in particular it detects triviality of monodromy. A representation of $\pi_1(C)$ extends to $X$ exactly when it kills the kernel of this surjection. Surjectivity alone does not make the fundamental groups isomorphic or ensure extension of arbitrary representations.
:::

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

::: {.front card-id="card-49cc848db9c8f1bf" tags="theorem"}
State hard Lefschetz and the primitive decomposition for a compact Kähler $n$-fold. What coefficient refinement applies to an ample integral class on a smooth complex projective variety?
:::

::: {.back card-id="card-49cc848db9c8f1bf"}
For $L=h\cup-$ with $h$ a Kähler class and $0\le k\le n$,
$$L^{n-k}:H^k(X,\mathbb R)\xrightarrow{\sim}H^{2n-k}(X,\mathbb R).$$
If $h$ is an ample integral class, the same isomorphism holds over $\mathbb Q$. With $P^j=\ker L^{n-j+1}$,
$$H^k(X,\mathbb R)=\bigoplus_{r\ge0}L^rP^{k-2r},\qquad P^j_{\mathbb C}=\bigoplus_{p+q=j}(P^j_{\mathbb C}\cap H^{p,q}(X)).$$
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
$X/\mathbb C$ smooth connected projective; fix rank $r$ and a polarization.

| Coarse moduli | Closed points |
| --- | --- |
| $M_B(X,r)$, Betti | Semisimple $\pi_1(X,x)\to\mathrm{GL}_r(\mathbb C)$ up to conjugacy |
| $M_{\mathrm{dR}}(X,r)$, de Rham | Semisimple integrable algebraic connections $(E,\nabla)$ up to isomorphism |
| $M_{\mathrm{Dol}}(X,r)$, Dolbeault | Polystable Higgs bundles $(E,\theta)$ with vanishing rational Chern classes |

Riemann–Hilbert gives $M_{\mathrm{dR}}^{\mathrm{an}}\cong M_B^{\mathrm{an}}$ by monodromy. Nonabelian Hodge theory gives a homeomorphism $M_{\mathrm{Dol}}^{\mathrm{an}}\cong M_B^{\mathrm{an}}$ via harmonic metrics, restricting to a diffeomorphism on smooth stable/irreducible loci. These comparisons are generally not algebraic; the Dolbeault–Betti comparison is generally not holomorphic.

Stable Higgs bundles correspond to irreducible local systems; polystable bundles correspond to semisimple ones. On a curve the Chern-class condition is degree zero. The analytic correspondence also holds for compact Kähler $X$ with stability defined by its Kähler class.

Reference: Simpson, [The Hodge filtration on nonabelian cohomology](https://arxiv.org/abs/alg-geom/9604005).
:::

::: {.front card-id="card-af845a3fa43df735"}
What is a rigid representation?
:::

::: {.back card-id="card-af845a3fa43df735"}
Local rigidity: the conjugacy class is isolated in the relevant character variety. Cohomological rigidity: $H^1(X,\operatorname{End}L)=0$; with determinant fixed, use $\operatorname{End}_0L$. The latter kills all first-order deformations and implies local rigidity; an isolated nonreduced point need not have zero tangent space. State which determinant and boundary-monodromy constraints are held fixed.

Simpson's geometric-origin conjecture, in the smooth complex projective setting: an irreducible rigid local system with finite-order determinant should be of geometric origin.

The proposed geometric description is a subquotient of a Gauss–Manin local system from a smooth projective morphism over a dense open $U\subset X$; this is the conjectured conclusion, not an established example for every rigid connection.

Concretely, $L|_U$ should occur as a direct summand of $R^if_*\mathbb C$ for such an $f:Y\to U$ (these local systems are semisimple).
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

$M$ has complex dimension $n$: $H^{2n}(M;\mathbb Q)\cong\mathbb Q(-n)$ for connected compact $M$.

For a Kähler class $\eta\in H^2(M;\mathbb R)$, $\eta$ is type $(1,1)$ and defines $L({-})\coloneqq\eta\cup({-})$. In the projective case an ample hyperplane class is integral, so the construction is defined over $\mathbb Q$.

Hard Lefschetz holds: $L^k:H^{n-k}(M;\mathbb R)\xrightarrow{\sim}H^{n+k}(M;\mathbb R)$ for $0\le k\le n$; use $\mathbb Q$ for an ample rational class.
$$\bigoplus_{k=0}^n H_\prim^{n-k}(M;\mathbb C)\otimes_{\mathbb C}\frac{\mathbb C[L]}{(L^{k+1})}\xrightarrow{\sim}H^*(M;\mathbb C).$$
For an ample rational class there is a rational polarization (use real coefficients for a general Kähler class)
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
For a vector bundle $V$ on a complex manifold $Y$, a connection differentiates local sections in tangent directions. It is not an endomorphism of a single fiber: its value depends on the first derivative of the section.

Satisfies $\nabla_\eta(fv) = \eta(f)v + f\nabla_\eta(v)$.

View as an operator $\nabla: V\to \Omega^1_Y \otimes V$ satisfying $\nabla(fv) = df\otimes v + f\nabla(v)$.
For a local system $L$, $V=\mathcal O_Y\otimes_\mathbb C L$ has a canonical flat connection $\nabla(f\otimes\ell)=df\otimes\ell$ for locally constant $\ell$; parallel transport recovers $L$.
:::

::: {.front card-id="card-d405c897c5dcf46b"}
When is a connection integrable?
:::

::: {.back card-id="card-d405c897c5dcf46b"}
For a holomorphic connection on a complex manifold, integrable means $\nabla^2=0$. Equivalently, locally there is a frame of $\operatorname{rank}V$ linearly independent horizontal sections solving $\nabla v=0$. Global horizontal sections may have smaller dimension because of monodromy.
:::

::: {.front card-id="card-13b2ac619d704015"}
What is the Gauss-Manin connection?
:::

::: {.back card-id="card-13b2ac619d704015"}
For a smooth proper morphism of complex varieties $f:X\to Y$, in the analytic topology $L=R^if_*\underline{\mathbb C}$ is a local system. Its associated bundle $V=\mathcal O_Y\otimes_\mathbb C L$ has the integrable Gauss–Manin connection; equivalently this is the connection on relative de Rham cohomology.

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
For a complex algebraic variety $X$, a middle-perverse sheaf is a constructible complex $K\in D^b_c(X^{\mathrm{an}},\mathbb C)$ satisfying $\dim_{\mathbb C}\operatorname{Supp}\mathcal H^j(K)\le-j$ and $\dim_{\mathbb C}\operatorname{Supp}\mathcal H^j(\mathbb D K)\le-j$ for every $j$, where $\mathbb D$ is Verdier duality. These complexes form the heart of the middle-perverse t-structure.

On smooth $X$ of complex dimension $d$, a local system $L[d]$ is perverse. Riemann–Hilbert identifies regular holonomic $D_X$-modules with perverse sheaves through the normalized de Rham functor; the normalized solution functor $R\mathcal Hom_{D_{X^{\mathrm{an}}}}(-,\mathcal O_{X^{\mathrm{an}}})[d]$ gives an anti-equivalence. Arbitrary bounded constructible complexes belong to the derived correspondence, not to this abelian heart.
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

::: {.front card-id="card-f684c22e4863facf" tags="theorem"}
For a smooth complex projective $n$-fold with ample class $h$ and $0\le k\le n$, state the Hodge–Riemann pairing on primitive degree-$k$ cohomology and its positivity on each Hodge type.
:::

::: {.back card-id="card-f684c22e4863facf"}
Set
$$P^k(X)=\ker\left(h^{n-k+1}:H^k(X,\mathbb C)\to H^{2n-k+2}(X,\mathbb C)\right),$$
and
$$Q_k(\alpha,\beta)=(-1)^{k(k-1)/2}\int_X\alpha\wedge\beta\wedge h^{n-k}.$$
For $0\ne\alpha\in P^k(X)\cap H^{p,q}(X)$, with $p+q=k$,
$$i^{p-q}Q_k(\alpha,\overline\alpha)>0.$$
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


::: {.front card-id="theorem-hodge-de-rham-degeneration" tags="theorem"}
For a smooth proper complex variety $X$, state the degeneration of the Hodge–de Rham spectral sequence and its dimension consequence.
:::

::: {.back card-id="theorem-hodge-de-rham-degeneration"}
The spectral sequence
$$E_1^{p,q}=H^q(X,\Omega_X^p)\Longrightarrow H_{\mathrm{dR}}^{p+q}(X)$$
degenerates at $E_1$. Consequently,
$$\dim H_{\mathrm{dR}}^n(X)=\sum_{p+q=n}h^q(X,\Omega_X^p).$$
:::

::: {.front card-id="theorem-weak-lefschetz" tags="theorem"}
Let $X$ be smooth complex projective of dimension $n\ge2$ and $H\subset X$ a smooth ample divisor. State the Lefschetz hyperplane theorem (weak Lefschetz) for integral homology, integral cohomology, and homotopy groups.
:::

::: {.back card-id="theorem-weak-lefschetz"}
Restriction
$$H^i(X,\mathbb Z)\longrightarrow H^i(H,\mathbb Z)$$
is an isomorphism for $i<n-1$ and injective for $i=n-1$. For compatible base points, the inclusion-induced map
$$\pi_i(H)\longrightarrow\pi_i(X)$$
is an isomorphism for $i<n-1$ and surjective for $i=n-1$.
The homology map
$$H_i(H,\mathbb Z)\longrightarrow H_i(X,\mathbb Z)$$
is likewise an isomorphism for $i<n-1$ and surjective for $i=n-1$.
:::

::: {.front card-id="proof-weak-lefschetz-affine-complement" tags="proof"}
Let $H$ be a smooth ample divisor in a smooth complex projective $n$-fold $X$. Prove the integral cohomology form of weak Lefschetz using the topology of $X\setminus H$. State the topological theorem used.
:::

::: {.back card-id="proof-weak-lefschetz-affine-complement"}
Set $U=X\setminus H$. A positive multiple of $H$ is very ample, so $U$ is a smooth affine variety. The Andreotti–Frankel theorem, proved by Morse theory, gives $U$ the homotopy type of a CW complex of real dimension at most $n$. Thus $H_j(U,\mathbb Z)=0$ for $j>n$.

Excision and Poincaré duality give
$$H^k(X,H;\mathbb Z)\cong H_c^k(U,\mathbb Z)\cong H_{2n-k}(U,\mathbb Z)=0\qquad(k<n).$$
In the exact sequence
$$H^k(X,H;\mathbb Z)\longrightarrow H^k(X,\mathbb Z)\longrightarrow H^k(H,\mathbb Z)\longrightarrow H^{k+1}(X,H;\mathbb Z),$$
both outer groups vanish for $k<n-1$, and the left group vanishes for $k=n-1$. Restriction is therefore an isomorphism below degree $n-1$ and injective in degree $n-1$.

Reference: [Popa, topology of algebraic varieties, §1](https://people.math.harvard.edu/~mpopa/571/chapter1.pdf).
:::

::: {.front card-id="application-weak-lefschetz-boundary-cubic" tags="application"}
Let $C\subset\mathbb P^2_{\mathbb C}$ be a smooth plane cubic. Compute the maps induced by inclusion on integral $H^1$, integral $H_1$, and $\pi_1$. What do they show about the boundary degree in weak Lefschetz?
:::

::: {.back card-id="application-weak-lefschetz-boundary-cubic"}
The curve has genus one, while $\mathbb P^2$ is simply connected. The maps are
$$H^1(\mathbb P^2,\mathbb Z)=0\longrightarrow H^1(C,\mathbb Z)\cong\mathbb Z^2,$$
$$H_1(C,\mathbb Z)\cong\mathbb Z^2\longrightarrow H_1(\mathbb P^2,\mathbb Z)=0,$$
$$\pi_1(C)\cong\mathbb Z^2\longrightarrow\pi_1(\mathbb P^2)=1.$$
Here the ambient dimension is $n=2$, so degree one is the boundary degree. Cohomology restriction is injective but not surjective; the homology and fundamental-group maps are surjective but not injective. The degree bounds are sharp even for smooth ample divisors.
:::

::: {.front card-id="application-weak-lefschetz-ampleness" tags="application"}
Let $C$ be a smooth complex projective curve of genus $g\ge1$, let $X=C\times\mathbb P^1$, and set $D=\{p\}\times\mathbb P^1$. Does this smooth divisor satisfy the conclusions of weak Lefschetz? Check ampleness and the maps on $H^1(-,\mathbb Z)$ and $\pi_1$.
:::

::: {.back card-id="application-weak-lefschetz-ampleness"}
The fiber has $D^2=0$, so $D$ is not ample: an ample divisor on a projective surface has positive square. Restriction is
$$H^1(X,\mathbb Z)\cong\mathbb Z^{2g}\longrightarrow H^1(D,\mathbb Z)=0,$$
which is not injective. The map
$$\pi_1(D)=1\longrightarrow\pi_1(X)\cong\pi_1(C)$$
is not surjective. Both conclusions required in boundary degree one fail. Smoothness of the divisor alone is insufficient.
:::

::: {.front card-id="application-weak-lefschetz-complete-intersections" tags="application"}
Let $Y\subset\mathbb P^N_{\mathbb C}$ be a smooth complete intersection of dimension $m\ge2$, and let $h=c_1(\mathcal O_Y(1))$. Determine $\pi_1(Y)$ and $H^k(Y,\mathbb Z)$ for $0\le k<m$. Explain how weak Lefschetz applies repeatedly and what it gives in degree $m$.
:::

::: {.back card-id="application-weak-lefschetz-complete-intersections"}
For general defining equations, the successive intersections are smooth, and each is an ample divisor in the preceding variety. Iterating weak Lefschetz gives
$$\pi_1(Y)=1,\qquad H^k(Y,\mathbb Z)=\begin{cases}\mathbb Z\,h^{k/2}&k\text{ even},\\0&k\text{ odd}\end{cases}\qquad(0\le k<m).$$
For an arbitrary smooth complete intersection of the same multidegree, deform the equations through the connected smooth parameter locus to a general choice. Ehresmann's theorem preserves the topology and the restricted hyperplane class.

In degree $m$, restriction $H^m(\mathbb P^N,\mathbb Z)\to H^m(Y,\mathbb Z)$ is injective; additional middle cohomology can occur.

Reference: [Catanese, Topological methods in moduli theory, Lefschetz theorems](https://link.springer.com/article/10.1007/s13373-015-0070-1).
:::

::: {.front card-id="application-weak-lefschetz-complete-intersection-irregularity" tags="application"}
Let $S\subset\mathbb P^4_{\mathbb C}$ be a smooth complete intersection of a quadric and a cubic, with hyperplane class $h$. Determine $\pi_1(S)$, $H^1(S,\mathbb Z)$, and $q(S)=h^1(S,\mathcal O_S)$ using weak Lefschetz and Hodge decomposition. Does weak Lefschetz also give $H^2(S,\mathbb Z)=\mathbb Z\,h$?
:::

::: {.back card-id="application-weak-lefschetz-complete-intersection-irregularity"}
Since $\dim S=2$, weak Lefschetz for complete intersections gives
$$\pi_1(S)=1,\qquad H^1(S,\mathbb Z)=0.$$
Hodge decomposition gives
$$0=H^1(S,\mathbb C)=H^{1,0}(S)\oplus H^{0,1}(S),$$
so $q(S)=h^{0,1}(S)=0$. In degree two the theorem gives only an injection
$$\mathbb Z\,h=H^2(\mathbb P^4,\mathbb Z)\hookrightarrow H^2(S,\mathbb Z).$$
It does not determine the middle cohomology. In fact, adjunction gives $K_S\cong\mathcal O_S$, so $S$ is a K3 surface and $H^2(S,\mathbb Z)$ has rank $22$.
:::

::: {.front card-id="theorem-ehresmann-monodromy" tags="theorem"}
State Ehresmann's theorem for a proper smooth submersion. What does it imply for a smooth proper family of complex manifolds over a connected complex manifold $S$?
:::

::: {.back card-id="theorem-ehresmann-monodromy"}
A proper smooth submersion is locally trivial as a differentiable fiber bundle. Its fibers are locally diffeomorphic, and the sheaves $R^if_*\mathbb Z$ are local systems. Choosing $s\in S$ gives monodromy representations
$$\pi_1(S,s)\longrightarrow\operatorname{Aut}(H^i(X_s,\mathbb Z)).$$
:::

::: {.front card-id="theorem-picard-lefschetz" tags="theorem"}
For a one-parameter degeneration of complex $n$-folds with a single ordinary double point and vanishing cycle $\delta\in H_n(X_t,\mathbb Z)$, state Picard–Lefschetz monodromy around a positive loop, using the complex-orientation intersection convention. How does parity affect its form?
:::

::: {.back card-id="theorem-picard-lefschetz"}
The monodromy is
$$T(x)=x+(-1)^{(n+1)(n+2)/2}(x\cdot\delta)\delta.$$
For even $n$ it is a reflection. For odd $n$ it is a symplectic transvection, which is the identity if $\delta$ vanishes in global homology.
:::

::: {.front card-id="theorem-decomposition" tags="theorem"}
For a projective morphism $f:X\to Y$ of complex algebraic varieties, state the decomposition theorem with rational coefficients. Describe the supports and local systems, and the Lefschetz consequence for projective varieties.
:::

::: {.back card-id="theorem-decomposition"}
With intersection complexes normalized to be perverse, there is a generally noncanonical decomposition
$$Rf_*\operatorname{IC}_X\simeq\bigoplus_{\alpha,i}\operatorname{IC}_{Z_\alpha}(\mathcal L_{\alpha,i})[-i].$$
Each $Z_\alpha$ is an irreducible closed subvariety of $Y$, and each $\mathcal L_{\alpha,i}$ is a semisimple local system on a smooth dense open subset of $Z_\alpha$. The perverse cohomology sheaves are semisimple. For a complex projective $n$-fold and an ample class $h$, intersection cohomology satisfies
$$h^{n-k}:IH^k(X,\mathbb Q)\xrightarrow{\sim}IH^{2n-k}(X,\mathbb Q)\qquad(0\le k\le n).$$
:::

::: {.front card-id="application-lefschetz-threefold-picard" tags="application"}
Let $X\subset\mathbb P^4_{\mathbb C}$ be a smooth hypersurface of positive degree. Determine $\operatorname{Pic}(X)$ without a very-general hypothesis. Which restriction theorem has the required dimension?
:::

::: {.back card-id="application-lefschetz-threefold-picard"}
The ambient variety has dimension four, and $X$ is a smooth ample divisor. Grothendieck–Lefschetz gives
$$\operatorname{Pic}(\mathbb P^4)\xrightarrow{\sim}\operatorname{Pic}(X).$$
Thus $\operatorname{Pic}(X)=\mathbb Z[\mathcal O_X(1)]$ for every smooth such hypersurface.
:::

::: {.front card-id="application-noether-lefschetz-quartic-line" tags="application"}
Compare the Picard rank of a very general smooth quartic surface $S\subset\mathbb P^3_{\mathbb C}$ with that of a smooth quartic containing a line $\ell$. Which theorem requires “very general,” and how does the line detect failure of rank one?
:::

::: {.back card-id="application-noether-lefschetz-quartic-line"}
Noether–Lefschetz gives rank one for a very general quartic. If $H$ is the hyperplane class and $\ell\subset S$ is a line, then $H^2=4$, $H\ell=1$, and $\ell^2=-2$ by adjunction on the K3 surface. The intersection matrix has determinant $4(-2)-1=-9\ne0$, so $H$ and $\ell$ are independent and $\rho(S)\ge2$. In ambient dimension three, Grothendieck–Lefschetz gives injectivity, not surjectivity, of Picard restriction.
:::

::: {.front card-id="application-hodge-index-orthogonal-isotropic" tags="application"}
Let $S$ be a smooth complex projective surface and $H$ ample. A divisor class $D\in N^1(S)_{\mathbb R}$ satisfies $HD=0$ and $D^2=0$. What can be concluded? Would the same argument prove that a line bundle representing $D$ is trivial?
:::

::: {.back card-id="application-hodge-index-orthogonal-isotropic"}
Hodge index is negative definite on $H^\perp$, so $D=0$ in $N^1(S)_{\mathbb R}$. This proves numerical triviality, not triviality as a line bundle. A nontrivial member of $\operatorname{Pic}^0(S)$ can have zero numerical class.
:::

::: {.front card-id="application-hard-versus-weak-lefschetz" tags="application"}
For a smooth cubic threefold $X\subset\mathbb P^4_{\mathbb C}$ with hyperplane class $h$, determine $H^2(X,\mathbb Q)$ and $H^4(X,\mathbb Q)$. Which theorem gives each, and does either identify $H^3(X,\mathbb Q)$ with that of $\mathbb P^4$?
:::

::: {.back card-id="application-hard-versus-weak-lefschetz"}
Weak Lefschetz gives $H^2(X,\mathbb Q)=\mathbb Qh$. Hard Lefschetz gives the isomorphism $h\cup-:H^2(X,\mathbb Q)\to H^4(X,\mathbb Q)$, so $H^4(X,\mathbb Q)=\mathbb Qh^2$. Weak Lefschetz is only injective in degree three here; neither statement identifies the middle cohomology with the zero group $H^3(\mathbb P^4,\mathbb Q)$.
:::

::: {.front card-id="application-smooth-family-picard-jump" tags="application"}
A smooth family of quartic surfaces has a very general fiber of Picard rank one and a special smooth fiber containing a line. Does the rank jump contradict local topological triviality or constancy of Betti numbers? Explain which structure changes.
:::

::: {.back card-id="application-smooth-family-picard-jump"}
No. Ehresmann gives locally diffeomorphic fibers, so $b_2=22$ remains constant; smooth properness also keeps $h^{1,1}=20$ fixed. The integral cohomology forms a local system, but its Hodge decomposition varies. By Lefschetz $(1,1)$, extra integral classes of type $(1,1)$ become algebraic on the special fiber.

For its hyperplane class $H$ and line $L$, the intersection matrix is $\left(\begin{smallmatrix}4&1\\1&-2\end{smallmatrix}\right)$, with determinant $-9$. Thus $H,L$ are independent and $\rho\ge2$. Picard rank can increase without changing the topological cohomology group or creating a singular fiber.
:::

::: {.front card-id="application-picard-lefschetz-parity" tags="application"}
Compare monodromy around one ordinary double point in a family of complex curves and in a family of complex surfaces. For a nonzero vanishing cycle $\delta$, determine $T(\delta)$ and the form of $T$ using the complex-orientation Picard–Lefschetz convention.
:::

::: {.back card-id="application-picard-lefschetz-parity"}
For curves, the pairing is alternating and $\delta^2=0$, so
$$T(x)=x-(x\cdot\delta)\delta,\qquad T(\delta)=\delta.$$
This is a transvection. For surfaces, $\delta^2=-2$ and
$$T(x)=x+(x\cdot\delta)\delta,\qquad T(\delta)=-\delta.$$
This is the reflection in the vanishing class.
:::

::: {.front card-id="card-2b275615aad39e6c" tags="definition"}
What is the definition of Algebraic class?
:::

::: {.back card-id="card-2b275615aad39e6c"}
A cohomology class in $H^{2k}(X;\mathbb Q)$ that is a $\mathbb Q$-linear combination of fundamental classes $[Z]$ of closed algebraic subvarieties $Z\subset X$ of codimension $k$.
:::

::: {.front card-id="card-f35177676acfe3b2" tags="definition"}
What is the definition of Algebraic representation?
:::

::: {.back card-id="card-f35177676acfe3b2"}
A representation $\rho:G\to\operatorname{GL}(V)$ of an algebraic group that is a morphism of varieties; equivalently a $G$-module whose matrix coefficients are regular functions on $G$.
:::

::: {.front card-id="card-d25f56f728d51c2e" tags="definition"}
What is the definition of Character of a torus?
:::

::: {.back card-id="card-d25f56f728d51c2e"}
A homomorphism $\chi:T\to\mathbb G_m$ of algebraic groups; for $T\cong\mathbb G_m^r$ the characters form the lattice $X^*(T)\cong\mathbb Z^r$, and a representation of $T$ decomposes into weight spaces $V_\chi$.
:::

::: {.front card-id="card-19c7492f4250dc0e" tags="definition"}
What is the definition of Character variety?
:::

::: {.back card-id="card-19c7492f4250dc0e"}
For a finitely presented group $\Gamma$ and complex reductive algebraic group $G$,
$$\mathcal X(\Gamma,G)=\operatorname{Spec}\bigl(\mathbb C[\operatorname{Hom}(\Gamma,G)]^G\bigr)
=\operatorname{Hom}(\Gamma,G)/\!/G.$$
The action is simultaneous conjugation. Closed points correspond to closed orbits; each orbit closure contains a unique closed orbit. For $G=\mathrm{GL}_r$, closed orbits are precisely semisimple representations, and the quotient replaces a representation by its semisimplification. For general reductive $G$, use $G$-complete reducibility: containment in a parabolic implies containment in a Levi subgroup of that parabolic.

The representation scheme records framed representations and can be nonreduced; its reduced scheme is often called the representation variety. Specify whether the scheme structure is retained.
:::

::: {.front card-id="card-47e9f5f5ac4967f4" tags="definition"}
What is the definition of Cocharacter?
:::

::: {.back card-id="card-47e9f5f5ac4967f4"}
A homomorphism $\lambda:\mathbb G_m\to G$ of algebraic groups; for a torus $T$, the cocharacters form $X_*(T)=\operatorname{Hom}(\mathbb G_m,T)$, the dual of the character lattice $X^*(T)$.
:::

::: {.front card-id="card-2cad8725835ecda3" tags="definition"}
What is the definition of Fiber bundle?
:::

::: {.back card-id="card-2cad8725835ecda3"}
A map $p:E\to B$ that is locally trivial: every $b\in B$ has a neighborhood $U$ and a homeomorphism $p^{-1}(U)\cong U\times F$ over $U$, with fiber $F$; a differentiable fiber bundle requires the trivializations to be diffeomorphisms.
:::

::: {.front card-id="card-b9f137da4c23e911" tags="definition"}
What is the definition of Flat connection?
:::

::: {.back card-id="card-b9f137da4c23e911"}
A connection $\nabla$ on a vector bundle $E\to X$ with vanishing curvature $\nabla^2=0$; equivalently a connection whose horizontal sections form a local system $E^\nabla$ with $E\cong\mathcal O_X\otimes_{\mathbb C}E^\nabla$.
:::

::: {.front card-id="card-f63b3fc4a50d2fff" tags="definition"}
What is the definition of Galois representation?
:::

::: {.back card-id="card-f63b3fc4a50d2fff"}
A continuous homomorphism $\rho:G_k\to\operatorname{GL}(V)$ for a Galois group $G_k=\operatorname{Gal}(\overline k/k)$ and a topological vector space $V$ (often $\ell$-adic); continuity uses the profinite topology on $G_k$ and the natural topology on $V$.
:::

::: {.front card-id="card-a9bab3596ebd4a38" tags="definition"}
What is the definition of Griffiths complex structure?
:::

::: {.back card-id="card-a9bab3596ebd4a38"}
On the real vector space underlying a Hodge structure of odd weight $2k-1$, the Griffiths complex structure has $(1,0)$-part the Hodge filtration $F^kV$; it defines the Griffiths intermediate Jacobian $J_G(V)=V/(V_{\mathbb Z}+F^kV)$.
:::

::: {.front card-id="card-c0d7789910359198" tags="definition"}
What is the definition of Hodge decomposition?
:::

::: {.back card-id="card-c0d7789910359198"}
For a compact Kähler manifold $X$, the decomposition $H^k(X;\mathbb C)=\bigoplus_{p+q=k}H^{p,q}(X)$ with $\overline{H^{p,q}}=H^{q,p}$; equivalently the splitting of a pure Hodge structure of weight $k$ into its $(p,q)$ pieces.
:::

::: {.front card-id="card-564f652a26b01565" tags="definition"}
What is the definition of Hodge structure?
:::

::: {.back card-id="card-564f652a26b01565"}
A rational Hodge structure of weight $n$ is a finite-dimensional $\mathbb Q$-vector space $V$ with a decomposition $V_{\mathbb C}=\bigoplus_{p+q=n}V^{p,q}$ satisfying $\overline{V^{p,q}}=V^{q,p}$. Equivalently, a decreasing Hodge filtration $F^\bullet$ on $V_{\mathbb C}$ with $F^p\oplus\overline{F^{n-p+1}}=V_{\mathbb C}$; $H^n(X,\mathbb Q)$ of a smooth projective complex variety carries one.
:::

::: {.front card-id="card-d0c4d9aa2c580577" tags="definition"}
What is the definition of Holomorphic differential operator?
:::

::: {.back card-id="card-d0c4d9aa2c580577"}
A $\mathbb C$-linear endomorphism of $\mathcal O_X$ locally of the form $\sum_{|\alpha|\le m} f_\alpha\partial^\alpha$ with $f_\alpha$ holomorphic; these operators form the sheaf $D_X$.
:::

::: {.front card-id="card-6b2a61a9df86fe75" tags="definition"}
What is the definition of Hyperkähler manifold?
:::

::: {.back card-id="card-6b2a61a9df86fe75"}
A Riemannian manifold $(X,g)$ with $\dim_{\mathbb R}X=4n$ and $\operatorname{Hol}(g)\subseteq\operatorname{Sp}(n)$; equivalently a Kähler manifold carrying a holomorphic symplectic $2$-form $\sigma$ with $\nabla\sigma=0$ and $\sigma^n$ nowhere vanishing.
:::

::: {.front card-id="card-f4991f604dc40dcf" tags="definition"}
What is the definition of Intersection cohomology?
:::

::: {.back card-id="card-f4991f604dc40dcf"}
The cohomology $IH^k(X;\mathbb Q)=H^k(X;IC_X(\mathbb Q))$ of the intersection complex; for a projective variety of dimension $n$ it satisfies Poincaré duality and hard Lefschetz, and it agrees with ordinary cohomology when $X$ is smooth.
:::

::: {.front card-id="card-b91684e8cd33e85f" tags="definition"}
What is the definition of Intersection complex?
:::

::: {.back card-id="card-b91684e8cd33e85f"}
For a local system $L$ on a smooth dense open subset of a variety $X$, the perverse sheaf $IC_X(L)$ obtained by truncating the pushforward $j_*L$ (Deligne's construction); its cohomology computes intersection cohomology with local coefficients.
:::

::: {.front card-id="card-c85bec55230a03d2" tags="definition"}
What is the definition of Irreducible representation?
:::

::: {.back card-id="card-c85bec55230a03d2"}
A nonzero representation $V$ of a group or algebra with no proper nonzero subrepresentation; equivalently $\operatorname{End}_G(V)$ is a division ring, and for algebraically closed fields and finite groups $\operatorname{End}_G(V)=\mathbb C$.
:::

::: {.front card-id="card-92fa2bc76a35c8d0" tags="definition"}
What is the definition of Kähler class?
:::

::: {.back card-id="card-92fa2bc76a35c8d0"}
The de Rham class $[\omega]\in H^{1,1}(X;\mathbb R)$ of a closed positive $(1,1)$-form $\omega$ on a complex manifold; equivalently the class of a Kähler form, so it is represented by a Kähler metric.
:::

::: {.front card-id="card-ae728ba7c6c78ce5" tags="definition"}
What is the definition of L-adic cohomology?
:::

::: {.back card-id="card-ae728ba7c6c78ce5"}
For a scheme $X$ separated of finite type over a field and a prime $\ell$ invertible on $X$, the $\mathbb Q_\ell$-vector spaces $H^i_{\mathrm{\acute et}}(X;\mathbb Q_\ell)=(\varprojlim_n H^i_{\mathrm{\acute et}}(X;\mathbb Z/\ell^n\mathbb Z))\otimes_{\mathbb Z_\ell}\mathbb Q_\ell$.
:::

::: {.front card-id="card-5dd0bc4617067172" tags="definition"}
What is the definition of Lefschetz operator?
:::

::: {.back card-id="card-5dd0bc4617067172"}
For a Kähler class $\omega$ on $X$, the operator $L:H^k(X)\to H^{k+2}(X)$ given by $L(\alpha)=\omega\cup\alpha$; its $\mathfrak{sl}_2$-adjoint is $\Lambda=L^*=\star^{-1}L\star$.
:::

::: {.front card-id="card-324ac9216b75b02e" tags="definition"}
What is the definition of Lowest weight vector?
:::

::: {.back card-id="card-324ac9216b75b02e"}
In an $\mathfrak{sl}_2$-representation, a vector $v$ annihilated by the lowering operator $\Lambda$; for the Lefschetz $\mathfrak{sl}_2$-action generated by $L$ and $\Lambda$, the lowest weight vectors are exactly the primitive cohomology classes.
:::

::: {.front card-id="card-ff783d82021dce75" tags="definition"}
What is the definition of Motivic representation?
:::

::: {.back card-id="card-ff783d82021dce75"}
A representation of a Galois group (or fundamental group) that occurs as a subquotient of the cohomology $H^i(X_{\overline k},\mathbb Q_\ell)$ of a smooth projective variety, hence is of geometric origin.
:::

::: {.front card-id="card-a3c337d2df6608aa" tags="definition"}
What is the definition of Numerical class?
:::

::: {.back card-id="card-a3c337d2df6608aa"}
Two divisors are numerically equivalent if they have the same intersection number with every curve; the numerical class is the image in $N^1(X)=(\operatorname{Div}/\equiv_{\mathrm{num}})\otimes\mathbb R$.
:::

::: {.front card-id="card-d23139a6a987d15e" tags="definition"}
What is the definition of Perverse cohomology?
:::

::: {.back card-id="card-d23139a6a987d15e"}
The cohomology objects ${}^p\mathcal H^i(K)$ of a complex $K$ with respect to the perverse $t$-structure on $D^b_c(X)$; they are perverse sheaves, and the decomposition theorem expresses $Rf_*\mathbb Q$ as a sum of shifts of simple perverse sheaves.
:::

::: {.front card-id="card-4b1d53806881ea83" tags="definition"}
What is the definition of Polarized hodge structure?
:::

::: {.back card-id="card-4b1d53806881ea83"}
A pure Hodge structure $(V,V^{p,q})$ of weight $m$ together with a $(-1)^m$-symmetric bilinear form $Q:V\times V\to\mathbb Q(-m)$ such that $Q(v,\overline w)$ is Hermitian and $i^{p-q}Q(v,\overline v)>0$ for $0\ne v\in V^{p,q}$; equivalently a morphism $V\to V^\vee(-m)$ satisfying Hodge–Riemann positivity.
:::

::: {.front card-id="card-77db280aaada1e82" tags="definition"}
What is the definition of Regular holonomic d-module?
:::

::: {.back card-id="card-77db280aaada1e82"}
A left module $M$ over the sheaf $D_X$ of holomorphic differential operators that is coherent over $D_X$, whose characteristic variety is Lagrangian (holonomic), and whose solutions have regular singularities along that variety (regular).
:::

::: {.front card-id="card-9408d7d0c684ef74" tags="definition"}
What is the definition of Riemann-hilbert correspondence?
:::

::: {.back card-id="card-9408d7d0c684ef74"}
For a smooth complex algebraic variety $X$ of complex dimension $d$, analytify and use the normalized de Rham functor
$$\mathrm{DR}(M)=
[M^{\mathrm{an}}\to\Omega^1_{X^{\mathrm{an}}}\otimes M^{\mathrm{an}}\to\cdots
\to\Omega^d_{X^{\mathrm{an}}}\otimes M^{\mathrm{an}}][d].$$
It gives a covariant equivalence from regular holonomic $D_X$-modules to algebraically constructible perverse sheaves, and a derived equivalence
$$D^b_{\mathrm{rh}}(D_X)\simeq D^b_c(X^{\mathrm{an}},\mathbb C).$$
The normalized solution functor $\mathrm{Sol}(M)=R\mathcal Hom_{D_{X^{\mathrm{an}}}}(M^{\mathrm{an}},\mathcal O_{X^{\mathrm{an}}})[d]$ is contravariant, giving the corresponding anti-equivalences. For a flat bundle with horizontal local system $L$, $\mathrm{DR}(E)=L[d]$ and $\mathrm{Sol}(E)=L^\vee[d]$. On nonproper $X$, the algebraic correspondence requires regularity at infinity.
:::

::: {.front card-id="card-9049bc9b0d97b074" tags="definition"}
What is the definition of Semisimple local system?
:::

::: {.back card-id="card-9049bc9b0d97b074"}
A local system whose associated monodromy representation is semisimple (completely reducible); equivalently a local system that is a direct sum of irreducible local systems.
:::

::: {.front card-id="card-0d1ed9edee3e0517" tags="definition"}
What is the definition of Sl_2-representation?
:::

::: {.back card-id="card-0d1ed9edee3e0517"}
A representation of the Lie algebra $\mathfrak{sl}_2(\mathbb C)=\langle e,f,h\rangle$ with $[h,e]=2e$, $[h,f]=-2f$, and $[e,f]=h$; every finite-dimensional one is a direct sum of symmetric powers $\operatorname{Sym}^n(\mathbb C^2)$.
:::

::: {.front card-id="card-4f2a54667ed3078d" tags="definition"}
What is the definition of Stable higgs bundle?
:::

::: {.back card-id="card-4f2a54667ed3078d"}
On a smooth projective variety of dimension $d$ with ample class $H$, a Higgs bundle $(E,\theta)$ is stable if
$$\mu_H(F)<\mu_H(E),\qquad
\mu_H(F)=\frac{c_1(F)\cdot H^{d-1}}{\operatorname{rk}F}$$
for every coherent $\theta$-invariant subsheaf with $0<\operatorname{rk}F<\operatorname{rk}E$. It suffices to test saturated subsheaves. Semistability uses $\le$; polystability means a direct sum of stable Higgs bundles of the same slope. S-equivalence identifies semistable objects with isomorphic polystable Jordan–Hölder graded objects.

The underlying bundle need not be stable: the test is restricted to $\theta$-invariant subsheaves.
:::

::: {.front card-id="card-59820f784bbd6226" tags="definition"}
What is the definition of Subquotient?
:::

::: {.back card-id="card-59820f784bbd6226"}
An object isomorphic to $A/B$ for a subobject $B$ of a subobject $A$ of a given object; the subquotients of a representation are its constituents and are closed under further subquotients.
:::

::: {.front card-id="card-d41a841dbe205641" tags="definition"}
What is the definition of Symplectic transvection?
:::

::: {.back card-id="card-d41a841dbe205641"}
For a symplectic form $\omega$ and a nonzero vector $v$, the automorphism $T_v(x)=x-\omega(x,v)v$; it is symplectic, fixes $v^\perp$, and satisfies $T_v(v)=v$.
:::

::: {.front card-id="card-bdd7373c2c7eb926" tags="definition"}
What is the definition of Tate hodge structure?
:::

::: {.back card-id="card-bdd7373c2c7eb926"}
The rank-one Hodge structure $\mathbb Z(1)$ of weight $-2$ with lattice $(2\pi i)\mathbb Z\subset\mathbb C$ and type $(-1,-1)$; its $m$-th tensor power $\mathbb Z(m)$ has weight $-2m$ and type $(-m,-m)$.
:::

::: {.front card-id="card-030a0cdb11931b03" tags="definition"}
What is the definition of Transvection?
:::

::: {.back card-id="card-030a0cdb11931b03"}
An automorphism of a vector space with bilinear form $B$ of the form $T(x)=x-\frac{2B(x,v)}{B(v,v)}v$ when $B(v,v)\ne0$, or $T(x)=x-B(x,v)v$ when $B$ is alternating; it fixes the hyperplane $v^\perp$ and shears along $\langle v\rangle$.
:::

::: {.front card-id="card-695648298794f57b" tags="definition"}
What is the definition of Variation of hodge structure?
:::

::: {.back card-id="card-695648298794f57b"}
A local system $\mathbb V$ of finite-dimensional $\mathbb Q$-vector spaces on a smooth variety $S$, with an increasing weight filtration by sub-local systems and a decreasing Hodge filtration $F^p\subset\mathcal O_S\otimes\mathbb V$ by subbundles, such that every fibre is a Hodge structure and $\nabla(F^p)\subset F^{p-1}\otimes\Omega^1_S$ (Griffiths transversality).
:::

::: {.front card-id="card-d76909b4beed0c4e" tags="definition"}
What is the definition of Weight filtration?
:::

::: {.back card-id="card-d76909b4beed0c4e"}
An increasing filtration $W_\bullet$ on a vector space underlying a mixed Hodge structure such that each graded piece $\operatorname{gr}^W_\ell$ carries a pure Hodge structure of weight $\ell$. On the cohomology of a complex variety it is Deligne's weight filtration, with weights recording the compactification and the open complement.
:::

::: {.front card-id="card-c3e44608ecf1b8d3" tags="definition"}
What is the definition of Weil complex structure?
:::

::: {.back card-id="card-c3e44608ecf1b8d3"}
On the real vector space underlying a Hodge structure, the complex structure $C$ acting on $V^{p,q}$ by $i^{p-q}$; it defines the Weil intermediate Jacobian $J_W(V)=V/(V_{\mathbb Z}+V_W^{1,0})$.
:::

::: {.front card-id="card-3d2a91af614ba2fc" tags="definition"}
What is the definition of Weyl algebra?
:::

::: {.back card-id="card-3d2a91af614ba2fc"}
The algebra $W^n=\mathbb C[x_1,\dots,x_n,\partial_1,\dots,\partial_n]$ with relations $[x_i,x_j]=[\partial_i,\partial_j]=0$ and $[\partial_i,x_j]=\delta_{ij}$; it is the ring of global differential operators on $\mathbb A^n$.
:::

::: {.front card-id="card-63fc125ab4cf0770" tags="definition"}
What is the definition of Weyl group?
:::

::: {.back card-id="card-63fc125ab4cf0770"}
The finite reflection group $W$ generated by the reflections in the hyperplanes orthogonal to the roots of a root system $\Phi$; equivalently $W=N(T)/T$ for a maximal torus $T$ in a connected reductive algebraic group. It acts on character lattices and on cohomology such as $H^*(G/B)$.
:::

::: {.front card-id="card-ed88ff202aea0a6a" tags="definition"}
What is the definition of Zariski closure?
:::

::: {.back card-id="card-ed88ff202aea0a6a"}
For a subset $S$ of an algebraic variety $X$, the smallest Zariski-closed subset $\overline S$ containing $S$; equivalently the common zero set of all regular functions on $X$ that vanish on $S$.
:::

::: {.front card-id="nl-locus-hodge-locus" tags="definition comparison"}
Define the Noether–Lefschetz locus for smooth degree-$d$ surfaces in $\mathbb P^3_{\mathbb C}$, $d\ge4$. How is an extra divisor class detected by periods in a smooth family?
:::

::: {.back card-id="nl-locus-hodge-locus"}
In the parameter space $U_d$ of smooth degree-$d$ surfaces, with hyperplane class $H$:
$$\operatorname{NL}_d=\{S\in U_d:\operatorname{Pic}(S)\ne\mathbb ZH\}.$$
The Noether–Lefschetz theorem makes this a proper exceptional locus: the complement contains every very general surface. Here very general means outside a countable union of proper closed algebraic subsets, not necessarily outside a single closed subset.

On a simply connected analytic patch in a smooth family, parallel-transport an integral class $\alpha\in H^2(S,\mathbb Z)$ independent of $H$. Its Hodge locus is where $\alpha$ has type $(1,1)$, equivalently
$$\int_{S_t}\alpha_t\wedge\omega=0\quad\text{for every }\omega\in H^{2,0}(S_t).$$
Lefschetz $(1,1)$ turns this into existence of a line bundle. The union over extra integral classes is the Noether–Lefschetz locus. It detects additional divisor classes, not singular surfaces.
:::
