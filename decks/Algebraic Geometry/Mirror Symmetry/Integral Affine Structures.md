---
title: "Algebraic Geometry::Mirror Symmetry::Integral Affine Structures"
---

::: {.front card-id="ias-visible-roots-mirror-monodromy" tags="construction theorem formula" cite="[@AE22, Theorem 6.19 and §6G; @AEGS25, Proposition 4.5]"}
How do visible cycles on an integral-affine sphere encode roots? State the mirror/monodromy identification and explain how root pairings control singularity collisions.
:::

::: {.back card-id="ias-visible-roots-mirror-monodromy"}
For a Lagrangian torus fibration $\mu:(\widehat X,\omega)\to B$, a visible cycle is a base one-cycle with parallel integral tangent-vector coefficients, balanced at its vertices. The coefficient specifies a circle in each torus fiber; its sweep gives a two-cycle upstairs.

A path between two $I_1$ points carrying the same parallel primitive vanishing direction gives a sphere of square $-2$. Successive paths between three such points give classes $\alpha,\beta$ with
$$\alpha^2=\beta^2=-2,\qquad \alpha\beta=1.$$
Thus their intersection matrix is negative $A_2$.

For generic $B$ with a triangulation into lattice-volume-one triangles, suppose both a type III Kulikov model and a Lagrangian torus fibration have base $B$. The mirror/monodromy theorem identifies a nearby K3 fiber with $\widehat X$ by a diffeomorphism, sending
$$[\text{torus fiber}]\mapsto e,\qquad [\omega]\mapsto\lambda\in(e^\perp/e)_\mathbb R.$$
For the simple visible roots in the Symington construction, the affine separation parameter is $\ell_i=\lambda\alpha_i$. A vanishing pairing puts the symplectic class on a root wall and collapses the corresponding separation.

For two parallel positive $I_1$ monodromies, choose the common basis so that their product is
$$\begin{pmatrix}1&1\\0&1\end{pmatrix}^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}.$$
Their collision is $I_2$. Nonparallel vanishing directions do not justify this conclusion.
:::

::: {.front card-id="ias-realization-polarized-equivariant" tags="theorem construction" cite="[@AET23, Proposition 2.22 and §6; @AE22, Theorem 8.3]"}
What does the realization theorem for a triangulated integral-affine sphere produce? What additional work produces a polarized model with an involution?
:::

::: {.back card-id="ias-realization-polarized-equivariant"}
Let $B\simeq S^2$ have integral-affine singularities obtained by the positive shear constructions for anticanonical pairs, all at vertices of a triangulation into triangles of lattice volume one (Euclidean area $1/2$). There exists a type III K3 degeneration with dual integral-affine complex $B$.

Construction data: realize every vertex star as a pseudofan of an anticanonical pair $(V_i,D_i)$, glue the boundary curves, and choose the gluing so the normal-crossing surface is $d$-semistable. Along a smooth double curve with two triple points,
$$D_{ij}^2|_{V_i}+D_{ji}^2|_{V_j}=-2.$$
For a polarization, specify nef $L_i$ with matching boundary degrees, at least one big, and choose gluing isomorphisms so they form a line bundle and its chosen divisor avoids log canonical centers. Numerical matching alone does not eliminate the period obstruction.

In the nonsymplectic-involution construction, start with an ample class on the mirror K3 and its Symington polygon $P$, double $P$ with opposite orientation, and choose an invariant lattice triangulation containing the equator. Invariant component choices and anti-invariant periods give an equivariant smoothing with the prescribed monodromy. Extend to nef wall classes by the singularity-collision construction.

An order-$m$ refinement multiplies lengths by $m$ and area by $m^2$; geometrically $t=s^m$ gives $\log T'=m\log T$ and $\lambda'=m\lambda$. It clears rational lengths and permits compatible integral subdivisions.
:::

::: {.front card-id="ias-polygon-blowup-contraction-example" tags="application calculation" cite="[@AET23, §2, Symington surgery and internal-blowup dictionary; @AEGS25, §§4 and 6.2, boundary-contraction operation]"}
Start with the toric triangle for $(\mathbb P^2,\mathcal O(2))$ and its three boundary lines. Blow up the two intersections of a smooth conic with one boundary line, away from the corners. Compute the affine surgery data, boundary intersections, and ample model of the strict transform of the conic.
:::

::: {.back card-id="ias-polygon-blowup-contraction-example"}
The polygon is $\operatorname{conv}((0,0),(2,0),(0,2))$, normalized area $4$. Write $H$ for the pullback of a line, $E_1,E_2$ for the exceptional curves. The internal blowups give
$$R'=2H-E_1-E_2,\qquad D'_1=H-E_1-E_2,\quad D'_2=D'_3=H.$$
The last equality is equality of divisor classes. Also
$$K=-3H+E_1+E_2,\quad D'_1+D'_2+D'_3=-K.$$
Each blowup corresponds to a unit Symington surgery on the chosen edge. Two surgeries reduce its affine length $2$ to $0$, reduce normalized area from $4$ to $2$, and add total charge two.

The decisive intersections are
$$R'^2=2,\quad R'D'_1=0,\quad R'D'_2=R'D'_3=2,\quad (D'_1)^2=-1.$$
The basepoint-free conics through the two points define $\operatorname{Bl}_{p_1,p_2}\mathbb P^2\to\mathbb P^1\times\mathbb P^1$, contracting $D'_1$. The ruling classes are $H-E_1$ and $H-E_2$; their sum is $R'$, so the descended polarization is $\mathcal O(1,1)$.

The two remaining boundary curves have class $(1,1)$, self-intersection two, and meet in two points. Their sum is anticanonical. This computes the component and its boundary contraction from the polygon operations; a global Kulikov model additionally requires compatible neighboring components and gluings.
:::

::: {.front card-id="anticanonical-period-torelli" tags="definition theorem application" cite="[@GHK12, Theorem 1.8 and its nef-cone formulation; @AEGS25, Corollary 4.9]"}
Define the period of an oriented rational anticanonical pair. State global Torelli in a form usable to recognize an isomorphism, and explain the ambiguity in realizing a lattice symmetry.
:::

::: {.back card-id="anticanonical-period-torelli"}
Let $Y$ be a smooth projective rational surface and $D\in|-K_Y|$ a nodal rational cycle with ordered components and an orientation. Then
$$D^\perp=\{L\in\operatorname{Pic}(Y):LD_i=0\ \forall i\},\qquad
\phi_Y:D^\perp\to\operatorname{Pic}^0(D)\simeq\mathbb C^\times,\quad L\mapsto L|_D.$$
For two such pairs and an intersection-lattice isomorphism $\mu:\operatorname{Pic}(Y_1)\to\operatorname{Pic}(Y_2)$, there is an isomorphism $f:(Y_2,D_2)\to(Y_1,D_1)$ with $f^*=\mu$ iff

- $\mu[D_{1,i}]=[D_{2,i}]$;
- $\mu(\operatorname{Nef}(Y_1))=\operatorname{Nef}(Y_2)$;
- $\phi_{Y_2}\circ\mu=\phi_{Y_1}$ on $D_1^\perp$.

