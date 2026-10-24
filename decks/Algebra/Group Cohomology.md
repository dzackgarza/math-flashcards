---
title: "Algebra::Group Cohomology"
---

::: {.front card-id="card-819e900b727840dd"}
When is $k[G]$ commutative?
:::

::: {.back card-id="card-819e900b727840dd"}
Iff $G$ is commutative.
:::

::: {.front card-id="card-e8ca5054254bf3da"}
What is ${}_{G}\Mod$?
:::

::: {.back card-id="card-e8ca5054254bf3da"}
$M\in   {}_{\ZZ}\Mod$ with an action $\psi\in   {}_{\ZZ}\Mod(G, \mathop{\mathrm{Aut}}({\mathbf{G}}_a M))$, so $g(x+y) = gx+gy$ and $(gh)x = g(hx)$.

$G\dash$equivariant morphisms, $gf(x) = f(gx)$.
:::

::: {.front card-id="card-d57881484e0bb6ef"}
How can you determine if a SES $\xi\in {}_{G}\Mod$ is exact?
:::

::: {.back card-id="card-d57881484e0bb6ef"}
Exact iff exact in ${}_{\ZZ}\Mod$
:::

::: {.front card-id="card-6183f61d2a02d4b2"}
Define $M^G$ and $M_G$ and discuss their exactness.
:::

::: {.back card-id="card-6183f61d2a02d4b2"}
$M^G \coloneqq\left\{{m\in M\st gm=m\,\,\forall G}\right\}$: invariants, largest $G\dash$trivial **submodule**. Left exact as a functor ${}_{G}\Mod\to  {}_{\ZZ}\Mod$, so preserves injections.

$M_G \coloneqq M/\left\langle{gm-m\st m\in M, g\in G}\right\rangle_\ZZ$: coinvariants, largest $G\dash$trivial **quotient**. Right exact as a functor, so preserves surjections.
:::

::: {.front card-id="card-306aeaa89da6a68e"}
Interpret $H^*(G; M)$ topologically.
:::

::: {.back card-id="card-306aeaa89da6a68e"}
$H^*(G; \ZZ) = H^*(K(G, 1); \ZZ)$ and $H^*(G; M) = H^*(K(G, 1); \underline{M})$ where $\underline{M}$ is a the corresponding local system.
:::

::: {.front card-id="card-71e719597b9254b5"}
Describe the monoid ring $R[M]$ for $R$ a ring and $M$ a monoid. What is its universal property?
:::

::: {.back card-id="card-71e719597b9254b5"}
Free ${}_{R}\Mod$ with basis $\left\{{m\in M}\right\}$ with $[m_1]\cdot [m_2] \coloneqq[m_1 m_2]$ using the monoid operation, extended bilinearly.

${}_{R}  \mathsf{Alg}(R[M], B) \cong \mathsf{Mon}(M, {\mathbf{G}}_m B)$.
:::

::: {.front card-id="card-318066493d5f7eeb"}
What is the norm element of a finite group? Why is it important?
:::

::: {.back card-id="card-318066493d5f7eeb"}
$N\coloneqq\sum_{g\in G} g\in \ZZ[G]$, which is $G\dash$invariant.

$\ZZ[G]^G = \left\langle{N}\right\rangle_\ZZ$.
:::

::: {.front card-id="card-456ddebfbbaa64a2"}
What is the augmentation on $\ZZ[G]$? Describe the augmentation ideal.
:::

::: {.back card-id="card-456ddebfbbaa64a2"}
$\alpha: \ZZ[G]\to \ZZ$ where $\sum n_g[g] \mapsto \sum n_g$, "evaluate each $g\in G$ at the point 1".

$I\coloneqq\ker \alpha$ fits into a SES $I\hookrightarrow\ZZ[G]\twoheadrightarrow\ZZ\in \mods{\ZZ[G]}$ where $\ZZ$ has the trivial action.

