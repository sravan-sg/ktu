# Polygon Clipping Algorithms: Sutherland-Hodgman and Weiler-Atherton

## 1. Explanation

While line clipping algorithms (such as Cohen-Sutherland and Liang-Barsky) operate on isolated line segments, **polygon clipping** requires processing a closed planar area bounded by an ordered cycle of vertices. 

The fundamental challenge in polygon clipping is that clipping an arbitrary polygon against a clipping window must produce **one or more valid, closed polygon perimeters**. This requires not only computing boundary intersection points, but also synthesizing new polygon edges along the window boundaries to ensure the output remains properly enclosed for scanline rasterization.

---

### The Sutherland-Hodgman Polygon Clipping Algorithm

Introduced by Ivan Sutherland and Gary Hodgman in 1974, this algorithm uses a **pipelined divide-and-conquer strategy**. Rather than attempting to clip a polygon against all four window boundaries simultaneously, the algorithm clips the input polygon sequentially against each infinite clipping plane in isolation:

```
┌─────────────────┐       ┌───────────────┐       ┌────────────────┐       ┌─────────────┐       ┌────────────────┐
│  Input Polygon  │ ────► │ Left Clipper  │ ────► │ Right Clipper  │ ────► │ Bottom Clip │ ────► │  Top Clipper   │ ────► Final Output
│  Vertices [V]   │       │ (x = xwmin)   │       │ (x = xwmax)    │       │ (y = ywmin) │       │  (y = ywmax)   │       Polygon [V']
└─────────────────┘       └───────────────┘       └────────────────┘       └─────────────┘       └────────────────┘
```

#### The Four Fundamental Edge Traversal Cases
For each boundary line, the algorithm considers the directed edge $V_1 \to V_2$ connecting each sequential pair of vertices in the polygon's cyclic vertex list. The boundary line partitions 2D space into an **inside half-space** (visible side) and an **outside half-space** (clipped side).

```
    Case 1 (In -> In)       Case 2 (In -> Out)      Case 3 (Out -> Out)     Case 4 (Out -> In)
        Inside                 Inside                  Inside                  Inside
       +------+               +------+                                        +------+
       │  V1  │               │  V1  │                                        │  V2  │
       │  │   │               │  │   │                                        │  ▲   │
       │  ▼   │               │  ▼   │                                        │  │   │
Boundary──┼───┼───────Boundary────┼──* V'─────Boundary────────────Boundary────┼──* V'─────
       │  │   │               │  │   │                V1     V2           │  │   │
       │  V2  │               │  V2  │                │      │            │  V1  │
       +------+               +------+                ▼      ▼            +------+
       Outside                Outside                 Outside                 Outside
    Output: [V2]           Output: [V']            Output: [None]          Output: [V', V2]
```

1. **Case 1: $V_1$ is INSIDE and $V_2$ is INSIDE**
   - The entire directed segment lies within the visible boundary half-space.
   - **Action**: Output vertex **$V_2$**.
2. **Case 2: $V_1$ is INSIDE and $V_2$ is OUTSIDE**
   - The directed edge exits the visible window.
   - Compute the geometric intersection point $V'$ between line segment $V_1 V_2$ and the boundary.
   - **Action**: Output intersection vertex **$V'$**.
3. **Case 3: $V_1$ is OUTSIDE and $V_2$ is OUTSIDE**
   - The directed edge lies completely outside the visible region.
   - **Action**: Output **nothing** (both vertices are suppressed).
4. **Case 4: $V_1$ is OUTSIDE and $V_2$ is INSIDE**
   - The directed edge enters the visible window from outside.
   - Compute the geometric intersection point $V'$ between line segment $V_1 V_2$ and the boundary.
   - **Action**: Output intersection vertex **$V'$**, followed immediately by vertex **$V_2$**.

---

### Mathematical Intersection Formulas

When computing the intersection point $V'(x', y')$ of directed edge $V_1(x_1, y_1) \to V_2(x_2, y_2)$ with a window boundary line:

1. **Vertical Boundary Line ($x = x_{\text{bound}}$, where $x_{\text{bound}} \in \{x_{w\min}, x_{w\max}\}$)**:
   $$x' = x_{\text{bound}}$$
   $$y' = y_1 + m \cdot (x_{\text{bound}} - x_1) = y_1 + \left(\frac{y_2 - y_1}{x_2 - x_1}\right) (x_{\text{bound}} - x_1)$$

2. **Horizontal Boundary Line ($y = y_{\text{bound}}$, where $y_{\text{bound}} \in \{y_{w\min}, y_{w\max}\}$)**:
   $$y' = y_{\text{bound}}$$
   $$x' = x_1 + \frac{1}{m} \cdot (y_{\text{bound}} - y_1) = x_1 + \left(\frac{x_2 - x_1}{y_2 - y_1}\right) (y_{\text{bound}} - y_1)$$

---

### Algorithm Pseudocode: Sutherland-Hodgman

```python
def sutherland_hodgman_polygon_clip(subject_polygon, clip_window):
    # boundaries = [LEFT, RIGHT, BOTTOM, TOP]
    output_list = subject_polygon
    
    for boundary in [clip_window.left, clip_window.right, clip_window.bottom, clip_window.top]:
        input_list = output_list
        output_list = []
        if len(input_list) == 0:
            break
            
        v1 = input_list[-1]  # Start with the last vertex to close the cycle
        
        for v2 in input_list:
            v2_inside = is_inside(v2, boundary)
            v1_inside = is_inside(v1, boundary)
            
            if v2_inside:
                if not v1_inside:
                    # Case 4: Out -> In
                    v_prime = compute_intersection(v1, v2, boundary)
                    output_list.append(v_prime)
                # Case 1 (In -> In) or Case 4 (Out -> In)
                output_list.append(v2)
            elif v1_inside:
                # Case 2: In -> Out
                v_prime = compute_intersection(v1, v2, boundary)
                output_list.append(v_prime)
            # Case 3: Out -> Out: emit nothing
            
            v1 = v2  # Advance to next vertex
            
    return output_list
```

---

### The Concave Polygon Limitation of Sutherland-Hodgman

A major limitation of the Sutherland-Hodgman algorithm arises when clipping **concave polygons** (e.g., U-shaped, dumbbell, or star-shaped polygons):

```
       SUTHERLAND-HODGMAN CONCAVE CLIPPING ARTIFACT
       
       Original Concave Polygon                 Clipped Result (Artifact)
       ┌───┐             ┌───┐                  ┌───┐             ┌───┐
       │   │             │   │                  │   │             │   │
       │   │             │   │                  │   │             │   │
       │   │   Window    │   │                  │   │             │   │
  ─────┼───┼─────────────┼───┼───── Boundary ───┼───*═════════════*───┼───── Spurious Edge
       │   └─────────────┘   │                  │   │  Artifact   │   │      joins disconnected
       │                     │                  │   │  bridge     │   │      pieces!
       └─────────────────────┘                  └───┘             └───┘
```

- When clipping a concave notch against a boundary, the polygon is physically divided into **two or more disjoint, disconnected polygons**.
- Because Sutherland-Hodgman maintains a **single, linear sequential vertex list**, it cannot output multiple disconnected polygon records.
- Instead, it traces along the window boundary to link the separated parts, producing an **extraneous, artificial line segment (bridge edge)** connecting the components.
- During scanline polygon filling, this spurious edge causes fill-parity errors and rendering artifacts.

---

### The Weiler-Atherton Polygon Clipping Algorithm

Developed by Kevin Weiler and Peter Atherton in 1977, this algorithm resolves the concave polygon limitation by naturally decomposing clipped geometry into multiple independent, closed polygonal loops. Furthermore, it supports clipping an arbitrary polygon against an **arbitrary concave clipping polygon with holes**.