The possibilities form a torsor under
$$\operatorname{Hom}(N',\mathbb C^\times),\qquad
N'=\operatorname{coker}\bigl[\operatorname{Pic}(Y_1)\to\mathbb Z^{\#D_i},\ L\mapsto(LD_i)_i\bigr].$$
Thus preserving periods and the nef cone realizes a lattice symmetry, but its lift need not be unique. An order-two lattice map does not alone prove that a chosen geometric lift squares to the identity. Reversing the cycle orientation replaces the period by its inverse.
:::

::: {.front card-id="anticanonical-generic-cone-roots" tags="definition comparison application" cite="[@EF21, §§1 and 9]"}
For an anticanonical pair, distinguish the present nef cone, generic ample cone, admissible isometries, and Looijenga roots. How does the period detect internal $(-2)$-curves?
:::

::: {.back card-id="anticanonical-generic-cone-roots"}
Use a marking in a deformation family of rational anticanonical pairs $(Y,D)$, with ordered boundary components. Set $\Lambda=D^\perp\subset H^2(Y,\mathbb Z)$ and let $\mathcal C^+$ be the positive-cone component containing ample classes.

- $\mathcal A_{\rm gen}$ is the ample cone of a very general deformation, transported by the marking. Its closure is taken inside $\mathcal C^+$.
- An admissible isometry fixes every $[D_i]$, preserves $\mathcal C^+$, and preserves $\overline{\mathcal A}_{\rm gen}$. The present nef cone can have additional walls from internal $(-2)$-curves.
- A Looijenga root is $\alpha\in\Lambda$, $\alpha^2=-2$, that becomes the class of an internal smooth rational curve on some deformation. Square $-2$ alone is not this geometric condition.

The period $\phi_Y(L)=L|_D\in\operatorname{Pic}^0(D)\simeq\mathbb C^\times$ of an internal curve class is $1$: its divisor is disjoint from $D$. Root hyperplanes in period coordinates are therefore $\phi_Y(\alpha)=1$. On these loci the nef chamber determines which signs and simple roots are effective; a root need not be an irreducible curve on the present surface.

Negative-definite configurations of internal $(-2)$-curves contract to ADE singularities, with Dynkin diagram given by their intersections. This connects lattice roots, periods, cone walls, and actual surface contractions.
:::

::: {.front card-id="anticanonical-open-monodromy" tags="definition formula application" cite="[@EF21, §§0 and 3]"}
For a Type III degeneration of negative-definite rational anticanonical pairs, where does nontrivial monodromy live? Define its invariant and describe base change.
:::

::: {.back card-id="anticanonical-open-monodromy"}
For a smooth fiber $(Y,D)$, put $\Lambda=D^\perp$. There is an exact sequence
$$0\to\mathbb Z\gamma\to H_2(Y\setminus D,\mathbb Z)\to\Lambda\to0,$$
where $\mathbb Z\gamma$ is the radical of the intersection pairing. The induced pairing with $\Lambda$ gives
$$T(x)=x-\langle\lambda,x\rangle\gamma,\qquad \lambda\in\Lambda.$$
Although $T|_{H_2(Y,\mathbb Z)}=\mathrm{id}$, one can have $T|_{H_2(Y\setminus D,\mathbb Z)}\ne\mathrm{id}$.

Choose the sign so that
$$\lambda\in B_{\rm gen}:=\operatorname{Int}_{\Lambda_{\mathbb R}}
(\overline{\mathcal A}_{\rm gen}\cap\Lambda_{\mathbb R}).$$
The invariant is the orbit of $\lambda$ under admissible isometries, with
$$\lambda^2=\#\{\text{triple points in the Type III central fiber}\}.$$
Base change $t=s^m$: $(T,\lambda)\mapsto(T^m,m\lambda)$. Hence $\mathbb Q_{>0}\lambda$, modulo admissible isometries, is unchanged. Do not infer trivial degeneration from trivial monodromy on the compact surface alone.
:::

::: {.front card-id="degeneration-elementary-modifications" tags="construction comparison" cite="[@EF21, §4; @AE23, §7]"}
Compare Type 0, I, and II modifications of a Type III normal-crossing surface degeneration. Where is the flopped curve, and how do the components change?
:::

::: {.back card-id="degeneration-elementary-modifications"}
For a flop in the smooth total space, centered on $C$ in the central fiber:

| Modification | Position of $C$ | Effect on components |
| --- | --- | --- |
| Type 0 | Internal $(-2)$-curve, disjoint from the double locus, not deforming to the general fiber | Central fiber's isomorphism type is unchanged; its marking can change |
| Type I | $(-1)$-curve on one component, meeting a double curve once transversely | Blow it down there; blow up its meeting point on the neighboring component |
| Type II | Double curve with self-intersection $-1$ on both adjacent components | Blow it down on both; blow up the two triple points on the opposite components |

Type I transfers an **internal** blowup. Type II transfers **corner** blowups and changes the diagonal of the corresponding quadrilateral in the dual triangulation. The operation preserves the general fiber. These modification labels describe birational operations; they are not the Kulikov Types I, II, and III.
:::

::: {.front card-id="ias-toric-model-corner-equivalence" tags="definition construction example" cite="[@AET23, §2]"}
Define a toric model of an anticanonical pair and corner-blowup equivalence. Distinguish internal and corner blowups in this construction.
:::

::: {.back card-id="ias-toric-model-corner-equivalence"}
For a rational anticanonical pair $(V,D)$, a toric model is a diagram
$$ (V,D)\longleftarrow(V',D')\longrightarrow(\overline V,\overline D)$$
where the first map is a sequence of corner blowups and the second is a sequence of blowdowns inverse to internal blowups; $(\overline V,\overline D)$ is a smooth toric surface with its full boundary.

- Corner blowup: blow up a node of $D$, include the exceptional curve in the new boundary.
- Internal blowup: blow up a smooth point of $D$, use only its strict transform as boundary.
- Corner-blowup equivalent: connected by corner blowups and their inverses.

Both preserve the anticanonical condition. Corner blowups refine the pseudofan without changing its singularity; an internal blowup changes the singularity and increases charge by one.

Example: start with the coordinate triangle in $\mathbb P^2$. Blowing up a vertex is toric; blowing up a nonvertex boundary point is an internal blowup.
:::

::: {.front card-id="ias-divisor-balancing-polarization" tags="definition comparison application" cite="[@AET23, Definitions 2.30–2.36]"}
Define an integral-affine divisor on an integral-affine sphere. State the extra data at singular vertices, balancing, and polarization.
:::

::: {.back card-id="ias-divisor-balancing-polarization"}
An integral-affine divisor consists of:

1. A graph of straight edges $e_{ij}$ with integer weights $n_{ij}=n_{ji}$.
2. At every vertex, an anticanonical pair $(V_i,D_i)$ whose pseudofan models the germ and includes the edge rays, and a line bundle $L_i$ with
$$L_iD_{ij}=n_{ij},\qquad L_iD=0\ \text{on other boundary components}.$$

At a nonsingular vertex, the primitive outgoing directions satisfy
$$\sum_jn_{ij}v_{ij}=0.$$
At singular vertices, this ordinary vector equation does not replace the line-bundle data. At a single $I_1$ singularity with invariant primitive direction $v$, the corresponding condition is $\sum_jn_{ij}v_{ij}\in\mathbb Zv$.

Effective means $n_{ij}\ge0$. Polarizing means every $L_i$ nef and $\sum_iL_i^2>0$; the sum is the self-intersection. Compatible with a triangulation means every graph edge is a union of triangulation edges.

Example: the three unit-weight directions $(1,0),(0,1),(-1,-1)$ balance; they represent $\mathcal O_{\mathbb P^2}(1)$ on the toric vertex model.
:::

::: {.front card-id="ias-nodal-slide-symington" tags="definition construction comparison" cite="[@AET23, Definitions 2.27 and 2.38]"}
Distinguish a nodal slide from Symington surgery on an almost-toric base. State the cut-and-glue operation.
:::

::: {.back card-id="ias-nodal-slide-symington"}
An $I_1$ affine singularity has monodromy conjugate to $\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$ and an invariant direction.

- **Nodal slide:** move the endpoint of its shear cut along the invariant eigenline; the affine structure outside the swept segment stays unchanged. From a multiple singularity, moving one shear ray splits off an $I_1$ point.
- **Symington surgery:** remove a triangle with base of lattice length $a$ on a boundary edge and primitive height $a$, then identify its two remaining sides by the integral shear fixing the apex and matching their primitive tangent vectors. The apex becomes an $I_1$ singularity.

In coordinates, remove the triangle with vertices $(0,0),(a,0),(0,a)$; the affine shear $(x,y)\mapsto(x+y-a,y)$ fixes $(0,a)$ and maps $(a,0)$ to $(0,0)$, identifying the two nonbase sides. The boundary shortens by $a$. This models a symplectic blowup of size $a$ at a smooth point of an anticanonical boundary component; the normalized area drops by $a^2$.
:::



::: {.front card-id="card-1e60c609baa1e7af"}
What is an **anticanonical pair**?
:::

::: {.back card-id="card-1e60c609baa1e7af"}
A pair $(Y, D)$ where $Y$ is a smooth projective rational surface and $D = \sum D_i\in|-K_Y|$ is a reduced cycle of rational curves. Include an irreducible nodal rational curve and two smooth rational curves meeting transversely twice. More broadly, “anticanonical pair” only specifies a surface with an effective anticanonical divisor; the rational-cycle convention is the one used here.

Example: the coordinate triangle in $\mathbb P^2$ is anticanonical because its class is $3H=-K_{\mathbb P^2}$. A cycle alone is not enough: the three strict transforms after blowing up a vertex have class $3H-2E$, whereas $-K=3H-E$; include $E$ to obtain the corner-blown-up anticanonical boundary.
:::

::: {.front card-id="card-8f58666bb53a9709"}
What is a negative definite pair?
:::

::: {.back card-id="card-8f58666bb53a9709"}
An ACP where $M_{ij} \coloneqq D_i \cdot D_j$ is negative definite, i.e. ${\left\langle {z},~{Mz} \right\rangle} < 0$ for all $z \in {\mathbf{R}}^n\setminus\left\{{0}\right\}$.
:::

::: {.front card-id="card-f64cc783f07e304d"}
What is a **toric pair**?
:::

::: {.back card-id="card-f64cc783f07e304d"}
An ACP $(Y, D)$ where $Y$ is a toric variety and $D$ is its toric boundary.
:::

::: {.front card-id="card-89fdc8b480c546ee"}
What is the hyperbolic Inoue surface?
:::

::: {.back card-id="card-89fdc8b480c546ee"}
From type $\rm{VII}_0$ in the classification of complex analytic surfaces, those $V$ with Betti number $b_1 = 1$ and Kodaira dimension $\kappa = -\infty$. Every curve $C_i$ in $X$ is a component of one of two cycles $D$ or $\widehat{D}$ where $D+\widehat{D} \in {\left\lvert {-K_X} \right\rvert}$. Blow $D$ and $\widehat{D}$ down to get $\overline{V}$ with two dual cusps $p, \widehat{p}$, tracked by the germ $(\overline{V}, p, \widehat{p}$).
:::

::: {.front card-id="card-aa75df981fa1d916"}
Discuss the **dual divisors** $D$ and $\widehat{D}$.
:::

::: {.back card-id="card-aa75df981fa1d916"}
For a cusp germ $(\overline V,p)$, the minimal resolution has a negative-definite rational cycle $D$. With at least three components, adjacent components meet transversely once; a two-component cycle has two intersections, and a one-component cycle is an irreducible nodal rational curve.

The cyclic weight data are $\mathbf d=[d_1,\ldots,d_n]$, with $d_i=-D_i^2$ for $n>1$ and $d_1=2-D_1^2$ for $n=1$. The hyperbolic Inoue surface has two cycles $D,\widehat D$ which contract to dual cusps $p,\widehat p$. This is the duality encoded by the cyclic weight-block formula.
:::

::: {.front card-id="card-e1f9c6c06a356657"}
What is **Looijenga's conjecture**?
:::

::: {.back card-id="card-e1f9c6c06a356657"}
Known: If $\widehat{D}$ contracts to a smoothable cusp singularity $\widehat{p}$, then $D$ is the anticanonical divisor of some rational surface. Conjecture: the converse, i.e. if $D$ is the anticanonical divisor of some rational surface, then the cusp singularity associated to $\widehat{D}$ is smoothable.
:::

::: {.front card-id="card-428498c896e7e4e6"}
Why is the converse to Looijenga's conjecture true?
:::

::: {.back card-id="card-428498c896e7e4e6"}
Statement: If $\widehat{D}$ contracts to a smoothable cusp singularity $\widehat{p}$, then $D$ is the anticanonical divisor for some rational surface. Suppose $\widehat{p}$ is smoothable, then Looijenga shows $\overline{V}$ has a universal deformation which is semi-universal for the germ $(\overline{V}, p, \widehat{p})$, so one gets a deformation $\pi: \mcv\to \mathbb{D}$ with $\mcv_0 = \overline{V}$ where $(\overline{V}, p)$ is constant and $(\overline{V}, \widehat{p})$ is smoothed. The general fiber $\mcv_t$ is a surface with a cusp singularity $p_t$ (basically $p$); simultaneously smooth all $p_t$ to get $\mcy\to \mathbb{D}$ where $\mcy_t$ is smooth and $\mcy_0$ is a partially contracted $V$ with a cusp $\widehat{p}$. The general fibers $\mcy_t$ are the desired rational surfaces with anticanonical divisor $D$.
:::

::: {.front card-id="card-20dcddff332cb1eb"}
What is a **pseudofan**?
:::

::: {.back card-id="card-20dcddff332cb1eb"}
For $(V,D)$ an anticanonical pair, the underlying triangulated surface is $\operatorname{Cone}(\Gamma(D))$. Make each sector a standard integral-affine basis triangle. Across the ray for $D_i$, glue by
$$v_{i-1}+v_{i+1}=d_i v_i,\qquad d_i=-D_i^2.$$
Here the $v_i$ are the primitive ray vectors in the successive local charts; they need not lie in a single global chart. For an irreducible nodal boundary use $d_1=2-D_1^2$; for a two-component cycle retain both edges of its dual graph. The apex may have affine monodromy. The boundary intersection data determine the affine structure, not merely the cone's topology.
:::

::: {.front card-id="card-f270c4dc468b873e"}
What are the two main **surgeries** on pseudofans?
:::

::: {.back card-id="card-f270c4dc468b873e"}
Internal blowups and node smoothing.

An internal blowup inserts an interior exceptional curve and changes one boundary self-intersection $D_i^2\mapsto D_i^2-1$. Smoothing the unique intersection between adjacent components replaces them by one with self-intersection $D_i^2+D_{i+1}^2+2$. For a two-component cycle, the components meet twice: smoothing one node gives an irreducible nodal boundary of square $D_1^2+D_2^2+4$.
:::

::: {.front card-id="card-a45da020a729aa8b"}
What is an **almost toric fibration**?
:::

::: {.back card-id="card-a45da020a729aa8b"}
A Lagrangian fibration $\mu:(X^4,\omega)\to S$ with regular fiber $T^2$ and only elliptic and focus-focus singularities.

- Along a boundary edge, one circle collapses; at an elliptic corner, both collapse.
- At an interior simple focus-focus value, a primitive circle in $T^2$ collapses. The fiber is a pinched torus, topologically $S^2$ with two points identified.
- The regular base has an integral-affine structure. A simple focus-focus point has monodromy conjugate to $\begin{pmatrix}1&1\\0&1\end{pmatrix}$.

For the rational anticanonical-pair fibrations used here, $\mu^{-1}(\partial S)$ is the anticanonical boundary. Boundary collapse and interior focus-focus points are different singular strata.
:::

::: {.front card-id="card-f4f2a1127c580098"}
Discuss almost toric fibrations over a disc.
:::

::: {.back card-id="card-f4f2a1127c580098"}
Represented by $\mu: (Y, D, \omega)\to S$ a symplectic anticanonical pair where components of $D$ map to ${{\partial}}S$. Doing internal blowups on a boundary component $P_i\subseteq {{\partial}}S$ corresponds to an internal blowup on $D_i$ in $Y$, similarly for node smoothing.
:::

::: {.front card-id="card-36d6504007dcd5d9"}
What is a **stratified space**?
:::

::: {.back card-id="card-36d6504007dcd5d9"}
A topological space $B$ with a filtration $\emptyset = B_{-1} \subseteq B_0 \subseteq \cdots$ where each $B_k$ is closed and the sections $S_d(B) \coloneqq B_d\setminus B_{d-1}$ are smooth $d\dash$dimensional manifolds and $B = \bigcup_{d\geq 0} B_d$. Say $B$ is dimension $n$ if $n$ is maximal such that $S_n(B) \neq \emptyset$, in which case $S_n(B)$ is the **top stratum**.
:::

::: {.front card-id="card-f7d3c07e867f37fd"}
What is a **Lagrangian torus fibration**?
:::

::: {.back card-id="card-f7d3c07e867f37fd"}
A fibration $f: (X^{2n}, \omega) \to B$ which is a proper continuous map where $B$ is an $n\dash$dimensional stratified space and $f$ is a smooth submersion over the top stratum of $B$ with connected Lagrangian fibers, where the remaining fibers are connected stratified spaces with isotropic strata.
:::

::: {.front card-id="card-bc08b869a67e268a"}
What is an order $k$ **refinement** of an IAS?
:::

::: {.back card-id="card-bc08b869a67e268a"}
For $S$ an IAS, the new IAS $S[k]$ gotten by post-composing the charts on $S$ with multiplication by $k$.
:::

::: {.front card-id="card-f5f851cb3bb46914"}
What is a **corner blowup**?
:::

::: {.back card-id="card-f5f851cb3bb46914"}
For $(Y, D)$ an ACP, a blowup at a node of $D$. Yields anticanonical $\pi^* D - E$
:::

::: {.front card-id="card-7cb45956de5022ad"}
What is an internal blowup?
:::

::: {.back card-id="card-7cb45956de5022ad"}
For $(Y,D)$ an anticanonical pair, blow up a **smooth point** $p\in D$. The new boundary is the strict transform
$$D'=\pi^*D-E,\qquad K_{Y'}+D'=\pi^*(K_Y+D)=0.$$
The exceptional $(-1)$-curve is internal: it is not a boundary component. The affected component has $D_i'^2=D_i^2-1$ and charge increases by one.

