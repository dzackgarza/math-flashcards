---
title: "Algebraic Geometry::Definitions::Morphisms"
---

::: {.front card-id="card-2fc77d27d9c19b46"}
What is a **separated morphism**?
:::

::: {.back card-id="card-2fc77d27d9c19b46"}
A morphism $f:X\to S$ of schemes is **separated** iff $\Delta_{X/S}: X\to X \underset{\scriptscriptstyle {S} }{\times} X$ is a **closed immersion**.
:::

::: {.front card-id="card-17e3b6dd4ac0258d"}
What is a **quasicompact morphism**? When is a scheme **quasicompact over a base**?
:::

::: {.back card-id="card-17e3b6dd4ac0258d"}
A morphism $f:X\to Y$ is **quasicompact** iff for every quasicompact open $U\subseteq Y$, the preimage $f^{-1}(U)$ is quasicompact. Equivalently, some open affine cover $\{V_i\}$ of $Y$ has every $f^{-1}(V_i)$ quasicompact.

A scheme $X$ over $S$ is **quasicompact over $S$** iff its structure morphism $X\to S$ is quasicompact. For $S=\Spec\ZZ$, this is the usual absolute notion of a quasicompact scheme.
:::

::: {.front card-id="card-67acbfbbf098e7b7"}
What is a locally finitely presented morphism?
:::

::: {.back card-id="card-67acbfbbf098e7b7"}
On open covers, the induced rings maps $R_i\to A_i$ are finite presentation, i.e. $R_i[x_1,\cdots, x_n] \twoheadrightarrow A_i$ with fg kernel for some $n$.
:::

::: {.front card-id="card-c35dccf24f080a71"}
What is a finitely presented morphism?
:::

::: {.back card-id="card-c35dccf24f080a71"}
Locally of finite presentation, quasicompact, quasiseparated.
:::

::: {.front card-id="card-525d10c2757e41de" tags="unsorted"}
What is a proper morphism? What are some consequences?
:::

::: {.back card-id="card-525d10c2757e41de"}
A morphism of schemes is proper if it is separated, of finite type, and universally closed. For a morphism of varieties $\phi: X \rightarrow Y$, separated and finite type are automatic, so $\phi$ is proper iff it is universally closed: for all $\psi: Z \rightarrow Y$, the base change $\phi^{\prime}: X \times_Y Z \rightarrow Z$ is a closed map in the Zariski topology.

Equivalently, for $f$ of finite type and quasi-separated, use the valuative criterion ($=1$ lift).

Consequences:

- $X$ is complete iff the structure morphism to a point is proper.
- Fibers of a proper morphism are complete.
- Inverse images of complete subvarieties of $Y$ are complete.
- Any morphism obtained by base change from a proper morphism is proper.
:::

::: {.front card-id="card-bf7f67bffb5a2228"}
What is an affine morphism?
:::

::: {.back card-id="card-bf7f67bffb5a2228"}
Inverse images of affines are affine.
:::

::: {.front card-id="card-50c3a5b5a43dbd56" tags="definition"}
What is a **finite morphism**?
:::

::: {.back card-id="card-50c3a5b5a43dbd56"}
Hartshorne: $f:X\to Y$ where $\operatorname{Spec}B_i\rightrightarrows Y$ is an open affine cover with each $f^{-1}(\operatorname{Spec}B_i) = \operatorname{Spec}A_i$ affine and $A_i \in   {}_{B_i}\Mod^\fg$. Equivalently, for every affine open $V=\operatorname{Spec}A\subseteq Y$, $f^{-1}(V)=\operatorname{Spec}B$ with $B$ a finite $A$-module, i.e. $f$ is affine and locally given by finite ring morphisms.

Note that being fg as a **module** is **stronger** than being fg as an **algebra**: $k[x] \in  {}_{k}  \mathsf{Alg}$ has one algebra generator but infinite rank in ${}_{k}\Mod$.

Thus **finite** implies **finite type** but not conversely.

Equivalently, proper and locally quasifinite.
:::

::: {.front card-id="card-b00d12404bc086fb"}
What is a **flat** morphism?
:::

::: {.back card-id="card-b00d12404bc086fb"}
For projective varieties: the induced maps on stalks are flat ring maps.

$f: X\to S$ is flat at $x$ iff ${\mathcal{O}}_{X, x} \in   {}_{{\mathcal{O}}_{S, f(x) } }\Mod^\flat$ (i.e. the module structure induced by $f$ yields a flat module.)

