---
title: "Algebraic Geometry::Numerical Invariants::Hodge Diamonds"
---

::: {.front card-id="definition-hodge-betti-euler" tags="definition application"}
Define Hodge numbers, Betti numbers, and the two Euler characteristics for a smooth complex projective variety. How do they differ on a K3 surface?
:::

::: {.back card-id="definition-hodge-betti-euler"}
For $X$ of complex dimension $n$,
$$h^{p,q}(X)=\dim_{\mathbb C}H^q(X,\Omega_X^p),\qquad b_i(X)=\dim_{\mathbb Q}H^i(X(\mathbb C),\mathbb Q).$$
Hodge decomposition gives $b_i=\sum_{p+q=i}h^{p,q}$. The topological and holomorphic Euler characteristics are
$$e(X)=\sum_{i=0}^{2n}(-1)^ib_i,\qquad \chi(\mathcal O_X)=\sum_{q=0}^n(-1)^qh^{0,q}.$$
For a K3 surface, $e=1+22+1=24$ while $\chi(\mathcal O)=1-0+1=2$. The decomposition and Hodge symmetry used here require the Kähler hypothesis in the compact complex setting.
:::

::: {.front card-id="application-invariants-flat-smooth-families" tags="application"}
Which invariants are constant in projective flat families, and what improves for smooth projective families over $\mathbb C$? Give examples of jumping.
:::

::: {.back card-id="application-invariants-flat-smooth-families"}
For a flat projective family with a fixed relative polarization, the Hilbert polynomial is locally constant, hence so are degree, dimension of nonempty fibers, and $\chi(\mathcal O)$. The same statement holds for a coherent sheaf flat over the base. Individual $h^i$ are upper semicontinuous and can jump.

A plane cubic degenerating from smooth to integral nodal has $p_a=1$ and $\chi(\mathcal O)=0$ throughout, but geometric genus drops from $1$ to $0$ and topological Euler characteristic changes from $0$ to $1$.

In a smooth projective family over a connected smooth complex base, Betti numbers, Hodge numbers, and Chern numbers are constant. Picard number can still jump: a very general quartic surface has Picard number one, whereas a smooth quartic containing a line has Picard number at least two. Even on a fixed elliptic curve, degree-zero line bundles have $h^0=0$ except at the trivial bundle, where $h^0=1$.
:::

::: {.front card-id="standard-hodge-curves" tags="formula"}
Give the Hodge diamond of a smooth connected projective complex curve of genus $g$.
:::

::: {.back card-id="standard-hodge-curves"}
$$\begin{matrix}&1&\\g&&g\\&1&\end{matrix}$$
:::

::: {.front card-id="standard-hodge-projective-space" tags="formula"}
Give all Hodge numbers of $\mathbb P^n_{\mathbb C}$.
:::

::: {.back card-id="standard-hodge-projective-space"}
$$h^{p,q}(\mathbb P^n)=\begin{cases}1&p=q,\ 0\le p\le n,\\0&\text{otherwise}.\end{cases}$$
:::

::: {.front card-id="standard-hodge-quadrics" tags="formula"}
Give all Hodge numbers of a smooth complex quadric $Q^n$, $n\ge1$.
:::

::: {.back card-id="standard-hodge-quadrics"}
All off-diagonal Hodge numbers vanish. Each $h^{p,p}=1$ for $0\le p\le n$, except that $h^{n/2,n/2}=2$ when $n$ is even.
:::

::: {.front card-id="standard-hodge-rational-surfaces" tags="formula"}
Give the Hodge diamonds of $\operatorname{Bl}_{p_1,\ldots,p_r}\mathbb P^2_{\mathbb C}$ at distinct points and of a Hirzebruch surface $\mathbb F_e$.
:::

::: {.back card-id="standard-hodge-rational-surfaces"}
Both have $q=p_g=0$. Their diamonds have the form
$$\begin{matrix}&&1&&\\&0&&0&\\0&&b_2&&0\\&0&&0&\\&&1&&\end{matrix}.$$
For the plane blowup, $b_2=r+1$; for $\mathbb F_e$, $b_2=2$.
:::

::: {.front card-id="standard-hodge-ruled-surfaces" tags="formula"}
Give the Hodge diamond of a geometrically ruled complex surface over a smooth projective curve of genus $g$.
:::

::: {.back card-id="standard-hodge-ruled-surfaces"}
$$\begin{matrix}&&1&&\\&g&&g&\\0&&2&&0\\&g&&g&\\&&1&&\end{matrix}$$
:::

::: {.front card-id="standard-hodge-enriques" tags="formula"}
Give the Hodge diamond of a complex Enriques surface. Does it record the torsion canonical bundle?
:::