At a node of $D$, a corner blowup instead includes $E$ in the new boundary; its charge is unchanged.
:::

::: {.front card-id="card-fdc3053e059f5adb"}
How do IAS surgeries affect **charge**?
:::

::: {.back card-id="card-fdc3053e059f5adb"}
**Internal blowup** on $D_i: d_i\mapsto d_{i} + 1$, no other changes. $Q(D) \mapsto Q(D) + 1$. **$+1$ charge**.

**Corner blowup** on $D_i \cap D_{i+1}$: $(\cdots, d_i, d_{i+1},\cdots)\mapsto (\cdots, d_i+1, 1, d_{i+1} +1,\cdots)$ and $Q(D) \mapsto Q(D)$ **$+0$ charge**.

**Node smoothing** on $D_{i} \cap D_{i+1}$: $(\cdots, d_i, d_{i+1}, \cdots)\mapsto (\cdots, d_{i} + d_{i+1} - 2,\cdots)$. **$+1$ charge.**
:::

::: {.front card-id="card-d49137a8cee771d1"}
What is a **type III anticanonical pair** $(\mcx_0, D)$?
:::

::: {.back card-id="card-d49137a8cee771d1"}
A surface $\mcx_0$ with a decomposition $\mcx_0 = \bigcup_{i=0}^n V_i$ such that...

