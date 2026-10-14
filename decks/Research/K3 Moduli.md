---
title: "Research::K3 Moduli"
---

::: {.front card-id="card-b0772e9197fde462"}
Discuss the moduli space of marked K3s.
:::

::: {.back card-id="card-b0772e9197fde462"}
Admits a fine moduli space ${\mathcal{M}}$

Has a surjective etale period map
$$\begin{align}\pi: {\mathcal{M}}&\to \mathbb{D}\\ (X, \phi) &\mapsto \phi(H^{2, 0}(X)) \in {\mathbf{P}}(L\otimes{\mathbf{C}})\end{align}$$
Non-Hausdorff 20-dimensional ${\mathbf{C}}{\hbox{-}}$manifold.

$\pi_0 {\mathcal{M}}= \left\{{{\mathcal{M}}_-, {\mathcal{M}}_+}\right\}$ two isomorphic connected components where are exchanged under $(X, \phi)\rightleftharpoons(X, -\phi)$.
:::

::: {.front card-id="card-f4d846ca75dbd06c"}
For $\rho \in {\operatorname{O}}(L)$, what is a $\rho{\hbox{-}}$marking?
:::

::: {.back card-id="card-f4d846ca75dbd06c"}
A $\rho$-marking of $(X, \sigma)$ is an isometry $\phi: H^2(X, \mathbb{Z}) \rightarrow L$ such that $\sigma^*=\phi^{-1} \circ \rho \circ \phi$. We say that $(X, \sigma)$ is $\rho$-markable if it admits a $\rho$-marking.
:::

::: {.front card-id="card-7432a08d3fb9ca0e"}
What is a family of $\rho{\hbox{-}}$marked surfaces?
:::

::: {.back card-id="card-7432a08d3fb9ca0e"}
A smooth morphism $f:({\mathcal{X}}, \sigma_B) \to B$

An automorphism $\sigma_B \in \mathop{\mathrm{Aut}}(X)$ over $B$

An isomorphism f local systems $\phi_S: {\mathbf{R}}^2f_* \underline{{\mathbf{Z}}} \to L\otimes\underline{{\mathbf{Z}}}_B$ where every fiber is a K3 with a $\rho{\hbox{-}}$marking.
:::

::: {.front card-id="card-c5cd55f831d1f567"}
What are the moduli stacks ${\mathcal{M}}_\rho, F_\rho$?
:::

::: {.back card-id="card-c5cd55f831d1f567"}
Moduli of $\rho{\hbox{-}}$marked resp. $\rho{\hbox{-}}$markable K3 surfaces, where e.g. ${\mathcal{M}}_\rho(B)$ is the groupoid of $\rho{\hbox{-}}$marked families over $B$.
:::

::: {.front card-id="card-258e4cde5f4ec632"}
How are deformation classes of K3 surfaces with nonsymplectic automorphisms $(X, \sigma)$ classified?
:::

::: {.back card-id="card-258e4cde5f4ec632"}
Primitive 2-elementary hyperbolic sublattices $S \subseteq L_{{\mathsf{K}}3}$.
:::

::: {.front card-id="card-19661256489998b1"}
What is a stable pair $(S, {\varepsilon}D)$? Give an example.
:::

::: {.back card-id="card-19661256489998b1"}
slc singularities and ${\mathsf{K}}_S + {\varepsilon}D \in {\mathbf{Q}}{\hbox{-}}\operatorname{CDiv}(X)^{\mathrm{amp}}$.

Any K3 $X$ with ADE singularities and any effective ample divisor $R$, since $\omega_X\cong {\mathcal{O}}_X \implies$ canonical singularities and there are no log centers.
:::

::: {.front card-id="card-11b89d75f2ba234f"}
What is a stable slc surface pair?
:::

::: {.back card-id="card-11b89d75f2ba234f"}
A stable slc surface pair is a pair $(S, \epsilon D)$, where

$S$ is a connected, reduced, projective Gorenstein surface $S$ with $\omega_S \simeq \mathcal{O}_S$ which has semi log canonical singularities.

$D$ is an effective ample Cartier divisor on $S$ that does not contain any log canonical centers of $S$.

Thus $(S, \exp D)$ is stable for small ${\varepsilon}> 0 \in {\mathbf{Q}}$.
:::

