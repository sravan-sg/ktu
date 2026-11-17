# Circle Generation Algorithms: Midpoint Circle and Bresenham's Algorithm

## 1. Explanation
A circle is defined geometrically as the locus of all points in a 2D plane that are at a fixed radial distance $r$ from a central coordinate point $(x_c, y_c)$:
$$(x - x_c)^2 + (y - y_c)^2 = r^2$$

Directly computing circle pixels using the explicit equation $y = y_c \pm \sqrt{r^2 - (x - x_c)^2}$ or polar coordinates $x = x_c + r\cos\theta, y = y_c + r\sin\theta$ is computationally unacceptable for real-time graphics because it demands square roots, trigonometric functions, and floating-point multiplications per pixel, and produces non-uniform pixel spacing when slope approaches vertical.

---

### The Eight-Way Symmetry of a Circle
A circle centered at the origin exhibits **eight-fold reflective symmetry**:
1. Reflection across the $Y$-axis: $(x, y) \leftrightarrow (-x, y)$
2. Reflection across the $X$-axis: $(x, y) \leftrightarrow (x, -y)$
3. Reflection across the line $y = x$: $(x, y) \leftrightarrow (y, x)$
4. Reflection across the line $y = -x$: $(x, y) \leftrightarrow (-y, -x)$

#### The Eight Symmetric Points
If a single pixel coordinate $(x, y)$ is calculated within the first octant ($0 \le x \le y$, from $\theta = 90^\circ$ to $45^\circ$), the remaining seven octant points are obtained by simple sign inversion and coordinate swapping without any arithmetic calculation:
$$\{(x, y), \ (y, x), \ (y, -x), \ (x, -y), \ (-x, -y), \ (-y, -x), \ (-y, x), \ (-x, y)\}$$

If the circle is centered at an arbitrary point $(x_c, y_c)$, each of these 8 points is translated: $(x \pm x_c, y \pm y_c)$.
This reduces computational workload by **$87.5\%$** (an 8-fold reduction).

---

### Midpoint Circle Algorithm
The Midpoint Circle Algorithm applies an incremental decision parameter to evaluate whether the midpoint between two candidate pixels lies inside or outside the theoretical circle boundary.

#### Circle Function Definition
Define the circle function $f_{\text{circle}}(x, y)$:
$$f_{\text{circle}}(x, y) = x^2 + y^2 - r^2$$
- $f_{\text{circle}}(x, y) < 0$: Point $(x, y)$ is **inside** the circle boundary.
- $f_{\text{circle}}(x, y) = 0$: Point $(x, y)$ is **exactly on** the circle boundary.
- $f_{\text{circle}}(x, y) > 0$: Point $(x, y)$ is **outside** the circle boundary.

#### Midpoint Formulation in the First Octant
Start at the top of the circle: $(x_0, y_0) = (0, r)$.
Moving clockwise in the first octant from $x = 0$ to $x = y$:
- Step along $x$ in unit increments: $x_{k+1} = x_k + 1$.
- The two candidate pixels are the **East** pixel $E(x_k + 1, y_k)$ and the **South-East** pixel $SE(x_k + 1, y_k - 1)$.
- The spatial **midpoint** between these two candidate pixels is:
  $$M = \left(x_k + 1, \ y_k - \frac{1}{2}\right)$$

Evaluate the circle function at this midpoint to define the **decision parameter** $p_k$:
$$p_k = f_{\text{circle}}\left(x_k + 1, \ y_k - \frac{1}{2}\right) = (x_k + 1)^2 + \left(y_k - \frac{1}{2}\right)^2 - r^2$$

#### Conditional Testing:
1. **If $p_k < 0$**:
   - The midpoint $M$ lies strictly **inside** the circle boundary.
   - Therefore, the circle boundary passes closer to the upper pixel $E(x_k + 1, y_k)$.
   - Choose pixel: $(x_k + 1, y_k)$.
2. **If $p_k \ge 0$**:
   - The midpoint $M$ lies **outside** (or on) the circle boundary.
   - Therefore, the circle boundary passes closer to the lower pixel $SE(x_k + 1, y_k - 1)$.
   - Choose pixel: $(x_k + 1, y_k - 1)$.

