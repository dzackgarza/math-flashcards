Rouche
%
If $f$ and $g$ are holomorphic on $\abs{z-z_0} \leq R$ with $f,g\neq 0$ on $\abs{z-z_0} = R$ and
\[
\abs{f-g} < \abs{f} + \abs{g}
,\]
then $f$ and $g$ have the same number of zeros in this region.
%
theorem
---

Cauchy Inequalities
%
\[
\abs{f^{(n)} (z_0) \over n!} \leq R^{-n} \sup_{\abs{z}=R} \abs{f(z)}
.\]
%
formula, theorem
---

Cauchy Integral Formula for $f(z)$
%
For $f$ holomorphic in $U\supseteq \bar D$, then for any $z\in D$,
\[
f(z) = {1 \over 2\pi i} \int _{\bd D} {f(\xi) \over \xi - z} \,d\xi
.\]
%
formula, theorem
---

Cauchy Integral Formula for $f^{(n)}(z)$
%
For $f$ holomorphic in $U\supseteq \bar D$ and $C$ is a circle such that $C^\circ \subset U$ then for any $z\in C^\circ$,
\[
f^{(n)}(z)=\frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta
.\]
%
formula, theorem
---

Maximum Length Lemma
%
\[
\abs{\int _\gamma f} \leq \sup_{z\in \gamma} \abs{f(z)} \cdot \ell(\gamma)
.\]
%

---

Double angle formulas involving $\tan$
%
The double angle formulas:
\[
\sin(2t) = {2\tan(t) \over 1+\tan^2(t)} \\ 
\cos(2t) = {1-\tan^2(2t) \over 1+\tan^2(t)}
.\]
%
formula
---

Standard parameterization of a circle in $\CC$
%
\[
F(t) = {1-x^2\over 1+x^2} + i{2x\over 1+x^2} \quad x = \tan(t), t\in (-\pi/2, \pi/2)
.\]
%
formula
---

Cross-ratio map
%
\[
R(z) \da (z, z_2, z_3, z_4) \da {z - z_3\over z-z_4}{z_2 - z_4 \over z_2 - z_3} \\
.\]

Sends 

- $z_2 \to 1$
- $z_3\to 0$
- $z_4\to \infty$
%
formula
---

The generalized residue formula
%
\[
\Res_{z=z_0} f = \lim_{z\to z_0} {1 \over (n-1)!} \qty{\dd{}{z}}^{n-1} (z-z_0)^n f(z)
.\]
%
formula
---

Inverting series: ${1\over \sin(z) } = \cdots$
%
\[
{1\over \sin(z)} = \frac{1}{z}+\frac{1}{3 !} z+\frac{7}{360} z^{3}+\mathrm{O}\left(z^{5}\right)
.\]
%
formula
---

Inverting series: for $A(z) = \sum c_k z^k$ and $1/A(z) = \sum b_k z^k$, the formula for the $b_k$ in terms of $c_k$.
%
- $b_0 = c_0\inv$
- $b_1 = -c_0\inv(c_1 b_0 )$
- $b_2 = -c_0\inv(c_2b_0 + c_1b_1)$
- $\cdots$
%
formula
