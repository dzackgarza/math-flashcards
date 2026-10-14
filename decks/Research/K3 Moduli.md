---
title: "Research::K3 Moduli"
---

::: {.front card-id="card-b0772e9197fde462"}
Discuss the moduli space of marked K3s.
:::

::: {.back card-id="card-b0772e9197fde462"}
Admits a fine moduli space $\mcm$

Has a surjective etale period map
$$\begin{align}\pi: \mcm&\to \mathbb{D}\\ (X, \phi) &\mapsto \phi(H^{2, 0}(X)) \in {\mathbf{P}}(L\otimes\CC)\end{align}$$
Non-Hausdorff 20-dimensional $\CC\dash$manifold.

$\pi_0 \mcm= \left\{{\mcm_-, \mcm_+}\right\}$ two isomorphic connected components where are exchanged under $(X, \phi)\rightleftharpoons(X, -\phi)$.
:::

::: {.front card-id="card-f4d846ca75dbd06c"}
For $\rho \in {\operatorname{O}}(L)$, what is a $\rho\dash$marking of $(X, \sigma)$? What is $\rho\dash$markable?
:::

::: {.back card-id="card-f4d846ca75dbd06c"}
For $L = \Lambda_{\mathrm{K3}}$, a $\rho$-marking of $(X, \sigma)$ is an isometry $\phi: H^2(X, \mathbb{Z}) \rightarrow L$ such that $\sigma^*=\phi^{-1} \circ \rho \circ \phi$.

We say that $(X, \sigma)$ is $\rho$-markable if it admits a $\rho$-marking.
:::

::: {.front card-id="card-7432a08d3fb9ca0e"}
What is a family of $\rho\dash$marked surfaces?
:::

::: {.back card-id="card-7432a08d3fb9ca0e"}
A smooth morphism $f:(\mcx, \sigma_B) \to B$

An automorphism $\sigma_B \in \mathop{\mathrm{Aut}}(X)$ over $B$

An isomorphism f local systems $\phi_S: {\mathbf{R}}^2f_* \underline{\ZZ} \to L\otimes\underline{\ZZ}_B$ where every fiber is a K3 with a $\rho\dash$marking.
:::

::: {.front card-id="card-c5cd55f831d1f567"}
What are the moduli stacks $\mcm_\rho, F_\rho$?
:::

::: {.back card-id="card-c5cd55f831d1f567"}
$\mcm_\rho$: moduli of $\rho\dash$marked K3 surfaces, e.g. $\mcm_\rho(B)$ is the groupoid of $\rho\dash$marked families over $B$.

$F_\rho$: moduli of $\rho\dash$markable K3 surfaces.
:::

::: {.front card-id="card-19661256489998b1"}
What is a stable pair $(S, {\varepsilon}D)$? Give an example.
:::

::: {.back card-id="card-19661256489998b1"}
slc singularities and ${\mathsf{K}}_S + {\varepsilon}D$ an ample $\QQ\dash$Cartier divisor.

A stable slc surface pair is a pair $(S, \epsilon D)$, where

$S$ is a connected, reduced, projective Gorenstein surface with $\omega_S \simeq \mathcal{O}_S$ which has semi log canonical singularities.

$D$ is an effective ample Cartier divisor on $S$ that does not contain any log canonical centers of $S$.

Thus $(S, {\varepsilon}D)$ is stable for small ${\varepsilon}> 0 \in \QQ$.

Example: any K3 $X$ with ADE singularities and any effective ample divisor $R$. It is CY ($\omega_X\cong {\mathcal{O}}_X$), has canonical singularities (better than slc), and has no log canonical centers.
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
What is the classification of Kulikov models?
:::

::: {.back card-id="card-4b6f92d8bb327f64"}
Write $\pi: \mcx\to \Delta$ for a semistable degeneration of K3s with $\omega_{\mcx}\cong {\mathcal{O}}_{\mcx}$ where all components of $\mcx_0$ are Kahler.

Type I: $\mcx_0$ is a smooth K3. No double curves, no triple points.

Type II: $\mcx_0$ is a chain of elliptic ruled components with rational surfaces at each end, where all double curves are smooth elliptic. Double curves but no triple points.

Type III: $\mcx_0$ is rational surfaces meeting along rational curves, which form cycles in each component, and the dual complex $\Gamma$ is a triangulation of $S^2$. Triple points.
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
Any degeneration of K3s can be converted to a Kulikov model after a base change and birational modification.

