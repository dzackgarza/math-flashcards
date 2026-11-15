---
title: "Algebraic Geometry::Numerical Invariants::Surfaces"
---

::: {.front card-id="numerical-pencil-base-length" tags="formula application"}
Let a pencil in $|L|$ on a smooth complex projective surface have no fixed curve. What is the length of its base scheme? How does this relate to the multiplicities of all proper and infinitely near base points?
:::

::: {.back card-id="numerical-pencil-base-length"}
Two generators have no common curve, so their intersection is the base scheme $Z$ and
$$\operatorname{length}Z=L^2.$$
If they meet transversely, this is the number of distinct base points. In general it counts local intersection multiplicities. After resolving all base points, with multiplicities $m_i$ in the total-transform basis, the fiber class has square zero:
$$F=\pi^*L-\sum_i m_iE_i,\qquad 0=F^2=L^2-\sum_i m_i^2.$$
Thus $\sum_i m_i^2=L^2$. For the local pencil $(x^2,y)$, the base scheme has length two at one point; resolution has two successive base points of multiplicity one. This differs from the jet-condition count $\binom{m+1}{2}$ used for interpolation.
:::

::: {.front card-id="numerical-del-pezzo-general-position" tags="definition application"}
For $r\le8$ distinct points of $\mathbb P^2_{\mathbb C}$, state the precise general-position conditions making their blowup del Pezzo. Explain the numerical obstruction behind each condition.
:::

::: {.back card-id="numerical-del-pezzo-general-position"}
No three points lie on a line, no six lie on a conic, and no eight lie on a cubic singular at one of those eight. Conditions requiring more than $r$ points are vacuous. These conditions are necessary and sufficient for $-K$ to be ample.

For a strict transform $C=eH-\sum m_iE_i$,
$$(-K)C=3e-\sum m_i.$$
The forbidden line, conic, and cubic give respectively $3-3=0$, $6-6=0$, and $9-(2+7)=0$, contradicting ampleness. The cubic condition is additional to the line and conic conditions.

