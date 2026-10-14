---
title: "Analysis::Functional Analysis"
---

::: {.front card-id="card-25240e0a1cfbb60a" tags="theorem"}
Riesz Representation Theorem
:::

::: {.back card-id="card-25240e0a1cfbb60a"}
For $1\leq p <\infty$, $X \subset \RR^n$ measurable, $\Lambda \in L^p(X)\dual$, there exists a unique $g\in L^q(X)$ such that
$$\begin{align*}
\forall f\in L^p(X), \quad \Lambda(f) &= \int_X fg \\
\norm{\Lambda}_{L^p(X)\dual} &= \norm{g}_{L^q(X)}
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
then $\sup_{T_n\in \mathcal{F}} \norm{T_n}_X < \infty$.

> Slogan: pointwise bounded sequences of operators are uniformly bounded.
:::

::: {.front card-id="card-63fa36a22df22e28"}
What is the uniform boundedness principle?
:::

::: {.back card-id="card-63fa36a22df22e28"}
If $\mathcal{F}$ is a family of bounded operators $T_n:X\to Y$ between Banach spaces with
$$\forall x\in X, \qquad \sup_{T_n \in \mathcal{F}} {\left\lVert {T_n(x)} \right\rVert}_Y < \infty$$
then $\sup_{T_n\in \mathcal{F}} {\left\lVert {T_n} \right\rVert}_X < \infty$.

Slogan: pointwise bounded sequences of operators are uniformly bounded.
:::

::: {.front card-id="card-a18e45a44e26f012"}
What is the Hahn-Banach theorem?
:::

::: {.back card-id="card-a18e45a44e26f012"}
If $p: V\to {\mathbf{R}}$ is a sublinear function and $\phi: U\to {\mathbf{R}}$ a linear functional on $U\leq V$ with $\phi \leq p$, then there exists a $p{\hbox{-}}$sublinear extension $\tilde \phi: V\to {\mathbf{R}}$
:::

::: {.front card-id="card-7bc8fd9fa6929936"}
What is the Riesz Representation theorem?
:::

::: {.back card-id="card-7bc8fd9fa6929936"}
For $H$ a Hilbert space and $\varphi \in H {}^{ \vee }$, there exists an $f\in H$ such that $x\in H \implies \varphi(x) = {\left\langle {f},~{x} \right\rangle}$ with ${\left\lVert {f} \right\rVert}_H = {\left\lVert {\varphi} \right\rVert}_{H {}^{ \vee }}$.
:::

::: {.front card-id="card-bbc73d2319c2d35e"}
What is a compact operator?
:::

::: {.back card-id="card-bbc73d2319c2d35e"}
The image of every bounded subset has compact closure.

Necessarily bounded

Closure of space of finite-rank operators in the norm topology
:::

::: {.front card-id="card-cfebb53fccab58c3" tags="theorem"}
Hahn-Banach Theorem
:::

::: {.back card-id="card-cfebb53fccab58c3"}
If $p: V\to \RR$ is a sublinear function and $\phi: U\to \RR$ a linear functional on $U\leq V$ with $\phi \leq p$, then there exists a $p\dash$sublinear extension $\tilde \phi: V\to \RR$
:::

::: {.front card-id="card-762a1f458d4aad89" tags="theorem"}
Riesz Representation Theorem
:::

::: {.back card-id="card-762a1f458d4aad89"}
For $H$ a Hilbert space and $\varphi \in H\dual$, there exists an $f\in H$ such that $x\in H \implies \varphi(x) = \inner{f}{x}$ with $\norm{f}_H = \norm{\varphi}_{H\dual}$.
:::

::: {.front card-id="card-30bcc45fb8eb91b9" tags="definition"}
Compact Operator
:::

::: {.back card-id="card-30bcc45fb8eb91b9"}
- The image of every bounded subset has compact closure.
- Necessarily bounded
- Closure of space of finite-rank operators in the norm topology
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
