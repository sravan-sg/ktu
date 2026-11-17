# Module 2: Revision Notes — Quick Review Guide

## 1. High-Yield Summary
- **Line Rasterization**:
  - *DDA*: Simple, but uses floating-point addition and rounding ($x_{k+1} = x_k + 1, y_{k+1} = y_k + m$ for $m \le 1$). Subject to precision drift.
  - *Bresenham*: Pure integer arithmetic. Evaluates distance difference $d_1 - d_2$.
- **Circle Generation**:
  - *8-Way Symmetry*: Computing one octant ($0 \le x \le y$) yields all 8 octant points: $(x, y), (y, x), (y, -x), (x, -y), (-x, -y), (-y, -x), (-y, x), (-x, y)$.
  - *Midpoint Circle*: Evaluates circle function at midpoint $M(x_k + 1, y_k - 0.5)$.
- **Polygon Filling**:
  - *Odd-Even Rule*: Count edge crossings. Odd = inside, Even = outside.
  - *Winding Number*: Sum signed crossings (+1 right-to-left, -1 left-to-right). Non-zero = inside.
  - *Scan-Line Fill*: ET buckets non-horizontal edges by $y_{\min}$. AET updates active edges incrementally ($x_{\text{new}} = x_{\text{old}} + 1/m$). Fill pixels between adjacent sorted pairs.
  - *Boundary-Fill vs Flood-Fill*: Boundary fill stops at a specified boundary color. Flood fill replaces an old interior color with a new color.

---

## 2. Essential Formulas & Decision Parameter Recurrences

### Bresenham Line ($0 < m < 1$):
- Initial Parameter:
  $$p_0 = 2\Delta y - \Delta x$$
- If $p_k < 0$: Choose $(x_k + 1, y_k)$; update:
  $$p_{k+1} = p_k + 2\Delta y$$
- If $p_k \ge 0$: Choose $(x_k + 1, y_k + 1)$; update:
  $$p_{k+1} = p_k + 2\Delta y - 2\Delta x$$

### Bresenham Line Steep ($m \ge 1$):
- Initial Parameter:
  $$p_0 = 2\Delta x - \Delta y$$
- If $p_k < 0$: Choose $(x_k, y_k + 1)$; update:
  $$p_{k+1} = p_k + 2\Delta x$$
- If $p_k \ge 0$: Choose $(x_k + 1, y_k + 1)$; update:
  $$p_{k+1} = p_k + 2\Delta x - 2\Delta y$$

### Midpoint Circle (First Octant, $0 \le x \le y$):
- Initial Point: $(x_0, y_0) = (0, r)$.
- Initial Parameter:
  $$p_0 = 1 - r \quad \left(\text{or } \frac{5}{4} - r\right)$$
- If $p_k < 0$: Choose $(x_k + 1, y_k)$; update:
  $$p_{k+1} = p_k + 2x_{k+1} + 1$$
- If $p_k \ge 0$: Choose $(x_k + 1, y_k - 1)$; update:
  $$p_{k+1} = p_k + 2x_{k+1} - 2y_{k+1} + 1$$

---

## 3. Comparison Table: Line and Polygon Algorithms

| Algorithm | Arithmetic Type | Main Advantage | Main Limitation |
|---|---|---|---|
| **DDA Line** | Floating-point | Conceptual simplicity | Accumulation of round-off errors |
| **Bresenham Line** | Pure Integer | Single-cycle ALU execution; exact | Requires slope case branches ($m < 1$ vs $m \ge 1$) |
| **Midpoint Circle** | Pure Integer | 8-fold computation reduction | Limited to circular arcs (ellipses need 2 regions) |
| **Scan-Line Fill** | Integer/Fixed-point | Fast, linear memory, no stack overflow | Requires edge pre-sorting and active management |
| **Recursive Boundary Fill** | Integer | Extremely easy to implement | Prone to thread stack overflow on large areas |

---

## 4. Top 3 Exam Traps & Tips
1. **Always Check the Slope First in Bresenham Line**: Before computing $p_0$, always calculate $m = \Delta y / \Delta x$. If $\Delta y > \Delta x$ ($m > 1$), you MUST swap the formulas to step along $y$, using $p_0 = 2\Delta x - \Delta y$. Using the $m < 1$ formula for a steep line fails the exam question.
2. **Horizontal Edges in Scan-Line Fill**: Never include horizontal edges in the Edge Table ($1/m = \infty$). Horizontal spans are filled when scanline hits their $y$-level.
3. **Vertex Intersections in Scanline**: When a scanline hits a vertex, remember: if the two adjoining edges continue in opposite directions (monotonic in $y$), count as **1** intersection. If the vertex is a local peak or valley (both edges go down or both go up), count as **2** (or 0) intersections.