Reference: [Van Luijk, Del Pezzo Surfaces](https://samirsiksek.github.io/siksek.github.io/arith/notes/delpezzo.pdf).
:::

::: {.front card-id="numerical-del-pezzo-exceptional-counts" tags="formula"}
How many $(-1)$-curves occur on a smooth complex del Pezzo surface of each degree? What distinguishes the two degree-eight surfaces?
:::

::: {.back card-id="numerical-del-pezzo-exceptional-counts"}

| $K^2$ | Surface | $(-1)$-curves |
| --- | --- | --- |
| 9 | $\mathbb P^2$ | 0 |
| 8 | $\mathbb P^1\times\mathbb P^1$ | 0 |
| 8 | $\mathbb F_1$ | 1 |
| 7 | $\operatorname{Bl}_2\mathbb P^2$ | 3 |
| 6 | $\operatorname{Bl}_3\mathbb P^2$ | 6 |
| 5 | $\operatorname{Bl}_4\mathbb P^2$ | 10 |
| 4 | $\operatorname{Bl}_5\mathbb P^2$ | 16 |
| 3 | $\operatorname{Bl}_6\mathbb P^2$ | 27 |
| 2 | $\operatorname{Bl}_7\mathbb P^2$ | 56 |
| 1 | $\operatorname{Bl}_8\mathbb P^2$ | 240 |

These are geometric counts over $\mathbb C$; over another ground field the curves need not all be individually defined. For $d\ge3$, the anticanonical embedding sends them to lines. The word “line” in degrees one and two refers instead to anticanonical degree one.
:::

::: {.front card-id="numerical-del-pezzo-anticanonical-basepoints" tags="application"}
For a smooth complex del Pezzo surface of degree $d$, compare the dimension, base locus, and map of $|-K|$ for $d=1$, $d=2$, and $d\ge3$. How does degree one connect to a cubic pencil?
:::

::: {.back card-id="numerical-del-pezzo-anticanonical-basepoints"}
Since $h^0(-K)=d+1$, the system has dimension $d$.

| Degree | Base locus of $|-K|$ | Map |
| --- | --- | --- |
| 1 | One reduced point | Pencil; blowing up that point gives a rational elliptic surface |
| 2 | Empty | Double cover of $\mathbb P^2$ branched over a smooth quartic |
| $\ge3$ | Empty | Closed immersion in $\mathbb P^d$ |

In degree one, write $S=\operatorname{Bl}_{p_1,\ldots,p_8}\mathbb P^2$. The anticanonical members are cubics through those points; their ninth intersection point is the remaining base point. Also $|-2K|$ is base-point-free and gives a double cover of a quadric cone in $\mathbb P^3$.
:::

::: {.front card-id="application-degree-two-del-pezzo-bitangents" tags="application"}
For a degree-two complex del Pezzo surface $f:S\to\mathbb P^2$ branched over a smooth quartic $B$, how do the bitangents of $B$ account for the exceptional curves on $S$?
:::

::: {.back card-id="application-degree-two-del-pezzo-bitangents"}
A bitangent line, allowing a hyperflex as coincident tangencies, meets $B$ in an even divisor $2D$. The double cover therefore splits over that line into two rational curves $E,E'$ with
$$f^*\ell=E+E',\qquad (-K)E=(-K)E'=1,\qquad E^2=(E')^2=-1.$$
Each bitangent gives a pair of exceptional curves, and every exceptional curve arises this way. Thus the quartic's $28$ bitangents give the del Pezzo's $56$ exceptional curves.
:::

::: {.front card-id="formula-divisor-sum-genus" tags="formula"}
For effective divisors $C,D$ with no common components on a smooth projective complex surface, compute $p_a(C+D)$.
:::

::: {.back card-id="formula-divisor-sum-genus"}
$$p_a(C+D)=p_a(C)+p_a(D)+CD-1.$$
:::

::: {.front card-id="formula-curve-diagonal-square" tags="formula"}
For a smooth connected projective complex curve $C$ of genus $g$, compute the self-intersection of the diagonal in $C\times C$.
:::

::: {.back card-id="formula-curve-diagonal-square"}
$$\Delta^2=2-2g.$$
:::

::: {.front card-id="formula-surface-arithmetic-adjunction" tags="formula"}
For an effective Cartier divisor $D$ on a smooth projective complex surface $S$, compute $p_a(D)$ from intersections.
:::

::: {.back card-id="formula-surface-arithmetic-adjunction"}
$$2p_a(D)-2=D(D+K_S).$$
:::

::: {.front card-id="formula-surface-hodge-euler" tags="formula"}
For a smooth connected projective complex surface $S$, write $\chi(\mathcal O_S)$ and $c_2(S)$ in terms of $q=h^1(\mathcal O_S)$, $p_g=h^0(K_S)$, and $h^{1,1}$.
:::

::: {.back card-id="formula-surface-hodge-euler"}
$$\chi(\mathcal O_S)=1-q+p_g,\qquad c_2(S)=e(S)=2-4q+2p_g+h^{1,1}.$$
:::

::: {.front card-id="formula-surface-betti-signature" tags="formula"}
For a smooth connected projective complex surface $S$, compute $b_2,b_2^+,b_2^-$ from its Hodge numbers.
:::

::: {.back card-id="formula-surface-betti-signature"}
$$b_2=2p_g+h^{1,1},\qquad b_2^+=1+2p_g,\qquad b_2^-=h^{1,1}-1.$$
:::

::: {.front card-id="formula-surface-signature-chern" tags="formula"}
For a smooth projective complex surface $S$, compute the signature $\tau(S)$ from its Chern numbers.
:::

::: {.back card-id="formula-surface-signature-chern"}
$$\tau(S)=\frac{K_S^2-2c_2(S)}3.$$
:::

::: {.front card-id="formula-surface-tangent-euler" tags="formula"}
For a smooth projective complex surface $S$, compute $\chi(T_S)$ and express $h^1(T_S)$ using $h^0(T_S),h^2(T_S)$ and numerical invariants.
:::

::: {.back card-id="formula-surface-tangent-euler"}
$$\chi(T_S)=2K_S^2-10\chi(\mathcal O_S),\qquad h^1(T_S)=h^0(T_S)+h^2(T_S)-2K_S^2+10\chi(\mathcal O_S).$$
:::

::: {.front card-id="formula-general-type-bounds" tags="formula"}
For a smooth minimal complex projective surface of general type, give the Noether and Bogomolov–Miyaoka–Yau bounds on $K_S^2$.
:::

::: {.back card-id="formula-general-type-bounds"}
$$2p_g-4\le K_S^2\le9\chi(\mathcal O_S).$$
:::

::: {.front card-id="formula-general-type-plurigenera" tags="formula"}
For a smooth minimal complex projective surface of general type, compute $P_m=h^0(S,mK_S)$ for $m\ge2$.
:::

::: {.back card-id="formula-general-type-plurigenera"}
$$P_m=\chi(\mathcal O_S)+\frac{m(m-1)}2K_S^2.$$
:::

::: {.front card-id="formula-point-blowup-invariants" tags="formula"}
For the blowup $\widetilde S$ of a smooth projective complex surface $S$ at a point, compute $c_2,\chi(\mathcal O),q,p_g$ in terms of those of $S$.
:::

::: {.back card-id="formula-point-blowup-invariants"}
$$c_2(\widetilde S)=c_2(S)+1,\qquad \chi(\mathcal O_{\widetilde S})=\chi(\mathcal O_S),\qquad q(\widetilde S)=q(S),\qquad p_g(\widetilde S)=p_g(S).$$
:::

::: {.front card-id="formula-strict-transform-intersections" tags="formula"}
Blow up a point of multiplicity $m$ on a curve $C$ in a smooth complex projective surface $S$. For exceptional curve $E$, compute the strict transform class, its square, and its intersection with $E$.
:::

::: {.back card-id="formula-strict-transform-intersections"}
$$\widetilde C=\pi^*C-mE,\qquad \widetilde C^2=C^2-m^2,\qquad \widetilde CE=m.$$
:::

::: {.front card-id="formula-strict-transform-genus" tags="formula"}
Blow up a multiplicity-$m$ point on a curve $C$ in a smooth complex projective surface $S$. Compute $K_{\widetilde S}\widetilde C$ and $p_a(\widetilde C)$.
:::

::: {.back card-id="formula-strict-transform-genus"}
$$K_{\widetilde S}\widetilde C=K_SC+m,\qquad p_a(\widetilde C)=p_a(C)-\binom m2.$$
:::

::: {.front card-id="formula-plane-blowup-basis" tags="formula"}
For successive point blowups $S\to\mathbb P^2_{\mathbb C}$, use the total-transform basis $H,E_1,\ldots,E_r$, allowing infinitely near centers. Compute its intersection matrix and $K_S$.
:::

::: {.back card-id="formula-plane-blowup-basis"}
$$H^2=1,\qquad HE_i=0,\qquad E_iE_j=-\delta_{ij},\qquad K_S=-3H+\sum_iE_i.$$
:::

::: {.front card-id="formula-plane-blowup-chern-numbers" tags="formula"}
For a surface obtained by $r$ successive point blowups of $\mathbb P^2_{\mathbb C}$, compute $K_S^2,c_2(S)$.
:::

::: {.back card-id="formula-plane-blowup-chern-numbers"}
$$K_S^2=9-r,\qquad c_2(S)=3+r.$$
:::

::: {.front card-id="formula-plane-blowup-divisor-intersections" tags="formula"}
On successive point blowups of $\mathbb P^2_{\mathbb C}$, write $D=dH-\sum_i m_iE_i$ in the total-transform basis. Compute $D^2$ and $K_SD$.
:::

::: {.back card-id="formula-plane-blowup-divisor-intersections"}
$$D^2=d^2-\sum_i m_i^2,\qquad K_SD=-3d+\sum_i m_i.$$
:::

::: {.front card-id="formula-plane-blowup-divisor-genus-euler" tags="formula"}
On successive point blowups of $\mathbb P^2_{\mathbb C}$, let $D=dH-\sum_i m_iE_i$ in the total-transform basis. Compute $\chi(\mathcal O_S(D))$ and, for effective $D$, $p_a(D)$ using polynomial binomial coefficients.
:::

::: {.back card-id="formula-plane-blowup-divisor-genus-euler"}
$$\chi(\mathcal O_S(D))=\binom{d+2}{2}-\sum_i\binom{m_i+1}{2},\qquad p_a(D)=\frac{(d-1)(d-2)}2-\sum_i\binom{m_i}{2}.$$
:::

::: {.front card-id="formula-quadric-divisor-computations" tags="formula"}
On $\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}$, compute $(a,b)(c,d)$, $(a,b)^2$, and the canonical class.
:::

::: {.back card-id="formula-quadric-divisor-computations"}
$$(a,b)(c,d)=ad+bc,\qquad (a,b)^2=2ab,\qquad K=(-2,-2).$$
:::

::: {.front card-id="formula-quadric-line-bundle-cohomology" tags="formula"}
For integers $a,b$, compute $\chi(\mathcal O(a,b))$ and $h^0(\mathcal O(a,b))$ on $\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}$.
:::

