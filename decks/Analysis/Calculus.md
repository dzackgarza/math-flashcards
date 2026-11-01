---
title: "Analysis::Calculus"
---

::: {.front card-id="card-9a8542fb631eb8ea"}
Series expansion for $\arctan(x)$.
:::

::: {.back card-id="card-9a8542fb631eb8ea"}
$$z - {1\over 3}z^3 + {1\over 5}z^5 + \cdots$$
:::

::: {.front card-id="card-002468197b6d24e0"}
Series expansion for $\log$
:::

::: {.back card-id="card-002468197b6d24e0"}
$$-\log(1-z) = \sum_{n\geq 1} {z^n\over n}$$
:::

::: {.front card-id="card-7696e37fb762a073" tags="definition, formula"}
What is the limit definition of the exponential function?
:::

::: {.back card-id="card-7696e37fb762a073"}
$e^x = \lim_{n \to \infty} \qty{1 + {x\over n}}^n$
:::

::: {.front card-id="card-1df98aa238ae6f4e"}
What is the weird trig substitution that bizarrely works sometimes?
:::

::: {.back card-id="card-1df98aa238ae6f4e"}
$\theta = 2\tan^{-1}(x)$.
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
$\sum c_n < \infty \implies c_n\overset{n\to\infty}\longrightarrow 0$.
:::

::: {.front card-id="card-ecab06dc74aa507e"}
What is the $p\dash$test?
:::

::: {.back card-id="card-ecab06dc74aa507e"}
$\sum_{n\geq 0} 1/n^p < \infty \iff p >1$ and diverges otherwise.
:::

::: {.front card-id="card-e46324bf760d03c5"}
What is the comparison test?
:::

::: {.back card-id="card-e46324bf760d03c5"}
If $a_n \leq b_n$ for $n \gg 0$, then $\sum b_n < \infty \implies \sum a_n < \infty$.

If $a_n\geq b_n$ for $n\gg 0$, then $\sum b_n \not<\infty \implies \sum a_n\not< \infty$.
:::

::: {.front card-id="card-7f7e5be1f01f486b"}
What is the limit comparison test?
:::

::: {.back card-id="card-7f7e5be1f01f486b"}
Let $L\coloneqq\lim_{n\to\infty}{a_n\over b_n}$, then

$L\neq 0:\, \sum a_n < \infty \iff \sum b_n < \infty$.

$L=0:\, \sum b_n < \infty \implies \sum a_n < \infty$

$L= \infty:\, \sum b_n \not < \infty \implies \sum a_n \not < \infty$.
:::

::: {.front card-id="card-2165512888b7e1ad"}
What is the integral test?
:::

::: {.back card-id="card-2165512888b7e1ad"}
If $c_n = f(n)$, then $\sum_{n\geq 0} c_n < \infty \iff \int_{N}^\infty f(x)\,dx< \infty$ for any $N$.
:::

::: {.front card-id="card-d9978fc3eb213700"}
What is the alternating series test?
:::

::: {.back card-id="card-d9978fc3eb213700"}
If $c_{n+1}\leq c_n$ for all $n$ and $c_n\to 0$ then $\sum (-1)^n c_n < \infty$.
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
How is $\nabla \times\mathbf{F}$ computed?
:::

::: {.back card-id="card-30a6b9e80aa8b86a"}
$$\nabla\times F = \operatorname{det}\begin{bmatrix}\widehat{i} & \widehat{j} & \widehat{k} \\ {\partial}_x &{\partial}_y &{\partial}_z \\ F_1 & F_2 & F_3 \end{bmatrix}$$
:::

::: {.front card-id="card-9e113f9c1391db7d"}
How is $\nabla \cdot \mathbf{F}$ computed?
:::

::: {.back card-id="card-9e113f9c1391db7d"}
$$\nabla \cdot \mathbf{F} \coloneqq\nabla \cdot {\left[ {F_1, \cdots, F_n} \right]} = \sum {\partial}_{x_i} F_i$$
:::

::: {.front card-id="card-639e9391ca2ff1da"}
What are the parametric and symmetric equations of lines in ${\mathbf{R}}^3$?
:::

::: {.back card-id="card-639e9391ca2ff1da"}
Parametric: $r(t) = t\mathbf{p}_0 + (1-t)\mathbf{p}_1$.

Symmetric: solve for $t$ in each component and set equal to get
$$\frac{x-x_0}{n_0}=\frac{y-y_0}{n_1}=\frac{z-z_0}{n_2}$$
:::

::: {.front card-id="card-93d805de0967ee64"}
What is the vector/scalar equation of a plane?
:::

::: {.back card-id="card-93d805de0967ee64"}
For $\mathbf{n}$ a normal and $\mathbf{p}_0$ on the plane, ${\left\langle {\mathbf{x} - \mathbf{p}_0},~{\mathbf{n}} \right\rangle} = 0$
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
$\,dx\,dy\,dz\leadsto \rho^2 \sin(\phi)\, \,d\rho\,d\phi 0\,d\theta$
:::

::: {.front card-id="card-cea01bff1ba205a0"}
What is Green's theorem?
:::

::: {.back card-id="card-cea01bff1ba205a0"}
Circulation form: for a vector field $\mathbf{F}(x, y) = {\left[ {F_1(x, y), F_2(x, y) } \right]}$ on ${\mathbf{R}}^2$,
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
$\nabla \cdot(\nabla \times\mathbf F) = 0$.

$\nabla\times(\nabla \mathbf F) = 0$.
:::

::: {.front card-id="card-aaf11f8908744b0b"}
How do you solve a linear second order ODE?
:::

::: {.back card-id="card-aaf11f8908744b0b"}
For $y''+p(x)y'+q(x)y=g(x)$, first find independent solutions $y_1,y_2$ of the homogeneous equation. The general solution is $c_1y_1+c_2y_2+y_p$, where $y_p$ is a particular solution, obtainable by variation of parameters. For constant coefficients, solve the characteristic polynomial for $y_1,y_2$.
:::
