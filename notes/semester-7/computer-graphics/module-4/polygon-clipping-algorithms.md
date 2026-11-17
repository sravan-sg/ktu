# Polygon Clipping Algorithms: Sutherland-Hodgman and Weiler-Atherton

## 1. Explanation
While line clipping algorithms operate on individual independent line segments, **polygon clipping** requires clipping an entire closed planar shape bounded by an ordered cycle of vertices.
The fundamental challenge in polygon clipping is that clipping an arbitrary polygon against a rectangular window must output **new closed polygon boundaries**, potentially generating new interior edges along the clipping window margins.

---

### Sutherland-Hodgman Polygon Clipping Algorithm
The Sutherland-Hodgman algorithm approaches polygon clipping using a **pipeline divide-and-conquer strategy**: instead of clipping against the entire rectangular window simultaneously, the polygon is clipped sequentially against each of the four infinite boundary lines:
$$\text{Input Polygon} \xrightarrow{\text{Left Clipper}} P_1 \xrightarrow{\text{Right Clipper}} P_2 \xrightarrow{\text{Bottom Clipper}} P_3 \xrightarrow{\text{Top Clipper}} \text{Final Clipped Polygon}$$

#### The Four Edge-Traversal Cases
For each clipping boundary, we test each directed edge connecting vertex $V_1$ to vertex $V_2$ in the polygon. Let the half-space containing the window interior be classified as the **in** side, and the outside half-space as the **out** side:

1. **Case 1: $V_1$ is IN and $V_2$ is IN**
   - The edge lies entirely inside the boundary.
   - **Action**: Output vertex **$V_2$**.
2. **Case 2: $V_1$ is IN and $V_2$ is OUT**
   - The edge exits the visible window.
   - Compute the geometric intersection point $V'$ between edge $V_1 V_2$ and the boundary line.
   - **Action**: Output intersection vertex **$V'$**.
3. **Case 3: $V_1$ is OUT and $V_2$ is OUT**
   - The edge lies entirely outside the boundary.
   - **Action**: Output **nothing** (both vertices discarded).
4. **Case 4: $V_1$ is OUT and $V_2$ is IN**
   - The edge enters the visible window.
   - Compute the geometric intersection point $V'$ between edge $V_1 V_2$ and the boundary line.
   - **Action**: Output intersection vertex **$V'$**, followed immediately by vertex **$V_2$**.

```
    Case 1 (In -> In)       Case 2 (In -> Out)      Case 3 (Out -> Out)     Case 4 (Out -> In)
        Inside                 Inside                  Inside                  Inside
       +------+               +------+                                        +------+
       |  V_1 |               |  V_1 |                                        |  V_2 |
       |   |  |               |   |  |                                        |   ^  |
       |   v  |               |   v  |                                        |   |  |
Boundary───┼──┼───────Boundary────┼──* V'─────Boundary────────────Boundary────┼──* V'─────
       |   |  |               |   |  |                V_1    V_2          |   |  |
       |  V_2 |               |  V_2 |                 |      |           |  V_1 |
       +------+               +------+                 v      v           +------+
       Outside                Outside                 Outside                 Outside
    Output: [V_2]          Output: [V']            Output: [None]          Output: [V', V_2]
```

#### Limitation of Sutherland-Hodgman (Concave Polygon Problem):
When clipping a **concave polygon** (such as a U-shaped figure or dumbbell), clipping can split the polygon into two or more disjoint, disconnected pieces.
- Because Sutherland-Hodgman outputs vertices as a single linear sequence, it connects the disjoint pieces by creating an extraneous, artificial line segment running along the clipping boundary.
- It cannot naturally represent multiple disjoint polygons without post-processing.

---

### Weiler-Atherton Polygon Clipping Algorithm
Developed by Kevin Weiler and Peter Atherton, this algorithm resolves the concave polygon limitation by outputting separate, disconnected polygon contours. It supports arbitrary polygon clipping (including clipping a concave subject polygon against an arbitrary concave clipping polygon).

#### Operating Principle:
1. **Intersection Calculation**:
   Compute all intersection points between the subject polygon edges and the clipping window boundaries.
