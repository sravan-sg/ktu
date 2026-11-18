# Line Drawing Algorithms: DDA and Bresenham's Algorithm

## 1. Explanation

Line drawing — formally called **scan-conversion of a line segment** — is the fundamental problem of determining which discrete integer pixel coordinates $(x_i, y_i)$ on a raster display best approximate a continuous mathematical line from endpoint $(x_0, y_0)$ to $(x_n, y_n)$.

### Why This Problem Is Non-Trivial

A continuous mathematical line contains uncountably infinite points. A display screen is a discrete lattice of integer-coordinate pixels. The scan-conversion algorithm must:
1. **Be geometrically accurate**: Selected pixels must lie as close as possible to the true line.
2. **Be computationally efficient**: For a 4K display (3840×2160), millions of pixels must be rasterized per frame at 60+ Hz — the algorithm must run in nanoseconds per pixel.
3. **Produce uniform visual brightness**: Gaps or clustering of pixels must be avoided.
4. **Handle all slopes**: Positive, negative, steep, shallow, horizontal, and vertical lines.

### Coordinate Conventions

Given endpoints $(x_0, y_0)$ and $(x_n, y_n)$, define:
$$\Delta x = x_n - x_0, \qquad \Delta y = y_n - y_0, \qquad m = \frac{\Delta y}{\Delta x}$$

---

## Digital Differential Analyzer (DDA) Algorithm

### Mathematical Basis

The DDA is an **incremental** algorithm that samples the line equation $y = mx + c$ at unit intervals.

**Case 1: $|m| \le 1$ (gentle slope — x-dominant)**
- Step $x$ by $+1$ each iteration.
- Compute: $y_{k+1} = y_k + m$
- Plot pixel at $\bigl(x_{k+1},\ \text{round}(y_{k+1})\bigr)$.

**Case 2: $|m| > 1$ (steep slope — y-dominant)**
- Step $y$ by $+1$ each iteration (to avoid pixel gaps along y-axis).
- Compute: $x_{k+1} = x_k + \frac{1}{m}$
- Plot pixel at $\bigl(\text{round}(x_{k+1}),\ y_{k+1}\bigr)$.

**Case 3: Negative slopes**
- If $\Delta x < 0$: reverse endpoint order, or use $\Delta x = -1$ and negate increment direction.

**Case 4: Special cases**
- **Horizontal** ($m = 0$): Only $x$ increments, $y$ stays constant.
- **Vertical** ($\Delta x = 0$): Only $y$ increments; $m = \infty$ so use Case 2 with $x$ fixed.
- **45° line** ($|m| = 1$): Both $x$ and $y$ increment by 1 each step.

### DDA Pseudocode
```c
void DrawLineDDA(float x0, float y0, float x1, float y1) {
    float dx = x1 - x0;
    float dy = y1 - y0;
    int steps = (int)(fabs(dx) >= fabs(dy) ? fabs(dx) : fabs(dy));

    float xInc = dx / steps;   // increment per step
    float yInc = dy / steps;

    float x = x0;
    float y = y0;

    for (int k = 0; k <= steps; k++) {
        PlotPixel((int)round(x), (int)round(y));  // round() = floating-point required
        x += xInc;
        y += yInc;
    }
}
```

### Limitations of DDA

| Limitation | Technical Explanation |
|---|---|
| **Floating-point arithmetic** | Each step requires a floating-point addition — slow on early hardware without FPUs |
| **Rounding errors accumulate** | After many steps, fractional drift in `y` causes pixels to shift off the true line |
| **Round() overhead** | The `round()` call adds latency per pixel |
| **Not hardware-friendly** | Integer-only hardware cannot execute DDA efficiently |

---

## Bresenham's Line Drawing Algorithm

### Historical Context
Jack E. Bresenham developed this algorithm in 1962 at IBM for use on digital plotters. Its genius lies in replacing all floating-point operations with **pure integer arithmetic**: additions, subtractions, and left-bit-shifts ($\times 2$).

### Derivation for $0 < m < 1$ (Octant 1)

At step $k$, we have just plotted pixel $(x_k, y_k)$. The next pixel has $x_{k+1} = x_k + 1$. The two candidates are:
- **East pixel** $E = (x_k + 1, y_k)$ — same row
- **North-East pixel** $NE = (x_k + 1, y_k + 1)$ — one row up

