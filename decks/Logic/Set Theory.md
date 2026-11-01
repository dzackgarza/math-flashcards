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

::: {.front card-id="card-fd475ee92dbc9e3c" tags="definition"}
Bijective
:::

::: {.back card-id="card-fd475ee92dbc9e3c"}
A function $f:X\to Y$ is bijective if it is both injective and surjective: for every $y\in Y$ there is exactly one $x\in X$ with $f(x)=y$. Equivalently, $f$ has a two-sided inverse.
:::

::: {.front card-id="card-b9fc088ef91deb67" tags="definition"}
Cardinality
:::

::: {.back card-id="card-b9fc088ef91deb67"}
The cardinality $|A|$ of a set $A$ is its size: $|A|=|B|$ iff there is a bijection $A\to B$. For finite sets it is the number of elements; for infinite sets it is a cardinal such as $\aleph_0$.
:::

::: {.front card-id="card-44f2714441531e52" tags="definition"}
Cartesian product
:::

::: {.back card-id="card-44f2714441531e52"}
The Cartesian product $A \times B$ is the set of ordered pairs $A \times B = \{(a,b) : a \in A,\ b \in B\}$.
:::

::: {.front card-id="card-23566624becbff1d" tags="definition"}
Chain
:::

::: {.back card-id="card-23566624becbff1d"}
A chain in a poset $P$ is a subset $C\subseteq P$ that is totally ordered by the induced order: for all $x,y\in C$, $x\le y$ or $y\le x$.
:::

::: {.front card-id="card-c35d8e9a34d445ea" tags="definition"}
Complement
:::

::: {.back card-id="card-c35d8e9a34d445ea"}
For $A\subseteq X$, the complement of $A$ in $X$ is $X\setminus A=\{x\in X:x\notin A\}$, often written $A^{c}$. More generally, the complement of $B$ in $A$ is $A\setminus B$.
:::

::: {.front card-id="card-e46c7da0b4229208" tags="definition"}
Countable
:::

::: {.back card-id="card-e46c7da0b4229208"}
A set $A$ is countable if there is an injection $A \hookrightarrow \mathbb{N}$; equivalently, $A$ is finite or in bijection with $\mathbb{N}$.
:::

::: {.front card-id="card-d9f71ee53d0d2061" tags="definition"}
Countable set
:::

::: {.back card-id="card-d9f71ee53d0d2061"}
A set $A$ is countable if it is finite or there is a bijection $A\to\mathbb{N}$. Equivalently, its elements can be listed as a sequence (possibly finite). A countably infinite set has cardinality $\aleph_0$.
:::

::: {.front card-id="card-80951cdbb461fde9" tags="definition"}
Disjoint sets
:::

::: {.back card-id="card-80951cdbb461fde9"}
Sets $A$ and $B$ are disjoint if $A\cap B=\varnothing$. A family $\{A_i\}_{i\in I}$ is pairwise disjoint if $A_i\cap A_j=\varnothing$ for all $i\neq j$.
:::

::: {.front card-id="card-94b5194d8015f8cf" tags="definition"}
Disjoint union
:::

::: {.back card-id="card-94b5194d8015f8cf"}
The disjoint union of a family $\{A_i\}_{i\in I}$ is $\coprod_{i\in I}A_i=\{(i,a):i\in I,\ a\in A_i\}$. It contains a copy of each $A_i$, and these copies are pairwise disjoint; it is the coproduct in $\mathbf{Set}$.
:::

::: {.front card-id="card-ba8a30c6642b6f38" tags="definition"}
Equivalence relation
:::

::: {.back card-id="card-ba8a30c6642b6f38"}
A relation $\sim$ on a set $A$ is an equivalence relation if it is reflexive ($a \sim a$), symmetric ($a \sim b \Rightarrow b \sim a$), and transitive ($a \sim b$ and $b \sim c$ imply $a \sim c$).
:::

::: {.front card-id="card-4bd35916e11750a6" tags="definition"}
Function
:::

::: {.back card-id="card-4bd35916e11750a6"}
A function $f:X\to Y$ assigns to each $x\in X$ a unique element $f(x)\in Y$. The set $X$ is the domain and $Y$ the codomain; two functions are equal iff they have the same domain, codomain, and values.
:::

::: {.front card-id="card-4047761b683cef32" tags="definition"}
Indexed family
:::

::: {.back card-id="card-4047761b683cef32"}
An indexed family $\{A_i\}_{i\in I}$ is a function $i\mapsto A_i$ from an index set $I$ to a collection of sets (or other objects). A sequence is the case $I=\mathbb{N}$.
:::

::: {.front card-id="card-b53b3c7595396074" tags="definition"}
Intersection
:::

::: {.back card-id="card-b53b3c7595396074"}
The intersection of a family $\{A_i\}_{i\in I}$ is $\bigcap_{i\in I}A_i=\{x:\forall i\in I,\ x\in A_i\}$. For two sets, $A\cap B=\{x:x\in A\text{ and }x\in B\}$.
:::

::: {.front card-id="card-fa2cab9329f11859" tags="definition"}
Inverse function
:::

::: {.back card-id="card-fa2cab9329f11859"}
If $f:X\to Y$ is bijective, its inverse $f^{-1}:Y\to X$ is the unique function with $f^{-1}(f(x))=x$ for all $x\in X$ and $f(f^{-1}(y))=y$ for all $y\in Y$; equivalently $f^{-1}\circ f=\mathrm{id}_X$ and $f\circ f^{-1}=\mathrm{id}_Y$.
:::

