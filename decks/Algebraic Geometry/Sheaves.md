---
title: "Algebraic Geometry::Sheaves"
---

::: {.front card-id="card-14008e56d2fec738" tags="definition"}
What is a **presheaf**?
:::

::: {.back card-id="card-14008e56d2fec738"}
A functor $F: {\mathsf{Open}}(X)^{\operatorname{op}}\to \mathsf{CRing}$ (say; or sets, abelian groups, ...) preserving terminal objects, i.e. for each open $U \subseteq X$ a ring $F(U)$ where $F(\emptyset) = 0$, for every $U\hookrightarrow V$ a restriction $\mathop{\mathrm{Res}}_{V< U}: F(V)\to F(U)$, where $\mathop{\mathrm{Res}}_{U, U} = \operatorname{id}_{F(U)}$ and $U\hookrightarrow V\hookrightarrow W \leadsto \mathop{\mathrm{Res}}_{VU} \circ \mathop{\mathrm{Res}}_{WV} = \mathop{\mathrm{Res}}_{WU}$.

A sheaf also satisfies gluing and uniqueness for compatible local sections.
:::

::: {.front card-id="card-c59fe5bb7a144af8"}
What is a **sheaf**?
:::

::: {.back card-id="card-c59fe5bb7a144af8"}
A presheaf satisfying unique gluing: given $\left\{{\phi_i \in F(U_i)}\right\}$ with ${ \left.{{\phi_i}} \right|_{{U_{ij}}} } = { \left.{{\phi_j}} \right|_{{U_{ij}}} }$ there exists a unique $\Phi\in F(\bigcup_i U_i)$ such that ${ \left.{{\Phi}} \right|_{{U_i}} } = \phi_i$ for all $i$.
:::

::: {.front card-id="card-d11a1c7edb702d31"}
Give an example of a presheaf that is not a sheaf.
:::

::: {.back card-id="card-d11a1c7edb702d31"}
Any presheaf of constant functions, since functions can be constant on disjoint open sets (thus agreeing on overlaps trivially) without being globally constant (jump discontinuities)
:::

::: {.front card-id="card-7a8067f2aeb0cca8"}
What is the **equalizer characterization** of a sheaf?
:::

::: {.back card-id="card-7a8067f2aeb0cca8"}
$$F(U) \rightarrow \prod_{i} F(U_i) {{{} \atop \longrightarrow}\atop{\longrightarrow \atop {}}} \prod_{i, j} F(U_i \cap U_j)$$
where the maps are the restrictions $U_i \to U_{ij}$ and $U_j\to U_{ij}$.
:::

::: {.front card-id="card-82b98ea9b3cb0231" tags="definition"}
What is the **sheafification** of a presheaf?
:::

::: {.back card-id="card-82b98ea9b3cb0231"}
For ${\mathcal{F}}$ a presheaf, define ${\mathcal{F}}^+(U)$ as the functions $s: U\to \amalg_{x\in U} {\mathcal{F}}_x$ where $s(p) \in {\mathcal{F}}_p$ and for each $p\in U$ there is a neighborhood $V\subseteq U$ of $p$ and $t\in {\mathcal{F}}(V)$ such that $\forall q\in V,\,\, t_q = s(q)$ (equivalently, continuous sections of the étalé space of ${\mathcal{F}}$).

There is a map ${\mathcal{F}}\to{\mathcal{F}}^+$ inducing isomorphisms on all stalks, and every map from ${\mathcal{F}}$ to a sheaf factors uniquely through ${\mathcal{F}}^+$.
:::

::: {.front card-id="card-ea14df10f5014961" tags="definition"}
What is a **morphism of presheaves**? Of sheaves?
:::

::: {.back card-id="card-ea14df10f5014961"}
A morphism $\phi: {\mathcal{F}}\to {\mathcal{G}}$ of presheaves is a collection $\phi_U: {\mathcal{F}}(U) \to {\mathcal{G}}(U)$ fitting into commuting squares with restrictions, i.e. commuting with every restriction map. A morphism of sheaves is a morphism of the underlying presheaves.
:::

::: {.front card-id="card-a8dbd6c1552876cc"}
What is a **germ**?
:::

::: {.back card-id="card-a8dbd6c1552876cc"}
Elements in the stalk ${\mathcal{F}}_p$ are germs of sections of ${\mathcal{F}}$ over $p$.
:::

