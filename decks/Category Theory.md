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

::: {.front card-id="card-e528fa481eb10556" tags="definition"}
Abelian category
:::

::: {.back card-id="card-e528fa481eb10556"}
An additive category that has kernels and cokernels, in which every monomorphism is a kernel and every epimorphism is a cokernel (equivalently, every morphism factors as an epimorphism followed by a monomorphism).
:::

::: {.front card-id="card-75b66c730269a306" tags="definition"}
Abelian group
:::

::: {.back card-id="card-75b66c730269a306"}
An abelian group is a set $A$ with an associative and commutative binary operation $+$, an identity element $0$, and additive inverses: for every $a\in A$ there is $-a$ with $a+(-a)=0$. Equivalently, it is a $\mathbb{Z}$-module.
:::

::: {.front card-id="card-d06c459821b905bd" tags="definition"}
Additive category
:::

::: {.back card-id="card-d06c459821b905bd"}
A category enriched over abelian groups with a zero object and finite biproducts; equivalently, hom-sets are abelian groups, composition is bilinear, and finite products and coproducts exist and coincide.
:::

::: {.front card-id="card-414271731d082070" tags="definition"}
Adjoint functor
:::

::: {.back card-id="card-414271731d082070"}
Functors $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ are adjoint, written $F \dashv G$, if there are natural bijections $\mathrm{Hom}_{\mathcal{D}}(F X, Y) \cong \mathrm{Hom}_{\mathcal{C}}(X, G Y)$ for all $X$ and $Y$.
:::

::: {.front card-id="card-2ac513c40cb8e940" tags="definition"}
Adjunction
:::

::: {.back card-id="card-2ac513c40cb8e940"}
An adjunction $F\dashv G$ between functors $F:\mathcal{C}\to\mathcal{D}$ and $G:\mathcal{D}\to\mathcal{C}$ is a natural bijection $\operatorname{Hom}_{\mathcal{D}}(F(X),Y)\cong\operatorname{Hom}_{\mathcal{C}}(X,G(Y))$ for all $X\in\mathcal{C}$ and $Y\in\mathcal{D}$. Then $F$ is left adjoint to $G$ and $G$ is right adjoint to $F$; equivalently, there are unit $\eta:1_{\mathcal{C}}\Rightarrow G\circ F$ and counit $\varepsilon:F\circ G\Rightarrow1_{\mathcal{D}}$ satisfying the triangle identities.
:::

::: {.front card-id="card-34b9d94f9754cbcb" tags="definition"}
Category
:::

::: {.back card-id="card-34b9d94f9754cbcb"}
A category $\mathcal{C}$ consists of a class of objects, a set of morphisms $\mathcal{C}(X,Y)=\operatorname{Hom}_{\mathcal{C}}(X,Y)$ for each pair of objects $X,Y$, an identity $1_X\in\mathcal{C}(X,X)$, and a composition $\mathcal{C}(Y,Z)\times\mathcal{C}(X,Y)\to\mathcal{C}(X,Z)$, $(g,f)\mapsto g\circ f$, such that composition is associative and $1_Y\circ f=f=f\circ 1_X$.
:::

::: {.front card-id="card-9d2eba9c6dac9b92" tags="definition"}
Class
:::

::: {.back card-id="card-9d2eba9c6dac9b92"}
A class is a collection of sets (or of objects of a category) specified by a property. A proper class is a class that is not a set, such as the class of all sets or of all groups. The objects of a category are allowed to form a proper class.
:::

::: {.front card-id="card-48d6063244a1eded" tags="definition"}
Cocone
:::

::: {.back card-id="card-48d6063244a1eded"}
A cocone under a diagram $F:I\to\mathcal{C}$ is an object $C$ together with morphisms $\iota_i:F(i)\to C$ for all $i\in I$ such that $\iota_j\circ F(u)=\iota_i$ for every morphism $u:i\to j$ in $I$.
:::

