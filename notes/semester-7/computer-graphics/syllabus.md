# CS401 — Computer Graphics

> **Credits:** 4-0-0-4 (4 Credits) | **Scheme:** KTU 2016 Scheme | **Semester:** Semester 7 (Derivation: $H=4 \implies 2 \times 4 - 1 = 7$, last digit $1$ is odd)

---

## Grading Criteria

| Component | Assessment Tool | Marks | Weightage | Description / Pattern |
|---|---|---|---|---|
| **CIE (Internal)** | Internal Exam 1 | 20 | 20% | Modules I & II (Written Exam) |
| | Internal Exam 2 | 20 | 20% | Modules III & IV (Written Exam) |
| | Course Projects / Assignments | 10 | 10% | Two assignments / practical graphics assignments |
| **ESE (End Sem)** | University Examination | 100 | 50% | 3 Hours duration; 4 Parts (A, B, C, D) |

### End Semester Examination Pattern (Total: 100 Marks)

- **Part A (40 Marks): Compulsory**
  - **10 questions** of 4 marks each ($10 \times 4 = 40$ marks).
  - Distribution: 3 questions from Modules I & II, 3 questions from Modules III & IV, 4 questions from Modules V & VI.
  - All questions are mandatory.
- **Part B (18 Marks): Module I & II Choice**
  - **3 questions** of 9 marks each (Q11, Q12, Q13).
  - One question exclusively from Module I, one exclusively from Module II, and one covering Modules I & II.
  - Answer any **2 questions** ($2 \times 9 = 18$ marks).
  - Each question may have up to 3 sub-parts.
- **Part C (18 Marks): Module III & IV Choice**
  - **3 questions** of 9 marks each (Q14, Q15, Q16).
  - One question exclusively from Module III, one exclusively from Module IV, and one covering Modules III & IV.
  - Answer any **2 questions** ($2 \times 9 = 18$ marks).
  - Each question may have up to 3 sub-parts.
- **Part D (24 Marks): Module V & VI Choice**
  - **3 questions** of 12 marks each (Q17, Q18, Q19).
  - One question exclusively from Module V, one exclusively from Module VI, and one covering Modules V & VI.
  - Answer any **2 questions** ($2 \times 12 = 24$ marks).
  - Each question may have up to 3 sub-parts.
- **Analytical & Numerical Rule:** At least **50% of total marks** across all possible question combinations will test analytical derivations, mathematical algorithm traces, and numerical problems.

---

## Textbooks

1. **Donald Hearn and M. Pauline Baker**, *Computer Graphics*, PHI, 2nd Edition, 1996.
   - *Scope:* Primary textbook covering **Modules I, II, III, IV, and V** (Display devices, raster algorithms, 2D/3D transformations, window-viewport mapping, clipping, 3D projections, and visible surface detection).
2. **E. Gose, R. Johnsonbaugh and S. Jost**, *Pattern Recognition and Image Analysis*, PHI PTR, 1996.
   - *Scope:* Primary textbook covering **Module VI** (Image Processing, pixel adjacency, histograms, spatial convolution, edge detectors).
3. **William M. Newman and Robert F. Sproull**, *Principles of Interactive Computer Graphics*, McGraw Hill, 2nd Edition, 1979.
   - *Scope:* Reference for interactive input techniques, clipping, and display processors.
