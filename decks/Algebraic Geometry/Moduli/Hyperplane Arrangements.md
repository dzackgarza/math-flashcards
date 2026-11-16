---
title: "Algebraic Geometry::Moduli::Hyperplane Arrangements"
---

::: {.front card-id="arrangement-weighted-stability" tags="definition application"}
For hyperplanes $H_i\subset\mathbb P^{r-1}$ with weights $0<b_i\le1$, state the lc and stable-pair tests. What does the compactified moduli problem allow?
:::

::: {.back card-id="arrangement-weighted-stability"}
Work over $\mathbb C$. For every nonempty proper intersection subspace $W$ of the hyperplanes:
$$\left(\mathbb P^{r-1},\sum b_iH_i\right)\text{ lc}
\iff \sum_{H_i\supset W}b_i\le\operatorname{codim}W.$$
Also $K_{\mathbb P^{r-1}}+\sum b_iH_i\sim_{\mathbb Q}(\sum b_i-r)H$, so ampleness requires $\sum b_i>r$.

A weighted stable hyperplane arrangement is a limit of these labeled pairs in the stable-pair moduli problem: $(X,\sum b_iB_i)$ is slc and $K_X+\sum b_iB_i$ ample, with $X$ and the labeled boundary obtained by the weighted-arrangement construction. $X$ may be reducible. An arbitrary stable pair is not thereby a hyperplane arrangement.

Example: in $\mathbb P^2$, three concurrent lines of weight $1$ fail lc since $3>2$; weights $2/3$ satisfy equality at their common point. Additional lines are needed to make total weight exceed $3$.

Reference: Alexeev, *Moduli of Weighted Hyperplane Arrangements*, §§4.3 and 5.
:::

::: {.front card-id="arrangement-visible-contour" tags="definition construction"}
Describe the visible contour of a stable toric variety in $\operatorname{Gr}(r,n)$. Why does it have the dimension of a hyperplane arrangement?
:::

::: {.back card-id="arrangement-visible-contour"}
Let $T=(\mathbb G_m)^n/\mathbb G_m$ act diagonally, $e=(1,\ldots,1)$, and let $Y\subset\operatorname{Gr}(r,n)$ be a stable toric limit of generic $T$-orbit closures. Define
$$G^e=\{V:e\in V\}\cong\operatorname{Gr}(r-1,n-1),\qquad X=Y\cap G^e.$$
This $X$ is the **visible contour**. The locus $G^e$ is the zero locus of the section of the rank-$(n-r)$ universal quotient bundle induced by $e$. In this construction its restriction to $Y$ is regular:
$$\dim X=(n-1)-(n-r)=r-1.$$
The facets $x_i=1$ of $\Delta(r,n)$ supply the labeled boundary divisors on $X$; the facets $x_i=0$ do not meet $X$.

Reference: Alexeev, *Weighted Grassmannians and Stable Hyperplane Arrangements*, §4.
:::

::: {.front card-id="arrangement-weighted-grassmannian" tags="definition construction"}
Define Alexeev's weighted Grassmannian from the Plücker ring. Which grading and weight restriction enter?
:::

::: {.back card-id="arrangement-weighted-grassmannian"}
Let $R=k[p_I]/I_{\mathrm{Pl}}$ be the homogeneous Plücker ring of $\operatorname{Gr}(r,n)$, with $\deg p_I=1$ and torus weight $e_I=\sum_{i\in I}e_i$.

For $b\in\mathbb Q^n$, $0<b_i\le1$, $\sum b_i>r$, retain homogeneous weight spaces whose normalized weight lies in the weighted hypersimplex:
$$R_b=\bigoplus_{\substack{m\ge0,\ \alpha\\
\sum\alpha_i=rm,\ 0\le\alpha_i\le mb_i}}R_{m,\alpha},
\qquad G_b=\operatorname{Proj}R_b.$$
The inequalities are additive, so $R_b$ is a subalgebra. A divisible Veronese gives an integral polarization. Orbit polytopes become $P(V)\cap\Delta_b(r,n)$.

This is the weighted Grassmannian used for arrangements, rather than an arbitrary reweighting of the Plücker variables.

Reference: Alexeev, *Weighted Grassmannians and Stable Hyperplane Arrangements*, Definition 5.2.
:::
