---
title: "Algebraic Geometry::Singularities::Birational Classes"
---

::: {.front card-id="definition-log-canonical-threshold" tags="definition application"}
Define the log canonical threshold of an effective divisor on a smooth complex variety. How do discrepancies compute it? Compare a node and a cusp.
:::

::: {.back card-id="definition-log-canonical-threshold"}
For a nonzero effective divisor $D$ on smooth $X$,
$$\operatorname{lct}_p(X,D)=\sup\{c\ge0:(X,cD)\text{ is log canonical near }p\}.$$
On a log resolution $\pi:Y\to X$, write $\pi^*D=\sum b_iE_i$ and $K_Y-\pi^*K_X=\sum a_iE_i$, including strict transforms with $a_i=0$. Then
$$\operatorname{lct}_p(X,D)=\min_{\substack{b_i>0\\p\in\pi(E_i)}}\frac{a_i+1}{b_i}.$$
The numerator is the log discrepancy. This gives a threshold for how much boundary can be added before log canonicity fails.

At the origin, $x^ay^b=0$ has threshold $\min(1/a,1/b)$ for positive integers $a,b$. A node $xy=0$ therefore has threshold one; the cusp $y^2-x^3=0$ has threshold $5/6$. Multiplicity alone does not distinguish these singularities.