```
                WEILER-ATHERTON TRAVERSAL LOGIC
                
              Subject Polygon List                Clip Window List
                  (Clockwise)                        (Clockwise)
                 ┌──────────┐                       ┌──────────┐
                 │    S1    │                       │    W1    │
                 ├──────────┤                       ├──────────┤
                 │ I_enter  │ ──────── Switch ────► │ I_enter  │
                 ├──────────┤                       ├──────────┤
                 │    S2    │                       │    W2    │
                 ├──────────┤                       ├──────────┤
                 │  I_exit  │ ◄─────── Switch ───── │  I_exit  │
                 └──────────┘                       └──────────┘
```

#### Operating Principle:
1. **Intersection Identification & Classification**:
   - Compute all intersection points between the edges of the Subject Polygon and the Clip Window.
   - Classify each intersection point:
     - **Entering Intersection ($I_{\text{enter}}$)**: The directed subject edge passes from the outside to the inside of the clipping window.
     - **Exiting Intersection ($I_{\text{exit}}$)**: The directed subject edge passes from the inside to the outside of the clipping window.
2. **Dual Circular Linked Lists**:
   - Construct two circular linked lists:
     1. **Subject Polygon List**: Contains subject vertices with intersection points inserted in directed traversal order.
     2. **Clip Window List**: Contains window vertices with the same intersection points inserted in directed traversal order.
3. **Traversal and Polygon Extraction**:
   - Select an unvisited **Entering Intersection** $I_{\text{enter}}$.
   - **Rule 1 (Subject Traversal)**: Follow the Subject Polygon list forward (inside the window) until encountering an **Exiting Intersection** $I_{\text{exit}}$.
   - **Rule 2 (Window Traversal)**: At $I_{\text{exit}}$, switch to the Clip Window list. Follow the window boundary in a clockwise direction until encountering an **Entering Intersection** $I_{\text{enter}}$.
   - **Rule 3 (Switch Back)**: At $I_{\text{enter}}$, switch back to the Subject Polygon list.
   - Continue alternating until the traversal returns to the initial starting vertex, completing one closed polygon.
   - Repeat for all remaining unvisited entering intersections to extract all disjoint output polygons.

---

## 2. Example: Step-by-Step Sutherland-Hodgman Walkthrough

**Problem**:
Clip the polygon with vertices:
$$V_1(10, 10), \quad V_2(50, 10), \quad V_3(50, 40), \quad V_4(30, 50), \quad V_5(10, 40)$$
against the rectangular clipping window:
$$x_{w\min} = 20, \quad x_{w\max} = 45, \quad y_{w\min} = 15, \quad y_{w\max} = 35$$

---

### Stage 1: Left Clipper ($x \ge 20$)
Test all edges against $x = 20$:
- Edge $V_5(10, 40) \to V_1(10, 10)$: Out $\to$ Out $\implies$ **None**.
- Edge $V_1(10, 10) \to V_2(50, 10)$: Out $\to$ In.
  - $x' = 20, \ y' = 10$. Intersection $I_1(20, 10)$.
  - **Output: $I_1(20, 10), V_2(50, 10)$**.
- Edge $V_2(50, 10) \to V_3(50, 40)$: In $\to$ In $\implies$ **Output: $V_3(50, 40)$**.
- Edge $V_3(50, 40) \to V_4(30, 50)$: In $\to$ In $\implies$ **Output: $V_4(30, 50)$**.
- Edge $V_4(30, 50) \to V_5(10, 40)$: In $\to$ Out.
  - Slope $m = \frac{40 - 50}{10 - 30} = \frac{-10}{-20} = 0.5$.
  - At $x' = 20$: $y' = 50 + 0.5(20 - 30) = 50 - 5 = 45$. Intersection $I_2(20, 45)$.
  - **Output: $I_2(20, 45)$**.

**Output of Left Clipper**: $[I_1(20, 10), V_2(50, 10), V_3(50, 40), V_4(30, 50), I_2(20, 45)]$.

---

