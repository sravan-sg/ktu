# Edge Detection Operators: Roberts, Prewitt, Sobel & Canny

## 1. Explanation
Edge detection is the primary segmentation technique in digital image processing. An **edge** is a localized boundary between two distinct visual regions characterized by significant spatial discontinuities or sharp gradients in image intensity.

---

### Mathematical Foundations of Edge Detection
In continuous space, edge discontinuities are detected using spatial derivatives:
1. **First-Order Derivative (Gradient Vector)**:
   Measures the rate of change of image intensity $f(x, y)$:
   $$\nabla f = \begin{bmatrix} G_x \\ G_y \end{bmatrix} = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$
   - **Gradient Magnitude**: Represents edge strength:
     $$M(x, y) = |\nabla f| = \sqrt{G_x^2 + G_y^2} \approx |G_x| + |G_y|$$
   - **Gradient Direction (Edge Angle)**: The angle of maximum rate of change (perpendicular to the edge boundary):
     $$\theta(x, y) = \tan^{-1}\left(\frac{G_y}{G_x}\right)$$
2. **Second-Order Derivative (Laplacian)**:
   Detects zero-crossings at points of maximum first-order gradient:
   $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$

---

### First-Order Gradient Operators

#### 1. Roberts Cross-Gradient Operator ($2 \times 2$)
Uses diagonal differences to approximate the gradient:
$$G_x = f(x+1, y+1) - f(x, y)$$
$$G_y = f(x, y+1) - f(x+1, y)$$

Convolution Masks:
$$G_x = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$
- *Advantage:* Highly compact ($2 \times 2$), minimal computation.
- *Limitation:* Extremely sensitive to high-frequency image noise; lacks spatial symmetry.

---

#### 2. Prewitt Operator ($3 \times 3$)
Combines central difference differentiation with uniform orthogonal smoothing:
$$G_x \text{ (Horizontal Edge Detector)} = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$
$$G_y \text{ (Vertical Edge Detector)} = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}$$
- *Characteristics:* Smooths noise across 3 adjacent rows/columns before computing differences.

---

#### 3. Sobel Operator ($3 \times 3$)
The industry standard first-order edge detector. Incorporates **weighted Gaussian-like smoothing** by assigning a weight of $2$ to the central row/column:
$$G_x \text{ (Horizontal Derivative / Detects Vertical Edges)} = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$
$$G_y \text{ (Vertical Derivative / Detects Horizontal Edges)} = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$

> **Why Sobel is Superior to Prewitt**:
> The central weight of $2$ provides superior spatial noise suppression (smoothing) around the target pixel, resulting in much cleaner, continuous edge contours on noisy real-world images.

---

### The Canny Edge Detector (The Optimal Edge Detector)
Developed by John F. Canny in 1986, the Canny edge detector was derived mathematically from three optimal edge criteria:
1. **Low Error Rate**: High probability of detecting true edges, low probability of false edges.
2. **Good Localization**: Detected edge points must be as close as possible to true edge centers.
3. **Single Response**: Only one response per true edge (elimination of thick, smeared multi-pixel edges).

#### The 5-Stage Canny Edge Detection Pipeline:

```
[ Input Grayscale Image ]
           │
           ▼
Stage 1: Gaussian Smoothing Filter
  Convolve with 2D Gaussian kernel G(x, y, sigma) = (1/2*pi*sigma^2) * exp(-(x^2+y^2)/2*sigma^2)
  Removes high-frequency sensor noise.
           │
           ▼
Stage 2: Gradient Intensity & Orientation Calculation
  Compute G_x and G_y using Sobel operators.
  Magnitude: M(x, y) = sqrt(G_x^2 + G_y^2)
  Direction: theta(x, y) = atan2(G_y, G_x)
           │
           ▼
Stage 3: Non-Maximum Suppression (NMS)
  Thin thick edge bands into 1-pixel wide continuous contours.
  Quantize edge angle theta into 4 sectors: 0 deg (horizontal), 45 deg, 90 deg (vertical), 135 deg.
  Compare M(x, y) with its two neighbors along the gradient direction.
  If M(x, y) is NOT the local maximum, set M(x, y) = 0.
           │
           ▼
Stage 4: Double Thresholding
  Classify remaining edge pixels using two thresholds: T_high and T_low (typically T_high = 2 * T_low):
  - If M(x, y) >= T_high: Classified as STRONG EDGE (definite edge).
  - If T_low <= M(x, y) < T_high: Classified as WEAK EDGE (candidate edge).
  - If M(x, y) < T_low: Classified as NON-EDGE (suppressed to 0).
           │
           ▼
Stage 5: Edge Tracking by Hysteresis
  Retain weak edge pixels IF AND ONLY IF they are 8-connected to a STRONG EDGE pixel.
  Suppresses spurious isolated noise while preserving weak, continuous edge chains.
           │
           ▼
[ Output Binary Edge Map (Thin, Continuous, Robust Edges) ]
```

