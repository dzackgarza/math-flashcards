---
title: "Algebraic Geometry::Singularities::Plane Curves"
---

::: {.front card-id="definition-delta-normalization-genus" tags="definition application"}
Define the delta invariant of a reduced complex curve singularity. How does it recover geometric genus from arithmetic genus, and why do a node and a cusp have the same delta?
:::

::: {.back card-id="definition-delta-normalization-genus"}
For the normalization $\nu:\widetilde C\to C$,
$$\delta_p=\dim_{\mathbb C}(\nu_*\mathcal O_{\widetilde C}/\mathcal O_C)_p.$$
It measures the local defect of normality. For an integral projective curve, the normalization sequence gives
$$p_a(C)=g(\widetilde C)+\sum_p\delta_p.$$
For a connected reduced curve with $r$ irreducible components, replace $g(\widetilde C)$ by $\sum_i g(\widetilde C_i)$ and subtract $r-1$ on the right.

For the cusp, $\mathbb C\{t\}\!/\mathbb C\{t^2,t^3\}$ has vector-space basis the class of $t$, so $\delta=1$. At a node, normalization separates two branches; functions on the curve are the pairs with equal constant terms, again giving a one-dimensional quotient. Delta alone does not distinguish their branch counts.
:::

::: {.front card-id="application-milnor-tjurina-meaning" tags="definition application"}
What do the Milnor and Tjurina numbers measure for an isolated complex plane-curve singularity? Compare a node and a cusp.
:::

::: {.back card-id="application-milnor-tjurina-meaning"}
The Milnor number $\mu=\dim_{\mathbb C}\mathbb C\{x,y\}/(f_x,f_y)$ is the rank of the first reduced homology of the Milnor fiber, hence counts its vanishing cycles. The Tjurina number $\tau=\dim_{\mathbb C}\mathbb C\{x,y\}/(f,f_x,f_y)$ is the dimension of the base of a miniversal deformation of the hypersurface germ. Always $\tau\le\mu$.

For $xy=0$, the Jacobian algebra is $\mathbb C$, so $\mu=\tau=1$. For $y^2-x^3=0$, it has basis $1,x$, so $\mu=\tau=2$. Both have $\delta=1$; the relation $\mu=2\delta-r+1$ distinguishes the node's two branches from the cusp's one branch. In these weighted-homogeneous examples Euler's identity puts $f$ in its Jacobian ideal, explaining $\tau=\mu$.
:::

::: {.front card-id="example-blowup-node-cusp" tags="example application"}
Blow up the origin of $\mathbb A^2_{\mathbb C}$. Compute the strict transforms of $y^2=x^2(x+1)$ and $y^2=x^3$, and their intersections with the exceptional divisor.
:::

::: {.back card-id="example-blowup-node-cusp"}
In the chart $y=xq$, the total transforms have equations $x^2(q^2-1-x)=0$ and $x^2(q^2-x)=0$. Removing the exceptional factor gives the strict transforms
$$q^2=1+x,\qquad q^2=x.$$
The first meets $E=V(x)$ transversely at $q=1,-1$, separating the node's branches. The second is smooth but tangent to $E$ at $q=0$, with intersection multiplicity two. Thus one blowup makes the cusp's strict transform smooth, but does not yet give a divisor with normal crossings.
:::

::: {.front card-id="example-node-smoothing" tags="example construction"}
For $X=V(xy-t)\subset\mathbb A^3_{\mathbb C}$ with map to $\mathbb A^1_t$, describe the fibers, total space, and flatness. Where is the morphism not smooth?
:::

::: {.back card-id="example-node-smoothing"}
For $t\ne0$ the fiber is $\mathbb G_m$; at zero it is the two coordinate axes meeting in a node. Eliminating $t$ identifies $X$ with $\mathbb A^2$, so the total space is smooth. Its coordinate ring is torsion-free over the PID $\mathbb C[t]$, hence flat. The differential of $t=xy$ vanishes only at $(0,0)$, so the morphism fails to be smooth only at that point.
:::

::: {.front card-id="singularity-node-cusp-tacnode" tags="definition"}
Give analytic normal forms over $\mathbb C$ for a node, an ordinary cusp, and a tacnode. Identify their plane-curve $A$-types.
:::

::: {.back card-id="singularity-node-cusp-tacnode"}
| Type | Equation | ADE type |
| --- | --- | --- |
| Node | $xy=0$ | $A_1$ |
| Ordinary cusp | $y^2-x^3=0$ | $A_2$ |
| Tacnode | $y^2-x^4=0$ | $A_3$ |
:::

