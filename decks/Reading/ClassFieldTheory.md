---
title: "Reading::ClassFieldTheory"
---

::: {.front card-id="card-819e900b727840dd"}
When is $k[G]$ commutative?
:::

::: {.back card-id="card-819e900b727840dd"}
Iff $G$ is commutative.
:::

::: {.front card-id="card-e8ca5054254bf3da"}
What is ${}_{G}{\mathsf{Mod}}$?
:::

::: {.back card-id="card-e8ca5054254bf3da"}
$M\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}$ with an action $\psi\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}(G, \mathop{\mathrm{Aut}}({\mathbf{G}}_a M))$, so $g(x+y) = gx+gy$ and $(gh)x = g(hx)$.

$G{\hbox{-}}$equivariant morphisms, $gf(x) = f(gx)$.
:::

::: {.front card-id="card-d57881484e0bb6ef"}
How can you determine if a SES $\xi\in {}_{G}{\mathsf{Mod}}$ is exact?
:::

::: {.back card-id="card-d57881484e0bb6ef"}
Exact iff exact in ${}_{{\mathbf{Z}}}{\mathsf{Mod}}$
:::

::: {.front card-id="card-6183f61d2a02d4b2"}
Define $M^G$ and $M_G$ and discuss their exactness.
:::

::: {.back card-id="card-6183f61d2a02d4b2"}
$M^G \coloneqq\left\{{m\in M{~\mathrel{\Big\vert}~}gm=m\,\,\forall G}\right\}$: invariants, largest $G{\hbox{-}}$trivial **submodule**. Left exact as a functor ${}_{G}{\mathsf{Mod}}\to  {}_{{\mathbf{Z}}}{\mathsf{Mod}}$, so preserves injections.

$M_G \coloneqq M/\left\langle{gm-m{~\mathrel{\Big\vert}~}m\in M, g\in G}\right\rangle_{\mathbf{Z}}$: coinvariants, largest $G{\hbox{-}}$trivial **quotient**. Right exact as a functor, so preserves surjections.
:::

::: {.front card-id="card-306aeaa89da6a68e"}
Interpret $H^*(G; M)$ topologically.
:::

::: {.back card-id="card-306aeaa89da6a68e"}
$H^*(G; {\mathbf{Z}}) = H^*(K(G, 1); {\mathbf{Z}})$ and $H^*(G; M) = H^*(K(G, 1); \underline{M})$ where $\underline{M}$ is a the corresponding local system.
:::

::: {.front card-id="card-71e719597b9254b5"}
Describe the monoid ring $R[M]$ for $R$ a ring and $M$ a monoid. What is its universal property?
:::

::: {.back card-id="card-71e719597b9254b5"}
Free ${}_{R}{\mathsf{Mod}}$ with basis $\left\{{m\in M}\right\}$ with $[m_1]\cdot [m_2] \coloneqq[m_1 m_2]$ using the monoid operation, extended bilinearly.

${}_{R}  \mathsf{Alg}(R[M], B) \cong \mathsf{Mon}(M, {\mathbf{G}}_m B)$.
:::

::: {.front card-id="card-318066493d5f7eeb"}
What is the norm element of a finite group? Why is it important?
:::

::: {.back card-id="card-318066493d5f7eeb"}
$N\coloneqq\sum_{g\in G} g\in {\mathbf{Z}}[G]$, which is $G{\hbox{-}}$invariant.

${\mathbf{Z}}[G]^G = \left\langle{N}\right\rangle_{\mathbf{Z}}$.
:::

::: {.front card-id="card-456ddebfbbaa64a2"}
What is the augmentation on ${\mathbf{Z}}[G]$? Describe the augmentation ideal.
:::

::: {.back card-id="card-456ddebfbbaa64a2"}
$\alpha: {\mathbf{Z}}[G]\to {\mathbf{Z}}$ where $\sum n_g[g] \mapsto \sum n_g$, "evaluate each $g\in G$ at the point 1".

$I\coloneqq\ker \alpha$ fits into a SES $I\hookrightarrow{\mathbf{Z}}[G]\twoheadrightarrow{\mathbf{Z}}\in \zgmod$ where ${\mathbf{Z}}$ has the trivial action.

$I\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\mathrm{free}}$ has basis $\left\{{[g] - [e] {~\mathrel{\Big\vert}~}g\in G}\right\}$.
:::

::: {.front card-id="card-5eab3dfa10f32541"}
When does the augmentation SES split? Why care?
:::

::: {.back card-id="card-5eab3dfa10f32541"}
Only if $G$ is trivial: a section has to send 1 to a $G{\hbox{-}}$invariant element, which is either zero or a multiple of $N$.

If $G$ is nontrivial, ${\mathbf{Z}}$ is not projective in $\zgmod$.
:::

::: {.front card-id="card-d79ac55113f033ef"}
What is Maschke's theorem?
:::

::: {.back card-id="card-d79ac55113f033ef"}
For $k$ a field and $G$ finite, TFAE:

$\operatorname{ch}k \nmid {\sharp}G$

$k[G]$ is a semisimple module, so every $M\in \kgmod$ is projective and injective, thus all higher cohomology vanishes.
:::

::: {.front card-id="card-95736ac32ec10e2f"}
Describe group (co)homology in terms of Tor and Ext.
:::

::: {.back card-id="card-95736ac32ec10e2f"}
$M^G = \zgmod({\mathbf{Z}}\to M)$

$M_G = {\mathbf{Z}}\otimes_{{\mathbf{Z}}[G]} M$.
:::

::: {.front card-id="card-a44f627c5535dc10"}
Which resolutions can be used for $\operatorname{Tor}$ and $\operatorname{Ext}$?
:::

::: {.back card-id="card-a44f627c5535dc10"}
$\operatorname{Tor}(A, B)$: a projective resolution of either argument

$\operatorname{Ext}(A, B)$: a projective resolution of $A$ or an injective resolution of $B$.
:::

::: {.front card-id="card-d7e6762dbf20fb8c"}
Interpret $H_1(G; {\mathbf{Z}})$.
:::

::: {.back card-id="card-d7e6762dbf20fb8c"}
$I/I^2 = G^{\operatorname{ab}}$.
:::

::: {.front card-id="card-5dfb91fdb8faed3e"}
Describe ${\mathbf{Z}}[{\mathbf{Z}}]$.
:::

::: {.back card-id="card-5dfb91fdb8faed3e"}
${\mathbf{Z}}[{\mathbf{Z}}] = {\mathbf{Z}}[t, t^{-1}]$ the Laurent polynomial ring with $I = \left\langle{e-1}\right\rangle$ principal corresponding to $\left\langle{t-1}\right\rangle$, so a free rank 1 $\zgmod$.

UFD of Krull dimension 2.
:::

::: {.front card-id="card-5dac57b1420308dd"}
Describe $H^*({\mathbf{Z}}; M)$ and $H_*({\mathbf{Z}}; M)$.
:::

::: {.back card-id="card-5dac57b1420308dd"}
Use the free resolution ${\mathbf{Z}}[G] \hookrightarrow{\mathbf{Z}}[G] \twoheadrightarrow{\mathbf{Z}}$ using $x\mapsto x\cdot([e] - [1])$ and the augmentation and that $I =\left\langle{e-1}\right\rangle \cong {\mathbf{Z}}[{\mathbf{Z}}]$.

$H_*(G; M) = M_G + M^G t$.

$H^*(G; M) = M^G + M_G t$
:::

::: {.front card-id="card-88b54dbab46175fc"}
What is $I$ for $G = C_n$?
:::

::: {.back card-id="card-88b54dbab46175fc"}
$I = \left\langle{\sigma - 1}\right\rangle$ where $C_n = \left\langle{\sigma}\right\rangle_{\mathbf{Z}}$.
:::

::: {.front card-id="card-655dc1269608105b"}
What is a free resolution of ${\mathbf{Z}}$ in $\zgmod$ for $G = C_n$?
:::

::: {.back card-id="card-655dc1269608105b"}
Periodic:
$$\cdots \xrightarrow{\sigma-1}{\mathbf{Z}}[G]\xrightarrow{\cdot N} {\mathbf{Z}}[G]\xrightarrow{\sigma-1}{\mathbf{Z}}[G]\xrightarrow{{\varepsilon}}{\mathbf{Z}}\to 0$$
:::

::: {.front card-id="card-3eff1b0c0da30d10"}
What are $H^*(C_n; M)$ and $H_*(C_n; M)$?
:::

::: {.back card-id="card-3eff1b0c0da30d10"}
$$H_*(C_n; M) = M_G \cdot t^0 + \bigoplus_{i}M^G/NM \cdot t^{2i+1} + \bigoplus_{i} \ker N/IM \cdot t^{2i}$$
$$H^*(C_n; M) = M^G\cdot t^0 + \bigoplus_{i} \ker N/IM \cdot t^{2i+1} + \bigoplus_{i} M^G/NM\cdot t^{2i}$$
:::

::: {.front card-id="card-bc1dcb9e5085b9c2"}
What are $K({\mathbf{Z}}, 1)$ and $K(C_2, 1)$?
:::

::: {.back card-id="card-bc1dcb9e5085b9c2"}
$K({\mathbf{Z}}, 1)\simeq S^1$.

$K(C_2, 1)\simeq{\mathbf{RP}}^\infty$
:::

::: {.front card-id="card-e4afb7b4e593536b"}
What are the ${}_{G}{\mathsf{Mod}}$ structures on ${}_{{\mathbf{Z}}}{\mathsf{Mod}}(A, B)$ and $A\otimes_{\mathbf{Z}}B$?
:::

::: {.back card-id="card-e4afb7b4e593536b"}
$g\curvearrowright\sum a_i\otimes b_i \coloneqq\sum ga_i\otimes gb_i$ the diagonal action.

$(g\curvearrowright f)(x) \coloneqq g.f(g^{-1}x)$ the adjoint action.
:::

::: {.front card-id="card-de338f6a3408eca9"}
Describe $f\in {}_{{\mathbf{Z}}}{\mathsf{Mod}}(A, B)^G$.
:::

::: {.back card-id="card-de338f6a3408eca9"}
$gf(g^{-1}x) = f(x) \implies gf(x) = f(gx)$, so $G{\hbox{-}}$equivariance.
:::

::: {.front card-id="card-d7b196454f24f6e4"}
Define a free $G{\hbox{-}}$action.
:::

::: {.back card-id="card-d7b196454f24f6e4"}
Trivial stabilizers.
:::

::: {.front card-id="card-0959803a2d48e016"}
What is the standard resolution of ${\mathbf{Z}}$ as a $\zgmod$?
:::

::: {.back card-id="card-0959803a2d48e016"}
$P_n \coloneqq\mathsf{Free}_{  {}_{{\mathbf{Z}}}{\mathsf{Mod}}}(G{ {}^{ \scriptscriptstyle\times^{n+1} }  })$, so $P_0 \cong {\mathbf{Z}}[G]$ and $\operatorname{rank}_{\mathbf{Z}}P_n = {\sharp}(G)^n$ whose differential is
$${\left[ {g_0,\cdots, g_n} \right]}\xrightarrow{{\partial}_n} \sum_{i=0}^n (-1)^i {\left[ {g_0, \cdots, \widehat{g}_i, \cdots, g_n} \right]}$$
:::

