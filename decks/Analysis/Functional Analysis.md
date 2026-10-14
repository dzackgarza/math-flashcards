---
title: "Analysis::Functional Analysis"
---

::: {.front card-id="card-25240e0a1cfbb60a" tags="theorem"}
Riesz Representation Theorem
:::

::: {.back card-id="card-25240e0a1cfbb60a"}
Hilbert spaces: for $H$ a Hilbert space and $\varphi \in \dualof{H}$, there exists a unique $f\in H$ such that $\varphi(x) = \inner{f}{x}$ for all $x\in H$ (inner product linear in the second slot), and $\norm{f}_H = \norm{\varphi}_{\dualof{H}}$.

$L^p$ spaces: for $1\leq p <\infty$ with ${1\over p} + {1\over q} = 1$, $X \subset \RR^n$ measurable, and $\Lambda \in \dualof{L^p(X)}$, there exists a unique $g\in L^q(X)$ such that
$$\begin{align*}
\forall f\in L^p(X), \quad \Lambda(f) &= \int_X fg \\
\norm{\Lambda}_{\dualof{L^p(X)}} &= \norm{g}_{L^q(X)}
\end{align*}$$
:::

::: {.front card-id="card-ee24799e0fe19fc4" tags="theorem"}
Uniform Boundedness Principle
:::

::: {.back card-id="card-ee24799e0fe19fc4"}
If $\mathcal{F}$ is a family of bounded operators $T_n:X\to Y$ between Banach spaces with
$$
\forall x\in X, \qquad \sup_{T_n \in \mathcal{F}} \norm{T_n(x)}_Y < \infty
,$$
then $\sup_{T_n\in \mathcal{F}} \norm{T_n}_{\mathrm{op}} < \infty$, where $\norm{T_n}_{\mathrm{op}} \definedas \sup_{\norm{x}_X \leq 1} \norm{T_n(x)}_Y$.

> Slogan: pointwise bounded families of operators are uniformly bounded.
:::

::: {.front card-id="card-a18e45a44e26f012" tags="theorem"}
Hahn-Banach Theorem
:::

::: {.back card-id="card-a18e45a44e26f012"}
If $p: V\to \RR$ is a sublinear function and $\phi: U\to \RR$ a linear functional on a subspace $U\leq V$ with $\phi \leq p$ on $U$, then there exists a linear extension $\tilde \phi: V\to \RR$ with $\tilde \phi\mid_U = \phi$ and $\tilde \phi \leq p$ on $V$.
:::

::: {.front card-id="card-bbc73d2319c2d35e" tags="definition"}
Compact Operator
:::

::: {.back card-id="card-bbc73d2319c2d35e"}
A linear map $T: X\to Y$ between Banach spaces is *compact* iff the image of every bounded subset has compact closure.

- Necessarily bounded.
- Every norm limit of finite-rank operators is compact. For Hilbert spaces, the compact operators are exactly the norm closure of the finite-rank operators; for general Banach spaces, equality can fail (Enflo).
:::

::: {.front card-id="card-b71874f5765eec11" tags="theorem"}
Open Mapping Theorem
:::

::: {.back card-id="card-b71874f5765eec11"}
Every surjective bounded linear map between Banach spaces is open: it sends open sets to open sets.
:::

::: {.front card-id="card-445ba0597d9308b6" tags="theorem"}
Closed Graph Theorem
:::

::: {.back card-id="card-445ba0597d9308b6"}
A linear map between Banach spaces is bounded if and only if its graph is closed in the product Banach space.
:::
