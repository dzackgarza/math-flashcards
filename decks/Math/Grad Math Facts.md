---
title: "Math::Grad Math Facts"
---

::: {.front card-id="card-7068a7cff51dec1f"}
What is Descartes' rule of signs?
:::

::: {.back card-id="card-7068a7cff51dec1f"}
The number of positive real roots of $ f $ is equivalent $ \operatorname{mod}2 $ to the number of sign changes in the coefficients of $ f(x) $. The number of *negative* real roots is the same process but for $ f(-x) $. E.g. $ f(x)=x^5+4 x^4-3 x^2+x-6 $ has 3 changes of sign, so an odd number of real roots.
:::

::: {.front card-id="card-16810d0968425f2a"}
Factor $ x^n-y^n $.
:::

::: {.back card-id="card-16810d0968425f2a"}
$$x^n-y^n=(x-y)\left(x^{n-1}+x^{n-2} y+\ldots+x y^{n-2}+y^{n-1}\right) = (x-y)\sum_{k=0}^{n-1}x^{n-k-1}y^k$$

How to prove: long division to obtain $ {x^n-y^n\over x-y} = x^n + y\qty{x^{n-1}-y^{n-1}\over x-y} $ and induct. How to remember: $ x^n-1 = (x-1)(x^{n-1} + x^{n-2} + \cdot + x + 1) $ and set $ x=b/a $.
:::

::: {.front card-id="card-8b0dd744cd1a2ea2"}
Factor $ x^n + y^n $ for $ n $ an odd prime.
:::

::: {.back card-id="card-8b0dd744cd1a2ea2"}
$$x^n+y^n=(x+y)\left(x^{n-1}-x^{n-2} y+\cdots-x y^{n-2}+y^{n-1}\right)$$
:::

::: {.front card-id="card-88d4f809c71073af"}
Write $ \log $ and $ \exp $ as group homomorphisms; i.e. what are the domains and codomains?
:::

::: {.back card-id="card-88d4f809c71073af"}
$${\mathbf{G}}_m \underset{\exp}{\overset{\log}{\rightleftharpoons}} {\mathbf{G}}_a$$
:::

::: {.front card-id="card-a3277cea83efd7d1"}
True or false: $ \log(a+b) = \log(a)\cdot \log(b) $.
:::

::: {.back card-id="card-a3277cea83efd7d1"}
False: $ \log_2(4+4) = \log_2(8) = 3 \neq 4 = 2 \cdot 2 = \log_2(4) \cdot \log_2(4) $.
:::

::: {.front card-id="card-842c1d995d6f9c86"}
$ \sin(\pi/6) $
:::

::: {.back card-id="card-842c1d995d6f9c86"}
$ 1/2 $
:::

::: {.front card-id="card-b917cdce2f310989"}
$ \cos(\pi/6) $
:::

::: {.back card-id="card-b917cdce2f310989"}
$ \sqrt 3 /2 $.
:::

::: {.front card-id="card-e4e1ce20bb7532be"}
$ \sin(\pi/3) $
:::

::: {.back card-id="card-e4e1ce20bb7532be"}
$ \sqrt 3/2 $
:::

::: {.front card-id="card-ffa0d62869bcbe86"}
$ \cos(\pi/3) $
:::

::: {.back card-id="card-ffa0d62869bcbe86"}
$ 1/2 $.
:::

::: {.front card-id="card-e4bf5a5d2b3c3632"}
$ \arctan(0) $
:::

::: {.back card-id="card-e4bf5a5d2b3c3632"}
$ 0 $
:::

::: {.front card-id="card-738a7317b424e2bd"}
$ \arctan(1) $
:::

::: {.back card-id="card-738a7317b424e2bd"}
$ \pi/4 $.
:::

::: {.front card-id="card-88161d095761b37c"}
$ \arctan(\infty) $
:::

::: {.back card-id="card-88161d095761b37c"}
$ \pi/2 $
:::

::: {.front card-id="card-1ac22c248a09ac1b"}
$ \arctan\qty{\sqrt 3\over 3} $
:::

::: {.back card-id="card-1ac22c248a09ac1b"}
$ \pi/6 $
:::

::: {.front card-id="card-8469cca47b6c6be7"}
$ \arctan\qty{\sqrt 3} $
:::

::: {.back card-id="card-8469cca47b6c6be7"}
$ \pi/3 $
:::

::: {.front card-id="card-7735b0a37c146f61"}
$ \sin(a+b) = \cdots $
:::

