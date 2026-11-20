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
${\mathsf{K}}_0(F) =   {}_{F}\Mod^{\fg, \mathop{\mathrm{proj}}, \cong,  {\operatorname{gp} }} = \ZZ_{\geq 0}^ {\operatorname{gp} }= \ZZ$.
:::

::: {.front card-id="card-1125f1062dd6328b"}
Describe ${\mathsf{K}}_1(A)$ for $A\in \mathsf{Ring}$.
:::

::: {.back card-id="card-1125f1062dd6328b"}
${\mathsf{K}}_1(A) = \operatorname{GL}(A)^\ab= \operatorname{GL}(A)/E(A)$.
:::

::: {.front card-id="card-2d447491800553bd"}
What is the $s\dash$cobordism theorem?
:::

::: {.back card-id="card-2d447491800553bd"}
If $W$ is an $h\dash$cobordism from $X$ to $Y$, when is $W$ a trivial cylinder?

Obstruction in a quotient of ${\mathsf{K}}_1(\ZZ[\pi_1 X])$.
:::

::: {.front card-id="card-b9908aac8fcaa3a4"}
What is ${\mathsf{K}}({ \mathbf{F} }_q)$?
:::

::: {.back card-id="card-b9908aac8fcaa3a4"}
$${\mathsf{K}}({ \mathbf{F} }_q) = \ZZ+ \bigoplus_{i \geq 1} C_{q^i-1}\cdot t^{2i-1}$$
:::

::: {.front card-id="card-2d66ec475c0602b2"}
Describe the state of computations for ${\mathsf{K}}(R)$.
:::

::: {.back card-id="card-2d66ec475c0602b2"}
$R = { \mathbf{F} }_q$ a finite field: known completely.

$R = F$ a field: known for $n=0, 1$.

$R = C_{p^k}$ for $k \geq 2$ currently unknown.

$R = \ZZ$ not completely known.

$R = (\ZZ[x]/\left\langle{x^n}\right\rangle, \left\langle{x}\right\rangle)$ partially known using trace methods: $\ZZ^{m-1}$ in odd degrees, order $\approx (mi)!(i!)^{m-2}$ in even degrees $2i$.

$R = \ZZ[x,y]/\left\langle{xy}\right\rangle, F[x,y]/\left\langle{xy}\right\rangle$ for $F$ characteristic $p$ well-understood.
:::

::: {.front card-id="card-67ea6844f9dac0cd"}
Give example applications of computing ${\mathsf{K}}(R)$.
:::

::: {.back card-id="card-67ea6844f9dac0cd"}
Vandiver's conjecture: for $p$ prime and $K \leq \QQ(\zeta_p)$ the maximal real subfield, $p\nmid \cl(K)$. Equivalent to ${\mathsf{K}}_{4n}(\ZZ) = 0$ for all $n\in \ZZ_{\gt 0}$.
:::

::: {.front card-id="card-142fbf4967edbb0c"}
What is the Atiyah-Hirzebruch spectral sequence?
:::

::: {.back card-id="card-142fbf4967edbb0c"}
$H^*_\sing\Rightarrow{\mathsf{K}}^\Top$.
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

For $I\normal A$ nilpotent, ${\mathsf{K}}_q(A, I) \otimes\QQ { \, \xrightarrow{\sim}\, }HC^i_q(A\otimes\QQ, I\otimes\QQ)$.
:::

::: {.front card-id="card-b4259e9bf938b1eb"}
How is ${\operatorname{THH}}(A)$ defined?
:::

::: {.back card-id="card-b4259e9bf938b1eb"}
${\operatorname{THH}}(A) \coloneqq A \wedge_{A^e} A$ where $A^e \coloneqq A\wedge A^{\operatorname{op}}$, defined for $A\in { {}_{{\mathbb{E}}_1}  \mathsf{Alg}}$.

For a discrete ring $A$, ${\operatorname{THH}}(A)$ means ${\operatorname{THH}}(HA)$ for $HA$ the Eilenberg-MacLane spectrum.

