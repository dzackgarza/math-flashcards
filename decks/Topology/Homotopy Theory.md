---
title: "Topology::Homotopy Theory"
---

::: {.front card-id="card-55490a6643fe8c7c"}
What is Quillen's construction of ${\mathsf{K}}(A)$?
:::

::: {.back card-id="card-55490a6643fe8c7c"}
$\pi_*  \mathbf{B}\mkern-3mu \operatorname{GL}_\infty(R)^+$
:::

::: {.front card-id="card-8e2d612bd67c49ea"}
What is ${\mathsf{K}}_0(F)$ for $F$ a field?
:::

::: {.back card-id="card-8e2d612bd67c49ea"}
${\mathsf{K}}_0(F) =   {}_{F}{\mathsf{Mod}}^{{\mathrm{fg}}, \mathop{\mathrm{proj}}, \cong,  {\operatorname{gp} }} = {\mathbf{Z}}_{\geq 0}^ {\operatorname{gp} }= {\mathbf{Z}}$.
:::

::: {.front card-id="card-1125f1062dd6328b"}
Describe ${\mathsf{K}}_1(A)$ for $A\in \mathsf{Ring}$.
:::

::: {.back card-id="card-1125f1062dd6328b"}
${\mathsf{K}}_1(A) = \operatorname{GL}(A)^{\operatorname{ab}}= \operatorname{GL}(A)/E(A)$.
:::

::: {.front card-id="card-2d447491800553bd"}
What is the $s{\hbox{-}}$cobordism theorem?
:::

::: {.back card-id="card-2d447491800553bd"}
If $W$ is an $h{\hbox{-}}$cobordism from $X$ to $Y$, when is $W$ a trivial cylinder?

Obstruction in a quotient of ${\mathsf{K}}_1({\mathbf{Z}}[\pi_1 X])$.
:::

::: {.front card-id="card-b9908aac8fcaa3a4"}
What is ${\mathsf{K}}({ \mathbf{F} }_q)$?
:::

::: {.back card-id="card-b9908aac8fcaa3a4"}
$${\mathsf{K}}({ \mathbf{F} }_q) = {\mathbf{Z}}+ \bigoplus_{i \geq 1} C_{q^i-1}\cdot t^{2i-1}$$
:::

::: {.front card-id="card-2d66ec475c0602b2"}
Describe the state of computations for ${\mathsf{K}}(R)$.
:::

::: {.back card-id="card-2d66ec475c0602b2"}
$R = { \mathbf{F} }_q$ a finite field: known completely.

$R = F$ a field: known for $n=0, 1$.

$R = C_{p^k}$ for $k \geq 2$ currently unknown.

$R = {\mathbf{Z}}$ not completely known.

$R = ({\mathbf{Z}}[x]/\left\langle{x^n}\right\rangle, \left\langle{x}\right\rangle)$ partially known using trace methods: ${\mathbf{Z}}^{m-1}$ in odd degrees, order $\approx (mi)!(i!)^{m-2}$ in even degrees $2i$.

$R = {\mathbf{Z}}[x,y]/\left\langle{xy}\right\rangle, F[x,y]/\left\langle{xy}\right\rangle$ for $F$ characteristic $p$ well-understood.
:::

::: {.front card-id="card-67ea6844f9dac0cd"}
Give example applications of computing ${\mathsf{K}}(R)$.
:::

::: {.back card-id="card-67ea6844f9dac0cd"}
Vandiver's conjecture: for $p$ prime and $K \leq {\mathbf{Q}}(\zeta_p)$ the maximal real subfield, $p\nmid { \operatorname{cl}}(K)$. Equivalent to ${\mathsf{K}}_{4n}({\mathbf{Z}}) = 0$ for all $n\in {\mathbf{Z}}_{\gt 0}$.
:::

::: {.front card-id="card-142fbf4967edbb0c"}
What is the Atiyah-Hirzebruch spectral sequence?
:::

::: {.back card-id="card-142fbf4967edbb0c"}
$H^*_{\mathrm{sing}}\Rightarrow{\mathsf{K}}^{\mathsf{Top}}$.
:::

::: {.front card-id="card-e361804891a52adf"}
What is the cyclic bar construction?
:::