---

## 2. Example: Canny Non-Maximum Suppression (NMS) Geometry
```
Gradient Direction theta = 90 deg (Vertical)
      (x, y+1) [Neighbor 1]
         ▲
         │
      p(x, y) ◄── Must be >= both Neighbor 1 and Neighbor 2
         │
         ▼
      (x, y-1) [Neighbor 2]

Direction Sectors:
  Sector 0 (0 deg):   Horizontal gradient -> Compare with Left (x-1, y) and Right (x+1, y)
  Sector 1 (45 deg):  Positive diagonal   -> Compare with (x+1, y+1) and (x-1, y-1)
  Sector 2 (90 deg):  Vertical gradient   -> Compare with Top (x, y+1) and Bottom (x, y-1)
  Sector 3 (135 deg): Negative diagonal   -> Compare with (x-1, y+1) and (x+1, y-1)
```

---

## 3. Applications & Use Cases
1. **Autonomous Vehicle Lane Detection (Tesla Autopilot, Waymo)**: Canny edge detection identifies high-contrast painted road markings and lane boundaries in automotive camera feeds.
2. **Barcode and QR-Code Scanners**: Sobel gradient filters extract the crisp rectangular boundary lines of QR codes under varying angles and lighting before decoding.
3. **Medical Ultrasound Vessel Boundary Segmentation**: Canny hysteresis pipelines extract carotid artery and cardiac ventricle wall boundaries from noisy B-mode ultrasound frames.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Sobel Gradient Calculation on Image Patch [KTU May 2019 / Jan 2023 - 6 Marks]
**Problem**:
Given the following $3 \times 3$ image neighborhood $F$:
$$F = \begin{bmatrix} 10 & 10 & 20 \\ 10 & 10 & 20 \\ 10 & 10 & 20 \end{bmatrix}$$
Apply the Sobel operator to compute:
1. Horizontal gradient $G_x$.
2. Vertical gradient $G_y$.
3. Gradient magnitude $M$.
4. Gradient orientation angle $\theta$.

**Step-by-step Solution**:
1. **Sobel Masks**:
   $$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$
2. **Calculate $G_x$**:
   $$\begin{aligned}
   G_x &= (-1 \times 10) + (0 \times 10) + (1 \times 20) \\
       &+ (-2 \times 10) + (0 \times 10) + (2 \times 20) \\
       &+ (-1 \times 10) + (0 \times 10) + (1 \times 20)
   \end{aligned}$$
   $$G_x = (-10 + 20) + (-20 + 40) + (-10 + 20) = 10 + 20 + 10 = \mathbf{40}$$
3. **Calculate $G_y$**:
   $$\begin{aligned}
   G_y &= (-1 \times 10) + (-2 \times 10) + (-1 \times 20) \\
       &+ (0 \times 10) + (0 \times 10) + (0 \times 20) \\
       &+ (1 \times 10) + (2 \times 10) + (1 \times 20)
   \end{aligned}$$
   $$G_y = (-10 - 20 - 20) + 0 + (10 + 20 + 20) = -50 + 50 = \mathbf{0}$$
4. **Gradient Magnitude $M$**:
   $$M = \sqrt{G_x^2 + G_y^2} = \sqrt{40^2 + 0^2} = \mathbf{40}$$
5. **Gradient Orientation $\theta$**:
   $$\theta = \tan^{-1}\left(\frac{G_y}{G_x}\right) = \tan^{-1}\left(\frac{0}{40}\right) = \mathbf{0^\circ}$$
   - *Physical Interpretation:* The gradient direction is $0^\circ$ (pointing horizontally along $+X$).
   - The edge itself runs **perpendicular** to the gradient, representing a **vertical edge at $90^\circ$**, which perfectly matches the vertical boundary between intensities 10 and 20!

---

### Example 2: Prewitt Operator Trace on Diagonal Edge [KTU Dec 2021 Pattern]
**Problem**:
Evaluate the Prewitt operator on the diagonal step edge patch:
$$F = \begin{bmatrix} 0 & 0 & 50 \\ 0 & 50 & 50 \\ 50 & 50 & 50 \end{bmatrix}$$

**Step-by-step Solution**:
1. **Prewitt Masks**:
   $$P_x = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}, \quad P_y = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$
2. **Compute $P_x$**:
   $$P_x = (-1(0) + 1(50)) + (-1(0) + 1(50)) + (-1(50) + 1(50)) = 50 + 50 + 0 = \mathbf{100}$$
3. **Compute $P_y$**:
   $$P_y = (-1(0) - 1(0) - 1(50)) + 0 + (1(50) + 1(50) + 1(50)) = -50 + 150 = \mathbf{100}$$