$I\in   {}_{\ZZ}\Mod^\free$ has basis $\left\{{[g] - [e] \st g\in G}\right\}$.
:::

::: {.front card-id="card-5eab3dfa10f32541"}
When does the augmentation SES split? Why care?
:::

::: {.back card-id="card-5eab3dfa10f32541"}
Only if $G$ is trivial: a section has to send 1 to a $G\dash$invariant element, which is either zero or a multiple of $N$.

If $G$ is nontrivial, $\ZZ$ is not projective in $\mods{\ZZ[G]}$.
:::

::: {.front card-id="card-d79ac55113f033ef"}
What is Maschke's theorem?
:::

::: {.back card-id="card-d79ac55113f033ef"}
For $k$ a field and $G$ finite, TFAE:

$\operatorname{ch}k \nmid {\sharp}G$

$k[G]$ is a semisimple module, so every $M\in \mods{k[G]}$ is projective and injective, thus all higher cohomology vanishes.
:::

::: {.front card-id="card-95736ac32ec10e2f"}
Describe group (co)homology in terms of Tor and Ext.
:::

::: {.back card-id="card-95736ac32ec10e2f"}
$M^G = \mods{\ZZ[G]}(\ZZ\to M)$

$M_G = \ZZ\otimes_{\ZZ[G]} M$.
:::

::: {.front card-id="card-d7e6762dbf20fb8c"}
Interpret $H_1(G; \ZZ)$.
:::

::: {.back card-id="card-d7e6762dbf20fb8c"}
$I/I^2 = G^\ab$.
:::

::: {.front card-id="card-5dfb91fdb8faed3e"}
Describe $\ZZ[\ZZ]$.
:::

::: {.back card-id="card-5dfb91fdb8faed3e"}
$\ZZ[\ZZ] = \ZZ[t, t^{-1}]$ the Laurent polynomial ring with $I = \left\langle{e-1}\right\rangle$ principal corresponding to $\left\langle{t-1}\right\rangle$, so a free rank 1 $\mods{\ZZ[G]}$.

UFD of Krull dimension 2.
:::

::: {.front card-id="card-5dac57b1420308dd"}
Describe $H^*(\ZZ; M)$ and $H_*(\ZZ; M)$.
:::

::: {.back card-id="card-5dac57b1420308dd"}
Use the free resolution $\ZZ[G] \hookrightarrow\ZZ[G] \twoheadrightarrow\ZZ$ using $x\mapsto x\cdot([e] - [1])$ and the augmentation and that $I =\left\langle{e-1}\right\rangle \cong \ZZ[\ZZ]$.

$H_*(G; M) = M_G + M^G t$.

$H^*(G; M) = M^G + M_G t$
:::

::: {.front card-id="card-88b54dbab46175fc"}
What is $I$ for $G = C_n$?
:::

::: {.back card-id="card-88b54dbab46175fc"}
$I = \left\langle{\sigma - 1}\right\rangle$ where $C_n = \left\langle{\sigma}\right\rangle_\ZZ$.
:::

::: {.front card-id="card-655dc1269608105b"}
What is a free resolution of $\ZZ$ in $\mods{\ZZ[G]}$ for $G = C_n$?
:::

::: {.back card-id="card-655dc1269608105b"}
Periodic:
$$\cdots \xrightarrow{\sigma-1}\ZZ[G]\xrightarrow{\cdot N} \ZZ[G]\xrightarrow{\sigma-1}\ZZ[G]\xrightarrow{{\varepsilon}}\ZZ\to 0$$
:::

::: {.front card-id="card-3eff1b0c0da30d10"}
What are $H^*(C_n; M)$ and $H_*(C_n; M)$?
:::