Idea of construction: replace $\ZZ$ with ${\mathbf{S}}$ and $\otimes_\ZZ$ with $\wedge$ to form a cyclic bar complex.
:::

::: {.front card-id="card-f9d6a7ea61c43f9f"}
What is the cyclotomic trace?
:::

::: {.back card-id="card-f9d6a7ea61c43f9f"}
${\mathsf{K}}(A) \to \TC(A)$ where $\TC(A; p) = \mathrm{ho}\projectivelim_{R, F} {\operatorname{THH}}(A)^{C_{p^n}}$ as the homotopy limit of a tower:
:::

::: {.front card-id="card-d23a52bc13865247"}
Why is $\TC(A)$ a good approximation of ${\mathsf{K}}(A)$?
:::

::: {.back card-id="card-d23a52bc13865247"}
For $I\normal A$ nilpotent, ${\mathsf{K}}_q(A; I)  { \, \xrightarrow{\sim}\, }\TC_q(A; I)$.
:::

::: {.front card-id="card-b333191a2c80a9ab"}
What is an orthogonal space?
:::

::: {.back card-id="card-b333191a2c80a9ab"}
$X\in \Fun(L, {\mathsf{CGWH}})^\text{cts}$ where $L$ is the (topological) linear isometry category (objects = inner product spaces, homs are $\mathop\Isom(V, W)$ with the Stiefel manifold topology)
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
$\xi(V, W) \subset W\times L(V\to W)$ given by $\left\{{(v, \psi) \st v\perp \psi(V)}\right\}$.
:::

::: {.front card-id="card-1cd0d32eba84d3c1"}
For finite-dimensional real inner product spaces $V,W$, what is the morphism space $O(V,W)$ used to define orthogonal spectra?
:::

::: {.back card-id="card-1cd0d32eba84d3c1"}
The one-point compactification of $\xi(V, W)$ the orthogonal complement bundle; equivalently its Thom space.
:::

::: {.front card-id="card-9185ede38bf3fdee"}
Define the topologically enriched category $O$ used to define orthogonal spectra, including composition.
:::

::: {.back card-id="card-9185ede38bf3fdee"}
Inner product spaces, homs are $O(V, W)$, composition is the smash product $(w, \phi) \wedge(v, \psi) \mapsto (w + \phi(v), \phi\circ \psi)$.
:::

::: {.front card-id="card-e1ec65255712c855" cite="[@Sch18, §3.1]"}
What is an orthogonal spectrum? A $G\dash$spectrum?
:::

::: {.back card-id="card-e1ec65255712c855"}
A based $X\in \Fun^\text{cts}(O, \Top_*)$ into based spaces.

For $G\dash$spectra: $X\in \Fun^\text{cts}(O, G\dash\Top_*)$ into based $G\dash$spaces.

This model encodes suspension by representation spheres and supports genuine equivariant stable homotopy theory when stable equivalences are tested on equivariant homotopy groups in a complete universe.
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
How are $G\dash$equivariant homotopy groups defined?
:::

::: {.back card-id="card-33c72c8164c3b52f"}
$\pi_0^G(X) \coloneqq\colim_{V\in s(U_G)}[S^V\to X(V)]^G_*$ which are $G\dash$equivariant homotopy classes of based maps, and $U_G$ a complete universe of $G\dash$subrepresentations of $U_G$.

$\pi_k^G(X) = \colim_{\cdots}[S^{V\oplus {\mathbf{R}}^k}\to X(V)]^G_*$ for $k > 0$ and $\pi_k^G(X) = \colim_{\cdots}[S^{V}\to X(V\oplus {\mathbf{R}}^{-k})]^G_*$ for $k < 0$.
:::

::: {.front card-id="card-e5ac5f064a016385" tags="definition"}
What is the definition of Circle action?
:::

