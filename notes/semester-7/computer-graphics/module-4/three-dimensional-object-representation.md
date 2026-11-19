# Three-Dimensional Object Representation: Polygon Surfaces, Plane Equations & Solid Representations

## 1. Explanation

In three-dimensional computer graphics, physical real-world objects and virtual synthetic geometries must be represented within computer memory using data structures that strike an optimal balance between **geometric fidelity**, **memory consumption**, and **rendering pipeline throughput**.

---

### Classification of 3D Object Representations

All 3D geometric modeling paradigms fall into two overarching mathematical categories:

```
                      3D OBJECT REPRESENTATIONS
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
BOUNDARY REPRESENTATIONS (B-reps)            SPACE-PARTITIONING REPRESENTATIONS
(Describes 2D boundary surface enclosing     (Describes solid interior volume
 the 3D solid object)                         occupied by the object)
 • Polygon Surface Meshes                    • Constructive Solid Geometry (CSG)
 • Parametric Bicubic Splines                • Binary Space Partitioning (BSP) Trees
 • Non-Uniform Rational B-Splines (NURBS)    • Octree Hierarchical Volumes
 • Subdivision Surfaces                      • Voxel Grids / Signed Distance Fields (SDF)
```

1. **Boundary Representations (B-reps)**:
   - Represent a 3D solid by explicitly modeling the **2D manifold boundary surface** that separates the interior of the object from the exterior universe.
   - The universal standard for real-time GPU rendering because modern graphics hardware is an optimized, massively parallel triangle-rasterization machine.
2. **Space-Partitioning Representations**:
   - Describe a solid object by subdividing the continuous 3D volume into collections of non-overlapping volumetric spatial cells.
   - Ideal for physical simulation, engineering mass-property analysis (center of mass, moments of inertia), collision detection, and Boolean machining operations.

---

### Polygon Surfaces & The Geometric Table Architecture

A **polygon surface** (or polyhedral mesh) decomposes an arbitrary 3D continuous surface into a collection of planar polygon facets (typically triangles or quadrilaterals).

#### The Standard Three-Table Relational Architecture
Storing coordinates redundantly at every polygon facet would consume excessive memory and make topological modifications (e.g., deforming a vertex) computationally intractable. Graphics systems organize polygon meshes into three relational tables:

```
VERTEX TABLE                    EDGE TABLE                     POLYGON (FACE) TABLE
┌────┬──────────────┐         ┌────┬─────────────┐            ┌────┬────────────────┐
│ V1 │ (x1, y1, z1) │ ◄──┐    │ E1 │ V1, V2      │ ◄──────────│ F1 │ E1, E2, E3     │
├────┼──────────────┤    │    ├────┼─────────────┤            ├────┼────────────────┤
│ V2 │ (x2, y2, z2) │ ◄──┼────│ E2 │ V2, V3      │            │ F2 │ E2, E4, E5     │
├────┼──────────────┤    │    ├────┼─────────────┤            └────┴────────────────┘
│ V3 │ (x3, y3, z3) │ ◄──┘    │ E3 │ V3, V1      │
└────┴──────────────┘         └────┴─────────────┘
```

1. **Vertex Table**:
   - Stores the 3D Cartesian coordinates $(x, y, z)$ of each distinct vertex point in the mesh.
   - Each vertex is assigned an integer index ($V_1, V_2, \dots, V_n$).
2. **Edge Table**:
   - Stores pairs of vertex indices defining each unique straight line segment.
   - May also store pointers to the two adjoining face facets that share the edge for rapid topological connectivity queries.
3. **Polygon Table (Face Table)**:
   - Stores the sequence of directed edges (or vertex indices) that bound each planar polygon face facet.
   - Vertices/edges are stored in **counterclockwise (CCW) order** when viewed from the outside of the solid.

