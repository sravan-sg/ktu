# Three-Dimensional Projections: Parallel and Perspective Projections

## 1. Explanation

In three-dimensional computer graphics, virtual objects and scenes exist within a continuous 3D Euclidean space $\mathbb{R}^3$. However, physical output display monitors (CRT, LCD, OLED) and printed media are intrinsically **planar, two-dimensional surfaces** $\mathbb{R}^2$. 

A **3D projection** is a mathematical transformation that maps points from a 3D coordinate space onto a designated 2D planar surface called the **Projection Plane** (or View Plane):
$$P(x, y, z) \xrightarrow{\text{Projection}} P_p(x_p, y_p)$$

The mapping is performed by casting imaginary straight lines called **Projectors** (lines of projection) from a **Center of Projection (COP)** (or Projection Reference Point - PRP), passing through each vertex of the object, until they intersect the projection plane.

---

### Comprehensive Taxonomy of 3D Projections

All planar geometric projections are classified according to the relationship between their projectors and the projection plane:

```
                            3D PLANAR PROJECTIONS
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            ▼                                                   ▼
   PARALLEL PROJECTIONS                               PERSPECTIVE PROJECTIONS
   (Center of Projection at infinity;                 (Center of Projection at finite
    Projectors are parallel)                           distance; Projectors converge at COP)
            │                                                   │
     ┌──────┴──────┐                                     ┌──────┼──────┐
     ▼             ▼                                     ▼      ▼      ▼
ORTHOGRAPHIC    OBLIQUE                              1-POINT  2-POINT 3-POINT
(Projectors     (Projectors at                       (One     (Two    (Three
 $\perp$ Plane)  angle $\alpha \ne 90^\circ$)         Pr. VP)  Pr. VPs) Pr. VPs)
     │             │
     ├─────────────┼────────────────────────┐
     ▼             ▼                        ▼
 MULTIVIEW    AXONOMETRIC               CAVALIER   CABINET
 (Front, Top, (Isometric,               ($\alpha=45^\circ$, ($\alpha=63.4^\circ$,
  Side)        Dimetric, Trimetric)      $L=1$)     $L=0.5$)
```

---

### Parallel Projections

In a **Parallel Projection**, the Center of Projection is situated at an infinite distance ($\infty$) from the projection plane. Consequently, all projector lines are strictly **parallel to each other**.

#### Architectural Properties:
- **Parallel lines in 3D remain parallel in the 2D projection**.
- **No Perspective Foreshortening**: The projected size of an object does not change with distance from the camera (depth $z$ is decoupled from $x_p, y_p$).
- Excellent for technical drafting, architecture, and engineering blueprints where exact physical dimensions and metric ratios must be measured directly off the drawing.

---

### 1. Orthographic Parallel Projections
Projectors are strictly **perpendicular (orthogonal)** to the projection plane ($\alpha = 90^\circ$).

If the projection plane is chosen as the $xy$-plane ($z = 0$), the transformation simply discards the $z$-coordinate:
$$x_p = x, \quad y_p = y, \quad z_p = 0$$

In $4 \times 4$ homogeneous matrix form:
$$\mathbf{M}_{\text{ortho}} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

#### Sub-categories of Orthographic Projections:
1. **Multiview Orthographic Projections**:
   The projection plane is parallel to one of the principal coordinate planes of the object:
   - **Front Elevation**: Projectors parallel to Z-axis onto the $xy$-plane ($z=0$).
   - **Top View (Plan View)**: Projectors parallel to Y-axis onto the $xz$-plane ($y=0$).
   - **Side Elevation**: Projectors parallel to X-axis onto the $yz$-plane ($x=0$).
   *Advantage*: Shows true lengths and true angles of object faces without distortion.
