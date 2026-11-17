# Scan Conversion & Polygon Filling Algorithms

## 1. Explanation
In computer graphics, a polygon is mathematically represented as an ordered sequence of planar vertex coordinates: $P = \{V_1, V_2, \dots, V_n\}$. While rendering a wireframe polygon requires merely drawing $n$ bounding line segments, **solid area scan conversion** (polygon filling) requires determining every interior pixel lying within the polygon boundary and coloring it in the frame buffer.

---

### Inside-Outside Tests
To determine whether an arbitrary query point $P(x, y)$ lies inside or outside an arbitrary (possibly self-intersecting or concave) polygon, two standardized topological rules are used:

#### 1. Odd-Even Parity Rule (Even-Odd Test)
- Construct a test ray starting from query point $P(x, y)$ extending to infinity in any arbitrary direction (typically along the positive $X$-axis).
- Count the number of polygon boundary edges intersected by the ray.
- **Decision**:
  - If the intersection count is **odd**, point $P$ is **inside** the polygon.
  - If the intersection count is **even**, point $P$ is **outside** the polygon.
- *Edge Vertex Case Handling*: If the test ray passes directly through a polygon vertex, the vertex is counted as an intersection if and only if the two adjoining edges lie on opposite sides of the ray. If both edges lie on the same side of the ray (a local minimum or maximum), it is counted as 0 or 2 intersections (even).

#### 2. Winding Number Rule (Non-Zero Winding Rule)
- Construct a test ray from point $P$ to infinity.
- Initialize a counter $\text{Winding Number } W = 0$.
- Traverse the polygon edges in their defined direction (clockwise or counter-clockwise).
- For every edge intersecting the test ray:
  - Add $+1$ if the edge crosses the ray from right-to-left.
  - Subtract $-1$ if the edge crosses the ray from left-to-right.
- **Decision**:
  - If the final winding number $W \ne 0$, point $P$ is **inside** the polygon.
  - If $W = 0$, point $P$ is **outside** the polygon.

---

### Polygon Filling Algorithms

#### 1. Scan-Line Polygon Fill Algorithm
The Scan-Line Fill algorithm is an image-space polygon rasterization method that exploits spatial coherence (edge coherence and scanline coherence) to efficiently determine interior pixel spans without recursive function overhead.

##### Algorithm Data Structures:
1. **Edge Table (ET)**:
   - A pre-sorted table containing all non-horizontal polygon edges.
   - Edges are bucket-sorted into indexed slots corresponding to their minimum $y$-coordinate ($y_{\min}$).
   - Within each bucket, edges are sorted in ascending order of their initial $x$-value ($x$ at $y_{\min}$).
   - Each edge record stores:
     $$\text{Edge Record} = \{ y_{\max}, \ x_{\text{current}}, \ \frac{1}{m} \}$$
     where $y_{\max}$ is the upper $y$ limit, $x_{\text{current}}$ is the $x$-intercept at the current scanline, and $\frac{1}{m} = \frac{x_2 - x_1}{y_2 - y_1}$ is the inverse slope (the incremental change in $x$ per unit increment in $y$).
2. **Active Edge Table (AET)**:
   - Contains only the edges that currently intersect the active scanline $y$.
   - Edges in the AET are kept sorted in strictly ascending order of their current $x$-coordinates.

##### Step-by-Step Execution Loop:
1. Initialize scanline $y$ to the lowest $y_{\min}$ in the Edge Table.
2. Transfer edges whose $y_{\min} = y$ from the ET into the AET.
3. Remove edges from the AET whose $y_{\max} = y$ (expired edges).
4. Sort the remaining edges in the AET by ascending $x_{\text{current}}$.
5. Pair adjacent edges in the sorted AET: $(e_1, e_2), (e_3, e_4), \dots$
6. Fill all pixels on the scanline between the pairs: from $x_1$ to $x_2$, from $x_3$ to $x_4$, etc.
7. Increment scanline: $y \leftarrow y + 1$.
8. Update $x$-coordinates for all active edges using the incremental recurrence:
   $$x_{\text{new}} = x_{\text{old}} + \frac{1}{m}$$
9. Repeat until both ET and AET are empty.

---

#### 2. Boundary-Fill Algorithm
An area-filling method that starts at an interior **seed point** $(x, y)$ and expands outward recursively until a specified **boundary color** is encountered.

