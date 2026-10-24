---
title: "Algebra::Rings"
---

::: {.front card-id="card-4108e89ad5ce521e"}
What are the implications for fields, UFDs, PIDs, etc?
:::

::: {.back card-id="card-4108e89ad5ce521e"}
$$\begin{aligned}\text { field } & \Longrightarrow \text { Euclidean Domain } \Longrightarrow \text { PID } \\ & \Longrightarrow \text { UFD } \Longrightarrow \text { integral domain }\end{aligned}$$
ED not a field: $\CC[x]$.

PID not an ED: $\ZZ { \left[ \scriptstyle { 1 + \sqrt{-19} \over 2} \right] }$.

UFD not a PID: $\ZZ[x]$; take $\left\langle{x, 2}\right\rangle$.

ID not a UFD: $\ZZ { \left[ \scriptstyle {\sqrt{-5}} \right] }$.
:::

::: {.front card-id="card-88343a401eaff1ce" tags="definition"}
Characteristic of a ring
:::

::: {.back card-id="card-88343a401eaff1ce"}
The smallest number $n$ such that $\sum_{j=1}^n 1_R = 0_R$.

Equivalently, the kernel $n\ZZ$ of the unique map $\ZZ\to R$.
:::

::: {.front card-id="card-569223be8caa3985" tags="definition"}
Zero Divisor
:::

::: {.back card-id="card-569223be8caa3985"}
An element $r\in R$ is a *zero divisor* if there exists an $x\in X$ such that $rx=0$.

Equivalently, the map $x\mapsto rx$ is *not* injective.
:::

::: {.front card-id="card-0a80013f33e82707" tags="definition"}
Definition: simple ring.
:::

::: {.back card-id="card-0a80013f33e82707"}
A ring $R$ is **simple** iff its only two-sided ideals are $(0)$ and $R$.
:::

::: {.front card-id="card-ea14ffe5f540048e" tags="definition"}
Definition: irreducible.
:::

::: {.back card-id="card-ea14ffe5f540048e"}
A nonzero nonunit ring element $r\in R$ is *irreducible* iff $r=ab$ implies $a$ or $b$ is a unit.
:::

::: {.front card-id="card-8656828e3e73a5c8" tags="definition"}
Definition: prime.
:::

::: {.back card-id="card-8656828e3e73a5c8"}
A nonzero nonunit ring element $r$ is prime iff $r\divides ab$ implies $r\divides a$ or $r\divides b$.
:::

::: {.front card-id="card-8c2e7e593b0d90ed" tags="definition"}
Definition: integral domain.
:::

::: {.back card-id="card-8c2e7e593b0d90ed"}
A nonzero commutative ring with no nonzero zero divisors.
:::

::: {.front card-id="card-8c25f204d9dacc48" tags="theorem"}
Gauss' Lemma
:::

::: {.back card-id="card-8c25f204d9dacc48"}
Let $R$ be a UFD with fraction field $F$ and $p \in R[x]$.
If $p$ is reducible in $F[x]$, then $p$ is reducible in $R[x]$.

> Implies that $R$ a UFD implies $R[\theset{x_i}]$ is again a UFD.
:::

::: {.front card-id="card-6fbd495f6099a924" tags="definition"}
Definition: prime ideal.
:::

::: {.back card-id="card-6fbd495f6099a924"}
An ideal $\mathfrak{p}\normal R$ is prime iff it is proper and $ab\in \mathfrak{p} \implies a\in \mathfrak{p}$ or $b\in \mathfrak{p}$.
:::

::: {.front card-id="card-da9bbf898137fff8" tags="definition"}
Definition: Maximal ideal.
:::

::: {.back card-id="card-da9bbf898137fff8"}
An ideal $I\normal R$ is **maximal** iff $I\subseteq J \normal R$ implies $J=R$.
:::

::: {.front card-id="card-b4c09528e7fa5d19" tags="definition"}
Definition: Euclidean domain.
:::

::: {.back card-id="card-b4c09528e7fa5d19"}
Admits a "remainder measuring" function $f: R\setminus\theset{0} \to \NN$ such that $a\in R, b\in R^\bullet$ implies there exist $q, r\in R$ such that $a = bq + r$ with either $r=0$ or $f(r) < f(b)$.
:::

::: {.front card-id="card-23c1a013e9df3a25" tags="definition"}
Definition: Unique Factorization Domain
:::

::: {.back card-id="card-23c1a013e9df3a25"}
Every nonzero element $x\in R$ can be written as $x = u\prod p_i$ where the $p_i$ are irreducible and $u \in R^\times$.

This decomposition is unique up to multiplication by a unit, and a permutation of the factors $\sigma$ that makes each $p_i$ associate to $p_{\sigma(i)}$
:::