**Central HIS and normality**: $V_0$ is the hyperbolic Inoue surface with cycles $D, \widehat{D}$ and for $i > 0$ the normalizations $\tilde V_i\to V_i$ are smooth rational surfaces.

**ACP Double Curves**: For $D_{ij}$ an irreducible double curve of $\mcx_0$ lying on $V_{i} \cap V_j$, let $D_i$ be the union of the double curves $D_{ij}$ contained in $V_i$ and let $\tilde D_i$ be its inverse image under normalization; then require $(\tilde V_i, \tilde D_i)$ to be an ACP.

**Triple point formula**: For $D_{ij}$ a double curve joining $V_i$ and $V_j$, then
$$\qty{{ \left.{{D_{ij}}} \right|_{{\tilde V_i}} }}^2 + \qty{{ \left.{{D_{ij}}} \right|_{{\tilde V_j}} }}^2 = \begin{cases}-2 & D_{ij} \text{ smooth} \\0 & D_{ij} \text{ nodal} \end{cases}$$
The dual complex $\Gamma(\mcx_0)$ is a triangulation of $S^2$.
:::

::: {.front card-id="card-726a9d643dacbb85"}
What is **$d\dash$semistability**?
:::

::: {.back card-id="card-726a9d643dacbb85"}
For a normal-crossing central fiber $\mathcal X_0$ with singular locus $D$:
$$\mathcal T^1_{\mathcal X_0}:=\mathcal Ext^1_{\mathcal O_{\mathcal X_0}}(\Omega^1_{\mathcal X_0},\mathcal O_{\mathcal X_0})\simeq\mathcal O_D.$$
This is an isomorphism of sheaves on the double locus, not an unindexed global Ext group. With two smooth components and no triple locus, it means $N_{D/Y_1}\otimes N_{D/Y_2}\simeq\mathcal O_D$. A semistable smoothing with smooth total space supplies this trivialization; the condition alone does not prove global smoothability.
:::

