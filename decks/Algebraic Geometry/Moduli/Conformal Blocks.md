---
title: "Algebraic Geometry::Moduli::Conformal Blocks"
---

::: {.front card-id="conformal-affine-level-weights" tags="definition construction example" cite="[@AGS14, §3.1]"}
Define the affine current algebra, level, and allowed highest weights used for conformal blocks. Specialize to $\mathfrak{sl}_2$.
:::

::: {.back card-id="conformal-affine-level-weights"}
For a simple complex Lie algebra $\mathfrak g$, use the invariant form with long roots of square two. Its central extension is
$$\widehat{\mathfrak g}=(\mathfrak g\otimes\mathbb C((z)))\oplus\mathbb CK,$$
$$[x\otimes f,y\otimes g]=[x,y]\otimes fg+(x,y)\operatorname{Res}(g\,df)K.$$
Level $\ell\in\mathbb Z_{\ge0}$ means $K$ acts by $\ell$. The integrable highest-weight modules $\mathcal H_{\lambda,\ell}$ are indexed by dominant integral weights with $\langle\lambda,\theta^\vee\rangle\le\ell$, where $\theta$ is the highest root.

For $\mathfrak{sl}_2$, write $\lambda=a\omega$; the allowed labels are $a=0,1,\ldots,\ell$. The zero-mode highest-weight space has dimension $a+1$; the affine module is generally infinite-dimensional.
:::

::: {.front card-id="conformal-coinvariants-bundles" tags="definition construction" cite="[@AGS14, §3.1]"}
Define conformal-block coinvariants on a pointed curve and the associated divisor. Specify the duality convention.
:::

::: {.back card-id="conformal-coinvariants-bundles"}
Let $(C;p_1,\ldots,p_n)$ be a smooth projective complex curve, with labels $\lambda_i$ at common level $\ell$. Put $U=C\setminus\{p_i\}$ and $\mathcal H=\bigotimes_i\mathcal H_{\lambda_i,\ell}$. Laurent expansion at each $p_i$ makes $\mathfrak g\otimes\mathcal O(U)$ act diagonally. Define
$$\mathbb V_{\mathfrak g,\ell,\vec\lambda}(C,\vec p)
=\mathcal H/(\mathfrak g\otimes\mathcal O(U))\mathcal H.$$
The central terms cancel by the residue theorem. This finite-dimensional space is independent of local-coordinate choices and extends in families to a vector bundle on $\overline{\mathcal M}_{g,n}$.

The associated conformal-block divisor is
$$\mathbb D_{\mathfrak g,\ell,\vec\lambda}
=c_1(\mathbb V)=c_1(\det\mathbb V).$$
Here $\mathbb V$ denotes coinvariants, as in Alexeev–Gibney–Swinarski. Another common convention calls $\mathbb V^\vee$ the space of conformal blocks; dualizing changes the sign of $c_1$.
:::

::: {.front card-id="conformal-factorization-fusion" tags="definition formula application" cite="[@AGS14, §3.2]"}
Define fusion coefficients and state factorization at a node. Compute the rank for four $\mathfrak{sl}_2$ labels all equal to one at levels one and two.
:::

::: {.back card-id="conformal-factorization-fusion"}
The fusion coefficient $N_{\lambda\mu}^{\nu}$ is the rank of genus-zero three-point coinvariants with labels $(\lambda,\mu,\nu^*)$. At a node, normalize and insert labels $\alpha,\alpha^*$ on its two preimages, then sum over all level-$\ell$ dominant weights $\alpha$.

For a separating node:
$$\mathbb V(C,\vec\lambda)\simeq
\bigoplus_{\alpha\in P_\ell}
\mathbb V(C_1,\vec\lambda_1,\alpha)\otimes
\mathbb V(C_2,\vec\lambda_2,\alpha^*).$$
For a nonseparating node, use one normalization component with both inserted labels.

For $\mathfrak{sl}_2$, labels $a,b,c\in\{0,\ldots,\ell\}$ are self-dual; the three-point rank is one iff
$$a+b+c\ \text{even},\qquad |a-b|\le c\le\min(a+b,2\ell-a-b),$$
and zero otherwise. Four labels $1$ have intermediate label $0$ at level one, and $0$ or $2$ at level two: ranks one and two.
:::

::: {.front card-id="conformal-quasiparabolic-bundles" tags="definition comparison example" cite="[@AGS14, §3.1]"}
Define a quasiparabolic principal bundle on a pointed curve. Distinguish its flags from parabolic weights.
:::

::: {.back card-id="conformal-quasiparabolic-bundles"}
Fix a connected reductive complex group $G$ and parabolic subgroups $P_i\subset G$. A quasiparabolic bundle is a principal $G$-bundle $E\to C$ with a reduction of $E_{p_i}$ to $P_i$ at each marking: equivalently, a point of $(E/P_i)_{p_i}$.

For $G=\operatorname{GL}_r$, this is a rank-$r$ vector bundle with prescribed partial flags in the marked fibers. For $r=2$, a full flag is a chosen line in each fiber.

A parabolic bundle additionally assigns ordered real weights to the flag steps. These weights enter parabolic degree and stability; the flag alone does not specify them. In the geometric construction of conformal blocks, the labels specify flag/character data and the level specifies the determinant-line power.
:::
