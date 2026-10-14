---
title: "Qual Real Analysis::QualClassReview"
---

::: {.front card-id="card-c45f7b39201a406b" tags="definition"}
Equivalent Characterizations of Completeness
:::

::: {.back card-id="card-c45f7b39201a406b"}
- Every Cauchy sequence converges
- Every absolutely convergent series converges
:::

::: {.front card-id="card-baf546c401c827d7" tags="theorem"}
Arzela-Ascoli Theorem
:::

::: {.back card-id="card-baf546c401c827d7"}
A sequence of functions $\theset{f_n}$ has a uniformly convergent subsequence $\iff \theset{f_n}$ is uniformly bounded and uniformly equicontinuous.
:::

::: {.front card-id="card-951bf4ff7a51114b" tags="theorem"}
Minkowski's Inequality
:::

::: {.back card-id="card-951bf4ff7a51114b"}
For $1 \leq p < \infty$,
$$
\norm{f + g}_p \leq \norm{f}_p + \norm{g}_p
.$$
:::

::: {.front card-id="card-ed683fc8f9e94f46" tags="formula"}
Young's Inequality
:::

::: {.back card-id="card-ed683fc8f9e94f46"}
For $1\leq p, q\leq r \leq \infty$ with ${1\over p} + {1\over q} - {1\over r} = 1$, then  $\norm{f\ast g}_r \leq \norm{f}_p \norm{g}_q$

Useful cases:
$$\begin{align*}
\norm{f\ast g}_1 & \leq \norm{f}_1 \norm{g}_1 \\
\norm{f\ast g}_p & \leq \norm{f}_1 \norm{g}_p \\
\norm{f\ast g}_\infty & \leq \norm{f}_p \norm{g}_q \\
\norm{f\ast g}_\infty & \leq \norm{f}_2 \norm{g}_2
\end{align*}$$
:::

::: {.front card-id="card-7cb6edcc46bd597b" tags="definition"}
Baire Space
:::

::: {.back card-id="card-7cb6edcc46bd597b"}
$X$ is a Baire space iff whenever $\theset{U_n}$ is a *countable* collection of open dense subsets of $X$, then their intersection $\intersect U_n$ is again dense.
:::

::: {.front card-id="card-601ba12e88c9c3f3" tags="definition"}
First and Second Category
:::

::: {.back card-id="card-601ba12e88c9c3f3"}
- A subset is *first category* iff it is countable union of nowhere dense sets.
- A subset is *second category* otherwise.
:::

::: {.front card-id="card-e724f880141b94a3" tags="definition, example, counterexample"}
Nowhere Dense
:::

::: {.back card-id="card-e724f880141b94a3"}
A set is $A$ **nowhere dense** if its closure has empty interior $\qty{\bar A}^\circ$, equivalently it is not dense in *any* nonempty open set.
For $\RR$, every interval $I$ contains a subinterval $S\subset I$ with $S\intersect A = \emptyset$, i.e. its closure contains no intervals.

Intuition: elements are not tightly clustered, set is full of holes.

Counterexample: $\theset{1 \over n}, \ZZ$ are nowhere dense, $\QQ, \ZZ\union \qty{(a, b)\intersect \QQ}$ is *not* nowhere dense
:::

::: {.front card-id="card-633e0bf4eea3325b" tags="definition"}
Equicontinuous
:::

::: {.back card-id="card-633e0bf4eea3325b"}
For $X, Y$ metric spaces and $\mathcal{F}$ a family of functions, $F$ is *equicontinuous at $x_0$* iff for every $\varepsilon > 0$ there exists a $\delta(\varepsilon, x_0)>0$ such that $$x\in B_\delta(x_0) \implies f_i(x) \in B_\varepsilon(f_i(x_0))$$ for all $f_i \in \mathcal{F}$.
The family $F$ is *uniformly equicontinuous* iff $\delta(\varepsilon)$ only depends on $\varepsilon$ and holds for any pair $x_1, x_2$ with $x_1 \in B_\delta(x_2)$.
:::

::: {.front card-id="card-a662b42449aad2f1" tags="formula"}
Reverse Triangle Inequality
:::

::: {.back card-id="card-a662b42449aad2f1"}
$\abs{\norm x - \norm y} \leq \norm{x-y}$
:::

::: {.front card-id="card-b4a7096646ad6de6" tags="definition"}
Meagre Set
:::

