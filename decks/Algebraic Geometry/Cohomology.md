---
title: "Algebraic Geometry::Cohomology"
---

::: {.front card-id="card-d87ef906950bd548"}
What is a **limit**? A **colimit**?
:::

::: {.back card-id="card-d87ef906950bd548"}
How to remember: limits are like sequences and live above (sequences project), colimits are like gluing and live below (include into disjoint unions) <https://q.uiver.app/?q=WzAsMTUsWzAsNCwiQV97aS0xfSJdLFswLDMsIlxcdmRvdHMiXSxbMCwyLCJBX3tpKzF9Il0sWzQsMywiXFxjZG90cyJdLFs1LDMsIkYoQV97aS0xfSkiXSxbNiwzLCJcXGNkb3RzIl0sWzcsMywiRihBX3tpKzF9KSJdLFs4LDMsIlxcY2RvdHMiXSxbMCwxLCJcXHZkb3RzIl0sWzAsNSwiXFx2ZG90cyJdLFs2LDIsIlxcdW5kZXJzZXR7XFxsb25nbGVmdGFycm93fXtcXG1hdGhybXtsaW19fVxcLCBGICJdLFs2LDQsIlxcdW5kZXJzZXR7XFxsb25ncmlnaHRhcnJvd317XFxtYXRocm17Y29saW19fVxcLCBGIl0sWzYsMCwiXFxmb3JhbGwgTCJdLFs2LDYsIlxcZm9yYWxsIEMiXSxbMCwwXSxbMyw0XSxbNCw1XSxbNSw2XSxbMCwxXSxbMSwyXSxbMiw4XSxbOSwwXSxbMTAsNF0sWzEwLDZdLFs0LDExXSxbNiwxMV0sWzEyLDQsIiIsMix7ImN1cnZlIjoyfV0sWzEyLDEwLCJcXGV4aXN0cyAhIiwyLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEyLDYsIiIsMix7ImN1cnZlIjotMn1dLFs0LDEzLCIiLDIseyJjdXJ2ZSI6Mn1dLFs2LDEzLCIiLDIseyJjdXJ2ZSI6LTJ9XSxbMTEsMTMsIlxcZXhpc3RzICEiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbNiw3XSxbMTksMTUsIkYiLDAseyJjdXJ2ZSI6LTMsInNob3J0ZW4iOnsic291cmNlIjoyMCwidGFyZ2V0IjoyMH19XV0=>https://q.uiver.app/?q=WzAsMTUsWzAsNCwiQV97aS0xfSJdLFswLDMsIlxcdmRvdHMiXSxbMCwyLCJBX3tpKzF9Il0sWzQsMywiXFxjZG90cyJdLFs1LDMsIkYoQV97aS0xfSkiXSxbNiwzLCJcXGNkb3RzIl0sWzcsMywiRihBX3tpKzF9KSJdLFs4LDMsIlxcY2RvdHMiXSxbMCwxLCJcXHZkb3RzIl0sWzAsNSwiXFx2ZG90cyJdLFs2LDIsIlxcdW5kZXJzZXR7XFxsb25nbGVmdGFycm93fXtcXG1hdGhybXtsaW19fVxcLCBGICJdLFs2LDQsIlxcdW5kZXJzZXR7XFxsb25ncmlnaHRhcnJvd317XFxtYXRocm17Y29saW19fVxcLCBGIl0sWzYsMCwiXFxmb3JhbGwgTCJdLFs2LDYsIlxcZm9yYWxsIEMiXSxbMCwwXSxbMyw0XSxbNCw1XSxbNSw2XSxbMCwxXSxbMSwyXSxbMiw4XSxbOSwwXSxbMTAsNF0sWzEwLDZdLFs0LDExXSxbNiwxMV0sWzEyLDQsIiIsMix7ImN1cnZlIjoyfV0sWzEyLDEwLCJcXGV4aXN0cyAhIiwyLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEyLDYsIiIsMix7ImN1cnZlIjotMn1dLFs0LDEzLCIiLDIseyJjdXJ2ZSI6Mn1dLFs2LDEzLCIiLDIseyJjdXJ2ZSI6LTJ9XSxbMTEsMTMsIlxcZXhpc3RzICEiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbNiw3XSxbMTksMTUsIkYiLDAseyJjdXJ2ZSI6LTMsInNob3J0ZW4iOnsic291cmNlIjoyMCwidGFyZ2V0IjoyMH19XV0=
:::

::: {.front card-id="card-75b0cf56e062765b"}
What is an **abelian category**?
:::

::: {.back card-id="card-75b0cf56e062765b"}
$\mathsf{C}(A, B) \in {\mathsf{Ab}}{\mathsf{Grp}}$ and composition is a group morphism,

All Finite direct sums

All kernels and cokernels

Mono = $\ker(\operatorname{coker})$.

Epi $= \operatorname{coker}(\ker)$.

Epi-mono factorization for all morphisms
:::

::: {.front card-id="card-089cfeaeedd8d036"}
What is a **delta functor**?
:::

