---
title: "Algebraic Geometry::Numerical Invariants::Curves"
---

::: {.front card-id="numerical-plane-pencil-reference" tags="formula application"}
For a general pencil of degree-$d$ plane curves over $\mathbb C$, $d\ge2$, compute the number of base points, genus of a smooth member, and number of singular members. Specialize to conics, cubics, and quartics.
:::

::: {.back card-id="numerical-plane-pencil-reference"}
The base points are transverse, so Bézout gives $d^2$ distinct points. A smooth member has $g=(d-1)(d-2)/2$. A general pencil meets the discriminant transversely in $3(d-1)^2$ points; each corresponding member has one ordinary node and no other singularity.

| $d$ | Base points | Genus | Singular members |
| --- | --- | --- | --- |
| 2 | 4 | 0 | 3 |
| 3 | 9 | 1 | 12 |
| 4 | 16 | 3 | 27 |

For a numerical check, the blown-up plane has $e=3+d^2$, while a smooth bundle over $\mathbb P^1$ with genus-$g$ fiber would have Euler number $4-4g$. Each nodal fiber adds one, giving $3+d^2-(4-4g)=3(d-1)^2$. Special pencils can have nonreduced base schemes or fewer distinct singular members.
:::

::: {.front card-id="application-cubic-interpolation-ninth-point" tags="application"}
Compare cubics through eight general plane points, cubics through nine general plane points, and cubics through the nine transverse intersection points of two cubics. Why does the last configuration behave differently?
:::

::: {.back card-id="application-cubic-interpolation-ninth-point"}
The vector space of cubics has dimension $10$.

| Point configuration | Dimension of cubics vanishing there | Projective system |
| --- | --- | --- |
| Eight general points | 2 | Pencil |
| Nine general points | 1 | Unique cubic |
| Nine transverse intersections of two cubics | 2 | Pencil |

In the last case the ideal in degree three is spanned by the two defining cubics. Cayley–Bacharach says every cubic through any eight of the nine points passes through the ninth. Thus the ninth condition is dependent. Nine points arising as the base locus of a cubic pencil are not nine independently general points.
:::

::: {.front card-id="numerical-theta-characteristics-bitangents" tags="formula application" cite="[@Kai19]"}
For a smooth complex curve of genus $g\ge1$, count theta characteristics and their even and odd parts. What does this give for bitangents of a smooth plane quartic?
:::

::: {.back card-id="numerical-theta-characteristics-bitangents"}
A theta characteristic is a line bundle $\theta$ with $\theta^{\otimes2}\cong\omega_C$; parity means $h^0(\theta)\bmod2$. They form a torsor under $\operatorname{Pic}^0(C)[2]$.

| Type | Count |
| --- | --- |
| All | $2^{2g}$ |
| Even | $2^{g-1}(2^g+1)$ |
| Odd | $2^{g-1}(2^g-1)$ |

For a plane quartic, $g=3$ and each odd theta characteristic has a unique effective divisor $D$ of degree two. The line cutting out $2D$ is a bitangent, including a hyperflex when $D=2p$. Hence there are $28$ bitangents, and $36$ even theta characteristics.
:::

::: {.front card-id="numerical-branch-count-versus-ramification" tags="application"}
For a degree-$n$ map $C\to\mathbb P^1_{\mathbb C}$ with $C$ smooth projective of genus $g$, when is the number of branch points $2g+2n-2$? Give the hyperelliptic specialization and explain what changes at a totally ramified fiber.
:::

::: {.back card-id="numerical-branch-count-versus-ramification"}
Riemann–Hurwitz always gives $\deg R=2g+2n-2$. This equals the number of branch values only when each branch fiber has exactly one ramification point of index two and all other points unramified.

| Cover | Number of branch values |
| --- | --- |
| Simply branched degree $n$ | $2g+2n-2$ |
| Hyperelliptic double cover | $2g+2$ |
| Elliptic double cover of $\mathbb P^1$ | 4 |

A totally ramified fiber contributes $n-1$ to $\deg R$ but only one branch value. Numerical ramification degree and the number of distinct branch points must therefore be kept separate.
:::

::: {.front card-id="application-curve-degree-thresholds" tags="application"}
For an arbitrary line bundle $L$ on a smooth projective curve of genus $g\ge2$, give degree bounds ensuring nonspeciality, base-point-freeness, and very ampleness. What do they imply for $2K_C$ and $3K_C$?
:::

::: {.back card-id="application-curve-degree-thresholds"}

| Property guaranteed for every $L$ | Sufficient degree |
| --- | --- |
| $H^1(L)=0$ | $\deg L\ge2g-1$ |
| Base-point-free | $\deg L\ge2g$ |
| Very ample | $\deg L\ge2g+1$ |

