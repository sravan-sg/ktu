# Windowing Concepts & Window-to-Viewport Transformation

## 1. Explanation
In computer graphics, an application's geometric scene is modeled in its own natural measurement units (e.g. meters, light-years, or micrometers), which are completely independent of any physical display monitor. The viewing pipeline bridges this gap by mapping a selected subregion of the continuous virtual world onto a dedicated rectangular display area on physical hardware.

---

### Key Terminology & Coordinate Systems

1. **World Coordinate System (WCS)**:
   - The user's application-defined Cartesian coordinate frame in which all objects, terrain, and geometry are modeled using natural units.
2. **Viewing Coordinates (VCS)**:
   - A coordinate system anchored to a virtual camera/observer positioned in the world space.
3. **Window (Clipping Window / World Window)**:
   - A rectangular region defined in the world coordinate system specifying **what** part of the virtual world is to be viewed.
   - Bounded by four coordinates: $[x_{w\min}, x_{w\max}]$ along the horizontal axis, and $[y_{w\min}, y_{w\max}]$ along the vertical axis.
4. **Viewport**:
   - A rectangular display area on the physical output device (or normalized device space) specifying **where** the contents of the window are to be displayed.
   - Bounded by coordinates: $[x_{v\min}, x_{v\max}]$ and $[y_{v\min}, y_{v\max}]$.
5. **Window-to-Viewport Transformation (Viewing Transformation)**:
   - The geometric mapping that scales and translates points from the world window into the display viewport.

---

### Derivation of Window-to-Viewport Mapping Equations
Let point $P_w(x_w, y_w)$ be an arbitrary point inside the world window. We want to find its corresponding location $P_v(x_v, y_v)$ inside the viewport such that relative spatial proportions are strictly preserved.

#### Proportion Invariance Principle
The relative horizontal position of $x_w$ within the window must equal the relative horizontal position of $x_v$ within the viewport:
$$\frac{x_w - x_{w\min}}{x_{w\max} - x_{w\min}} = \frac{x_v - x_{v\min}}{x_{v\max} - x_{v\min}}$$

Similarly, along the vertical dimension:
$$\frac{y_w - y_{w\min}}{y_{w\max} - y_{w\min}} = \frac{y_v - y_{v\min}}{y_{v\max} - y_{v\min}}$$

#### Solving for Viewport Coordinates $(x_v, y_v)$:
$$x_v = x_{v\min} + (x_w - x_{w\min}) \cdot \left(\frac{x_{v\max} - x_{v\min}}{x_{w\max} - x_{w\min}}\right)$$
$$y_v = y_{v\min} + (y_w - y_{w\min}) \cdot \left(\frac{y_{v\max} - y_{v\min}}{y_{w\max} - y_{w\min}}\right)$$

Define the **scaling factors**:
$$s_x = \frac{x_{v\max} - x_{v\min}}{x_{w\max} - x_{w\min}} = \frac{\Delta x_v}{\Delta x_w}$$
$$s_y = \frac{y_{v\max} - y_{v\min}}{y_{w\max} - y_{w\min}} = \frac{\Delta y_v}{\Delta y_w}$$

Then the equations simplify to:
$$x_v = x_{v\min} + (x_w - x_{w\min}) \cdot s_x = s_x \cdot x_w + (x_{v\min} - s_x \cdot x_{w\min})$$
$$y_v = y_{v\min} + (y_w - y_{w\min}) \cdot s_y = s_y \cdot y_w + (y_{v\min} - s_y \cdot y_{w\min})$$

---

### Matrix Formulation of the Viewing Transformation
The window-to-viewport transformation is a composite affine transformation composed of three elementary stages:
1. Translate the lower-left corner of the window $(x_{w\min}, y_{w\min})$ to the coordinate origin:
   $$\mathbf{T}(-x_{w\min}, -y_{w\min}) = \begin{bmatrix} 1 & 0 & -x_{w\min} \\ 0 & 1 & -y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$$
2. Scale the window dimensions to match the viewport dimensions using scaling factors $s_x$ and $s_y$:
   $$\mathbf{S}(s_x, s_y) = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
3. Translate the origin to the lower-left corner of the viewport $(x_{v\min}, y_{v\min})$:
   $$\mathbf{T}(x_{v\min}, y_{v\min}) = \begin{bmatrix} 1 & 0 & x_{v\min} \\ 0 & 1 & y_{v\min} \\ 0 & 0 & 1 \end{bmatrix}$$

Multiplying the three matrices yields the composite Viewing Transformation Matrix $\mathbf{M}_{\text{view}}$:
$$\mathbf{M}_{\text{view}} = \mathbf{T}(x_{v\min}, y_{v\min}) \cdot \mathbf{S}(s_x, s_y) \cdot \mathbf{T}(-x_{w\min}, -y_{w\min})$$

$$\mathbf{M}_{\text{view}} = \begin{bmatrix} s_x & 0 & x_{v\min} - s_x \cdot x_{w\min} \\ 0 & s_y & y_{v\min} - s_y \cdot y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$$

