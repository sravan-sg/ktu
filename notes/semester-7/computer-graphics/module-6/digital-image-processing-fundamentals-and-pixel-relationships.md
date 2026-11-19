# Digital Image Processing Fundamentals & Relationships Between Pixels

## 1. Explanation

While computer graphics synthesizes 2D images from abstract mathematical geometric descriptions (top-down visual modeling), **Digital Image Processing (DIP)** analyzes, transforms, restores, and extracts semantic information from physical visual images (bottom-up digital signal processing).

A continuous visual scene is captured by optical sensors as a two-dimensional continuous optical intensity distribution $f(x, y)$, where $(x, y)$ denotes spatial coordinates and $f$ represents the radiant energy (luminance) at that spatial coordinate.

---

### Digitization: Sampling and Quantization

To process a continuous analog image on digital computers, the continuous function $f(x, y)$ must be converted into a discrete numerical matrix through two distinct mathematical processes:
1. **Sampling**: Discretization of the continuous spatial coordinates $(x, y)$ into a discrete lattice of rows and columns.
2. **Quantization**: Discretization of the continuous luminance amplitude $f(x, y)$ into discrete integer intensity values (gray levels).

```
   Continuous Spatial Signal f(x, y)                  Digitized Sampled Matrix f[x, y]
          Luminance                                             Discrete Gray Levels
             ▲                                                         ▲
             │    /\                                                   │    ┌─┐
             │   /  \      Sampling (Spatial Grid)                     │  ┌─┘ └─┐
             │  /    \    ────────────────────────►                    │  │     │   Quantization
             │ /      \                                                │──┴─────┴──►
             └─────────► Spatial Position (x)                          └──────────► Pixel Index
```

#### 1. Spatial Sampling & The Nyquist-Shannon Theorem
Sampling partitions the continuous spatial domain into an $M \times N$ grid of discrete elements called **picture elements (pixels)**.
- According to the **2D Nyquist-Shannon Sampling Theorem**, to prevent spatial aliasing (moiré artifacts and high-frequency degradation), the spatial sampling frequency ($f_{sx}, f_{sy}$) must be at least **twice the highest spatial frequency ($u_{\max}, v_{\max}$)** present in the optical scene:
  $$f_{sx} \ge 2 u_{\max}, \quad f_{sy} \ge 2 v_{\max}$$
- If this criterion is violated, high-frequency spatial textures fold into low-frequency ghost patterns (aliasing).

#### 2. Amplitude Quantization & Dynamic Range
Quantization maps continuous photon-induced analog sensor voltages into discrete digital integer levels:
$$L = 2^k$$
where $k$ is the number of quantization bits (bit depth), and $L$ is the number of distinct permissible gray levels:
- For standard $8\text{-bit}$ grayscale imaging: $k = 8 \implies L = 256$ levels, spanning $[0, 255]$ ($0 = \text{pure black}$, $255 = \text{pure white}$).
- For medical radiographic imaging (DICOM): $k = 12 \implies L = 4096$ levels.
- For high-dynamic-range (HDR) imaging: $k = 16 \implies L = 65,536$ levels.

#### 3. Storage Requirement Formula
The memory footprint $b$ in bits required to store an uncompressed digitized image of size $M \times N$ with $k$ bits per pixel is:
$$b = M \times N \times k \text{ bits} = \frac{M \times N \times k}{8} \text{ bytes}$$

---

### Digital Image Representation

Mathematically, a digital image is represented as a 2D matrix of size $M \times N$, where row index $x \in \{0, 1, \dots, M-1\}$ denotes the vertical position (top to bottom) and column index $y \in \{0, 1, \dots, N-1\}$ denotes the horizontal position (left to right):

$$f(x, y) = \begin{bmatrix} f(0, 0) & f(0, 1) & \cdots & f(0, N-1) \\ f(1, 0) & f(1, 1) & \cdots & f(1, N-1) \\ \vdots & \vdots & \ddots & \vdots \\ f(M-1, 0) & f(M-1, 1) & \cdots & f(M-1, N-1) \end{bmatrix}$$

