# Two-Dimensional Clipping: Cohen-Sutherland and Midpoint Subdivision

## 1. Explanation
Clipping is the computational procedure in computer graphics that removes parts of geometric primitives (points, lines, curves, polygons) lying outside a specified viewing region (the clipping window).

### Why Clipping is Fundamental
1. **Computational Efficiency**: Avoids running expensive rasterization, lighting, and fragment shading on geometry that cannot be viewed on screen.
2. **Memory Safety**: Prevents attempts to write pixels outside the physical bounds of the frame buffer memory.

---

### Point Clipping
A point $P(x, y)$ is saved (accepted) if and only if it satisfies all four boundary inequality conditions:
$$x_{w\min} \le x \le x_{w\max}$$
$$y_{w\min} \le y \le y_{w\max}$$
Otherwise, the point is discarded (clipped).

---

### Line Clipping: Cohen-Sutherland Algorithm
The Cohen-Sutherland algorithm accelerates line clipping by using **4-bit region codes (outcodes)** to quickly identify lines that are completely visible (trivial accept) or completely outside (trivial reject) before calculating any floating-point intersection coordinates.

#### Region Code (Outcode) Generation
The 2D plane is divided into nine regions by extending the four boundary edges of the rectangular clipping window: $x = x_{w\min}, x = x_{w\max}, y = y_{w\min}, y = y_{w\max}$.
Every endpoint $(x, y)$ is assigned a 4-bit binary code `[b4 b3 b2 b1]`:
$$\text{Bit 4: Top (T)} = \begin{cases} 1 & \text{if } y > y_{w\max} \\ 0 & \text{otherwise} \end{cases}$$
$$\text{Bit 3: Bottom (B)} = \begin{cases} 1 & \text{if } y < y_{w\min} \\ 0 & \text{otherwise} \end{cases}$$
$$\text{Bit 2: Right (R)} = \begin{cases} 1 & \text{if } x > x_{w\max} \\ 0 & \text{otherwise} \end{cases}$$
$$\text{Bit 1: Left (L)} = \begin{cases} 1 & \text{if } x < x_{w\min} \\ 0 & \text{otherwise} \end{cases}$$

#### The Nine 2D Region Codes:
```
     1001 (Top-Left)    | 1000 (Top)    | 1010 (Top-Right)
   ─────────────────────┼───────────────┼──────────────────── y_wmax
     0001 (Left)        | 0000 (WINDOW) | 0010 (Right)
   ─────────────────────┼───────────────┼──────────────────── y_wmin
     0101 (Bottom-Left) | 0100 (Bottom) | 0110 (Bottom-Right)
                        |               |
                      x_wmin          x_wmax
```

#### Trivial Tests (Bitwise Logic):
Let $C_1$ and $C_2$ be the 4-bit outcodes of line endpoints $P_1$ and $P_2$:
1. **Trivial Acceptance**:
   $$(C_1 = 0000) \ \text{AND} \ (C_2 = 0000) \implies (C_1 \mid C_2) == 0$$
   Both endpoints lie completely inside the clipping window. The line is displayed in its entirety without intersection calculations.
2. **Trivial Rejection**:
   $$(C_1 \ \& \ C_2) \ne 0000$$
   Both endpoints share a common external half-space (e.g. both are to the Left, or both are above Top). The line lies completely outside the window and is discarded immediately.
3. **Partial Intersection (Non-Trivial Case)**:
   $$(C_1 \mid C_2) \ne 0 \quad \text{and} \quad (C_1 \ \& \ C_2) == 0$$
   The line crosses one or more window boundaries.

#### Intersection Point Calculation:
For an endpoint outside a boundary, compute the intersection with the corresponding window boundary line using the line slope $m = \frac{y_2 - y_1}{x_2 - x_1}$:
- **Intersection with Top boundary ($y = y_{w\max}$)**:
  $$x = x_1 + \frac{1}{m}(y_{w\max} - y_1), \quad y = y_{w\max}$$
- **Intersection with Bottom boundary ($y = y_{w\min}$)**:
  $$x = x_1 + \frac{1}{m}(y_{w\min} - y_1), \quad y = y_{w\min}$$
- **Intersection with Right boundary ($x = x_{w\max}$)**:
  $$y = y_1 + m(x_{w\max} - x_1), \quad x = x_{w\max}$$