::: {.front card-id="card-bc1a1f1752512b0b"}
Describe $\zgmod(P_n, M)$ for $P_\bullet \rightrightarrows{\mathbf{Z}}$ the standard resolution.
:::

::: {.back card-id="card-bc1a1f1752512b0b"}
$\zgmod(P_n\to M) =   {}_{{\mathbf{Z}}}{\mathsf{Mod}}(P_n \to M)^G$, so $f(g.g_0,\cdots, g.g_n) = gf(g_0,\cdots, g_n)$ for $f: G{ {}^{ \scriptscriptstyle\times^{n+1} }  }\to M$.
:::

::: {.front card-id="card-2867e12caed8a73c"}
Describe $Z^1(G; M)$ and $B^1(G; M)$
:::

::: {.back card-id="card-2867e12caed8a73c"}
$f\in Z^1(G; M)$ are functions $f: G\to M$ st $f(g_1 g_2) = f(g_1) + g_1 f(g_2)$, so twisted by $g_1$.

$f\in B^1(G; M)$ are functions where $f(g) = ga-a$ for all $g$ for some fixed $a\in M$.
:::

::: {.front card-id="card-8c80a6a3d5e769b8"}
What is the cocycle condition for $Z^2(G; M)$?
:::

::: {.back card-id="card-8c80a6a3d5e769b8"}
$g_1 f(g_2, g_3) - f(g_1g_2, g_3) + f(g_1, g_2 g_3) - f(g_1, g_2) = 0$.
:::

::: {.front card-id="card-e3e52f477a2a52bf"}
Explain how an extension $E$ of $G$ by $M\in {}_{{\mathbf{Z}}}{\mathsf{Mod}}$ puts a ${}_{G}{\mathsf{Mod}}$ structure on $M$
:::

::: {.back card-id="card-e3e52f477a2a52bf"}
For $M\hookrightarrow E \twoheadrightarrow G$, let $g.m \coloneqq\tilde g m \tilde g^{-1}$ where $\tilde g\in E$ is any lift.
:::

::: {.front card-id="card-6cba8e3d7af69c56"}
How is $H^2(G; M)$ interpreted?
:::

::: {.back card-id="card-6cba8e3d7af69c56"}
Equivalence classes of extensions $M\hookrightarrow E \twoheadrightarrow G$.

The trivial element is $M \rtimes G$ where $M{~\trianglelefteq~}E$.
:::

::: {.front card-id="card-2b6f54fd8f0fdc89"}
Why is $H^*(G; M)$ finite with $G, M$ are finite?
:::

::: {.back card-id="card-2b6f54fd8f0fdc89"}
${\sharp}Z^n(G; M) \leq ({\sharp}M)^{{\sharp}G} < \infty$.
:::

::: {.front card-id="card-25a58edd3c607c88"}
Define $\mathrm{Ind}^{H}_{G} M$ for $M\in {}_{H}{\mathsf{Mod}}$.
:::

::: {.back card-id="card-25a58edd3c607c88"}
$\mathrm{Ind}^{H}_{G}({-}) \coloneqq{\mathbf{Z}}[G]\otimes_{{\mathbf{Z}}[H]} ({-}) \in \zgmod$ acting diagonally.
:::

::: {.front card-id="card-4ae12f9179709702"}
Define $\mathrm{coInd}^{H}_{G} M$ for $M\in {}_{H}{\mathsf{Mod}}$.
:::

::: {.back card-id="card-4ae12f9179709702"}
$\mathrm{coInd}^{H}_{G}({-}) =   {}_{{\mathbf{Z}}[H]}{\mathsf{Mod}}({\mathbf{Z}}[G], {-}) \in \zgmod$ with a funny action $(g.f)(x) \coloneqq f(xg)$.
:::

::: {.front card-id="card-22f2f2a4ffc1708d"}
What is Artin's theorem on representations of finite groups?
:::

::: {.back card-id="card-22f2f2a4ffc1708d"}
For $G\in {\mathsf{Fin}}{\mathsf{Grp}}$, any $V\in {\mathsf{Rep}}(G)^{\mathrm{fd}}_{/ {{\mathbf{C}}}}$ is a ${\mathbf{Q}}{\hbox{-}}$linear combinations of $\mathrm{Ind}^{H}_{G} W$ where $H\leq G$ is cyclic and $W$ is a character.
:::

::: {.front card-id="card-5a798c1532df1e68"}
What is Brauer's theorem on representations of finite groups?
:::

::: {.back card-id="card-5a798c1532df1e68"}
For $G\in {\mathsf{Fin}}{\mathsf{Grp}}$, any $V\in {\mathsf{Rep}}(G)^{\mathrm{fd}}_{/ {{\mathbf{C}}}}$ is a ${\mathbf{Z}}{\hbox{-}}$linear combinations of $\mathrm{Ind}^{H}_{G} W$ where $H\leq G$ is an elementary subgroup, so $H\cong C\times P$ with $C$ cyclic and $P$ a $p{\hbox{-}}$group, and $W$ is a character.
:::

::: {.front card-id="card-c6daf2e47c2b6cf7"}
What is Artin's holomorphy conjecture?
:::

::: {.back card-id="card-c6daf2e47c2b6cf7"}
Every Artin $L{\hbox{-}}$function attached to a nontrivial representation of a finite group has a holomorphic continuation to ${\mathbf{C}}$.

Shown recently for $A_5$ using Langlands.

Brauer shows *meromorphic* continuation as an easy corollary of his induction theorem.
:::

::: {.front card-id="card-4647169caa41a3e2"}
What is Shapiro's lemma?
:::

::: {.back card-id="card-4647169caa41a3e2"}
For $H\leq G$ and $N\in   {}_{H}{\mathsf{Mod}}$,
$$H_n(G; \mathrm{Ind}^{H}_{G} N)  { \, \xrightarrow{\sim}\, }H_n(H; N)$$
$$H^n(G; \mathrm{coInd}^{H}_{G} N)  { \, \xrightarrow{\sim}\, }H_n(H; N)$$
:::

::: {.front card-id="card-1e52d15fd1f67abd"}
What are $\mathrm{Ind}^{{\operatorname{pt}}}_{G} A$ and $\mathrm{coInd}^{{\operatorname{pt}}}_{G} A$?
:::

::: {.back card-id="card-1e52d15fd1f67abd"}
$\mathrm{Ind}^{{\operatorname{pt}}}_{G} A = {\mathbf{Z}}[G]\otimes_{\mathbf{Z}}A$ and $\mathrm{coInd}^{{\operatorname{pt}}}_{G} A =   {}_{{\mathbf{Z}}}{\mathsf{Mod}}({\mathbf{Z}}[G] \to A)$.
:::

::: {.front card-id="card-2a2bbbb6b39f28ca"}
What are acyclic modules for group homology?
:::

::: {.back card-id="card-2a2bbbb6b39f28ca"}
Induced modules: any module isomorphic to $\mathrm{Ind}^{H}_{G} A$ for some $H$ and $A$.

E.g. $H_n(G; \mathrm{Ind}^{{\operatorname{pt}}}_{G} A) = 0$.
:::

::: {.front card-id="card-933022ad9dd315c4"}
Describe how any $M\in {}_{G}{\mathsf{Mod}}$ is surjected onto by an induced module and injects into a coinduced module.
:::

::: {.back card-id="card-933022ad9dd315c4"}
$\mathrm{Ind}^{{\operatorname{pt}}}_{G}M^\mathop{\mathrm{triv}}\twoheadrightarrow M$ and $M\hookrightarrow\mathrm{coInd}^{{\operatorname{pt}}}_{G} M^\mathop{\mathrm{triv}}$.

The maps are $g\otimes m\mapsto gm$ and $x\mapsto (\cdot x)$.
:::

::: {.front card-id="card-7f4c8634f74d038b"}
What are weakly projective/injective modules? Why care?
:::

::: {.back card-id="card-7f4c8634f74d038b"}
Direct summands of induced/coinduced modules respectively.

Easiest acyclic objects to use in practice, since $M\oplus N$ acyclic implies $M, N$ acyclic, since $H^n(G; \bigoplus M_i) = \bigoplus_i H^n(G; M_i)$.
:::

::: {.front card-id="card-8f0637a73510cc02"}
What are the homological versions of Shapiro's lemma?
:::

::: {.back card-id="card-8f0637a73510cc02"}
$$\operatorname{Tor}_n^{{\mathbf{Z}}[H]}(M, N)  { \, \xrightarrow{\sim}\, }\operatorname{Tor}_n^{{\mathbf{Z}}[G]}(M, \mathrm{Ind}^{H}_{G} N)$$
$$ \operatorname{Ext}^n_{{\mathbf{Z}}[H]}(M, N)  { \, \xrightarrow{\sim}\, } \operatorname{Ext}^n_{{\mathbf{Z}}[G]}(M, \mathrm{coInd}^{H}_{G} N)$$
$$ \operatorname{Ext}^n_{{\mathbf{Z}}[H]}(N, M)  { \, \xrightarrow{\sim}\, } \operatorname{Ext}^n_{{\mathbf{Z}}[G]}(\mathrm{Ind}^{H}_{G} N, M)$$
:::

::: {.front card-id="card-cf3e8b4760093ce1"}
What is the adjunction induced by $f\in \mathsf{CRing}(R\to S)$?
:::

::: {.back card-id="card-cf3e8b4760093ce1"}
$(S\otimes_R({-}), \mathrm{Res}^{R}_{S}({-}))$.

$(\mathrm{Res}^{R}_{S} ({-}), \mathop{\mathrm{Hom}}_R(S, {-}))$.
:::

::: {.front card-id="card-1274043ce26249d7"}
Summarize the adjoint relationships between restriction and (co)induction.
:::

::: {.back card-id="card-1274043ce26249d7"}
$(\mathrm{Ind}^{H}_{G}, \mathrm{Res}^{H}_{G})$

$(\mathrm{Res}^{H}_{G}, \mathrm{coInd}^{H}_{G})$.
:::

::: {.front card-id="card-36d71b66bac2997a"}
Compare induction vs. coinduction for finite index subgroups.
:::

::: {.back card-id="card-36d71b66bac2997a"}
If $H\leq G$ is finite index, then $\mathrm{Ind}^{H}_{G} \cong \mathrm{coInd}^{H}_{G}$.
:::

::: {.front card-id="card-f9380b8776e53be6"}
Discuss commuting limits with (co)homology.
:::

::: {.back card-id="card-f9380b8776e53be6"}
$\colim_i H^n(G; A_i)  { \, \xrightarrow{\sim}\, }H^n(G; \colim_i A_i)$.
:::

::: {.front card-id="card-3a3c93240965db25"}
Discuss how to push/pull homology under changes of group $f: G\to G'$.
:::

