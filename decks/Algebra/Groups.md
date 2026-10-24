---
title: "Algebra::Groups"
---

::: {.front card-id="card-b008f5085a6d1cda" tags="fact"}
Groups of Order 4
:::

::: {.back card-id="card-b008f5085a6d1cda"}
$\ZZ/4\ZZ, (\ZZ/2\ZZ)^2$

![](https://i.imgur.com/8H2HQKO.png)
:::

::: {.front card-id="card-cf40695dd24f6bfe" tags="definition"}
Simple group
:::

::: {.back card-id="card-cf40695dd24f6bfe"}
No nontrivial normal subgroups
:::

::: {.front card-id="card-915f54b39fa8258a" tags="theorem"}
Sylow Theorems
:::

::: {.back card-id="card-915f54b39fa8258a"}
Write $\abs{G} = p^n m$ with $(p, m) = 1$.
**Sylow 1**
Writing $\abs{G} = \prod p_i^{n_i}$, there exist Sylow $p_i\dash$subgroups $P_i$ of order $p_i^{n_i}$ for every $i$.
**Sylow 2**
All Sylows are conjugate.
**Sylow 3**
1. $n_p$ divides $m$
1. $n_p \equiv 1 \mod p$
2. $n_p = [G: N_G(P)]$
:::

::: {.front card-id="card-a18d602866d2f5e7" tags="theorem"}
Recognizing Direct Products
:::

::: {.back card-id="card-a18d602866d2f5e7"}
When there exist two subgroups $H, K \leq G$ such that

1. $H\intersect K = \theset{e}$
2. $G = HK$
3. $H$ and $K$ are both normal.
:::

::: {.front card-id="card-72f30598d5e143df" tags="definition"}
Solvable Group
:::

::: {.back card-id="card-72f30598d5e143df"}
A group is **solvable** iff it has a composition series with *abelian* composition factors.
:::

::: {.front card-id="card-ea4a8e83e6ef9a58" tags="definition"}
Composition Series
:::

::: {.back card-id="card-ea4a8e83e6ef9a58"}
A **composition series** of $G$ is a sequence of subgroups
$$
1=N_{0} \leq N_{1} \leq N_{2} \leq \cdots \leq N_{k-1} \leq N_{k}=G
$$
such that $N_i \normal N_{i+1}$ and the *composition factors* $N_{i+1}/N_i$ are simple.
:::

::: {.front card-id="card-4599c237f2075f09" tags="definition"}
Alternating Group
:::

::: {.back card-id="card-4599c237f2075f09"}
The kernel of the sign homomorphism, i.e. the set of even permutations (sign = 1).
:::

::: {.front card-id="card-b75d2d555be43bd8" tags="definition"}
Even vs Odd Permutations
:::

::: {.back card-id="card-b75d2d555be43bd8"}
- Even: $\varepsilon(\sigma) = 1$, product of even number of transpositions.
- Odd: $\varepsilon(\sigma) = -1$, product of *odd* number of transpositions.
:::

::: {.front card-id="card-459d6ef8cf6969e1" tags="definition"}
How to determine sign of a permutation
:::

::: {.back card-id="card-459d6ef8cf6969e1"}
A permutation is odd iff it has an odd number of odd cycles (i.e. *even* number of elements in cycle).
:::

::: {.front card-id="card-e49ce84d5f6805f6" tags="problem"}
What is the sign of the permutation $\sigma=(123456)(789)(10~11)(12~13~14~15)(16~17~18)$?
:::

::: {.back card-id="card-e49ce84d5f6805f6"}
$\varepsilon(\sigma) = -1$, since it has 3 (an odd number) cycles of odd cycles (even length).
:::

::: {.front card-id="card-c856cf15aaf01e5f" tags="formula"}
Burnside's Formula
:::

::: {.back card-id="card-c856cf15aaf01e5f"}
The number of orbits is equal to the average number of fixed points:
$$\abs{G} \abs{X/G} = \sum \abs{X^g}$$
where

- $X/G$ is the set of orbits
- $X^g = \theset{x\in X \suchthat g.x = x}$ are the fixed points of $g$.
:::

::: {.front card-id="card-fd5acb683e622ef6" tags="definition, notation"}
Stabilizer $G_x$
:::

::: {.back card-id="card-fd5acb683e622ef6"}
The stabilizer subgroup of $x\in X$: $G_x = \theset{g\in G \suchthat g.x = x} \leq G$.
:::

::: {.front card-id="card-f11068e768c2ff54" tags="definition, notation"}
Notation and definition of fixed points of a group action.
:::

::: {.back card-id="card-f11068e768c2ff54"}
$X^g = \theset{x\in X \suchthat g.x = x} \subseteq X$
:::

::: {.front card-id="card-8e26c93389690ee9" tags="definition, notation"}
Class Equation
:::

::: {.back card-id="card-8e26c93389690ee9"}
$$
\abs{G} = \abs{Z(G)} + \sum_{i} [G: C_G(x_i)]
$$
where the $x_i$ are representatives of the conjugacy classes not contained in $Z(G)$, and $C_G(x) \definedas \theset{ g\in G \st gx\inverseof{g} = x }$ is the centralizer of $x$.
:::

::: {.front card-id="card-5aa5a4e54b29a608" tags="definition"}
$p\dash$group
:::

::: {.back card-id="card-5aa5a4e54b29a608"}
A group of order $p^n$ for some $n\geq 1$.
:::

::: {.front card-id="card-a0038397f434b584" tags="theorem"}
Lagrange's Theorem
:::

::: {.back card-id="card-a0038397f434b584"}
Any $H\leq G$ has size dividing $\abs{G}$.
:::

::: {.front card-id="card-5840af88e7b1b12e" tags="theorem"}
Fermat's Little Theorem
:::

::: {.back card-id="card-5840af88e7b1b12e"}
$a^p \cong a \mod p$, and if $p$ does not divide $a$, $a^{p-1} \cong 1 \mod p$.
:::

::: {.front card-id="card-0a9c3e99c060fbc3" tags="theorem"}
Euler's Theorem
:::

::: {.back card-id="card-0a9c3e99c060fbc3"}
$a^{\phi(n)} \cong 1 \mod n$.
:::

::: {.front card-id="card-fc9997caf3d294d1" tags="formula"}
$\phi(p^k) = ?$
:::

::: {.back card-id="card-fc9997caf3d294d1"}
$\phi(p^k) = p^{k-1}(p-1) = p^k \qty{1 - {1\over p}}$
:::

::: {.front card-id="card-babf2a63ffe295fa" tags="definition"}
Definition: Transitive Group Action
:::

::: {.back card-id="card-babf2a63ffe295fa"}
A group action $G\actson X$ is *transitive* iff for every pair $x, y\in X$ there exists a $g\in G$ such that $g.x = y$.
:::

::: {.front card-id="card-b9b26b87a4fad5ea" tags="fact"}
Groups of Order 6
:::

::: {.back card-id="card-b9b26b87a4fad5ea"}
1 Abelian, 1 Nonabelian

1. $\ZZ/6\ZZ$
2. $D_3$
:::

::: {.front card-id="card-3b54585e15103700" tags="fact"}
Groups of Order 8
:::

::: {.back card-id="card-3b54585e15103700"}
3 Abelian, 2 Nonabelian

1. $\ZZ/8\ZZ$
2. $\ZZ/4\ZZ \times \ZZ/2\ZZ$
3. $(\ZZ/2\ZZ)^3$
4. $D_4$
5. $Q_8$
:::

::: {.front card-id="card-e7fa33f2ca7be927" tags="fact"}
Groups of Order 9
:::

::: {.back card-id="card-e7fa33f2ca7be927"}
1. $\ZZ/9\ZZ$
2. $(\ZZ/3\ZZ)^2$
:::

::: {.front card-id="card-c82040664e08b3fe" tags="fact"}
Groups of Order 10
:::

::: {.back card-id="card-c82040664e08b3fe"}
1 Abelian, 1 Nonabelian

1. $\ZZ/10\ZZ$
2. $D_{5}$
:::

::: {.front card-id="card-0c2d27e174dd0f9f" tags="fact"}
Groups of Order 12
:::

::: {.back card-id="card-0c2d27e174dd0f9f"}
2 Abelian, 3 Nonabelian

1. $\ZZ/4\ZZ \times \ZZ/3\ZZ$
2. $(\ZZ/2\ZZ)^2 \times \ZZ/3\ZZ$
3. $A_4$
4. $D_6$
5. $\generators{a,b,c\suchthat a^2, b^2, c^2, abc}$
:::

::: {.front card-id="card-993f4b0747a17bfe" tags="fact"}
Groups of Order 14
:::

::: {.back card-id="card-993f4b0747a17bfe"}
1 Abelian, 1 Nonabelian

1. $\ZZ/14\ZZ$
2. $D_7$
:::

::: {.front card-id="card-4434149847c1fef7" tags="fact"}
Groups of Order 15
:::

::: {.back card-id="card-4434149847c1fef7"}
$\ZZ/15\ZZ$
:::

::: {.front card-id="card-dd6caf4026bbdf6a" tags="fact"}
Groups of Order 16
:::

::: {.back card-id="card-dd6caf4026bbdf6a"}
5 Abelian, 9 Nonabelian

1. $\ZZ/16\ZZ$
2. $(\ZZ/4\ZZ)^2$
3. $\ZZ/8\ZZ \times \ZZ/2\ZZ$
4. $\ZZ/4\ZZ \times (\ZZ/2\ZZ)^2$
5. $(\ZZ/2\ZZ)^4$
6. $(\ZZ/4\ZZ \cross \ZZ/2\ZZ) \semidirect \ZZ/2\ZZ$
7. $\ZZ/4\ZZ \semidirect \ZZ/4\ZZ$
8. $\ZZ/8\ZZ \semidirect \ZZ/2\ZZ$
9. $D_8$
10. $D_4\cross \ZZ/2\ZZ$
11. $Q_8 \cross \ZZ/2\ZZ$
12. $Q_{16} = \generators{a,b,c \suchthat a^4=b^2=c^2=abc}$
13. $QD_{16} = \generators{r,s\suchthat r^8, s^2, sr\inverseof{s} s^{-3}}$
14. $(\ZZ/4\ZZ\cross \ZZ/2\ZZ)\semidirect \ZZ/2\ZZ$ (Pauli matrices)
:::

::: {.front card-id="card-12c78965899c507d" tags="fact"}
Groups of Order 18
:::

::: {.back card-id="card-12c78965899c507d"}
2 Abelian, 2 Nonabelian

1. $\ZZ/18\ZZ$
2. $(\ZZ/3\ZZ)^2\times \ZZ/2\ZZ$
3. $D_9$
4. $S_3 \cross \ZZ/3\ZZ$
:::

::: {.front card-id="card-510ef3bac0943b94" tags="fact"}
Groups of Order 20
:::

::: {.back card-id="card-510ef3bac0943b94"}
2 Abelian, 3 Nonabelian

1. $\ZZ/20\ZZ$
2. $(\ZZ/2\ZZ)^2\times \ZZ/5\ZZ$
3. $D_{10}$
4. $\ZZ/5\ZZ \semidirect \ZZ/4\ZZ$
5. $\generators{a,b,c \suchthat a^5, b^2,c^2}$
:::

::: {.front card-id="card-f92cc6898a6b1ed6" tags="fact"}
Order of the smallest nonabelian group
:::

::: {.back card-id="card-f92cc6898a6b1ed6"}
Order six: $D_3$
:::

::: {.front card-id="card-0e162a922273d1f9" tags="fact"}
One step subgroup test
:::

::: {.back card-id="card-0e162a922273d1f9"}
$a, b\in H \implies ab^{-1} \in H$ implies that $H$ is a subgroup.
:::

::: {.front card-id="card-6eec437405b93857" tags="definition"}
Elementary Divisors
:::

::: {.back card-id="card-6eec437405b93857"}
$G \cong \bigoplus \ZZ/p_i^{\alpha_i} \ZZ$ with the $p_i$ not necessarily distinct.
:::

::: {.front card-id="card-265c167b145b9341" tags="definition"}
Invariant Factors
:::

::: {.back card-id="card-265c167b145b9341"}
$r_1 \divides r_2 \divides \cdots$
:::

::: {.front card-id="card-892b21c1809e1616" tags="definition"}
Centralizer
:::

::: {.back card-id="card-892b21c1809e1616"}
$$
Z_G(S) = \theset{g\in G \st gs\inverseof{g} = s\, \forall s\in S}
.$$
:::

::: {.front card-id="card-edbf73faf92e1c26" tags="definition"}
Normalizer
:::

::: {.back card-id="card-edbf73faf92e1c26"}
$$
N_G(S) \definedas \theset{g\in G \st gS\inverseof{g} = S}
.$$
:::

::: {.front card-id="card-6872241e3d971a34"}
What is the Mathieu group?
:::

::: {.back card-id="card-6872241e3d971a34"}
$M_{20} = A_5\rtimes C_2^4$, order 960.
:::

::: {.front card-id="card-5742bfb73f112647"}
What is a sporadic simple group?
:::

::: {.back card-id="card-5742bfb73f112647"}
One of 26 exceptional groups: not cyclic, alternating, or of Lie type.
:::

