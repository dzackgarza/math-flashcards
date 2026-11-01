---
title: "Logic::Set Theory"
---

::: {.front card-id="card-d2550c00c7687b84"}
What is $\aleph_0$?
:::

::: {.back card-id="card-d2550c00c7687b84"}
Countable cardinality.
:::

::: {.front card-id="card-12631aeb3b722a12" tags="theorem"}
Zorn's Lemma
:::

::: {.back card-id="card-12631aeb3b722a12"}
If every chain in a poset $P$ has an upper bound in $P$, then $P$ contains a maximal element.

Note: a *chain* is a totally ordered subset.
:::

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

::: {.front card-id="card-a1b3c6041fd134eb" tags="definition"}
Axiom of choice
:::

::: {.back card-id="card-a1b3c6041fd134eb"}
Every family $(A_i)_{i \in I}$ of nonempty sets has a choice function: a map $f$ with $f(i) \in A_i$ for all $i \in I$.
:::

::: {.front card-id="card-d9f71ee53d0d2061" tags="definition"}
Countable set
:::

::: {.back card-id="card-d9f71ee53d0d2061"}
A set $A$ is countable if it is finite or there is a bijection $A\to\mathbb{N}$. Equivalently, its elements can be listed as a sequence (possibly finite). A countably infinite set has cardinality $\aleph_0$.
:::

::: {.front card-id="card-fa2cab9329f11859" tags="definition"}
Inverse function
:::

::: {.back card-id="card-fa2cab9329f11859"}
If $f:X\to Y$ is bijective, its inverse $f^{-1}:Y\to X$ is the unique function with $f^{-1}(f(x))=x$ for all $x\in X$ and $f(f^{-1}(y))=y$ for all $y\in Y$; equivalently $f^{-1}\circ f=\mathrm{id}_X$ and $f\circ f^{-1}=\mathrm{id}_Y$.
:::

::: {.front card-id="card-5b9d076709fa737f" tags="definition"}
Right inverse
:::

::: {.back card-id="card-5b9d076709fa737f"}
A right inverse of $f:X\to Y$ is a function $g:Y\to X$ with $f\circ g=\mathrm{id}_Y$, i.e. $f(g(y))=y$ for all $y\in Y$. A function has a right inverse iff it is surjective (the converse uses the axiom of choice).
:::

::: {.front card-id="card-47e9186b0c6eb7b5" tags="definition"}
Set difference
:::

::: {.back card-id="card-47e9186b0c6eb7b5"}
The set difference of $A$ and $B$ is $A\setminus B=\{x\in A:x\notin B\}$. When $B\subseteq A$, this is also called the complement of $B$ in $A$.
:::

::: {.front card-id="card-fb924f154ffa2466" tags="definition"}
Total order
:::

::: {.back card-id="card-fb924f154ffa2466"}
A total order (linear order) on $P$ is a partial order such that for all $x,y\in P$, $x\le y$ or $y\le x$. A set equipped with a total order is totally ordered.
:::