::: {.back card-id="formula-quadric-line-bundle-cohomology"}
$$\chi(\mathcal O(a,b))=(a+1)(b+1),\qquad h^0(\mathcal O(a,b))=\max(a+1,0)\max(b+1,0).$$
:::

::: {.front card-id="formula-hirzebruch-intersection-canonical" tags="formula"}
On the Hirzebruch surface $\mathbb F_e/\mathbb C$, $e\ge0$, let $S$ be the standard minimal section and $F$ a fiber. Compute $S^2,SF,F^2,K_{\mathbb F_e}$ and $K_{\mathbb F_e}^2$.
:::

::: {.back card-id="formula-hirzebruch-intersection-canonical"}
$$S^2=-e,\qquad SF=1,\qquad F^2=0,\qquad K_{\mathbb F_e}=-2S-(e+2)F,\qquad K_{\mathbb F_e}^2=8.$$
:::

::: {.front card-id="formula-hirzebruch-divisor-intersections" tags="formula"}
On $\mathbb F_e/\mathbb C$, with $S^2=-e$ and $F$ a fiber, compute $D^2$ and $KD$ for $D=aS+bF$.
:::

::: {.back card-id="formula-hirzebruch-divisor-intersections"}
$$D^2=-ea^2+2ab,\qquad KD=a(e-2)-2b.$$
:::

