---
title: "Grad Math Facts::Grad Math Facts"
---

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
True or false: $ X =_? (f^{-1} \circ f)(X) $
:::

::: {.back card-id="card-f24d683913c1e5a1"}
Only when $f$ is injective, otherwise just $ \subseteq $.
:::

::: {.front card-id="card-f0af314ba0599d9d" tags="misc"}
True or false: $ X =_? (f\circ f^{-1})(X) $
:::

::: {.back card-id="card-f0af314ba0599d9d"}
Only when $f$ is surjective, otherwise just $ \subseteq $.
:::

::: {.front card-id="card-8b225a8506b564ad" tags="misc"}
True or false: $ f^{-1}(A) \setminus f^{-1}(B) =_? f^{-1}(A\setminus B) $
:::

::: {.back card-id="card-8b225a8506b564ad"}
Yes.
For forward direction, only an inclusion.
:::

::: {.front card-id="card-efc49202ba80c5d4" tags="unsorted"}
True or false: $ \log(a-b) = \log(a) / \log(b) $
:::

::: {.back card-id="card-efc49202ba80c5d4"}
False: take $b=1$, this would force dividing by zero.
:::

::: {.front card-id="card-c34ff24d2266b166" tags="unsorted"}
True or false: $ \log(a+b) = \log(a) + \log(b) $
:::

::: {.back card-id="card-c34ff24d2266b166"}
False
:::

::: {.front card-id="card-3a469b2ce4fc9251" tags="unsorted"}
True or false: $ \log(a+b) = \log(a) \log(b) $
:::

::: {.back card-id="card-3a469b2ce4fc9251"}
False
:::

::: {.front card-id="card-0fd9e0a82ce28c1b" tags="unsorted"}
Write $ \log $ as a group homomorphism. What are the domain and codomain?
:::

::: {.back card-id="card-0fd9e0a82ce28c1b"}
$$
\log: \GG_m(\RR) \to \GG_a(\RR) 
.$$
:::

::: {.front card-id="card-ff56ab1fbdbb17c2" tags="unsorted"}
Write $ \exp $  as a group homomorphism.
:::

::: {.back card-id="card-ff56ab1fbdbb17c2"}
$$
\exp: \GG_a(\RR) \to \GG_m(\RR) 
.$$
:::

::: {.front card-id="card-3929386b1324c8e9" tags="unsorted"}
What inverses exist for injective (resp. surjective) functions?
:::

::: {.back card-id="card-3929386b1324c8e9"}
- Injections: left inverses, i.e. $f(x) = f(y) \implies x=y$
- Surjections: right inverses
:::
