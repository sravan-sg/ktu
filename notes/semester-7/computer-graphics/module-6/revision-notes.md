# Module 6: Revision Notes — Quick Review Guide

## 1. High-Yield Summary
- **Digital Image Sampling & Quantization**: Continuous image $f(x, y)$ is sampled into an $M \times N$ discrete grid and quantized into $L = 2^k$ gray levels.
- **Relationships Between Pixels**:
  - $N_4(p)$: 4 orthogonal neighbors.
  - $N_D(p)$: 4 diagonal neighbors.
  - $N_8(p) = N_4(p) \cup N_D(p)$.
  - **$m$-Adjacency**: Eliminates ambiguous 8-paths. $q \in N_4(p)$, OR $q \in N_D(p)$ with $N_4(p) \cap N_4(q) \cap V = \emptyset$.
- **Distance Metrics**:
  - Euclidean: $D_e = \sqrt{\Delta x^2 + \Delta y^2}$ (circular contour).
  - City-Block: $D_4 = |\Delta x| + |\Delta y|$ (diamond contour).
  - Chessboard: $D_8 = \max(|\Delta x|, |\Delta y|)$ (square contour).
  - Ordering: $D_8 \le D_e \le D_4$.
- **Histogram Equalization**: Transforms narrow-contrast images into uniform flat histograms using the scaled Cumulative Distribution Function (CDF):
  $$s_k = \text{round}\left( \frac{L-1}{MN} \sum_{j=0}^k n_j \right)$$
- **Spatial Convolution vs Correlation**:
  - Convolution rotates the kernel by **$180^\circ$** before sliding over the image. Identical for symmetric kernels.
- **Edge Detectors**:
  - *Roberts*: $2 \times 2$ diagonal differences. High noise sensitivity.
  - *Prewitt*: $3 \times 3$ central differences with uniform smoothing.
  - *Sobel*: $3 \times 3$ central differences with Gaussian-weighted smoothing (center weight 2).
  - *Canny (Optimal)*: 5 stages (Gaussian blur $\to$ Sobel gradient $\to$ Non-Maximum Suppression $\to$ Double Thresholding $\to$ Hysteresis Tracking).

---

## 2. Master Kernel Reference Table

| Operator | Horizontal Kernel ($G_x$) | Vertical Kernel ($G_y$) |
|---|---|---|
| **Roberts Cross** ($2 \times 2$) | $\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ |
| **Prewitt** ($3 \times 3$) | $\begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}$ |
| **Sobel** ($3 \times 3$) | $\begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$ |
| **Laplacian** ($3 \times 3$) | $\begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 & 1 \\ 1 & -8 & 1 \\ 1 & 1 & 1 \end{bmatrix} \quad (\text{Includes diagonals})$ |

---

## 3. Top 3 Exam Traps & Tips
1. **$m$-Adjacency Rule**: When asked to trace an $m$-path, remember: if two diagonally adjacent pixels share a common 4-neighbor that also has a value from $V$, the diagonal step is **STRICTLY FORBIDDEN**. You must route through the 4-neighbor.
2. **Canny NMS Orientation**: Remember that the gradient direction $\theta = \tan^{-1}(G_y / G_x)$ is **perpendicular** to the edge direction. If $\theta = 0^\circ$ (horizontal gradient), the edge itself is **vertical** ($90^\circ$).
3. **Histogram Equalization Summation**: In discrete histogram equalization, always compute the cumulative count $\sum_{j=0}^k n_j$ sequentially, multiply by $(L - 1) / MN$, and **round to the nearest integer**. Never round the floating-point probabilities before multiplying by $(L - 1)$!

