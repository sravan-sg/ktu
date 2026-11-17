# Module 4: Revision Notes — Quick Review Guide

## 1. High-Yield Summary
- **Sutherland-Hodgman Polygon Clipping**:
  - Clips polygon sequentially against Left, Right, Bottom, Top boundary lines.
  - Four cases:
    1. In $\to$ In: Output $V_2$.
    2. In $\to$ Out: Output intersection $V'$.
    3. Out $\to$ Out: Output nothing.
    4. Out $\to$ In: Output $V'$, then $V_2$.
  - Limitation: Creates false bridging lines when clipping concave polygons that split into disjoint pieces.
- **Weiler-Atherton Clipping**:
  - Uses dual linked lists (Subject List & Window List).
  - Traverses from Entering intersections along subject polygon, switches at Exiting intersections to window boundary (clockwise). Correctly clips concave and disjoint polygons.
- **3D Object Representation**:
  - *Polygon Mesh Tables*: Vertex Table $(x, y, z)$, Edge Table $(V_1, V_2)$, Polygon Table $(E_1, E_2, \dots)$. Eliminates redundancy.
  - *Plane Equation*: $Ax + By + Cz + D = 0$, where normal $\vec{N} = (V_2 - V_1) \times (V_3 - V_1)$.
  - *Quadrics*: Defined by second-degree 3D polynomials (Sphere: $(x-x_c)^2+(y-y_c)^2+(z-z_c)^2=r^2$; Ellipsoid: $\sum (x-x_c)^2/r_x^2 = 1$).
- **3D Affine Transformations**:
  - Represented by $4 \times 4$ homogeneous matrices.
  - Non-commutative ($\mathbf{R}_x \mathbf{R}_y \ne \mathbf{R}_y \mathbf{R}_x$).
  - Rotation about arbitrary 3D axis requires 5 steps: Translate to origin $\to$ Rotate into $XZ$ plane $\to$ Rotate onto $Z$ axis $\to$ Rotate by $\theta$ about $Z \to$ Invert previous rotations and translation.

---

## 2. Master $4 \times 4$ Matrix Reference Table

| Transformation | Matrix Representation |
|---|---|
| **Translation** $\mathbf{T}(t_x, t_y, t_z)$ | $\begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}$ |
| **Scaling** $\mathbf{S}(s_x, s_y, s_z)$ | $\begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ |
| **Rotation about Z-axis** $\mathbf{R}_z(\theta)$ | $\begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ |
| **Rotation about X-axis** $\mathbf{R}_x(\theta)$ | $\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta & 0 \\ 0 & \sin\theta & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ |
| **Rotation about Y-axis** $\mathbf{R}_y(\theta)$ | $\begin{bmatrix} \cos\theta & 0 & \sin\theta & 0 \\ 0 & 1 & 0 & 0 \\ -\sin\theta & 0 & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ |
| **Fixed Point 3D Scaling** | $\begin{bmatrix} s_x & 0 & 0 & x_f(1 - s_x) \\ 0 & s_y & 0 & y_f(1 - s_y) \\ 0 & 0 & s_z & z_f(1 - s_z) \\ 0 & 0 & 0 & 1 \end{bmatrix}$ |

---

## 3. Top 3 Exam Traps & Tips
1. **Sign in $\mathbf{R}_y(\theta)$**: In $\mathbf{R}_y(\theta)$, the negative sign is on the bottom-left term ($-\sin\theta$ at row 3, col 1) and positive $\sin\theta$ is at row 1, col 3. This differs from $\mathbf{R}_x$ and $\mathbf{R}_z$ due to cyclic coordinate permutation ($X \to Y \to Z$).
2. **Sutherland-Hodgman Vertex Output Order**: In Case 4 (Out $\to$ In), remember to output the **intersection point $V'$ FIRST**, and then vertex **$V_2$ SECOND**. Outputting them in reverse order will invert the polygon's winding direction.
3. **Plane Constant $D$ Calculation**: When calculating the plane equation from normal vector $\vec{N} = (A, B, C)$, remember that $D = -(Ax_1 + By_1 + Cz_1)$. Omitting the negative sign is the single most common error in student solutions.