#### Architectural Benefits of the Three-Table Structure:
- **Zero Coordinate Duplication**: Spatial coordinates are stored exactly once. In a closed manifold triangular mesh, each vertex is shared by an average of $6$ triangles; storing coordinates once reduces vertex memory footprint by $\approx 6 \times$.
- **Fast Vertex Mutation**: Modifying the spatial location of a vertex requires updating only a single entry in the Vertex Table; all incident edges and polygon facets update automatically.
- **Topological Adjacency**: Adjacent faces sharing an edge are identified instantly, essential for Gouraud and Phong vertex-normal averaging and silhouette edge detection.
- **Data Integrity Verification**: Enables automated detection of non-manifold edges (e.g., an edge shared by $3$ or more faces) or open boundary leaks.

---

### Polygon Plane Equations & Surface Normal Vectors

Every planar polygon facet in 3D space satisfies the algebraic plane equation:
$$Ax + By + Cz + D = 0$$
where $\vec{N} = \begin{bmatrix} A & B & C \end{bmatrix}^T$ is the surface normal vector perpendicular to the planar facet, and $|D|/\sqrt{A^2 + B^2 + C^2}$ represents the perpendicular distance from the coordinate origin to the plane.

#### Derivation of Plane Coefficients from Three Vertices
Given three non-collinear vertices $V_1(x_1, y_1, z_1), V_2(x_2, y_2, z_2), V_3(x_3, y_3, z_3)$ ordered in counterclockwise sequence when viewed from the front (exterior) of the polygon:

```
               V3 (x3, y3, z3)
                 ▲
                 │
                 │  V3 - V1
                 │
                 V1 (x1, y1, z1) ──────────► V2 (x2, y2, z2)
                                   V2 - V1
```

The outward-pointing surface normal vector $\vec{N}$ is given by the vector cross-product:
$$\vec{N} = (V_2 - V_1) \times (V_3 - V_1)$$

Evaluating the vector cross-product using determinants:
$$\vec{N} = \det \begin{bmatrix} \hat{i} & \hat{j} & \hat{k} \\ x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ x_3 - x_1 & y_3 - y_1 & z_3 - z_1 \end{bmatrix}$$

Expanding the sub-determinants yields plane coefficients $A, B, C$:
$$A = (y_2 - y_1)(z_3 - z_1) - (z_2 - z_1)(y_3 - y_1)$$
$$B = (z_2 - z_1)(x_3 - x_1) - (x_2 - x_1)(z_3 - z_1)$$
$$C = (x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1)$$

Because vertex $V_1$ lies directly on the plane, substituting $(x_1, y_1, z_1)$ solves for $D$:
$$A x_1 + B y_1 + C z_1 + D = 0 \implies D = -(A x_1 + B y_1 + C z_1)$$

#### Point-Plane Spatial Classification Test
For any arbitrary spatial point $P(x, y, z)$ in 3D space, evaluating the plane equation determines its position relative to the object's surface:
$$f(x, y, z) = Ax + By + Cz + D$$

| Value of $f(x, y, z)$ | Spatial Relationship | Physical Meaning |
|---|---|---|
| $f(x, y, z) > 0$ | Point lies in the **Positive Half-Space** | Point is **OUTSIDE** (in front of the surface). |
| $f(x, y, z) = 0$ | Point lies **ON THE PLANE** | Point is directly on the polygon surface boundary. |
| $f(x, y, z) < 0$ | Point lies in the **Negative Half-Space** | Point is **INSIDE** (behind the surface). |

*Application in Back-Face Culling*: If the observer's camera is at $(x_c, y_c, z_c)$ looking along view vector $\vec{V}_{\text{view}}$, evaluating the dot product $\vec{N} \cdot \vec{V}_{\text{view}}$ determines visibility. If $\vec{N} \cdot \vec{V}_{\text{view}} \ge 0$, the surface normal points away from the camera, identifying it as an occluded back-face.

---

### Space-Partitioning Representations

#### 1. Binary Space Partitioning (BSP) Tree
A **BSP Tree** is a hierarchical spatial data structure that recursively bisects 3D space into convex sub-spaces using the infinite planes of polygon surfaces.