::: {.back card-id="card-e5ac5f064a016385"}
A circle action on a space $X$ is a continuous map $S^1\times X\to X$, $(z,x)\mapsto z\cdot x$, with $1\cdot x=x$ and $(zz')\cdot x=z\cdot(z'\cdot x)$; equivalently, a continuous homomorphism $S^1\to\operatorname{Homeo}(X)$.
:::

::: {.front card-id="card-08f2e6f801fc661c" tags="definition"}
What is the definition of Cobordism?
:::

::: {.back card-id="card-08f2e6f801fc661c"}
A cobordism from a closed manifold $X$ to a closed manifold $Y$ is a compact manifold $W$ with boundary $\partial W=X\sqcup Y$. It is trivial if $W\cong X\times[0,1]$ with $X=X\times\{0\}$ and $Y=X\times\{1\}$.
:::

::: {.front card-id="card-97d690c5b8f51720" tags="definition"}
What is the definition of Compactly generated weak hausdorff space?
:::

::: {.back card-id="card-97d690c5b8f51720"}
A compactly generated weak Hausdorff (CGWH) space is a weak Hausdorff space whose topology is determined by its compact subsets (a $k$-space). CGWH spaces form a convenient cartesian closed category of spaces, closed under limits, colimits, and function spaces.
:::

::: {.front card-id="card-802eac03481a4ac5" tags="definition"}
What is the definition of Complete universe?
:::

::: {.back card-id="card-802eac03481a4ac5"}
A complete universe $U_G$ for a compact Lie group $G$ is an infinite-dimensional real inner product space with a continuous linear $G$-action in which every irreducible real representation of $G$ occurs with infinite multiplicity. The symbol $s(U_G)$ denotes the poset of finite-dimensional $G$-subrepresentations of $U_G$.
:::

::: {.front card-id="card-92edb0e74a3dc521" tags="definition"}
What is the definition of Cyclic homology?
:::

::: {.back card-id="card-92edb0e74a3dc521"}
Cyclic homology $HC_*(A)$ is the homology of the total complex of Connes' cyclic bicomplex, whose two differentials are the Hochschild differential $b$ and Connes' operator $B$. It is related to negative cyclic and Hochschild homology by Connes' $SBI$ exact sequence.
:::

::: {.front card-id="card-d06805fdb4f6e544" tags="definition"}
What is the definition of Cyclic object?
:::

::: {.back card-id="card-d06805fdb4f6e544"}
A cyclic object in a category $\mathcal{C}$ is a simplicial object $X$ equipped with cyclic operators $t_n:X_n\to X_n$ satisfying $t_n^{n+1}=\operatorname{id}$, $\partial_i t_n=t_{n-1}\partial_{i-1}$ and $s_i t_n=t_{n+1}s_{i-1}$ with indices modulo $n+1$; equivalently, a functor $\Lambda^{\mathrm{op}}\to\mathcal{C}$ on Connes' cyclic category.
:::

::: {.front card-id="card-80513598c5a9ae07" tags="definition"}
What is the definition of Cyclotomic field?
:::

::: {.back card-id="card-80513598c5a9ae07"}
The $n$-th cyclotomic field is $\mathbb{Q}(\zeta_n)$, where $\zeta_n$ is a primitive $n$-th root of unity; it is the splitting field of $x^n-1$ over $\mathbb{Q}$ and has degree $\varphi(n)$.
:::

::: {.front card-id="card-71d47bb2560459c9" tags="definition"}
What is the definition of Degeneracy map?
:::

::: {.back card-id="card-71d47bb2560459c9"}
The $i$-th degeneracy map of a simplicial object $X$ is $s_i:X_n\to X_{n+1}$ for $0\le i\le n$, induced by the surjection $[n+1]\to[n]$ that repeats $i$; it inserts a degenerate $(i+1)$-st vertex.
:::

::: {.front card-id="card-15c2398358609871" tags="definition"}
What is the definition of Differential?
:::