::: {.front card-id="card-77ee8321ad40e058" tags="definition"}
Maximal element
:::

::: {.back card-id="card-77ee8321ad40e058"}
An element $m\in P$ is maximal if there is no $x\in P$ with $m<x$; equivalently, $m\le x$ implies $x=m$. A greatest element (maximum) is an upper bound of all of $P$; it is maximal, but a maximal element need not be greatest.
:::

::: {.front card-id="card-f4b465c564475ad6" tags="definition"}
Ordered pair
:::

::: {.back card-id="card-f4b465c564475ad6"}
An ordered pair $(a,b)$ is a set with the property $(a,b)=(c,d)$ if and only if $a=c$ and $b=d$; the Kuratowski model is $(a,b)=\{\{a\},\{a,b\}\}$.
:::

::: {.front card-id="card-77bebd51ba2ee791" tags="definition"}
Poset
:::

::: {.back card-id="card-77bebd51ba2ee791"}
A partially ordered set (poset) is a pair $(P,\le)$ where $\le$ is reflexive ($x\le x$), transitive ($x\le y$ and $y\le z$ imply $x\le z$), and antisymmetric ($x\le y$ and $y\le x$ imply $x=y$).
:::

::: {.front card-id="card-c6051ab15af14b0b" tags="definition"}
Power set
:::

::: {.back card-id="card-c6051ab15af14b0b"}
The power set $\mathcal{P}(A)$ of $A$ is the set of all subsets of $A$: $\mathcal{P}(A) = \{B : B \subseteq A\}$.
:::

::: {.front card-id="card-9bca59f793558272" tags="definition"}
Preimage
:::

::: {.back card-id="card-9bca59f793558272"}
For $f:X\to Y$ and $B\subseteq Y$, the preimage (or inverse image) of $B$ is $f^{-1}(B)=\{x\in X:f(x)\in B\}\subseteq X$. It is defined for every function $f$, whether or not $f$ is invertible.
:::

::: {.front card-id="card-541fd61b8f78963f" tags="definition"}
Relation
:::

::: {.back card-id="card-541fd61b8f78963f"}
A (binary) relation from $A$ to $B$ is a subset $R \subseteq A \times B$; we write $a \mathrel{R} b$ if and only if $(a,b) \in R$.
:::

::: {.front card-id="card-5b9d076709fa737f" tags="definition"}
Right inverse
:::

::: {.back card-id="card-5b9d076709fa737f"}
A right inverse of $f:X\to Y$ is a function $g:Y\to X$ with $f\circ g=\mathrm{id}_Y$, i.e. $f(g(y))=y$ for all $y\in Y$. A function has a right inverse iff it is surjective (the converse uses the axiom of choice).
:::

::: {.front card-id="card-d38f961a10aa08a1" tags="definition"}
Set
:::

::: {.back card-id="card-d38f961a10aa08a1"}
A set is a collection of objects, called its elements. A set is determined by its elements (extensionality): $x\in A$ means that $x$ is an element of $A$, and $A=B$ iff every element of $A$ is an element of $B$ and conversely.
:::

::: {.front card-id="card-47e9186b0c6eb7b5" tags="definition"}
Set difference
:::

::: {.back card-id="card-47e9186b0c6eb7b5"}
The set difference of $A$ and $B$ is $A\setminus B=\{x\in A:x\notin B\}$. When $B\subseteq A$, this is also called the complement of $B$ in $A$.
:::

::: {.front card-id="card-7614eef730ffa76f" tags="definition"}
Subset
:::

::: {.back card-id="card-7614eef730ffa76f"}
$A$ is a subset of $B$, written $A\subseteq B$, if every element of $A$ is an element of $B$. It is a proper subset, written $A\subsetneq B$, if $A\subseteq B$ and $A\neq B$.
:::

::: {.front card-id="card-fb924f154ffa2466" tags="definition"}
Total order
:::

::: {.back card-id="card-fb924f154ffa2466"}
A total order (linear order) on $P$ is a partial order such that for all $x,y\in P$, $x\le y$ or $y\le x$. A set equipped with a total order is totally ordered.
:::

::: {.front card-id="card-6c951c9e85ad5b76" tags="definition"}
Uncountable
:::

::: {.back card-id="card-6c951c9e85ad5b76"}
A set is uncountable if it is not countable, that is, it admits no injection into $\mathbb{N}$.
:::

::: {.front card-id="card-0e8d87064c84183c" tags="definition"}
Union
:::

::: {.back card-id="card-0e8d87064c84183c"}
The union of a family $\{A_i\}_{i\in I}$ is $\bigcup_{i\in I}A_i=\{x:\exists i\in I,\ x\in A_i\}$. For two sets, $A\cup B=\{x:x\in A\text{ or }x\in B\}$.
:::

::: {.front card-id="card-9873a6d0534b8d25" tags="definition"}
Upper bound
:::

::: {.back card-id="card-9873a6d0534b8d25"}
An upper bound of $S\subseteq P$ in a poset $P$ is an element $u\in P$ with $s\le u$ for all $s\in S$. A least upper bound (supremum) is an upper bound $u$ with $u\le v$ for every upper bound $v$ of $S$.
:::
