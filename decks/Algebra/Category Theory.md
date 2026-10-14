---
title: "Algebra::Category Theory"
---

::: {.front card-id="card-03b60cc91948791d" tags="definition"}
Definition: A natural transformation between $F, G: \mathcal{C}\to\mathcal{D}$
:::

::: {.back card-id="card-03b60cc91948791d"}
A natural transformation $\eta$ is a class of morphism $\eta = \theset{\eta_x: F(x) \to G(x)~\forall x\in  \mathcal{C}}$ such that the following square commutes:
:::

::: {.front card-id="card-707d4e469f20e7cc" tags="definition, terms"}
Match up: Limit Colimit to Direct Limit Inverse Limit
:::

::: {.back card-id="card-707d4e469f20e7cc"}
- Limit $\iff$ Inverse Limit
- Colimit $\iff$ Direct Limit
:::

::: {.front card-id="card-0e239a28d7be7486" tags="fact"}
Which adjoints preserve which limits?
:::

::: {.back card-id="card-0e239a28d7be7486"}
Left adjoints preserve colimits.
:::

::: {.front card-id="card-469bd94605accb19"}
What are full and faithful functors?
:::

::: {.back card-id="card-469bd94605accb19"}
Explicitly, let $C$ and $D$ be (locally small) categories and let $F: C \rightarrow D$ be a functor from $C$ to $D$. The functor $F$ induces a function
$$F_{X, Y}: \operatorname{Hom}_{\mathcal{C}}(X, Y) \rightarrow \operatorname{Hom}_{\mathcal{D}}(F(X), F(Y))$$
for every pair of objects $X$ and $Y$ in $C$. The functor $F$ is said to be - faithful if $F_{X, Y}$ is injective ${ }^{[1][2]}$ - full if $F_{X, Y}$ is surjective ${ }^{[2][3]}$ - fully faithful (= full and faithful) if $F_{X, Y}$ is bijective for each $X$ and $Y$ in $C$. A mnemonic for remembering the term "full" is that the image of the function fills the codomain; a mnemonic for remembering the term "faithful" is that you can trust (have faith) that $F(X)=F(Y)$ implies $X=Y$.

Warning: faithful need not imply injective on objects or morphisms!
:::
