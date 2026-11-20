---
title: "Algebraic Geometry::Singularities::Local Models and Resolutions"
---

::: {.front card-id="singularity-regular-singular" tags="definition"}
For a complex algebraic variety $X$, how do the local ring and tangent space detect whether $p$ is nonsingular?
:::

::: {.back card-id="singularity-regular-singular"}
The local ring $\mathcal O_{X,p}$ is regular:
$$\dim_{\mathbb C}\mathfrak m_p/\mathfrak m_p^2=\dim\mathcal O_{X,p}.$$
The left side is the embedding dimension, equal to $\dim_{\mathbb C}T_pX$.
:::

::: {.front card-id="singularity-ordinary-double" tags="definition"}
Give the analytic normal form of an ordinary double point on a complex hypersurface of dimension $n$. What condition on its quadratic term characterizes it?
:::

::: {.back card-id="singularity-ordinary-double"}
$$x_0^2+\cdots+x_n^2=0.$$
The quadratic term is nondegenerate. For $n=1$ this is a node; for $n=2$ it is a Du Val $A_1$ surface singularity.
:::

::: {.front card-id="singularity-normal-crossings" tags="definition"}
For a reduced divisor in a smooth complex variety, distinguish normal crossings from simple normal crossings.
:::

::: {.back card-id="singularity-normal-crossings"}
Normal crossings means that locally analytically its equation is $x_1\cdots x_r=0$ in smooth coordinates. Simple normal crossings additionally requires its irreducible components to be smooth. An irreducible nodal plane cubic has normal crossings but not simple normal crossings.
:::

::: {.front card-id="singularity-pinch-point" tags="definition"}
Give an equation and normalization parametrization for the complex pinch point. Where is its singular locus?
:::

::: {.back card-id="singularity-pinch-point"}
$$x^2=y^2z,\qquad (u,v)\longmapsto(x,y,z)=(uv,u,v^2).$$
The singular locus is $x=y=0$. Away from the origin it has double normal crossings; the origin is the pinch point.
:::

::: {.front card-id="singularity-embedded-resolution" tags="definition"}
What does an embedded resolution of a reduced divisor $D$ in a smooth complex variety require beyond making the strict transform smooth?
:::

::: {.back card-id="singularity-embedded-resolution"}
A proper birational morphism $f:Y\to X$, an isomorphism over $X\setminus D$, with $Y$ smooth and the reduced total transform $(f^{-1}D)_{\mathrm{red}}$ a simple normal crossings divisor. The strict transform must also meet the exceptional divisor with normal crossings.
:::

::: {.front card-id="card-8c26bb201aefe21c" tags="definition" cite="[@BKR01, Theorem 1.2]"}
What is a crepant resolution? Which singularities can have one? Give examples where one exists and where none exists.
:::

::: {.back card-id="card-8c26bb201aefe21c"}
A resolution $f:Y\to X$ of a normal $\mathbb Q$-Gorenstein variety is crepant if $K_Y=f^*K_X$ as $\mathbb Q$-divisors, equivalently if all exceptional discrepancies are zero.

- Necessary: $X$ canonical and $K_X$ Cartier. Since $K_Y$ is Cartier, $f^*K_X$ is Cartier, and $a(E)=0$ for every exceptional divisor of $Y$.
- Exists: the minimal resolution of a Du Val surface germ (all $(-2)$-curves). A small resolution of the threefold node $xy=zw$, with exceptional curve $\mathbb P^1$ and no exceptional divisor. $\mathbb C^3/G$ for finite $G\subset\mathrm{SL}_3$ (Bridgeland–King–Reid: $G$-Hilb).
- None: a singular terminal $X$, since every exceptional divisor has $a(E)>0$; e.g. $\frac12(1,1,1)$. Any klt non-canonical germ, e.g. $\frac13(1,1)$.
:::

::: {.front card-id="card-3ee6736250e4d3aa"}
What is a resolution of singularities of an integral complex variety $X$?
:::

::: {.back card-id="card-3ee6736250e4d3aa"}
A proper birational morphism $f:Y\to X$ with $Y$ smooth, restricting to an isomorphism over $X_{\mathrm{reg}}$. For an integral complex curve, normalization is a resolution.
:::

::: {.front card-id="card-28accb71191608ee"}
What is a **resolution**?
:::

::: {.back card-id="card-28accb71191608ee"}
For $X$ singular, a proper morphism $\pi: W\to X$ where $W$ is smooth, $\pi^{-1}(X^{\mathsf{sm}}) \subseteq W$ is dense and $\pi$ induces an isomorphism on the smooth locus.
:::

::: {.front card-id="card-63ead0b6b3f67ab5"}
What is a **minimal resolution**?
:::

::: {.back card-id="card-63ead0b6b3f67ab5"}
Minimal $W$ is minimal iff whenever $W'\to V$ is another resolution, it factors as $W'\to W\to V$.

Exist uniquely in dimensions 1 and 2, but may not in higher dimensions. For a surface with an isolated singularity at 0: $\pi: W\to V$ is minimal iff $\pi^{-1}(0)$ does not contain any exceptional curves of the first kind. Any non-minimal resolution must contain a -1 curve.
:::

::: {.front card-id="theorem-hironaka-resolution" tags="theorem"}
State resolution of singularities for a reduced variety over a field of characteristic zero, including the behavior over the regular locus and the exceptional divisor.
:::

::: {.back card-id="theorem-hironaka-resolution"}
There is a proper birational morphism $\pi:\widetilde X\to X$ with $\widetilde X$ smooth, which is an isomorphism over the regular locus of $X$. It can be chosen so that the exceptional locus is a divisor with simple normal crossings.
:::

::: {.front card-id="card-d5ec173bf75ab3ce"}
What is a smoothing of an isolated complex analytic singularity? Give a hypersurface example.
:::

::: {.back card-id="card-d5ec173bf75ab3ce"}
A flat deformation over a disk whose central fiber is the given germ and whose nearby fibers are smooth. For an isolated hypersurface singularity $f=0$, the family $f(x)=t$ gives a local smoothing on a sufficiently small representative.
:::

::: {.front card-id="card-3fb785303c85fc6d"}
Describe the weighted dual graph of a good resolution of a normal complex surface singularity. Must it be a tree?
:::

::: {.back card-id="card-3fb785303c85fc6d"}
Vertices represent exceptional curves and carry their genera and self-intersections. Edges represent intersection points. The intersection matrix is negative definite. The graph need not be a tree: surface cusp resolutions have cycles. Du Val resolutions have ADE trees of rational curves with self-intersection $-2$.
:::

::: {.front card-id="card-dee2f67fdb8f773a"}
What is a complex analytic hypersurface singularity?
:::

::: {.back card-id="card-dee2f67fdb8f773a"}
A germ analytically isomorphic to $(V(f),0)\subset(\mathbb C^{n+1},0)$, with $f$ a nonzero convergent power series, $f(0)=0$, and $df(0)=0$. Its analytic local ring is $\mathbb C\{x_0,\ldots,x_n\}/(f)$.
:::

