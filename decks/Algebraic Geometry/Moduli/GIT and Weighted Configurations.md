---
title: "Algebraic Geometry::Moduli::GIT and Weighted Configurations"
---

::: {.front card-id="git-kirwan-partial-desingularization" tags="construction example" cite="[@MS18, §4; @Kir85]"}
What does Kirwan partial desingularization do to a projective GIT problem? Use eight equally weighted points on $\mathbb P^1$ to identify its first centers.
:::

::: {.back card-id="git-kirwan-partial-desingularization"}
Let reductive $G$ act on smooth projective $X$ with ample linearization $L$ and nonempty stable locus. Among closed semistable orbits with positive-dimensional stabilizer, take the maximal stabilizer dimension. Blow up the $G$-saturations of the corresponding reductive fixed loci in $X^{ss}$.

For blowup $\pi$ and exceptional divisor $E$, use the linearization
$$\pi^*L^{\otimes m}\otimes\mathcal O(-E),\qquad m\gg0,$$
and recompute semistability. Iterate as the maximal stabilizer dimension decreases. The quotient retains the original stable quotient as an open subset and has only finite stabilizers upstairs; finite quotient singularities can remain.

For $(\mathbb P^1)^8$ with diagonal $\operatorname{SL}_2$ action and symmetric weights:

- Semistable: at most four coincident points.
- Stable: at most three coincident points.
- Closed strictly semistable orbit: four points at $0$ and four at $\infty$, with a one-dimensional torus stabilizer.

The unordered $4+4$ partitions index the first centers. Blowing up the coarse quotient without changing the linearization is not this construction.
:::

::: {.front card-id="git-linearization-stability" tags="definition comparison example"}
For a reductive group $G$ acting on a projective variety $X/\mathbb C$, define a linearization and the semistable, polystable, and stable loci for an ample line bundle $L$.
:::

::: {.back card-id="git-linearization-stability"}
A **linearization** lifts the action to $L$, linearly on fibers, compatibly with the identity and multiplication in $G$.

| Point $x$ | Condition |
| --- | --- |
| Semistable | $s(x)\ne0$ for some $m>0$ and invariant $s\in H^0(X,L^m)^G$ |
| Polystable | Semistable and $Gx$ closed in $X^{ss}$ |
| Stable | Polystable with finite stabilizer |

“Closed” here means inside the semistable locus. The projective GIT quotient is $\operatorname{Proj}\bigoplus_{m\ge0}H^0(X,L^m)^G$.

Example: $t[x:y]=[tx:t^{-1}y]$ on $\mathbb P^1$ with the induced linearization of $\mathcal O(1)$. The invariant $xy$ gives $X^{ss}=\{xy\ne0\}$; it is one orbit with finite stabilizer, hence stable, and its quotient is a point. Twisting a linearization by a character can change $X^{ss}$.
:::

::: {.front card-id="git-hilbert-mumford-weight" tags="definition theorem application"}
State the Hilbert–Mumford criterion with a fixed sign convention. Compute its weight for a diagonal action on projective space.
:::

::: {.back card-id="git-hilbert-mumford-weight"}
$X/\mathbb C$ projective, $G$ reductive, $L$ ample and linearized. For a nontrivial one-parameter subgroup $\lambda$, set $x_0=\lim_{t\to0}\lambda(t)x$ and define $\mu^L(x,\lambda)$ as the weight on $L_{x_0}$.
$$x\in X^{ss}\iff\mu^L(x,\lambda)\ge0\ \forall\lambda,\qquad
x\in X^s\iff\mu^L(x,\lambda)>0\ \forall\lambda.$$
For $X=\mathbb P(V)$ parametrizing lines, $L=\mathcal O(1)$ and $\lambda(t)v_i=t^{a_i}v_i$:
$$\mu([\sum x_iv_i],\lambda)=-\min\{a_i:x_i\ne0\}.$$
For a torus this says: zero belongs to the convex hull of the active weights. Stability requires zero in its interior in the full real character space. Opposite definitions of $\mu$ reverse the inequalities.
:::

::: {.front card-id="git-good-geometric-chow" tags="definition comparison" cite="[@Ale15, Chapters 2 and 5]"}
Distinguish a good quotient, a geometric quotient, and a Chow quotient. Which orbit data does each retain?
:::

::: {.back card-id="git-good-geometric-chow"}
For an invariant surjection $q:X\to Y$:

| Quotient | Defining data/conditions |
| --- | --- |
| Good | $q$ affine, $\mathcal O_Y=(q_*\mathcal O_X)^G$; images of invariant closed sets are closed; disjoint invariant closed sets have disjoint images |
| Geometric | Fibers are orbits, $Y$ has the quotient topology, and $\mathcal O_Y=(q_*\mathcal O_X)^G$ |
| Chow | For projective $X$, take the closure in its Chow variety of the cycles $[\overline{Gx}]$ for generic orbits of fixed dimension and degree |

In GIT, $X^{ss}\to X/\!/G$ is good; two points map together iff their orbit closures in $X^{ss}$ meet. Each fiber has one closed orbit. Its restriction over the stable locus is geometric.

A Chow quotient records limiting **orbit cycles**, including components and multiplicities. It is not defined by selecting a linearization. Authors may then normalize the Chow quotient; state that extra operation.
:::

::: {.front card-id="weighted-curves-hassett" tags="definition application"}
Define a weighted stable pointed curve and its Hassett space. What are the exact collision and rational-component conditions?
:::

::: {.back card-id="weighted-curves-hassett"}
Weights $a_i\in\mathbb Q$, $0<a_i\le1$, $2g-2+\sum a_i>0$. A connected projective nodal curve $C$ with labeled smooth points $p_i$ is $a$-stable iff:

- For every coincident group $I$, $\sum_{i\in I}a_i\le1$.
- $K_C+\sum a_ip_i$ is ample.

On a component $E$ of normalization genus $g_E$, with $n_E$ branches of nodes:
$$2g_E-2+n_E+\sum_{p_i\in E}a_i>0.$$
Thus a rational tail with one attaching node needs total marking weight $>1$; a rational bridge needs positive marking weight. The stack of these curves is $\overline{\mathcal M}_{g,a}$; its coarse space is $\overline M_{g,a}$.

Example: two weight-$1/2$ points may collide; a weight-$1$ point cannot collide with any other positive-weight marking.
:::

::: {.front card-id="weighted-chambers-reduction-git" tags="definition comparison construction" cite="[@AS12]"}
Compare Hassett weight chambers and GIT chambers. Describe the reduction map when curve weights decrease and the GIT test for weighted points on $\mathbb P^1$.
:::

::: {.back card-id="weighted-chambers-reduction-git"}
Hassett walls: $\sum_{i\in I}a_i=1$. In a chamber the allowed collision subsets and stable components stay fixed. If $0<b_i\le a_i$ and $2g-2+\sum b_i>0$, the reduction
$$\overline M_{g,a}\longrightarrow\overline M_{g,b}$$
lowers weights and contracts components on which $K_C+\sum b_ip_i$ is not ample. A rational tail of total new weight $\le1$ contracts to a collision.

GIT-equivalent linearizations have the same semistable locus; their regions form a chamber decomposition of the ample linearization cone. Wall crossing changes the quotient through the wall quotient.

For $(\mathbb P^1)^n$ with diagonal $\operatorname{SL}_2$ action and weights $w_i>0$:
$$\text{semistable}\iff\sum_{p_i=p}w_i\le\tfrac12\sum_iw_i\quad\forall p;$$
replace $\le$ by $<$ for stability. For four equal weights, two coincident points are semistable but not stable; three are unstable.
:::

::: {.front card-id="moduli-f-curves-stable-graphs" tags="definition construction example"}
Define a stable graph, an F-curve on $\overline M_{0,n}$, and an F-nef divisor. Give the moving component explicitly.
:::

::: {.back card-id="moduli-f-curves-stable-graphs"}
A stable graph is a connected finite graph with labeled legs and vertex genera $g_v\ge0$, satisfying $2g_v-2+\operatorname{val}(v)>0$ at every vertex; valence includes legs. Total genus: $\sum_vg_v+b_1(\Gamma)$.

Partition $[n]=I_1\sqcup I_2\sqcup I_3\sqcup I_4$ into nonempty sets. Vary a four-pointed rational spine in $\overline M_{0,4}\cong\mathbb P^1$. At its $j$th point attach a fixed rational tail carrying $I_j$ when $|I_j|\ge2$; for a singleton use the marking itself. The resulting numerical curve class is $F_{I_1,I_2,I_3,I_4}$.

$D$ is F-nef iff $D\cdot F\ge0$ for all such classes. Nef $\Rightarrow$ F-nef. The converse is the F-conjecture, not part of the definition. For $n=4$, the spine is the entire $\overline M_{0,4}$.
:::
