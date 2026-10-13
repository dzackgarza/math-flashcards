---
title: "Analysis::QualClassReview"
---

::: {.front card-id="card-4be0991bac313ffa" tags="definition"}
Equivalent Characterizations of Completeness
:::

::: {.back card-id="card-4be0991bac313ffa"}
- Every Cauchy sequence converges
- Every absolutely convergent series converges
:::

::: {.front card-id="card-9877e4377e61211d" tags="theorem"}
Arzela-Ascoli Theorem
:::

::: {.back card-id="card-9877e4377e61211d"}
A sequence of functions $\theset{f_n}$ has a uniformly convergent subsequence $\iff \theset{f_n}$ is uniformly bounded and uniformly equicontinuous.
:::

::: {.front card-id="card-7857fcc55c22eba0" tags="theorem"}
Minkowski's Inequality
:::

::: {.back card-id="card-7857fcc55c22eba0"}
For $1 \leq p < \infty$,
$$
\norm{f + g}_p \leq \norm{f}_p + \norm{g}_p
.$$
:::

::: {.front card-id="card-5e69d956767fc9c7" tags="formula"}
Young's Inequality
:::

::: {.back card-id="card-5e69d956767fc9c7"}
For $1\leq p, q\leq r \leq \infty  $ with ${1\over p} + {1\over q} - {1\over r} = 1  $, then  $\norm{f\ast g}_r \leq \norm{f}_p \norm{g}_q $ 

Useful cases:
$$\begin{align*}
\norm{f\ast g}_1 & \leq \norm{f}_1 \norm{g}_1 \\
\norm{f\ast g}_p & \leq \norm{f}_1 \norm{g}_p \\
\norm{f\ast g}_\infty & \leq \norm{f}_p \norm{g}_q \\
\norm{f\ast g}_\infty & \leq \norm{f}_2 \norm{g}_2 
\end{align*}$$
:::

::: {.front card-id="card-9ff87b8743249324" tags="definition"}
Baire Space
:::

::: {.back card-id="card-9ff87b8743249324"}
$X$ is a Baire space iff whenever $ \theset{U_n}$ is a *countable* collection of open dense subsets of $X$, then their intersection $\intersect U_n$ is again dense.
:::

::: {.front card-id="card-84b79cab675f8b50" tags="definition"}
First and Second Category
:::

::: {.back card-id="card-84b79cab675f8b50"}
- A subset is *first category* iff it is countable union of nowhere dense sets.
- A subset is *second category* otherwise.
:::

::: {.front card-id="card-5d174d7e3bd8ecdb" tags="definition, example, counterexample"}
Nowhere Dense
:::

::: {.back card-id="card-5d174d7e3bd8ecdb"}
A set is $A$ **nowhere dense** if its closure has empty interior $\qty{\bar A}^\circ$, equivalently it is not dense in *any* nonempty open set.
For $\RR$, every interval $I$ contains a subinterval $S\subset I$ with $S\intersect A = \emptyset$, i.e. its closure contains no intervals.

Intuition: elements are not tightly clustered, set is full of holes.

Counterexample: $\theset{1 \over n}, \ZZ$ are nowhere dense, $\QQ, \ZZ\union \qty{(a, b)\intersect \QQ}$ is *not* nowhere dense
:::

::: {.front card-id="card-5b7dbece06083471" tags="definition"}
Equicontinuous
:::

::: {.back card-id="card-5b7dbece06083471"}
For $X, Y$ metric spaces and $\mathcal{F}$ a family of functions, $F$ is *equicontinuous at $x_0$* iff for every $\varepsilon > 0$ there exists a $\delta(\varepsilon, x_0)>0$ such that $$x\in B_\delta(x_0) \implies f_i(x) \in B_\varepsilon(f_i(x_0))$$ for all $f_i \in \mathcal{F}$.
The family $F$ is *uniformly equicontinuous* iff $\delta(\varepsilon)$ only depends on $\varepsilon$ and holds for any pair $x_1, x_2$ with $x_1 \in B_\delta(x_2)$.
:::

::: {.front card-id="card-a07d32cab67edbc4" tags="formula"}
Reverse Triangle Inequality
:::

::: {.back card-id="card-a07d32cab67edbc4"}
$\abs{\norm x - \norm y} \leq \norm{x-y}$
:::

::: {.front card-id="card-43196da656dae3b7" tags="definition"}
Meagre Set
:::

::: {.back card-id="card-43196da656dae3b7"}
A set is *meagre* iff it is a countable union of nowhere dense sets.
:::

::: {.front card-id="card-62de93284dfe86d8" tags="fact"}
Characterizations of $D_f$, the set of discontinuities of functions
:::

::: {.back card-id="card-62de93284dfe86d8"}
- Always $F_\sigma$, closed, positive oscillation.
- $f_n\to f$ with $f_n$ continuous $\implies D_f$ is meager.
- (Lebesgue criterion) $f \in \mathcal{R}(a, b)$ and bounded $\implies D_f$ is null.
- $f$ monotone $\implies D_f$ is countable, and additionally $f$ differentiable on $(a, b) \implies D_f$ is null.
:::

