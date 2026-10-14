---
title: "Analysis::Complex Analysis::Conformal Maps"
---

::: {.front card-id="card-8f650043a174ec60" tags="definition"}
Conformal map: $\HH\to \DD$
:::

::: {.back card-id="card-8f650043a174ec60"}
$w=(z-i)/(z+i)$ maps the upper half-plane $\mathbb H$ biholomorphically onto the unit disc $\mathbb D$; $i\mapsto0$ and the real axis maps to the unit circle.
:::

::: {.front card-id="card-4907d3a3dc6d8806" tags="definition"}
Conformal map: right-half-plane to $\DD$
:::

::: {.back card-id="card-4907d3a3dc6d8806"}
$w=(z-1)/(z+1)$ maps $\{\operatorname{Re}z>0\}$ biholomorphically onto $\mathbb D$; $1\mapsto0$ and the imaginary axis maps to the unit circle.
:::

::: {.front card-id="card-56fad98534b35cc5" tags="definition"}
Conformal map: image of a region under the exponential map
:::

::: {.back card-id="card-56fad98534b35cc5"}
Write $z=x+iy$. Then $e^z=e^x e^{iy}$: vertical lines $x=c$ map to circles $|w|=e^c$, and horizontal lines $y=c$ map to rays of argument $c$ (mod $2\pi$). Thus a horizontal strip of height less than $2\pi$ maps injectively to an angular sector.
:::

::: {.front card-id="card-412951010185d47d" tags="definition"}
Conformal map: strip to half-plane
:::

::: {.back card-id="card-412951010185d47d"}
$z\mapsto e^{\pi z/b}$ maps the horizontal strip $0<\operatorname{Im}z<b$ biholomorphically onto $\mathbb H$: its argument ranges over $(0,\pi)$.
:::

::: {.front card-id="card-d0cd68c2d4ae8a2d" tags="definition"}
Conformal map: $\CC \sm (-\infty ,0]$ to a horizontal strip
:::

::: {.back card-id="card-d0cd68c2d4ae8a2d"}
The principal logarithm $z\mapsto\Log z$ maps the slit plane $\CC\sm(-\infty,0]$ biholomorphically onto the horizontal strip $\theset{w : -\pi<\operatorname{Im}w<\pi}$. It restricts to a biholomorphism of $\mathbb H$ onto $\theset{w : 0<\operatorname{Im}w<\pi}$.
:::

::: {.front card-id="card-b6ff03aaf0820e35" tags="definition"}
Conformal map: what does $z+\inverseof{a}$ do?
:::

::: {.back card-id="card-b6ff03aaf0820e35"}
For $a\ne0$, $z\mapsto z+a^{-1}$ is a translation by $1/a$. It moves every point and the whole region by the same vector; it preserves angles and distances.
:::

::: {.front card-id="card-595105d101b34f0b" tags="definition"}
Conformal map: upper half-disc to $\HH$
:::

::: {.back card-id="card-595105d101b34f0b"}
$w=-(z+z^{-1})$ maps $\{z:|z|<1,\ \operatorname{Im}z>0\}$ biholomorphically onto $\mathbb H$. Indeed, $\operatorname{Im}w=\operatorname{Im}z\,(|z|^{-2}-1)>0$; its boundary maps to $\mathbb R$.
:::