2. **Axonometric Projections**:
   The projection plane is tilted relative to all principal coordinate axes, displaying multiple faces of the 3D solid simultaneously:
   - **Isometric Projection**: The projection plane intersects all three principal coordinate axes at **equal angles** ($\approx 54.74^\circ$).
     - All three axes are foreshortened by the exact same ratio:
       $$\text{Foreshortening Factor} = \sqrt{\frac{2}{3}} \approx 0.816 \quad (81.6\%)$$
     - In the projected 2D image, the three coordinate axes are oriented at equal $120^\circ$ angles relative to each other.
   - **Dimetric Projection**: Two of the three principal axes make equal angles with the projection plane (two axes share equal foreshortening).
   - **Trimetric Projection**: All three principal axes make different angles with the projection plane (all three axes have different foreshortening factors).

---

### 2. Oblique Parallel Projections

In an **Oblique Parallel Projection**, projectors are **not perpendicular** to the projection plane, intersecting it at an arbitrary angle $\alpha \ne 90^\circ$.

```
                       Z (Depth)
                       ▲
                       │     Projector Line
                       │    /
                       │   /  Angle alpha with plane
                       │  /
                       │ /
                       └──────────────────► X (Width)
                       │\
                       │ \ Projected vector
                       │  \ makes angle phi with X-axis
                       ▼
                       Y (Height)
```

#### Derivation of the Oblique Projection Matrix
Let the projection plane be the $xy$-plane ($z = 0$).
Consider a point $P(x, y, z)$. Its projector line strikes the projection plane at $P_p(x_p, y_p, 0)$.

Let:
- $\alpha$ = Angle that the projector makes with the projection plane ($0 < \alpha \le 90^\circ$).
- $\phi$ = Angle that the projected line of a unit z-segment makes with the horizontal X-axis on the projection plane.
- $L$ = Length of the projection of a unit segment perpendicular to the projection plane:
  $$L = \frac{1}{\tan\alpha} = \cot\alpha$$

For an arbitrary point at depth $z$, the projected displacement along the projection plane is:
$$\Delta x = z \cdot L \cos\phi$$
$$\Delta y = z \cdot L \sin\phi$$

Therefore, the coordinates of the projected point $P_p$ are:
$$x_p = x + z \cdot L \cos\phi$$
$$y_p = y + z \cdot L \sin\phi$$
$$z_p = 0$$

In $4 \times 4$ homogeneous matrix form:
$$\mathbf{M}_{\text{oblique}} = \begin{bmatrix} 1 & 0 & L\cos\phi & 0 \\ 0 & 1 & L\sin\phi & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

#### Special Classes of Oblique Projections:

| Parameter | Cavalier Projection | Cabinet Projection |
|---|---|---|
| **Projector Angle ($\alpha$)** | $\alpha = 45^\circ \implies \tan 45^\circ = 1$ | $\alpha = \arctan(2) \approx 63.43^\circ \implies \tan 63.43^\circ = 2$ |
| **Length Factor ($L = \cot\alpha$)** | $L = \frac{1}{\tan 45^\circ} = 1.0$ | $L = \frac{1}{\tan 63.43^\circ} = 0.5$ |
| **Foreshortening of Depth** | **Zero foreshortening ($100\%$)**. Lines perpendicular to the view plane are projected at **true length**. | **$50\%$ foreshortening**. Lines perpendicular to the view plane are drawn at **half true length**. |
| **Common Direction Angle ($\phi$)**| Typically $\phi = 45^\circ$ or $\phi = 30^\circ$. | Typically $\phi = 45^\circ$ or $\phi = 63.43^\circ$. |
| **Visual Appearance** | Looks unnaturally elongated and deep; front faces are true size, but depth appears exaggerated. | **Most realistic oblique view**. Depth proportions appear natural to human perception. |
| **Transformation Matrix ($\phi = 45^\circ$)** | $\mathbf{M}_{\text{cav}} = \begin{bmatrix} 1 & 0 & \frac{\sqrt{2}}{2} & 0 \\ 0 & 1 & \frac{\sqrt{2}}{2} & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ | $\mathbf{M}_{\text{cab}} = \begin{bmatrix} 1 & 0 & \frac{\sqrt{2}}{4} & 0 \\ 0 & 1 & \frac{\sqrt{2}}{4} & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ |

---

### Perspective Projections

