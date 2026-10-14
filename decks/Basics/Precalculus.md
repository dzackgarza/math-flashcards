---
title: "Basics::Precalculus"
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
The number $r^+$ of positive real roots (counted with multiplicity) of a polynomial $p(x)$ are at most the number $n$ of sign changes in the coefficients.
Moreover, $r^+$ is *exactly* $n-2k$ for some $k\in \ZZ^{\geq 0}$.
Similarly, the number $r^-$ of negative real roots is the same idea applied to $p(-x)$.
The minimal number of nonreal roots is thus $n - (r^+ + r^-)$.

*Examples:*

- $f(x) = x^3 + x^2 - x - 1$ has exactly 1 positive real root.
- $f(-x) = -x^3 + x^2 + x - 1$ has either 2 or 0 positive real roots, so $f$ has 2 or 0 negative real roots.
- $g(x) = x^3 - 1$ has exactly 1 positive real root, $g(-x) = -x^3 - 1$ has 0 positive roots, so $g$ has 2 complex roots.
:::

::: {.front card-id="card-0bc178fa054568ae" tags="formula"}
Factor $x^n - a^n$
:::

::: {.back card-id="card-0bc178fa054568ae"}
$$
(x-a)\sum_{k=0}^{n-1} a^k x^{n-k}
$$
:::

::: {.front card-id="card-39cd778ed0f32a27" tags="formula"}
Factor $x^n + a^n$
:::

::: {.back card-id="card-39cd778ed0f32a27"}
$$
(x+a) \sum _{k=0}^{n-1} (-a)^k x^{n-k}
$$
:::

::: {.front card-id="card-b294a9fbcf87653a" tags="formula"}
Factor $x^n - y^n$
:::

::: {.back card-id="card-b294a9fbcf87653a"}
$$
(x-y)(x^{n-1} + x^{n-2} y + \cdots + y^{n-1})
$$
:::

::: {.front card-id="card-5f42b26733c7f9e1" tags="formula"}
Factor $x^n + y^n$
:::

::: {.back card-id="card-5f42b26733c7f9e1"}
$$
(x+y)(x^{n-1} + x^{n-2}(-y) + \cdots + (-y)^{n+1})
$$
:::

::: {.front card-id="card-61d6eb294244344e" tags="fact"}
Descartes' Rule of Signs
:::

::: {.back card-id="card-61d6eb294244344e"}
The number $r^+$ of positive real roots of a polynomial $p(x)$ are at most the number $n$ of sign changes in the coefficients.
Moreover, $r$ is *exactly* $n-2k$ for some $k\in \ZZ^{\geq 0}$.
Similarly, the number $r^-$ of negative real roots is the same idea applied to $p(-x)$.

Examples: $x^3 + x^2 - x - 2$ has at most one real root.
:::

::: {.front card-id="card-7d6d264132ec25e5" tags="formula"}
Factor $x^n + a^n$
:::

::: {.back card-id="card-7d6d264132ec25e5"}
$$
(x+a)\sum_{k=0}^{n-1} (-a)_^k x^{n-k}
$$
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
$\arctan\qty{1\over \sqrt 3} = {\pi\over 6}$
:::

::: {.front card-id="card-04057a39257444a7" tags="formula"}
$\arctan\qty{\sqrt{3} \over 3} = \cdots$
:::

::: {.back card-id="card-04057a39257444a7"}
$\arctan\qty{\sqrt{3} \over 3} = {\pi\over 6}$
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
$\arctan(\infty) = {\pi \over 2}$
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
False
:::

::: {.front card-id="card-0fd9e0a82ce28c1b" tags="unsorted"}
Write $\log$ as a group homomorphism. What are the domain and codomain?
:::

::: {.back card-id="card-0fd9e0a82ce28c1b"}
$$
\log: \GG_m(\RR) \to \GG_a(\RR)
.$$
:::

::: {.front card-id="card-ff56ab1fbdbb17c2" tags="unsorted"}
Write $\exp$  as a group homomorphism.
:::

::: {.back card-id="card-ff56ab1fbdbb17c2"}
$$
\exp: \GG_a(\RR) \to \GG_m(\RR)
.$$
:::

::: {.front card-id="card-7068a7cff51dec1f"}
What is Descartes' rule of signs?
:::

::: {.back card-id="card-7068a7cff51dec1f"}
The number of positive real roots of $f$ is equivalent $\operatorname{mod}2$ to the number of sign changes in the coefficients of $f(x)$. The number of *negative* real roots is the same process but for $f(-x)$. E.g. $f(x)=x^5+4 x^4-3 x^2+x-6$ has 3 changes of sign, so an odd number of real roots.
:::

