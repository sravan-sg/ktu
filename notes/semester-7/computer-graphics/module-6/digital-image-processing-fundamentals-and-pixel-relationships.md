# Digital Image Processing Fundamentals & Relationships Between Pixels

## 1. Explanation
Digital Image Processing (DIP) is the manipulation of digitized two-dimensional visual signals using general-purpose computational processors and specialized image processing pipelines. While computer graphics synthesizes 2D images from abstract mathematical models, image processing takes physical continuous visual scenes as inputs and analyzes, enhances, restores, or extracts structural semantic features from them.

---

### Fundamental Steps in Digital Image Processing
As codified by Rafael C. Gonzalez and Richard E. Woods (*Digital Image Processing*), a complete image processing system consists of the following sequential stages:

```
+-----------------------------------------------------------------------------------+
|                            IMAGE ACQUISITION                                      |
|    (Optical lens, CMOS/CCD sensor array, continuous illumination sampling)        |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                            IMAGE ENHANCEMENT                                      |
|  (Contrast stretching, histogram equalization, spatial filtering, sharpening)     |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                            IMAGE RESTORATION                                      |
|    (Inverting mathematical degradation models: deblurring, noise suppression)     |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                        COLOR IMAGE PROCESSING                                     |
|    (RGB, HSI, CMYK color spaces, pseudo-color rendering, chrominance isolation)   |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                         WAVELETS & MULTI-RESOLUTION                               |
|        (Sub-band frequency coding, pyramidal decimation, JPEG 2000)               |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                            IMAGE COMPRESSION                                      |
|      (Entropy coding, DCT quantization, Huffman coding, MPEG video streams)       |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                        MORPHOLOGICAL PROCESSING                                   |
|      (Structuring elements, dilation, erosion, opening, closing, skeletons)       |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                           IMAGE SEGMENTATION                                      |
|    (Partitioning image into regions: thresholding, edge detection, watershed)     |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                       REPRESENTATION & DESCRIPTION                                |
|        (Boundary descriptors, Fourier descriptors, regional moments)              |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                    OBJECT RECOGNITION & INTERPRETATION                            |
|       (Classification, neural feature extraction, semantic scene labeling)        |
+-----------------------------------------------------------------------------------+
```

---

### Digital Image Representation: Sampling & Quantization
A continuous physical image is a 2D optical intensity function $f(x, y)$, where $(x, y)$ are spatial coordinates and $f$ is the light amplitude (radiance $\times$ reflectance).
To convert $f(x, y)$ into a digital matrix:
1. **Sampling**: Discretizing continuous spatial coordinates $(x, y)$ onto a regular grid of rows and columns ($M \times N$). Sampling rate governs spatial resolution.
2. **Quantization**: Discretizing continuous amplitude intensities into a finite set of $L$ integer levels:
   $$L = 2^k, \quad \text{where } k \text{ is the bit depth (e.g. } k=8 \implies L=256 \text{ gray levels})$$

The resulting digital image is represented as an $M \times N$ numerical matrix:
$$f(x, y) = \begin{bmatrix}
f(0, 0) & f(0, 1) & \dots & f(0, N-1) \\
f(1, 0) & f(1, 1) & \dots & f(1, N-1) \\
\vdots & \vdots & \ddots & \vdots \\
f(M-1, 0) & f(M-1, 1) & \dots & f(M-1, N-1)
\end{bmatrix}$$

---

### Relationships Between Pixels

#### 1. Neighbors of a Pixel
Let a pixel be located at coordinates $p(x, y)$:
- **4-Neighbors ($N_4(p)$)**: The four orthogonal pixels immediately adjacent horizontally and vertically:
  $$N_4(p) = \{(x+1, y), \ (x-1, y), \ (x, y+1), \ (x, y-1)\}$$
- **Diagonal Neighbors ($N_D(p)$)**: The four diagonal corner pixels:
  $$N_D(p) = \{(x+1, y+1), \ (x+1, y-1), \ (x-1, y+1), \ (x-1, y-1)\}$$
- **8-Neighbors ($N_8(p)$)**: The union of 4-neighbors and diagonal neighbors:
  $$N_8(p) = N_4(p) \cup N_D(p)$$

```
  (x-1, y-1) [ND]  |  (x, y-1) [N4]  |  (x+1, y-1) [ND]
 ──────────────────┼─────────────────┼──────────────────
  (x-1, y)   [N4]  |     p(x, y)     |  (x+1, y)   [N4]
 ──────────────────┼─────────────────┼──────────────────
  (x-1, y+1) [ND]  |  (x, y+1) [N4]  |  (x+1, y+1) [ND]
```