---

### Aspect Ratio Preservation & Distortion
- If $s_x = s_y$, the aspect ratio of the window is preserved in the viewport, ensuring circles remain circular and squares remain square.
- If $s_x \ne s_y$, differential scaling occurs, causing geometric distortion (stretching or squashing of shapes).

---

## 2. Example: Window-to-Viewport Transformation Diagram
```
WORLD COORDINATE SYSTEM (WCS)                    DISPLAY SCREEN / DEVICE
y_w                                              y_v
 ▲                                                ▲
 │      +-----------------+ (x_wmax, y_wmax)      │          +----------+ (x_vmax, y_vmax)
 │      |                 |                       │          |          |
 │      |     * P_w       |                       │          |   * P_v  |
 │      |                 |     ===============>  │          |          |
 │      +-----------------+                       │          +----------+
 │   (x_wmin, y_wmin)                             │      (x_vmin, y_vmin)
 └─────────────────────────► x_w                  └─────────────────────► x_v
          WINDOW                                          VIEWPORT
    (What is to be seen)                            (Where it is displayed)
```

---

## 3. Applications & Use Cases
1. **Interactive Zooming and Panning (Google Maps, CAD)**: Panning moves the window boundaries $(x_{w\min}, y_{w\min})$ across the world coordinates. Zooming in shrinks the world window dimensions while keeping the screen viewport fixed, enlarging scene details.
2. **Multi-View Architectural CAD Viewports**: Software like Blender, Maya, and AutoCAD simultaneously displays four split viewports on a single monitor (Top, Front, Side, Perspective), each mapping different 3D camera windows to separate screen regions.
3. **Split-Screen Multiplayer Video Games**: The physical screen is partitioned into two or four distinct viewports, each rendering a separate player's viewpoint independently.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Window-to-Viewport Point Transformation [KTU May 2019 / June 2024 - 4 Marks]
**Problem**:
A clipping window in world coordinates is bounded by $(x_{w\min}, y_{w\min}) = (20, 20)$ and $(x_{w\max}, y_{w\max}) = (80, 80)$.
The display viewport is defined by $(x_{v\min}, y_{v\min}) = (100, 100)$ and $(x_{v\max}, y_{v\max}) = (400, 400)$.
Find the viewport coordinates for the world point $P_w(35, 65)$.

**Step-by-step Solution**:
1. **Compute Window and Viewport Dimensions**:
   $$\Delta x_w = 80 - 20 = 60, \quad \Delta y_w = 80 - 20 = 60$$
   $$\Delta x_v = 400 - 100 = 300, \quad \Delta y_v = 400 - 100 = 300$$
2. **Compute Scaling Factors**:
   $$s_x = \frac{\Delta x_v}{\Delta x_w} = \frac{300}{60} = 5$$
   $$s_y = \frac{\Delta y_v}{\Delta y_w} = \frac{300}{60} = 5$$
   *(Since $s_x = s_y = 5$, aspect ratio is strictly preserved).*
3. **Compute Viewport Coordinates**:
   $$x_v = x_{v\min} + (x_w - x_{w\min}) \cdot s_x = 100 + (35 - 20) \times 5 = 100 + 15 \times 5 = 100 + 75 = 175$$
   $$y_v = y_{v\min} + (y_w - y_{w\min}) \cdot s_y = 100 + (65 - 20) \times 5 = 100 + 45 \times 5 = 100 + 225 = 325$$
4. **Final Coordinate**: The point maps to $\mathbf{P_v(175, 325)}$.

---

### Example 2: Distortion Analysis with Non-Uniform Scaling [KTU Dec 2021 Pattern]
**Problem**:
A circle with center $(50, 50)$ and radius $r = 10$ is defined in a world window $[0, 100] \times [0, 100]$.
It is mapped to a widescreen viewport $[0, 400] \times [0, 200]$.
Determine the geometric shape and equation of the mapped object in viewport coordinates.

**Step-by-step Solution**:
1. **Scaling Factors**:
   $$s_x = \frac{400 - 0}{100 - 0} = 4, \quad s_y = \frac{200 - 0}{100 - 0} = 2$$
2. **Mapped Center**:
   $$x_{vc} = 0 + (50 - 0) \times 4 = 200$$
   $$y_{vc} = 0 + (50 - 0) \times 2 = 100$$
3. **Mapped Radii**:
   $$r_x = r \times s_x = 10 \times 4 = 40$$
   $$r_y = r \times s_y = 10 \times 2 = 20$$
4. **Geometric Shape**:
   Because $s_x \ne s_y$, the circle is distorted into an **ellipse** with semi-major axis $a = 40$ along $X$ and semi-minor axis $b = 20$ along $Y$:
   $$\frac{(x_v - 200)^2}{40^2} + \frac{(y_v - 100)^2}{20^2} = 1$$

---