::: {.front card-id="card-f119fd025c46d264" tags="definition"}
Colimit
:::

::: {.back card-id="card-f119fd025c46d264"}
The colimit of a diagram $D : I \to \mathcal{C}$ is an object $\varinjlim D$ together with morphisms $D(i) \to \varinjlim D$ forming a cocone, universal among all cocones over $D$.
:::

::: {.front card-id="card-e561c0aeefcb997b" tags="definition"}
Commutative diagram
:::

::: {.back card-id="card-e561c0aeefcb997b"}
A diagram is commutative if every two composable paths in it with the same source and target have equal composites. For example, a square commutes when $G(f)\circ\eta_x=\eta_y\circ F(f)$.
:::

::: {.front card-id="card-daa562cc213b94f1" tags="definition"}
Compatible family
:::

::: {.back card-id="card-daa562cc213b94f1"}
Given an inverse system $(S_i,f_{ij})_{i\ge j}$, a compatible family is a family $(x_i)_{i\in I}$ with $x_i\in S_i$ and $f_{ij}(x_i)=x_j$ for all $i\ge j$. The projective limit $\varprojlim S_i$ is the set of compatible families.
:::

::: {.front card-id="card-9a9c026fdf5d91f0" tags="definition"}
Cone
:::

::: {.back card-id="card-9a9c026fdf5d91f0"}
A cone over a diagram $F:I\to\mathcal{C}$ is an object $L$ together with morphisms $\lambda_i:L\to F(i)$ for all $i\in I$ such that $F(u)\circ\lambda_i=\lambda_j$ for every morphism $u:i\to j$ in $I$. The maps $\lambda_i$ are the legs of the cone.
:::

::: {.front card-id="card-55efc5861576a2e0" tags="definition"}
Coproduct
:::

::: {.back card-id="card-55efc5861576a2e0"}
A coproduct of objects $\{X_i\}_{i\in I}$ is an object $\coprod_{i\in I}X_i$ with injections $\iota_i:X_i\to\coprod_{i\in I}X_i$ such that for every object $A$ and morphisms $f_i:X_i\to A$ there is a unique $f:\coprod_{i\in I}X_i\to A$ with $f\circ\iota_i=f_i$. It is the dual of the product; in $\mathbf{Set}$ it is the disjoint union.
:::

::: {.front card-id="card-1a6fb58590700430" tags="definition"}
Diagram
:::

::: {.back card-id="card-1a6fb58590700430"}
A diagram in a category $\mathcal{C}$ is a functor $F:I\to\mathcal{C}$ from a small index category $I$ (often a poset, a graph, or a finite shape) to $\mathcal{C}$; it selects objects $F(i)$ and morphisms $F(i\to j)$.
:::

::: {.front card-id="card-5ed4b24560148b76" tags="definition"}
Functor
:::

::: {.back card-id="card-5ed4b24560148b76"}
A functor $F:\mathcal{C}\to\mathcal{D}$ assigns to each object $X$ of $\mathcal{C}$ an object $F(X)$ of $\mathcal{D}$, and to each morphism $f:X\to Y$ a morphism $F(f):F(X)\to F(Y)$, such that $F(1_X)=1_{F(X)}$ and $F(g\circ f)=F(g)\circ F(f)$. A contravariant functor reverses the direction of morphisms.
:::

::: {.front card-id="card-8c793764756f2e0d" tags="definition"}
Hom-set
:::

::: {.back card-id="card-8c793764756f2e0d"}
For objects $X,Y$ of a category $\mathcal{C}$, the hom-set is $\operatorname{Hom}_{\mathcal{C}}(X,Y)=\mathcal{C}(X,Y)$, the set of all morphisms $X\to Y$. A category is locally small when every hom-collection is a set.
:::

::: {.front card-id="card-d17ebd79aa765e53" tags="definition"}
Homomorphism
:::

