---
title: "Algebraic Geometry::Moduli::Hyperplane Arrangements"
---

::: {.front card-id="arrangement-weighted-stability" tags="definition application" cite="[@Ale15, §§4.3 and 5]"}
For hyperplanes $H_i\subset\mathbb P^{r-1}$ with weights $0<b_i\le1$, state the lc and stable-pair tests. What singularities and positivity must a KSBA limit satisfy?
:::

::: {.back card-id="arrangement-weighted-stability"}
Work over $\mathbb C$. For every nonempty proper intersection subspace $W$ of the hyperplanes:
$$\left(\mathbb P^{r-1},\sum b_iH_i\right)\text{ lc}
\iff \sum_{H_i\supset W}b_i\le\operatorname{codim}W.$$
Also $K_{\mathbb P^{r-1}}+\sum b_iH_i\sim_{\mathbb Q}(\sum b_i-r)H$, so ampleness requires $\sum b_i>r$.

A KSBA limit $(X,\sum b_iB_i)$ must be slc with $K_X+\sum b_iB_i$ ample and $\mathbb Q$-Cartier; $X$ may be reducible.

Example: in $\mathbb P^2$, three concurrent lines of weight $1$ fail lc since $3>2$; weights $2/3$ satisfy equality at their common point. Additional lines are needed to make total weight exceed $3$.
:::

::: {.front card-id="arrangement-visible-contour" tags="definition construction" cite="[@Ale08b, §4]"}
Describe the visible contour of a stable toric variety in $\operatorname{Gr}(r,n)$. Why does it have the dimension of a hyperplane arrangement?
:::

::: {.back card-id="arrangement-visible-contour"}
Let $T=(\mathbb G_m)^n/\mathbb G_m$ act diagonally, $e=(1,\ldots,1)$, and let $Y\subset\operatorname{Gr}(r,n)$ be a stable toric limit of generic $T$-orbit closures. Define
$$G^e=\{V:e\in V\}\cong\operatorname{Gr}(r-1,n-1),\qquad X=Y\cap G^e.$$
This $X$ is the **visible contour**. The locus $G^e$ is the zero locus of the section of the rank-$(n-r)$ universal quotient bundle induced by $e$. In this construction its restriction to $Y$ is regular:
$$\dim X=(n-1)-(n-r)=r-1.$$
The facets $x_i=1$ of $\Delta(r,n)$ supply the labeled boundary divisors on $X$; the facets $x_i=0$ do not meet $X$.
:::

::: {.front card-id="arrangement-weighted-grassmannian" tags="definition construction" cite="[@Ale08b, Definition 5.2]"}
Define Alexeev's weighted Grassmannian from the Plücker ring. Which grading and weight restriction enter?
:::

::: {.back card-id="arrangement-weighted-grassmannian"}
Let $R=k[p_I]/I_{\mathrm{Pl}}$ be the homogeneous Plücker ring of $\operatorname{Gr}(r,n)$, with $\deg p_I=1$ and torus weight $e_I=\sum_{i\in I}e_i$.

For $b\in\mathbb Q^n$, $0<b_i\le1$, $\sum b_i>r$, retain homogeneous weight spaces whose normalized weight lies in the weighted hypersimplex:
$$R_b=\bigoplus_{\substack{m\ge0,\ \alpha\\
\sum\alpha_i=rm,\ 0\le\alpha_i\le mb_i}}R_{m,\alpha},
\qquad G_b=\operatorname{Proj}R_b.$$
The inequalities are additive, so $R_b$ is a subalgebra. A divisible Veronese gives an integral polarization. Orbit polytopes become $P(V)\cap\Delta_b(r,n)$.

For $b=(1,\ldots,1)$, the weight restriction keeps the whole Plücker ring, so $G_b=\operatorname{Gr}(r,n)$. Lower weights cut the same orbit polytopes by the half-spaces $x_i\le b_i$.
:::

::: {.front card-id="arrangement-weighted-toric-git-construction" tags="definition construction" cite="[@Ale08b, §§5–7; @Ale15, §5.3]"}
Construct a weighted stable hyperplane arrangement from a stable toric variety over the weighted Grassmannian. Specify the quotient, its linearization, and the boundary.
:::

::: {.back card-id="arrangement-weighted-toric-git-construction"}
Let $b\in\mathbb Q^n$, $0<b_i\le1$, $|b|=\sum b_i>r$, and $T=(\mathbb G_m)^n/\mathbb G_m$. On the incidence variety
$$U=\{([z],V)\in\mathbb P^{n-1}\times\operatorname{Gr}(r,n):z\in V\},$$
use the rational line bundle $\mathcal O_{\mathbb P^{n-1}}(|b|-r)\boxtimes\mathcal O_{\operatorname{Gr}}(1)$ with character $b$. Explicitly, for $m$ clearing denominators, retain sections of bidegree $(m(|b|-r),m)$ and torus weight $mb$. Let $U_b^{ss}$ be the locus where some such positive-degree section is nonzero; it has a natural map to $G_b$.

Take a finite equivariant stable toric map $Y\to G_b$ whose polarized components tile $\Delta_b(r,n)$. Then
$$X=(Y\times_{G_b}U_b^{ss})/\!/_{b}T,\qquad
B_i=(Y\times_{G_b}(U_b^{ss}\cap\{z_i=0\}))/\!/_{b}T.$$
This defines the labeled pair $(X,\sum b_iB_i)$, which is slc with ample log canonical divisor. For the normalized orbit closure of a subspace $V$ giving an lc arrangement, the construction recovers $\mathbb P V$ and its coordinate hyperplane sections.

For $r=2$, the output is a weighted stable pointed rational curve: coincident markings indexed by $I$ are allowed iff $\sum_{i\in I}b_i\le1$. This is the curve case of the same weighted stable-pair construction.
:::