::: {.back card-id="card-3a3c93240965db25"}
$H^n(G'; {-}) \to H^n(G; {-})$ (contravariant).
:::

::: {.front card-id="card-f7cca75927695f65"}
Discuss restriction and inflation.
:::

::: {.back card-id="card-f7cca75927695f65"}
$f: H\hookrightarrow G$ yields restriction $H^n(G; M) \to H^n(H; M)$.

$N{~\trianglelefteq~}G$ and $M\in   {}_{G}{\mathsf{Mod}}$ yields $M^N\in   {}_{G/N}{\mathsf{Mod}}$ and inflation $H^n(G/N; M^N) \to H^n(G; M)$.
:::

::: {.front card-id="card-83626d3f3af8c6cd"}
When do functors preserve injectives/projectives?
:::

::: {.back card-id="card-83626d3f3af8c6cd"}
Has an exact left adjoint $\implies$ preserves injectives.

Has an exact right adjoint $\implies$ preserves projectives.
:::

::: {.front card-id="card-66cb45fc8793ff61"}
Characterize projectives/injectives using Hom.
:::

::: {.back card-id="card-66cb45fc8793ff61"}
$\mathop{\mathrm{Hom}}(P, {-})\iff$projective

$\mathop{\mathrm{Hom}}({-}, I) \iff$injective
:::

::: {.front card-id="card-25f59b8a0a87a778"}
What is the inflation-restriction exact sequence?
:::

::: {.back card-id="card-25f59b8a0a87a778"}
$$H^1(G/H; A^H) \xhookrightarrow{\mathrm{Inf}} H^1(G; A) \xrightarrow{\mathrm{Res}} H^1(H; A)^{G/H} \longrightarrow H^2(G/H; A^H) \xrightarrow{\mathrm{Inf}} H^2(G/H; A^H) \to H^2(G; A)$$
:::

::: {.front card-id="card-919d2fe8b2dce362"}
What is restriction? What is its important property?
:::

::: {.back card-id="card-919d2fe8b2dce362"}
$\mathop{\mathrm{coRes}}: H^*(H; N) \to H^*(G; N)$ for $H\leq G$ finite index.

Satisfies $\mathop{\mathrm{coRes}}\circ \operatorname{res}= \cdot n$ where $n = [G:H]$.
:::

::: {.front card-id="card-6526cd656c6174f5"}
What is the explicit map for corestriction in degree $n=0$?
:::

::: {.back card-id="card-6526cd656c6174f5"}
Sometimes called trace or norm

$\mathop{\mathrm{coRes}}: M^H \to M^G$ where $x\mapsto \qty{ \sum_{g\in G/H}[g]}x$.
:::

::: {.front card-id="card-4a38f58feea75535"}
Discuss $H^*(G; M)$ and $H_*(G; M)$ for $G$ finite cycle.
:::

::: {.back card-id="card-4a38f58feea75535"}
$H^{2n}(G; M) \cong H_{2n+1}(G; M) = M^G / NM$ for $N$ the norm

$H^{2n+1}(G; M) \cong H_{2n}(G; M) = (\ker N)/IM$ for $I$ the augmentation ideal.

Except at $n=0$, there $H^0(G; M) = M^G$ and $H_0(G; M) = M/IM$.

So higher $H^n$ are quotients of $H^0$ and higher $H_n$ are subs of $H_0$.
:::

::: {.front card-id="card-3ac1b1a541a620af"}
Define Tate cohomology:
:::

::: {.back card-id="card-3ac1b1a541a620af"}
Set $\tilde H^0 (G; M)\coloneqq M^G/NM$ and $\tilde H_0(G; M) \coloneqq(\ker N)/ IM$

Set $\widehat{H}^n(G; M) \coloneqq H^n(G; M)$ for $n\geq 1$.

$\widehat{H}^0(G; M) \coloneqq\tilde H^0(G; M) = M^G/NM$

$\widehat{H}^{-1}(G; M) \coloneqq\tilde H_0(G; M) = (\ker N)/ IM$

$\widehat{H}^{-n}(G; M) \coloneqq H_{-n-1}(G; M)$ for all $n\leq -2$.
:::

::: {.front card-id="card-fd61eb79689387ca"}
What is the LES in Tate cohomology?
:::

::: {.back card-id="card-fd61eb79689387ca"}
$A\hookrightarrow B\twoheadrightarrow C$ yields a bi-infinite LES
$$\cdots \to\widehat{H}^i(G; C) \to \widehat{H}^i(G; B) \to \widehat{H}^i(G; A)\to \widehat{H}^{i+1}(G; C)\to \cdots$$
:::

::: {.front card-id="card-5a8a7e7f468f0f0d"}
Discuss vanishing of $\widehat{H}(G; M)$ for $G\in{\mathsf{Fin}}{\mathsf{Grp}}$.
:::

::: {.back card-id="card-5a8a7e7f468f0f0d"}
Since induced = coinduced for finite groups, weakly injective = weakly projective, so $\widehat{H}^i(G; M) =0$ for all $i$, including $i=0$.
:::

::: {.front card-id="card-ca23e4bdbace6f6c"}
Describe how to compute $\widehat{H}^*(G; M)$ at the cochain level.
:::

::: {.back card-id="card-ca23e4bdbace6f6c"}
Take the "resolution $X_\bullet$ where $X_n = X_{-1-n} = {\mathbf{Z}}[G{ {}^{ \scriptscriptstyle\times^{n+1} }  }]$ with the usual ${\partial}_n$, then $\widehat{H}^n(G; M) =H^n(\mathop{\mathrm{Hom}}(X_n, M)^G)$.
:::

::: {.front card-id="card-8931a01268da4819"}
What is dimension shifting for $\widehat{H}$?
:::

::: {.back card-id="card-8931a01268da4819"}
For $A\hookrightarrow I \twoheadrightarrow B\in   {}_{G}{\mathsf{Mod}}$ with $I$ coinduced, then $\widehat{H}(G; B)\cong \widehat{H}^{n+1}(G; A)$.
:::

::: {.front card-id="card-6b17205179edc5b6"}
Describe (co)restriction for $L/K$ a Galois extension
:::

::: {.back card-id="card-6b17205179edc5b6"}
Noting ${\mathbf{G}}_a(L)^G = K$ for $G\coloneqq{ \mathsf{Gal}}(L/K)$,

$\mathrm{Res}^{H}_{G}: M^G\to M^H$ corresponds to $K\hookrightarrow L$.

$\mathrm{coRes}^{H}_{G}: M^H \to M^K$ corresponds to $\operatorname{Trace}_{L/K}: L\to K$.
:::

::: {.front card-id="card-381db49f4793df13"}
Discuss finiteness for Tate cohomology.
:::

::: {.back card-id="card-381db49f4793df13"}
$\widehat{H}^n(G; M) = \widehat{H}^n(G; M)[m]$ is always a torsion ${}_{{\mathbf{Z}}}{\mathsf{Mod}}$, where $m = {\sharp}G$.

If $M\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\mathrm{fg}}$ then every $\widehat{H}^n(G; M)\in{\mathsf{Fin}}{\mathsf{Grp}}$.

Use that a group is finite iff finitely generated and torsion.
:::

::: {.front card-id="card-ff80a060563c9016"}
What is the transfer?
:::

::: {.back card-id="card-ff80a060563c9016"}
For $H\leq G$ there is an obvious map $H^{\operatorname{ab}}\to G^{\operatorname{ab}}$, but there is also a wrong-way transfer map $G^{\operatorname{ab}}\to H^{\operatorname{ab}}$.
:::

::: {.front card-id="card-a0319417af0eb6b8"}
What is the Herbrand quotient?
:::

::: {.back card-id="card-a0319417af0eb6b8"}
$h(A) \coloneqq h^0(A)/ h^1(A) \in {\mathbf{Z}}_{\geq 0}$ where $h^i(A) \coloneqq{\sharp}\widehat{H}^i(G; A)$.
:::

::: {.front card-id="card-99b40936cb7a50de"}
Discuss the Herbrand quotient.
:::

::: {.back card-id="card-99b40936cb7a50de"}
For $A\hookrightarrow B\twoheadrightarrow C$ a SES, if any two $h({-})$ are defined then it is also defined for the third, and $h(B) = h(A) h(C)$.

If $A$ is finite then $h(A) = 1$ since $h^1 = h^0$.

If $f\in   {}_{G}{\mathsf{Mod}}(A\to B)$ with finite kernel and cokernel then $h(A) = h(B)$.
:::

::: {.front card-id="card-cc0436ecd1b5cc0b"}
What is $\sum (-1)^i {\sharp}A_i$ for $A_i$ in a LES in ${}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\mathrm{fin}}$? For vector spaces?
:::

::: {.back card-id="card-cc0436ecd1b5cc0b"}
$\sum (-1)^i {\sharp}A_i = 1$.

For vector spaces, $\sum (-1)^i \dim A_i = 0$.
:::

::: {.front card-id="card-5772f627c442bf54"}
What is a cohomologically trivial group?
:::

::: {.back card-id="card-5772f627c442bf54"}
Acyclic for group cohomology, not just for $G$ itself but for all $H\leq G$.

So $H\leq G \implies H^n(H; M) = 0$ for all $M\in   {}_{G}{\mathsf{Mod}}$.
:::

::: {.front card-id="card-a28d9eaa9c55722b"}
Discuss $p{\hbox{-}}$groups $G$ acting on $p{\hbox{-}}$primary $G{\hbox{-}}$modules $M$.
:::

::: {.back card-id="card-a28d9eaa9c55722b"}
If $M\neq 0$ then $M^G\neq 0$.
:::

::: {.front card-id="card-9c49955d526039c7"}
Discuss duality in group (co)homology.
:::

::: {.back card-id="card-9c49955d526039c7"}
For $A {}^{ \vee }\coloneqq\mathop{\mathrm{Hom}}(A, {\mathbf{Q}}/{\mathbf{Z}})$, $H^n(G; A) {}^{ \vee }\cong H_n(G; A {}^{ \vee })$ for $G$ finite.
:::

::: {.front card-id="card-e8cd3f416cfb75b7"}
What is the universal property for $\mathop{\mathrm{Hom}}$ and products?
:::

::: {.back card-id="card-e8cd3f416cfb75b7"}
$\mathop{\mathrm{Hom}}(A, \prod B_i) = \prod \mathop{\mathrm{Hom}}(A, B_i)$, i.e. homs **into** a product are determined by homs into coordinates.
:::

::: {.front card-id="card-758a5cbac10a9b22"}
How can cohomological triviality be checked locally?
:::

::: {.back card-id="card-758a5cbac10a9b22"}
$A$ is $G{\hbox{-}}$cohomologically trivial $\iff A$ is $G_p{\hbox{-}}$cohomologically trivial for every sylow $p{\hbox{-}}$subgroup $G_p$ for every $p\mathrel{\Big|}{\sharp}G$.
:::

::: {.front card-id="card-c7e254871b94cd3c"}
When does flat coincide with torsionfree?
:::

::: {.back card-id="card-c7e254871b94cd3c"}
Modules over a PID.
:::

::: {.front card-id="card-70a4f711e884a8b2"}
What is the cup product on cochains?
:::

::: {.back card-id="card-70a4f711e884a8b2"}
$$\begin{align}K^p(G; A) \otimes_{\mathbf{Z}}K^q(G; B) &\to K^{p+q}(G; A\otimes_{\mathbf{Z}}B)\\ a\otimes b &\mapsto \mathbf{g} \mapsto a(g_0,\cdots, g_p)\otimes b(g_{p-1}, \cdots g_{p+q}) \end{align}$$
:::

::: {.front card-id="card-4a8c41cd2c2b1ce0"}
How does ${\partial}$ interact with $\smile$?
:::

::: {.back card-id="card-4a8c41cd2c2b1ce0"}
$d(a\smile b) = (da)\smile b + (-1)^{p}a\smile(db)$.
:::

::: {.front card-id="card-9eea7abfb9816052"}
What is the Tate-Nakayama theorem?
:::