Hartshorne's definition: for $f:X\to Y$ and $\mcf\in  {}_{{\mathcal{O}}_X}\Mod$, $\mcf$ is flat over $Y$ at $x\in X$ if $\mcf_x \in   {}_{{\mathcal{O}}_{Y, f(x)}}\Mod^\flat$; flat if flat at every $x\in S$, and $X$ is flat over $Y$ if $\mcf\coloneqq{\mathcal{O}}_X$ is flat.

$f\in \mathsf{CRing}(A, B)$ is a flat map iff $B\in   {}_{A}\Mod^\flat$, and a morphism $f\in \Sch(X, Y)$ is flat iff flat on local rings, i.e. $f_x: {\mathcal{O}}_{Y, f(x)}\to {\mathcal{O}}_{X, x}$ is flat.
:::

::: {.front card-id="card-e504a4da2d4624f3"}
What is a **smooth morphism** of relative dimension $n$?
:::

::: {.back card-id="card-e504a4da2d4624f3"}
(Hartshorne, for schemes of finite type over $k$) $f: X\to Y$ such that

1. $f$ is flat;
2. $\dim X' = \dim Y' + n$ for all irreducible components $X'\subseteq X$ and $Y'\subseteq Y$ with $f(X')\subseteq Y'$;
3. $\dim_{\kappa(x)}(\Omega_{X/Y}\otimes\kappa(x)) = n$ for each point $x\in X$ (closed or not).

For $Y$ irreducible and $f$ flat, condition 2 is equivalent to: every irreducible component of every fiber $X_y$ of $f$ has dimension $n$.

For $X$ integral, condition 3 can be replaced with: $\Omega_{X/Y}$ is locally free of rank $n$.

Closed under base change, composition, fiber products.
:::

::: {.front card-id="card-e9ced257a3fb0b70"}
What is an **unramified** morphism?
:::

::: {.back card-id="card-e9ced257a3fb0b70"}
For every $x\in X$, $f^\sharp(\mfm_{f(x)}) \cdot {\mathcal{O}}_{X, x} \cong\mfm_x$ where $f^\sharp: {\mathcal{O}}_{Y, f(x)}\to {\mathcal{O}}_{X, x}$, and $\kappa(x)/\kappa(y)$ is a separable algebraic extension.

Equivalently, $f:X\to Y$ with $\Omega_{X/Y} = 0$.

Equivalently, $f$ locally of finite presentation and the diagonal is an open immersion.

For curves: $\exists e_p\in \ZZ_{\geq 0}$ such that $f^\sharp(\mfm_{f(p)}) {\mathcal{O}}_{X, x} = \mfm_{x}^{e_p}$, and unramified iff $e_p = 1$ for all $p\in X$.

Flat + unramified = etale.
:::

::: {.front card-id="card-a484edc8e6016938"}
What is an **etale** morphism $f:X\to Y\in \Sch_{/ {k}}$?
:::

::: {.back card-id="card-a484edc8e6016938"}
Fully general: flat, finite type, unramified.

Smooth of relative dimension 0.

Flat and $\Omega_{X/ Y} = 0$.

For varieties: flat and unramified.
:::

::: {.front card-id="card-c79260140f5f0dbd"}
When is a morphism of schemes an immersion?
:::

::: {.back card-id="card-c79260140f5f0dbd"}
$\iota: X\to Z$ making $X$ isomorphic to an open subscheme *of a closed subscheme* of $Z$.
:::

::: {.front card-id="card-86f3fc66ea0fc489"}
What is a **closed immersion** of schemes?
:::

::: {.back card-id="card-86f3fc66ea0fc489"}
$f:X\to Y$ inducing a homeomorphism $\tilde f: {\left\lvert {X} \right\rvert} \to {\left\lvert {V} \right\rvert}$ for ${\left\lvert {V} \right\rvert} \subseteq {\left\lvert {Y} \right\rvert}$ a closed subspace of the underlying topological spaces, such that $f^\sharp: {\mathcal{O}}_Y \twoheadrightarrow f_* {\mathcal{O}}_X$ is a surjective map of sheaves.

Equivalently, separates points and tangent vectors, i.e. $p\neq q$ closed points in $X \implies \exists s\in \mfm_p \mcl_p \setminus\mfm_q \mcl_q$, and $\left\{{s\in V \st s_p\in \mfm_p \mcl_p}\right\}$ spans $\mfm_p \mcl_p/\mfm_p^2 \mcl_p$, where $\phi: X\to {\mathbf{P}}^n_{/ {k}}$ corresponds to $\mcl$ and $\left\{{s_0, \cdots, s_n}\right\}\in H^0(X; \mcl)$.
:::
