# Two-Dimensional Clipping: Cohen-Sutherland, Midpoint Subdivision & Liang-Barsky

## 1. Explanation

Clipping is the fundamental computational process of removing (or trimming) parts of geometric primitives — points, line segments, polygons, text — that fall **outside** the visible window region. Everything that cannot be seen on screen must be discarded before rasterization, both for efficiency (don't waste GPU cycles on invisible pixels) and for correctness (don't write to memory outside the frame buffer bounds).

### The Clipping Window

A **clipping window** (also called the clip rectangle or viewport window in world coordinates) is a rectangular region defined by four boundary lines:
$$x_{\min} \le x \le x_{\max}, \qquad y_{\min} \le y \le y_{\max}$$

The objective is to find, for each geometric primitive, the portion that lies within this window.

---

### 1. Point Clipping

The simplest case. A point $P(x, y)$ is **visible** (retained) if and only if:
$$x_{\min} \le x \le x_{\max} \quad \text{AND} \quad y_{\min} \le y \le y_{\max}$$

Otherwise it is **clipped** (discarded).

---

### 2. Text Clipping

Three strategies for handling text primitives near window boundaries:

1. **All-or-Nothing String Clipping**: Accept or reject the entire text string based on whether the string's bounding box is entirely inside or entirely outside the window. Fast but coarse.
2. **All-or-Nothing Character Clipping**: Test each individual character's bounding box. Accept characters fully inside; reject characters fully outside. Characters partially overlapping the boundary are discarded.
3. **Component-Level (Pixel) Clipping**: Rasterize each character and then apply pixel clipping — only display individual pixels that fall within the window. Most precise, highest computational cost.

---

### 3. Cohen-Sutherland Line Clipping Algorithm

The Cohen-Sutherland algorithm (1967) uses **4-bit region codes (outcodes)** to quickly classify line endpoints, enabling fast trivial acceptance or rejection before computing any expensive intersection arithmetic.

#### Region Code Generation

The 2D plane is divided into 9 regions by extending all 4 window boundaries:

```
Region Map (bit order: Top Bottom Right Left):

      1001 (TL)  |  1000 (T)  |  1010 (TR)
  ───────────────┼────────────┼────────────── y_max
      0001 (L)   |  0000 (IN) |  0010 (R)
  ───────────────┼────────────┼────────────── y_min
      0101 (BL)  |  0100 (B)  |  0110 (BR)
                 |            |
               x_min        x_max
```

**Bit assignment** for endpoint $(x, y)$:
- **Bit 4 (T = Top)**: 1 if $y > y_{\max}$, else 0
- **Bit 3 (B = Bottom)**: 1 if $y < y_{\min}$, else 0
- **Bit 2 (R = Right)**: 1 if $x > x_{\max}$, else 0
- **Bit 1 (L = Left)**: 1 if $x < x_{\min}$, else 0

#### Trivial Tests (Bitwise, O(1))

Let $C_1$ and $C_2$ be the outcodes of the two line endpoints:

| Test | Condition | Meaning |
|---|---|---|
| **Trivial Accept** | $(C_1\ \text{OR}\ C_2) = 0000$ | Both points inside window — display the whole line |
| **Trivial Reject** | $(C_1\ \text{AND}\ C_2) \ne 0000$ | Both points on same side of some boundary — discard entirely |
| **Non-Trivial** | $(C_1\ \text{OR}\ C_2) \ne 0000$ AND $(C_1\ \text{AND}\ C_2) = 0000$ | Line crosses boundary — must clip |

#### Intersection Formulas

For the non-trivial case, select an **outside** endpoint (say, the one with non-zero outcode). Check its outcode bits in priority order (Top → Bottom → Right → Left) and compute intersection with the first active boundary:

| Boundary | Intersection Formula |
|---|---|
| **Top** ($y = y_{\max}$) | $x = x_1 + \frac{1}{m}(y_{\max} - y_1)$, $\quad y = y_{\max}$ |
| **Bottom** ($y = y_{\min}$) | $x = x_1 + \frac{1}{m}(y_{\min} - y_1)$, $\quad y = y_{\min}$ |
| **Right** ($x = x_{\max}$) | $y = y_1 + m(x_{\max} - x_1)$, $\quad x = x_{\max}$ |
| **Left** ($x = x_{\min}$) | $y = y_1 + m(x_{\min} - x_1)$, $\quad x = x_{\min}$ |