::: {.back card-id="card-3eff1b0c0da30d10"}
$$H_*(C_n; M) = M_G \cdot t^0 + \bigoplus_{i}M^G/NM \cdot t^{2i+1} + \bigoplus_{i} \ker N/IM \cdot t^{2i}$$
$$H^*(C_n; M) = M^G\cdot t^0 + \bigoplus_{i} \ker N/IM \cdot t^{2i+1} + \bigoplus_{i} M^G/NM\cdot t^{2i}$$
Here $G \coloneqq C_n$, $N$ is the norm, $I$ is the augmentation ideal, and the sums over even degrees start at $i = 1$. So for $k\geq 1$:

$H^{2k}(G; M) \cong H_{2k+1}(G; M) = M^G / NM$.

$H^{2k+1}(G; M) \cong H_{2k}(G; M) = (\ker N)/IM$.

Except in degree 0: $H^0(G; M) = M^G$ and $H_0(G; M) = M_G = M/IM$.

So the even $H^n$ and odd $H_n$ are quotients of $H^0$, and the odd $H^n$ and even $H_n$ ($n\geq 2$) are subgroups of $H_0$.
:::

::: {.front card-id="card-bc1dcb9e5085b9c2"}
What are $K(\ZZ, 1)$ and $K(C_2, 1)$?
:::

::: {.back card-id="card-bc1dcb9e5085b9c2"}
$K(\ZZ, 1)\simeq S^1$.

$K(C_2, 1)\simeq\RP^\infty$
:::

::: {.front card-id="card-e4afb7b4e593536b"}
What are the ${}_{G}\Mod$ structures on ${}_{\ZZ}\Mod(A, B)$ and $A\otimes_\ZZ B$?
:::

::: {.back card-id="card-e4afb7b4e593536b"}
$g\curvearrowright\sum a_i\otimes b_i \coloneqq\sum ga_i\otimes gb_i$ the diagonal action.

$(g\curvearrowright f)(x) \coloneqq g.f(g^{-1}x)$ the adjoint action.
:::

::: {.front card-id="card-de338f6a3408eca9"}
Describe $f\in {}_{\ZZ}\Mod(A, B)^G$.
:::

::: {.back card-id="card-de338f6a3408eca9"}
$gf(g^{-1}x) = f(x) \implies gf(x) = f(gx)$, so $G\dash$equivariance.
:::

::: {.front card-id="card-d7b196454f24f6e4"}
Define a free $G\dash$action.
:::

::: {.back card-id="card-d7b196454f24f6e4"}
Trivial stabilizers.
:::

::: {.front card-id="card-0959803a2d48e016"}
What is the standard resolution of $\ZZ$ as a $\mods{\ZZ[G]}$?
:::

::: {.back card-id="card-0959803a2d48e016"}
$P_n \coloneqq\mathsf{Free}_{  {}_{\ZZ}\Mod}(G{ {}^{ \scriptscriptstyle\times^{n+1} }  })$, so $P_0 \cong \ZZ[G]$ and $\operatorname{rank}_\ZZ P_n = {\sharp}(G)^n$ whose differential is
$${\left[ {g_0,\cdots, g_n} \right]}\xrightarrow{{\partial}_n} \sum_{i=0}^n (-1)^i {\left[ {g_0, \cdots, \widehat{g}_i, \cdots, g_n} \right]}$$
:::

::: {.front card-id="card-bc1a1f1752512b0b"}
Describe $\mods{\ZZ[G]}(P_n, M)$ for $P_\bullet \rightrightarrows\ZZ$ the standard resolution.
:::

::: {.back card-id="card-bc1a1f1752512b0b"}
$\mods{\ZZ[G]}(P_n\to M) =   {}_{\ZZ}\Mod(P_n \to M)^G$, so $f(g.g_0,\cdots, g.g_n) = gf(g_0,\cdots, g_n)$ for $f: G{ {}^{ \scriptscriptstyle\times^{n+1} }  }\to M$.
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
Explain how an extension $E$ of $G$ by $M\in {}_{\ZZ}\Mod$ puts a ${}_{G}\Mod$ structure on $M$
:::

::: {.back card-id="card-e3e52f477a2a52bf"}
For $M\hookrightarrow E \twoheadrightarrow G$, let $g.m \coloneqq\tilde g m \tilde g^{-1}$ where $\tilde g\in E$ is any lift.
:::

