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

::: {.front card-id="modules-length-composition-series" tags="definition theorem application" cite="[@AM18, Propositions 6.7–6.9]"}
Define module length and a composition series. What are the simple factors, and how does length behave in short exact sequences? Compute the length of $k[x,y]/(x^2,y)$.
:::

::: {.back card-id="modules-length-composition-series"}
A composition series of an $R$-module $M$ is a finite strict chain
$$M=M_0\supsetneq M_1\supsetneq\cdots\supsetneq M_n=0$$
whose successive quotients $M_{i-1}/M_i$ are simple. Its length is $n$, the number of links. Every composition series has the same length and the same simple factors with multiplicities (Jordan–Hölder); the common length is $\ell_R(M)$. A module has finite length exactly when it is both Noetherian and Artinian. Every simple $R$-module is $R/\mathfrak m$ for a maximal ideal $\mathfrak m$.

For a short exact sequence $0\to M'\to M\to M''\to0$ of finite-length modules,
$$\ell_R(M)=\ell_R(M')+\ell_R(M'').$$
Composition series for $M'$ and $M''$ concatenate after taking images and inverse images. Finite direct sums therefore add lengths.

Let $S=k[x,y]$ and $M=S/(x^2,y)$. The chain
$$M\supsetneq(x)M\supsetneq0$$
has quotients isomorphic to $S/(x,y)=k$, so $\ell_S(M)=2$ and the only simple factor is $k$, twice. Both Noetherian and Artinian are necessary for finite length in general: $k[x]$ is Noetherian but not Artinian and has infinite length, while a Prüfer group is Artinian but not Noetherian as a $\mathbb Z$-module and also has infinite module length.
:::
