---
title: "Mathematical Physics"
---

::: {.front card-id="card-8edb2235ecd7bad5"}
Describe geometric Langlands.
:::

::: {.back card-id="card-8edb2235ecd7bad5"}
$\rho \in {\mathcal{X}}(\pi_1\Sigma_g, G)\leadsto$ a flat connection $\nabla_\rho$ on a principal $G{\hbox{-}}$bundle over $C$

Irreducible such connections $\rightleftharpoons$ $R\in    {}_{\mathcal{D}}{\mathsf{Mod}} ({\mathsf{Bun}}_{{}^L G})$.
:::

::: {.front card-id="card-e0267814e9c4ee2e"}
What is a large complex structure limit?
:::

::: {.back card-id="card-e0267814e9c4ee2e"}
Idea: line bundle $L$ over the total space of a family which specifies $c_1(L)$ and thus a symplectic class.

A polarized algebraic family of $n$-dim CY manifolds $X \rightarrow S \backslash\{0\}$ over a punctured algebraic curve, whose 'essential skeleton' (simplicial subcomplex of dual complex) has dimension $n$.

Also called "maximal degeneration"

Semistable SNC model.
:::

::: {.front card-id="card-a62507d3e1e915e7"}
What is ${\mathsf{Bun}}_G$?
:::

::: {.back card-id="card-a62507d3e1e915e7"}
${\mathsf{Bun}}_G(k)$ is the maximal subgroupoid of ${\mathsf{G}{\hbox{-}}\mathsf{Torsors}}_{/ {X}}$.

Forms an algebraic stack.

Observation due to Weil: $\dcoset{G(F)}{G({\mathbf{A}}_F)}{\prod_{x\in {\left\lvert {X} \right\rvert}}' G({\mathcal{O}}_x)}  { \, \xrightarrow{\sim}\, }{\mathsf{Bun}}_G$ where $F= k(X)$, $F_x$ is the completion at $x$, and ${\mathcal{O}}_x$ is its valuation ring. Supposed to resemble
$$\dcoset{G(F)}{G({\mathbf{A}}_F)}{K }$$
:::

::: {.front card-id="card-8e8acdcff9808d4b"}
What are Higgs bundles? Why care?
:::

::: {.back card-id="card-8e8acdcff9808d4b"}
$(E, \theta)$ where $E$ is a holomorphic bundle and $\theta: E\to E\otimes\Omega^1_{X}$ is an endomorphism-valued 1-form satisfying $\theta\wedge \theta =0$.

On a curve $C$, $\theta\wedge\theta = 0$ is automatic and $\theta$ is a holomorphic section of ${ \operatorname{ad}}(E)\otimes K_C$, so ${ \overline{{\partial}}}\theta = 0$.

Stable Higgs bundles with vanishing Chern classes (on a curve: degree 0) biject with irreducible representations of $\pi_1(X)$.
:::

::: {.front card-id="card-5ab68700993ee9f6"}
What is Batyrev-Borisov's mirror symmetry?
:::

::: {.back card-id="card-5ab68700993ee9f6"}
For e.g. complete intersections in Fanos, $H^1(X; {\mathbf{T}} {}^{ \vee }X) \cong H^1(X {}^{ \vee }; {\mathbf{T}}X {}^{ \vee })$.

LHS: variations of $\omega_X$ a symplectic form (A-model)

RHS: variations of complex structure (B-model)
:::

::: {.front card-id="card-6b4152564621a373"}
What is EM duality in Maxwell theory?
:::

::: {.back card-id="card-6b4152564621a373"}
Setup: $\nabla$ a connection on a principal ${\operatorname{U}}_1{\hbox{-}}$bundle over $X\in {\mathsf{Mfd}}^4$.

Equations of motion: $d\star d\nabla = 0$.

Theory invariant under $d\nabla \mapsto \star d\nabla$, exchanges $E_i$ and $B_i$.
:::

::: {.front card-id="card-88579f2dff310206"}
What is Yang-Mills theory?
:::

::: {.back card-id="card-88579f2dff310206"}
Nonabelian gauge theory.

Equations of motion: $d_A F = 0$ and $d_A \star F = 0$ where $F = dA + A{ {}^{ \scriptscriptstyle\wedge^{2} }  }\in \Omega^2( { \operatorname{ad}}E)$ is the curvature of $E$ for $E\to X^4\in \mathop{\mathrm{Prin}}_{G}{}_{/ {X}}$ and $A$ a connection with covariant derivative $d_A$.
:::

::: {.front card-id="card-e45dc9a233508299"}
What is AB symmetry on a CY?
:::

::: {.back card-id="card-e45dc9a233508299"}
A: path integral localized on holomorphic maps to $M$, computes GW, depends only on symplectic structure

B: path integral localized on constant maps, deformation theory of $M$, depends only on complex structure
:::

::: {.front card-id="card-8668e3c5ffaa389d"}
What is mirror symmetry for the Hitchin moduli space?
:::

::: {.back card-id="card-8668e3c5ffaa389d"}
SYZ: ${\mathcal{M}}_H(G, C) \rightleftharpoons{\mathcal{M}}_H({}^L G, C)$ are SYZ mirrors

HMS: A-branes on ${\mathcal{M}}_H(G, C)$ is derived equivalent to $\mathbf{D}{{\mathsf{Coh}}}({\mathcal{M}}_{\flat}({}^L G, C))$.

GL: $\mathbf{D}{{\mathsf{Coh}}}({\mathcal{M}}_{\flat}({}^L G, C))  { \, \xrightarrow{\sim}\, }   {}_{\mathcal{D}}{\mathsf{Mod}} ({\mathsf{Bun}}_G(C))$ sending points to Hecke eigensheaves.
:::

::: {.front card-id="card-7285b57d6a08451f"}
Motivate the affine Grassmannian.
:::

::: {.back card-id="card-7285b57d6a08451f"}
Hecke transformations modify a $G{\hbox{-}}$bundle at a point, such modifications are parameterized by ${\operatorname{Gr}}_G$, transformations from 't Hooft operators $T_\mu$ correspond to Schubert cells $\mu$.
:::

::: {.front card-id="card-bdf64736043c43b5"}
What is geometric Satake?
:::

::: {.back card-id="card-bdf64736043c43b5"}
Equivariant perverse sheaves on ${\operatorname{Gr}}_G$ is equivalent to ${\mathsf{Rep}}({}^L G)^{\mathrm{fd}}$.
:::

::: {.front card-id="card-c4ac7649a95611d6"}
What is the strong force?
:::

::: {.back card-id="card-c4ac7649a95611d6"}
Holds protons and neutrons together in the nucleus of an atom

Holds quarks together in protons/neutrons
:::

::: {.front card-id="card-40e26ae9de203073"}
What is the standard model?
:::

::: {.back card-id="card-40e26ae9de203073"}
Yang Mills for the gauge group ${\operatorname{SU}}_3 \times {\operatorname{SU}}_2 \times {\operatorname{U}}_1$.
:::

::: {.front card-id="card-7d9882a64aabff25"}
What is the defining property of a $D{\hbox{-}}$brane?
:::

::: {.back card-id="card-7d9882a64aabff25"}
Dirichlet boundary conditions: surfaces which can occur at the ends of open strings.
:::

::: {.front card-id="card-7ffecd2148901865"}
What is quantization?
:::

::: {.back card-id="card-7ffecd2148901865"}
Replacing Poisson brackets with commutators.
:::

::: {.front card-id="card-e205faa8a99ea77a"}
What is the central charge?
:::

::: {.back card-id="card-e205faa8a99ea77a"}
*(Answer was a figure; image not recovered.)*
:::