::: {.front card-id="card-903e35430d43d1de"}
What is the **stalk** of a sheaf?
:::

::: {.back card-id="card-903e35430d43d1de"}
${\mathcal{F}}_p \coloneqq\colim_{U\ni p} {\mathcal{F}}(U)$.
:::

::: {.front card-id="card-29db92d857211565"}
What is the **kernel sheaf**?
:::

::: {.back card-id="card-29db92d857211565"}
$U\mapsto \ker \phi(U)$, which is already a sheaf.
:::

::: {.front card-id="card-e37a62e39fa49064"}
What is the **image sheaf**?
:::

::: {.back card-id="card-e37a62e39fa49064"}
Sheafify $U\mapsto \operatorname{im}\phi(U)$.
:::

::: {.front card-id="card-eca54149334d9622"}
Give an example to show that the image presheaf is not necessarily a sheaf.
:::

::: {.back card-id="card-eca54149334d9622"}
Problem: may fail existence. Take $0\to \underline{{\mathbf{Z}}}\xrightarrow{2\pi i} {\mathcal{O}}_X \xrightarrow{\exp} {\mathcal{O}}_X^{\times}\to 0$; this is exact as a sequence of sheaves since it's exact on stalks, but not exact as a sequence of presheaves, showing that $\operatorname{im}_{{\mathsf{pre}}} \exp \neq (\operatorname{im}_{\mathsf{pre}}\exp)^+$ (where ${\mathcal{F}}= {\mathcal{F}}^+$ for any sheaf). Cover ${\mathbf{C}}^{\times}$ by contractible $U_i$, then take sections $f_i \coloneqq\operatorname{id}_{U_i} \in {\mathcal{O}}_X^{\times}$; then $f_i\in (\operatorname{im}\exp)^-$ since $\log(z)$ exists on each $U_i$. The sectors glue to ${\mathbf{C}}^{\times}$, but there is no global $\log(z)$. So $\operatorname{id}_{{\mathbf{C}}^{\times}} \not\in (\operatorname{im}\exp)^-$, so it fails the gluing axiom.
:::

::: {.front card-id="card-199b042d968cba02"}
What is the **cokernel sheaf**?
:::

::: {.back card-id="card-199b042d968cba02"}
For $\phi: {\mathcal{F}}\to {\mathcal{G}}$, sheafify $U\mapsto \operatorname{coker}\phi(U) \coloneqq{\mathcal{G}}/ \operatorname{im}\phi(U)$.
:::

::: {.front card-id="card-b4ef69e82c4e525c"}
Give an example to show that the cokernel presheaf is not a sheaf.
:::

::: {.back card-id="card-b4ef69e82c4e525c"}
Problem: may fail uniqueness. Let ${\mathcal{G}}\leq \mathop{\mathrm{Hol}}({\mathbf{C}}, {\mathbf{C}})$ be the sheaf of nonvanishing holomorphic functions and take $\exp: \mathop{\mathrm{Hol}}({\mathbf{C}}, {\mathbf{C}})\to {\mathcal{G}}$ and $U = {\mathbf{C}}\setminus\left\{{0}\right\}$. Set $f(z) = z$, then $f\in {\mathcal{G}}(U)$ since it's nonvanishing. Cover $U$ by sectors $U_i$, then $f\in \operatorname{im}{ \left.{{\exp}} \right|_{{U_i}} }$ for all $i$ since $\log f$ exists and $\exp(\log f) = f$, so $f = 0$ in $\operatorname{coker}{ \left.{{\exp}} \right|_{{U_i}} }$ for all $i$. But $f\not\in \operatorname{im}\exp$ since there is no global logarithm, so $f\neq 0\in \operatorname{coker}\exp$ as a morphism of presheaves.
:::

::: {.front card-id="card-79c3642c37f8ed12" tags="definition"}
What is the **pullback/pushforward** (inverse/direct images) of a sheaf?
:::

