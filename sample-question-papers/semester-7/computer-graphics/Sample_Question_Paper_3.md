# APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY
## SEVENTH SEMESTER B.TECH DEGREE EXAMINATION
### Course Code: CS401 | Course Name: COMPUTER GRAPHICS
**Max. Marks: 100 | Duration: 3 Hours**

---

### PART A
*(Answer all questions. Each question carries 4 marks.)*

1. **[Module I]** Explain the purpose and operation of a Color Lookup Table (LUT) in raster-scan display systems. How does an 8-bit frame buffer index into a 24-bit True Color palette? *(4 Marks)*
2. **[Module II]** In Bresenham's line algorithm for slope $|m| < 1$, prove that the decision parameter recurrence is $p_{k+1} = p_k + 2\Delta y$ if $p_k < 0$, and $p_{k+1} = p_k + 2\Delta y - 2\Delta x$ if $p_k \ge 0$. *(4 Marks)*
3. **[Module II]** Explain why the simple recursive 4-connected boundary fill algorithm can cause stack overflow in large solid area scan conversion. How does scanline flood filling overcome this limitation? *(4 Marks)*
4. **[Module III]** Formulate the $3 \times 3$ homogeneous transformation matrix for reflecting a 2D object across the arbitrary line $y = mx + c$. *(4 Marks)*
5. **[Module III]** A line segment has endpoints with Cohen-Sutherland outcodes `1001` and `0000`. Can this line segment be trivially accepted or trivially rejected? Explain the bitwise operations involved. *(4 Marks)*
6. **[Module IV]** Explain the geometric representation of quadric surfaces (spheres and ellipsoids) using implicit equations and parametric equations in 3D computer graphics modeling. *(4 Marks)*
7. **[Module V]** Derive the surface normal equation $\vec{N} = \vec{V}_1 \times \vec{V}_2$ for a planar polygon with vertices $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, and $(x_3, y_3, z_3)$. State the plane coefficient formulas $A, B, C, D$. *(4 Marks)*
8. **[Module V]** Explain the difference between orthographic parallel projection, axonometric projection, and isometric projection. What are the direction angles for isometric projection? *(4 Marks)*
9. **[Module VI]** Explain how digital images are represented in matrix format $f(x, y)$ after continuous 2D sampling and amplitude quantization. Relate pixel bit depth to total distinct intensity levels. *(4 Marks)*
10. **[Module VI]** Define the Laplacian operator $\nabla^2 f$ in 2D image processing. Write the standard $3 \times 3$ discrete approximation masks for the Laplacian (with and without diagonal neighbor inclusion). *(4 Marks)*

---

### PART B
*(Answer any two full questions. Each question carries 9 marks.)*

#### Question 11 (Module I)
- **a)** Explain the beam penetration CRT method and contrast it with the shadow mask CRT method in terms of color capability, resolution, manufacturing complexity, and cost. *(5 Marks)*
- **b)** Consider a display screen with a resolution of $1024 \times 768$ pixels. Calculate the aspect ratio of the monitor. If the screen size is 15 inches diagonally, determine the pixel density in pixels per inch (PPI) and the physical dimensions (width and height) of a single pixel. *(4 Marks)*

#### Question 12 (Module II)
- **a)** Derive Bresenham's line algorithm for lines with steep slope $m > 1$. Show the decision parameter formulation, the initial value $p_0$, and the conditional coordinate increments along the $y$-axis. *(5 Marks)*
- **b)** Scan convert a line connecting $(1, 1)$ to $(5, 8)$ using Bresenham's line algorithm for steep lines ($m > 1$). Tabulate the decision parameter $p_k$ and the selected pixel points at each step. *(4 Marks)*

#### Question 13 (Modules I & II)
- **a)** Explain the Active Edge Table (AET) data structure used in Scan-Line Polygon Fill. Describe the fields in each edge record ($y_{\max}, x_{\text{current}}, 1/m$). How are edges sorted, added, and removed as the scanline increments? *(5 Marks)*
- **b)** Digitize a circle of radius $r = 6$ centered at origin $(0, 0)$ using the Midpoint Circle algorithm. Trace from $x = 0$ to $x = y$ showing all calculations of decision parameter $p_k$. *(4 Marks)*

---

### PART C
*(Answer any two full questions. Each question carries 9 marks.)*