### Stage 2: Right Clipper ($x \le 45$)
Test all edges against $x = 45$:
- Edge $I_2(20, 45) \to I_1(20, 10)$: In $\to$ In $\implies$ **Output: $I_1(20, 10)$**.
- Edge $I_1(20, 10) \to V_2(50, 10)$: In $\to$ Out.
  - At $x' = 45$: $y' = 10$. Intersection $I_3(45, 10)$.
  - **Output: $I_3(45, 10)$**.
- Edge $V_2(50, 10) \to V_3(50, 40)$: Out $\to$ Out $\implies$ **None**.
- Edge $V_3(50, 40) \to V_4(30, 50)$: Out $\to$ In.
  - Slope $m = \frac{50 - 40}{30 - 50} = \frac{10}{-20} = -0.5$.
  - At $x' = 45$: $y' = 40 + (-0.5)(45 - 50) = 40 + 2.5 = 42.5$. Intersection $I_4(45, 42.5)$.
  - **Output: $I_4(45, 42.5), V_4(30, 50)$**.
- Edge $V_4(30, 50) \to I_2(20, 45)$: In $\to$ In $\implies$ **Output: $I_2(20, 45)$**.

**Output of Right Clipper**: $[I_1(20, 10), I_3(45, 10), I_4(45, 42.5), V_4(30, 50), I_2(20, 45)]$.

---

### Stage 3: Bottom Clipper ($y \ge 15$)
Test all edges against $y = 15$:
- Edge $I_2(20, 45) \to I_1(20, 10)$: In $\to$ Out.
  - At $y' = 15$: $x' = 20$. Intersection $I_5(20, 15)$.
  - **Output: $I_5(20, 15)$**.
- Edge $I_1(20, 10) \to I_3(45, 10)$: Out $\to$ Out $\implies$ **None**.
- Edge $I_3(45, 10) \to I_4(45, 42.5)$: Out $\to$ In.
  - At $y' = 15$: $x' = 45$. Intersection $I_6(45, 15)$.
  - **Output: $I_6(45, 15), I_4(45, 42.5)$**.
- Edge $I_4(45, 42.5) \to V_4(30, 50)$: In $\to$ In $\implies$ **Output: $V_4(30, 50)$**.
- Edge $V_4(30, 50) \to I_2(20, 45)$: In $\to$ In $\implies$ **Output: $I_2(20, 45)$**.

**Output of Bottom Clipper**: $[I_5(20, 15), I_6(45, 15), I_4(45, 42.5), V_4(30, 50), I_2(20, 45)]$.

---

### Stage 4: Top Clipper ($y \le 35$)
Test all edges against $y = 35$:
- Edge $I_2(20, 45) \to I_5(20, 15)$: Out $\to$ In.
  - At $y' = 35$: $x' = 20$. Intersection $I_7(20, 35)$.
  - **Output: $I_7(20, 35), I_5(20, 15)$**.
- Edge $I_5(20, 15) \to I_6(45, 15)$: In $\to$ In $\implies$ **Output: $I_6(45, 15)$**.
- Edge $I_6(45, 15) \to I_4(45, 42.5)$: In $\to$ Out.
  - At $y' = 35$: $x' = 45$. Intersection $I_8(45, 35)$.
  - **Output: $I_8(45, 35)$**.
- Edge $I_4(45, 42.5) \to V_4(30, 50)$: Out $\to$ Out $\implies$ **None**.
- Edge $V_4(30, 50) \to I_2(20, 45)$: Out $\to$ Out $\implies$ **None**.

**Final Clipped Polygon Vertices**:
$$[I_7(20, 35), \ I_5(20, 15), \ I_6(45, 15), \ I_8(45, 35)]$$
The output is a perfectly clipped, closed rectangular sub-polygon.

---

## 3. Applications & Use Cases

1. **Hardware Rasterization Pipelines (OpenGL / DirectX)**:
   Modern GPUs implement Sutherland-Hodgman clipping directly in fixed-function hardware between the Geometry Shader and the Rasterizer. Guard-band clipping extends the clip volume beyond viewport boundaries so that primitive triangles are clipped strictly against NDC frustum planes.