##### 4-Connected vs. 8-Connected:
- **4-Connected**: Checks adjacent orthogonal neighbors $(x \pm 1, y)$ and $(x, y \pm 1)$. Can fail to fill across diagonal boundary cracks.
- **8-Connected**: Checks orthogonal and diagonal neighbors. Prevents leaking across diagonal boundaries.

##### Recursive Pseudocode (4-Connected):
```c
void BoundaryFill4(int x, int y, int fillColor, int boundaryColor) {
    int current = GetPixel(x, y);
    if (current != boundaryColor && current != fillColor) {
        SetPixel(x, y, fillColor);
        BoundaryFill4(x + 1, y,     fillColor, boundaryColor); // East
        BoundaryFill4(x - 1, y,     fillColor, boundaryColor); // West
        BoundaryFill4(x,     y + 1, fillColor, boundaryColor); // North
        BoundaryFill4(x,     y - 1, fillColor, boundaryColor); // South
    }
}
```

---

#### 3. Flood-Fill Algorithm
Used when the polygon boundary is defined by multiple different colors, but the interior region has a uniform **interior color** (or old color) that needs to be replaced by a new **fill color**.

##### Recursive Pseudocode (4-Connected):
```c
void FloodFill4(int x, int y, int newColor, int oldColor) {
    if (GetPixel(x, y) == oldColor) {
        SetPixel(x, y, newColor);
        FloodFill4(x + 1, y,     newColor, oldColor); // East
        FloodFill4(x - 1, y,     newColor, oldColor); // West
        FloodFill4(x,     y + 1, newColor, oldColor); // North
        FloodFill4(x,     y - 1, newColor, oldColor); // South
    }
}
```

---

## 2. Example: Scan-Line Edge Table & Active Edge Table Processing
```
Scanline y = 8 +---------------------------------------------------+
               |                                                   |
Scanline y = 7 +-----------*=======================*---------------+ [Fill Span]
               |          /                         \              |
Scanline y = 6 +---------*===========================*-------------+ [Fill Span]
               |        /                             \            |
               |      Edge 1                        Edge 2         |
               |      (1/m = 1.0)                   (1/m = -1.0)   |
Scanline y = 5 +-----*=================================*-----------+ [Fill Span]
                     x_1                              x_2
```
As scanline $y$ increments from 5 to 7, edge intersection coordinates update:
$x_1 \leftarrow x_1 + 1.0$ and $x_2 \leftarrow x_2 - 1.0$.

---

## 3. Applications & Use Cases
1. **Vector Drawing Packages & Font Rasterization (FreeType, PostScript)**: TrueType and OpenType fonts store character glyphs (e.g. letter 'B') as closed vector spline contours. The rasterizer executes scan-line polygon fill with the non-zero winding rule to fill font glyph interiors without raster gaps.
2. **Paint Bucket Tool in Digital Art Software (Photoshop, GIMP)**: The interactive bucket tool initiates an optimized scanline flood-fill algorithm starting from the user's click coordinate.
3. **Geographic Information Systems (GIS)**: GIS software (QGIS, ArcGIS) renders geopolitical boundaries, water bodies, and land parcels by applying scan-line polygon fill across multi-million vertex polygon tables.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Scan-Line Polygon Fill Edge Table Construction [KTU Dec 2023 / June 2024 - 9 Marks]
**Problem**:
Consider a polygon with four vertices: $A(2, 2)$, $B(8, 2)$, $C(10, 8)$, and $D(4, 8)$.
1. Construct the initial Edge Table (ET) for this polygon.
2. Trace the Active Edge Table (AET) for scanlines $y = 3, 4, 5$, showing filled pixel intervals.

**Step-by-step Solution**:
1. **Edge Calculations**:
   - Edge $AB$: From $(2, 2)$ to $(8, 2)$. This is a horizontal edge ($y_1 = y_2 = 2$). Horizontal edges are excluded from the Edge Table because their spans are handled directly on scanline $y = 2$.
   - Edge $BC$: From $(8, 2)$ to $(10, 8)$.
     $$y_{\min} = 2, \quad y_{\max} = 8, \quad x_{\text{current}} = 8$$
     $$\frac{1}{m} = \frac{10 - 8}{8 - 2} = \frac{2}{6} = \frac{1}{3}$$
   - Edge $CD$: From $(10, 8)$ to $(4, 8)$. Horizontal edge; excluded from ET.
   - Edge $DA$: From $(4, 8)$ to $(2, 2)$.
     $$y_{\min} = 2, \quad y_{\max} = 8, \quad x_{\text{current}} = 2$$
     $$\frac{1}{m} = \frac{4 - 2}{8 - 2} = \frac{2}{6} = \frac{1}{3}$$