In a **Perspective Projection**, the Center of Projection (COP) is situated at a **finite distance** from the projection plane. Projectors radiate from the COP through the scene like visual rays converging at an observer's pupil or camera focal point.

```
                  PERSPECTIVE PROJECTION GEOMETRY
                  
            Projection Reference
            Point (PRP) at Zprp                 Projection Plane at Zvp
                   * (0, 0, Zprp)                         │
                   │ \                                    │
                   │  \                                   │
                   │   \                                  │
                   │    \                          Pp(xp,yp)
                   │     \                                * ────────────► P(x, y, z)
                   │      \                               │            /
                   │       \                              │           /
                   │        \                             │          /
      ─────────────┴─────────\────────────────────────────┴─────────/─────────────► Zv
                   0          \                           Zvp      /
                               \                                  /
                                ──────────────────────────────────
```

#### Key Characteristics:
1. **Perspective Foreshortening**: Objects appear progressively smaller as their distance ($z$) from the observer increases:
   $$\text{Apparent Size} \propto \frac{1}{\text{Distance}}$$
2. **Non-Parallelism**: Parallel lines in 3D space that are not parallel to the projection plane converge to a single point called a **Vanishing Point**.
3. Produces realistic images matching human binocular and photographic vision.

---

### Mathematical Derivation of Perspective Transformation Matrix

Let the viewing coordinate system be aligned with the camera:
- The observer's eye is located at the **Projection Reference Point (PRP)**: $(0, 0, z_{\text{prp}})$.
- The **View Plane (Projection Plane)** is parallel to the $xy$-plane at distance $z = z_{\text{vp}}$.
- We seek to project an arbitrary 3D spatial point $P(x, y, z)$ onto the view plane at $P_p(x_p, y_p, z_{\text{vp}})$.

#### 1. Derivation Using Similar Triangles
In the $XZ$-plane projection, consider the similar triangles formed by the projector ray connecting $(0, 0, z_{\text{prp}})$ and $(x, y, z)$:

$$\frac{x_p}{x} = \frac{z_{\text{vp}} - z_{\text{prp}}}{z - z_{\text{prp}}} \implies x_p = x \cdot \left[ \frac{z_{\text{vp}} - z_{\text{prp}}}{z - z_{\text{prp}}} \right]$$

Similarly, in the $YZ$-plane projection:
$$\frac{y_p}{y} = \frac{z_{\text{vp}} - z_{\text{prp}}}{z - z_{\text{prp}}} \implies y_p = y \cdot \left[ \frac{z_{\text{vp}} - z_{\text{prp}}}{z - z_{\text{prp}}} \right]$$

Let $d_{\text{proj}} = z_{\text{vp}} - z_{\text{prp}}$ be the distance from the PRP to the view plane:
$$x_p = \frac{x \cdot d_{\text{proj}}}{z - z_{\text{prp}}}, \quad y_p = \frac{y \cdot d_{\text{proj}}}{z - z_{\text{prp}}}$$

Dividing numerator and denominator by $-z_{\text{prp}}$:
$$x_p = \frac{x \left(\frac{d_{\text{proj}}}{-z_{\text{prp}}}\right)}{\frac{z - z_{\text{prp}}}{-z_{\text{prp}}}} = \frac{x \left(\frac{d_{\text{proj}}}{-z_{\text{prp}}}\right)}{1 - \frac{z}{z_{\text{prp}}}}$$

---

#### 2. Special Case (i): View Plane at Coordinate Origin ($z_{\text{vp}} = 0$, UV-Plane)
When the view plane coincides with the $xy$-plane ($z_{\text{vp}} = 0$), $d_{\text{proj}} = 0 - z_{\text{prp}} = -z_{\text{prp}}$:
$$x_p = \frac{x(-z_{\text{prp}})}{z - z_{\text{prp}}} = \frac{x}{1 - z/z_{\text{prp}}}$$
$$y_p = \frac{y(-z_{\text{prp}})}{z - z_{\text{prp}}} = \frac{y}{1 - z/z_{\text{prp}}}$$
$$z_p = 0$$

