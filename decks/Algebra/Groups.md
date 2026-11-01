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


::: {.front card-id="card-dc7999a8f6c6fd7f" tags="definition"}
Center
:::

::: {.back card-id="card-dc7999a8f6c6fd7f"}
The center of a group $G$ is $Z(G) = \{z \in G : zg = gz \text{ for all } g \in G\}$; it is a normal subgroup of $G$.
:::

::: {.front card-id="card-0a36ff1308b232bf" tags="definition"}
Center of a group
:::

::: {.back card-id="card-0a36ff1308b232bf"}
The center of $G$ is $Z(G)=\{z\in G:zg=gz\text{ for all }g\in G\}$; it is a normal abelian subgroup.
:::

::: {.front card-id="card-be29258462168dfc" tags="definition"}
Composition factor
:::

::: {.back card-id="card-be29258462168dfc"}
For a composition series $1=N_0\trianglelefteq N_1\trianglelefteq\cdots\trianglelefteq N_k=G$, the composition factors are the simple quotient groups $N_{i+1}/N_i$.
:::

::: {.front card-id="card-0ffd0be50f3dd00e" tags="definition"}
Conjugacy class
:::

::: {.back card-id="card-0ffd0be50f3dd00e"}
The conjugacy class of $x\in G$ is $\{gxg^{-1}:g\in G\}$; conjugacy classes partition $G$.
:::

::: {.front card-id="card-3901fd88342de459" tags="definition"}
Coprime
:::

::: {.back card-id="card-3901fd88342de459"}
Integers $a$ and $b$ are coprime (relatively prime) if $\gcd(a,b)=1$.
:::

::: {.front card-id="card-c9ac48471e97591c" tags="definition, prerequisite"}
Coset
:::

::: {.back card-id="card-c9ac48471e97591c"}
For $H\le G$ and $g\in G$, the left coset is $gH=\{gh:h\in H\}$ and the right coset is $Hg=\{hg:h\in H\}$; the left cosets partition $G$, as do the right cosets.
:::

::: {.front card-id="card-003ad7055ed7c0f5" tags="definition"}
Cycle decomposition
:::

::: {.back card-id="card-003ad7055ed7c0f5"}
Every permutation of a finite set is a product of disjoint cycles, uniquely up to order; the cycle $(a_1\cdots a_k)$ sends $a_i\mapsto a_{i+1}$ and $a_k\mapsto a_1$.
:::

::: {.front card-id="card-3905282a990eaff1" tags="definition"}
Derived subgroup
:::

::: {.back card-id="card-3905282a990eaff1"}
The derived subgroup (commutator subgroup) of $G$ is $[G,G] = \langle \{ghg^{-1}h^{-1} : g,h \in G\} \rangle$; it is the smallest normal subgroup of $G$ with abelian quotient.
:::

::: {.front card-id="card-0905ae3af369942c" tags="definition"}
Dihedral group
:::

::: {.back card-id="card-0905ae3af369942c"}
The dihedral group $D_n$ of order $2n$ is the symmetry group of a regular $n$-gon; it has presentation $\langle r,s\mid r^n=s^2=e,\ srs=r^{-1}\rangle$.
:::

::: {.front card-id="card-a27839d2f99893f1" tags="definition"}
Direct product
:::

::: {.back card-id="card-a27839d2f99893f1"}
For groups $G$ and $H$, the direct product $G\times H$ is the set of ordered pairs with componentwise operation; more generally $\prod_i G_i$ is the Cartesian product with componentwise operation.
:::

::: {.front card-id="card-b310befb160a3863" tags="definition"}
Euler totient function
:::

::: {.back card-id="card-b310befb160a3863"}
Euler's totient function $\varphi(n)$ counts the integers $1\le k\le n$ with $\gcd(k,n)=1$. If $n=\prod_i p_i^{e_i}$, then $\varphi(n)=\prod_i p_i^{e_i-1}(p_i-1)$.
:::

::: {.front card-id="card-d4b75f23a7727c9f" tags="definition"}
Free group
:::

::: {.back card-id="card-d4b75f23a7727c9f"}
The free group $F(S)$ on a set $S$ consists of finite words in $S \cup S^{-1}$ modulo cancellation, with concatenation as multiplication; every map $S \to G$ into a group extends uniquely to a homomorphism $F(S) \to G$.
:::

::: {.front card-id="card-8c23df2ebf32bad0" tags="definition, prerequisite"}
Group
:::