2. **Dual Linked List Construction**:
   Construct two cyclical, circular linked lists:
   - **Subject Polygon Vertex List**: Contains original subject vertices with intersection points inserted in traversal order.
   - **Clipping Window Vertex List**: Contains window corner vertices with intersection points inserted in traversal order.
3. **Intersection Classification**:
   Every intersection point is classified as either:
   - **Entering Vertex**: The subject polygon edge crosses from outside to inside the clipping window.
   - **Exiting Vertex**: The subject polygon edge crosses from inside to outside the clipping window.
4. **List Traversal Rules**:
   - Begin at an unvisited **Entering** intersection point.
   - Traverse forward along the **Subject Polygon List** until an **Exiting** intersection is reached (outputting all traversed vertices).
   - At the exiting intersection, **switch** to the **Clipping Window List**.
   - Traverse along the clipping window list (in clockwise direction) until an **Entering** intersection point is encountered.
   - **Switch back** to the subject polygon list and repeat until the traversal loops back to the starting vertex, forming a closed polygon.
   - Repeat for any remaining unvisited entering intersections to extract all disjoint polygon pieces.

---

## 2. Example: Sutherland-Hodgman Pipeline Diagram
```
Original Polygon       1. Clip Left Boundary     2. Clip Right Boundary     3. Clip Bottom & Top
     +-------+                +-----+                   +-----+                    +-----+
    /         \               |     \                   |     |                    |     |
   /  WINDOW   \    ===>      | WIND \       ===>       |WIND |         ===>       +-----+
  /             \             |       \                 |     |                    |     |
 +---------------+            +--------+                +-----+                    +-----+
```

---

## 3. Applications & Use Cases
1. **Shadow Volume Generation & Stencil Shadows (Doom 3 engine)**: Shadow casting algorithms clip light frustum polygons against occluder geometry to build closed shadow volume meshes.
2. **Geographical Information Systems (GIS Map Overlay)**: Merging geographic layers (e.g., intersecting land use polygons with zoning districts) requires Weiler-Atherton arbitrary polygon clipping to calculate intersection areas.
3. **Desktop Window Compositors (Wayland, Windows DWM)**: Overlapping application windows clip damaged rectangular regions to ensure translucent and occluded surfaces are updated efficiently.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Sutherland-Hodgman Triangle Clipping Trace [KTU Dec 2021 / May 2019 - 9 Marks]
**Problem**:
A triangle has vertices $V_1(10, 10)$, $V_2(60, 60)$, and $V_3(60, 10)$.
Clip this triangle against a rectangular window with boundaries:
$$x_{\min} = 20, \quad x_{\max} = 50, \quad y_{\min} = 20, \quad y_{\max} = 50$$
Show the output vertex sequence after clipping against each boundary: Left, Right, Bottom, and Top.

**Step-by-step Solution**:
1. **Initial Vertex List**:
   $$P_0 = [V_1(10, 10), \ V_2(60, 60), \ V_3(60, 10)]$$

2. **Stage 1: Clip Against LEFT Boundary ($x = 20$)**:
   - Edge $V_1(10, 10) \to V_2(60, 60)$: Out $\to$ In.
     - Slope $m = \frac{60 - 10}{60 - 10} = 1$.
     - Intersection at $x = 20$: $y = 10 + 1(20 - 10) = 20 \implies I_1(20, 20)$.
     - Output: $[I_1(20, 20), \ V_2(60, 60)]$.
   - Edge $V_2(60, 60) \to V_3(60, 10)$: In $\to$ In.
     - Output: $[V_3(60, 10)]$.
   - Edge $V_3(60, 10) \to V_1(10, 10)$: In $\to$ Out.
     - Horizontal edge $y = 10$. Intersection at $x = 20 \implies I_2(20, 10)$.
     - Output: $[I_2(20, 10)]$.
   - **Output of Left Clipper**:
     $$P_{\text{Left}} = [I_1(20, 20), \ V_2(60, 60), \ V_3(60, 10), \ I_2(20, 10)]$$