#### Evaluating the Successive Decision Parameter $p_{k+1}$:
At step $k+1$:
$$p_{k+1} = f_{\text{circle}}\left(x_{k+1} + 1, \ y_{k+1} - \frac{1}{2}\right) = [(x_k + 1) + 1]^2 + \left(y_{k+1} - \frac{1}{2}\right)^2 - r^2$$
$$p_{k+1} - p_k = (x_k + 2)^2 - (x_k + 1)^2 + \left(y_{k+1} - \frac{1}{2}\right)^2 - \left(y_k - \frac{1}{2}\right)^2$$
$$p_{k+1} - p_k = 2x_k + 3 + (y_{k+1}^2 - y_k^2) - (y_{k+1} - y_k)$$

- **Case 1: If $p_k < 0$** ($y_{k+1} = y_k$):
  $$p_{k+1} = p_k + 2x_k + 3 = p_k + 2x_{k+1} + 1$$
- **Case 2: If $p_k \ge 0$** ($y_{k+1} = y_k - 1$):
  $$p_{k+1} = p_k + 2x_k + 3 + (y_k - 1)^2 - y_k^2 - (y_k - 1 - y_k)$$
  $$p_{k+1} = p_k + 2x_k + 3 - 2y_k + 1 + 1 = p_k + 2x_k - 2y_k + 5 = p_k + 2x_{k+1} - 2y_{k+1} + 1$$

#### Initial Decision Parameter $p_0$:
Evaluate $p_k$ at the starting point $(x_0, y_0) = (0, r)$:
$$p_0 = f_{\text{circle}}\left(1, \ r - \frac{1}{2}\right) = 1^2 + \left(r - \frac{1}{2}\right)^2 - r^2 = 1 + r^2 - r + \frac{1}{4} - r^2 = \frac{5}{4} - r$$
Since $r$ is an integer in discrete screen coordinates:
- If rounding to integer: $\frac{5}{4} \approx 1$, yielding the integer form:
  $$p_0 = 1 - r$$
(Both $\frac{5}{4} - r$ and $1 - r$ produce identical discrete pixel decisions because $p_k$ increments only by integers at every step).

---

## 2. Example: 8-Way Symmetry and Midpoint Decision Geometry
```
                        (0, r)
                          │
                  Octant 2│ Octant 1 (x <= y)
             (-y, x)      │      (y, x)
                \         │         /
                 \        │        /
                  \       │       /
                   \      │      /
    Octant 3        \     │     /        Octant 8
  (-x, y) ───────────+────┼────+─────────── (x, y)
                     │    │    │
  (-x, -y) ──────────+────┼────+─────────── (x, -y)
    Octant 4        /     │     \        Octant 7
                   /      │      \
                  /       │       \
                 /        │        \
             (-y, -x)     │      (y, -x)
                  Octant 5│ Octant 6
                          │
                       (0, -r)
```

---

## 3. Applications & Use Cases
1. **Digital Radar & Sonar Displays**: Radar sweeps render range rings and azimuth markers centered at the emitter using midpoint circle generators at sub-microsecond latency.
2. **2D Graphics Rendering Engines (Skia, Cairo, HTML5 Canvas)**: Low-level stroke rendering for `arc()` and circle primitives applies midpoint stepping to populate geometry buffers before pixel shading.
3. **Circular Region-of-Interest (ROI) Masking in Medical Imaging**: Diagnostic ultrasound and ophthalmology fundus scanners apply integer midpoint circle rasterization to bound anatomical optical disks and lesions.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Midpoint Circle Algorithm Trace for Radius $r = 8$ [KTU May 2019 / Dec 2021 - 9 Marks]
**Problem**:
Digitize a circle of radius $r = 8$ centered at the origin $(0, 0)$ from $x = 0$ to $x = y$ using the Midpoint Circle algorithm. Tabulate step index $k$, decision parameter $p_k$, and chosen pixel $(x_{k+1}, y_{k+1})$, and determine all eight symmetric points for the step where $x = 4$.

**Step-by-step Solution**:
1. **Initial Setup**:
   $$r = 8, \quad (x_0, y_0) = (0, 8)$$
   $$\text{Initial decision parameter: } p_0 = 1 - r = 1 - 8 = -7$$
2. **Iteration Table**:

| Step $k$ | Decision $p_k$ | Condition | Action / Chosen Pixel $(x_{k+1}, y_{k+1})$ | Next Decision Parameter $p_{k+1}$ |
|---|---|---|---|---|
| 0 | $-7$ | $p_0 < 0$ | $x_1 = 1, y_1 = 8 \implies \mathbf{(1, 8)}$ | $p_1 = -7 + 2(1) + 1 = -4$ |
| 1 | $-4$ | $p_1 < 0$ | $x_2 = 2, y_2 = 8 \implies \mathbf{(2, 8)}$ | $p_2 = -4 + 2(2) + 1 = 1$ |
| 2 | $1$ | $p_2 \ge 0$ | $x_3 = 3, y_3 = 7 \implies \mathbf{(3, 7)}$ | $p_3 = 1 + 2(3) - 2(7) + 1 = -6$ |
| 3 | $-6$ | $p_3 < 0$ | $x_4 = 4, y_4 = 7 \implies \mathbf{(4, 7)}$ | $p_4 = -6 + 2(4) + 1 = 3$ |
| 4 | $3$ | $p_4 \ge 0$ | $x_5 = 5, y_5 = 6 \implies \mathbf{(5, 6)}$ | $p_5 = 3 + 2(5) - 2(6) + 1 = 2$ |
| 5 | $2$ | $p_5 \ge 0$ | $x_6 = 6, y_6 = 5 \implies \mathbf{(6, 5)}$ | Algorithm Terminates ($x > y$) |

3. **Eight Symmetric Points for Pixel $(4, 7)$**:
   $$\mathbf{(4, 7), \ (7, 4), \ (7, -4), \ (4, -7), \ (-4, -7), \ (-7, -4), \ (-7, 4), \ (-4, 7)}$$

---

### Example 2: Circle Scan Conversion with Arbitrary Center $(x_c, y_c) = (5, 5)$ and Radius $r = 6$ [KTU Dec 2020 Pattern]
**Problem**:
Generate the pixel positions in the first octant for a circle with radius $r = 6$ centered at $(x_c, y_c) = (5, 5)$ using the Midpoint Circle algorithm.

**Step-by-step Solution**:
1. **Initial Setup (Relative to Origin)**:
   $$r = 6, \quad (x_0, y_0) = (0, 6), \quad p_0 = 1 - r = 1 - 6 = -5$$
2. **Relative Octant Points**:
   - $k=0: p_0 = -5 < 0 \implies (1, 6), \quad p_1 = -5 + 2(1) + 1 = -2$
   - $k=1: p_1 = -2 < 0 \implies (2, 6), \quad p_2 = -2 + 2(2) + 1 = 3$
   - $k=2: p_2 = 3 \ge 0 \implies (3, 5), \quad p_3 = 3 + 2(3) - 2(5) + 1 = 0$
   - $k=3: p_3 = 0 \ge 0 \implies (4, 4), \quad p_4 = 0 + 2(4) - 2(4) + 1 = 1$
   - Termination condition met ($x = y = 4$).
   - Relative first octant points: $\mathbf{(0, 6), (1, 6), (2, 6), (3, 5), (4, 4)}$.
3. **Translation to Center $(5, 5)$**:
   Add $(x_c, y_c) = (5, 5)$ to each relative coordinate:
   - $(0 + 5, 6 + 5) \implies \mathbf{(5, 11)}$
   - $(1 + 5, 6 + 5) \implies \mathbf{(6, 11)}$
   - $(2 + 5, 6 + 5) \implies \mathbf{(7, 11)}$
   - $(3 + 5, 5 + 5) \implies \mathbf{(8, 10)}$
   - $(4 + 5, 4 + 5) \implies \mathbf{(9, 9)}$

---

### Example 3: Error Bound Analysis of Midpoint Circle Algorithm [KTU Analytical Pattern]
**Problem**:
Prove that the Midpoint Circle algorithm never deviates from the true mathematical circle by more than half a pixel in the radial direction.

**Step-by-step Solution**:
1. In the first octant, $0 \le x \le y$, the slope of the circle tangent is:
   $$\frac{dy}{dx} = -\frac{x}{y}$$
   Since $x \le y$, $|\frac{dy}{dx}| \le 1$. The vertical distance between adjacent horizontal grid lines is $\Delta y = 1$.
2. At step $k$, having plotted $(x_k, y_k)$, the true mathematical circle passes through $(x_k + 1, y_{\text{true}})$, where:
   $$y_k - 1 \le y_{\text{true}} \le y_k$$
