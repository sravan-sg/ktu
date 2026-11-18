# Circle Generation Algorithms: Midpoint Circle and Bresenham's Algorithm

## 1. Explanation

A circle is defined as the locus of all points equidistant from a center point $(x_c, y_c)$ at radius $r$:
$$(x - x_c)^2 + (y - y_c)^2 = r^2$$

### Why Not Use the Direct Formula?

**Explicit form** $y = y_c \pm \sqrt{r^2 - (x-x_c)^2}$:
- Requires a square-root per pixel — extremely expensive (dozens of CPU cycles).
- Near vertical tangent ($x \approx x_c \pm r$), pixel spacing becomes non-uniform (large gaps appear in the rasterized circle).

**Polar form** $x = x_c + r\cos\theta$, $y = y_c + r\sin\theta$:
- Requires `cos()` and `sin()` per pixel — transcendental functions are even slower than `sqrt()`.
- Equal angular steps $\Delta\theta$ produce non-uniform arc-length steps (crowded near horizontal, sparse near diagonal).

**Solution**: Use an **incremental decision-parameter algorithm** that exploits the implicit circle equation and 8-way symmetry to generate all circle pixels using only integer arithmetic.

---

### The Eight-Way Symmetry Principle

A circle centered at the origin satisfies $x^2 + y^2 = r^2$. This equation is **symmetric** under:
- Sign inversion of $x$: $(x,y) \leftrightarrow (-x,y)$ [Y-axis reflection]
- Sign inversion of $y$: $(x,y) \leftrightarrow (x,-y)$ [X-axis reflection]
- Coordinate swap: $(x,y) \leftrightarrow (y,x)$ [line $y=x$ reflection]

Combined, these generate 8 symmetric points from any single point $(x, y)$ in the first octant:

| Octant | Point | Derivation |
|---|---|---|
| 1 (original) | $(x, y)$ | Computed directly |
| 2 | $(y, x)$ | Swap coordinates |
| 3 | $(-y, x)$ | Swap + negate $x$ |
| 4 | $(-x, y)$ | Negate $x$ |
| 5 | $(-x, -y)$ | Negate both |
| 6 | $(-y, -x)$ | Swap + negate both |
| 7 | $(y, -x)$ | Swap + negate $y$ |
| 8 | $(x, -y)$ | Negate $y$ |

**Key benefit**: Compute pixels only in the first octant (from $\theta = 90°$ to $45°$, i.e., $x: 0 \to r/\sqrt{2}$) — this gives only about $r/\sqrt{2}$ steps instead of $2\pi r$ steps, while producing all $\approx 8 \times r/\sqrt{2} \approx 2\pi r/\sqrt{2} \approx 4.44r$ circle pixels. Efficiency gain: **8× fewer computations**.

For a circle centered at $(x_c, y_c)$, translate each $(x,y)$ pair: plot all 8 symmetric points as $(x + x_c, y + y_c)$.

---

### Midpoint Circle Algorithm

#### Implicit Circle Function

Define:
$$f_{\text{circle}}(x, y) = x^2 + y^2 - r^2$$

- $f < 0$: Point is **inside** the circle
- $f = 0$: Point is **on** the circle  
- $f > 0$: Point is **outside** the circle

#### First Octant Setup

Start at the topmost pixel $(x_0, y_0) = (0, r)$. In the first octant, moving from $\theta = 90°$ down to $\theta = 45°$:
- $x$ increases by 1 each step
- $y$ either stays the same or decreases by 1
- Two candidate pixels at step $k$: **East** $E(x_k+1, y_k)$ or **South-East** $SE(x_k+1, y_k-1)$

The **midpoint** between these two candidates is:
$$M = \left(x_k + 1,\ y_k - \frac{1}{2}\right)$$

**Decision parameter** = circle function at midpoint:
$$p_k = f_{\text{circle}}\!\left(x_k + 1,\ y_k - \tfrac{1}{2}\right) = (x_k+1)^2 + \left(y_k - \tfrac{1}{2}\right)^2 - r^2$$

**Decision rules:**
- $p_k < 0$: Midpoint is **inside** → circle boundary is closer to E → choose **East pixel $(x_k+1, y_k)$**
- $p_k \ge 0$: Midpoint is **outside** → circle boundary is closer to SE → choose **South-East pixel $(x_k+1, y_k-1)$**

#### Recurrence Relations (Incremental Update)

Expanding $p_{k+1} - p_k$:

$$p_{k+1} = \left[(x_k+1)+1\right]^2 + \left(y_{k+1} - \tfrac{1}{2}\right)^2 - r^2$$

