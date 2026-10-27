---
title: "Category Theory"
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
$$F_{X, Y}: \operatorname{Hom}_\mcc(X, Y) \rightarrow \operatorname{Hom}_\mcd(F(X), F(Y))$$
for every pair of objects $X$ and $Y$ in $C$. The functor $F$ is said to be - faithful if $F_{X, Y}$ is injective ${ }^{[1][2]}$ - full if $F_{X, Y}$ is surjective ${ }^{[2][3]}$ - fully faithful (= full and faithful) if $F_{X, Y}$ is bijective for each $X$ and $Y$ in $C$. A mnemonic for remembering the term "full" is that the image of the function fills the codomain; a mnemonic for remembering the term "faithful" is that you can trust (have faith) that $F(X)=F(Y)$ implies $X=Y$.

Warning: faithful need not imply injective on objects or morphisms!
:::

::: {.front card-id="card-e8cd3f416cfb75b7"}
What is the universal property for $\mathop{\mathrm{Hom}}$ and products?
:::

::: {.back card-id="card-e8cd3f416cfb75b7"}
$\mathop{\mathrm{Hom}}(A, \prod B_i) = \prod \mathop{\mathrm{Hom}}(A, B_i)$, i.e. homs **into** a product are determined by homs into coordinates.
:::

::: {.front card-id="card-e28fa3a138b69aea"}
How is the projective limit as a set?
:::

::: {.back card-id="card-e28fa3a138b69aea"}
$$\projectivelim S_i=\left\{\left(x_i\right)_{i \in I} \in \prod_{i \in I} S_i \st f_{i j}\left(x_i\right)=x_j \text { for all } i, j \in I \text { with } i \geq j\right\} \text {. }$$
:::

::: {.front card-id="card-d87ef906950bd548"}
What is a **limit**? A **colimit**?
:::

::: {.back card-id="card-d87ef906950bd548"}
How to remember: limits are like sequences and live above (sequences project), colimits are like gluing and live below (include into disjoint unions)

\begin{tikzcd}
	{} &&&&&& {\forall L} && \\
	\vdots \\
	{A_{i+1}} &&&&&& {\underset{\longleftarrow}{\mathrm{lim}}\, F } \\
	\vdots &&&& \cdots & {F(A_{i-1})} & \cdots & {F(A_{i+1})} & \cdots \\
	{A_{i-1}} &&&&&& {\underset{\longrightarrow}{\mathrm{colim}}\, F} \\
	\vdots \\
	&&&&&& {\forall C}
	\arrow["{\exists !}"', dashed, from=1-7, to=3-7]
	\arrow[curve={height=12pt}, from=1-7, to=4-6]
	\arrow[curve={height=-12pt}, from=1-7, to=4-8]
	\arrow[from=3-1, to=2-1]
	\arrow[from=3-7, to=4-6]
	\arrow[from=3-7, to=4-8]
	\arrow[""{name=0, anchor=center, inner sep=0}, from=4-1, to=3-1]
	\arrow[""{name=1, anchor=center, inner sep=0}, from=4-5, to=4-6]
	\arrow[from=4-6, to=4-7]
	\arrow[from=4-6, to=5-7]
	\arrow[curve={height=12pt}, from=4-6, to=7-7]
	\arrow[from=4-7, to=4-8]
	\arrow[from=4-8, to=4-9]
	\arrow[from=4-8, to=5-7]
	\arrow[curve={height=-12pt}, from=4-8, to=7-7]
	\arrow[from=5-1, to=4-1]
	\arrow["{\exists !}", dashed, from=5-7, to=7-7]
	\arrow[from=6-1, to=5-1]
	\arrow["F", curve={height=-18pt}, between={0.2}{0.8}, Rightarrow, nfold, from=0, to=1]
\end{tikzcd}
:::

::: {.front card-id="card-6b282cf8ba9d9f58"}
What is an **additive** functor?
:::

::: {.back card-id="card-6b282cf8ba9d9f58"}
$F$ is additive iff $\mathsf{C}(A, B)\to \mathsf{D}(FA, FB)$ is a group morphism.
:::

::: {.front card-id="card-88d001160cff1c9a"}
How do you map into or out of a product?
:::

::: {.back card-id="card-88d001160cff1c9a"}
Into: map into each component.
:::

::: {.front card-id="card-72ae81b6c3284eda"}
Describe pullbacks in terms of homs for representable functors.
:::

::: {.back card-id="card-72ae81b6c3284eda"}
If $\mcf= \mathop{\mathrm{Hom}}_X({-}, Z)$, then $f^* \mcf= \mathop{\mathrm{Hom}}_Y({-}, Y \underset{\scriptscriptstyle {X} }{\times} Z)$.
:::