::: {.front card-id="card-6cba8e3d7af69c56"}
How is $H^2(G; M)$ interpreted?
:::

::: {.back card-id="card-6cba8e3d7af69c56"}
Equivalence classes of extensions $M\hookrightarrow E \twoheadrightarrow G$.

The trivial element is $M \rtimes G$ where $M\normal E$.
:::

::: {.front card-id="card-2b6f54fd8f0fdc89"}
Why is $H^*(G; M)$ finite with $G, M$ are finite?
:::

::: {.back card-id="card-2b6f54fd8f0fdc89"}
${\sharp}Z^n(G; M) \leq ({\sharp}M)^{{\sharp}G} < \infty$.
:::

::: {.front card-id="card-25a58edd3c607c88"}
Define $\mathrm{Ind}^{H}_{G} M$ for $M\in {}_{H}\Mod$.
:::

::: {.back card-id="card-25a58edd3c607c88"}
$\mathrm{Ind}^{H}_{G}({-}) \coloneqq\ZZ[G]\otimes_{\ZZ[H]} ({-}) \in \mods{\ZZ[G]}$ acting diagonally.
:::

::: {.front card-id="card-4ae12f9179709702"}
Define $\mathrm{coInd}^{H}_{G} M$ for $M\in {}_{H}\Mod$.
:::

::: {.back card-id="card-4ae12f9179709702"}
$\mathrm{coInd}^{H}_{G}({-}) =   {}_{\ZZ[H]}\Mod(\ZZ[G], {-}) \in \mods{\ZZ[G]}$ with a funny action $(g.f)(x) \coloneqq f(xg)$.
:::

::: {.front card-id="card-22f2f2a4ffc1708d"}
What is Artin's theorem on representations of finite groups?
:::

::: {.back card-id="card-22f2f2a4ffc1708d"}
For $G\in \Fin\Grp$, any $V\in \Rep(G)^\fd_{/ {\CC}}$ is a $\QQ\dash$linear combinations of $\mathrm{Ind}^{H}_{G} W$ where $H\leq G$ is cyclic and $W$ is a character.
:::

::: {.front card-id="card-5a798c1532df1e68"}
What is Brauer's theorem on representations of finite groups?
:::

::: {.back card-id="card-5a798c1532df1e68"}
For $G\in \Fin\Grp$, any $V\in \Rep(G)^\fd_{/ {\CC}}$ is a $\ZZ\dash$linear combinations of $\mathrm{Ind}^{H}_{G} W$ where $H\leq G$ is an elementary subgroup, so $H\cong C\times P$ with $C$ cyclic and $P$ a $p\dash$group, and $W$ is a character.
:::

::: {.front card-id="card-c6daf2e47c2b6cf7"}
What is Artin's holomorphy conjecture?
:::

::: {.back card-id="card-c6daf2e47c2b6cf7"}
Every Artin $L\dash$function attached to a nontrivial representation of a finite group has a holomorphic continuation to $\CC$.

Shown recently for $A_5$ using Langlands.

Brauer shows *meromorphic* continuation as an easy corollary of his induction theorem.
:::

::: {.front card-id="card-4647169caa41a3e2"}
What is Shapiro's lemma?
:::

::: {.back card-id="card-4647169caa41a3e2"}
For $H\leq G$ and $N\in   {}_{H}\Mod$,
$$H_n(G; \mathrm{Ind}^{H}_{G} N)  { \, \xrightarrow{\sim}\, }H_n(H; N)$$
$$H^n(G; \mathrm{coInd}^{H}_{G} N)  { \, \xrightarrow{\sim}\, }H_n(H; N)$$
:::

::: {.front card-id="card-1e52d15fd1f67abd"}
What are $\mathrm{Ind}^{\pt}_{G} A$ and $\mathrm{coInd}^{\pt}_{G} A$?
:::