4. **Magnitude and Direction**:
   $$M = \sqrt{100^2 + 100^2} = \sqrt{20000} \approx \mathbf{141.42}$$
   $$\theta = \tan^{-1}\left(\frac{100}{100}\right) = \mathbf{45^\circ}$$
   The gradient points at $45^\circ$, identifying an edge inclined at $135^\circ$ ($45^\circ + 90^\circ$).

---

### Example 3: Canny Double Thresholding Decision Trace [KTU Analytical Pattern]
**Problem**:
In a Canny edge detector with thresholds $T_{\text{low}} = 30$ and $T_{\text{high}} = 70$, an image patch yields three adjacent thinned pixels after Non-Maximum Suppression:
- Pixel $A(10, 10)$: Magnitude $M_A = 85$
- Pixel $B(10, 11)$: Magnitude $M_B = 45$ (8-neighbor of $A$)
- Pixel $C(10, 12)$: Magnitude $M_C = 40$ (8-neighbor of $B$)
- Pixel $D(15, 20)$: Magnitude $M_D = 50$ (isolated weak pixel with no adjacent strong pixels)
Determine which pixels appear in the final binary edge map.

**Step-by-step Solution**:
1. **Classify by Double Thresholds**:
   - $M_A = 85 \ge 70 \implies \mathbf{A \text{ is a STRONG EDGE}}$.
   - $M_B = 45 \in [30, 70) \implies \mathbf{B \text{ is a WEAK EDGE}}$.
   - $M_C = 40 \in [30, 70) \implies \mathbf{C \text{ is a WEAK EDGE}}$.
   - $M_D = 50 \in [30, 70) \implies \mathbf{D \text{ is a WEAK EDGE}}$.
2. **Hysteresis Connectivity Tracking**:
   - Pixel $A$ is strong: **Accepted**.
   - Pixel $B$ is an 8-neighbor of strong pixel $A$: **Promoted and Accepted**.
   - Pixel $C$ is an 8-neighbor of promoted pixel $B$: **Promoted and Accepted** (chain continuity).
   - Pixel $D$ is weak and has no connected path to any strong edge pixel: **Suppressed to 0 (Rejected)**.
3. **Output Edge Map**: Pixels $A, B, C$ are retained as valid continuous edge pixels; pixel $D$ is discarded as noise.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / June 2024 - 4 Marks]
**Question**:
State the convolution masks for Roberts, Prewitt, and Sobel edge detectors. Which is preferred for noisy images and why?

**Solution**:
1. **Convolution Masks**:
   - **Roberts Cross ($2 \times 2$)**:
     $$G_x = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$
   - **Prewitt Operator ($3 \times 3$)**:
     $$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$
   - **Sobel Operator ($3 \times 3$)**:
     $$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$
2. **Preferred Operator for Noisy Images**:
   **The Sobel operator is strongly preferred** because:
   - It incorporates a central weight of $2$ in the smoothing dimension, which provides weighted local Gaussian smoothing.
   - This suppresses high-frequency sensor noise far more effectively than the uniform weighting of Prewitt or the zero-smoothing $2 \times 2$ difference of Roberts.

---

### Question 2 [KTU December 2020 / December 2023 - 6 Marks]
**Question**:
Explain the multistage pipeline of the Canny edge detection algorithm in detail.

**Solution**:
The Canny edge detector achieves optimal edge detection through a five-stage pipeline:
1. **Gaussian Filtering**:
   Convolves the input image with a 2D Gaussian smoothing filter kernel $G(x, y, \sigma)$ to attenuate high-frequency noise that causes false edge detections.
2. **Gradient Calculation**:
   Applies horizontal and vertical Sobel masks to compute gradient components $G_x$ and $G_y$. The gradient magnitude $M = \sqrt{G_x^2 + G_y^2}$ and direction $\theta = \tan^{-1}(G_y / G_x)$ are calculated for every pixel.
3. **Non-Maximum Suppression (NMS)**:
   Thins wide gradient ridges into 1-pixel wide edge contours. Edge direction $\theta$ is rounded into one of four principal sectors ($0^\circ, 45^\circ, 90^\circ, 135^\circ$). If the pixel's magnitude is not strictly greater than its two neighbors along the gradient vector direction, it is suppressed to zero.
4. **Double Thresholding**:
   Applies two thresholds $T_{\text{high}}$ and $T_{\text{low}}$ (with $T_{\text{high}} \approx 2 \times T_{\text{low}}$):
   - $M \ge T_{\text{high}}$: Strong edge (definitely an edge).
   - $T_{\text{low}} \le M < T_{\text{high}}$: Weak edge (candidate edge).
   - $M < T_{\text{low}}$: Suppressed (noise).
5. **Edge Tracking by Hysteresis**:
   Retains a weak edge pixel in the final binary edge map if and only if it is 8-connected to a strong edge pixel. This links broken edge segments while filtering out spurious isolated noise spikes.

