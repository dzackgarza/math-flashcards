---
title: "Quals::Real Analysis"
---

- What is the $ M{\hbox{-}} $test?

    $ \sum_{n\geq 0} {\left\lVert {f_n} \right\rVert}_{\infty, A} < \infty \implies \sum f_n $ converges absolutely and uniformly on $ A $.

    Here $ {\left\lVert {f_n} \right\rVert}_{\infty, A}\coloneqq\sup_{x\in A}{\left\lvert {f_n(x)} \right\rvert} $.

    Equivalently, if there is a sequence $ \left\{{M_n}\right\} $ where $ {\left\lvert {f_n(x)} \right\rvert} \leq M_n $ for all $ x\in A $ and $ \sum M_n < \infty $.

- Give several equivalent characterizations of completeness.

    $ X $ is complete $ \iff $ $ X $ is Cauchy complete $ \iff $ absolutely convergent implies convergent for series.

- What is the Arzela-Ascoli theorem?

    A sequence $ f_i $ has a uniformly convergent subsequence $ \iff $ the sequence is uniformly bounded and uniformly equicontinuous.

- What is Minkowski's inequality?

    For $ 1 \leq p < \infty $,

    $${\left\lVert {f + g} \right\rVert}_p \leq {\left\lVert {f} \right\rVert}_p + {\left\lVert {g} \right\rVert}_p$$

- What is Young's inequality?

    For $ 1\leq p, q\leq r \leq \infty $ with $ {1\over p} + {1\over q} - {1\over r} = 1 $, then

    $${\left\lVert {f\ast g} \right\rVert}_r \leq {\left\lVert {f} \right\rVert}_p {\left\lVert {g} \right\rVert}_q$$

    Useful cases:

    $$\begin{aligned} \|f * g\|_1 & \leq\|f\|_1\|g\|_1 \\ \|f * g\|_p & \leq\|f\|_1\|g\|_p \\ \|f * g\|_{\infty} & \leq\|f\|_p\|g\|_q \\ \|f * g\|_{\infty} & \leq\|f\|_2\|g\|_2\end{aligned}$$

- What is a Baire space?

    $ X $ is a Baire space $ \iff $ whenever $ \left\{{U_n}\right\} $ is a *countable* collection of open dense subsets of $ X $, then their intersection $ \cap U_n $ is again dense.

- What is a first category set? A second category?

    A subset is *first category* $ \iff $ it is countable union of nowhere dense sets, *second category* otherwise.

- What does it mean for a set to be nowhere dense?

    A set is $ A $ **nowhere dense** if its closure has empty interior $ \qty{\overline{A}}^\circ $, equivalently it is not dense in *any* nonempty open set.

    For $ {\mathbf{R}} $, every interval $ I $ contains a subinterval $ S\subset I $ with $ S\cap A = \emptyset $, i.e. its closure contains no intervals.

    Intuition: elements are not tightly clustered, set is full of holes.

- Give an example of a set that is not nowhere dense.

    Counterexample: $ \left\{{1 \over n}\right\}, {\mathbf{Z}} $ are nowhere dense, $ {\mathbf{Q}}, {\mathbf{Z}}\cup\qty{(a, b)\cap{\mathbf{Q}}} $ is *not* nowhere dense

- What is equicontinuity? Uniform equicontinuity?

    For $ X, Y $ metric spaces and $ \mathcal{F} $ a family of functions, $ F $ is *equicontinuous at $ x_0 $* $ \iff $ for every $ \varepsilon > 0 $ there exists a $ \delta(\varepsilon, x_0)>0 $ such that

    $$x\in B_\delta(x_0) \implies f_i(x) \in B_\varepsilon(f_i(x_0))$$

    for all $ f_i \in \mathcal{F} $.

    The family $ F $ is *uniformly equicontinuous* $ \iff $ $ \delta(\varepsilon) $ only depends on $ \varepsilon $ and holds for any pair $ x_1, x_2 $ with $ x_1 \in B_\delta(x_2) $.

- What is the reverse triangle inequality?

    $${\left\lvert {\, {\left\lVert {x_{}} \right\rVert} - {\left\lVert {y} \right\rVert} \,} \right\rvert} \leq {\left\lVert {x-y} \right\rVert}$$

- What is a meagre set?

    A set is *meagre* $ \iff $ it is a countable union of nowhere dense sets.

- Characterize the set $ D_f $ of discontinuities of a function.

    Always $ F_\sigma $, closed, positive oscillation.

    $ f_n\to f $ with $ f_n $ continuous $ \implies D_f $ is meager.

    (Lebesgue criterion) $ f \in \mathcal{R}(a, b) $ and bounded $ \implies D_f $ is null.

    $ f $ monotone $ \implies D_f $ is countable, and additionally $ f $ d$ \iff $erentiable on $ (a, b) \implies D_f $ is null.

- What is the Baire category theorem?

    If $ X $ is a complete metric space or a locally compact Hausdorff space, then $ X $ is a Baire space.

    A (non-empty) complete metric space is *not* the countable union of nowhere dense sets.