::: {.back card-id="card-089cfeaeedd8d036"}
A collection $T^n$ ($T^{> 0}$ are *satellite functors*) and for each $A\hookrightarrow B\twoheadrightarrow C$ a collection of morphisms $\delta^n: T^n(C) \to T^n(A)$ fitting into a LES, and for each morphism of SESs $\xi_1\to \xi_1$ the $\delta^n$ fit into commuting squares.
:::

::: {.front card-id="card-f2225028df666042"}
What is a **universal delta functor**?
:::

::: {.back card-id="card-f2225028df666042"}
$\delta = (T^n)$ is universal iff for any other delta functor $(S^n)$ and any morphism $f^0: T^0\to S^0$ of functors there exist lifts $f^i: T^i \to S^i$ which commute with the $\delta^i$.
:::

::: {.front card-id="card-84dafb6fde17d894"}
What is a **homotopy** between maps $f,g: A\to B$ of complexes?
:::

::: {.back card-id="card-84dafb6fde17d894"}
A morphism $k: A \to B[1]$, so $k^i: A^i\to B^{i-1}$, with $f-g = dk + kd$.
:::

::: {.front card-id="card-6b282cf8ba9d9f58"}
What is an **additive** functor?
:::

::: {.back card-id="card-6b282cf8ba9d9f58"}
$F$ is additive iff $\mathsf{C}(A, B)\to \mathsf{D}(FA, FB)$ is a group morphism.
:::

::: {.front card-id="card-2c05ae67c19d8075"}
What is a **left exact functor**?
:::

::: {.back card-id="card-2c05ae67c19d8075"}
Additive and $A\hookrightarrow B\twoheadrightarrow C \leadsto FA \hookrightarrow FB \to FC \to \cdots$.
:::

::: {.front card-id="card-9a24470a30061150"}
What are the variance and exactness of hom functors?
:::

::: {.back card-id="card-9a24470a30061150"}
Both are left-exact (just remember $\mathop{\mathrm{\mathbb{R}Hom}}$), $\mathsf{C}(A, {-})$ is covariant and $\mathsf{C}({-}, A)$ is contravariant.
:::

::: {.front card-id="card-d4171256cc976c1e"}
What is an **injective resolution** of $A$?
:::

::: {.back card-id="card-d4171256cc976c1e"}
$A \xrightarrow{{\varepsilon}} I^0 \to I^1 \to \cdots$ an exact complex with $I^j$ injective objects
:::

::: {.front card-id="card-d51a653fa3481330"}
What is an **injective object**?
:::

::: {.back card-id="card-d51a653fa3481330"}
Remembering injectives and projectives: <https://q.uiver.app/?q=WzAsNSxbMCwyLCJBIl0sWzIsMiwiQiJdLFs0LDIsIkMiXSxbMCw0LCJJIl0sWzQsMCwiUCJdLFswLDEsIiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzEsMiwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoiZXBpIn19fV0sWzQsMl0sWzAsM10sWzQsMSwiXFxleGlzdHMgXFxpZmYgQyBcXHRleHR7IHByb2plY3RpdmV9IiwyLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEsMywiXFxleGlzdHMgXFxpZmYgQSBcXHRleHR7IGluamVjdGl2ZX0iLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XV0=>
:::

::: {.front card-id="card-e37ad2148e34f1cb"}
What is a **(co)effaceable functor**?
:::

::: {.back card-id="card-e37ad2148e34f1cb"}
For each $A$ there is a mono $u: A\to I$ with $F(u) = 0$. Coeffaceable if there is an epi $u: P\to A$ with $F(u) = 0$.
:::

::: {.front card-id="card-6fd5f64c060e98bb"}
Discuss **effaceable functors**.
:::

::: {.back card-id="card-6fd5f64c060e98bb"}
If $T$ is a delta functor and each $T^i$ is effaceable then $T$ is universal. Derived functors computed via injective resolutions form a universal $\delta$ functor.
:::

::: {.front card-id="card-dc50c39867acc702"}
Why does ${}_{{\mathcal{O}}_X}{\mathsf{Mod}}$ have enough injectives?
:::

::: {.back card-id="card-dc50c39867acc702"}
For ${\mathcal{F}}\in   {}_{{\mathcal{O}}_X}{\mathsf{Mod}}$, the stalk ${\mathcal{F}}_{x} \in   {}_{{\mathcal{O}}_{X, x}}{\mathsf{Mod}}$ and module categories have enough injectives. So find ${\mathcal{F}}_x \hookrightarrow I_x$, let $j^x: \left\{{x}\right\} \hookrightarrow X$ and set ${\mathcal{I}}\coloneqq\prod_{x\in x} j^x_*(I_x)$; claim this is injective. Check
$$\mathop{\mathrm{Hom}}_{{\mathcal{O}}_X}({\mathcal{G}}, {\mathcal{I}}) = \prod_{x\in X} \mathop{\mathrm{Hom}}_{{\mathcal{O}}_X}({\mathcal{G}}, j^x_* I_x) = \prod_{x\in X} \mathop{\mathrm{Hom}}_{{\mathcal{O}}_{X, x}}({\mathcal{G}}_x, I_x)$$
So one gets a sheaf morphism ${\mathcal{F}}\to {\mathcal{I}}$ induced by ${\mathcal{F}}_x \to {\mathcal{I}}_x$ which is injective. Claim: $\mathop{\mathrm{Hom}}_{{\mathcal{O}}_X}({-}, {\mathcal{I}})$ is exact. Use that it is $\prod_{x\in X}({-})_x$, the product of stalk functors (which is exact) followed by $\mathop{\mathrm{Hom}}_{{\mathcal{O}}_{X, x}}({-}, I_x)$ (which is exact). I.e. it's a composition of exact functors:
$$\mathop{\mathrm{Hom}}_{{\mathcal{O}}_X}({-}, {\mathcal{I}}) = \mathop{\mathrm{Hom}}_{{\mathcal{O}}_{X, x}}({-}, I_x) \circ \prod_{x\in X} ({-})_x$$
:::

