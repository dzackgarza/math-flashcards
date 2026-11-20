---
title: "Algebraic Geometry::Moduli::K3 Moduli"
---

::: {.front card-id="period-cusps-isotropic-flags-groups" tags="definition construction" cite="[@AEGS25, §§2.3, 3.1–3.3, 3.8–3.9]"}
For a type-IV arithmetic quotient of dimension $n$, describe Baily–Borel cusps, their incidence, and the group acting on a zero-cusp cone. How does a primitive lattice inclusion induce cusp maps?
:::

::: {.back card-id="period-cusps-isotropic-flags-groups"}
Let $N$ have signature $(2,n)$ and $\Gamma\subset O^+(N)$ be arithmetic.

| Primitive isotropic sublattice | Boundary | Lattice used |
| --- | --- | --- |
| Line $J=\mathbb Ze$ | Point | $J^\perp/J$, signature $(1,n-1)$ |
| Plane $I$ | Arithmetic quotient of a half-plane | $I^\perp/I$, negative definite |

Take $\Gamma$-orbits, not just isometry classes of quotient lattices. Incidence means that representatives satisfy $J\subset I$; inequivalent embeddings can have isometric complements.

The stabilizer of $J$ acts on $J^\perp/J$; its image is the cusp arithmetic group. With $e$ fixed, the kernel consists of the integral unipotent translations in the parabolic stabilizer. Neither its image nor its integral translation lattice should be replaced by the full orthogonal group without an extension calculation.

For a primitive inclusion $N\subset N'$ of type-IV lattices and compatible arithmetic groups, send an isotropic flag to the same rational flag in $N'$, taking its integral saturation there. Divisibility can change since more pairings are available in $N'$. Orbit identifications are taken in the target group.
:::

::: {.front card-id="period-arithmetic-group-gluing" tags="construction application" cite="[@AEGS25, Lemmas 2.4 and 2.8; @Nik80, gluing of primitive sublattices]"}
How do discriminant gluing and centralizers determine the arithmetic group of a lattice-polarized or involution-marked K3 moduli problem?
:::

::: {.back card-id="period-arithmetic-group-gluing"}
For primitive $S\subset L_{\mathrm{K3}}$, let $T=S^\perp$ and let $\gamma:A_S\to A_T$ be the gluing anti-isometry.

- Marking $S$ pointwise: an isometry $g_T$ extends with identity on $S$ iff $\bar g_T=1$ on $A_T$. The period group is the subgroup of $\ker[O(T)\to O(q_T)]$ preserving the chosen domain component.
- Allowing $H\subset O(S)$: admit $g_T$ iff $\bar g_T=\gamma\bar h\gamma^{-1}$ for some $h\in H$.
- Marking an automorphism $\rho$ of $L_{\mathrm{K3}}$: allowed changes of marking commute with $\rho$. Restrict that centralizer to its period eigenspace and divide out any ineffective action.

For an embedded period subdomain, first take its setwise stabilizer. To replace it by a claimed larger arithmetic group, prove integral extensions using the discriminant condition. A subgroup index can change the degree of the moduli map even when the domain is unchanged.
:::

::: {.front card-id="period-compactification-restrict-fans" tags="theorem construction" cite="[@AEGS25, §3.3, §5.1 and Definition 5.3, with Baily–Borel and toroidal functoriality for arithmetic-domain embeddings]"}
How do an inclusion of type-IV period domains and compatible arithmetic groups extend to Baily–Borel and toroidal compactifications? Which fan defines the normalized closure of the smaller quotient?
:::