3. The midpoint between candidate pixels is $M = (x_k + 1, y_k - 0.5)$.
   - If the true circle is above $M$, $y_{\text{true}} > y_k - 0.5$. The algorithm selects $y_k$. The error is:
     $$|y_{\text{true}} - y_k| < 0.5 \text{ pixels}$$
   - If the true circle is below $M$, $y_{\text{true}} \le y_k - 0.5$. The algorithm selects $y_k - 1$. The error is:
     $$|y_{\text{true}} - (y_k - 1)| \le 0.5 \text{ pixels}$$
4. Therefore, the maximum vertical deviation between the chosen pixel and the continuous circle boundary is bounded by $\epsilon_{\max} = 0.5 \text{ pixels}$.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / June 2024 - 4 Marks]
**Question**:
How 8-way symmetry of a circle can be used for writing circle drawing algorithms? Write the symmetric points if $(x, y)$ is a point on the circle with centre at origin.

**Solution**:
1. **Use of 8-Way Symmetry**:
   A circle centered at the origin $(0, 0)$ satisfies $x^2 + y^2 = r^2$. Because this equation is completely invariant under permutations and sign inversions of $x$ and $y$, the circle exhibits eight-fold reflective symmetry across the $X$-axis, $Y$-axis, and the diagonal lines $y = x$ and $y = -x$.
   - Consequently, an algorithm only needs to compute the pixel coordinates for **one octant** (from $x = 0$ to $x = y$, covering $45^\circ$).
   - The remaining seven octants are generated simultaneously at zero computational cost by reflecting the calculated point.
2. **The Eight Symmetric Points**:
   If $(x, y)$ is a computed point on a circle centered at $(0, 0)$ in the first octant, the 8 symmetric points are:
   1. $(x, y)$ — Octant 1
   2. $(y, x)$ — Octant 2
   3. $(y, -x)$ — Octant 7
   4. $(x, -y)$ — Octant 8
   5. $(-x, -y)$ — Octant 5
   6. $(-y, -x)$ — Octant 6
   7. $(-y, x)$ — Octant 3
   8. $(-x, y)$ — Octant 4

---

### Question 2 [KTU December 2020 / December 2023 - 4 Marks]
**Question**:
Generate 4 pixel positions of a circle in the first quadrant with radius $r = 10$ centered on the origin, using the midpoint circle algorithm.

**Solution**:
1. **Initial Setup**:
   $$r = 10, \quad (x_0, y_0) = (0, 10)$$
   $$p_0 = 1 - r = 1 - 10 = -9$$
2. **Step-by-Step Pixel Generation**:
   - **Initial Pixel**: Plot $\mathbf{(0, 10)}$.
   - **Step 1**:
     - $p_0 = -9 < 0$.
     - Increment $x_1 = 1$, keep $y_1 = 10$.
     - Chosen Pixel: $\mathbf{(1, 10)}$.
     - $p_1 = p_0 + 2x_1 + 1 = -9 + 2(1) + 1 = -6$.
   - **Step 2**:
     - $p_1 = -6 < 0$.
     - Increment $x_2 = 2$, keep $y_2 = 10$.
     - Chosen Pixel: $\mathbf{(2, 10)}$.
     - $p_2 = p_1 + 2x_2 + 1 = -6 + 2(2) + 1 = -1$.
   - **Step 3**:
     - $p_2 = -1 < 0$.
     - Increment $x_3 = 3$, keep $y_3 = 10$.
     - Chosen Pixel: $\mathbf{(3, 10)}$.
     - $p_3 = p_2 + 2x_3 + 1 = -1 + 2(3) + 1 = 6$.
   - **Step 4**:
     - $p_3 = 6 \ge 0$.
     - Increment $x_4 = 4$, decrement $y_4 = 10 - 1 = 9$.
     - Chosen Pixel: $\mathbf{(4, 9)}$.
     - $p_4 = p_3 + 2x_4 - 2y_4 + 1 = 6 + 2(4) - 2(9) + 1 = 6 + 8 - 18 + 1 = -3$.

3. **Generated Pixel Positions**:
   The first four generated pixel positions in the first quadrant are:
   $$\mathbf{(0, 10), \ (1, 10), \ (2, 10), \ (3, 10), \ (4, 9)}$$

