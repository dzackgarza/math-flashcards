---
title: "Number Theory::Analytic Number Theory"
---

::: {.front card-id="analytic-nt-dirichlet-convolution" cite="[@Apo98, §2.1; @Apo98, §2.6, Thms. 2.6–2.7; @Apo98, §2.9, Def. and Thm. 2.12; @Apo98, §2.10, Thm. 2.14]"}
Define arithmetic functions and Dirichlet convolution. What is the identity for convolution, and how does multiplicativity behave under it?
:::

::: {.back card-id="analytic-nt-dirichlet-convolution"}
An arithmetic function is $f:\mathbb Z_{>0}\to\mathbb C$. For arithmetic functions $f,g$,
$$(f*g)(n)=\sum_{d\mid n}f(d)g(n/d)=\sum_{ab=n}f(a)g(b).$$
Convolution is commutative and associative. Its identity is
$$I(n)=\begin{cases}1&n=1,\\0&n>1,\end{cases}\qquad I*f=f*I=f.$$
$f$ is **multiplicative** if $f\not\equiv0$ and $f(mn)=f(m)f(n)$ whenever $\gcd(m,n)=1$; then $f(1)=1$. It is **completely multiplicative** if the same equation holds for all $m,n\ge1$.

If $f,g$ are multiplicative, so is $f*g$: for $\gcd(m,n)=1$, split each divisor of $mn$ uniquely as $ab$ with $a\mid m$ and $b\mid n$, then factor the resulting double sum. Complete multiplicativity need not persist: if $u(n)=1$ and $d=u*u$ is the divisor-counting function, then $d(4)=3\ne4=d(2)^2$.
:::

::: {.front card-id="analytic-nt-mobius-inversion" cite="[@Apo98, §2.2, Def. and Thm. 2.1; @Apo98, §2.7, Thm. 2.9; @Apo98, §§2.3–2.4, Thms. 2.2–2.3]"}
Define the Möbius function $\mu$, state its fundamental divisor sum and Möbius inversion, and illustrate inversion with Euler's totient $\varphi$.
:::

::: {.back card-id="analytic-nt-mobius-inversion"}
$\mu(1)=1$. If $n=p_1^{a_1}\cdots p_r^{a_r}$ with distinct primes $p_i$,
$$\mu(n)=\begin{cases}(-1)^r&a_1=\cdots=a_r=1,\\0&\text{otherwise}.\end{cases}$$
For $u(n)=1$ and the convolution identity $I$,
$$\sum_{d\mid n}\mu(d)=I(n)=\begin{cases}1&n=1,\\0&n>1,\end{cases}\qquad\mu*u=I.$$
Thus $\mu$ and $u$ are Dirichlet inverses, and for arithmetic functions $f,g$,
$$f=g*u\iff g=f*\mu,$$
or explicitly,
$$f(n)=\sum_{d\mid n}g(d)\iff g(n)=\sum_{d\mid n}\mu(d)f(n/d).$$
Example: $N(n)=n$ satisfies $N=u*\varphi$, so $\varphi=\mu*N$ and
$$n=\sum_{d\mid n}\varphi(d),\qquad \varphi(n)=\sum_{d\mid n}\mu(d)\frac nd.$$
At $n=6$: $6=1+1+2+2=\varphi(1)+\varphi(2)+\varphi(3)+\varphi(6)$, while $\varphi(6)=6(1-\tfrac12-\tfrac13+\tfrac16)=2$.
:::

::: {.front card-id="analytic-nt-von-mangoldt" cite="[@Apo98, §2.8, Def. and Thms. 2.10–2.11]"}
Define the von Mangoldt function $\Lambda$. Recover its divisor-sum identity with $\log n$ and the inverse formula, then compute $\Lambda(4)$ by inversion.
:::

