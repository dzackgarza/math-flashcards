---
title: "Algebraic Geometry::Moduli::K3 Moduli"
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

::: {.front card-id="card-2eef1a10735a855d"}
What is the moduli space of all K3s vs projective K3s?
:::

::: {.back card-id="card-2eef1a10735a855d"}
All K3s, including non-projective: $\dcosetr{\Omega}{{\operatorname{O}}(\Lambda_{\mathrm{K3}})}$, 20-dimensional. Its points are the isomorphism classes of K3s, but the quotient is not Hausdorff, since ${\operatorname{O}}(\Lambda_{\mathrm{K3}})$ does not act properly discontinuously on $\Omega$.

Algebraic (projective) K3s: 19-dimensional, since one has to vary periods in the orthogonal complement of an ample class.
:::

::: {.front card-id="card-a3226206edbadebd"}
What are the dimensions of moduli of all and just algebraic Kummer surfaces?
:::

::: {.back card-id="card-a3226206edbadebd"}
All: 4-dimensional

Algebraic: 3-dimensional.
:::

::: {.front card-id="card-e5204c524e5af7fb"}
Define the period domain $\mathbb{D}$. What is its dimension?
:::

::: {.back card-id="card-e5204c524e5af7fb"}
$$\mathbb{D} = \Omega \coloneqq\left\{{[\omega]\in {\mathbf{P}}(\Lambda_{{\mathsf{K}}3}\otimes_\ZZ\CC) \st\omega^2 = 0,\,\, \omega.\overline{\omega }> 0}\right\}$$
In coordinates that diagonalize the form on $\Lambda_{\mathrm{K3}}\otimes{\mathbf{R}}$ with signature $(3, 19)$,
$$\Omega \cong \left\{{{\left[ {z_0:\cdots:z_{21}} \right]}\in {\mathbf{P}}^{21}\st z_0^2+z_1^2 + z_2^2 - z_3^2 -\cdots - z_{21}^2 = 0,\, {\left\lvert {z_0} \right\rvert}^2 + {\left\lvert {z_1} \right\rvert}^2 + {\left\lvert {z_2} \right\rvert}^2 - {\left\lvert {z_3} \right\rvert}^2 - \cdots - {\left\lvert {z_{21}} \right\rvert}^2 > 0}\right\}$$
which is an open subset of a quadric in ${\mathbf{P}}^{21}$ and thus a 20-dimensional $\CC\dash$manifold.

For a marking $\Phi: H^2(X;\ZZ)\to \Lambda_{\mathrm{K3}}$, the period of $(X, \Phi)$ is $\Phi(\CC\omega_X) \in \Omega$, where $\CC\omega_X = H^{2,0}(X) \in {\mathbf{P}}H^2(X;\CC)$. Surjectivity of the period map (Todorov, Looijenga, Siu): every point of $\Omega$ is the period of some marked K3.

For a marked polarized K3 $(X, \phi)$, drops 1 dimension:
$$\mathbb{D}_{2k} \coloneqq\left\{{[\omega]\in \mathbb{D}\st\omega.h = 0}\right\}$$
where $h\in \Lambda_{{\mathsf{K}}3}$ is a fixed primitive class with $h^2 = 2k$ and $\phi^{-1}(h)\in \NS(X)^\amp$. It is 19-dimensional, with two connected components, each a bounded symmetric domain of type IV.
:::

::: {.front card-id="card-a7590df0a74c3577"}
What is a marking of a K3?
:::

::: {.back card-id="card-a7590df0a74c3577"}
Let $X$ be a K3 surface. A marking is an isometry $\phi: H^2(X; \ZZ) { \, \xrightarrow{\sim}\, }\Lambda_{{\mathsf{K}}3}$, where $\Lambda_{{\mathsf{K}}3}$ (also written $L$) is the K3 lattice $U{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  }$.
:::

::: {.front card-id="card-4bf015e09e65996f"}
What is the dimension of quartics in ${\mathbf{P}}^3$? Up to coordinate changes?
:::

::: {.back card-id="card-4bf015e09e65996f"}
$h^0({\mathcal{O}}_{{\mathbf{P}}^3}(4)) = {4+3\choose 4} = 35$ and its projective dimension is 34.

$\dim \operatorname{PGL}_4(\CC) = 16-1 = 15$

So $34-15 = 19$ moduli.
:::

::: {.front card-id="card-feb6d5dd0d9fef49"}
What are the dimensions of moduli for $S_{2,3}, S_{2,2,2}$, and the double plane $S\to {\mathbf{P}}^2$?
:::