::: {.back card-id="card-9eea7abfb9816052"}
For $A\in   {}_{G}{\mathsf{Mod}}$ and $a\in H^2(G; A)$ satisfying for all primes $p$ that $H^1(G_p; A) = 0$ and ${\sharp}H^2(G_p; A) = {\sharp}G_p$ and is generated by $a_p \coloneqq\mathrm{Res}^{G_p}_{G} a$, for $G_p$ the Sylow $p{\hbox{-}}$subgroups, then

For all $D\in   {}_{G}{\mathsf{Mod}}$ torsionfree and all $H\leq G$, there are isomorphism $\widehat{H}^n(H; D) \underset{ {{-}\smile a} }{ { \, \xrightarrow{\sim}\, }}\widehat{H}^{n+2}(H; A\otimes_{\mathbf{Z}}D)$.

Taking $D = {\mathbf{Z}}$ yields $\widehat{H}^n(H; {\mathbf{Z}}) { \, \xrightarrow{\sim}\, }\widehat{H}^{n+2}(H; D)$, so $D$ cohomology is just a shift of ${\mathbf{Z}}$ cohomology.
:::

::: {.front card-id="card-df98d4dc6835b4d2"}
What is the significance of Tate-Nakayama?
:::

::: {.back card-id="card-df98d4dc6835b4d2"}
For $K\in \mathsf{Local}\mathsf{Field}$ and $L/K$ finite Galois, set $G\coloneqq{ \mathsf{Gal}}(L/K)$ and $A\coloneqq L^{\times}$

The hypotheses of Tate-Nakayama apply and yields
$$G^{\operatorname{ab}}= \widehat{H}^{-2}(G; {\mathbf{Z}})  { \, \xrightarrow{\sim}\, }\widehat{H}^0(G; L^{\times}) = K^{\times}/NL^{\times}$$
Thus if $L/K$ is abelian then $G \cong \operatorname{coker}\operatorname{Nm}_{L/K}$.

Suggests target group for CFT should be $K^{\times}$, so there should be an isomorphism between ${ \mathsf{Gal}}^{\operatorname{ab}}(\overline{K}/K)$ and $\mathsf{pro}K^{\times}$.
:::

::: {.front card-id="card-d1667afc3614c99b"}
Characterize compact totally disconnected spaces.
:::

::: {.back card-id="card-d1667afc3614c99b"}
Inverse limits of finite discrete spaces.

Also called profinite spaces, Stone spaces, boolean spaces.

See Stone duality.
:::

::: {.front card-id="card-754753be1bdb9fee"}
What is a profinite group?
:::

::: {.back card-id="card-754753be1bdb9fee"}
A group object in profinite spaces

A topological group whose underlying space is a profinite space.
:::

::: {.front card-id="card-26a569c2e2ae65ea"}
Discuss open subgroups of compact topological groups
:::

::: {.back card-id="card-26a569c2e2ae65ea"}
A subgroup is open iff closed and finite index.

Note that open iff closed always holds, so compactness is giving finite index.

NOT true that every finite index subgroup is closed!
:::

::: {.front card-id="card-5689c73b27f7cdd4"}
How do you extract a Hausdorff topological group from an non-Hausdorff one?
:::

::: {.back card-id="card-5689c73b27f7cdd4"}
Mod out by the closure of the identity.
:::

::: {.front card-id="card-d2550c00c7687b84"}
What is $\aleph_0$?
:::

::: {.back card-id="card-d2550c00c7687b84"}
Countable cardinality.
:::

::: {.front card-id="card-6f09c31e889f6770"}
Is a finite index subgroup of a topological group open?
:::

::: {.back card-id="card-6f09c31e889f6770"}
No! $V\coloneqq\prod { \mathbf{F} }_2$ has $\aleph_0$ open subgroups but $2^{2^{\aleph_0}}$ index 2 subgroups.
:::

::: {.front card-id="card-24034aab968ea04a"}
Write a profinite group as a limit.
:::

::: {.back card-id="card-24034aab968ea04a"}
$G = \cocolim_{U\leq G \text{ open}, [G:U] < \infty} G/U$.
:::

::: {.front card-id="card-5eb386e405e9386c"}
Describe the image of $G$ in $\mathsf{pro}G$.
:::

::: {.back card-id="card-5eb386e405e9386c"}
$\operatorname{im}(G\to \mathsf{pro}G)$ is dense, but need not be an injection.

E.g. cts image of connected is connected.
:::

::: {.front card-id="card-5c50810c3d981267"}
What is a residually finite group? Why care?
:::

::: {.back card-id="card-5c50810c3d981267"}
$G\hookrightarrow\mathsf{pro}G$ is an injection, so any $g\neq e$ admits a finite index subgroup not containing $g$.

Useful since $\pi_1^\text{ét}(X) = \mathsf{pro}\pi_1(X({\mathbf{C}}))$, so not residually finite means losing information from $\pi_1$.
:::

::: {.front card-id="card-fc6ad817c2e32bcd"}
What is the Galois correspondence for infinite extensions?
:::

::: {.back card-id="card-fc6ad817c2e32bcd"}
Subextensions of $k^{ {}^{ \operatorname{sep} } }/k$ correspond to **closed** subgroups of ${ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k)$ with the Krull topology.
:::

::: {.front card-id="card-fc790016b53e422d"}
Characterize topological groups acting on discrete modules.
:::

::: {.back card-id="card-fc790016b53e422d"}
The action is cts iff ${\operatorname{Stab}}_G(x)$ is open for every $x$.

If $G$ is profinite, the actions is cts iff $G = \bigcup_{U\leq G \text{ open}}M^U$, the union of its (open) invariants.

Profinite groups acting on discrete modules have finite orbits.
:::

::: {.front card-id="card-2ffce7da1f1ee84f"}
What does it mean to be topologically finitely generated?
:::

::: {.back card-id="card-2ffce7da1f1ee84f"}
There is a generating set $S$ such that the smallest closed subgroup of $G$ containing $S$ is $G$ itself.
:::

::: {.front card-id="card-84753f6c4a8ee634"}
Is $H\leq G$ finite index iff open?
:::

::: {.back card-id="card-84753f6c4a8ee634"}
Open $\implies$ finite index, but not conversely.

Converse is true if $G$ is topologically finitely generated.

$\iff$ holds when $G$ is strongly complete.
:::

::: {.front card-id="card-ae7e6fa40cd013a1"}
Show that functions into a discrete space are locally constant.
:::

::: {.back card-id="card-ae7e6fa40cd013a1"}
The fibers must be open sets
:::

::: {.front card-id="card-3fe02311cc766f48"}
Show that $f:X\to Y$ with $X$ profinite and $Y$ discrete must have finite image.
:::

::: {.back card-id="card-3fe02311cc766f48"}
$X$ is compact and partitioned into open fibers, thus finitely many fibers.
:::

::: {.front card-id="card-e8df8f7e71d5095e"}
Discuss commuting limits for profinite groups.
:::

::: {.back card-id="card-e8df8f7e71d5095e"}
If $G$ is profinite and $Y$ is discrete, $f:G\to Y$ factors through a finite quotient $\tilde f: G/U\to Y$ and so
$${\mathsf{Top}}(G, Y) = {\mathsf{Top}}(\lim G/N, Y) = \colim {\mathsf{Top}}(G/N, Y)$$
:::

::: {.front card-id="card-daafc2582fc47c4e"}
What are continuous cochains?
:::

::: {.back card-id="card-daafc2582fc47c4e"}
$K_\text{cts}^n(G; M) \coloneqq{\mathsf{Top}}(G{ {}^{ \scriptscriptstyle\times^{n} }  }, M)$.
:::

::: {.front card-id="card-e23d5e0a1a45b10f"}
Discuss continuity for profinite group cohomology.
:::

::: {.back card-id="card-e23d5e0a1a45b10f"}
$H^n(\cocolim G_i; \colim M_i) \cong \colim H^n(G_i; M_i)$.

In particular $H^n(G; A)=\colim_U H^n(G/U; A^U)$ using that $U_2\hookrightarrow U_1 \implies G/U_1 \twoheadrightarrow G/U_2$ (inflation).
:::

::: {.front card-id="card-a0e7561b884f9ba2"}
Discuss limits for Galois cohomology.
:::

::: {.back card-id="card-a0e7561b884f9ba2"}
For $g_K \coloneqq{ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k)$ and $A\in   {}_{g_K}{\mathsf{Mod}}$ write $A(L) \coloneqq A^{g_L}$, then
$$H^1(g_U; A) = \colim_{L/K} H^n({ \mathsf{Gal}}(L/K); A(L))$$
:::

::: {.front card-id="card-3e262f5d983331a0"}
Write a module as a limit.
:::

::: {.back card-id="card-3e262f5d983331a0"}
$A =\colim_{B\leq A \text{ f.g.}} B$; i.e. every module is a colimit of its finitely generated submodules.
:::

::: {.front card-id="card-4a35203ca016760c"}
Discuss higher profinite cohomology.
:::

::: {.back card-id="card-4a35203ca016760c"}
$H^{\geq 1}(G; A)\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\operatorname{tors}}$ is always torsion.

Proof: $H^q(G; A) = \colim H^q(G/U; A^U) = \colim H^q(G/U; A^u)[n]$ for $n \coloneqq[G: U]$ by restriction-corestriction, and ${}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\operatorname{tors}}$ is closed under colimits.
:::

::: {.front card-id="card-095230d6aa734d77"}
What is $H^q(K; M)$ for $K\in \mathsf{Field}$?
:::

::: {.back card-id="card-095230d6aa734d77"}
$H^q({ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k); M)$ the profinite group cohomology.
:::

::: {.front card-id="card-63e5e2b2fef8dfc0"}
What is the Weil-Chatelet group $\mathrm{WC}(A/K)$?
:::

::: {.back card-id="card-63e5e2b2fef8dfc0"}
For $A\in{\mathsf{Grp}}{\mathsf{Sch}}$ commutative, or $A$ any commutative group, $H^1(K; A)\coloneqq H^1({ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k); A(k^{ {}^{ \operatorname{sep} } }))$.
:::

::: {.front card-id="card-6ed7fecddc2418ed"}
What is the relative Galois cohomology $H^n(L/K; A)$?
:::

::: {.back card-id="card-6ed7fecddc2418ed"}
$\ker\qty{H^n(K; M) \to H^n(L; M)}$.
:::

::: {.front card-id="card-fe6430fdbe903e0a"}
Define a Galois extension.
:::

::: {.back card-id="card-fe6430fdbe903e0a"}
Algebraic, normal, separable.
:::

::: {.front card-id="card-570ae19fe569a383"}
What is $H^n({ \mathsf{Gal}}(L/K); L)$?
:::

::: {.back card-id="card-570ae19fe569a383"}
Zero for $n\geq 1$; "additive" Hilbert 90 since $\implies H^n(K; {\mathbf{G}}_a) = 0$.
:::

::: {.front card-id="card-228e5547c91384fb"}
What is the normal basis theorem?
:::

::: {.back card-id="card-228e5547c91384fb"}
For $L/K$ Galois, $\exists \alpha\in L$ such that $G_{L/K}.\alpha$ generates $L\in   {}_{K}{\mathsf{Mod}}$.

