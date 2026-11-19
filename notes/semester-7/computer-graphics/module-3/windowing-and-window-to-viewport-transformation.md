# Windowing Concepts & Window-to-Viewport Transformation

## 1. Explanation

In computer graphics applications, synthetic geometric models, maps, terrain simulations, and engineering CAD assemblies are created in their own natural, continuous measurement units (such as meters, angstroms, light-years, or feet). These real-world units are completely independent of any physical display hardware. 

The **2D Viewing Pipeline** establishes the algorithmic bridge between continuous world-coordinate models and the discrete pixel coordinate space of a physical monitor.

---

### The 2D Viewing Pipeline

The progression of coordinate transformations that carries geometry from initial object-space definitions to final rendered display pixels consists of the following sequential stages:

```
┌──────────────────────────────────────────────┐
│          MODEL COORDINATES (MC)              │  Local object coordinate frame
│   (Object designed around its own origin)    │  (e.g., car wheel centered at 0,0)
└──────────────────────┬───────────────────────┘
                       │ Modeling Transformation (Scale, Rotate, Translate)
                       ▼
┌──────────────────────────────────────────────┐
│          WORLD COORDINATES (WC)              │  Assembled virtual environment
│   (Multiple objects placed in global scene)  │  Measured in application units (meters)
└──────────────────────┬───────────────────────┘
                       │ Viewing Transformation / Window Definition
                       ▼
┌──────────────────────────────────────────────┐
│         VIEWING COORDINATES (VC)             │  Camera-centric space
│  (Scene oriented relative to virtual observer)
└──────────────────────┬───────────────────────┘
                       │ Normalization & Clipping against Window Margins
                       ▼
┌──────────────────────────────────────────────┐
│  NORMALIZED DEVICE COORDINATES (NDC)         │  Hardware-independent normalized space
│        ([-1, 1]² or [0, 1]² square)          │  Enables portable graphics libraries
└──────────────────────┬───────────────────────┘
                       │ Viewport Transformation (Device Mapping)
                       ▼
┌──────────────────────────────────────────────┐
│         DEVICE COORDINATES (DC)              │  Screen space: raster pixel addresses
│      (Integer grid: 0 to H-1, 0 to V-1)      │  Mapped directly to Frame Buffer memory
└──────────────────────────────────────────────┘
```

---

### Fundamental Definitions: Window vs. Viewport

Two fundamental spatial constructs govern the viewing process:

```
      WORLD COORDINATE SYSTEM                         DEVICE COORDINATE SYSTEM
                 Y                                                Y
                 ▲                                                ▲
                 │                                                │
                 │      (ywmax) ┌───────────────┐                 │        (yvmax) ┌─────────────┐
                 │              │               │                 │                │             │
                 │              │  CLIP WINDOW  │                 │                │  VIEWPORT   │
                 │              │ (What to see) │ ──────────────► │                │(Where to see│
                 │              │               │    Viewing      │                │  on screen) │
                 │      (ywmin) └───────────────┘  Transformation │        (yvmin) └─────────────┘
                 │              (xwmin)   (xwmax)                 │                (xvmin) (xvmax)
                 └──────────────────────────────► X               └──────────────────────────────► X
```

1. **Window (World Window / Clipping Window)**:
   - Defined in the **World Coordinate System**.
   - Specifies **WHAT** part of the virtual scene is to be captured and viewed by the observer.
   - A rectangular region bounded by four boundary lines:
     $$\text{Horizontal bounds: } [x_{w\min}, \ x_{w\max}]$$
     $$\text{Vertical bounds: } [y_{w\min}, \ y_{w\max}]$$
   - Scene primitives lying outside this boundary are culled by clipping algorithms.

2. **Viewport**:
   - Defined in the **Normalized Device Coordinate** or physical **Device Coordinate System**.
   - Specifies **WHERE** on the display screen the contents of the window are to be presented.
   - A rectangular sub-region on the monitor bounded by:
     $$\text{Horizontal bounds: } [x_{v\min}, \ x_{v\max}]$$
     $$\text{Vertical bounds: } [y_{v\min}, \ y_{v\max}]$$
   - By sizing and positioning multiple viewports, a single display screen can show split-screen views (e.g., top, front, side, and isometric views in CAD tools; or rear-view mirrors in racing simulators).