- **Intersection with Left boundary ($x = x_{w\min}$)**:
  $$y = y_1 + m(x_{w\min} - x_1), \quad x = x_{w\min}$$

The outside endpoint is replaced by the calculated intersection point, its outcode is re-evaluated, and the loop repeats until trivial accept or reject is reached.

---

### Midpoint Subdivision Algorithm
The Midpoint Subdivision algorithm applies a **binary search divide-and-conquer strategy** to locate boundary intersections using only integer additions and right-shifts ($\div 2$), completely avoiding floating-point division by slope $m$.

#### Step-by-Step Procedure:
1. Compute outcodes $C_1$ and $C_2$ for endpoints $P_1$ and $P_2$.
2. Test for trivial accept ($C_1 \mid C_2 = 0$) or trivial reject ($C_1 \ \& \ C_2 \ne 0$).
3. If non-trivial, compute the spatial midpoint:
   $$P_m = \left( \frac{x_1 + x_2}{2}, \ \frac{y_1 + y_2}{2} \right)$$
4. Subdivide the line into two subsegments: $P_1 P_m$ and $P_m P_2$.
5. Recursively apply the algorithm to each subsegment until the segments shrink to a single pixel width (terminal pixel resolution) or reach trivial acceptance/rejection.

---

## 2. Example: Cohen-Sutherland Outcode and Clipping Trace
```
             P_1(20, 80) [Outcode 1000]
                 \
                  \  I_1 (Intersection with Top: y = 60)
    +--------------*----------------+ (y_wmax = 60)
    |               \               |
    |                \              |
    |                 \             |
    |                  * I_2 (Intersection with Right: x = 70)
    +-------------------\-----------+ (y_wmin = 20)
    (x_wmin = 30)        \
                          P_2(90, 10) [Outcode 0110]
```
- Active segment after clipping: $I_1 I_2$.

---

## 3. Applications & Use Cases
1. **Interactive Canvas Viewports (Figma, Adobe Illustrator)**: Zooming and panning constantly clip hundreds of thousands of vector bezier control paths against the visible screen viewport using Cohen-Sutherland outcode tests.
2. **Hardware Clipping Units in Modern GPUs**: Dedicated silicon clipping stages (Vertex Processing Unit) evaluate 4D clip space coordinates $[x, y, z, w]$ using generalized homogeneous outcodes before rasterization.
3. **Geographic GIS Vector Layer Rendering**: Map servers (Mapbox, OpenStreetMap) clip road network polyline segments against spatial tile boundaries.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Cohen-Sutherland Line Clipping Trace [KTU January 2023 / June 2022 - 9 Marks]
**Problem**:
Use the Cohen-Sutherland algorithm to clip the line segment joining $P_1(70, 20)$ and $P_2(100, 10)$ against a rectangular clipping window with lower-left corner $(50, 10)$ and upper-right corner $(80, 40)$.

**Step-by-step Solution**:
1. **Window Parameters**:
   $$x_{w\min} = 50, \quad x_{w\max} = 80, \quad y_{w\min} = 10, \quad y_{w\max} = 40$$
2. **Calculate Endpoints Outcodes**:
   - For $P_1(70, 20)$:
     - $y = 20 \le y_{w\max}(40) \implies \text{Top} = 0$
     - $y = 20 \ge y_{w\min}(10) \implies \text{Bottom} = 0$
     - $x = 70 \le x_{w\max}(80) \implies \text{Right} = 0$
     - $x = 70 \ge x_{w\min}(50) \implies \text{Left} = 0$
     - Outcode: $C_1 = \mathbf{0000}$ (Inside window).
   - For $P_2(100, 10)$:
     - $y = 10 \le 40 \implies \text{Top} = 0$
     - $y = 10 \ge 10 \implies \text{Bottom} = 0$
     - $x = 100 > 80 \implies \text{Right} = 1$
     - $x = 100 \ge 50 \implies \text{Left} = 0$
     - Outcode: $C_2 = \mathbf{0010}$ (To the right).
3. **Trivial Tests**:
   - $C_1 \mid C_2 = 0000 \mid 0010 = 0010 \ne 0 \implies$ Not trivially accepted.
   - $C_1 \ \& \ C_2 = 0000 \ \& \ 0010 = 0000 \implies$ Not trivially rejected.
   - The line crosses the **Right boundary** ($x = 80$).
