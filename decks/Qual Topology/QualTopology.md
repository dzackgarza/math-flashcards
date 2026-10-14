---
title: "Qual Topology::QualTopology"
---

::: {.front card-id="card-8e1068b00b1b80c0" tags="definition"}
Retract
:::

::: {.back card-id="card-8e1068b00b1b80c0"}
Retract: A subspace $A \subset X$ is a *retract* of $X$ iff there exists a continuous map $f: X\to A$ such that $f\mid_{A} = \id_A$.
Equivalently it is a *left* inverse to the inclusion.
:::

::: {.front card-id="card-1d8d3dd04e78abea" tags="definition"}
Deformation Retract
:::

::: {.back card-id="card-1d8d3dd04e78abea"}
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a morphism $F:X\cross I$ to $X$ such that $F(x, 0) = x, F(x, 1)\in A, F(a, 1) = a$.
Equivalently it is a homotopy between a retraction and the identity.
:::

::: {.front card-id="card-e8afc902c0df3d86" tags="definition, counterexample"}
Locally Compact
:::

::: {.back card-id="card-e8afc902c0df3d86"}
A space $X$ is *locally compact* iff for every $x\in X$ there exists an open $U$ and compact $K$ such that $x\in U \subseteq K$.

Compact implies locally compact but not conversely: $\RR^n$.

Non locally-compact spaces: $\QQ, \theset{\vector 0} \union \theset{(x, y) \suchthat x>0} \subset\RR^2$ (since the origin admits no compact neighborhood).
:::

::: {.front card-id="card-c8b7096ca39ec9c0" tags="theorem"}
Are singletons open or closed?
:::

::: {.back card-id="card-c8b7096ca39ec9c0"}
- In Hausdorff spaces: closed.
:::

::: {.front card-id="card-0271bf42f0833a28" tags="definition"}
Normal Space
:::

::: {.back card-id="card-0271bf42f0833a28"}
A space $X$ is **normal** iff every two disjoint closed sets have disjoint open neighborhoods.
:::

::: {.front card-id="card-5acd656b9c28e873" tags="theorem"}
Urysohn's Lemma
:::

::: {.back card-id="card-5acd656b9c28e873"}
A space $X$ is normal iff for every closed $U, V \subset X$ there exists a continuous function $f: X\to [0, 1]$ with $f(U) = 0, f(V) = 1$, or equivalently $\chi_U \leq f \leq \chi_V$.
:::

::: {.front card-id="card-369c4f64acc62dc4" tags="definition"}
Hausdorff Space
:::

::: {.back card-id="card-369c4f64acc62dc4"}
A space $X$ is **Hausdorff** iff for every $x,y \in X$ there exist neighborhoods of $x$ and $y$ that are disjoint from each other.

(Implies uniqueness of limits.)
:::

::: {.front card-id="card-d31b00070a4d3f45" tags="definition"}
Semilocally Simply Connected
:::

::: {.back card-id="card-d31b00070a4d3f45"}
Every point admits a neighborhood $U$ such that $\pi_1(U) = 0$.
:::

::: {.front card-id="card-482d55ab1d1671cf" tags="definition"}
Local homeomorphism
:::

::: {.back card-id="card-482d55ab1d1671cf"}
A map $f:X\to Y$ is a local homeomorphism iff for every $x\in X$ there exists a neighborhood $U_x$ such that $f(U_x)$ is open in $Y$ and $f\mid_{U_x}: U_x \to f(U_x)$ is a homeomorphism.

Examples: etale spaces, covering spaces.
:::

::: {.front card-id="card-7a1354eee12f05ea" tags="definition"}
Locally homeomorphic
:::

::: {.back card-id="card-7a1354eee12f05ea"}
$X$ is *locally homeomorphic* to $Y$ iff every $x\in X$ admits a neighborhood $U_x$ that is homeomorphic to an open subset of $Y$.

Note that $X$ being locally homeomorphic to $Y$ does *not* imply that there exists a local homeomorphism, which needs to be a single map. Counterexample: $S^2$ locally homeomorphic to $\RR^2$, but there is no single local homeomorphism $f:S^2 \to \RR$.
:::

::: {.front card-id="card-4224d81286acd4e9" tags="definition"}
First Countable
:::