::: {.front card-id="card-34641c38d14db4fa"}
What is the **Friedman-Miranda criterion**?
:::

::: {.back card-id="card-34641c38d14db4fa"}
The cusp singularity associated to $\widehat{D}$ is smoothable iff there exists a type III ACP $(\mcx_0, D)$.
:::

::: {.front card-id="card-eeb1f10b7050ade0"}
What is the **dual complex** of a type III anticanonical pair?
:::

::: {.back card-id="card-eeb1f10b7050ade0"}
For $(\mcx_0, D)$ an ACP, the triangulation of $S^2$ with vertices are the components of $V_i$, directed edges $e_{ij}$ for double curves $D_{ij}$, triangular faces are triple points $T_{ijk}$.
:::

::: {.front card-id="card-eb930237132be4b8"}
What is a **degeneration**?
:::

::: {.back card-id="card-eb930237132be4b8"}
A degeneration of $X$: a flat proper morphism $\pi:\mathcal X\to\Delta$ of complex analytic spaces, smooth over $\Delta^*$, with general fibers deformation equivalent to $X$. The central fiber may be singular.

Semistability and unipotent monodromy are additional conditions. For a geometric polarized variation, monodromy is quasi-unipotent; a finite base change makes it unipotent. Finite monodromy becomes trivial after such a base change. A degeneration need not have nonzero $N=\log T$.
:::

::: {.front card-id="card-701904cdad9a4b3c"}
What is a **maximally unipotent degeneration**?
:::

::: {.back card-id="card-701904cdad9a4b3c"}
Unipotent: $T-I$ is nilpotent; for an $r\times r$ matrix the characteristic polynomial is $(t-1)^r$. Its unipotency index is the least $s$ with $(T-I)^s=0$.

For a polarized variation of weight $n$ arising from a smooth projective degeneration, after unipotent base change $(T-I)^{n+1}=0$. **Maximally unipotent** on $H^n$ means
$$(T-I)^n\ne0,\qquad (T-I)^{n+1}=0,$$
equivalently $N^n\ne0$, $N^{n+1}=0$ for $N=\log T$.

For K3 surfaces, this is Type III; the limiting mixed Hodge structure is then Hodge–Tate. Hodge–Tate is a statement about the Hodge structures on all weight-graded pieces, not a general synonym for maximal nilpotency.
:::

::: {.front card-id="card-2392e89f2c4ead0e"}
What is a basis triangle?
:::

::: {.back card-id="card-2392e89f2c4ead0e"}
A triangle $\Delta \subseteq {\mathbf{R}}^2$ such that $\mathrm{Vert}(\Delta) \subset \ZZ^2$ and $\mu(\Delta) = 1/2$.
:::

::: {.front card-id="card-9247748d2ed4dab9"}
What is a **triangulated integral affine structure with singularities**?
:::

::: {.back card-id="card-9247748d2ed4dab9"}
A real surface with boundary (possibly empty) $\Sigma_g$ equipped with a triangulation $T$ such that $\Sigma_g\setminus\mathrm{Vert}(T)$ admits an atlas $\left\{{(U_i, \phi_i: U_i\to {\mathbf{R}}^2)}\right\}$ such that $\phi_i \circ \phi_j^{-1}\in \SL_2(\ZZ)\rtimes\ZZ^2$ and for each triangle $\Delta \in T$, the interior $\Delta^\circ$ admits a chart to a *basis triangle*.
:::

::: {.front card-id="card-8e3344790c13a342"}
What is a **nodal trade**?
:::

::: {.back card-id="card-8e3344790c13a342"}
Alternative terminology for node smoothing.
:::

::: {.front card-id="card-4110e677dd492db8"}
What is the **SYZ conjecture**?
:::

::: {.back card-id="card-4110e677dd492db8"}
Gross, 2008: If $X, X {}^{ \vee }$ are mirror CYs, they admit a common cospanning fibration $X\to B \leftarrow X {}^{ \vee }$ whose fibers are special Lagrangians and the general fiber is a torus. There should also be a canonical map $X {}^{ \vee }_t { \, \xrightarrow{\sim}\, }H^1(X_t; {\mathbf{R}}/\ZZ)$ and $X_t { \, \xrightarrow{\sim}\, }H^1(X {}^{ \vee }_t; {\mathbf{R}}/\ZZ)$ (likely too strong to be true)
:::

::: {.front card-id="card-23688564458dd17f"}
What is the relation to **SYZ mirror symmetry**?
:::

::: {.back card-id="card-23688564458dd17f"}
Generally about boundaries in a CY moduli space, particularly near especially "bad" degenerations: maximally unipotent degenerations (MUD) or large complex structure limits. One can find special Lagrangian tori on CYs near these limit points, and approaching the limit, expect to see a larger portion of the CY filled by tori. Toric degenerations are a special case of MUD. Expect the base $B$ of a special Lagrangian fibration to be the Gromov-Hausdorff limit of a sequence of CYs near MUD, and GH limit should be the dual intersection complex of the AG degeneration. The base is an affine manifold. If $\pi:\mcx\to \mathbb{D}$ is such a degeneration of CYs and $\mcx$ is polarized (equipped with $\mcl\in \operatorname{Pic}(\mcx)$ relatively ample), should exists a dual polarization $\widehat{\mcl}$ on $\widehat{\mcx}$.
:::

::: {.front card-id="card-b3a5d5b512719741"}
What is **charge**?
:::

::: {.back card-id="card-b3a5d5b512719741"}
$Q(Y,D)=12+\sum_{i=1}^n(d_i-3)$, where $d_i=-D_i^2$ for $n>1$ and $d_1=2-D_1^2$ for an irreducible nodal boundary.

When $\mathbf d=(a_1+3,\underbrace{2,\ldots,2}_{b_1},\ldots,a_k+3,\underbrace{2,\ldots,2}_{b_k})$ with $a_i,b_i\ge0$, this becomes $Q=12+\sum_{i=1}^k(a_i-b_i)$. For a rational anticanonical pair, $Q=e(Y\setminus D)$. All toric pairs have charge zero.
:::

::: {.front card-id="card-0d5e3770ce1f2ca9"}
How can one obtain $\widehat{ \mathbf d}$ for $\widehat{D}$ from $\mathbf d$?
:::

::: {.back card-id="card-0d5e3770ce1f2ca9"}
Interchange the $a_i$ and $b_i$: $\widehat{\mathbf{d}}=\left(\widehat{d_1},\cdots, \widehat{d_s} \right)=(b_1+3, \underbrace{2, \ldots, 2}_{a_1}, \ldots, b_k+3, \underbrace{2, \ldots, 2}_{a_k})$
:::