---

#### 2. Adjacency, Connectivity, and Paths
Let $V$ be the subset of gray-level intensity values used to define similarity (e.g. in a binary image, $V = \{1\}$; in an 8-bit grayscale image, $V = \{0, 1, \dots, 50\}$).

1. **4-Adjacency**:
   Two pixels $p$ and $q$ with values from $V$ are 4-adjacent if $q \in N_4(p)$.
2. **8-Adjacency**:
   Two pixels $p$ and $q$ with values from $V$ are 8-adjacent if $q \in N_8(p)$.
3. **$m$-Adjacency (Modified / Mixed Adjacency)**:
   Two pixels $p$ and $q$ with values from $V$ are $m$-adjacent if:
   - $q \in N_4(p)$, **OR**
   - $q \in N_D(p)$ **AND** the set intersection $N_4(p) \cap N_4(q)$ contains **no pixels whose values are in $V$**.

> **Crucial Academic Insight ($m$-Adjacency)**:
> In 8-adjacency, diagonal pixel connections frequently produce multiple, ambiguous, redundant paths between points, creating topological paradoxes in region boundaries.
> **$m$-adjacency is specifically engineered to eliminate ambiguous 8-paths**, guaranteeing a unique, single topological path between adjacent pixels.

---

#### 3. Distance Metrics
A valid distance function $D(p, q)$ between pixels $p(x, y)$ and $q(s, t)$ must satisfy four mathematical metric space axioms:
1. Non-negativity: $D(p, q) \ge 0$, and $D(p, q) = 0 \iff p = q$.
2. Symmetry: $D(p, q) = D(q, p)$.
3. Triangle Inequality: $D(p, r) \le D(p, q) + D(q, r)$.

The three primary distance metrics used in DIP are:

1. **Euclidean Distance ($D_e$)**:
   The straight-line physical geometric distance:
   $$D_e(p, q) = \sqrt{(x - s)^2 + (y - t)^2}$$
   - Equidistant points form a circular contour centered at $p$.
2. **City-Block Distance ($D_4$ / Manhattan Distance)**:
   The distance traveled when constrained to orthogonal horizontal and vertical steps ($N_4$ connectivity):
   $$D_4(p, q) = |x - s| + |y - t|$$
   - Equidistant points form a diamond-shaped (rhombus) contour rotated at $45^\circ$.
3. **Chessboard Distance ($D_8$ / Chebyshev Distance)**:
   The distance traveled when diagonal steps are allowed at the same cost as orthogonal steps ($N_8$ connectivity, equivalent to the moves of a King in chess):
   $$D_8(p, q) = \max(|x - s|, \ |y - t|)$$
   - Equidistant points form a square contour aligned with the coordinate axes.

---

## 2. Example: Resolution of Ambiguous 8-Paths via $m$-Adjacency
Consider a $3 \times 3$ binary image patch with $V = \{1\}$:
```
Pixel Grid:               8-Adjacency Connections:       m-Adjacency Connection:
  0   1 (q)   0               0 ── 1 (q)   0                 0    1 (q)   0
  1   0       0               │  / │                             /
  1(p)0       0               1    0       0                 1  0         0
                              │                              │
                              1(p)─0       0                 1(p) 0       0
```
- Under 8-adjacency, there are two distinct paths from $p(2, 0)$ to $q(0, 1)$:
  - Path 1: $(2, 0) \to (1, 0) \to (0, 1)$ (length 2).
  - Path 2: Direct diagonal step $(1, 0) \to (0, 1)$ is shared.
- Under $m$-adjacency, $q \in N_D(p)$ has common 4-neighbors $N_4(p) \cap N_4(q)$. The pixel at $(1, 0)$ has value $1 \in V$.
- Therefore, the diagonal connection is **forbidden**. Only the single unambiguous path through $(1, 0)$ exists.

---