---

### Mathematical Derivation of Window-to-Viewport Transformation

Let $P_w(x_w, y_w)$ be an arbitrary point situated within the clipping window. We seek to derive the mathematical equations that map this point to a corresponding location $P_v(x_v, y_v)$ inside the display viewport such that **relative spatial proportions are strictly invariant**.

#### 1. The Proportion Invariance Principle
The fractional distance of $x_w$ relative to the window's horizontal span must equal the fractional distance of $x_v$ relative to the viewport's horizontal span:
$$\frac{x_w - x_{w\min}}{x_{w\max} - x_{w\min}} = \frac{x_v - x_{v\min}}{x_{v\max} - x_{v\min}}$$

Similarly, along the vertical coordinate axis:
$$\frac{y_w - y_{w\min}}{y_{w\max} - y_{w\min}} = \frac{y_v - y_{v\min}}{y_{v\max} - y_{v\min}}$$

#### 2. Algebraic Solution for Viewport Coordinates $(x_v, y_v)$
Solving the horizontal proportion for $x_v$:
$$x_v - x_{v\min} = (x_w - x_{w\min}) \cdot \left[ \frac{x_{v\max} - x_{v\min}}{x_{w\max} - x_{w\min}} \right]$$
$$x_v = x_{v\min} + (x_w - x_{w\min}) \cdot s_x$$

Solving the vertical proportion for $y_v$:
$$y_v - y_{v\min} = (y_w - y_{w\min}) \cdot \left[ \frac{y_{v\max} - y_{v\min}}{y_{w\max} - y_{w\min}} \right]$$
$$y_v = y_{v\min} + (y_w - y_{w\min}) \cdot s_y$$

where $s_x$ and $s_y$ denote the **horizontal and vertical scaling factors**:
$$s_x = \frac{x_{v\max} - x_{v\min}}{x_{w\max} - x_{w\min}} = \frac{\Delta x_v}{\Delta x_w}$$
$$s_y = \frac{y_{v\max} - y_{v\min}}{y_{w\max} - y_{w\min}} = \frac{\Delta y_v}{\Delta y_w}$$

Rearranging into standard linear slope-intercept form ($y = mx + c$):
$$x_v = s_x \cdot x_w + (x_{v\min} - s_x \cdot x_{w\min})$$
$$y_v = s_y \cdot y_w + (y_{v\min} - s_y \cdot y_{w\min})$$

---

### Matrix Formulation: Composition of Elementary Transformations

The window-to-viewport transformation can be deconstructed into a sequence of three elementary affine geometric operations:

1. **Step 1: Translate the window origin to the coordinate origin**:
   Displace the lower-left corner of the window $(x_{w\min}, y_{w\min})$ to $(0, 0)$:
   $$\mathbf{T}_1 = \mathbf{T}(-x_{w\min}, -y_{w\min}) = \begin{bmatrix} 1 & 0 & -x_{w\min} \\ 0 & 1 & -y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$$

2. **Step 2: Scale the window dimensions to match the viewport dimensions**:
   Apply non-uniform scaling using scaling factors $s_x$ and $s_y$:
   $$\mathbf{S} = \mathbf{S}(s_x, s_y) = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

3. **Step 3: Translate the scaled origin to the lower-left corner of the viewport**:
   Translate $(0, 0)$ to the viewport minimum coordinate $(x_{v\min}, y_{v\min})$:
   $$\mathbf{T}_2 = \mathbf{T}(x_{v\min}, y_{v\min}) = \begin{bmatrix} 1 & 0 & x_{v\min} \\ 0 & 1 & y_{v\min} \\ 0 & 0 & 1 \end{bmatrix}$$

