---
title: "Algebraic Geometry::Examples"
---

::: {.front card-id="projective-gale-self-duality" tags="definition construction example"}
Construct the Gale dual of an ordered point configuration. State the non-degeneracy needed and the matrix criterion for self-duality.
:::

::: {.back card-id="projective-gale-self-duality"}
Represent $n$ points of $\mathbb P^{r-1}$ by the columns of a rank-$r$ matrix $A$, with $n>r$. Strong non-degeneracy: deleting any column leaves rank $r$; equivalently every hyperplane misses at least two points.

Choose a basis of $\ker(A:k^n\to k^r)$ as the rows of an $(n-r)\times n$ matrix $B$. Then $AB^t=0$. Its columns are nonzero by strong non-degeneracy and define the Gale dual in $\mathbb P^{n-r-1}$. Changing the kernel basis changes only projective coordinates; rescaling columns of $A$ inversely rescales columns of $B$. Dualizing twice returns the original projective configuration.

For $n=2r$, ordered self-duality means $B=GA D$ for invertible $G$ and invertible diagonal $D$, equivalently
$$A D A^t=0.$$
Example: $A=[I_r\mid I_r]$, $B=[I_r\mid-I_r]$. Both represent the configuration with each coordinate point repeated twice; $D=\operatorname{diag}(I_r,-I_r)$ proves self-duality.