For $G\coloneqq G_{L/K}$, iff $L \cong K[G] \in   {}_{K[G]}{\mathsf{Mod}}$, so rank 1 with generator $\alpha$.

Iff $L\cong {\mathbf{Z}}[G]\otimes_{\mathbf{Z}}K \in   {}_{{\mathbf{Z}}[G]}{\mathsf{Mod}}$, so $L$ is induced.
:::

::: {.front card-id="card-2fc69737d44e07a9"}
What is Hilbert 90?
:::

::: {.back card-id="card-2fc69737d44e07a9"}
For $L/K$ Galois, $G = { \mathsf{Gal}}(L/K)$,
$$H^1(G; L^{\times}) = 0$$
This is false for $q\gt 1$!

Think of this as $H^1(G; {\mathbf{G}}_m) = 0$.
:::

::: {.front card-id="card-27a39505ab4a8c1b"}
What is $\mathrm{Br}(K)$?
:::

::: {.back card-id="card-27a39505ab4a8c1b"}
$\mathrm{Br}(K) \coloneqq H^2(K; {\mathbf{G}}_m)$.
:::

::: {.front card-id="card-dfccee2093478cfd"}
What is classical Hilbert 90?
:::

::: {.back card-id="card-dfccee2093478cfd"}
For $L/K$ finite cyclic Galois with $G_{L/K} = \left\langle{\sigma}\right\rangle$,

For $\alpha\in L$, $\operatorname{Trace}_{L/K}(\alpha) = 0 \iff \exists \lambda\in L$ such that $\alpha = \lambda - \sigma(\lambda)$.

Why: $0 = H^1(G;L) = \widehat{H}^{-1}(G; L) = \widehat{H}_0(G; L) = \ker(N: L\to K)/(\sigma - 1)L$ but here $N$ is the sum of Galois conjugates, hence the trace

$\operatorname{Trace}_{L/K}(\alpha) = 1 \iff \exists \lambda \in L$ such that $\alpha = \lambda/\sigma(\lambda)$.

Why: $0 = H^1(G; L^{\times}) = \widehat{H}^0(G; L^{\times})=\ker(N)/ (\sigma-1)L$ multiplicatively.
:::

::: {.front card-id="card-19dda55760e13c46"}
Discuss Kummer theory for ${\mathbf{G}}_m$.
:::

::: {.back card-id="card-19dda55760e13c46"}
Set $\mu_n = (k^{ {}^{ \operatorname{sep} } })^{\times}[n]$, then $H^1(k; \mu_n) = k^{\times}/(k^{\times})^n$, where these are $n$th powers.

Proof: LES for $\mu_n\hookrightarrow(k^{ {}^{ \operatorname{sep} } })^{\times}\twoheadrightarrow(k^{ {}^{ \operatorname{sep} } })^{\times}$ and apply Hilbert 90.

If $K$ contains an $n$th root of unity, $\mu_n = C_n$ has trivial $G_K{\hbox{-}}$ action and $H^1(K; \mu_n) = \mathop{\mathrm{Hom}}(g_K, C_n)$.
:::

::: {.front card-id="card-53eab47f7ef628ba"}
What is the Pontryagin dual?
:::

::: {.back card-id="card-53eab47f7ef628ba"}
$G {}^{ \vee }\coloneqq{\mathsf{Top}}(G, {\operatorname{U}}_1)$ with the compact-open topology, for $G$ a locally compact abelian topological group.

Duality: profinite abelian groups $\rightleftharpoons$ discrete torsion abelian groups (

So limits of finite discrete groups vs colimits

Generalizes $G$ isomorphic to its character group
:::

::: {.front card-id="card-af6028d38b5cb858"}
What is $({\operatorname{U}}_1)_{\operatorname{tors}}$?
:::

::: {.back card-id="card-af6028d38b5cb858"}
${\mathbf{Q}}/{\mathbf{Z}}$, the group of all roots of unity.
:::

::: {.front card-id="card-a5d289a805257b70"}
How does one interpret $K^{\times}/(K^{\times})^n$.
:::

::: {.back card-id="card-a5d289a805257b70"}
$K^{\times}/(K^{\times})^n \cong g_K^{{\operatorname{ab}}, n}$ the Galois group of the maximal abelian extension of $K$ with exponent $n$.
:::

::: {.front card-id="card-3b96ac4266574cb6"}
What is the issue with Kummer theory?
:::

::: {.back card-id="card-3b96ac4266574cb6"}
In positive characteristic $p$, need $n$ prime to $p$ to consider $H^1(k; \mu_n)$.

Need
:::

::: {.front card-id="card-2d0a3d1a30e63ef3"}
What is Artin-Schreier theory?
:::

::: {.back card-id="card-2d0a3d1a30e63ef3"}
Characteristic $p$ analogue of Kummer theory.

Want an analogue for cyclic extensions of prime power order $p^k$, AS works for $k=1$.
:::

::: {.front card-id="card-9f8fd98a972d6eaf"}
How is Artin-Schreier theory expressed cohomologically?
:::

::: {.back card-id="card-9f8fd98a972d6eaf"}
Take $\phi \coloneqq\operatorname{Frob}- 1$ so $\phi(x) = x^p-x$, this is an isogeny of ${\mathbf{G}}_a$ so get a SES ${ \mathbf{F} }_p\hookrightarrow k^{ {}^{ \operatorname{sep} } } \xrightarrow[]{\phi} { \mathrel{\mkern-16mu}\rightarrow }\,  k^{ {}^{ \operatorname{sep} } }$.

Take LES, use additive Hilbert 90 to get $\mathop{\mathrm{Hom}}(g_k, { \mathbf{F} }_p) \cong k/\phi(k)$.

This says $(g_k^{{\operatorname{ab}}, p}) {}^{ \vee }= k/\phi(k)$.

Generalizes to $(g_k^{{\operatorname{ab}}, p^n}) = W_n(k)/ \phi(W_n(k))$ for $W_n$ the length $n$ Witt vectors.
:::

::: {.front card-id="card-c9837b1d36c43ff6"}
What is $W_n(k)$?
:::

::: {.back card-id="card-c9837b1d36c43ff6"}
As a scheme, ${\mathbf{G}}_a{ {}^{ \scriptscriptstyle\times^{n} }  }$, but what a twisted group law.
:::

::: {.front card-id="card-56812a42bf98ef46"}
What is the relative Brauer group?
:::

::: {.back card-id="card-56812a42bf98ef46"}
$\mathrm{Br}(L/K) \coloneqq H^2({ \mathsf{Gal}}(L/K); L^{\times})$.
:::

::: {.front card-id="card-8961c453a837af89"}
What is $\operatorname{cohdim}G$?
:::

::: {.back card-id="card-8961c453a837af89"}
$\sup_{p \in \operatorname{Spec}{\mathbf{Z}}} \operatorname{cohdim}_p G$ where $\operatorname{cohdim}_p G$ is the least $d$ such that for all $n\geq d$ and for all discrete torsion $A\in   {}_{G}{\mathsf{Mod}}$, one has $H^n(G; A[p^\infty]) = 0$.
:::

::: {.front card-id="card-3886538b2e514584"}
What is $\operatorname{cohdim}C_p$?
:::

::: {.back card-id="card-3886538b2e514584"}
$\operatorname{cohdim}_\ell C_p =0$ if $p\neq \ell$ and $\infty$ if $p=\ell$, so $\operatorname{cohdim}C_p = \infty$.
:::

::: {.front card-id="card-0bd0a971ed2aeda5"}
Discuss $\operatorname{cohdim}G$ for $G$ a pro${\hbox{-}}p$ group.
:::

::: {.back card-id="card-0bd0a971ed2aeda5"}
$\operatorname{cohdim}_p G \leq n \iff H^{n+1}(G; C_p) = 0$.
:::

::: {.front card-id="card-1f3689519ae590a6"}
Write $\mathsf{pro}{\mathbf{Z}}$ as a product.
:::

::: {.back card-id="card-1f3689519ae590a6"}
$$\mathsf{pro}{\mathbf{Z}}= \cocolim C_n = \cocolim \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} C_{p_i^{k_i}} = \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} \cocolim C_{p_i^{k_i}} = \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} { {\mathbf{Z}}_{\widehat{p}} }$$
:::

::: {.front card-id="card-65cd3d53082ae059"}
What is ${\operatorname{Syl}}_p (\mathsf{pro}{\mathbf{Z}})$?
:::

::: {.back card-id="card-65cd3d53082ae059"}
Uniquely ${ {\mathbf{Z}}_{\widehat{p}} }$.
:::

::: {.front card-id="card-b06e08a3e7103026"}
What is $\operatorname{cohdim}{ {\mathbf{Z}}_{\widehat{p}} }$?
:::

::: {.back card-id="card-b06e08a3e7103026"}
$\operatorname{cohdim}{ {\mathbf{Z}}_{\widehat{p}} }= 1$.

Why: $H^2({ {\mathbf{Z}}_{\widehat{p}} }; C_p) = 0$ and $H^1({ {\mathbf{Z}}_{\widehat{p}} }; C_p) = \mathop{\mathrm{Hom}}({ {\mathbf{Z}}_{\widehat{p}} }, C_p) = C_p$.
:::

::: {.front card-id="card-e3b30a624c45bf53"}
What is $\operatorname{cohdim}(\mathsf{pro}{\mathbf{Z}})$?
:::

::: {.back card-id="card-e3b30a624c45bf53"}
$\operatorname{cohdim}(\mathsf{pro}{\mathbf{Z}}) = 1$ since $\operatorname{cohdim}_p({ {\mathbf{Z}}_{\widehat{p}} }) = 1$ for all primes $p$ and $\operatorname{cohdim}_p G = \operatorname{cohdim}_p G_p$ for $G_p$ a Sylow $p{\hbox{-}}$subgroup.
:::

::: {.front card-id="card-388130dd5c67f1b1"}
Compare $G_L$ and $G_K$ for $L/K$ an extension.
:::

::: {.back card-id="card-388130dd5c67f1b1"}
$G_L\hookrightarrow G_K$ as a closed subgroup.
:::

::: {.front card-id="card-9533eaca3452aa02"}
What is the inflation/restriction sequence for Brauer groups?
:::

::: {.back card-id="card-9533eaca3452aa02"}
$\mathrm{Br}(L/K)\xhookrightarrow{\mathrm{inflation}} \mathrm{Br}(K) \xrightarrow{\mathrm{restriction}} \mathrm{Br}(L)^{{ \mathsf{Gal}}(L/K)}$.
:::

::: {.front card-id="card-cc76cd508bd43e53"}
How do you interpret $\mathrm{Br}(L/K)$?
:::

::: {.back card-id="card-cc76cd508bd43e53"}
Elements of $\mathrm{Br}(K)$ that are annihilated by restriction to $\mathrm{Br}(L)$.
:::

::: {.front card-id="card-ae492cb6a89e0aa8"}
What is $H^2(K; \mu_n)$?
:::

::: {.back card-id="card-ae492cb6a89e0aa8"}
$H^2(K; \mu_n) = \mathrm{Br}(K)[n]$.
:::

::: {.front card-id="card-07975ce6c91081cd"}
What is an etale group scheme?
:::

::: {.back card-id="card-07975ce6c91081cd"}
Idea: for $G$, lose no information by considering $G(k^{ {}^{ \operatorname{sep} } })\in   {}_{G_k}{\mathsf{Mod}}$.
:::