::: {.back card-id="card-4224d81286acd4e9"}
A space $X$ is **first countable** iff each $x\in X$ admits a countable neighborhood basis.
:::

::: {.front card-id="card-547950e7ba2aaa04" tags="definition"}
Neighborhood Basis
:::

::: {.back card-id="card-547950e7ba2aaa04"}
A neighborhood basis about a point $x$ is a collection of open sets $\theset{B_k}_{k\in J}$ such that for every neighborhood $U_x$ of $x$, there exists some $j$ such that $B_k \subseteq U_x$
:::

::: {.front card-id="card-71975ecfbe1f419d" tags="fact"}
Classification of Closed Surfaces
:::

::: {.back card-id="card-71975ecfbe1f419d"}
There is a commutative monoid $\Sigma = \gens{P, K, T, S \suchthat S=0, 3P = PT, PK = PT}$ where $P = \RP^2, K$ is the Klein bottle, and $T$ is a 2-torus of genus 1.
Thus every surface is homeomorphic to either $\Sigma_{g}$ for $g\geq 0$, i.e. $S^2, \Sigma_1 = T^2, \Sigma_2 = T^2\# T^2, \cdots$ **or** if it is nonorientable, a surface $\bar \Sigma_1 = \RP^2, \bar \Sigma_2 = \RP^2 \# \RP^2, \cdots$.
:::

::: {.front card-id="card-260937d86cb5d14b" tags="formulas"}
Euler Characteristics of Surfaces: $S^n, \Sigma_g, \RP^2, K$.
:::

::: {.back card-id="card-260937d86cb5d14b"}
- $\chi(S^1) = 0$
- $\chi(S^2) = 2$
- $\chi(\Sigma_1) = 0$
- $\chi(\Sigma_2) = -2$
- $\chi(\Sigma_3) = -4$
- $\chi(\Sigma_g) = 2-2g$
- $\chi(\RP^2) = 1$
- $\chi(K) = 0$
:::

::: {.front card-id="card-b5a5e82a06ad8406" tags="definition"}
Definition: Closed Surfaces
:::

::: {.back card-id="card-b5a5e82a06ad8406"}
Compact and without boundary.
:::

::: {.front card-id="card-d5a07b6a9ce1b1b1" tags="theorem, proof"}
Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
:::

::: {.back card-id="card-d5a07b6a9ce1b1b1"}
- Closed subspaces of compact spaces are compact
- Continuous images of compact spaces are compact
- Compact subspaces of Hausdorff spaces are closed
:::

::: {.front card-id="card-a66a1d236e2e9f1d" tags="definition"}
Definition: Limit Point
:::

::: {.back card-id="card-a66a1d236e2e9f1d"}
A point $x\in X$ is a limit point of $A\subseteq X$ iff every open $U \ni x$ contains a point $y\in A\setminus\theset{x}$.
:::

::: {.front card-id="card-891893be111fb5e7" tags="definition"}
Definition: Dense
:::

::: {.back card-id="card-891893be111fb5e7"}
A subset $A\subset X$ is dense in $X$ iff $\cl_X(A) = X$.
:::

::: {.front card-id="card-3d6992d3ac8e71db" tags="definition"}
Definition: separable
:::

::: {.back card-id="card-3d6992d3ac8e71db"}
Contains a countable dense subset
:::

::: {.front card-id="card-e835aebf5b70f977" tags="definition"}
Definition: the discrete topology
:::

::: {.back card-id="card-e835aebf5b70f977"}
For $X$ a space, the discrete topology is given by $\tau = \mcp(X)$, i.e. every subset is open.
:::

::: {.front card-id="card-688c3d7ee61e8756" tags="definition"}
Definition: the indiscrete topology
:::

::: {.back card-id="card-688c3d7ee61e8756"}
For $X$ a space, the indiscrete topology is given by $\tau = \theset{\emptyset, X}$.
:::

::: {.front card-id="card-87d70af608f74523" tags="example"}
Give an example of a function $f: \RR^n \to \RR$ that is continuous in each variable but not continuous.
:::

::: {.back card-id="card-87d70af608f74523"}
Take limit along $y=x$ and compare to $y=0$:
\begin{align*}
f(x, y) =
\begin{dcases}
{xy \over x^2 +y^2} & (x, y) \neq \vector 0 \\
0 & \text{else}
\end{dcases}
.\end{align*}
:::