The true mathematical $y$-value at $x = x_k + 1$ is:
$$y_{\text{true}} = m(x_k + 1) + c$$

Define the vertical distances:
$$d_1 = y_{\text{true}} - y_k = m(x_k + 1) + c - y_k \qquad (\text{distance to lower pixel})$$
$$d_2 = (y_k + 1) - y_{\text{true}} = y_k + 1 - m(x_k + 1) - c \qquad (\text{distance to upper pixel})$$

**Decision rule**: Choose the pixel closer to the true line:
- If $d_1 < d_2 \implies$ line is below midpoint $\implies$ choose $E$ (East)
- If $d_1 \ge d_2 \implies$ line is above or at midpoint $\implies$ choose $NE$ (North-East)

**Equivalent condition** via sign of $d_1 - d_2$:
$$d_1 - d_2 = 2m(x_k + 1) + 2c - 2y_k - 1$$

Multiply both sides by $\Delta x$ (always positive for $0 < m < 1$) to clear the fraction $m = \frac{\Delta y}{\Delta x}$:

$$\underbrace{\Delta x (d_1 - d_2)}_{p_k} = 2\Delta y(x_k + 1) + \Delta x(2c - 1) - 2\Delta x \cdot y_k$$

Since the constant $C = 2\Delta y + \Delta x(2c - 1)$ is independent of $k$:
$$\boxed{p_k = 2\Delta y \cdot x_k - 2\Delta x \cdot y_k + C}$$

**Decision using $p_k$**:
- $p_k < 0 \implies d_1 < d_2 \implies$ Select East pixel $(x_k+1, y_k)$
- $p_k \ge 0 \implies d_1 \ge d_2 \implies$ Select NE pixel $(x_k+1, y_k+1)$

### Incremental Recurrence

Compute $p_{k+1}$ from $p_k$ without recomputing from scratch:
$$p_{k+1} = p_k + 2\Delta y - 2\Delta x(y_{k+1} - y_k)$$

- **If $p_k < 0$**: $y_{k+1} = y_k$ (East pixel chosen), so $y_{k+1} - y_k = 0$:
$$\boxed{p_{k+1} = p_k + 2\Delta y}$$

- **If $p_k \ge 0$**: $y_{k+1} = y_k + 1$ (NE pixel chosen), so $y_{k+1} - y_k = 1$:
$$\boxed{p_{k+1} = p_k + 2\Delta y - 2\Delta x}$$

### Initial Decision Parameter

Evaluate at the starting pixel $(x_0, y_0)$ where $c = y_0 - m x_0$:
$$p_0 = 2\Delta y \cdot x_0 - 2\Delta x \cdot y_0 + 2\Delta y + \Delta x(2c - 1)$$
$$= 2\Delta y \cdot x_0 - 2\Delta x \cdot y_0 + 2\Delta y + \Delta x(2y_0 - 2m x_0 - 1)$$
$$= 2\Delta y \cdot x_0 - 2\Delta x \cdot y_0 + 2\Delta y + 2\Delta x \cdot y_0 - 2\Delta y \cdot x_0 - \Delta x$$
$$\boxed{p_0 = 2\Delta y - \Delta x}$$

### Complete Algorithm — All 4 Octants

```c
void BresenhamLine(int x0, int y0, int x1, int y1) {
    int dx = abs(x1 - x0), dy = abs(y1 - y0);
    int sx = (x0 < x1) ? 1 : -1;   // step direction for x
    int sy = (y0 < y1) ? 1 : -1;   // step direction for y

    if (dx >= dy) {
        // Gentle slope: |m| <= 1 — step along x
        int p = 2*dy - dx;
        for (int x = x0, y = y0; x != x1 + sx; x += sx) {
            PlotPixel(x, y);
            if (p < 0) {
                p += 2*dy;
            } else {
                y += sy;
                p += 2*dy - 2*dx;
            }
        }
    } else {
        // Steep slope: |m| > 1 — step along y
        int p = 2*dx - dy;
        for (int y = y0, x = x0; y != y1 + sy; y += sy) {
            PlotPixel(x, y);
            if (p < 0) {
                p += 2*dx;
            } else {
                x += sx;
                p += 2*dx - 2*dy;
            }
        }
    }
}
```

