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

::: {.front card-id="card-ff702937bc14f55a" tags="definition"}
Absolute convergence
:::

::: {.back card-id="card-ff702937bc14f55a"}
A series $\sum a_n$ converges absolutely if $\sum |a_n|$ converges.
:::

::: {.front card-id="card-062a149dfc31e301" tags="definition"}
Alternating series
:::

::: {.back card-id="card-062a149dfc31e301"}
A series whose terms alternate in sign, i.e. $\sum (-1)^n c_n$ or $\sum (-1)^{n+1} c_n$ with $c_n \geq 0$.
:::

::: {.front card-id="card-9daf0302f1654048" tags="definition"}
Change of variables
:::

::: {.back card-id="card-9daf0302f1654048"}
Substitution $x=g(u)$ in an integral, with $dx = |\det Dg(u)|\,du$ in several variables.
:::

::: {.front card-id="card-f834fd58e1aa2c2e" tags="definition"}
Circulation
:::

::: {.back card-id="card-f834fd58e1aa2c2e"}
The line integral $\oint_C F \cdot dr$ of a vector field around a closed curve $C$.
:::

::: {.front card-id="card-73cdd608fb014f29" tags="definition"}
Convergent series
:::

::: {.back card-id="card-73cdd608fb014f29"}
A series $\sum a_n$ converges if its sequence of partial sums converges.
:::

::: {.front card-id="card-031020efa6f380ce" tags="definition"}
Curl
:::

::: {.back card-id="card-031020efa6f380ce"}
For $F=(F_1,F_2,F_3)$ on $\RR^3$, $\nabla \times F = \left(\frac{\partial F_3}{\partial y}-\frac{\partial F_2}{\partial z},\frac{\partial F_1}{\partial z}-\frac{\partial F_3}{\partial x},\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\right)$.
:::

::: {.front card-id="card-226447c0d4b49a89" tags="definition"}
Divergence
:::

::: {.back card-id="card-226447c0d4b49a89"}
For $F=(F_1,\dots,F_n)$, $\nabla \cdot F = \sum_{i=1}^{n} \frac{\partial F_i}{\partial x_i}$.
:::

::: {.front card-id="card-838a909ec81fcb40" tags="definition"}
Divergent series
:::

::: {.back card-id="card-838a909ec81fcb40"}
A series whose sequence of partial sums does not converge.
:::

::: {.front card-id="card-03c2a6d2f30ed38c" tags="definition"}
Double integral
:::

::: {.back card-id="card-03c2a6d2f30ed38c"}
The integral $\iint_R f(x,y)\,dA$ of a function over a plane region $R$.
:::

::: {.front card-id="card-7a4e89fcfa0afda7" tags="definition"}
Flux
:::

::: {.back card-id="card-7a4e89fcfa0afda7"}
The surface integral $\iint_S F \cdot N\,dS$ of a vector field across an oriented surface $S$ with unit normal $N$.
:::

::: {.front card-id="card-f2729d026df34595" tags="definition"}
General solution
:::

::: {.back card-id="card-f2729d026df34595"}
A family of solutions containing every solution, typically $c_1 y_1+c_2 y_2+y_p$ for a second-order linear ODE.
:::

::: {.front card-id="card-474e9482a49632f1" tags="definition"}
Gradient
:::

::: {.back card-id="card-474e9482a49632f1"}
$\nabla f = \left(\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\right)$.
:::

::: {.front card-id="card-8aeea673fb0b3ce5" tags="definition"}
Homogeneous equation
:::

::: {.back card-id="card-8aeea673fb0b3ce5"}
An ODE with zero forcing term, e.g. $y''+p(x)y'+q(x)y=0$.
:::

::: {.front card-id="card-3e738ebf0a3261de" tags="definition"}
Indeterminate form
:::

::: {.back card-id="card-3e738ebf0a3261de"}
An expression such as $0/0$, $\infty/\infty$, $0\cdot\infty$, $0^0$, $1^\infty$, or $\infty^0$ whose limit is not determined by the form alone.
:::

::: {.front card-id="card-7128131356c8e6fb" tags="definition"}
L'hopital's rule
:::

::: {.back card-id="card-7128131356c8e6fb"}
If $f,g$ are differentiable near $a$, $f(a)=g(a)=0$ or both tend to $\pm\infty$, and $\lim f'(x)/g'(x)=L$, then $\lim f(x)/g(x)=L$, provided the hypotheses hold on a punctured neighborhood.
:::

::: {.front card-id="card-5aec7fa2f93688d3" tags="definition"}
Line integral
:::