::: {.front card-id="card-c21ec1bb268a318e"}
What is a canonical choice of polarizing divisor?
:::

::: {.back card-id="card-c21ec1bb268a318e"}
An algebraically varying big and nef $R \in \operatorname{Div}(U)$ for $U$ a Zariski dense subset of $F_\rho$.
:::

::: {.front card-id="card-7c387d6e0e37b1ee"}
What is a Kulikov model?
:::

::: {.back card-id="card-7c387d6e0e37b1ee"}
Let $(C, 0)$ be the germ of a smooth curve at $0$ and $C^* = C\setminus\left\{{0}\right\}$ and let $X^* \to C^*$ be a family of algebraic K3s.

$X \to (C, 0)$ which extends $X^* \to C^*$ where $X$ is a smooth algebraic space,

$K_X \sim_C 0$,

$X_0$ has reduced normal crossings
:::

::: {.front card-id="card-4b6f92d8bb327f64"}
What are Types I, II, II of Kulikov models?
:::

::: {.back card-id="card-4b6f92d8bb327f64"}
I: $X_0$ smooth,

II: $X_0$ has double curves but no triple points,

III: $X_0$ has triple points
:::

::: {.front card-id="card-83b6a861985d607a"}
What is a Kulikov surface?
:::

::: {.back card-id="card-83b6a861985d607a"}
$X_0$ the central fiber of a Kulikov model.
:::

::: {.front card-id="card-34ee9fdbfea0ed5c"}
What is Kulikov's key result on degenerations of K3s?
:::

