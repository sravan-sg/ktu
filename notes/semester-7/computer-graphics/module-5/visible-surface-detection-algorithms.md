# Visible Surface Detection Algorithms (Hidden Surface Elimination)

## 1. Explanation

When rendering a 3D scene containing multiple objects, many polygon surfaces are occluded (hidden) behind other surfaces from the observer's viewpoint. **Visible Surface Detection** (also called **Hidden Surface Elimination — HSE**, or **Hidden Surface Removal — HSR**) is the set of algorithms that determine which parts of each surface are visible to the observer, and discard all hidden parts before rasterization.

### Why This Is Hard

The visibility problem is fundamentally a **sorting problem in 3D**. For $n$ polygons, brute-force comparison requires $O(n^2)$ pairwise tests. Additionally, polygons can **partially overlap** (one polygon in front of another at some pixels, but behind at other pixels), and **cyclic overlaps** (A in front of B, B in front of C, C in front of A) can occur, making simple sorting impossible.

---

### Classification: Object-Space vs. Image-Space Methods

| Criterion | Object-Space Methods | Image-Space Methods |
|---|---|---|
| **Domain** | Continuous 3D coordinate space | Discrete 2D raster pixel grid |
| **Complexity** | $O(n^2)$ or $O(n \log n)$ in $n$ polygons | $O(n \cdot p)$ where $p = W \times H$ pixels |
| **Resolution** | Resolution-independent | Depends on screen resolution |
| **Examples** | Back-Face Removal, Painter's Algorithm (Depth Sort), BSP-tree | Z-Buffer, A-Buffer, Scan-Line, Warnock |

---

### 1. Back-Face Removal (Back-Face Culling)

**Principle**: For a closed solid polyhedron, any polygon face whose outward surface normal points **away** from the viewer cannot possibly be seen — it is on the "back" of the object. Remove these faces before further processing.

**Mathematical test**: Given plane equation $Ax + By + Cz + D = 0$ with outward normal $\vec{N} = (A, B, C)$ and viewing direction $\vec{V}$ (from surface toward camera):

$$\text{Visible (front-face): } \vec{N} \cdot \vec{V} > 0$$
$$\text{Hidden (back-face): } \vec{N} \cdot \vec{V} \le 0$$