::: {.front card-id="card-e2d5b7767b890517"}
Discuss $Q(D)$ and $Q(\widehat{D})$.
:::

::: {.back card-id="card-e2d5b7767b890517"}
$Q(D) \coloneqq 12 + \sum (d_i - 3)$ and $Q(D) + Q(\widehat{D}) = 24$. This follows from the formula $Q(D) = 12 + \sum(a_i - b_i)$ and that $\widehat{D}$ swaps $a_i$ and $b_i$.
:::

::: {.front card-id="card-2985fd69293c1543"}
Discuss **conservation of charge**.
:::

::: {.back card-id="card-2985fd69293c1543"}
For $(\mcx_0, D)$ a Type III ACP, $\sum Q(V_i, D_i) = 24$.
:::

::: {.front card-id="card-4498d8364f0200a3"}
What is a **nonsingular IAS**?
:::

::: {.back card-id="card-4498d8364f0200a3"}
When the atlas of charts on an IAS for $S\setminus\mathrm{Vert}(T)$ extends to $S$; if not, denote the points where this fails as $S^\sing$.
:::

::: {.front card-id="card-974cd49e9a49cf40"}
What is the **developing map**?
:::

::: {.back card-id="card-974cd49e9a49cf40"}
For $S$ an IAS with singularities, take contractible opens $U \subset S\setminus S^\sing$ with charts $\phi_U: U\to {\mathbf{R}}^2$, uniquely defined up to an element of $\SL_2(\ZZ)\rtimes\ZZ^2$, and define $\Phi: \widetilde{S\setminus S^\sing} \to {\mathbf{R}}^2$ from the universal cover by gluing any charts $\phi_U, \phi_V$ which agree on $U\cap V$. Equivalent to the data of a monodromy representation $\pi_1(S\setminus S^\sing) \to \SL_2(\ZZ) \rtimes\ZZ^2$.
:::

::: {.front card-id="card-3c8695ea7ecde08d"}
How are ACPs related to toric pairs?
:::

::: {.back card-id="card-3c8695ea7ecde08d"}
Every ACP $(Y, D)$ is a sequence of node smoothings and internal blowups of a toric pair $(\overline{Y}, \overline{D})$.
:::

::: {.front card-id="card-bfda170c1a6d2203"}
What is the negative self-intersection of an edge in an IAS?
:::

::: {.back card-id="card-bfda170c1a6d2203"}
For $e_{ik}$ an edge in $\Delta \subset T$ for an IAS, letting $e_{ij}, e_{il}$ be the edges emanating from $v_i$ clockwise and counterclockwise to $e_{ik}$, define $d_{ik}$ to be the "negative self intersection" of $e_{ik}$ by
$$d_{ik} e_{ik} = e_{ij} + e_{il}$$
The data of $d_{ik}$ for each edge $e_{ik}$ satisfying $d_{ik} + d_{ki} = 2$ for each $i, k$ uniquely determines a triangulated IAS.
:::

::: {.front card-id="card-ad1873dac9f9941a"}
When does a surface $\mcx_0$ smooth to an anticanonical pair in a family $\mcx\to \mathbb{D}$?
:::

::: {.back card-id="card-ad1873dac9f9941a"}
Being a Type III ACP $(\mcx_0, D)$ plus $d\dash$semistability.
:::

::: {.front card-id="card-de8cda450126374b"}
Motivation: singularities.
:::

::: {.back card-id="card-de8cda450126374b"}
- Examples:
- Blowups:
:::


::: {.front card-id="card-c354b1c7c752e729" tags="definition"}
What is the definition of Affine manifold?
:::

::: {.back card-id="card-c354b1c7c752e729"}
An affine manifold is a smooth manifold $B$ with an atlas $\{(U_i,\phi_i)\}$ whose transition maps $\phi_i\circ\phi_j^{-1}$ are affine transformations of $\mathbb R^n$; equivalently $B$ carries a flat torsion-free connection. It is integral when the linear parts lie in $\mathrm{GL}_n(\mathbb Z)$; translations may be real. Integral translations additionally specify an integral-vertex structure.
:::

::: {.front card-id="card-b1cc21ccaddb6e46" tags="definition"}
What is the definition of Almost toric base?
:::

::: {.back card-id="card-b1cc21ccaddb6e46"}
The stratified base $S$ of an almost toric fibration, with an integral-affine structure on its regular locus, boundary collapse data, and interior focus-focus values. A boundary edge has circle fibers, a corner has a point fiber, and a regular interior point has a torus fiber. Interior affine singularities record focus-focus monodromy; they do not record all singular fibers, since boundary fibers also degenerate.
:::

::: {.front card-id="card-92769a4b13586c9a" tags="definition"}
What is the definition of Cycle of rational curves?
:::

::: {.back card-id="card-92769a4b13586c9a"}
A reduced connected nodal divisor of arithmetic genus one whose normalized components are rational. For $n\ge3$, its smooth rational components meet transversely in a cycle, with no other intersections. For $n=2$, the components meet at two distinct points; for $n=1$, it is an irreducible nodal rational curve.

Cusp resolutions have such cycles with negative-definite intersection matrix. The cycle condition alone does not imply contractibility: the three coordinate lines in $\mathbb P^2$ form a cycle with positive-square components.
:::

::: {.front card-id="card-e5ac4665a3c590e7" tags="definition"}
What is the definition of Deformation equivalent?
:::

::: {.back card-id="card-e5ac4665a3c590e7"}
Two compact complex varieties $X$ and $Y$ are deformation equivalent if they are fibers of the same proper smooth family $\mathcal X\to S$ over a connected base $S$; equivalently they are joined by a chain of deformations.
:::

::: {.front card-id="card-7ec42e54742410f3" tags="definition"}
What is the definition of Double curve?
:::

::: {.back card-id="card-7ec42e54742410f3"}
In a reducible surface $X_0=\bigcup_i V_i$, a double curve is an irreducible curve $D_{ij}\subset V_i\cap V_j$ along which two irreducible components $V_i$ and $V_j$ meet. Locally $X_0$ is $xy=0$ times a curve, and the normalization separates the two branches.
:::

::: {.front card-id="card-5fa52bc6d9e5d4e3" tags="definition"}
What is the definition of Dual cusp?
:::

::: {.back card-id="card-5fa52bc6d9e5d4e3"}
For a cusp singularity with cycle $D$ and self-intersection data $\mathbf d=(d_1,\dots,d_n)$, the dual cusp is the cusp whose minimal-resolution cycle $\widehat D$ has data $\widehat{\mathbf d}$ obtained by interchanging the coefficients $a_i$ and $b_i$ in $\mathbf d=(a_1+3,2,\dots,2,\dots,a_k+3,2,\dots,2)$. It satisfies $Q(D)+Q(\widehat D)=24$.
:::

::: {.front card-id="card-57cc973230f7ba94" tags="definition"}
What is the definition of Dual intersection complex?
:::