::: {.back card-id="card-8c23df2ebf32bad0"}
A group is a set $G$ with a binary operation $\cdot$ such that the operation is associative, there is an identity $e$ with $eg=ge=g$, and every $g\in G$ has an inverse $g^{-1}$ with $gg^{-1}=g^{-1}g=e$.
:::

::: {.front card-id="card-139d9f345ad2a7de" tags="definition, prerequisite"}
Group action
:::

::: {.back card-id="card-139d9f345ad2a7de"}
A left action of a group $G$ on a set $X$ is a map $G\times X\to X$, $(g,x)\mapsto g\cdot x$, with $e\cdot x=x$ and $(gh)\cdot x=g\cdot(h\cdot x)$; equivalently, a homomorphism $G\to\operatorname{Sym}(X)$.
:::

::: {.front card-id="card-3665e688bed7d83b" tags="definition, prerequisite"}
Group homomorphism
:::

::: {.back card-id="card-3665e688bed7d83b"}
A map $\varphi:G\to H$ between groups is a homomorphism if $\varphi(ab)=\varphi(a)\varphi(b)$ for all $a,b\in G$; then $\varphi(e_G)=e_H$ and $\varphi(g^{-1})=\varphi(g)^{-1}$.
:::

::: {.front card-id="card-87fe69a5afd1401f" tags="definition"}
Group of lie type
:::

::: {.back card-id="card-87fe69a5afd1401f"}
A finite group of Lie type is the group of $\mathbb{F}_q$-points of a connected reductive algebraic group over $\mathbb{F}_q$, or equivalently the fixed points of a Frobenius endomorphism; examples include $\mathrm{GL}_n(\mathbb{F}_q)$ and $\mathrm{SL}_n(\mathbb{F}_q)$.
:::

::: {.front card-id="card-52312fa352f5e3c0" tags="definition"}
Group presentation
:::

::: {.back card-id="card-52312fa352f5e3c0"}
A presentation $\langle S \mid R \rangle$ denotes the group $F(S)/N$, where $F(S)$ is the free group on $S$ and $N$ is the normal closure of the set $R$ of relators.
:::

::: {.front card-id="card-8363ce39057c40e3" tags="definition, prerequisite"}
Image
:::

::: {.back card-id="card-8363ce39057c40e3"}
For a map $\varphi:G\to H$, the image is $\operatorname{im}\varphi=\{\varphi(g):g\in G\}\subseteq H$; for a group homomorphism it is a subgroup of $H$.
:::

::: {.front card-id="card-803bc68692ec52be" tags="definition"}
Index of a subgroup
:::

::: {.back card-id="card-803bc68692ec52be"}
For $H\le G$, the index $[G:H]$ is the number of distinct left cosets of $H$ in $G$ (equivalently, the number of right cosets); if $G$ is finite, $[G:H]=|G|/|H|$.
:::

::: {.front card-id="card-73ef693dc7fa7d03" tags="definition, prerequisite"}
Inverse
:::

::: {.back card-id="card-73ef693dc7fa7d03"}
In a group $G$, the inverse of $g$ is the unique element $g^{-1}$ with $g g^{-1} = g^{-1} g = e$. For a bijection $f : X \to Y$, the inverse map $f^{-1} : Y \to X$ satisfies $f^{-1} \circ f = \mathrm{id}_X$ and $f \circ f^{-1} = \mathrm{id}_Y$.
:::

::: {.front card-id="card-cfa1f0e3b3dec3ee" tags="definition, prerequisite"}
Kernel
:::

::: {.back card-id="card-cfa1f0e3b3dec3ee"}
For a group homomorphism $\varphi:G\to H$, the kernel is $\ker\varphi=\{g\in G:\varphi(g)=e_H\}$; it is a normal subgroup of $G$.
:::

::: {.front card-id="card-f42c869a59bd7fc2" tags="definition, prerequisite"}
Normal subgroup
:::

::: {.back card-id="card-f42c869a59bd7fc2"}
A subgroup $N\le G$ is normal, written $N\trianglelefteq G$, if $gNg^{-1}=N$ for every $g\in G$; equivalently, every left coset of $N$ equals a right coset, so $G/N$ is a group.
:::

::: {.front card-id="card-bacde55ea4062944" tags="definition, prerequisite"}
Orbit
:::

::: {.back card-id="card-bacde55ea4062944"}
For a group action $G\curvearrowright X$ and $x\in X$, the orbit is $G\cdot x=\{g\cdot x:g\in G\}$; the orbits partition $X$.
:::