::: {.back card-id="card-e361804891a52adf"}
$B_n^{\mathrm{cyc}}(A) \coloneqq A{ {}^{ \scriptstyle\otimes_{}^{n+1} }  }$ with

Differentials: collapsing ${\partial}_i(\mathbf{a}) = a_0\otimes\cdots \otimes a_i a_{i+1}\otimes\cdots\otimes a_n$ for $0\leq i\leq n-1$ and cycling ${\partial}_i(\mathbf{a}) = a_n a_0\otimes\cdots \otimes a_{n-1}$ for $i=n$.

Form the full differential as ${\partial}= \sum_i (-1)^i {\partial}_i$.

Degeneracy maps $s_i$ insert the unit into the $i$th coordinate.

$n$th level carries an action of $C_{n+1}$ where the generator acts by $\mathbf{a} \mapsto a_n \otimes a_0 \otimes\cdots \otimes a_{n-1}$.
:::

::: {.front card-id="card-534078a51e642917"}
Define ${\operatorname{HH}}_n(A)$.
:::

::: {.back card-id="card-534078a51e642917"}
The homology of the cyclic bar complex, $H_n(C_\bullet(A))$, or by Dold-Kan, $\pi_n { {\left\lvert {B_\bullet^{\mathrm{cyc}}(A)} \right\rvert} }$, the geometric realization of a simplicial object.
:::

::: {.front card-id="card-7eeb7c9a13adaa9c"}
Why are cyclic objects $X$ important?
:::

::: {.back card-id="card-7eeb7c9a13adaa9c"}
$S^1\curvearrowright{ {\left\lvert {X} \right\rvert} }$.
:::

::: {.front card-id="card-018fb09fa8f77dfa"}
What is the Dennis trace?
:::

::: {.back card-id="card-018fb09fa8f77dfa"}
${\mathsf{K}}_q(A) \to {\operatorname{HH}}_q(A)$.
:::

::: {.front card-id="card-f326fea48c45a233"}
Why is Hochschild homology an approximation of K-theory?
:::

::: {.back card-id="card-f326fea48c45a233"}
The Dennis trace factors as ${\mathsf{K}}_q(A) \to HC^-_q(A)\to {\operatorname{HH}}_q(A)$.

For $I{~\trianglelefteq~}A$ nilpotent, ${\mathsf{K}}_q(A, I) \otimes{\mathbf{Q}} { \, \xrightarrow{\sim}\, }HC^i_q(A\otimes{\mathbf{Q}}, I\otimes{\mathbf{Q}})$.
:::

::: {.front card-id="card-b4259e9bf938b1eb"}
What does ${\operatorname{THH}}(A)$ mean?
:::

::: {.back card-id="card-b4259e9bf938b1eb"}
${\operatorname{THH}}(HA)$ for $HA$ the Eilenberg-MacLane spectrum.

Idea of construction: replace ${\mathbf{Z}}$ with ${\mathbf{S}}$ and $\otimes_{\mathbf{Z}}$ with $\wedge$ to form acyclic bar complex.
:::

::: {.front card-id="card-f9d6a7ea61c43f9f"}
What is the cyclotomic trace?
:::

::: {.back card-id="card-f9d6a7ea61c43f9f"}
${\mathsf{K}}(A) \to {\operatorname{TC}}(A)$ where ${\operatorname{TC}}(A; p) = \mathrm{ho}\cocolim_{R, F} {\operatorname{THH}}(A)^{C_{p^n}}$ as the homotopy limit of a tower:
:::

::: {.front card-id="card-d23a52bc13865247"}
Why is ${\operatorname{TC}}(A)$ a good approximation of ${\mathsf{K}}(A)$?
:::

::: {.back card-id="card-d23a52bc13865247"}
For $I{~\trianglelefteq~}A$ nilpotent, ${\mathsf{K}}_q(A; I)  { \, \xrightarrow{\sim}\, }{\operatorname{TC}}_q(A; I)$.
:::

::: {.front card-id="card-ae09d315ac9447c7"}
How is ${\operatorname{THH}}(A)$ defined?
:::

