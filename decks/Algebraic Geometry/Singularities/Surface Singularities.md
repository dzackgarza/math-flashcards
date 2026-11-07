---
title: "Algebraic Geometry::Singularities::Surface Singularities"
---

::: {.front card-id="card-8f343de9852359e9" tags="definition"}
Characterize a rational double point over $\mathbb C$ using rationality and multiplicity.
:::

::: {.back card-id="card-8f343de9852359e9"}
An isolated normal surface singularity that is rational and has multiplicity $2$. These are precisely the Du Val surface singularities.
:::

::: {.front card-id="singularity-duval-equations" tags="definition"}
Give analytic equations for the complex Du Val singularities.
:::

::: {.back card-id="singularity-duval-equations"}
| Type | Equation in $\mathbb C^3$ |
| --- | --- |
| $A_n$, $n\ge1$ | $xy-z^{n+1}=0$ |
| $D_n$, $n\ge4$ | $x^2+y^2z+z^{n-1}=0$ |
| $E_6$ | $x^2+y^3+z^4=0$ |
| $E_7$ | $x^2+y^3+yz^3=0$ |
| $E_8$ | $x^2+y^3+z^5=0$ |
:::

::: {.front card-id="singularity-duval-recognition" tags="application"}
Identify the surface germs $xy=z^5$, $x^2+y^2z+z^3=0$, and $x^2+y^3+z^5=0$. How many exceptional curves occur in their minimal resolutions?
:::

::: {.back card-id="singularity-duval-recognition"}
| Equation | Type | Exceptional curves |
| --- | --- | --- |
| $xy=z^5$ | $A_4$ | $4$ |
| $x^2+y^2z+z^3=0$ | $D_4$ | $4$ |
| $x^2+y^3+z^5=0$ | $E_8$ | $8$ |

Each exceptional curve is rational with self-intersection $-2$.
:::

::: {.front card-id="singularity-cyclic-quotient" tags="definition"}
Define the complex cyclic quotient surface germ $\frac1r(1,a)$, where $r>1$ and $\gcd(r,a)=1$. Which member gives $A_{r-1}$?
:::

::: {.back card-id="singularity-cyclic-quotient"}
It is the quotient of $(\mathbb C^2,0)$ by
$$\zeta\cdot(u,v)=(\zeta u,\zeta^a v),\qquad \zeta^r=1.$$
For $a=r-1$, the invariant functions $x=u^r,y=v^r,z=uv$ satisfy $xy=z^r$, giving $A_{r-1}$.
:::

::: {.front card-id="singularity-duval-quotients" tags="definition"}
Which finite linear quotients of $\mathbb C^2$ give Du Val surface singularities?
:::

::: {.back card-id="singularity-duval-quotients"}
The quotients $\mathbb C^2/G$ for nontrivial finite subgroups $G\subset\operatorname{SL}_2(\mathbb C)$. Cyclic groups give $A$-types; binary dihedral groups give $D$-types; binary tetrahedral, octahedral, and icosahedral groups give $E_6,E_7,E_8$.
:::

::: {.front card-id="singularity-simple-elliptic" tags="definition"}
What is a simple elliptic surface singularity? Give a geometric example and distinguish it from a surface cusp.
:::

::: {.back card-id="singularity-simple-elliptic"}
A normal complex surface singularity whose minimal resolution has exceptional divisor a smooth elliptic curve. The affine cone over a smooth plane cubic is an example; its exceptional elliptic curve has self-intersection $-3$. A surface cusp instead has a cycle of rational curves, or a nodal rational curve.
:::

::: {.front card-id="card-862154888a8bb22d"}
Give an analytic equation for a complex surface singularity of type $A_1$.
:::

::: {.back card-id="card-862154888a8bb22d"}
$$xy-z^2=0\quad\text{in }(\mathbb C^3,0).$$
It is the vertex of a quadratic cone, also isomorphic to $\mathbb C^2/\{\pm1\}$.
:::

::: {.front card-id="card-df4853bcf54d4927"}
What type of curve is the resolution of an $A_1$ singularity?
:::

::: {.back card-id="card-df4853bcf54d4927"}
$D\cong {\mathbf{P}}^1$ with $D^2 = -2$.
:::

::: {.front card-id="card-1aab55ee31850bbb"}
Characterize a complex Du Val surface singularity by its minimal resolution.
:::

::: {.back card-id="card-1aab55ee31850bbb"}
The exceptional curves are smooth rational curves of self-intersection $-2$ whose dual graph is an ADE Dynkin diagram. These are the rational double points, equivalently the singular canonical surface germs.
:::

::: {.front card-id="card-dcd1e437d41fbead"}
What is a cusp singularity of a complex normal surface?
:::

::: {.back card-id="card-dcd1e437d41fbead"}
Its minimal resolution has exceptional divisor a negative-definite cycle of smooth rational curves, or an irreducible rational curve with one node. This is a surface germ; the plane-curve cusp $y^2=x^3$ is a different, one-dimensional singularity.
:::

