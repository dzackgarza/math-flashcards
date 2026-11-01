---
title: "Analysis::Precalculus"
---

::: {.front card-id="card-3da969015f7a0ced" tags="formula"}
$\sin(\pi/6) = \cdots$
:::

::: {.back card-id="card-3da969015f7a0ced"}
$$
\sin(\pi/6) = {1\over 2}
.$$
:::

::: {.front card-id="card-c43fcef1f7134a7d" tags="formula"}
$\sin(\pi/4) = \cdots$
:::

::: {.back card-id="card-c43fcef1f7134a7d"}
$$
\sin(\pi/4) = {\sqrt 2 \over 2}
.$$
:::

::: {.front card-id="card-c1ffb6d1be5908e1" tags="formula"}
$\sin(\pi/3) = \cdots$
:::

::: {.back card-id="card-c1ffb6d1be5908e1"}
$$
\sin(\pi/3) = {\sqrt 3 \over 2}
.$$
:::

::: {.front card-id="card-c09e3f122bfc8334" tags="formula"}
$\cos(\pi/6) = \cdots$
:::

::: {.back card-id="card-c09e3f122bfc8334"}
$$
\cos(\pi/6) = {\sqrt 3 \over 2}
.$$
:::

::: {.front card-id="card-da26ea1267490355" tags="formula"}
$\cos(\pi/4) = \cdots$
:::

::: {.back card-id="card-da26ea1267490355"}
$$
\cos(\pi/4) = {\sqrt 2 \over 2}
.$$
:::

::: {.front card-id="card-b166005070df3fc0" tags="formula"}
$\cos(\pi/3) = \cdots$
:::

::: {.back card-id="card-b166005070df3fc0"}
$$
\cos(\pi/3) = {1 \over 2}
.$$
:::

::: {.front card-id="card-e8b153b9155d75ae" tags="formula"}
$\tan(\pi/6) = \cdots$
:::

::: {.back card-id="card-e8b153b9155d75ae"}
$$
\tan(\pi/6) = {\sqrt 3 \over 3}
.$$
:::

::: {.front card-id="card-e802bf57d687eeb5" tags="formula"}
$\tan(\pi/4) = \cdots$
:::

::: {.back card-id="card-e802bf57d687eeb5"}
$$
\tan(\pi/4) = 1
.$$
:::

::: {.front card-id="card-aa385abeb29c6790" tags="formula"}
$\tan(\pi/3) = \cdots$
:::

::: {.back card-id="card-aa385abeb29c6790"}
$$
\tan(\pi/3) = \sqrt 3
.$$
:::

::: {.front card-id="card-aa6cd6dd8b9f932a" tags="formula"}
$e^{2\pi i \over 3} = \cdots$ in rectangular coordinates
:::

::: {.back card-id="card-aa6cd6dd8b9f932a"}
$$
e^{2\pi i \over 3} = {1\over 2}\qty{-1 + i\sqrt 3}
.$$
:::

::: {.front card-id="card-060314ba1f6e3402" tags="formula"}
$e^{2\pi i \over 6} = \cdots$ in rectangular coordinates
:::

::: {.back card-id="card-060314ba1f6e3402"}
$$
e^{2\pi i \over 6} = {1\over 2}\qty{1 + i\sqrt 3}
.$$
:::

::: {.front card-id="card-9c83862120c41169" tags="fact"}
Descartes' Rule of Signs
:::

::: {.back card-id="card-9c83862120c41169"}
Let $p(x)$ be a real polynomial and let $n$ be the number of sign changes in its sequence of nonzero coefficients.
The number $r^+$ of positive real roots (counted with multiplicity) of $p(x)$ is at most $n$.
Moreover, $r^+$ is *exactly* $n-2k$ for some $k\in \ZZ^{\geq 0}$; in particular $r^+ \equiv n \mod 2$.
Similarly, the number $r^-$ of negative real roots is the same idea applied to $p(-x)$.
If $p(0) \neq 0$ and $n^+, n^-$ are the numbers of sign changes of $p(x)$ and $p(-x)$, then at least $\deg p - (n^+ + n^-)$ roots of $p$ are nonreal.

