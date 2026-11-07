---
title: "Algebraic Geometry::Singularities::Birational Classes"
---

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
Assume $X$ normal, $\Delta$ an effective $\mathbb Q$-divisor with coefficients at most $1$, and $K_X+\Delta$ $\mathbb Q$-Cartier. The pair is dlt if there is a log resolution $f:Y\to X$ for which every $f$-exceptional prime divisor has discrepancy greater than $-1$.
:::

::: {.front card-id="singularity-snc-pair-example" tags="application"}
Let $D_1,D_2$ be the coordinate axes in $\mathbb A^2_{\mathbb C}$. For $a,b\ge0$, when is $(\mathbb A^2,aD_1+bD_2)$ klt or log canonical? What discrepancy appears on blowing up the origin?
:::

::: {.back card-id="singularity-snc-pair-example"}
It is klt iff $a,b<1$, and log canonical iff $a,b\le1$. The exceptional divisor has
$$a(E,\mathbb A^2,aD_1+bD_2)=1-a-b.$$
For $a=b=1$ the pair is dlt and log canonical, but not klt.
:::

::: {.front card-id="singularity-surface-class-examples" tags="application"}
Classify the surface germs $xy=z^2$ and $\frac13(1,1)$ as terminal, canonical, or klt.
:::

::: {.back card-id="singularity-surface-class-examples"}
The $A_1$ germ $xy=z^2$ is canonical and klt but not terminal: its exceptional $(-2)$-curve has discrepancy $0$. The quotient $\frac13(1,1)$ has a single exceptional $(-3)$-curve with discrepancy $-1/3$, so it is klt but not canonical. Terminal complex surface singularities are smooth.
:::

::: {.front card-id="singularity-slc-node-example" tags="application"}
Why is the curve germ $xy=0$ semi-log-canonical but not log canonical as a variety?
:::

::: {.back card-id="singularity-slc-node-example"}
It is not normal, so it does not satisfy the normality hypothesis for log canonical varieties. Its normalization is two smooth branches, each with the origin as conductor boundary of coefficient $1$. Those pairs are log canonical, and the nodal curve is Gorenstein and satisfies $S_2$, so it is slc.
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

