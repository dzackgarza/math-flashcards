---
title: "Topology::Point-Set Topology"
---

::: {.front card-id="card-81d97890a737a1d2" tags="definition, counterexample"}
Locally Compact
:::

::: {.back card-id="card-81d97890a737a1d2"}
A space $X$ is *locally compact* iff for every $x\in X$ there exists an open $U$ and compact $K$ such that $x\in U \subseteq K$.

Compact implies locally compact but not conversely: $\RR^n$.

Non locally-compact spaces:

- $\QQ$,
- $\theset{\vector 0} \union \theset{(x, y) \suchthat x>0} \subset\RR^2$ (since the origin admits no compact neighborhood).
:::

::: {.front card-id="card-1daed49cda4a94ab" tags="theorem"}
Are singletons open or closed?
:::

::: {.back card-id="card-1daed49cda4a94ab"}
- In Hausdorff spaces: closed.
:::

::: {.front card-id="card-6b7a37da40cd9b4d" tags="definition"}
Normal Space
:::

::: {.back card-id="card-6b7a37da40cd9b4d"}
A space $X$ is **normal** iff every two disjoint closed sets have disjoint open neighborhoods.
:::

::: {.front card-id="card-dcac4601570e9b53" tags="theorem"}
Urysohn's Lemma
:::

::: {.back card-id="card-dcac4601570e9b53"}
A space $X$ is normal iff for every pair of disjoint closed sets $U, V \subset X$ there exists a continuous function $f: X\to [0, 1]$ with $f(U) = 0, f(V) = 1$.

Equivalently $\chi_V \leq f \leq \chi_{X\setminus U}$.

Related (Urysohn metrization theorem): a topological space is separable and metrizable $\iff$ it is regular, Hausdorff, and second-countable.
:::

::: {.front card-id="card-33f04bfb88b19535" tags="definition"}
Hausdorff Space
:::

::: {.back card-id="card-33f04bfb88b19535"}
A space $X$ is **Hausdorff** iff for every $x,y \in X$ there exist neighborhoods of $x$ and $y$ that are disjoint from each other.

(Implies uniqueness of limits.)
:::

::: {.front card-id="card-8261391897c1535c" tags="definition"}
Local homeomorphism
:::

::: {.back card-id="card-8261391897c1535c"}
A map $f:X\to Y$ is a local homeomorphism iff for every $x\in X$ there exists a neighborhood $U_x$ such that $f(U_x)$ is open in $Y$ and $f\mid_{U_x}: U_x \to f(U_x)$ is a homeomorphism.

Examples: etale spaces, covering spaces.
:::

::: {.front card-id="card-d434e9fd9377bd7f" tags="definition"}
Locally homeomorphic
:::

::: {.back card-id="card-d434e9fd9377bd7f"}
$X$ is *locally homeomorphic* to $Y$ iff every $x\in X$ admits a neighborhood $U_x$ that is homeomorphic to an open subset of $Y$.

Note that $X$ being locally homeomorphic to $Y$ does *not* imply that there exists a local homeomorphism, which needs to be a single map.

Counterexample: $S^2$ locally homeomorphic to $\RR^2$, but there is no single local homeomorphism $f:S^2 \to \RR^2$: its image would be open and compact in $\RR^2$.
:::

::: {.front card-id="card-c0177f68763dc8b7" tags="definition"}
First Countable
:::

::: {.back card-id="card-c0177f68763dc8b7"}
A space $X$ is **first countable** iff each $x\in X$ admits a countable neighborhood basis.
:::

::: {.front card-id="card-fcb3764c80ce9fad" tags="definition"}
Neighborhood Basis
:::

::: {.back card-id="card-fcb3764c80ce9fad"}
A neighborhood basis about a point $x$ is a collection of open sets $\theset{B_k}_{k\in J}$ containing $x$ such that for every neighborhood $U_x$ of $x$, there exists some $j\in J$ such that $B_j \subseteq U_x$.
:::

::: {.front card-id="card-4ded1dbb972567f6" tags="theorem, proof"}
Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
:::

::: {.back card-id="card-4ded1dbb972567f6"}
- Closed subspaces of compact spaces are compact
- Continuous images of compact spaces are compact
- Compact subspaces of Hausdorff spaces are closed
:::

::: {.front card-id="card-5a97c0a0c9bfc623" tags="definition"}
Definition: Limit Point
:::

::: {.back card-id="card-5a97c0a0c9bfc623"}
A point $x\in X$ is a limit point of $A\subseteq X$ iff every open $U \ni x$ contains a point $y\in A\setminus\theset{x}$.
:::

::: {.front card-id="card-ebaadd8d90edd6fe" tags="definition"}
Definition: Dense
:::

::: {.back card-id="card-ebaadd8d90edd6fe"}
A subset $A\subset X$ is dense in $X$ iff $\cl_X(A) = X$.
:::

::: {.front card-id="card-b80f7435b6f5dde9" tags="definition"}
Definition: separable
:::

::: {.back card-id="card-b80f7435b6f5dde9"}
A space is *separable* iff it contains a countable dense subset.
:::

::: {.front card-id="card-bef9f615b9f3bb0c" tags="definition"}
Definition: the discrete topology
:::

::: {.back card-id="card-bef9f615b9f3bb0c"}
For $X$ a space, the discrete topology is given by $\tau = \mathcal{P}(X)$, i.e. every subset is open.
:::

::: {.front card-id="card-3a7efdf18e9ffc4c" tags="definition"}
Definition: the indiscrete topology
:::

::: {.back card-id="card-3a7efdf18e9ffc4c"}
For $X$ a space, the indiscrete topology is given by $\tau = \theset{\emptyset, X}$.
:::

::: {.front card-id="card-8efb4f8684cc0aef" tags="example"}
Give an example of a function $f: \RR^n \to \RR$ that is continuous in each variable but not continuous.
:::

::: {.back card-id="card-8efb4f8684cc0aef"}
Take limit along $y=x$ and compare to $y=0$:
$$
f(x, y) =
\begin{cases}
{xy \over x^2 +y^2} & (x, y) \neq \vector 0 \\
0 & \text{else}
\end{cases}
.$$
Each slice $x\mapsto f(x, y_0)$ and $y\mapsto f(x_0, y)$ is continuous, but $f(x, x) = {1\over 2}$ for $x\neq 0$ while $f(x, 0) = 0$, so $f$ is not continuous at $\vector 0$.
:::

::: {.front card-id="card-355d255cd65af97d" tags="definition"}
Definition: Sequentially Compact
:::

::: {.back card-id="card-355d255cd65af97d"}
Every sequence has a convergent subsequence.
:::

::: {.front card-id="card-5479f7524e7e99ef" tags="definition"}
Definition: Limit Point Compactness
:::

::: {.back card-id="card-5479f7524e7e99ef"}
Every infinite subset has a limit point.
:::

::: {.front card-id="card-42173ddd8e85dad2"}
Definition: Totally Bounded
:::

::: {.back card-id="card-42173ddd8e85dad2"}
A metric space $(M, d)$ is totally bounded iff $\forall \varepsilon$ there exists a *finite* collection of open balls of radius $\varepsilon$ whose union contains $M$.
:::
