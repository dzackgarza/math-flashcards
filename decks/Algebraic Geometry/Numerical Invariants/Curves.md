---
title: "Algebraic Geometry::Numerical Invariants::Curves"
---

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