::: {.back card-id="card-15c2398358609871"}
In a chain complex $(C_*,d)$, the differential is the family of homomorphisms $d_n:C_n\to C_{n-1}$ satisfying $d_{n-1}\circ d_n=0$. For the cyclic bar construction, $d=\sum_{i=0}^{n}(-1)^i\partial_i$.
:::

::: {.front card-id="card-f092986af3750576" tags="definition"}
What is the definition of Disc bundle?
:::

::: {.back card-id="card-f092986af3750576"}
For a vector bundle $E\to B$ with a metric, the disc bundle is $D(E)=\{v\in E:\|v\|\le 1\}$, a fibre bundle with fibre the closed disc $D^n$; its boundary is the sphere bundle $S(E)$.
:::

::: {.front card-id="card-638eb552d1975c94" tags="definition"}
What is the definition of Eilenberg-maclane spectrum?
:::

::: {.back card-id="card-638eb552d1975c94"}
For an abelian group $A$, the Eilenberg–MacLane spectrum $HA$ is the spectrum with $\pi_0(HA)=A$ and $\pi_i(HA)=0$ for $i\ne 0$. It represents singular cohomology: $H^n(X;A)\cong[\Sigma^\infty X_+,\Sigma^n HA]$. For a discrete ring $A$, $HA$ is the corresponding ring spectrum.
:::

::: {.front card-id="card-e50795cbdd174a93" tags="definition"}
What is the definition of Elementary matrix group?
:::

::: {.back card-id="card-e50795cbdd174a93"}
For a ring $A$, $E_n(A)\subseteq \mathrm{GL}_n(A)$ is the subgroup generated by elementary matrices $I+aE_{ij}$ with $i\ne j$, and $E(A)=\operatorname{colim}_n E_n(A)$. For $n\ge 3$, $E_n(A)=[\mathrm{GL}_n(A),\mathrm{GL}_n(A)]$.
:::

::: {.front card-id="card-0b0ec6a6d70ed6ae" tags="definition"}
What is the definition of Face map?
:::

::: {.back card-id="card-0b0ec6a6d70ed6ae"}
The $i$-th face map of a simplicial object $X$ is $\partial_i:X_n\to X_{n-1}$ for $0\le i\le n$, induced by the injection $[n-1]\to[n]$ that omits $i$; on an $n$-simplex it omits the $i$-th vertex.
:::

::: {.front card-id="card-eef4f5cce0123c36" tags="definition"}
What is the definition of Frobenius map?
:::

::: {.back card-id="card-eef4f5cce0123c36"}
In $\mathrm{TC}(A;p)=\operatorname{holim}_n(\mathrm{THH}(A)^{C_{p^n}},R,F)$, the Frobenius map $F:\mathrm{THH}(A)^{C_{p^n}}\to\mathrm{THH}(A)^{C_{p^{n-1}}}$ is induced by the cyclotomic Frobenius (Tate diagonal) of $\mathrm{THH}(A)$; together with the restriction map $R$ it forms the two structure maps of the homotopy limit.
:::

::: {.front card-id="card-2f3635e497f22c83" tags="definition"}
What is the definition of G-space?
:::

::: {.back card-id="card-2f3635e497f22c83"}
A $G$-space for a topological group $G$ is a space $X$ with a continuous action $G\times X\to X$. A based $G$-space is a based space with a $G$-action fixing the basepoint, and a $G$-map is an equivariant continuous map.
:::

::: {.front card-id="card-ddb77ea2b67686e7" tags="definition"}
What is the definition of Geometric realization?
:::

::: {.back card-id="card-ddb77ea2b67686e7"}
The geometric realization of a simplicial object $X$ is $|X|=\left(\coprod_n X_n\times\Delta^n\right)/\sim$, where $(x,\partial_i t)\sim(\partial_i x,t)$ and $(x,s_i t)\sim(s_i x,t)$; equivalently $|X|=\int^{n} X_n\times\Delta^n$. For a cyclic object, $|X|$ carries a circle action.
:::

::: {.front card-id="card-e95654230f929604" tags="definition"}
What is the definition of Grothendieck group?
:::