**Case 1 — $p_k < 0$ (chose East: $y_{k+1} = y_k$):**
$$p_{k+1} - p_k = (x_k+2)^2 - (x_k+1)^2 = 2x_k + 3 = 2x_{k+1} + 1$$
$$\boxed{p_{k+1} = p_k + 2x_{k+1} + 1}$$

**Case 2 — $p_k \ge 0$ (chose South-East: $y_{k+1} = y_k - 1$):**
$$p_{k+1} - p_k = 2x_k + 3 + (y_k - 1)^2 - y_k^2 - \left[(y_k-1) - y_k\right]$$
$$= 2x_k + 3 + (-2y_k + 1) - (-1) = 2x_k - 2y_k + 5$$
$$\boxed{p_{k+1} = p_k + 2(x_{k+1} - y_{k+1}) + 1}$$

(where $x_{k+1} = x_k+1$, $y_{k+1} = y_k-1$)

#### Initial Decision Parameter Derivation

Evaluate at starting point $(x_0, y_0) = (0, r)$, checking midpoint $(1, r - \frac{1}{2})$:
$$p_0 = 1^2 + \left(r - \tfrac{1}{2}\right)^2 - r^2 = 1 + r^2 - r + \tfrac{1}{4} - r^2 = \tfrac{5}{4} - r$$

Since we work with integers and $\lfloor 5/4 \rfloor = 1$:
$$\boxed{p_0 = 1 - r}$$

(The $\frac{1}{4}$ fractional part does not affect the sign decisions for integer $r$.)

#### Termination Condition