In $4 \times 4$ homogeneous coordinates:
$$\begin{bmatrix} X_h \\ Y_h \\ Z_h \\ w \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & -1/z_{\text{prp}} & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} = \begin{bmatrix} x \\ y \\ 0 \\ 1 - z/z_{\text{prp}} \end{bmatrix}$$

Dividing by the homogeneous scale factor $w = 1 - z/z_{\text{prp}}$:
$$x_p = \frac{X_h}{w} = \frac{x}{1 - z/z_{\text{prp}}}, \quad y_p = \frac{Y_h}{w} = \frac{y}{1 - z/z_{\text{prp}}}, \quad z_p = 0$$

---

#### 3. Special Case (ii): Projection Reference Point at Origin ($z_{\text{prp}} = 0$)
When the camera eye is placed at the coordinate origin $(0, 0, 0)$ looking down the $+Z$ axis, and the view plane is placed at $z = d$:
$$x_p = \frac{x \cdot d}{z} = \frac{x}{z/d}$$
$$y_p = \frac{y \cdot d}{z} = \frac{y}{z/d}$$

In $4 \times 4$ homogeneous matrix form:
$$\mathbf{M}_{\text{persp}} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 1/d & 0 \end{bmatrix}$$

Applying this matrix to $P(x, y, z, 1)$:
$$\mathbf{M}_{\text{persp}} \cdot \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} = \begin{bmatrix} x \\ y \\ z \\ z/d \end{bmatrix}$$
After **perspective division** by $w = z/d$:
$$P_p = \begin{bmatrix} x/(z/d) \\ y/(z/d) \\ d \\ 1 \end{bmatrix} = \begin{bmatrix} x \cdot d / z \\ y \cdot d / z \\ d \\ 1 \end{bmatrix}$$

---

### Vanishing Points & Perspective Classifications

A **Vanishing Point (VP)** is the point on the projection plane where the projections of a family of mutually parallel 3D lines appear to intersect.

#### Mathematical Derivation of Vanishing Point:
Consider a set of parallel lines defined parametrically with direction vector $\vec{V} = \begin{bmatrix} a & b & c \end{bmatrix}^T$:
$$x(t) = x_0 + a \cdot t, \quad y(t) = y_0 + b \cdot t, \quad z(t) = z_0 + c \cdot t$$
Substituting into the perspective equations (with COP at origin and view plane at $z = d$):
$$x_p(t) = \frac{(x_0 + a \cdot t) d}{z_0 + c \cdot t}, \quad y_p(t) = \frac{(y_0 + b \cdot t) d}{z_0 + c \cdot t}$$

Taking the limit as distance $t \to \infty$:
$$\lim_{t \to \infty} x_p(t) = \lim_{t \to \infty} \frac{x_0/t + a}{z_0/t + c} d = \frac{a \cdot d}{c}$$
$$\lim_{t \to \infty} y_p(t) = \lim_{t \to \infty} \frac{y_0/t + b}{z_0/t + c} d = \frac{b \cdot d}{c}$$

**The Vanishing Point Coordinates**:
$$\text{VP} = \left( \frac{a \cdot d}{c}, \ \frac{b \cdot d}{c}, \ d \right)$$
Notice that the vanishing point depends **only on the direction vector $(a, b, c)$** and is completely independent of the starting coordinates $(x_0, y_0, z_0)$. All lines with direction $(a, b, c)$ converge to the same vanishing point.

#### Principal Vanishing Points:
Vanishing points formed by lines parallel to one of the principal coordinate axes ($X, Y,$ or $Z$):
1. **One-Point Perspective**:
   - The projection plane is parallel to **two principal axes** (e.g., $XY$-plane).
   - Only lines parallel to the $Z$-axis (depth) converge to a vanishing point.
   - Used for looking down straight hallways, railroad tracks, or tunnels.
2. **Two-Point Perspective**:
   - The projection plane is parallel to **one principal axis** (typically the vertical $Y$-axis).
   - Horizontal lines parallel to $X$ and $Z$ converge to two distinct vanishing points on the horizon line.
   - Standard architectural view of building exteriors viewed from street level.