::: {.back card-id="card-e95654230f929604"}
For an abelian category $\mathcal{A}$ (or, more generally, an exact category), $K_0(\mathcal{A})$ is the abelian group with generators the isomorphism classes $[A]$ and relations $[B]=[A]+[C]$ for every admissible short exact sequence $0\to A\to B\to C\to 0$. For a ring $A$ and $\mathcal{A}={}_{A}\Mod^{\mathrm{fg},\mathrm{proj}}$ with the split exact structure, this is $K_0(A)$.
:::

::: {.front card-id="card-f0ed3e61ecb0a3a3" tags="definition"}
What is the definition of Group completion?
:::

::: {.back card-id="card-f0ed3e61ecb0a3a3"}
The group completion of a commutative monoid $M$ is a group $M^{-1}M$ with a monoid map $M\to M^{-1}M$ universal among maps from $M$ to groups; concretely $M^{-1}M=\{m-n:m,n\in M\}/\sim$ with $(m,n)\sim(m',n')$ iff $m+n'+k=m'+n+k$ for some $k$, and for a topological monoid $M$ it is computed by $\Omega BM$.
:::

::: {.front card-id="card-2eb80c9f06fa37cc" tags="definition"}
What is the definition of H-cobordism?
:::

::: {.back card-id="card-2eb80c9f06fa37cc"}
An $h$-cobordism from $X$ to $Y$ is a cobordism $W$ for which both inclusions $X\hookrightarrow W$ and $Y\hookrightarrow W$ are homotopy equivalences.
:::

::: {.front card-id="card-fea42249a38c40d2" tags="definition"}
What is the definition of Homotopy class?
:::

::: {.back card-id="card-fea42249a38c40d2"}
The homotopy class of a map $f:X\to Y$ is its equivalence class under the relation of homotopy; the set of such classes is denoted $[X,Y]$. For based spaces one uses based homotopies and writes $[X,Y]_*$.
:::

::: {.front card-id="card-dd758512672c9e50" tags="definition"}
What is the definition of Homotopy equivalence?
:::

::: {.back card-id="card-dd758512672c9e50"}
A map $f:X\to Y$ is a homotopy equivalence if there is $g:Y\to X$ with $g\circ f\simeq \operatorname{id}_X$ and $f\circ g\simeq \operatorname{id}_Y$. If $X$ and $Y$ are CW complexes, this is equivalent to $f$ inducing a bijection on path components and on $\pi_n$ for every basepoint and every $n\ge 1$.
:::

::: {.front card-id="card-9cba5a7bd123f88f" tags="definition"}
What is the definition of Homotopy group?
:::

::: {.back card-id="card-9cba5a7bd123f88f"}
For $n\ge 0$, $\pi_n(X,x_0)$ is the set of based homotopy classes of maps $(S^n,*)\to(X,x_0)$; for $n\ge 1$ it is a group under the pinch map $S^n\to S^n\vee S^n$ (abelian for $n\ge 2$), and $\pi_0$ is the set of path components.
:::

::: {.front card-id="card-4621c7c737c7564c" tags="definition"}
What is the definition of Homotopy limit?
:::

::: {.back card-id="card-4621c7c737c7564c"}
The homotopy limit of a diagram $X:I\to\mathcal{C}$ of spaces or spectra is its derived limit, computed by replacing $X$ by a fibrant diagram and taking the ordinary limit. For a tower $\cdots\to X_2\to X_1\to X_0$ it is the homotopy fibre of $1-\mathrm{shift}:\prod_n X_n\to\prod_n X_n$.
:::

::: {.front card-id="card-c92ef5e073255a5e" tags="definition"}
What is the definition of Linear isometry category?
:::

::: {.back card-id="card-c92ef5e073255a5e"}
The linear isometry category $\mathcal{L}$ has as objects finite-dimensional real inner product spaces $V$, and as morphism space $\mathcal{L}(V,W)=\operatorname{Isom}(V,W)$, the set of linear isometries $V\to W$ topologized as the Stiefel manifold; composition is composition of isometries.
:::