::: {.front card-id="formula-hirzebruch-euler" tags="formula"}
On $\mathbb F_e/\mathbb C$, with $S^2=-e$ and $F$ a fiber, compute $\chi(\mathcal O(aS+bF))$ for integers $a,b$.
:::

::: {.back card-id="formula-hirzebruch-euler"}
$$\chi(\mathcal O(aS+bF))=(a+1)(b+1)-\frac e2a(a+1).$$
:::

::: {.front card-id="formula-hirzebruch-sections" tags="formula"}
On $\mathbb F_e/\mathbb C$, with $S^2=-e$ and $F$ a fiber, compute $h^0(\mathcal O(aS+bF))$ for $a\ge0$.
:::

::: {.back card-id="formula-hirzebruch-sections"}
$$h^0(\mathcal O(aS+bF))=\sum_{i=0}^a\max(b-ie+1,0).$$
:::

::: {.front card-id="formula-ruled-surface-invariants" tags="formula"}
For a geometrically ruled complex projective surface $S\to B$ with $g(B)=g$, compute $K_S^2,c_2(S),q,p_g,\chi(\mathcal O_S)$.
:::

::: {.back card-id="formula-ruled-surface-invariants"}
$$K_S^2=8(1-g),\quad c_2(S)=4(1-g),\quad q=g,\quad p_g=0,\quad \chi(\mathcal O_S)=1-g.$$
:::

