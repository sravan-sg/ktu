# Line Drawing Algorithms: DDA and Bresenham's Algorithm

## 1. Explanation
Line drawing (scan-conversion of a line) is the process of approximating a continuous mathematical line segment $y = mx + c$ onto a discrete two-dimensional grid of integer pixel coordinates $(x, y)$.

### The Scan Conversion Challenge
In Cartesian space, a line between endpoints $(x_0, y_0)$ and $(x_n, y_n)$ contains an uncountably infinite number of points defined by:
$$y = m x + c, \quad \text{where } m = \frac{\Delta y}{\Delta x} = \frac{y_n - y_0}{x_n - x_0}, \quad c = y_0 - m x_0$$
However, computer displays consist of a discrete matrix of integer coordinate points. The raster algorithm must determine which integer pixel coordinates $(x, y)$ best approximate the true continuous line path with:
1. Minimal geometric deviation (straightness and uniform brightness).
2. High execution speed (ideally using pure integer additions without floating-point arithmetic or multiplications).
3. Independence from the direction of line traversal.

---

### Digital Differential Analyzer (DDA) Algorithm
The DDA algorithm is an incremental scan-conversion method based on calculating either $\Delta y = m \Delta x$ or $\Delta x = \frac{\Delta y}{m}$.

#### Mathematical Formulation
1. **Case 1: $|m| \le 1$ (Gentle Slope / Horizontal Dominant)**:
   - Step along $x$ in unit increments: $\Delta x = 1 \implies x_{k+1} = x_k + 1$.
   - The corresponding $y$ coordinate increments continuously by the slope $m$:
     $$y_{k+1} = y_k + m$$
   - The raster pixel is obtained by rounding: $\text{Pixel} = (x_{k+1}, \text{round}(y_{k+1}))$.
2. **Case 2: $|m| > 1$ (Steep Slope / Vertical Dominant)**:
   - Stepping along $x$ would create large gaps and disjoint pixels along the $y$-axis.
   - Therefore, step along $y$ in unit increments: $\Delta y = 1 \implies y_{k+1} = y_k + 1$.
   - The corresponding $x$ coordinate increments by $\frac{1}{m}$:
     $$x_{k+1} = x_k + \frac{1}{m}$$
   - The raster pixel is obtained by rounding: $\text{Pixel} = (\text{round}(x_{k+1}), y_{k+1})$.

#### Limitations of DDA:
- **Floating-point Arithmetic**: Accumulating the fractional slope $m$ or $1/m$ at every step requires expensive floating-point addition.
- **Round-off Error Accumulation**: Repeated addition of floating-point numbers in finite-precision registers causes precision drift, skewing line endpoints away from the true geometric path.
- **Explicit Rounding Overhead**: Calls to `round()` or `floor()` introduce additional CPU cycle latency per pixel.

---

### Bresenham's Line Drawing Algorithm
Developed by Jack E. Bresenham in 1962, this algorithm is an optimized rasterization technique that eliminates floating-point arithmetic entirely. It relies strictly on **fast integer addition, subtraction, and bit-shift multiplication ($\times 2$)**.

#### Derivation for Line with Slope $0 < m < 1$
Assume a line with endpoints $(x_0, y_0)$ and $(x_n, y_n)$ where $x_0 < x_n$ and $0 < m < 1$.
At step $k$, having plotted pixel $(x_k, y_k)$, the next candidate pixel at column $x_{k+1} = x_k + 1$ must be either:
- The **East** pixel: $(x_k + 1, y_k)$
- The **North-East** pixel: $(x_k + 1, y_k + 1)$

The true mathematical $y$-coordinate at $x = x_k + 1$ is:
$$y = m(x_k + 1) + c$$

Calculate the vertical distance from the true line to the lower pixel and upper pixel:
$$d_1 = y - y_k = m(x_k + 1) + c - y_k$$
$$d_2 = (y_k + 1) - y = y_k + 1 - [m(x_k + 1) + c]$$

The difference between these two separation distances is:
$$d_1 - d_2 = 2m(x_k + 1) + 2c - 2y_k - 1$$

Substitute $m = \frac{\Delta y}{\Delta x}$:
$$d_1 - d_2 = 2 \frac{\Delta y}{\Delta x}(x_k + 1) + 2c - 2y_k - 1$$

To eliminate the division by $\Delta x$, define the **decision parameter** $p_k = \Delta x (d_1 - d_2)$:
$$p_k = 2\Delta y \cdot x_k - 2\Delta x \cdot y_k + C, \quad \text{where } C = 2\Delta y + \Delta x(2c - 1)$$