```
                  [Root: Polygon A]
                  /               \
         Front Subspace       Back Subspace
        [Polygon B]           [Polygon C]
        /         \           /         \
      Front      Back       Front      Back
```

- **Construction Algorithm**:
  1. Select a polygon $A$ from the scene to act as the root partitioning plane.
  2. For every remaining polygon in the scene, evaluate its vertices against the plane equation of $A$:
     - If all vertices have $f(x,y,z) > 0$: Place in $A$'s **Front List**.
     - If all vertices have $f(x,y,z) < 0$: Place in $A$'s **Back List**.
     - If vertices span across the plane (some positive, some negative): Split the polygon into two sub-polygons along the intersection line; assign one piece to the Front List and the other to the Back List.
  3. Recursively subdivide the front and back lists until all polygons are leaf nodes.
- **Rendering via In-Order Traversal (Painter's Algorithm)**:
  For any dynamic camera location $P_{\text{eye}}$, a BSP tree enables rendering an entire 3D scene in **strict back-to-front depth order** without performing dynamic runtime sorting:
  - If $P_{\text{eye}}$ is in front of root polygon $A$:
    $\text{Traverse}(A.\text{back}) \to \text{Draw}(A) \to \text{Traverse}(A.\text{front})$.
  - If $P_{\text{eye}}$ is behind root polygon $A$:
    $\text{Traverse}(A.\text{front}) \to \text{Draw}(A) \to \text{Traverse}(A.\text{back})$.
  *Historical Impact*: The 1993 game *DOOM* achieved groundbreaking $60\text{ FPS}$ 3D rendering on 486 CPUs by using BSP trees for real-time visibility determination.

#### 2. Octree Representation
An **Octree** is a hierarchical tree data structure that models 3D solid volumes by recursively subdividing a bounding cube into **eight octants** (extending the 2D quadtree concept into three dimensions).

```
                            OCTREE DIVISION
                               ┌───────┬───────┐
                              /   2   /   3   /│
                             ┌───────┬───────┐ │
                            /   0   /   1   /│3│
                           ┌───────┬───────┐ │/│
                           │   0   │   1   │1│ 7
                           ├───────┼───────┤/│/
                           │   4   │   5   │5/
                           └───────┴───────┘
```

- **Node Types**:
  - **Empty (White)**: The octant lies completely outside the solid volume (no further subdivision needed).
  - **Full (Black)**: The octant lies completely inside the solid volume (no further subdivision needed).
  - **Partial (Gray)**: The octant partially intersects the object boundary $\implies$ recursively subdivided into $8$ child octants until maximum tree depth or voxel resolution is reached.
- **Applications**: LiDAR volumetric point cloud compression, fast collision detection in physics engines, and sparse voxel octree (SVO) ray marching.

#### 3. Constructive Solid Geometry (CSG)
**Constructive Solid Geometry (CSG)** represents complex 3D solid shapes as a binary tree of **Boolean set operations** applied to simple geometric primitives (cubes, spheres, cylinders, cones, tori).

```
                      [CSG ROOT: Difference (-)]
                                /    \
             [Primitive: Block]        [Primitive: Cylinder]
             
       Resulting Solid: A mechanical bracket with a drilled cylindrical hole
```

- **Boolean Operations**:
  1. **Union ($A \cup B$)**: Combines the volumes of solids $A$ and $B$ into a single merged solid.
  2. **Intersection ($A \cap B$)**: Retains only the volume shared simultaneously by both solids.
  3. **Difference ($A - B$)**: Subtracts the volume of solid $B$ from solid $A$ (e.g., cutting a slot, drilling a hole).
- **Applications**: CAD/CAM engineering modeling (SolidWorks, AutoCAD), CNC toolpath generation, and 3D printing preparation.

#### 4. Quadric Surfaces
Quadric surfaces are implicit surfaces defined by a general second-degree algebraic polynomial equation in three variables:
$$Ax^2 + By^2 + Cz^2 + Dxy + Exz + Fyz + Gx + Hy + Iz + J = 0$$

Standard Canonical Quadric Shapes:
- **Sphere** (centered at origin, radius $r$):
  $$x^2 + y^2 + z^2 = r^2$$
- **Ellipsoid** (semi-axes $r_x, r_y, r_z$):
  $$\frac{x^2}{r_x^2} + \frac{y^2}{r_y^2} + \frac{z^2}{r_z^2} = 1$$
- **Circular Cone** (along Z-axis):
  $$\frac{x^2}{r_x^2} + \frac{y^2}{r_y^2} = \frac{z^2}{r_z^2}$$
- **Elliptic Paraboloid**:
  $$\frac{x^2}{r_x^2} + \frac{y^2}{r_y^2} = \frac{z}{r_z}$$
- **Hyperboloid of One Sheet**:
  $$\frac{x^2}{r_x^2} + \frac{y^2}{r_y^2} - \frac{z^2}{r_z^2} = 1$$

---

## 2. Example: Concrete Polygon Table Formulation for a Tetrahedron

Consider a 3D triangular pyramid (tetrahedron) with four vertices:
$$V_1(0, 0, 0), \quad V_2(2, 0, 0), \quad V_3(1, 2, 0), \quad V_4(1, 1, 3)$$

```
                                V4 (1, 1, 3)
                                    ▲
                                   /│\
                                  / │ \
                                 /  │  \
                                /   │   \
                               /    │    \
                              /     │     \
                             /      │      \
              V1 (0, 0, 0)  └───────┼───────► V2 (2, 0, 0)
                                \   │   /
                                 \  │  /
                                  \ │ /
                                   ▼ /
                               V3 (1, 2, 0)
```

### 1. Vertex Table
| Vertex Index | Coordinates $(X, Y, Z)$ |
|---|---|
| **$V_1$** | $(0, 0, 0)$ |
| **$V_2$** | $(2, 0, 0)$ |
| **$V_3$** | $(1, 2, 0)$ |
| **$V_4$** | $(1, 1, 3)$ |

### 2. Edge Table
| Edge Index | Endpoint Vertices | Adjoining Faces |
|---|---|---|
| **$E_1$** | $(V_1, V_2)$ | $F_1 \text{ (Base)}, \ F_2 \text{ (Front)}$ |
| **$E_2$** | $(V_2, V_3)$ | $F_1 \text{ (Base)}, \ F_3 \text{ (Right)}$ |
| **$E_3$** | $(V_3, V_1)$ | $F_1 \text{ (Base)}, \ F_4 \text{ (Left)}$ |
| **$E_4$** | $(V_1, V_4)$ | $F_2 \text{ (Front)}, \ F_4 \text{ (Left)}$ |
| **$E_5$** | $(V_2, V_4)$ | $F_2 \text{ (Front)}, \ F_3 \text{ (Right)}$ |
| **$E_6$** | $(V_3, V_4)$ | $F_3 \text{ (Right)}, \ F_4 \text{ (Left)}$ |

### 3. Polygon / Face Table
| Face Index | Bounding Edges | Vertex Loop (CCW from Outside) |
|---|---|---|
| **$F_1$ (Base)** | $E_1, E_2, E_3$ | $V_1 \to V_3 \to V_2$ *(Normal points $-\hat{k}$)* |
| **$F_2$ (Front)** | $E_1, E_5, E_4$ | $V_1 \to V_2 \to V_4$ |
| **$F_3$ (Right)** | $E_2, E_6, E_5$ | $V_2 \to V_3 \to V_4$ |
| **$F_4$ (Left)** | $E_3, E_4, E_6$ | $V_3 \to V_1 \to V_4$ |

---

## 3. Applications & Use Cases

1. **GPU Vertex Buffer & Index Buffer Architecture**:
   The modern GPU rendering pipeline (Vulkan, DirectX 12) directly implements the geometric table structure:
   - **VBO (Vertex Buffer Object)**: Stores the Vertex Table as a contiguous memory array.
   - **IBO (Index Buffer Object)**: Stores the Polygon Table as indices into the VBO, reducing PCIe transfer bandwidth by $> 60\%$.
2. **CAD Solid Modeling (SolidWorks, Parasolid)**:
   Industrial mechanical engineering platforms store parts as CSG feature trees (extrudes, cuts, fillets) combined with B-rep topological boundary representations.
3. **Ray Tracing & Collision Acceleration**:
   Real-time ray tracing (NVIDIA RTX) constructs Bounding Volume Hierarchies (BVH) and Octrees over polygon meshes to accelerate ray-triangle intersection tests from $O(N)$ brute force to $O(\log N)$ tree traversal.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Determining Plane Coefficients from Three Vertices [Analytical Problem]
**Problem**:
Calculate the plane equation coefficients $A, B, C, D$ for the polygon face with vertices:
$$V_1(1, 1, 1), \quad V_2(3, 2, 1), \quad V_3(2, 4, 3)$$
Classify the position of point $P_{\text{test}}(2, 2, 5)$ relative to this plane.

**Solution**:
1. **Compute Displacement Vectors**:
   $$\vec{u} = V_2 - V_1 = \begin{bmatrix} 3 - 1 \\ 2 - 1 \\ 1 - 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}$$
   $$\vec{v} = V_3 - V_1 = \begin{bmatrix} 2 - 1 \\ 4 - 1 \\ 3 - 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix}$$