2. **Geographic Information Systems (GIS Map Tiling)**:
   Vector map renderers (Google Maps, OpenStreetMap) clip administrative land boundaries, lake shorelines, and road networks against fixed $256 \times 256$ pixel tile boundaries before vector serialization.
3. **Shadow Volume Silhouette Generation (Stencil Shadow Algorithms)**:
   In 3D shadow volume rendering, light-extruded polygon volumes are clipped against the view frustum near-plane to avoid artifacts when the virtual camera enters a shadow volume.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Sutherland-Hodgman Triangle Clipping [KTU June 2022 Pattern]
**Problem**:
Clip the triangle $A(10, 20), B(80, 20), C(40, 80)$ against the clipping window $x \in [30, 70], y \in [10, 60]$. Determine the final output vertex list.

**Solution**:
Input: Triangle $[A(10, 20), B(80, 20), C(40, 80)]$.
Window: $x_{w\min} = 30, x_{w\max} = 70, y_{w\min} = 10, y_{w\max} = 60$.

**1. Left Clipper ($x \ge 30$)**:
- $C(40, 80) \to A(10, 20)$: In $\to$ Out.
  - Slope $m = \frac{20 - 80}{10 - 40} = \frac{-60}{-30} = 2$.
  - At $x' = 30$: $y' = 80 + 2(30 - 40) = 80 - 20 = 60$. Intersection $I_1(30, 60)$.
  - Output: $I_1(30, 60)$.
- $A(10, 20) \to B(80, 20)$: Out $\to$ In.
  - At $x' = 30$: $y' = 20$. Intersection $I_2(30, 20)$.
  - Output: $I_2(30, 20), B(80, 20)$.
- $B(80, 20) \to C(40, 80)$: In $\to$ In $\implies$ Output: $C(40, 80)$.
- Output of Left: $[I_1(30, 60), I_2(30, 20), B(80, 20), C(40, 80)]$.

**2. Right Clipper ($x \le 70$)**:
- $C(40, 80) \to I_1(30, 60)$: In $\to$ In $\implies$ Output: $I_1(30, 60)$.
- $I_1(30, 60) \to I_2(30, 20)$: In $\to$ In $\implies$ Output: $I_2(30, 20)$.
- $I_2(30, 20) \to B(80, 20)$: In $\to$ Out.
  - At $x' = 70$: $y' = 20$. Intersection $I_3(70, 20)$.
  - Output: $I_3(70, 20)$.
- $B(80, 20) \to C(40, 80)$: Out $\to$ In.
  - Slope $m = \frac{80 - 20}{40 - 80} = \frac{60}{-40} = -1.5$.
  - At $x' = 70$: $y' = 20 + (-1.5)(70 - 80) = 20 + 15 = 35$. Intersection $I_4(70, 35)$.
  - Output: $I_4(70, 35), C(40, 80)$.
- Output of Right: $[I_1(30, 60), I_2(30, 20), I_3(70, 20), I_4(70, 35), C(40, 80)]$.

**3. Bottom Clipper ($y \ge 10$)**:
- All current vertices have $y \ge 20 > 10$. All edges are In $\to$ In.
- Output remains unchanged: $[I_1(30, 60), I_2(30, 20), I_3(70, 20), I_4(70, 35), C(40, 80)]$.

**4. Top Clipper ($y \le 60$)**:
- $C(40, 80) \to I_1(30, 60)$: Out $\to$ In (vertex $I_1$ is on boundary $y=60$, classified as In).
  - Slope $m = 2$. At $y' = 60$: $x' = 30$. Intersection is $I_1(30, 60)$.
  - Output: $I_1(30, 60)$.