[Reference: log resolutions and thresholds, §2.6](https://people.math.harvard.edu/~mpopa/notes/DMBG-posted.pdf).
:::

::: {.front card-id="singularity-pair-discrepancies" tags="definition"}
Define discrepancies and log discrepancies for a complex pair $(X,\Delta)$ and state the klt and log canonical conditions.
:::

::: {.back card-id="singularity-pair-discrepancies"}
Assume $X$ normal, $\Delta\ge0$ a $\mathbb Q$-divisor, and $K_X+\Delta$ $\mathbb Q$-Cartier. For $f:Y\to X$ birational with $Y$ smooth, write
$$K_Y=f^*(K_X+\Delta)+\sum_E a(E,X,\Delta)E,\qquad A(E,X,\Delta)=1+a(E,X,\Delta).$$
Include strict transforms of boundary components in the sum. The pair is klt if every $A(E,X,\Delta)>0$, and log canonical if every $A(E,X,\Delta)\ge0$, over all prime divisors on all birational models. A boundary component of coefficient $b$ has discrepancy $-b$.
:::

::: {.front card-id="singularity-rational-definition" tags="definition"}
Define rational singularities for a normal complex variety $X$.
:::

::: {.back card-id="singularity-rational-definition"}
For one, equivalently every, resolution $f:Y\to X$,
$$R^if_*\mathcal O_Y=0\quad(i>0).$$
Normality gives $f_*\mathcal O_Y=\mathcal O_X$.
:::

::: {.front card-id="singularity-dlt-definition" tags="definition"}
Define a divisorially log terminal pair $(X,\Delta)$ over $\mathbb C$.
:::

::: {.back card-id="singularity-dlt-definition"}
Assume $X$ normal, $\Delta$ an effective $\mathbb Q$-divisor with coefficients at most $1$, and $K_X+\Delta$ $\mathbb Q$-Cartier. The pair is dlt if there exists a proper birational morphism $f:Y\to X$ such that:

- $Y$ is smooth;
- the exceptional locus is a divisor (possibly empty), and its union with the support of the strict transform $f_*^{-1}\Delta$ has simple normal crossings;
- every $f$-exceptional prime divisor $E$ satisfies $a(E,X,\Delta)>-1$.

The first two conditions say that $f$ is a log resolution. The last condition is required on at least one such resolution. For two coefficient-one coordinate axes on $\mathbb A^2$, the identity meets all three conditions: the axes have simple normal crossings and there are no exceptional divisors to test. Blowing up their intersection produces discrepancy $-1$, so that resolution fails the last condition. The pair remains dlt. Requiring the inequality for every exceptional divisor over $X$ would instead give plt.
:::

::: {.front card-id="singularity-snc-pair-example" tags="application"}
Let $D_1,D_2$ be the coordinate axes in $\mathbb A^2_{\mathbb C}$. For $a,b\ge0$, when is $(\mathbb A^2,aD_1+bD_2)$ klt or log canonical? What discrepancy appears on blowing up the origin? Refine the classification to plt and dlt, and identify the lc centers.
:::

::: {.back card-id="singularity-snc-pair-example"}
It is klt iff $a,b<1$, and log canonical iff $a,b\le1$. The exceptional divisor has
$$a(E,\mathbb A^2,aD_1+bD_2)=1-a-b.$$
For $a=b=1$ the pair is dlt and log canonical, but not klt.

| Coefficients | Classification | lc centers |
| --- | --- | --- |
| $a,b<1$ | klt, hence plt and dlt | None |
| $a=1,\ b<1$ | plt, not klt | $D_1$ |
| $a<1,\ b=1$ | plt, not klt | $D_2$ |
| $a=b=1$ | dlt, not plt | $D_1,D_2,\{0\}$ |
| $\max(a,b)>1$ | Not lc | The lc-center terminology above assumes an lc pair |

In the double coefficient-one case, the axes themselves have discrepancy $-1$, and the exceptional curve of the blowup supplies the center $\{0\}$. The non-klt locus is still just $D_1\cup D_2$; listing its irreducible components alone misses the smaller lc center.
:::

::: {.front card-id="singularity-surface-class-examples" tags="application"}
Classify the surface germs $xy=z^2$ and $\frac13(1,1)$ as terminal, canonical, or klt.
:::

::: {.back card-id="singularity-surface-class-examples"}
The $A_1$ germ $xy=z^2$ is canonical and klt but not terminal: its exceptional $(-2)$-curve has discrepancy $0$. The quotient $\frac13(1,1)$ has a single exceptional $(-3)$-curve with discrepancy $-1/3$, so it is klt but not canonical. Terminal complex surface singularities are smooth.
:::

::: {.front card-id="singularity-slc-node-example" tags="application"}
Why is the curve germ $xy=0$ semi-log-canonical but not log canonical as a variety? Compare it with the same equation used as a boundary on $\mathbb A^2$.
:::

::: {.back card-id="singularity-slc-node-example"}
It is not normal, so it does not satisfy the normality hypothesis for log canonical varieties. Its normalization is two smooth branches, each with the origin as conductor boundary of coefficient $1$. Those pairs are log canonical, and the nodal curve is Gorenstein and satisfies $S_2$, so it is slc.

For $D=V(xy)\subset\mathbb A^2$, the ambient pair $(\mathbb A^2,D)$ is dlt and lc, but not plt. Here normality is required of $\mathbb A^2$, not of the boundary $D$. Thus the same equation gives an slc variety and the boundary of an lc pair; these are different objects.
:::

::: {.front card-id="card-704cc7c711f84485"}
For a normal complex variety $X$ with $K_X$ $\mathbb Q$-Cartier, define terminal, canonical, and klt singularities by discrepancies.
:::

::: {.back card-id="card-704cc7c711f84485"}
For every prime exceptional divisor $E$ on a smooth birational model $f:Y\to X$, use
$$K_Y=f^*K_X+\sum_E a(E,X)E.$$
Terminal means $a(E,X)>0$; canonical means $a(E,X)\ge0$; klt means $a(E,X)>-1$, for all such $E$.
:::

::: {.front card-id="theorem-rational-singularities" tags="theorem"}
Let $Y$ be a complex variety with rational singularities and $f:X\to Y$ a resolution. State the direct-image identities. What do klt singularities imply?
:::

::: {.back card-id="theorem-rational-singularities"}
One has
$$f_*\mathcal O_X=\mathcal O_Y,\qquad R^if_*\mathcal O_X=0\quad(i>0).$$
A normal complex variety with klt singularities has rational singularities. Rational singularities are Cohen–Macaulay, so klt varieties are Cohen–Macaulay.
:::

::: {.front card-id="card-a07cec7de306d8eb"}
What is a log canonical center of a log canonical pair $(X,\Delta)$?
:::

::: {.back card-id="card-a07cec7de306d8eb"}
A subvariety $c_X(E)$ that is the center of a prime divisor over $X$ with $a(E,X,\Delta)=-1$. The union of these centers is the non-klt locus.
:::

::: {.front card-id="card-e65c8bbc605edf10"}
Define a semi-log-canonical pair $(X,\Delta)$ over $\mathbb C$, including its normalization criterion.
:::

::: {.back card-id="card-e65c8bbc605edf10"}
The scheme $X$ is reduced, equidimensional, of finite type, satisfies $S_2$, and has only nodes or regular points in codimension one. The effective $\mathbb Q$-divisor $\Delta$ has no component in the codimension-one singular locus, and $K_X+\Delta$ is $\mathbb Q$-Cartier.
For the normalization $\nu:\bar X\to X$, reduced conductor divisor $B$, and strict transform $\bar\Delta$, the pair $(\bar X,B+\bar\Delta)$ is log canonical:
$$K_{\bar X}+B+\bar\Delta=\nu^*(K_X+\Delta).$$
:::

::: {.front card-id="singularity-pair-hierarchy" tags="definition application"}
Organize klt, plt, dlt, and lc pairs into an implication chain. Compare their discrepancy tests and give a simple example separating each adjacent class.
:::

::: {.back card-id="singularity-pair-hierarchy"}
Work over $\mathbb C$ with $X$ normal, $0\le\Delta\le1$, and $K_X+\Delta$ $\mathbb Q$-Cartier. Write $A(E)=a(E)+1$. Then
$$\mathrm{klt}\ \Longrightarrow\ \mathrm{plt}\ \Longrightarrow\ \mathrm{dlt}\ \Longrightarrow\ \mathrm{lc}.$$

| Class | Discrepancy test |
| --- | --- |
| Kawamata log terminal (klt) | $A(E)>0$ for every prime divisor over $X$, including divisors on $X$ |
| Purely log terminal (plt) | $A(E)>0$ for every exceptional prime divisor over $X$ |
| Divisorially log terminal (dlt) | Some log resolution has $A(E)>0$ for every exceptional divisor on that resolution |
| Log canonical (lc) | $A(E)\ge0$ for every prime divisor over $X$, including divisors on $X$ |

Here a log resolution is a proper birational $f:Y\to X$ with $Y$ smooth and exceptional locus a divisor (possibly empty), whose union with the support of $f_*^{-1}\Delta$ has simple normal crossings.

- **plt, not klt:** $(\mathbb A^2,D_1)$ for a coordinate axis $D_1$; $A(D_1)=0$.
- **dlt, not plt:** $(\mathbb A^2,D_1+D_2)$ for both axes; the identity witnesses dlt, but blowing up their intersection gives $A(E)=0$.
- **lc, not dlt:** the affine cone over a smooth plane cubic, with zero boundary; its exceptional elliptic curve has $A(E)=0$.

For $\Delta=0$, klt, plt, and dlt coincide. The differences between them concern how coefficient-one boundary components meet and behave.

[Reference: Kollár, Definition 13 and discussion](https://web.math.princeton.edu/~kollar/book/chap2.pdf).
:::

::: {.front card-id="singularity-variety-hierarchy" tags="definition application"}
Compare terminal, canonical, klt, and lc complex varieties in one discrepancy table. Separate the classes using familiar surface singularities. How does this differ from the hierarchy for pairs?
:::

::: {.back card-id="singularity-variety-hierarchy"}
Assume $X$ normal and $K_X$ $\mathbb Q$-Cartier, with zero boundary. For exceptional prime divisors over $X$:

| Class | Discrepancy $a(E,X)$ | Log discrepancy $A(E,X)$ |
| --- | --- | --- |
| Terminal | $>0$ | $>1$ |
| Canonical | $\ge0$ | $\ge1$ |
| klt | $>-1$ | $>0$ |
| lc | $\ge-1$ | $\ge0$ |

Thus
$$\text{smooth}\ \Longrightarrow\ \text{terminal}\ \Longrightarrow\ \text{canonical}\ \Longrightarrow\ \mathrm{klt}\ \Longrightarrow\ \mathrm{lc}.$$
The surface examples are:

- $xy=z^2$: canonical, not terminal; the exceptional $(-2)$-curve has $a=0$.
- $\frac13(1,1)$: klt, not canonical; the exceptional $(-3)$-curve has $a=-1/3$.
- A cone over a smooth plane cubic: lc, not klt; the exceptional elliptic curve has $a=-1$.

Terminal surfaces are smooth. This equivalence is special to surfaces: the threefold ordinary double point $xy-zw=0$ is singular and terminal; blowing up its vertex gives a smooth resolution with exceptional quadric and discrepancy $1$.

Divisors already on $X$ have $a=0$ when $\Delta=0$, so terminality must test exceptional divisors. For pairs with boundary, use the separate klt–plt–dlt–lc chain; the zero-boundary implication canonical $\Rightarrow$ klt must not be applied to arbitrary boundary pairs. For example $(\mathbb A^2,D_1)$ has nonnegative exceptional discrepancies but is not klt.
:::

::: {.front card-id="singularity-log-resolution-test" tags="definition application"}
What is a log resolution of a complex pair? How does it turn the klt/lc conditions into a finite calculation? Give the discrepancy formula for blowing up a smooth center, including boundary contributions.
:::

::: {.back card-id="singularity-log-resolution-test"}
For normal $X$ and an effective $\mathbb Q$-divisor $\Delta$ with $K_X+\Delta$ $\mathbb Q$-Cartier, a log resolution is a proper birational morphism $f:Y\to X$ with $Y$ smooth, exceptional locus a divisor, and
$$\operatorname{Exc}(f)\cup\operatorname{Supp}(f_*^{-1}\Delta)$$
a simple normal crossings divisor. In characteristic zero one can choose it to be an isomorphism over the locus where the pair is already simple normal crossings.

Compute
$$K_Y+\Delta_Y=f^*(K_X+\Delta),\qquad a(E,X,\Delta)=-\operatorname{coeff}_E\Delta_Y.$$
The divisor $\Delta_Y$ may have negative coefficients. Check every component of $\Delta_Y$, including strict transforms:

- klt iff every coefficient is $<1$;
- lc iff every coefficient is $\le1$.

These tests on a log resolution control further blowups. Checking only exceptional components misses a boundary coefficient greater than one even when $X$ is smooth.

For the blowup of a smooth center $Z$ of codimension $c\ge2$ in smooth $X$, with $\Delta=\sum b_iD_i$,
$$K_Y=f^*K_X+(c-1)E,\qquad f^*D_i=D_i'+m_iE,\qquad m_i=\operatorname{mult}_Z D_i,$$
so
$$a(E,X,\Delta)=c-1-\sum_i b_im_i,\qquad A(E,X,\Delta)=c-\sum_i b_im_i.$$
The axes give $a(E)=1-a-b$. This calculation detects a violating divisor immediately; passing it alone is not sufficient unless the chosen morphism resolves the whole pair.

[Reference: Kollár, Lemma 15 and Corollary 17](https://web.math.princeton.edu/~kollar/book/chap2.pdf).
:::

::: {.front card-id="singularity-plane-cone-repertoire" tags="application"}
Let $C_d\subset\mathbb P^2$ be a smooth plane curve of degree $d\ge2$, and let $X_d$ be its affine cone. Use one blowup to compare its discrepancy, rationality, and lc behavior as $d$ changes.
:::

::: {.back card-id="singularity-plane-cone-repertoire"}
Blowing up the vertex gives $f:Y\to X_d$ with exceptional curve $E=C_d$ and $E^2=-d$. The cone is a normal hypersurface, hence Gorenstein, and
$$K_Y=f^*K_{X_d}+aE.$$
Adjunction gives
$$(a+1)E^2=(K_Y+E)E=2g(C_d)-2=d(d-3),\qquad a=2-d.$$

| Degree | Exceptional curve | Discrepancy | Singularity |
| --- | --- | --- | --- |
| $2$ | $\mathbb P^1$, square $-2$ | $0$ | $A_1$: canonical, klt, rational, not terminal |
| $3$ | Elliptic, square $-3$ | $-1$ | Simple elliptic: lc, not klt, not rational |
| $d\ge4$ | Genus $(d-1)(d-2)/2$ | $\le-2$ | Not lc, not rational |

For $d\ge3$, $H^1(C_d,\mathcal O_{C_d})\ne0$ obstructs rational singularities of the cone. Thus a normal Gorenstein, Cohen–Macaulay singularity need not be rational or lc. Changing the degree of the same construction supplies both counterexamples.
:::

::: {.front card-id="singularity-adjunction-boundary-comparison" tags="theorem application"}
How do adjunction and inversion of adjunction compare ambient plt/lc pairs with singularities on a boundary divisor? Compute the boundary for coordinate axes and for a cyclic quotient.
:::

::: {.back card-id="singularity-adjunction-boundary-comparison"}
Let $X$ be normal over $\mathbb C$, $S$ a normal prime divisor, and $\Delta\ge0$ with $S\not\subset\operatorname{Supp}\Delta$ and $K_X+S+\Delta$ $\mathbb Q$-Cartier. Adjunction defines the different $B_S=\operatorname{Diff}_S(\Delta)$ by the residue construction, with
$$(K_X+S+\Delta)|_S=K_S+B_S.$$
Then
$$\begin{aligned}
(X,S+\Delta)\text{ plt near }S&\iff(S,B_S)\text{ klt},\\
(X,S+\Delta)\text{ lc near }S&\iff(S,B_S)\text{ lc}.
\end{aligned}$$
For a nonnormal $S$, lc inversion of adjunction uses its normalization and the different there, including the conductor contribution. Plt forces $S$ to be normal.

- For smooth $X$ and $S$, $B_S=\Delta|_S$. On $\mathbb A^2$, take $S=(x=0)$ and $\Delta=b(y=0)$. Then $B_S=b[0]$: plt holds for $b<1$, lc for $b\le1$.
- For $X=\mathbb A^2/\mu_r$, with $\zeta(u,v)=(\zeta u,\zeta v)$ and $r\ge2$, let $S$ be the image of $(u=0)$. Then $S\cong\mathbb A^1$ and $\operatorname{Diff}_S(0)=(1-1/r)[0]$. On the cover of $S$, $t=v^r$ has ramification order $r-1$, so $r\,\operatorname{coeff}_0 B_S=r-1$. Even with $\Delta=0$, the different records the ambient quotient singularity.

[Reference: Kollár, Adjunction](https://web.math.princeton.edu/~kollar/book/chap2.pdf).
:::

::: {.front card-id="singularity-local-algebra-comparison" tags="definition application"}
For a normal complex variety, compare Cohen–Macaulay, Gorenstein, $\mathbb Q$-Gorenstein, factorial, and $\mathbb Q$-factorial. How do rational and canonical singularities connect to them? Give counterexamples to tempting converses.
:::

::: {.back card-id="singularity-local-algebra-comparison"}
| Property | Local condition |
| --- | --- |
| Cohen–Macaulay (CM) | $\operatorname{depth}\mathcal O_{X,x}=\dim\mathcal O_{X,x}$ for every $x$ |
| Gorenstein | CM and the dualizing sheaf $\omega_X$ is invertible |
| $\mathbb Q$-Gorenstein | $K_X$ is $\mathbb Q$-Cartier; equivalently some positive reflexive power $\omega_X^{[m]}=(\omega_X^{\otimes m})^{**}$ is invertible locally |
| Locally factorial | Every Weil divisor is Cartier; local rings are UFDs |
| $\mathbb Q$-factorial | Every Weil divisor has a positive Cartier multiple |

Thus Gorenstein implies CM and $\mathbb Q$-Gorenstein, while factorial implies $\mathbb Q$-factorial implies $\mathbb Q$-Gorenstein. The latter conditions concern all Weil divisors versus just the canonical class. Cartier $K_X$ alone does not imply Gorenstein: CM is also required.

Over $\mathbb C$,
$$\text{canonical}\ \Longrightarrow\ \mathrm{klt}\ \Longrightarrow\ \text{rational}\ \Longrightarrow\ \mathrm{CM}.$$
For normal Gorenstein varieties, rational, canonical, and klt are equivalent: Cartier $K_X$ makes discrepancies integral, and rational Gorenstein singularities are canonical.

- $\frac13(1,1)$ is klt, rational, CM, and $\mathbb Q$-factorial, but not Gorenstein or canonical. The form $du\wedge dv$ transforms by $\zeta^2$, giving canonical index $3$.
- The cone over a smooth plane cubic is Gorenstein and CM, but not rational.
- The $A_1$ surface germ has local class group $\mathbb Z/2$: it is Gorenstein and $\mathbb Q$-factorial, but not factorial.
- The threefold node $xy-zw=0$ is Gorenstein, terminal, and rational, but not $\mathbb Q$-factorial: its local class group is $\mathbb Z$.
- A cone over an Enriques surface embedded by a very ample line bundle with projectively normal image is rational and $\mathbb Q$-Gorenstein but not klt. Rationality does not reverse the klt implication even after imposing the rational Cartier hypothesis.

[Reference: Popa, rational singularities and Gorenstein comparison](https://people.math.harvard.edu/~mpopa/265/Math265-notes.pdf).
:::

::: {.front card-id="singularity-cone-cartier-comparison" tags="application"}
Compare the affine cones over $\mathbb P^1\times\mathbb P^1$ polarized by $\mathcal O(1,1)$ and by $\mathcal O(1,2)$. What do they show about rational singularities, $\mathbb Q$-Gorenstein, and $\mathbb Q$-factorial?
:::

::: {.back card-id="singularity-cone-cartier-comparison"}
Write $V=\mathbb P^1\times\mathbb P^1$, $L=\mathcal O(a,b)$ with $a,b>0$, and
$$X_L=\operatorname{Spec}\bigoplus_{m\ge0}H^0(V,L^m).$$
These embeddings are projectively normal. The blowup of the vertex is the total space of $L^{-1}$. Künneth gives
$$H^i(V,L^m)=0\quad(i>0,\ m\ge0),$$
so both cones have rational singularities.

At the vertex the divisor class group is
$$\operatorname{Pic}(V)/\mathbb Z[L]=\mathbb Z^2/\mathbb Z(a,b).$$
The canonical class is represented by $K_V=(-2,-2)$. Hence $X_L$ is $\mathbb Q$-Gorenstein exactly when $K_V$ is rationally proportional to $L$.

| Polarization | Cone |
| --- | --- |
| $(1,1)$ | The threefold node $xy-zw=0$; $K_V=-2L$, so $K_{X_L}$ is Cartier |
| $(1,2)$ | Rational, but not $\mathbb Q$-Gorenstein: $(-2,-2)$ is not proportional to $(1,2)$ |

Both class groups have positive rank, so neither cone is $\mathbb Q$-factorial. Thus rationality alone does not even guarantee that the usual zero-boundary discrepancy classes are defined. The $\mathbb Q$-Cartier hypothesis must be checked.
:::

::: {.front card-id="singularity-torsion-canonical-cones" tags="application"}
Use cones over familiar surfaces with torsion canonical bundle to separate lc, rational, Cohen–Macaulay, and Gorenstein singularities. Compare a product of elliptic curves, a K3 surface, and an Enriques surface.
:::

::: {.back card-id="singularity-torsion-canonical-cones"}
Let $V$ be one of these smooth complex surfaces and $L$ a very ample line bundle whose complete linear system embeds $V$ as a projectively normal variety. Set
$$X=\operatorname{Spec}\bigoplus_{m\ge0}H^0(V,L^m).$$
Blowing up the vertex gives the total space of $L^{-1}$ with exceptional divisor $V$. Since $K_V$ is torsion, $K_X$ is $\mathbb Q$-Cartier and the exceptional discrepancy is $-1$: these cones are lc, not klt, and therefore Du Bois.

Kodaira vanishing removes higher cohomology of $L^m$ for $m>0$. The remaining degree-zero cohomology distinguishes the cones:

| Base $V$ | $h^1(\mathcal O_V)$ | $h^2(\mathcal O_V)$ | Cone at its vertex |
| --- | --- | --- | --- |
| $E_1\times E_2$ | $2$ | $1$ | Not CM, not rational; $K_X$ Cartier but not Gorenstein |
| K3 | $0$ | $1$ | CM and Gorenstein, not rational |
| Enriques | $0$ | $0$ | Rational and CM; canonical index $2$, not Gorenstein |

For these surface bases, CM requires $H^1(V,L^m)=0$ for all integers $m$; Serre duality handles negative $m$. Rationality additionally requires vanishing of $H^2(V,L^m)$ for $m\ge0$. Thus lc and Du Bois need not imply CM, while rational and $\mathbb Q$-Gorenstein need not imply klt.

This is the same cone construction as the simple elliptic example, with the base replaced by a familiar surface.

[Reference: Kollár, Example 50](https://web.math.princeton.edu/~kollar/book/chap2.pdf).
:::

::: {.front card-id="singularity-du-bois-definition-use" tags="definition theorem application"}
Define Du Bois singularities. Place them relative to rational, lc/slc, and seminormal singularities, and state a cohomological use for proper varieties.
:::

::: {.back card-id="singularity-du-bois-definition-use"}
For a reduced complex variety $X$, let $\underline\Omega_X^0$ be the degree-zero graded piece of the filtered Du Bois complex. Equivalently, using a proper smooth hyperresolution $\epsilon:X_\bullet\to X$,
$$\underline\Omega_X^0\simeq R\epsilon_*\mathcal O_{X_\bullet}.$$
The variety is **Du Bois** if the natural map
$$\mathcal O_X\longrightarrow\underline\Omega_X^0$$
is a quasi-isomorphism.

| Sufficient condition | Consequence |
| --- | --- |
| Rational singularities | Du Bois |
| Log canonical singularities | Du Bois |
| Semi-log-canonical singularities | Du Bois |
| Du Bois | Seminormal |

Du Bois does not require normality: a nodal curve is Du Bois. The cone over a smooth plane cubic is Du Bois but not rational. A normal Gorenstein variety is Du Bois iff it is lc.

For proper Du Bois $X$, Hodge theory gives
$$\operatorname{Gr}_F^0H^i(X^{\mathrm{an}},\mathbb C)\cong H^i(X,\mathcal O_X).$$
In particular, the natural map from singular cohomology to coherent cohomology is surjective. This is a useful bridge when studying cohomology of singular fibers and stable varieties.

[Reference: Kovács–Schwede, Du Bois survey](https://sites.math.washington.edu/~kovacs/2013/papers/Kovacs_Schwede__Du_Bois_survey.pdf).
:::

::: {.front card-id="singularity-seminormal-node-cusp" tags="definition application"}
Define seminormality for a reduced complex affine variety. Use a node, a cusp, and a familiar normal cone to distinguish normality, seminormality, and Du Bois singularities.
:::

::: {.back card-id="singularity-seminormal-node-cusp"}
A reduced finitely generated $\mathbb C$-algebra $R$ is seminormal if, for $b$ in its total ring of fractions,
$$b^2,b^3\in R\quad\Longrightarrow\quad b\in R.$$
Equivalently, every finite birational extension inside its normalization that is bijective on prime spectra and induces isomorphisms on residue fields is already $R$. A variety is seminormal when its local rings are.

- **Node:** $\mathbb C[x,y]/(xy)$ is seminormal but not normal. Inside its normalization $\mathbb C[x]\oplus\mathbb C[y]$, it consists of pairs $(f,g)$ with $f(0)=g(0)$. Equality of both squares and cubes of the constant terms forces equality of the terms themselves. The node is also slc and Du Bois.
- **Cusp:** $\mathbb C[t^2,t^3]$ is not seminormal: $t^2,t^3$ lie in the ring but $t$ does not. Hence the cusp is not Du Bois. Its normalization being smooth does not suffice.
- **Cone over a smooth plane quartic:** normal, hence seminormal, and Gorenstein, but not lc, hence not Du Bois. Thus seminormality is strictly weaker than the Du Bois condition.

[References: Popa, §3.2](https://people.math.harvard.edu/~mpopa/265/Math265-notes.pdf); [Kovács–Schwede, Gorenstein Du Bois criterion](https://sites.math.washington.edu/~kovacs/2013/papers/Kovacs_Schwede__Du_Bois_survey.pdf).
:::

::: {.front card-id="singularity-epsilon-lc-definition-use" tags="definition application"}
Define $\epsilon$-lc and compare it with lc and klt. Test it on coordinate-axis boundaries. Why is a fixed positive $\epsilon$ useful in boundedness questions?
:::

::: {.back card-id="singularity-epsilon-lc-definition-use"}
For a normal complex pair $(X,\Delta)$ with $\Delta\ge0$ and $K_X+\Delta$ $\mathbb Q$-Cartier, and $\epsilon\ge0$, the pair is **$\epsilon$-log canonical** if
$$A(E,X,\Delta)=1+a(E,X,\Delta)\ge\epsilon$$
for every prime divisor over $X$, including divisors on $X$.

Thus $0$-lc is lc, and $\epsilon$-lc with $\epsilon>0$ implies klt. A fixed finite-type klt rational pair admits some positive $\epsilon$: a common Cartier index bounds discrepancy denominators. A collection of klt pairs need not admit a uniform positive $\epsilon$.

For $0\le a,b\le1$, the pair $(\mathbb A^2,aD_1+bD_2)$ is $\epsilon$-lc precisely when
$$\epsilon\le\min(1-a,1-b).$$
The axes give these bounds; further divisors over their intersection have log discrepancies at least their sum. In particular, $(\mathbb A^2,(1-1/m)D_1)$ is klt for every integer $m\ge1$, but its largest allowed $\epsilon$ is $1/m$.

Birkar's boundedness theorem fixes dimension $d$ and $\epsilon>0$: normal projective $\epsilon$-lc Fano varieties of dimension $d$ form a bounded family. The quantitative margin is part of the hypothesis.

[Reference: Birkar, Singularities of linear systems and boundedness of Fano varieties](https://arxiv.org/abs/1609.05543).
:::

::: {.front card-id="singularity-research-hypothesis-map" tags="application"}
Which singularity conditions should you check when applying vanishing, running the MMP, taking adjunction, constructing stable limits, or comparing coherent and singular cohomology?
:::

::: {.back card-id="singularity-research-hypothesis-map"}
| Research task | Useful condition and its role |
| --- | --- |
| Kawamata–Viehweg vanishing | A projective klt pair and a Cartier $D$ with $D-(K_X+\Delta)$ nef and big; lc alone does not supply this version |
| Cone/contraction and base-point-free arguments | Check the precise klt hypotheses and positivity in the theorem being used; $\mathbb Q$-factoriality is a separate condition needed for the usual $\mathbb Q$-factorial MMP setup |
| MMP starting from smooth varieties with zero boundary | Terminal singularities occur; canonical models have canonical singularities |
| Adjunction to a coefficient-one boundary | plt gives a normal boundary with klt different; dlt accommodates intersecting coefficient-one strata |
| Stable limits | slc allows nonnormal fibers; check the normalized pair with its conductor, as well as ampleness of the log canonical divisor |
| Cohomology via a resolution | Rational singularities give $R f_*\mathcal O_Y\simeq\mathcal O_X$ |
| Singular versus coherent cohomology | Proper Du Bois varieties identify $H^i(\mathcal O_X)$ with the zeroth Hodge graded piece |
| Uniform boundedness of Fano varieties | Fix dimension and a positive $\epsilon$-lc bound |

The class name supplies only the singularity hypothesis. Projectivity, Cartier conditions, positivity, and the precise boundary remain part of each application.
:::

