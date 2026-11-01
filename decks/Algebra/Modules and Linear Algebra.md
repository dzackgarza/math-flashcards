---
title: "Algebra::Modules and Linear Algebra"
---

::: {.front card-id="card-093f9a272e38ffe6" tags="counterexample"}
For matrices, does $A^n=B^n$ imply $A=B$?
:::

::: {.back card-id="card-093f9a272e38ffe6"}
No, counterexample with $n=2$: $M = \matt 0 1 1 0$ satisfies
$$M^2 = I = I^2$$
but $M \neq I$.
Similarly $A = \matt 0 1 {-1} 0$ satisfies $A^2 = -I$, so $A^4 = I = I^4$.
:::

::: {.front card-id="card-3d439f796f8b6ed5" tags="theorem"}
Characterizations of Diagonalizability of a Square Matrix $M$
:::

::: {.back card-id="card-3d439f796f8b6ed5"}
- $\min_M(x)/\FF$ splits into distinct linear factors over $\FF$ (i.e. is separable)
- $\FF$ contains all of the roots of $\min_M(x)/\FF$
- There exists a basis of $\FF^n$ consisting of eigenvectors of $M$
- All elementary divisors are linear
- (Sufficient) $M$ has $n$ distinct eigenvalues
- (Sufficient) $\min_M(x)/\FF$ has $n$ distinct roots.
:::

::: {.front card-id="card-2eff695f633e6c32" tags="definition"}
Definition: Free module
:::

