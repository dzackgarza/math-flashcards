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
How to remember: limits are like sequences and live above (sequences project), colimits are like gluing and live below (include into disjoint unions) <https://q.uiver.app/?q=WzAsMTUsWzAsNCwiQV97aS0xfSJdLFswLDMsIlxcdmRvdHMiXSxbMCwyLCJBX3tpKzF9Il0sWzQsMywiXFxjZG90cyJdLFs1LDMsIkYoQV97aS0xfSkiXSxbNiwzLCJcXGNkb3RzIl0sWzcsMywiRihBX3tpKzF9KSJdLFs4LDMsIlxcY2RvdHMiXSxbMCwxLCJcXHZkb3RzIl0sWzAsNSwiXFx2ZG90cyJdLFs2LDIsIlxcdW5kZXJzZXR7XFxsb25nbGVmdGFycm93fXtcXG1hdGhybXtsaW19fVxcLCBGICJdLFs2LDQsIlxcdW5kZXJzZXR7XFxsb25ncmlnaHRhcnJvd317XFxtYXRocm17Y29saW19fVxcLCBGIl0sWzYsMCwiXFxmb3JhbGwgTCJdLFs2LDYsIlxcZm9yYWxsIEMiXSxbMCwwXSxbMyw0XSxbNCw1XSxbNSw2XSxbMCwxXSxbMSwyXSxbMiw4XSxbOSwwXSxbMTAsNF0sWzEwLDZdLFs0LDExXSxbNiwxMV0sWzEyLDQsIiIsMix7ImN1cnZlIjoyfV0sWzEyLDEwLCJcXGV4aXN0cyAhIiwyLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEyLDYsIiIsMix7ImN1cnZlIjotMn1dLFs0LDEzLCIiLDIseyJjdXJ2ZSI6Mn1dLFs2LDEzLCIiLDIseyJjdXJ2ZSI6LTJ9XSxbMTEsMTMsIlxcZXhpc3RzICEiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbNiw3XSxbMTksMTUsIkYiLDAseyJjdXJ2ZSI6LTMsInNob3J0ZW4iOnsic291cmNlIjoyMCwidGFyZ2V0IjoyMH19XV0=>https://q.uiver.app/?q=WzAsMTUsWzAsNCwiQV97aS0xfSJdLFswLDMsIlxcdmRvdHMiXSxbMCwyLCJBX3tpKzF9Il0sWzQsMywiXFxjZG90cyJdLFs1LDMsIkYoQV97aS0xfSkiXSxbNiwzLCJcXGNkb3RzIl0sWzcsMywiRihBX3tpKzF9KSJdLFs4LDMsIlxcY2RvdHMiXSxbMCwxLCJcXHZkb3RzIl0sWzAsNSwiXFx2ZG90cyJdLFs2LDIsIlxcdW5kZXJzZXR7XFxsb25nbGVmdGFycm93fXtcXG1hdGhybXtsaW19fVxcLCBGICJdLFs2LDQsIlxcdW5kZXJzZXR7XFxsb25ncmlnaHRhcnJvd317XFxtYXRocm17Y29saW19fVxcLCBGIl0sWzYsMCwiXFxmb3JhbGwgTCJdLFs2LDYsIlxcZm9yYWxsIEMiXSxbMCwwXSxbMyw0XSxbNCw1XSxbNSw2XSxbMCwxXSxbMSwyXSxbMiw4XSxbOSwwXSxbMTAsNF0sWzEwLDZdLFs0LDExXSxbNiwxMV0sWzEyLDQsIiIsMix7ImN1cnZlIjoyfV0sWzEyLDEwLCJcXGV4aXN0cyAhIiwyLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEyLDYsIiIsMix7ImN1cnZlIjotMn1dLFs0LDEzLCIiLDIseyJjdXJ2ZSI6Mn1dLFs2LDEzLCIiLDIseyJjdXJ2ZSI6LTJ9XSxbMTEsMTMsIlxcZXhpc3RzICEiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbNiw3XSxbMTksMTUsIkYiLDAseyJjdXJ2ZSI6LTMsInNob3J0ZW4iOnsic291cmNlIjoyMCwidGFyZ2V0IjoyMH19XV0=
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
