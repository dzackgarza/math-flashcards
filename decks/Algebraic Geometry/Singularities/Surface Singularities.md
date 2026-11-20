---
title: "Algebraic Geometry::Singularities::Surface Singularities"
---

::: {.front card-id="singularity-smoothing-adjacency-resolution" tags="definition comparison example" cite="[@EF21, introduction, with the simultaneous resolution of du Val singularities]"}
Distinguish a smoothing, a smoothing component, an adjacency, and a simultaneous resolution of a complex surface singularity. Use an $A_1$ example.
:::

::: {.back card-id="singularity-smoothing-adjacency-resolution"}
- **Smoothing:** a flat deformation over a pointed smooth curve whose special fiber is the singularity and whose nearby fibers are smooth.
- **Smoothing component:** an irreducible component of the reduced base of a semiuniversal deformation whose general point parametrizes a smooth fiber. Different smoothing components can give different Milnor fibers.
- **Adjacency:** a deformation of the given singularity whose nearby fibers have a specified singularity, or configuration of singularities. State the direction: the special singularity deforms to the nearby configuration. Adjacency alone does not specify a smoothing component.
- **Simultaneous resolution:** a proper map from a smooth family over the same base to the singular family, restricting on each fiber to a resolution. A finite base change can be necessary; resolving the total space alone does not imply that the resolved family is smooth over the base.

Example: $xy-z^2=t$ smooths $A_1$. After $t=s^2$, write $xy=(z+is)(z-is)$. Blowing up the ideal $(x,z+is)$ gives a simultaneous resolution: an isomorphism for $s\ne0$, and the minimal resolution with one $(-2)$-curve at $s=0$.

For a nontrivial adjacency, $xy=z^3+t z^2$ has an $A_2$ singularity at $t=0$ and an $A_1$ singularity at the origin for $t\ne0$. Thus $A_2$ deforms to $A_1$; this family is not itself a smoothing.
:::

::: {.front card-id="hypersurface-milnor-tjurina-modality-suspension" tags="definition comparison example" cite="[@GPSZ22, §2.3, with Arnold's hypersurface classification]"}
For an isolated complex hypersurface germ, compare Milnor number, Tjurina number, and modality. What does suspension preserve? Compute the example $x^2+y^3+z^7$.
:::

::: {.back card-id="hypersurface-milnor-tjurina-modality-suspension"}
For $f\in\mathbb C\{x_0,\ldots,x_n\}$ with an isolated critical point,
$$\mu=\dim_{\mathbb C}\frac{\mathbb C\{x\}}{(\partial f)},\qquad
\tau=\dim_{\mathbb C}\frac{\mathbb C\{x\}}{(f,\partial f)}.$$
$\mu$ is the rank of the middle reduced homology of the Milnor fiber; $\tau$ is the dimension of the first-order deformation space of the hypersurface germ. Weighted-homogeneous $f$ satisfies $\mu=\tau$ by the Euler relation.

For Arnold's function-germ classification, right equivalence means an analytic change of source coordinates. Modality counts the maximum number of parameters of inequivalent germs in nearby orbit strata: for a sufficiently high finite jet space, take the maximum of $\dim S-\dim(\text{orbit in }S)$ over the local constant-orbit-dimension strata. Modality zero means simple; modality one means unimodal. It is not $\mu$, $\tau$, or the number of coefficients in an arbitrary equation.

Suspension replaces $f$ by $f+u^2$. Stable right equivalence allows adding nondegenerate quadratic variables; $\mu$ and the Arnold type are unchanged, while the hypersurface dimension increases.

Example: $x^2+y^3+z^7$ is the $E_{12}$ surface germ. Its Jacobian algebra has basis $y^a z^b$ for $0\le a<2$, $0\le b<6$, so $\mu=\tau=12$. It is unimodal, unlike the simple du Val $E_6,E_7,E_8$. The branch-curve germ $y^3+z^7$ has the same stable label but is a curve, not a surface.
:::