---

### Fundamental Steps in Digital Image Processing

As formalized by Gonzalez and Woods (*Digital Image Processing*), a complete end-to-end DIP system comprises the following stages:

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                              IMAGE ACQUISITION                                    │
│   (Optical lens, sensor array, illumination source, analog-to-digital conversion) │
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                              IMAGE ENHANCEMENT                                    │
│   (Subjective improvement: contrast stretching, histogram equalization, spatial   │
│    filtering, high-boost sharpening — brings out hidden details for human viewing)│
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                              IMAGE RESTORATION                                    │
│   (Objective correction: inverting degradation models, Wiener deblurring,         │
│    atmospheric turbulence correction, removing periodic sensor noise)             │
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                            COLOR IMAGE PROCESSING                                 │
│   (RGB, HSI, CMYK conversions, pseudo-color enhancement, chrominance tracking)   │
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                         WAVELETS & MULTI-RESOLUTION                               │
│   (Pyramidal decomposition, sub-band spatial-frequency analysis, JPEG 2000)       │
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                              IMAGE COMPRESSION                                    │
│   (Redundancy reduction: Huffman coding, Run-Length Encoding, DCT JPEG, MPEG)     │
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                          MORPHOLOGICAL PROCESSING                                 │
│   (Structuring elements: dilation, erosion, opening, closing, boundary extraction)│
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                             IMAGE SEGMENTATION                                    │
│   (Partitioning image into meaningful regions: Otsu thresholding, Canny edges,    │
│    region growing, watershed segmentation)                                        │
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                        REPRESENTATION & DESCRIPTION                               │
│   (Boundary chain codes, Fourier descriptors, regional moments, texture features) │
└─────────────────────────────────────────┬─────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                         OBJECT RECOGNITION / ML                                   │
│   (Classifying segmented patterns into semantic classes using deep CNNs/SVMs)     │
└───────────────────────────────────────────────────────────────────────────────────┘
```

---

### Pixel Relationships: Neighbors, Adjacency, Connectivity & Distance

Neighborhood topologies and connectivity rules form the mathematical foundation of spatial convolution, edge tracking, contour tracing, and region-growing segmentation.

#### 1. Pixel Neighborhoods
Let $p$ be a pixel at spatial coordinates $(x, y)$:

```
           (x-1, y-1)   (x-1, y)   (x-1, y+1)
                \          │          /
                 \         │         /
           (x, y-1) ────── p(x, y) ───── (x, y+1)
                 /         │         \
                /          │          \
           (x+1, y-1)   (x+1, y)   (x+1, y+1)
