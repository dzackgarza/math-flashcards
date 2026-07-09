Retract
%
Retract: A subspace $A \subset X$ is a *retract* of $X$ iff there exists a continuous map $f: X\to A$ such that $f\mid_{A} = \id_A$. 
Equivalently it is a *left* inverse to the inclusion.
%
definition
---

Deformation Retract
%
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a morphism $F:X\cross I$ to $X$ such that $F(x, 0) = x, F(x, 1)\in A, F(a, 1) = a$.
Equivalently it is a homotopy between a retraction and the identity.
%
definition
---

Locally Compact
%
A space $X$ is *locally compact* iff for every $x\in X$ there exists an open $U$ and compact $K$ such that $x\in U \subseteq K$.

Compact implies locally compact but not conversely: $\RR^n$.

Non locally-compact spaces: $\QQ, \theset{\vector 0} \union \theset{(x, y) \suchthat x>0} \subset\RR^2$ (since the origin admits no compact neighborhood).
%
definition, counterexample
---

Are singletons open or closed?
%
- In Hausdorff spaces: closed.
%
theorem
---

Normal Space
%
A space $X$ is **normal** iff every two disjoint closed sets have disjoint open neighborhoods.
%
definition
---

Urysohn's Lemma
%
A space $X$ is normal iff for every closed $U, V \subset X$ there exists a continuous function $f: X\to [0, 1]$ with $f(U) = 0, f(V) = 1$, or equivalently $\chi_U \leq f \leq \chi_V$.
%
theorem
---

Hausdorff Space
%
A space $X$ is **Hausdorff** iff for every $x,y \in X$ there exist neighborhoods of $x$ and $y$ that are disjoint from each other.

(Implies uniqueness of limits.)
%
definition
---

Semilocally Simply Connected
%
Every point admits a neighborhood $U$ such that $\pi_1(U) = 0$.
%
definition
---

Local homeomorphism
%
A map $f:X\to Y$ is a local homeomorphism iff for every $x\in X$ there exists a neighborhood $U_x$ such that $f(U_x)$ is open in $Y$ and $f\mid_{U_x}: U_x \to f(U_x)$ is a homeomorphism.

Examples: etale spaces, covering spaces.
%
definition
---

Locally homeomorphic
%
$X$ is *locally homeomorphic* to $Y$ iff every $x\in X$ admits a neighborhood $U_x$ that is homeomorphic to an open subset of $Y$.

Note that $X$ being locally homeomorphic to $Y$ does *not* imply that there exists a local homeomorphism, which needs to be a single map. Counterexample: $S^2$ locally homeomorphic to $\RR^2$, but there is no single local homeomorphism $f:S^2 \to \RR$.
%
definition
---

First Countable
%
A space $X$ is **first countable** iff each $x\in X$ admits a countable neighborhood basis.
%
definition
---

Neighborhood Basis
%
A neighborhood basis about a point $x$ is a collection of open sets $\theset{B_k}_{k\in J}$ such that for every neighborhood $U_x$ of $x$, there exists some $j$ such that $B_k \subseteq U_x$
%
definition
---

Classification of Closed Surfaces
%
There is a commutative monoid $\Sigma = \gens{P, K, T, S \suchthat S=0, 3P = PT, PK = PT}$ where $P = \RP^2, K$ is the Klein bottle, and $T$ is a 2-torus of genus 1.
Thus every surface is homeomorphic to either $\Sigma_{g}$ for $g\geq 0$, i.e. $S^2, \Sigma_1 = T^2, \Sigma_2 = T^2\# T^2, \cdots$ **or** if it is nonorientable, a surface $\bar \Sigma_1 = \RP^2, \bar \Sigma_2 = \RP^2 \# \RP^2, \cdots$.
%
fact
---

Euler Characteristics of Surfaces: $S^n, \Sigma_g, \RP^2, K$.
%
- $\chi(S^1) = 0$
- $\chi(S^2) = 2$
- $\chi(\Sigma_1) = 0$
- $\chi(\Sigma_2) = -2$
- $\chi(\Sigma_3) = -4$
- $\chi(\Sigma_g) = 2-2g$
- $\chi(\RP^2) = 1$
- $\chi(K) = 0$
%
formulas
---

Definition: Closed Surfaces
%
Compact and without boundary.
%
definition
---

Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
%
- Closed subspaces of compact spaces are compact
- Continuous images of compact spaces are compact
- Compact subspaces of Hausdorff spaces are closed
%
theorem, proof
---

Definition: Limit Point
%
A point $x\in X$ is a limit point of $A\subseteq X$ iff every open $U \ni x$ contains a point $y\in A\setminus\theset{x}$.
%
definition
---

Definition: Dense
%
A subset $A\subset X$ is dense in $X$ iff $\cl_X(A) = X$.
%
definition
---

Definition: separable
%
Contains a countable dense subset
%
definition
---

Definition: the discrete topology
%
For $X$ a space, the discrete topology is given by $\tau = \mcp(X)$, i.e. every subset is open.
%
definition
---

Definition: the indiscrete topology
%
For $X$ a space, the indiscrete topology is given by $\tau = \theset{\emptyset, X}$.
%
definition
---

Give an example of a function $f: \RR^n \to \RR$ that is continuous in each variable but not continuous.
%
Take limit along $y=x$ and compare to $y=0$:
\begin{align*}
f(x, y) = 
{\begin{dcases}
xy \over x^2 +y^2} & (x, y) \neq \vector 0 \\
0 & \text{else}
\end{dcases}
.\end{align*}
%
example
