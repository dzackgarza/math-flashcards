Descartes' Rule of Signs
%
The number $r^+$ of positive real roots (counted with multiplicity) of a polynomial $p(x)$ are at most the number $n$ of sign changes in the coefficients.
Moreover, $r^+$ is *exactly* $n-2k$ for some $k\in \ZZ^{\geq 0}$.
Similarly, the number $r^-$ of negative real roots is the same idea applied to $p(-x)$.
The minimal number of nonreal roots is thus $n - (r^+ + r^-)$.

*Examples:*

- $f(x) = x^3 + x^2 - x - 1$ has exactly 1 positive real root.
- $f(-x) = -x^3 + x^2 + x - 1$ has either 2 or 0 positive real roots, so $f$ has 2 or 0 negative real roots.
- $g(x) = x^3 - 1$ has exactly 1 positive real root, $g(-x) = -x^3 - 1$ has 0 positive roots, so $g$ has 2 complex roots.
%
fact
---

Factor $x^n - a^n$
%
\[
(x-a)\sum_{k=0}^{n-1} a^k x^{n-k}
\]
%
formula
---

Factor $x^n + a^n$
%
\[
(x+a) \sum _{k=0}^{n-1} (-a)^k x^{n-k}
\]
%
formula
---

Functional characterization of injective functions.
%
\[  
f(x) = f(y) \implies x=y \iff f \text{ has a left inverse.}
.\]
%
definition
---

Functional characterization of surjective functions.
%
\[  
\forall y, \exists X \text{ such that } f(x) = y \iff f\text{ has a right inverse, } \exists g \text{ such that } f(g(y)) = y\, \forall y
.\]
%
definition
---

Factor $x^n - y^n$
%
\[
(x-y)(x^{n-1} + x^{n-2} y + \cdots + y^{n-1})
\]
%
formula
---

Factor $x^n + y^n$
%
\[
(x+y)(x^{n-1} + x^{n-2}(-y) + \cdots + (-y)^{n+1})
\]
%
formula