Stop when $x > y$ (we've passed the 45° boundary between octants 1 and 2). At this point, the symmetry-generated points would start overlapping.

#### Complete Pseudocode

```c
void MidpointCircle(int xc, int yc, int r) {
    int x = 0, y = r;
    int p = 1 - r;  // initial decision parameter

    // Plot all 8 symmetric points of starting position
    PlotCirclePoints(xc, yc, x, y);

    while (x < y) {
        x++;
        if (p < 0) {
            // East pixel chosen: y stays same
            p = p + 2*x + 1;
        } else {
            // South-East pixel chosen: y decreases
            y--;
            p = p + 2*(x - y) + 1;
        }
        PlotCirclePoints(xc, yc, x, y);
    }
}

void PlotCirclePoints(int xc, int yc, int x, int y) {
    // 8 symmetric pixels
    SetPixel(xc+x, yc+y);  SetPixel(xc-x, yc+y);
    SetPixel(xc+x, yc-y);  SetPixel(xc-x, yc-y);
    SetPixel(xc+y, yc+x);  SetPixel(xc-y, yc+x);
    SetPixel(xc+y, yc-x);  SetPixel(xc-y, yc-x);
}
```

**Time complexity**: $O(r)$ — only $r/\sqrt{2}$ iterations, each $O(1)$ integer operations.  
**Space complexity**: $O(1)$ — only 3 integer variables needed.

---

## 2. Example: Decision Geometry in First Octant

```
         (0, r)   ← Start here
            *
          * * * ← y stays same (p < 0 region, E chosen)
        *       *
       *    M=midpoint between E and SE
      *            *
     *               *
    *                 *
(r, 0) ← Would reach here (but we stop at x=y, 45° line)
```

**Decision geometry at step $k$:**
```
y_k   : ---- E = (x_k+1, y_k)
         M = (x_k+1, y_k - 0.5)   ← test midpoint
y_k-1 : ---- SE = (x_k+1, y_k-1)

p_k = f_circle(M):
  < 0 → M inside circle → circle boundary above M → E is closer → choose E
  ≥ 0 → M outside/on circle → circle boundary below M → SE is closer → choose SE
```

---

## 3. Applications & Use Cases

1. **GPU Primitive Rasterization**: Modern GPUs use midpoint-style decision tests (implemented as fixed-function hardware) to rasterize circles, ellipses, and arc primitives in 2D graphics APIs (`DrawCircle` in DirectX, `arc()` in HTML5 Canvas).

2. **Digital Radar and Sonar**: Radar PPI (Plan Position Indicator) displays render range rings at fixed distances. These rings are circles centered at the radar location; midpoint circle rasterization generates them in $O(r)$ time without transcendental functions.

3. **Font Rendering (Hinting)**: TrueType and OpenType fonts contain quadratic/cubic Bézier curves. For small point sizes where curves approximate circular arcs, font renderers (FreeType) fall back to midpoint circle algorithms for specific glyph curves.

4. **Medical Imaging (ROI Tools)**: In ultrasound and mammography software, radiologists draw circular regions of interest (ROIs) around lesions. The boundary pixels are generated by the midpoint circle algorithm and used as masks for quantitative analysis (mean intensity, texture features).

5. **Game Engine Collision Detection**: 2D game engines represent circular hitboxes/colliders. The pixel outline of a circle hitbox is rasterized using the midpoint algorithm for debug visualization overlays in developer mode.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Midpoint Circle — Radius $r = 5$, Center $(5, 10)$ [KTU Dec 2023 — 9 Marks]

**Setup:** $r = 5$, center $(x_c, y_c) = (5, 10)$. Compute relative to origin, then shift.

$$p_0 = 1 - r = 1 - 5 = -4$$

Starting point: $(x, y) = (0, 5)$. Termination when $x > y$.

| Step | $p_k$ | Condition | Chosen Pixel (relative) | $p_{k+1}$ |
|---|---|---|---|---|
| Start | — | — | **(0, 5)** | $p_0 = -4$ |
| 1 | $-4$ | $< 0$ → E | **(1, 5)** | $-4 + 2(1)+1 = -1$ |
| 2 | $-1$ | $< 0$ → E | **(2, 5)** | $-1 + 2(2)+1 = 4$ |
| 3 | $4$ | $\ge 0$ → SE | **(3, 4)** | $4 + 2(3-4)+1 = 3$ |
| 4 | $3$ | $\ge 0$ → SE | **(4, 3)** | $3 + 2(4-3)+1 = 6$ |
| Terminate | | $x=4 < y=3$? No, $4 > 3$ | Stop |

Wait — termination is at $x > y$, so we stop after plotting $(4, 3)$ since now $x=4 > y=3$.

**All relative points in first octant**: $(0,5), (1,5), (2,5), (3,4), (4,3)$

**Translate by center $(5, 10)$** and plot all 8 symmetric points for each:

For $(0, 5)$ relative → actual 8 points:
$(5+0, 10+5)=(5,15)$, $(5-0, 10+5)=(5,15)$ [same], $(5+5, 10+0)=(10,10)$, $(5-5, 10+0)=(0,10)$, etc.

For $(3, 4)$ relative → actual 8 points:
$(8,14), (2,14), (8,6), (2,6), (9,13), (1,13), (9,7), (1,7)$

---

### Example 2: Midpoint Circle — Radius $r = 10$, Center $(20, 10)$ [KTU Dec 2021, Dec 2019 — 9 Marks]

**Setup:** $r = 10$, center $(20, 10)$.

$$p_0 = 1 - 10 = -9, \quad \text{Start: } (0, 10)$$

| Step | $p_k$ | Condition | Relative Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| Start | — | — | (0, 10) | $-9$ |
| 1 | $-9$ | $< 0$ → E | (1, 10) | $-9+2+1=-6$ |
| 2 | $-6$ | $< 0$ → E | (2, 10) | $-6+4+1=-1$ |
| 3 | $-1$ | $< 0$ → E | (3, 10) | $-1+6+1=6$ |
| 4 | $6$ | $\ge 0$ → SE | (4, 9) | $6+2(4-9)+1=6-10+1=-3$ |
| 5 | $-3$ | $< 0$ → E | (5, 9) | $-3+10+1=8$ |
| 6 | $8$ | $\ge 0$ → SE | (6, 8) | $8+2(6-8)+1=8-4+1=5$ |
| 7 | $5$ | $\ge 0$ → SE | (7, 7) | $5+2(7-7)+1=6$ |
| Terminate | | $x=7 = y=7$ then $x>y$ next | Stop |

**Relative first-octant pixels**: $(0,10), (1,10), (2,10), (3,10), (4,9), (5,9), (6,8), (7,7)$

**Translate by $(20, 10)$**: $(20,20), (21,20), (22,20), (23,20), (24,19), (25,19), (26,18), (27,17)$

---

### Example 3: Derivation of Initial Decision Parameter [KTU June 2022, Dec 2020 — 5 Marks]

**Problem**: Derive the initial decision parameter used in the Midpoint Circle drawing algorithm from first principles.

**Derivation**:

**Step 1**: Start at the topmost pixel of the circle $(0, r)$ (where the circle intersects the positive $y$-axis).

**Step 2**: The next pixel will be at $x = 1$. The two candidates are $E = (1, r)$ and $SE = (1, r-1)$. The midpoint between them is $M = (1, r - \frac{1}{2})$.

**Step 3**: The decision parameter $p_0$ is the circle function evaluated at this midpoint:
$$p_0 = f_{\text{circle}}\!\left(1, r - \tfrac{1}{2}\right) = (1)^2 + \left(r - \tfrac{1}{2}\right)^2 - r^2$$

**Step 4**: Expand:
$$= 1 + r^2 - r + \frac{1}{4} - r^2 = 1 - r + \frac{1}{4} = \frac{5}{4} - r$$

**Step 5**: Since $r$ is an integer and all subsequent increments to $p_k$ are integers (see recurrence: $+2x+1$ or $+2(x-y)+1$), the fractional $\frac{1}{4}$ never affects sign decisions. Therefore we use the rounded integer form:

$$\boxed{p_0 = 1 - r}$$

**Interpretation**: For a large circle ($r \gg 1$), $p_0 = 1 - r < 0$, meaning the starting midpoint $(1, r-\frac{1}{2})$ is inside the circle, so the East pixel $(1, r)$ is selected initially — the circle boundary hugs the top pixel and descends gradually.

---

## 5. Previous Year Questions & Solutions

### Q1 [KTU Dec 2023 — 9 Marks]
**Question**: Write the midpoint circle drawing algorithm. Use midpoint circle drawing algorithm to plot a circle whose radius = 5 units and centre at (5, 10).

**Solution**:

**Algorithm**:
```
Input: Circle center (xc, yc) and radius r
Output: Raster pixels on the circle

1. Set x = 0, y = r
2. Compute p₀ = 1 - r
3. Plot all 8 symmetric points of (xc, yc, x, y)
4. While (x < y):
   a. x = x + 1
   b. If p < 0:
         p = p + 2x + 1   [E pixel chosen: y unchanged]
      Else:
         y = y - 1
         p = p + 2(x - y) + 1  [SE pixel chosen: y decremented]
   c. Plot all 8 symmetric points of (xc, yc, x, y)
5. Stop
```

**Trace for r=5, center=(5,10)**: (computed relative to origin, then translate by (5,10))

$p_0 = 1 - 5 = -4$, Start: $(0, 5)$

| $k$ | $p_k$ | Pixel (relative) | $p_{k+1}$ |
|---|---|---|---|
| 0 | $-4$ | (0, 5) start | — |
| 1 | $-4$ | (1, 5) [E] | $-4+2(1)+1=-1$ |
| 2 | $-1$ | (2, 5) [E] | $-1+2(2)+1=4$ |
| 3 | $4$ | (3, 4) [SE] | $4+2(3-4)+1=3$ |
| 4 | $3$ | (4, 3) [SE] | — stop ($x>y$?) $4>3$ → Yes, stop |

**Relative points**: $(0,5),(1,5),(2,5),(3,4),(4,3)$

Translated (add $xc=5, yc=10$) sample points with 8-way symmetry shown for $(3,4)$:
$(3+5, 4+10)=(8,14)$, $(-3+5, 4+10)=(2,14)$, $(3+5, -4+10)=(8,6)$, $(-3+5,-4+10)=(2,6)$, $(4+5, 3+10)=(9,13)$, $(-4+5, 3+10)=(1,13)$, $(4+5,-3+10)=(9,7)$, $(-4+5,-3+10)=(1,7)$

---

### Q2 [KTU Jan 2023 — 9 Marks]
**Question**: Write the steps of midpoint circle drawing algorithm.

**Solution**:

**Midpoint Circle Algorithm — Step-by-Step**:

**Inputs**: Center $(x_c, y_c)$, integer radius $r$  
**Outputs**: All integer pixel coordinates on the circle

**Step 1**: Initialize variables:
- Set $x = 0$, $y = r$ (topmost point of circle)
- Compute initial decision parameter: $p = 1 - r$

**Step 2**: Plot 8 symmetric pixels centered at $(x_c, y_c)$:
```
(xc+x, yc+y), (xc-x, yc+y), (xc+x, yc-y), (xc-x, yc-y)
(xc+y, yc+x), (xc-y, yc+x), (xc+y, yc-x), (xc-y, yc-x)
```

**Step 3**: Check loop condition: while $x < y$:

**Step 4**: Increment $x$: $x = x + 1$

**Step 5**: Update decision parameter:
- If $p < 0$ (midpoint inside circle): $p = p + 2x + 1$; $y$ unchanged
- If $p \ge 0$ (midpoint outside circle): $y = y - 1$; $p = p + 2(x - y) + 1$

**Step 6**: Plot 8 symmetric pixels for new $(x, y)$

**Step 7**: Return to Step 3

**Step 8**: Stop when $x \ge y$

**Key Properties**:
- Uses only integer arithmetic (addition only — no multiplication or division in the loop)
- Each iteration produces 8 circle pixels at zero extra cost
- Time complexity: $O(r)$; Space complexity: $O(1)$

---

### Q3 [KTU Dec 2020 — 4 Marks]
**Question**: Generate 4 pixel positions of a circle in the first quadrant with radius $r = 10$ centered on the origin, using the midpoint circle algorithm.

**Solution**:

$p_0 = 1 - 10 = -9$. Start at $(0, 10)$.

| $k$ | $p_k$ | Decision | Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| 0 | $-9$ | $< 0$ → E | **(1, 10)** | $-9+2(1)+1=-6$ |
| 1 | $-6$ | $< 0$ → E | **(2, 10)** | $-6+2(2)+1=-1$ |
| 2 | $-1$ | $< 0$ → E | **(3, 10)** | $-1+2(3)+1=6$ |
| 3 | $6$ | $\ge 0$ → SE | **(4, 9)** | $6+2(4-9)+1=-3$ |

**4 Generated First-Quadrant Pixel Positions** (starting from $(0,10)$): **(0,10), (1,10), (2,10), (3,10), (4,9)**

---

### Q4 [KTU May 2019, Dec 2018 — 9 Marks]
**Question**: Use midpoint circle drawing algorithm to plot a circle whose radius = 20 units and center is (50, 30).

**Solution**:

$r = 20$, center $(50, 30)$. $p_0 = 1 - 20 = -19$. Start at $(0, 20)$.

| $k$ | $p_k$ | Decision | Relative Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| 0 | $-19$ | $< 0$ | (1, 20) | $-16$ |
| 1 | $-16$ | $< 0$ | (2, 20) | $-9$ |
| 2 | $-9$ | $< 0$ | (3, 20) | $2$ |
| 3 | $2$ | $\ge 0$ | (4, 19) | $2+2(4-19)+1=-27$ |

Wait — recalculate: $p_{k+1} = p_k + 2(x_{k+1} - y_{k+1}) + 1 = 2 + 2(4-19) + 1 = 2 - 30 + 1 = -27$

| 4 | $-27$ | $< 0$ | (5, 19) | $-27+2(5)+1=-16$ |
| 5 | $-16$ | $< 0$ | (6, 19) | $-16+2(6)+1=-3$ |
| 6 | $-3$ | $< 0$ | (7, 19) | $-3+2(7)+1=12$ |
| 7 | $12$ | $\ge 0$ | (8, 18) | $12+2(8-18)+1=-7$ |
| 8 | $-7$ | $< 0$ | (9, 18) | $-7+2(9)+1=12$ |
| 9 | $12$ | $\ge 0$ | (10, 17) | $12+2(10-17)+1=-1$ |
| 10 | $-1$ | $< 0$ | (11, 17) | $-1+2(11)+1=22$ |
| 11 | $22$ | $\ge 0$ | (12, 16) | $22+2(12-16)+1=15$ |
| 12 | $15$ | $\ge 0$ | (13, 15) | $15+2(13-15)+1=12$ |
| 13 | $12$ | $\ge 0$ | (14, 14) | stop: $x=14=y$ |

**Relative first-octant pixels**: $(0,20),(1,20),(2,20),(3,20),(4,19),(5,19),(6,19),(7,19),(8,18),(9,18),(10,17),(11,17),(12,16),(13,15),(14,14)$

Add center $(50, 30)$ to each. Sample translated pixel: $(0+50, 20+30) = (50, 50)$; $(14+50, 14+30) = (64, 44)$.

---

### Q5 [KTU June 2024 — 4 Marks]
**Question**: How 8-way symmetry of a circle can be used for writing circle drawing algorithms? Write the symmetric points if $(x, y)$ is a point on the circle with centre at origin.

**Solution**:

**How 8-way symmetry is used**:

The circle equation $x^2 + y^2 = r^2$ is completely invariant under:
1. Replacing $x$ with $-x$ (Y-axis symmetry)
2. Replacing $y$ with $-y$ (X-axis symmetry)
3. Swapping $x$ and $y$ (diagonal $y=x$ symmetry)

Combined, these generate 8 equal octants. If we compute pixels only in Octant 1 ($0 \le x \le y$), we can reflect each computed pixel $(x, y)$ to get 7 more pixels without any computation.

This reduces the number of algorithm iterations from $\approx 2\pi r$ (full circle) to $\approx \frac{\pi r}{4\sqrt{2}} \approx r/\sqrt{2}$ (one octant) — an **8× speedup**.

**The 8 symmetric points** for a point $(x, y)$ on a circle with center at origin:
$$\boxed{(x, y),\ (y, x),\ (-x, y),\ (-y, x),\ (-x, -y),\ (-y, -x),\ (x, -y),\ (y, -x)}$$

For center $(x_c, y_c)$, translate each point by adding $(x_c, y_c)$.