::: {.back card-id="analytic-nt-von-mangoldt"}
$$\Lambda(n)=\begin{cases}\log p&n=p^m\text{ for a prime }p\text{ and }m\ge1,\\0&\text{otherwise}.\end{cases}$$
For $n=\prod_{p^a\parallel n}p^a$, only prime-power divisors contribute, giving
$$\log n=\sum_{d\mid n}\Lambda(d)=\sum_{p^a\parallel n}a\log p.$$
Equivalently, $\log=u*\Lambda$. Möbius inversion gives
$$\Lambda(n)=\sum_{d\mid n}\mu(d)\log\frac nd=-\sum_{d\mid n}\mu(d)\log d,$$
because $\log n\sum_{d\mid n}\mu(d)=I(n)\log n=0$.
For $n=4$, $\mu(1)=1$, $\mu(2)=-1$, $\mu(4)=0$, so $\Lambda(4)=-\mu(2)\log2=\log2$.
:::

::: {.front card-id="analytic-nt-chebyshev-definitions" cite="[@Apo98, §4.1; @Apo98, §4.2, Defs. and Eq. (3)]"}
Define $\pi(x)$, Chebyshev's $\vartheta(x)$, and $\psi(x)$ for $x>0$, including every summation range and the treatment of higher prime powers.
:::

::: {.back card-id="analytic-nt-chebyshev-definitions"}
Throughout, $p$ is prime and $m\in\mathbb Z_{>0}$:
$$\pi(x)=\sum_{p\le x}1,\qquad \vartheta(x)=\sum_{p\le x}\log p,$$
$$\psi(x)=\sum_{n\le x}\Lambda(n)=\sum_{\substack{p,m\\p^m\le x}}\log p=\sum_{m\le\log_2x}\vartheta(x^{1/m}).$$
Thus $\vartheta$ counts each prime $p\le x$ once with weight $\log p$, while $\psi$ counts every prime power $p^m\le x$ once with the same weight $\log p$. The $m$-sum is finite: $p^m\le x$ implies $m\le\log_2x$.
:::

::: {.front card-id="analytic-nt-dirichlet-series" cite="[@Apo98, §11.2, Example 1; @Apo98, §11.4, Thm. 11.5 and Example 1; @Apo98, §11.7, Thm. 11.12 and Eqs. (12)–(13)]"}
For $\sigma=\operatorname{Re}s>1$, identify the Dirichlet series with coefficients $1$, $\mu(n)$, $\log n$, and $\Lambda(n)$. How do the last coefficients encode $\psi(x)$?
:::

::: {.back card-id="analytic-nt-dirichlet-series"}
All four series converge absolutely for $\sigma>1$:
$$\sum_{n=1}^{\infty}\frac1{n^s}=\zeta(s),\qquad \sum_{n=1}^{\infty}\frac{\mu(n)}{n^s}=\frac1{\zeta(s)},$$
$$\sum_{n=1}^{\infty}\frac{\log n}{n^s}=-\zeta'(s),\qquad \sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s}=-\frac{\zeta'(s)}{\zeta(s)}.$$
Termwise differentiation of $\zeta(s)$ gives the logarithm series. Multiplication of absolutely convergent Dirichlet series corresponds to convolution, so $\log=u*\Lambda$ gives
$$-\zeta'(s)=\zeta(s)\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s},$$
which yields the logarithmic-derivative formula. Its coefficient partial sums are precisely
$$\psi(x)=\sum_{n\le x}\Lambda(n).$$
:::

::: {.front card-id="analytic-nt-partial-summation" cite="[@Apo98, §4.3, Thm. 4.2 and Note, Eq. (5)]"}
State Abel's partial-summation identity for $\sum_{y<n\le x}a(n)f(n)$, including the continuous-derivative hypothesis. What form does it take when $y<1$?
:::

::: {.back card-id="analytic-nt-partial-summation"}
Let $0<y<x$, $A(x)=\sum_{n\le x}a(n)$ with $A(x)=0$ for $x<1$, and suppose $f$ has a continuous derivative on $[y,x]$. Then
$$\sum_{y<n\le x}a(n)f(n)=A(x)f(x)-A(y)f(y)-\int_y^xA(t)f'(t)\,dt.$$
If $0<y<1<x$, then $A(y)=0$, and the identity becomes
$$\sum_{n\le x}a(n)f(n)=A(x)f(x)-\int_1^xA(t)f'(t)\,dt.$$
:::

::: {.front card-id="analytic-nt-chebyshev-relations" cite="[@Apo98, §4.2, Thm. 4.1; @Apo98, §4.3, Thm. 4.3]"}
Relate $\psi$ to $\vartheta$ and both functions to $\pi$. Include the error estimate used to interchange the $\vartheta$ and $\psi$ forms of the prime number theorem.
:::