::: {.front card-id="card-1ba2e2fa4a5b7c9b" tags="definition"}
What is the definition of Maximal real subfield?
:::

::: {.back card-id="card-1ba2e2fa4a5b7c9b"}
The maximal real subfield of $\mathbb{Q}(\zeta_n)$ is $\mathbb{Q}(\zeta_n)^+=\mathbb{Q}(\zeta_n+\zeta_n^{-1})$, the fixed field of complex conjugation; for $n\ge 3$ it has degree $\varphi(n)/2$ over $\mathbb{Q}$.
:::

::: {.front card-id="card-c70cadc7405c9385" tags="definition"}
What is the definition of Negative cyclic homology?
:::

::: {.back card-id="card-c70cadc7405c9385"}
Negative cyclic homology $HC^-_*(A)$ is the homology of the complex $(C_*(A)[[u]],\,b+uB)$ with $|u|=2$, where $C_*(A)$ is the Hochschild chain complex, $b$ the Hochschild differential, and $B$ Connes' operator. The inclusion of coefficients gives a natural map $HC^-_*(A)\to \mathrm{HH}_*(A)$.
:::

::: {.front card-id="card-4798d901dada98e9" tags="definition"}
What is the definition of Opposite algebra?
:::

::: {.back card-id="card-4798d901dada98e9"}
The opposite algebra $A^{\mathrm{op}}$ of an algebra $A$ has the same underlying abelian group, but multiplication $a\cdot^{\mathrm{op}}b=ba$. Left $A$-modules are the same as right $A^{\mathrm{op}}$-modules.
:::

::: {.front card-id="card-138c03c0d23e4c35" tags="definition"}
What is the definition of Plus construction?
:::

::: {.back card-id="card-138c03c0d23e4c35"}
Quillen's plus construction $X^+$ is obtained from a space $X$ by attaching $2$- and $3$-cells that kill a chosen perfect normal subgroup $N\triangleleft\pi_1(X)$, without changing integral homology: $H_*(X^+;\mathbb{Z})\cong H_*(X;\mathbb{Z})$. For a ring $A$, $K_n(A)=\pi_n(\mathbf{B}\mathrm{GL}(A)^+)$.
:::

::: {.front card-id="card-04bfa0dee46e06d5" tags="definition"}
What is the definition of Relative k-theory?
:::

::: {.back card-id="card-04bfa0dee46e06d5"}
For a ring $A$ and an ideal $I\triangleleft A$, relative $K$-theory $K_n(A,I)$ is $\pi_n$ of the homotopy fibre of $K(A)\to K(A/I)$; it fits in the long exact sequence $\cdots\to K_n(A,I)\to K_n(A)\to K_n(A/I)\to K_{n-1}(A,I)\to\cdots$.
:::

::: {.front card-id="card-a826a46a3c91875f" tags="definition"}
What is the definition of Representation?
:::

::: {.back card-id="card-a826a46a3c91875f"}
A real representation of a group $G$ is a real vector space $V$ with a homomorphism $G\to \mathrm{GL}(V)$ (continuous when $G$ is topological), equivalently a linear $G$-action on $V$. A subrepresentation is a $G$-invariant linear subspace $W\subseteq V$.
:::

::: {.front card-id="card-f92290f560c1fcd4" tags="definition"}
What is the definition of Restriction map?
:::

::: {.back card-id="card-f92290f560c1fcd4"}
In $\mathrm{TC}(A;p)=\operatorname{holim}_n(\mathrm{THH}(A)^{C_{p^n}},R,F)$, the restriction map $R:\mathrm{THH}(A)^{C_{p^n}}\to\mathrm{THH}(A)^{C_{p^{n-1}}}$ is the inclusion of $C_{p^n}$-fixed points into $C_{p^{n-1}}$-fixed points, induced by the subgroup inclusion $C_{p^{n-1}}\subset C_{p^n}$; it forgets the action of the remaining $C_p$-factor.
:::