For $Y^*\to C^*$ a family of algebraic K3s, there is a finite base change $(C', 0) \to (C, 0)$ and a birational modification of its pullback $Y'\dashrightarrow X$ such that $X$ has smooth total space, $K_X \sim_{C'} 0$, and $X_0$ is reduced normal crossings.
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
$$Nx = (x\cdot \lambda)\delta - (x\cdot \delta)\lambda,\qquad \delta\in H^2(X_t; \ZZ), \lambda \in \delta^\perp/\delta$$
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

::: {.front card-id="card-73c1ede663f47ad5"}
What is a $(\rho, \chi)\dash$marking of $(X, \sigma)$
:::

::: {.back card-id="card-73c1ede663f47ad5"}
Let $\rho: G\hookrightarrow{\operatorname{O}}(L)$ be finite subgroup, $\chi: G\to {\CC^{\times}}$ a character, and $\sigma: G\to \mathop{\mathrm{Aut}}(X)$.

Marking: an isometry $H^2(X; \ZZ) \to L$ where $\phi \circ \sigma(g)^* = \rho(g) \circ \phi$ such that the induced character $\alpha: G\to {\CC^{\times}}$ equals $\chi$.
:::

::: {.front card-id="card-e1ee23dc3c9549c9"}
What is a family of $(\rho, \chi)\dash$marked K3s?
:::

::: {.back card-id="card-e1ee23dc3c9549c9"}
A smooth model $(\chi, \sigma_B, \phi_B) \xrightarrow{f} B$ where $\sigma_B: G\to \mathop{\mathrm{Aut}}(\mcx/B)$ and $\phi_B: {\mathbf{R}}^2 f_* \underline{\ZZ} \to L\otimes\underline{\ZZ}_B$ where every fiber is a $(\rho, \chi)\dash$marked surface.
:::

::: {.front card-id="card-4072dbd12abda6c8"}
What is the change-of-markings group?
:::

::: {.back card-id="card-4072dbd12abda6c8"}
$\Gamma_\rho \coloneqq\left\{{\gamma\in {\operatorname{O}}(L) \st\gamma\circ \rho = \rho \circ \gamma}\right\}$.
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
The irreducible coarse moduli space of polarized complex K3s $(X, L)$ with ADE singularities and $L\in \operatorname{Pic}(X)^{\amp, \prim}$ with $L^2 = 2d$.

Writing $2d = 2g-2$, this is $F_g$, the moduli of polarized K3s of genus $g\geq 2$.

An arithmetic quotient of a type IV domain, i.e. a Shimura variety for $\SO_{2, 19}({\mathbf{R}})$; smooth K3s form an open subset.

Quasiprojective, $\dim F_{2d} = 19$ for each $d$.
:::

::: {.front card-id="card-681a11bbc6a0be2c"}
What is $F_\rho^{\mathrm{ade}}$?
:::

::: {.back card-id="card-681a11bbc6a0be2c"}
$(\mathbb{D}_\rho \setminus\Delta_\rho)/\Gamma_\rho$

Obtained from smooth K3s by contracting $(-2)\dash$curves orthogonal to $C_1 \in  \mathrm{Fix}(\sigma)$ with $g\geq 2$

Has a separated stack.
:::

::: {.front card-id="card-6e339cb955627865"}
What is $\overline{F_\rho}^\mathrm{slc}$?
:::

::: {.back card-id="card-6e339cb955627865"}
The geometrically meaningful compactification Valery constructs, stable pairs w/automorphisms

Main theorem: is a semitoroidal compactification of $\mathbb{D}_\rho/\Gamma_\rho$.
:::

::: {.front card-id="card-ac88b51027b8331a"}
What is $\Delta_\rho$?
:::

::: {.back card-id="card-ac88b51027b8331a"}
Discriminant locus: $\mathbb{D}_\rho \cap\bigcup_{\text{roots }\delta \in (L^G)^\perp} \delta^\perp$.

$L^G \coloneqq \mathrm{Fix}(\rho) \subset S_\rho$ the fixed classes for $G = \left\langle{\rho}\right\rangle$

$L \coloneqq\Lambda_{\mathrm{K3}}$.

$S_\rho \coloneqq T_\rho^\perp$, $T_\rho \coloneqq L^\prim_\CC\cap L$ generic Picard/transcendental lattices.

$L^\prim_\CC$ the sum of primitive eigenspaces of $\rho$.
:::

::: {.front card-id="card-f1f9e680ce07e9ba"}
How does an involution act on $H^2$?
:::

::: {.back card-id="card-f1f9e680ce07e9ba"}
Fixes $S_X$ and acts by $\cdot(-1)$ on $T_X$.
:::

::: {.front card-id="card-f6dea11f91a6b646"}
Classify $(X, \sigma)$ with $\sigma$ a nonsymplectic involution, up to deformation.
:::

::: {.back card-id="card-f6dea11f91a6b646"}
By the invariant lattice $S = H^2(X; \ZZ)^\sigma$: a primitive 2-elementary hyperbolic sublattice $S \subseteq \Lambda_{\mathrm{K3}}$. Nikulin classified these using $(r, a, \delta)$, equivalently $(g, k, \delta)$: 75 cases.
:::

::: {.front card-id="card-beee68f3907963f4"}
What is the importance of a recognizable divisor?
:::

::: {.back card-id="card-beee68f3907963f4"}
If $R$ is recognizable, then $\overline{F_\rho}^{\mathrm{slc}}$ is a semitoroidal compactification of $F_\rho$ for a unique semifan $\mcf_R$.
:::

::: {.front card-id="card-77e273a483fa5164"}
What is the Baily-Borel compactification associated to a lattice $N$ with isometry $\rho$?
:::

::: {.back card-id="card-77e273a483fa5164"}
$\mathbb{D}_N \coloneqq\left\{{x\in {\mathbf{P}}(N\otimes\CC)\st x^2=0, {\left\lvert {x} \right\rvert} > 0}\right\}$ a type IV domain

$\mathbb{D}_\rho = \left\{{x\in {\mathbf{P}}(N\otimes\CC)^{\zeta_n} \st{\left\lvert {x} \right\rvert} > 0}\right\}$ a Type I subdomain

$\tilde \Gamma_\rho \coloneqq Z_{{\operatorname{O}}(N)}(\rho)\curvearrowright\mathbb{D}_\rho$, and also for any finite index subgroup $\Gamma$.

Set $\overline{\mathbb{D}_\rho}$ the closure of the compact dual (dropping ${\left\lvert {x} \right\rvert} > 0$)

Define $\overline{\mathbb{D}_\rho}^\mathrm{BB} = \mathbb{D}_\rho \cup\bigcup_{J} B_J$ by adding *rational boundary components*, usually ${\mathbb{H}}{\textstyle\coprod}(-{\mathbb{H}})$ or points.

BB compactification is $\overline{\mathbb{D}_\rho/\Gamma}\coloneqq\overline{\mathbb{D}_\rho}^{\mathrm{BB}}/\Gamma$.
:::