```

1. **4-Neighbors of $p$, denoted $N_4(p)$**:
   The four immediate horizontal and vertical orthogonal neighbors sharing a boundary edge with $p$:
   $$N_4(p) = \{(x-1, y), \ (x+1, y), \ (x, y-1), \ (x, y+1)\}$$
   Each neighbor in $N_4(p)$ is situated at unit Euclidean distance ($1.0$) from $p$.
2. **Diagonal Neighbors of $p$, denoted $N_D(p)$**:
   The four corner neighbors sharing only a vertex corner with $p$:
   $$N_D(p) = \{(x-1, y-1), \ (x-1, y+1), \ (x+1, y-1), \ (x+1, y+1)\}$$
   Each neighbor in $N_D(p)$ is situated at distance $\sqrt{2} \approx 1.414$ from $p$.
3. **8-Neighbors of $p$, denoted $N_8(p)$**:
   The complete set of all eight adjacent neighbors surrounding $p$:
   $$N_8(p) = N_4(p) \cup N_D(p)$$

---

#### 2. Pixel Adjacency & The $V$-Set
Two pixels $p$ and $q$ are **adjacent** if they are spatial neighbors AND their intensity values both belong to a specified set of allowable grayscale values $V \subseteq \{0, 1, \dots, L-1\}$. The set $V$ defines the "foreground" or "feature" brightness levels.

1. **4-Adjacency**:
   Pixels $p$ and $q$ with values from $V$ are 4-adjacent if:
   $$q \in N_4(p)$$
2. **8-Adjacency**:
   Pixels $p$ and $q$ with values from $V$ are 8-adjacent if:
   $$q \in N_8(p)$$
3. **m-Adjacency (Mixed Adjacency)**:
   Pixels $p$ and $q$ with values from $V$ are m-adjacent if:
   - $q \in N_4(p)$, **OR**
   - $q \in N_D(p)$ **AND** the intersection set $N_4(p) \cap N_4(q)$ contains **no pixels whose values belong to $V$**:
     $$N_4(p) \cap N_4(q) \cap V = \emptyset$$

> **Why m-Adjacency is Critical in Image Processing**:
> 8-adjacency often introduces **path ambiguity (multiple concurrent paths)** across diagonal connections, which causes closed contour loops to appear ambiguous during boundary-following and morphological thinning. Mixed adjacency ($m$-adjacency) strictly eliminates multiple alternative paths, guaranteeing a unique, single-pixel-wide path across diagonal neighbors.

---

#### 3. Digital Paths & Path Length
A **digital path** (or curve) from pixel $p(x_0, y_0)$ to pixel $q(x_n, y_n)$ is an ordered sequence of distinct pixels:
$$(x_0, y_0), \ (x_1, y_1), \ (x_2, y_2), \ \dots, \ (x_n, y_n)$$
where each pixel $(x_i, y_i)$ is adjacent to its predecessor $(x_{i-1}, y_{i-1})$ for $1 \le i \le n$.
- If adjacency is 4-adjacency, the path is a **4-path**.
- If adjacency is 8-adjacency, the path is an **8-path**.
- If adjacency is m-adjacency, the path is an **m-path**.
- **Path Length**: Defined as the number of step transitions $n$ (not the number of pixels $n+1$).

---

#### 4. Digital Distance Measures
For pixels $p(x, y)$, $q(s, t)$, and $z(u, v)$, a distance metric $D(p, q)$ must satisfy four fundamental metric axioms:
1. Non-negativity: $D(p, q) \ge 0$, and $D(p, q) = 0 \iff p = q$
2. Symmetry: $D(p, q) = D(q, p)$
3. Triangle Inequality: $D(p, z) \le D(p, q) + D(q, z)$

Standard Distance Metrics:
1. **Euclidean Distance ($D_e$)**:
   $$D_e(p, q) = \sqrt{(x - s)^2 + (y - t)^2}$$
   Points at distance $\le r$ form a continuous disk.
2. **City-Block / Manhattan Distance ($D_4$)**:
   The length of the shortest 4-path:
   $$D_4(p, q) = |x - s| + |y - t|$$
   Points at distance $\le r$ form a diamond (rhombus) shape oriented at $45^\circ$.
3. **Chessboard Distance ($D_8$)**:
   The length of the shortest 8-path:
   $$D_8(p, q) = \max(|x - s|, \ |y - t|)$$
   Points at distance $\le r$ form a square aligned with the coordinate axes.

---

## 2. Example: Concrete Path Tracing Walkthrough

Consider a $4 \times 4$ image grid with pixel values:

```
Coordinates:    (col 0)  (col 1)  (col 2)  (col 3)
   (row 0)         1        2        3        0
   (row 1)         0        2        2        1
   (row 2)         1        1        0        2
   (row 3)         2        1        2        1