::: {.front card-id="card-0fa66696121a93e0"}
What is $\mathrm{Br}({\mathbf{R}})$? Sketch a proof.
:::

::: {.back card-id="card-0fa66696121a93e0"}
Classified finite dimensional central simple division algebras.

$\mathrm{Br}({\mathbf{R}}) \cong C_2 \left\langle{{\mathbf{R}}, {\mathbb{H}}}\right\rangle$ where $\dim_{\mathbf{R}}{\mathbb{H}}= 4$ is the Hamilton quaternions.

Proof: $\mathrm{Br}({\mathbf{R}}) = \widehat{H}^0(\mathop{\mathrm{Aut}}({\mathbf{C}}/{\mathbf{R}}); {\mathbf{C}}^{\times}) = {\mathbf{R}}^{\times}/N{\mathbf{C}}^{\times}= {\mathbf{R}}^{\times}/{\mathbf{R}}_{\gt 0} = C_2$.
:::

::: {.front card-id="card-d7379378881c9532"}
Describe $\operatorname{Nm}: { \mathbf{F} }_{q^n} \to { \mathbf{F} }_q$.
:::

::: {.back card-id="card-d7379378881c9532"}
$\operatorname{Nm}(x) = x \cdot x^q \cdot x^{q^2}\cdots x^{q^{n-1}} = x^{[n]_q}$, the q-binomial $[n]_q \coloneqq{q^n-1\over q-1}$.
:::

::: {.front card-id="card-ed6fc5f2467c56da"}
What is $\mathrm{Br}({ \mathbf{F} }_q)$? What is the interpretation?
:::

::: {.back card-id="card-ed6fc5f2467c56da"}
$\mathrm{Br}({ \mathbf{F} }_q) = 0$; every finite division algebra is a field.

True because inflations are injective, ${ \mathsf{Gal}}({ \mathbf{F} }_{q^n}/{ \mathbf{F} }_q) = \left\langle{\operatorname{Frob}_q}\right\rangle$, and $\widehat{H}^0(\left\langle{\operatorname{Frob}_q}\right\rangle; { \mathbf{F} }_{q^n}^{\times}) = { \mathbf{F} }_q^{\times}/N{ \mathbf{F} }_{q^n}^{\times}= 0$ since the norm is surjective on finite fields.
:::

::: {.front card-id="card-ff081ebce96f915a"}
Characterize procyclic groups.
:::

::: {.back card-id="card-ff081ebce96f915a"}
Quotients of $\mathsf{pro}{\mathbf{Z}}$ by closed subgroups.
:::

::: {.front card-id="card-692232f75a34b981"}
What is a $C_1$ field?
:::

::: {.back card-id="card-692232f75a34b981"}
All homogeneous polynomials $f\in k[x_1,\cdots, x_n]$ of degree $d < n$ have a nonzero root in $k$.
:::

::: {.front card-id="card-68e86873bda3a8fc"}
What is the Chevalley-Warning theorem?
:::

::: {.back card-id="card-68e86873bda3a8fc"}
${ \mathbf{F} }_q$ is a $C_1$ field.
:::

::: {.front card-id="card-af37691e18301572"}
What is Tsen's theorem?
:::

::: {.back card-id="card-af37691e18301572"}
If $k ={ \overline{k} }$ and ${\mathrm{trdeg}}(L/k)=1$ then $L$ is a $C_1$ field.

In particular, $k(C)$ the function field of a curve over $k={ \overline{k} }$ is $C_1$.
:::

::: {.front card-id="card-6c6248f50912e197"}
What is Lang's theorem?
:::

::: {.back card-id="card-6c6248f50912e197"}
Is $K$ is a complete discretely valued field with algebraically closed residue field, then $K$ is a $C_1$ field.
:::

::: {.front card-id="card-7a6c44e233582a4d"}
What is $\mathrm{Br}(K)$ for $K$ a $C_1$ field?
:::

::: {.back card-id="card-7a6c44e233582a4d"}
$\mathrm{Br}(K) = 0$.
:::

::: {.front card-id="card-8e2cb08e735bc212"}
Discuss the decomposition of $\mathrm{Br}(K)$ for $K$ a CDVR with perfect residue field $k$.
:::

::: {.back card-id="card-8e2cb08e735bc212"}
$\mathrm{Br}(K) = \mathrm{Br}(k) \oplus \mathop{\mathrm{Hom}}(g_k, {\mathbf{Q}}/{\mathbf{Z}})$.

If $k$ is finite, $\mathrm{Br}(K) = {\mathbf{Q}}/{\mathbf{Z}}$.
:::

::: {.front card-id="card-766c454787487177"}
Discuss limits of $C_n$.
:::

::: {.back card-id="card-766c454787487177"}
$\colim C_n = {\mathbf{Q}}/{\mathbf{Z}}$

$\cocolim C_n = \mathsf{pro}{\mathbf{Z}}$.
:::

::: {.front card-id="card-10d1272606dd6f30"}
What is the characteristic property of unramified extensions?
:::

::: {.back card-id="card-10d1272606dd6f30"}
For $L/K$ with residue fields $l/k$, ${ \mathsf{Gal}}(L/K)\twoheadrightarrow{ \mathsf{Gal}}(l/k)$ is an isomorphism.
:::

::: {.front card-id="card-8fd920f18e320d3c"}
For a decreasing filtration $M_1 \supseteq M_2\supseteq\cdots$, what does it mean for $M_1$ to be complete and separated for the $M_i{\hbox{-}}$adic topology?
:::

::: {.back card-id="card-8fd920f18e320d3c"}
$M_1\to \cocolim M_1/M_n$ is an isomorphism, realizing $M_1$ as an adic completion wrt the quotients.
:::

::: {.front card-id="card-ecbf81a3501e47c7"}
What is a residual extension?
:::

::: {.back card-id="card-ecbf81a3501e47c7"}
For $L/K$ with residue fields $l$ and $k$ respectively, the extension of residue fields $l/k$.
:::

::: {.front card-id="card-9b48c86ec18ac71d"}
What are the higher unit groups of a local field $L$?
:::

::: {.back card-id="card-9b48c86ec18ac71d"}
$U^n(L) \coloneqq\left\{{x\in R(L) {~\mathrel{\Big\vert}~}v(x-1)\geq n}\right\}$ where $R(L)$ is the valuation ring.

Can write as $1 + {\mathfrak{m}}^n$.
:::

::: {.front card-id="card-fce84017162b3b45"}
What is the profinite index of $H\leq G$ a closed subgroup of a profinite group
:::

::: {.back card-id="card-fce84017162b3b45"}
$[G: H] = \operatorname{lcm}_{U\supseteq H \text{ open}} [G:U]$.
:::

::: {.front card-id="card-62ca6a4845ff33f7"}
What is the virtual cohomology dimension?
:::

::: {.back card-id="card-62ca6a4845ff33f7"}
$\mathrm{vcohdim}_p(G) \coloneqq\inf_{U \leq G \text{ open}}\operatorname{cohdim}_p(U)$, and $\mathrm{vcohdim}(G) \coloneqq\sup_p \mathrm{vcohdim}_p(G)$.
:::

::: {.front card-id="card-04eb0883ac6aed5c"}
What explains $\mathrm{vcohdim}_p G < \infty$ but $\operatorname{cohdim}_p G = \infty$?
:::

::: {.back card-id="card-04eb0883ac6aed5c"}
The presence of elements of finite order $p$.

Theorem of Serre: if $G$ is profinite with no elements of order $p$, for all $U\leq G$ open, $\operatorname{cohdim}_p U = \operatorname{cohdim}_p G$.
:::

::: {.front card-id="card-4618648279592873"}
What is a virtually torsionfree group?
:::

::: {.back card-id="card-4618648279592873"}
$\exists U\leq G$ open (thus finite index) which is torsionfree.
:::

::: {.front card-id="card-ace67f214e73cf15"}
What does "virtually" having a property $P$ mean?
:::

::: {.back card-id="card-ace67f214e73cf15"}
Admitting some finite index subgroup which has property $P$.
:::

::: {.front card-id="card-5f4e3322c228111a"}
When is $M\in {\mathsf{Fin}} {}_{{\mathbf{Z}}}{\mathsf{Mod}}$ a product of its Sylow subgroups?
:::

::: {.back card-id="card-5f4e3322c228111a"}
Iff nilpotent.
:::

::: {.front card-id="card-58c10e687053fd85"}
What is the structure theory of $\mathsf{pro}{\mathsf{Ab}}{\mathsf{Grp}}^{{\mathsf{Top}}{\hbox{-}}{\mathrm{fg}}}$?
:::

::: {.back card-id="card-58c10e687053fd85"}
$G = \prod G_p$ is a product of Sylow $p{\hbox{-}}$subgroups.

If $G$ is pro${\hbox{-}}p$, then $G\cong { {\mathbf{Z}}_{\widehat{p}} }{ {}^{ \scriptscriptstyle\oplus^{\mathrm{v}\operatorname{cohdim}(G)} }  } \oplus G_{\operatorname{tors}}$ where ${\sharp}G_{{\operatorname{tors}}} < \infty$.
:::

::: {.front card-id="card-eb8e491195492d06"}
Define a local field.
:::

::: {.back card-id="card-eb8e491195492d06"}
Complete DVR, a field, with finite residue field.
:::

::: {.front card-id="card-521ced20606cb4e1"}
What is the valuation ring of a DVF $K$?
:::

::: {.back card-id="card-521ced20606cb4e1"}
$R(K) = v^{-1}([0, \infty])$
:::

::: {.front card-id="card-aa139882c510b936"}
Give equivalent conditions for a field $K$ to be a DVF
:::

::: {.back card-id="card-aa139882c510b936"}
$K$ is locally compact.

The valuation ring $R(K)$ is compact.

${\mathbf{G}}_a(R(K))$ is a profinite group (since compact and totally disconnected).

$K$ is complete and the residue field $\kappa(K) \coloneqq R(K)/{\mathfrak{m}}$ is a finite field.
:::

::: {.front card-id="card-1109d37fbb1e4a7b"}
Discuss characteristic zero local fields $K$.
:::

::: {.back card-id="card-1109d37fbb1e4a7b"}
$K \in   {}_{{ {\mathbf{Q}}_p }}{\mathsf{Mod}}^{\mathrm{fd}}$ canonically

${\mathbf{Q}}\hookrightarrow K$ with ${ \operatorname{cl}}^{\mathsf{Top}}_K({\mathbf{Q}}) ={ {\mathbf{Q}}_p }$ and $[K: { {\mathbf{Q}}_p }] = e\cdot f$ where...

$\kappa = { \mathbf{F} }_{p^f}$ is the residual degree

$e = e(K/{ {\mathbf{Q}}_p }) = v(p)$ where $p\coloneqq\operatorname{ch}\kappa$.
:::

::: {.front card-id="card-aa39b93824571d7c"}
Give an example of a totally ramified extension.
:::

::: {.back card-id="card-aa39b93824571d7c"}
${ \mathbf{F} }_q(\hspace{-0.25em}( t^{1\over n} )\hspace{-0.22em})$ over ${ \mathbf{F} }_q(\hspace{-0.25em}( t )\hspace{-0.22em})$.
:::

::: {.front card-id="card-8bb26ae43d3b8576"}
Discuss the Galois theory of ${ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k)$ for $k$ local of positive characteristic $p$.
:::