::: {.back card-id="card-1e52d15fd1f67abd"}
$\mathrm{Ind}^{\pt}_{G} A = \ZZ[G]\otimes_\ZZ A$ and $\mathrm{coInd}^{\pt}_{G} A =   {}_{\ZZ}\Mod(\ZZ[G] \to A)$.
:::

::: {.front card-id="card-2a2bbbb6b39f28ca"}
What are acyclic modules for group homology?
:::

::: {.back card-id="card-2a2bbbb6b39f28ca"}
Induced modules: any module isomorphic to $\mathrm{Ind}^{H}_{G} A$ for some $H$ and $A$.

E.g. $H_n(G; \mathrm{Ind}^{\pt}_{G} A) = 0$.
:::

::: {.front card-id="card-933022ad9dd315c4"}
Describe how any $M\in {}_{G}\Mod$ is surjected onto by an induced module and injects into a coinduced module.
:::

::: {.back card-id="card-933022ad9dd315c4"}
$\mathrm{Ind}^{\pt}_{G}M^{\mathrm{triv}}\twoheadrightarrow M$ and $M\hookrightarrow\mathrm{coInd}^{\pt}_{G} M^{\mathrm{triv}}$.

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
$$\operatorname{Tor}_n^{\ZZ[H]}(M, N)  { \, \xrightarrow{\sim}\, }\operatorname{Tor}_n^{\ZZ[G]}(M, \mathrm{Ind}^{H}_{G} N)$$
$$ \operatorname{Ext}^n_{\ZZ[H]}(M, N)  { \, \xrightarrow{\sim}\, } \operatorname{Ext}^n_{\ZZ[G]}(M, \mathrm{coInd}^{H}_{G} N)$$
$$ \operatorname{Ext}^n_{\ZZ[H]}(N, M)  { \, \xrightarrow{\sim}\, } \operatorname{Ext}^n_{\ZZ[G]}(\mathrm{Ind}^{H}_{G} N, M)$$
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

$N\normal G$ and $M\in   {}_{G}\Mod$ yields $M^N\in   {}_{G/N}\Mod$ and inflation $H^n(G/N; M^N) \to H^n(G; M)$.
:::

::: {.front card-id="card-25f59b8a0a87a778"}
What is the inflation-restriction exact sequence?
:::

::: {.back card-id="card-25f59b8a0a87a778"}
$$H^1(G/H; A^H) \xhookrightarrow{\mathrm{Inf}} H^1(G; A) \xrightarrow{\mathrm{Res}} H^1(H; A)^{G/H} \longrightarrow H^2(G/H; A^H) \xrightarrow{\mathrm{Inf}} H^2(G/H; A^H) \to H^2(G; A)$$
:::

::: {.front card-id="card-919d2fe8b2dce362"}
What is corestriction? What is its important property?
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
Discuss vanishing of $\widehat{H}(G; M)$ for $G\in\Fin\Grp$.
:::

::: {.back card-id="card-5a8a7e7f468f0f0d"}
Since induced = coinduced for finite groups, weakly injective = weakly projective, so $\widehat{H}^i(G; M) =0$ for all $i$, including $i=0$.
:::

::: {.front card-id="card-ca23e4bdbace6f6c"}
Describe how to compute $\widehat{H}^*(G; M)$ at the cochain level.
:::

::: {.back card-id="card-ca23e4bdbace6f6c"}
Take the "resolution $X_\bullet$ where $X_n = X_{-1-n} = \ZZ[G{ {}^{ \scriptscriptstyle\times^{n+1} }  }]$ with the usual ${\partial}_n$, then $\widehat{H}^n(G; M) =H^n(\mathop{\mathrm{Hom}}(X_n, M)^G)$.
:::

::: {.front card-id="card-8931a01268da4819"}
What is dimension shifting for $\widehat{H}$?
:::

