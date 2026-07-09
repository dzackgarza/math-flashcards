---
title: "Math::Grad Math Facts"
---

- What is Descartes' rule of signs?

    The number of positive real roots of $ f $ is equivalent $ \operatorname{mod}2 $ to the number of sign changes in the coefficients of $ f(x) $. The number of *negative* real roots is the same process but for $ f(-x) $. E.g. $ f(x)=x^5+4 x^4-3 x^2+x-6 $ has 3 changes of sign, so an odd number of real roots.

- Factor $ x^n-y^n $.

    $$x^n-y^n=(x-y)\left(x^{n-1}+x^{n-2} y+\ldots+x y^{n-2}+y^{n-1}\right) = (x-y)\sum_{k=0}^{n-1}x^{n-k-1}y^k$$

    How to prove: long division to obtain $ {x^n-y^n\over x-y} = x^n + y\qty{x^{n-1}-y^{n-1}\over x-y} $ and induct. How to remember: $ x^n-1 = (x-1)(x^{n-1} + x^{n-2} + \cdot + x + 1) $ and set $ x=b/a $.

- Factor $ x^n + y^n $ for $ n $ an odd prime.

    $$x^n+y^n=(x+y)\left(x^{n-1}-x^{n-2} y+\cdots-x y^{n-2}+y^{n-1}\right)$$

- Write $ \log $ and $ \exp $ as group homomorphisms; i.e. what are the domains and codomains?

    $${\mathbf{G}}_m \underset{\exp}{\overset{\log}{\rightleftharpoons}} {\mathbf{G}}_a$$

- True or false: $ \log(a+b) = \log(a)\cdot \log(b) $.

    False: $ \log_2(4+4) = \log_2(8) = 3 \neq 4 = 2 \cdot 2 = \log_2(4) \cdot \log_2(4) $.

- $ \sin(\pi/6) $

    $ 1/2 $

- $ \cos(\pi/6) $

    $ \sqrt 3 /2 $.

- $ \sin(\pi/3) $

    $ \sqrt 3/2 $

- $ \cos(\pi/3) $

    $ 1/2 $.

- $ \arctan(0) $

    $ 0 $

- $ \arctan(1) $

    $ \pi/4 $.

- $ \arctan(\infty) $

    $ \pi/2 $

- $ \arctan\qty{\sqrt 3\over 3} $

    $ \pi/6 $

- $ \arctan\qty{\sqrt 3} $

    $ \pi/3 $

- $ \sin(a+b) = \cdots $

    $ \sin(a)\cos(b) + \cos(a)\sin(b) $.

- $ \cos(a+b) = \cdots $

    $ \cos(a)\cos(b) - \sin(a)\sin(b) $.

- $ \tan(a+b) = \cdots $

    $ {\tan(a)\tan(b) \over 1-\tan(a)\tan(b)} $.

- Double angle formulas converting $ f(2t) $ into $ \tan $ for $ f=\sin,\cos $.

    $$\begin{align}\sin(2t) &= {2\tan(t) \over 1+\tan^2(t)} \\ \cos(2t) &= {1-\tan^2(2t) \over 1+\tan^2(t)}\end{align}.$$

- Standard parameterization of a circle in $ {\mathbf{C}} $

    $$F(t) = {1-x^2\over 1+x^2} + i{2x\over 1+x^2}$$

    where $ x = \tan(t) $ and $ t\in (-\pi/2, \pi/2) $.

- Exponential definitions of $ \sin,\cos, \sinh, \cosh $.

    $$\begin{align}  \cos(z) &= {e^{iz} + e^{-iz}\over 2} \qquad \cosh(z) = {e^{z} - e^{-z}\over 2}  \\ \sin(z) &= {e^{iz} + e^{-iz}\over 2i} \qquad \sinh(z) = {e^{z} - e^{-z}\over 2} \end{align}.$$

- Relating hyperbolic functions to usual ones: $ \cosh(iz) = \cdots $

    $$\cosh(iz) = \cos(z), \qquad \cos(iz) = \cosh(z).$$