### Example 3: Construction of the Viewing Matrix $\mathbf{M}_{\text{view}}$ [KTU Analytical Pattern]
**Problem**:
Construct the explicit $3 \times 3$ viewing transformation matrix $\mathbf{M}_{\text{view}}$ for a window $[-10, 10] \times [-10, 10]$ mapped onto a normalized viewport $[0, 1] \times [0, 1]$.

**Step-by-step Solution**:
1. **Window and Viewport Extents**:
   $$x_{w\min} = -10, \ x_{w\max} = 10 \implies \Delta x_w = 20$$
   $$y_{w\min} = -10, \ y_{w\max} = 10 \implies \Delta y_w = 20$$
   $$x_{v\min} = 0, \ x_{v\max} = 1 \implies \Delta x_v = 1$$
   $$y_{v\min} = 0, \ y_{v\max} = 1 \implies \Delta y_v = 1$$
2. **Scaling Factors**:
   $$s_x = \frac{1}{20} = 0.05, \quad s_y = \frac{1}{20} = 0.05$$
3. **Translation Offsets**:
   $$t_{xv} = x_{v\min} - s_x \cdot x_{w\min} = 0 - (0.05 \times -10) = +0.5$$
   $$t_{yv} = y_{v\min} - s_y \cdot y_{w\min} = 0 - (0.05 \times -10) = +0.5$$
4. **Resulting Matrix**:
   $$\mathbf{M}_{\text{view}} = \begin{bmatrix} 0.05 & 0 & 0.5 \\ 0 & 0.05 & 0.5 \\ 0 & 0 & 1 \end{bmatrix}$$

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / June 2022 - 4 Marks]
**Question**:
Define the terms window, viewport and windowing transformation in the context of 2D viewing with suitable diagrams.

**Solution**:
1. **Definitions**:
   - **Window (World Window)**: A rectangular region specified in world coordinates (WCS) that defines the exact portion of the modeled graphical scene selected for viewing. It answers the question *"What is to be displayed?"*
   - **Viewport**: A rectangular area on a display device (or normalized device screen) where the contents of the clipping window are rendered. It answers the question *"Where is the image to be displayed?"*
   - **Windowing Transformation (Viewing Transformation)**: The mathematical mapping that maps geometric primitives from the world coordinate window into the display device viewport, scaling and translating the coordinates appropriately while maintaining relative spatial relationships.
2. **Diagram**:
```
   World Coordinates (WCS)                        Device Coordinates (DCS)
   +-----------------------+                      +-----------------------+
   |                       |                      |                       |
   |     +-----------+     |                      |       +-------+       |
   |     |  WINDOW   |     |   === Mapping ===>   |       |VIEWPORT       |
   |     |           |     |                      |       |       |       |
   |     +-----------+     |                      |       +-------+       |
   |                       |                      |                       |
   +-----------------------+                      +-----------------------+
```

---

### Question 2 [KTU December 2023 / June 2024 - 5 Marks]
**Question**:
Derive the window-to-viewport transformation equations and express them in matrix notation using homogeneous coordinates.

**Solution**:
1. **Derivation**:
   Let $(x_w, y_w)$ be a point in the world window $[x_{w\min}, x_{w\max}] \times [y_{w\min}, y_{w\max}]$.
   Let $(x_v, y_v)$ be the corresponding point in the viewport $[x_{v\min}, x_{v\max}] \times [y_{v\min}, y_{v\max}]$.
   To preserve the relative position of the point:
   $$\frac{x_v - x_{v\min}}{x_{v\max} - x_{v\min}} = \frac{x_w - x_{w\min}}{x_{w\max} - x_{w\min}}$$
   $$\frac{y_v - y_{v\min}}{y_{v\max} - y_{v\min}} = \frac{y_w - y_{w\min}}{y_{w\max} - y_{w\min}}$$
   Solving for $(x_v, y_v)$:
   $$x_v = s_x \cdot x_w + (x_{v\min} - s_x \cdot x_{w\min})$$
   $$y_v = s_y \cdot y_w + (y_{v\min} - s_y \cdot y_{w\min})$$
   where $s_x = \frac{x_{v\max} - x_{v\min}}{x_{w\max} - x_{w\min}}$ and $s_y = \frac{y_{v\max} - y_{v\min}}{y_{w\max} - y_{w\min}}$.
2. **Homogeneous Matrix Formulation**:
   The transformation corresponds to translating window origin to $(0,0)$, scaling by $(s_x, s_y)$, and translating to viewport origin $(x_{v\min}, y_{v\min})$:
   $$\mathbf{M}_{\text{view}} = \mathbf{T}(x_{v\min}, y_{v\min}) \cdot \mathbf{S}(s_x, s_y) \cdot \mathbf{T}(-x_{w\min}, -y_{w\min})$$
   $$\begin{bmatrix} x_v \\ y_v \\ 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & x_{v\min} - s_x \cdot x_{w\min} \\ 0 & s_y & y_{v\min} - s_y \cdot y_{w\min} \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_w \\ y_w \\ 1 \end{bmatrix}$$