::: {.back card-id="card-79c3642c37f8ed12"}
For $f:X\to Y$, ${\mathcal{F}}\in {\mathsf{Sh}}(X), {\mathcal{G}}\in {\mathsf{Sh}}(Y)$. Pushforward/direct image: already a sheaf
$$f_*{\mathcal{F}}(U) ={\mathcal{F}}(f^{-1}(U)),\qquad f_*{\mathcal{F}}\in {\mathsf{Sh}}(Y)$$
Pullback/inverse image: **sheafify**
$$f^{-1}{\mathcal{G}}(U) \coloneqq\colim_{V\supseteq f(U)} {\mathcal{G}}(V)$$
For $f: X\hookrightarrow Y$ the inclusion of an open subset, $f^{-1}{\mathcal{G}}(U) = {\mathcal{G}}(U)$, so denote $f^{-1}{\mathcal{G}}\coloneqq{ \left.{{{\mathcal{G}}}} \right|_{{X}} }$.

For modules on ringed spaces, $f^*{\mathcal{G}}\coloneqq f^{-1}{\mathcal{G}}\otimes_{f^{-1}{\mathcal{O}}_Y}{\mathcal{O}}_X$.
:::

::: {.front card-id="card-e8e12fcc8b9e24a2" tags="definition"}
What is a **constant sheaf**?
:::

::: {.back card-id="card-e8e12fcc8b9e24a2"}
For $A\in {\mathsf{Ab}}{\mathsf{Grp}}$, $\underline{A}$ is the sheafification of the constant presheaf $U\mapsto A$. Equivalently, $\underline{A} \coloneqq C^0({-}, A^{{\operatorname{disc}}})$, the sheaf of locally constant functions to $A$. On nonempty connected sets $U$, $\underline{A}(U) = A$; on locally connected $U$, sections are the functions constant on every connected component. Stalks are all $A$.
:::

::: {.front card-id="card-0ccf704bc953a261" tags="definition"}
What is the **skyscraper sheaf**? Its stalks? Its adjoint characterization?
:::

::: {.back card-id="card-0ccf704bc953a261"}
For a point $p\in X$, the inclusion $\iota_p: \left\{{p}\right\} \hookrightarrow X$, and an abelian group $A$ (the constant sheaf $\underline{A}$ on $\left\{{p}\right\}$), the skyscraper sheaf is the direct image $(\iota_p)_*\underline{A}$. It assigns $U\mapsto A$ if $p\in U$ and $U\mapsto 0$ otherwise, with restrictions the identity or zero maps. Stalks are $A$ at each point in ${ \operatorname{cl}}_X(p)$ and 0 elsewhere. Adjoint to taking stalks: ${\mathsf{Ab}}({\mathcal{F}}_p, A)  { \, \xrightarrow{\sim}\, }{\mathsf{Sh}}(X)({\mathcal{F}}, (\iota_p)_* A)$.
:::

::: {.front card-id="card-0859e1c888527f03"}
What is the **canonical sheaf**?
:::

::: {.back card-id="card-0859e1c888527f03"}
For $X$ smooth over $S$ of relative dimension $n$, $\omega_{X/S} \coloneqq\operatorname{det}\Omega_{X/S} \coloneqq\bigwedge\nolimits^n \Omega_{X/S}$, a line bundle. Over a field $k$, $\omega_X \coloneqq\operatorname{det}\Omega_{X/k}$ with $n\coloneqq\dim X$.
:::

::: {.front card-id="card-9535c31c3ca2f51d"}
What is the **dualizing sheaf**?
:::

::: {.back card-id="card-9535c31c3ca2f51d"}
For $X$ proper over a field, $\omega_X^\circ\in {\mathsf{Coh}}(X)$ together with a trace $\operatorname{tr}: H^n(X; \omega_X^\circ)\to k$ such that $\forall {\mathcal{F}}\in {\mathsf{Coh}}(X)$, the composition
$$H^n(X; {\mathcal{F}}) \times \mathop{\mathrm{Hom}}({\mathcal{F}}, \omega_X^\circ) \to H^n(X, \omega_X^\circ) \xrightarrow{{\mathrm{tr}}}k$$
yields an isomorphism $\mathop{\mathrm{Hom}}({\mathcal{F}}, \omega_X^\circ)  { \, \xrightarrow{\sim}\, }H^n(X; {\mathcal{F}}) {}^{ \vee }$ and more generally $\operatorname{Ext}^i({\mathcal{F}}, \omega_X^\circ) \cong H^{n-i}(X; {\mathcal{F}}) {}^{ \vee }$. Exists for any projective scheme, not always equal to $\operatorname{det}\Omega_{X/k}$.
:::

