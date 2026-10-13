---
title: "Algebra::Commutative Algebra"
---

::: {.front card-id="card-78a30c232cf446be" tags="definition"}
*Reduced* ring
:::

::: {.back card-id="card-78a30c232cf446be"}
A ring $R$ is *reduced* $\iff R$ has no nonzero nilpotent elements, i.e. $x^n  = 0 \implies x=0$.
:::

::: {.front card-id="card-4857b1586d54ca2b" tags="theorem"}
Nakayama's Lemma
:::

::: {.back card-id="card-4857b1586d54ca2b"}
If $M \in \rmod$ is finitely generated and $I\normal R$ with $I \subseteq \mcj(R)$, then $$IM = M \implies M = 0.$$
:::

::: {.front card-id="card-03b60cc91948791d" tags="definition"}
Definition: A natural transformation between $F, G: \mathcal{C}\to\mathcal{D}$
:::

::: {.back card-id="card-03b60cc91948791d"}
A natural transformation $\eta$ is a class of morphism $\eta = \theset{\eta_x: F(x) \to G(x)~\forall x\in  \mathcal{C}}$ such that the following square commutes:
:::

::: {.front card-id="card-2b24915fc8a6f88e" tags="theorem"}
Noether Normalization
:::

::: {.back card-id="card-2b24915fc8a6f88e"}
If $A$ is a finitely generated algebra over a field $k$, there are algebraically independent elements $x_1,\ldots,x_d\in A$ such that $A$ is finite as a module over $k[x_1,\ldots,x_d]$. Here $d=\dim A$.
:::

::: {.front card-id="card-2e1939e74e2dff9e" tags="theorem"}
Zariski's Lemma
:::

::: {.back card-id="card-2e1939e74e2dff9e"}
If a field extension is finitely generated as a $k\dash$algebra then it is finite degree.
:::

::: {.front card-id="card-4d279de678f7f5fe" tags="algebra, commutative-algebra"}
Regular Ring
:::

::: {.back card-id="card-4d279de678f7f5fe"}
$R$ is regular $\iff R$ is Noetherian and every finitely generated $R\dash$module has a finite resolution by finitely-generated projective $R\dash$modules.
:::

::: {.front card-id="card-e7c416c9ce41a7cd" tags="commutative-algebra"}
Dedekind Rings
:::

::: {.back card-id="card-e7c416c9ce41a7cd"}
Every ideal is projective.
:::

::: {.front card-id="card-cacc12c1d9815f7a" tags="algebra"}
Idempotent
:::

::: {.back card-id="card-cacc12c1d9815f7a"}
An element $x$ in a set with a closed binary operation $\cdot$ is *idempotent* iff $x\cdot x = x$.
:::

::: {.front card-id="card-3e058eb429a38ac7" tags="definition"}
Definition: Primary Decomposition
:::

::: {.back card-id="card-3e058eb429a38ac7"}
In a Noetherian ring, every ideal $I$ can be written as a finite intersection $I=Q_1\cap\cdots\cap Q_r$ of primary ideals. An ideal $Q$ is primary if $ab\in Q$ and $a\notin Q$ imply $b^n\in Q$ for some $n\geq1$.
:::