Where slope $m = \frac{y_2 - y_1}{x_2 - x_1}$.

The outside endpoint is **replaced** by the intersection point, its outcode is **re-evaluated**, and the loop repeats until trivial accept or trivial reject.

#### Algorithm Pseudocode

```
CohenSutherland(P1(x1,y1), P2(x2,y2), window):
  while True:
    C1 = ComputeOutcode(x1, y1)
    C2 = ComputeOutcode(x2, y2)
    
    if (C1 OR C2) == 0:          // Both inside
        Accept and display P1→P2
        break
    elif (C1 AND C2) != 0:       // Both outside same region
        Reject line
        break
    else:                        // Partial intersection
        // Choose outside endpoint
        C_out = C1 if C1 != 0 else C2
        
        if Top bit of C_out:
            x = x1 + (1/m)*(ymax - y1); y = ymax
        elif Bottom bit:
            x = x1 + (1/m)*(ymin - y1); y = ymin
        elif Right bit:
            y = y1 + m*(xmax - x1);     x = xmax
        elif Left bit:
            y = y1 + m*(xmin - x1);     x = xmin
        
        // Replace outside endpoint
        if C_out == C1: (x1, y1) = (x, y)
        else:           (x2, y2) = (x, y)
```

**Time complexity**: $O(1)$ per line (bounded number of boundary intersections — at most 4 clip boundaries).

---

### 4. Midpoint Subdivision Algorithm

An alternative line clipping method using **binary search** instead of slope computation. Completely avoids floating-point division.

**Procedure:**
1. Compute outcodes $C_1$, $C_2$ for $P_1$, $P_2$.
2. Trivial accept/reject test (same as Cohen-Sutherland).
3. If non-trivial, compute midpoint: $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$
4. Subdivide into $P_1 M$ and $M P_2$; apply recursively to each half.
5. Continue until each sub-segment is trivially accepted or rejected (terminates when segment is 1 pixel long).

**Key advantage**: Midpoint computation uses only **integer addition and right-shift** (`x >> 1`). No division by slope. Ideal for hardware with no FPU.

**Key disadvantage**: Requires many iterations (depth = $\log_2(\text{line length in pixels})$) compared to Cohen-Sutherland's direct intersection.

---

### 5. Liang-Barsky Algorithm

A parametric approach that is **more efficient than Cohen-Sutherland** for lines that need clipping (fewer multiplications, no slope).

**Parametric line representation**:
$$P(t) = P_1 + t(P_2 - P_1), \quad t \in [0, 1]$$
$$x(t) = x_1 + t \cdot \Delta x, \quad y(t) = y_1 + t \cdot \Delta y$$

**Four boundary inequalities** (the line must satisfy all four):
$$x_{\min} \le x_1 + t \cdot \Delta x \le x_{\max}$$
$$y_{\min} \le y_1 + t \cdot \Delta y \le y_{\max}$$

Rewritten as $p_k t \le q_k$ for $k = 1, 2, 3, 4$:
- $k=1$ (Left): $p_1 = -\Delta x$, $q_1 = x_1 - x_{\min}$
- $k=2$ (Right): $p_2 = +\Delta x$, $q_2 = x_{\max} - x_1$
- $k=3$ (Bottom): $p_3 = -\Delta y$, $q_3 = y_1 - y_{\min}$
- $k=4$ (Top): $p_4 = +\Delta y$, $q_4 = y_{\max} - y_1$

**$t$-interval clipping**:
- If $p_k = 0$ and $q_k < 0$: line is parallel to boundary $k$ and outside → **reject**.
- If $p_k < 0$: line enters window at boundary $k$ at $t = q_k/p_k$ → **update $t_1 = \max(t_1, q_k/p_k)$**
- If $p_k > 0$: line exits window at boundary $k$ at $t = q_k/p_k$ → **update $t_2 = \min(t_2, q_k/p_k)$**

If $t_1 > t_2$: line entirely outside → reject.  
Otherwise: visible segment from $P(t_1)$ to $P(t_2)$.

---

## 2. Example: Region Code Diagram