#### Concatenation of the Composite Viewing Matrix
The composite transformation matrix $\mathbf{M}_{\text{view}}$ is obtained by multiplying the three matrices in order:
$$\mathbf{M}_{\text{view}} = \mathbf{T}_2 \cdot \mathbf{S} \cdot \mathbf{T}_1 = \mathbf{T}(x_{v\min}, y_{v\min}) \cdot \mathbf{S}(s_x, s_y) \cdot \mathbf{T}(-x_{w\min}, -y_{w\min})$$

Evaluating the product:
$$\mathbf{S} \cdot \mathbf{T}_1 = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -x_{w\min} \\ 0 & 1 & -y_{w\min} \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & -s_x \cdot x_{w\min} \\ 0 & s_y & -s_y \cdot y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$$

Multiplying by $\mathbf{T}_2$:
$$\mathbf{M}_{\text{view}} = \begin{bmatrix} 1 & 0 & x_{v\min} \\ 0 & 1 & y_{v\min} \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} s_x & 0 & -s_x \cdot x_{w\min} \\ 0 & s_y & -s_y \cdot y_{w\min} \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & x_{v\min} - s_x \cdot x_{w\min} \\ 0 & s_y & y_{v\min} - s_y \cdot y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$$

Applying $\mathbf{M}_{\text{view}}$ to a point $P_w(x_w, y_w, 1)$:
$$\begin{bmatrix} x_v \\ y_v \\ 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & x_{v\min} - s_x \cdot x_{w\min} \\ 0 & s_y & y_{v\min} - s_y \cdot y_{w\min} \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_w \\ y_w \\ 1 \end{bmatrix} = \begin{bmatrix} s_x \cdot x_w + (x_{v\min} - s_x \cdot x_{w\min}) \\ s_y \cdot y_w + (y_{v\min} - s_y \cdot y_{w\min}) \\ 1 \end{bmatrix}$$
This exactly matches the derived proportion invariance equations.

---

### Aspect Ratio Considerations & Geometric Distortion

The **Aspect Ratio** of a rectangular area is defined as the ratio of its width to its height:
$$\text{AR}_{\text{window}} = \frac{x_{w\max} - x_{w\min}}{y_{w\max} - y_{w\min}} = \frac{\Delta x_w}{\Delta y_w}$$
$$\text{AR}_{\text{viewport}} = \frac{x_{v\max} - x_{v\min}}{y_{v\max} - y_{v\min}} = \frac{\Delta x_v}{\Delta y_v}$$

The relationship between the scaling factors is:
$$\frac{s_x}{s_y} = \frac{\Delta x_v / \Delta x_w}{\Delta y_v / \Delta y_w} = \frac{\Delta x_v / \Delta y_v}{\Delta x_w / \Delta y_w} = \frac{\text{AR}_{\text{viewport}}}{\text{AR}_{\text{window}}}$$

#### Cases of Aspect Ratio Mapping:
1. **Equal Aspect Ratios ($\text{AR}_{\text{viewport}} = \text{AR}_{\text{window}} \iff s_x = s_y$)**:
   - Uniform scaling occurs.
   - Geometric shapes retain their true proportions: circles remain perfect circles, squares remain squares, angles between intersecting lines are preserved.
2. **Unequal Aspect Ratios ($\text{AR}_{\text{viewport}} \ne \text{AR}_{\text{window}} \iff s_x \ne s_y$)**:
   - Non-uniform scaling (differential distortion).
   - Circles are stretched or squished into ellipses; squares become rectangles.
   - To prevent distortion, graphics systems apply **letterboxing** (adding black bars above and below) or **pillarboxing** (adding vertical bars on left and right) by forcing $s = \min(s_x, s_y)$ and centering the viewport.

---

## 2. Example: Step-by-Step Numerical Mapping

Let a world window be defined with coordinates:
$$x_{w\min} = 20, \quad x_{w\max} = 80, \quad y_{w\min} = 10, \quad y_{w\max} = 50$$
Let the display viewport have pixel coordinates:
$$x_{v\min} = 100, \quad x_{v\max} = 400, \quad y_{v\min} = 100, \quad y_{v\max} = 300$$