::: {.back card-id="card-57cc973230f7ba94"}
For a semistable degeneration $\pi:\mathcal X\to\Delta$ with central fiber $X_0=\sum_{i\in I}D_i$, the dual intersection complex is the simplicial complex with a vertex for each component $D_i$, an edge for each irreducible component of $D_i\cap D_j$, a triangle for each triple intersection, and so on. It records the incidence pattern of the components and is the base of the SYZ fibration in the large complex structure limit.
:::

::: {.front card-id="card-615708f96cbc7338" tags="definition"}
What is the definition of Grauert-mumford theorem?
:::

::: {.back card-id="card-615708f96cbc7338"}
The Grauert-Mumford theorem states that a connected compact divisor $E=\sum E_i$ on a smooth complex surface can be contracted to a normal surface singularity if and only if its intersection matrix $(E_i\cdot E_j)$ is negative definite; the contraction is then unique up to isomorphism.
:::

::: {.front card-id="card-9065f7ad2a1a7ff3" tags="definition"}
What is the definition of Gromov-hausdorff limit?
:::

::: {.back card-id="card-9065f7ad2a1a7ff3"}
The Gromov-Hausdorff limit of compact metric spaces $(X_i,d_i)$ is a compact metric space $(X,d)$ with $d_{GH}(X_i,X)\to0$; equivalently the $X_i$ admit $\epsilon_i$-dense $\epsilon_i$-isometric nets into $X$ with $\epsilon_i\to0$.
:::

::: {.front card-id="card-5572b0772967e64e" tags="definition"}
What is the definition of Hodge-tate?
:::

::: {.back card-id="card-5572b0772967e64e"}
A mixed Hodge structure is Hodge-Tate if every graded piece $\mathrm{gr}^W_k$ is a direct sum of Tate twists $\mathbb Q(-p)$ of Hodge type $(p,p)$; equivalently it is a successive extension of the $\mathbb Q(n)$.
:::


::: {.front card-id="card-c52d15822bcdec98" tags="definition"}
What is the definition of Integral affine structure?
:::

::: {.back card-id="card-c52d15822bcdec98"}
An atlas $\{(U_i,\phi_i:U_i\to\mathbb R^n)\}$ with transition maps $x\mapsto Ax+b$, where $A\in\mathrm{GL}_n(\mathbb Z)$ and $b\in\mathbb R^n$. Equivalently, an affine structure with a parallel lattice in its tangent bundle. For an oriented structure use $\mathrm{SL}_n(\mathbb Z)$.

Requiring $b\in\mathbb Z^n$ is the stronger integral-vertex convention used for lattice triangulations. An ordinary integral-affine structure specifies integral tangent vectors, not a distinguished lattice of points.
:::

::: {.front card-id="card-2bfad83d9328a7f6" tags="definition"}
What is the definition of Lagrangian fibration?
:::

::: {.back card-id="card-2bfad83d9328a7f6"}
A Lagrangian fibration is a proper surjective map $f:(X^{2n},\omega)\to B$ whose smooth fibers are connected Lagrangian submanifolds of $X$, i.e. $\omega|_{f^{-1}(b)}=0$. A Lagrangian torus fibration has fibers $T^n$; the smooth locus of $B$ carries an integral affine structure.
:::

::: {.front card-id="card-63b5131f7fd0118f" tags="definition"}
What is the definition of Limiting mixed hodge structure?
:::

::: {.back card-id="card-63b5131f7fd0118f"}
For a polarized variation of Hodge structure of weight $m$ over $\Delta^*$ with unipotent monodromy, fix a coordinate $t=e^{2\pi iz}$ and identify nearby cohomology with $H_{\mathbb Q}$. Put $N=\log T$, using the convention $F(z+1)=T F(z)$.

The limit is
$$F_\infty=\lim_{\operatorname{Im}z\to\infty}e^{-zN}F(z),\qquad
H_{\lim}=(H_{\mathbb Q},W(N)[m],F_\infty).$$
The weight filtration is characterized by
$$NW_k\subset W_{k-2},\qquad
N^j:\operatorname{Gr}_{m+j}^W\xrightarrow{\sim}\operatorname{Gr}_{m-j}^W.$$
Untwisting multivalued flat sections by $e^{-zN}$ gives a frame for Deligne's canonical extension; its connection has nilpotent residue.

This is a mixed Hodge structure on **nearby cohomology**, not $H^m(X_0)$. Specialization maps $H^m(X_0)\to H^m_{\lim}$ and need not be an isomorphism. If $N=0$, the limit is pure of weight $m$, even when the central fiber is reducible: two smooth curves meeting at a separating node give the compact-type example.
:::

::: {.front card-id="card-02b0355c3650e92b" tags="definition"}
What is the definition of Moment polytope?
:::

::: {.back card-id="card-02b0355c3650e92b"}
For a Hamiltonian torus action on a compact symplectic manifold $(X,\omega)$ with moment map $\mu:X\to\mathfrak t^*$, the moment polytope is the convex polytope $\mu(X)\subset\mathfrak t^*$ (Atiyah-Guillemin-Sternberg). For a toric variety it is the polytope $P_D$ of an ample torus-invariant divisor.
:::

::: {.front card-id="card-1fd74048e90db1c2" tags="definition"}
What is the definition of Monodromy operator?
:::

::: {.back card-id="card-1fd74048e90db1c2"}
For a degeneration $\pi:\mathcal X\to\Delta^*$, the monodromy operator is the automorphism $T$ of $H^*(\mathcal X_t)$ induced by the positive generator of $\pi_1(\Delta^*)\cong\mathbb Z$. For a semistable degeneration it is unipotent, and $N=\log T$ is nilpotent.
:::

::: {.front card-id="card-795c0ca34a8a8864" tags="definition"}
What is the definition of Monodromy representation?
:::

::: {.back card-id="card-795c0ca34a8a8864"}
For a locally topologically trivial family $f:X\to B$ with fiber $F$, parallel transport gives
$$\pi_1(B,b_0)\to\operatorname{Aut}(H^*(F;\mathbb Z)).$$
Over a punctured disk it is specified by the automorphism $T$ for one positive loop. Picard–Lefschetz is the formula for this action in an ordinary quadratic-singularity degeneration; general monodromy need not be a single Picard–Lefschetz transformation.
:::

::: {.front card-id="card-56810efcabc4bf7c" tags="definition"}
What is the definition of Semi-universal deformation?
:::

::: {.back card-id="card-56810efcabc4bf7c"}
A semiuniversal (miniversal) deformation is versal and induces an isomorphism on tangent spaces. For the formal deformation functor $\operatorname{Def}_X$, its complete local base $R$ defines a smooth natural transformation $h_R\to\operatorname{Def}_X$ with tangent isomorphism; this is a hull. Here $h_R(A)=\operatorname{Hom}_{\mathrm{local},k}^{\mathrm{cont}}(R,A)$. Smoothness means compatible lifts exist across small extensions. The tangent space is $\operatorname{Ext}^1_X(L_{X/k},\mathcal O_X)$, or $H^1(X,T_X)$ for smooth $X$. A tangent isomorphism alone does not imply versality; inducing base maps need not be unique.
:::