::: {.back card-id="period-compactification-restrict-fans"}
For a rational inclusion $\mathbb D_N\subset\mathbb D_{N'}$ induced by a primitive lattice inclusion, with arithmetic groups making the quotient map well-defined:

1. The arithmetic-domain map extends to Baily–Borel; rational boundary components map by their isotropic flags.
2. At a cusp $J\subset N$, include its positive cone in that for $J\subset N'$. Pull back a target admissible fan by intersecting each cone with the smaller cone space.
3. With the induced arithmetic identifications, these fans define the toroidal compactification of the normalization of the image. A finer source fan also gives a morphism to the target compactification.

If the open map is generically injective, this normalization compactifies the original smaller quotient. Otherwise it compactifies the quotient with the identifications induced by the target stabilizer. For semifans, also check compatibility at incident isotropic-plane cusps.

In AEGS the restricted reflection walls are computed by folding; restriction of the ramification semifans then gives the candidate Enriques compactification.
:::

::: {.front card-id="period-wythoff-semifan-strata" tags="construction comparison" cite="[@AEGS25, §§5.1–5.2, especially Lemmas 5.6–5.8]"}
Construct a generalized Coxeter semifan from relevant and irrelevant roots. Explain its strata and the test for toroidality in the AEGS construction.
:::

::: {.back card-id="period-wythoff-semifan-strata"}
Let $W$ act on a hyperbolic lattice, with chamber $C$ and simple roots indexed by $I\sqcup J$ (relevant/irrelevant). Put
$$W_J=\langle s_j:j\in J\rangle,\qquad C_{\mathrm{gen}}=\bigcup_{w\in W_J}wC.$$
Its $W$-translates and their faces form the generalized Coxeter semifan. It coarsens the Coxeter fan by erasing walls internal to these unions. In a finite $A_2$ example, marking one simple root irrelevant joins two adjacent Weyl chambers along that root's wall.

For a cusp lattice of rank $n$:

| Chamber face | Diagram | Toroidal meaning |
| --- | --- | --- |
| Meeting the positive cone | Elliptic, rank $r$ | Cone dimension $n-r$, stratum codimension $n-r$ |
| Isotropic ray | Maximal parabolic | Type II divisor over a Baily–Borel curve |

For the generalized Coxeter construction used in AEGS, retain diagrams with no connected component consisting entirely of irrelevant vertices. Removing such components records the contraction of their moduli. A finite $W_J$ gives polyhedral unions of finitely many chambers; the infinite irrelevant groups in AEGS give genuinely nonpolyhedral cones. At a type II cusp, toroidality holds precisely when its maximal parabolic diagram has no wholly irrelevant connected component.
:::

::: {.front card-id="period-semitoroidal-comparison-finiteness" tags="theorem application" cite="[@AE23, published Theorem 7.18; @AEGS25, proof of Theorem 5.9]"}
State the characterization of semitoroidal compactifications between toroidal and Baily–Borel compactifications. How does it help prove a KSBA comparison map finite?
:::

::: {.back card-id="period-semitoroidal-comparison-finiteness"}
For a type-IV arithmetic quotient $F$, a normal compactification $Y$ is semitoroidal iff there are morphisms restricting to the identity on $F$:
$$\overline F^{\Sigma}\longrightarrow Y\longrightarrow\overline F^{\mathrm{BB}},$$
with $\overline F^{\Sigma}$ toroidal. The first map is encoded by coarsening the cusp fans to compatible semifans.

Application to a proper comparison $B^\nu\to\overline F^{\mathrm{KSBA}}$ that is the identity on $F$:

1. Prove that the normalized KSBA target maps to Baily–Borel, including recovery of type II elliptic moduli.
2. The theorem makes this target semitoroidal, with a semifan coarser than that of $B^\nu$.
3. Rule out strict coarsening by showing that the proposed contracted strata still vary as stable pairs. In AEGS, maximal double-curve configurations give this obstruction.
4. Equality of the semifans identifies the normalizations; the resulting map to the KSBA closure is finite.

Properness and generic injectivity alone do not prove finiteness: a blowup has both and has a positive-dimensional exceptional fiber.
:::

::: {.front card-id="k3-invariant-boundary-periods-models" tags="construction comparison" cite="[@AEGS25, Theorem 4.6 and Remark 4.11; @AE22, §8]"}
How do orientation and boundary periods enter an involution-equivariant Kulikov smoothing? Why can an involution be regular on the stable model but only birational on a chosen Kulikov model?
:::

::: {.back card-id="k3-invariant-boundary-periods-models"}
For an oriented type III dual sphere, the boundary period is $\psi:\Lambda\to\mathbb C^\times$. Reversing orientation inverts the identification $H^2(S^2,\mathbb C^\times)\simeq\mathbb C^\times$. Thus an orientation-reversing involution $J$ requires
$$\psi(J\alpha)=\psi(\alpha)^{-1}.$$
Invariant classes have period in $\{\pm1\}$. On the component of the period locus where the classes required for a lattice polarization remain Cartier, their periods are $1$. The signs on other components encode additional discrete data.

In the AEGS construction, choose component moduli and gluing parameters with this symmetry; the corresponding smoothing preserving the specified Cartier lattice carries the Enriques involution. Symmetry of the dual graph alone does not supply the gluing action.

Kulikov models are related by flops. An automorphism can exchange their nef chambers and hence fail to be regular on the chosen model. Contracting the invariant ADE configurations removes that chamber choice. On the KSBA model the log canonical ring gives a unique model, and an automorphism preserving the pair acts on this ring and therefore regularly on its Proj.
:::

::: {.front card-id="k3-lattice-quasipolarization-small-cones" tags="definition comparison" cite="[@AE25, Definitions 4.1, 4.2, 4.9, 5.1]"}
Define lattice quasipolarization with its chamber choice. What are the small cones in Alexeev–Engel's corrected definition?
:::

::: {.back card-id="k3-lattice-quasipolarization-small-cones"}
Fix a primitive hyperbolic sublattice $\Lambda\subset L_{\mathrm{K3}}$ and $h\in\Lambda_{\mathbb R}$, $h^2>0$, **very irrational**: it lies in no proper rational subspace of $\Lambda_{\mathbb R}$.

A $(\Lambda,h)$-quasipolarized smooth K3 is $(X,j)$ with a primitive isometric embedding $j:\Lambda\hookrightarrow\operatorname{NS}(X)$ and $j(h)$ big and nef. Isomorphisms satisfy $j=f^*j'$.

Small cones are the connected components of $\{x\in\Lambda_{\mathbb R}:x^2>0\}$ after removing
$$\beta^\perp\cap\Lambda_{\mathbb R},\qquad
\beta\in L_{\mathrm{K3}}\setminus\Lambda^\perp,\quad
\beta^2=-2,\quad \langle\Lambda,\beta\rangle\text{ hyperbolic}.$$
Roots outside $\Lambda$ can cut additional walls. For $\Lambda=U(2)$, $\Lambda$ has no $(-2)$-roots, but such additional walls exist. Using only its own Weyl chambers loses this data.

The ample model is a K3 with ADE singularities, carrying $j:\Lambda\to\operatorname{Pic}(\overline X)$ with $j(h)$ ample; on the smooth resolution, contract the $(-2)$-curves orthogonal to $j(\Lambda)$. Rank one recovers ample versus big-and-nef polarization.
:::

::: {.front card-id="k3-heegner-unigonal-enriques" tags="definition comparison example" cite="[@AE23a, Definition 2.3; @AEGS25, §2]"}
Define a Heegner divisor and the unigonal locus for a primitive degree-two K3 polarization. Distinguish nodal and unnodal Enriques surfaces.
:::

::: {.back card-id="k3-heegner-unigonal-enriques"}
For a lattice $N$ of signature $(2,n)$ and type-IV domain $\mathbb D_N$, a **Heegner divisor** is the image in $\mathbb D_N/\Gamma$ of
$$v^\perp\cap\mathbb D_N,\qquad v\in N_{\mathbb Q},\quad v^2<0,$$
or a specified union of such hyperplanes modulo $\Gamma$. This imposes an additional algebraic class in K3 moduli. The numerical square and discriminant-group class specify which divisor is meant.

For a primitive big-and-nef degree-two class $h$, the **unigonal** case has a primitive nef isotropic class $E$ with $hE=1$. Then $h=2E+\Gamma$ with $\Gamma$ a $(-2)$-section, $E\Gamma=1$; $|h|$ has fixed component $\Gamma$. It is not the usual basepoint-free double-plane system.

An Enriques surface is nodal iff it contains a smooth rational $(-2)$-curve; unnodal iff it has none. This concerns the smooth surface, even though its canonical polarized model may contract that curve to a node. In degree-two Enriques moduli, the unigonal locus is a separate Heegner locus, described by double covers of $\mathbb P(1,1,2)$.
:::

::: {.front card-id="k3-nef-divisor-stable-models" tags="definition construction comparison" cite="[@AE23, Definitions 3.10–3.12]"}
Distinguish a nef model, divisor model, and stable model of a polarized K3 degeneration.
:::

::: {.back card-id="k3-nef-divisor-stable-models"}
Start with a smooth K3 family $X^*\to C^*$, a relatively big-and-nef $L^*$, and an effective divisor $R^*\in|L^*|$ without vertical components.

| Model over $(C,0)$ | Conditions |
| --- | --- |
| Nef model $(X,L)$ | $X$ Kulikov, $L$ extends $L^*$ and is relatively nef |
| Divisor model $(X,R)$ | Nef model with $R=\overline{R^*}$ Cartier and containing no stratum of $X_0$ |
| Stable model $(\overline X,\epsilon\overline R)$ | Relative ample model $\operatorname{Proj}_C\bigoplus_{m\ge0}\pi_*\mathcal O_X(mR)$, with boundary pushed forward |

Strata include components, double curves, and triple points. On a divisor model, $R|_{V_i}$ is nef on each component and big on at least one. The ample model contracts the curves invisible to $R$ and has slc stable fibers for every sufficiently small positive rational $\epsilon$.

Finite base change and modifications may be needed to obtain these models; a general Kulikov model need not extend the polarization nef.
:::

::: {.front card-id="k3-boundary-lattice-period" tags="definition construction" cite="[@AE23, §§3C–4]"}
For a Type III Kulikov surface, define numerically Cartier classes, its reduced lattice, and the boundary period. What prevents componentwise line bundles from gluing?
:::

::: {.back card-id="k3-boundary-lattice-period"}
Write the normalization components $V_i$ and double curves $D_{ij}\subset V_i$. Set
$$\widetilde\Lambda=\{(\alpha_i)\in\bigoplus_iH^2(V_i,\mathbb Z):
\alpha_iD_{ij}=\alpha_jD_{ji}\},\qquad
(\alpha,\beta)=\sum_i\alpha_i\beta_i.$$
For a Kulikov total space, let $\xi_i$ be the tuple of restrictions of $\mathcal O_X(V_i)$; put $\Xi=\langle\xi_i\rangle$, $\Lambda=\widetilde\Lambda/\Xi$. These component classes form the radical; quotienting removes them.

Each $\alpha_i$ determines a line bundle $L_i$ on rational $V_i$. Matching degrees identifies their restrictions on the double curves, but the identifications can fail the cocycle condition at triple points. Their obstruction lies in
$$H^2(\Gamma(X_0),\mathbb C^\times)\cong\mathbb C^\times$$
after orienting the dual sphere. This defines the boundary period homomorphism $\widetilde\psi:\widetilde\Lambda\to\mathbb C^\times$. Its kernel consists of gluable classes. For a $d$-semistable surface it descends to $\Lambda$; the reduced Picard group is $\operatorname{Pic}(X_0)/\Xi=\ker\psi$.
:::

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

::: {.front card-id="card-34ee9fdbfea0ed5c" cite="[@KKMS73, Chapter II; @Kul77, Theorem I; @Huy16, Chapter 6, §5 and Theorem 5.1]"}
What is Kulikov's key result on degenerations of K3s?
:::

::: {.back card-id="card-34ee9fdbfea0ed5c"}
Two steps. Mumford's semistable reduction: after a finite base change $z\mapsto z^m$, a degeneration of K3 surfaces over a disk has a semistable modification (smooth total space, reduced normal-crossings central fiber).

Kulikov: a semistable degeneration $X\to\Delta$ of K3 surfaces whose central-fiber components are algebraic (or Kähler) admits a modification $X'\to\Delta$ with $K_{X'}\sim0$, still semistable. This is a Kulikov model.
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