::: {.front card-id="card-6ebf3e3244b6ee35"}
What is the **higher direct image**?
:::

::: {.back card-id="card-6ebf3e3244b6ee35"}
Idea: for a family $f:X\to Y$, a form of relative cohomology of $X$ over $Y$ or cohomology along the fibers of $f$. $f_*: {\mathsf{Sh}}(X; {\mathsf{Ab}}{\mathsf{Grp}})\to{\mathsf{Sh}}(Y; {\mathsf{Ab}}{\mathsf{Grp}})$ left exact, so take right-derived functors. Can be computed using flasque resolutions.\
:::

::: {.front card-id="card-7c74fccd355ba8a2"}
Discuss **higher direct images**.
:::

::: {.back card-id="card-7c74fccd355ba8a2"}
If ${\mathbf{R}}^i f_* {\mathcal{F}}= 0$ for $i>0$ then $H^i(X; {\mathcal{F}}) { \, \xrightarrow{\sim}\, }H^i(Y, f_* {\mathcal{F}})$. ${\mathbf{R}}^if_*({\mathcal{F}})$ is the sheafification of $V\mapsto H^i(f^{-1}(V); { \left.{{{\mathcal{F}}}} \right|_{{f^{-1}(V)}} })$.
:::

::: {.front card-id="card-8e70c9d4c2c1b1b1"}
Discuss higher direct images for morphisms $f:X\to \operatorname{Spec}A$.
:::

::: {.back card-id="card-8e70c9d4c2c1b1b1"}
Let $M_i \coloneqq H^i(X; {\mathcal{F}})$, then ${\mathbf{R}}^i f_* {\mathcal{F}}= \tilde M_i$.
:::

::: {.front card-id="card-c05f6f48457e723e"}
What is a **flasque** or **flabby** sheaf?
:::

::: {.back card-id="card-c05f6f48457e723e"}
$V\subseteq U \implies F(U) \twoheadrightarrow F(V)$. Any flasque is injective and thus $\Gamma{\hbox{-}}$acyclic.
:::

::: {.front card-id="card-29097df5554a634a"}
Give examples of flasque sheaves.
:::

::: {.back card-id="card-29097df5554a634a"}
$\tilde M \in {\mathsf{QCoh}}(\operatorname{Spec}A)$ for $M\in   {}_{A}{\mathsf{Mod}}$ an injective object.
:::

::: {.front card-id="card-8e4c415bc760a4cd"}
What is a **fine** sheaf?
:::

::: {.back card-id="card-8e4c415bc760a4cd"}
Sheaves admitting a partition of unity: for any ${\mathcal{U}}\rightrightarrows X$ there exist $\phi_i: {\mathcal{F}}(U_i) \to {\mathcal{F}}(U)$ where for all $s\in{\mathcal{F}}(U)$ one has $\mathop{\mathrm{supp}}(s(U_i)) \subseteq U_i$ and $\sum_i \phi_i({ \left.{{s}} \right|_{{U_i}} }) = s$.

Equivalently: for every two disjoint $A, B\subseteq X$, there exists $f\in { \operatorname{End} }({\mathcal{F}})$ such that ${ \left.{{f}} \right|_{{A}} } = \operatorname{id}$ and ${ \left.{{f}} \right|_{{B}} } = 0$.

More generally, for all ${\mathcal{U}}\rightrightarrows X, \exists 1=\sum f_i$ subordinate to the cover.

Fine implies soft.
:::

::: {.front card-id="card-88283a5b704c6e21"}
What is the **tangent sheaf**?
:::

::: {.back card-id="card-88283a5b704c6e21"}
${\mathbf{T}}_X \coloneqq\Omega_{X/k} {}^{ \vee }\coloneqq {\mathcal{H}}\kern-0.5pt{\operatorname{om}}_{{\mathcal{O}}_X}(\Omega_{X/k}, {\mathcal{O}}_X)$, locally free of rank $\dim X$.
:::

::: {.front card-id="card-2578e6e4881e953d"}
What is the **geometric genus** in full generality?
:::

::: {.back card-id="card-2578e6e4881e953d"}
$p_g(X) \coloneqq h^{n, 0}(X) \coloneqq H^0(\omega_X)$, the number of linearly-independent top forms.
:::

::: {.front card-id="card-037ffa2cb5372691"}
What are the **conormal** sheaf and the **normal sheaf**?
:::

