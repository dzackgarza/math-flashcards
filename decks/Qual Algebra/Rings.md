---
title: "Qual Algebra::Rings"
---

- Characteristic of a ring

    The smallest number $n$ such that $\sum_{j=1}^n 1_R = 0_R$.

    Equivalently, the kernel $n\ZZ$ of the unique map $\ZZ\to R$.

    tags: definition

- Zorn's Lemma

    If every chain in a poset $P$ has an upper bound in $P$, then $P$ contains a maximal element.

    Note: a *chain* is a totally ordered subset.

    tags: theorem

- Zero Divisor

    An element $r\in R$ is a *zero divisor* if there exists an $ x\in X $ such that $ rx=0$.

    Equivalently, the map $x\mapsto rx$ is *not* injective.

    tags: definition

- Definition: simple ring.

    A ring $R$ is **simple** iff its only two-sided ideals are $(0)$ and $R$.

    tags: definition

- Definition: irreducible.

    A nonzero nonunit ring element $r\in R$ is *irreducible* iff $r=ab$ implies $a$ or $b$ is a unit.

    tags: definition

- Definition: prime.

    A nonzero nonunit ring element $r$ is prime iff $r\divides ab$ implies $r\divides a$ or $r\divides b$.

    tags: definition

- Definition: integral domain.

    A nonzero commutative ring with no nonzero zero divisors.

    tags: definition

- Gauss' Lemma

    Let $R$ be a UFD with fraction field $F$ and $p \in R[x]$.
    If $p$ is reducible in $F[x]$, then $p$ is reducible in $R[x]$.

    > Implies that $R$ a UFD implies $R[\theset{x_i}]$ is again a UFD.

    tags: theorem

- Definition: prime ideal.

    An ideal $\mathfrak{p}\normal R$ is prime iff it is proper and $ab\in \mathfrak{p} \implies a\in \mathfrak{p}$ or $b\in \mathfrak{p}$.

    tags: definition

- Definition: Maximal ideal.

    An ideal $I\normal R$ is **maximal** iff $I\subseteq J \normal R$ implies $J=R$.

    tags: definition

- Definition: Euclidean domain.

    Admits a "remainder measuring" function $f: R\setminus\theset{0} \to \NN$ such that $a\in R, b\in R^\bullet$ implies there exist $q, r\in R$ such that $a = bq + r$ with either $r=0$ or $f(r) < f(b)$.

    tags: definition

- Definition: Unique Factorization Domain

    Every nonzero element $x\in R$ can be written as $x = u\prod p_i$ where the $p_i$ are irreducible and $u \in R^\times$.

    This decomposition is unique up to multiplication by a unit, and a permutation of the factors $\sigma$ that makes each $p_i$ associate to $p_{\sigma(i)}$

    tags: definition