::: {.front card-id="surface-double-crossing-involution-quotient" tags="application calculation" cite="[@AEGS25, Proposition 4.8 and equation (4.1), with the finite crepant-cover discrepancy criterion]"}
Describe the normalization and conductor of $S=\{xz=0\}\subset\mathbb A^3_{x,y,z}$ modulo $(x,y,z)\mapsto(-x,-y,-z)$. Why is this quotient slc, and does the image of the origin become an isolated log canonical center?
:::

::: {.back card-id="surface-double-crossing-involution-quotient"}
The action preserves each plane. Its normalization is the disjoint union of two $A_1$ surfaces:
$$\mathbb A^2_{x,y}/\{\pm1\}=\operatorname{Spec}\mathbb C[u,v,w]/(uw-v^2),\qquad
u=x^2,\ v=xy,\ w=y^2,$$
and the analogous plane with $x$ replaced by $z$. The conductor on each is the image of $x=0$, respectively $z=0$; its coordinate is $w=y^2$. Glue these conductor lines by the identity.

Upstairs the normalized pair is a smooth plane with one coefficient-one line, hence plt. The quotient is étale away from the origin, and the log canonical divisor pulls back to that of the plane pair. The quotient normalized pair is therefore plt as well. Its only lc center is the conductor curve, not the origin separately. Along its conductor, adjunction has different $\tfrac12[0]$, recording $y\mapsto y^2$.

The glued surface is demi-normal: nodal in codimension one, and $S_2$ by the invariant direct-summand description of this Cohen–Macaulay double crossing. Its canonical class is $\mathbb Q$-Cartier of index at most two. The normalization criterion therefore gives slc. This permits a polarizing divisor through the image of the origin, provided it does not contain the double curve and its coefficient is sufficiently small for log canonicity.
:::

::: {.front card-id="surface-resolution-graph-determinant" tags="definition computation" cite="[@AL19, §2]"}
Define the weighted dual graph and determinant of a resolved normal surface singularity. Compute a two-vertex chain.
:::

::: {.back card-id="surface-resolution-graph-determinant"}
For a resolution $f:Y\to(X,x)$ with exceptional curves $E_i$, put one vertex per $E_i$, labeled by its genus and self-intersection. Distinct vertices have $E_iE_j$ edges for transverse intersections; record non-SNC intersections separately.

The exceptional intersection matrix $Q=(E_iE_j)$ is negative definite. Define the graph determinant
$$\det(\Gamma)=\det(-Q)>0.$$
A rational chain with self-intersections $-b_1,-b_2$ has
$$-Q=\begin{pmatrix}b_1&-1\\-1&b_2\end{pmatrix},\qquad
\det(\Gamma)=b_1b_2-1.$$
For an $A_2$ singularity, $b_1=b_2=2$, so the determinant is three. For a rational tree whose plumbing boundary is a rational homology sphere, this determinant is the order of its first homology. Genus and graph cycles cannot be omitted when deciding that hypothesis.
:::

::: {.front card-id="card-8f343de9852359e9" tags="definition"}
Characterize a rational double point over $\mathbb C$ using rationality and multiplicity.
:::

::: {.back card-id="card-8f343de9852359e9"}
An isolated normal surface singularity that is rational and has multiplicity $2$. These are precisely the Du Val surface singularities.
:::

::: {.front card-id="singularity-duval-equations" tags="definition"}
Give analytic equations for the complex Du Val singularities.
:::

::: {.back card-id="singularity-duval-equations"}
| Type | Equation in $\mathbb C^3$ |
| --- | --- |
| $A_n$, $n\ge1$ | $xy-z^{n+1}=0$ |
| $D_n$, $n\ge4$ | $x^2+y^2z+z^{n-1}=0$ |
| $E_6$ | $x^2+y^3+z^4=0$ |
| $E_7$ | $x^2+y^3+yz^3=0$ |
| $E_8$ | $x^2+y^3+z^5=0$ |
:::

::: {.front card-id="singularity-duval-recognition" tags="application"}
Identify the surface germs $xy=z^5$, $x^2+y^2z+z^3=0$, and $x^2+y^3+z^5=0$. How many exceptional curves occur in their minimal resolutions?
:::