::: {.back card-id="card-037ffa2cb5372691"}
For $Y\hookrightarrow X$ a closed embedding of smooth varieties, $N_{Y/X} {}^{ \vee }\coloneqq{\mathcal{I}}_Y/{\mathcal{I}}_Y^2$ is the conormal sheaf and $N_{Y/X} = ({\mathcal{I}}_Y/{\mathcal{I}}_Y^2) {}^{ \vee }$ is the normal sheaf, which is locally free of rank $\operatorname{codim}_X(Y)$.
:::

::: {.front card-id="card-c30e1b1de3ce90bd"}
What is a **derivation**?
:::

::: {.back card-id="card-c30e1b1de3ce90bd"}
$d\in \mathop{\mathrm{Der}}_A(B, M) \iff d$ is additive and $d(b_1b_2) = d(b_1)b_2 + b_1d(b_2)$ where $d(a) = 0$ for all $a\in A$.
:::

::: {.front card-id="card-30c6432017c0b3b9"}
What is the module of relative differentials $\Omega_{B/A}$?
:::

::: {.back card-id="card-30c6432017c0b3b9"}
$\Omega_{B/A}\in   {}_{B}{\mathsf{Mod}}$ with $d\in \mathop{\mathrm{Der}}_A(B, \Omega_{B/A})$ satisfying a universal property: for any $M\in   {}_{B}{\mathsf{Mod}}$ and $d'\in \mathop{\mathrm{Der}}_A(B, M)$, it factors through $d$. Can be constructed as $\mathsf{Free}_B(db {~\mathrel{\Big\vert}~}b\in B)/R$ where $R$ are relations $d(b_1+b_2)-d(b_1)-d(b_2), da, d(b_1b_2)-d(b_1)b_2-b_1d(b_2)$.
:::

::: {.front card-id="card-9fcd3600930c58fb"}
What is the **sheaf of differentials** or **relative differential forms**?
:::

::: {.back card-id="card-9fcd3600930c58fb"}
For $f:X\to Y$, embed $X$ as a locally closed subscheme $X\hookrightarrow W \coloneqq\Delta_{X/Y}$ with sheaf of ideals ${\mathcal{I}}$ and define $\Omega_{X/Y} \coloneqq\Delta^*({\mathcal{I}}/{\mathcal{I}}^2) \in {\mathsf{QCoh}}(X)$. The local derivations glue to $d:{\mathcal{O}}_X\to \Omega_{X/Y}$.
:::

::: {.front card-id="card-8c48673ca22f6b18"}
What are the two SESs for sheaves of differentials?
:::

::: {.back card-id="card-8c48673ca22f6b18"}
For $X \xrightarrow{f} Y \xrightarrow{g} Z$,
$$f^* \Omega_{Y / Z} \rightarrow \Omega_{X / Z} \rightarrow \Omega_{X / Y} \rightarrow 0$$
. For $f:X\to Y$ and $Z\leq X$ a closed subscheme with ideal sheaf ${\mathcal{I}}$,
$$\mathscr{I} / \mathscr{I}^2 \stackrel{\delta}{\rightarrow} \Omega_{X / Y} \otimes \mathcal{O}_Z \rightarrow \Omega_{Z / Y} \rightarrow 0$$
:::

::: {.front card-id="card-5f3e42595989e5b5"}
What is the **geometric genus** and the **arithmetic genus** for curves and for general schemes?
:::

::: {.back card-id="card-5f3e42595989e5b5"}
For a smooth projective curve, $p_a(X) = h^1({\mathcal{O}}_X)$ and $p_g(X) =h^0(\omega_X)$. More generally, $p_a(X) \coloneqq(-1)^{\dim X} (\chi({\mathcal{O}}_X)-1)$ and $p_g(X) = h^0(\Omega_{X/k})$
:::

::: {.front card-id="card-213db50f27de0ed0"}
What is **Cech cohomology**?
:::

::: {.back card-id="card-213db50f27de0ed0"}
For an open cover ${\mathcal{U}}\rightrightarrows X$, define
$$C^p({\mathcal{U}}; {\mathcal{F}}) \coloneqq\prod_{I \coloneqq i_0 < \cdots < i_p} {\mathcal{F}}(U_{I}),\qquad U_{I} \coloneqq U_{i_1}\cap\cdots \cap U_{i_p}$$
with boundary map
$$(d\alpha)_{I} \coloneqq\sum_{0\leq k\leq p+1} (-1)^k \alpha_{I\setminus i_k}\mathrel{\Big|}_{U_I}$$
More explicitly,
$$C^p({\mathcal{U}}; {\mathcal{F}}) = \prod_{i_1 < \cdots < i_p} {\mathcal{F}}(U_{i_1} \cap\cdots \cap U_{i_p})$$
So a $p{\hbox{-}}$chain is a collection of elements $\alpha_{i_1,\cdots, i_p} \in {\mathcal{F}}(U_{i_1\cdots i_p})$ for each $(p+1){\hbox{-}}$tuple of elements $i_1 < \cdots < i_p$ in $I$ where ${\mathcal{U}}\coloneqq\left\{{U_i}\right\}_{i\in I}$. The boundary map is
$$(d \alpha)_{i_0, \ldots, i_{p+1}}=\sum_{k=0}^{p+1}(-1)^k \alpha_{i_0}, \ldots, \widehat{i}_k, \ldots, i_{p+1} \mathrel{\Big|}_{U_{i_0, \ldots, i_{p+1}}}$$
:::