```
Window: x_min=20, x_max=90, y_min=20, y_max=70

P1(10,30) is Left of window:  code = 0001
P2(80,90) is Above window:    code = 1000
(C1 AND C2) = 0000 → non-trivial → clip

Intersection with Top (y=70):
  m = (90-30)/(80-10) = 60/70 = 6/7
  x = 10 + (1/(6/7))*(70-30) = 10 + (7/6)*40 = 10 + 46.67 = 56.67
  New P2 = (56.67, 70), code = 0000

Intersection with Left (y=70, now recalc from P1(10,30)):
  y = 30 + (6/7)*(20-10) = 30 + 60/7 = 30 + 8.57 = 38.57
  New P1 = (20, 38.57), code = 0000

Both codes = 0000 → Accept segment (20, 38.57) → (56.67, 70)
```

---

## 3. Applications & Use Cases

1. **GPU Hardware Clip Stage**: Modern GPU pipelines perform clipping in **clip space** (after the perspective divide, in $[-1,1]^3$) using the Sutherland-Hodgman algorithm for polygons. Line clipping is handled by Cohen-Sutherland-style bitwise outcodes extended to 6 bits (for 3D frustum planes).

2. **Interactive Vector Graphics Editors (Figma, Illustrator)**: When a user scrolls or zooms a canvas, millions of Bézier path segments must be clipped to the visible viewport. Cohen-Sutherland's fast trivial reject handles the common case (most segments are off-screen) in $O(1)$.

3. **GIS Map Tile Rendering (Mapbox, OpenStreetMap)**: Road networks, country borders, and waterways are polylines with millions of segments. Clipping each polyline to a 256×256 pixel tile boundary uses Cohen-Sutherland to discard segments outside tile bounds.

4. **Raytracing Bounding Box Tests**: Ray-AABB (axis-aligned bounding box) intersection in raytracing engines is mathematically equivalent to Liang-Barsky line clipping — the parametric $t$-interval approach identifies the entry and exit $t$-values of the ray intersecting the box.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Cohen-Sutherland — P1(10,30) to P2(80,90), Window (20,20)-(90,70) [KTU June 2024, Dec 2023 — 9 Marks]

**Window**: $x_{\min}=20, x_{\max}=90, y_{\min}=20, y_{\max}=70$

**Step 1 — Compute Outcodes:**

$P_1(10, 30)$:
- Top: $30 > 70$? No → 0
- Bottom: $30 < 20$? No → 0
- Right: $10 > 90$? No → 0
- Left: $10 < 20$? **Yes → 1**
- $C_1 = \mathbf{0001}$ (Left)

$P_2(80, 90)$:
- Top: $90 > 70$? **Yes → 1**
- Bottom: $90 < 20$? No → 0
- Right: $80 > 90$? No → 0
- Left: $80 < 20$? No → 0
- $C_2 = \mathbf{1000}$ (Top)

**Step 2 — Trivial Tests:**
- $C_1 \text{ OR } C_2 = 1001 \ne 0000$ → Not trivially accepted.
- $C_1 \text{ AND } C_2 = 0000$ → Not trivially rejected.
- Must clip.

**Step 3 — Clip $P_2$ (outside, Top bit set):**

$m = \frac{90-30}{80-10} = \frac{60}{70} = \frac{6}{7}$

Intersection with **Top boundary** ($y = 70$):
$$x = x_1 + \frac{1}{m}(y_{\max} - y_1) = 10 + \frac{7}{6}(70 - 30) = 10 + \frac{7 \times 40}{6} = 10 + 46.67 = 56.67$$
New $P_2 = (56.67, 70)$.

Re-evaluate: $56.67 \in [20,90]$, $70 = y_{\max}$ → $C_2 = \mathbf{0000}$ ✓

**Step 4 — Clip $P_1$ (outside, Left bit set):**

Intersection with **Left boundary** ($x = 20$):
$$y = y_1 + m(x_{\min} - x_1) = 30 + \frac{6}{7}(20 - 10) = 30 + \frac{60}{7} = 30 + 8.57 = 38.57$$
New $P_1 = (20, 38.57)$.

Re-evaluate: $20 = x_{\min}$, $38.57 \in [20,70]$ → $C_1 = \mathbf{0000}$ ✓

**Result**: Both outcodes = 0000 → Trivially accepted.
$$\boxed{\text{Visible segment: } (20,\ 38.57) \to (56.67,\ 70)}$$

---

### Example 2: Cohen-Sutherland — P1(70,20) to P2(100,10), Window (50,10)-(80,40) [KTU Jan 2023, June 2022 — 9 Marks]