::: {.back card-id="singularity-duval-recognition"}
| Equation | Type | Exceptional curves |
| --- | --- | --- |
| $xy=z^5$ | $A_4$ | $4$ |
| $x^2+y^2z+z^3=0$ | $D_4$ | $4$ |
| $x^2+y^3+z^5=0$ | $E_8$ | $8$ |

Each exceptional curve is rational with self-intersection $-2$.
:::

::: {.front card-id="singularity-cyclic-quotient" tags="definition"}
Define the complex cyclic quotient surface germ $\frac1r(1,a)$, where $r>1$ and $\gcd(r,a)=1$. Which member gives $A_{r-1}$?
:::

::: {.back card-id="singularity-cyclic-quotient"}
It is the quotient of $(\mathbb C^2,0)$ by
$$\zeta\cdot(u,v)=(\zeta u,\zeta^a v),\qquad \zeta^r=1.$$
For $a=r-1$, the invariant functions $x=u^r,y=v^r,z=uv$ satisfy $xy=z^r$, giving $A_{r-1}$.
:::

::: {.front card-id="singularity-duval-quotients" tags="definition"}
Which finite linear quotients of $\mathbb C^2$ give Du Val surface singularities?
:::

::: {.back card-id="singularity-duval-quotients"}
The quotients $\mathbb C^2/G$ for nontrivial finite subgroups $G\subset\operatorname{SL}_2(\mathbb C)$. Cyclic groups give $A$-types; binary dihedral groups give $D$-types; binary tetrahedral, octahedral, and icosahedral groups give $E_6,E_7,E_8$.
:::

::: {.front card-id="singularity-simple-elliptic" tags="definition"}
What is a simple elliptic surface singularity? Give a geometric example and distinguish it from a surface cusp.
:::

::: {.back card-id="singularity-simple-elliptic"}
A normal complex surface singularity whose minimal resolution has exceptional divisor a smooth elliptic curve. The affine cone over a smooth plane cubic is an example; its exceptional elliptic curve has self-intersection $-3$. A surface cusp instead has a cycle of rational curves, or a nodal rational curve.
:::

::: {.front card-id="card-862154888a8bb22d"}
Give an analytic equation for a complex surface singularity of type $A_1$.
:::

::: {.back card-id="card-862154888a8bb22d"}
$$xy-z^2=0\quad\text{in }(\mathbb C^3,0).$$
It is the vertex of a quadratic cone, also isomorphic to $\mathbb C^2/\{\pm1\}$.
:::

::: {.front card-id="card-df4853bcf54d4927"}
What type of curve is the resolution of an $A_1$ singularity?
:::

::: {.back card-id="card-df4853bcf54d4927"}
$D\cong {\mathbf{P}}^1$ with $D^2 = -2$.
:::

::: {.front card-id="card-1aab55ee31850bbb"}
Characterize a complex Du Val surface singularity by its minimal resolution.
:::

::: {.back card-id="card-1aab55ee31850bbb"}
The exceptional curves are smooth rational curves of self-intersection $-2$ whose dual graph is an ADE Dynkin diagram. These are the rational double points, equivalently the singular canonical surface germs.
:::

::: {.front card-id="card-dcd1e437d41fbead"}
What is a cusp singularity of a complex normal surface?
:::

::: {.back card-id="card-dcd1e437d41fbead"}
Its minimal resolution has exceptional divisor a negative-definite cycle of smooth rational curves, or an irreducible rational curve with one node. This is a surface germ; the plane-curve cusp $y^2=x^3$ is a different, one-dimensional singularity.
:::


::: {.front card-id="surface-cyclic-quotient-decoding" tags="construction calculation example" cite="[@CLS11, §10.1–10.2 and Example 11.4.6; @KM98, §4.1]"}
Decode the cyclic quotient germ $\frac1r(1,a)$, $\gcd(r,a)=1$: action, isomorphic labels, toric cone, minimal resolution, discrepancies, and index of $K_X$. Work out $\frac14(1,1)$ and $\frac15(1,2)$.
:::

::: {.back card-id="surface-cyclic-quotient-decoding"}
**Action.** $X=\mathbb C^2/\mu_r$, $\zeta\cdot(u,v)=(\zeta u,\zeta^a v)$. Since $\gcd(r,a)=1$, no $\zeta^k\ne1$ fixes a line, so $\mu_r$ has no pseudoreflections and $0$ is the only singular point.