::: {.front card-id="card-b1d78709d3678358" cite="[@AEH24, §3E; @Loo02, §6 and Definition 6.1]"}
What is a semitoroidal compactification?
:::

::: {.back card-id="card-b1d78709d3678358"}
Simultaneously generalizes BB and toroidal compactifications.

For a type-IV arithmetic quotient, use a $\Gamma$-admissible semifan in the cusp positive cones: locally rational polyhedral cones may have infinitely many faces, and their data agree along rank-two isotropic cusps. Glue the cusp partial compactifications specified by these cones and divide by the cusp stabilizers. This is Looijenga's compactification; he calls it semitoric.

In the complex-ball case, the toroidal boundary at a cusp is an abelian variety $A$. A semifan specifies a subtorus $B\subset A$ from a primitive sublattice of the cusp lattice; replace the boundary by $A/B$. $B=0$ gives the toroidal boundary; $B=A$ contracts it to the Baily–Borel point.
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

::: {.front card-id="card-681a11bbc6a0be2c" cite="[@AEH24, §3B, Remark 3.6]"}
What is $F_\rho^{\mathrm{ade}}$ when the nonsymplectic automorphism fixes a curve $R$ of genus $g\ge2$? How is its surface model obtained?
:::

::: {.back card-id="card-681a11bbc6a0be2c"}
Start with a $\rho$-markable K3 surface $(X,\sigma)$ and its fixed curve $R$, with $R^2=2g-2>0$. Contract the curves $C\cong\mathbb P^1$ with $C^2=-2$ and $R\cdot C=0$:
$$\pi:X\longrightarrow\overline X,\qquad \overline R=\pi_*R\ \text{ample}.$$
The result is an ADE K3 surface with the induced automorphism. These models form the separated moduli space
$$F_\rho^{\mathrm{ade}}=F_\rho^{\mathrm{sep}}\cong(\mathbb D_\rho\setminus\Delta_\rho)/\Gamma_\rho.$$
Here $\mathbb D_\rho$ is the period domain for the chosen action on $H^{2,0}$, $\Gamma_\rho$ the change-of-markings group, and $\Delta_\rho$ the root discriminant orthogonal to the invariant lattice.
:::