3. **Three-Point Perspective**:
   - The projection plane is tilted relative to **all three principal axes**.
   - Lines along $X, Y,$ and $Z$ converge to three separate vanishing points.
   - Used for high dramatic angles: bird's-eye view (looking down from skyscraper) or worm's-eye view (looking up).

---

## 2. Example: Complete Comparison Table

| Property | Parallel Projections | Perspective Projections |
|---|---|---|
| **Center of Projection** | At infinity ($\infty$). | At finite, specified distance ($z_{\text{prp}}$). |
| **Projector Lines** | Mutually parallel. | Converge at the Center of Projection. |
| **Parallel Lines** | Remain strictly parallel after projection. | Converge to vanishing points (unless parallel to view plane). |
| **Object Size vs. Distance** | Constant. No foreshortening; distance from camera has zero impact. | Inversely proportional to distance ($1/z$). Distant objects appear smaller. |
| **Angles & Proportions** | Preserved on planes parallel to view plane. | Distorted; angles change dynamically across view field. |
| **Realism** | Low realism. Appears flat, isometric, or unnatural. | **High realism**. Accurately mimics human vision and photography. |
| **Engineering Utility** | High. Dimensions can be scaled directly with a physical ruler. | Low. Cannot measure true dimensions directly due to foreshortening. |
| **Transformation Matrix** | Affine $4 \times 4$ matrix with fourth row $\begin{bmatrix} 0 & 0 & 0 & 1 \end{bmatrix}$. | Projective $4 \times 4$ matrix; fourth row contains $-1/z_{\text{prp}}$ or $1/d$. |

---

## 3. Applications & Use Cases

1. **CAD/CAM Engineering Drafts (SolidWorks / CATIA)**:
   Orthographic multiview projections (Front, Top, Right-side) provide unambiguous mechanical specifications with accurate dimension tolerancing for CNC milling and manufacturing.
2. **Video Game Rendering Engines (Unreal Engine / Unity)**:
   3D perspective projection matrices are calculated dynamically per frame from the player's camera Field of View (FOV) and aspect ratio:
   $$\mathbf{P}_{\text{persp}} = \begin{bmatrix} \frac{1}{\text{aspect} \cdot \tan(\text{FOV}/2)} & 0 & 0 & 0 \\ 0 & \frac{1}{\tan(\text{FOV}/2)} & 0 & 0 \\ 0 & 0 & -\frac{f+n}{f-n} & -\frac{2fn}{f-n} \\ 0 & 0 & -1 & 0 \end{bmatrix}$$
3. **2.5D Isometric RPG Games (*Diablo*, *SimCity*, *Age of Empires*)**:
   Use isometric axonometric parallel projections where all 3D tiles maintain identical pixel dimensions regardless of spatial position, allowing infinite map panning without geometric scaling recalculations.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Perspective Projection of a 3D Line Segment [KTU Dec 2020 Pattern]
**Problem**:
A perspective projection system has its Center of Projection at the coordinate origin $(0, 0, 0)$ and its view plane at $z = 10$. 
Determine the projected coordinates of the 3D line segment joining endpoints $P_1(2, 4, 20)$ and $P_2(6, 12, 60)$.

**Solution**:
Camera at origin, view plane distance $d = 10$.
Perspective projection formulas:
$$x_p = \frac{x \cdot d}{z} = \frac{10x}{z}, \quad y_p = \frac{y \cdot d}{z} = \frac{10y}{z}$$

**1. Transform Endpoint $P_1(2, 4, 20)$**:
$$x_{p1} = \frac{10(2)}{20} = \frac{20}{20} = 1.0$$
$$y_{p1} = \frac{10(4)}{20} = \frac{40}{20} = 2.0$$
$$P_{p1} = (1.0, 2.0, 10.0)$$