**Labels.** $\frac1r(1,a)\cong\frac1r(1,a')$ iff $a'=a$ or $aa'\equiv1\pmod r$. Reason: swap $u,v$ and use the generator $\zeta^{a}$; the weights become $(1,a^{-1})$.

**Toric cone.** In $N=\mathbb Z^2$: $\sigma=\operatorname{Cone}(e_2,\ re_1-ae_2)$. Equivalently, $\sigma=\mathbb R^2_{\ge0}$ in $N'=\mathbb Z^2+\mathbb Z\cdot\frac1r(1,a)$.

**Resolution.** Hirzebruch–Jung continued fraction
$$\frac ra=b_1-\cfrac{1}{b_2-\cfrac{1}{\ddots-\cfrac1{b_k}}}=[b_1,\dots,b_k],\qquad b_i\ge2.$$
The minimal resolution is a chain $E_1-\cdots-E_k$ of smooth rational curves with $E_i^2=-b_i$. Its determinant is $r$. The rays of the resolved fan are the lattice points of $N'$ on the boundary of $\operatorname{conv}(\sigma\cap N'\setminus0)$.

**Discrepancies.** In $N'$ coordinates, $K_X$ pulls back by the linear function $\varphi(x,y)=x+y$, which is $1$ on $e_1,e_2$. The divisor of a primitive ray $v$ has log discrepancy $A(E_v)=\varphi(v)$. For example, $v=\frac1r(1,a)$ gives $A=\frac{1+a}r$. Equivalently, solve $\sum_j a_jE_jE_i=-K_Y E_i=2-b_i$ for $K_Y=\pi^*K_X+\sum a_jE_j$.

- Every $A(E_i)\in(0,1]$, so cyclic quotients are klt.
- Canonical $\iff$ every $a_i=0\iff$ all $b_i=2\iff a\equiv-1$: the germ is $A_{r-1}$.

**Index.** $du\wedge dv\mapsto\zeta^{1+a}du\wedge dv$, so the index of $K_X$ is $r/\gcd(r,1+a)$.

| Germ | $r/a$ | Chain | Discrepancies | Index |
| --- | --- | --- | --- | --- |
| $\frac1r(1,r-1)$ | $[2,\dots,2]$ | $r-1$ curves $(-2)$ | all $0$ | $1$ ($A_{r-1}$) |
| $\frac1r(1,1)$ | $[r]$ | one $(-r)$-curve | $\frac2r-1$ | $r/\gcd(r,2)$ |
| $\frac14(1,1)$ | $[4]$ | one $(-4)$-curve | $-\frac12$ | $2$ |
| $\frac15(1,2)$ | $[3,2]$ | $(-3)-(-2)$ | $-\frac25,-\frac15$ | $5$ |

Check for $\frac15(1,2)$: $3-\frac12=\frac52$. The rays $\frac15(1,2)$ and $\frac15(3,1)$ give $A=\frac35,\frac45$. The linear system $-3a_1+a_2=1$, $a_1-2a_2=0$ gives the same values.
:::

::: {.front card-id="surface-klt-lc-graph-classification" tags="theorem classification" cite="[@KM98, Theorem 4.7 and Proposition 4.18]"}
Which complex normal surface germs are klt? Classify klt and strictly lc germs by the dual graph of the minimal resolution.
:::

::: {.back card-id="surface-klt-lc-graph-classification"}
**klt $\iff$ quotient.** A normal surface germ $(X,x)$ is klt iff it is analytically $\mathbb C^2/G$ for a finite $G\subset\mathrm{GL}_2(\mathbb C)$. One can take $G$ with no pseudoreflections.

In the graphs below, every exceptional curve is a smooth rational curve with $E^2\le-2$. For a branch chain, $d_i$ is its determinant: the $r$ of its $\frac{r}{a}$.