Notice that $C$ is a constant independent of pixel step $k$.

#### Evaluating Successive Decision Parameters
At step $k+1$, the decision parameter is:
$$p_{k+1} = 2\Delta y \cdot x_{k+1} - 2\Delta x \cdot y_{k+1} + C$$
Subtract $p_k$:
$$p_{k+1} - p_k = 2\Delta y (x_{k+1} - x_k) - 2\Delta x (y_{k+1} - y_k)$$
Since $x_{k+1} = x_k + 1$, this simplifies to:
$$p_{k+1} = p_k + 2\Delta y - 2\Delta x(y_{k+1} - y_k)$$

#### Conditional Update Rules:
1. **If $p_k < 0$**:
   - $d_1 < d_2$, meaning the true line is closer to the lower pixel $y_k$.
   - Select pixel $(x_k + 1, y_k)$. Here $y_{k+1} - y_k = 0$.
   - Update:
     $$p_{k+1} = p_k + 2\Delta y$$
2. **If $p_k \ge 0$**:
   - $d_1 \ge d_2$, meaning the true line is closer to (or equidistant to) the upper pixel $y_k + 1$.
   - Select pixel $(x_k + 1, y_k + 1)$. Here $y_{k+1} - y_k = 1$.
   - Update:
     $$p_{k+1} = p_k + 2\Delta y - 2\Delta x$$

#### Initial Decision Parameter $p_0$:
Evaluate $p_k$ at the starting endpoint $(x_0, y_0)$:
$$c = y_0 - m x_0 = y_0 - \frac{\Delta y}{\Delta x} x_0$$
$$p_0 = \Delta x \left[ 2\frac{\Delta y}{\Delta x}(x_0 + 1) + 2\left(y_0 - \frac{\Delta y}{\Delta x} x_0\right) - 2y_0 - 1 \right]$$
$$p_0 = 2\Delta y(x_0 + 1) + 2\Delta x y_0 - 2\Delta y x_0 - 2\Delta x y_0 - \Delta x$$
$$p_0 = 2\Delta y - \Delta x$$

#### Derivation for Steep Slope ($m \ge 1$):
When the slope is steep ($m \ge 1$), swap roles of $x$ and $y$:
- Increment $y$ by 1 at each step: $y_{k+1} = y_k + 1$.
- Candidate pixels are $(x_k, y_k + 1)$ and $(x_k + 1, y_k + 1)$.
- Initial decision parameter:
  $$p_0 = 2\Delta x - \Delta y$$
- If $p_k < 0$: Choose $x_{k+1} = x_k$; update: $p_{k+1} = p_k + 2\Delta x$.
- If $p_k \ge 0$: Choose $x_{k+1} = x_k + 1$; update: $p_{k+1} = p_k + 2\Delta x - 2\Delta y$.

---

## 2. Example: Bresenham Decision Geometry
```
y_k + 1 +-------------------+ (x_k + 1, y_k + 1) [NE Pixel]
        |                   |   ▲
        |                   |   | d_2
        |         *=========|===+=== True mathematical line: y = m(x+1) + c
        |                   |   | d_1
    y_k +-------------------+ (x_k + 1, y_k)     [E Pixel]
        x_k               x_k + 1
```
- If $d_1 < d_2 \implies p_k < 0 \implies$ Pick Lower (East) Pixel $(x_k + 1, y_k)$.
- If $d_1 \ge d_2 \implies p_k \ge 0 \implies$ Pick Upper (North-East) Pixel $(x_k + 1, y_k + 1)$.

---

## 3. Applications & Use Cases
1. **GPU Rasterizer Fixed-Function Hardware**: Modern graphics hardware silicon (NVIDIA Raster Engine, AMD RDNA) implements Bresenham variants in pure integer logic gates to generate fragments from triangle bounding edges at hundreds of billions of pixels per second.
2. **Computer Numerical Control (CNC) Machining & 3D Printing**: Stepper motors controlling the tool head on CNC milling machines and FDM 3D printers execute Bresenham's incremental algorithm to synchronize the simultaneous stepping of X-axis and Y-axis motor pulses without floating-point error drift.
3. **Ray-Marching and Voxel Traversal**: Fast voxel traversal algorithms (Amanatides & Woo grid traversal) use Bresenham-style integer decision parameters to step ray packets through 3D voxel grids in volumetric rendering and game collision detection.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Bresenham Line Scan Conversion ($0 < m < 1$) [KTU June 2024 / Dec 2023 - 9 Marks]
**Problem**:
Digitize the line with endpoints $(2, 2)$ and $(10, 7)$ using Bresenham's line drawing algorithm. Tabulate the step index $k$, decision parameter $p_k$, and chosen pixel coordinates $(x_{k+1}, y_{k+1})$.