::: {.front card-id="card-e0452aa13f84cac6"}
Give an example of a computation with Cech cohomology.
:::

::: {.back card-id="card-e0452aa13f84cac6"}
See example 4.0.3 on page 219 and example 4.0.4 for $S^1$.

$H^*({\mathbf{P}}^1; \Omega_{{\mathbf{P}}^1/k})$ over $k$: let ${\mathcal{U}}= \left\{{H_0, H_\infty}\right\}$ with coordinates $x$ and $1/x$, then:
$$\begin{align} 0 \to C^0 &\to C^1\to 0 \\ 0 \to {{\Gamma}\qty{H_0; \Omega} } \times {{\Gamma}\qty{H_\infty;\Omega} } &\to {{\Gamma}\qty{H_0\cap H_\infty;\Omega} } \\ 0 \to k[x]\,dx\times k[y]\,dy&\xrightarrow{d: x\mapsto x, y\mapsto 1/x, dy\mapsto -x^{-2}\,dx} k[x, x^{-1}]\,dx\to 0\end{align}$$
Then $\ker d = \left\langle{f(x)\,dx, g(y)\,dy}\right\rangle$ such that $f(x) = -x^{-2} g(x^{-1}) \implies f=g=0$ since one side is a polynomial in $x$ and the other is a polynomial in $1/x$ with no constant term, so $H^0 = 0$.

For $H^1$, check that $\operatorname{im}d = \left\langle{f(x) + x^{-2} g(x^{-1})\,dx}\right\rangle$ where $f,g$ are polynomials. This is the subspace of $k[x,x^{-1}]\,dx$ generated by $x^n\,dx$ for $n\in {\mathbf{Z}}\setminus\left\{{ -1 }\right\}$, so $H^1 = \left\langle{x^{-1}\,dx}\right\rangle$ is 1-dimensional.

The circle:
:::

::: {.front card-id="card-b3dc6977ff83178a"}
When does Cech cohomology compute sheaf cohomology?
:::

::: {.back card-id="card-b3dc6977ff83178a"}
For $X$ a Noetherian separated scheme and ${\mathcal{F}}\in {\mathsf{QCoh}}(X)$. (Thm 4.5) Alternatively, whenever ${\mathcal{F}}$ has no cohomology on any open in a cover ${\mathcal{U}}$.
:::

::: {.front card-id="card-7b6fdb224bdd77f2"}
What is a **regular immersion**?
:::

::: {.back card-id="card-7b6fdb224bdd77f2"}
An immersion whose sheaf of ideals is regular, where ${\mathcal{I}}\leq {\mathcal{O}}_X$ is regular iff for every $x\in \mathop{\mathrm{supp}}({\mathcal{O}}_X/{\mathcal{I}})$ admits an open neighborhood $U$ and a regular sequence $f_1,\cdots, f_r\in {\mathcal{O}}_X(U)$ generating ${ \left.{{{\mathcal{I}}}} \right|_{{U}} }$.
:::

::: {.front card-id="card-f6ef6d64003c7e76"}
What are consequences of a morphism being flat?
:::

::: {.back card-id="card-f6ef6d64003c7e76"}
The Hilbert polynomials of all fibers are the same.

If $f:X\to Y$ with $X,Y$ finite type over a field, $\dim_x X_y = \dim_x X - \dim_y Y$ where $\dim_x X \coloneqq\dim {\mathcal{O}}_{X, x}$.

For ${\mathcal{X}}\to C^\circ$ a flat family of closed subschemes of ${\mathbf{P}}^n$ over a punctured curve $C^\circ$, one can "pass to the limit": given $Y$ regular integral of dimension 1 and $p\in Y$ a closed point, let $Y^\circ \coloneqq Y\setminus\left\{{ p }\right\}$ and $X\subseteq {\mathbf{P}}^n_{Y^\circ}$ be a closed subscheme which is flat over $Y^\circ$; then $\exists ! \tilde X \subseteq {\mathbf{P}}^n_{Y}$ a closed subscheme flat over $Y$ which restricts to $X$.
:::

::: {.front card-id="card-f29f14b3c651a2c2"}
Give an example and a non-example of a flat morphism.
:::

::: {.back card-id="card-f29f14b3c651a2c2"}
Example: any open immersion, $\tilde M$ over $A$ for any $M \in   {}_{A}{\mathsf{Mod}}^\flat$. Any smooth morphism by miracle flatness Non-example: any blowup, since the fibers jump in dimension.
:::

::: {.front card-id="card-069f1fe38915b1c4"}
What is an **associated point**?
:::

::: {.back card-id="card-069f1fe38915b1c4"}
$x\in X$ where every element of ${\mathfrak{m}}_x$ is a zero divisor.
:::

::: {.front card-id="card-1f647ebbef5efd37"}
What is a **flat family**?
:::