::: {.front card-id="card-6e339cb955627865" cite="[@AEH24, §§3B and 3F]"}
How is $\overline F_\rho^{\mathrm{slc}}$ constructed from K3 surfaces with a nonsymplectic automorphism fixing a curve $R$ with $g(R)\ge2$?
:::

::: {.back card-id="card-6e339cb955627865"}
Contract the curves $C$ with $R\cdot C=0$ to obtain $(\overline X,\overline R)$ with $\overline R$ ample. Fix $\epsilon\in\mathbb Q_{>0}$ such that $(\overline X,\epsilon\overline R)$ is log canonical throughout this fixed numerical moduli problem. Then $K_{\overline X}+\epsilon\overline R\sim_{\mathbb Q}\epsilon\overline R$ is ample. Send
$$\psi:(X,\sigma)\longmapsto(\overline X,\epsilon\overline R).$$
Take the reduced closure of $\operatorname{im}\psi$ in the projective moduli space of stable slc pairs with these numerical invariants, then normalize:
$$\overline F_\rho^{\mathrm{slc}}=\left(\overline{\operatorname{im}\psi}\right)^\nu.$$
Its open part is $F_\rho^{\mathrm{ade}}$. The normalization can retain finite data over a stable pair. The compactification is semitoroidal; the fixed-curve divisor supplies the recognizable polarizing divisor.
:::

