---
title: "Category Theory"
---

::: {.front card-id="card-03b60cc91948791d" tags="definition"}
Definition: A natural transformation between $F, G: \mathcal{C}\to\mathcal{D}$
:::

::: {.back card-id="card-03b60cc91948791d"}
A natural transformation $\eta: F \Rightarrow G$ is a family of morphisms $\eta = \theset{\eta_x: F(x) \to G(x)}_{x\in \mathcal{C}}$, one for each object $x$ of $\mathcal{C}$, such that for every morphism $f: x \to y$ in $\mathcal{C}$ the following square commutes:

\begin{tikzcd}
	{F(x)} & {G(x)} \\
	{F(y)} & {G(y)}
	\arrow["{\eta_x}", from=1-1, to=1-2]
	\arrow["{F(f)}"', from=1-1, to=2-1]
	\arrow["{G(f)}", from=1-2, to=2-2]
	\arrow["{\eta_y}"', from=2-1, to=2-2]
\end{tikzcd}

That is, $G(f) \circ \eta_x = \eta_y \circ F(f)$.
:::

::: {.front card-id="card-707d4e469f20e7cc" tags="definition, terms"}
Match the terms *limit* and *colimit* to the terms *direct limit* and *inverse limit*.
:::

::: {.back card-id="card-707d4e469f20e7cc"}
- Limit $\iff$ Inverse Limit
- Colimit $\iff$ Direct Limit
:::

::: {.front card-id="card-0e239a28d7be7486" tags="fact"}
Which adjoints preserve which limits?
:::

::: {.back card-id="card-0e239a28d7be7486"}
Left adjoints preserve colimits, and right adjoints preserve limits.
:::

::: {.front card-id="card-469bd94605accb19"}
What are full and faithful functors?
:::

::: {.back card-id="card-469bd94605accb19"}
Let $\mathcal{C}$ and $\mathcal{D}$ be locally small categories and let $F: \mathcal{C} \rightarrow \mathcal{D}$ be a functor. The functor $F$ induces a function
$$F_{X, Y}: \operatorname{Hom}_\mcc(X, Y) \rightarrow \operatorname{Hom}_\mcd(F(X), F(Y))$$
for every pair of objects $X$ and $Y$ in $\mathcal{C}$. The functor $F$ is said to be

- faithful if $F_{X, Y}$ is injective for each $X$ and $Y$
- full if $F_{X, Y}$ is surjective for each $X$ and $Y$
- fully faithful (= full and faithful) if $F_{X, Y}$ is bijective for each $X$ and $Y$ in $\mathcal{C}$.

A mnemonic for remembering the term "full" is that the image of the function fills the codomain; a mnemonic for remembering the term "faithful" is that you can trust (have faith) that $F(f)=F(g)$ implies $f=g$ for parallel morphisms $f, g: X \to Y$.

Warning: a faithful functor need not be injective on objects, and it need not be injective on the class of all morphisms, because morphisms with different sources or targets can have the same image. A full functor need not be surjective on objects or on morphisms.
:::

::: {.front card-id="card-e8cd3f416cfb75b7"}
What is the universal property for $\mathop{\mathrm{Hom}}$ and products?
:::

::: {.back card-id="card-e8cd3f416cfb75b7"}
$\mathop{\mathrm{Hom}}(A, \prod B_i) \cong \prod \mathop{\mathrm{Hom}}(A, B_i)$, naturally in $A$. That is, a morphism **into** a product is determined by its components, the morphisms into each factor.
:::

::: {.front card-id="card-e28fa3a138b69aea"}
How is the projective limit of an inverse system of sets $(S_i, f_{ij}: S_i \to S_j)_{i \geq j}$ constructed as a set?
:::

::: {.back card-id="card-e28fa3a138b69aea"}
$$\projectivelim S_i=\left\{\left(x_i\right)_{i \in I} \in \prod_{i \in I} S_i \st f_{i j}\left(x_i\right)=x_j \text { for all } i, j \in I \text { with } i \geq j\right\}.$$
:::

::: {.front card-id="card-d87ef906950bd548"}
What is a **limit**? A **colimit**?
:::

::: {.back card-id="card-d87ef906950bd548"}
For a diagram $F: I \to \mathcal{C}$:

- A **limit** $\lim F$ is a cone over $F$ (an object with compatible maps *to* every $F(i)$) that is universal: every other cone over $F$ factors through it by a unique morphism.
- A **colimit** $\operatorname{colim} F$ is a cocone under $F$ (an object with compatible maps *from* every $F(i)$) that is universal: it factors through every other cocone under $F$ by a unique morphism.

How to remember: limits are like sequences and live above (sequences project), colimits are like gluing and live below (include into disjoint unions).

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
A functor $F: \mathsf{C} \to \mathsf{D}$ between preadditive categories is additive iff each map $\mathsf{C}(A, B)\to \mathsf{D}(FA, FB)$ is a homomorphism of abelian groups.
:::

::: {.front card-id="card-88d001160cff1c9a"}
How do you map into or out of a product?
:::

::: {.back card-id="card-88d001160cff1c9a"}
Into: a morphism $A \to \prod_i B_i$ is the same as a family of morphisms $A \to B_i$, one into each factor.

Out of: there is no general description of morphisms out of a product. The dual statement holds for coproducts: a morphism $\coprod_i B_i \to A$ is the same as a family of morphisms $B_i \to A$, one out of each summand.
:::

::: {.front card-id="card-72ae81b6c3284eda"}
Describe pullbacks in terms of homs for representable functors.
:::

::: {.back card-id="card-72ae81b6c3284eda"}
Let $f: Y \to X$. If $\mcf= \mathop{\mathrm{Hom}}_X({-}, Z)$, then $f^* \mcf= \mathop{\mathrm{Hom}}_Y({-}, Y \underset{\scriptscriptstyle {X} }{\times} Z)$.
:::