4. **Zhigang Xiang and Roy Plastock**, *Computer Graphics* (Schaum's Outline Series), McGraw Hill, 1986 / 2000.
   - *Scope:* Extensive collection of solved numerical problems, geometric transformation matrices, and clipping walkthroughs.

### References
1. **David F. Rogers**, *Procedural Elements for Computer Graphics*, Tata McGraw Hill, 2nd Edition, 2001.
2. **M. Sonka, V. Hlavac, and R. Boyle**, *Image Processing, Analysis, and Machine Vision*, Thomson India Edition, 2007.
3. **Rafael C. Gonzalez and Richard E. Woods**, *Digital Image Processing*, Pearson Education, 4th Edition, 2017.

---

## Modules

### Module I — Introduction to Computer Graphics and Display Hardware
- Basic concepts in Computer Graphics
- Types of Graphic Devices
- Interactive Graphic inputs (Locators, Stroke, String, Valuator, Choice, Pick devices)
- Raster Scan and Random Scan (Vector) Displays: Architecture, refresh rates, electron gun operation, shadow-mask CRT vs monochrome, frame buffers, lookup tables, and comparative trade-offs.

### Module II — Scan Conversion & Rasterization Algorithms
- Line Drawing Algorithms:
  - Digital Differential Analyzer (DDA) algorithm
  - Bresenham's Line Drawing algorithm (Integer arithmetic derivation, decision parameters for $|m| < 1$ and $|m| \ge 1$)
- Circle Generation Algorithms:
  - Midpoint Circle algorithm (Derivation of decision parameter $p_k$, 8-way symmetry)
  - Bresenham's Circle algorithm
- Scan Conversion & Frame Buffers:
  - Organization, bit planes, depth, color lookup tables
- Solid Area Scan Conversion:
  - Inside-outside tests (Odd-even rule, Winding number rule)
  - Polygon filling algorithms: Scan-line polygon fill algorithm (Edge table, Active Edge Table - AET), Boundary-fill algorithm (4-connected and 8-connected recursion), Flood-fill algorithm.

### Module III — 2D Transformations, Windowing & Line Clipping
- Two-Dimensional Transformations:
  - Basic transformations: Translation, Rotation, Scaling
  - Other transformations: Reflection, Shear
- Homogeneous Coordinate Systems:
  - Matrix formulation in homogeneous coordinates ($3 \times 3$)
  - Concatenation and composite transformations (Rotation about arbitrary pivot point, scaling about fixed point)
- Windowing Concepts:
  - World coordinate system, Viewing coordinate system, Normalized device coordinates (NDC), Device coordinates
  - Window-to-Viewport Transformation and mapping matrix derivation
- Two-Dimensional Clipping:
  - Point clipping
  - Line clipping: Cohen-Sutherland line clipping algorithm (Outcode generation, bitwise tests, parametric intersection calculation), Midpoint Subdivision algorithm.

### Module IV — Polygon Clipping & 3D Transformations
- Polygon Clipping Algorithms:
  - Sutherland-Hodgman Polygon Clipping algorithm (Left, Right, Bottom, Top boundary processing, vertex intersection cases)
  - Weiler-Atherton Polygon Clipping algorithm (Concave polygon handling, inner/outer loops, entering and exiting vertex intersections)
- Three-Dimensional Object Representation:
  - Polygon surfaces (Polygon tables, edge tables, vertex tables)
  - Quadric surfaces (Sphere, Ellipsoid, Torus)
  - Spline representations (overview)
- Basic 3D Transformations:
  - 3D Translation, 3D Scaling
  - 3D Rotation (Rotation about coordinate axes $X, Y, Z$, and composite rotation about an arbitrary axis in 3D space using Euler angles / directional cosines).

### Module V — 3D Projections & Visible Surface Detection
- 3D Projections:
  - Taxonomy of projections (Planar vs non-planar)
  - Parallel Projections: Orthographic (isometric, dimetric, trimetric) and Oblique projections (Cavalier $\alpha=45^\circ$, Cabinet $\alpha=63.4^\circ$)
  - Perspective Projections: Center of projection, vanishing points (1-point, 2-point, 3-point), perspective transformation matrix and foreshortening
- Visible Surface Detection (Hidden Surface Elimination):
  - Object-space vs Image-space algorithms
  - Back-Face Removal (Surface normal dot-product test: $A_{\text{poly}}x + B_{\text{poly}}y + C_{\text{poly}}z + D_{\text{poly}} \le 0$)
  - Depth-Buffer (Z-Buffer) Algorithm: Data structures (Frame buffer, Depth buffer), incremental calculation of depth along scan lines
  - A-Buffer Algorithm: Anti-aliased, accumulative image-space method, linked list pixel structure for transparency
  - Depth-Sorting Method (Painter's Algorithm): Priority ordering, depth overlap tests
  - Scan-Line Method: Edge table, active edge table, polygon scan-line intersection.

### Module VI — Digital Image Processing Fundamentals & Edge Detection
- Image Processing Fundamentals:
  - Introduction to digital image processing
  - Fundamental steps in digital image processing systems
  - Digital image representation: Sampling, quantization, matrix form $f(x, y)$
- Relationship Between Pixels:
  - Neighbors of a pixel ($N_4(p), N_D(p), N_8(p)$)
  - Adjacency (4-adjacency, 8-adjacency, $m$-adjacency)
  - Connectivity, paths, regions, boundaries
  - Distance metrics: Euclidean distance ($D_e$), City-block distance ($D_4$), Chessboard distance ($D_8$)
- Gray Level Histogram:
  - Definition, histogram computation
  - Histogram equalization, contrast enhancement
- Spatial Filtering:
  - Spatial convolution and correlation mechanisms with 2D kernels
- Edge Detection Operators:
  - First-order derivative masks: Robert's Cross operator ($2 \times 2$), Prewitt operator ($3 \times 3$), Sobel operator ($3 \times 3$)
  - Second-order derivative operators: Laplacian, Laplacian of Gaussian (LoG)
  - Canny Edge Detector: Multistage pipeline (Gaussian smoothing, gradient calculation, Non-maximum suppression, Double thresholding, Edge tracking by hysteresis).

---

## Exam Focus — What to Prioritize

As a senior Computer Science professor evaluating KTU examination records, the following 6 core pillars represent over **75% of high-mark questions**:

1. **Bresenham's Integer Line and Circle Algorithms (Module II)**:
   - *Why:* Pure integer arithmetic derivations are a permanent fixture. You must master deriving the initial decision parameter ($p_0 = 2\Delta y - \Delta x$ for line; $p_0 = 1 - r$ or $\frac{5}{4} - r$ for circle) and stepping through a complete coordinate table for given endpoints (e.g. $(2, 2)$ to $(10, 7)$ or radius $r=10$).
2. **2D & 3D Composite Transformations (Modules III & IV)**:
   - *Why:* Solved matrix multiplications make up the bulk of Part C numericals. Focus on:
     - Deriving the composite matrix for 2D rotation about an arbitrary point $(x_r, y_r)$.
     - 3D rotation about an arbitrary line in space passing through point $P_0(x_0, y_0, z_0)$ with direction cosines $(\alpha_x, \alpha_y, \alpha_z)$.
     - Window-to-Viewport transformation matrix.
3. **Cohen-Sutherland & Sutherland-Hodgeman Clipping (Modules III & IV)**:
   - *Why:* Frequent 9-mark questions. Must know how to calculate 4-bit outcodes (`TBRL`), test for trivial accept/reject, compute exact intersection points, and apply Sutherland-Hodgman vertex clipping sequence (Left, Right, Bottom, Top) on concave and convex polygons.
4. **Z-Buffer and Visible Surface Detection (Module V)**:
   - *Why:* Guaranteed 12-mark question in Part D. Understand the recurrence relation for plane equation $Ax + By + Cz + D = 0 \implies z' = z - \frac{A}{C}$ along a scan-line, compare Z-Buffer against A-Buffer, and contrast Object-Space vs Image-Space trade-offs.
5. **Perspective vs Parallel Projection Matrices (Module V)**:
   - *Why:* Vanishing points calculation, projection matrix derivations using similar triangles ($x_p = \frac{x}{z/d}$, $y_p = \frac{y}{z/d}$), and distinguishing Cavalier from Cabinet oblique projections.
6. **Pixel Adjacency, Distance Metrics & Edge Operators (Module VI)**:
   - *Why:* Part D analytical section regularly tests $m$-adjacency to avoid ambiguous paths, calculating $D_4$, $D_8$, $D_e$ between coordinates, and manually convolving $3 \times 3$ image patches with Sobel and Prewitt kernels to determine edge gradient magnitude and angle.