3. **Stage 2: Clip Against RIGHT Boundary ($x = 50$)**:
   - Edge $I_1(20, 20) \to V_2(60, 60)$: In $\to$ Out.
     - Intersection at $x = 50$: $y = 20 + 1(50 - 20) = 50 \implies I_3(50, 50)$.
     - Output: $[I_3(50, 50)]$.
   - Edge $V_2(60, 60) \to V_3(60, 10)$: Out $\to$ Out ($x=60 > 50$).
     - Output: $[\text{None}]$.
   - Edge $V_3(60, 10) \to I_2(20, 10)$: Out $\to$ In.
     - Horizontal edge $y = 10$. Intersection at $x = 50 \implies I_4(50, 10)$.
     - Output: $[I_4(50, 10), \ I_2(20, 10)]$.
   - Edge $I_2(20, 10) \to I_1(20, 20)$: In $\to$ In.
     - Output: $[I_1(20, 20)]$.
   - **Output of Right Clipper**:
     $$P_{\text{Right}} = [I_3(50, 50), \ I_4(50, 10), \ I_2(20, 10), \ I_1(20, 20)]$$

4. **Stage 3: Clip Against BOTTOM Boundary ($y = 20$)**:
   - Edge $I_3(50, 50) \to I_4(50, 10)$: In $\to$ Out.
     - Vertical edge $x = 50$. Intersection at $y = 20 \implies I_5(50, 20)$.
     - Output: $[I_5(50, 20)]$.
   - Edge $I_4(50, 10) \to I_2(20, 10)$: Out $\to$ Out ($y = 10 < 20$).
     - Output: $[\text{None}]$.
   - Edge $I_2(20, 10) \to I_1(20, 20)$: Out $\to$ In.
     - Vertical edge $x = 20$. Endpoint $I_1$ is on boundary $(20, 20)$.
     - Output: $[I_1(20, 20)]$.
   - Edge $I_1(20, 20) \to I_3(50, 50)$: In $\to$ In.
     - Output: $[I_3(50, 50)]$.
   - **Output of Bottom Clipper**:
     $$P_{\text{Bottom}} = [I_5(50, 20), \ I_1(20, 20), \ I_3(50, 50)]$$

5. **Stage 4: Clip Against TOP Boundary ($y = 50$)**:
   - All vertices in $P_{\text{Bottom}}$ have $y \le 50$. All edges are In $\to$ In.
   - **Final Clipped Polygon Vertices**:
     $$\mathbf{[I_5(50, 20), \ I_1(20, 20), \ I_3(50, 50)]}$$
   - Notice that the final clipped polygon is a triangle with vertices at $(50, 20)$, $(20, 20)$, and $(50, 50)$.

---

### Example 2: Weiler-Atherton Linked List Classification [KTU Analytical Pattern]
**Problem**:
Explain how Weiler-Atherton manages entering and exiting vertices on a concave U-shaped polygon that is clipped into two disconnected components.

**Step-by-step Solution**:
1. When traversing the subject polygon perimeter, the boundary will cross into the clipping window, exit, re-enter, and exit again.
2. Intersections are labeled:
   - $I_1$: Entering (outside to inside).
   - $I_2$: Exiting (inside to outside).
   - $I_3$: Entering (outside to inside).
   - $I_4$: Exiting (inside to outside).
3. **First Component Extraction**:
   - Start at $I_1$ (Entering).
   - Follow subject polygon list to $I_2$ (Exiting).
   - Switch to window list at $I_2$. Follow window boundary clockwise until reaching $I_1$ (Entering).
   - Loop closed: Output Polygon 1.
4. **Second Component Extraction**:
   - Start at unvisited entering intersection $I_3$.
   - Follow subject polygon list to $I_4$ (Exiting).
   - Switch to window list at $I_4$. Follow window boundary clockwise until reaching $I_3$ (Entering).
   - Loop closed: Output Polygon 2.
5. Two completely disjoint polygons are produced with zero false bridging edges.

---