::: {.front card-id="card-ac88b51027b8331a" cite="[@ADH24, §2.1]"}
For K3 surfaces with a finite-order nonsymplectic automorphism acting as $\rho$ on the K3 lattice, which root hyperplanes form the discriminant in its period domain?
:::

::: {.back card-id="card-ac88b51027b8331a"}
Write $\mathbb D_\rho$ for the K3 period domain in the eigenspace corresponding to the action on $H^{2,0}$. The discriminant is
$$\Delta_\rho=\mathbb{D}_\rho \cap\bigcup_{\substack{\delta \in (L^G)^\perp\\ \delta^2=-2}} \delta^\perp.$$
$L^G \coloneqq \mathrm{Fix}(\rho) \subset S_\rho$ the fixed classes for $G = \left\langle{\rho}\right\rangle$

$L \coloneqq\Lambda_{\mathrm{K3}}$.

$S_\rho \coloneqq T_\rho^\perp$, $T_\rho \coloneqq L^\prim_\CC\cap L$ generic Picard/transcendental lattices.

$L^\prim_\CC$ the sum of primitive eigenspaces of $\rho$.

The condition $(\omega,\delta)=0$ makes the root $\delta$ algebraic. These hyperplanes exclude roots orthogonal to the invariant lattice; they do not exclude every possible Picard-rank jump.
:::

::: {.front card-id="card-f1f9e680ce07e9ba" cite="[@AEGS25, §2.3, and its explicit three lattice involutions]"}
How does an involution act on $H^2$?
:::

::: {.back card-id="card-f1f9e680ce07e9ba"}
For an involution $\sigma$ of a complex projective K3 surface, put $L=H^2(X,\mathbb Z)$ and $L^\pm=\ker(\sigma^*\mp1)$. These are primitive orthogonal sublattices, and
$$L\otimes\mathbb Q=(L^+\otimes\mathbb Q)\oplus(L^-\otimes\mathbb Q).$$
The integral sum can have nontrivial finite index, killed by two.

- Nonsymplectic: $\sigma^*\omega=-\omega$, $L^+\subset\operatorname{NS}(X)$, and $\sigma^*=-1$ on $T_X=\operatorname{NS}(X)^\perp$. The Picard lattice can also contain anti-invariant classes.
- Symplectic: $\sigma^*\omega=\omega$, and $\sigma^*=1$ on $T_X$. The action on the Picard lattice need not be trivial.

For a nonsymplectic involution, $L^+$ equals $\operatorname{NS}(X)$ only on the locus without extra algebraic classes. An invariant lattice and the full Picard lattice are different objects.
:::

::: {.front card-id="card-f6dea11f91a6b646" cite="[@Nik80, Theorem 3.6.2; @Nik79a, §4]"}
Classify $(X, \sigma)$ with $\sigma$ a nonsymplectic involution, up to deformation.
:::

::: {.back card-id="card-f6dea11f91a6b646"}
By the invariant lattice $S = H^2(X; \ZZ)^\sigma$: a primitive 2-elementary hyperbolic sublattice $S \subseteq \Lambda_{\mathrm{K3}}$. Nikulin classified these using $(r, a, \delta)$, equivalently $(g, k, \delta)$: 75 cases.
:::

::: {.front card-id="card-beee68f3907963f4"}
What is the importance of a recognizable divisor?
:::

::: {.back card-id="card-beee68f3907963f4"}
For the moduli $F_\rho$ of K3 surfaces with the specified nonsymplectic automorphism, choose a canonical polarizing divisor $R$. Let $\overline{F_\rho}^{\mathrm{slc}}$ denote the normalization of the closure of the associated pairs $(X,\epsilon R)$ in stable-pair moduli, for small positive rational $\epsilon$.

If $R$ is recognizable, then $\overline{F_\rho}^{\mathrm{slc}}$ is semitoroidal for a unique semifan $\mcf_R$.
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


