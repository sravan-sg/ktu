# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SEVENTH SEMESTER B.TECH DEGREE EXAMINATION
### Course Code: CS401 | Course Name: COMPUTER GRAPHICS
**Max. Marks: 100 | Duration: 3 Hours**

---

### PART A
*(Answer all questions. Each question carries 4 marks.)*

1. **[Module I]** Contrast Raster Scan displays with Random Scan (Vector) displays in terms of refresh mechanism, resolution, deflection circuitry, and suitability for realistic photo rendering. *(4 Marks)*
2. **[Module II]** Explain the concept of 8-way symmetry in circle generation. If the circle is centered at $(0, 0)$ and a calculated pixel position is $(x, y) = (4, 7)$, determine the remaining seven symmetric pixel coordinates. *(4 Marks)*
3. **[Module II]** Compare the boundary-fill algorithm with the flood-fill algorithm for polygon scan conversion. State the termination condition for a 4-connected boundary fill implementation. *(4 Marks)*
4. **[Module III]** What are homogeneous coordinates? Why are they indispensable in 2D and 3D computer graphics pipelines when concatenating affine transformations? *(4 Marks)*
5. **[Module III]** Define the viewing transformation (Window-to-Viewport mapping). Given a world window bounded by $(0, 0)$ to $(100, 100)$ and a display viewport bounded by $(20, 20)$ to $(180, 180)$, find the viewport coordinates for the world point $(40, 60)$. *(4 Marks)*
6. **[Module IV]** Distinguish between Sutherland-Hodgman polygon clipping and Weiler-Atherton polygon clipping. Why does Sutherland-Hodgman fail to produce disjoint polygons when clipping concave figures? *(4 Marks)*
7. **[Module V]** Distinguish between Cavalier and Cabinet oblique projections. Calculate the projection angle and foreshortening factor for each. *(4 Marks)*
8. **[Module V]** State the geometric condition under which a polygon with surface normal $\vec{N} = (A, B, C)$ and plane equation $Ax + By + Cz + D = 0$ is identified as a back-face when viewed along the $-Z$ axis. *(4 Marks)*
9. **[Module VI]** Define 4-neighbors ($N_4(p)$), diagonal neighbors ($N_D(p)$), and 8-neighbors ($N_8(p)$) of a pixel $p(x, y)$. Calculate the Euclidean distance ($D_e$) and City-block distance ($D_4$) between pixels $p(2, 3)$ and $q(7, 9)$. *(4 Marks)*
10. **[Module VI]** State the convolution masks for the $3 \times 3$ Sobel and Prewitt edge detection operators along the horizontal ($G_x$) and vertical ($G_y$) directions. Explain how the gradient magnitude and edge angle are derived. *(4 Marks)*

---

### PART B
*(Answer any two full questions. Each question carries 9 marks.)*

#### Question 11 (Module I)
- **a)** Explain the architectural components and operating principle of a raster-scan display system featuring a video controller, refresh buffer, and color lookup table (LUT). *(5 Marks)*
- **b)** Compute the total memory capacity required for a frame buffer supporting a display resolution of $1920 \times 1080$ pixels with 24-bit True Color depth. How many distinct colors can be simultaneously rendered? *(4 Marks)*

#### Question 12 (Module II)
- **a)** Derive Bresenham's line drawing algorithm for a line segment with slope $0 < m < 1$. Clearly deduce the initial decision parameter $p_0$ and the recurrence relation for successive decision parameters $p_{k+1}$. *(5 Marks)*
- **b)** Digitize the line segment joining endpoints $(2, 3)$ and $(9, 7)$ using Bresenham's line algorithm. Tabulate the values of $k$, decision parameter $p_k$, and chosen pixel coordinates $(x_{k+1}, y_{k+1})$ at each step. *(4 Marks)*

#### Question 13 (Modules I & II)
- **a)** Explain the Scan-Line Polygon Fill algorithm. Describe the structure and management of the Edge Table (ET) and Active Edge Table (AET). How are parity rules applied during scan conversion? *(5 Marks)*
- **b)** Trace the Midpoint Circle algorithm for a circle with radius $r = 8$ centered at the origin $(0, 0)$ from $x = 0$ to $x = y$. Tabulate the decision parameter $p_k$, pixel coordinates $(x, y)$, and plot the initial octant points. *(4 Marks)*

