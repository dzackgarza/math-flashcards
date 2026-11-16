---
title: "Algebraic Geometry::Deformation Theory"
---

::: {.front card-id="deformation-finite-group-invariants" tags="theorem application"}
For a smooth proper complex variety with a finite group action, what controls deformations carrying that action over a base with trivial group action? Apply this to an involution and a lattice polarization on a K3 surface.
:::

::: {.back card-id="deformation-finite-group-invariants"}
For $G\curvearrowright X$, equivariant infinitesimal automorphisms, tangent directions, and an obstruction space are respectively
$$H^0(X,T_X)^G,\qquad H^1(X,T_X)^G,\qquad H^2(X,T_X)^G.$$
For a small extension with kernel $I$, tensor the obstruction group with $I$. Averaging $|G|^{-1}\sum_{g\in G}g$ makes invariants exact over $\mathbb C$, eliminating higher group-cohomology terms. For singular $X$, use the equivariant cotangent complex and $\operatorname{Ext}^i(L_X,\mathcal O_X)^G$; the tangent sheaf alone misses smoothing directions.

For a K3 surface, $H^0(T_X)=H^2(T_X)=0$, so deformations preserving a given finite action are unobstructed. Under local Torelli, preserving a nonsymplectic involution means keeping the period in its $(-1)$-eigenspace. Preserving a specified Picard sublattice $S$ imposes
$$\omega\perp S;\qquad \xi\mathbin{\lrcorner}c_1(L)=0\in H^2(\mathcal O_X)\quad(L\in S)$$
on the period and first-order Kodaira–Spencer class respectively. At a Kulikov boundary, component actions, gluing, and invariant period data must also be supplied; a symmetric dual complex is not an equivariant deformation by itself.

Reference: Lyu–Pan, *Remarks on Automorphism and Cohomology of Cyclic Coverings*, §3; AEGS, Theorem 4.6.
:::

::: {.front card-id="deformation-perfect-obstruction-virtual-class" tags="definition comparison"}
Define a two-term perfect obstruction theory and its virtual fundamental class. Why does expected dimension alone not define a curve-counting invariant?
:::

::: {.back card-id="deformation-perfect-obstruction-virtual-class"}
For a finite-type Deligne–Mumford stack $M/\mathbb C$, a perfect obstruction theory is a morphism
$$\phi:E^\bullet\longrightarrow L_M,\qquad
E^\bullet\simeq[E^{-1}\to E^0]$$
locally with vector bundles in degrees $-1,0$, such that $h^0(\phi)$ is an isomorphism and $h^{-1}(\phi)$ is surjective. At a point, $h^0((E^\bullet)^\vee)$ gives the tangent space and $h^1((E^\bullet)^\vee)$ an obstruction space.

The intrinsic normal cone embeds in the vector-bundle stack $h^1/h^0((E^\bullet)^\vee)$; intersecting it with the zero section defines
$$[M]^{\mathrm{vir}}\in A_v(M),\qquad v=\operatorname{rk}E^0-\operatorname{rk}E^{-1}.$$
For stacks use rational Chow groups when stabilizers require them. Properness permits pushforward to a point after insertions of codimension $v$. The virtual class depends on the obstruction theory; a dimension formula does not supply its cone or multiplicities.