#### Question 14 (Module III)
- **a)** Derive the composite transformation matrix for scaling a 2D polygon by factors $s_x$ and $s_y$ about an arbitrary fixed point $(x_f, y_f)$. *(5 Marks)*
- **b)** Given a square with vertices $A(1, 1)$, $B(3, 1)$, $C(3, 3)$, and $D(1, 3)$:
  1. Magnify the square to twice its size keeping vertex $A(1, 1)$ fixed.
  2. Apply a shear transformation of factor $sh_x = 2$ parallel to the $x$-axis keeping the $y = 0$ axis fixed.
  Compute the final coordinates of all four vertices after the composite transformation. *(4 Marks)*

#### Question 15 (Module IV)
- **a)** Explain the Sutherland-Hodgman polygon clipping pipeline. Show why clipping against individual infinite window boundaries sequentially ensures correct convex polygon output. *(5 Marks)*
- **b)** A convex polygon has vertices $V_1(10, 20)$, $V_2(40, 20)$, $V_3(40, 50)$, and $V_4(10, 50)$. Clip this polygon against a clipping window bounded by $x_{\min} = 20, x_{\max} = 60, y_{\min} = 10, y_{\max} = 40$. Provide the step-by-step vertex list after clipping against the Left, Right, Bottom, and Top clipping edges. *(4 Marks)*

#### Question 16 (Modules III & IV)
- **a)** Explain the Midpoint Subdivision line clipping algorithm using binary search divide-and-conquer strategy. Provide the flowchart and describe how bitwise outcodes guide subdivision. *(5 Marks)*
- **b)** Use the Cohen-Sutherland line clipping algorithm to clip the line segment $P_1(15, 25)$ to $P_2(75, 65)$ against the window $x_{\min}=20, x_{\max}=60, y_{\min}=20, y_{\max}=50$. Determine which endpoint is clipped first, compute the exact intersection coordinates, and output the clipped segment. *(4 Marks)*

---

### PART D
*(Answer any two full questions. Each question carries 12 marks.)*

#### Question 17 (Module V)
- **a)** Derive the complete $4 \times 4$ perspective transformation matrix in homogeneous coordinates where the projection plane is located at $z = 0$ and the center of projection (COP) is at $(0, 0, -d)$. Map an arbitrary 3D point $P(x, y, z)$ to its projected point $P'(x', y', 0)$. *(6 Marks)*
- **b)** Explain the Z-Buffer algorithm in detail. Provide step-by-step pseudocode for initializing the depth buffer $D(x, y) = 1.0$ (or $-\infty$) and frame buffer $C(x, y) = \text{background\_color}$, and updating pixel colors based on depth comparison. Why is Z-Buffer so easily implemented in modern GPU hardware? *(6 Marks)*

#### Question 18 (Module VI)
- **a)** What is a gray-level histogram of an image? Explain the theoretical foundation of histogram equalization. Derive the continuous transformation function $s = T(r) = (L-1) \int_0^r p_r(w) dw$ and its discrete summation equivalent. Why does histogram equalization enhance visual contrast? *(6 Marks)*
- **b)** An 8-level quantized image of size $64 \times 64$ pixels ($N = 4096$) has the following intensity distribution:
  
  | Gray Level $r_k$ | Number of Pixels $n_k$ |
  |---|---|
  | $r_0 = 0$ | 790 |
  | $r_1 = 1$ | 1023 |
  | $r_2 = 2$ | 850 |
  | $r_3 = 3$ | 656 |
  | $r_4 = 4$ | 329 |
  | $r_5 = 5$ | 245 |
  | $r_6 = 6$ | 122 |
  | $r_7 = 7$ | 81 |

  Perform discrete histogram equalization. Tabulate $r_k, n_k, p_r(r_k), \text{CDF } s_k$, rounded output levels $s_k$, and the new histogram values $n_{s_k}$. *(6 Marks)*

#### Question 19 (Modules V & VI)
- **a)** Explain the Back-Face Removal algorithm for hidden surface elimination. 
  1. Derive the condition $\vec{N} \cdot \vec{V} > 0$ for visibility where $\vec{V}$ is the viewing vector.
  2. Prove that if the viewing direction is along the $-Z$ axis in right-handed viewing coordinates, the back-face condition simplifies to $C \le 0$ (where $Ax + By + Cz + D = 0$).
  3. Discuss why back-face removal alone cannot solve the visible surface detection problem for general concave or overlapping scenes. *(6 Marks)*
- **b)** Compare the Robert's, Prewitt, and Sobel edge detection operators in detail:
  1. Provide the mathematical formulation and convolution masks for each.
  2. Explain why the Sobel operator is preferred over Prewitt and Roberts for noisy real-world images (weighting of central coefficients).
  3. Explain how edge gradient direction is mapped to horizontal, vertical, or diagonal edge orientations ($0^\circ, 45^\circ, 90^\circ, 135^\circ$). *(6 Marks)*