- $I_1(30, 60) \to I_2(30, 20)$: In $\to$ In $\implies$ Output: $I_2(30, 20)$.
- $I_2(30, 20) \to I_3(70, 20)$: In $\to$ In $\implies$ Output: $I_3(70, 20)$.
- $I_3(70, 20) \to I_4(70, 35)$: In $\to$ In $\implies$ Output: $I_4(70, 35)$.
- $I_4(70, 35) \to C(40, 80)$: In $\to$ Out.
  - Slope $m = -1.5$.
  - At $y' = 60$: $x' = 70 + \frac{60 - 35}{-1.5} = 70 - \frac{25}{1.5} \approx 70 - 16.67 = 53.33$. Intersection $I_5(53.33, 60)$.
  - Output: $I_5(53.33, 60)$.

**Final Clipped Polygon**: $[I_1(30, 60), I_2(30, 20), I_3(70, 20), I_4(70, 35), I_5(53.33, 60)]$.

---

### Example 2: Weiler-Atherton Traversal on Overlapping Rectangles [Analytical Example]
**Problem**:
Consider clipping subject polygon $S = [S_1(20, 20), S_2(60, 20), S_3(60, 60), S_4(20, 60)]$ against clipping window $W = [W_1(30, 30), W_2(70, 30), W_3(70, 70), W_4(30, 70)]$. Show the dual list structure and trace the clipped polygon.

**Solution**:
1. **Intersection Points**:
   - Edge $S_1(20, 20) \to S_2(60, 20)$: Horizontal line at $y = 20$. Window is $y \in [30, 70]$. No intersection.
   - Edge $S_2(60, 20) \to S_3(60, 60)$: Vertical line at $x = 60$. Intersects bottom window edge $y = 30$ at $I_1(60, 30)$. 
     - Directed from outside ($y = 20 < 30$) to inside ($y = 60 > 30$) $\implies$ **Entering Intersection ($I_1$)**.
   - Edge $S_3(60, 60) \to S_4(20, 60)$: Horizontal line at $y = 60$. Intersects left window edge $x = 30$ at $I_2(30, 60)$.
     - Directed from inside ($x = 60 > 30$) to outside ($x = 20 < 30$) $\implies$ **Exiting Intersection ($I_2$)**.
   - Edge $S_4(20, 60) \to S_1(20, 20)$: Outside window. No intersection.

2. **Construct Dual Lists (Clockwise Order)**:
   - **Subject Polygon List**:
     $$S_1(20, 20) \to S_2(60, 20) \to I_1(60, 30) \text{ [Enter]} \to S_3(60, 60) \to I_2(30, 60) \text{ [Exit]} \to S_4(20, 60) \to S_1(20, 20)$$
   - **Clip Window List**:
     $$W_1(30, 30) \to I_1(60, 30) \text{ [Enter]} \to W_2(70, 30) \to W_3(70, 70) \to W_4(30, 70) \to I_2(30, 60) \text{ [Exit]} \to W_1(30, 30)$$

3. **Trace Traversal**:
   - Start at unvisited entering intersection: $I_1(60, 30)$.
   - Follow Subject list forward: $I_1(60, 30) \to S_3(60, 60) \to I_2(30, 60)$ (Encountered $I_2$ [Exit]).
   - Switch to Clip Window list at $I_2(30, 60)$ and follow clockwise:
     $I_2(30, 60) \to W_1(30, 30) \to I_1(60, 30)$.
   - Loop closes at starting vertex $I_1(60, 30)$!

**Resulting Clipped Polygon**: $[I_1(60, 30), \ S_3(60, 60), \ I_2(30, 60), \ W_1(30, 30)]$.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [June 2024 Q15a / Dec 2023 Q16b / Dec 2018 Q16a — 5–9 Marks]
**Question**:
Explain the Sutherland-Hodgman polygon clipping algorithm with suitable illustrations.

**Solution**:

The **Sutherland-Hodgman Algorithm** clips an arbitrary polygon against a convex clipping window by decomposing the 2D window into four independent, infinite half-plane clipping boundaries: Left, Right, Bottom, and Top. The polygon is passed through a pipeline of four clippers, where the output vertex list of one stage serves as the input to the next.

**The Four Edge Cases**:
For each clipping boundary, we examine each directed edge connecting vertex $V_1$ to vertex $V_2$ in cyclic order:

```
    Case 1 (In -> In)       Case 2 (In -> Out)      Case 3 (Out -> Out)     Case 4 (Out -> In)
        Inside                 Inside                  Inside                  Inside
       +------+               +------+                                        +------+
       │  V1  │               │  V1  │                                        │  V2  │
       │  │   │               │  │   │                                        │  ▲   │
       │  ▼   │               │  ▼   │                                        │  │   │
Boundary──┼───┼───────Boundary────┼──* V'─────Boundary────────────Boundary────┼──* V'─────
       │  │   │               │  │   │                V1     V2           │  │   │
       │  V2  │               │  V2  │                │      │            │  V1  │
       +------+               +------+                ▼      ▼            +------+
       Outside                Outside                 Outside                 Outside
    Output: [V2]           Output: [V']            Output: [None]          Output: [V', V2]
```

1. **Case 1: $V_1$ Inside, $V_2$ Inside**:
   The entire edge lies within the visible half-space. **Output: $V_2$**.
2. **Case 2: $V_1$ Inside, $V_2$ Outside**:
   The edge exits the clipping boundary. Calculate intersection point $V'$. **Output: $V'$**.
3. **Case 3: $V_1$ Outside, $V_2$ Outside**:
   The edge lies completely in the invisible half-space. **Output: Nothing**.
4. **Case 4: $V_1$ Outside, $V_2$ Inside**:
   The edge enters the visible boundary. Calculate intersection point $V'$. **Output: $V'$, then $V_2$**.

**Example Walkthrough**:
Let unit polygon $V_1(1, 1), V_2(8, 1), V_3(8, 8), V_4(1, 8)$ be clipped against window $[3, 2]$ to $[6, 7]$:
1. **Left Clipper ($x \ge 3$)**:
   - $V_4(1, 8) \to V_1(1, 1)$: Out $\to$ Out $\implies$ None.
   - $V_1(1, 1) \to V_2(8, 1)$: Out $\to$ In $\implies$ Intersection $I_1(3, 1)$, Output: $I_1(3, 1), V_2(8, 1)$.
   - $V_2(8, 1) \to V_3(8, 8)$: In $\to$ In $\implies$ Output: $V_3(8, 8)$.
   - $V_3(8, 8) \to V_4(1, 8)$: In $\to$ Out $\implies$ Intersection $I_2(3, 8)$, Output: $I_2(3, 8)$.
   - List: $[I_1(3, 1), V_2(8, 1), V_3(8, 8), I_2(3, 8)]$.
2. **Right Clipper ($x \le 6$)**:
   - Clips $V_2(8, 1)$ and $V_3(8, 8)$ to $x = 6$, giving $I_3(6, 1)$ and $I_4(6, 8)$.
   - List: $[I_1(3, 1), I_3(6, 1), I_4(6, 8), I_2(3, 8)]$.
3. **Bottom Clipper ($y \ge 2$)**:
   - Clips $y = 1$ to $y = 2$, replacing bottom corners with $(3, 2)$ and $(6, 2)$.
4. **Top Clipper ($y \le 7$)**:
   - Clips $y = 8$ to $y = 7$, replacing top corners with $(6, 7)$ and $(3, 7)$.
5. **Final Output**: $[(3, 2), (6, 2), (6, 7), (3, 7)]$, representing the perfectly clipped sub-polygon.

---

### Question 2 [June 2024 Q16b — 5 Marks]
**Question**:
Describe the Weiler-Atherton polygon clipping algorithm with a suitable example.

**Solution**:

The **Weiler-Atherton Algorithm** was developed to overcome the concave polygon limitation of the Sutherland-Hodgman algorithm. It can clip arbitrary concave polygons (including polygons with holes) against arbitrary concave clipping regions, producing separate disjoint polygon outputs without spurious connecting edges.

**Operating Principle**:
1. **Intersection Calculation & Classification**:
   - Compute all intersection points between the directed edges of the Subject Polygon and the Clip Window.
   - Classify each intersection as:
     - **Entering**: The directed subject edge enters the interior of the clipping window.
     - **Exiting**: The directed subject edge exits the clipping window into the outside half-space.