### Steep Slope Derivation ($m \ge 1$)

For steep lines, swap the roles of $x$ and $y$. Step $y$ by $+1$:
- Initial parameter: $p_0 = 2\Delta x - \Delta y$
- If $p_k < 0$: Choose pixel $(x_k, y_k+1)$; update: $p_{k+1} = p_k + 2\Delta x$
- If $p_k \ge 0$: Choose pixel $(x_k+1, y_k+1)$; update: $p_{k+1} = p_k + 2\Delta x - 2\Delta y$

### Comparison: DDA vs Bresenham

| Property | DDA | Bresenham |
|---|---|---|
| **Arithmetic** | Floating-point addition + round() | Integer addition only |
| **Speed** | Slower (FPU latency + rounding) | Faster (single-cycle integer ops) |
| **Precision** | Round-off error accumulates over long lines | Exact — no floating-point error |
| **Hardware Cost** | Requires FPU or emulation | Can be implemented in pure digital logic |
| **Memory** | Needs float registers | Only integer registers |
| **Negative slope** | Natural — just negate increment | Needs explicit sign tracking (`sx`, `sy`) |
| **Accuracy** | Same quality pixels as Bresenham (for short lines) | Identical quality, faster on hardware |

### Methods for Drawing Dashed and Dotted Lines [KTU Dec 2018 — 4 Marks]

A **dashed line** is drawn by alternating between plotting and skipping pixels according to a pattern:

**Method 1: Dash Counter**
```c
// Pattern: 4 pixels ON, 2 pixels OFF (repeating)
int dashPattern[] = {1, 1, 1, 1, 0, 0};
int patternLen = 6;
int patternIdx = 0;

for each pixel (x, y) along the Bresenham line:
    if dashPattern[patternIdx % patternLen] == 1:
        PlotPixel(x, y);
    patternIdx++;
```

**Method 2: Accumulator modulo**
```c
// Sum Euclidean distance along line; plot/skip based on threshold
float dashLen = 10.0;  // length of dash in pixels
float gapLen  =  5.0;  // length of gap
float acc = 0;
bool drawing = true;
float threshold = dashLen;

for each pixel (x, y):
    if drawing and acc < threshold:
        PlotPixel(x, y);
        acc++;
    elif acc >= threshold:
        drawing = !drawing;
        acc = 0;
        threshold = drawing ? dashLen : gapLen;
```

---

## 2. Example: Decision Geometry Visualization

```
y_k+1  +-----------NE--+  NE = (x_k+1, y_k+1)
        |          /    |   ▲
        |         / d2  |   | d2 = (y_k+1) - y_true
        |        /------+===*=== true line y = m(x_k+1) + c
        |       /  d1   |   | d1 = y_true - y_k
y_k    +-------E--------+  E  = (x_k+1, y_k)
       x_k          x_k+1
```

**Decision**: Sign of $p_k = \Delta x (d_1 - d_2)$:
- $p_k < 0 \Rightarrow d_1 < d_2 \Rightarrow$ line closer to E (lower) $\Rightarrow$ plot E
- $p_k \ge 0 \Rightarrow d_1 \ge d_2 \Rightarrow$ line closer to NE (upper) $\Rightarrow$ plot NE

---

## 3. Applications & Use Cases

1. **GPU Rasterizer Fixed-Function Hardware**: NVIDIA and AMD GPUs implement Bresenham-style integer decision logic in silicon to rasterize triangle edges at billions of pixels per second. The edge traversal in the rasterization stage uses exactly this incremental decision to find which pixels lie inside a triangle.

2. **CNC Machining & 3D Printing**: Stepper-motor controllers (G-code interpreters like Marlin/Grbl) use Bresenham's algorithm to synchronize the step pulses of two orthogonal motors (X-axis and Y-axis) so the tool head traces a straight diagonal path without accumulating integer step-rounding errors.

3. **Embedded Microcontroller Display Drivers**: On resource-constrained MCUs (ARM Cortex-M0 with no FPU), Bresenham's integer-only arithmetic enables fast line drawing on OLED/LCD screens in embedded UI libraries (LVGL, uGFX, Adafruit GFX).