::: {.front card-id="card-dd98a36a2f192516" tags="definition"}
What is the definition of Simplicial object?
:::

::: {.back card-id="card-dd98a36a2f192516"}
A simplicial object in a category $\mathcal{C}$ is a functor $\Delta^{\mathrm{op}}\to\mathcal{C}$, where $\Delta$ has objects $[n]=\{0,\dots,n\}$ and order-preserving maps; concretely it consists of objects $X_n$ with face maps $\partial_i$ and degeneracy maps $s_i$ satisfying the simplicial identities.
:::

::: {.front card-id="card-9dc5ade542e178e7" tags="definition"}
What is the definition of Singular cohomology?
:::

::: {.back card-id="card-9dc5ade542e178e7"}
For a space $X$ and an abelian group $A$, $H^n_{\mathrm{sing}}(X;A)=H^n(\operatorname{Hom}(C_*(X),A))$, the cohomology of the cochain complex dual to the singular chain complex $C_*(X)$ of all continuous simplices $\Delta^n\to X$.
:::

::: {.front card-id="card-703318974dfbc92f" tags="definition"}
What is the definition of Smash product?
:::

::: {.back card-id="card-703318974dfbc92f"}
For based spaces, $X\wedge Y=(X\times Y)/(X\vee Y)$. For based spectra, the smash product is the symmetric monoidal product with unit the sphere spectrum $S$; it satisfies $S^V\wedge S^W\cong S^{V\oplus W}$ for finite-dimensional inner product spaces $V,W$.
:::

::: {.front card-id="card-8ad0a543068a2e53" tags="definition"}
What is the definition of Spectral sequence?
:::

::: {.back card-id="card-8ad0a543068a2e53"}
A spectral sequence is a family of bigraded objects $E^r_{p,q}$ with differentials $d^r:E^r_{p,q}\to E^r_{p-r,q+r-1}$ satisfying $d^r\circ d^r=0$ and isomorphisms $E^{r+1}_{p,q}\cong H_{p,q}(E^r)$, together with a filtration of a limit object whose associated graded is $E^\infty_{p,q}$.
:::

::: {.front card-id="card-1e6faa577c535c78" tags="definition"}
What is the definition of Spectrum?
:::

::: {.back card-id="card-1e6faa577c535c78"}
A spectrum is a sequence of based spaces $X_n$ for $n\ge 0$ with structure maps $\Sigma X_n\to X_{n+1}$; an orthogonal spectrum is a based continuous functor (copresheaf) from the linear isometry category of finite-dimensional real inner product spaces to based spaces, a model of the same stable homotopy theory. A spectrum represents a generalized cohomology theory, with $\pi_n(X)=[S^n,X]$.
:::

::: {.front card-id="card-48e698561084e65a" tags="definition"}
What is the definition of Sphere bundle?
:::

::: {.back card-id="card-48e698561084e65a"}
For a rank-$n$ vector bundle $E\to B$ with a metric, the sphere bundle is $S(E)=\{v\in E:\|v\|=1\}$, a fibre bundle with fibre $S^{n-1}$; it is the boundary of the disc bundle $D(E)$.
:::

::: {.front card-id="card-c06ec75567736ce6" tags="definition"}
What is the definition of Sphere spectrum?
:::

::: {.back card-id="card-c06ec75567736ce6"}
The sphere spectrum $S=\Sigma^\infty S^0$ is the suspension spectrum of the based two-point space. It is the unit for the smash product of spectra, and $\pi_n(S)$ is the $n$-th stable homotopy group of spheres.
:::

::: {.front card-id="card-1e2bc5f0dc619866" tags="definition"}
What is the definition of Stable homotopy category?
:::

