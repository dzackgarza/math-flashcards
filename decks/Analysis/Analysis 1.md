Equivalent Characterizations of Completeness
%
- Every Cauchy sequence converges
- Every absolutely convergent series converges
%
definition
---

Arzela-Ascoli Theorem
%
A sequence of functions \(\theset{f_n}\) has a uniformly convergent subsequence \(\iff \theset{f_n}\) is uniformly bounded and uniformly equicontinuous.
%
theorem
---

Minkowski's Inequality
%
For $1 \leq p < \infty$,
\[
\norm{f + g}_p \leq \norm{f}_p + \norm{g}_p
.\]
%
theorem
---

Young's Inequality
%
For $1\leq p, q\leq r \leq \infty$ with ${1\over p} + {1\over q} - {1\over r} = 1$, then $\norm{f\ast g}_r \leq \norm{f}_p \norm{g}_q$.

Useful cases:
\[\begin{align*}
\norm{f\ast g}_1 & \leq \norm{f}_1 \norm{g}_1 \\
\norm{f\ast g}_p & \leq \norm{f}_1 \norm{g}_p \\
\norm{f\ast g}_\infty & \leq \norm{f}_p \norm{g}_q \\
\norm{f\ast g}_\infty & \leq \norm{f}_2 \norm{g}_2
\end{align*}\]
%
formula
---

Baire Space
%
$X$ is a Baire space iff whenever \( \theset{U_n}\) is a *countable* collection of open dense subsets of $X$, then their intersection $\intersect U_n$ is again dense.
%
definition
---

First and Second Category
%
- A subset is *first category* iff it is countable union of nowhere dense sets.
- A subset is *second category* otherwise.
%
definition
---

Nowhere Dense
%
A set is $A$ **nowhere dense** if its closure has empty interior $\qty{\bar A}^\circ$, equivalently it is not dense in *any* nonempty open set.
For $\RR$, every interval $I$ contains a subinterval $S\subset I$ with $S\intersect A = \emptyset$, i.e. its closure contains no intervals.

Intuition: elements are not tightly clustered, set is full of holes.

Counterexample: $\theset{1 \over n}, \ZZ$ are nowhere dense, $\QQ, \ZZ\union \qty{(a, b)\intersect \QQ}$ is *not* nowhere dense
%
definition, example, counterexample
---

Equicontinuous
%
For $X, Y$ metric spaces and $\mathcal{F}$ a family of functions, $F$ is *equicontinuous at \(x_0\)* iff for every $\varepsilon > 0$ there exists a \(\delta(\varepsilon, x_0)>0\) such that \[x\in B_\delta(x_0) \implies f_i(x) \in B_\varepsilon(f_i(x_0))\] for all \(f_i \in \mathcal{F}\).
The family $F$ is *uniformly equicontinuous* iff $\delta(\varepsilon)$ only depends on $\varepsilon$ and holds for any pair \(x_1, x_2\) with \(x_1 \in B_\delta(x_2)\).
%
definition
---

Reverse Triangle Inequality
%
$\abs{\norm x - \norm y} \leq \norm{x-y}$
%
formula
---

Meagre Set
%
A set is *meagre* iff it is a countable union of nowhere dense sets.
%
definition
---

Characterizations of $D_f$, the set of discontinuities of functions
%
- Always \(F_\sigma\), closed, positive oscillation.
- \(f_n\to f\) with \(f_n\) continuous \(\implies D_f\) is meager.
- (Lebesgue criterion) \(f \in \mathcal{R}(a, b)\) and bounded \(\implies D_f\) is null.
- $f$ monotone \(\implies D_f\) is countable, and additionally $f$ differentiable on \((a, b) \implies D_f\) is null.
%
fact
---

Baire Category Theorem
%
If $X$ is a complete metric space or a locally compact Hausdorff space, then $X$ is a Baire space.
A (non-empty) complete metric space is *not* the countable union of nowhere dense sets.
%
theorem
---

Caratheodory Characterization
%
$E\subseteq \RR^n$ is measurable $\iff$ for all $A\subset \RR^n$, 
\( 
m_*(A) = m_*(E\intersect A) + m_*(E\intersect A^c)
\)
%
theorem
---

Definition: Almost Disjoint
%
$A^\circ \intersect B^\circ = \emptyset$
%
definition
---

Convergence in Measure
%
\[
\lim _{k \rightarrow \infty} m\left(\left\{x \in E|| f_{k}(x)-f(x) |>\alpha\right\}\right)=0
.\]
%
definition
---

Proposition: Convergence in measure is equivalent to a.e. convergence
%
Proof: ? Use Egorov's Theorem
%
proof
---

Definition: separable
%
Has a countable dense subset
%
definition
---

Limit definition of exponential function
%
$e^x = \lim_{n \to \infty} \qty{1 + {x\over n}}^n$
%
definition, formula
---

Is a composition of Lebesgue measurable functions measurable?
%
No:

- Take $f: [0, 1]\to [0, 1]$ the Cantor-Lebesgue function (monotonic and cts) and $C$ the Cantor set
- $f(C) = [0, 1]$, so define $g(x) = f(x) +x$ so $g:[0, 1] \to [0, 2]$ (strictly monotonic and cts, so a homeomorphism), so $g\inv$ is cts and thus measurable.
- $\mu(g(C)) = 1>0$ (because $f$ is constant on every interval in $C^c$) so $g(C) \supseteq A$ a non-measurable subset
- $g\inv(A) \subset C$ with $\mu(C) = 0$ implies $g\inv(A)$ is a measurable set, so $\chi_{g\inv(A)}$ is a measurable function
- Then \(k\definedas \chi_{g\inv(A)} \circ g\inv\) isn't measurable since 
  \[ 
  k\inv(1) = \qty{ (g\inv)\inv \circ \chi_{g\inv(A)} }(1) = g(g\inv(A)) = A
  \]
  is not a measurable set.
%
example
---

Dense
%
A subset $A\subseteq X$ is *dense* in $X$ iff $\mathrm{cl}_X(A) = X$.
%
definitions
---

Diameter
%
\[
\mathrm{diam}(A) = \sup_{x, y\in  A} \abs d(x, y)
.\]
%
definition
---

Bolzano Weierstrass Property
%
Every sequence has a convergent subsequence
%
definition
---

Complete Measure
%
A measure whose domain includes all subsets of null sets.
%
definition
---

Uniform Boundedness Principle
%
If $\mathcal{F}$ is a family of bounded operators \(T_n:X\to Y\) between Banach spaces with 
\[  
\forall x\in X, \qquad \sup_{T_n \in \mathcal{F}} \norm{T_n(x)}_Y < \infty
,\]
then \(\sup_{T_n\in \mathcal{F}} \norm{T_n}_X < \infty\).

> Slogan: pointwise bounded sequences of operators are uniformly bounded.
%
theorem
---

Interpretation of $\sup, \inf$ and $\limsup, \liminf$ as set operations
%
- Supremum: Union, $\limsup = \inf\sup$, in infinitely many
- Infimum: Intersection, $\liminf = \sup\inf$, eventually in
%
analysis