::: {.back card-id="card-8931a01268da4819"}
For $A\hookrightarrow I \twoheadrightarrow B\in   {}_{G}\Mod$ with $I$ coinduced, then $\widehat{H}(G; B)\cong \widehat{H}^{n+1}(G; A)$.
:::

::: {.front card-id="card-6b17205179edc5b6"}
Describe (co)restriction for $L/K$ a Galois extension
:::

::: {.back card-id="card-6b17205179edc5b6"}
Noting ${\mathbf{G}}_a(L)^G = K$ for $G\coloneqq\Gal(L/K)$,

$\mathrm{Res}^{H}_{G}: M^G\to M^H$ corresponds to $K\hookrightarrow L$.

$\mathrm{coRes}^{H}_{G}: M^H \to M^K$ corresponds to $\operatorname{Trace}_{L/K}: L\to K$.
:::

::: {.front card-id="card-381db49f4793df13"}
Discuss finiteness for Tate cohomology.
:::

::: {.back card-id="card-381db49f4793df13"}
$\widehat{H}^n(G; M) = \widehat{H}^n(G; M)[m]$ is always a torsion ${}_{\ZZ}\Mod$, where $m = {\sharp}G$.

If $M\in   {}_{\ZZ}\Mod^\fg$ then every $\widehat{H}^n(G; M)\in\Fin\Grp$.

Use that a group is finite iff finitely generated and torsion.
:::

::: {.front card-id="card-ff80a060563c9016"}
What is the transfer?
:::

::: {.back card-id="card-ff80a060563c9016"}
For $H\leq G$ there is an obvious map $H^\ab\to G^\ab$, but there is also a wrong-way transfer map $G^\ab\to H^\ab$.
:::

::: {.front card-id="card-a0319417af0eb6b8"}
What is the Herbrand quotient?
:::

::: {.back card-id="card-a0319417af0eb6b8"}
For $G$ finite cyclic, $h(A) \coloneqq h^0(A)/ h^1(A) \in \QQ_{> 0}$ where $h^i(A) \coloneqq{\sharp}\widehat{H}^i(G; A)$, defined when both are finite.

For $A\hookrightarrow B\twoheadrightarrow C$ a SES, if any two $h({-})$ are defined then it is also defined for the third, and $h(B) = h(A) h(C)$.

If $A$ is finite then $h(A) = 1$ since $h^1 = h^0$.

If $f\in   {}_{G}\Mod(A\to B)$ with finite kernel and cokernel then $h(A) = h(B)$.
:::

::: {.front card-id="card-cc0436ecd1b5cc0b"}
What is $\sum (-1)^i {\sharp}A_i$ for $A_i$ in a LES in ${}_{\ZZ}\Mod^\fin$? For vector spaces?
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

So $H\leq G \implies H^n(H; M) = 0$ for all $M\in   {}_{G}\Mod$.
:::

::: {.front card-id="card-a28d9eaa9c55722b"}
Discuss $p\dash$groups $G$ acting on $p\dash$primary $G\dash$modules $M$.
:::

::: {.back card-id="card-a28d9eaa9c55722b"}
If $M\neq 0$ then $M^G\neq 0$.
:::

::: {.front card-id="card-9c49955d526039c7"}
Discuss duality in group (co)homology.
:::

::: {.back card-id="card-9c49955d526039c7"}
For $A {}^{ \vee }\coloneqq\mathop{\mathrm{Hom}}(A, \QQ/\ZZ)$, $H^n(G; A) {}^{ \vee }\cong H_n(G; A {}^{ \vee })$ for $G$ finite.
:::

::: {.front card-id="card-758a5cbac10a9b22"}
How can cohomological triviality be checked locally?
:::

::: {.back card-id="card-758a5cbac10a9b22"}
$A$ is $G\dash$cohomologically trivial $\iff A$ is $G_p\dash$cohomologically trivial for every sylow $p\dash$subgroup $G_p$ for every $p\mathrel{\Big|}{\sharp}G$.
:::