::: {.front card-id="card-0c6c3a54e08bf4fb"}
What is a **local system**?
:::

::: {.back card-id="card-0c6c3a54e08bf4fb"}
A locally constant sheaf, i.e. a sheaf such that every $x\in X$ admits a neighborhood $U\ni x$ such that ${ \left.{{{\mathcal{F}}}} \right|_{{U}} }$ is a constant sheaf.
:::

::: {.front card-id="card-2a19d4bf210f5449"}
What is an **invertible sheaf**?
:::

::: {.back card-id="card-2a19d4bf210f5449"}
${\mathcal{L}}\in {\mathsf{Sh}}(X)$ such that $\exists {\mathcal{L}}^{-1}\in {\mathsf{Sh}}(X)$ with ${\mathcal{L}}\otimes_{{\mathcal{O}}_X} {\mathcal{L}}^{-1}\cong {\mathcal{O}}_X$.

Equivalently, every $x\in X$ admits a neighborhood $U\ni x$ such that ${ \left.{{{\mathcal{F}}}} \right|_{{U}} } \cong {\mathcal{O}}_U$.

Equivalently, a locally free ${\mathcal{O}}_X{\hbox{-}}$module of rank 1.
:::

::: {.front card-id="card-09446192b8f9ece5"}
Discuss invertible sheaves on affine schemes.
:::

::: {.back card-id="card-09446192b8f9ece5"}
${\mathcal{F}}\in \operatorname{Pic}(\operatorname{Spec}A)\implies {\mathcal{F}}$ corresponds to $M\in  {}_{A}{\mathsf{Mod}}$ which is finite projective locally free of rank 1 and thus flat and finitely presented. Every invertible sheaf on ${\mathbf{A}}^2_{/ {k}}$ is trivial.
:::

::: {.front card-id="card-e8e690603a360318"}
What is a **constructible sheaf**?
:::

::: {.back card-id="card-e8e690603a360318"}
${\mathcal{F}}\in {\mathsf{Sh}}(X)$ is constructible iff $\exists \left\{{i_{Y_i}: Y_i\hookrightarrow X}\right\}_{i\leq N}$ with $X = \bigcup_{i\leq N}Y_i$, i.e. $Y$ is a finite union of locally closed subschemes, such that ${ \left.{{{\mathcal{F}}}} \right|_{{Y_i}} } \coloneqq\iota_{Y_i}^* {\mathcal{F}}$ is a finite locally constant sheaf.
:::

::: {.front card-id="card-45174c1167af9df9"}
What is the **sheaf of rational functions** on a scheme?
:::

::: {.back card-id="card-45174c1167af9df9"}
Define the function field of $X$ to be $K\coloneqq{\mathcal{O}}_{X, \eta_X}$, the stalk at the generic point, and define ${\mathcal{K}}_X \coloneqq\underline{K}$, the constant sheaf associated to this field. Equivalently, sheafify $U\to \operatorname{ff}({\mathcal{O}}_X(U))$.
:::

::: {.front card-id="card-0b18a6dfa59ccde0"}
What is the fundamental exact sequence involving the tangent sheaf for ${\mathbf{P}}^n$?
:::