::: {.front card-id="card-e5204c524e5af7fb" tags="theorem" cite="[@Tod80; @Loo81a; @Siu81; @Huy16, Chapter 6, Remark 3.2]"}
Describe the period domain for marked complex K3 surfaces and its dimension. Which of its points occur as periods? How does fixing a polarization change the domain?
:::

::: {.back card-id="card-e5204c524e5af7fb"}
$$\mathbb{D} = \Omega \coloneqq\left\{{[\omega]\in {\mathbf{P}}(\Lambda_{{\mathsf{K}}3}\otimes_\ZZ\CC) \st\omega^2 = 0,\,\, \omega.\overline{\omega }> 0}\right\}$$
In coordinates that diagonalize the form on $\Lambda_{\mathrm{K3}}\otimes{\mathbf{R}}$ with signature $(3, 19)$,
$$\Omega \cong \left\{{{\left[ {z_0:\cdots:z_{21}} \right]}\in {\mathbf{P}}^{21}\st z_0^2+z_1^2 + z_2^2 - z_3^2 -\cdots - z_{21}^2 = 0,\, {\left\lvert {z_0} \right\rvert}^2 + {\left\lvert {z_1} \right\rvert}^2 + {\left\lvert {z_2} \right\rvert}^2 - {\left\lvert {z_3} \right\rvert}^2 - \cdots - {\left\lvert {z_{21}} \right\rvert}^2 > 0}\right\}$$
which is an open subset of a quadric in ${\mathbf{P}}^{21}$ and thus a 20-dimensional $\CC\dash$manifold.

For a marking $\Phi: H^2(X;\ZZ)\to \Lambda_{\mathrm{K3}}$, the period of $(X, \Phi)$ is $\Phi(\CC\omega_X) \in \Omega$, where $\CC\omega_X = H^{2,0}(X) \in {\mathbf{P}}H^2(X;\CC)$. Surjectivity of the period map (Todorov, Looijenga, Siu): every point of $\Omega$ is the period of some marked K3.

Fixing a primitive class $h\in\Lambda_{\mathrm{K3}}$ with $h^2=2k>0$ gives
$$\mathbb D_{2k}=\{[\omega]\in\mathbb D:(\omega,h)=0\}.$$
This domain is 19-dimensional, with two connected components, each a bounded symmetric domain of type IV. Periods for which $h$ is an ample polarization fill the open subset
$$\mathbb D_{2k}^{\mathrm{amp}}=\mathbb D_{2k}\setminus\bigcup_{\substack{\delta\in\Lambda_{\mathrm{K3}}\\\delta^2=-2,\;(\delta,h)=0}}\delta^\perp.$$
Here $\delta^\perp$ means the locus $(\omega,\delta)=0$.
:::

::: {.front card-id="card-a7590df0a74c3577"}
What is a marking of a K3?
:::

::: {.back card-id="card-a7590df0a74c3577"}
Let $X$ be a K3 surface. A marking is an isometry $\phi: H^2(X; \ZZ) { \, \xrightarrow{\sim}\, }\Lambda_{{\mathsf{K}}3}$, where $\Lambda_{{\mathsf{K}}3}$ (also written $L$) is the K3 lattice $U{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  }$.
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





::: {.front card-id="application-period-root-obstructs-ampleness" tags="application"}
A K3 period $\omega$ satisfies $(\omega,h)=(\omega,\delta)=0$, where $h$ is primitive, $h^2>0$, $\delta^2=-2$, and $(h,\delta)=0$. Can a marked K3 with this period have $h$ as an ample polarization? Explain the obstruction, not just the period-domain exclusion.
:::

::: {.back card-id="application-period-root-obstructs-ampleness"}
No. Orthogonality to $\omega$ makes $\delta$ an integral $(1,1)$ class, so it is the class of a line bundle by Lefschetz $(1,1)$. K3 Riemann–Roch gives $\chi(\mathcal O(\delta))=1$; Serre duality implies that either $\delta$ or $-\delta$ is effective. An ample class must intersect every nonzero effective divisor positively, contradicting $(h,\delta)=0$.
:::


::: {.front card-id="card-6b14f9ae9d6474c8" tags="definition"}
What is the definition of Arithmetic quotient?
:::

::: {.back card-id="card-6b14f9ae9d6474c8"}
A quotient $\Gamma\backslash D$ of a symmetric domain $D$ by a discrete subgroup $\Gamma$ commensurable with an arithmetic lattice. Moduli spaces of polarized K3 surfaces are arithmetic quotients of type IV domains.
:::

::: {.front card-id="card-bc716af8baef6126" tags="definition" cite="[@KKMS73, Chapter II; @Kul77, Theorem I; @Huy16, Chapter 6, §5]"}
What is the definition of Birational modification?
:::

