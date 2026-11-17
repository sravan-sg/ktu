# Visible Surface Detection Algorithms (Hidden Surface Elimination)

## 1. Explanation
In 3D computer graphics, a realistic image must display only the surface facets that are directly visible to the observer, completely removing (culling) all occluded surfaces, hidden lines, and rear faces. This process is termed **Visible Surface Detection** or **Hidden Surface Elimination (HSE)**.

---

### Classification: Object-Space vs. Image-Space Methods
Visible surface algorithms are broadly partitioned into two distinct algorithmic paradigms:

| Criterion | Object-Space Methods | Image-Space Methods |
|---|---|---|
| **Operating Domain** | Continuous 3D object coordinate space (physical geometric units). | Discrete 2D raster screen space (pixel matrix). |
| **Computational Complexity** | Scales as $O(n^2)$ or $O(n \log n)$, where $n$ is total polygon/edge count in the scene. | Scales as $O(n \times p)$, where $n$ is polygon count and $p$ is total screen pixel count ($W \times H$). |
| **Resolution Dependence** | Resolution-independent; calculated purely on geometric boundaries. | Resolution-dependent; repeated if display resolution increases. |
| **Precision** | Exact floating-point boundary calculation. | Subject to pixel discretization/rasterization artifacts. |
| **Representative Algorithms** | Back-Face Removal, Roberts algorithm, BSP-tree sorting. | Depth-Buffer (Z-Buffer), A-Buffer, Scan-Line, Warnock. |

---

### 1. Back-Face Removal (Back-Face Culling)
Back-face removal is a fast object-space method that eliminates all polygon faces that point away from the viewer. For closed polyhedra, approximately **$50\%$** of all polygon faces are back-facing and can be discarded before rasterization.

#### Mathematical Formulation:
Let a planar polygon have outward-pointing unit normal vector $\vec{N} = \begin{bmatrix} A & B & C \end{bmatrix}^T$ from plane equation $Ax + By + Cz + D = 0$.
Let $\vec{V}_{\text{view}}$ be the viewing vector pointing from the polygon surface toward the eye/camera:
- A polygon is a **front-face** (visible) if:
  $$\vec{N} \cdot \vec{V}_{\text{view}} > 0$$
- A polygon is a **back-face** (culled) if:
  $$\vec{N} \cdot \vec{V}_{\text{view}} \le 0$$

#### Viewing Along the $-Z$ Axis (Standard Right-Handed Viewing):
If the observer views the scene looking along the $-Z$ axis, the viewing vector is $\vec{V}_{\text{view}} = \begin{bmatrix} 0 & 0 & -1 \end{bmatrix}^T$.
Then:
$$\vec{N} \cdot \vec{V}_{\text{view}} = A(0) + B(0) + C(-1) = -C$$
- Front-face condition: $-C > 0 \implies \mathbf{C < 0}$.
- Back-face condition: $-C \le 0 \implies \mathbf{C \ge 0}$.

*(Note: In left-handed viewing coordinate systems where viewing is along $+Z$, the back-face condition is $C \le 0$).*

---

### 2. Depth-Buffer (Z-Buffer) Algorithm
The Z-Buffer algorithm is an image-space visible surface detection method universally accelerated in modern GPU hardware (DirectX, Vulkan, OpenGL).

#### Memory Buffers:
1. **Frame Buffer $C(x, y)$**: Stores the RGB color intensity of each pixel on screen.
2. **Depth Buffer (Z-Buffer) $D(x, y)$**: Stores the closest depth ($z$-value) currently observed at each pixel $(x, y)$.

#### Algorithm Pseudocode:
```c
void ZBufferAlgorithm() {
    // 1. Initialization
    for (int x = 0; x < ScreenWidth; x++) {
        for (int y = 0; y < ScreenHeight; y++) {
            DepthBuffer[x][y] = 1.0; // Max depth (or -infinity depending on coordinate convention)
            FrameBuffer[x][y] = BackgroundColor;
        }
    }
    
    // 2. Scan conversion of polygons
    for (each polygon P in scene) {
        for (each pixel (x, y) covered by polygon P) {
            float z = CalculateDepth(P, x, y);
            
            // If current polygon fragment is closer than previous closest fragment
            if (z < DepthBuffer[x][y]) {
                DepthBuffer[x][y] = z;               // Update depth buffer
                FrameBuffer[x][y] = CalculateShading(P, x, y); // Update frame buffer color
            }
        }
    }
}
```