---

### PART C
*(Answer any two full questions. Each question carries 9 marks.)*

#### Question 14 (Module III)
- **a)** Derive the composite transformation matrix ($3 \times 3$ in homogeneous coordinates) for rotating an object in 2D space by an angle $\theta$ counterclockwise about an arbitrary pivot point $(x_r, y_r)$. *(5 Marks)*
- **b)** A triangle has vertices at $A(2, 2)$, $B(6, 2)$, and $C(4, 6)$. Rotate the triangle by $90^\circ$ counterclockwise about the fixed point $(2, 2)$. Determine the new coordinates of vertices $A'$, $B'$, and $C'$. *(4 Marks)*

#### Question 15 (Module IV)
- **a)** Describe the Sutherland-Hodgman polygon clipping algorithm. Explain the four vertex classification rules applied when traversing edge $V_1 V_2$ against a clipping boundary line. *(5 Marks)*
- **b)** Given a rectangular clipping window with lower-left corner $(10, 10)$ and upper-right corner $(60, 60)$, apply the Sutherland-Hodgman algorithm to clip the triangle with vertices $P_1(5, 20)$, $P_2(70, 20)$, and $P_3(35, 70)$. Show the intermediate vertex output lists after clipping against each boundary (Left, Right, Bottom, Top). *(4 Marks)*

#### Question 16 (Modules III & IV)
- **a)** Explain the Cohen-Sutherland line clipping algorithm. Detail how 4-bit region codes (`Top`, `Bottom`, `Right`, `Left`) are generated, and explain the bitwise `AND` condition for trivial rejection. *(5 Marks)*
- **b)** Use the Cohen-Sutherland algorithm to clip the line segment connecting $P_1(20, 70)$ and $P_2(80, 30)$ against a window with boundaries $x_{\min} = 30$, $x_{\max} = 70$, $y_{\min} = 20$, $y_{\max} = 60$. Determine the intersection points and identify the accepted line segment. *(4 Marks)*

---

### PART D
*(Answer any two full questions. Each question carries 12 marks.)*

#### Question 17 (Module V)
- **a)** Derive the perspective projection transformation matrix onto the view plane $z = d$ with the center of projection (COP) positioned at the origin $(0, 0, 0)$. Explain the phenomenon of perspective foreshortening and vanishing points. *(6 Marks)*
- **b)** Explain the Z-Buffer (Depth Buffer) algorithm for hidden surface elimination. Provide the pseudocode, describe the initialization of the frame buffer and depth buffer, and derive the incremental calculation of depth $z$ along a scanline for polygon plane $Ax + By + Cz + D = 0$. *(6 Marks)*

#### Question 18 (Module VI)
- **a)** Explain the concept of $m$-adjacency (modified adjacency) in digital image processing. Why is $m$-adjacency introduced over 8-adjacency? Given a binary matrix, trace how ambiguous 8-paths are resolved using $m$-connectivity. *(6 Marks)*
- **b)** Perform histogram equalization on the following $4 \times 4$ sub-image with 8 gray levels ($r_k \in [0, 7]$):
  $$\begin{bmatrix} 1 & 2 & 2 & 1 \\ 3 & 4 & 5 & 4 \\ 2 & 3 & 6 & 7 \\ 1 & 2 & 4 & 5 \end{bmatrix}$$
  Tabulate the gray levels, frequency counts $n_k$, probability $p_r(r_k)$, cumulative distribution $s_k$, and round to determine the mapped output gray levels $s_k$. *(6 Marks)*

#### Question 19 (Modules V & VI)
- **a)** Explain the A-Buffer visible surface detection algorithm and compare its performance, memory footprint, and antialiasing/transparency handling with the standard Z-Buffer algorithm. *(6 Marks)*
- **b)** Describe the complete multistage pipeline of the Canny Edge Detector:
  1. Gaussian Smoothing filter
  2. Gradient intensity and orientation calculation
  3. Non-maximum suppression (NMS)
  4. Double thresholding ($T_{\text{high}}, T_{\text{low}}$)
  5. Edge tracking by hysteresis. *(6 Marks)*

