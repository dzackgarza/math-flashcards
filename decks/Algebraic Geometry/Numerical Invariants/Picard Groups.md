---
title: "Algebraic Geometry::Numerical Invariants::Picard Groups"
---

::: {.front card-id="standard-picard-structure" tags="formula"}
For a smooth connected projective complex variety, distinguish $\operatorname{Pic}(X)$, $\operatorname{Pic}^0(X)$, $\operatorname{NS}(X)$, and $\rho(X)$.
:::

::: {.back card-id="standard-picard-structure"}
$$0\to\operatorname{Pic}^0(X)\to\operatorname{Pic}(X)\to\operatorname{NS}(X)\to0,\qquad \rho(X)=\operatorname{rank}\operatorname{NS}(X).$$
$\operatorname{Pic}(X)$ is the group of line bundles; $\operatorname{Pic}^0(X)$ consists of classes algebraically equivalent to zero and is an abelian variety of dimension $h^{0,1}$. The Néron–Severi group is finitely generated and can have torsion. The Picard number records only its rank.
:::

::: {.front card-id="standard-picard-basic-spaces" tags="formula"}
Compute the algebraic Picard groups of $\mathbb A^n_{\mathbb C}$, $(\mathbb G_m)^n_{\mathbb C}$, and $\mathbb P^n_{\mathbb C}$, for $n\ge1$.
:::

::: {.back card-id="standard-picard-basic-spaces"}
$$\operatorname{Pic}(\mathbb A^n)=0,\qquad\operatorname{Pic}((\mathbb G_m)^n)=0,\qquad\operatorname{Pic}(\mathbb P^n)=\mathbb Z[\mathcal O(1)].$$
:::

::: {.front card-id="standard-picard-curves" tags="formula"}
Describe the Picard group of a smooth connected projective complex curve $C$. What changes after choosing a point $p\in C$?
:::

::: {.back card-id="standard-picard-curves"}
$$0\to\operatorname{Jac}(C)\to\operatorname{Pic}(C)\xrightarrow{\deg}\mathbb Z\to0.$$
Choosing $p$ splits this sequence by $d\mapsto\mathcal O_C(dp)$. Thus $\operatorname{Pic}(C)\cong\operatorname{Jac}(C)\oplus\mathbb Z$ noncanonically and $\operatorname{NS}(C)\cong\mathbb Z$.
:::

::: {.front card-id="standard-picard-projective-bundles" tags="formula"}
For a rank-$r\ge2$ vector bundle $E$ on a smooth connected complex variety $X$, compute $\operatorname{Pic}(\mathbb P(E))$.
:::

::: {.back card-id="standard-picard-projective-bundles"}
$$\operatorname{Pic}(\mathbb P(E))=\pi^*\operatorname{Pic}(X)\oplus\mathbb Z[\mathcal O_{\mathbb P(E)}(1)].$$
In particular, $\operatorname{Pic}(\mathbb P^a\times\mathbb P^b)=\mathbb Z[\mathcal O(1,0)]\oplus\mathbb Z[\mathcal O(0,1)]$ for $a,b\ge1$.
:::

::: {.front card-id="standard-picard-blowups" tags="formula"}
For a smooth connected complex variety $X$ and a smooth connected center $Z$ with $\operatorname{codim}_XZ\ge2$, compute $\operatorname{Pic}(\operatorname{Bl}_ZX)$.
:::

::: {.back card-id="standard-picard-blowups"}
$$\operatorname{Pic}(\operatorname{Bl}_ZX)\cong f^*\operatorname{Pic}(X)\oplus\mathbb Z[E].$$
Here $E$ is the exceptional divisor. For a blowup of $\mathbb P^2$ at $r$ distinct points, the generators are $H,E_1,\ldots,E_r$.
:::

::: {.front card-id="standard-picard-quadrics" tags="formula"}
Describe $\operatorname{Pic}(Q^n)$ for a smooth complex quadric, including the low-dimensional exceptions and the hyperplane class.
:::

::: {.back card-id="standard-picard-quadrics"}
| Dimension | Picard group | Hyperplane class |
| --- | --- | --- |
| $n=1$ | $\mathbb Z[\mathcal O_{\mathbb P^1}(1)]$ | $2[\mathcal O_{\mathbb P^1}(1)]$ |
| $n=2$ | $\mathbb Z f_1\oplus\mathbb Z f_2$ | $f_1+f_2$ |
| $n\ge3$ | $\mathbb Z[\mathcal O_Q(1)]$ | primitive generator |
:::

::: {.front card-id="standard-picard-enriques" tags="formula"}
Describe the torsion, rank, and identity component of the Picard group of a complex Enriques surface.
:::

::: {.back card-id="standard-picard-enriques"}
$$\operatorname{Pic}^0(S)=0,\qquad\operatorname{Pic}(S)=\operatorname{NS}(S)\cong\mathbb Z^{10}\oplus\mathbb Z/2.$$
The nonzero torsion class is $K_S$. The numerical lattice is $\operatorname{Num}(S)\cong U\oplus E_8(-1)$.
:::

::: {.front card-id="standard-picard-abelian" tags="formula"}
For a complex abelian variety $A$, identify $\operatorname{Pic}^0(A)$. What is $\operatorname{NS}(A)$ for a very general principally polarized $A$?
:::

::: {.back card-id="standard-picard-abelian"}
$$\operatorname{Pic}^0(A)=\widehat A.$$
For a very general principally polarized abelian variety, $\operatorname{NS}(A)=\mathbb Z[\Theta]$. Thus Picard number one does not mean that every line bundle is a power of $\Theta$: degree-zero classes still vary in $\widehat A$.
:::

::: {.front card-id="standard-picard-rho-hodge" tags="formula"}
For a smooth projective complex surface, must $\rho(X)=h^{1,1}(X)$? Explain using K3 surfaces.
:::

::: {.back card-id="standard-picard-rho-hodge"}
No. $\rho(X)\le h^{1,1}(X)$ counts integral algebraic classes, not the complex dimension of the whole $(1,1)$-space. Every complex K3 has $h^{1,1}=20$, while a very general polarized K3 has $\rho=1$.
:::