::: {.front card-id="card-70a4f711e884a8b2"}
What is the cup product on cochains?
:::

::: {.back card-id="card-70a4f711e884a8b2"}
$$\begin{align}K^p(G; A) \otimes_\ZZ K^q(G; B) &\to K^{p+q}(G; A\otimes_\ZZ B)\\ a\otimes b &\mapsto \mathbf{g} \mapsto a(g_0,\cdots, g_p)\otimes b(g_{p-1}, \cdots g_{p+q}) \end{align}$$
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
For $A\in   {}_{G}\Mod$ and $a\in H^2(G; A)$ satisfying for all primes $p$ that $H^1(G_p; A) = 0$ and ${\sharp}H^2(G_p; A) = {\sharp}G_p$ and is generated by $a_p \coloneqq\mathrm{Res}^{G_p}_{G} a$, for $G_p$ the Sylow $p\dash$subgroups, then

For all $D\in   {}_{G}\Mod$ torsionfree and all $H\leq G$, there are isomorphism $\widehat{H}^n(H; D) \underset{ {{-}\smile a} }{ { \, \xrightarrow{\sim}\, }}\widehat{H}^{n+2}(H; A\otimes_\ZZ D)$.

Taking $D = \ZZ$ yields $\widehat{H}^n(H; \ZZ) { \, \xrightarrow{\sim}\, }\widehat{H}^{n+2}(H; D)$, so $D$ cohomology is just a shift of $\ZZ$ cohomology.
:::

::: {.front card-id="card-df98d4dc6835b4d2"}
What is the significance of Tate-Nakayama?
:::

::: {.back card-id="card-df98d4dc6835b4d2"}
For $K\in \mathsf{Local}\mathsf{Field}$ and $L/K$ finite Galois, set $G\coloneqq\Gal(L/K)$ and $A\coloneqq L^{\times}$

The hypotheses of Tate-Nakayama apply and yields
$$G^\ab= \widehat{H}^{-2}(G; \ZZ)  { \, \xrightarrow{\sim}\, }\widehat{H}^0(G; L^{\times}) = K^{\times}/NL^{\times}$$
Thus if $L/K$ is abelian then $G \cong \operatorname{coker}\operatorname{Nm}_{L/K}$.

Suggests target group for CFT should be $K^{\times}$, so there should be an isomorphism between $\Gal^\ab(\overline{K}/K)$ and $\mathsf{pro}K^{\times}$.
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

Open $\implies$ closed holds in every topological group, since the complement is a union of open cosets; the converse fails. Compactness gives finite index, since the open cosets cover $G$.

So open $\implies$ finite index, but not conversely: NOT true that every finite index subgroup is closed! E.g. $V\coloneqq\prod_{i\in {\mathbf{N}}} { \mathbf{F} }_2$ has $\aleph_0$ open subgroups but $2^{2^{\aleph_0}}$ index 2 subgroups.

The converse is true if $G$ is profinite and topologically finitely generated.

$\iff$ holds when $G$ is strongly complete.
:::

::: {.front card-id="card-5689c73b27f7cdd4"}
How do you extract a Hausdorff topological group from an non-Hausdorff one?
:::

::: {.back card-id="card-5689c73b27f7cdd4"}
Mod out by the closure of the identity.
:::

::: {.front card-id="card-24034aab968ea04a"}
Write a profinite group as a limit.
:::

::: {.back card-id="card-24034aab968ea04a"}
$G = \projectivelim_{U\leq G \text{ open}, [G:U] < \infty} G/U$.
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

Useful since $\pi_1^\text{ét}(X) = \mathsf{pro}\pi_1(X(\CC))$, so not residually finite means losing information from $\pi_1$.
:::

::: {.front card-id="card-fc790016b53e422d"}
Characterize topological groups acting on discrete modules.
:::

::: {.back card-id="card-fc790016b53e422d"}
The action is cts iff $\Stab_G(x)$ is open for every $x$.