**Step-by-step Solution**:
1. **Parameter Setup**:
   $$(x_0, y_0) = (2, 2), \quad (x_n, y_n) = (10, 7)$$
   $$\Delta x = 10 - 2 = 8, \quad \Delta y = 7 - 2 = 5$$
   $$\text{Slope } m = \frac{5}{8} = 0.625 \implies 0 < m < 1$$
   $$\text{Constant terms: } 2\Delta y = 2(5) = 10, \quad 2\Delta y - 2\Delta x = 10 - 16 = -6$$
   $$\text{Initial decision parameter: } p_0 = 2\Delta y - \Delta x = 10 - 8 = 2$$
2. **Initial Pixel**: Plot $(x_0, y_0) = (2, 2)$.
3. **Step-by-step Iteration**:

| Step $k$ | Decision $p_k$ | Condition | Action / Next Pixel $(x_{k+1}, y_{k+1})$ | Next Parameter $p_{k+1}$ |
|---|---|---|---|---|
| 0 | $2$ | $p_0 \ge 0$ | $x_1 = 3, y_1 = 3 \implies \mathbf{(3, 3)}$ | $p_1 = 2 + (-6) = -4$ |
| 1 | $-4$ | $p_1 < 0$ | $x_2 = 4, y_2 = 3 \implies \mathbf{(4, 3)}$ | $p_2 = -4 + 10 = 6$ |
| 2 | $6$ | $p_2 \ge 0$ | $x_3 = 5, y_3 = 4 \implies \mathbf{(5, 4)}$ | $p_3 = 6 + (-6) = 0$ |
| 3 | $0$ | $p_3 \ge 0$ | $x_4 = 6, y_4 = 5 \implies \mathbf{(6, 5)}$ | $p_4 = 0 + (-6) = -6$ |
| 4 | $-6$ | $p_4 < 0$ | $x_5 = 7, y_5 = 5 \implies \mathbf{(7, 5)}$ | $p_5 = -6 + 10 = 4$ |
| 5 | $4$ | $p_5 \ge 0$ | $x_6 = 8, y_6 = 6 \implies \mathbf{(8, 6)}$ | $p_6 = 4 + (-6) = -2$ |
| 6 | $-2$ | $p_6 < 0$ | $x_7 = 9, y_7 = 6 \implies \mathbf{(9, 6)}$ | $p_7 = -2 + 10 = 8$ |
| 7 | $8$ | $p_7 \ge 0$ | $x_8 = 10, y_8 = 7 \implies \mathbf{(10, 7)}$ | Algorithm Terminates |

**Final Raster Pixel Sequence**:
$$\mathbf{(2, 2) \to (3, 3) \to (4, 3) \to (5, 4) \to (6, 5) \to (7, 5) \to (8, 6) \to (9, 6) \to (10, 7)}$$

---

### Example 2: Bresenham Line Scan Conversion for Steep Slope ($m > 1$) [KTU May 2019 / Jan 2021 Pattern]
**Problem**:
Digitize the line with endpoints $(1, 1)$ and $(4, 8)$ using Bresenham's line algorithm.

**Step-by-step Solution**:
1. **Parameter Setup**:
   $$(x_0, y_0) = (1, 1), \quad (x_n, y_n) = (4, 8)$$
   $$\Delta x = 4 - 1 = 3, \quad \Delta y = 8 - 1 = 7$$
   $$\text{Slope } m = \frac{7}{3} \approx 2.33 > 1 \implies \text{Steep line (increment along } y)$$
   $$\text{Constant terms: } 2\Delta x = 2(3) = 6, \quad 2\Delta x - 2\Delta y = 6 - 14 = -8$$
   $$\text{Initial decision parameter: } p_0 = 2\Delta x - \Delta y = 6 - 7 = -1$$
2. **Initial Pixel**: Plot $(x_0, y_0) = (1, 1)$.
3. **Step-by-step Iteration**:

| Step $k$ | Decision $p_k$ | Condition | Action / Next Pixel $(x_{k+1}, y_{k+1})$ | Next Parameter $p_{k+1}$ |
|---|---|---|---|---|
| 0 | $-1$ | $p_0 < 0$ | $y_1 = 2, x_1 = 1 \implies \mathbf{(1, 2)}$ | $p_1 = -1 + 6 = 5$ |
| 1 | $5$ | $p_1 \ge 0$ | $y_2 = 3, x_2 = 2 \implies \mathbf{(2, 3)}$ | $p_2 = 5 + (-8) = -3$ |
| 2 | $-3$ | $p_2 < 0$ | $y_3 = 4, x_3 = 2 \implies \mathbf{(2, 4)}$ | $p_3 = -3 + 6 = 3$ |
| 3 | $3$ | $p_3 \ge 0$ | $y_4 = 5, x_4 = 3 \implies \mathbf{(3, 5)}$ | $p_4 = 3 + (-8) = -5$ |
| 4 | $-5$ | $p_4 < 0$ | $y_5 = 6, x_5 = 3 \implies \mathbf{(3, 6)}$ | $p_5 = -5 + 6 = 1$ |
| 5 | $1$ | $p_5 \ge 0$ | $y_6 = 7, x_6 = 4 \implies \mathbf{(4, 7)}$ | $p_6 = 1 + (-8) = -7$ |
| 6 | $-7$ | $p_6 < 0$ | $y_7 = 8, x_7 = 4 \implies \mathbf{(4, 8)}$ | Algorithm Terminates |

**Final Raster Pixel Sequence**:
$$\mathbf{(1, 1) \to (1, 2) \to (2, 3) \to (2, 4) \to (3, 5) \to (3, 6) \to (4, 7) \to (4, 8)}$$

---

### Example 3: Comparison Trace between DDA and Bresenham [KTU Dec 2018 / Dec 2020 Pattern]
**Problem**:
Trace the DDA algorithm for endpoints $(2, 3)$ and $(8, 6)$ and verify whether its chosen pixels match Bresenham's algorithm.

**Step-by-step Solution**:
1. **DDA Computation**:
   $$\Delta x = 6, \quad \Delta y = 3, \quad m = \frac{3}{6} = 0.5$$
   - Since $m \le 1$, step $\Delta x = 1, \Delta y = 0.5$.
   - $k=0: x=2, y=3.0 \to \text{round}(3.0) = 3 \implies \mathbf{(2, 3)}$
   - $k=1: x=3, y=3.5 \to \text{round}(3.5) = 4 \implies \mathbf{(3, 4)}$
   - $k=2: x=4, y=4.0 \to \text{round}(4.0) = 4 \implies \mathbf{(4, 4)}$
   - $k=3: x=5, y=4.5 \to \text{round}(4.5) = 5 \implies \mathbf{(5, 5)}$
   - $k=4: x=6, y=5.0 \to \text{round}(5.0) = 5 \implies \mathbf{(6, 5)}$
   - $k=5: x=7, y=5.5 \to \text{round}(5.5) = 6 \implies \mathbf{(7, 6)}$
   - $k=6: x=8, y=6.0 \to \text{round}(6.0) = 6 \implies \mathbf{(8, 6)}$
2. **Bresenham Computation**:
   $$p_0 = 2\Delta y - \Delta x = 2(3) - 6 = 0$$
   - $p_0 = 0 \ge 0 \implies \mathbf{(3, 4)}, p_1 = 0 + 6 - 12 = -6$
   - $p_1 = -6 < 0 \implies \mathbf{(4, 4)}, p_2 = -6 + 6 = 0$
   - $p_2 = 0 \ge 0 \implies \mathbf{(5, 5)}, p_3 = 0 - 6 = -6$
   - $p_3 = -6 < 0 \implies \mathbf{(6, 5)}, p_4 = -6 + 6 = 0$
   - $p_4 = 0 \ge 0 \implies \mathbf{(7, 6)}, p_5 = 0 - 6 = -6$
   - $p_5 = -6 < 0 \implies \mathbf{(8, 6)}$
3. **Conclusion**:
   Both algorithms produce the identical pixel sequence $\mathbf{(2, 3), (3, 4), (4, 4), (5, 5), (6, 5), (7, 6), (8, 6)}$, but Bresenham avoids all floating-point math and rounding operations.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / December 2021 - 4 Marks]
**Question**:
Write the DDA line drawing algorithm. Which algorithm is better for line drawing and why?