- Relating hyperbolic functions to usual ones: $ \sin(z) = f(\sinh(\cdots) $

    $$\sinh(iz) = i\sin(z),\qquad \sin(iz) = i\sinh(z).$$

- Series expansion for $ \arctan(x) $.

    $$z - {1\over 3}z^3 + {1\over 5}z^5 + \cdots$$

- Series expansion for $ \log $

    $$-\log(1-z) = \sum_{n\geq 1} {z^n\over n}$$

- Series expansion for $ { \mathrm{sech} }(z) = {1\over \cosh(z)} $

    ****

    $$\operatorname{sech} x=1-\frac{x^{2}}{2}+\frac{5 x^{4}}{24}-\frac{61 x^{6}}{720}+\cdots.$$

- Series expansion for $ \operatorname{csch}(z) = {1\over \sinh(z)} $

    ****

    $$\operatorname{csch} x=x^{-1}-\frac{x}{6}+\frac{7 x^{3}}{360}-\frac{31 x^{5}}{15120}+\cdots.$$

- Inverting series: for $ A(z) = \sum a_k z^k $ and $ 1/A(z) = \sum b_k z^k $, the formula for the $ b_k $ in terms of $ a_k $.

    - $ b_0 = a_0^{-1} $
    - $ b_1 = -a_0^{-1}(a_1 b_0 ) $
    - $ b_2 = -a_0^{-1}(a_1b_1 + a_2b_0) $
    - $ b_3 = -a_0^{-1}(a_1b_2 + a_2b_1 + a_3 b_0) $
    - $ \cdots $

    ****

    $$b_n = -a_0^{-1}\sum_{k=1}^n a_n b_{n-k} = -a_0^{-1}\qty{a_1b_{n-1} + a_2b_{n-2} + \cdots + a_n b_0}$$

    i.e. count up the $ a $s and down the $ b $s, starting at $ b_{n-1} $ since $ b_n $ is unknown.

- $ f^{-1} \left( \bigcup_i U_i \right) =_? \bigcup_i f^{-1}(U_i) $?

    True.

    $$\begin{aligned} f^{-1}\left[\bigcup_{i \in I} Y_i\right] & =\left\{x \in X \mathrel{\Big|}f(x) \in \bigcup_{i \in I} Y_i\right\} \\ & =\left\{x \in \lambda \mathrel{\Big|}\quad \exists i \in I \text { such that } f(x) \in Y_i\right\} \\ & =\bigcup_{i \in I}\left\{x \in X \mathrel{\Big|}f(x) \in Y_i\right\} \\ & =\bigcup_{i \in I} f^{-1}\left[Y_i\right] \end{aligned}$$

- What is the limit definition of the exponential function?

    $ e^x = \lim_{n \to \infty} \qty{1 + {x\over n}}^n $

- $ \sin ^2 \theta=\cdots $

    $ \sin ^2 \theta=\frac{1-\cos (2 \theta)}{2} $

- $ \cos ^2 \theta=\cdots $

    $ \cos ^2 \theta=\frac{1+\cos (2 \theta)}{2} $

- What is the weird trig substitution that bizarrely works sometimes?

    $ \theta = 2\tan^{-1}(x) $.

- What are the allowed indeterminate forms for L'Hopital's rule?

    - Grad Math Facts-2

- What is the divergence test?

    $ \sum c_n < \infty \implies c_n\overset{n\to\infty}\longrightarrow 0 $.

- What is the $ p{\hbox{-}} $test?

    $ \sum_{n\geq 0} 1/n^p < \infty \iff p >1 $ and diverges otherwise.

- What is the comparison test?

    If $ a_n \leq b_n $ for $ n \gg 0 $, then $ \sum b_n < \infty \implies \sum a_n < \infty $.

    If $ a_n\geq b_n $ for $ n\gg 0 $, then $ \sum b_n \not<\infty \implies \sum a_n\not< \infty $.

- What is the limit comparison test?

    Let $ L\coloneqq\lim_{n\to\infty}{a_n\over b_n} $, then

    $ L\neq 0:\, \sum a_n < \infty \iff \sum b_n < \infty $.

    $ L=0:\, \sum b_n < \infty \implies \sum a_n < \infty $

    $ L= \infty:\, \sum b_n \not < \infty \implies \sum a_n \not < \infty $.

- What is the integral test?

    If $ c_n = f(n) $, then $ \sum_{n\geq 0} c_n < \infty \iff \int_{N}^\infty f(x)\,dx< \infty $ for any $ N $.

- What is the alternating series test?

    If $ c_{n+1}\leq c_n $ for all $ n $ and $ c_n\to 0 $ then $ \sum (-1)^n c_n < \infty $.

- What is the ratio test?

    Grad Math Facts-3

- What is the root test?

    Grad Math Facts-3

- How is $ \nabla \times\mathbf{F} $ computed?

    $$\nabla\times F = \operatorname{det}\begin{bmatrix}\widehat{i} & \widehat{j} & \widehat{k} \\ {\partial}_x &{\partial}_y &{\partial}_z \\ F_1 & F_2 & F_3 \end{bmatrix}$$

- How is $ \nabla \cdot \mathbf{F} $ computed?

    $$\nabla \cdot \mathbf{F} \coloneqq\nabla \cdot {\left[ {F_1, \cdots, F_n} \right]} = \sum {\partial}_{x_i} F_i$$

- What are the parametric and symmetric equations of lines in $ {\mathbf{R}}^3 $?

    Parameteric: $ r(t) = t\mathbf{p}_0 + (1-t)\mathbf{p}_1 $.

    Symmetric: solve for $ t $ in each component and set equal to get

    $$\frac{x-x_0}{n_0}=\frac{y-y_0}{n_1}=\frac{z-z_0}{n_2}$$

- What is the vector/scalar equation of a plane?

    For $ \mathbf{n} $ a normal and $ \mathbf{p}_0 $ on the plane, $ {\left\langle {\mathbf{x} - \mathbf{p}_0},~{\mathbf{n}} \right\rangle} = 0 $

- What are the changes of variables for cartesian to spherical coordinates?

    $$\begin{aligned} & x=r \sin \theta \cos \varphi \\ & y=r \sin \theta \sin \varphi \\ & z=r \cos \theta \end{aligned}$$

- What is the differential for a change of rectangular to spherical coordinates?

    $ \,dx\,dy\,dz\leadsto \rho^2 \sin(\phi)\, \,d\rho\,d\phi 0\,d\theta $

- What is Green's theorem?

    Circulation form: for a vector field $ \mathbf{F}(x, y) = {\left[ {F_1(x, y), F_2(x, y) } \right]} $ on $ {\mathbf{R}}^2 $,

    $$\begin{align*}\oint_{{{\partial}}R} \mathbf{F}(x,y)\cdot d\mathbf{r} &= \oint_{{{\partial}}R} \mathbf{F}(x,y)\cdot \mathbf{T}(x,y) \,ds\\ &=  \oint_{{{\partial}}R}F_1(x,y)\,dx+ F_2(x,y)\,dy\\ &= \iint_R \qty{{\partial}_x F_2(x,y) - {\partial}_y F_1(x,y)} \,dA\\ &=\iint_R (\nabla\times F(x,y) )\,dA\end{align*}$$

    Flux form:

    $$\oint_{{{\partial}}R} \mathbf{F}(x,y)\cdot \mathbf{N}(x,y)\,ds= \iint_R {\partial}_x F_1(x,y) + {\partial}_y F_2(x,y)\,dA= \iint_R (\nabla \cdot \mathbf{F}(x,y)) \,dA$$

- What is Stokes' theorem?

    $$\int_{{{\partial}}S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla\times\mathbf{F}) \cdot d\mathbf{S} \coloneqq\iint_S (\nabla\times\mathbf{F}) \cdot \mathbf{N} \, dS$$

- What is Faraday's law?

    $$\nabla \times\mathbf{E} = -{\frac{\partial }{\partial t}\,} \mathbf{B}$$

- What is the fundamental theorem of line integrals?

    $$\int_C f\cdot d\mathbf{r} = F(p_1) - F(p_2) \iff \nabla F = f$$

- What is the divergence theorem?

    $$\iiint_M \nabla\cdot \mathbf{F}(x,y,z)\,dV= \iint_{{{\partial}}M}\mathbf{F}(x,y,z) \cdot d\mathbf{S} \coloneqq\iint_{S} \mathbf{F} \cdot \mathbf{N} \, dS$$

- What are the div-grad-curl theorems?

    $ \nabla \cdot(\nabla \times\mathbf F) = 0 $.

    $ \nabla\times(\nabla \mathbf F) = 0 $.

- How do you solve a linear second order ODE?

    Grad Math Facts-3

- Define $ \log(z) $ for $ z\in {\mathbf{C}} $.

    $ \log(z) = \log\left(re^{i\theta}\right) = \log(r) + i\theta = \log(|z|)+i\arg(z) $

- What are the implications for fields, UFDs, PIDs, etc?

    $$\begin{aligned}\text { field } & \Longrightarrow \text { Euclidean Domain } \Longrightarrow \text { PID } \\ & \Longrightarrow \text { UFD } \Longrightarrow \text { integral domain }\end{aligned}$$

    ED not a field: $ {\mathbf{C}}[x] $.

    PID not an ED: $ {\mathbf{Z}} { \left[ \scriptstyle { 1 + \sqrt{-19} \over 2} \right] }  $.

    UFD not a PID: $ {\mathbf{Z}}[x] $; take $ \left\langle{x, 2}\right\rangle $.

    ID not a UFD: $ {\mathbf{Z}} { \left[ \scriptstyle {\sqrt{-5}} \right] }  $.