**2. Transform Endpoint $P_2(6, 12, 60)$**:
$$x_{p2} = \frac{10(6)}{60} = \frac{60}{60} = 1.0$$
$$y_{p2} = \frac{10(12)}{60} = \frac{120}{60} = 2.0$$
$$P_{p2} = (1.0, 2.0, 10.0)$$

**Analytical Insight**:
Both endpoints project to the exact same point $(1.0, 2.0)$!
*Reason*: Points $P_1(2, 4, 20)$ and $P_2(6, 12, 60)$ lie on the exact same ray radiating from the center of projection ($P_2 = 3 \cdot P_1$). In perspective projection, the entire line segment projects directly along the line of sight, degenerating into a single visible point.

---

### Example 2: Cavalier vs. Cabinet Projection of a Unit Cube [KTU Dec 2021 Pattern]
**Problem**:
A unit cube has a vertex at $P(1, 1, 1)$. Compute its projected coordinates on the $xy$-plane using:
(a) Cavalier projection with $\phi = 45^\circ$.
(b) Cabinet projection with $\phi = 45^\circ$.

**Solution**:
Projection formulas:
$$x_p = x + z \cdot L\cos\phi, \quad y_p = y + z \cdot L\sin\phi$$
For $\phi = 45^\circ$: $\cos 45^\circ = \sin 45^\circ = \frac{1}{\sqrt{2}} \approx 0.7071$.

**Part (a): Cavalier Projection ($L = 1.0$)**:
$$x_p = 1 + 1(1.0)(0.7071) = 1 + 0.7071 = 1.7071$$
$$y_p = 1 + 1(1.0)(0.7071) = 1 + 0.7071 = 1.7071$$
Projected coordinates: $P_{\text{cav}}'(1.7071, 1.7071)$.

**Part (b): Cabinet Projection ($L = 0.5$)**:
$$x_p = 1 + 1(0.5)(0.7071) = 1 + 0.3536 = 1.3536$$
$$y_p = 1 + 1(0.5)(0.7071) = 1 + 0.3536 = 1.3536$$
Projected coordinates: $P_{\text{cab}}'(1.3536, 1.3536)$.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [Dec 2020 Q17b / Dec 2019 Q17b / Dec 2018 Q19b / Jan 2023 / Sep 2020 — 6 Marks]
**Question**:
Derive the transformation matrix for perspective projection with the projection reference point at position $z_{\text{prp}}$ along the $z_v$ axis and the view plane at $z_{\text{vp}}$. Write the perspective transformation equations:
(i) if the view plane is taken to be the uv-plane ($z_{\text{vp}} = 0$).
(ii) if the projection reference point is taken to be at the viewing coordinate origin ($z_{\text{prp}} = 0$).

**Solution**:

Let the viewing coordinate system have the Projection Reference Point (PRP) at $(0, 0, z_{\text{prp}})$ and the view plane at $z = z_{\text{vp}}$.

```
                     Similar Triangles in XZ Plane
                     
                     (0, 0, Zprp)
                          *
                          │\
                          │ \
                          │  \
                          │   \
            (0, 0, Zvp) ──┼────* (xp, Zvp)
                          │    │ \
                          │    │  \
                          │    │   \
                          │    │    \
             (0, 0, z) ───┴────┴─────* (x, z)
```

**Geometric Derivation**:
Using the principle of similar triangles in the $XZ$ plane:
$$\frac{x_p}{x} = \frac{z_{\text{vp}} - z_{\text{prp}}}{z - z_{\text{prp}}} \implies x_p = x \cdot \left[ \frac{z_{\text{vp}} - z_{\text{prp}}}{z - z_{\text{prp}}} \right]$$

Similarly, in the $YZ$ plane:
$$\frac{y_p}{y} = \frac{z_{\text{vp}} - z_{\text{prp}}}{z - z_{\text{prp}}} \implies y_p = y \cdot \left[ \frac{z_{\text{vp}} - z_{\text{prp}}}{z - z_{\text{prp}}} \right]$$

Let $d_p = z_{\text{vp}} - z_{\text{prp}}$ be the distance from PRP to the view plane:
$$x_p = \frac{x \cdot d_p}{z - z_{\text{prp}}}, \quad y_p = \frac{y \cdot d_p}{z - z_{\text{prp}}}, \quad z_p = z_{\text{vp}}$$