::: {.front card-id="card-f330da61391269f6" tags="theorem"}
Baire Category Theorem
:::

::: {.back card-id="card-f330da61391269f6"}
If $X$ is a complete metric space or a locally compact Hausdorff space, then $X$ is a Baire space.
A (non-empty) complete metric space is *not* the countable union of nowhere dense sets.
:::

::: {.front card-id="card-02ae8d65d6e00185" tags="theorem"}
Caratheodory Characterization
:::

::: {.back card-id="card-02ae8d65d6e00185"}
$E\subseteq \RR^n$ is measurable $\iff$ for all $A\subset \RR^n$, 
$ 
m_*(A) = m_*(E\intersect A) + m_*(E\intersect A^c)
$
:::

::: {.front card-id="card-2ea1124805fcec39" tags="definition"}
Definition: Almost Disjoint
:::

::: {.back card-id="card-2ea1124805fcec39"}
$A^\circ \intersect B^\circ = \emptyset$
:::

::: {.front card-id="card-8685c0b351caa9ac" tags="definition"}
Convergence in Measure
:::

::: {.back card-id="card-8685c0b351caa9ac"}
$$
\lim _{k \rightarrow \infty} m\left(\left\{x \in E|| f_{k}(x)-f(x) |>\alpha\right\}\right)=0
.$$
:::

::: {.front card-id="card-f3a48756f4a28d90" tags="proof"}
Proposition: Convergence in measure is equivalent to a.e. convergence
:::

::: {.back card-id="card-f3a48756f4a28d90"}
Proof: ? Use Egorov's Theorem
:::

::: {.front card-id="card-90c55f2c49052305" tags="definition"}
Definition: separable
:::

::: {.back card-id="card-90c55f2c49052305"}
Has a countable dense subset
:::

::: {.front card-id="card-1c4f6645633ad07e" tags="definition, formula"}
Limit definition of exponential function
:::

::: {.back card-id="card-1c4f6645633ad07e"}
$e^x = \lim_{n \to \infty} \qty{1 + {x\over n}}^n$
:::

::: {.front card-id="card-82595f30c24b1bff" tags="example"}
Is a composition of Lebesgue measurable functions measurable?
:::

::: {.back card-id="card-82595f30c24b1bff"}
No:

- Take $f: [0, 1]\to [0, 1]$ the Cantor-Lebesgue function (monotonic and cts) and $C$ the Cantor set
- $f(C) = [0, 1]$, so define $g(x) = f(x) +x$ so $g:[0, 1] \to [0, 2]$ (strictly monotonic and cts, so a homeomorphism), so $g\inv$ is cts and thus measurable.
- $\mu(g(C)) = 1>0$ (because $f$ is constant on every interval in $C^c$) so $g(C) \supseteq A$ a non-measurable subset
- $g\inv(A) \subset C$ with $\mu(C) = 0$ implies $g\inv(A)$ is a measurable set, so $\chi_{g\inv(A)}$ is a measurable function
- Then $k\definedas \chi_{g\inv(A)} \circ g\inv$ isn't measurable since 
  $$ 
  k\inv(1) = \qty{ (g\inv)\inv \circ \chi_{g\inv(A)} }(1) = g(g\inv(A)) = A
  $$
  is not a measurable set.
:::

::: {.front card-id="card-e58a36f724f1d806" tags="definitions"}
Dense
:::

::: {.back card-id="card-e58a36f724f1d806"}
A subset $A\subseteq X$ is *dense* in $X$ iff $\mathrm{cl}_X(A) = X$.
:::

::: {.front card-id="card-d2ba1b631af8c561" tags="definition"}
Diameter
:::

::: {.back card-id="card-d2ba1b631af8c561"}
$$
\mathrm{diam}(A) = \sup_{x, y\in  A} \abs d(x, y)
.$$
:::

::: {.front card-id="card-26ca2d603c2066a0" tags="definition"}
Bolzano Weierstrass Property
:::

::: {.back card-id="card-26ca2d603c2066a0"}
Every sequence has a convergent subsequence
:::

::: {.front card-id="card-5b863cd3b607da60" tags="definition"}
Complete Measure
:::

::: {.back card-id="card-5b863cd3b607da60"}
A measure whose domain includes all subsets of null sets.
:::

::: {.front card-id="card-dfdbcbd02a009d68" tags="theorem"}
Uniform Boundedness Principle
:::

::: {.back card-id="card-dfdbcbd02a009d68"}
If $\mathcal{F}$ is a family of bounded operators $T_n:X\to Y$ between Banach spaces with 
$$  
\forall x\in X, \qquad \sup_{T_n \in \mathcal{F}} \norm{T_n(x)}_Y < \infty
,$$
then $\sup_{T_n\in \mathcal{F}} \norm{T_n}_X < \infty$.

> Slogan: pointwise bounded sequences of operators are uniformly bounded.
:::