```

Let start pixel be $q$ at $(0, 0)$ with value $f(0, 0) = 1$.
Let destination pixel be $p$ at $(3, 3)$ with value $f(3, 3) = 1$.

### Case A: Let $V = \{1, 2\}$
Both $1$ and $2$ are allowable path pixels.
- **Shortest 8-Path**:
  Starting at $q(0, 0) = 1$:
  - Step 1: $(0, 0) \to (1, 1)$ [value $2 \in V$]
  - Step 2: $(1, 1) \to (2, 2)$ [value $0 \notin V \implies$ cannot go to $(2, 2)$].
    Instead: $(1, 1) \to (1, 2)$ [value $2 \in V$]
  - Step 3: $(1, 2) \to (2, 3)$ [value $2 \in V$]
  - Step 4: $(2, 3) \to (3, 3)$ [value $1 \in V$]
  Path: $(0, 0) \to (1, 1) \to (1, 2) \to (2, 3) \to (3, 3)$.
  **8-Path Length = 4**.

- **Shortest 4-Path**:
  Only horizontal and vertical transitions allowed through $\{1, 2\}$:
  $(0, 0) \to (0, 1) \to (1, 1) \to (1, 2) \to (2, 2 \text{ [blocked: 0]}) \dots$
  Trace along valid path:
  $(0, 0) \to (0, 1) \to (1, 1) \to (1, 2) \to (1, 3) \to (2, 3) \to (3, 3)$.
  **4-Path Length = 6**.

---

## 3. Applications & Use Cases

1. **Autonomous Robot Obstacle Navigation**:
   Robotics occupancy grids represent navigable free space as $V = \{0\}$ and obstacles as $\{1\}$. Path planning algorithms (A*, Dijkstra) compute shortest $m$-paths through free space to generate collision-free trajectories.
2. **Medical MRI/CT Tumor Boundary Segmentation**:
   Radiological segmentation isolates lesion boundaries by finding connected components of voxels exceeding an attenuation threshold $V = [T_{\min}, T_{\max}]$.
3. **OCR & Document Processing**:
   Optical Character Recognition identifies printed alphanumeric characters by computing 8-connected components of black text pixels ($V = \{0\}$) against white backgrounds.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Exhaustive 4-, 8-, and m-Path Computation [KTU Dec 2021 Q18b / Sep 2020 Q19b]
**Problem**:
Consider the $4 \times 4$ image segment given below:
```
(q)  1   2   3   0
     0   2   2   1
     1   1   0   2
     2   1   2   1  (p)