2. **Edge Table (ET)**:
   - Index $y = 2$:
     - Node 1: $\{ y_{\max} = 8, \ x = 2, \ \frac{1}{m} = \frac{1}{3} \}$ (Edge $DA$)
     - Node 2: $\{ y_{\max} = 8, \ x = 8, \ \frac{1}{m} = \frac{1}{3} \}$ (Edge $BC$)
   - Indices $y = 3, 4, 5, 6, 7, 8$: Empty.
3. **Scanline Tracing**:
   - **Scanline $y = 3$**:
     - Increment $x$: $x_1 = 2 + 1/3 \approx 2.33$, $x_2 = 8 + 1/3 \approx 8.33$.
     - Span filled: $x \in [\lceil 2.33 \rceil, \lfloor 8.33 \rfloor] \implies \mathbf{x = 3 \text{ to } 8}$.
   - **Scanline $y = 4$**:
     - Increment $x$: $x_1 = 2.33 + 0.33 = 2.67$, $x_2 = 8.33 + 0.33 = 8.67$.
     - Span filled: $x \in [\lceil 2.67 \rceil, \lfloor 8.67 \rfloor] \implies \mathbf{x = 3 \text{ to } 8}$.
   - **Scanline $y = 5$**:
     - Increment $x$: $x_1 = 2.67 + 0.33 = 3.00$, $x_2 = 8.67 + 0.33 = 9.00$.
     - Span filled: $x \in [3, 9] \implies \mathbf{x = 3 \text{ to } 9}$.

---

### Example 2: Odd-Even Test vs. Winding Number on Self-Intersecting Polygons [KTU Analytical Pattern]
**Problem**:
Consider a self-intersecting star pentagon with ordered vertices $V_1(0, 10), V_2(2, 2), V_3(10, 2), V_4(4, -2), V_5(6, -10), V_6(0, -5), V_7(-6, -10), V_8(-4, -2), V_9(-10, 2), V_{10}(-2, 2)$.
Determine whether the central core of the star is classified as **inside** or **outside** under:
1. The Odd-Even Parity Rule.
2. The Non-Zero Winding Number Rule.

**Step-by-step Solution**:
1. **Odd-Even Parity Test**:
   - Cast a ray from the center point $O(0, 0)$ to $+X$ infinity.
   - The ray crosses exactly two boundary edges (Edge $V_2 V_3$ and Edge $V_4 V_5$).
   - Total edge intersections $= 2$ (an **even** number).
   - Under the odd-even rule: **The center is classified as OUTSIDE (unfilled hole)**.
2. **Non-Zero Winding Number Rule**:
   - Both edges cross the ray in the same directional orientation (both winding clockwise relative to origin).
   - Each crossing adds $+1$ to the winding number: $W = +1 + 1 = 2$.
   - Since $W = 2 \ne 0$: **The center is classified as INSIDE (solid filled)**.
3. **Significance**: Winding number rules prevent unwanted transparent hollow cores in self-intersecting vector art.

---

### Example 3: Stack Depth and Memory Consumption in Recursive Boundary Fill [KTU Analytical Pattern]
**Problem**:
A square region of size $500 \times 500$ pixels is filled using the naive 4-connected recursive boundary-fill algorithm.
1. What is the maximum recursive stack depth encountered?
2. If each recursive call frame consumes 32 bytes of stack memory, determine the maximum stack memory required. Why does this necessitate scanline filling in practical software?

**Step-by-step Solution**:
1. **Maximum Stack Depth**:
   - In the worst-case fill order, depth-first recursion traverses the entire area before backtracking.
   - Total pixels in region $= 500 \times 500 = 250,000 \text{ pixels}$.
   - Maximum stack depth $= 250,000$ active stack frames.
2. **Stack Memory Requirement**:
   $$\text{Stack Memory} = 250,000 \times 32 \text{ bytes} = 8,000,000 \text{ bytes} \approx 7.63 \text{ MB}$$