If $G$ is profinite, the actions is cts iff $G = \bigcup_{U\leq G \text{ open}}M^U$, the union of its (open) invariants.

Profinite groups acting on discrete modules have finite orbits.
:::

::: {.front card-id="card-2ffce7da1f1ee84f"}
What does it mean to be topologically finitely generated?
:::

::: {.back card-id="card-2ffce7da1f1ee84f"}
There is a generating set $S$ such that the smallest closed subgroup of $G$ containing $S$ is $G$ itself.
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
$$\Top(G, Y) = \Top(\lim G/N, Y) = \colim \Top(G/N, Y)$$
:::

::: {.front card-id="card-daafc2582fc47c4e"}
What are continuous cochains?
:::

::: {.back card-id="card-daafc2582fc47c4e"}
$K_\text{cts}^n(G; M) \coloneqq\Top(G{ {}^{ \scriptscriptstyle\times^{n} }  }, M)$.
:::

::: {.front card-id="card-e23d5e0a1a45b10f"}
Discuss continuity for profinite group cohomology.
:::

::: {.back card-id="card-e23d5e0a1a45b10f"}
$H^n(\projectivelim G_i; \colim M_i) \cong \colim H^n(G_i; M_i)$.

In particular $H^n(G; A)=\colim_U H^n(G/U; A^U)$ using that $U_2\hookrightarrow U_1 \implies G/U_1 \twoheadrightarrow G/U_2$ (inflation).
:::

::: {.front card-id="card-a0e7561b884f9ba2"}
Discuss limits for Galois cohomology.
:::

::: {.back card-id="card-a0e7561b884f9ba2"}
For $g_K \coloneqq\Gal(k^{ {}^{ \operatorname{sep} } }/k)$ and $A\in   {}_{g_K}\Mod$ write $A(L) \coloneqq A^{g_L}$, then
$$H^1(g_U; A) = \colim_{L/K} H^n(\Gal(L/K); A(L))$$
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
$H^{\geq 1}(G; A)\in   {}_{\ZZ}\Mod^\tors$ is always torsion.

Proof: $H^q(G; A) = \colim H^q(G/U; A^U) = \colim H^q(G/U; A^u)[n]$ for $n \coloneqq[G: U]$ by restriction-corestriction, and ${}_{\ZZ}\Mod^\tors$ is closed under colimits.
:::

::: {.front card-id="card-6966b7db2a0f8235"}
What is the profinite completion?
:::

::: {.back card-id="card-6966b7db2a0f8235"}
For a group $G$: take the poset $N\geq M \iff N \subseteq M$ for $N, M \normal G$ of finite index and the directed system of quotients $G/N$; the profinite completion is $\widehat{G} \coloneqq \projectivelim_N G/N$.

For spaces: regard objects $X$ in $\mathsf{pro}\mathsf{C}$ as sequences $X = \left\{{X_\alpha}\right\}_{\alpha\in I}$ where $X_\alpha\in \mathsf{C}$.

Let $\Spaces_{\Fin\Grp}$ be the full subcategory of spaces with $\pi_i \in \Fin\Grp$.

The profinite completion of $X\in\Spaces$ is the left-adjoint to the inclusion $\mathsf{pro}\Spaces_{\Fin\Grp} \to \mathsf{pro}\Spaces$.
:::

::: {.front card-id="card-8a49e729201758aa"}
Discuss topological properties of profinite groups.
:::

::: {.back card-id="card-8a49e729201758aa"}
Always compact and totally disconnected; conversely every compact totally disconnected topological group is profinite.
:::

::: {.front card-id="card-9518c9f55fe23645"}
Give examples of profinite groups.
:::

::: {.back card-id="card-9518c9f55fe23645"}
$\widehat{\ZZ}= \projectivelim_{n>0} \ZZ/n\ZZ$ the profinite completion of $\ZZ$

${ \ZZ_{\widehat{p}} }\coloneqq\projectivelim \ZZ/p^n\ZZ$ the $p\dash$completion
:::