::: {.back card-id="card-8bb26ae43d3b8576"}
$k^{\scriptscriptstyle\mathrm{un}}/k$ has ramification index 1, so unramified extensions correspond to extensions of the residue field, and so ${ \mathsf{Gal}}(k^{\scriptscriptstyle\mathrm{un}}/k) \cong { \mathsf{Gal}}(\overline{{ \mathbf{F} }}_q/{ \mathbf{F} }_q) \cong \mathsf{pro}{\mathbf{Z}}$.

$k^{\mathrm{tame}}$ has ramification indices all prime to $p$, $k^{\mathrm{tame}}/k^{\scriptscriptstyle\mathrm{un}}$ corresponds to taking $\pi^{1\over n}$.

$I \coloneqq\mathop{\mathrm{Aut}}(k^{ {}^{ \operatorname{sep} } }/k^{\scriptscriptstyle\mathrm{un}}) = \ker(g_k \twoheadrightarrow g_{{ \mathbf{F} }_q})$ is the inertia group

$I_p$ is the wild ramification, the Sylow $p{\hbox{-}}$subgroup of $I$.
:::

::: {.front card-id="card-1db1d625e8452bf6"}
Define the higher unit groups.
:::

::: {.back card-id="card-1db1d625e8452bf6"}
For $R$ the valuation ring, define $r_n: R\twoheadrightarrow R/{\mathfrak{m}}^n$.

In this special case, the induced map $r_n^{\times}: R^{\times}\to (R/{\mathfrak{m}}^n)^{\times}$ is surjective

Define $U_n \coloneqq\ker r_n^{\times}= 1 + {\mathfrak{m}}^n$, so units that are trivial modulo ${\mathfrak{m}}^n$.

Can use $p{\hbox{-}}$adic logarithm to get an isomorphism $U_n { \, \xrightarrow{\sim}\, }{\mathfrak{m}}^n$.
:::

::: {.front card-id="card-1f124014b7ebda6c"}
What does local class field theory say about the maximal abelian extension of a local field $K$?
:::

::: {.back card-id="card-1f124014b7ebda6c"}
Isomorphic to $\mathsf{pro}{\mathbf{G}}_m(K) \cong \mathsf{pro}{\mathbf{Z}}\times U(K)$, so the unit group gives most of the information.
:::

::: {.front card-id="card-402c1ba1d41cc1ca"}
What is the normal basis theorem?
:::

::: {.back card-id="card-402c1ba1d41cc1ca"}
For $L/K$ Galois, ${\exists}\alpha\in L$ such that $L = \left\langle{G_{L/K}.\alpha}\right\rangle_K \in   {}_{K}{\mathsf{Mod}}$.

Equivalently, ${\mathbf{G}}_a(K) \cong K[G] \in   {}_{K[G]}{\mathsf{Mod}}$ for $G\coloneqq{ \mathsf{Gal}}(L/K)$.
:::

::: {.front card-id="card-54368a00e14742d7"}
For $G = \mathop{\mathrm{Aut}}(L/K)\in{\mathsf{Fin}}{\mathsf{Grp}}$ cyclic, what is $K^{\times}/N L^{\times}$?
:::

::: {.back card-id="card-54368a00e14742d7"}
${\sharp}K^{\times}/N L^{\times}= [L: K]$.
:::

::: {.front card-id="card-66baf534cd2f7009"}
What is ${ \mathsf{Gal}}(K^{\scriptscriptstyle\mathrm{un}}/K)$?
:::

::: {.back card-id="card-66baf534cd2f7009"}
${ \mathsf{Gal}}(K^{\scriptscriptstyle\mathrm{un}}/K)\cong { \mathsf{Gal}}(\overline{\kappa}/\kappa) = \mathsf{pro}{\mathbf{Z}}$.
:::

::: {.front card-id="card-14239b3b335fdb91"}
What is the unit group SES?
:::

::: {.back card-id="card-14239b3b335fdb91"}
$U\hookrightarrow K^{\times} \xrightarrow[]{v} { \mathrel{\mkern-16mu}\rightarrow }\,  {\mathbf{Z}}$.
:::

::: {.front card-id="card-3db412aa9ca534fb"}
What is the invariant map?
:::

::: {.back card-id="card-3db412aa9ca534fb"}
$\mathrm{inv}_K: \mathrm{Br}(K)  { \, \xrightarrow{\sim}\, }{\mathbf{Q}}/{\mathbf{Z}}$ for $K$ a local field.
:::

::: {.front card-id="card-63d9dec15c450fea"}
For $L/K$, what is the induced restriction map on Brauer groups? Corestriction?
:::

::: {.back card-id="card-63d9dec15c450fea"}
$\mathrm{Res}^{K}_{L}: \mathrm{Br}(K) \to \mathrm{Br}(L)$ is $\cdot n: {\mathbf{Q}}/{\mathbf{Z}}\to {\mathbf{Q}}/{\mathbf{Z}}$ where $n \coloneqq[L: K]$.

Corestriction is the identity.
:::

::: {.front card-id="card-523977123bb2324a"}
What is $\mathrm{Br}(L/K)$ for $L/K$ a finite extension?
:::

::: {.back card-id="card-523977123bb2324a"}
$\mathrm{Br}(L/K) = \mathrm{Br}(K)[n]$ for $n\coloneqq[L: K]$.
:::

::: {.front card-id="card-153e8ee23c511946"}
What is the fundamental class? What is its significance?
:::

::: {.back card-id="card-153e8ee23c511946"}
$v_{L/K}\in \mathrm{Br}(L/K) = H^2(G_{L/K}; {\mathbf{G}}_m(L))$ the unique class where
$$\mathrm{inv}_K(v_{L/K}) = {1\over n} + {\mathbf{Z}}\in \qty{{1\over n} {\mathbf{Z}}}/{\mathbf{Z}}\subseteq {\mathbf{Q}}/{\mathbf{Z}}$$
Apply Tate-Nakayama to get
$$G^{\operatorname{ab}}= \widehat{H}^{-2}(G; {\mathbf{Z}}) \underset{{-}\smile v_{L/K}}{ { \, \xrightarrow{\sim}\, }} \widehat{H}^0(G; {\mathbf{G}}_m(L)) =K^{\times}/N L^{\times}$$
Yields $\omega_{L/K}: K^{\times}/NL^{\times} { \, \xrightarrow{\sim}\, }G^{\operatorname{ab}}$, so e.g. the norm map is surjective iff $G = G^{\operatorname{ab}}$ is abelian.

Alternatively, for abelian extensions, ${ \mathsf{Gal}}(L/K)  { \, \xrightarrow{\sim}\, }\operatorname{coker}N$.
:::

::: {.front card-id="card-6153b701f329a586"}
Discuss the significance of $\omega$.
:::

::: {.back card-id="card-6153b701f329a586"}
Isomorphisms of $\omega_{L/K}$ assemble into a compatible inverse system.

Yields $\omega: K^{\times}\to\cocolim_{L/K \text{ fin. ab}}K^{\times}/NL^{\times} { \, \xrightarrow{\sim}\, }G_K^{\operatorname{ab}}$, so is this injective? Is it the profinite completion of $K^{\times}$?

Equivalently, are there enough finite abelian extensions to be cofinal in the system of all finite index subgroups of $K^{\times}$?

$\omega(K^{\times}) \subseteq G_K^{\operatorname{ab}}$ is dense.
:::

::: {.front card-id="card-d2c81ce19310d677"}
What is $I_K^{\operatorname{ab}}$?
:::

::: {.back card-id="card-d2c81ce19310d677"}
$I_K^{\operatorname{ab}}= \mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K^{\scriptscriptstyle\mathrm{un}})\subseteq \mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K)$.
:::

::: {.front card-id="card-5f3ac63317a6e4d6"}
What is a projective profinite group?
:::

::: {.back card-id="card-5f3ac63317a6e4d6"}
$P$ is projective iff $\forall \pi: G\twoheadrightarrow P$ there is a section $\pi\circ s = \operatorname{id}_P$.

$\iff \operatorname{cohdim}P \leq 1$.

$\iff G_p$ is a free pro $p{\hbox{-}}$group.
:::

::: {.front card-id="card-79a859109812a9d2"}
Describe $\mathsf{pro}K^{\times}$.
:::

::: {.back card-id="card-79a859109812a9d2"}
$K^{\times}= U_K \times {\mathbf{Z}}$ since everything is a unit times a uniformizer, so

$\mathsf{pro}K^{\times}= U_K \times \mathsf{pro}{\mathbf{Z}}$.
:::

::: {.front card-id="card-365de60e896eb42f"}
What is the reciprocity map?
:::

::: {.back card-id="card-365de60e896eb42f"}
$\omega:\mathsf{pro}(K^{\times})\to G_K^{\operatorname{ab}}$; restricts to $U_K { \, \xrightarrow{\sim}\, }I_K^{\operatorname{ab}}$.
:::

::: {.front card-id="card-d0d01d2c0a99e93f"}
What is $N L^{\times}$ for $L/K$ unramified?
:::

::: {.back card-id="card-d0d01d2c0a99e93f"}
$U_K \subseteq NL^{\times}= \left\{{x\in K^{\times}{~\mathrel{\Big\vert}~}n\mathrel{\Big|}v(x)}\right\}$.
:::

::: {.front card-id="card-e565bc3ee54ccd7a"}
What is a proper map of profinite groups?
:::

::: {.back card-id="card-e565bc3ee54ccd7a"}
$f:X\to Y$ where $f\times \operatorname{id}_Z: X\times Z\to Y\times Z$ is closed for every $Z$.

$\iff f$ is closed with quasicompact fibers.

For $X$ Hausdorff and $Y$ locally compact, $\iff$ preimage of compact is compact.
:::

::: {.front card-id="card-16426ec4249da425"}
What is the Galois correspondence induced by the reciprocity map?
:::

::: {.back card-id="card-16426ec4249da425"}
Subextensions of $L/K$ $\rightleftharpoons$ open subgroups of $K^{\times}$ containing $NL^{\times}$ where $\omega^{-1}(M) \coloneqq N M^{\times}$ for such a subgroup $M$.
:::

::: {.front card-id="card-8ee9b56e0afe4adb"}
Interpret $\mathop{\mathrm{Hom}}(G, C_n)$.
:::

::: {.back card-id="card-8ee9b56e0afe4adb"}
The character group $\chi(\tilde G)$ where $\tilde G = G^{\operatorname{ab}}/(G^{\operatorname{ab}})^n$ is the maximal abelian quotient of exponent $n$.
:::

::: {.front card-id="card-94b46fb9af7d6bf3"}
What is the norm residue symbol / Hilbert symbol?
:::

::: {.back card-id="card-94b46fb9af7d6bf3"}
$(a, b)_n \coloneqq b \smile\delta(\chi_a)\in H^2(K; {\mathbf{G}}_m) = \mathrm{Br}(K)$ for $a,b\in K^{\times}$.

Here $\delta: K^{\times}/(K^{\times})^n  { \, \xrightarrow{\sim}\, }H^1(K; \mu_n)$ is the coboundary, which is an isomorphism by Kummer theory.

Yields a perfect pairing $({-}, {-})_n: (K^{\times}/ (K^{\times})^n){ {}^{ \scriptstyle\otimes_{}^{2} }  } \to {\mathbf{Q}}/{\mathbf{Z}}$.
:::