### Example 3: Edge Case Analysis (Vertex on Boundary) [KTU Analytical Pattern]
**Problem**:
In Sutherland-Hodgman clipping, how is an edge processed if its end vertex lies exactly on the clipping boundary?

**Step-by-step Solution**:
1. Mathematically, a point lying on the clipping boundary satisfies $x = x_{\text{bound}}$ or $y = y_{\text{bound}}$.
2. By convention, points on the boundary are defined as **IN**.
3. Therefore:
   - If $V_1$ is outside and $V_2$ is on the boundary: Treated as Out $\to$ In. The intersection point $V' = V_2$ is identical to $V_2$. To avoid duplicating points, the algorithm detects $V' = V_2$ and outputs only **$V_2$**.
   - If $V_1$ is inside and $V_2$ is on the boundary: Treated as In $\to$ In. Output **$V_2$**.
   - If both $V_1$ and $V_2$ lie along the boundary: Treated as In $\to$ In. Output **$V_2$**.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU January 2023 / June 2022 - 9 Marks]
**Question**:
Explain the two different polygon clipping algorithms with illustrations.

**Solution**:
1. **Sutherland-Hodgman Polygon Clipping Algorithm**:
   - **Method**: Sutherland-Hodgman clips a polygon against a convex window by processing the polygon sequentially against each infinite clipping boundary line (Left, Right, Bottom, Top).
   - **Edge Processing Rules**: Each directed edge $V_1 \to V_2$ is evaluated under four conditions:
     1. In $\to$ In: Output $V_2$.
     2. In $\to$ Out: Calculate intersection $V'$ with boundary line; output $V'$.
     3. Out $\to$ Out: Output nothing.
     4. Out $\to$ In: Calculate intersection $V'$ with boundary line; output $V'$, then output $V_2$.
   - **Limitation**: When clipping concave polygons that split into separate components, Sutherland-Hodgman creates spurious connecting edges along the boundary lines because it only outputs a single vertex list.
2. **Weiler-Atherton Polygon Clipping Algorithm**:
   - **Method**: Developed to overcome the concave limitation of Sutherland-Hodgman. It can clip any arbitrary (convex or concave) polygon against an arbitrary clipping polygon and outputs multiple separate, disconnected polygon contours.
   - **Algorithm Steps**:
     1. Calculate all intersections between the subject polygon and the clipping window.
     2. Create two circular linked lists: the Subject Polygon List and the Clipping Window List, inserting all intersection points into both lists in topological order.
     3. Classify intersections as **Entering** (subject edge enters clipping window) or **Exiting** (subject edge exits clipping window).
     4. Traverse from an unvisited Entering intersection along the subject polygon list until an Exiting intersection is reached.
     5. Switch to the clipping window list and traverse clockwise until an Entering intersection is encountered.
     6. Repeat until the path returns to the starting intersection, closing the polygon component.
     7. Continue for all remaining unvisited Entering intersections to produce all disjoint polygon pieces.

---

### Question 2 [KTU December 2019 / December 2020 - 4 Marks]
**Question**:
Why does the Sutherland-Hodgman algorithm fail for concave polygons? How is this resolved?

**Solution**:
1. **Why Sutherland-Hodgman Fails for Concave Polygons**:
   - The Sutherland-Hodgman algorithm is architected around a single sequential output stream: the output of one boundary clipper is fed directly as the input to the next.
   - When a concave polygon (such as an inverted V or U-shape) is clipped, the visible portion may consist of two or more completely disconnected, disjoint polygon regions.
   - Because Sutherland-Hodgman can only maintain a single continuous vertex sequence, it connects the separate regions by drafting a false, extraneous line segment along the clipping boundary, producing an erroneous joined polygon instead of two separate polygons.
2. **How It is Resolved**:
   - It is resolved by deploying the **Weiler-Atherton Polygon Clipping Algorithm**, which utilizes dual circular linked lists (Subject List and Window List) and classifies intersections into Entering and Exiting points.
   - By following entering paths through the polygon and exiting paths along the window boundary, Weiler-Atherton outputs independent closed vertex lists for each disconnected component without creating artificial boundary bridges.