**Window**: $x_{\min}=50, x_{\max}=80, y_{\min}=10, y_{\max}=40$

**Outcodes:**

$P_1(70,20)$: $20 \in [10,40]$, $70 \in [50,80]$ → $C_1 = \mathbf{0000}$ (Inside)

$P_2(100,10)$: $10 = y_{\min}$ (boundary, not outside), $100 > 80$ → $C_2 = \mathbf{0010}$ (Right)

**Trivial tests**: OR = 0010 ≠ 0; AND = 0000 → clip required.

**Clip $P_2$ (Right bit set):**

$m = \frac{10-20}{100-70} = \frac{-10}{30} = -\frac{1}{3}$

Intersection with **Right boundary** ($x = 80$):
$$y = y_1 + m(x_{\max} - x_1) = 20 + \left(-\frac{1}{3}\right)(80 - 70) = 20 - \frac{10}{3} = 20 - 3.33 = 16.67$$
New $P_2 = (80, 16.67)$.

$16.67 \in [10,40]$, $80 = x_{\max}$ → $C_2 = \mathbf{0000}$ ✓

Both $C_1 = C_2 = 0000$ → Accept.

$$\boxed{\text{Visible segment: } P_1(70,\ 20) \to (80,\ 16.67)}$$

---

### Example 3: Cohen-Sutherland — P(40,80) to Q(120,30), Window (20,20)-(60,40) [KTU Dec 2020 — 9 Marks]

**Window**: $x_{\min}=20, x_{\max}=60, y_{\min}=20, y_{\max}=40$

**Outcodes:**

$P(40,80)$: $80 > 40$ (Top=1), $40 \in [20,60]$ → $C_P = \mathbf{1000}$

$Q(120,30)$: $30 \in [20,40]$, $120 > 60$ (Right=1) → $C_Q = \mathbf{0010}$

AND = 0000, non-trivial.

$m = \frac{30-80}{120-40} = \frac{-50}{80} = -\frac{5}{8}$

**Iteration 1 — Clip $P$ (Top bit set, $y=40$):**
$$x = 40 + \frac{1}{-5/8}(40-80) = 40 + \frac{-8}{5} \times (-40) = 40 + 64 = 104$$

Wait — $x=104 > x_{\max}=60$. $C_P' = \mathbf{0010}$ (Right).

**Iteration 2 — Clip new $P(104,40)$ (Right bit set, $x=60$):**
$$y = y_P + m(x_{\max} - x_P) = 40 + \left(-\frac{5}{8}\right)(60-104) = 40 + \left(-\frac{5}{8}\right)(-44) = 40 + 27.5 = 67.5$$

Hmm, $67.5 > 40 = y_{\max}$. $C_P'' = \mathbf{1000}$ (Top again).

**Iteration 3 — Clip $P(60, 67.5)$ (Top bit):**
$$x = 60 + \frac{1}{m}(40-67.5) = 60 + \frac{-8}{5}(-27.5) = 60 + 44 = 104$$

This seems to cycle. Let's check trivial reject test:
$C_P = 1000, C_Q = 0010$; AND = 0000.

Actually let us recompute more carefully. The intersection of line PQ with the window boundaries:
- Line: from $(40,80)$ to $(120,30)$. Slope $m = (30-80)/(120-40) = -50/80 = -5/8$.
- With $y=40$ (Top): $x = 40 + (8/5)(40-80) \cdot (-1) = 40 + (8/5)(-40)/(-1)$... 

Let me redo: $x = x_1 + (1/m)(y_{top} - y_1) = 40 + (-8/5)(40-80) = 40 + (-8/5)(-40) = 40 + 64 = 104$.
- With $x=60$ (Right): $y = 80 + (-5/8)(60-40) = 80 - 12.5 = 67.5 > 40$, still above.
- With $x=20$ (Left): $y = 80 + (-5/8)(20-40) = 80 + 12.5 = 92.5 > 40$, above.

Both intersections with $x$-boundaries give $y > 40$ (above Top). Check AND:
- Updated $C_P$ (at $x=104, y=40$): Right=1, Top=0 → $C_P'' = 0010$
- Intersection Q with Left ($x=20$): $y = 30 + (-5/8)(20-120) = 30 + (-5/8)(-100) = 30 + 62.5 = 92.5 > 40$. So new Q after Right clip...