::: {.front card-id="card-2e3d766f0efeb706" tags="definition"}
What is the definition of Special lagrangian?
:::

::: {.back card-id="card-2e3d766f0efeb706"}
A special Lagrangian submanifold of phase $\theta$ in a Calabi–Yau manifold $(X,\omega,\Omega)$ is an oriented Lagrangian $L\subset X$ (so $\omega|_L=0$ and $\dim_{\mathbb R}L=\dim_{\mathbb C}X$) with
$$\operatorname{Im}(e^{-i\theta}\Omega)|_L=0,\qquad
\operatorname{Re}(e^{-i\theta}\Omega)|_L=\operatorname{vol}_L.$$
Here $\Omega$ has the metric normalization making its real part a calibration. Equivalently, $L$ is calibrated by $\operatorname{Re}(e^{-i\theta}\Omega)$, hence a compact $L$ minimizes volume in its homology class. The orientation fixes the positive sign; the vanishing condition alone permits either orientation. Phase zero recovers $\operatorname{Im}\Omega|_L=0$ with positive real part.

Example: $\mathbb R^n\subset\mathbb C^n$, $\Omega=dz_1\wedge\cdots\wedge dz_n$, has phase zero. Rotating each coordinate by $e^{i\alpha_j}$ gives phase $\sum_j\alpha_j$.
:::

::: {.front card-id="card-50e0c6eeda83171e" tags="definition"}
What is the definition of Symplectic reduction?
:::

::: {.back card-id="card-50e0c6eeda83171e"}
Symplectic reduction (Marsden-Weinstein quotient) of a symplectic manifold $(X,\omega)$ by a Hamiltonian action of a Lie group $G$ with moment map $\mu:X\to\mathfrak g^*$ is $\mu^{-1}(0)/G$, with the induced symplectic form on the smooth locus; more generally one uses $\mu^{-1}(\xi)/G_\xi$.
:::

::: {.front card-id="card-aa1ee324431e9f74" tags="definition"}
What is the definition of Toric boundary?
:::

::: {.back card-id="card-aa1ee324431e9f74"}
The toric boundary of a toric variety $X_\Sigma$ is the reduced divisor $D=\sum_{\rho\in\Sigma(1)}D_\rho$, the complement of the dense torus $T\subset X_\Sigma$. It is a normal-crossing divisor, and $(X_\Sigma,D)$ is a toric pair.
:::

::: {.front card-id="card-d03d58dd6041270c" tags="definition"}
What is the definition of Toric degeneration?
:::

::: {.back card-id="card-d03d58dd6041270c"}
In the irreducible sense, a toric degeneration is a flat family whose special fiber is a toric variety. Smoothness of the general fiber and normality of the special fiber must be specified when required.

In the normal-crossing constructions used for Calabi–Yau degenerations, the special fiber is instead a union of toric components glued along toric strata. A compatible toroidal or log structure supplies the integral-affine data. An arbitrary flat family with toric special fiber need not be locally toric, and the two usages are not equivalent.
:::

::: {.front card-id="card-b4e485673235edf3" tags="definition"}
What is the definition of Triple point?
:::

::: {.back card-id="card-b4e485673235edf3"}
A triple point of a reducible surface $X_0=\bigcup_i V_i$ is a point at which three irreducible components meet, or at which three double curves meet. In the dual complex it corresponds to a triangular face whose vertices are the components and whose edges are the double curves.
:::

::: {.front card-id="card-356efa2f005e6ec3" tags="definition"}
What is the definition of Type vii_0 surface?
:::

::: {.back card-id="card-356efa2f005e6ec3"}
A minimal compact complex surface of class VII: $b_1=1$ and Kodaira dimension $\kappa=-\infty$. The subscript $0$ means **minimal**, not $b_2=0$.

Class VII contains surfaces with $b_2=0$ and surfaces with $b_2>0$. Hyperbolic Inoue surfaces have $b_2>0$ and two disjoint cycles of rational curves.
:::

::: {.front card-id="card-e8b82c81356a6955" tags="definition"}
What is the definition of Unipotency index?
:::

::: {.back card-id="card-e8b82c81356a6955"}
For a unipotent endomorphism $T$ (so $T-I$ is nilpotent), the unipotency index is the least integer $r\ge1$ such that $(T-I)^r=0$; equivalently it is the maximal Jordan-block size of $T$. A degeneration is maximally unipotent when this index is as large as possible, namely $r=n+1$ on $H^n$.
:::

::: {.front card-id="card-34e632bf729f4796" tags="definition"}
What is the definition of Universal deformation?
:::

::: {.back card-id="card-34e632bf729f4796"}
A deformation $\mathcal X\to S$ of $X$ is universal if, in the chosen category of pointed local bases, every marked deformation is induced by a unique base map to $S$, up to isomorphism of marked families. Formally, a complete local base $R$ prorepresents the set-valued deformation functor when $h_R\xrightarrow{\sim}\operatorname{Def}_X$. A hull gives only a smooth transformation with tangent isomorphism. The tangent isomorphism does not supply uniqueness of base maps, and set-valued universality does not remove automorphisms of families.
:::

::: {.front card-id="card-8934770be8e9010f" tags="definition"}
What is the definition of Node smoothing?
:::

::: {.back card-id="card-8934770be8e9010f"}
Deform a boundary node locally by $xy=t$. When it is the unique intersection of $D_i,D_{i+1}$, they merge into one component with self-intersection
$$D_{\mathrm{new}}^2=D_i^2+D_{i+1}^2+2.$$
For a two-component cycle, smoothing one of the two nodes gives an irreducible nodal component of square $D_1^2+D_2^2+4$. With the nodal convention $d=2-D^2$, both cases give $(\ldots,d_i,d_{i+1},\ldots)\mapsto(\ldots,d_i+d_{i+1}-2,\ldots)$ and charge increases by one.

This is a deformation of the boundary, not the contraction of a corner exceptional curve. A corner blowdown is birational and preserves charge.
:::

::: {.front card-id="card-d64fe05250d1165d" tags="definition"}
What is the definition of Top stratum?
:::

::: {.back card-id="card-d64fe05250d1165d"}
Let $B$ be a stratified space with filtration $\emptyset=B_{-1}\subseteq B_0\subseteq\cdots$ and strata $S_d(B)=B_d\setminus B_{d-1}$. If $n$ is the largest integer with $S_n(B)\neq\emptyset$, the top stratum is $S_n(B)=B_n\setminus B_{n-1}$. It is an open dense $n$-dimensional manifold, and its complement is the union of the lower-dimensional strata.
:::

::: {.front card-id="card-1a1d68d156466368" tags="definition"}
What is the definition of Triple point formula?
:::

::: {.back card-id="card-1a1d68d156466368"}
For a double curve $D_{ij}$ joining the components $V_i$ and $V_j$ of a type III anticanonical pair, the self-intersections in the two normalized components satisfy $(D_{ij}|_{\tilde V_i})^2+(D_{ij}|_{\tilde V_j})^2=-2$ when $D_{ij}$ is smooth and $0$ when $D_{ij}$ is nodal, where $\tilde V_i$ is the normalization of $V_i$.
:::