::: {.back card-id="standard-hodge-enriques"}
$$\begin{matrix}&&1&&\\&0&&0&\\0&&10&&0\\&0&&0&\\&&1&&\end{matrix}$$
Hodge numbers do not record torsion. The canonical bundle is nontrivial of order $2$.
:::

::: {.front card-id="standard-hodge-abelian-surface" tags="formula"}
Specialize the abelian-variety Hodge formula to an abelian surface.
:::

::: {.back card-id="standard-hodge-abelian-surface"}
$$\begin{matrix}&&1&&\\&2&&2&\\1&&4&&1\\&2&&2&\\&&1&&\end{matrix}$$
:::

::: {.front card-id="standard-hodge-threefolds" tags="formula"}
Give the Hodge diamonds of a smooth complex cubic threefold and a smooth complex quintic threefold.
:::

::: {.back card-id="standard-hodge-threefolds"}
$$\begin{matrix}&&&1&&&\\&&0&&0&&\\&0&&1&&0&\\0&&5&&5&&0\\&0&&1&&0&\\&&0&&0&&\\&&&1&&&\end{matrix}
\qquad
\begin{matrix}&&&1&&&\\&&0&&0&&\\&0&&1&&0&\\1&&101&&101&&1\\&0&&1&&0&\\&&0&&0&&\\&&&1&&&\end{matrix}$$
:::

::: {.front card-id="standard-hodge-blowup" tags="formula"}
How do Hodge numbers change when a smooth complex projective variety $X$ is blown up along a smooth center $Z$ of codimension $c\ge2$?
:::

::: {.back card-id="standard-hodge-blowup"}
$$h^{p,q}(\operatorname{Bl}_ZX)=h^{p,q}(X)+\sum_{i=1}^{c-1}h^{p-i,q-i}(Z).$$
Indices outside the range of $Z$ contribute zero. A point blowup of a surface adds one to $h^{1,1}$ and leaves the other Hodge numbers unchanged.
:::

::: {.front card-id="standard-hodge-products" tags="formula"}
How are the Hodge numbers of a product of smooth projective complex varieties computed?
:::

::: {.back card-id="standard-hodge-products"}
$$h^{p,q}(X\times Y)=\sum_{\substack{a+c=p\\b+d=q}}h^{a,b}(X)h^{c,d}(Y).$$
For curves of genera $g,h$, their product has $q=g+h$, $p_g=gh$, and $h^{1,1}=2+2gh$.
:::

::: {.front card-id="card-b895e365a3b35d5b"}
What is the Hodge diamond for a surface?
:::

::: {.back card-id="card-b895e365a3b35d5b"}
For a smooth projective complex surface, the Hodge diamond is
$$\begin{matrix}&&1&&\\&q&&q&\\p_g&&h^{1,1}&&p_g\\&q&&q&\\&&1&&\end{matrix}$$
where $q=h^{1,0}=h^1(\mathcal O_X)$ and $p_g=h^{2,0}=h^0(\omega_X)$.
:::

::: {.front card-id="card-dca3b01c137d5f80"}
What is the Hodge diamond of a K3?
:::

::: {.back card-id="card-dca3b01c137d5f80"}
For a complex K3 surface, $q=0$, $p_g=1$, and $h^{1,1}=20$.

$h^{p, q}(X) = 1$ for the corners: $h^{0,0} = h^{2,2} = 1$ and $h^{2,0} = h^{0,2} = 1$ since $\Omega^2_X\cong{\mathcal{O}}_X$. $h^{0, 1}(X) = h^{1,0}(X) = 0$, and $h^{2,1} = h^{1,2} = 0$ by Serre duality.

By HRR, Serre duality, and $\Omega_X \cong {\mathbf{T}}_X$,
$$2 h^0\left(\Omega_X\right)-h^1\left(\Omega_X\right)=\operatorname{ch}_2\left(\Omega_X\right)+4=4-\mathrm{c}_2\left(\Omega_X\right)=-20$$
so $h^1(\Omega_X) = 20$ since $h^0(\Omega_X) = h^{1,0}(X) = 0$. The Hodge diamond is
$$\begin{matrix}&&1&&\\&0&&0&\\1&&20&&1\\&0&&0&\\&&1&&\end{matrix}.$$
:::

::: {.front card-id="numerical-abelian-hodge" tags="formula"}
For a complex abelian variety $A$ of dimension $g\ge1$, compute its Hodge numbers, Betti numbers, and Euler characteristics.
:::

::: {.back card-id="numerical-abelian-hodge"}
$$h^{p,q}(A)=\binom gp\binom gq,\qquad b_k(A)=\binom{2g}k,\qquad e(A)=\chi(\mathcal O_A)=0.$$
:::