::: {.back card-id="card-1e2bc5f0dc619866"}
The stable homotopy category $\mathrm{Ho}(\mathsf{Sp})$, often denoted $\mathsf{Sp}$, is the homotopy category of spectra, obtained by inverting the stable weak equivalences. It is triangulated and symmetric monoidal under the smash product, and suspension is invertible in it.
:::

::: {.front card-id="card-a82a6bf23532debf" tags="definition"}
What is the definition of Stiefel manifold?
:::

::: {.back card-id="card-a82a6bf23532debf"}
The Stiefel manifold $V_k(\mathbb{R}^n)=\operatorname{Isom}(\mathbb{R}^k,\mathbb{R}^n)$ is the space of ordered orthonormal $k$-frames in $\mathbb{R}^n$. It is a manifold of dimension $nk-\binom{k+1}{2}$, diffeomorphic to $O(n)/O(n-k)$.
:::

::: {.front card-id="card-7e735bc78c49b226" tags="definition"}
What is the definition of Suspension?
:::

::: {.back card-id="card-7e735bc78c49b226"}
The suspension of a based space $X$ is $\Sigma X=X\wedge S^1$, equivalently $X\times[0,1]$ with $X\times\{0\}$ and $X\times\{1\}$ collapsed to a point. For a finite-dimensional real inner product space $V$, the $V$-fold suspension is $\Sigma^V X=S^V\wedge X$ with $S^V=V^+$.
:::

::: {.front card-id="card-291324581483b94e" tags="definition"}
What is the definition of Topological cyclic homology?
:::

::: {.back card-id="card-291324581483b94e"}
Topological cyclic homology is the homotopy limit $\mathrm{TC}(A;p)=\operatorname{holim}_{n,\,R,F}\mathrm{THH}(A)^{C_{p^n}}$, taken over the fixed-point spectra $\mathrm{THH}(A)^{C_{p^n}}$ with the restriction maps $R$ and Frobenius maps $F$. The spectrum $\mathrm{TC}(A)$ is assembled from the $p$-typical pieces $\mathrm{TC}(A;p)$ over primes $p$.
:::

::: {.front card-id="card-4c3a8f47ea8def13" tags="definition"}
What is the definition of Topological k-theory?
:::

::: {.back card-id="card-4c3a8f47ea8def13"}
Complex topological $K$-theory assigns to a compact space $X$ the Grothendieck group $K^0(X)$ of complex vector bundles on $X$, with $K^{-n}(X)=K^0(\Sigma^n X)$; Bott periodicity gives $K^{n}(X)\cong K^{n+2}(X)$. Real topological $K$-theory is the analogous theory for real vector bundles, with period $8$.
:::

::: {.front card-id="card-42eba366d5de9afa" tags="definition"}
What is the definition of Tower?
:::

::: {.back card-id="card-42eba366d5de9afa"}
A tower (inverse system) is a sequence of objects and maps $X_0\leftarrow X_1\leftarrow X_2\leftarrow\cdots$. Its limit is $\varprojlim_n X_n$, and its homotopy limit is $\operatorname{holim}_n X_n$.
:::

::: {.front card-id="card-a2a5cb70644b097d" tags="definition"}
What is the definition of Trace method?
:::

::: {.back card-id="card-a2a5cb70644b097d"}
Trace methods compare algebraic $K$-theory with Hochschild and topological Hochschild homology through natural trace maps $K(A)\to \mathrm{HH}(A)$ and $K(A)\to \mathrm{TC}(A)$; these maps become equivalences after rationalization, or after completion with respect to a nilpotent ideal, in favourable cases.
:::

::: {.front card-id="card-5ab2267e28edd83e" tags="definition"}
What is the definition of Whitehead group?
:::

::: {.back card-id="card-5ab2267e28edd83e"}
The Whitehead group of a group $\pi$ is $\mathrm{Wh}(\pi)=K_1(\mathbb{Z}\pi)/\{\pm\pi\}$, the quotient of $K_1$ of the integral group ring by the subgroup generated by the classes of $\pm g$ for $g\in\pi$. It is the obstruction group in the $s$-cobordism theorem.
:::