::: {.front card-id="formula-conic-fibration-invariants" tags="formula"}
Let $S\to B$ be a conic fibration from a smooth projective complex surface to a smooth curve. Suppose its $s$ singular fibers are each two smooth rational curves meeting transversely once. Compute $c_2(S),K_S^2$.
:::

::: {.back card-id="formula-conic-fibration-invariants"}
$$c_2(S)=4(1-g(B))+s,\qquad K_S^2=8(1-g(B))-s.$$
:::

::: {.front card-id="formula-hypersurface-surface-chern" tags="formula"}
For a smooth degree-$d$ surface $S\subset\mathbb P^3_{\mathbb C}$ with hyperplane class $H$, compute $H^2,K_S,K_S^2,c_2(S)$.
:::

::: {.back card-id="formula-hypersurface-surface-chern"}
$$H^2=d,\quad K_S=(d-4)H,\quad K_S^2=d(d-4)^2,\quad c_2(S)=d(d^2-4d+6).$$
:::

::: {.front card-id="formula-hypersurface-surface-genera" tags="formula"}
For a smooth degree-$d$ surface $S\subset\mathbb P^3_{\mathbb C}$, compute $\chi(\mathcal O_S),q(S),p_g(S)$ and the genus of a smooth hyperplane section.
:::

::: {.back card-id="formula-hypersurface-surface-genera"}
$$\chi(\mathcal O_S)=\frac{d(d^2-6d+11)}6,\quad q=0,\quad p_g=\frac{(d-1)(d-2)(d-3)}6,\quad g(H)=\frac{(d-1)(d-2)}2.$$
:::

::: {.front card-id="formula-ci-surface-canonical" tags="formula"}
For a smooth complete-intersection surface of type $(d,e)$ in $\mathbb P^4_{\mathbb C}$, compute $H^2,K_S,K_S^2$.
:::

::: {.back card-id="formula-ci-surface-canonical"}
$$H^2=de,\qquad K_S=(d+e-5)H,\qquad K_S^2=de(d+e-5)^2.$$
:::

::: {.front card-id="formula-ci-surface-euler" tags="formula"}
For a smooth complete-intersection surface $S$ of type $(d,e)$ in $\mathbb P^4_{\mathbb C}$, compute $c_2(S)$ and $\chi(\mathcal O_S)$.
:::

::: {.back card-id="formula-ci-surface-euler"}
$$c_2(S)=de(d^2+de+e^2-5d-5e+10),\qquad \chi(\mathcal O_S)=\frac{de}{12}\left[(d+e-5)^2+d^2+de+e^2-5d-5e+10\right].$$
:::

::: {.front card-id="formula-product-curves-invariants" tags="formula"}
For $S=C_g\times C_h$, the product of smooth connected projective complex curves of genera $g,h$, compute $K_S^2,c_2(S),\chi(\mathcal O_S),q,p_g$.
:::

::: {.back card-id="formula-product-curves-invariants"}
$$K_S^2=8(g-1)(h-1),\quad c_2(S)=4(g-1)(h-1),\quad \chi(\mathcal O_S)=(g-1)(h-1),\quad q=g+h,\quad p_g=gh.$$
:::

::: {.front card-id="formula-enriques-canonical-numbers" tags="formula"}
For a complex Enriques surface $S$, give the torsion and numerical canonical-class identities and compute $K_S^2,c_2(S)$.
:::

::: {.back card-id="formula-enriques-canonical-numbers"}
$$2K_S\sim0,\qquad K_S\equiv0,\qquad K_S^2=0,\qquad c_2(S)=12.$$
:::

