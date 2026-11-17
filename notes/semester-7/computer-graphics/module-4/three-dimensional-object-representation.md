# Three-Dimensional Object Representation: Polygon Surfaces & Quadric Surfaces

## 1. Explanation
In 3D computer graphics, real-world objects and synthetic virtual shapes must be modeled mathematically using data structures that balance geometric accuracy, memory footprint, and rendering pipeline throughput.

---

### Classification of 3D Object Representations
3D representations are broadly divided into:
1. **Boundary Representations (B-reps)**: Describe 3D objects by their enclosing boundary surfaces (e.g., polygon mesh surfaces, parametric spline patches).
2. **Space-Partitioning Representations**: Describe 3D objects as spatial volumes (e.g., Constructive Solid Geometry - CSG, Octrees, Voxel grids).

---

### Polygon Surfaces (Polyhedral Meshes)
A polygon mesh represents a 3D surface as a collection of planar polygon facets (typically triangles or quadrilaterals). Because graphic processors (GPUs) are designed as massively parallel triangle processing engines, polygon meshes are the universal rendering standard.

#### Data Structures for Polygon Surfaces: Geometric Tables
To eliminate redundant storage and facilitate fast topological lookups, a polygon surface is organized into three relational tables:

1. **Vertex Table**:
   - Stores the 3D spatial coordinates $(x, y, z)$ of each distinct vertex point in the mesh.
   $$\text{V1: } (x_1, y_1, z_1), \quad \text{V2: } (x_2, y_2, z_2), \dots$$
2. **Edge Table**:
   - Stores pointers/indices to the two endpoint vertices that define each unique line segment.
   - May also store pointers to the adjoining polygon faces for fast neighbor connectivity.
   $$\text{E1: } (V_1, V_2), \quad \text{E2: } (V_2, V_3), \dots$$
3. **Polygon Table (Face Table)**:
   - Stores the sequence of directed edges (or vertices) that bound each planar polygon facet.
   $$\text{F1: } (E_1, E_2, E_3), \quad \text{F2: } (E_3, E_4, E_5), \dots$$

```
VERTEX TABLE            EDGE TABLE                  POLYGON TABLE
V1: (x1, y1, z1) ◄──┐   E1: (V1, V2) ◄──────────┐   F1: (E1, E2, E3)
V2: (x2, y2, z2) ◄──┼───E2: (V2, V3)            │   F2: (E3, E4, E5)
V3: (x3, y3, z3) ◄──┘   E3: (V3, V1) ───────────┘
```
**Benefits of the Three-Table Architecture**:
- Coordinate data $(x, y, z)$ is stored exactly once; moving a vertex updates only a single entry in the vertex table.
- Shared edges between adjacent faces are identified immediately, essential for Gouraud and Phong normal averaging.
- Detects topological inconsistencies (e.g., unclosed meshes, non-manifold edges).

---

### Polygon Plane Equations
Every planar polygon surface in 3D space satisfies the algebraic plane equation:
$$Ax + By + Cz + D = 0$$
where $\vec{N} = \begin{bmatrix} A & B & C \end{bmatrix}^T$ is the surface normal vector perpendicular to the polygon face.

#### Determining Plane Coefficients from Three Vertices:
Given three non-collinear vertices $V_1(x_1, y_1, z_1), V_2(x_2, y_2, z_2), V_3(x_3, y_3, z_3)$ ordered counterclockwise when viewed from the outside:
$$\vec{N} = (V_2 - V_1) \times (V_3 - V_1)$$
Evaluating the vector cross-product using determinants:
$$A = (y_2 - y_1)(z_3 - z_1) - (z_2 - z_1)(y_3 - y_1)$$
$$B = (z_2 - z_1)(x_3 - x_1) - (x_2 - x_1)(z_3 - z_1)$$
$$C = (x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1)$$
$$D = -(Ax_1 + By_1 + Cz_1)$$

#### Point-Plane Spatial Spatial Test:
For any arbitrary 3D spatial point $(x, y, z)$:
- $Ax + By + Cz + D < 0 \implies$ Point lies **behind / inside** the surface.
- $Ax + By + Cz + D = 0 \implies$ Point lies **on** the surface plane.
- $Ax + By + Cz + D > 0 \implies$ Point lies **in front / outside** the surface.

---

### Quadric Surfaces
Quadric surfaces are curved 3D surfaces defined algebraically by a second-degree polynomial equation in three spatial variables:
$$Ax^2 + By^2 + Cz^2 + Dxy + Eyz + Fxz + Gx + Hy + Iz + J = 0$$

#### 1. Sphere
A sphere centered at $(x_c, y_c, z_c)$ with radius $r$:
- **Implicit Equation**:
  $$(x - x_c)^2 + (y - y_c)^2 + (z - z_c)^2 = r^2$$
- **Parametric Formulation** (using latitude $\phi \in [-\pi/2, \pi/2]$ and longitude $\theta \in [-\pi, \pi]$):
  $$x = x_c + r\cos\phi\cos\theta$$
  $$y = y_c + r\cos\phi\sin\theta$$
  $$z = z_c + r\sin\phi$$