| Class | Minimal-resolution graph | Origin |
| --- | --- | --- |
| klt | chain | cyclic $\frac1r(1,a)$ |
| klt | one central curve with three branch chains, $(d_1,d_2,d_3)\in\{(2,2,n),(2,3,3),(2,3,4),(2,3,5)\}$, i.e. $\sum1/d_i>1$ | dihedral, tetrahedral, octahedral, icosahedral quotients |
| lc, not klt | one smooth elliptic curve | simple elliptic |
| lc, not klt | a cycle of rational curves, or one nodal rational curve | cusp |
| lc, not klt | a central curve with four $(-2)$-branches | $\mathbb Z/2$ quotient of simple elliptic |
| lc, not klt | a chain with two $(-2)$-curves attached at each end | $\mathbb Z/2$ quotient of a cusp |
| lc, not klt | a central curve with three branches, $(d_i)\in\{(3,3,3),(2,4,4),(2,3,6)\}$, i.e. $\sum1/d_i=1$ | $\mathbb Z/3,\mathbb Z/4,\mathbb Z/6$ quotients of simple elliptic |

Du Val germs are the klt rows with all $b_i=2$: chains give $A_n$; $(2,2,n)$ gives $D_{n+2}$; $(2,3,3),(2,3,4),(2,3,5)$ give $E_6,E_7,E_8$.

Reading test: the graph $(-3)-(-2)$ is a chain, hence $\frac15(1,2)$, klt. A single $(-4)$-curve is $\frac14(1,1)$. An elliptic curve of any negative square is simple elliptic, hence lc but not klt.
:::

::: {.front card-id="surface-t-wahl-singularities" tags="definition construction example" cite="[@KS88, Proposition 3.10; @Wah81]"}
Define T-singularities and Wahl singularities. Give the cyclic family, its index-one cover, a $\mathbb Q$-Gorenstein smoothing, and the examples $\frac14(1,1)$ and $\frac19(1,2)$. Why do they matter for KSBA limits?
:::

::: {.back card-id="surface-t-wahl-singularities"}
**T-singularity:** a quotient surface singularity with a $\mathbb Q$-Gorenstein smoothing, i.e. a smoothing over a disc on which $K$ of the total space is $\mathbb Q$-Cartier. Classification: Du Val germs, or
$$\frac1{dn^2}(1,\,dna-1),\qquad n\ge2,\ d\ge1,\ \gcd(n,a)=1.$$
**Wahl singularity:** the case $d=1$, $\frac1{n^2}(1,na-1)$. Its smoothing has Milnor fibre a rational homology ball ($\mu=0$).

**Construction.** The index of $K_X$ is $n$. The index-one cover is $A_{dn-1}=\{xy=z^{dn}\}$ with
$$X=\{xy=z^{dn}\}/\mu_n,\qquad\zeta\cdot(x,y,z)=(\zeta x,\zeta^{-1}y,\zeta^az).$$
The $\mu_n$-invariant deformation
$$xy=z^{dn}+\sum_{k=0}^{d-1}t_kz^{kn}$$
descends to a $\mathbb Q$-Gorenstein smoothing of $X$. Its Milnor number is $d-1$.

| Germ | $(d,n,a)$ | Resolution chain | Index |
| --- | --- | --- | --- |
| $\frac14(1,1)$ | $(1,2,1)$ | $[4]$ | $2$ |
| $\frac19(1,2)$ | $(1,3,1)$ | $[5,2]$ | $3$ |
| $\frac18(1,3)$ | $(2,2,1)$ | $[3,3]$ | $2$ |

Check: $\frac92=5-\frac12$, so $[5,2]$; $\frac83=3-\frac13$, so $[3,3]$.

**KSBA use.** A $\mathbb Q$-Gorenstein family keeps $K^2$ and $\chi(\mathcal O)$ constant. In a $\mathbb Q$-Gorenstein family of surfaces with smooth general fibre, each quotient singularity of the special fibre is a T-singularity. Example: in the Coble quotient of a surface with a node, the composite action on the node is $\mathbb A^2/\mu_4$, $(u,v)\mapsto(\zeta u,\zeta v)$. The image is a $\frac14(1,1)$ point, and its minimal resolution contains a $(-4)$-curve. Restoring the constant term killed by the quotient gives the local smoothing.
:::