::: {.back card-id="card-d17ebd79aa765e53"}
A group homomorphism is a map $\varphi:G\to H$ between groups such that $\varphi(xy)=\varphi(x)\varphi(y)$ for all $x,y\in G$; then $\varphi(e)=e$ and $\varphi(x^{-1})=\varphi(x)^{-1}$. For abelian groups written additively, the condition is $\varphi(x+y)=\varphi(x)+\varphi(y)$.
:::

::: {.front card-id="card-df511473d35130fc" tags="definition"}
Initial object
:::

::: {.back card-id="card-df511473d35130fc"}
An initial object of a category is an object $I$ such that for every object $X$ there is exactly one morphism $I \to X$.
:::

::: {.front card-id="card-9d68f09f357cdb2a" tags="definition"}
Inverse system
:::

::: {.back card-id="card-9d68f09f357cdb2a"}
An inverse system (projective system) in a category $\mathcal{C}$ consists of a partially ordered index set $I$ (usually directed), objects $S_i$ for $i\in I$, and morphisms $f_{ij}:S_i\to S_j$ for $i\ge j$ such that $f_{ii}=1_{S_i}$ and $f_{jk}\circ f_{ij}=f_{ik}$ whenever $i\ge j\ge k$. Its limit is the projective limit $\varprojlim S_i$.
:::

::: {.front card-id="card-452a8b8ab43c3a42" tags="definition"}
Locally small category
:::

::: {.back card-id="card-452a8b8ab43c3a42"}
A category $\mathcal{C}$ is locally small if for every pair of objects $X,Y$, the morphisms $X\to Y$ form a set (rather than a proper class).
:::

::: {.front card-id="card-a3c78f865c43299c" tags="definition"}
Morphism
:::

::: {.back card-id="card-a3c78f865c43299c"}
A morphism (arrow) $f:X\to Y$ in a category $\mathcal{C}$ is an element of the hom-set $\mathcal{C}(X,Y)$. $X$ is its domain (source) and $Y$ its codomain (target); morphisms compose associatively and have identities.
:::

::: {.front card-id="card-12805de172fcbf35" tags="definition"}
Natural isomorphism
:::

::: {.back card-id="card-12805de172fcbf35"}
A natural transformation $\eta:F\Rightarrow G$ is a natural isomorphism if every component $\eta_X:F(X)\to G(X)$ is an isomorphism. Equivalently, there is a natural transformation $\eta^{-1}:G\Rightarrow F$ with $\eta^{-1}\circ\eta=1_F$ and $\eta\circ\eta^{-1}=1_G$; one writes $F\cong G$.
:::

::: {.front card-id="card-a70cf264e4dc4c27" tags="definition"}
Object
:::

::: {.back card-id="card-a70cf264e4dc4c27"}
An object of a category $\mathcal{C}$ is one of the entities $X,Y,\dots$ among which morphisms are defined. Its only data are the hom-sets $\mathcal{C}(X,Y)$ and the composition and identity morphisms involving it.
:::

::: {.front card-id="card-59ce6ef14b0fad41" tags="definition"}
Parallel morphisms
:::

::: {.back card-id="card-59ce6ef14b0fad41"}
Two morphisms $f,g:X\to Y$ in a category are parallel if they have the same domain $X$ and the same codomain $Y$; the pair $(f,g)$ is a parallel pair.
:::

::: {.front card-id="card-e3aab7371e1a02b1" tags="definition"}
Preadditive category
:::