::: {.back card-id="card-feb6d5dd0d9fef49"}
All 19.
:::

::: {.front card-id="card-b5a57050c6bdb637"}
Compute the dimension of moduli of K3s with an order 3 symplectic automorphism.
:::

::: {.back card-id="card-b5a57050c6bdb637"}
For algebraic complex K3 surfaces, the dimension is $7$. An order-three symplectic automorphism has six fixed points. The Lefschetz formula gives $6=2+\operatorname{tr}(\sigma^*|H^2)$; with eigenvalue multiplicities $a$ for $1$ and $b$ for each primitive cube root, $a-b=4$ and $a+2b=22$. Thus $a=10$, $b=6$, and the coinvariant lattice has rank $12$ in $\operatorname{NS}(X)$. An invariant ample class raises the generic Picard rank to $13$, leaving $20-13=7$ moduli. Families attain this bound (Garbagnati–Sarti, *Symplectic automorphisms of prime order on K3 surfaces*, §5).
:::

::: {.front card-id="card-3669e4b341b8e820"}
Describe the period map of a single K3.
:::

::: {.back card-id="card-3669e4b341b8e820"}
Pick $\omega\in H^{2, 0}(X) \subseteq H^2(X;\CC)$ a nonvanishing holomorphic 2-form.

Check the cup product satisfies $\omega^2 = 0$ and $\omega.\overline{\omega }> 0$.

Extend a marking $\phi$ to $\phi_\CC: H^2(X;\CC)\to \Lambda_{{\mathsf{K}}3}\otimes_\ZZ\CC$.

Check $\operatorname{im}\phi_\CC= \mathop{\mathrm{span}}_\CC\left\{{\phi_\CC(\omega)}\right\}$ is a line through the origin

Thus $\operatorname{im}\phi \in \mathbb{D}$.
:::

::: {.front card-id="card-5123fd7566ad8ab0"}
How is $\mathbb{D}$ related to moduli of K3s?
:::

::: {.back card-id="card-5123fd7566ad8ab0"}
Weak Torelli: $X { \, \xrightarrow{\sim}\, }X' \iff$ there is an isometry $H^2(X;\ZZ) { \, \xrightarrow{\sim}\, }H^2(X';\ZZ)$ whose $\CC\dash$linear extension preserves Hodge decompositions. So two K3s are isomorphic iff they admit markings defining the same point in $\mathbb{D}$.

Local Torelli: for a marked K3 $(X, \phi)$, the period map from the versal deformation space to $\mathbb{D}$ is a local isomorphism.

Surjectivity: every $d\in \mathbb{D}$ is a period point for some marked K3.

Thus almost a coarse moduli space: families $\mcx\to B$ yield $B\to \mathbb{D}$ and points correspond to iso classes, but quotienting by change-of-marking yields a non-Hausdorff quotient since it does not act properly discontinuously.
:::

::: {.front card-id="card-95ea8d364c6151bd"}
Describe the period map of a family of K3s.
:::

::: {.back card-id="card-95ea8d364c6151bd"}
Let $f:\mcx\to B$ be a flat family with fiber $X$.

Choosing a marking $\phi: H^2(X;\ZZ) { \, \xrightarrow{\sim}\, }\Lambda_{{\mathsf{K}}3}$ extends to a sheaf morphism $\phi_B: {\mathbf{R}}^2 f_*\underline{\ZZ}\to\underline{\Lambda_{{\mathsf{K}}3}}$ where the latter is a constant sheaf.

Yields a holomorphic map $B\to \mathbb{D}$.
:::

::: {.front card-id="card-31b8cfe1587ec0da"}
What is a semistable degeneration?
:::

::: {.back card-id="card-31b8cfe1587ec0da"}
$\pi:\mcx\to \Delta$ with $\mcx$ smooth and central fiber reduced normal crossings.
:::

::: {.front card-id="card-75f1921216084ec3"}
What is the dual graph of a degeneration?
:::

::: {.back card-id="card-75f1921216084ec3"}
Let $S_0=\bigcup V_i$ be the central fibre in a semistable degeneration. Define the dual graph $\Gamma$ of $S_0$ as follows: $\Gamma$ is a simplicial complex whose vertices $P_1, \ldots, P_r$ correspond to the components $V_1, \ldots, V_r$ of $S_0$; the $k$-simplex $\left\langle P_{i_0}, \ldots, P_{i_k}\right\rangle$ belongs to $\Gamma$ if and only if $V_{i_0} \cap \cdots \cap V_{i_k} \neq \emptyset$.
:::