```
Compute the length of the shortest 4-, 8-, and m-path between $p$ at $(3, 3)$ and $q$ at $(0, 0)$ for:
(i) $V = \{0, 1\}$
(ii) $V = \{1, 2\}$
If a particular path does not exist, provide the mathematical justification.

**Solution**:
Coordinates: $q = (0, 0)$ with $f(0, 0) = 1$. $p = (3, 3)$ with $f(3, 3) = 1$.

---

#### Part (i): $V = \{0, 1\}$
Allowable pixels must have values $0$ or $1$.

1. **4-Path ($V = \{0, 1\}$)**:
   Let us check if a connected 4-path exists from $q(0, 0)$ to $p(3, 3)$:
   - From $q(0, 0) = 1$:
     - Down to $(1, 0) = 0 \in V$ ✓
     - Right to $(0, 1) = 2 \notin V$ ✗
   - From $(1, 0) = 0$:
     - Down to $(2, 0) = 1 \in V$ ✓
     - Right to $(1, 1) = 2 \notin V$ ✗
   - From $(2, 0) = 1$:
     - Right to $(2, 1) = 1 \in V$ ✓
     - Down to $(3, 0) = 2 \notin V$ ✗
   - From $(2, 1) = 1$:
     - Neighbors: Up is $(1, 1) = 2 \notin V$; Left is $(2, 0)$ (visited); Down is $(3, 1) = 1 \in V$ ✓; Right is $(2, 2) = 0 \in V$ ✓.
     - Option A: Move to $(2, 2) = 0$. From $(2, 2)$: Right is $(2, 3) = 2 \notin V$; Down is $(3, 2) = 2 \notin V$. Dead end!
     - Option B: Move to $(3, 1) = 1$. From $(3, 1)$: Down is out of bounds; Left is $(3, 0) = 2 \notin V$; Right is $(3, 2) = 2 \notin V$. Dead end!
   - Destination $p(3, 3) = 1$ is surrounded by:
     - Above: $(2, 3) = 2 \notin V$
     - Left: $(3, 2) = 2 \notin V$
   Both 4-neighbors of $p(3, 3)$ have value $2$, which is not in $V = \{0, 1\}$.
   **Conclusion**: **No 4-path exists** between $p$ and $q$ because $p(3, 3)$ has zero 4-neighbors belonging to $V$.

2. **8-Path ($V = \{0, 1\}$)**:
   Examine the 8-neighbors of $p(3, 3)$:
   - $N_8(p) = \{(2, 2)=0, \ (2, 3)=2, \ (3, 2)=2\}$.
   - Vertex $(2, 2)$ has value $0 \in V$, providing an entry!
   Tracing path backward from $p(3, 3)$:
   - $p(3, 3) \to (2, 2) = 0$
   - From $(2, 2) \to (2, 1) = 1$
   - From $(2, 1) \to (2, 0) = 1$
   - From $(2, 0) \to (1, 0) = 0$
   - From $(1, 0) \to q(0, 0) = 1$
   Full 8-path:
   $$q(0, 0) \to (1, 0) \to (2, 0) \to (2, 1) \to (2, 2) \to p(3, 3)$$
   Number of steps = 5.
   **Shortest 8-Path Length = 5**.

3. **m-Path ($V = \{0, 1\}$)**:
   Examine every diagonal step in the 8-path to test the m-adjacency condition ($N_4(u) \cap N_4(v) \cap V = \emptyset$):
   - Step $(2, 2) \to (3, 3)$: This is a diagonal step ($q \in N_D(p)$).
     - $N_4((2, 2)) \cap N_4((3, 3)) = \{(2, 3), \ (3, 2)\}$.
     - Value of $(2, 3)$ is $2 \notin V$.
     - Value of $(3, 2)$ is $2 \notin V$.
     - Intersection set contains NO pixels from $V \implies$ Condition satisfied! $(2, 2)$ and $(3, 3)$ are validly **m-adjacent**.
   - All other steps ($(0, 0) \to (1, 0) \to (2, 0) \to (2, 1) \to (2, 2)$) are orthogonal 4-adjacency steps.
   Therefore, the exact same sequence forms a valid m-path:
   $$q(0, 0) \to (1, 0) \to (2, 0) \to (2, 1) \to (2, 2) \to p(3, 3)$$
   **Shortest m-Path Length = 5**.

---

#### Part (ii): $V = \{1, 2\}$
Allowable pixels must have values $1$ or $2$.

1. **Shortest 8-Path ($V = \{1, 2\}$)**:
   - $q(0, 0) = 1$
   - Step 1: $(0, 0) \to (1, 1)$ [value $2 \in V$]
   - Step 2: $(1, 1) \to (1, 2)$ [value $2 \in V$]
   - Step 3: $(1, 2) \to (2, 3)$ [value $2 \in V$]
   - Step 4: $(2, 3) \to p(3, 3)$ [value $1 \in V$]
   Path: $(0, 0) \to (1, 1) \to (1, 2) \to (2, 3) \to (3, 3)$.
   **Shortest 8-Path Length = 4**.

2. **Shortest 4-Path ($V = \{1, 2\}$)**:
   - $(0, 0) = 1 \to (0, 1) = 2 \to (1, 1) = 2 \to (1, 2) = 2 \to (1, 3) = 1 \to (2, 3) = 2 \to (3, 3) = 1$.
   Number of steps = 6.
   **Shortest 4-Path Length = 6**.

3. **Shortest m-Path ($V = \{1, 2\}$)**:
   - Test step $(0, 0) \to (1, 1)$:
     - Diagonal step: $N_4((0, 0)) \cap N_4((1, 1)) = \{(0, 1), \ (1, 0)\}$.
     - Value of $(0, 1)$ is $2 \in V$!
     - Because a common 4-neighbor belongs to $V$, $(0, 0)$ and $(1, 1)$ are **NOT m-adjacent**!
     - We must take the 4-path step $(0, 0) \to (0, 1) \to (1, 1)$.
   - Test step $(1, 2) \to (2, 3)$:
     - Diagonal step: $N_4((1, 2)) \cap N_4((2, 3)) = \{(1, 3), \ (2, 2)\}$.
     - Value of $(1, 3)$ is $1 \in V$!
     - Common neighbor in $V \implies$ $(1, 2)$ and $(2, 3)$ are **NOT m-adjacent**!
     - Must take step $(1, 2) \to (1, 3) \to (2, 3)$.
   - Constructed m-path:
     $$q(0, 0) \to (0, 1) \to (1, 1) \to (1, 2) \to (1, 3) \to (2, 3) \to p(3, 3)$$
   Number of steps = 6.
   **Shortest m-Path Length = 6**.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [June 2024 Q18b / Dec 2023 Q18a / Dec 2021 Q18a / Dec 2018 Q18a — 7–10 Marks]
**Question**:
Describe the fundamental steps in Digital Image Processing with a neat block diagram.

**Solution**:

The discipline of Digital Image Processing encompasses a comprehensive chain of algorithmic stages that transform raw optical data into enhanced, compressed, or high-level semantic representations:

```
┌─────────────────────────────────────────────────────────────┐
│                     IMAGE ACQUISITION                       │
│  Sensors (CCD/CMOS), illumination, continuous-to-digital A/D│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     IMAGE ENHANCEMENT                       │
│  Histogram equalization, spatial filtering, sharpening      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     IMAGE RESTORATION                       │
│  Inverting mathematical blur models, noise suppression      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   COLOR IMAGE PROCESSING                    │
│  RGB, HSI, CMYK color spaces, pseudo-color rendering        │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 WAVELETS & MULTI-RESOLUTION                 │
│  Sub-band frequency coding, pyramidal decimation            │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     IMAGE COMPRESSION                       │
│  Entropy reduction: JPEG DCT, Huffman coding, MPEG video    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   MORPHOLOGICAL PROCESSING                  │
│  Structuring elements, dilation, erosion, skeletonization   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     IMAGE SEGMENTATION                      │
│  Region extraction, thresholding, Sobel/Canny edge detection│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 REPRESENTATION & DESCRIPTION                │
│  Boundary chain codes, Fourier descriptors, regional moments│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 OBJECT RECOGNITION / ML                     │
│  Classification into semantic categories (Deep Neural Nets) │
└─────────────────────────────────────────────────────────────┘
```

1. **Image Acquisition**: The physical capture of illumination energy by optical sensor arrays (CCD/CMOS) followed by 2D spatial sampling and intensity quantization.
2. **Image Enhancement**: Subjective processing designed to make details more visible to human observers (contrast stretching, unsharp masking, high-pass filtering).
3. **Image Restoration**: Objective processing that models physical degradation phenomena (defocus blur, motion blur, atmospheric turbulence) and mathematically inverts the degradation function (e.g., Wiener filtering).
4. **Color Image Processing**: Manipulation of spectral components across color models (RGB for display, HSI for human color perception, CMYK for printing).
5. **Wavelets & Multiresolution Processing**: Representing images at multiple spatial scales, enabling scalable progressive transmission (JPEG 2000).
6. **Image Compression**: Eliminating coding, interpixel, and psychovisual redundancies to minimize storage and transmission bandwidth (Huffman, LZW, JPEG DCT).
7. **Morphological Processing**: Extracting geometric structural features using morphological set operators (dilation, erosion, opening, closing) with structuring elements.
8. **Image Segmentation**: Partitioning an image into its constituent objects or regions (Otsu global thresholding, watershed transform, edge detection).
9. **Representation and Description**: Converting segmented pixel regions into symbolic data structures (boundary chain codes, polygonal approximations, compactness, texture descriptors).
10. **Object Recognition**: Labeling segmented regions with semantic identities (e.g., classifying a tumor in an MRI scan or recognizing a pedestrian in autonomous driving).

---

### Question 2 [Dec 2018 Q12 / June 2024 Q8 / June 2022 Q38 — 4 Marks]
**Question**:
What do you understand by the following terms with respect to pixels:
(i) Neighbours
(ii) Adjacency
(iii) Connectivity

**Solution**:

#### (i) Neighbours
Spatial proximity relationships surrounding a central pixel $p$ at coordinates $(x, y)$:
- **4-Neighbours ($N_4(p)$)**: The four orthogonal neighbors sharing a boundary edge:
  $$N_4(p) = \{(x-1, y), \ (x+1, y), \ (x, y-1), \ (x, y+1)\}$$
- **Diagonal Neighbours ($N_D(p)$)**: The four corner neighbors sharing only a corner point:
  $$N_D(p) = \{(x-1, y-1), \ (x-1, y+1), \ (x+1, y-1), \ (x+1, y+1)\}$$
- **8-Neighbours ($N_8(p)$)**: The union of all 4-neighbors and diagonal neighbors:
  $$N_8(p) = N_4(p) \cup N_D(p)$$

---

#### (ii) Adjacency
Two pixels are **adjacent** if they are spatial neighbors AND their pixel intensity values both satisfy a specified similarity criterion $V$ (where $V$ is a set of allowable gray levels):
- **4-Adjacency**: $p$ and $q$ are 4-adjacent if $q \in N_4(p)$ and both $f(p), f(q) \in V$.
- **8-Adjacency**: $p$ and $q$ are 8-adjacent if $q \in N_8(p)$ and both $f(p), f(q) \in V$.
- **m-Adjacency (Mixed Adjacency)**: $p$ and $q$ with values from $V$ are m-adjacent if:
  1. $q \in N_4(p)$, **OR**
  2. $q \in N_D(p)$ **AND** $N_4(p) \cap N_4(q) \cap V = \emptyset$. (This eliminates multiple concurrent paths across diagonal pixels).

---

#### (iii) Connectivity
Let $S$ be a subset of pixels in an image:
- Two pixels $p$ and $q$ are **connected** in $S$ if there exists a valid digital path between them consisting entirely of pixels belonging to $S$.
- For any pixel $p \in S$, the set of all pixels in $S$ that are connected to $p$ is called a **Connected Component** (or Region $R$).
- If $S$ consists of a single connected component, $S$ is called a **Connected Set**.

---

### Question 3 [June 2024 Q18a — 2 Marks]
**Question**:
Give the digital image representation of an image.

**Solution**:

A digital image is mathematically modeled as a two-dimensional discrete matrix of size $M \times N$, where each element represents the digitized optical intensity (gray level) at discrete spatial coordinates $(x, y)$:

$$f(x, y) = \begin{bmatrix} f(0, 0) & f(0, 1) & \cdots & f(0, N-1) \\ f(1, 0) & f(1, 1) & \cdots & f(1, N-1) \\ \vdots & \vdots & \ddots & \vdots \\ f(M-1, 0) & f(M-1, 1) & \cdots & f(M-1, N-1) \end{bmatrix}$$

- $x \in \{0, 1, \dots, M-1\}$ represents the vertical row index (origin at top-left).
- $y \in \{0, 1, \dots, N-1\}$ represents the horizontal column index.
- For an 8-bit grayscale image, each matrix entry is an integer $f(x, y) \in [0, 255]$.