4. **Network Routing Visualization**: Graph visualization tools (Gephi, D3.js) use scan-converted lines for rendering millions of directed graph edges. Bresenham underlies the low-level pixel rendering even when high-level SVG abstractions are used.

5. **Medical Imaging**: CT/MRI slice viewers compute projected scan lines across volumetric data using fast integer traversal (derived from Bresenham) to render maximum-intensity projections (MIP) in real time.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Bresenham Trace — $(5, 5)$ to $(13, 9)$ [KTU June 2024, June 2022, Dec 2020 — 9 Marks]

**Setup:**
$$\Delta x = 13-5 = 8, \quad \Delta y = 9-5 = 4, \quad m = \frac{4}{8} = 0.5 \quad (0 < m < 1)$$
$$2\Delta y = 8, \quad 2\Delta y - 2\Delta x = 8-16 = -8, \quad p_0 = 2\Delta y - \Delta x = 8-8 = 0$$

Initial pixel: Plot $(5, 5)$.

| Step $k$ | $p_k$ | Decision ($p\ge0$?) | Next Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| 0 | 0 | $p \ge 0$ → NE | $(6, 6)$ | $0 + (-8) = -8$ |
| 1 | -8 | $p < 0$ → E | $(7, 6)$ | $-8 + 8 = 0$ |
| 2 | 0 | $p \ge 0$ → NE | $(8, 7)$ | $0 + (-8) = -8$ |
| 3 | -8 | $p < 0$ → E | $(9, 7)$ | $-8 + 8 = 0$ |
| 4 | 0 | $p \ge 0$ → NE | $(10, 8)$ | $0 + (-8) = -8$ |
| 5 | -8 | $p < 0$ → E | $(11, 8)$ | $-8 + 8 = 0$ |
| 6 | 0 | $p \ge 0$ → NE | $(12, 9)$ | $0 + (-8) = -8$ |
| 7 | -8 | $p < 0$ → E | $(13, 9)$ | Done |

**Plotted pixels**: $(5,5) \to (6,6) \to (7,6) \to (8,7) \to (9,7) \to (10,8) \to (11,8) \to (12,9) \to (13,9)$

---

### Example 2: Bresenham Trace — $(1, 1)$ to $(8, 5)$ [KTU Jan 2023, May 2019, Dec 2018 — 9 Marks]

**Setup:**
$$\Delta x = 8-1 = 7, \quad \Delta y = 5-1 = 4, \quad m = \frac{4}{7} \approx 0.571 \quad (0 < m < 1)$$
$$2\Delta y = 8, \quad 2\Delta y - 2\Delta x = 8-14 = -6, \quad p_0 = 2(4) - 7 = 1$$

Initial pixel: Plot $(1, 1)$.

| Step $k$ | $p_k$ | Decision | Next Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| 0 | 1 | $p \ge 0$ → NE | $(2, 2)$ | $1-6 = -5$ |
| 1 | -5 | $p < 0$ → E | $(3, 2)$ | $-5+8 = 3$ |
| 2 | 3 | $p \ge 0$ → NE | $(4, 3)$ | $3-6 = -3$ |
| 3 | -3 | $p < 0$ → E | $(5, 3)$ | $-3+8 = 5$ |
| 4 | 5 | $p \ge 0$ → NE | $(6, 4)$ | $5-6 = -1$ |
| 5 | -1 | $p < 0$ → E | $(7, 4)$ | $-1+8 = 7$ |
| 6 | 7 | $p \ge 0$ → NE | $(8, 5)$ | Done |

**Plotted pixels**: $(1,1) \to (2,2) \to (3,2) \to (4,3) \to (5,3) \to (6,4) \to (7,4) \to (8,5)$

---

### Example 3: DDA Trace — $(30, 20)$ to $(15, 10)$ [KTU Sep 2020, Dec 2019, May 2019 — 4 Marks]

The endpoint order has $x_0 > x_1$, so we can simply reverse them: draw from $(15, 10)$ to $(30, 20)$.

**Setup:**
$$\Delta x = 30-15 = 15, \quad \Delta y = 20-10 = 10, \quad m = \frac{10}{15} = 0.667 \quad (|m| < 1)$$
$$x\text{-step} = 1, \quad y\text{-step} = 0.667$$