::: {.front card-id="card-16810d0968425f2a"}
Factor $x^n-y^n$.
:::

::: {.back card-id="card-16810d0968425f2a"}
$$x^n-y^n=(x-y)\left(x^{n-1}+x^{n-2} y+\ldots+x y^{n-2}+y^{n-1}\right) = (x-y)\sum_{k=0}^{n-1}x^{n-k-1}y^k$$
How to prove: long division to obtain ${x^n-y^n\over x-y} = x^n + y\qty{x^{n-1}-y^{n-1}\over x-y}$ and induct. How to remember: $x^n-1 = (x-1)(x^{n-1} + x^{n-2} + \cdot + x + 1)$ and set $x=b/a$.
:::

::: {.front card-id="card-8b0dd744cd1a2ea2"}
Factor $x^n + y^n$ for $n$ an odd prime.
:::

::: {.back card-id="card-8b0dd744cd1a2ea2"}
$$x^n+y^n=(x+y)\left(x^{n-1}-x^{n-2} y+\cdots-x y^{n-2}+y^{n-1}\right)$$
:::

::: {.front card-id="card-88d4f809c71073af"}
Write $\log$ and $\exp$ as group homomorphisms; i.e. what are the domains and codomains?
:::

::: {.back card-id="card-88d4f809c71073af"}
$${\mathbf{G}}_m \underset{\exp}{\overset{\log}{\rightleftharpoons}} {\mathbf{G}}_a$$
:::

::: {.front card-id="card-a3277cea83efd7d1"}
True or false: $\log(a+b) = \log(a)\cdot \log(b)$.
:::

::: {.back card-id="card-a3277cea83efd7d1"}
False: $\log_2(4+4) = \log_2(8) = 3 \neq 4 = 2 \cdot 2 = \log_2(4) \cdot \log_2(4)$.
:::

::: {.front card-id="card-842c1d995d6f9c86"}
$\sin(\pi/6)$
:::

::: {.back card-id="card-842c1d995d6f9c86"}
$1/2$
:::

::: {.front card-id="card-b917cdce2f310989"}
$\cos(\pi/6)$
:::

::: {.back card-id="card-b917cdce2f310989"}
$\sqrt 3 /2$.
:::

::: {.front card-id="card-e4e1ce20bb7532be"}
$\sin(\pi/3)$
:::

::: {.back card-id="card-e4e1ce20bb7532be"}
$\sqrt 3/2$
:::

::: {.front card-id="card-ffa0d62869bcbe86"}
$\cos(\pi/3)$
:::

::: {.back card-id="card-ffa0d62869bcbe86"}
$1/2$.
:::

::: {.front card-id="card-e4bf5a5d2b3c3632"}
$\arctan(0)$
:::

::: {.back card-id="card-e4bf5a5d2b3c3632"}
$0$
:::

::: {.front card-id="card-738a7317b424e2bd"}
$\arctan(1)$
:::

::: {.back card-id="card-738a7317b424e2bd"}
$\pi/4$.
:::

::: {.front card-id="card-88161d095761b37c"}
$\arctan(\infty)$
:::

::: {.back card-id="card-88161d095761b37c"}
$\pi/2$
:::

::: {.front card-id="card-1ac22c248a09ac1b"}
$\arctan\qty{\sqrt 3\over 3}$
:::

::: {.back card-id="card-1ac22c248a09ac1b"}
$\pi/6$
:::

::: {.front card-id="card-8469cca47b6c6be7"}
$\arctan\qty{\sqrt 3}$
:::

::: {.back card-id="card-8469cca47b6c6be7"}
$\pi/3$
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
${\tan(a)\tan(b) \over 1-\tan(a)\tan(b)}$.
:::

::: {.front card-id="card-ea216c0db40e8656"}
Double angle formulas converting $f(2t)$ into $\tan$ for $f=\sin,\cos$.
:::

::: {.back card-id="card-ea216c0db40e8656"}
$$\begin{align}\sin(2t) &= {2\tan(t) \over 1+\tan^2(t)} \\ \cos(2t) &= {1-\tan^2(2t) \over 1+\tan^2(t)}\end{align}.$$
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

::: {.front card-id="card-df28c7619c664624" tags="formula"}
Double angle formulas involving $\tan$
:::

::: {.back card-id="card-df28c7619c664624"}
The double angle formulas:
$$
\sin(2t) = {2\tan(t) \over 1+\tan^2(t)} \\
\cos(2t) = {1-\tan^2(2t) \over 1+\tan^2(t)}
.$$
:::
