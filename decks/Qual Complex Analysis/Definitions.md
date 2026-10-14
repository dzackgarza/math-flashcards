---
title: "Qual Complex Analysis::Definitions"
---

::: {.front card-id="card-1772fa06172bf1d1" tags="definition"}
Definition: A pole $a$ of order $m$
:::

::: {.back card-id="card-1772fa06172bf1d1"}
The smallest $m$ such that
$$
\lim_{z\to a}(z-a)^{m+1}f(z) < \infty \text{ but } \lim_{z\to a}(z-a)^{k\leq m} f(z) = \infty
.$$
:::

::: {.front card-id="card-8cdacf40fc69f9b6" tags="definition"}
Definition: A removable singularity
:::

::: {.back card-id="card-8cdacf40fc69f9b6"}
A pole of order zero, so
$$
\lim_{z\to z_0}f(z) < \infty
$$
and $f$ is bounded on some neighborhood of $z_0$.
:::

::: {.front card-id="card-42fcb708069d4ac4" tags="definition"}
Definition: An essential singularity
:::

::: {.back card-id="card-42fcb708069d4ac4"}
An isolated singularity that is not a pole (or removable).
$$
\lim_{z\to z_0 } f(z) \text{ DNE }
.$$
:::

::: {.front card-id="card-d56e3e1aa8104309" tags="definition"}
Conformal Map
:::

::: {.back card-id="card-d56e3e1aa8104309"}
A holomorphic map with nowhere vanishing derivative (locally injective).
:::

::: {.front card-id="card-281605aabeb43de5" tags="definition"}
Normal family
:::

::: {.back card-id="card-281605aabeb43de5"}
A family of functions $\mcf \da \ts{f_j}_{j\in J}$ is **normal** iff every sequence $\ts{f_k}$ has a subsequence that converges locally uniformly, i.e. $\ts{f_{k_i}}$ converges uniformly on every compact subset.
:::

::: {.front card-id="card-50336b73cd2145a3" tags="definition"}
Equicontinuity
:::

::: {.back card-id="card-50336b73cd2145a3"}
A family of functions $f_n$ is **equicontinuous** iff for every $\eps$ there exists a $\delta = \delta(\eps)$ (not depending on $n$ or $f_n$) such that
$$
\abs{x-y}<\delta \implies \abs{f_n(x) - f_n(y)} < \eps
\qquad \forall n
.$$
:::