::: {.back card-id="card-bc716af8baef6126"}
A birational map between varieties, usually resolved by a sequence of blowups and blowdowns. After a finite base change, semistable reduction (Mumford) gives a semistable model by a birational modification; Kulikov's theorem then modifies a semistable K3 degeneration to one with trivial canonical bundle.
:::

::: {.front card-id="card-223d21f6a7d001e5" tags="definition"}
What is the definition of Bounded symmetric domain?
:::

::: {.back card-id="card-223d21f6a7d001e5"}
A bounded open domain $\Omega\subset\mathbb C^n$ such that every point is the unique fixed point of an involutive holomorphic automorphism of $\Omega$. Period domains of K3 type are bounded symmetric domains of type IV.
:::

::: {.front card-id="card-fdf58d78e130682d" tags="definition"}
What is the definition of Central fiber?
:::

::: {.back card-id="card-fdf58d78e130682d"}
The fibre $X_0=\pi^{-1}(0)$ of a family $\pi:\mathcal X\to\Delta$ over a disc. In a semistable degeneration it is a reduced normal-crossings divisor.
:::

::: {.front card-id="card-30b9ac4219789b76" tags="definition"}
What is the definition of Discriminant locus?
:::

::: {.back card-id="card-30b9ac4219789b76"}
In the period domain of $\rho$-marked K3 surfaces, $\Delta_\rho=\mathbb D_\rho\cap\bigcup_{\delta}\delta^\perp$, where $\delta$ runs over $(-2)$-roots orthogonal to the invariant lattice $L^G$. Its complement excludes these roots from the algebraic classes; other extra algebraic classes can remain.
:::

::: {.front card-id="card-4527c4cdf3791038" tags="definition"}
What is the definition of Fine moduli space?
:::

::: {.back card-id="card-4527c4cdf3791038"}
A moduli space that represents the moduli functor: every family is the pullback of a universal family over it. Equivalently, it carries a universal object.
:::

::: {.front card-id="card-76e785e17a4b4a7c" tags="definition"}
What is the definition of Groupoid?
:::

::: {.back card-id="card-76e785e17a4b4a7c"}
A category in which every morphism is an isomorphism. The moduli stack of a moduli problem assigns to a base $B$ the groupoid of families over $B$.
:::

::: {.front card-id="card-8e37fe59c02842a4" tags="definition"}
What is the definition of Local torelli theorem?
:::

::: {.back card-id="card-8e37fe59c02842a4"}
For a marked K3 surface $(X,\phi)$, the period map from the versal deformation space of $X$ to the period domain $\mathbb D$ is a local isomorphism.
:::


::: {.front card-id="card-35ca437ea0e015b1" tags="definition"}
What is the definition of Picard lattice?
:::

::: {.back card-id="card-35ca437ea0e015b1"}
The lattice $\operatorname{Pic}(X)$ with its intersection form. For a projective K3 surface, $\operatorname{Pic}(X)=\operatorname{NS}(X)$ is an even primitive sublattice of $\Lambda_{\mathrm{K3}}$ of signature $(1,\rho(X)-1)$.
:::

::: {.front card-id="card-4e9bb43f4ef3673f" tags="definition"}
What is the definition of Q-cartier divisor?
:::

::: {.back card-id="card-4e9bb43f4ef3673f"}
A divisor $D$ on a normal variety such that some nonzero multiple $mD$ is Cartier. If $K_X$ is $\mathbb Q$-Cartier, then $X$ is $\mathbb Q$-Gorenstein.
:::

::: {.front card-id="card-9fc12fa0cf8ba0dd" tags="definition"}
What is the definition of Rational boundary component?
:::

::: {.back card-id="card-9fc12fa0cf8ba0dd"}
A boundary stratum added to a symmetric domain in the Baily–Borel compactification. For a type IV domain these are points or copies of the upper half-plane $\mathbb H$ (and $-\mathbb H$).
:::


::: {.front card-id="card-f67ebfdf6dac4a2b" tags="definition" cite="[@AEH24, Definitions 3.17–3.18]"}
What is the definition of Semifan?
:::

::: {.back card-id="card-f67ebfdf6dac4a2b"}
For a type-IV lattice $N$ of signature $(2,n)$, a $\Gamma$-admissible semifan assigns to each primitive isotropic line $J\subset N$ a convex rational locally polyhedral conical decomposition $\mathfrak F_J$ of the rational closure of a positive cone in $(J^\perp/J)_{\mathbb R}$. Cones meet along faces; they need not be finitely generated. Require $\Gamma$-invariance.

Compatibility at a primitive isotropic plane $I$: for every $J\subset I$, intersect the kernels of the wall forms of $\mathfrak F_J$ whose walls contain $I/J$, intersect with $I^\perp/J$, and descend to $I^\perp/I$. The resulting rational subspace, or saturated lattice, must be independent of $J$.