Reference: Behrend–Fantechi, [The intrinsic normal cone](https://arxiv.org/abs/alg-geom/9601010).
:::

::: {.front card-id="deformation-virtual-zero-locus-example" tags="application comparison"}
For a section of a vector bundle on a smooth variety, describe the natural obstruction theory. Compare a transverse section with the zero section.
:::

::: {.back card-id="deformation-virtual-zero-locus-example"}
$V$ smooth, $B\to V$ of rank $r$, $s\in H^0(V,B)$, $Z=Z(s)$:
$$[B^\vee|_Z\xrightarrow{ds}\Omega_V|_Z]\longrightarrow L_Z,\qquad
\operatorname{vdim}Z=\dim V-r.$$
Its virtual class is the refined intersection of $s(V)$ with the zero section; its pushforward to $V$ is $c_r(B)\cap[V]$.

| Section | Actual zero locus | Virtual class |
| --- | --- | --- |
| Transverse $s$ | Smooth of codimension $r$ | $[Z]$ |
| $s=0$ | All of $V$ | $c_r(B)\cap[V]$ |

For $V=\mathbb P^1$ and $B=\mathcal O(2)$, a section with two simple zeros gives degree two. The zero section still has virtual degree two although its actual zero locus is a curve. The same scheme $V$ with its ordinary smooth obstruction theory instead has virtual dimension one and class $[V]$.
:::

::: {.front card-id="deformation-stable-nodal-curve-parameters" tags="application comparison"}
Separate the locally trivial and node-smoothing directions for a stable $n$-pointed nodal complex curve of genus $g$. Compute them for two copies of $\mathbb P^1$ meeting in three nodes, with no markings.
:::

::: {.back card-id="deformation-stable-nodal-curve-parameters"}
Let $\delta$ be the number of nodes. On each normalization component $C_v$ of genus $g_v$, mark the original markings and every preimage of a node; let their total number be $n_v$.

Locally trivial tangent directions deform these pointed components and have dimension
$$\sum_v(3g_v-3+n_v)=3g-3+n-\delta.$$
Each node contributes a one-dimensional smoothing space with local equation $xy=t_e$. The local-to-global sequence is surjective onto these spaces and has zero obstruction group, so the marked miniversal base is smooth of dimension $3g-3+n$. The splitting into component and smoothing coordinates is not canonical.

For two rational components meeting at three nodes, the dual graph has first Betti number two, hence $g=2$. Each component has three special points and is rigid. All three deformation parameters smooth nodes: locally trivial dimension zero, total dimension three. Finite automorphisms can still act on this smooth base when passing to coarse moduli.
:::

::: {.front card-id="deformation-simple-bundle-k3" tags="application comparison"}
For a simple vector bundle $E$ on a complex K3 surface, why does $\operatorname{Ext}^2(E,E)\ne0$ not imply obstructed deformations? Explain the trace-free calculation.
:::

::: {.back card-id="deformation-simple-bundle-k3"}
Simplicity means $\operatorname{Hom}(E,E)=\mathbb C\,\mathrm{id}$. Since $\omega_X\cong\mathcal O_X$, Serre duality gives
$$\operatorname{Ext}^2(E,E)\cong\operatorname{Hom}(E,E)^\vee\cong\mathbb C.$$
The trace map $\operatorname{Ext}^2(E,E)\to H^2(\mathcal O_X)$ is dual to the isomorphism $H^0(\mathcal O_X)\to\operatorname{Hom}(E,E)$ sending $1$ to $\mathrm{id}$. Hence its kernel is zero.

Fixed-determinant obstructions lie in this trace-free kernel. The determinant itself has a unique deformation class on the fixed K3 because $H^1(\mathcal O_X)=0$ and it always lifts by pullback. Thus deformations of $E$ on the fixed K3 are unobstructed despite the nonzero full Ext group. Scalar automorphisms remain in the deformation groupoid.
:::

::: {.front card-id="deformation-artinian-marked-families" tags="definition comparison"}
Define $\operatorname{Art}_k$ and a deformation of a finite-type $k$-scheme $X$ over an object of this category. What are the marking, morphisms, trivial deformation, and tangent space?
:::

::: {.back card-id="deformation-artinian-marked-families"}
$\operatorname{Art}_k$: local Artinian $k$-algebras with identified residue field $k$; morphisms are local $k$-algebra maps inducing the identity on the residue field.

A deformation is a flat finite-type $X_A\to\operatorname{Spec}A$ with a marking $\iota:X_A\times_Ak\xrightarrow{\sim}X$. Isomorphisms respect $\iota$; a map $A\to B$ gives base change $X_B$.
$$\operatorname{Def}_X(A)=\{(X_A,\iota)\}/\cong,\qquad
t_X=\operatorname{Def}_X(k[\varepsilon]/\varepsilon^2).$$
The trivial deformation is $X\times_k\operatorname{Spec}A$ with its evident marking. Keeping all marked isomorphisms gives the deformation groupoid; taking isomorphism classes forgets stabilizers. A first-order deformation is only the case $A=k[\varepsilon]/\varepsilon^2$, not an arbitrary infinitesimal base.
:::

::: {.front card-id="deformation-small-extension-flatness" tags="definition application"}
Define square-zero and small extensions of local Artinian $k$-algebras. Formulate the lifting problem and explain why flatness is essential using $k[t]/(t^2)$.
:::

::: {.back card-id="deformation-small-extension-flatness"}
For $A'\twoheadrightarrow A$ with kernel $I$:

- Square-zero: $I^2=0$.
- Small: $\mathfrak m_{A'}I=0$ and $\dim_k I=1$ (the convention used here).

Every surjection in $\operatorname{Art}_k$ factors into small extensions. Kernels annihilated by the maximal ideal but of larger dimension can be handled by a flag of $k$-subspaces.

Given $X_A$, seek a cartesian square with right-hand map flat:
$$\begin{array}{ccc}
X_A&\longrightarrow&X_{A'}\\
\downarrow&&\downarrow\\
\operatorname{Spec}A&\hookrightarrow&\operatorname{Spec}A'.
\end{array}$$
The identification $X_{A'}\times_{A'}A\cong X_A$ is part of the lift. For $A'=k[t]/t^2$, the module $k=A'/(t)$ is not flat: tensoring $(t)\hookrightarrow A'$ with $k$ gives the zero map $k\to k$. Thus merely having the desired special fiber does not define a deformation.

The map $k[t]/t^{n+1}\twoheadrightarrow k[t]/t^n$ is small, with kernel $k\cdot t^n$ for $n\ge1$.
:::

::: {.front card-id="deformation-obstruction-torsor-package" tags="theorem comparison"}
For a finite-type $k$-scheme $X$, a marked deformation $X_A$, and a small extension $A'\twoheadrightarrow A$ with kernel $I$, state the cotangent obstruction, classification of lifts, and infinitesimal automorphisms. Why is the set of lifts a torsor?
:::

::: {.back card-id="deformation-obstruction-torsor-package"}
Set $T_X^i=\operatorname{Ext}^i_X(L_{X/k},\mathcal O_X)$.

| Object | Controlling group |
| --- | --- |
| Obstruction $o(X_A,A')$ | $T_X^2\otimes_k I$ |
| Isomorphism classes of lifts with fixed identification over $A$, when nonempty | Torsor under $T_X^1\otimes_k I$ |
| Automorphisms of a lift reducing to the identity over $A$ | $T_X^0\otimes_k I$ |

The obstruction vanishes iff a lift exists. Two lifts have a difference in $T_X^1\otimes I$, but no lift is distinguished as zero. Choosing one lift identifies the torsor with the vector space. Forgetting the identification over $A$ can further quotient by automorphisms of $X_A$.

For smooth $X$, $L_{X/k}=\Omega_X^1[0]$ and $T_X^i=H^i(X,T_X)$. These are global Ext groups, not merely sections of sheaf Ext.

Reference: [Stacks, cotangent deformation theory](https://stacks.math.columbia.edu/tag/08UX).
:::

::: {.front card-id="deformation-gluing-cech" tags="construction explanation"}
For smooth separated $X/k$, explain how lifting local trivializations across a small extension produces $H^2(T_X)$ obstructions, $H^1(T_X)$ choices, and $H^0(T_X)$ automorphisms.
:::

::: {.back card-id="deformation-gluing-cech"}
Choose an affine cover with affine intersections. Smooth affine pieces have unobstructed, trivial abstract infinitesimal deformations. Lift their overlap isomorphisms to $g'_{ij}$ over $A'$.

On triple overlaps the cocycle condition can fail by
$$g'_{ij}g'_{jk}g'_{ki}=1+c_{ijk},\qquad c_{ijk}\in T_X(U_{ijk})\otimes I.$$
Because $I^2=0$, composition of infinitesimal errors becomes addition. The $c_{ijk}$ form a Čech two-cocycle. Changing overlap lifts changes it by a coboundary, giving $o\in H^2(T_X)\otimes I$.

If $o=0$, correct the overlap maps to glue. Differences between corrected gluing data are one-cocycles modulo changes of local trivializations, hence $H^1(T_X)\otimes I$. Compatible infinitesimal local automorphisms are global sections, hence $H^0(T_X)\otimes I$.
:::

::: {.front card-id="deformation-unobstructed-rigid-comparison" tags="comparison application"}
Distinguish formal smoothness, infinitesimal rigidity, and vanishing of a chosen obstruction space. Compare $\mathbb P^n$, a genus-$g\ge2$ curve, and a complex abelian surface.
:::

::: {.back card-id="deformation-unobstructed-rigid-comparison"}
Formally smooth means $F(A')\to F(A)$ is surjective for every small extension. Infinitesimally rigid means $t_F=0$. A complete obstruction theory detects liftability by vanishing of its obstruction class; vanishing of its entire obstruction space is stronger.

| Variety over $\mathbb C$ | Tangent space | Deformation behavior |
| --- | --- | --- |
| $\mathbb P^n$ | $H^1(T)=0$ | Infinitesimally rigid; all Artinian abstract deformations are trivial |
| Smooth curve, $g\ge2$ | $h^1(T)=3g-3$ | Unobstructed since $H^2(T)=0$ |
| Abelian surface | $h^1(T)=4$, $h^2(T)=2$ | Unobstructed by Bogomolov–Tian–Todorov |

The last example disproves “unobstructed iff $H^2(T)=0$.” Rigidity does not imply absence of automorphisms: $h^0(T_{\mathbb P^n})=(n+1)^2-1$.
:::

::: {.front card-id="deformation-hulls-universality" tags="definition comparison"}
For a set-valued deformation functor $F$ on $\operatorname{Art}_k$, compare prorepresentability, a versal formal object, and a hull. State smoothness of a transformation $h_R\to F$ explicitly.
:::

::: {.back card-id="deformation-hulls-universality"}
Let $R$ be complete Noetherian local with residue field $k$, and $h_R(A)=\operatorname{Hom}_{\mathrm{local},k}^{\mathrm{cont}}(R,A)$.

| Property of a formal object $\xi$ over $R$ | Requirement |
| --- | --- |
| Universal / prorepresenting | $h_R\xrightarrow{\sim}F$ |
| Versal | $h_R\to F$ is smooth |
| Hull / miniversal in Schlessinger's setting | Smooth and $t_{h_R}\xrightarrow{\sim}t_F$ |

Smoothness requires surjectivity of
$$h_R(A')\longrightarrow h_R(A)\times_{F(A)}F(A')$$
for every small extension $A'\twoheadrightarrow A$. Thus a prescribed inducing map over $A$ can be lifted compatibly with a prescribed deformation over $A'$.

A tangent isomorphism alone is insufficient. The quotient $k[x]/x^3\twoheadrightarrow k[x]/x^2$ induces $h_{k[x]/x^2}\to h_{k[x]/x^3}$ with a tangent isomorphism. Over $A=k[t]/t^2$, the map $x\mapsto t$ cannot lift through $k[x]/x^2$ to $A'=k[t]/t^3$, although it lifts through $k[x]/x^3$: $(t+ct^2)^2=t^2\ne0$. Thus this transformation is not smooth. Hulls need not give unique inducing maps.
:::

::: {.front card-id="deformation-schlessinger-criteria" tags="theorem"}
State Schlessinger's criteria for a functor $F:\operatorname{Art}_k\to\mathrm{Sets}$ with $F(k)$ a singleton. Which conditions give a hull, and which give prorepresentability?
:::

::: {.back card-id="deformation-schlessinger-criteria"}
For $A'\to A\leftarrow A''$, let
$$\theta:F(A'\times_A A'')\to F(A')\times_{F(A)}F(A'').$$

| Condition | Requirement |
| --- | --- |
| H1 | $\theta$ surjective whenever $A''\twoheadrightarrow A$ is small |
| H2 | $\theta$ bijective when $A=k$, $A''=k[\varepsilon]/\varepsilon^2$ |
| H3 | $t_F=F(k[\varepsilon]/\varepsilon^2)$ finite-dimensional over $k$ |
| H4 | $\theta$ bijective when $A'=A''=B$ with the same small map $B\twoheadrightarrow A$ |

H2 supplies the natural vector-space structure on $t_F$. H1–H3 are equivalent to existence of a hull. H1–H4 are equivalent to prorepresentability by a complete Noetherian local $k$-algebra.

H1 concerns existence of gluing; H4 adds uniqueness at the level of isomorphism classes. Automorphisms can obstruct that uniqueness after passing from a groupoid to a set, but their mere presence does not by itself disprove prorepresentability.

Reference: [Stacks, formal deformation theory](https://stacks.math.columbia.edu/tag/06G8).
:::

::: {.front card-id="deformation-kuranishi-equations" tags="theorem comparison"}
Describe the Kuranishi germ of a compact complex manifold, its tangent space, and its equations. How do automorphisms affect universality and comparison with a coarse moduli space?
:::

::: {.back card-id="deformation-kuranishi-equations"}
Locally the germ is the zero locus of a holomorphic map
$$\kappa:(H^1(X,T_X),0)\to(H^2(X,T_X),0),\qquad \kappa(0)=0,\quad d\kappa_0=0.$$
It carries a semiuniversal deformation. Its tangent space is $H^1(T_X)$; its local dimension is at least $h^1(T_X)-h^2(T_X)$. The choice of map and coordinates is not canonical.

If $H^0(T_X)=0$, the family is universal as a germ. Finite automorphisms of the central fiber can still act on that germ when the marking is forgotten; the coarse moduli germ can be a quotient and can be singular even when the marked deformation space is smooth. Infinitesimal automorphisms and finite automorphisms are different issues.

For compact Kähler $X$ with trivial canonical bundle, Bogomolov–Tian–Todorov gives a smooth Kuranishi germ; it does not assert $H^2(T_X)=0$.
:::

::: {.front card-id="deformation-hypersurface-tangent-cohomology" tags="construction formula application"}
Compute the cotangent complex and $T^1,T^2$ for an affine hypersurface $R=k[x_1,\ldots,x_n]/(f)$ with $f$ a nonzerodivisor. Work out a node and a cusp in characteristic zero.
:::

::: {.back card-id="deformation-hypersurface-tangent-cohomology"}
$$L_{R/k}\simeq[R\xrightarrow{df}R^{\oplus n}]\quad\text{in degrees }-1,0.$$
Dualizing gives $[R^{\oplus n}\xrightarrow{(f_{x_i})}R]$ in degrees $0,1$, hence
$$T^0=\operatorname{Der}_k(R,R),\qquad T^1=R/(f_{x_1},\ldots,f_{x_n}),\qquad T^2=0.$$
First-order equations $f+\varepsilon g$ are identified modulo infinitesimal coordinate changes and unit multiples of $f$, which produce the ideal $(f,f_{x_i})$ in the polynomial ring.

| Germ over $\mathbb C$ | $T^1$ | Miniversal formal equation |
| --- | --- | --- |
| Node $xy=0$ | $\mathbb C$ | $xy=t$ |
| Cusp $y^2-x^3=0$ | $\mathbb C[x]/(x^2)$ | $y^2-x^3=a+bx$ |

These affine hypersurface deformation problems are unobstructed. A projective lci scheme can still have global obstructions; local amplitude alone does not kill global Ext in degree two.
:::

::: {.front card-id="deformation-node-flat-smoothing" tags="construction application"}
Verify flatness and describe the fibers of $xy=t$ over $k[t]$. Distinguish smoothing from a locally trivial deformation of the node.
:::

::: {.back card-id="deformation-node-flat-smoothing"}
$$k[t,x,y]/(xy-t)\cong k[x,y],\qquad t\mapsto xy.$$
This is torsion-free as a $k[t]$-module, hence flat because $k[t]$ is a PID. The fiber at $t=0$ is the two coordinate axes meeting in a node. At $t\ne0$, neither $x$ nor $y$ vanishes, and the fiber is smooth, isomorphic to $\mathbb G_m$ after fixing the nonzero parameter.

The first-order smoothing $xy=\varepsilon$ represents the generator of $T^1=k$. It is not locally isomorphic to the product node over the dual numbers. Locally trivial deformations keep the local singularity unchanged; their global variation is governed by the tangent-sheaf part of deformation theory.
:::

::: {.front card-id="deformation-local-global-obstructions" tags="formula application"}
For a projective lci $k$-scheme $X$, relate local singularity deformations to global deformations through the local-to-global Ext sequence. Apply it to a nodal projective curve.
:::

::: {.back card-id="deformation-local-global-obstructions"}
Set $\mathcal T_X^q=\mathcal E xt_X^q(L_{X/k},\mathcal O_X)$ and $T_X^n=\operatorname{Ext}_X^n(L_{X/k},\mathcal O_X)$. Then
$$E_2^{p,q}=H^p(X,\mathcal T_X^q)\Longrightarrow T_X^{p+q}.$$
Since lci gives $\mathcal T_X^{q\ge2}=0$, the low-degree sequence begins
$$0\to H^1(\mathcal T_X^0)\to T_X^1\to H^0(\mathcal T_X^1)
\to H^2(\mathcal T_X^0)\to T_X^2\to H^1(\mathcal T_X^1)\to H^3(\mathcal T_X^0).$$
The first term describes locally trivial deformations. The connecting map tests whether prescribed local first-order deformations globalize.

For a nodal projective curve over an algebraically closed field, $\mathcal T_X^1=\bigoplus_{p\text{ node}}k(p)$, $H^2(\mathcal T_X^0)=0$, and $H^1(\mathcal T_X^1)=0$. Thus $T_X^2=0$ and every collection of node-smoothing parameters lifts to a global first-order deformation.
:::

::: {.front card-id="deformation-embedded-abstract-comparison" tags="formula application"}
For smooth $Z\subset X$ with $X$ fixed, relate embedded and abstract deformations via the tangent-normal sequence. Why can a line in projective space move even though $\mathbb P^1$ is rigid?
:::

::: {.back card-id="deformation-embedded-abstract-comparison"}
$$0\to T_Z\to T_X|_Z\to N_{Z/X}\to0$$
gives
$$H^0(T_X|_Z)\to H^0(N_{Z/X})\xrightarrow{\delta}H^1(T_Z)\to H^1(T_X|_Z)\to H^1(N_{Z/X}).$$
Embedded tangent directions are $H^0(N)$; their underlying abstract deformation is $\delta$. Embedded obstructions lie in $H^1(N)$. Sections of $T_X|_Z$ need not extend to global vector fields on $X$.

For a line $\ell\subset\mathbb P^n$,
$$N_{\ell/\mathbb P^n}=\mathcal O(1)^{n-1},\qquad h^0(N)=2n-2,\quad H^1(N)=0,\quad H^1(T_\ell)=0.$$
The line moves in the Grassmannian, but every underlying abstract curve is still $\mathbb P^1$. Moving an embedding and deforming the isomorphism class are different problems.
:::

::: {.front card-id="deformation-sheaves-ext-determinant" tags="theorem comparison application"}
State the automorphism, tangent, and obstruction groups for a coherent sheaf $E$ on a fixed smooth projective variety. For a vector bundle in characteristic zero, what changes when its determinant is fixed?
:::

::: {.back card-id="deformation-sheaves-ext-determinant"}
For deformations of $E$ flat over the Artinian base, with identified special fiber,
$$\text{infinitesimal automorphisms}:\operatorname{Ext}^0(E,E),\quad
\text{tangent}:\operatorname{Ext}^1(E,E),\quad
\text{obstructions}:\operatorname{Ext}^2(E,E).$$
Across a small extension with kernel $I$, tensor these groups with $I$; the nonempty set of identified lifts is an $\operatorname{Ext}^1(E,E)\otimes I$-torsor.

For a rank-$r>0$ vector bundle in characteristic zero,
$$\mathcal E nd(E)=\mathcal O_X\,\mathrm{id}\oplus\mathcal E nd_0(E),\qquad
\mathcal E nd_0(E)=\ker(\operatorname{tr}).$$
With a fixed identification of the determinant, use $H^i(\mathcal E nd_0(E))$ for $i=0,1,2$. The splitting uses $1/r$; it is not automatic when the characteristic divides $r$.

On a smooth projective curve $H^2(\mathcal E nd(E))=0$, so vector-bundle deformations are unobstructed. This concerns the deformation groupoid; a coarse moduli space can retain quotient singularities.
:::

::: {.front card-id="deformation-explicit-obstructed-module" tags="application counterexample"}
Let $R=k[x]/x^2$ and $E=k$ with $x$ acting by zero. Over $A=k[t]/t^2$, let $E_A=A$ with $x$ acting by multiplication by $t$. Can it lift flatly to $A'=k[t]/t^3$? Identify the obstruction space.
:::

::: {.back card-id="deformation-explicit-obstructed-module"}
No. $E_A$ is free of rank one over $A$, and $x^2$ acts as $t^2=0$, so it is a valid deformation. Any finite flat lift over local Artinian $A'$ must be free of rank one. The lifted action of $x$ would be multiplication by
$$u=t+ct^2,\qquad u^2=t^2\ne0\pmod{t^3},$$
contradicting the relation $x^2=0$. This holds in every characteristic.

The periodic resolution
$$\cdots\xrightarrow{x}R\xrightarrow{x}R\xrightarrow{x}R\to k\to0$$
becomes a complex with zero differentials after applying $\operatorname{Hom}_R(-,k)$, so $\operatorname{Ext}^i_R(k,k)=k$ for all $i\ge0$. The obstruction is a nonzero element of $\operatorname{Ext}^2_R(k,k)\otimes(t^2)$, witnessed directly by $u^2=t^2$.
:::

::: {.front card-id="deformation-line-bundle-thickening" tags="formula application"}
For a square-zero thickening $X\hookrightarrow X'$ with ideal $J$, derive the obstruction to extending a line bundle. Identify the choices of lifts and explain the Picard tangent and obstruction spaces.
:::

::: {.back card-id="deformation-line-bundle-thickening"}
The identification $a\mapsto1+a$ gives an exact sequence of abelian sheaves
$$0\to J\to\mathcal O_{X'}^\times\to\mathcal O_X^\times\to1.$$
Its cohomology gives
$$H^1(X,J)\to\operatorname{Pic}(X')\to\operatorname{Pic}(X)\xrightarrow{\delta}H^2(X,J).$$
A line bundle $L$ extends iff $\delta(L)=0$. With a fixed identification of the restriction with $L$, isomorphism classes of lifts form an $H^1(J)$-torsor, and automorphisms inducing the identity are $H^0(J)$ under addition. Forgetting that identification also permits the action of automorphisms of $L$.

For the product first-order thickening, $J=\mathcal O_X\varepsilon$, so the Picard tangent is $H^1(\mathcal O_X)$ and a complete obstruction space is $H^2(\mathcal O_X)$. On a smooth projective curve this obstruction space vanishes; on an abelian surface it does not, although the characteristic-zero Picard scheme is smooth.
:::

::: {.front card-id="deformation-atiyah-varying-base" tags="construction formula"}
Given a vector bundle $E$ on a smooth complex variety $X$ and a first-order deformation of $X$ with Kodaira–Spencer class $\xi$, what obstructs extending $E$? Specialize to a line bundle.
:::

::: {.back card-id="deformation-atiyah-varying-base"}
The principal-parts extension defines the Atiyah class
$$\operatorname{At}(E)\in\operatorname{Ext}^1(E,E\otimes\Omega_X^1),\qquad
0\to E\otimes\Omega_X^1\to P^1(E)\to E\to0.$$
For $\xi\in\operatorname{Ext}^1(\Omega_X^1,\mathcal O_X)$, the obstruction is the Yoneda composite
$$E\xrightarrow{\operatorname{At}(E)}E\otimes\Omega_X^1[1]
\xrightarrow{1\otimes\xi}E[2]$$
in $\operatorname{Ext}^2(E,E)$, up to the common sign convention for the Kodaira–Spencer class. Its vanishing is independent of that sign.

For a line bundle $L$, $\operatorname{At}(L)$ is its $d\log$ Chern class in $H^1(\Omega_X^1)$. The obstruction is
$$\xi\mathbin{\lrcorner}c_1(L)\in H^2(\mathcal O_X).$$
Deforming $L$ on a fixed $X$ and extending $L$ while $X$ moves are different lifting problems.

Reference: Huybrechts–Thomas, [deformation-obstruction theory via Atiyah and Kodaira–Spencer classes](https://arxiv.org/abs/0805.3527).
:::

::: {.front card-id="deformation-polarized-k3" tags="formula application"}
Describe deformations of a smooth complex variety together with a line bundle using the Atiyah algebra. Compute the tangent dimension and obstruction space for a polarized K3 surface.
:::

::: {.back card-id="deformation-polarized-k3"}
$\mathcal A_L$ is the sheaf of first-order differential operators on $L$ with scalar symbol:
$$0\to\mathcal O_X\to\mathcal A_L\to T_X\to0.$$
Its extension class is $c_1(L)\in H^1(\Omega_X^1)$; $H^i(\mathcal A_L)$ for $i=0,1,2$ controls automorphisms, deformations, and obstructions of $(X,L)$.

For a complex K3 surface and ample $L$,
$$H^1(\mathcal O_X)=0,\quad h^1(T_X)=20,\quad H^2(T_X)=0,\quad H^2(\mathcal O_X)=\mathbb C.$$
The map $H^1(T_X)\xrightarrow{\lrcorner c_1(L)}H^2(\mathcal O_X)$ is nonzero, hence surjective, by Serre duality and $c_1(L)\ne0$. Therefore
$$h^1(\mathcal A_L)=19,\qquad H^2(\mathcal A_L)=0.$$
The polarized deformation space is smooth of dimension nineteen. Scalar automorphisms of $L$ remain; rigidifying them is a separate moduli operation.
:::

::: {.front card-id="deformation-pointed-curves-pairs" tags="formula application comparison"}
What controls deformations of a smooth variety with an SNC divisor, and of a smooth pointed curve? Compute the tangent dimension for a stable pointed curve.
:::

::: {.back card-id="deformation-pointed-curves-pairs"}
For a smooth complex $X$ and labeled SNC divisor $D$, deformations locally trivial as a pair are controlled by
$$T_X(-\log D)=\{v\in T_X:v(I_{D_j})\subset I_{D_j}\text{ for every component }D_j\}.$$
The groups $H^0,H^1,H^2$ give infinitesimal automorphisms, tangent directions, and an obstruction space. This problem preserves the local crossing type; it does not include smoothing a crossing of the boundary.

For a smooth connected projective curve with distinct labeled points and $D=p_1+\cdots+p_n$,
$$T_C(-\log D)=T_C(-D),\qquad\deg T_C(-D)=2-2g-n.$$
If $2g-2+n>0$, then $H^0(T_C(-D))=0$, $H^2=0$, and Riemann–Roch gives
$$h^1(T_C(-D))=3g-3+n.$$
Examples: $(g,n)=(0,3)$ is rigid; $(1,1)$ has a one-dimensional smooth deformation space. Nodal stable curves need cotangent-complex terms for node smoothing as well.
:::

::: {.front card-id="deformation-maps-moving-source" tags="formula comparison"}
For $f:C\to Y$ with $C$ a smooth projective complex curve and $Y$ smooth, compare deformations with fixed source to those allowing the source to move. What changes when values at marked points are fixed?
:::

::: {.back card-id="deformation-maps-moving-source"}
With $C,Y$ fixed: tangent $H^0(C,f^*T_Y)$, obstruction space $H^1(C,f^*T_Y)$. Fixing the values at a reduced marked divisor $D$ replaces $f^*T_Y$ by $f^*T_Y(-D)$.

With $Y$ fixed but $C$ varying, the complex
$$\mathcal K_f=[T_C\xrightarrow{df}f^*T_Y]\quad\text{in degrees }0,1$$
has $\mathbb H^0$ for infinitesimal automorphisms, $\mathbb H^1$ for deformations, and $\mathbb H^2$ for obstructions. Its long exact sequence includes
$$H^0(T_C)\to H^0(f^*T_Y)\to\mathbb H^1(\mathcal K_f)
\to H^1(T_C)\to H^1(f^*T_Y)\to\mathbb H^2(\mathcal K_f)\to0.$$
For constant $f$, $df=0$: source deformations and moving the image point occur separately at first order. Quotienting fixed-source maps by reparametrization is not the same as allowing the complex structure of the source to vary.
:::

::: {.front card-id="deformation-formal-algebraic-analytic" tags="definition theorem comparison"}
Distinguish an infinitesimal deformation, a formal deformation, an effective formal deformation, and analytic convergence. State a useful algebraization criterion with a polarization.
:::

::: {.back card-id="deformation-formal-algebraic-analytic"}
For a complete Noetherian local $k$-algebra $(R,\mathfrak m)$:

- Infinitesimal: one flat family over $R/\mathfrak m^{n+1}$.
- Formal: compatible flat families $X_n$ over all $R/\mathfrak m^{n+1}$, with specified transition isomorphisms.
- Effective/algebraizable: a finite-type $R$-scheme $X$ whose reductions give this system, with properness when required.
- Analytically convergent: over $\mathbb C$, the formal data arise from a germ of an analytic family; formal series alone do not ensure convergence.

Grothendieck algebraization: a compatible proper flat system $X_n$ equipped with compatible line bundles $L_n$, with $L_0$ ample, comes from a flat projective $R$-scheme with an ample line bundle. The polarization must extend through all orders; ampleness of a line bundle on $X_0$ alone does not supply those lifts.

For $xy=t$ the displayed polynomial already gives an algebraic family. In contrast, $\sum_{n\ge0}n!t^n$ defines a formal map to $\mathbb A^1$ over $\mathbb C[[t]]$ but has zero analytic radius of convergence. Algebraization over a complete ring and descent to a finite-type $k$-base are distinct assertions.

Reference: [Stacks, Grothendieck algebraization](https://stacks.math.columbia.edu/tag/089A).
:::

::: {.front card-id="deformation-dg-lie-maurer-cartan" tags="definition formula application"}
Over a characteristic-zero field, state the Maurer–Cartan description associated to a dg Lie algebra concentrated in nonnegative degrees. Identify tangent, automorphism, and obstruction groups and the primary obstruction.
:::

::: {.back card-id="deformation-dg-lie-maurer-cartan"}
For a dg Lie algebra $\mathfrak g$ and $A\in\operatorname{Art}_k$,
$$\operatorname{MC}_{\mathfrak g}(A)=\{\alpha\in\mathfrak g^1\otimes\mathfrak m_A:
d\alpha+\tfrac12[\alpha,\alpha]=0\}.$$
The nilpotent gauge group $\exp(\mathfrak g^0\otimes\mathfrak m_A)$ acts by
$$e^a*\alpha=e^{\operatorname{ad}a}\alpha-
\sum_{n\ge0}\frac{(\operatorname{ad}a)^n}{(n+1)!}(da).$$
The sums are finite because $\mathfrak m_A$ is nilpotent. Gauge classes define the deformation functor; at the origin its infinitesimal automorphisms, tangent, and obstruction space are $H^0(\mathfrak g),H^1(\mathfrak g),H^2(\mathfrak g)$.

For $\alpha=t\alpha_1+t^2\alpha_2$,
$$d\alpha_1=0,\qquad d\alpha_2=-\tfrac12[\alpha_1,\alpha_1].$$
Thus the primary obstruction is $[\tfrac12[\alpha_1,\alpha_1]]\in H^2(\mathfrak g)$. Its vanishing permits second order, not automatically all orders. For a compact complex manifold the Kodaira–Spencer dg Lie algebra is $\mathcal A^{0,\bullet}(T_X^{1,0})$ with differential $\bar\partial$; the Maurer–Cartan equation expresses integrability of the deformed complex structure.
:::

::: {.front card-id="deformation-dg-lie-obstructed-versus-abelian" tags="application comparison"}
Let $\mathfrak g^1=ke$, $\mathfrak g^2=kf$, all other degrees zero, and $d=0$. Compare the brackets $[e,e]=2f$ and $[e,e]=0$ in characteristic zero. Do the dimensions of $H^1,H^2$ decide unobstructedness?
:::

::: {.back card-id="deformation-dg-lie-obstructed-versus-abelian"}
In both cases $H^1=k$, $H^2=k$, and there is no gauge group. Write $\alpha=ae$ with $a\in\mathfrak m_A$.

| Bracket | Maurer–Cartan condition | Representing ring |
| --- | --- | --- |
| $[e,e]=2f$ | $a^2=0$ | $k[[u]]/(u^2)$ |
| Zero | No condition | $k[[u]]$ |

For the first, $a=t$ over $k[t]/t^2$ cannot lift to $k[t]/t^3$, since $(t+ct^2)^2=t^2\ne0$. The second is unobstructed despite $H^2\ne0$. Obstruction maps and higher structure, not just vector-space dimensions, determine the deformation problem.
:::