::: {.back card-id="card-5aec7fa2f93688d3"}
An integral along a curve $C$: $\int_C f\,ds$ for a scalar function, or $\int_C F \cdot dr$ for a vector field.
:::

::: {.front card-id="card-ee6575462586e6bb" tags="definition"}
Linear independence
:::

::: {.back card-id="card-ee6575462586e6bb"}
A set of vectors or functions is linearly independent if no nontrivial linear combination equals zero.
:::

::: {.front card-id="card-4d8462535001ef8a" tags="definition"}
Normal vector
:::

::: {.back card-id="card-4d8462535001ef8a"}
A nonzero vector perpendicular to a plane or surface at a point.
:::

::: {.front card-id="card-8e915f7217a60689" tags="definition"}
Ordinary differential equation
:::

::: {.back card-id="card-8e915f7217a60689"}
An equation involving an unknown function of one variable and its derivatives.
:::

::: {.front card-id="card-4865888ec43b8ab0" tags="definition"}
Parametric equations
:::

::: {.back card-id="card-4865888ec43b8ab0"}
Equations expressing the coordinates of points on a curve or surface in terms of one or more parameters, e.g. $r(t)=t p_0+(1-t)p_1$.
:::

::: {.front card-id="card-beb83ae942b90c12" tags="definition"}
Particular solution
:::

::: {.back card-id="card-beb83ae942b90c12"}
A single solution $y_p$ of an inhomogeneous equation, before adding the homogeneous general solution.
:::

::: {.front card-id="card-8ffc80ba2aae0fd0" tags="definition"}
Plane
:::

::: {.back card-id="card-8ffc80ba2aae0fd0"}
A set of the form $\{x \in \RR^3 : \langle x-p_0, n\rangle = 0\}$, where $p_0$ is a point on the plane and $n$ is a normal vector.
:::

::: {.front card-id="card-1f06a57c84074d61" tags="definition"}
Series expansion
:::

::: {.back card-id="card-1f06a57c84074d61"}
A representation of a function as a sum of terms, typically a power series $\sum a_n (x-a)^n$.
:::

::: {.front card-id="card-468cafe7a9b2604f" tags="definition"}
Spherical coordinates
:::

::: {.back card-id="card-468cafe7a9b2604f"}
Coordinates $(r,\theta,\varphi)$ with $x=r\sin\theta\cos\varphi$, $y=r\sin\theta\sin\varphi$, $z=r\cos\theta$, where $\theta$ is the polar angle and $\varphi$ the azimuthal angle.
:::

::: {.front card-id="card-30ce93134b9ffdb1" tags="definition"}
Surface integral
:::

::: {.back card-id="card-30ce93134b9ffdb1"}
An integral over a surface $S$: $\iint_S f\,dS$ for a scalar function, or $\iint_S F \cdot N\,dS$ for a vector field.
:::

::: {.front card-id="card-6cd271d119fcb7b2" tags="definition"}
Symmetric equations
:::

::: {.back card-id="card-6cd271d119fcb7b2"}
Equations of a line obtained by eliminating the parameter, e.g. $\frac{x-x_0}{n_0}=\frac{y-y_0}{n_1}=\frac{z-z_0}{n_2}$.
:::

::: {.front card-id="card-0ff182eb2e7d18f5" tags="definition"}
Trigonometric substitution
:::

::: {.back card-id="card-0ff182eb2e7d18f5"}
A substitution that introduces a trigonometric function or its inverse for a variable, e.g. $\theta=2\arctan x$, to simplify an integral.
:::

::: {.front card-id="card-aa3c58d62caac136" tags="definition"}
Triple integral
:::

::: {.back card-id="card-aa3c58d62caac136"}
The integral $\iiint_M f(x,y,z)\,dV$ of a function over a solid region $M$.
:::

::: {.front card-id="card-5eb6084f8cc39544" tags="definition"}
Variation of parameters
:::

::: {.back card-id="card-5eb6084f8cc39544"}
A method for finding a particular solution by replacing the constants in the homogeneous solution with functions and solving for them.
:::

::: {.front card-id="card-a3c35686dac5f92c" tags="definition"}
Vector field
:::

::: {.back card-id="card-a3c35686dac5f92c"}
An assignment of a vector $F(x)$ to each point $x$ in a subset of $\RR^n$.
:::

::: {.front card-id="card-c0807240a03a7284" tags="definition"}
Volume element
:::

::: {.back card-id="card-c0807240a03a7284"}
The factor relating coordinate differentials to volume, e.g. $dV = dx\,dy\,dz = r^2\sin\theta\,dr\,d\theta\,d\varphi$ in spherical coordinates.
:::