#### Incremental Depth Calculation along a Scanline:
The equation of a polygon plane is $Ax + By + Cz + D = 0$.
Solving for depth $z$:
$$z = \frac{-Ax - By - D}{C}$$

At the adjacent pixel along the same scanline $(x + 1, y)$:
$$z' = \frac{-A(x + 1) - By - D}{C} = z - \frac{A}{C}$$
Thus, depth is updated across a scanline using a single fast **subtraction**:
$$\mathbf{z_{x+1} = z_x - \frac{A}{C}}$$

---

### 3. A-Buffer (Accumulative / Anti-aliased Buffer) Algorithm
The A-Buffer is an extension of the Z-Buffer designed by Loren Carpenter to handle **transparency, translucency, and antialiasing**.
In a standard Z-Buffer, each pixel stores only a single opaque color and depth. The A-Buffer replaces the single depth float with a **linked list of surface fragment records**:
- If a fragment is opaque and covers $100\%$ of the pixel: Operates identically to Z-Buffer.
- If a fragment is translucent (transparent) or only partially covers the pixel (edge fragment): It is appended to a linked list at that pixel.
- **Fragment Record Structure**:
  $$\text{Fragment} = \{ \text{RGB Color}, \ \text{Depth } z, \ \text{Alpha / Transparency}, \ \text{Area Coverage Mask (4x4 bitmask)}, \ \text{Next Pointer} \}$$
At the end of the frame, all fragments in the linked list are depth-sorted from back-to-front and blended together.

---

### 4. Depth-Sorting Method (Painter's Algorithm)
The Painter's Algorithm operates in a manner analogous to an oil painter: background objects are painted first, and foreground objects are painted over them, naturally obscuring occluded surfaces.

#### Step-by-Step Procedure:
1. Sort all polygons in descending order of their maximum depth $z_{\max}$ (farthest polygons first).
2. For each polygon $P$, test whether its depth range overlaps with any other polygon $Q$.
3. If $z$-extents overlap ($z_{\min}(P) < z_{\max}(Q)$), apply the **Five Disambiguation Tests**:
   - **Test 1 ($X$-overlap)**: Do bounding boxes overlap in $X$? ($\Delta x$)
   - **Test 2 ($Y$-overlap)**: Do bounding boxes overlap in $Y$? ($\Delta y$)
   - **Test 3 (Plane separation)**: Are all vertices of $Q$ completely on the far side of $P$'s plane?
   - **Test 4 (Plane separation)**: Are all vertices of $P$ completely on the near side of $Q$'s plane?
   - **Test 5 (Screen overlap)**: Do 2D projections of $P$ and $Q$ overlap on the screen?
4. If all tests fail, cyclic overlap (e.g. three overlapping triangles forming an impossible priority loop) occurs; split one polygon into two along the plane of the other and re-sort.
5. Render polygons into the frame buffer in strictly sorted order.

---

### 5. Scan-Line Visible Surface Detection
Combines the 2D scan-line polygon fill algorithm with 3D depth testing:
- Maintains an **Edge Table (ET)** and **Active Edge Table (AET)** for all polygons simultaneously.
- Also maintains an **Active Polygon Table (APT)** listing polygons currently intersected by the scanline.
- As the scanline increments across pixels, active polygon depths are compared, and only the span of the closest polygon is written to the frame buffer.
- Eliminates the need for a full 2D depth buffer, requiring only a 1D scanline buffer.

---

## 2. Example: Z-Buffer vs. Painter's Algorithm Depth Comparison
```
Scanline y
    │              Polygon A (z = 4)
    │           +=======================+
    │           |                       |
    │           |     Polygon B (z = 2) |
    │           |    +=============+    |
    │           |    |  (CLOSER)   |    |
    │           |    +=============+    |
    │           +=======================+
    └───────────────────────────────────────► x

Depth Buffer Values D(x):
  [ 4.0 | 4.0 | 2.0 | 2.0 | 2.0 | 4.0 | 4.0 ]
Frame Buffer Output:
  [ Col A | Col A | Col B | Col B | Col B | Col A | Col A ]
```

---