| $k$ | $x$ | $y$ (cumulative) | Rounded Pixel |
|---|---|---|---|
| 0 | 15 | 10.000 | **(15, 10)** |
| 1 | 16 | 10.667 | **(16, 11)** |
| 2 | 17 | 11.333 | **(17, 11)** |
| 3 | 18 | 12.000 | **(18, 12)** |
| 4 | 19 | 12.667 | **(19, 13)** |
| 5 | 20 | 13.333 | **(20, 13)** |
| 6 | 21 | 14.000 | **(21, 14)** |
| 7 | 22 | 14.667 | **(22, 15)** |
| 8 | 23 | 15.333 | **(23, 15)** |
| 9 | 24 | 16.000 | **(24, 16)** |
| 10 | 25 | 16.667 | **(25, 17)** |
| 11 | 26 | 17.333 | **(26, 17)** |
| 12 | 27 | 18.000 | **(27, 18)** |
| 13 | 28 | 18.667 | **(28, 19)** |
| 14 | 29 | 19.333 | **(29, 19)** |
| 15 | 30 | 20.000 | **(30, 20)** |

---

## 5. Previous Year Questions & Solutions

### Q1 [KTU Dec 2023 — 9 Marks]
**Question**: Digitize a line with end points (10, 20) and (20, 25) using Bresenham's line drawing algorithm.

**Solution**:

**Setup:**
$$\Delta x = 20-10 = 10, \quad \Delta y = 25-20 = 5, \quad m = \frac{5}{10} = 0.5 \quad (0 < m < 1)$$
$$2\Delta y = 10, \quad 2\Delta y - 2\Delta x = 10-20 = -10, \quad p_0 = 2(5) - 10 = 0$$

Initial pixel: Plot $(10, 20)$.

| Step $k$ | $p_k$ | Decision | Next Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| 0 | 0 | $\ge 0$ → NE | $(11, 21)$ | $0-10 = -10$ |
| 1 | -10 | $< 0$ → E | $(12, 21)$ | $-10+10 = 0$ |
| 2 | 0 | $\ge 0$ → NE | $(13, 22)$ | $0-10 = -10$ |
| 3 | -10 | $< 0$ → E | $(14, 22)$ | $-10+10 = 0$ |
| 4 | 0 | $\ge 0$ → NE | $(15, 23)$ | $0-10 = -10$ |
| 5 | -10 | $< 0$ → E | $(16, 23)$ | $-10+10 = 0$ |
| 6 | 0 | $\ge 0$ → NE | $(17, 24)$ | $0-10 = -10$ |
| 7 | -10 | $< 0$ → E | $(18, 24)$ | $-10+10 = 0$ |
| 8 | 0 | $\ge 0$ → NE | $(19, 25)$ | $0-10 = -10$ |
| 9 | -10 | $< 0$ → E | $(20, 25)$ | Done |

**Plotted Pixels**: $(10,20) \to (11,21) \to (12,21) \to (13,22) \to (14,22) \to (15,23) \to (16,23) \to (17,24) \to (18,24) \to (19,25) \to (20,25)$

---

### Q2 [KTU June 2022 — 9 Marks]
**Question**: Consider the line from (5, 6) to (13, 9). Use Bresenham's Line Drawing Algorithm to rasterize this line.

**Solution**:

**Setup:**
$$\Delta x = 13-5 = 8, \quad \Delta y = 9-6 = 3, \quad m = \frac{3}{8} = 0.375 \quad (0 < m < 1)$$
$$2\Delta y = 6, \quad 2\Delta y - 2\Delta x = 6-16 = -10, \quad p_0 = 2(3) - 8 = -2$$

Initial pixel: Plot $(5, 6)$.

| Step $k$ | $p_k$ | Decision | Next Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| 0 | -2 | $< 0$ → E | $(6, 6)$ | $-2+6 = 4$ |
| 1 | 4 | $\ge 0$ → NE | $(7, 7)$ | $4-10 = -6$ |
| 2 | -6 | $< 0$ → E | $(8, 7)$ | $-6+6 = 0$ |
| 3 | 0 | $\ge 0$ → NE | $(9, 8)$ | $0-10 = -10$ |
| 4 | -10 | $< 0$ → E | $(10, 8)$ | $-10+6 = -4$ |
| 5 | -4 | $< 0$ → E | $(11, 8)$ | $-4+6 = 2$ |
| 6 | 2 | $\ge 0$ → NE | $(12, 9)$ | $2-10 = -8$ |
| 7 | -8 | $< 0$ → E | $(13, 9)$ | Done |