::: {.front card-id="formula-enriques-line-bundles" tags="formula"}
For a complex Enriques surface $S$, compute $\chi(\mathcal O_S(D))$ for a divisor $D$ and $h^0(S,L)$ for an ample line bundle $L$.
:::

::: {.back card-id="formula-enriques-line-bundles"}
$$\chi(\mathcal O_S(D))=1+\frac{D^2}{2},\qquad h^0(S,L)=1+\frac{L^2}{2}.$$
:::

::: {.front card-id="formula-enriques-deformations-plurigenera" tags="formula"}
For a complex Enriques surface $S$, compute $h^1(T_S),h^2(T_S)$ and $P_m$ for $m\ge1$.
:::

::: {.back card-id="formula-enriques-deformations-plurigenera"}
$$h^1(T_S)=10,\qquad h^2(T_S)=0,\qquad P_m=\begin{cases}0&m\text{ odd},\\1&m\text{ even}.\end{cases}$$
:::

::: {.front card-id="formula-abelian-surface-canonical-chern" tags="formula"}
For a complex abelian surface $A$, compute its canonical class and second Chern class.
:::

::: {.back card-id="formula-abelian-surface-canonical-chern"}
$$K_A\sim0,\qquad c_2(A)=0.$$
:::

::: {.front card-id="formula-abelian-surface-line-bundles" tags="formula"}
For a complex abelian surface $A$, compute $\chi(\mathcal O_A(D))$ and, for ample $L$ of polarization type $(d_1,d_2)$, compute $L^2,h^0(A,L)$.
:::

::: {.back card-id="formula-abelian-surface-line-bundles"}
$$\chi(\mathcal O_A(D))=\frac{D^2}{2},\qquad L^2=2d_1d_2,\qquad h^0(A,L)=d_1d_2=\frac{L^2}{2}.$$
:::

::: {.front card-id="formula-del-pezzo-invariants" tags="formula"}
For a smooth complex del Pezzo surface $S$ of degree $d=K_S^2$, compute $\chi(\mathcal O_S),c_2(S)$ and $h^0(-mK_S)$ for $m\ge0$.
:::

::: {.back card-id="formula-del-pezzo-invariants"}
$$\chi(\mathcal O_S)=1,\quad c_2(S)=12-d,\quad h^0(-mK_S)=1+\frac{m(m+1)}2d,\quad h^0(-K_S)=d+1.$$
:::

::: {.front card-id="formula-cyclic-surface-canonical-square" tags="formula"}
Let $X\to Y$ be the smooth degree-$n$ cyclic cover of a smooth projective complex surface defined by $B\in\lvert nL\rvert$ smooth. Compute $K_X^2$.
:::

::: {.back card-id="formula-cyclic-surface-canonical-square"}
$$K_X^2=n(K_Y+(n-1)L)^2.$$
:::

::: {.front card-id="formula-cyclic-surface-holomorphic-euler" tags="formula"}
Let $X\to Y$ be a smooth degree-$n$ cyclic cover of smooth projective complex surfaces, branched along smooth $B\in\lvert nL\rvert$. Compute $\chi(\mathcal O_X)$ using intersections on $Y$.
:::

::: {.back card-id="formula-cyclic-surface-holomorphic-euler"}
$$\chi(\mathcal O_X)=n\chi(\mathcal O_Y)+\frac{n(n-1)(2n-1)}{12}L^2+\frac{n(n-1)}4K_YL.$$
:::

::: {.front card-id="formula-cyclic-surface-chern-hodge" tags="formula"}
Let $X\to Y$ be a smooth degree-$n$ cyclic cover of smooth projective complex surfaces, branched along smooth $B\in\lvert nL\rvert$. Compute $c_2(X),q(X),p_g(X)$.
:::