## 3. Applications & Use Cases
1. **GPU Hardware Rasterization Pipeline**: All modern 3D graphics cards (GeForce, Radeon, Apple Silicon) contain dedicated hardware Z-culling units (Early-Z, Hi-Z) that discard occluded pixels before executing expensive fragment/pixel shaders.
2. **CAD Solid Modeling & Architectural Walkthroughs**: Scanline visible surface algorithms and BSP-trees render interior architectural models with millions of structural elements.
3. **Medical Volume Slicing**: Orthogonal depth buffers slice through volumetric MRI datasets to reveal internal anatomical boundaries.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Back-Face Culling Vector Test [KTU May 2019 / Jan 2023 - 4 Marks]
**Problem**:
A polygon has vertices $V_1(1, 1, 1), V_2(3, 1, 1)$, and $V_3(1, 4, 1)$ in a right-handed viewing coordinate system with the eye positioned at $(0, 0, 10)$ looking along the $-Z$ axis.
Determine whether this polygon is a front-face or a back-face.

**Step-by-step Solution**:
1. **Calculate Edge Vectors**:
   $$\vec{e}_1 = V_2 - V_1 = (3 - 1, 1 - 1, 1 - 1) = (2, 0, 0)$$
   $$\vec{e}_2 = V_3 - V_1 = (1 - 1, 4 - 1, 1 - 1) = (0, 3, 0)$$
2. **Calculate Surface Normal Vector $\vec{N}$**:
   $$\vec{N} = \vec{e}_1 \times \vec{e}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 0 & 0 \\ 0 & 3 & 0 \end{vmatrix} = (0)\hat{i} - (0)\hat{j} + (2 \times 3 - 0)\hat{k} = \begin{bmatrix} 0 \\ 0 \\ 6 \end{bmatrix}$$
   The plane normal coefficients are $A = 0, B = 0, C = 6$.
3. **Evaluate Back-Face Condition**:
   - The viewing vector along $-Z$ is $\vec{V}_{\text{view}} = \begin{bmatrix} 0 & 0 & -1 \end{bmatrix}^T$.
   $$\vec{N} \cdot \vec{V}_{\text{view}} = 6 \times (-1) = -6 \le 0$$
   - Since $\vec{N} \cdot \vec{V}_{\text{view}} \le 0$ (or equivalently $C = 6 \ge 0$), the surface normal points directly **away** from the camera.
4. **Conclusion**:
   The polygon is a **BACK-FACE** and will be **culled (removed)** from the rendering pipeline.

---

### Example 2: Incremental Z-Buffer Depth Calculation [KTU Dec 2020 Pattern]
**Problem**:
A polygon has plane equation $2x + 3y + 4z - 24 = 0$.
1. If the depth at pixel $(10, 5)$ is known to be $z = -3.75$, calculate the incremental change $\Delta z$ along the scanline ($+X$ direction).
2. Determine the depth at the next two consecutive pixels $(11, 5)$ and $(12, 5)$.

**Step-by-step Solution**:
1. **Plane Coefficients**:
   $$A = 2, \quad B = 3, \quad C = 4, \quad D = -24$$
2. **Incremental Recurrence Relation**:
   $$\Delta z = -\frac{A}{C} = -\frac{2}{4} = -0.5$$
3. **Consecutive Pixel Depths**:
   - At $(10, 5)$:
     $$z(10, 5) = \frac{-2(10) - 3(5) + 24}{4} = \frac{-20 - 15 + 24}{4} = \frac{-11}{4} = -2.75$$
   - At $(11, 5)$:
     $$z(11, 5) = z(10, 5) + \Delta z = -2.75 - 0.5 = \mathbf{-3.25}$$
   - At $(12, 5)$:
     $$z(12, 5) = z(11, 5) + \Delta z = -3.25 - 0.5 = \mathbf{-3.75}$$
   Notice that the calculation requires only a single addition per pixel without re-evaluating the plane equation.

---

### Example 3: Painter's Algorithm Depth Overlap Ambiguity [KTU Analytical Pattern]
**Problem**:
Two polygons $P$ and $Q$ have the following depth ranges in viewing coordinates:
$$P: z \in [10, 25], \quad Q: z \in [20, 35]$$
Explain why sorting by $z_{\max}$ alone is insufficient to determine drawing priority, and state the first two tests applied to resolve the ambiguity.

**Step-by-step Solution**:
1. Maximum depths: $z_{\max}(P) = 25$, $z_{\max}(Q) = 35$.
   - Since $z_{\max}(Q) > z_{\max}(P)$, $Q$ appears to be further back than $P$.
   - However, the depth ranges overlap between $z = 20$ and $z = 25$ ($z_{\min}(P) \le z_{\max}(Q)$ and $z_{\min}(Q) \le z_{\max}(P)$).
   - If $Q$ extends in front of $P$ at certain screen coordinates, painting $Q$ first might erroneously overdraw parts of $P$ or vice versa.
