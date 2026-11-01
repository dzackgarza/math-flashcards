---
title: "Algebra::Lie Algebras"
---

::: {.front card-id="card-3258d55eef2bcb2b" tags="lie-algebra"}
$\Phi$
:::

::: {.back card-id="card-3258d55eef2bcb2b"}
The **root system**.
$$
\alpha \in \Phi \subset \mathfrak{h}^* \iff [h, x] = \alpha(h) x \text{ for all } h\in \mathfrak{h}
$$

- Span a Euclidean space
- $\alpha, c\alpha \in \Phi \implies c=-1$
- $s_\alpha \Phi \subseteq \Phi$ for all $\alpha$
:::

::: {.front card-id="card-4e1818b58dff2d3d" tags="lie-algebra"}
$\mathfrak{g}_\alpha$
:::

::: {.back card-id="card-4e1818b58dff2d3d"}
The **root space**.
$$
\mathfrak{g}_\alpha = \{g\in \mathfrak{g} \mid [h, g] = \alpha(h) g\}
$$
:::

::: {.front card-id="card-a6d7a6a5d7b36275" tags="topics"}
$\Lambda_r$
:::

::: {.back card-id="card-a6d7a6a5d7b36275"}
The (integral) **root lattice**.
$$
\Lambda_r = \mathrm{span}_{\mathbb{Z}}\Phi \subset E
$$
Has a basis given by $\Phi$ or $\Delta$.
:::

::: {.front card-id="card-f9e8cf553a1714d8" tags="topics"}
$\alpha\beta$
:::

::: {.back card-id="card-f9e8cf553a1714d8"}
Something new.
$$
a^b = c
$$
:::

::: {.front card-id="card-aabe516e9962f80b" tags="definition"}
Cartan subalgebra
:::

::: {.back card-id="card-aabe516e9962f80b"}
A maximal abelian subalgebra $\mathfrak h$ of a semisimple Lie algebra consisting of semisimple (diagonalizable) elements; it acts diagonally in the root space decomposition.
:::

::: {.front card-id="card-59b580ba3c70c604" tags="definition"}
Lie algebra
:::

::: {.back card-id="card-59b580ba3c70c604"}
A vector space $\mathfrak g$ with a bilinear bracket $[-,-]:\mathfrak g\times\mathfrak g\to\mathfrak g$ satisfying $[x,x]=0$ (the alternating condition) and the Jacobi identity $[x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0$.
:::

::: {.front card-id="card-defd33894fbf96de" tags="definition"}
Lie bracket
:::

::: {.back card-id="card-defd33894fbf96de"}
The bilinear operation $[-,-]$ on a Lie algebra; it is antisymmetric and satisfies the Jacobi identity.
:::

::: {.front card-id="card-a9efd8b164dcfd36" tags="definition"}
Positive root
:::

::: {.back card-id="card-a9efd8b164dcfd36"}
A root that is a nonnegative integer combination of the simple roots.
:::

::: {.front card-id="card-28e9be3f80ff7129" tags="definition"}
Root reflection
:::

::: {.back card-id="card-28e9be3f80ff7129"}
The reflection $s_\alpha(\beta)=\beta-\frac{2(\alpha,\beta)}{(\alpha,\alpha)}\alpha$ across the hyperplane perpendicular to the root $\alpha$.
:::

::: {.front card-id="card-e1a63b27cfa8a086" tags="definition"}
Root space
:::

::: {.back card-id="card-e1a63b27cfa8a086"}
For a Lie algebra $\mathfrak g$ with Cartan subalgebra $\mathfrak h$ and $\alpha\in\mathfrak h^*$, the subspace $\mathfrak g_\alpha=\{x\in\mathfrak g:[h,x]=\alpha(h)x\text{ for all }h\in\mathfrak h\}$.
:::

::: {.front card-id="card-3ab440387f15649b" tags="definition"}
Root system
:::

::: {.back card-id="card-3ab440387f15649b"}
A finite set $\Phi$ of nonzero vectors spanning a Euclidean space $E$ such that for each $\alpha\in\Phi$ the only multiples of $\alpha$ in $\Phi$ are $\pm\alpha$, the reflection $s_\alpha$ permutes $\Phi$, and $2(\beta,\alpha)/(\alpha,\alpha)\in\mathbb Z$ for all $\alpha,\beta\in\Phi$.
:::

::: {.front card-id="card-3bd92481facd8c81" tags="definition"}
Universal enveloping algebra
:::

::: {.back card-id="card-3bd92481facd8c81"}
The associative algebra $U(\mathfrak g)=T(\mathfrak g)/(xy-yx-[x,y]:x,y\in\mathfrak g)$, universal for homomorphisms from $\mathfrak g$ to associative algebras.
:::