2. **Dual Circular Linked Lists**:
   - Construct two linked lists in clockwise order:
     - **Subject List**: Vertices of subject polygon with inserted intersection points.
     - **Clip List**: Vertices of clip window with inserted intersection points.
3. **Traversal Rules**:
   - Locate an unvisited **Entering Intersection** $I_{\text{enter}}$.
   - Follow the **Subject List** forward until reaching an **Exiting Intersection** $I_{\text{exit}}$.
   - At $I_{\text{exit}}$, switch to the **Clip List** and follow the window boundary clockwise until reaching an **Entering Intersection**.
   - Switch back to the Subject List.
   - Repeat switching until the path loops back to the starting vertex, yielding a single closed polygon component.
   - Repeat the process for all unvisited entering intersections to extract all remaining disjoint polygons.

---

### Question 3 [Dec 2021 Q15a — 6 Marks]
**Question**:
Illustrate the clipping of the polygon shown against the rectangular clipping window using the Sutherland-Hodgman algorithm. Draw the intermediate results.

**Solution**:

Consider clipping a concave L-shaped polygon against a rectangular clipping window.
- **Input Vertices**: $V_1(10, 10), V_2(60, 10), V_3(60, 30), V_4(30, 30), V_5(30, 60), V_6(10, 60)$.
- **Window**: $x \in [20, 50], y \in [20, 50]$.

**Pipelined Boundary Processing**:

1. **Left Boundary ($x = 20$)**:
   - Edges crossing $x = 20$:
     - $V_6(10, 60) \to V_1(10, 10)$: Completely outside $\implies$ None.
     - $V_1(10, 10) \to V_2(60, 10)$: Out $\to$ In at $I_1(20, 10) \implies$ Output: $I_1(20, 10), V_2(60, 10)$.
     - $V_2 \to V_3 \to V_4$: All have $x \ge 30 \ge 20 \implies$ Output: $V_3(60, 30), V_4(30, 30)$.
     - $V_4(30, 30) \to V_5(30, 60)$: Inside $\implies$ Output: $V_5(30, 60)$.
     - $V_5(30, 60) \to V_6(10, 60)$: In $\to$ Out at $I_2(20, 60) \implies$ Output: $I_2(20, 60)$.
   - *Left Intermediate List*: $[I_1(20, 10), V_2(60, 10), V_3(60, 30), V_4(30, 30), V_5(30, 60), I_2(20, 60)]$.

2. **Right Boundary ($x = 50$)**:
   - Clips the rightmost extension: $V_2(60, 10)$ and $V_3(60, 30)$ exceed $x = 50$.
   - Intersects $I_1 \to V_2$ at $I_3(50, 10)$, and $V_3 \to V_4$ at $I_4(50, 30)$.
   - *Right Intermediate List*: $[I_1(20, 10), I_3(50, 10), I_4(50, 30), V_4(30, 30), V_5(30, 60), I_2(20, 60)]$.

3. **Bottom Boundary ($y = 20$)**:
   - Clips bottom portion below $y = 20$: $I_1(20, 10)$ and $I_3(50, 10)$ are discarded.
   - Intersects at $I_5(20, 20)$ and $I_6(50, 20)$.
   - *Bottom Intermediate List*: $[I_5(20, 20), I_6(50, 20), I_4(50, 30), V_4(30, 30), V_5(30, 60), I_2(20, 60)]$.

4. **Top Boundary ($y = 50$)**:
   - Clips top extension above $y = 50$: $V_5(30, 60)$ and $I_2(20, 60)$ are clipped at $y = 50$.
   - Intersects at $I_7(30, 50)$ and $I_8(20, 50)$.
   - *Final Output List*: $[I_5(20, 20), I_6(50, 20), I_4(50, 30), V_4(30, 30), I_7(30, 50), I_8(20, 50)]$.

All intermediate stages systematically trim the geometry to conform strictly to the clipping window.