**Solution**:
1. **DDA Algorithm Pseudocode**:
   ```c
   void DrawLineDDA(int x0, int y0, int x1, int y1) {
       int dx = x1 - x0;
       int dy = y1 - y0;
       int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);
       
       float xInc = (float)dx / steps;
       float yInc = (float)dy / steps;
       
       float x = x0;
       float y = y0;
       
       for (int i = 0; i <= steps; i++) {
           SetPixel((int)round(x), (int)round(y));
           x += xInc;
           y += yInc;
       }
   }
   ```
2. **Which Algorithm is Better and Why**:
   **Bresenham's algorithm is significantly better than DDA** for the following three technical reasons:
   - **Pure Integer Arithmetic**: Bresenham operates exclusively using integer addition, subtraction, and bitwise shift operations ($\times 2$). It requires zero floating-point arithmetic.
   - **Zero Round-off Error**: In DDA, accumulating fractional numbers in floating-point registers leads to truncation and rounding errors that drift endpoints away from the true path. Bresenham tracks the exact error using an integer decision parameter $p_k$.
   - **Silicon Hardware Efficiency**: Fixed-point/integer ALUs in graphics hardware process integer additions in a single clock cycle, whereas floating-point division and rounding incur multi-cycle pipelines and higher power consumption.

---

### Question 2 [KTU December 2019 / June 2022 - 9 Marks]
**Question**:
Derive Bresenham's line drawing algorithm for a line segment with slope $0 < m < 1$. Scan convert the line segment connecting $(2, 3)$ and $(9, 7)$.

**Solution**:
1. **Derivation**:
   *(Full step-by-step mathematical derivation as detailed in Section 1 above)*:
   - True line: $y = m(x_k + 1) + c$.
   - Separation distances: $d_1 = y - y_k = m(x_k + 1) + c - y_k$, and $d_2 = (y_k + 1) - y = y_k + 1 - m(x_k + 1) - c$.
   - Difference: $d_1 - d_2 = 2m(x_k + 1) - 2y_k + 2c - 1$.
   - Multiplying by $\Delta x$ yields decision parameter $p_k = 2\Delta y \cdot x_k - 2\Delta x \cdot y_k + C$.
   - Recurrence: $p_{k+1} - p_k = 2\Delta y - 2\Delta x(y_{k+1} - y_k)$.
   - If $p_k < 0 \implies y_{k+1} = y_k \implies p_{k+1} = p_k + 2\Delta y$.
   - If $p_k \ge 0 \implies y_{k+1} = y_k + 1 \implies p_{k+1} = p_k + 2\Delta y - 2\Delta x$.
   - Initial value: $p_0 = 2\Delta y - \Delta x$.

2. **Scan Conversion for Endpoints $(2, 3)$ and $(9, 7)$**:
   - $\Delta x = 9 - 2 = 7$, $\Delta y = 7 - 3 = 4$.
   - $m = 4/7 \approx 0.571$ ($0 < m < 1$).
   - $2\Delta y = 8$, $2\Delta y - 2\Delta x = 8 - 14 = -6$.
   - Initial decision parameter: $p_0 = 2\Delta y - \Delta x = 8 - 7 = 1$.
   - Initial point: Plot $(2, 3)$.
   - Trace Table:
     - $k=0: p_0 = 1 \ge 0 \implies \text{Plot } \mathbf{(3, 4)}, p_1 = 1 + (-6) = -5$
     - $k=1: p_1 = -5 < 0 \implies \text{Plot } \mathbf{(4, 4)}, p_2 = -5 + 8 = 3$
     - $k=2: p_2 = 3 \ge 0 \implies \text{Plot } \mathbf{(5, 5)}, p_3 = 3 + (-6) = -3$
     - $k=3: p_3 = -3 < 0 \implies \text{Plot } \mathbf{(6, 5)}, p_4 = -3 + 8 = 5$
     - $k=4: p_4 = 5 \ge 0 \implies \text{Plot } \mathbf{(7, 6)}, p_5 = 5 + (-6) = -1$
     - $k=5: p_5 = -1 < 0 \implies \text{Plot } \mathbf{(8, 6)}, p_6 = -1 + 8 = 7$
     - $k=6: p_6 = 7 \ge 0 \implies \text{Plot } \mathbf{(9, 7)}$
   - **Plotted Pixels**: $\mathbf{(2, 3), (3, 4), (4, 4), (5, 5), (6, 5), (7, 6), (8, 6), (9, 7)}$.