---

#### Case (i): View Plane at UV-Plane ($z_{\text{vp}} = 0$)
Substituting $z_{\text{vp}} = 0 \implies d_p = -z_{\text{prp}}$:
$$x_p = \frac{x(-z_{\text{prp}})}{z - z_{\text{prp}}} = \frac{x}{1 - z/z_{\text{prp}}}$$
$$y_p = \frac{y(-z_{\text{prp}})}{z - z_{\text{prp}}} = \frac{y}{1 - z/z_{\text{prp}}}$$
$$z_p = 0$$

In $4 \times 4$ homogeneous matrix notation:
$$\begin{bmatrix} X_h \\ Y_h \\ Z_h \\ w \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & -1/z_{\text{prp}} & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} = \begin{bmatrix} x \\ y \\ 0 \\ 1 - z/z_{\text{prp}} \end{bmatrix}$$
After perspective division by $w = 1 - z/z_{\text{prp}}$:
$$x_p = \frac{x}{1 - z/z_{\text{prp}}}, \quad y_p = \frac{y}{1 - z/z_{\text{prp}}}, \quad z_p = 0$$

---

#### Case (ii): Projection Reference Point at Origin ($z_{\text{prp}} = 0$)
Substituting $z_{\text{prp}} = 0$ with view plane at distance $z_{\text{vp}} = d$:
$$x_p = \frac{x \cdot d}{z} = \frac{x}{z/d}$$
$$y_p = \frac{y \cdot d}{z} = \frac{y}{z/d}$$
$$z_p = d$$

In $4 \times 4$ homogeneous matrix notation:
$$\mathbf{M}_{\text{persp}} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 1/d & 0 \end{bmatrix}$$
Multiplying by $\begin{bmatrix} x & y & z & 1 \end{bmatrix}^T$ yields $\begin{bmatrix} x & y & z & z/d \end{bmatrix}^T$.
Perspective division by $w = z/d$ gives:
$$P_p = \begin{bmatrix} x \cdot d / z \\ y \cdot d / z \\ d \\ 1 \end{bmatrix}$$

---

### Question 2 [Dec 2020 Q19a / May 2019 Q19a — 6 Marks]
**Question**:
Derive the transformation matrix for oblique parallel projection.

**Solution**:

In an **Oblique Parallel Projection**, projectors intersect the projection plane at an arbitrary angle $\alpha \ne 90^\circ$.

Let the projection plane be the $xy$-plane ($z = 0$).
Let $P(x, y, z)$ be an arbitrary 3D point and $P_p(x_p, y_p, 0)$ be its oblique projection on the $xy$-plane.

```
                       Z
                       ▲
                       │     Projector Line
                       │    /
                       │   /  Angle alpha with plane
                       │  /
                       │ /
                       └──────────────────► X
                       │\
                       │ \ Projected line segment of
                       │  \ length L*z at angle phi
                       ▼
                       Y
```

**Geometric Derivation**:
- Let $\alpha$ be the angle between the projector and the projection plane.
- Let $\phi$ be the angle between the projected segment and the positive X-axis on the projection plane.
- A line segment of unit length along the Z-axis projects to a line of length $L$ on the projection plane:
  $$L = \cot\alpha = \frac{1}{\tan\alpha}$$
- For a point at coordinate $z$, the projected length along the plane is $z \cdot L$.
- Resolving this displacement along the $X$ and $Y$ Cartesian axes:
  $$\Delta x = z \cdot L \cos\phi$$
  $$\Delta y = z \cdot L \sin\phi$$
- Therefore, the projected coordinates are:
  $$x_p = x + z \cdot L\cos\phi$$
  $$y_p = y + z \cdot L\sin\phi$$
  $$z_p = 0$$

**Matrix Formulation**:
Expressing in $4 \times 4$ homogeneous coordinate form:
$$\begin{bmatrix} x_p \\ y_p \\ z_p \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & L\cos\phi & 0 \\ 0 & 1 & L\sin\phi & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$