**Plotted Pixels**: $(5,6) \to (6,6) \to (7,7) \to (8,7) \to (9,8) \to (10,8) \to (11,8) \to (12,9) \to (13,9)$

---

### Q3 [KTU Dec 2021 — 4 Marks]
**Question**: Rasterize the line segment from pixel coordinate (10, 12) to (15, 15) using Bresenham's line drawing algorithm.

**Solution**:

**Setup:**
$$\Delta x = 15-10 = 5, \quad \Delta y = 15-12 = 3, \quad m = \frac{3}{5} = 0.6 \quad (0 < m < 1)$$
$$2\Delta y = 6, \quad 2\Delta y - 2\Delta x = 6-10 = -4, \quad p_0 = 2(3) - 5 = 1$$

Initial pixel: Plot $(10, 12)$.

| Step $k$ | $p_k$ | Decision | Next Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| 0 | 1 | $\ge 0$ → NE | $(11, 13)$ | $1-4 = -3$ |
| 1 | -3 | $< 0$ → E | $(12, 13)$ | $-3+6 = 3$ |
| 2 | 3 | $\ge 0$ → NE | $(13, 14)$ | $3-4 = -1$ |
| 3 | -1 | $< 0$ → E | $(14, 14)$ | $-1+6 = 5$ |
| 4 | 5 | $\ge 0$ → NE | $(15, 15)$ | Done |

**Plotted Pixels**: $(10,12) \to (11,13) \to (12,13) \to (13,14) \to (14,14) \to (15,15)$

---

### Q4 [KTU June 2024 — 4 Marks]
**Question**: Write Bresenham's Line drawing algorithm. What are its advantages over DDA?

**Solution**:

**Bresenham's Line Drawing Algorithm** (for $0 < m < 1$):

**Input**: Integer endpoints $(x_0, y_0)$ and $(x_n, y_n)$ where $x_0 < x_n$.  
**Output**: Set of raster pixels approximating the line.

```
Step 1: Compute Δx = x_n - x_0, Δy = y_n - y_0
Step 2: Compute initial decision parameter p₀ = 2Δy - Δx
Step 3: Plot starting pixel (x₀, y₀)
Step 4: For k = 0, 1, 2, ..., Δx - 1:
    If p_k < 0:
        Next pixel: (x_k + 1, y_k)
        p_{k+1} = p_k + 2Δy
    Else:
        Next pixel: (x_k + 1, y_k + 1)
        p_{k+1} = p_k + 2Δy - 2Δx
Step 5: Stop when x = x_n
```

**Advantages over DDA:**
1. **Integer arithmetic only** — no floating-point operations or division; uses only addition and bit-shifts.
2. **No rounding error** — the integer decision parameter $p_k$ tracks the exact geometric position without floating-point drift.
3. **Hardware efficiency** — integer adders are orders of magnitude faster and simpler than FPUs; Bresenham can be implemented directly in digital logic gates.
4. **Higher speed** — eliminates the `round()` function call present in every DDA iteration.

---

### Q5 [KTU Dec 2018 — 4 Marks]
**Question**: Write the methods used to plot a dashed line segment.

**Solution**:

A dashed line segment is a line drawn with alternating "drawn" and "skipped" pixel segments. Three implementation methods:

**Method 1: Pattern Counter**
Assign a bit pattern (e.g., `1111 0011` = 4 on, 2 off) to a circular buffer. For each pixel computed by Bresenham:
- If current pattern bit = 1: call PlotPixel()
- If current pattern bit = 0: skip (do not plot)
- Advance the pattern index modulo pattern length

**Method 2: Parameterized Dash Length**
Pre-compute the total number of pixels in the line = $\max(|\Delta x|, |\Delta y|)$. Divide into repeated cycles of (dashLen + gapLen) pixels. Use modulo arithmetic to decide plot/skip per pixel.