3. **Engineering Impact**:
   Standard thread stack limits on modern OSs are typically 1 MB to 8 MB. A recursive boundary fill on a modest $1080\text{p}$ image ($2 \times 10^6$ pixels) demands $>64\text{ MB}$ of stack, triggering instant **stack overflow** crash. Hence, real-world graphics engines deploy iterative **scanline fill algorithms** that push only horizontal span endpoints $(y, x_{\text{left}}, x_{\text{right}})$ onto an auxiliary heap queue.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU January 2023 / December 2018 - 4 Marks]
**Question**:
Write the flood fill algorithm to fill a polygon. Differentiate between 4-connected and 8-connected flood fill.

**Solution**:
1. **Flood Fill Algorithm**:
   Flood fill replaces an existing target interior color (`oldColor`) with a replacement fill color (`newColor`) starting from a seed point $(x, y)$:
   ```c
   void FloodFill4(int x, int y, int newColor, int oldColor) {
       if (GetPixel(x, y) == oldColor) {
           SetPixel(x, y, newColor);
           FloodFill4(x + 1, y,     newColor, oldColor); // Right
           FloodFill4(x - 1, y,     newColor, oldColor); // Left
           FloodFill4(x,     y + 1, newColor, oldColor); // Up
           FloodFill4(x,     y - 1, newColor, oldColor); // Down
       }
   }
   ```
2. **Differences Between 4-Connected and 8-Connected Approaches**:

| Feature | 4-Connected Flood Fill | 8-Connected Flood Fill |
|---|---|---|
| **Neighbor Connectivity** | Tests only 4 orthogonal neighbors: $(x \pm 1, y)$ and $(x, y \pm 1)$. | Tests all 8 neighbors (4 orthogonal + 4 diagonal neighbors: $(x \pm 1, y \pm 1)$). |
| **Diagonal Leakage** | Confined within diagonal boundary barriers; will not leak across corners. | Can step diagonally across single-pixel diagonal boundaries and leak out. |
| **Complex Area Coverage** | Fails to reach corner-adjacent regions separated by diagonal pixel connections. | Completely fills complex regions connected by diagonal paths. |
| **Stack Overhead** | Makes 4 recursive branches per pixel. | Makes 8 recursive branches per pixel (higher stack memory consumption). |

---

### Question 2 [KTU May 2019 / June 2022 - 9 Marks]
**Question**:
Explain the Scan-Line polygon fill algorithm with suitable diagrams. Describe how the Edge Table (ET) and Active Edge Table (AET) are maintained.

**Solution**:
1. **Scan-Line Polygon Fill Overview**:
   The scanline algorithm operates by sweeping horizontal scanlines across a polygon from bottom to top. For each scanline, it calculates the intersection points with all intersecting polygon edges, sorts the intersections in increasing order of $x$, and colors the pixels between odd and even intersection pairs ($x_1$ to $x_2$, $x_3$ to $x_4$).
2. **Edge Table (ET) Management**:
   - Horizontal edges are discarded.
   - All non-horizontal edges are stored in an array of linked lists indexed by the edge's minimum $y$ value ($y_{\min}$).
   - Each edge record stores:
     - $y_{\max}$: Upper limit of the edge.
     - $x_{\text{start}}$: $x$-coordinate at $y_{\min}$.
     - $\Delta x / \Delta y$ ($1/m$): Inverse slope.
   - Edges within each bucket are sorted by ascending $x$.
3. **Active Edge Table (AET) Management**:
   - The AET maintains the list of edges that intersect the current scanline $y$.
   - **Step 1 (Add)**: At scanline $y$, all edges in ET at index $y$ are moved into the AET.
   - **Step 2 (Remove)**: Any edge in AET whose $y_{\max} = y$ is removed (since it does not extend to scanline $y+1$).
   - **Step 3 (Sort)**: The active edges in AET are sorted in ascending order of current $x$.
   - **Step 4 (Fill)**: Scanline pixels between pairs of active edge intersections $(x_1 \to x_2, x_3 \to x_4)$ are set to the fill color.
   - **Step 5 (Update)**: For the next scanline $y+1$, the $x$ coordinate of each active edge is updated:
     $$x_{y+1} = x_y + \frac{1}{m}$$
4. **Vertex Intersection Parity Rule**:
   When a scanline intersects a polygon vertex, the vertex is shared by two edges.
   - If both edges lie on opposite sides of the scanline (one goes up, one goes down), the vertex counts as **one** intersection.
   - If both edges lie on the same side of the scanline (local minimum or maximum), the vertex counts as **two** intersections (or zero), maintaining correct odd-even parity.