*Examples:*

- $f(x) = x^3 + x^2 - x - 1$ has exactly 1 positive real root.
- $f(-x) = -x^3 + x^2 + x - 1$ has either 2 or 0 positive real roots, so $f$ has 2 or 0 negative real roots.
- $g(x) = x^3 - 1$ has exactly 1 positive real root, $g(-x) = -x^3 - 1$ has 0 positive roots, so $g$ has 2 nonreal roots.
- $x^3 + x^2 - x - 2$ has exactly 1 positive real root.
- $x^5+4 x^4-3 x^2+x-6$ has 3 sign changes, so it has 3 or 1 positive real roots.
:::

::: {.front card-id="card-0bc178fa054568ae" tags="formula"}
Factor $x^n - y^n$.
:::

::: {.back card-id="card-0bc178fa054568ae"}
$$x^n-y^n=(x-y)\left(x^{n-1}+x^{n-2} y+\cdots+x y^{n-2}+y^{n-1}\right) = (x-y)\sum_{k=0}^{n-1}x^{n-1-k}y^k.$$
How to prove: long division gives $x^n-y^n = x^{n-1}(x-y) + y\qty{x^{n-1}-y^{n-1}}$, so ${x^n-y^n\over x-y} = x^{n-1} + y\qty{x^{n-1}-y^{n-1}\over x-y}$; induct on $n$.
How to remember: $t^n-1 = (t-1)(t^{n-1} + t^{n-2} + \cdots + t + 1)$; set $t=x/y$ and multiply by $y^n$.
:::

::: {.front card-id="card-39cd778ed0f32a27" tags="formula"}
Factor $x^n + y^n$ for $n$ odd.
:::

::: {.back card-id="card-39cd778ed0f32a27"}
For $n$ odd, replace $y$ by $-y$ in the factorization of $x^n - y^n$:
$$x^n+y^n=(x+y)\left(x^{n-1}-x^{n-2} y+\cdots-x y^{n-2}+y^{n-1}\right) = (x+y)\sum_{k=0}^{n-1}(-y)^k x^{n-1-k}.$$
For $n$ even, $x+y$ does not divide $x^n+y^n$, since $(-y)^n + y^n = 2y^n$.
:::

::: {.front card-id="card-fc7980ff12c7ffbf" tags="formula"}
$\arctan(0) = \cdots$
:::

::: {.back card-id="card-fc7980ff12c7ffbf"}
$\arctan(0) = 0$
:::

::: {.front card-id="card-2d305cad87c6c59b" tags="formula"}
$\arctan\qty{1\over \sqrt 3} = \cdots$
:::

::: {.back card-id="card-2d305cad87c6c59b"}
$\arctan\qty{1\over \sqrt 3} = \arctan\qty{\sqrt{3} \over 3} = {\pi\over 6}$
:::

::: {.front card-id="card-87ca1c324a0e7fe6" tags="formula"}
$\arctan(1) = \cdots$
:::

::: {.back card-id="card-87ca1c324a0e7fe6"}
$\arctan(1) = {\pi\over 4}$
:::

::: {.front card-id="card-b9ab8ffc020f07fe" tags="formula"}
$\arctan(\sqrt 3) = \cdots$
:::

::: {.back card-id="card-b9ab8ffc020f07fe"}
$\arctan(\sqrt 3) = {\pi \over 3}$
:::

::: {.front card-id="card-1c1427a24bc7dc54" tags="formula"}
$\arctan(\infty) = \cdots$
:::

::: {.back card-id="card-1c1427a24bc7dc54"}
$\arctan(\infty) = \lim_{x\to+\infty}\arctan x = {\pi \over 2}$
:::

::: {.front card-id="card-c6801344324a2f26" tags="formula"}
$\arctan$ values:
:::