::: {.back card-id="card-34ee9fdbfea0ed5c"}
For $Y^*\to C^*$ a family, there is a finite base change $(C', 0) \to (C, 0)$ and a birational modification of its pullback $Y'\dashrightarrow X$ such that $X$ has smooth total space, $K_X \sim_{C'} 0$, and $X_0$ is reduced normal crossings.
:::

::: {.front card-id="card-000de75a6010754a"}
What are the log monodromies for Kulikov degenerations.
:::

::: {.back card-id="card-000de75a6010754a"}
Define $N \coloneqq\log T = (T-I) - {1\over 2}(T-I)^2 + \cdots$

Type I $\implies N = 0$.

Type II $\implies N\neq 0, N^2 = 0$.

Type III $\implies N \neq 0, N^2 \neq 0, N^3=0$.

$N$ is always integral and of the form
$$Nx = (x\cdot \lambda)\delta - (x\cdot \delta)\lambda,\qquad \delta\in H^2(X_t; {\mathbf{Z}}), \lambda \in \delta^\perp/\delta$$
:::

::: {.front card-id="card-1337dfaa959f59d5"}
What is a **recognizable divisor**?
:::

::: {.back card-id="card-1337dfaa959f59d5"}
A canonical choice of polarizing divisor $R$ for $U \subset F_\rho$ is **recognizable** if

For every Kulikov surface $X_0$ of Type I, II, or III which smooths to some $\rho$-markable $\mathrm{K} 3$ surface,

There is a divisor $R_0 \subset X_0$ such that on any smoothing into $\rho$-markable K3 surfaces $X \rightarrow(C, 0)$ with $C^* \subset U$,

The divisor $R_0$ is, up to the action of$\mathop{\mathrm{Aut}}^0\left(X_0\right)$, the flat limit of $R_t$ for $t \neq 0 \in C^*$.
:::

::: {.front card-id="card-871e3f72e6855780"}
When is $G\subseteq \mathop{\mathrm{Aut}}(X)$ nonsymplectic?
:::

::: {.back card-id="card-871e3f72e6855780"}
$G\curvearrowright H^{2, 0}(X) = {\mathbf{C}}\omega_X$ gives a SES
$$G_0 \hookrightarrow G \twoheadrightarrow\mu_n,\qquad \mu_n\in {{\mathbf{C}}^{\times}}$$
and $G$ is non symplectic if $G\ne G_0$.
:::

::: {.front card-id="card-73c1ede663f47ad5"}
What is a $(\rho, \chi){\hbox{-}}$marking of $(X, \sigma)$
:::

::: {.back card-id="card-73c1ede663f47ad5"}
Let $\rho: G\hookrightarrow{\operatorname{O}}(L)$ be finite subgroup, $\chi: G\to {{\mathbf{C}}^{\times}}$ a character, and $\sigma: G\to \mathop{\mathrm{Aut}}(X)$.

Marking: an isometry $H^2(X; {\mathbf{Z}}) \to L$ where $\phi \circ \sigma(g)^* = \rho(g) \circ \phi$ such that the induced character $\alpha: G\to {{\mathbf{C}}^{\times}}$ equals $\chi$.
:::

::: {.front card-id="card-e1ee23dc3c9549c9"}
What is a family of $(\rho, \chi){\hbox{-}}$marked K3s?
:::

::: {.back card-id="card-e1ee23dc3c9549c9"}
A smooth model $(\chi, \sigma_B, \phi_B) \xrightarrow{f} B$ where $\sigma_B: G\to \mathop{\mathrm{Aut}}({\mathcal{X}}/B)$ and $\phi_B: {\mathbf{R}}^2 f_* \underline{{\mathbf{Z}}} \to L\otimes\underline{{\mathbf{Z}}}_B$ where every fiber is a $(\rho, \chi){\hbox{-}}$marked surface.
:::

::: {.front card-id="card-4072dbd12abda6c8"}
What is the change-of-markings group?
:::

::: {.back card-id="card-4072dbd12abda6c8"}
$\Gamma_\rho \coloneqq\left\{{\gamma\in {\operatorname{O}}(L) {~\mathrel{\Big\vert}~}\gamma\circ \rho = \rho \circ \gamma}\right\}$.
:::

::: {.front card-id="card-b1d78709d3678358"}
What is a semitoroidal compactification?
:::

::: {.back card-id="card-b1d78709d3678358"}
Simultaneously generalizes BB and toroidal compactifications.
:::

::: {.front card-id="card-858f92b97e0db0b0"}
What is $F_{2d}$?
:::

::: {.back card-id="card-858f92b97e0db0b0"}
Moduli of polarized K3s $(X, L)$,

ADE singularities,

$L\in \operatorname{Pic}(X)^{{\mathrm{amp}}, {\operatorname{prim}}}$ with $L^2 = 2d$
:::

::: {.front card-id="card-581f4b720509da01"}
What is $F_\rho$?
:::

::: {.back card-id="card-581f4b720509da01"}
Moduli of $\rho{\hbox{-}}$markable K3s.
:::

::: {.front card-id="card-681a11bbc6a0be2c"}
What is $F_\rho^{\mathrm{ade}}$?
:::

::: {.back card-id="card-681a11bbc6a0be2c"}
$(\mathbb{D}_\rho \setminus\Delta_\rho)/\Gamma_\rho$

Obtained from smooth K3s by contracting $(-2){\hbox{-}}$curves orthogonal to $C_1 \in  \mathrm{Fix}(\sigma)$ with $g\geq 2$

Has a separated stack.
:::

::: {.front card-id="card-6e339cb955627865"}
What is $\overline{F_\rho}^\mathrm{slc}$?
:::

::: {.back card-id="card-6e339cb955627865"}
The geometrically meaningful compactification Valery constructs, stable pairs w/automorphisms

Main theorem: is a semitoroidal compactification of $\mathbb{D}_\rho/\Gamma_\rho$.
:::

::: {.front card-id="card-4cc1f994590eae37"}
What are the lattice signatures for $S_X, T_X$?
:::

::: {.back card-id="card-4cc1f994590eae37"}
$S_X: (1, \rho - 1)$

$T_X: (2, 20-\rho)$.
:::

::: {.front card-id="card-ac88b51027b8331a"}
What is $\Delta_\rho$?
:::

::: {.back card-id="card-ac88b51027b8331a"}
Discriminant locus: $\mathbb{D}_\rho \cap\bigcup_{\text{roots }\delta \in (L^G)^\perp} \delta^\perp$.

$L^G \coloneqq \mathrm{Fix}(\rho) \subset S_\rho$ the fixed classes for $G = \left\langle{\rho}\right\rangle$

$L \coloneqq\Lambda_{\mathrm{K3}}$.

$S_\rho \coloneqq T_\rho^\perp$, $T_\rho \coloneqq L^{\operatorname{prim}}_{\mathbf{C}}\cap L$ generic Picard/transcendental lattices.

$L^{\operatorname{prim}}_{\mathbf{C}}$ the sum of primitive eigenspaces of $\rho$.
:::

::: {.front card-id="card-f1f9e680ce07e9ba"}
How does an involution act on $H^2$?
:::

::: {.back card-id="card-f1f9e680ce07e9ba"}
Fixes $S_X$ and acts by $\cdot(-1)$ on $T_X$.
:::

::: {.front card-id="card-f6dea11f91a6b646"}
Classify $(X, \sigma)$ with $\sigma$ an involution, up to deformation.
:::

::: {.back card-id="card-f6dea11f91a6b646"}
Primitive 2-elementary sublattices $S \leq \Lambda_{\mathrm{K3}}$, classified by Nikulin using $(g, k, \delta)$, 75 cases.
:::

::: {.front card-id="card-c1eb89a76c7d96b3"}
What is the Picard number $\rho(X)$?
:::

::: {.back card-id="card-c1eb89a76c7d96b3"}
For $X$ compact complex,
$$\rho(X) \coloneqq\operatorname{rank}_{\mathbf{Z}}\operatorname{im}(\operatorname{Pic}(X) \to H^{1, 1}(X))$$
If $X$ is Kahler, $\rho(X) = \operatorname{rank}H^{1,1}(X) = \operatorname{rank}{\operatorname{NS}}(X)$.
:::

::: {.front card-id="card-124bcc550fa595fc"}
For $\rho \in {\operatorname{O}}(L)$, what is a $\rho{\hbox{-}}$marking of $(X, \sigma)$? What is $\rho{\hbox{-}}$markable?
:::

::: {.back card-id="card-124bcc550fa595fc"}
An isometry $\phi: H^2(X, \mathbb{Z}) \rightarrow \Lambda_{\mathrm{K3}}$ such that $\sigma^*=\phi^{-1} \circ \rho \circ \phi$.

We say that $(X, \sigma)$ is $\rho$-markable if it admits a $\rho$-marking.
:::

::: {.front card-id="card-c2a5cc29eb61a8ad"}
Give an example of a stable slc pair.
:::

::: {.back card-id="card-c2a5cc29eb61a8ad"}
Any K3 $X$ with ADE singularities and any effective ample divisor $R$,

CY: $\omega_X\cong {\mathcal{O}}_X$

Has canonical singularities, better than slc

No log centers.
:::

::: {.front card-id="card-beee68f3907963f4"}
What is the importance of a recognizable divisor?
:::

::: {.back card-id="card-beee68f3907963f4"}
If $R$ is recognizable, then $\overline{F_\rho}^{\mathrm{slc}}$ is a semitoroidal compactification of $F_\rho$ for a unique semifan ${\mathcal{F}}_R$.
:::

::: {.front card-id="card-77e273a483fa5164"}
What is the Baily-Borel compactification associated to a lattice $N$ with isometry $\rho$?
:::

::: {.back card-id="card-77e273a483fa5164"}
$\mathbb{D}_N \coloneqq\left\{{x\in {\mathbf{P}}(N\otimes{\mathbf{C}}){~\mathrel{\Big\vert}~}x^2=0, {\left\lvert {x} \right\rvert} > 0}\right\}$ a type IV domain

$\mathbb{D}_\rho = \left\{{x\in {\mathbf{P}}(N\otimes{\mathbf{C}})^{\zeta_n} {~\mathrel{\Big\vert}~}{\left\lvert {x} \right\rvert} > 0}\right\}$ a Type I subdomain

$\tilde \Gamma_\rho \coloneqq Z_{{\operatorname{O}}(N)}(\rho)\curvearrowright\mathbb{D}_\rho$, and also for any finite index subgroup $\Gamma$.

Set $\overline{\mathbb{D}_\rho}$ the closure of the compact dual (dropping ${\left\lvert {x} \right\rvert} > 0$)

Define $\overline{\mathbb{D}_\rho}^\mathrm{BB} = \mathbb{D}_\rho \cup\bigcup_{J} B_J$ by adding *rational boundary components*, usually ${\mathbb{H}}{\textstyle\coprod}(-{\mathbb{H}})$ or points.

BB compactification is $\overline{\mathbb{D}_\rho/\Gamma}\coloneqq\overline{\mathbb{D}_\rho}^{\mathrm{BB}}/\Gamma$.
:::