::: {.back card-id="card-1f647ebbef5efd37"}
Any morphism ${\mathcal{X}}\to X$ of schemes to $X$ which is flat.
:::

::: {.front card-id="card-3c776a71df041421"}
How can one check if a morphism is flat?
:::

::: {.back card-id="card-3c776a71df041421"}
For $f: X\to Y$ with $Y$ integral and regular of dimension 1, $f$ is flat iff every *associated point* maps to $\eta_Y$. For $X$ reduced, this says every irreducible component of $X$ dominates $Y$.
:::

::: {.front card-id="card-16b1ac8dbea48ede"}
What are some properties not preserved in a flat family?
:::

::: {.back card-id="card-16b1ac8dbea48ede"}
Being irreducible or reduced, Picard numbers, generally most things that aren't related to Hilbert polynomials.
:::

::: {.front card-id="card-7b0ae0c2f2899228"}
What is **Serre's vanishing** characterization of affine schemes among Noetherian schemes?
:::

::: {.back card-id="card-7b0ae0c2f2899228"}
For $X\in {\mathsf{Sch}}$ Noetherian, $X$ is affine $\iff H^{i\geq 1}(X; {\mathcal{F}}) = 0$ for all ${\mathcal{G}}\in {\mathsf{QCoh}}(X)$ $\iff H^1(X; {\mathcal{I}}) = 0$ for all coherent sheaves of ideals ${\mathcal{I}}$.

Equivalently, $X$ is affine $\iff \mathrm{cd}(X) = 0$; this is the *cohomological dimension*, the least $n$ such that $H^i({\mathcal{F}}) = 0$ for all $i> n$ and for all ${\mathcal{F}}\in {\mathsf{QCoh}}(X)$.

Another **Serre vanishing**: for $X \in {\mathsf{Sch}}_{/ {A}}$ projective and $A$ Noetherian with ${\mathcal{O}}_X(1)$ very ample over $\operatorname{Spec}A$, if ${\mathcal{F}}\in {\mathsf{Coh}}(X)$ then $H^i({\mathcal{F}}(n)) = 0$ for $n\gg 0$ and every $i>0$.
:::

::: {.front card-id="card-9f661756ec76f08d"}
Discuss cohomology for ${\mathsf{QCoh}}(\operatorname{Spec}A)$.
:::

::: {.back card-id="card-9f661756ec76f08d"}
$H^{i\geq 1}(\operatorname{Spec}A, {\mathcal{F}}) = 0$ for any ${\mathcal{F}}\in {\mathsf{QCoh}}(\operatorname{Spec}A)$. Why: let $M = {{\Gamma}\qty{X; {\mathcal{F}}} }$ and take $M\hookrightarrow I$ an injective resolution in ${}_{A}{\mathsf{Mod}}$ to get an exact sequence $\tilde M \hookrightarrow\tilde I \in {\mathsf{QCoh}}(X)$. Check ${\mathcal{F}}\cong \tilde M$ by an early result and each $\tilde I^i$ is flasque thus $\Gamma{\hbox{-}}$acyclic, so use it to compute cohomology. Apply ${{\Gamma}\qty{X; {-}} }$ to $0\to \tilde M\to \tilde I$ to get $0\to M\to I\in   {}_{A}{\mathsf{Mod}}$ and thus $H^0({\mathcal{F}}) = M$ and $H^i({\mathcal{F}}) = 0$ for $i\geq 1$.
:::

::: {.front card-id="card-81d3dee3bf3d5a16"}
What is $H^i(X; {\mathcal{O}}_X(n))$ for $X \coloneqq{\mathbf{P}}^r_{/ {A}}$?
:::

::: {.back card-id="card-81d3dee3bf3d5a16"}
Write $\Gamma^*({\mathcal{F}}) \coloneqq\bigoplus_{n\geq 0} H^0(X; {\mathcal{O}}_X(n))$ for the section ring, then $A[x_0,\cdots, x_r]  { \, \xrightarrow{\sim}\, }\Gamma({\mathcal{O}}_X)$ as graded rings. So $H^0(X; {\mathcal{O}}_X(n)) \cong A[x_0, \cdots, x_r]_n$, degree $n$ homogeneous polynomials over $A$.

$H^i(X; {\mathcal{O}}_X(n)) = 0$ for $0<i<r$ and every $n$.

$H^r(X; {\mathcal{O}}_X(-(r+1))) = A$.
:::

::: {.front card-id="card-c86c46b3d1c22faa"}
What is the **Hilbert polynomial** of a sheaf?
:::

::: {.back card-id="card-c86c46b3d1c22faa"}
A polynomial $p\in {\mathbf{Q}}[z]$ such that $p(n) = \chi({\mathcal{F}}(n))$ for every $n$.
:::

::: {.front card-id="card-847e440e17d15caf"}
When is an invertible sheaf ample?
:::

::: {.back card-id="card-847e440e17d15caf"}
For $A$ Noetherian and $X\in {\mathsf{Sch}}_{/ {A}}$ proper, ${\mathcal{L}}$ is ample $\iff \forall {\mathcal{F}}\in {\mathsf{Coh}}(X)$ one has $H^i({\mathcal{L}}\otimes{\mathcal{F}}^n) = 0$ for $n\gg 0$ and every $i$.
:::