2. **Evaluate Surface Normal Vector via Cross-Product $\vec{N} = \vec{u} \times \vec{v}$**:
   $$\vec{N} = \det \begin{bmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & 0 \\ 1 & 3 & 2 \end{bmatrix}$$
   $$A = (1)(2) - (0)(3) = 2 - 0 = 2$$
   $$B = (0)(1) - (2)(2) = 0 - 4 = -4$$
   $$C = (2)(3) - (1)(1) = 6 - 1 = 5$$
   Normal vector $\vec{N} = \begin{bmatrix} 2 & -4 & 5 \end{bmatrix}^T$.

3. **Compute Coefficient $D$**:
   Substitute $V_1(1, 1, 1)$ into $Ax + By + Cz + D = 0$:
   $$2(1) + (-4)(1) + 5(1) + D = 0$$
   $$2 - 4 + 5 + D = 0 \implies 3 + D = 0 \implies D = -3$$
   **Plane Equation**: $2x - 4y + 5z - 3 = 0$.

4. **Spatial Classification of $P_{\text{test}}(2, 2, 5)$**:
   Evaluate $f(2, 2, 5)$:
   $$f(2, 2, 5) = 2(2) - 4(2) + 5(5) - 3 = 4 - 8 + 25 - 3 = 18$$
   Because $f(2, 2, 5) = 18 > 0$, the point lies in the **Positive Half-Space (OUTSIDE / in front of the polygon face)**.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [June 2024 Q6 / Dec 2018 Q5 — 4 Marks]
**Question**:
What are the different tables used for representing polygon surfaces? Illustrate with an example.

**Solution**:

To represent 3D polyhedral polygon surfaces efficiently without redundant data duplication, computer graphics systems organize polygon meshes into **three interrelated tables**:

1. **Vertex Table**:
   Contains the spatial coordinates $(x, y, z)$ of each distinct vertex point in the mesh.
2. **Edge Table**:
   Contains pairs of vertex indices specifying the two endpoint vertices for each unique edge segment. It may also include pointers to adjoining faces.
3. **Polygon Table (Face Table)**:
   Contains ordered sequences of edge indices (or vertex indices) defining the closed planar boundary of each polygon face in counterclockwise order.

**Illustrative Example (A 3D Triangle Face)**:
Consider a single triangular polygon facet $F_1$ formed by vertices $V_1(0, 0, 0), V_2(2, 0, 0), V_3(0, 3, 0)$:

- **Vertex Table**:
  - $V_1: (0, 0, 0)$
  - $V_2: (2, 0, 0)$
  - $V_3: (0, 3, 0)$
- **Edge Table**:
  - $E_1: (V_1, V_2)$
  - $E_2: (V_2, V_3)$
  - $E_3: (V_3, V_1)$
- **Polygon Table**:
  - $F_1: (E_1, E_2, E_3)$

**Benefits**:
- Vertex coordinates are stored once; moving a vertex updates only a single entry in the Vertex Table.
- Identifies shared edges between adjacent faces for normal vector interpolation.
- Reduces memory consumption and detects topological errors.

---

### Question 2 [Dec 2021 Q6 — 4 Marks]
**Question**:
Show how plane equations are used to identify the position of spatial points relative to the plane surface of an object.

**Solution**:

Every planar polygon surface in 3D space satisfies the algebraic plane equation:
$$Ax + By + Cz + D = 0$$
where $\vec{N} = \begin{bmatrix} A & B & C \end{bmatrix}^T$ is the surface normal vector pointing outward from the front face of the polygon, and $D$ is the scalar plane offset.

To determine the spatial position of any arbitrary test point $P(x, y, z)$ relative to the polygon surface, we evaluate the function:
$$f(x, y, z) = Ax + By + Cz + D$$

**Spatial Point Classification**:
1. **$f(x, y, z) > 0$ (Positive Half-Space)**:
   The point lies on the **outside** (in front of the surface). The angle between the vector from the plane to the point and the normal $\vec{N}$ is acute ($< 90^\circ$).
2. **$f(x, y, z) = 0$ (On the Surface Boundary)**:
   The point lies **directly on the plane** containing the polygon.
3. **$f(x, y, z) < 0$ (Negative Half-Space)**:
   The point lies on the **inside** (behind the surface). The angle between the vector from the plane to the point and the normal $\vec{N}$ is obtuse ($> 90^\circ$).

**Applications**:
- **Back-Face Culling**: If the camera position $(x_c, y_c, z_c)$ satisfies $f(x_c, y_c, z_c) < 0$, the camera is positioned behind the surface, identifying it as an occluded back-face that can be culled before rasterization.
- **Collision Detection**: A moving point object collides with the surface when the sign of $f(x, y, z)$ transitions between successive animation frames.

---

### Question 3 [Dec 2021 Q15b — 3 Marks]
**Question**:
Explain the boundary representation and space partitioning representation schemes used for solid object representation.

**Solution**:

| Dimension | Boundary Representation (B-rep) | Space-Partitioning Representation |
|---|---|---|
| **Fundamental Principle** | Represents a 3D solid by explicitly defining the **2D boundary surfaces** that enclose the object volume. | Represents a 3D solid by describing the **interior volume** occupied by the object in space. |
| **Mathematical Elements** | Expressed as collections of planar polygon facets (Vertex, Edge, Face tables), parametric surface patches (Bézier, B-splines), or NURBS surfaces. | Expressed as hierarchical spatial subdivision trees (Octrees, BSP trees) or combinations of primitive solids (CSG trees). |
| **Volume & Interior Properties** | Interior volume is implicit; computing mass properties requires integrating across surface boundary equations. | Interior volume is explicit; mass properties, volume, and moments of inertia are computed by aggregating cell volumes. |
| **GPU Rendering Throughput** | Exceptionally high. Modern GPUs are hardware-optimized to render B-rep triangle meshes at billions of triangles per second. | Requires conversion to boundary surface meshes (polygonization / marching cubes) before standard GPU rasterization. |
| **Primary Applications** | Real-time computer graphics, video game engines, animation, visual simulations. | CAD solid modeling, Boolean machining simulations (milling, drilling), finite element analysis (FEA), robotics collision volumes. |
