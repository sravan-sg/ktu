# Module 5: Revision Notes — Quick Review Guide

## 1. High-Yield Summary
- **Parallel Projections**: Center of Projection at infinity. Projectors are parallel. Preserves parallel lines and true scale.
  - *Orthographic*: Projectors perpendicular to view plane.
    - Axonometric: Isometric (equal angles), Dimetric (2 equal), Trimetric (all 3 different).
  - *Oblique*: Projectors intersect view plane at angle $\alpha \ne 90^\circ$.
    - Cavalier ($\alpha = 45^\circ$): Full scale on depth ($L_1 = 1$).
    - Cabinet ($\alpha = 63.4^\circ$): Half scale on depth ($L_1 = 0.5$, looks more natural).
- **Perspective Projections**: Projectors converge at Center of Projection (COP).
  - Produces *perspective foreshortening* (distant objects appear smaller: $x_p = \frac{x}{z/d}, y_p = \frac{y}{z/d}$).
  - Parallel lines not parallel to view plane converge at a *Vanishing Point*.
- **Visible Surface Detection (Hidden Surface Elimination)**:
  - *Object-Space*: Works in 3D object space ($O(n^2)$). Example: Back-Face Culling.
  - *Image-Space*: Works at screen pixel resolution ($O(n \cdot p)$). Example: Z-Buffer, A-Buffer.
  - *Back-Face Removal*: Discards faces where $\vec{N} \cdot \vec{V} \le 0$ ($C \ge 0$ when viewing along $-Z$).
  - *Z-Buffer*: Updates pixel if new $z < \text{DepthBuffer}[x][y]$. Incremental depth along scanline: $z' = z - A/C$.
  - *A-Buffer*: Replaces single float depth with linked list of fragment records for transparency and antialiasing.
  - *Painter's Algorithm (Depth Sort)*: Sorts polygons back-to-front. Resolves overlaps using 5 tests.

---

## 2. Essential Formulas & Matrices

### Perspective Projection Matrix (COP at origin, View plane at $z = d$):
$$\mathbf{P}_{\text{persp}} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 1/d & 0 \end{bmatrix}$$
$$\text{Coordinates after division by } w = z/d: \quad x_p = \frac{x}{z/d}, \quad y_p = \frac{y}{z/d}, \quad z_p = d$$

### Oblique Projection Equations:
$$x_p = x + z(L_1 \cos\phi), \quad y_p = y + z(L_1 \sin\phi)$$
- Cavalier: $L_1 = 1$ ($\alpha = 45^\circ$).
- Cabinet: $L_1 = 0.5$ ($\alpha = 63.4^\circ$).

### Back-Face Culling Condition:
$$\text{Plane: } Ax + By + Cz + D = 0$$
$$\text{Viewing along } -Z: \quad \vec{N} \cdot \begin{bmatrix} 0 \\ 0 \\ -1 \end{bmatrix} = -C \implies \begin{cases} C < 0 & \text{Front-Face (Visible)} \\ C \ge 0 & \text{Back-Face (Culled)} \end{cases}$$

### Z-Buffer Incremental Recurrence:
$$\mathbf{z_{x+1} = z_x - \frac{A}{C}}$$

---

## 3. Top 3 Exam Traps & Tips
1. **Cavalier vs. Cabinet Angles**: Remember that Cavalier uses $\alpha = 45^\circ$ ($L_1 = 1$, full length), while Cabinet uses $\alpha = 63.4^\circ$ ($\tan\alpha = 2 \implies L_1 = 0.5$, half length). Do not mix up the angles.
2. **Back-Face Condition Sign**: Be crystal clear about the viewing direction. When looking down the **$-Z$ axis** (right-handed convention), $C \ge 0$ means the normal points away, so it is a **back-face**.
3. **Z-Buffer Complexity**: Remember that the time complexity of the Z-Buffer algorithm is $O(n \cdot p)$ (proportional to total pixels and polygon coverage), but its execution time is practically independent of the number of overlapping polygons at a pixel because depth comparisons happen in fast hardware memory.

