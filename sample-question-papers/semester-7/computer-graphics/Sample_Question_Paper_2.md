# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SEVENTH SEMESTER B.TECH DEGREE EXAMINATION
### Course Code: CS401 | Course Name: COMPUTER GRAPHICS
**Max. Marks: 100 | Duration: 3 Hours**

---

### PART A
*(Answer all questions. Each question carries 4 marks.)*

1. **[Module I]** Explain the functional difference between locator devices, stroke devices, valuator devices, and pick devices in interactive graphics hardware. Provide one industrial hardware example for each. *(4 Marks)*
2. **[Module II]** Derive the digital differential analyzer (DDA) recurrence relation for computing line points with slope $|m| > 1$. Why is floating-point arithmetic in DDA considered a computational bottleneck? *(4 Marks)*
3. **[Module II]** Explain the winding number rule used to determine the interior regions of complex self-intersecting polygons. How does it differ from the odd-even parity test? *(4 Marks)*
4. **[Module III]** Prove that two successive 2D rotations $\mathbf{R}(\theta_1)$ and $\mathbf{R}(\theta_2)$ are commutative: $\mathbf{R}(\theta_1) \cdot \mathbf{R}(\theta_2) = \mathbf{R}(\theta_2) \cdot \mathbf{R}(\theta_1) = \mathbf{R}(\theta_1 + \theta_2)$. Do 2D rotation and scaling matrices commute in general? Justify. *(4 Marks)*
5. **[Module III]** Describe the Midpoint Subdivision algorithm for line clipping. Under what hardware architecture is Midpoint Subdivision preferred over the Cohen-Sutherland method? *(4 Marks)*
6. **[Module IV]** Formulate the $4 \times 4$ homogeneous transformation matrix for 3D scaling with scaling factors $(s_x, s_y, s_z)$ with respect to an arbitrary fixed point $(x_f, y_f, z_f)$. *(4 Marks)*
7. **[Module V]** Distinguish between object-space methods and image-space methods for visible surface detection. State the computational complexity of each approach in terms of polygon count $n$ and display resolution $p$. *(4 Marks)*
8. **[Module V]** What is a vanishing point in perspective projection? How do principal vanishing points arise geometrically, and how are 1-point, 2-point, and 3-point perspective projections categorized? *(4 Marks)*
9. **[Module VI]** Define spatial convolution and spatial correlation in digital image processing. Give a mathematical expression for the discrete $2D$ convolution between image $f(x, y)$ and kernel $w(s, t)$ of size $m \times n$. *(4 Marks)*
10. **[Module VI]** Explain the Robert's Cross edge detector. Write the $2 \times 2$ gradient kernels $G_x$ and $G_y$, and evaluate their response on a step edge. *(4 Marks)*

---

### PART B
*(Answer any two full questions. Each question carries 9 marks.)*

#### Question 11 (Module I)
- **a)** Explain the internal construction and operational physics of a Shadow-Mask Cathode Ray Tube (CRT). Detail the role of the electron guns, convergence yoke, shadow mask grid, and phosphor triads. *(5 Marks)*
- **b)** A raster display has a resolution of $1280 \times 1024$ and operates at a refresh rate of 60 frames per second non-interlaced. Determine:
  1. The time allocated for scanning one complete horizontal scanline (assume horizontal retrace time is $15\%$ of scanline time).
  2. The pixel access time (dwell time) for the frame buffer video controller. *(4 Marks)*

#### Question 12 (Module II)
- **a)** Derive the Midpoint Circle algorithm. Deduce the initial decision parameter $p_0 = \frac{5}{4} - r$ (or $1 - r$ for integer coordinates) and the conditional parameter updates for $p_{k+1}$ when moving East ($E$) or South-East ($SE$). *(5 Marks)*
- **b)** Digitize a circle of radius $r = 7$ centered at $(0, 0)$ in the first quadrant from $x = 0$ to $x = y$ using the Midpoint Circle algorithm. Tabulate $k, p_k, (x_{k+1}, y_{k+1})$ and list all 8-way symmetric points corresponding to the calculated coordinates. *(4 Marks)*

#### Question 13 (Modules I & II)
- **a)** Contrast the DDA Line Drawing algorithm with Bresenham's Line Drawing algorithm across computational overhead, round-off error accumulation, hardware execution speed, and arithmetic operations. *(5 Marks)*
- **b)** Apply the DDA algorithm to generate the pixel path connecting point $A(1, 1)$ to point $B(8, 5)$. Provide the step-by-step floating-point calculations and the final rounded raster coordinates. *(4 Marks)*

---