::: {.back card-id="formula-cyclic-surface-chern-hodge"}
$$\begin{aligned}c_2(X)&=nc_2(Y)+(n-1)B(B+K_Y),\\q(X)&=\sum_{i=0}^{n-1}h^1(Y,L^{-i}),\\p_g(X)&=\sum_{i=0}^{n-1}h^0(Y,\omega_Y\otimes L^i).\end{aligned}$$
:::

::: {.front card-id="formula-double-cover-surface-invariants" tags="formula"}
For a smooth double cover $X\to Y$ of smooth projective complex surfaces, branched along smooth $B\in\lvert 2L\rvert$, compute $K_X^2,\chi(\mathcal O_X),p_g(X)$.
:::

::: {.back card-id="formula-double-cover-surface-invariants"}
$$K_X^2=2(K_Y+L)^2,\quad \chi(\mathcal O_X)=2\chi(\mathcal O_Y)+\frac12L(L+K_Y),\quad p_g(X)=p_g(Y)+h^0(Y,K_Y+L).$$
:::

::: {.front card-id="formula-double-plane-invariants" tags="formula"}
For a double cover $X\to\mathbb P^2_{\mathbb C}$ branched along a smooth curve of degree $2b$, $b\ge1$, compute $K_X^2,\chi(\mathcal O_X),c_2(X)$.
:::

::: {.back card-id="formula-double-plane-invariants"}
$$K_X^2=2(b-3)^2,\qquad \chi(\mathcal O_X)=2+\frac{b(b-3)}2,\qquad c_2(X)=6+2b(2b-3).$$
:::

::: {.front card-id="formula-double-plane-hodge" tags="formula"}
For a double cover $X\to\mathbb P^2_{\mathbb C}$ branched along a smooth degree-$2b$ curve, $b\ge2$, compute $p_g(X),q(X)$.
:::

::: {.back card-id="formula-double-plane-hodge"}
$$p_g(X)=\binom{b-1}{2},\qquad q(X)=0.$$
:::

::: {.front card-id="formula-etale-surface-invariants" tags="formula"}
For a degree-$n$ finite étale cover $X\to Y$ of smooth projective complex surfaces, compute $K_X^2,c_2(X),\chi(\mathcal O_X)$.
:::

::: {.back card-id="formula-etale-surface-invariants"}
$$K_X^2=nK_Y^2,\qquad c_2(X)=nc_2(Y),\qquad \chi(\mathcal O_X)=n\chi(\mathcal O_Y).$$
:::

::: {.front card-id="formula-fibration-fiber-intersections" tags="formula"}
Let $S\to B$ be a fibration from a smooth projective complex surface to a smooth curve, with smooth connected general fiber $F$ of genus $g$. Compute $F^2,K_SF$.
:::

::: {.back card-id="formula-fibration-fiber-intersections"}
$$F^2=0,\qquad K_SF=2g-2.$$
:::

::: {.front card-id="formula-elliptic-canonical-bundle" tags="formula"}
For a relatively minimal elliptic fibration $f:S\to B$ of smooth projective complex varieties with section, put $L=(R^1f_*\mathcal O_S)^\vee$. Compute $\deg L,\omega_S,K_S^2$.
:::

::: {.back card-id="formula-elliptic-canonical-bundle"}
$$\deg L=\chi(\mathcal O_S),\qquad \omega_S\cong f^*(\omega_B\otimes L),\qquad K_S^2=0.$$
:::

::: {.front card-id="formula-elliptic-euler-section" tags="formula"}
For a relatively minimal complex projective elliptic surface with zero section $O$, compute $c_2(S)$ and $O^2$ using $\chi(\mathcal O_S)$.
:::

::: {.back card-id="formula-elliptic-euler-section"}
$$c_2(S)=12\chi(\mathcal O_S),\qquad O^2=-\chi(\mathcal O_S).$$
:::

::: {.front card-id="formula-elliptic-discriminant-degree" tags="formula"}
For a relatively minimal complex projective elliptic surface with section, compute the degree of its minimal discriminant divisor and its Euler number from the fibers $F_v$.
:::