**Step 1: Compute Window and Viewport Spans**:
$$\Delta x_w = 80 - 20 = 60, \quad \Delta y_w = 50 - 10 = 40$$
$$\Delta x_v = 400 - 100 = 300, \quad \Delta y_v = 300 - 100 = 200$$

**Step 2: Compute Aspect Ratios**:
$$\text{AR}_{\text{window}} = \frac{60}{40} = 1.5, \quad \text{AR}_{\text{viewport}} = \frac{300}{200} = 1.5$$
Because $\text{AR}_{\text{window}} = \text{AR}_{\text{viewport}}$, scaling is uniform and there is zero geometric distortion.

**Step 3: Compute Scaling Factors**:
$$s_x = \frac{\Delta x_v}{\Delta x_w} = \frac{300}{60} = 5.0, \quad s_y = \frac{\Delta y_v}{\Delta y_w} = \frac{200}{40} = 5.0$$

**Step 4: Formulate the Composite Transformation Matrix**:
$$x_{\text{trans}} = x_{v\min} - s_x \cdot x_{w\min} = 100 - (5.0 \times 20) = 100 - 100 = 0$$
$$y_{\text{trans}} = y_{v\min} - s_y \cdot y_{w\min} = 100 - (5.0 \times 10) = 100 - 50 = 50$$

$$\mathbf{M}_{\text{view}} = \begin{bmatrix} 5.0 & 0 & 0 \\ 0 & 5.0 & 50 \\ 0 & 0 & 1 \end{bmatrix}$$

**Step 5: Transform World Point $P_w(35, 25)$**:
$$x_v = 5.0(35) + 0 = 175$$
$$y_v = 5.0(25) + 50 = 125 + 50 = 175$$
Point $P_w(35, 25)$ maps to viewport pixel $(175, 175)$.

---

## 3. Applications & Use Cases

1. **CAD Multiview Viewports (AutoCAD / Blender)**:
   A single high-resolution monitor screen ($1920 \times 1080$) is partitioned into four non-overlapping viewports:
   - Viewport 1 (Top-Left): Top View ($XZ$-plane)
   - Viewport 2 (Top-Right): Front View ($XY$-plane)
   - Viewport 3 (Bottom-Left): Side View ($YZ$-plane)
   - Viewport 4 (Bottom-Right): 3D Perspective Orbit Camera
   Each viewport defines its own independent viewing matrix, enabling concurrent multi-angle editing.
2. **Geographic Information Systems (GIS / Google Maps)**:
   The world window represents latitude/longitude bounding boxes across continental scales. As users pan and zoom, the window coordinates dynamically adjust while the viewport coordinates remain fixed to the browser window, triggering continuous recalculation of $s_x, s_y$.
3. **Responsive UI & Aspect Ratio Letterboxing (Video Streaming)**:
   Video players (YouTube, Netflix) fit a $16:9$ aspect ratio video window into arbitrary monitor aspect ratios ($16:10$, $21:9$ ultrawide, or mobile vertical screens) using aspect-ratio preserving viewport transformations that automatically generate black border padding.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Viewport Mapping with Line Segment Endpoints [KTU May 2019 / Jan 2023]
**Problem**:
A clipping window has corners at $(0, 0)$ and $(100, 100)$. A viewport has corners at $(10, 10)$ and $(60, 60)$. 
1. Determine the transformation equations.
2. Find the viewport coordinates of the line segment connecting $P_1(20, 40)$ and $P_2(80, 60)$.

**Solution**:
Window parameters: $x_{w\min} = 0, x_{w\max} = 100, y_{w\min} = 0, y_{w\max} = 100$.
Viewport parameters: $x_{v\min} = 10, x_{v\max} = 60, y_{v\min} = 10, y_{v\max} = 60$.