**Special Cases**:
1. **Cavalier Projection ($\alpha = 45^\circ \implies L = 1$)**:
   $$\mathbf{M}_{\text{cav}} = \begin{bmatrix} 1 & 0 & \cos\phi & 0 \\ 0 & 1 & \sin\phi & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
2. **Cabinet Projection ($\alpha = 63.43^\circ \implies L = 0.5$)**:
   $$\mathbf{M}_{\text{cab}} = \begin{bmatrix} 1 & 0 & 0.5\cos\phi & 0 \\ 0 & 1 & 0.5\sin\phi & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

---

### Question 3 [Dec 2021 Q17b / Dec 2019 Q18b — 4 Marks]
**Question**:
Distinguish between Cavalier and Cabinet projections.

**Solution**:

| Dimension | Cavalier Projection | Cabinet Projection |
|---|---|---|
| **Angle with Projection Plane ($\alpha$)** | $\alpha = 45^\circ$ | $\alpha = \arctan(2) \approx 63.43^\circ$ |
| **Length Factor ($L = \cot\alpha$)** | $L = \frac{1}{\tan 45^\circ} = 1.0$ | $L = \frac{1}{\tan 63.43^\circ} = 0.5$ |
| **Depth Foreshortening Ratio** | **$100\%$ (Full true length)**. Lines perpendicular to the view plane are drawn at their exact true measurement scale. | **$50\%$ (Half true length)**. Lines perpendicular to the view plane are drawn at half their actual physical length. |
| **Visual Realism** | Appears unnaturally stretched and elongated along the depth dimension. | **Significantly more realistic**. Accurately mimics human depth perception for oblique views. |
| **Transformation Equations ($\phi = 45^\circ$)** | $x_p = x + z\cos 45^\circ = x + \frac{z}{\sqrt{2}}$<br>$y_p = y + z\sin 45^\circ = y + \frac{z}{\sqrt{2}}$ | $x_p = x + 0.5z\cos 45^\circ = x + \frac{z}{2\sqrt{2}}$<br>$y_p = y + 0.5z\sin 45^\circ = y + \frac{z}{2\sqrt{2}}$ |

---

### Question 4 [June 2024 Q7 / June 2022 Q7 / May 2019 Q9 — 4 Marks]
**Question**:
Illustrate the concept of Vanishing Point in perspective projection.

**Solution**:

A **Vanishing Point (VP)** is the point on the projection plane where the perspective projections of a family of mutually parallel 3D lines appear to intersect.

```
                          VANISHING POINT ILLUSTRATION
                          
                                    Horizon Line
                 \                       │                       /
                  \                      │                      /
                   \                     ▼                     /
                    \             Vanishing Point             /
                     \                   *                   /
                      \                 / \                 /
                       \               /   \               /
                        \             /     \             /
                         \           /       \           /
                          \         /  Road   \         /
                           \       /  Tracks   \       /
```

**Geometric Principles**:
1. In reality, parallel lines in 3D Euclidean space never intersect.
2. In perspective projection, distant segments undergo perspective division by depth $z$:
   $$x_p = \frac{x \cdot d}{z}, \quad y_p = \frac{y \cdot d}{z}$$
   As $z \to \infty$, the distance between two parallel lines approaches zero, causing their projections to converge at a single spatial point on the projection plane.
3. **Number of Principal Vanishing Points**:
   Classified by how many principal coordinate axes ($X, Y, Z$) intersect the projection plane:
   - **One-Point Perspective**: Projection plane is parallel to two axes (e.g., looking down railway tracks). All lines parallel to the depth axis converge to a single central vanishing point.
   - **Two-Point Perspective**: Projection plane is parallel to one axis (e.g., viewing the corner of a building). Horizontal lines converge to two vanishing points (left and right on the horizon).
   - **Three-Point Perspective**: Projection plane is tilted relative to all three axes (e.g., looking up at a skyscraper). Produces three vanishing points (left, right, and top/bottom).