::: {.back card-id="analytic-nt-chebyshev-relations"}
For $x>0$,
$$0\le\psi(x)-\vartheta(x)=\sum_{2\le m\le\log_2x}\vartheta(x^{1/m})\le\frac{\sqrt x\,(\log x)^2}{2\log2}.$$
In particular, $\vartheta(x)\le\psi(x)$ and
$$\frac{\psi(x)}x-\frac{\vartheta(x)}x=O\!\left(\frac{(\log x)^2}{\sqrt x}\right)=o(1).$$
For $x\ge2$, partial summation gives
$$\vartheta(x)=\pi(x)\log x-\int_2^x\frac{\pi(t)}t\,dt,$$
$$\pi(x)=\frac{\vartheta(x)}{\log x}+\int_2^x\frac{\vartheta(t)}{t(\log t)^2}\,dt.$$
For the first formula, weight the prime indicator by $\log n$; for the second, apply $1/\log n$ to coefficients equal to $\log n$ at primes and zero elsewhere.
:::

::: {.front card-id="analytic-nt-pnt-equivalences" cite="[@Apo98, §4.4, Thm. 4.4]"}
State the prime number theorem in its $\pi$, $\vartheta$, and $\psi$ forms. Derive their equivalence from the connecting integral identities and error estimates.
:::

::: {.back card-id="analytic-nt-pnt-equivalences"}
The prime number theorem is any one, hence all, of the equivalent assertions
$$\pi(x)\sim\frac{x}{\log x}\iff\vartheta(x)\sim x\iff\psi(x)\sim x\qquad(x\to\infty).$$
Put $R(x)=\pi(x)\log x/x$. The identities relating $\pi$ and $\vartheta$ become
$$\frac{\vartheta(x)}x=R(x)-\frac1x\int_2^x\frac{\pi(t)}t\,dt,$$
$$R(x)=\frac{\vartheta(x)}x+\frac{\log x}x\int_2^x\frac{\vartheta(t)}{t(\log t)^2}\,dt.$$
If $R(x)\to1$, then $\pi(t)=O(t/\log t)$, so the first integral term is $O\!\left(x^{-1}\int_2^xdt/\log t\right)$. If $\vartheta(x)\sim x$, then $\vartheta(t)=O(t)$, so the second is $O\!\left((\log x)x^{-1}\int_2^xdt/(\log t)^2\right)$.

Both terms tend to $0$: split each integral at $\sqrt x$ and use, for $j=1,2$ and large $x$,
$$\int_2^x\frac{dt}{(\log t)^j}\le\frac{\sqrt x}{(\log2)^j}+\frac{x}{(\log\sqrt x)^j}.$$
Multiplication by $1/x$ or $\log x/x$, respectively, gives $o(1)$. Thus $R(x)\to1\iff\vartheta(x)/x\to1$. Finally,
$$\frac{\psi(x)}x-\frac{\vartheta(x)}x=O\!\left(\frac{(\log x)^2}{\sqrt x}\right)=o(1),$$
so the $\vartheta$ and $\psi$ limits are also equivalent.
:::

::: {.front card-id="analytic-nt-zeta-nonvanishing-line-one" cite="[@Apo98, §13.5, Thm. 13.6; @Apo98, §13.1]"}
State precisely the nonvanishing input on $\operatorname{Re}s=1$ used in the analytic proof of the prime number theorem. What happens at $t=0$, and what is the input's role?
:::

::: {.back card-id="analytic-nt-zeta-nonvanishing-line-one"}
**Theorem.** For every real $t\ne0$,
$$\zeta(1+it)\ne0.$$
At $t=0$, $\zeta(s)$ has a simple pole at $s=1$, so this point is excluded. The analytic proof of the prime number theorem uses this nonvanishing to control $-\zeta'(s)/\zeta(s)$ on $\operatorname{Re}s=1$ away from $s=1$ and pass its contour-integral argument to that line; the conclusion obtained is $\psi(x)\sim x$.

This statement asserts nonvanishing on the line itself, not a zero-free region of positive width to its left.
:::