::: {.back card-id="card-c6801344324a2f26"}
$\arctan 0=0$, $\arctan(1/\sqrt3)=\pi/6$, $\arctan 1=\pi/4$, $\arctan\sqrt3=\pi/3$, and $\lim_{x\to+\infty}\arctan x=\pi/2$.
:::

::: {.front card-id="card-efc49202ba80c5d4" tags="unsorted"}
True or false: $\log(a-b) = \log(a) / \log(b)$
:::

::: {.back card-id="card-efc49202ba80c5d4"}
False: take $b=1$, this would force dividing by zero.
:::

::: {.front card-id="card-c34ff24d2266b166" tags="unsorted"}
True or false: $\log(a+b) = \log(a) + \log(b)$
:::

::: {.back card-id="card-c34ff24d2266b166"}
False
:::

::: {.front card-id="card-3a469b2ce4fc9251" tags="unsorted"}
True or false: $\log(a+b) = \log(a) \log(b)$
:::

::: {.back card-id="card-3a469b2ce4fc9251"}
False: $\log_2(4+4) = \log_2(8) = 3 \neq 4 = 2 \cdot 2 = \log_2(4) \cdot \log_2(4)$.
:::

::: {.front card-id="card-0fd9e0a82ce28c1b" tags="unsorted"}
Write $\log$ and $\exp$ as group homomorphisms. What are the domains and codomains?
:::

::: {.back card-id="card-0fd9e0a82ce28c1b"}
$$
\log: (\RR_{>0}, \cdot) \to (\RR, +), \qquad \exp: (\RR, +) \to (\RR_{>0}, \cdot)
.$$
These are inverse isomorphisms.
Here $(\RR, +) = \GG_a(\RR)$ and $\RR_{>0}$ is the identity component of $\GG_m(\RR) = \RR^\times$, so $\exp: \GG_a(\RR) \to \GG_m(\RR)$ is injective with image $\RR_{>0}$.
Over $\CC$, $\exp: \GG_a(\CC) \to \GG_m(\CC)$ is surjective with kernel $2\pi i \ZZ$, so $\log$ is defined only modulo $2\pi i\ZZ$.
:::

::: {.front card-id="card-7735b0a37c146f61"}
$\sin(a+b) = \cdots$
:::

::: {.back card-id="card-7735b0a37c146f61"}
$\sin(a)\cos(b) + \cos(a)\sin(b)$.
:::

::: {.front card-id="card-9b1c923db6310b6f"}
$\cos(a+b) = \cdots$
:::

::: {.back card-id="card-9b1c923db6310b6f"}
$\cos(a)\cos(b) - \sin(a)\sin(b)$.
:::

::: {.front card-id="card-17a29c822d6de20a"}
$\tan(a+b) = \cdots$
:::

::: {.back card-id="card-17a29c822d6de20a"}
${\tan(a)+\tan(b) \over 1-\tan(a)\tan(b)}$.
:::

::: {.front card-id="card-ea216c0db40e8656" tags="formula"}
Double angle formulas converting $f(2t)$ into $\tan$ for $f=\sin,\cos$.
:::

::: {.back card-id="card-ea216c0db40e8656"}
$$\begin{align}\sin(2t) &= {2\tan(t) \over 1+\tan^2(t)} \\ \cos(2t) &= {1-\tan^2(t) \over 1+\tan^2(t)}\end{align}.$$
:::

::: {.front card-id="card-6cd5f936b8576c92"}
$\sin ^2 \theta=\cdots$
:::

::: {.back card-id="card-6cd5f936b8576c92"}
$\sin ^2 \theta=\frac{1-\cos (2 \theta)}{2}$
:::

::: {.front card-id="card-1e5a093e1b6d71d9"}
$\cos ^2 \theta=\cdots$
:::

::: {.back card-id="card-1e5a093e1b6d71d9"}
$\cos ^2 \theta=\frac{1+\cos (2 \theta)}{2}$
:::