Let's check if line actually intersects window: $y=40$ gives $x=104$ (outside right), $y=20$ gives $x = 40 + (-8/5)(20-80) = 40+96=136$ (way outside). The line passes entirely to the right and above the window.

**Trivial Reject detection**: After computing $P$ at Top intersection $(104,40)$: Right=1. $Q$ at Right intersection: $C_Q=0010$ (Right). AND = $0010 \ne 0$ → **Trivially REJECT the line**.

The line segment from $P(40,80)$ to $Q(120,30)$ is **entirely outside** window $[20,60]\times[20,40]$ and is discarded.

---

## 5. Previous Year Questions & Solutions

### Q1 [KTU Dec 2023, Dec 2021 — 9 Marks]
**Question**: Let ABCD be the rectangular window with A(20,20), B(90,20), C(90,70), D(20,70). Use Cohen-Sutherland algorithm to clip line P1(10,30) and P2(80,90).

**Solution**:

Window: $x_{\min}=20, x_{\max}=90, y_{\min}=20, y_{\max}=70$.

**Outcodes:**

$P_1(10,30)$: Left=1 (10<20) → $C_1 = 0001$

$P_2(80,90)$: Top=1 (90>70) → $C_2 = 1000$

AND = 0000, OR ≠ 0 → non-trivial.

$m = \frac{90-30}{80-10} = \frac{60}{70} = \frac{6}{7}$

**Clip $P_2$ (Top, $y=70$):**
$$x = 10 + \frac{7}{6}(70-30) = 10 + \frac{280}{6} = 10 + 46.67 = 56.67$$
$P_2' = (56.67, 70)$. Check: $56.67 \in [20,90]$, $70 \in [20,70]$ → $C_2' = 0000$ ✓

**Clip $P_1$ (Left, $x=20$):**
$$y = 30 + \frac{6}{7}(20-10) = 30 + \frac{60}{7} = 30 + 8.57 = 38.57$$
$P_1' = (20, 38.57)$. Check: → $C_1' = 0000$ ✓

**Visible segment**: $(20, 38.57) \to (56.67, 70)$ ✓

---

### Q2 [KTU Jan 2023 — 9 Marks]
**Question**: Clipping window ABCD: A(0,0), B(40,0), C(40,40), D(0,40). Using Midpoint Subdivision algorithm, find the visible portion of line P(-10,20) to Q(50,10).

**Solution**:

Window: $[0,40]\times[0,40]$.

$C_P(-10,20)$: Left=1 (x<0) → $0001$
$C_Q(50,10)$: Right=1 (x>40) → $0010$
AND = 0000, non-trivial.

**Midpoint subdivisions:**

**Iteration 1**: $M_1 = \left(\frac{-10+50}{2}, \frac{20+10}{2}\right) = (20,15)$. $C_{M_1} = 0000$ (inside).
- Subsegment $PM_1$: $C_P=0001, C_{M_1}=0000$ → non-trivial, refine left intersection.
- Subsegment $M_1Q$: $C_{M_1}=0000, C_Q=0010$ → non-trivial, refine right intersection.

**Left boundary ($x=0$) refinement** (subsegment $P(-10,20)$ to $M_1(20,15)$):

$M_2 = \left(\frac{-10+20}{2}, \frac{20+15}{2}\right) = (5, 17.5)$ → $C=0000$ (inside).

$M_3 = \left(\frac{-10+5}{2}, \frac{20+17.5}{2}\right) = (-2.5, 18.75)$ → Left=1.

$M_4 = \left(\frac{-2.5+5}{2}, \frac{18.75+17.5}{2}\right) = (1.25, 18.125)$ → $C=0000$.

$M_5 = (-0.625, 18.4375)$ → Left=1. Converging to $x\approx0$.

**Direct calculation** (for exactness): Line $P(-10,20)$ to $Q(50,10)$:
$$m = \frac{10-20}{50-(-10)} = \frac{-10}{60} = -\frac{1}{6}$$

Left boundary ($x=0$): $y = 20 + (-1/6)(0-(-10)) = 20 - 10/6 = 20 - 1.67 = 18.33$

Right boundary ($x=40$): $y = 20 + (-1/6)(40-(-10)) = 20 - 50/6 = 20 - 8.33 = 11.67$

**Visible segment**: $(0, 18.33) \to (40, 11.67)$