These are uniform sufficient bounds, not necessary conditions for a particular $L$. Since $\deg(2K)=4g-4$, $2K$ is very ample for $g\ge3$. In genus two it is base-point-free but factors through the hyperelliptic map and the conic embedding of $\mathbb P^1$. The bundle $3K$ is very ample for every $g\ge2$.
:::

::: {.front card-id="numerical-plane-flex-count" tags="formula application"}
For a smooth plane curve of degree $d\ge3$ over $\mathbb C$, compute the total inflection weight. How do ordinary flexes and hyperflexes contribute? Specialize to cubics and quartics.
:::

::: {.back card-id="numerical-plane-flex-count"}
The Hessian determinant has degree $3(d-2)$, and its intersection with the curve is the inflection divisor, of degree $3d(d-2)$. Tangent contact order $r\ge3$ contributes weight $r-2$.

| Curve | Total weight | Distinct flexes for a general curve |
| --- | --- | --- |
| Smooth cubic | 9 | 9 |
| Smooth quartic | 24 | 24 |

A quartic hyperflex has contact order four and contributes weight two; an ordinary flex contributes one. Thus a special quartic can have fewer distinct flex points while keeping the same total weight.
:::

::: {.front card-id="numerical-hurwitz-automorphism-bound" tags="theorem application"}
State the Hurwitz bound for automorphisms of a smooth complex projective curve of genus $g\ge2$. What quotient ramification data give equality, and what is the genus-three example?
:::

::: {.back card-id="numerical-hurwitz-automorphism-bound"}
The automorphism group is finite and satisfies
$$|\operatorname{Aut}(C)|\le84(g-1).$$
Equality requires quotient $\mathbb P^1$ with three branch values of inertia orders $(2,3,7)$. The Riemann–Hurwitz factor is
$$-2+\left(1-\frac12\right)+\left(1-\frac13\right)+\left(1-\frac17\right)=\frac1{42},$$
so $2g-2=|G|/42$. The Klein quartic $x^3y+y^3z+z^3x=0$ has genus three and automorphism group of order $168$, attaining the bound. The characteristic-zero hypothesis matters; wild automorphisms can violate this bound in positive characteristic.
:::

::: {.front card-id="card-c75bc53b976644b0" tags="formula"}
For a smooth connected projective complex curve $C$ of genus $g$, compute the degree of its canonical divisor.
:::

::: {.back card-id="card-c75bc53b976644b0"}
$$\deg K_C=2g-2.$$
:::

::: {.front card-id="card-65a63ab68d3c91f4"}
Compute the canonical sheaf of a smooth plane curve of degree $d$ and its degree.
:::

::: {.back card-id="card-65a63ab68d3c91f4"}
For $X\subseteq {\mathbf{P}}^n$ a hypersurface one has $\omega_X = {\mathcal{O}}_X(d-n-1)$, here $n=2$ so $\omega_X = {\mathcal{O}}_X(d-3)$. Since $\deg {\mathcal{O}}_X(1) = d$, we have $\deg \omega_X = d(d-3)$.
:::

::: {.front card-id="formula-curve-tangent-euler" tags="formula"}
For a smooth connected projective complex curve $C$ of genus $g$, compute $\chi(T_C)$ and, when $g\ge2$, $h^1(T_C)$.
:::

::: {.back card-id="formula-curve-tangent-euler"}
$$\chi(T_C)=3-3g,\qquad h^1(T_C)=3g-3\quad(g\ge2).$$
:::

::: {.front card-id="formula-double-cover-curve-genus" tags="formula"}
For a double cover $C\to B$ of smooth connected projective complex curves, simply branched at $2r$ points, compute $g(C)$.
:::

::: {.back card-id="formula-double-cover-curve-genus"}
$$g(C)=2g(B)-1+r.$$
:::

::: {.front card-id="formula-ci-curve-genus" tags="formula"}
For a smooth connected complete-intersection curve $C\subset\mathbb P^n_{\mathbb C}$ of multidegree $(d_1,\ldots,d_{n-1})$, compute its degree and genus.
:::

::: {.back card-id="formula-ci-curve-genus"}
$$\deg C=\prod_i d_i,\qquad 2g(C)-2=\left(\sum_i d_i-n-1\right)\prod_i d_i.$$
:::

::: {.front card-id="formula-space-ci-curve-genus" tags="formula"}
For a smooth connected intersection of surfaces of degrees $d,e$ in $\mathbb P^3_{\mathbb C}$, compute its genus.
:::

::: {.back card-id="formula-space-ci-curve-genus"}
$$g=1+\frac{de(d+e-4)}2.$$
:::

::: {.front card-id="formula-plane-singularity-jacobian-algebras" tags="formula"}
For an isolated reduced complex plane-curve singularity $f=0$, compute its Milnor and Tjurina numbers using local analytic algebras.
:::

