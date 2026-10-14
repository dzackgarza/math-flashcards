---
title: "Analysis::Complex Analysis::Definitions"
---

::: {.front card-id="card-cad38830857677f5"}
Define $\log(z)$ for $z\in {\mathbf{C}}$.
:::

::: {.back card-id="card-cad38830857677f5"}
$\log(z) = \log\left(re^{i\theta}\right) = \log(r) + i\theta = \log(|z|)+i\arg(z)$
:::

::: {.front card-id="card-1772fa06172bf1d1" tags="definition"}
Definition: A pole $a$ of order $m$
:::

::: {.back card-id="card-1772fa06172bf1d1"}
The smallest $m$ such that
$$
\lim_{z\to a}(z-a)^{m+1}f(z) = 0
.$$
Equivalently, $\lim_{z\to a}(z-a)^{m}f(z)$ is finite and nonzero, while $\lim_{z\to a}\abs{(z-a)^{k}f(z)} = \infty$ for every $k < m$.
:::

::: {.front card-id="card-8cdacf40fc69f9b6" tags="definition"}
Definition: A removable singularity
:::

::: {.back card-id="card-8cdacf40fc69f9b6"}
A pole of order zero, so
$$
\lim_{z\to z_0}(z-z_0)f(z) = 0
.$$
Equivalently, $\lim_{z\to z_0}f(z)$ exists and is finite, and $f$ is bounded on some punctured neighborhood of $z_0$.
:::

::: {.front card-id="card-42fcb708069d4ac4" tags="definition"}
Definition: An essential singularity
:::

::: {.back card-id="card-42fcb708069d4ac4"}
An isolated singularity that is not a pole (or removable). Equivalently,
$$
\lim_{z\to z_0 } f(z) \text{ DNE in } \CC\cup\theset{\infty}
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
A family of functions $\mcf \definedas \theset{f_j}_{j\in J}$ is **normal** iff every sequence $\theset{f_k}$ has a subsequence that converges locally uniformly, i.e. $\theset{f_{k_i}}$ converges uniformly on every compact subset.
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

::: {.front card-id="card-563af3ac08990f07" tags="complex, fact"}
Types of isolated singularities
:::

::: {.back card-id="card-563af3ac08990f07"}
- Removable: $\abs{f(z)}$ is bounded in a punctured disc.
- Poles: $\lim_{z\to p} \abs{f(z)} = \infty$.
- Essential: neither removable nor a pole.
:::
