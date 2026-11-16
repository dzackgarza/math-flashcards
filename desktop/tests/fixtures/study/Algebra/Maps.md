---
title: Algebra::Maps
tags: [study-fixture, maps]
---

::: {.front card-id="study-diagram" tags="diagram"}
Name the source and target of $f$.

\begin{tikzcd}
A \arrow[r, "f"] & B
\end{tikzcd}
:::

::: {.back card-id="study-diagram"}
Source: $A$. Target: $B$.
:::

::: {.front card-id="study-injective" tags="definition"}
When is a map $f:A\to B$ injective?
:::

::: {.back card-id="study-injective"}
For all $a,a'\in A$, $f(a)=f(a')$ implies $a=a'$.
:::

::: {.front card-id="study-surjective" tags="definition"}
When is a map $f:A\to B$ surjective?
:::

::: {.back card-id="study-surjective"}
For every $b\in B$ there is $a\in A$ with $f(a)=b$.
:::

::: {.front card-id="study-composition" tags="definition"}
For maps $f:A\to B$ and $g:B\to C$, give $(g\circ f)(a)$.
:::

::: {.back card-id="study-composition"}
$(g\circ f)(a)=g(f(a))$ for $a\in A$.
:::