::: {.back card-id="card-7735b0a37c146f61"}
$ \sin(a)\cos(b) + \cos(a)\sin(b) $.
:::

::: {.front card-id="card-9b1c923db6310b6f"}
$ \cos(a+b) = \cdots $
:::

::: {.back card-id="card-9b1c923db6310b6f"}
$ \cos(a)\cos(b) - \sin(a)\sin(b) $.
:::

::: {.front card-id="card-17a29c822d6de20a"}
$ \tan(a+b) = \cdots $
:::

::: {.back card-id="card-17a29c822d6de20a"}
$ {\tan(a)\tan(b) \over 1-\tan(a)\tan(b)} $.
:::

::: {.front card-id="card-ea216c0db40e8656"}
Double angle formulas converting $ f(2t) $ into $ \tan $ for $ f=\sin,\cos $.
:::

::: {.back card-id="card-ea216c0db40e8656"}
$$\begin{align}\sin(2t) &= {2\tan(t) \over 1+\tan^2(t)} \\ \cos(2t) &= {1-\tan^2(2t) \over 1+\tan^2(t)}\end{align}.$$
:::

::: {.front card-id="card-f959da8514f073d1"}
Standard parameterization of a circle in $ {\mathbf{C}} $
:::

::: {.back card-id="card-f959da8514f073d1"}
$$F(t) = {1-x^2\over 1+x^2} + i{2x\over 1+x^2}$$

where $ x = \tan(t) $ and $ t\in (-\pi/2, \pi/2) $.
:::

::: {.front card-id="card-54a4f4e158f3a677"}
Exponential definitions of $ \sin,\cos, \sinh, \cosh $.
:::

::: {.back card-id="card-54a4f4e158f3a677"}
$$\begin{align}  \cos(z) &= {e^{iz} + e^{-iz}\over 2} \qquad \cosh(z) = {e^{z} - e^{-z}\over 2}  \\ \sin(z) &= {e^{iz} + e^{-iz}\over 2i} \qquad \sinh(z) = {e^{z} - e^{-z}\over 2} \end{align}.$$
:::

::: {.front card-id="card-a9efbdda15a4c467"}
Relating hyperbolic functions to usual ones: $ \cosh(iz) = \cdots $
:::

::: {.back card-id="card-a9efbdda15a4c467"}
$$\cosh(iz) = \cos(z), \qquad \cos(iz) = \cosh(z).$$
:::