**Step 1: Scaling Factors**:
$$s_x = \frac{x_{v\max} - x_{v\min}}{x_{w\max} - x_{w\min}} = \frac{60 - 10}{100 - 0} = \frac{50}{100} = 0.5$$
$$s_y = \frac{y_{v\max} - y_{v\min}}{y_{w\max} - y_{w\min}} = \frac{60 - 10}{100 - 0} = \frac{50}{100} = 0.5$$

**Step 2: Mapping Equations**:
$$x_v = x_{v\min} + (x_w - x_{w\min}) \cdot s_x = 10 + (x_w - 0)(0.5) = 0.5 x_w + 10$$
$$y_v = y_{v\min} + (y_w - y_{w\min}) \cdot s_y = 10 + (y_w - 0)(0.5) = 0.5 y_w + 10$$

**Step 3: Transform Endpoints**:
- For $P_1(20, 40)$:
  $$x_{v1} = 0.5(20) + 10 = 10 + 10 = 20$$
  $$y_{v1} = 0.5(40) + 10 = 20 + 10 = 30 \implies P_1'(20, 30)$$
- For $P_2(80, 60)$:
  $$x_{v2} = 0.5(80) + 10 = 40 + 10 = 50$$
  $$y_{v2} = 0.5(60) + 10 = 30 + 10 = 40 \implies P_2'(50, 40)$$

**Transformed Line Segment in Viewport**: Connects $(20, 30)$ to $(50, 40)$.

---

### Example 2: Aspect-Ratio Correction and Pillarboxing Calculation [KTU Dec 2021 Pattern]
**Problem**:
A 2D graphics engine renders a square game world within window bounds $x_w \in [0, 1000], y_w \in [0, 1000]$. The target display is a Full HD monitor with viewport resolution $x_v \in [0, 1920], y_v \in [0, 1080]$.
1. Compute the scaling factors if mapped directly, and identify the resulting distortion.
2. Design an aspect-ratio-corrected, horizontally centered viewport that eliminates distortion (pillarboxing).

**Solution**:
1. **Direct Mapping**:
   $$s_x = \frac{1920 - 0}{1000 - 0} = 1.92, \quad s_y = \frac{1080 - 0}{1000 - 0} = 1.08$$
   $$\frac{s_x}{s_y} = \frac{1.92}{1.08} \approx 1.778$$
   Because $s_x \ne s_y$, objects are horizontally stretched by a factor of $1.778 \times$. A circular coin of radius $100$ in the game world appears as a wide horizontal ellipse with semi-major axis $192$ pixels and semi-minor axis $108$ pixels.
2. **Aspect-Ratio Correction (Pillarboxing)**:
   To preserve aspect ratio, we must enforce a uniform scaling factor $s = \min(s_x, s_y) = 1.08$.
   - The vertical span occupies full monitor height:
     $$\Delta y_v = s \cdot \Delta y_w = 1.08 \times 1000 = 1080 \text{ pixels} \implies [y_{v\min}, y_{v\max}] = [0, 1080]$$
   - The required active horizontal span is:
     $$\Delta x_v = s \cdot \Delta x_w = 1.08 \times 1000 = 1080 \text{ pixels}$$
   - Centering horizontally across the 1920-pixel display width:
     $$\text{Horizontal Pillar Margin} = \frac{1920 - 1080}{2} = \frac{840}{2} = 420 \text{ pixels}$$
     $$x_{v\min} = 420, \quad x_{v\max} = 420 + 1080 = 1500$$
   - Corrected Viewport: $x_v \in [420, 1500], y_v \in [0, 1080]$. Left $[0, 419]$ and right $[1501, 1920]$ bands are rendered black.

---

### Example 3: Viewport Mapping with Arbitrary Non-Origin Window Coordinates [KTU June 2024]
**Problem**:
A world window has lower-left corner $(-30, -20)$ and upper-right corner $(50, 40)$. The corresponding screen viewport is defined between pixels $(200, 150)$ and $(600, 450)$. Find the pixel coordinates for world point $P(-10, 10)$.