2. **Disambiguation Tests**:
   - **Test 1 ($X$-Extent Test)**: Check if the bounding boxes of $P$ and $Q$ overlap along $X$:
     $$[x_{\min}(P), x_{\max}(P)] \cap [x_{\min}(Q), x_{\max}(Q)] == \emptyset$$
     If there is no $X$ overlap, the polygons project to completely separate screen columns. Drawing order does not matter; paint $Q$ then $P$.
   - **Test 2 ($Y$-Extent Test)**: Check if the bounding boxes overlap along $Y$:
     $$[y_{\min}(P), y_{\max}(P)] \cap [y_{\min}(Q), y_{\max}(Q)] == \emptyset$$
     If there is no $Y$ overlap, the polygons project to completely separate scanlines. Drawing order does not matter; paint $Q$ then $P$.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / January 2023 - 6 Marks]
**Question**:
Explain the Depth-Buffer (Z-Buffer) algorithm for visible surface detection. Derive the recurrence relation used for incremental depth calculation along a scanline.

**Solution**:
1. **Z-Buffer Algorithm Overview**:
   The Z-Buffer algorithm is an image-space approach that compares surface depths at every pixel position across the projection plane. It maintains two 2D arrays matching the screen dimensions:
   - `FrameBuffer(x, y)`: Stores color intensity for pixel $(x, y)$.
   - `DepthBuffer(x, y)`: Stores the closest depth $z$ recorded so far at pixel $(x, y)$.
2. **Step-by-step Algorithm**:
   - Initialize `DepthBuffer[x][y] = 1.0` (or maximum depth) and `FrameBuffer[x][y] = BackgroundColor` for all pixels.
   - For each polygon in the scene, scan convert the polygon to determine each pixel $(x, y)$ covered by the polygon.
   - Calculate depth $z(x, y)$ of the polygon at that pixel.
   - If $z(x, y) < \text{DepthBuffer}[x][y]$:
     - $\text{DepthBuffer}[x][y] = z(x, y)$
     - $\text{FrameBuffer}[x][y] = \text{PolygonColor}(x, y)$
3. **Derivation of Incremental Depth Recurrence**:
   Every polygon facet lies on a plane:
   $$Ax + By + Cz + D = 0$$
   Solving for depth $z$:
   $$z = -\frac{Ax + By + D}{C}$$
   For the adjacent pixel along the same scanline, $x$ increases by $1$ ($x' = x + 1$) while $y$ remains constant:
   $$z' = -\frac{A(x + 1) + By + D}{C} = -\frac{Ax + By + D}{C} - \frac{A}{C} = z - \frac{A}{C}$$
   Therefore:
   $$\mathbf{z_{\text{next}} = z_{\text{current}} - \frac{A}{C}}$$
   This allows the hardware to calculate the depth of the next pixel along a scanline with a single scalar subtraction, avoiding expensive division operations.

---

### Question 2 [KTU December 2021 / June 2024 - 4 Marks]
**Question**:
Explain the Back-Face Removal method for hidden surface elimination. Why can back-face removal alone not solve the visible surface detection problem for a complete scene?

**Solution**:
1. **Back-Face Removal Principle**:
   For any closed polyhedral object, polygon faces whose surface normal vectors point away from the camera are hidden behind the object itself.
   - Let a polygon have plane equation $Ax + By + Cz + D = 0$ with outward normal $\vec{N} = (A, B, C)$.
   - When viewed along the $-Z$ axis in a right-handed coordinate system, the viewing vector is $\vec{V} = (0, 0, -1)$.
   - The dot product test is:
     $$\vec{N} \cdot \vec{V} = -C$$
   - If $C \ge 0$, the normal points away from the observer; the polygon is a **back-face** and is culled immediately.
2. **Why Back-Face Removal Alone is Insufficient**:
   - **Inter-Object Occlusion**: Back-face removal only removes the rear faces of an *individual* object. It cannot determine if a completely front-facing polygon on Object A is occluded by another front-facing polygon on Object B positioned in front of it.
   - **Concave Objects (Self-Occlusion)**: For concave polyhedra, a front-facing surface can be partially or completely occluded by another front-facing protrusion belonging to the exact same object.
   - Consequently, back-face culling is used only as an initial preprocessing filter (eliminating $\approx 50\%$ of primitives), which must then be followed by a comprehensive visible surface algorithm like Z-Buffer.