These data define semitoroidal compactifications. In the recognizable-divisor theorem, the stable-pair compactification determines a unique semifan.
:::

::: {.front card-id="card-a6dd0db307a9ada3" tags="definition"}
What is the definition of Toroidal compactification?
:::

::: {.back card-id="card-a6dd0db307a9ada3"}
A compactification of $\Gamma\backslash D$ built from torus embeddings at rational cusps. At each cusp, choose a rational polyhedral fan in the cone attached to the center of its unipotent radical. Require cusp-stabilizer invariance, finitely many cone orbits, and agreement at incident cusps.

After quotienting by the integral central translations, replace each torus chart by the toric variety of its fan, glue the charts, and quotient by the remaining stabilizer. Full-support fans give a compactification; it depends on the fan and maps to Baily–Borel. A refinement gives a proper modification. Semifans allow the more general semitoroidal construction.
:::

::: {.front card-id="card-da95f37a1b1f62ae" tags="definition"}
What is the definition of Type iv domain?
:::

::: {.back card-id="card-da95f37a1b1f62ae"}
For $N$ of signature $(2,n)$, choose one connected component of
$$\mathbb D_N=\{[x]\in\mathbb P(N\otimes\mathbb C):(x,x)=0,\ (x,\bar x)>0\}.$$
It has complex dimension $n$ and parametrizes oriented positive-definite real two-planes in $N_{\mathbb R}$.

For polarized K3s, use $N=h^\perp\subset\Lambda_{\mathrm{K3}}$, signature $(2,19)$. The full K3 lattice has signature $(3,19)$: its $20$-dimensional period domain has the same equations but is not a type-IV Hermitian symmetric domain.
:::

::: {.front card-id="card-af9f71bcc0ea225f" tags="definition"}
What is the definition of Weak torelli theorem?
:::

::: {.back card-id="card-af9f71bcc0ea225f"}
Two complex K3 surfaces $X$ and $X'$ are isomorphic iff there is an isometry $H^2(X;\mathbb Z)\to H^2(X';\mathbb Z)$ whose $\mathbb C$-linear extension preserves the Hodge decompositions.
:::

::: {.front card-id="nl-polarized-k3-divisors" tags="definition construction" cite="[@MP12a, §1]"}
Define Noether–Lefschetz divisors in the moduli space of primitively polarized complex K3 surfaces of degree $2d$. Describe their period equations and the numerical data of an extra class.
:::

::: {.back card-id="nl-polarized-k3-divisors"}
Fix primitive $h$ with $h^2=2d>0$. The polarized period domain lies in $\mathbb P(h^\perp\otimes\mathbb C)$ and satisfies $(\omega,\omega)=0$, $(\omega,\bar\omega)>0$. An extra integral class $\beta\notin\mathbb Qh$ is algebraic exactly on
$$\Omega_h\cap\beta^\perp.$$
Nonempty such hyperplane sections descend, after grouping by the monodromy action, to Noether–Lefschetz divisors. Their union is the locus $\rho\ge2$; a general point of an irreducible component has Picard rank two.

Writing $h\beta=m$, $\beta^2=2s$, the generated lattice has Gram matrix
$$\begin{pmatrix}2d&m\\m&2s\end{pmatrix},\qquad D=m^2-4ds>0.$$
The positivity of $D$ expresses signature $(1,1)$. To distinguish components, retain the primitive saturation and embedding data; this matrix alone does not assert existence or uniqueness of a divisor. For ample polarization omit periods orthogonal to a root $\delta$ with $\delta^2=-2$ and $h\delta=0$.
:::

::: {.front card-id="nl-quartic-line-dimension" tags="application"}
Show by an incidence calculation that smooth quartics containing a line form a divisor in quartic K3 moduli. Recover the lattice discriminant and explain why “very general” is the right qualifier in Noether–Lefschetz.
:::

::: {.back card-id="nl-quartic-line-dimension"}
Quartic equations form $\mathbb P^{34}$. Containing a fixed line imposes $h^0(\mathbb P^1,\mathcal O(4))=5$ independent linear conditions, giving $\mathbb P^{29}$. Lines vary in $\operatorname{Gr}(2,4)$ of dimension four, so the incidence variety has dimension $33$.

On a smooth quartic, lines are isolated: $N_{L/S}=\mathcal O_{\mathbb P^1}(-2)$ has no sections. Hence the image has dimension $33$, codimension one in $\mathbb P^{34}$. Quotienting by $\operatorname{PGL}_4$ gives dimensions $18$ inside $19$.

The lattice generated by $H,L$ has matrix $\left(\begin{smallmatrix}4&1\\1&-2\end{smallmatrix}\right)$ and discriminant $-9$. Other extra divisor classes give other Noether–Lefschetz loci; excluding just the line locus does not force Picard rank one.
:::