::: {.back card-id="formula-elliptic-discriminant-degree"}
$$\deg\operatorname{div}(\Delta)=12\chi(\mathcal O_S),\qquad e(S)=\sum_{v\in B}e(F_v).$$
:::

::: {.front card-id="formula-shioda-tate-rank" tags="formula"}
For a relatively minimal complex projective elliptic surface $f:S\to B$ with section and at least one singular fiber, let $m_v$ count irreducible components of $F_v$. Compute $\rho(S)$ from the Mordell–Weil rank.
:::

::: {.back card-id="formula-shioda-tate-rank"}
$$\rho(S)=2+\operatorname{rank}\operatorname{MW}(f)+\sum_v(m_v-1).$$
:::

::: {.front card-id="formula-kodaira-euler-numbers" tags="formula"}
For complex Kodaira fibers, compute the Euler numbers of $I_0,I_n$ ($n\ge1$), $II,III,IV,I_n^*$ ($n\ge0$), $IV^*,III^*,II^*$.
:::

::: {.back card-id="formula-kodaira-euler-numbers"}
$$\begin{array}{c|ccccccccc}F&I_0&I_n&II&III&IV&I_n^*&IV^*&III^*&II^*\\\hline e(F)&0&n&2&3&4&n+6&8&9&10\end{array}$$
:::

::: {.front card-id="formula-shioda-height-pairing" tags="formula"}
For sections $P,Q$ of a relatively minimal complex projective elliptic surface with zero section $O$ and at least one singular fiber, express the Shioda pairing and its diagonal using the local correction terms $\operatorname{contr}_v$.
:::

::: {.back card-id="formula-shioda-height-pairing"}
$$\begin{aligned}\langle P,Q\rangle&=\chi(\mathcal O_S)+PO+QO-PQ-\sum_v\operatorname{contr}_v(P,Q),\\\langle P,P\rangle&=2\chi(\mathcal O_S)+2PO-\sum_v\operatorname{contr}_v(P).\end{aligned}$$
:::

::: {.front card-id="formula-fibration-relative-invariants" tags="formula"}
For a relatively minimal semistable fibration $f:S\to B$ of smooth projective complex varieties with connected fibers of genus $g\ge2$ and $b=g(B)$, express $K_f,K_f^2,\chi_f,\delta_f$ in terms of absolute invariants.
:::

::: {.back card-id="formula-fibration-relative-invariants"}
$$\begin{aligned}K_f&=K_S-f^*K_B,\\K_f^2&=K_S^2-8(g-1)(b-1),\\\chi_f&=\chi(\mathcal O_S)-(g-1)(b-1),\\\delta_f&=c_2(S)-4(g-1)(b-1).\end{aligned}$$
:::

::: {.front card-id="formula-fibration-relative-noether" tags="formula"}
For a relatively minimal semistable genus-$g\ge2$ fibration $f:S\to B$ of smooth projective complex varieties, give the relative Noether identity and compute $\chi_f$ from the relative dualizing sheaf.
:::

::: {.back card-id="formula-fibration-relative-noether"}
$$12\chi_f=K_f^2+\delta_f,\qquad \chi_f=\deg f_*\omega_{S/B}.$$
:::

::: {.front card-id="formula-fibration-node-count" tags="formula"}
For a semistable genus-$g$ fibration $f:S\to B$ from a smooth projective complex surface, express $\delta_f=c_2(S)-4(g-1)(g(B)-1)$ using the fibers.
:::

::: {.back card-id="formula-fibration-node-count"}
$$\delta_f=\sum_{v\in B}\#\{\text{nodes of }F_v\}.$$
:::

::: {.front card-id="formula-cubic-surface-lines" tags="formula"}
How many lines lie on a smooth cubic surface over $\mathbb C$?
:::

::: {.back card-id="formula-cubic-surface-lines"}
$$\#\{\text{lines}\}=27.$$
:::