#### 2. Ellipsoid
An ellipsoid is a generalized quadratic surface with three semi-principal axes $r_x, r_y, r_z$:
- **Implicit Equation**:
  $$\left(\frac{x - x_c}{r_x}\right)^2 + \left(\frac{y - y_c}{r_y}\right)^2 + \left(\frac{z - z_c}{r_z}\right)^2 = 1$$
- **Parametric Formulation**:
  $$x = x_c + r_x\cos\phi\cos\theta$$
  $$y = y_c + r_y\cos\phi\sin\theta$$
  $$z = z_c + r_z\sin\phi$$

#### 3. Torus (Donut-shaped surface)
Formed by rotating a circle of radius $r$ about a coplanar axis at a distance $R$ ($R > r$):
- **Implicit Equation**:
  $$\left(R - \sqrt{x^2 + y^2}\right)^2 + z^2 = r^2$$
- **Parametric Formulation** ($\phi, \theta \in [0, 2\pi]$):
  $$x = (R + r\cos\phi)\cos\theta$$
  $$y = (R + r\cos\phi)\sin\theta$$
  $$z = r\sin\phi$$

---

## 2. Example: Polygon Table Relational Structure
```
            V2 (0, 10, 0)
              /\
             /  \
        E1  / F1 \ E2
           /      \
          /   E3   \
V1 (-10, 0, 0)────V3 (10, 0, 0)

Vertex Table:
  V1: (-10, 0, 0)
  V2: (0, 10, 0)
  V3: (10, 0, 0)

Edge Table:
  E1: (V1, V2)
  E2: (V2, V3)
  E3: (V3, V1)

Polygon Face Table:
  F1: (E1, E2, E3)
```

---

## 3. Applications & Use Cases
1. **Video Game Asset Modeling (glTF, OBJ, FBX)**: Modern 3D character models (in Unreal Engine, Unity) are stored using vertex, index, and normal buffers representing indexed triangle meshes.
2. **Ray Tracing of Mathematical Primitives**: Quadric surfaces (spheres, ellipsoids, cylinders) have closed-form analytical ray-surface intersection formulas ($at^2 + bt + c = 0$), enabling direct, exact ray tracing without polygon tessellation.
3. **Collision Detection in Robotics & Physics Engines (Bullet, PhysX)**: Robot links and physical rigid bodies are bounded by quadric bounding volumes (spheres, capsules) for rapid $O(1)$ overlap detection before detailed mesh-mesh collision tests.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Determining 3D Polygon Plane Equation [KTU May 2019 / Dec 2023 - 4 Marks]
**Problem**:
A triangular polygon in 3D space has vertices $V_1(0, 0, 0)$, $V_2(2, 0, 0)$, and $V_3(0, 3, 0)$.
Determine the plane coefficients $A, B, C, D$ and state the surface normal vector.

**Step-by-step Solution**:
1. **Edge Vectors**:
   $$\vec{e}_1 = V_2 - V_1 = (2 - 0, 0 - 0, 0 - 0) = (2, 0, 0)$$
   $$\vec{e}_2 = V_3 - V_1 = (0 - 0, 3 - 0, 0 - 0) = (0, 3, 0)$$
2. **Cross Product for Normal Vector $\vec{N}$**:
   $$\vec{N} = \vec{e}_1 \times \vec{e}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 0 & 0 \\ 0 & 3 & 0 \end{vmatrix}$$
   $$A = (0 \times 0 - 0 \times 3) = 0$$
   $$B = -(2 \times 0 - 0 \times 0) = 0$$
   $$C = (2 \times 3 - 0 \times 0) = 6$$
   Normal vector $\vec{N} = (0, 0, 6)$ (or normalized unit vector $\hat{N} = (0, 0, 1)$).
3. **Determine Constant $D$**:
   $$D = -(Ax_1 + By_1 + Cz_1) = -(0(0) + 0(0) + 6(0)) = 0$$
4. **Final Plane Equation**:
   $$0x + 0y + 6z + 0 = 0 \implies \mathbf{z = 0}$$
   (The polygon lies squarely on the $xy$-plane).

---

### Example 2: Ray-Sphere Quadric Intersection [KTU Analytical Pattern]
**Problem**:
A 3D sphere centered at the origin $(0, 0, 0)$ has a radius $r = 5$.
A viewing ray originates at $P_0(0, 0, 10)$ and travels in direction $\vec{d} = (0, 0, -1)$.
Find the exact entry and exit intersection points of the ray with the sphere.

**Step-by-step Solution**:
1. **Parametric Ray Equation**:
   $$P(t) = P_0 + t\vec{d} = (0, 0, 10 - t)$$
2. **Sphere Equation**:
   $$x^2 + y^2 + z^2 = r^2 \implies 0^2 + 0^2 + (10 - t)^2 = 5^2$$
   $$(10 - t)^2 = 25 \implies 10 - t = \pm 5$$
   $$t_1 = 10 - 5 = 5, \quad t_2 = 10 + 5 = 15$$