::: {.front card-id="card-f8a5b441dd2af28f"}
Relating hyperbolic functions to usual ones: $ \sin(z) = f(\sinh(\cdots) $
:::

::: {.back card-id="card-f8a5b441dd2af28f"}
$$\sinh(iz) = i\sin(z),\qquad \sin(iz) = i\sinh(z).$$
:::

::: {.front card-id="card-9a8542fb631eb8ea"}
Series expansion for $ \arctan(x) $.
:::

::: {.back card-id="card-9a8542fb631eb8ea"}
$$z - {1\over 3}z^3 + {1\over 5}z^5 + \cdots$$
:::

::: {.front card-id="card-002468197b6d24e0"}
Series expansion for $ \log $
:::

::: {.back card-id="card-002468197b6d24e0"}
$$-\log(1-z) = \sum_{n\geq 1} {z^n\over n}$$
:::

::: {.front card-id="card-4a77bc4987f9aafb"}
Series expansion for $ { \mathrm{sech} }(z) = {1\over \cosh(z)} $
:::

::: {.back card-id="card-4a77bc4987f9aafb"}
****

$$\operatorname{sech} x=1-\frac{x^{2}}{2}+\frac{5 x^{4}}{24}-\frac{61 x^{6}}{720}+\cdots.$$
:::

::: {.front card-id="card-80cd9af57714d4d1"}
Series expansion for $ \operatorname{csch}(z) = {1\over \sinh(z)} $
:::

::: {.back card-id="card-80cd9af57714d4d1"}
****

$$\operatorname{csch} x=x^{-1}-\frac{x}{6}+\frac{7 x^{3}}{360}-\frac{31 x^{5}}{15120}+\cdots.$$
:::

::: {.front card-id="card-05bb5c6be34086f4"}
Inverting series: for $ A(z) = \sum a_k z^k $ and $ 1/A(z) = \sum b_k z^k $, the formula for the $ b_k $ in terms of $ a_k $.
:::

::: {.back card-id="card-05bb5c6be34086f4"}
- $ b_0 = a_0^{-1} $
- $ b_1 = -a_0^{-1}(a_1 b_0 ) $
- $ b_2 = -a_0^{-1}(a_1b_1 + a_2b_0) $
- $ b_3 = -a_0^{-1}(a_1b_2 + a_2b_1 + a_3 b_0) $
- $ \cdots $

****

$$b_n = -a_0^{-1}\sum_{k=1}^n a_n b_{n-k} = -a_0^{-1}\qty{a_1b_{n-1} + a_2b_{n-2} + \cdots + a_n b_0}$$

i.e. count up the $ a $s and down the $ b $s, starting at $ b_{n-1} $ since $ b_n $ is unknown.
:::

::: {.front card-id="card-80afbd28f63b7e96"}
$ f^{-1} \left( \bigcup_i U_i \right) =_? \bigcup_i f^{-1}(U_i) $?
:::

::: {.back card-id="card-80afbd28f63b7e96"}
True.

$$\begin{aligned} f^{-1}\left[\bigcup_{i \in I} Y_i\right] & =\left\{x \in X \mathrel{\Big|}f(x) \in \bigcup_{i \in I} Y_i\right\} \\ & =\left\{x \in \lambda \mathrel{\Big|}\quad \exists i \in I \text { such that } f(x) \in Y_i\right\} \\ & =\bigcup_{i \in I}\left\{x \in X \mathrel{\Big|}f(x) \in Y_i\right\} \\ & =\bigcup_{i \in I} f^{-1}\left[Y_i\right] \end{aligned}$$
:::

::: {.front card-id="card-7696e37fb762a073"}
What is the limit definition of the exponential function?
:::

::: {.back card-id="card-7696e37fb762a073"}
$ e^x = \lim_{n \to \infty} \qty{1 + {x\over n}}^n $
:::

::: {.front card-id="card-6cd5f936b8576c92"}
$ \sin ^2 \theta=\cdots $
:::

::: {.back card-id="card-6cd5f936b8576c92"}
$ \sin ^2 \theta=\frac{1-\cos (2 \theta)}{2} $
:::

::: {.front card-id="card-1e5a093e1b6d71d9"}
$ \cos ^2 \theta=\cdots $
:::

::: {.back card-id="card-1e5a093e1b6d71d9"}
$ \cos ^2 \theta=\frac{1+\cos (2 \theta)}{2} $
:::

::: {.front card-id="card-1df98aa238ae6f4e"}
What is the weird trig substitution that bizarrely works sometimes?
:::

::: {.back card-id="card-1df98aa238ae6f4e"}
$ \theta = 2\tan^{-1}(x) $.
:::

::: {.front card-id="card-7cd1c0cd5720855d"}
What are the allowed indeterminate forms for L'Hopital's rule?
:::

::: {.back card-id="card-7cd1c0cd5720855d"}
The direct forms are $0/0$ and $\infty/\infty$. Rewrite products such as $0\cdot\infty$, differences such as $\infty-\infty$, and powers such as $0^0$, $1^\infty$, or $\infty^0$ before applying the rule. The derivative quotient must meet the rule's hypotheses.
:::

::: {.front card-id="card-dfbf87f69f38785a"}
What is the divergence test?
:::

::: {.back card-id="card-dfbf87f69f38785a"}
$ \sum c_n < \infty \implies c_n\overset{n\to\infty}\longrightarrow 0 $.
:::

::: {.front card-id="card-ecab06dc74aa507e"}
What is the $ p{\hbox{-}} $test?
:::

::: {.back card-id="card-ecab06dc74aa507e"}
$ \sum_{n\geq 0} 1/n^p < \infty \iff p >1 $ and diverges otherwise.
:::

::: {.front card-id="card-e46324bf760d03c5"}
What is the comparison test?
:::

::: {.back card-id="card-e46324bf760d03c5"}
If $ a_n \leq b_n $ for $ n \gg 0 $, then $ \sum b_n < \infty \implies \sum a_n < \infty $.

If $ a_n\geq b_n $ for $ n\gg 0 $, then $ \sum b_n \not<\infty \implies \sum a_n\not< \infty $.
:::

::: {.front card-id="card-7f7e5be1f01f486b"}
What is the limit comparison test?
:::

::: {.back card-id="card-7f7e5be1f01f486b"}
Let $ L\coloneqq\lim_{n\to\infty}{a_n\over b_n} $, then

$ L\neq 0:\, \sum a_n < \infty \iff \sum b_n < \infty $.

$ L=0:\, \sum b_n < \infty \implies \sum a_n < \infty $

$ L= \infty:\, \sum b_n \not < \infty \implies \sum a_n \not < \infty $.
:::

::: {.front card-id="card-2165512888b7e1ad"}
What is the integral test?
:::

::: {.back card-id="card-2165512888b7e1ad"}
If $ c_n = f(n) $, then $ \sum_{n\geq 0} c_n < \infty \iff \int_{N}^\infty f(x)\,dx< \infty $ for any $ N $.
:::

::: {.front card-id="card-d9978fc3eb213700"}
What is the alternating series test?
:::

::: {.back card-id="card-d9978fc3eb213700"}
If $ c_{n+1}\leq c_n $ for all $ n $ and $ c_n\to 0 $ then $ \sum (-1)^n c_n < \infty $.
:::

::: {.front card-id="card-f304a76d8de0f862"}
What is the ratio test?
:::

::: {.back card-id="card-f304a76d8de0f862"}
For $\sum a_n$ with $a_n\ne0$ eventually, let $L=\lim_{n\to\infty}|a_{n+1}/a_n|$ if it exists. The series converges absolutely if $L<1$, diverges if $L>1$, and the test is inconclusive if $L=1$.
:::

::: {.front card-id="card-e75a240f6a028504"}
What is the root test?
:::

::: {.back card-id="card-e75a240f6a028504"}
For $\sum a_n$, let $L=\limsup_{n\to\infty}|a_n|^{1/n}$. The series converges absolutely if $L<1$, diverges if $L>1$, and the test is inconclusive if $L=1$.
:::

::: {.front card-id="card-30a6b9e80aa8b86a"}
How is $ \nabla \times\mathbf{F} $ computed?
:::

::: {.back card-id="card-30a6b9e80aa8b86a"}
$$\nabla\times F = \operatorname{det}\begin{bmatrix}\widehat{i} & \widehat{j} & \widehat{k} \\ {\partial}_x &{\partial}_y &{\partial}_z \\ F_1 & F_2 & F_3 \end{bmatrix}$$
:::

::: {.front card-id="card-9e113f9c1391db7d"}
How is $ \nabla \cdot \mathbf{F} $ computed?
:::

::: {.back card-id="card-9e113f9c1391db7d"}
$$\nabla \cdot \mathbf{F} \coloneqq\nabla \cdot {\left[ {F_1, \cdots, F_n} \right]} = \sum {\partial}_{x_i} F_i$$
:::

::: {.front card-id="card-639e9391ca2ff1da"}
What are the parametric and symmetric equations of lines in $ {\mathbf{R}}^3 $?
:::

::: {.back card-id="card-639e9391ca2ff1da"}
Parametric: $ r(t) = t\mathbf{p}_0 + (1-t)\mathbf{p}_1 $.

Symmetric: solve for $ t $ in each component and set equal to get

$$\frac{x-x_0}{n_0}=\frac{y-y_0}{n_1}=\frac{z-z_0}{n_2}$$
:::

::: {.front card-id="card-93d805de0967ee64"}
What is the vector/scalar equation of a plane?
:::

::: {.back card-id="card-93d805de0967ee64"}
For $ \mathbf{n} $ a normal and $ \mathbf{p}_0 $ on the plane, $ {\left\langle {\mathbf{x} - \mathbf{p}_0},~{\mathbf{n}} \right\rangle} = 0 $
:::

::: {.front card-id="card-e8e0738177a2a990"}
What are the changes of variables for cartesian to spherical coordinates?
:::

::: {.back card-id="card-e8e0738177a2a990"}
$$\begin{aligned} & x=r \sin \theta \cos \varphi \\ & y=r \sin \theta \sin \varphi \\ & z=r \cos \theta \end{aligned}$$
:::

::: {.front card-id="card-3950fe7cebc3e7cf"}
What is the differential for a change of rectangular to spherical coordinates?
:::

::: {.back card-id="card-3950fe7cebc3e7cf"}
$ \,dx\,dy\,dz\leadsto \rho^2 \sin(\phi)\, \,d\rho\,d\phi 0\,d\theta $
:::

::: {.front card-id="card-cea01bff1ba205a0"}
What is Green's theorem?
:::

::: {.back card-id="card-cea01bff1ba205a0"}
Circulation form: for a vector field $ \mathbf{F}(x, y) = {\left[ {F_1(x, y), F_2(x, y) } \right]} $ on $ {\mathbf{R}}^2 $,

$$\begin{align*}\oint_{{{\partial}}R} \mathbf{F}(x,y)\cdot d\mathbf{r} &= \oint_{{{\partial}}R} \mathbf{F}(x,y)\cdot \mathbf{T}(x,y) \,ds\\ &=  \oint_{{{\partial}}R}F_1(x,y)\,dx+ F_2(x,y)\,dy\\ &= \iint_R \qty{{\partial}_x F_2(x,y) - {\partial}_y F_1(x,y)} \,dA\\ &=\iint_R (\nabla\times F(x,y) )\,dA\end{align*}$$

Flux form:

$$\oint_{{{\partial}}R} \mathbf{F}(x,y)\cdot \mathbf{N}(x,y)\,ds= \iint_R {\partial}_x F_1(x,y) + {\partial}_y F_2(x,y)\,dA= \iint_R (\nabla \cdot \mathbf{F}(x,y)) \,dA$$
:::

::: {.front card-id="card-c5b0d710266073a4"}
What is Stokes' theorem?
:::

::: {.back card-id="card-c5b0d710266073a4"}
$$\int_{{{\partial}}S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla\times\mathbf{F}) \cdot d\mathbf{S} \coloneqq\iint_S (\nabla\times\mathbf{F}) \cdot \mathbf{N} \, dS$$
:::

::: {.front card-id="card-08bd9b5aba58c5e2"}
What is Faraday's law?
:::

::: {.back card-id="card-08bd9b5aba58c5e2"}
$$\nabla \times\mathbf{E} = -{\frac{\partial }{\partial t}\,} \mathbf{B}$$
:::

::: {.front card-id="card-04736c7b73f6412c"}
What is the fundamental theorem of line integrals?
:::

::: {.back card-id="card-04736c7b73f6412c"}
$$\int_C f\cdot d\mathbf{r} = F(p_1) - F(p_2) \iff \nabla F = f$$
:::

::: {.front card-id="card-ef6ab3acffc1ff9e"}
What is the divergence theorem?
:::

::: {.back card-id="card-ef6ab3acffc1ff9e"}
$$\iiint_M \nabla\cdot \mathbf{F}(x,y,z)\,dV= \iint_{{{\partial}}M}\mathbf{F}(x,y,z) \cdot d\mathbf{S} \coloneqq\iint_{S} \mathbf{F} \cdot \mathbf{N} \, dS$$
:::

::: {.front card-id="card-c3228f57a99806e6"}
What are the div-grad-curl theorems?
:::

::: {.back card-id="card-c3228f57a99806e6"}
$ \nabla \cdot(\nabla \times\mathbf F) = 0 $.

$ \nabla\times(\nabla \mathbf F) = 0 $.
:::

::: {.front card-id="card-aaf11f8908744b0b"}
How do you solve a linear second order ODE?
:::

::: {.back card-id="card-aaf11f8908744b0b"}
For $y''+p(x)y'+q(x)y=g(x)$, first find independent solutions $y_1,y_2$ of the homogeneous equation. The general solution is $c_1y_1+c_2y_2+y_p$, where $y_p$ is a particular solution, obtainable by variation of parameters. For constant coefficients, solve the characteristic polynomial for $y_1,y_2$.
:::

::: {.front card-id="card-cad38830857677f5"}
Define $ \log(z) $ for $ z\in {\mathbf{C}} $.
:::

::: {.back card-id="card-cad38830857677f5"}
$ \log(z) = \log\left(re^{i\theta}\right) = \log(r) + i\theta = \log(|z|)+i\arg(z) $
:::

::: {.front card-id="card-4108e89ad5ce521e"}
What are the implications for fields, UFDs, PIDs, etc?
:::

::: {.back card-id="card-4108e89ad5ce521e"}
$$\begin{aligned}\text { field } & \Longrightarrow \text { Euclidean Domain } \Longrightarrow \text { PID } \\ & \Longrightarrow \text { UFD } \Longrightarrow \text { integral domain }\end{aligned}$$

ED not a field: $ {\mathbf{C}}[x] $.

PID not an ED: $ {\mathbf{Z}} { \left[ \scriptstyle { 1 + \sqrt{-19} \over 2} \right] }  $.

UFD not a PID: $ {\mathbf{Z}}[x] $; take $ \left\langle{x, 2}\right\rangle $.

ID not a UFD: $ {\mathbf{Z}} { \left[ \scriptstyle {\sqrt{-5}} \right] }  $.
:::
