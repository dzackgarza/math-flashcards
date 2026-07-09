Simple group
%
No nontrivial normal subgroups
%
definition
---

Sylow Theorems
%
Write $\abs{G} = p^n m$ with $(p, m) = 1$.

# Sylow 1

Writing \(\abs{G} = \prod p_i^{n_i}\), there exist Sylow \(p_i\dash\)subgroups \(P_i\) of order \(p_i^{n_i}\) for every $i$.

# Sylow 2

All Sylows are conjugate.

# Sylow 3

1. \(n_p\) divides $m$
1. \(n_p \equiv 1 \mod p\)
2. \(n_p = [G: N_G(P)]\)
%
theorem
---

Recognizing Direct Products
%
When there exist two subgroups $H, K \leq G$ such that

1. $H\intersect K = \emptyset$
2. $G = HK$
3. $H$ and $K$ are both normal.
%
theorem
---

Solvable Group
%
A group is **solvable** iff it has a composition series with *abelian* composition factors.
%
definition
---

Composition Series
%
A **composition series** of $G$ is a sequence of subgroups
\[
1=N_{0} \leq N_{1} \leq N_{2} \leq \cdots \leq N_{k-1} \leq N_{k}=G
\]
such that $N_i \normal N_{i+1}$ and the *composition factors* $N_{i+1}/N_i$ are simple.
%
definition
---

Alternating Group
%
The kernel of the sign homomorphism, i.e. the set of even permutations (sign = 1).
%
definition
---

Even vs Odd Permutations
%
- Even: $\varepsilon(\sigma) = 1$, product of even number of transpositions.
- Odd: $\varepsilon(\sigma) = -1$, product of *odd* number of transpositions.
%
definition
---

How to determine sign of a permutation
%
A cycle is odd iff it has an odd number of odd cycles (i.e. *even* number of elements in cycle).
%
definition
---

What is the sign of the cycle $\sigma=(123456)(789)(10~11)(12~13~14~15)(16~17~18)$?
%
$\varepsilon(\sigma) = -1$, since it has 3 (an odd number) cycles of odd cycles (even length).
%
problem
---

Burnside's Formula
%
The number of orbits is equal to the average number of fixed points:
\[\abs{G} \abs{X/G} = \sum \abs{X^g}\]
where

- $X/G$ is the set of orbits
- $X^g = \theset{x\in X \suchthat g.x = x}$ are the fixed points of $g$.
%
formula
---

Stabilizer
%
A subgroup: $G_x = \theset{g\in G \suchthat g.x = x}$.
%
definition, notation
---

$G_x$
%
The Stabilizer subgroup: $G_x = \theset{g\in G \suchthat g.x = x} \leq G$.
%
definition, notation
---

Notation and definition of fixed points of a group action.
%
$X^g = \theset{x\in X \suchthat g.x = x} \subseteq X$
%
definition, notation
---

Class Equation
%
\[
\abs{G} = \abs{Z(G)} + \sum_{i} [G: C_G(x_i)]
\]
where $C_G(x) \da \ts{ g\in G \st gxg\inv = x }$ is the centralizer of $x$.
%
definition, notation
---

$p\dash$group
%
A group of order $p^n$ for some $n\geq 1$.
%
definition
---

Lagrange's Theorem
%
Any $H\leq G$ has size dividing $\abs{G}$.
%
theorem
---

Fermat's Little Theorem
%
$a^p \cong a \mod p$, and if $p$ does not divide $a$, $a^{p-1} \cong 1 \mod p$.
%
theorem
---

Euler's Theorem
%
$a^{\phi(n)} \cong 1 \mod n$.
%
theorem
---

$\phi(p^k) = ?$
%
$\phi(p^k) = p^{k-1}(p-1) = p^k \qty{1 - {1\over p}}$
%
formula
---

Definition: Transitive Group Action
%
A group action $G\actson X$ is *transitive* iff for every pair $x, y\in X$ there exists a $g\in G$ such that $g.x = y$.
%
definition
---

Groups of Order 6
%
1 Abelian, 1 Nonabelian

1. $\ZZ/6\ZZ$
2. $D_3$
%
fact
---

Groups of Order 8
%
3 Abelian, 2 Nonabelian

1. $\ZZ/8\ZZ$
2. $\ZZ/4\ZZ \times \ZZ/2\ZZ$
3. $(\ZZ/2\ZZ)^3$
4. $D_4$
5. $Q_8$
%
fact
---

Groups of Order 9
%
1. $\ZZ/9\ZZ$
2. $(\ZZ/3\ZZ)^2$
%
fact
---

Groups of Order 10
%
1 Abelian, 1 Nonabelian

1. $\ZZ/10\ZZ$
2. $D_{5}$
%
fact
---

Groups of Order 12
%
2 Abelian, 3 Nonabelian

1. $\ZZ/4\ZZ \times \ZZ/3\ZZ$
2. $(\ZZ/2\ZZ)^2 \times \ZZ/3\ZZ$
3. $A_4$
4. $D_6$
5. $\gens{a,b,c\suchthat a^2, b^2, c^2, abc}$
%
fact
---

Groups of Order 14
%
1 Abelian, 1 Nonabelian

1. $\ZZ/14\ZZ$
2. $D_7$
%
fact
---

Groups of Order 15
%
$\ZZ/15\ZZ$
%
fact
---

Groups of Order 16
%
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
12. $Q_{16} = \gens{a,b,c \suchthat a^4=b^2=c^2=abc}$
13. $QD_{16} = \gens{r,s\suchthat r^8, s^2, srs\inv s^{-3}}$
14. $(\ZZ/4\ZZ\cross \ZZ/2\ZZ)\semidirect \ZZ/2\ZZ$ (Pauli matrices)
%
fact
---

Groups of Order 18
%
2 Abelian, 2 Nonabelian

1. $\ZZ/18\ZZ$
2. $(\ZZ/3\ZZ)^2\times \ZZ/2\ZZ$
3. $D_9$
4. $S_3 \cross \ZZ/3\ZZ$
%
fact
---

Groups of Order 20
%
2 Abelian, 3 Nonabelian

1. $\ZZ/20\ZZ$
2. $(\ZZ/2\ZZ)^2\times \ZZ/5\ZZ$
3. $D_{10}$
4. $\ZZ/5\ZZ \semidirect \ZZ/4\ZZ$
5. $\gens{a,b,c \suchthat a^5, b^2,c^2}$
%
fact
---

Order of the smallest nonabelian group
%
Order six: $D_3$
%
fact
---

Groups of Order 4
%
$\ZZ/4\ZZ, (\ZZ/2\ZZ)^2$

![](https://i.imgur.com/8H2HQKO.png)
%
fact
---

One step subgroup test
%
\( a, b\in H \implies ab^{-1} \in H  \) implies that $H$ is a subgroup.
%
fact
---

Elementary Divisors
%
\(G \cong \bigoplus \ZZ/p_i^{\alpha_i} \ZZ\) with the $p_i$ not necessarily distinct.
%
definition
---

Invariant Factors
%
\( r_1 \divides r_2 \divides \cdots \)
%
definition
---

Centralizer
%
\[
Z_G(S) = \ts{g\in G \st gsg\inv = s\, \forall s\in S}
.\]
%
definition
---

Normalizer
%
\[
N_G(S) \da \ts{g\in G \st gSg\inv = S}
.\]
%
definition
---

$X^n$
%
$X^g = \theset{x\in X \suchthat g.x = x} \subseteq X$
%
definition, notation