::: {.back card-id="card-2eff695f633e6c32"}
![](https://i.imgur.com/h5r2lty.png)
:::

::: {.front card-id="card-f7021c5f2bcd3e95" tags="definition"}
Definition: Projective module
:::

::: {.back card-id="card-f7021c5f2bcd3e95"}
![](https://i.imgur.com/z4sW2hh.png)

Equivalently, for $R\dash$modules, $M$ is projective $\iff$ $M$ is a direct summand of a free module.
:::

::: {.front card-id="card-ec459ce58f2c31a5" tags="fact"}
One-step submodule test
:::

::: {.back card-id="card-ec459ce58f2c31a5"}
If $N \subseteq M$ is nonempty and $r\in R,\, m,n \in N \implies rm + n \in N$, then $N$ is a submodule of $M$.
:::

::: {.front card-id="card-69e87f20c01c0c7d" tags="definition"}
$\generators{p}\dash$primary
:::

::: {.back card-id="card-69e87f20c01c0c7d"}
For every $m\in M$ and $t\in R$ with $t\not\in \generators{p}$, there exists a $a\in R$ such that $atm = m$.
:::

::: {.front card-id="card-812bbb249aa65dc0" tags="definition"}
Noetherian Module
:::

::: {.back card-id="card-812bbb249aa65dc0"}
Any strictly increasing chain of submodules $M_1 \subsetneq M_2 \cdots$ is finite.
:::

::: {.front card-id="card-99a0471b7b951a66"}
Definition: Torsion element
:::

::: {.back card-id="card-99a0471b7b951a66"}
$m\in M$ is torsion iff $\Tor(m)\neq 0$.
:::

::: {.front card-id="card-159277c02da4e274" tags="definition"}
Definition: Torsion submodule.
:::

::: {.back card-id="card-159277c02da4e274"}
$$
\Tor(M) = \{m \in M \suchthat \exists r \in R, ~r \neq 0, ~rm = 0\}
.$$
:::

::: {.front card-id="card-1493db086eeb6fa8" tags="definition"}
Rank of a Free module
:::

::: {.back card-id="card-1493db086eeb6fa8"}
Maximal number of $R\dash$linearly independent elements of $M$.
:::

::: {.front card-id="card-a273d57c858616ae" tags="definition"}
Definition: torsionfree
:::

::: {.back card-id="card-a273d57c858616ae"}
$\Tor(M) = \theset{0}$
:::

::: {.front card-id="card-42bbc5e5051f6542" tags="definition"}
Annihilator of a module
:::

::: {.back card-id="card-42bbc5e5051f6542"}
For $M$ an $R\dash$module,
$$
\mathrm{ann}_R(M) = \theset{r\in R\suchthat \forall m\in M,\, rm=0} \normal R
.$$
:::

::: {.front card-id="card-56f070e8b6e8f02a" tags="definition"}
Irreducible Module
:::

::: {.back card-id="card-56f070e8b6e8f02a"}
Simple module, i.e. no nontrivial proper submodules.
:::

::: {.front card-id="card-83f833bba7441cf3" tags="definition"}
Indecomposable Module
:::

::: {.back card-id="card-83f833bba7441cf3"}
Can not be written as a direct sum of two nonzero submodules.
:::

::: {.front card-id="card-4cf0741a85880ea1" tags="definition"}
Definition: Rational Canonical Form
:::

::: {.back card-id="card-4cf0741a85880ea1"}
For $\phi:V\to V$, corresponds to invariant factor decomposition of $V$ as a $k[x]\dash$module,
$$
V \cong \bigoplus k[x]/ (r_i) \qquad r_1 \divides r_2 \divides \cdots
.$$
The $r_i$ are the minimal polynomials of $\phi$ restricted to $V_i$.
The matrix of $\phi$ consists of blocks of companion matrices for the $\phi_i$.
:::

::: {.front card-id="card-eb8f4e6c80b4ed10" tags="definition"}
Definition: Characteristic polynomial
:::

::: {.back card-id="card-eb8f4e6c80b4ed10"}
$$
p_A(x) = \mathrm{det}(xI - A)
.$$
:::

::: {.front card-id="card-47b4512ff859a290" tags="definition"}
Definition: Diagonalizable.
:::

::: {.back card-id="card-47b4512ff859a290"}
For a matrix $A$, similar to a diagonal matrix.
I.e. there exists a diagonal $D$ and some $P\in \mathrm{GL}(n, R)$ such that $A = PDP^{-1}$
:::

::: {.front card-id="card-98cf185a9f1888ee" tags="definition"}
Cyclic Module
:::

::: {.back card-id="card-98cf185a9f1888ee"}
For $M$ an $R\dash$module, $M$ is cyclic iff $M = \generators{m}$ iff $M \cong R/I$ for some ideal $I\normal R$.
:::

::: {.front card-id="card-c802213c7fcfdf63" tags="theorem"}
Classification of Finitely Generated Modules over a PID
:::

::: {.back card-id="card-c802213c7fcfdf63"}
![](https://i.imgur.com/z4sW2hh.png)
:::

::: {.front card-id="card-4b4a17361288fe65" tags="proposition"}
Proposition: Every free module is projective.
:::

::: {.back card-id="card-4b4a17361288fe65"}
![](https://i.imgur.com/qZiRxvR.png)
:::

::: {.front card-id="card-0a7fed02f00e4ba5" tags="definition"}
Companion matrix
:::

::: {.back card-id="card-0a7fed02f00e4ba5"}
The companion matrix of a monic polynomial $f(x)=x^n+c_{n-1}x^{n-1}+\cdots+c_0$ is the $n\times n$ matrix with ones on the subdiagonal and last column $(-c_0,\dots,-c_{n-1})^T$; its characteristic and minimal polynomials are both $f$.
:::

::: {.front card-id="card-866806e4b6b15d94" tags="definition"}
Determinant
:::

::: {.back card-id="card-866806e4b6b15d94"}
The determinant is the multiplicative map $\det:M_n(R)\to R$ given by $\det(A)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^n a_{i\sigma(i)}$; over a field, $\det A\neq0$ iff $A$ is invertible.
:::

::: {.front card-id="card-4034504749f42211" tags="definition"}
Diagonal matrix
:::

::: {.back card-id="card-4034504749f42211"}
A matrix $D=(d_{ij})$ is diagonal if $d_{ij}=0$ for all $i\neq j$.
:::

::: {.front card-id="card-569939a5be76c056" tags="definition"}
Eigenvalue
:::

::: {.back card-id="card-569939a5be76c056"}
For a linear map $T:V\to V$ over a field $k$, an eigenvalue is $\lambda\in k$ for which there exists a nonzero $v\in V$ with $T(v)=\lambda v$.
:::

::: {.front card-id="card-396d7e209117ccb1" tags="definition"}
Eigenvector
:::

::: {.back card-id="card-396d7e209117ccb1"}
An eigenvector of $T:V\to V$ for eigenvalue $\lambda$ is a nonzero $v\in V$ with $T(v)=\lambda v$.
:::

::: {.front card-id="card-52686d1a018f6aea" tags="definition"}
Finitely generated module
:::

::: {.back card-id="card-52686d1a018f6aea"}
An $R$-module $M$ is finitely generated if there exist $m_1,\dots,m_n\in M$ such that every $m\in M$ is a finite $R$-linear combination of the $m_i$; equivalently, $M$ is a quotient of $R^n$.
:::

::: {.front card-id="card-fa57eb0176bd623d" tags="definition"}
General linear group
:::

::: {.back card-id="card-fa57eb0176bd623d"}
The general linear group $\mathrm{GL}_n(R)$ is the group of invertible $n\times n$ matrices over $R$ under multiplication; over a field $k$, $\mathrm{GL}_n(k)=\{A\in M_n(k):\det A\neq0\}$.
:::

::: {.front card-id="card-84d53a4eea2910c0" tags="definition"}
Linearly independent
:::

::: {.back card-id="card-84d53a4eea2910c0"}
A subset $S$ of an $R$-module $M$ is linearly independent if every finite relation $\sum_i r_i s_i=0$ with $s_i\in S$ has all $r_i=0$; otherwise $S$ is linearly dependent.
:::

::: {.front card-id="card-44373a6fadf9b02d" tags="definition"}
Matrix
:::

::: {.back card-id="card-44373a6fadf9b02d"}
An $m\times n$ matrix over a ring $R$ is an array $(a_{ij})$ with $a_{ij}\in R$; it represents a linear map $R^n\to R^m$, and matrix multiplication is $(AB)_{ij}=\sum_k a_{ik}b_{kj}$.
:::

::: {.front card-id="card-05028f955eb3eb1f" tags="definition"}
Minimal polynomial
:::

::: {.back card-id="card-05028f955eb3eb1f"}
For a linear map $T:V\to V$ over a field, the minimal polynomial is the monic polynomial $m_T(x)$ of least positive degree with $m_T(T)=0$. For $\alpha$ algebraic over $k$, $m_\alpha(x)$ is the monic polynomial of least positive degree with $m_\alpha(\alpha)=0$.
:::

::: {.front card-id="card-1e0083c047568382" tags="definition"}
Similar matrices
:::

::: {.back card-id="card-1e0083c047568382"}
Square matrices $A,B\in M_n(k)$ are similar if $B=P^{-1}AP$ for some invertible $P\in\mathrm{GL}_n(k)$; they represent the same linear map in different bases.
:::

::: {.front card-id="card-086228c8f0868f40" tags="definition"}
Submodule
:::

::: {.back card-id="card-086228c8f0868f40"}
A subset $N\subseteq M$ is a submodule if it is a subgroup of $(M,+)$ and is closed under scalar multiplication; equivalently, $N$ is nonempty and $r\in R$, $m,n\in N$ imply $rm+n\in N$.
:::

::: {.front card-id="card-aa872b79c6d7fb88" tags="definition"}
Tensor product
:::

::: {.back card-id="card-aa872b79c6d7fb88"}
The tensor product $M \otimes_R N$ of $R$-modules is the universal target of $R$-bilinear maps: there is a bilinear map $\otimes : M \times N \to M \otimes_R N$ such that every bilinear map $M \times N \to P$ factors uniquely through it. It is constructed as the quotient of the free abelian group on $M \times N$ by the bilinearity relations.
:::

::: {.front card-id="card-307de933dfdd2661" tags="definition"}
Torsion
:::

::: {.back card-id="card-307de933dfdd2661"}
Let $R$ be an integral domain and $M$ an $R$-module. An element $m \in M$ is torsion if $rm = 0$ for some nonzero $r \in R$; the torsion submodule $M_{\mathrm{tor}}$ is the set of all such elements. $M$ is torsion if $M = M_{\mathrm{tor}}$.
:::

::: {.front card-id="card-482ee1ddf8f9c51a" tags="definition"}
Trace
:::

::: {.back card-id="card-482ee1ddf8f9c51a"}
For a finite-dimensional $k$-vector space $V$ and an endomorphism $T$, the trace $\mathrm{tr}(T)$ is the sum of the diagonal entries of any matrix of $T$, independent of the basis. For a finite extension $L/K$, $\mathrm{Tr}_{L/K}(\alpha)$ is the trace of multiplication by $\alpha$.
:::