::: {.front card-id="card-24f0f5d5999e4fbf"}
What is **Serre duality**?
:::

::: {.back card-id="card-24f0f5d5999e4fbf"}
For $X$ smooth proper of dimension $n$ and ${\mathcal{L}}\in {\mathsf{Coh}}(X)$ there is a perfect pairing
$$ H^i(X;{\mathcal{L}}) \otimes H^{n-i}(X; {\mathcal{K}}\otimes{\mathcal{L}} {}^{ \vee }) \to H^n(X;{\mathcal{K}}) \cong {\mathbf{C}}\implies H^i(X;{\mathcal{L}}) \cong H^{n-i}(X; {\mathcal{K}}\otimes{\mathcal{L}} {}^{ \vee }) {}^{ \vee }$$
For curves
$$H^0(C; {\mathcal{L}}) \cong H^1(C; {\mathcal{K}}\otimes{\mathcal{L}} {}^{ \vee }) {}^{ \vee }$$
Consequence for Hodge numbers:
$$h^i(X; {\mathcal{L}}) = h^{n-i}(X; {\mathcal{K}}\otimes{\mathcal{L}} {}^{ \vee }),\qquad \chi(X; {\mathcal{L}}) = (-1)^n \chi(X; {\mathcal{K}}\otimes{\mathcal{L}} {}^{ \vee })$$
:::

::: {.front card-id="card-69f8989719a40f16"}
How is $\operatorname{Pic}(X)$ related to cohomology?
:::

::: {.back card-id="card-69f8989719a40f16"}
$\operatorname{Pic}(X) \cong H^1(X; {\mathcal{O}}_X^{\times})$. Idea: use Cech cohomology, pick ${\mathcal{L}}\in \operatorname{Pic}(X)$, restrict to opens where ${ \left.{{{\mathcal{L}}}} \right|_{{U_i}} }$ is free, fix isos $\phi_i: {\mathcal{O}}_{U_i} { \, \xrightarrow{\sim}\, }{ \left.{{{\mathcal{L}}}} \right|_{{U_i}} }$, check that on $U_{ij}$ one gets isomorphisms $\phi_i^{-1}\phi_j: {\mathcal{O}}_{U_{ij}}{\circlearrowleft}$ which give an element in ${\check{H}}({\mathcal{U}}; {\mathcal{O}}_X^{\times})$, take a limit over all coverings.
:::

::: {.front card-id="card-822818bff1088759"}
What is the **exponential exact sequence**?
:::

::: {.back card-id="card-822818bff1088759"}
$$2\pi i {\mathbf{Z}}\hookrightarrow{\mathcal{O}}_X \twoheadrightarrow{\mathcal{O}}_X^{\times}$$
Since $H^1({\mathcal{O}}_X) = \operatorname{Pic}(X)$, $\delta^1 = c_1({-}) \in H^2(2\pi i {\mathbf{Z}})$ is the first Chern class.
:::

::: {.front card-id="card-1f21f65d8810cd17"}
What is the **conormal exact sequence**?
:::

::: {.back card-id="card-1f21f65d8810cd17"}
How to derive:
$${\mathbf{T}}_X \hookrightarrow{\mathbf{T}}_Y \twoheadrightarrow N_{X/Y} \quad\underset{\text{dualize}}{\leadsto}\quad N_{X/Y} {}^{ \vee }\to j^*\Omega_{Y/Z} \twoheadrightarrow\Omega_{X/Z}.$$
:::

::: {.front card-id="card-25c14144c18e5ef3"}
What is the **Euler exact sequence**?
:::

