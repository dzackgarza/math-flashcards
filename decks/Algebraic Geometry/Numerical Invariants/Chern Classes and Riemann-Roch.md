---
title: "Algebraic Geometry::Numerical Invariants::Chern Classes and Riemann-Roch"
---

::: {.front card-id="formula-curve-vector-bundle-rr" tags="formula"}
For a rank-$r$ vector bundle $E$ on a smooth connected projective complex curve of genus $g$, compute $\chi(E)$.
:::

::: {.back card-id="formula-curve-vector-bundle-rr"}
$$\chi(E)=\deg E+r(1-g).$$
:::

::: {.front card-id="formula-curve-normal-degree" tags="formula"}
For a smooth connected curve $C\subset\mathbb P^n_{\mathbb C}$ of degree $d$ and genus $g$, compute $\deg N_{C/\mathbb P^n}$.
:::

::: {.back card-id="formula-curve-normal-degree"}
$$\deg N_{C/\mathbb P^n}=(n+1)d+2g-2.$$
:::

::: {.front card-id="formula-curve-normal-euler" tags="formula"}
For a smooth connected degree-$d$, genus-$g$ curve $C\subset\mathbb P^n_{\mathbb C}$, compute $\chi(N_{C/\mathbb P^n})$, including the case $n=3$.
:::

::: {.back card-id="formula-curve-normal-euler"}
$$\chi(N_{C/\mathbb P^n})=(n+1)d+(n-3)(1-g),\qquad \chi(N_{C/\mathbb P^3})=4d.$$
:::

::: {.front card-id="formula-surface-curve-normal" tags="formula"}
For a smooth connected curve $C$ of genus $g$ on a smooth projective complex surface $S$, compute the degree and Euler characteristic of $N_{C/S}$.
:::

::: {.back card-id="formula-surface-curve-normal"}
$$\deg N_{C/S}=C^2,\qquad \chi(N_{C/S})=C^2+1-g=\frac{C^2-K_SC}{2}.$$
:::

::: {.front card-id="formula-chern-sum-dual" tags="formula"}
For complex algebraic vector bundles $E,F$, compute $c(E\oplus F)$ and $c_i(E^\vee)$.
:::

::: {.back card-id="formula-chern-sum-dual"}
$$c(E\oplus F)=c(E)c(F),\qquad c_i(E^\vee)=(-1)^ic_i(E).$$
:::

::: {.front card-id="formula-chern-line-twist" tags="formula"}
For a rank-$r$ vector bundle $E$ and a line bundle $L$, set $\ell=c_1(L)$. Compute the first two Chern classes of $E\otimes L$.
:::

::: {.back card-id="formula-chern-line-twist"}
$$c_1(E\otimes L)=c_1(E)+r\ell,\qquad c_2(E\otimes L)=c_2(E)+(r-1)c_1(E)\ell+\binom r2\ell^2.$$
:::

::: {.front card-id="formula-chern-character-expansion" tags="formula"}
For a rank-$r$ vector bundle $E$, write $\operatorname{ch}(E)$ through codimension three in terms of $c_i=c_i(E)$.
:::

::: {.back card-id="formula-chern-character-expansion"}
$$\operatorname{ch}(E)=r+c_1+\frac{c_1^2-2c_2}{2}+\frac{c_1^3-3c_1c_2+3c_3}{6}+\cdots.$$
:::

::: {.front card-id="formula-todd-expansion" tags="formula"}
For a smooth complex variety $X$, write $\operatorname{td}(T_X)$ through codimension three, with $c_i=c_i(T_X)$.
:::

::: {.back card-id="formula-todd-expansion"}
$$\operatorname{td}(T_X)=1+\frac{c_1}{2}+\frac{c_1^2+c_2}{12}+\frac{c_1c_2}{24}+\cdots.$$
:::

::: {.front card-id="formula-complete-intersection-chern-canonical" tags="formula"}
For a smooth complete intersection $X\subset\mathbb P^n_{\mathbb C}$ of multidegree $(d_1,\ldots,d_r)$ and hyperplane class $H$, compute $K_X$, $c(T_X)$, and the top hyperplane intersection.
:::

::: {.back card-id="formula-complete-intersection-chern-canonical"}
$$K_X\sim\left(\sum_i d_i-n-1\right)H,\qquad c(T_X)=\frac{(1+H)^{n+1}}{\prod_i(1+d_iH)},\qquad \int_XH^{n-r}=\prod_i d_i.$$
:::

::: {.front card-id="formula-hypersurface-chern-classes" tags="formula"}
For a smooth degree-$d$ hypersurface $X\subset\mathbb P^n_{\mathbb C}$ with hyperplane class $H$, compute $c_1(T_X),c_2(T_X),c_3(T_X)$ in its Chow ring.
:::

::: {.back card-id="formula-hypersurface-chern-classes"}
$$\begin{aligned}c_1&=(n+1-d)H,\\c_2&=\left[\binom{n+1}{2}-(n+1)d+d^2\right]H^2,\\c_3&=\left[\binom{n+1}{3}-\binom{n+1}{2}d+(n+1)d^2-d^3\right]H^3.\end{aligned}$$
:::

::: {.front card-id="formula-surface-vector-bundle-rr" tags="formula"}
For a rank-$r$ vector bundle $E$ on a smooth projective complex surface $S$, compute $\chi(E)$ using its Chern classes.
:::

::: {.back card-id="formula-surface-vector-bundle-rr"}
$$\chi(E)=r\chi(\mathcal O_S)+\frac12c_1(E)(c_1(E)-K_S)-c_2(E).$$
:::