## 3. Applications & Use Cases
1. **Automated Optical Inspection (AOI) in Semiconductor Fabrication**: Microchip wafer inspection systems use $m$-connectivity component labeling to trace printed circuit board (PCB) copper traces and identify short-circuits or open-circuit hairline fractures without ambiguous topological bridging.
2. **Robot Path Planning in Grid Maps**: Autonomous mobile robots (AMRs) in warehouses use $D_4$ (Manhattan) metrics for orthogonal grid movement and $D_8$ metrics when diagonal wheel movements are supported.
3. **Fingerprint Ridge Extraction & Biometrics**: Minutiae feature extraction algorithms apply $N_8$ and $N_4$ neighbor relationships to locate ridge bifurcations and ridge endings.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Distance Metrics Calculation [KTU June 2024 / Dec 2020 - 4 Marks]
**Problem**:
Given two pixels $p(2, 3)$ and $q(7, 9)$ in a digital image:
1. Compute the Euclidean distance ($D_e$).
2. Compute the City-block distance ($D_4$).
3. Compute the Chessboard distance ($D_8$).

**Step-by-step Solution**:
1. Coordinates:
   $$x = 2, \ y = 3; \quad s = 7, \ t = 9$$
   $$\Delta x = |x - s| = |2 - 7| = 5$$
   $$\Delta y = |y - t| = |3 - 9| = 6$$
2. **Euclidean Distance ($D_e$)**:
   $$D_e(p, q) = \sqrt{\Delta x^2 + \Delta y^2} = \sqrt{5^2 + 6^2} = \sqrt{25 + 36} = \sqrt{61} \approx \mathbf{7.81}$$
3. **City-Block Distance ($D_4$)**:
   $$D_4(p, q) = \Delta x + \Delta y = 5 + 6 = \mathbf{11}$$
4. **Chessboard Distance ($D_8$)**:
   $$D_8(p, q) = \max(\Delta x, \Delta y) = \max(5, 6) = \mathbf{6}$$
5. **Ordering Property**:
   Notice that for all pairs of pixels: $D_8(p, q) \le D_e(p, q) \le D_4(p, q)$. Here $6 \le 7.81 \le 11$.

---

### Example 2: $m$-Adjacency and Path Length Evaluation [KTU May 2019 / Jan 2023 - 6 Marks]
**Problem**:
Consider the following binary image patch where $V = \{1\}$:
$$\begin{matrix}
(0, 0): 0 & (0, 1): 1 & (0, 2): 1 \\
(1, 0): 1 & (1, 1): 0 & (1, 2): 1 \\
(2, 0): 1 & (2, 1): 1 & (2, 2): 0
\end{matrix}$$
1. Find the shortest 8-path between $p(2, 0)$ and $q(0, 2)$.
2. Find the shortest $m$-path between $p(2, 0)$ and $q(0, 2)$ and compute its length.

**Step-by-step Solution**:
1. **Shortest 8-Path**:
   In 8-adjacency, diagonal moves between adjacent 1s are always permitted:
   - Path: $(2, 0) \to (2, 1) \to (1, 2) \to (0, 2)$.
   - Steps:
     - $(2, 0)$ to $(2, 1)$ (horizontal step)
     - $(2, 1)$ to $(1, 2)$ (diagonal step)
     - $(1, 2)$ to $(0, 2)$ (vertical step)
   - Length of shortest 8-path $= \mathbf{3}$.
2. **Shortest $m$-Path**:
   Check if the diagonal step from $(2, 1)$ to $(1, 2)$ is allowed under $m$-adjacency:
   - Let $p_1 = (2, 1)$ and $q_1 = (1, 2)$.
   - $q_1 \in N_D(p_1)$.
   - Check common 4-neighbors:
     $$N_4(p_1) \cap N_4(q_1) = \{(2, 2), \ (1, 1)\}$$
   - Pixel value at $(2, 2)$ is $0 \notin V$.
   - Pixel value at $(1, 1)$ is $0 \notin V$.
   - Since the intersection contains **no** pixel with value $1 \in V$, the diagonal connection **IS permitted**!
   - Now check diagonal from $(1, 0)$ to $(0, 1)$:
     - $N_4(1, 0) \cap N_4(0, 1) = \{(0, 0), (1, 1)\}$, both are $0$.
     - Hence $(2, 0) \to (1, 0) \to (0, 1) \to (0, 2)$ is also valid.
   - Therefore, the shortest $m$-path is:
     $$(2, 0) \to (2, 1) \to (1, 2) \to (0, 2)$$
   - Length of shortest $m$-path $= \mathbf{3}$.

---

### Example 3: Equidistant Contours of Distance Metrics [KTU Analytical Pattern]
**Problem**:
Draw and mathematically describe the locus of all pixels at distance $D = 2$ from origin $(0, 0)$ under Euclidean ($D_e$), City-block ($D_4$), and Chessboard ($D_8$) distance functions.