---

### Q3 [KTU Dec 2018, May 2019 — 9 Marks]
**Question**: Given clipping window A(-20,-20), B(40,-20), C(40,30), D(-20,30). Using Cohen-Sutherland, find visible portion of line P(-30,20) to Q(60,-10).

**Solution**:

Window: $x_{\min}=-20, x_{\max}=40, y_{\min}=-20, y_{\max}=30$.

**Outcodes:**

$P(-30,20)$: Left=1 (-30<-20) → $C_P = 0001$

$Q(60,-10)$: Right=1 (60>40) → $C_Q = 0010$

AND = 0000, non-trivial.

$m = \frac{-10-20}{60-(-30)} = \frac{-30}{90} = -\frac{1}{3}$

**Clip $P$ (Left, $x=-20$):**
$$y = 20 + (-1/3)(-20-(-30)) = 20 + (-1/3)(10) = 20 - 3.33 = 16.67$$
$P' = (-20, 16.67)$. $C_{P'} = 0000$ ✓

**Clip $Q$ (Right, $x=40$):**
$$y = 20 + (-1/3)(40-(-30)) = 20 + (-1/3)(70) = 20 - 23.33 = -3.33$$
$Q' = (40, -3.33)$. $-3.33 \in [-20,30]$ → $C_{Q'} = 0000$ ✓

**Visible segment**: $(-20, 16.67) \to (40, -3.33)$

---

### Q4 [KTU Dec 2021 — 9 Marks]
**Question**: Given clipping window A(10,-20), B(80,-20), C(80,20), D(10,20). Using Cohen-Sutherland, clip line P(-20,10) to Q(70,-20).

**Solution**:

Window: $x_{\min}=10, x_{\max}=80, y_{\min}=-20, y_{\max}=20$.

$P(-20,10)$: Left=1 (-20<10) → $C_P = 0001$

$Q(70,-20)$: $y=-20=y_{\min}$ (boundary, not outside), $x=70 \in [10,80]$ → $C_Q = 0000$ (Inside!)

AND = 0000, OR ≠ 0 → clip only $P$.

$m = \frac{-20-10}{70-(-20)} = \frac{-30}{90} = -\frac{1}{3}$

**Clip $P$ (Left, $x=10$):**
$$y = 10 + (-1/3)(10-(-20)) = 10 + (-1/3)(30) = 10 - 10 = 0$$
$P' = (10, 0)$. $0 \in [-20,20]$ → $C_{P'} = 0000$ ✓

**Visible segment**: $(10, 0) \to Q(70, -20)$

---

### Q5 [KTU Dec 2023 / Sep 2020 / Jan 2023 — 4 Marks]
**Question**: How does Cohen-Sutherland algorithm determine whether a line is visible, invisible or a candidate for clipping based on the region codes assigned to the end points of the line?

**Solution**:

The Cohen-Sutherland algorithm computes a **4-bit region code (outcode)** for each line endpoint and uses **bitwise Boolean operations** to categorize the line:

**Step 1 — Compute Outcode** for each endpoint $(x, y)$:
- Bit 4 (Top): 1 if $y > y_{\max}$
- Bit 3 (Bottom): 1 if $y < y_{\min}$
- Bit 2 (Right): 1 if $x > x_{\max}$
- Bit 1 (Left): 1 if $x < x_{\min}$

**Step 2 — Apply Three-Way Decision:**

| Condition | Determination | Action |
|---|---|---|
| $(C_1 \text{ OR } C_2) = 0$ | **Visible (Trivially Accept)** | Both endpoints inside window; display entire line |
| $(C_1 \text{ AND } C_2) \ne 0$ | **Invisible (Trivially Reject)** | Both endpoints on same outside half-plane; discard line |
| Neither | **Candidate for Clipping** | Line partially crosses window; compute boundary intersection |

**Example**: $P(10,30)$ has $C_1=0001$ (Left), $P(50,80)$ has $C_2=1000$ (Top).
- $C_1$ OR $C_2 = 1001 \ne 0$ → not trivially accepted
- $C_1$ AND $C_2 = 0000$ → not trivially rejected
- **Candidate for clipping** → compute actual intersection points

**Efficiency**: The bitwise OR and AND tests are single-clock-cycle operations — they process all 4 boundary conditions simultaneously using just one instruction on a 4-bit or wider integer register.