::: {.back card-id="card-ae09d315ac9447c7"}
${\operatorname{THH}}(A) \coloneqq A \wedge_{A^e} A$ where $A^e \coloneqq A\wedge A$, defined for $A\in { {}_{{\mathbb{E}}_1}  \mathsf{Alg}}$.
:::

::: {.front card-id="card-b333191a2c80a9ab"}
What is an orthogonal space?
:::

::: {.back card-id="card-b333191a2c80a9ab"}
$X\in {\mathsf{Fun}}(L, \CGWH)^\text{cts}$ where $L$ is the (topological) linear isometry category (objects = inner product spaces, homs are $\mathop{\mathrm{Isom}}(V, W)$ with the Stiefel manifold topology)
:::

::: {.front card-id="card-ca2c8b3bdfb28736"}
What is the Thom space of a bundle?
:::

::: {.back card-id="card-ca2c8b3bdfb28736"}
Total space of disc bundle mod total space of sphere bundle.
:::

::: {.front card-id="card-a5d6de11110a89f8"}
What is the orthogonal complement bundle?
:::

::: {.back card-id="card-a5d6de11110a89f8"}
$\xi(V, W) \subset W\times L(V\to W)$ given by $\left\{{(v, \psi) {~\mathrel{\Big\vert}~}v\perp \psi(V)}\right\}$.
:::

::: {.front card-id="card-1cd0d32eba84d3c1"}
What is $O(V, W)$?
:::

::: {.back card-id="card-1cd0d32eba84d3c1"}
The one-point compactification of $\xi(V, W)$ the orthogonal complement bundle; equivalently its Thom space.
:::

::: {.front card-id="card-9185ede38bf3fdee"}
What is the category $O$?
:::

::: {.back card-id="card-9185ede38bf3fdee"}
Inner product spaces, homs are $O(V, W)$, composition is the smash product $(w, \phi) \wedge(v, \psi) \mapsto (w + \phi(v), \phi\circ \psi)$.
:::

::: {.front card-id="card-e1ec65255712c855"}
What is an orthogonal spectrum? A $G{\hbox{-}}$spectrum?
:::

::: {.back card-id="card-e1ec65255712c855"}
A based $X\in {\mathsf{Fun}}^\text{cts}(O, {\mathsf{Top}}_*)$ into based spaces.

For $G{\hbox{-}}$spectra: $X\in {\mathsf{Fun}}^\text{cts}(O, G{\hbox{-}}{\mathsf{Top}}_*)$ into based $G{\hbox{-}}$spaces.
:::

::: {.front card-id="card-f6b5c945918010b8"}
What is $S^V$ for $V$ a vector space?
:::

::: {.back card-id="card-f6b5c945918010b8"}
$V\cup\left\{{\infty}\right\}$ the one-point compactification.
:::

::: {.front card-id="card-a7a19be06f2d9bd6"}
Discuss the actions and structure maps on ${\mathsf{Sp}}$.
:::

::: {.back card-id="card-a7a19be06f2d9bd6"}
$O(V, V) = {\operatorname{O}}(V)_+$ is an orthogonal group and one gets ${\operatorname{O}}(V)_+\wedge X(V)\to X(V)$

$i_V: S^V \to O(V, V\oplus W)$ induces $\sigma_{V, W}: S^V\wedge X(W) \to X(V\oplus W)$.
:::

::: {.front card-id="card-33c72c8164c3b52f"}
How are $G{\hbox{-}}$equivariant homotopy groups defined?
:::

::: {.back card-id="card-33c72c8164c3b52f"}
$\pi_0^G(X) \coloneqq\colim_{V\in s(U_G)}[S^V\to X(V)]^G_*$ which are $G{\hbox{-}}$equivariant homotopy classes of based maps, and $U_G$ a complete universe of $G{\hbox{-}}$subrepresentations of $U_G$.

$\pi_k^G(X) = \colim_{\cdots}[S^{V\oplus {\mathbf{R}}^k}\to X(V)]^G_*$ for $k > 0$ and $\pi_k^G(X) = \colim_{\cdots}[S^{V}\to X(V\oplus {\mathbf{R}}^{-k})]^G_*$ for $k < 0$.
:::