4. **Compute Intersection with Right Boundary ($x = x_{w\max} = 80$)**:
   $$\text{Slope } m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{10 - 20}{100 - 70} = \frac{-10}{30} = -\frac{1}{3}$$
   $$y = y_1 + m(x_{w\max} - x_1) = 20 + \left(-\frac{1}{3}\right)(80 - 70) = 20 - \frac{10}{3} = \frac{50}{3} \approx 16.67$$
   Intersection point: $I_1\left(80, \frac{50}{3}\right) \approx \mathbf{(80, 16.67)}$.
5. **Re-evaluate Outcode for $I_1(80, 16.67)$**:
   $$x = 80 \le 80, \ x \ge 50, \ y = 16.67 \in [10, 40] \implies C_{I_1} = \mathbf{0000}$$
6. **Final Acceptance**:
   Both endpoints now have outcodes `0000`.
   The clipped line segment extends from $\mathbf{P_1(70, 20)}$ to $\mathbf{I_1(80, 16.67)}$.

---

### Example 2: Midpoint Subdivision Trace [KTU January 2023 - 9 Marks]
**Problem**:
A clipping window $ABCD$ is specified as $A(0, 0), B(40, 0), C(40, 40)$, and $D(0, 40)$. Using the Midpoint Subdivision algorithm, find the visible portion of the line segment joining $P(-10, 20)$ and $Q(50, 10)$.

**Step-by-step Solution**:
1. **Window Extents**: $x \in [0, 40], \ y \in [0, 40]$.
2. **Initial Outcodes**:
   - $P(-10, 20): x = -10 < 0 \implies \text{Outcode } C_P = \mathbf{0001}$ (Left).
   - $Q(50, 10): x = 50 > 40 \implies \text{Outcode } C_Q = \mathbf{0010}$ (Right).
   - $C_P \ \& \ C_Q = 0000$, non-trivial case.
3. **Midpoint Subdivision Step 1**:
   $$M_1 = \left(\frac{-10 + 50}{2}, \frac{20 + 10}{2}\right) = (20, 15)$$
   - Outcode of $M_1(20, 15) = \mathbf{0000}$ (Inside).
   - Line is subdivided into $P M_1$ and $M_1 Q$.
4. **Subsegment $P(-10, 20)$ to $M_1(20, 15)$**:
   - $M_2 = \left(\frac{-10 + 20}{2}, \frac{20 + 15}{2}\right) = (5, 17.5)$.
   - Outcode of $M_2(5, 17.5) = \mathbf{0000}$ (Inside).
   - Next midpoint: $M_3 = \left(\frac{-10 + 5}{2}, \frac{20 + 17.5}{2}\right) = (-2.5, 18.75) \implies \text{Left (0001)}$.
   - Binary search converges to Left boundary $x = 0$:
     $$y_{\text{left}} = 20 + \left(\frac{15 - 20}{20 - (-10)}\right)(0 - (-10)) = 20 + \left(-\frac{5}{30}\right)(10) = 20 - 1.67 = \mathbf{18.33}$$
     Left boundary intersection: $I_{\text{left}}(0, 18.33)$.
5. **Subsegment $M_1(20, 15)$ to $Q(50, 10)$**:
   - Binary search converges to Right boundary $x = 40$:
     $$y_{\text{right}} = 15 + \left(\frac{10 - 15}{50 - 20}\right)(40 - 20) = 15 + \left(-\frac{5}{30}\right)(20) = 15 - 3.33 = \mathbf{11.67}$$
     Right boundary intersection: $I_{\text{right}}(40, 11.67)$.
6. **Result**: The visible clipped segment is from $\mathbf{(0, 18.33)}$ to $\mathbf{(40, 11.67)}$.

---

### Example 3: Trivial Rejection Bitwise Proof [KTU Dec 2019 Pattern]
**Problem**:
Endpoints $P_1(15, 75)$ and $P_2(45, 95)$ are to be clipped against a window $[20, 60] \times [20, 60]$.
Show using bitwise logic why the Cohen-Sutherland algorithm trivially rejects this line without computing any intersection.