::: {.back card-id="card-0b18a6dfa59ccde0"}
$0\to {\mathcal{O}}_X \to {\mathcal{O}}_X(1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\to {\mathcal{T}}_X\to 0$.
:::

::: {.front card-id="card-aac019483de7ed9e"}
What does it mean to **twist a sheaf**?
:::

::: {.back card-id="card-aac019483de7ed9e"}
${\mathcal{F}}(n) \coloneqq{\mathcal{F}}\otimes_{{\mathcal{O}}_X} {\mathcal{O}}_X(n)$.
:::

::: {.front card-id="card-4d2fa6a3304404c6"}
Characterize coherent sheaves over $\operatorname{Spec}A$ for $A$ Noetherian.
:::

::: {.back card-id="card-4d2fa6a3304404c6"}
${\mathcal{F}}\in {\mathsf{Coh}}(\operatorname{Spec}A)\implies \exists \bigoplus_{i\in I} {\mathcal{O}}(n_i) \twoheadrightarrow{\mathcal{F}}$, i.e. always a quotient of a free sheaf. Easy proof: ${\mathcal{F}}(n)$ is globally generated for some $n$, so $\exists \bigoplus_{i\leq N} {\mathcal{O}}_X \twoheadrightarrow{\mathcal{F}}(n)$, now twist this exact sequence by $-n$.
:::

::: {.front card-id="card-c5e1189afc267094"}
What is the **six functor formalism**?
:::

::: {.back card-id="card-c5e1189afc267094"}
Direct image (pushforward) and inverse image (pullback), extension by zero (lower shriek) and exceptional image (upper shriek), internal tensor and internal hom.
:::

::: {.front card-id="card-5fb0674e6ef318ad"}
How is the **inverse image sheaf** defined? What are its stalks?
:::

::: {.back card-id="card-5fb0674e6ef318ad"}
$f^{-1}{\mathcal{G}}(U) \coloneqq\colim_{V\supseteq f(U)} {\mathcal{G}}(V)$. Stalks: ${\mathcal{G}}_p  { \, \xrightarrow{\sim}\, }(f^{-1}{\mathcal{G}})_p$.
:::

::: {.front card-id="card-7253757c78a0c001"}
What is the **extension by zero** sheaf? What are its stalks?
:::

::: {.back card-id="card-7253757c78a0c001"}
Sheafify $U\mapsto \chi_{V\subseteq U}{\mathcal{F}}(V)$ to get $\iota_! {\mathcal{F}}$ for $\iota: U \subseteq X$. Stalks are ${\mathcal{F}}_p \chi_{p\in U}$.

Alternatively take $\iota_* {\mathcal{F}}$.
:::

::: {.front card-id="card-c15fc4f7707b0b75"}
How is the pushforward sheaf defined? What are its stalks?
:::

::: {.back card-id="card-c15fc4f7707b0b75"}
$f_*{\mathcal{F}}(V) \coloneqq{\mathcal{F}}(f^{-1}(V))$. Can't say much in general about its stalks.
:::

::: {.front card-id="card-77682f622e066702"}
What is the restriction of a sheaf?
:::

::: {.back card-id="card-77682f622e066702"}
For $\iota: X\hookrightarrow Y$, ${ \left.{{{\mathcal{G}}}} \right|_{{X}} } \coloneqq\iota^{-1}{\mathcal{F}}$, same stalks as ${\mathcal{G}}$.
:::

::: {.front card-id="card-42718a4202cf6938"}
What is a **flasque sheaf**?
:::

::: {.back card-id="card-42718a4202cf6938"}
$U\hookrightarrow V \implies {\mathcal{F}}(V) \twoheadrightarrow{\mathcal{F}}(U)$.
:::

::: {.front card-id="card-29a3dfbf0b8411fd"}
Discuss flasque sheaves.
:::

::: {.back card-id="card-29a3dfbf0b8411fd"}
$H^{\geq 1}(X; {\mathcal{F}}) = 0$ for any flasque sheaf on any topological space, so are $\Gamma{\hbox{-}}$acyclic.
:::

::: {.front card-id="card-096a65dfbddd6a03"}
What is **Grothendieck vanishing**?
:::

::: {.back card-id="card-096a65dfbddd6a03"}
For $X$ a noetherian topological space, for all ${\mathcal{F}}\in {\mathsf{Sh}}(X, {\mathsf{Ab}}{\mathsf{Grp}})$, one has
$$H^{i\geq \dim X+1}(X; {\mathcal{F}}) = 0.$$
How to remember: $\mathrm{cd}(X) \leq \dim X$.
:::

::: {.front card-id="card-51fc917eb022892e"}
Is a morphism of sheaves injective if injective on sections? Surjective?
:::

::: {.back card-id="card-51fc917eb022892e"}
Injective: yes, surjective: no.
:::

::: {.front card-id="card-b5dfbf872b61db5b" tags="definition"}
What is: sheaf kernel/cokernel
:::

::: {.back card-id="card-b5dfbf872b61db5b"}
The kernel of $F\to G$ is the subsheaf $U\mapsto\ker(F(U)\to G(U))$. The cokernel is the sheafification of $U\mapsto\operatorname{coker}(F(U)\to G(U))$; a section of the sheaf cokernel need only have local representatives.
:::