::: {.front card-id="card-0989d534d9332209"}
What is the Steinberg relation?
:::

::: {.back card-id="card-0989d534d9332209"}
$(a, 1-a)_n = 0$.
:::

::: {.front card-id="card-e5a0051674920341"}
What is the existence theorem for $p{\hbox{-}}$adic fields?
:::

::: {.back card-id="card-e5a0051674920341"}
If $U\leq K^{\times}$ is finite index then $\exists ! L$ a subextension of $\overline{K}/K$ such that $U = \operatorname{Nm}_{L/K} L^{\times}$.
:::

::: {.front card-id="card-55df79fb6dddfb6f"}
What is the main result concerning LCFT for $p{\hbox{-}}$adic fields?
:::

::: {.back card-id="card-55df79fb6dddfb6f"}
$\widehat{\omega}: \mathsf{pro}K^{\times} { \, \xrightarrow{\sim}\, }g_K^{\operatorname{ab}}$ is an isomorphism

$\omega: U_K { \, \xrightarrow{\sim}\, }I_K^{\operatorname{ab}}= { \mathsf{Gal}}(K^{\operatorname{ab}}/K^{\scriptscriptstyle\mathrm{un}})$, so we understand the totally ramified piece of $K^{ {}^{ \operatorname{sep} } }/K$.
:::

::: {.front card-id="card-dce455f2aa934948"}
Discuss Lubin-Tate theory.
:::

::: {.back card-id="card-dce455f2aa934948"}
A generalization of complex multiplication to local fields.

Constructs $K^{\operatorname{ab}}= K^{\scriptscriptstyle\mathrm{un}}(\cdots)$ where one adjoins torsion points of FGLs.
:::

::: {.front card-id="card-4502c07a8c557b29"}
What is CFT?
:::

::: {.back card-id="card-4502c07a8c557b29"}
Given a field $K$, find a topological group $G$ and an isomorphism $\mathsf{pro}G\to G_K$.
:::

::: {.front card-id="card-b5d2319946186416"}
What is local CFT?
:::

::: {.back card-id="card-b5d2319946186416"}
The reciprocity map $\omega: {\mathbf{G}}_m(K) \to G_K^{\operatorname{ab}}$ becomes an isomorphism after passing to the profinite completion.
:::

::: {.front card-id="card-2594d9e0a9390842"}
What is explicit class field theory?
:::

::: {.back card-id="card-2594d9e0a9390842"}
Since $K^{\operatorname{ab}}/K$ is a countably infinite degree algebraic extension, produce a sequence of algebraic numbers $a_n$ such that $K^{\operatorname{ab}}= \colim(K[a_1]\hookrightarrow K[a_1, a_2]\hookrightarrow\cdots)$.
:::

::: {.front card-id="card-ee8cd8706a6bd8a0"}
State Kronecker-Weber.
:::

::: {.back card-id="card-ee8cd8706a6bd8a0"}
${\mathbf{Q}}^{\operatorname{ab}}= {\mathbf{Q}}(\zeta_n {~\mathrel{\Big\vert}~}n\in {\mathbf{Z}}_{\geq 0})$.
:::

::: {.front card-id="card-259f06e97092cb5e"}
What is the mod $n$ cyclotomic character?
:::

::: {.back card-id="card-259f06e97092cb5e"}
$\chi_n: G_K\to C_n^{\times}$ induced by $G_K\curvearrowright K(\zeta_n)$, take inverse limit to obtain $\chi: G_K \to (\mathsf{pro}{\mathbf{Z}})^{\times}$.

The kernel always yields an abelian extension of $K$, the maximal cyclotomic extension (obtained by adjoining all roots of unity)
:::

::: {.front card-id="card-f6cdbc638824fec6"}
Discuss explicit CFT for imaginary quadratics.
:::

::: {.back card-id="card-f6cdbc638824fec6"}
For $E/k$ with ${\mathcal{O}}_K{\hbox{-}}$CM, get $\rho_N: G_K \to \mathop{\mathrm{Aut}}E[N] \cong \operatorname{GL}_1(C_N)$.

Completes to $\rho: G_K \to \operatorname{GL}_1(\mathsf{pro}{\mathbf{Z}})$.

Check $E[N]$ is a rank 2 $C_N$ module but a rank 1 ${\mathcal{O}}_K/N$ module.

Get $\rho_N: G_K \to \operatorname{GL}_1({\mathcal{O}}_K/N)$ which completes to $\rho: G_K \to \operatorname{GL}_1(\mathsf{pro}{\mathcal{O}}_K)$.

Take $\psi: G_K \to \mathsf{pro}{\mathcal{O}}_K^{\times}\to \mathsf{pro}{\mathcal{O}}_K^{\times}/{\mathcal{O}}_K^{\times}$ to get $K^{\ker \psi} = K^{\operatorname{ab}}$.

So for $K$, write down $E/K$ with CM by ${\mathcal{O}}_K$ and get $K^{\operatorname{ab}}= K(x(p) {~\mathrel{\Big\vert}~}p\in E[{\operatorname{tors}}])$, the $x{\hbox{-}}$coordinates of torsion points.
:::

::: {.front card-id="card-8c5d2b136e0764af"}
For $R$ the valuation ring of $K$, $U$ doesn't give $K^{\operatorname{ab}}$. Why? What does?
:::

::: {.back card-id="card-8c5d2b136e0764af"}
$\mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K) = U \times\mathsf{pro}{\mathbf{Z}}$, so $U$ only gives the totally ramified part.
:::

::: {.front card-id="card-30d9359488c1df16"}
What does $f = g + { \mathsf{O}}(k)$ mean?
:::

::: {.back card-id="card-30d9359488c1df16"}
$f\equiv g \in k{\llbracket x_1,\cdots, x_n \rrbracket  }/\left\langle{x_1,\cdots,x_n}\right\rangle^k$, so equal up to terms of order $k$.
:::

::: {.front card-id="card-f33d6daf6119c6ba"}
When can power series be substituted into each other?
:::

::: {.back card-id="card-f33d6daf6119c6ba"}
When the constant term is zero, e.g. $e^{e^x}$ has infinitely many constant terms.
:::

::: {.front card-id="card-9c31c990452572db"}
What is a formal group law?
:::

::: {.back card-id="card-9c31c990452572db"}
Associativity: $F(F(x,y), z) = F(x, F(y,z))$

Identities: $F(x, 0) = x$ and $F(0, y) = y$.

Inverses: $\exists !\iota \in R{\llbracket t \rrbracket  }$ such that $F(x, \iota(x)) = 0$.
:::

::: {.front card-id="card-6ab20a703009190d"}
How does one get an honest group from a FGL?
:::

::: {.back card-id="card-6ab20a703009190d"}
Take $(R, {\mathfrak{m}})$ complete local, then $R { \, \xrightarrow{\sim}\, }\cocolim_n R/{\mathfrak{m}}^n$ so $x+y \coloneqq F(x,y)$ converges in the ${\mathfrak{m}}{\hbox{-}}$adic topology.
:::

::: {.front card-id="card-37578c7420249421"}
What is the multiplicative formal group?
:::

::: {.back card-id="card-37578c7420249421"}
$F(x,y) = x + y + xy = (x+1)(y+1) - 1$.
:::

::: {.front card-id="card-054429efc3a37b22"}
What is a formal $R{\hbox{-}}$module?
:::

::: {.back card-id="card-054429efc3a37b22"}
A ring morphism $R\to { \operatorname{End} }_{\fgl}(F)$ for $F$ a formal group.
:::

::: {.front card-id="card-ad2d11d11ca5cd23"}
What is $[n](T)$ for ${\mathbf{G}}_a$ and ${\mathbf{G}}_m$, where $[n] \in { \operatorname{End} }_{\fgl}(F)$ is $1 \oplus_F 1\oplus_F \cdots \oplus_F 1$?
:::

::: {.back card-id="card-ad2d11d11ca5cd23"}
$[n](T) =nT$ for ${\mathbf{G}}_a$.

$[n](T) = (T+1)^n - 1$ for ${\mathbf{G}}_m$.
:::

::: {.front card-id="card-e9e25b1747d58f6c"}
What is $\operatorname{ht}{\mathbf{G}}_m$ in characteristic zero?
:::

::: {.back card-id="card-e9e25b1747d58f6c"}
Height 1
:::

::: {.front card-id="card-904751811797f1ac"}
What is $\operatorname{ht}{\mathbf{G}}_a$ in characteristic $p$?
:::

::: {.back card-id="card-904751811797f1ac"}
Height $\infty$.
:::

::: {.front card-id="card-530f8b7d350ac21b"}
What are the torsion points on ${\mathbf{G}}_m$?
:::

::: {.back card-id="card-530f8b7d350ac21b"}
Roots of unity.
:::

::: {.front card-id="card-5496190b1d9e0cc4"}
What is $F_\pi$? Give an example of $f\in F_\pi$.
:::

::: {.back card-id="card-5496190b1d9e0cc4"}
$F_\pi \coloneqq\left\{{ f\in R{\llbracket T \rrbracket  } {~\mathrel{\Big\vert}~}f(T) = \pi T + { \mathsf{O}}(T^2) ,\,\, f\equiv T^q \operatorname{mod}\pi}\right\}$.

For $K = { {\mathbf{Q}}_p }$, take $f(T) = (1+T)^p - 1 = T^p + {p\choose p-1}T^{p-1} + \cdots + pT$, so $f = [p]$ on ${\mathbf{G}}_m$.
:::

::: {.front card-id="card-1b6f81d13cff9302"}
What are the key properties of $F_\pi$?
:::

::: {.back card-id="card-1b6f81d13cff9302"}
For $f,g\in F_\pi$ and $\phi_1 \in R{\llbracket x_1,\cdots, x_n \rrbracket  }$, $\exists ! \phi \in R{\llbracket x_1,\cdots, x_n \rrbracket  }$ st $\phi = \phi_1 + { \mathsf{O}}(x^2)$ and $f\circ \phi = \phi \circ \Delta_g$, i.e.$f(\phi(x_1,\cdots, x_n)) = \phi(g(x_1), \cdots, g(x_n))$.
:::

::: {.front card-id="card-9065d30f1cc7ba3c"}
What is the Lubin-Tate FGL attached to $f\in F_\pi$?
:::

::: {.back card-id="card-9065d30f1cc7ba3c"}
The unique FGL $F_f\in R{\llbracket x,y \rrbracket  }$ st $f\in { \operatorname{End} }_{\fgl} F_f$ canonically, so $f(F_f(x,y)) = F_f(f(x), f(y))$.
:::

::: {.front card-id="card-f8c7dd23d0446e5a"}
What do we know about field extensions generated by Eisenstein polynomials?
:::

::: {.back card-id="card-f8c7dd23d0446e5a"}
- Totally ramified.
:::

::: {.front card-id="card-e94fbcf6815d8767"}
How are an unramified and a totally ramified extension related?
:::

::: {.back card-id="card-e94fbcf6815d8767"}
- Disjoint
:::

::: {.front card-id="card-9c6ca18eb9036a9f"}
How is $\overline{{ \mathbf{F} }_{q}}$ obtained from ${{ \mathbf{F} }_{q}}$?
:::

::: {.back card-id="card-9c6ca18eb9036a9f"}
- Adjoin all roots of unity.
:::