**Solution**:
Window: $x_{w\min} = -30, x_{w\max} = 50, y_{w\min} = -20, y_{w\max} = 40$.
Viewport: $x_{v\min} = 200, x_{v\max} = 600, y_{v\min} = 150, y_{v\max} = 450$.

**Step 1: Calculate Spans and Scaling Factors**:
$$\Delta x_w = 50 - (-30) = 80$$
$$\Delta y_w = 40 - (-20) = 60$$
$$\Delta x_v = 600 - 200 = 400$$
$$\Delta y_v = 450 - 150 = 300$$
$$s_x = \frac{400}{80} = 5.0$$
$$s_y = \frac{300}{60} = 5.0$$

**Step 2: Map Point $P(-10, 10)$**:
$$x_v = x_{v\min} + (x_w - x_{w\min}) \cdot s_x = 200 + (-10 - (-30)) \cdot 5.0 = 200 + (20 \times 5.0) = 200 + 100 = 300$$
$$y_v = y_{v\min} + (y_w - y_{w\min}) \cdot s_y = 150 + (10 - (-20)) \cdot 5.0 = 150 + (30 \times 5.0) = 150 + 150 = 300$$

**Result**: World point $P(-10, 10)$ maps to viewport pixel $(300, 300)$.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [June 2024 Q5 — 4 Marks]
**Question**:
Explain window-to-viewport coordinate transformation with a neat diagram.

**Solution**:

The **window-to-viewport coordinate transformation** (also called the Viewing Transformation) is the mathematical mapping that scales and translates a selected rectangular region of a virtual world scene (the window) onto a specified rectangular display area on a physical monitor (the viewport).

```
      WORLD COORDINATE SYSTEM                         PHYSICAL DISPLAY MONITOR
                 Y                                                Y
                 ▲                                                ▲
                 │                                                │
         (ywmax) ┌──────────────┐                                 │
                 │              │                         (yvmax) ┌──────────────┐
                 │    WINDOW    │                                 │   VIEWPORT   │
                 │(What is seen)│ ──────────────────────────────► │(Where to see)│
                 │              │            Viewing              │              │
         (ywmin) └──────────────┘         Transformation  (yvmin) └──────────────┘
                 (xwmin)  (xwmax)                                 (xvmin)  (xvmax)
                 └──────────────► X                               └──────────────► X
```

**Key Operational Steps**:
1. **Window Selection**: The user defines a rectangular clipping window in the World Coordinate System with bounds $[x_{w\min}, x_{w\max}]$ and $[y_{w\min}, y_{w\max}]$. All primitives outside this boundary are clipped away.
2. **Viewport Definition**: The user or windowing system defines a display viewport on the screen with bounds $[x_{v\min}, x_{v\max}]$ and $[y_{v\min}, y_{v\max}]$.
3. **Proportional Mapping**: To preserve relative spatial positions, the normalized displacement of a point $(x_w, y_w)$ inside the window is equated to its normalized displacement inside the viewport:
   $$\frac{x_w - x_{w\min}}{x_{w\max} - x_{w\min}} = \frac{x_v - x_{v\min}}{x_{v\max} - x_{v\min}}, \quad \frac{y_w - y_{w\min}}{y_{w\max} - y_{w\min}} = \frac{y_v - y_{v\min}}{y_{v\max} - y_{v\min}}$$
4. **Coordinate Computation**:
   $$x_v = x_{v\min} + (x_w - x_{w\min}) \cdot s_x$$
   $$y_v = y_{v\min} + (y_w - y_{w\min}) \cdot s_y$$
   where $s_x = \frac{x_{v\max} - x_{v\min}}{x_{w\max} - x_{w\min}}$ and $s_y = \frac{y_{v\max} - y_{v\min}}{y_{w\max} - y_{w\min}}$.
5. If $s_x = s_y$, the aspect ratio is preserved without geometric distortion.

---

### Question 2 [Dec 2018 Q14b — 3 Marks]
**Question**:
Derive an equation for window-to-viewport transformation by specifying the sequence of basic transformations involved.

**Solution**:

The window-to-viewport transformation maps a world coordinate window bounded by $[x_{w\min}, x_{w\max}]$ and $[y_{w\min}, y_{w\max}]$ to a screen viewport bounded by $[x_{v\min}, x_{v\max}]$ and $[y_{v\min}, y_{v\max}]$. It is formulated as a composite sequence of three basic affine transformations:

**Step 1: Translate the window lower-left corner to the coordinate origin**:
$$\mathbf{T}_1 = \mathbf{T}(-x_{w\min}, -y_{w\min}) = \begin{bmatrix} 1 & 0 & -x_{w\min} \\ 0 & 1 & -y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$$

**Step 2: Scale the window dimensions to match the viewport dimensions**:
$$\mathbf{S} = \mathbf{S}(s_x, s_y) = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
where:
$$s_x = \frac{x_{v\max} - x_{v\min}}{x_{w\max} - x_{w\min}}, \quad s_y = \frac{y_{v\max} - y_{v\min}}{y_{w\max} - y_{w\min}}$$

**Step 3: Translate the origin to the viewport lower-left corner**:
$$\mathbf{T}_2 = \mathbf{T}(x_{v\min}, y_{v\min}) = \begin{bmatrix} 1 & 0 & x_{v\min} \\ 0 & 1 & y_{v\min} \\ 0 & 0 & 1 \end{bmatrix}$$

**Concatenation of Composite Transformation Matrix $\mathbf{M}_{\text{view}}$**:
$$\mathbf{M}_{\text{view}} = \mathbf{T}_2 \cdot \mathbf{S} \cdot \mathbf{T}_1$$
$$\mathbf{M}_{\text{view}} = \begin{bmatrix} 1 & 0 & x_{v\min} \\ 0 & 1 & y_{v\min} \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -x_{w\min} \\ 0 & 1 & -y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{M}_{\text{view}} = \begin{bmatrix} 1 & 0 & x_{v\min} \\ 0 & 1 & y_{v\min} \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} s_x & 0 & -s_x \cdot x_{w\min} \\ 0 & s_y & -s_y \cdot y_{w\min} \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & x_{v\min} - s_x \cdot x_{w\min} \\ 0 & s_y & y_{v\min} - s_y \cdot y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$$

**Final Coordinate Mapping Equations**:
Multiplying $\mathbf{M}_{\text{view}}$ by point $\begin{bmatrix} x_w & y_w & 1 \end{bmatrix}^T$:
$$x_v = s_x \cdot x_w + (x_{v\min} - s_x \cdot x_{w\min})$$
$$y_v = s_y \cdot y_w + (y_{v\min} - s_y \cdot y_{w\min})$$

---

### Question 3 [KTU General Pattern — 4 Marks]
**Question**:
Differentiate between a Window and a Viewport in computer graphics.

**Solution**:

| Dimension | Window (World Window) | Viewport |
|---|---|---|
| **Definition** | A rectangular area defined in the World Coordinate System that selects a specific sub-portion of the virtual scene for rendering. | A rectangular area defined on the physical display monitor (or Normalized Device space) where the selected scene is drawn. |
| **Question Answered** | Determines **WHAT** to view (scene content selection). | Determines **WHERE** to display (screen location assignment). |
| **Coordinate System** | World Coordinate System (application-defined units: meters, miles, millimeters). | Device Coordinate System (screen pixels: integer column/row addresses) or NDC ($[0, 1]$). |
| **Associated Process** | **Clipping**: Primitives extending beyond the window margins are culled or segmented. | **Device Mapping**: Geometric coordinates are scaled to match the resolution of the physical output device. |
| **Multiplicity & Layout** | Usually one global camera window defined per view frustum. | Multiple viewports can be arranged across a single physical display screen (e.g., quad-split screen in CAD systems). |
| **Effect of Changing Size**| Enlarging the window shows a larger physical area of the virtual world (zooming out); shrinking it zooms in on details. | Enlarging the viewport enlarges the physical display area on screen without changing the content visible in the scene. |