3. **Intersection Coordinates**:
   - At $t_1 = 5$: $P(5) = (0, 0, 10 - 5) = \mathbf{(0, 0, 5)}$ (front entry point).
   - At $t_2 = 15$: $P(15) = (0, 0, 10 - 15) = \mathbf{(0, 0, -5)}$ (rear exit point).

---

### Example 3: Storage Comparison: Raw Vertices vs. Relational Tables [KTU Analytical Pattern]
**Problem**:
A 3D mesh model of a regular octahedron has 6 vertices, 12 edges, and 8 triangular faces.
Compare the memory footprint required to store this geometry using:
1. An unindexed array of triangles (raw coordinates per vertex per face).
2. A relational Vertex Table + Polygon Face Table (indexed mesh).
Assume coordinates and indices each consume 4 bytes.

**Step-by-step Solution**:
1. **Unindexed Raw Triangles**:
   - 8 faces $\times$ 3 vertices per face $= 24$ vertex points.
   - Each vertex point has 3 coordinates $(x, y, z) \implies 3 \times 4 \text{ bytes} = 12 \text{ bytes}$.
   - Total Memory $= 24 \times 12 \text{ bytes} = \mathbf{288 \text{ bytes}}$.
2. **Indexed Relational Structure**:
   - **Vertex Table**: 6 unique vertices $\times$ 12 bytes $= 72 \text{ bytes}$.
   - **Polygon Table**: 8 faces $\times$ 3 vertex indices $\times$ 4 bytes $= 96 \text{ bytes}$.
   - Total Memory $= 72 + 96 = \mathbf{168 \text{ bytes}}$.
3. **Savings**: The relational table reduces memory by $\approx 42\%$, and this advantage scales dramatically on large meshes where each vertex is shared by 6 to 8 adjacent triangles.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / June 2022 - 4 Marks]
**Question**:
Explain the geometric tables used for representing 3D polygon surfaces. What are their advantages?

**Solution**:
1. **The Three Geometric Tables**:
   - **Vertex Table**: Stores the physical coordinate geometry of every unique vertex in the model:
     $$V_1(x_1, y_1, z_1), \ V_2(x_2, y_2, z_2), \dots, V_n(x_n, y_n, z_n)$$
   - **Edge Table**: Stores pointers to the pair of vertex indices defining each unique edge segment:
     $$E_1(V_1, V_2), \ E_2(V_2, V_3), \dots, E_m(V_i, V_j)$$
   - **Polygon Table (Face Table)**: Stores the ordered sequence of edge indices (or vertex indices) forming each closed polygon facet:
     $$F_1(E_1, E_2, E_3), \ F_2(E_3, E_4, E_5), \dots$$
2. **Key Advantages**:
   - **Eliminates Storage Redundancy**: In a 3D mesh, a vertex is typically shared by 4 to 8 adjacent faces. Storing its 3D coordinates once in the vertex table saves massive memory.
   - **Efficient Geometric Manipulation**: Applying geometric transformations (translation, rotation, scaling) requires modifying only the coordinates in the vertex table; edge and polygon tables remain unchanged.
   - **Rapid Neighbor Lookups & Shading**: Adjoining polygons sharing a common edge can be looked up instantly, essential for computing vertex normal averages in Gouraud and Phong shading.

---

### Question 2 [KTU December 2020 / December 2023 - 4 Marks]
**Question**:
What are quadric surfaces? Give the implicit and parametric equations of a sphere and an ellipsoid.

**Solution**:
1. **Definition of Quadric Surfaces**:
   Quadric surfaces are curved 3D geometric surfaces described implicitly by a second-degree polynomial equation in three spatial coordinates:
   $$Ax^2 + By^2 + Cz^2 + Dxy + Eyz + Fxz + Gx + Hy + Iz + J = 0$$
   They represent fundamental analytical shapes including spheres, ellipsoids, paraboloids, hyperboloids, and tori.
2. **Equations**:
   - **Sphere** (radius $r$, centered at $(x_c, y_c, z_c)$):
     - *Implicit Equation*:
       $$(x - x_c)^2 + (y - y_c)^2 + (z - z_c)^2 = r^2$$
     - *Parametric Equation* ($\phi \in [-\pi/2, \pi/2], \theta \in [-\pi, \pi]$):
       $$x = x_c + r\cos\phi\cos\theta$$
       $$y = y_c + r\cos\phi\sin\theta$$
       $$z = z_c + r\sin\phi$$
   - **Ellipsoid** (semi-axes $r_x, r_y, r_z$, centered at $(x_c, y_c, z_c)$):
     - *Implicit Equation*:
       $$\left(\frac{x - x_c}{r_x}\right)^2 + \left(\frac{y - y_c}{r_y}\right)^2 + \left(\frac{z - z_c}{r_z}\right)^2 = 1$$
     - *Parametric Equation* ($\phi \in [-\pi/2, \pi/2], \theta \in [-\pi, \pi]$):
       $$x = x_c + r_x\cos\phi\cos\theta$$
       $$y = y_c + r_y\cos\phi\sin\theta$$
       $$z = z_c + r_z\sin\phi$$