::: {.back card-id="card-e3aab7371e1a02b1"}
A preadditive category is a category in which every hom-set $\mathcal{C}(X,Y)$ is an abelian group and composition is bilinear: $(g+g')\circ f=g\circ f+g'\circ f$ and $g\circ(f+f')=g\circ f+g\circ f'$. Equivalently, it is a category enriched over abelian groups.
:::

::: {.front card-id="card-9b06b57ebd9b85d6" tags="definition"}
Product
:::

::: {.back card-id="card-9b06b57ebd9b85d6"}
A product of objects $\{X_i\}_{i\in I}$ in a category is an object $\prod_{i\in I}X_i$ with projections $\pi_i:\prod_{i\in I}X_i\to X_i$ such that for every object $A$ and morphisms $f_i:A\to X_i$ there is a unique $f:A\to\prod_{i\in I}X_i$ with $\pi_i\circ f=f_i$. Equivalently, $\operatorname{Hom}(A,\prod_i X_i)\cong\prod_i\operatorname{Hom}(A,X_i)$ naturally in $A$.
:::

::: {.front card-id="card-12d35eb6988ddb4f" tags="definition"}
Pullback
:::

::: {.back card-id="card-12d35eb6988ddb4f"}
A pullback (fiber product) of $f:X\to Z$ and $g:Y\to Z$ is an object $X\times_Z Y$ with morphisms $p:X\times_Z Y\to X$ and $q:X\times_Z Y\to Y$ such that $f\circ p=g\circ q$, universal among such squares: every $h:W\to X$ and $k:W\to Y$ with $f\circ h=g\circ k$ factors uniquely through $(p,q)$. In $\mathbf{Set}$, $X\times_Z Y=\{(x,y)\in X\times Y:f(x)=g(y)\}$.
:::

::: {.front card-id="card-1886ee9af32f10b9" tags="definition"}
Pushout
:::

::: {.back card-id="card-1886ee9af32f10b9"}
Given morphisms $f : Z \to X$ and $g : Z \to Y$, the pushout is an object $P$ with morphisms $i : X \to P$ and $j : Y \to P$ satisfying $i \circ f = j \circ g$, universal with this property. In $\mathbf{Set}$, $P = (X \sqcup Y)/\sim$ with $f(z) \sim g(z)$.
:::

::: {.front card-id="card-7dbbd4d254d4e3c7" tags="definition"}
Representable functor
:::

::: {.back card-id="card-7dbbd4d254d4e3c7"}
A functor $F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$ is representable if there is an object $X$ of $\mathcal{C}$ and a natural isomorphism $F\cong\operatorname{Hom}_{\mathcal{C}}(-,X)$; $X$ is the representing object. A covariant functor $F:\mathcal{C}\to\mathbf{Set}$ is representable if $F\cong\operatorname{Hom}_{\mathcal{C}}(X,-)$.
:::

::: {.front card-id="card-6039a6c78a2df71a" tags="definition"}
Summand
:::

::: {.back card-id="card-6039a6c78a2df71a"}
A summand of an object $X$ is an object $Y$ for which there is an object $Z$ with $X\cong Y\coprod Z$ (or $X\cong Y\oplus Z$ when a biproduct exists). In a coproduct $\coprod_i B_i$, each $B_i$ is a summand.
:::

::: {.front card-id="card-e38854feec65c1c7" tags="definition"}
Terminal object
:::

::: {.back card-id="card-e38854feec65c1c7"}
A terminal object of a category is an object $T$ such that for every object $X$ there is exactly one morphism $X \to T$.
:::

::: {.front card-id="card-81678eb151beb4dd" tags="definition"}
Universal property
:::

::: {.back card-id="card-81678eb151beb4dd"}
A universal property characterizes an object $U$, together with specified structure maps, by a unique factorisation condition: for every object $X$ with the same kind of structure there is a unique morphism $X\to U$ (or $U\to X$) making the relevant diagram commute. Limits, colimits, products, and adjunctions are defined by universal properties.
:::

::: {.front card-id="card-7fb7720a0562f2b2" tags="definition"}
Yoneda lemma
:::

::: {.back card-id="card-7fb7720a0562f2b2"}
For a functor $F : \mathcal{C} \to \mathbf{Set}$, there is a natural bijection $\mathrm{Nat}(\mathrm{Hom}_{\mathcal{C}}(A,-), F) \cong F(A)$, natural in $A$ and in $F$.
:::