**Simplified test** for viewing along $-Z$ axis (standard right-hand coordinate system):
- Viewing vector $\vec{V} = (0, 0, -1)$
- $\vec{N} \cdot \vec{V} = -C$
- **Back-face condition**: $C \ge 0$ (normal's Z-component is non-negative → faces away from camera)
- **Front-face condition**: $C < 0$ (normal's Z-component is negative → faces toward camera)

**Identifying back-faces using 2D vertex order**:
In screen space, a polygon appears as a clockwise sequence of vertices if it is a back-face (for CCW front-face convention):
$$\text{Signed Area} = \sum_{i=0}^{n-1} (x_i \cdot y_{i+1} - x_{i+1} \cdot y_i)$$
- If Signed Area > 0: CCW (front-face in standard OpenGL convention)
- If Signed Area < 0: CW (back-face → cull)

**Efficiency**: Eliminates approximately **50% of all polygons** in a typical closed solid — before any expensive depth calculations.

**Limitation**: Only works for closed convex polyhedra. Does not resolve visibility between **different objects** or handle **self-occlusion** in concave objects.

---

### 2. Depth-Buffer (Z-Buffer) Algorithm

Invented by Edwin Catmull (1974), this is the universally dominant visible surface algorithm implemented in all modern GPU hardware.

**Core Idea**: For each pixel, keep track of the **depth (z-coordinate)** of the closest surface seen so far. When rasterizing a new polygon fragment at pixel $(x, y)$, only update the color if the new fragment is closer than the previously recorded depth.

**Data Structures**:
- **Frame Buffer** `FB[x][y]`: RGB color of the visible surface at pixel $(x, y)$.
- **Depth Buffer (Z-Buffer)** `DB[x][y]`: Minimum $z$-value (closest depth) seen at pixel $(x, y)$.

**Algorithm**:
```
Initialize:
  For all pixels (x, y):
    DB[x][y] = +∞  (or 1.0 in normalized [0,1] depth space)
    FB[x][y] = background_color

For each polygon P in scene:
  For each pixel (x, y) covered by P's projected area:
    z = depth of polygon P at pixel (x, y)
    If z < DB[x][y]:           // Closer than current closest
      DB[x][y] = z             // Update depth
      FB[x][y] = shade(P, x, y) // Update color
```

**Incremental Depth Computation Along Scanline**:

The polygon plane equation: $Ax + By + Cz + D = 0$ gives:
$$z(x, y) = -\frac{Ax + By + D}{C}$$

For the next pixel along the same scanline $(x+1, y)$:
$$z(x+1, y) = -\frac{A(x+1) + By + D}{C} = z(x,y) - \frac{A}{C}$$

$$\boxed{\Delta z = -\frac{A}{C} \quad \text{(constant per polygon per scanline)}}$$

This means depth along a scanline is updated by a **single subtraction** — no division needed per pixel.

**Properties**:
- **Time**: $O(n \cdot p)$ — proportional to number of polygons × screen pixels.
- **Space**: $O(p)$ — just the depth buffer array (same size as frame buffer).
- **Handles any scene complexity**: Correctly resolves interpenetrating polygons, cyclic overlaps, and complex scenes without special cases.
- **Weakness**: Cannot handle transparency/translucency (last fragment wins, regardless of alpha). The A-Buffer solves this.

---

### 3. A-Buffer Algorithm

The A-Buffer (Accumulation Buffer / Anti-aliased Buffer) was developed by Loren Carpenter at Pixar (1984) to handle **transparency, translucency, and sub-pixel antialiasing** — limitations of the standard Z-Buffer.

**Key Innovation**: Instead of one depth value per pixel, the A-Buffer stores a **linked list of fragment records** at each pixel:

```
Fragment record structure:
  struct AFragment {
    RGB color;        // Surface color at this fragment
    float depth;      // z-value of this fragment
    float alpha;      // Opacity (0=transparent, 1=opaque)
    int coverage;     // 4×4 bit mask indicating sub-pixel coverage
    AFragment* next;  // Pointer to next fragment (linked list)
  };
```

**Algorithm**:
1. For each polygon fragment at pixel $(x, y)$:
   - If fragment is **100% opaque and covers full pixel**: replace fragment at this pixel if closer (like Z-Buffer).
   - If fragment is **translucent or partial**: append to linked list at $(x, y)$.
2. After all polygons are processed: for each pixel with a linked list, **sort fragments by depth** (back-to-front) and **alpha-composite** them:
   $$C_{\text{out}} = \alpha_{\text{front}} \cdot C_{\text{front}} + (1 - \alpha_{\text{front}}) \cdot C_{\text{back}}$$

**Used by**: Pixar's RenderMan (original production use), modern GPU Order-Independent Transparency (OIT) algorithms.

**What information is stored in an A-buffer linked list?**:
- Object identifier
- Surface color (RGB)
- Opacity/alpha value
- Depth value ($z$)
- 4×4 coverage bitmask (16 bits) for sub-pixel antialiasing
- Pointer to next fragment in list

---

### 4. Depth-Sorting Method (Painter's Algorithm)

Inspired by how oil painters work: **paint far objects first, then paint nearer objects on top** — naturally achieving correct occlusion.

**Step-by-Step Procedure**:

**Step 1 — Sort**: Sort all polygons in **descending order of maximum $z$-coordinate** ($z_{\max}$), so the farthest polygon is first.

**Step 2 — Render in order**: For each polygon in sorted order, rasterize it into the frame buffer. Later polygons (closer to camera) overwrite earlier ones, achieving correct visibility.

**But wait — cyclic and intersecting overlap breaks simple sorting!**

**Step 3 — Five Overlap Tests** (performed when $z$-extents of two adjacent sorted polygons $P$ and $Q$ overlap, i.e., $z_{\min}(P) < z_{\max}(Q)$):

If any test **passes** (proves no ambiguity), proceed with current order:

| Test | Condition | Pass means... |
|---|---|---|
| **Test 1** (X-separation) | $x$-extents do not overlap | Draw in any order |
| **Test 2** (Y-separation) | $y$-extents do not overlap | Draw in any order |
| **Test 3** (Q behind P's plane) | All vertices of $Q$ lie on the far side of $P$'s plane | Draw $Q$ before $P$ |
| **Test 4** (P in front of Q's plane) | All vertices of $P$ lie on the near side of $Q$'s plane | Draw $Q$ before $P$ |
| **Test 5** (2D projection separation) | 2D projected outlines of $P$ and $Q$ don't overlap on screen | No visibility conflict |

If **all 5 tests fail**: Cyclic overlap — **split one polygon** along the plane of the other and re-sort.

**Complexity**: $O(n \log n)$ for sorting + $O(n^2)$ worst-case for overlap tests.

**Failure case — Cyclic overlap**: Three triangles A, B, C where A is in front of B at some pixels, B is in front of C at some, C is in front of A at others. No single linear ordering resolves this. Must split.

---

### 5. Scan-Line Visible Surface Detection

Extends the 2D scan-line polygon fill to handle 3D visibility.

**Data Structures**:
- **Edge Table (ET)** and **Active Edge Table (AET)**: Same as 2D polygon filling, but for all polygons simultaneously.
- **Active Polygon Table (APT)**: For each scanline, lists all polygons that cross the current scanline.

**Algorithm**:
1. For each scanline $y$:
   - Update AET: add new polygon edges starting at $y$; remove edges ending at $y$.
   - For each span along the scanline, determine which active polygon is **closest** (minimum $z$) using the incremental $z$ formula.
   - Write the color of the closest polygon to the frame buffer at that pixel.

**Advantage over Z-Buffer**: Only needs 1D depth comparison per scanline span, not per pixel. More memory-efficient (no full 2D depth buffer). **Disadvantage**: Complex data structure management; harder to parallelize than Z-Buffer.

---

### 6. Warnock Algorithm (Area Subdivision)

A recursive divide-and-conquer algorithm:

1. Consider the viewport as the initial area.
2. For the current area, check the polygon list:
   - **Surrounding polygon** (one polygon completely encloses the area): Draw that polygon's color.
   - **Disjoint polygons** (no polygon overlaps the area): Draw background color.
   - **Contained polygon** (all polygons fit completely inside the area and have no overlap): Draw them all.
   - **Intersecting polygons** (ambiguous): **Subdivide** the area into 4 quadrants; recursively apply.
3. Stop when area is a single pixel — use Z-Buffer logic to pick the closest polygon.

**Complexity**: Efficient for sparse scenes with few polygons relative to screen area; degrades for dense scenes.

---

## 2. Example: Z-Buffer Trace

```
Two overlapping triangles on scanline y=5:
  Triangle A (plane: z = 10 everywhere)
  Triangle B (plane: z = 5 everywhere, overlaps Triangle A in x=[3,7])

Initial:  DB[0..9] = [∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

Process Triangle A (covers x=1 to x=8, z=10):
  DB[1..8] = [10, 10, 10, 10, 10, 10, 10, 10]
  FB[1..8] = red (Triangle A color)

Process Triangle B (covers x=3 to x=7, z=5):
  At x=3: z=5 < DB[3]=10 → update DB[3]=5, FB[3]=blue
  At x=4: z=5 < DB[4]=10 → update DB[4]=5, FB[4]=blue
  ...
  At x=7: z=5 < DB[7]=10 → update DB[7]=5, FB[7]=blue

Final state:
  FB = [bg, red, red, blue, blue, blue, blue, blue, red, bg]
  DB = [∞,  10,  10,  5,    5,    5,    5,    5,   10,  ∞]
```

Triangle B correctly appears in front of Triangle A for pixels 3–7.

---

## 3. Applications & Use Cases

1. **GPU Hardware Z-Buffer**: All modern GPUs (NVIDIA, AMD, Intel, Apple) implement the Z-Buffer in dedicated silicon with **Early-Z culling** (discarding fragments before expensive pixel shader execution) and **Hi-Z** (hierarchical depth buffer for fast tile-based culling). OpenGL's `glDepthTest()` and DirectX's depth-stencil state directly control this hardware unit.

2. **Painter's Algorithm in CSS/SVG Compositing**: Web browsers use the Painter's Algorithm concept when compositing DOM elements by `z-index` order — elements with higher `z-index` are painted on top of elements with lower `z-index`, which is correct only for non-intersecting 2D layers.

3. **CAD Hidden-Line Removal**: Engineering CAD tools use scan-line visible surface detection to generate clean hidden-line removed (HLR) technical drawings from 3D solid models, as required for manufacturing blueprints.

4. **3D Game Rendering Transparency**: The A-Buffer approach is used in game engines (Unreal Engine OIT, Unity HDRP) to correctly render particles, glass, water, and foliage that require order-correct alpha blending.

5. **Medical Volume Visualization**: Z-buffer-based ray casting through CT/MRI volumes finds the closest surface voxel along each viewing ray, enabling interactive real-time 3D medical imaging.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Z-Buffer Depth Calculation [KTU Dec 2020, Dec 2019 — 9 Marks]

**Problem**: A polygon has plane equation $3x + 2y + 6z - 24 = 0$. 
(a) Find the depth value $z$ at pixel $(1, 1)$.
(b) Derive the incremental formula for computing $z$ at subsequent pixels along the scanline.
(c) Compute depths at pixels $(2,1)$ and $(3,1)$.

**Solution**:

**(a) Depth at $(1, 1)$:**

$A=3, B=2, C=6, D=-24$. Solve $3(1) + 2(1) + 6z = 24$:
$$6z = 24 - 3 - 2 = 19 \implies z(1,1) = \frac{19}{6} \approx 3.167$$

**(b) Incremental formula:**

$$z(x, y) = \frac{-Ax - By - D}{C} = \frac{-3x - 2y + 24}{6}$$

For next pixel $(x+1, y)$:
$$z(x+1, y) = \frac{-3(x+1) - 2y + 24}{6} = z(x,y) - \frac{3}{6} = z(x,y) - 0.5$$

$$\boxed{\Delta z = -\frac{A}{C} = -\frac{3}{6} = -0.5}$$

**(c) Subsequent depths:**

$z(2,1) = 3.167 - 0.5 = 2.667$

$z(3,1) = 2.667 - 0.5 = 2.167$

**Significance**: The incremental update requires only 1 subtraction per pixel — no multiplication or division — making Z-Buffer extremely fast in hardware.

---

### Example 2: Back-Face Detection [KTU June 2024 — 4 Marks]

**Problem**: A polygon has vertices listed in order: $P_1(2,0,4)$, $P_2(6,0,4)$, $P_3(6,4,4)$. The viewer is at the origin looking along $+z$. Is this polygon a front-face or back-face?

**Solution**:

**Compute surface normal** $\vec{N} = \vec{e_1} \times \vec{e_2}$:

$\vec{e_1} = P_2 - P_1 = (4, 0, 0)$

$\vec{e_2} = P_3 - P_1 = (4, 4, 0)$

$$\vec{N} = \vec{e_1} \times \vec{e_2} = \begin{vmatrix}\hat{i} & \hat{j} & \hat{k} \\ 4 & 0 & 0 \\ 4 & 4 & 0\end{vmatrix}$$
$$= \hat{i}(0 \cdot 0 - 0 \cdot 4) - \hat{j}(4 \cdot 0 - 0 \cdot 4) + \hat{k}(4 \cdot 4 - 0 \cdot 4) = (0, 0, 16)$$

So $C = 16 > 0$.

**Viewing along $+z$**: Viewing vector $\vec{V} = (0, 0, 1)$.
$$\vec{N} \cdot \vec{V} = 0 + 0 + 16 \times 1 = 16 > 0$$

**Result**: Since $\vec{N} \cdot \vec{V} > 0$, the polygon is a **FRONT-FACE** — it faces toward the viewer and should be rendered.

---

### Example 3: Painter's Algorithm — Overlap Tests [KTU Jan 2023, Dec 2023 — 8 Marks]

**Problem**: Explain the depth-sorting (Painter's) algorithm for visible surface detection. What are the 5 tests to identify overlapping surfaces?

**Solution**:

**Depth-Sorting Algorithm — Step-by-Step:**

**Step 1**: Compute $z_{\max}$ (farthest $z$ coordinate) for each polygon in the scene. Sort polygons in **descending order of $z_{\max}$** (farthest first).

**Step 2**: Starting from the farthest polygon in the sorted list, check if the current polygon $P$ overlaps in depth with the next polygon $Q$ (i.e., do their $z$-extents intersect?).

**Step 3**: If $z_{\min}(P) < z_{\max}(Q)$ (depth ranges overlap), apply the **5 disambiguation tests** in order. If any test **passes** (i.e., proves no actual visibility conflict), skip the remaining tests and continue with current order:

| Test No. | Test | Condition for PASS |
|---|---|---|
| **1** | Do x-extents of P and Q NOT overlap? | $x_{\max}(P) < x_{\min}(Q)$ or $x_{\max}(Q) < x_{\min}(P)$ |
| **2** | Do y-extents of P and Q NOT overlap? | $y_{\max}(P) < y_{\min}(Q)$ or $y_{\max}(Q) < y_{\min}(P)$ |
| **3** | Are all vertices of P completely behind Q's plane? | $Ax + By + Cz + D < 0$ for all vertices of P (using Q's plane equation) |
| **4** | Are all vertices of Q completely in front of P's plane? | $Ax + By + Cz + D > 0$ for all vertices of Q (using P's plane equation) |
| **5** | Do 2D projected outlines of P and Q NOT overlap on screen? | No pixel covered by both P and Q |

**Step 4**: If all 5 tests **fail** (genuine cyclic overlap — e.g., P is in front of Q from one angle, but Q is in front of P from another), **split** polygon P along the plane of Q. Re-insert both halves back into the polygon list and re-sort.

**Step 5**: Render polygons from the sorted list (back-to-front) using the frame buffer. Each polygon overwrites previous polygons at covered pixels.

**Example of cyclic overlap**: Three triangles A, B, C arranged so that vertex of A is in front of B, vertex of B is in front of C, vertex of C is in front of A — no linear order satisfies all three constraints. Must split at least one triangle.

**Complexity**: 
- Sorting: $O(n \log n)$
- Overlap tests: $O(n^2)$ worst case
- Appropriate for small $n$ (< 1000 polygons); Z-Buffer is better for large scenes.

---

## 5. Previous Year Questions & Solutions

### Q1 [KTU Dec 2023 — 8 Marks]
**Question**: Explain Depth Sorting method. Compare object space and image space methods of visible surface detection.

**Solution**:

**Depth Sorting (Painter's Algorithm) — Detailed Explanation:**

The depth-sorting method is an **object-space** algorithm for visible surface detection that renders polygons from farthest to nearest, allowing closer polygons to overwrite farther ones in the frame buffer — simulating how a painter covers the canvas.

**Algorithm Steps:**
1. Compute the maximum $z$-extent ($z_{\max}$) for each polygon in world coordinates.
2. Sort polygons into a priority list $L$ in descending order of $z_{\max}$ (most distant first).
3. Starting from polygon $P$ at the front of $L$ and comparing with $Q$ (next in list):
   - If $z$-extents of $P$ and $Q$ do NOT overlap: proceed, draw $Q$ then $P$.
   - If $z$-extents overlap: apply 5 tests (see Example 3 above). If all 5 fail: split $P$ along $Q$'s plane, return both halves to $L$, re-sort.
4. Draw all polygons in sorted order: farthest first. The frame buffer accumulates the final image with correct visibility.

**Comparison — Object Space vs. Image Space:**

| Feature | Object Space (e.g., Depth Sort) | Image Space (e.g., Z-Buffer) |
|---|---|---|
| **Computation domain** | Continuous 3D geometry | Discrete 2D pixel grid |
| **Resolution** | Resolution-independent | Resolution-dependent |
| **Complexity** | $O(n^2)$ pairwise tests | $O(n \cdot W \cdot H)$ |
| **Transparency** | Cannot handle easily | A-Buffer extension handles transparency |
| **Cyclic overlaps** | Must split polygons | Handled naturally (pixel-by-pixel) |
| **Hardware acceleration** | No GPU hardware support | Full hardware support (Z-Buffer in silicon) |
| **Scene size** | Good for small $n$ | Good for any $n$, large scenes |
| **Output** | Sorted polygon list | Pixel frame buffer |

---

### Q2 [KTU Dec 2023, Dec 2020, May 2019 — 6 Marks]
**Question**: Describe Z-buffer algorithm. Derive the equation to find the depth values for a surface position (x, y).

**Solution**:

**Z-Buffer Algorithm:**

**Initialize**: For every pixel $(x, y)$ in screen space:
- `DepthBuffer[x][y] = ∞` (or maximum representable depth)
- `FrameBuffer[x][y] = background_color`

**Process each polygon** $P$ in the scene:
- Scan-convert polygon $P$ to find all covered pixels $(x, y)$.
- For each covered pixel, compute depth $z(x, y)$ of polygon $P$ at that pixel.
- **Comparison**: If $z(x, y) < \text{DepthBuffer}[x][y]$:
  - `DepthBuffer[x][y] = z(x, y)`
  - `FrameBuffer[x][y] = shade(P, x, y)`

**Derivation of depth value at surface position $(x, y)$:**

A polygon facet lies on a plane:
$$Ax + By + Cz + D = 0$$

Solving for the depth coordinate $z$:
$$Cz = -Ax - By - D$$
$$z(x, y) = \frac{-Ax - By - D}{C}$$

For the **adjacent pixel** $(x+1, y)$ on the same scanline (y unchanged):
$$z(x+1, y) = \frac{-A(x+1) - By - D}{C} = \frac{-Ax - By - D}{C} - \frac{A}{C}$$

$$\boxed{z_{\text{next}} = z_{\text{current}} - \frac{A}{C}}$$

The term $\Delta z = -A/C$ is **constant** for a given polygon along a given scanline. This means depth can be computed incrementally with just one subtraction per pixel — no division per pixel.

**Advantages**: Simple to implement; handles any scene complexity; trivially parallelizable.

**Disadvantages**: Requires memory proportional to screen resolution for depth buffer; cannot handle transparency; may exhibit depth precision issues (Z-fighting) when two surfaces are very close in depth.

---

### Q3 [KTU Dec 2018 / Dec 2019 — 4 Marks]
**Question**: List out the differences between Z-buffer method and A-buffer method for determining visible surfaces.

**Solution**:

| Feature | Z-Buffer | A-Buffer |
|---|---|---|
| **Storage per pixel** | Single depth float + color | Linked list of fragment records (depth, color, alpha, coverage mask) |
| **Transparency handling** | Cannot — opaque surfaces only | Yes — composites transparent fragments via alpha blending |
| **Antialiasing** | No sub-pixel information | Yes — 4×4 coverage bitmask per fragment enables antialiasing |
| **Memory usage** | Fixed: 1 depth value per pixel | Variable: unlimited fragments per pixel |
| **Algorithm complexity** | $O(1)$ per fragment | $O(k)$ per pixel where $k$ = number of overlapping fragments |
| **Hardware support** | Full GPU hardware acceleration | Software (CPU) or specialized GPU compute |
| **Applications** | General opaque 3D rendering | Film production rendering (Pixar), glass/water effects |
| **Fragment blending** | Last fragment wins (overwrite) | Sorts all fragments by depth, composites with $C = \alpha C_{front} + (1-\alpha) C_{back}$ |

---

### Q4 [KTU June 2024, Dec 2020 — 4 Marks]
**Question**: Describe the various classifications of visible-surface detection algorithms.

**Solution**:

Visible surface detection algorithms are classified into two major categories based on their operating space:

**1. Object-Space Methods** (operate in continuous 3D coordinate space):
- Compare and sort geometric primitives (polygons, edges) against each other in full 3D coordinate precision.
- Results are resolution-independent.

**Examples**:
- **Back-Face Culling**: Tests polygon normal vs. view vector; culls rear-facing polygons. $O(n)$ per frame.
- **Depth-Sorting (Painter's Algorithm)**: Sorts polygons by z-depth; renders back-to-front. $O(n \log n)$ + $O(n^2)$ disambiguation.
- **BSP-Tree Algorithm**: Builds a binary space partition tree once; traverses front-to-back for each viewpoint. $O(n \log n)$ construction, $O(n)$ traversal.
- **Roberts Algorithm**: Exact algorithm using plane geometry to find all hidden edges in a wireframe scene.

**2. Image-Space Methods** (operate in discrete 2D raster pixel space):
- Compare polygon depths at each pixel position on the raster.
- Results depend on screen resolution; must recompute if resolution changes.

**Examples**:
- **Z-Buffer Algorithm**: Maintains a depth array; compares depth per pixel during rasterization. $O(n \cdot p)$.
- **A-Buffer Algorithm**: Linked list of fragments per pixel; handles transparency and antialiasing. $O(n \cdot p)$ + compositing.
- **Scan-Line Visible Surface Detection**: Extends 2D scanline fill with depth comparison across active polygon spans. $O(n \cdot W)$.
- **Warnock Algorithm (Area Subdivision)**: Recursively subdivides the viewport until simple visibility decisions can be made. Efficient for sparse scenes.

**Practical use**: Modern systems combine both — Back-Face Culling (object-space, eliminates ~50% of polygons) feeds into Z-Buffer (image-space, handles full visibility at pixel resolution).

---

### Q5 [KTU Dec 2023 — 4 Marks]
**Question**: Describe A-buffer algorithm for detecting visible surfaces.

**Solution**:

The **A-Buffer (Accumulation Buffer)** algorithm is an extension of the Z-Buffer that handles **transparency** and **antialiasing** — two capabilities absent from the basic Z-Buffer.

**Data Structure**: Each pixel $(x, y)$ contains not just one depth value, but a **linked list of fragment records**:

```
struct AFragment {
    float r, g, b;      // Surface color at this fragment
    float depth;        // z-value of this fragment
    float alpha;        // Opacity: 0.0 (transparent) to 1.0 (opaque)
    int coverage[4][4]; // 4×4 sub-pixel coverage bitmask (16 bits)
    AFragment* next;    // Pointer to next fragment in linked list
};
```

**Algorithm Steps**:

**Step 1 — Fragment Accumulation**: For each polygon fragment at pixel $(x, y)$:
- If fragment is **fully opaque** AND **fully covers the pixel**: Replace existing closest fragment (like standard Z-Buffer).
- If fragment is **translucent** or **partially covers the pixel** (at edges): Append a new record to the pixel's linked list.

**Step 2 — Compositing**: After all polygons are processed, for each pixel with a non-trivial linked list:
1. Sort fragment records by depth (back-to-front).
2. Blend fragments using **Porter-Duff alpha compositing**:
   $$C_{\text{result}} = \alpha_{\text{front}} \cdot C_{\text{front}} + (1 - \alpha_{\text{front}}) \cdot C_{\text{back}}$$
3. Apply this recursively through the entire linked list from back to front.

**Information stored in each linked list node**: Object/surface identifier, RGB color, opacity (alpha), depth value, 4×4 sub-pixel coverage bitmask, pointer to next node.

**Advantage over Z-Buffer**: Correctly renders glass, water, smoke, trees with alpha channels, and antialiased polygon edges — all of which require multiple overlapping fragments per pixel.