### PART C
*(Answer any two full questions. Each question carries 9 marks.)*

#### Question 14 (Module III)
- **a)** Derive the mathematical transformation equations for mapping a 2D world coordinate window $(x_{w\min}, y_{w\min})$ to $(x_{w\max}, y_{w\max})$ onto a device viewport $(x_{v\min}, y_{v\min})$ to $(x_{v\max}, y_{v\max})$. Formulate the transformation in matrix notation. *(5 Marks)*
- **b)** A rectangular window has lower-left corner $(1, 1)$ and upper-right corner $(5, 3)$. The normalized viewport has lower-left corner $(0, 0)$ and upper-right corner $(1, 1)$. Find the viewport coordinates corresponding to window points $P_1(2, 2)$, $P_2(3, 1.5)$, and $P_3(5, 3)$. *(4 Marks)*

#### Question 15 (Module IV)
- **a)** Derive the complete $4 \times 4$ transformation matrix for rotating a 3D point about an arbitrary axis in space that passes through the origin with direction unit vector $\vec{u} = (\alpha_x, \alpha_y, \alpha_z)$ by an angle $\theta$. *(5 Marks)*
- **b)** Given a 3D unit cube with vertices at $(0,0,0)$ to $(1,1,1)$, perform uniform scaling by a factor of 2 followed by a rotation of $90^\circ$ counterclockwise about the $Z$-axis. Compute the final coordinates of vertices $(0,0,0)$ and $(1,1,1)$. *(4 Marks)*

#### Question 16 (Modules III & IV)
- **a)** Explain the Weiler-Atherton polygon clipping algorithm. Detail how intersecting vertices are classified as 'Entering' or 'Exiting' and how dual linked lists (polygon vertex list and window vertex list) are traversed to handle concave clipping. *(5 Marks)*
- **b)** A line segment joins $A(10, 30)$ and $B(80, 90)$. Clip the line using Cohen-Sutherland line clipping against the clipping window defined by $(x_{\min}, y_{\min}) = (20, 20)$ and $(x_{\max}, y_{\max}) = (60, 60)$. Show the outcodes, the intersection calculation, and final line segment. *(4 Marks)*

---

### PART D
*(Answer any two full questions. Each question carries 12 marks.)*

#### Question 17 (Module V)
- **a)** Explain the Depth-Sorting algorithm (Painter's Algorithm) for visible surface detection. Describe the preliminary $z$-extent sorting and the 5 sequential tests applied to resolve depth ambiguity when two polygon $z$-extents overlap. *(6 Marks)*
- **b)** Derive the mathematical equations and $4 \times 4$ projection matrix for an oblique parallel projection onto the $xy$-plane with projection direction making an angle $\alpha$ with the projection plane and angle $\phi$ with the $x$-axis. Contrast Cavalier and Cabinet projections. *(6 Marks)*

#### Question 18 (Module VI)
- **a)** Discuss the fundamental steps in digital image processing with a neat architectural block diagram (Image Acquisition, Enhancement, Restoration, Morphological Processing, Segmentation, Representation, Recognition). *(6 Marks)*
- **b)** Given a $5 \times 5$ image patch and a $3 \times 3$ Sobel horizontal gradient operator $G_x$:
  $$\text{Image Patch } I = \begin{bmatrix} 10 & 10 & 20 & 20 & 20 \\ 10 & 10 & 20 & 20 & 20 \\ 10 & 10 & 20 & 20 & 20 \\ 10 & 10 & 20 & 20 & 20 \\ 10 & 10 & 20 & 20 & 20 \end{bmatrix}, \quad G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$
  Compute the convolved response at the center pixel $(3, 3)$. Calculate the gradient magnitude $M(3, 3) = \sqrt{G_x^2 + G_y^2}$ and the edge orientation angle $\theta(3, 3) = \tan^{-1}\left(\frac{G_y}{G_x}\right)$. *(6 Marks)*

#### Question 19 (Modules V & VI)
- **a)** Explain the Scan-Line algorithm for visible surface detection. How does it leverage both edge coherence and scan-line coherence to reduce depth buffer memory requirements? *(6 Marks)*
- **b)** Define the following distance metrics between two pixels $p(x, y)$ and $q(s, t)$ in digital image processing:
  1. Euclidean Distance ($D_e$)
  2. City-Block Distance ($D_4$)
  3. Chessboard Distance ($D_8$)
  For pixels $p(1, 1)$ and $q(5, 4)$, compute all three distance metrics. Illustrate the geometric contours formed by pixels equidistant from origin under $D_4$ and $D_8$. *(6 Marks)*

