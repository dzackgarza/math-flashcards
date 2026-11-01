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
State the open mapping theorem for Banach spaces.
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

::: {.front card-id="card-7cae640f57d55bda" tags="definition"}
Bounded set
:::

::: {.back card-id="card-7cae640f57d55bda"}
A subset $A$ of a normed space $X$ is bounded if
$$\sup_{x\in A}\|x\|<\infty.$$
:::

::: {.front card-id="card-a7af668fcce47ce1" tags="definition"}
Dual space
:::

::: {.back card-id="card-a7af668fcce47ce1"}
For a normed space $X$, the continuous dual $X^*$ is the vector space of all bounded (equivalently continuous) linear functionals $X\to\FF$, equipped with the operator norm.
:::

::: {.front card-id="card-b4abc92182328f79" tags="definition"}
Finite-rank operator
:::

::: {.back card-id="card-b4abc92182328f79"}
A linear map $T:X\to Y$ whose image $T(X)$ is finite-dimensional.
:::

::: {.front card-id="card-4c4fd091114c1cba" tags="definition"}
Graph of a linear map
:::

::: {.back card-id="card-4c4fd091114c1cba"}
For a linear map $T:X\to Y$, its graph is
$$\Gamma(T)=\{(x,Tx):x\in X\}\subseteq X\times Y.$$
:::

::: {.front card-id="card-16702478a880ee87" tags="definition"}
Hölder conjugate exponent
:::

::: {.back card-id="card-16702478a880ee87"}
For $1\le p\le\infty$, the exponent $q\in[1,\infty]$ satisfying
$$\frac1p+\frac1q=1$$
(with $1/\infty=0$).
:::

::: {.front card-id="card-cc8b669ee76fb8e1" tags="definition"}
Linear extension
:::

::: {.back card-id="card-cc8b669ee76fb8e1"}
A linear map $\widetilde\varphi:V\to W$ whose restriction to a subspace $U\subseteq V$ equals a given linear map $\varphi:U\to W$.
:::

::: {.front card-id="card-d172e0c26193a4d7" tags="definition"}
Linear functional
:::

::: {.back card-id="card-d172e0c26193a4d7"}
A linear map $\varphi:V\to\FF$ from a vector space over a field $\FF$ to its scalar field.
:::

::: {.front card-id="card-d77f00243dea830b" tags="definition"}
Norm closure
:::

::: {.back card-id="card-d77f00243dea830b"}
The closure of a subset $S$ of a normed space in the norm topology, i.e. the set of all limits of norm-convergent sequences from $S$.
:::

::: {.front card-id="card-9a0915fcecc51d0f" tags="definition"}
Operator norm
:::

::: {.back card-id="card-9a0915fcecc51d0f"}
For a bounded linear map $T:X\to Y$,
$$\|T\|_{\mathrm{op}}=\sup_{\|x\|_X\le1}\|Tx\|_Y=\sup_{x\neq0}\frac{\|Tx\|_Y}{\|x\|_X}.$$
:::

::: {.front card-id="card-1198a6fd8855dc53" tags="definition"}
Pointwise bounded family
:::

::: {.back card-id="card-1198a6fd8855dc53"}
A family $\mathcal F$ of maps $T:X\to Y$ into a normed space is pointwise bounded if
$$\sup_{T\in\mathcal F}\|Tx\|_Y<\infty\qquad\text{for each }x\in X.$$
:::

::: {.front card-id="card-65fff27ea134525e" tags="definition"}
Product banach space
:::

::: {.back card-id="card-65fff27ea134525e"}
For Banach spaces $X$ and $Y$, the product $X\times Y$ with a norm such as $\|(x,y)\|=\|x\|_X+\|y\|_Y$ (or the maximum of the two norms) is again a Banach space.
:::

::: {.front card-id="card-941154ccb8f2e3d0" tags="definition"}
Sublinear function
:::

::: {.back card-id="card-941154ccb8f2e3d0"}
A map $p:V\to\RR$ on a real vector space such that
$$p(x+y)\le p(x)+p(y),\qquad p(\lambda x)=\lambda p(x)\quad(\lambda\ge0).$$
:::

::: {.front card-id="card-94e5e3d1d5c2a278" tags="definition"}
Uniformly bounded family
:::

::: {.back card-id="card-94e5e3d1d5c2a278"}
A family $\mathcal F$ of bounded operators is uniformly bounded if
$$\sup_{T\in\mathcal F}\|T\|_{\mathrm{op}}<\infty.$$
:::