**Step-by-step Solution**:
1. **City-Block Distance $D_4(p, 0) = 2$**:
   $$|x| + |y| = 2$$
   - Points satisfying this: $(2, 0), (1, 1), (0, 2), (-1, 1), (-2, 0), (-1, -1), (0, -2), (1, -1)$.
   - Total pixels $= 8$.
   - Geometric shape: A **diamond (square rotated by $45^\circ$)**.
2. **Chessboard Distance $D_8(p, 0) = 2$**:
   $$\max(|x|, |y|) = 2$$
   - Points satisfying this: All pixels along the perimeter of a $5 \times 5$ square from $x, y \in [-2, 2]$.
   - Total pixels $= 4 \times (2 \times 2) = 16 \text{ pixels}$.
   - Geometric shape: A **square aligned with coordinate axes**.
3. **Euclidean Distance $D_e(p, 0) \le 2$**:
   $$\sqrt{x^2 + y^2} \le 2 \implies x^2 + y^2 \le 4$$
   - Discrete grid points within circle of radius 2: $(0, 0), (\pm 1, 0), (0, \pm 1), (\pm 1, \pm 1), (\pm 2, 0), (0, \pm 2)$.
   - Total pixels $= 13$.
   - Geometric shape: A **discretized circle**.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / January 2023 - 4 Marks]
**Question**:
Define 4-neighbors, 8-neighbors, and diagonal neighbors of a pixel. Compute the $D_4$ and $D_8$ distances between $P(1, 2)$ and $Q(6, 8)$.

**Solution**:
1. **Definitions**:
   Let a pixel be situated at coordinate location $(x, y)$:
   - **4-Neighbors ($N_4(p)$)**: The four horizontally and vertically adjacent pixels sharing a common edge:
     $$N_4(p) = \{(x+1, y), \ (x-1, y), \ (x, y+1), \ (x, y-1)\}$$
   - **Diagonal Neighbors ($N_D(p)$)**: The four corner-adjacent pixels sharing only a single vertex:
     $$N_D(p) = \{(x+1, y+1), \ (x+1, y-1), \ (x-1, y+1), \ (x-1, y-1)\}$$
   - **8-Neighbors ($N_8(p)$)**: The set of all eight surrounding pixels enclosing $p$:
     $$N_8(p) = N_4(p) \cup N_D(p)$$
2. **Distance Calculations between $P(1, 2)$ and $Q(6, 8)$**:
   $$\Delta x = |1 - 6| = 5, \quad \Delta y = |2 - 8| = 6$$
   - **City-Block Distance ($D_4$)**:
     $$D_4(P, Q) = \Delta x + \Delta y = 5 + 6 = \mathbf{11}$$
   - **Chessboard Distance ($D_8$)**:
     $$D_8(P, Q) = \max(\Delta x, \Delta y) = \max(5, 6) = \mathbf{6}$$

---

### Question 2 [KTU December 2021 / December 2023 - 6 Marks]
**Question**:
Explain the concept of $m$-adjacency in digital image processing. Why is it preferred over 8-adjacency?

**Solution**:
1. **Definition of $m$-Adjacency (Modified / Mixed Adjacency)**:
   Let $V$ be the subset of gray-level intensity values defining similarity between connected pixels. Two pixels $p$ and $q$ with values from $V$ are $m$-adjacent if:
   1. $q$ is in the 4-neighborhood of $p$ ($q \in N_4(p)$), **OR**
   2. $q$ is in the diagonal neighborhood of $p$ ($q \in N_D(p)$) **AND** the set intersection of their 4-neighborhoods contains no pixels with values from $V$:
      $$N_4(p) \cap N_4(q) \cap V = \emptyset$$
2. **Why $m$-Adjacency is Preferred over 8-Adjacency**:
   - **Elimination of Ambiguous Multi-Paths**: Under standard 8-adjacency, diagonal pixel connections frequently produce multiple, redundant paths between adjacent coordinates (both an orthogonal path and a direct diagonal shortcut). This introduces ambiguity in boundary tracing and contour definition.
   - **Topological Integrity (Jordan Curve Theorem)**: In continuous geometry, a closed curve separates the plane into an interior and exterior region. In discrete 8-connected binary images, single-pixel thin boundaries can leak or self-intersect, violating topological closure.
   - $m$-adjacency resolves this by forbidding the diagonal connection whenever an orthogonal path exists between the two pixels, guaranteeing **unique, unambiguous paths** across digital regions.