**Method 3: Distance Accumulator**
Accumulate the Euclidean distance along the line. When the accumulated distance is within [0, dashLen], plot the pixel. When in [dashLen, dashLen+gapLen], skip. Reset the accumulator after each cycle.

**Example** — dashed line from $(0,0)$ to $(10,0)$ with dash=3px, gap=2px:
- Pixels 0,1,2 → plot (dash)
- Pixels 3,4 → skip (gap)
- Pixels 5,6,7 → plot (dash)
- Pixels 8,9 → skip (gap)
- Pixel 10 → plot (new dash)

---

### Q6 [KTU Sep 2020 — 9 Marks]
**Question**: Generate the points between the end points of a line viz. (2,2) and (9,6) by using Bresenham's line drawing algorithm.

**Solution**:

**Setup:**
$$\Delta x = 9-2 = 7, \quad \Delta y = 6-2 = 4, \quad m = \frac{4}{7} \approx 0.571 \quad (0 < m < 1)$$
$$2\Delta y = 8, \quad 2\Delta y - 2\Delta x = 8-14 = -6, \quad p_0 = 2(4) - 7 = 1$$

Initial pixel: Plot $(2, 2)$.

| Step $k$ | $p_k$ | Decision | Next Pixel | $p_{k+1}$ |
|---|---|---|---|---|
| 0 | 1 | $\ge 0$ → NE | $(3, 3)$ | $1-6 = -5$ |
| 1 | -5 | $< 0$ → E | $(4, 3)$ | $-5+8 = 3$ |
| 2 | 3 | $\ge 0$ → NE | $(5, 4)$ | $3-6 = -3$ |
| 3 | -3 | $< 0$ → E | $(6, 4)$ | $-3+8 = 5$ |
| 4 | 5 | $\ge 0$ → NE | $(7, 5)$ | $5-6 = -1$ |
| 5 | -1 | $< 0$ → E | $(8, 5)$ | $-1+8 = 7$ |
| 6 | 7 | $\ge 0$ → NE | $(9, 6)$ | Done |

**Plotted Pixels**: $(2,2) \to (3,3) \to (4,3) \to (5,4) \to (6,4) \to (7,5) \to (8,5) \to (9,6)$

---

### Q7 [KTU Dec 2019 — 2 Marks + 2 Marks]
**Question**: (a) Which algorithm is better for line drawing — DDA or Bresenham's? Defend your view. (b) Write a note on any two interactive graphics input devices.

**Solution**:

**(a) Bresenham's algorithm is better.** Three defenses:
1. **Accuracy**: Bresenham uses integer arithmetic with no floating-point rounding — the decision parameter $p_k$ captures the exact error. DDA accumulates rounding errors over long lines.
2. **Speed**: Integer addition (Bresenham) is a single-cycle operation. Floating-point addition + rounding (DDA) is typically 4–8 cycles on RISC architectures.
3. **Hardware**: GPU rasterizers implement Bresenham-style integer decision logic directly in fixed-function silicon; DDA would require floating-point arithmetic units, which consume much more power and silicon area.

**(b) Two interactive graphics input devices:**

**1. Joystick**:
- A joystick uses two potentiometer voltage dividers (one for the X-axis, one for the Y-axis of the stick deflection).
- When the stick is displaced from center, it moves a wiper along the resistance track, generating a voltage proportional to displacement: $V_{out} = V_{supply} \times \frac{R_{wiper}}{R_{total}}$.
- An Analog-to-Digital Converter (ADC) samples $V_x$ and $V_y$, digitizing the continuous displacement into integer coordinates fed to the graphics application.
- Use in graphics: 3D viewport rotation, flight simulator control, game character movement.

**2. Light Pen**:
- A light pen contains a photosensitive detector (photodiode or phototransistor) at its tip.
- When held against a CRT screen, it detects the brief flash of light as the electron beam passes across the screen at the pen's location.
- The display controller correlates the photodetection timing pulse with the current horizontal/vertical scan address to determine the $(x, y)$ screen position of the pen tip.
- Limitation: Only works with CRT displays (not LCD/OLED since those emit continuous light, not a sweeping beam pulse).
- Use in graphics: drawing directly on screen, selecting graphical objects in CAD systems.