**Step-by-step Solution**:
1. Window bounds: $x \in [20, 60], y \in [20, 60]$.
2. Endpoint $P_1(15, 75)$:
   - $y = 75 > 60 \implies \text{Top} = 1$
   - $y = 75 \ge 20 \implies \text{Bottom} = 0$
   - $x = 15 \le 60 \implies \text{Right} = 0$
   - $x = 15 < 20 \implies \text{Left} = 1$
   - Outcode $C_1 = \mathbf{1001}$.
3. Endpoint $P_2(45, 95)$:
   - $y = 95 > 60 \implies \text{Top} = 1$
   - $y = 95 \ge 20 \implies \text{Bottom} = 0$
   - $x = 45 \le 60 \implies \text{Right} = 0$
   - $x = 45 \ge 20 \implies \text{Left} = 0$
   - Outcode $C_2 = \mathbf{1000}$.
4. Bitwise `AND` Evaluation:
   $$C_1 \ \& \ C_2 = 1001_2 \ \& \ 1000_2 = \mathbf{1000_2} \ne 0000_2$$
5. Conclusion: Since the bitwise `AND` result is non-zero, both endpoints share the property that they lie entirely above the Top clipping boundary ($y > 60$). The line is **trivially rejected** with zero floating-point division operations.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / January 2023 - 9 Marks]
**Question**:
Explain the Cohen Sutherland line clipping algorithm. Describe how outcodes are generated and explain the trivial accept and trivial reject conditions.

**Solution**:
1. **Outcode Generation**:
   The Cohen-Sutherland algorithm divides 2D space into 9 regions using the 4 boundaries of the rectangular clipping window: $x = x_{\min}, x = x_{\max}, y = y_{\min}, y = y_{\max}$.
   Every line endpoint $(x, y)$ is assigned a 4-bit binary outcode `[Top Bottom Right Left]`:
   - Bit 4 (Top): Set to 1 if $y > y_{\max}$, else 0.
   - Bit 3 (Bottom): Set to 1 if $y < y_{\min}$, else 0.
   - Bit 2 (Right): Set to 1 if $x > x_{\max}$, else 0.
   - Bit 1 (Left): Set to 1 if $x < x_{\min}$, else 0.
   Points inside the window have the outcode `0000`.
2. **Trivial Tests**:
   - **Trivial Accept**: If both endpoints have outcodes equal to `0000` ($(C_1 \mid C_2) == 0$), the line segment lies entirely inside the window and is rendered immediately.
   - **Trivial Reject**: If the bitwise logical `AND` of the two outcodes is non-zero ($(C_1 \ \& \ C_2) \ne 0$), both points share a common outside region (both above top, both below bottom, both right, or both left). The line lies completely outside and is discarded.
3. **Clipping Iteration**:
   If a line cannot be trivially accepted or rejected, an endpoint lying outside (outcode $\ne 0000$) is selected. The algorithm intersects the line with the boundary corresponding to the set bit:
   - If Top bit is 1: $x = x_1 + \frac{1}{m}(y_{\max} - y_1), \ y = y_{\max}$.
   - If Bottom bit is 1: $x = x_1 + \frac{1}{m}(y_{\min} - y_1), \ y = y_{\min}$.
   - If Right bit is 1: $y = y_1 + m(x_{\max} - x_1), \ x = x_{\max}$.
   - If Left bit is 1: $y = y_1 + m(x_{\min} - x_1), \ x = x_{\min}$.
   The outside endpoint is replaced with the computed intersection point, its outcode is re-evaluated, and the process repeats until the line is either accepted or rejected.

---

### Question 2 [KTU December 2021 / December 2023 - 4 Marks]
**Question**:
What is the advantage of the Midpoint Subdivision algorithm over the Cohen-Sutherland line clipping algorithm?

**Solution**:
1. **Elimination of Floating-Point Division**:
   The Cohen-Sutherland algorithm requires computing intersection points using floating-point multiplication and division by the slope $m = \frac{\Delta y}{\Delta x}$. In hardware implementations or embedded processors lacking dedicated floating-point units (FPUs), division is a high-latency, multi-cycle operation.
2. **Binary Shift Arithmetic**:
   The Midpoint Subdivision algorithm replaces floating-point divisions with a binary search divide-and-conquer strategy. The midpoint $P_m = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$ is computed purely using integer addition and arithmetic right-shift operations (`>> 1`), which execute in a single clock cycle in digital logic.
3. **Hardware Suitability**:
   Midpoint subdivision is ideally suited for direct hardware implementation in FPGA and early raster display processors.