::: {.front card-id="card-d5f7d876e651169f" tags="definition"}
Order of a group
:::

::: {.back card-id="card-d5f7d876e651169f"}
The order $|G|$ of a group $G$ is the cardinality of its underlying set. A group is finite if $|G|<\infty$.
:::

::: {.front card-id="card-a84a6f53e8d2101f" tags="definition"}
Prime number
:::

::: {.back card-id="card-a84a6f53e8d2101f"}
A prime number is an integer $p>1$ whose only positive divisors are $1$ and $p$.
:::

::: {.front card-id="card-4dae99ac10104cdd" tags="definition"}
Product of subgroups
:::

::: {.back card-id="card-4dae99ac10104cdd"}
For $H,K\le G$, the product is $HK=\{hk:h\in H,\ k\in K\}$; it is a subgroup iff $HK=KH$.
:::

::: {.front card-id="card-f7194cce580b0b61" tags="definition"}
Quaternion group
:::

::: {.back card-id="card-f7194cce580b0b61"}
The quaternion group is $Q_8=\{\pm1,\pm i,\pm j,\pm k\}$ with $i^2=j^2=k^2=ijk=-1$; the generalized quaternion group $Q_{2^n}$ has order $2^n$ and presentation $\langle a,b\mid a^{2^{n-1}}=e,\ b^2=a^{2^{n-2}},\ bab^{-1}=a^{-1}\rangle$.
:::

::: {.front card-id="card-f476dc23874c19e1" tags="definition, prerequisite"}
Quotient group
:::

::: {.back card-id="card-f476dc23874c19e1"}
For $N\trianglelefteq G$, the quotient group $G/N$ is the set of cosets $\{gN:g\in G\}$ with multiplication $(gN)(hN)=ghN$.
:::

::: {.front card-id="card-fb5a91e10631831b" tags="definition"}
Semidirect product
:::

::: {.back card-id="card-fb5a91e10631831b"}
If $N\trianglelefteq G$, $H\le G$, $N\cap H=\{e\}$, and $G=NH$, then $G$ is the internal semidirect product $N\rtimes H$. Equivalently, a homomorphism $\alpha:H\to\operatorname{Aut}(N)$ gives the external semidirect product with $(n,h)(n',h')=(n\,\alpha(h)(n'),hh')$.
:::

::: {.front card-id="card-e332dd610e6a7a7e" tags="definition"}
Sign homomorphism
:::

::: {.back card-id="card-e332dd610e6a7a7e"}
The sign homomorphism $\varepsilon:S_n\to\{\pm1\}$ sends a permutation to $(-1)^k$, where $k$ is the number of transpositions in any decomposition; it is well defined, and $\ker\varepsilon=A_n$.
:::

::: {.front card-id="card-1e593a43a522a7db" tags="definition, prerequisite"}
Subgroup
:::

::: {.back card-id="card-1e593a43a522a7db"}
A subset $H\subseteq G$ is a subgroup, written $H\le G$, if $H$ is nonempty and $a,b\in H$ implies $ab^{-1}\in H$; equivalently, $H$ is closed under the group operation and inverses.
:::

::: {.front card-id="card-538c931c90bd562b" tags="definition"}
Subgroup generated by a subset
:::

::: {.back card-id="card-538c931c90bd562b"}
For $S\subseteq G$, the subgroup generated by $S$ is the smallest subgroup $\langle S\rangle\le G$ containing $S$; it consists of all finite products of elements of $S$ and their inverses.
:::

::: {.front card-id="card-9c28023c578ad25f" tags="definition"}
Sylow p-subgroup
:::

::: {.back card-id="card-9c28023c578ad25f"}
If $|G|=p^n m$ with $p$ prime and $p\nmid m$, a Sylow $p$-subgroup is a subgroup of order $p^n$; equivalently, it is a maximal subgroup whose order is a power of $p$.
:::

::: {.front card-id="card-1fb1c7623a79c00d" tags="definition"}
Symmetric group
:::

::: {.back card-id="card-1fb1c7623a79c00d"}
The symmetric group $S_n$ is the group of all permutations of $\{1,\dots,n\}$ under composition; $|S_n|=n!$.
:::

::: {.front card-id="card-a8ebd8c9eb453a0d" tags="definition"}
Transposition
:::

::: {.back card-id="card-a8ebd8c9eb453a0d"}
A transposition is a permutation that swaps two elements and fixes all others, i.e. a 2-cycle $(i\,j)$.
:::