::: {.back card-id="card-b4a7096646ad6de6"}
A set is *meagre* iff it is a countable union of nowhere dense sets.
:::

::: {.front card-id="card-efb33f167cd45fc9" tags="fact"}
Characterizations of $D_f$, the set of discontinuities of functions
:::

::: {.back card-id="card-efb33f167cd45fc9"}
- Always $F_\sigma$, closed, positive oscillation.
- $f_n\to f$ with $f_n$ continuous $\implies D_f$ is meager.
- (Lebesgue criterion) $f \in \mathcal{R}(a, b)$ and bounded $\implies D_f$ is null.
- $f$ monotone $\implies D_f$ is countable, and additionally $f$ differentiable on $(a, b) \implies D_f$ is null.
:::

::: {.front card-id="card-9e970e13e6262861" tags="theorem"}
Baire Category Theorem
:::

::: {.back card-id="card-9e970e13e6262861"}
If $X$ is a complete metric space or a locally compact Hausdorff space, then $X$ is a Baire space.
A (non-empty) complete metric space is *not* the countable union of nowhere dense sets.
:::

::: {.front card-id="card-dd168c4b3ba95075" tags="theorem"}
Caratheodory Characterization
:::

::: {.back card-id="card-dd168c4b3ba95075"}
$E\subseteq \RR^n$ is measurable $\iff$ for all $A\subset \RR^n$,
$m_*(A) = m_*(E\intersect A) + m_*(E\intersect A^c)$
:::

::: {.front card-id="card-eca1d0195fdff25f" tags="definition"}
Definition: Almost Disjoint
:::

::: {.back card-id="card-eca1d0195fdff25f"}
$A^\circ \intersect B^\circ = \emptyset$
:::

::: {.front card-id="card-d91c232df8de82a8" tags="definition"}
Convergence in Measure
:::

::: {.back card-id="card-d91c232df8de82a8"}
$$
\lim _{k \rightarrow \infty} m\left(\left\{x \in E|| f_{k}(x)-f(x) |>\alpha\right\}\right)=0
.$$
:::

::: {.front card-id="card-17e7d38a9f92423f" tags="proof"}
How are convergence in measure and almost-everywhere convergence related?
:::

::: {.back card-id="card-17e7d38a9f92423f"}
On a finite measure space, almost-everywhere convergence implies convergence in measure: Egorov's theorem gives uniform convergence outside a set of arbitrarily small measure. Conversely, convergence in measure gives an almost-everywhere convergent subsequence: choose $n_k$ with $\mu(|f_{n_k}-f|>2^{-k})<2^{-k}$ and apply Borel–Cantelli. The full sequence need not converge almost everywhere.
:::

::: {.front card-id="card-7355ee6da5d3f002" tags="definition"}
Definition: separable
:::

::: {.back card-id="card-7355ee6da5d3f002"}
Has a countable dense subset
:::

::: {.front card-id="card-75fcba9490873a31" tags="definition, formula"}
Limit definition of exponential function
:::

::: {.back card-id="card-75fcba9490873a31"}
$e^x = \lim_{n \to \infty} \qty{1 + {x\over n}}^n$
:::

::: {.front card-id="card-a80ec116a352d39f" tags="example"}
Is a composition of Lebesgue measurable functions measurable?
:::

::: {.back card-id="card-a80ec116a352d39f"}
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

::: {.front card-id="card-25dce4162d60bbb6" tags="definitions"}
Dense
:::

::: {.back card-id="card-25dce4162d60bbb6"}
A subset $A\subseteq X$ is *dense* in $X$ iff $\mathrm{cl}_X(A) = X$.
:::

::: {.front card-id="card-a76cbf9b24086110" tags="definition"}
Diameter
:::

::: {.back card-id="card-a76cbf9b24086110"}
$$
\mathrm{diam}(A) = \sup_{x, y\in  A} \abs d(x, y)
.$$
:::

::: {.front card-id="card-15ce5e4bd24e859e" tags="definition"}
Bolzano Weierstrass Property
:::

::: {.back card-id="card-15ce5e4bd24e859e"}
Every sequence has a convergent subsequence
:::

::: {.front card-id="card-a66021250ef22637" tags="definition"}
Complete Measure
:::

::: {.back card-id="card-a66021250ef22637"}
A measure whose domain includes all subsets of null sets.
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
