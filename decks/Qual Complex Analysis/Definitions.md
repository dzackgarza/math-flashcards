---
title: "Qual Complex Analysis::Definitions"
---

- Definition: A pole $a$ of order $m$

    The smallest $m$ such that 
    $$
    \lim_{z\to a}(z-a)^{m+1}f(z) < \infty \text{ but } \lim_{z\to a}(z-a)^{k\leq m} f(z) = \infty
    .$$

    tags: definition

- Definition: A removable singularity

    A pole of order zero, so 
    $$
    \lim_{z\to z_0}f(z) < \infty
    $$
    and $f$ is bounded on some neighborhood of $z_0$.

    tags: definition

- Definition: An essential singularity

    An isolated singularity that is not a pole (or removable).
    $$
    \lim_{z\to z_0 } f(z) \text{ DNE }
    .$$

    tags: definition

- Conformal Map

    A holomorphic map with nowhere vanishing derivative (locally injective).

    tags: definition

- Normal family

    A family of functions $\mcf \da \ts{f_j}_{j\in J}$ is **normal** iff every sequence $\ts{f_k}$ has a subsequence that converges locally uniformly, i.e. $\ts{f_{k_i}}$ converges uniformly on every compact subset.

    tags: definition

- Equicontinuity

    A family of functions $f_n$ is **equicontinuous** iff for every $\eps$ there exists a $\delta = \delta(\eps)$ (not depending on $n$ or $f_n$) such that
    $$
    \abs{x-y}<\delta \implies \abs{f_n(x) - f_n(y)} < \eps
    \qquad \forall n
    .$$

    tags: definition
