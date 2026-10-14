---
title: "Basics::Functions and Sets"
---

::: {.front card-id="card-44cb3f71b3da138c" tags="definition"}
Functional characterization of injective functions.
:::

::: {.back card-id="card-44cb3f71b3da138c"}
$$
f(x) = f(y) \implies x=y \iff f \text{ has a left inverse.}
.$$
:::

::: {.front card-id="card-0e941ec5ea10f983" tags="definition"}
Functional characterization of surjective functions.
:::

::: {.back card-id="card-0e941ec5ea10f983"}
$$
\forall y, \exists X \text{ such that } f(x) = y \iff f\text{ has a right inverse, } \exists g \text{ such that } f(g(y)) = y\, \forall y
.$$
:::

::: {.front card-id="card-bbc70498dfc1b62d" tags="misc"}
$f^{-1} \left( \bigcup_i U_i \right) =_? \bigcup_i f^{-1}(U_i)$?
:::

::: {.back card-id="card-bbc70498dfc1b62d"}
Yes:
$$
\begin{align}
f^{-1}\left[\bigcup_{i \in I} U_{i}\right] &=\left\{x \in X \mid f(x) \in \bigcup_{i \in I} U_{i}\right\} \\
&=\left\{x \in X \mid \exists i \in I \text { such that } f(x) \in U_{i}\right\} \\
&=\bigcup_{i \in I}\left\{x \in X \mid f(x) \in U_{i}\right\} \\
&=\bigcup_{i \in I} f^{-1}\left[U_{i}\right]
\end{align}
$$
Preimages of disjoint sets are disjoint, so the same holds for disjoint unions: $f^{-1} \left( \coprod_i U_i \right) = \coprod_i f^{-1}(U_i)$.
:::

::: {.front card-id="card-4e3e938b00ff3359" tags="misc"}
$f^{-1} \left( \bigcap U_i \right) =_? \bigcap_i f^{-1} U_i$?
:::

::: {.back card-id="card-4e3e938b00ff3359"}
Yes
:::

::: {.front card-id="card-f24d683913c1e5a1" tags="misc"}
True or false: $X =_? (f^{-1} \circ f)(X)$
:::

::: {.back card-id="card-f24d683913c1e5a1"}
Only when $f$ is injective: in general only $X \subseteq (f^{-1} \circ f)(X)$, with equality for every $X$ iff $f$ is injective.
:::

::: {.front card-id="card-f0af314ba0599d9d" tags="misc"}
True or false: $X =_? (f\circ f^{-1})(X)$
:::

::: {.back card-id="card-f0af314ba0599d9d"}
Only when $f$ is surjective: in general $(f\circ f^{-1})(X) = X \cap \operatorname{im} f \subseteq X$, with equality for every $X$ iff $f$ is surjective.
:::

::: {.front card-id="card-8b225a8506b564ad" tags="misc"}
True or false: $f^{-1}(A) \setminus f^{-1}(B) =_? f^{-1}(A\setminus B)$
:::

::: {.back card-id="card-8b225a8506b564ad"}
Yes.
For images, only an inclusion: $f(A) \setminus f(B) \subseteq f(A\setminus B)$.
:::

::: {.front card-id="card-3929386b1324c8e9" tags="unsorted"}
What inverses exist for injective (resp. surjective) functions?
:::

::: {.back card-id="card-3929386b1324c8e9"}
- Injections: left inverses, i.e. $f(x) = f(y) \implies x=y$
- Surjections: right inverses
:::