::: {.front card-id="singularity-ordinary-multiple" tags="definition"}
What is an ordinary $m$-fold point of a reduced complex plane curve? Give an equation.
:::

::: {.back card-id="singularity-ordinary-multiple"}
It has multiplicity $m$ and tangent cone a product of $m$ distinct linear forms. Equivalently, its branches are smooth with pairwise distinct tangent lines. For distinct $\lambda_i$,
$$\prod_{i=1}^m(y-\lambda_i x)=0$$
is an example.
:::

::: {.front card-id="singularity-recognize-tangent-branches" tags="application"}
Classify the germ $y^2-x^6=0$ over $\mathbb C$. How many branches does it have, and what is their intersection multiplicity?
:::

::: {.back card-id="singularity-recognize-tangent-branches"}
It is an $A_5$ plane-curve singularity with smooth branches $y=x^3$ and $y=-x^3$. Their intersection multiplicity is $3$. It is not an ordinary double point: the branches share a tangent.
:::

::: {.front card-id="singularity-puiseux-branch" tags="definition"}
For coprime integers $p,q>1$, parametrize the plane branch $y^p=x^q$ and give its multiplicity and delta invariant.
:::

::: {.back card-id="singularity-puiseux-branch"}
$$x=t^p,\qquad y=t^q,\qquad \operatorname{mult}_0C=\min(p,q),\qquad \delta=\frac{(p-1)(q-1)}2.$$
:::

::: {.front card-id="singularity-curve-ade-equations" tags="definition"}
Give the complex analytic normal forms of the simple plane-curve singularities $A_n,D_n,E_6,E_7,E_8$.
:::

::: {.back card-id="singularity-curve-ade-equations"}
| Type | Equation |
| --- | --- |
| $A_n$, $n\ge1$ | $x^2+y^{n+1}=0$ |
| $D_n$, $n\ge4$ | $x^2y+y^{n-1}=0$ |
| $E_6$ | $x^3+y^4=0$ |
| $E_7$ | $x^3+xy^3=0$ |
| $E_8$ | $x^3+y^5=0$ |

This is the simple classification, not a classification of all plane-curve singularities.
:::

::: {.front card-id="example-cuspidal-cubic" tags="example construction"}
Give a projective cuspidal cubic over $\mathbb C$ and its normalization map. What is its local singularity?
:::

::: {.back card-id="example-cuspidal-cubic"}
Take $Y^2Z=X^3$. Its normalization is
$$\mathbb P^1\longrightarrow C,\qquad [s:t]\longmapsto[s^2t:s^3:t^3].$$
On $Z=1$ this is $u\mapsto(u^2,u^3)$. The cusp $(0,0)$ has one branch, tangent cone $y^2=0$, and $\delta=1$. The arithmetic genus is one; the normalization has genus zero.
:::

::: {.front card-id="example-nodal-cubic" tags="example construction"}
Give a projective nodal cubic over $\mathbb C$ and its normalization map. Which points lie above the node?
:::

::: {.back card-id="example-nodal-cubic"}
Take $Y^2Z=X^2(X+Z)$. Its normalization is
$$[s:t]\longmapsto[t(s^2-t^2):s(s^2-t^2):t^3].$$
On $Z=1$, $x=u^2-1$ and $y=u(u^2-1)$. The points $u=1,-1$ lie above the node $(0,0)$. Its tangent cone is $(y-x)(y+x)=0$ and $\delta=1$. Its arithmetic genus is one and its normalization has genus zero.
:::

::: {.front card-id="example-cubic-degeneration" tags="example construction"}
Give a flat family of plane cubics over $\mathbb C$ whose fiber at zero is nodal and whose nearby fibers are smooth. Is the total space smooth at the node?
:::

::: {.back card-id="example-cubic-degeneration"}
Use
$$Y^2Z=X^3+X^2Z+tZ^3.$$
On $Z=1$, repeated roots of $x^3+x^2+t$ occur only for $t=0,-4/27$. Restrict the base to $\mathbb A^1\setminus\{-4/27\}$. The zero fiber is the nodal cubic $y^2=x^2(x+1)$; all other fibers are smooth. This family of nonzero cubic equations is flat, with Hilbert polynomial $3m$. At the node the partial derivative of the defining equation with respect to $t$ is $-1$, so the total space is smooth there.
:::

::: {.front card-id="card-1543972cfbfd2c13"}
What is a branch of a reduced complex curve germ?
:::

::: {.back card-id="card-1543972cfbfd2c13"}
An irreducible component of the analytic germ. Branches correspond to minimal primes of the completed local ring and to points of the normalization above the singular point.
:::