::: {.back card-id="card-25c14144c18e5ef3"}
For $X \coloneqq{\mathbf{P}}^n _{/ {A}}$, dualize ${\mathcal{O}}_X\hookrightarrow{\mathcal{O}}_X(1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\twoheadrightarrow{\mathbf{T}}_X$ to get the sequence
$$\Omega^1_{X}\hookrightarrow{\mathcal{O}}_X(-1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\twoheadrightarrow{\mathcal{O}}_X$$
:::

::: {.front card-id="card-1ad7a8deaabeb009"}
What is $\omega_X$ for $X = {\mathbf{P}}^n_{/ {A}}$? Derive it.
:::

::: {.back card-id="card-1ad7a8deaabeb009"}
Take determinants in the Euler exact sequence $\Omega^1_{X}\hookrightarrow{\mathcal{O}}_X(-1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\twoheadrightarrow{\mathcal{O}}_X$ to get $\operatorname{det}{\mathcal{O}}_X(-1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  } = \omega_X \otimes{\mathcal{O}}_X = \omega_X$ and so $\omega_X = {\mathcal{O}}_X(-(n+1))$.
:::

::: {.front card-id="card-37dc6345919da7f9"}
What are the two main exact sequences for modules of algebraic differentials?
:::

::: {.back card-id="card-37dc6345919da7f9"}
The composition exact sequence: for $A\to B\to C$,
$$\Omega_{B / A} \otimes_B C \rightarrow \Omega_{C / A} \rightarrow \Omega_{C / B} \rightarrow 0 \in   {}_{C}{\mathsf{Mod}}$$
The "conormal" exact sequence: for $B\in  \mathsf{Alg}_{A}, I{~\trianglelefteq~}B, C\coloneqq B/I$,
$$I / I^2 \stackrel{\delta}{\rightarrow} \Omega_{B / A} \otimes_B C \rightarrow \Omega_{C / A} \rightarrow 0\in   {}_{C}{\mathsf{Mod}}$$
:::

::: {.front card-id="card-884b60a5d4ee268a"}
What is the composition exact sequence for $X\to Y\to Z$?
:::

::: {.back card-id="card-884b60a5d4ee268a"}
At the level of sheaves,
$$f^* \Omega_{Y/Z} \to \Omega_{X/Z} \to \Omega_{X/Y} \to 0 \qquad \in {\mathsf{Sh}}_X$$
How to remember:
:::

::: {.front card-id="card-80827d05561a93ed"}
What is the conormal exact sequence for an immersion $C\hookrightarrow S$?
:::

::: {.back card-id="card-80827d05561a93ed"}
At the level of sheaves on $C$, for $\iota: C\hookrightarrow S$,
$$N_{C/S} {}^{ \vee }\to \iota^*\Omega_{S/k} \twoheadrightarrow\Omega_{C/k}\to 0 \qquad \in {\mathsf{Sh}}(C)$$
where $N_{C/S} {}^{ \vee }\coloneqq I_C/I_C^2$ which is a sheaf version of: if $C,S\in   {}_{R}{\mathsf{Mod}}$ with $\iota: C\twoheadrightarrow S$ a surjection with kernel $I$
$$I/I^2 \to \Omega_{C/R}\otimes_R S \twoheadrightarrow\Omega_{S/R}\to 0 \qquad\in  {}_{S}{\mathsf{Mod}}$$
For $C \subseteq S$ a closed subscheme and $f:S\to T$, can rewrite this as
$$ {\mathcal{I}}_C / {\mathcal{I}}_C^2 \to \Omega_{S/T} \otimes{\mathcal{O}}_C \twoheadrightarrow\Omega_{C/T}\to 0 \qquad \in {\mathsf{Sh}}_C$$
:::

::: {.front card-id="card-00941d78f8260900"}
Compute the canonical sheaf for $Y$ a smooth hypersurface of degree $d$ in ${\mathbf{P}}^n$ for $n\geq 2$.
:::

::: {.back card-id="card-00941d78f8260900"}
Use that for $Y\hookrightarrow X$ one has $\omega_Y = \omega_X \otimes\operatorname{det}N_{Y/X} = \omega_X \otimes{\mathcal{O}}_X(Y) \otimes{\mathcal{O}}_Y$ for codimension 1 and $X = {\mathbf{P}}^n \implies \omega_X = {\mathcal{O}}_X(-n-1)$ and so
$$\omega_Y = {\mathcal{O}}_X(-n-1) \otimes{\mathcal{O}}_{{\mathbf{P}}^n}(Y) \otimes{\mathcal{O}}_Y = {\mathcal{O}}_Y(-n-1+d)$$
:::

::: {.front card-id="card-65a63ab68d3c91f4"}
Compute the canonical sheaf of a smooth plane curve of degree $d$ and its degree.
:::

::: {.back card-id="card-65a63ab68d3c91f4"}
For $X\subseteq {\mathbf{P}}^n$ a hypersurface one has $\omega_X = {\mathcal{O}}_X(d-n-1)$, here $n=2$ so $\omega_X = {\mathcal{O}}_X(d-3)$. Since $\deg {\mathcal{O}}_X(1) = d$, we have $\deg \omega_X = d(d-3)$.
:::

::: {.front card-id="card-a167931134065e17"}
Show that a smooth plane curve of degree $d\geq 4$ is not rational.
:::

::: {.back card-id="card-a167931134065e17"}
$\omega_X = {\mathcal{O}}_X(d-3)$ and $d-3>0$ so $p_g(X) > 0$, and a curve is rational iff $p_g(X) = 0$.
:::

::: {.front card-id="card-594fc45f771e7003" tags="definition"}
What is: Dualizing sheaf and Serre duality
:::

::: {.back card-id="card-594fc45f771e7003"}
For a smooth proper connected curve $X/k$, the dualizing sheaf is $\omega_X=\Omega^1_{X/k}$. Serre duality gives $H^1(X,L)^\vee\cong H^0(X,\omega_X\otimes L^{-1})$ for every invertible sheaf $L$. In dimension $n$, it pairs $H^i(X,F)$ with $\operatorname{Ext}^{n-i}(F,\omega_X)$.
:::

::: {.front card-id="card-65cfb8efb1626b1d" tags="definition"}
What is: relation to the canonical sheaf
:::

::: {.back card-id="card-65cfb8efb1626b1d"}
On a smooth $n$-dimensional variety over a field, the canonical sheaf is $\omega_X=\bigwedge^n\Omega^1_{X/k}$, which is also the dualizing sheaf. On a singular scheme the dualizing object need not be an invertible sheaf.
:::
