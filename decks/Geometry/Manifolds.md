---
title: "Geometry::Manifolds"
---

::: {.front card-id="card-6ac0da19537d1bf9" tags="definition"}
Embedding
:::

::: {.back card-id="card-6ac0da19537d1bf9"}
Homeomorphism onto its image
:::

::: {.front card-id="card-85d8e3873abb3fcb" tags="definition"}
Immersion
:::

::: {.back card-id="card-85d8e3873abb3fcb"}
A smooth map $f:M\to N$ is an immersion if $d f_p:T_pM\to T_{f(p)}N$ is injective for every $p\in M$. Locally, it has the form $(x_1,\ldots,x_m)\mapsto(x_1,\ldots,x_m,0,\ldots,0)$ in suitable coordinates.
:::

::: {.front card-id="card-041a7aff1bdad643" tags="definition"}
Submersion
:::

::: {.back card-id="card-041a7aff1bdad643"}
A smooth map $f:M\to N$ is a submersion if $d f_p:T_pM\to T_{f(p)}N$ is surjective for every $p\in M$. Locally, it is a coordinate projection.
:::

::: {.front card-id="card-a3598957d16b80b1" tags="definition"}
1-form
:::

::: {.back card-id="card-a3598957d16b80b1"}
A section of $T^*M$; locally it has the form $\sum_i f_i\,dx_i$.
:::

::: {.front card-id="card-882f35c6b256788b" tags="definition"}
Coordinate projection
:::

::: {.back card-id="card-882f35c6b256788b"}
A map $(x_1,\dots,x_n)\mapsto(x_1,\dots,x_m)$ that forgets coordinates.
:::

::: {.front card-id="card-e5aad72d9050bd6d" tags="definition"}
Differential of a smooth map
:::

::: {.back card-id="card-e5aad72d9050bd6d"}
For $f:M\to N$, the linear map $df_p:T_pM\to T_{f(p)}N$; in coordinates it is the Jacobian matrix.
:::

::: {.front card-id="card-45bb001ecb537ab9" tags="definition"}
Holonomy
:::

::: {.back card-id="card-45bb001ecb537ab9"}
For a connection, the group of linear transformations of a fiber obtained by parallel transport around loops; the holonomy group measures curvature.
:::

::: {.front card-id="card-4a472c25ea79ed09" tags="definition"}
Local coordinates
:::

::: {.back card-id="card-4a472c25ea79ed09"}
The functions $x_i=\varphi_i$ on a chart; a point $p$ is represented by $(x_1(p),\dots,x_n(p))$.
:::

::: {.front card-id="card-4172f3e641781673" tags="definition"}
Section
:::

::: {.back card-id="card-4172f3e641781673"}
A section of $\pi:E\to X$ is a map $s:X\to E$ such that $\pi\circ s=\mathrm{id}_X$.
:::

::: {.front card-id="card-a6269366cff8a0d2" tags="definition"}
Smooth
:::

::: {.back card-id="card-a6269366cff8a0d2"}
A function $f : U \subseteq \mathbb{R}^n \to \mathbb{R}^m$ is smooth ($C^\infty$) if all partial derivatives of all orders exist and are continuous; on manifolds, $f$ is smooth if $f$ is smooth in every pair of charts.
:::

::: {.front card-id="card-e843cbd8a58329f9" tags="definition"}
Smooth manifold
:::

::: {.back card-id="card-e843cbd8a58329f9"}
A smooth manifold of dimension $n$ is a second-countable Hausdorff topological space locally homeomorphic to $\mathbb{R}^n$, equipped with an atlas whose transition maps are $C^\infty$.
:::

::: {.front card-id="card-b714f938b1494f33" tags="definition"}
Smooth map
:::

::: {.back card-id="card-b714f938b1494f33"}
A map $f:M\to N$ whose local coordinate expression is $C^\infty$.
:::

::: {.front card-id="card-55bd09c5e01a02fe" tags="definition"}
Submanifold
:::

::: {.back card-id="card-55bd09c5e01a02fe"}
A subset $N\subset M$ that is locally a coordinate slice; equivalently, the image of an embedding.
:::

::: {.front card-id="card-4514b4079428150a" tags="definition"}
Wedge product
:::

::: {.back card-id="card-4514b4079428150a"}
The graded-antisymmetric product $\wedge:\Omega^p\times\Omega^q\to\Omega^{p+q}$, with $dx^i\wedge dx^j=-dx^j\wedge dx^i$.
:::
