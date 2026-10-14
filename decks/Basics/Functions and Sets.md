---
title: "Basics::Functions and Sets"
---

::: {.front card-id="card-44cb3f71b3da138c" tags="definition"}
Functional characterization of injective functions.
:::

::: {.back card-id="card-44cb3f71b3da138c"}
$$
f(x) = f(y) \implies x=y \iff f \text{ has a left inverse.}
.$$
:::

::: {.front card-id="card-0e941ec5ea10f983" tags="definition"}
Functional characterization of surjective functions.
:::

::: {.back card-id="card-0e941ec5ea10f983"}
$$
\forall y, \exists X \text{ such that } f(x) = y \iff f\text{ has a right inverse, } \exists g \text{ such that } f(g(y)) = y\, \forall y
.$$
:::

::: {.front card-id="card-bbc70498dfc1b62d" tags="misc"}
$f^{-1} \left( \coprod U_i \right) =_? \coprod_i f^{-1} U_i$?
:::

::: {.back card-id="card-bbc70498dfc1b62d"}
Yes:
$$
\begin{align}
f^{-1}\left[\bigcup_{i \in I} Y_{i}\right] &=\left\{x \in X \mid f(x) \in \bigcup_{i \in I} Y_{i}\right\} \\
&=\left\{x \in X \mid \exists i \in I \text { such that } f(x) \in Y_{i}\right\} \\
&=\bigcup_{i \in I}\left\{x \in X \mid f(x) \in Y_{i}\right\} \\
&=\bigcup_{i \in I} f^{-1}\left[Y_{i}\right]
\end{align}
$$
:::

::: {.front card-id="card-4e3e938b00ff3359" tags="misc"}
$f^{-1} \left( \bigcap U_i \right) =_? \bigcap_i f^{-1} U_i$?
:::

::: {.back card-id="card-4e3e938b00ff3359"}
Yes
:::

::: {.front card-id="card-f24d683913c1e5a1" tags="misc"}
True or false: $X =_? (f^{-1} \circ f)(X)$
:::

::: {.back card-id="card-f24d683913c1e5a1"}
Only when $f$ is injective, otherwise just $\subseteq$.
:::

::: {.front card-id="card-f0af314ba0599d9d" tags="misc"}
True or false: $X =_? (f\circ f^{-1})(X)$
:::

::: {.back card-id="card-f0af314ba0599d9d"}
Only when $f$ is surjective, otherwise just $\subseteq$.
:::

::: {.front card-id="card-8b225a8506b564ad" tags="misc"}
True or false: $f^{-1}(A) \setminus f^{-1}(B) =_? f^{-1}(A\setminus B)$
:::

::: {.back card-id="card-8b225a8506b564ad"}
Yes.
For forward direction, only an inclusion.
:::

::: {.front card-id="card-3929386b1324c8e9" tags="unsorted"}
What inverses exist for injective (resp. surjective) functions?
:::

::: {.back card-id="card-3929386b1324c8e9"}
- Injections: left inverses, i.e. $f(x) = f(y) \implies x=y$
- Surjections: right inverses
:::

::: {.front card-id="card-f11cf8eae16c4395" tags="misc"}
$f^{-1} \left( \coprod U_i \right) =_? \coprod_i f^{-1} U_i$?
:::

::: {.back card-id="card-f11cf8eae16c4395"}
Yes:
$$
\begin{align}
f^{-1}\left[\bigcup_{i \in I} Y_{i}\right] &=\left\{x \in X \mid f(x) \in \bigcup_{i \in I} Y_{i}\right\} \\
&=\left\{x \in \lambda \mid \quad \exists i \in I \text { such that } f(x) \in Y_{i}\right\} \\
&=\bigcup_{i \in I}\left\{x \in X \mid f(x) \in Y_{i}\right\} \\
&=\bigcup_{i \in I} f^{-1}\left[Y_{i}\right]
\end{align}
$$
:::

::: {.front card-id="card-9dd80decbe8075b1" tags="misc"}
$X =_? (f^{-1} \circ f)(X)$
:::

::: {.back card-id="card-9dd80decbe8075b1"}
Only when $f$ is injective, otherwise just $\subseteq$.
:::

::: {.front card-id="card-82657fed9f8ead27" tags="misc"}
$X =_? (f\circ f^{-1})(X)$
:::

::: {.back card-id="card-82657fed9f8ead27"}
Only when $f$ is surjective, otherwise just $\subseteq$.
:::

::: {.front card-id="card-ba2adb60698e1060" tags="misc"}
$f^{-1}(A) \setminus f^{-1}(B) =_? f^{-1}(A\setminus B)$
:::

::: {.back card-id="card-ba2adb60698e1060"}
Yes.
For forward direction, only an inclusion.
:::

::: {.front card-id="card-80afbd28f63b7e96"}
$f^{-1} \left( \bigcup_i U_i \right) =_? \bigcup_i f^{-1}(U_i)$?
:::

::: {.back card-id="card-80afbd28f63b7e96"}
True.
$$\begin{aligned} f^{-1}\left[\bigcup_{i \in I} Y_i\right] & =\left\{x \in X \mathrel{\Big|}f(x) \in \bigcup_{i \in I} Y_i\right\} \\ & =\left\{x \in \lambda \mathrel{\Big|}\quad \exists i \in I \text { such that } f(x) \in Y_i\right\} \\ & =\bigcup_{i \in I}\left\{x \in X \mathrel{\Big|}f(x) \in Y_i\right\} \\ & =\bigcup_{i \in I} f^{-1}\left[Y_i\right] \end{aligned}$$
:::