References: [Caminata et al., §4](https://arxiv.org/abs/1711.06286); [Gallardo–Schaffler, §3](https://arxiv.org/abs/2610.35060).
:::

::: {.front card-id="projective-evaluation-determinantal-loci" tags="definition construction example"}
How do evaluation matrices express the condition that a point configuration lies on a degree-$d$ hypersurface? Define its determinantal rank loci.
:::

::: {.back card-id="projective-evaluation-determinantal-loci"}
For $n$ points $p_i\in\mathbb P^r$, choose homogeneous representatives and a monomial basis of $H^0(\mathbb P^r,\mathcal O(d))$, of size $N=\binom{r+d}{d}$. The $n\times N$ matrix
$$E_d=(m_j(p_i))$$
represents evaluation after trivializing the fibers $\mathcal O(d)|_{p_i}$. Its kernel consists of degree-$d$ equations through all the points. Rescaling point representatives rescales rows and does not change rank.

Rank $\le s$ is cut out scheme-theoretically by all $(s+1)$-minors. A nonzero equation exists iff $\operatorname{rank}E_d<N$. If $n<N$, this is automatic. Independent conditions means rank $\min(n,N)$.

Examples: three plane points collinear iff the $3\times3$ coordinate determinant vanishes. Six plane points lie on a conic, possibly reducible or nonreduced, iff the determinant of their quadratic $6\times6$ evaluation matrix vanishes.

Reference: Caminata–Moon–Schaffler, *Determinantal varieties from point configurations on hypersurfaces*, §2.
:::

::: {.front card-id="projective-osculating-jets" tags="definition construction example"}
Define the order-$k$ osculating space to an embedded smooth curve over $\mathbb C$. Compute it for a rational normal curve, including its osculating hyperplane.
:::

::: {.back card-id="projective-osculating-jets"}
For a local nonzero vector lift $v(t)$ of $C\subset\mathbb P^r$ at $t_0$:
$$\operatorname{Osc}^k_{t_0}(C)=\mathbb P\langle v(t_0),v'(t_0),\ldots,v^{(k)}(t_0)\rangle.$$
Reparametrization and changing the lift preserve the span. Equivalently its annihilator consists of hyperplanes whose defining sections vanish to order at least $k+1$. Dimension is at most $\min(k,r)$; a drop records deficient jets.

For $v(t)=(1,t,\ldots,t^r)$, $\dim\operatorname{Osc}^k= k$ for $0\le k\le r$. At $t=0$, it is $X_{k+1}=\cdots=X_r=0$. The osculating hyperplane at finite $a$ has coefficients of $(t-a)^r$:
$$\sum_{j=0}^r\binom rj(-a)^{r-j}X_j=0.$$
It meets the curve at $a$ with multiplicity $r$. For the twisted cubic: points, tangent lines, osculating planes, then all of $\mathbb P^3$.

Reference: Caminata–Carlini–Schaffler, *Simplices osculating rational normal curves*, §2.
:::

::: {.front card-id="construction-delpezzo-weighted-low-degree" tags="construction application"}
Construct smooth complex del Pezzo surfaces of degrees two and one by equations. Recover their degrees and anticanonical maps.
:::

::: {.back card-id="construction-delpezzo-weighted-low-degree"}
In degree two, use
$$X_4=\{w^2=f_4(x,y,z)\}\subset\mathbb P(1,1,1,2),$$
where $f_4=0$ is a smooth plane quartic. Weighted adjunction gives $-K=\mathcal O_X(1)$ and $K^2=4/(1\cdot1\cdot1\cdot2)=2$. Projection to $[x:y:z]$ is the anticanonical double cover.

In degree one, use a smooth sextic
$$X_6=\{w^2=z^3+f_4(x,y)z+f_6(x,y)\}\subset\mathbb P(1,1,2,3).$$
Again $-K=\mathcal O_X(1)$, now with square $6/(1\cdot1\cdot2\cdot3)=1$. The sections $x,y$ give an anticanonical pencil with one base point; $x^2,xy,y^2,z$ give the bi-anticanonical double cover of a quadric cone.

Concrete smooth examples are $w^2=x^4+y^4+z^4$ and $w^2=z^3+x^6+y^6$. Their affine cones are smooth away from the vertex and the surfaces avoid the singular points of the ambient weighted spaces. Thus the weighted formulas apply to smooth surfaces, not merely to stacks.
:::

::: {.front card-id="example-quadric-projection-parametrization" tags="example application"}
Parametrize $Q=V(X_0X_3-X_1X_2)\subset\mathbb P^3_{\mathbb C}$ birationally by projection from $p=[1:0:0:0]$. Give the rational inverse and locate its base points.
:::

::: {.back card-id="example-quadric-projection-parametrization"}
Projection is $[X_0:X_1:X_2:X_3]\dashrightarrow[X_1:X_2:X_3]$. On $X_3\ne0$, the equation recovers $X_0=X_1X_2/X_3$. Thus the inverse is
$$[u:v:w]\dashrightarrow[uv:uw:vw:w^2].$$
Substitution gives $X_0X_3=X_1X_2$, and composition is the identity on $w\ne0$. Its base points are $[1:0:0]$ and $[0:1:0]$. The line $w=0$ contracts to $p$ away from those points. Projection from $p$ contracts the two ruling lines on $Q$ through $p$, away from $p$ itself.
:::

::: {.front card-id="example-plane-product-birational-map" tags="example application"}
Give explicit inverse birational maps between $\mathbb P^2_{\mathbb C}$ and $\mathbb P^1\times\mathbb P^1$. Describe their indeterminacy and a common smooth resolution.
:::

::: {.back card-id="example-plane-product-birational-map"}
Use
$$[x:y:z]\dashrightarrow([x:y],[x:z]),\qquad
([a:b],[c:d])\dashrightarrow[ac:bc:ad].$$
They are inverse where $x\ne0$ and $ac\ne0$. The forward map has base points $[0:1:0]$ and $[0:0:1]$; the inverse has base point $([0:1],[0:1])$.

Blow up the two plane base points. The strict transform of $x=0$ has class $H-E_1-E_2$ and square $-1$; contracting it gives $\mathbb P^1\times\mathbb P^1$. The ruling classes pull back to $H-E_1$ and $H-E_2$, with square zero and mutual intersection one. This surface is also the blowup of the product at the inverse base point.
:::

::: {.front card-id="example-conic-pencil-four-basepoints" tags="example application"}
Consider the pencil spanned by $F=x(y-z)$ and $G=y(x-z)$ in $\mathbb P^2_{\mathbb C}$. Find its base scheme, resolve the map $[F:G]$, and describe the fiber class, sections, and singular members.
:::

::: {.back card-id="example-conic-pencil-four-basepoints"}
The base scheme consists of four reduced points
$$[1:0:0],\quad[0:1:0],\quad[0:0:1],\quad[1:1:1].$$
The gradients of $F,G$ are independent at each point. Blowing them up resolves the map, with fiber class $D=2H-E_1-E_2-E_3-E_4$. Then $D^2=0$, $K_SD=-2$, and the general fiber has genus zero. Each $E_i$ meets $D$ once and is a section.

The singular members are $F$, $G$, and $F-G=z(y-x)$: the three pairings of the four base points into pairs of lines. Each resolved singular fiber consists of two $(-1)$-curves meeting once. There are no others: the determinant of the symmetric matrix of $\lambda F+\mu G$ is a nonzero scalar times $\lambda\mu(\lambda+\mu)$.
:::

::: {.front card-id="example-cubic-pencil-elliptic-surface" tags="example application"}
A general pencil of plane cubics over $\mathbb C$ has nine distinct base points. What surface and fibration result from blowing them up? Compute the fiber class, canonical class, sections, and number of singular fibers.
:::

::: {.back card-id="example-cubic-pencil-elliptic-surface"}
Blowing up the base points gives a rational elliptic surface $f:S\to\mathbb P^1$, with
$$F=3H-\sum_{i=1}^9E_i=-K_S,\qquad F^2=0,\qquad K_SF=0.$$
Adjunction gives genus one for a smooth fiber. Each $E_i$ has $E_iF=1$ and is a section, so the fibration has a section as well as genus-one fibers.

For a general pencil all singular fibers are irreducible nodal cubics. Since $e(S)=e(\mathbb P^2)+9=12$, smooth elliptic fibers have Euler characteristic zero, and each nodal fiber contributes one, there are twelve singular fibers. Distinct base points alone do not guarantee this fiber type; special pencils can have reducible or cuspidal fibers.

Reference: [Vakil, Twelve points on the projective line, branched covers, and rational elliptic fibrations](https://arxiv.org/abs/math/9910077).
:::

::: {.front card-id="example-conic-system-discriminant" tags="example application"}
How do you find singular members of a pencil or net of plane conics over $\mathbb C$? Compute the discriminant of the net $ax^2+by^2+cz^2$ and distinguish this discriminant from the base locus.
:::

::: {.back card-id="example-conic-system-discriminant"}
Write a conic as $\mathbf x^TA\mathbf x$ with $A$ symmetric. It is singular exactly when $\det A=0$. Rank two gives two distinct lines, and rank one gives a double line. For a pencil $A=\lambda A_0+\mu A_1$, the determinant is a binary cubic; if not identically zero, it has three roots counted with multiplicity.

For a net $A=aA_0+bA_1+cA_2$, the discriminant is a cubic in its parameter plane, unless identically zero. In the diagonal example it is $abc=0$: a triangle. A general point on each side gives a pair of lines, and each vertex gives a double line. The net's base locus lies in the original plane and is empty, since $x^2=y^2=z^2=0$ has no projective solution.
:::

::: {.front card-id="example-cremona-net-complete-subsystem" tags="example application"}
View the quadratic Cremona map as a net. Which conditions on conics define it? Is it complete as a plane conic system, and what happens to completeness on the blowup?
:::

::: {.back card-id="example-cremona-net-complete-subsystem"}
Vanishing at $[1:0:0]$, $[0:1:0]$, and $[0:0:1]$ kills the coefficients of $x^2,y^2,z^2$, leaving
$$V=\langle yz,xz,xy\rangle.$$
Thus it is an incomplete subsystem of $|\mathcal O_{\mathbb P^2}(2)|$, but contains every conic through the three points. On their blowup it is the complete, base-point-free system $|2H-E_1-E_2-E_3|$. This class has square one, so the morphism to its image $\mathbb P^2$ has degree one; the strict transforms of the coordinate lines are contracted.
:::

::: {.front card-id="application-hilbert-family-conics" tags="application"}
For the family $xy=t z^2$ in $\mathbb P^2_{\mathbb C}\times\mathbb A^1_t$, find its Hilbert polynomial and explain why it defines a morphism to a single projective Hilbert scheme, including at $t=0$.
:::

::: {.back card-id="application-hilbert-family-conics"}
The total space is integral and dominates the smooth base curve, so the family is flat. Every fiber is a plane conic, with Hilbert polynomial
$$P(m)=\binom{m+2}{2}-\binom m2=2m+1.$$
Hilbert representability therefore gives a morphism $\mathbb A^1\to\operatorname{Hilb}^{2m+1}_{\mathbb P^2}$. The union of two lines at $t=0$ is a valid fiber of the same flat family.
:::

::: {.front card-id="application-smoothness-conic-family" tags="application"}
Over $\mathbb C$, the family $xy=tz^2$ in $\mathbb P^2\times\mathbb A^1_t$ is flat. Determine the largest open subset of the base over which the morphism is smooth.
:::

::: {.back card-id="application-smoothness-conic-family"}
It is $\mathbb A^1\setminus\{0\}$. The fibers there are smooth conics. At $t=0$, the fiber is two lines crossing at $[0:0:1]$, so it is not smooth. Finite presentation and flatness let the fiberwise smoothness criterion decide the question.
:::





::: {.front card-id="example-plane-conic" tags="example construction"}
Over $\mathbb C$, give an equation and an isomorphism from $\mathbb P^1$ for a smooth plane conic.
:::

::: {.back card-id="example-plane-conic"}
The conic $XZ-Y^2=0$ is the image of
$$[s:t]\longmapsto[s^2:st:t^2].$$
This is the embedding defined by $|\mathcal O_{\mathbb P^1}(2)|$. Its degree is two and its genus is zero.
:::

::: {.front card-id="example-rational-normal-curve" tags="example construction"}
For $d\ge2$, construct the rational normal curve in $\mathbb P^d_{\mathbb C}$. Give its homogeneous ideal, degree, and Hilbert polynomial.
:::

::: {.back card-id="example-rational-normal-curve"}
The complete linear system $|\mathcal O_{\mathbb P^1}(d)|$ gives
$$[s:t]\longmapsto[s^d:s^{d-1}t:\cdots:st^{d-1}:t^d].$$
Its ideal is generated by the $2\times2$ minors of
$$\begin{pmatrix}x_0&x_1&\cdots&x_{d-1}\\x_1&x_2&\cdots&x_d\end{pmatrix}.$$
It is smooth of genus zero and degree $d$, with Hilbert polynomial $dm+1$.
:::

::: {.front card-id="example-twisted-cubic" tags="example construction"}
Give a parametrization and the homogeneous ideal of the twisted cubic in $\mathbb P^3_{\mathbb C}$. Is it a complete intersection?
:::

::: {.back card-id="example-twisted-cubic"}
It is the image of $[s:t]\mapsto[s^3:s^2t:st^2:t^3]$, with ideal
$$I=(x_0x_2-x_1^2,\ x_0x_3-x_1x_2,\ x_1x_3-x_2^2).$$
It has degree three and genus zero. A complete intersection curve of degree three in $\mathbb P^3$ would have defining degrees one and three and would be planar. The twisted cubic spans $\mathbb P^3$, so it is not a complete intersection.
:::



::: {.front card-id="example-elliptic-plane-cubic" tags="example construction"}
Construct a smooth plane cubic with a marked point over $\mathbb C$. State the condition on its coefficients and explain its genus.
:::

::: {.back card-id="example-elliptic-plane-cubic"}
Use
$$E:\ Y^2Z=X^3+AXZ^2+BZ^3,\qquad 4A^3+27B^2\ne0.$$
The marked point is $[0:1:0]$. A smooth plane curve of degree $d$ has genus $(d-1)(d-2)/2$, so $E$ has genus one. For example, $Y^2Z=X^3-XZ^2$ is smooth.
:::

::: {.front card-id="example-hyperelliptic-model" tags="example construction"}
For $g\ge2$, construct a smooth projective hyperelliptic curve of genus $g$ over $\mathbb C$ from an affine equation. Describe the points and ramification at infinity.
:::

::: {.back card-id="example-hyperelliptic-model"}
Take the smooth projective model of $y^2=f(x)$ with $f$ squarefree of degree $2g+1$ or $2g+2$. The map $x:C\to\mathbb P^1$ has degree two.

For odd degree there is one ramified point above infinity; for even degree there are two unramified points. Together with the roots of $f$, there are $2g+2$ branch points. Riemann–Hurwitz gives $2g(C)-2=-4+(2g+2)$.
:::

::: {.front card-id="example-plane-quartic" tags="example construction"}
Give an explicit smooth nonhyperelliptic curve of genus three over $\mathbb C$. Describe its canonical map.
:::

::: {.back card-id="example-plane-quartic"}
The Fermat quartic $X^4+Y^4+Z^4=0$ is smooth: its partial derivatives have no common projective zero. Its genus is three. Adjunction gives $K_C\cong\mathcal O_C(1)$, so its plane embedding is its canonical embedding and it is nonhyperelliptic.
:::

::: {.front card-id="example-elliptic-quartic" tags="example construction"}
Give equations for a smooth genus-one curve of degree four in $\mathbb P^3_{\mathbb C}$.
:::

::: {.back card-id="example-elliptic-quartic"}
For distinct $\lambda_0,\ldots,\lambda_3\in\mathbb C$, take
$$\sum_{i=0}^3x_i^2=0,\qquad\sum_{i=0}^3\lambda_i x_i^2=0.$$
Dependence of the gradients would force at most one nonzero coordinate, which the first equation excludes. This smooth complete intersection has degree four and $K_C\cong\mathcal O_C(2+2-4)\cong\mathcal O_C$, hence genus one.
:::

::: {.front card-id="example-segre-quadric" tags="example construction"}
Construct the smooth quadric surface in $\mathbb P^3_{\mathbb C}$ as a product. Give its equation and describe its lines.
:::

::: {.back card-id="example-segre-quadric"}
The Segre embedding is
$$([s:t],[u:v])\longmapsto[su:sv:tu:tv].$$
Its image is $x_0x_3-x_1x_2=0$. The two rulings are the fibers of the two projections of $\mathbb P^1\times\mathbb P^1$; each fiber maps to a line. The hyperplane bundle is $\mathcal O(1,1)$.
:::

::: {.front card-id="example-scroll-bundle" tags="example construction"}
For $1\le a\le b$, construct the rational normal surface scroll $S(a,b)$ over $\mathbb C$ from a vector bundle. Give its ambient space, degree, and relation to a Hirzebruch surface.
:::

::: {.back card-id="example-scroll-bundle"}
Let $E=\mathcal O_{\mathbb P^1}(a)\oplus\mathcal O_{\mathbb P^1}(b)$ and let $\mathbb P(E)$ parametrize one-dimensional quotients. Its tautological bundle embeds it in $\mathbb P^{a+b+1}$, with each bundle fiber mapping to a line. The image has degree $a+b$.

As an abstract surface it is $\mathbb F_{b-a}$. If $C_0^2=-(b-a)$ and $f$ is a fiber, the hyperplane class is $C_0+bf$.
:::

::: {.front card-id="example-scroll-equations" tags="example construction"}
For $1\le a\le b$, give homogeneous equations for $S(a,b)\subset\mathbb P^{a+b+1}_{\mathbb C}$.
:::

::: {.back card-id="example-scroll-equations"}
With coordinates $x_0,\ldots,x_a,y_0,\ldots,y_b$, its homogeneous ideal is generated by the $2\times2$ minors of
$$\begin{pmatrix}x_0&\cdots&x_{a-1}&y_0&\cdots&y_{b-1}\\x_1&\cdots&x_a&y_1&\cdots&y_b\end{pmatrix}.$$
For each $[s:t]\in\mathbb P^1$, join the corresponding points of the degree-$a$ and degree-$b$ rational normal curves in disjoint coordinate subspaces. The union of these lines is the scroll.
:::

::: {.front card-id="example-cubic-scroll" tags="example construction"}
Give equations for a smooth cubic scroll in $\mathbb P^4_{\mathbb C}$. Describe it as a blowup and identify its hyperplane class.
:::

::: {.back card-id="example-cubic-scroll"}
The scroll $S(1,2)$ has ideal
$$I=(x_0y_1-x_1y_0,\ x_0y_2-x_1y_1,\ y_0y_2-y_1^2).$$
It is $\mathbb F_1\cong\operatorname{Bl}_p\mathbb P^2$. If $L$ is the pullback of a line and $E$ the exceptional curve, its embedding is defined by $|2L-E|$, the conics through $p$. The exceptional curve and the strict transforms of lines through $p$ map to lines.
:::

::: {.front card-id="example-scroll-cone" tags="example construction"}
For $b\ge2$, describe the image of $\mathbb P(\mathcal O\oplus\mathcal O(b))$ under its tautological linear system. Compare it with a smooth scroll.
:::

::: {.back card-id="example-scroll-cone"}
Its image $S(0,b)\subset\mathbb P^{b+1}$ is the cone over the degree-$b$ rational normal curve. The section corresponding to the quotient onto $\mathcal O$ has self-intersection $-b$ and contracts to the vertex. The cone has degree $b$ and is singular at the vertex. For $b=2$ its equation is $y_0y_2-y_1^2=0$ with the remaining coordinate free.
:::

::: {.front card-id="example-veronese-surface" tags="example construction"}
Construct the Veronese surface in $\mathbb P^5_{\mathbb C}$ and give its homogeneous ideal. Does it contain a line?
:::

::: {.back card-id="example-veronese-surface"}
Use $[s:t:u]\mapsto[s^2:t^2:u^2:st:su:tu]$. In coordinates $[a:b:c:d:e:f]$, the ideal is generated by the $2\times2$ minors of
$$\begin{pmatrix}a&d&e\\d&b&f\\e&f&c\end{pmatrix}.$$
The image has degree four. Every curve in it has even degree, since the hyperplane bundle pulls back to $\mathcal O_{\mathbb P^2}(2)$. Thus it contains no line.
:::

::: {.front card-id="example-quadric-bidegree" tags="example construction"}
Over $\mathbb C$, construct curves of bidegree $(a,b)$ on a smooth quadric, with $a,b\ge1$. For a smooth member, compute its degree and the degrees of its projections to the ruling parameter spaces.
:::

::: {.back card-id="example-quadric-bidegree"}
Identify the quadric with $\mathbb P^1_{[s:t]}\times\mathbb P^1_{[u:v]}$ by the Segre embedding. A bihomogeneous polynomial $F(s,t;u,v)$ of degrees $a,b$ defines such a curve. A general member is smooth and connected. Its degree in $\mathbb P^3$ is
$$ (a,b)\cdot(1,1)=a+b.$$
The projections onto the first and second factors have degrees $b$ and $a$, respectively, by intersecting with their fibers.
:::

::: {.front card-id="example-rational-space-quartic" tags="example construction"}
Construct a smooth rational quartic in $\mathbb P^3_{\mathbb C}$. Compare its linear series with that of the rational normal quartic.
:::

::: {.back card-id="example-rational-space-quartic"}
Take the graph of $[s:t]\mapsto[s^3:t^3]$ in $\mathbb P^1\times\mathbb P^1$ and apply Segre:
$$[s:t]\longmapsto[s^4:st^3:ts^3:t^4].$$
The graph has bidegree $(3,1)$ and is isomorphic to $\mathbb P^1$. The resulting embedding has degree four. It uses a four-dimensional subspace of $H^0(\mathbb P^1,\mathcal O(4))$; the full five-dimensional space gives the rational normal quartic in $\mathbb P^4$. The space quartic is not linearly normal.
:::

::: {.front card-id="example-canonical-genus-four" tags="example construction"}
Construct a canonical genus-four curve over $\mathbb C$ as a complete intersection. Recover its degree and canonical bundle from its equations.
:::

::: {.back card-id="example-canonical-genus-four"}
Take a smooth complete intersection $C=V(Q,F)\subset\mathbb P^3$ with $\deg Q=2$ and $\deg F=3$. General choices give a smooth curve. Bézout and adjunction give
$$\deg C=6,\qquad K_C\cong\mathcal O_C(2+3-4)=\mathcal O_C(1).$$
Thus $2g-2=6$ and $g=4$; the embedding is canonical. Every smooth nonhyperelliptic genus-four curve has this form.
:::

::: {.front card-id="example-genus-four-pencils" tags="example application"}
Let a smooth canonical genus-four curve over $\mathbb C$ lie on a smooth quadric or on a quadric cone. How do the rulings give its trigonal pencils?
:::

::: {.back card-id="example-genus-four-pencils"}
On a smooth quadric the curve has bidegree $(3,3)$. Each ruling restricts to a degree-three map to $\mathbb P^1$, giving two distinct trigonal pencils. On a quadric cone there is one ruling and one trigonal pencil. A smooth complete intersection curve avoids the vertex, so the ruling map is defined everywhere on the curve. These exhaust the trigonal pencils in each case.
:::

::: {.front card-id="example-canonical-genus-five" tags="example construction"}
Construct a canonical genus-five curve over $\mathbb C$ from quadrics. Which nonhyperelliptic genus-five curves fail to have this construction?
:::

::: {.back card-id="example-canonical-genus-five"}
A general intersection of three quadrics in $\mathbb P^4$ is a smooth curve $C$ with
$$\deg C=8,\qquad K_C\cong\mathcal O_C(2+2+2-5)=\mathcal O_C(1).$$
Hence $g=5$ and this is the canonical embedding. A nonhyperelliptic genus-five curve is such a complete intersection exactly when it is nontrigonal. For a trigonal curve, its containing quadrics cut out a cubic scroll surface; further cubic equations are needed to cut out the curve.
:::

::: {.front card-id="example-blowup-plane-charts" tags="example construction"}
Construct $\operatorname{Bl}_0\mathbb A^2_{\mathbb C}$ by an incidence equation. Give its affine charts, exceptional divisor, and normal bundle of that divisor.
:::

::: {.back card-id="example-blowup-plane-charts"}
Inside $\mathbb A^2_{x,y}\times\mathbb P^1_{[u:v]}$ take $xv=yu$, with projection to $(x,y)$. On $u\ne0$, put $q=v/u$, obtaining $y=xq$ and coordinates $(x,q)$. On $v\ne0$, put $p=u/v$, obtaining $x=yp$ and coordinates $(y,p)$.

The exceptional divisor is $E=\{0\}\times\mathbb P^1$, cut out by $x=0$ and $y=0$ in the respective charts. The blowup is the total space of $\mathcal O_{\mathbb P^1}(-1)$ and $N_{E/\operatorname{Bl}_0\mathbb A^2}\cong\mathcal O_{\mathbb P^1}(-1)$.
:::


::: {.front card-id="example-plane-cremona" tags="example construction"}
Give the standard quadratic Cremona transformation of $\mathbb P^2_{\mathbb C}$, its inverse, base points, and contracted curves.
:::

::: {.back card-id="example-plane-cremona"}
The map is $[x:y:z]\dashrightarrow[yz:xz:xy]$. Its base points are the three coordinate points. Each coordinate line contracts to the opposite coordinate point. On $xyz\ne0$, applying the map twice gives $[x:y:z]$, so it is its own rational inverse.
:::

::: {.front card-id="example-cremona-resolution" tags="example application"}
Resolve the standard quadratic Cremona transformation by a blowup. Express the pullback of a target line and the contracted curves as divisor classes.
:::

::: {.back card-id="example-cremona-resolution"}
Blow up the three coordinate points of $\mathbb P^2$, with exceptional classes $E_1,E_2,E_3$ and line pullback $H$. The conics through these points define a morphism to the target plane with line pullback
$$H'=2H-E_1-E_2-E_3.$$
The strict transforms of the coordinate lines have classes $H-E_i-E_j$ for $i<j$. They are disjoint $(-1)$-curves, have zero intersection with $H'$, and are contracted by this morphism.
:::

::: {.front card-id="example-cubic-surface-blowup" tags="example construction"}
Construct a smooth cubic surface over $\mathbb C$ from a plane blowup. State the conditions on the points and the embedding linear system.
:::

::: {.back card-id="example-cubic-surface-blowup"}
Blow up six distinct points of $\mathbb P^2$, with no three collinear and not all six on a conic. With line pullback $H$ and exceptional curves $E_i$, the anticanonical system is
$$|-K_S|=|3H-E_1-\cdots-E_6|.$$
It embeds $S$ into $\mathbb P^3$ as a smooth cubic surface: $(-K_S)^2=9-6=3$. Every smooth complex cubic surface arises this way.
:::

::: {.front card-id="example-cubic-surface-lines" tags="example application"}
On a cubic surface obtained by blowing up six plane points in general position, identify all lines by their divisor classes and plane constructions.
:::

::: {.back card-id="example-cubic-surface-lines"}
The classes are
$$E_i,\qquad H-E_i-E_j\ (i<j),\qquad 2H-\sum_{j\ne i}E_j.$$
They represent exceptional curves, strict transforms of lines through pairs of points, and strict transforms of conics through five points. There are respectively $6$, $15$, and $6$. Each has self-intersection $-1$ and anticanonical degree one, so its anticanonical image is a line.
:::

::: {.front card-id="example-del-pezzo-degree-four" tags="example construction"}
Construct a del Pezzo surface of degree four over $\mathbb C$ both as a plane blowup and by equations in projective space.
:::

::: {.back card-id="example-del-pezzo-degree-four"}
Blow up five distinct points of $\mathbb P^2$ with no three collinear. The anticanonical system $|3H-\sum_{i=1}^5E_i|$ embeds the surface in $\mathbb P^4$ as an intersection of two quadrics.

An explicit smooth model, for distinct $\lambda_0,\ldots,\lambda_4\in\mathbb C$, is
$$\sum_{i=0}^4x_i^2=0,\qquad\sum_{i=0}^4\lambda_i x_i^2=0.$$
Adjunction gives $-K_S=\mathcal O_S(1)$ and $K_S^2=4$.
:::

::: {.front card-id="example-klein-quadric" tags="example construction"}
Construct $\operatorname{Gr}(2,4)$ in Plücker coordinates over $\mathbb C$. Give its defining equation and interpret its points geometrically.
:::

::: {.back card-id="example-klein-quadric"}
For a plane spanned by $u,v\in\mathbb C^4$, put $p_{ij}=u_iv_j-u_jv_i$. Changing the basis rescales all coordinates by its determinant. The image in $\mathbb P^5$ is the smooth quadric
$$p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0.$$
This is the decomposability condition for $u\wedge v$. Its points parametrize two-dimensional vector subspaces of $\mathbb C^4$, equivalently projective lines in $\mathbb P^3$.
:::



::: {.front card-id="example-double-line" tags="example construction"}
Describe the projective double line $D=V(X^2)\subset\mathbb P^2_{\mathbb C}$ scheme-theoretically. Give its reduction, associated prime, and Hilbert polynomial.
:::

::: {.back card-id="example-double-line"}
Its homogeneous ring is $\mathbb C[X,Y,Z]/(X^2)$ and its reduction is the line $L=V(X)$. The class of $X$ is a nonzero square-zero element. The only associated prime is $(X)$, so there is no embedded associated point. The sequence
$$0\longrightarrow\mathcal O_L(-1)\longrightarrow\mathcal O_D\longrightarrow\mathcal O_L\longrightarrow0$$
gives $P_D(m)=m+(m+1)=2m+1$.
:::

::: {.front card-id="example-line-embedded-point" tags="example construction"}
Give an affine line with an embedded point over $\mathbb C$. Compute a primary decomposition and its associated primes.
:::

::: {.back card-id="example-line-embedded-point"}
Take $A=\mathbb C[x,y]/(x^2,xy)$. In $\mathbb C[x,y]$,
$$(x^2,xy)=(x)\cap(x^2,y).$$
The associated primes are $(x)$ and $(x,y)$. The reduction is the line $x=0$, and the origin is embedded. The nonzero nilpotent class of $x$ is annihilated by $(x,y)$; away from the origin it vanishes because $y$ is invertible and $xy=0$.
:::

::: {.front card-id="card-3f53ea5eafc329a2" tags="definition"}
What is the definition of Anticanonical system?
:::

::: {.back card-id="card-3f53ea5eafc329a2"}
The anticanonical system of a normal variety $X$ is the complete linear system $|-K_X|$ of effective divisors linearly equivalent to $-K_X$; its associated rational map is the anticanonical map.
:::


::: {.front card-id="card-29597195b8ada34a" tags="definition"}
What is the definition of Bézout's theorem?
:::

::: {.back card-id="card-29597195b8ada34a"}
If projective varieties $X_1,\dots,X_r\subset\mathbb P^n_k$ of degrees $d_1,\dots,d_r$ meet in finitely many points, then $\sum_p i(X_1,\dots,X_r;p)=d_1\cdots d_r$, where $i$ is the intersection multiplicity; more generally, when the intersection has the expected dimension, $\deg(X_1\cap\cdots\cap X_r)=d_1\cdots d_r$.
:::

::: {.front card-id="card-e689ca1225015881" tags="definition"}
What is the definition of Homogeneous ring?
:::

::: {.back card-id="card-e689ca1225015881"}
For a closed subscheme $X\subset\mathbb P^n_k$ with homogeneous ideal $I$, the homogeneous coordinate ring is $R(X)=k[x_0,\dots,x_n]/I=\bigoplus_{m\ge0}H^0(X,\mathcal O_X(m))$.
:::

::: {.front card-id="card-1de60a8a7a9e9277" tags="definition"}
What is the definition of J-invariant?
:::

::: {.back card-id="card-1de60a8a7a9e9277"}
For a short Weierstrass model $y^2=x^3+a_4x+a_6$ over a field of characteristic different from $2,3$,
$$j(E)=1728\,\frac{4a_4^3}{4a_4^3+27a_6^2}.$$
In arbitrary characteristic, use $j=c_4^3/\Delta$ from a generalized Weierstrass equation. Over an algebraically closed field, two elliptic curves are isomorphic as pointed curves iff their $j$-invariants agree. Over a nonclosed field, twists can share $j$ without being isomorphic.
:::

::: {.front card-id="card-cbddcb3e60505698" tags="definition"}
What is the definition of Linearly normal?
:::

::: {.back card-id="card-cbddcb3e60505698"}
A projective variety $X\subset\mathbb P^n$ is linearly normal if the restriction map $H^0(\mathbb P^n,\mathcal O(1))\to H^0(X,\mathcal O_X(1))$ is surjective; equivalently $X$ is not obtained by projecting a nondegenerate variety in $\mathbb P^{n+1}$ from a point.
:::

::: {.front card-id="card-bdb2b9814086f7ac" tags="definition"}
What is the definition of Tangent cone?
:::

::: {.back card-id="card-bdb2b9814086f7ac"}
For a closed point $p\in X$ with maximal ideal $\mathfrak m_p$, the tangent cone is $C_pX=\operatorname{Spec}(\mathrm{gr}_{\mathfrak m_p}\mathcal O_{X,p})$, the cone in the Zariski tangent space $T_pX$ cut out by the leading homogeneous forms of the ideal of $X$ at $p$.
:::