- What is the Caratheodory characterization of outer measure?

    $ E\subseteq {\mathbf{R}}^n $ is measurable \( \$\iff \)$ for all $ A\subset {\mathbf{R}}^n $,

    $$m_*(A) = m_*(E\cap A) + m_*(E\cap A^c)$$

- What are almost disjoint sets?

    $ A^\circ \cap B^\circ = \emptyset $

- What is convergence in measure?

    $$\lim _{k \rightarrow \infty} m\left(\left\{x \in E|| f_{k}(x)-f(x) |>\alpha\right\}\right)=0$$

- What is a separable space?

    Contains a countable dense subset.

- Is the composition of Lebesgue measurable functions again Lebesgue measurable?

    **No:** Take $ f: [0, 1]\to [0, 1] $ the Cantor-Lebesgue function (monotonic and cts) and $ C $ the Cantor set

    $ f(C) = [0, 1] $, so define $ g(x) = f(x) +x $ so $ g:[0, 1] \to [0, 2] $ (strictly monotonic and cts, so a homeomorphism), so $ g^{-1} $ is cts and thus measurable.

    $ \mu(g(C)) = 1>0 $ (because $ f $ is constant on every interval in $ C^c $) so $ g(C) \supseteq A $ a non-measurable subset

    $ g^{-1}(A) \subset C $ with $ \mu(C) = 0 $ implies $ g^{-1}(A) $ is a measurable set, so $ \chi_{g^{-1}(A)} $ is a measurable function

    Then $ k\coloneqq\chi_{g^{-1}(A)} \circ g^{-1} $ isn't measurable since

    $$k^{-1}(1) = \qty{ (g^{-1})^{-1}\circ \chi_{g^{-1}(A)} }(1) = g(g^{-1}(A)) = A.$$

    is not a measurable set.

- What is a dense subset?

    A subset $ A\subseteq X $ is *dense* in $ X $ $ \iff $ $ \mathrm{cl}_X(A) = X $.

- What is the uniform boundedness principle?

    If $ \mathcal{F} $ is a family of bounded operators $ T_n:X\to Y $ between Banach spaces with

    $$\forall x\in X, \qquad \sup_{T_n \in \mathcal{F}} {\left\lVert {T_n(x)} \right\rVert}_Y < \infty$$

    then $ \sup_{T_n\in \mathcal{F}} {\left\lVert {T_n} \right\rVert}_X < \infty $.

    Slogan: pointwise bounded sequences of operators are uniformly bounded.

- What is the diameter of set?

    $ \mathrm{diam}(A) = \sup_{x, y\in A} {\left\lvert {d} \right\rvert}(x, y) $

- What is the Bolzano-Weierstrass Property

    Every sequence has a convergent subsequence

- What is a complete measure?

    A measure whose domain includes all subsets of null sets.

- Define $ \limsup, \liminf $ for sequences of sets. What are their containments?

    $$\liminf _{n \rightarrow \infty} A_n=\bigcup_{n \geq 1} \bigcap_{j \geq n} A_j, \qquad \limsup _{n \rightarrow \infty} A_n=\bigcap_{n \geq 1} \bigcup_{j \geq n} A_j$$

    - Supremum: Union, $ \limsup = \inf\sup $, in infinitely many
    - Infimum: Intersection, $ \liminf = \sup\inf $, eventually in
    - $ \liminf _{n \rightarrow \infty} A_n \subseteq \limsup _{n \rightarrow \infty} A_n $ since "all but finitely many" implies "infinitely often".

- What is the Hahn-Banach theorem?

    If $ p: V\to {\mathbf{R}} $ is a sublinear function and $ \phi: U\to {\mathbf{R}} $ a linear functional on $ U\leq V $ with $ \phi \leq p $, then there exists a $ p{\hbox{-}} $sublinear extension $ \tilde \phi: V\to {\mathbf{R}} $

- What is the Riesz Representation theorem?

    For $ H $ a Hilbert space and $ \varphi \in H {}^{ \vee } $, there exists an $ f\in H $ such that $ x\in H \implies \varphi(x) = {\left\langle {f},~{x} \right\rangle} $ with $ {\left\lVert {f} \right\rVert}_H = {\left\lVert {\varphi} \right\rVert}_{H {}^{ \vee }} $.

- What is a compact operator?

    The image of every bounded subset has compact closure.

    Necessarily bounded

    Closure of space of finite-rank operators in the norm topology

- What is the Borel-Canteli lemma?

    $ \sum P(E_n) < \infty \implies P(\limsup_n E_n) == 0 $

    If $ E_n $ are independent events and $ \sum P(E_n) = \infty $< then $ P(\limsup_n E_n) = 1 $.

- What does small tails mean? Absolute continuity?

    Let $ f\in L^1 $ and $ \varepsilon> 0 $.

    **Small Tails**: there exists an $ N $ such that $ \int_{B_N^c} f < \varepsilon $.

    **Absolute Continuity**: there exists a $ \delta $ such that $ m(E) < \delta \implies \int_E {\left\lvert {f} \right\rvert} < \varepsilon $.