::: {.back card-id="formula-plane-singularity-jacobian-algebras"}
$$\mu(f)=\dim_{\mathbb C}\frac{\mathbb C\{x,y\}}{(f_x,f_y)},\qquad \tau(f)=\dim_{\mathbb C}\frac{\mathbb C\{x,y\}}{(f,f_x,f_y)}.$$
:::

::: {.front card-id="formula-plane-singularity-milnor-delta" tags="formula"}
For a reduced isolated complex plane-curve singularity with $r$ branches, relate its Milnor number and delta invariant.
:::

::: {.back card-id="formula-plane-singularity-milnor-delta"}
$$\mu=2\delta-r+1.$$
:::

::: {.front card-id="formula-ordinary-multiple-point-delta" tags="formula"}
Compute the delta invariant of an ordinary $m$-fold point of a complex plane curve.
:::

::: {.back card-id="formula-ordinary-multiple-point-delta"}
$$\delta=\binom m2.$$
:::

::: {.front card-id="formula-an-plane-singularity" tags="formula"}
For the complex plane-curve singularity $A_n$, with equation $y^2=x^{n+1}$ and $n\ge1$, compute $\delta,\mu,\tau$.
:::

::: {.back card-id="formula-an-plane-singularity"}
$$\delta=\left\lfloor\frac{n+1}{2}\right\rfloor,\qquad \mu=\tau=n.$$
:::

::: {.front card-id="formula-resolution-delta" tags="formula"}
An embedded resolution of a reduced complex plane-curve singularity uses successive point blowups. If $m_i$ are the multiplicities of the strict transform at their centers, compute $\delta$.
:::

::: {.back card-id="formula-resolution-delta"}
$$\delta=\sum_i\binom{m_i}{2}.$$
:::

::: {.front card-id="formula-nodal-curve-genus" tags="formula"}
For a connected projective nodal complex curve with dual graph $\Gamma$ and normalized components $\widetilde C_i$, compute the arithmetic genus.
:::

::: {.back card-id="formula-nodal-curve-genus"}
$$p_a(C)=\sum_i g(\widetilde C_i)+b_1(\Gamma).$$
:::

::: {.front card-id="formula-nodal-dualizing-degree" tags="formula"}
For a stable complex nodal curve $C$ with normalization $\nu$, let $n_i$ count nodal branches on $\widetilde C_i$. Compute the degree of $\nu^*\omega_C$ on this component.
:::

::: {.back card-id="formula-nodal-dualizing-degree"}
$$\deg\left((\nu^*\omega_C)|_{\widetilde C_i}\right)=2g(\widetilde C_i)-2+n_i.$$
:::

::: {.front card-id="formula-general-lines-intersections" tags="formula"}
For $d$ lines in $\mathbb P^2_{\mathbb C}$ in general position, compute the number of distinct pairwise intersection points.
:::

::: {.back card-id="formula-general-lines-intersections"}
$$\#\{\text{intersection points}\}=\binom d2.$$
:::

::: {.front card-id="formula-quadric-curve-genus" tags="formula"}
For a smooth connected curve of bidegree $(a,b)$ in $\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}$, compute the genus.
:::

::: {.back card-id="formula-quadric-curve-genus"}
$$g=(a-1)(b-1).$$
:::

::: {.front card-id="formula-weierstrass-discriminant-j" tags="formula"}
For a complex elliptic curve in short Weierstrass form $y^2=x^3+a_4x+a_6$, compute $\Delta$ and $j$.
:::

::: {.back card-id="formula-weierstrass-discriminant-j"}
$$\Delta=-16(4a_4^3+27a_6^2),\qquad j=1728\frac{4a_4^3}{4a_4^3+27a_6^2}.$$
:::

::: {.front card-id="numerical-curve-basic-invariants" tags="formula"}
For a smooth connected projective complex curve of genus $g$, give its Betti numbers, topological Euler characteristic, and holomorphic Euler characteristic.
:::

::: {.back card-id="numerical-curve-basic-invariants"}
$$b_0=b_2=1,\qquad b_1=2g,\qquad e(C)=2-2g,\qquad \chi(\mathcal O_C)=1-g.$$
:::

::: {.front card-id="numerical-plane-genus" tags="formula"}
What is the genus of a smooth degree-$d$ plane curve over $\mathbb C$?
:::

::: {.back card-id="numerical-plane-genus"}
$$g=\frac{(d-1)(d-2)}2.$$
:::

::: {.front card-id="numerical-large-degree-sections" tags="formula"}
For a line bundle $L$ of degree $d>2g-2$ on a smooth connected projective curve of genus $g$, compute $h^0(L)$ and $h^1(L)$.
:::

::: {.back card-id="numerical-large-degree-sections"}
$$h^0(L)=d+1-g,\qquad h^1(L)=0.$$
:::

