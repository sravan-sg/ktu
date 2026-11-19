# Edge Detection Operators: Roberts, Prewitt, Sobel, Laplacian & Canny

## 1. Explanation

Edge detection is the foundational segmentation technique in digital image processing, computer vision, and machine perception. An **edge** is a local spatial discontinuity in image brightness—a localized boundary across which image pixel intensities exhibit a sharp, significant step change or steep gradient.

Edges correspond to physical real-world boundaries:
- Depth discontinuities (object occluding background)
- Surface normal orientation changes (creases, corners)
- Material property boundaries (albedo/color transitions)
- Illumination discontinuities (shadow boundaries)

---

### Mathematical Foundations: First-Order and Second-Order Derivatives

In continuous 2D space, intensity discontinuities are detected using spatial calculus:

```
        Intensity Profile f(x)             First Derivative f'(x)              Second Derivative f''(x)
           (Step Edge)                         (Gradient Peak)                    (Zero-Crossing)
                ▲                                   ▲                                   ▲
                │      ┌─────────                   │         ┌─┐                       │      /\
                │      │                            │        /   \                      │     /  \
                │      │                            │       /     \                     │────/────\────►
                │──────┘                            │───────┴─────┴─►                   │          \  /
                └───────────────►                   └───────────────►                   │           \/
```

#### 1. First-Order Derivative (The Gradient Vector)
The gradient of a 2D continuous image $f(x, y)$ is defined as the 2D spatial vector of first-order partial derivatives:
$$\nabla f = \begin{bmatrix} G_x \\ G_y \end{bmatrix} = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$

- **Gradient Magnitude ($M(x, y)$)**: Measures the rate of intensity change (edge strength):
  $$M(x, y) = |\nabla f| = \sqrt{G_x^2 + G_y^2} \approx |G_x| + |G_y|$$
- **Gradient Direction ($\alpha(x, y)$)**: The spatial angle of maximum rate of change (perpendicular to the edge boundary):
  $$\alpha(x, y) = \arctan\left(\frac{G_y}{G_x}\right)$$
  The edge boundary itself runs perpendicular to $\alpha(x, y)$ along angle $\theta = \alpha(x, y) \pm 90^\circ$.

#### 2. Second-Order Derivative (The Laplacian Operator)
The Laplacian is an isotropic, rotation-invariant second-order derivative:
$$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$
- An edge appears as a sharp **zero-crossing** (transition from a positive peak to a negative peak) in the second derivative.
- *Limitation*: The Laplacian is extremely sensitive to high-frequency image noise because differentiating twice doubles noise amplification.

---

### First-Order Gradient Operators: Roberts, Prewitt & Sobel

In digital images, derivatives are approximated by discrete spatial convolution masks (kernels).

#### 1. Roberts Cross-Gradient Operator ($2 \times 2$)
Proposed by Lawrence Roberts in 1963, this operator computes diagonal first-order differences:
$$G_x = f(x+1, y+1) - f(x, y)$$
$$G_y = f(x+1, y) - f(x, y+1)$$

Convolution Masks:
$$G_x = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$
- **Kernel Size**: $2 \times 2$ (smallest possible difference kernel).
- **Advantages**: Minimal computational overhead; very fast execution.
- **Disadvantages**: Highly sensitive to noise; lacks central symmetry; cannot average noise across multiple rows/columns.

---

#### 2. Prewitt Operator ($3 \times 3$)
Developed by Judith M. S. Prewitt in 1970, this operator combines **central difference differentiation** along one axis with **uniform unweighted box averaging** across three adjacent orthogonal lines to suppress high-frequency noise.

Convolution Masks:
$$G_x \text{ (Vertical Edge Detector / Horizontal Derivative)} = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}$$
$$G_y \text{ (Horizontal Edge Detector / Vertical Derivative)} = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$

- **Separability Property**:
  $$G_x = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \ast \begin{bmatrix} -1 & 0 & 1 \end{bmatrix}$$
  The column vector $\begin{bmatrix} 1 & 1 & 1 \end{bmatrix}^T$ performs smoothing; the row vector $\begin{bmatrix} -1 & 0 & 1 \end{bmatrix}$ computes the central difference derivative.

---

#### 3. Sobel Operator ($3 \times 3$)
Invented by Irwin Sobel and Gary Feldman in 1968, the Sobel operator replaces Prewitt's uniform smoothing with **weighted Gaussian-like triangular smoothing**, assigning a weight of $2$ to the center row/column:

$$G_x \text{ (Detects Vertical Edges / Horizontal Derivative)} = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$
$$G_y \text{ (Detects Horizontal Edges / Vertical Derivative)} = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$

- **Separability Property**:
  $$G_x = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \ast \begin{bmatrix} -1 & 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \ast \begin{bmatrix} 1 & 2 & 1 \end{bmatrix}$$

> **Why the Sobel Operator is Superior to the Prewitt Operator**:
> 1. **Superior Noise Suppression**: The binomial/Gaussian weighting coefficients $[1, 2, 1]^T$ act as an optimal discrete low-pass filter, significantly attenuating random sensor noise while preserving edge gradients.
> 2. **Better Gradient Angular Precision**: The central weight of $2$ produces a more accurate estimation of the true continuous gradient angle $\alpha(x, y)$, reducing directional quantization error.
> 3. **Reduced False Edges**: Prewitt's uniform weighting creates slight ringing and false edge responses around noisy pixels that Sobel smoothly suppresses.

---

### Comparative Evaluation of Gradient Edge Operators

| Property | Roberts Cross | Prewitt Operator | Sobel Operator | Laplacian Operator | Canny Operator |
|---|---|---|---|---|---|
| **Kernel Dimensions** | $2 \times 2$ | $3 \times 3$ | $3 \times 3$ | $3 \times 3$ or $5 \times 5$ | Multi-stage pipeline |
| **Derivative Order** | First-Order | First-Order | First-Order | Second-Order | First-Order Gaussian |
| **Noise Sensitivity** | **Extremely High** | Moderate | **Low** | Very High | **Minimal** |
| **Edge Thickness** | $\approx 1\text{–}2$ pixels | $\approx 2\text{–}3$ pixels | $\approx 2\text{–}3$ pixels | $1$ pixel (zero-crossing) | **Strictly $1$ pixel** (thin) |
| **Computational Cost** | Ultra-Low ($4$ ops) | Low ($6$ adds, $0$ mults)| Low ($6$ adds, shifts) | Low | High (multi-pass) |
| **Output Type** | Gradient Magnitude | Gradient Magnitude | Gradient Magnitude | Zero-Crossings | Binary Edge Map |

---

### The Canny Edge Detector: The Mathematically Optimal Detector

Formulated by John F. Canny in 1986, the Canny edge detection algorithm was derived mathematically by optimizing three performance criteria:
1. **Low Error Rate**: High probability of detecting true edge points; minimum probability of marking non-edge noise.
2. **Optimal Localization**: Distance between detected edge points and actual physical edge centers must be minimized.
3. **Single Response Constraint**: Only one response per true edge (elimination of thick, smeared multi-pixel bands).

```
                      THE 5-STAGE CANNY EDGE PIPELINE
                      
┌───────────────────────┐
│  Input Noisy Image    │
└──────────┬────────────┘
           │ Stage 1: Gaussian Filtering (Noise suppression)
           ▼
┌───────────────────────┐
│ Smooth Image I_sigma  │
└──────────┬────────────┘
           │ Stage 2: Sobel Convolution (Compute |G| and angle alpha)
           ▼
┌───────────────────────┐
│ Gradient Map & Angles │
└──────────┬────────────┘
           │ Stage 3: Non-Maximum Suppression (Thin edges to 1-pixel width)
           ▼
┌───────────────────────┐
│ Thinned Edge Peaks    │
└──────────┬────────────┘
           │ Stage 4: Double Thresholding (Classify Strong vs. Weak edges)
           ▼
┌───────────────────────┐
│ Hysteresis Candidates │
└──────────┬────────────┘
           │ Stage 5: Edge Tracking by Hysteresis (Link 8-connected weak edges)
           ▼
┌───────────────────────┐
│ Clean Binary Edge Map │
└───────────────────────┘
```

#### Detailed Stage Operations:
1. **Stage 1: Gaussian Smoothing**:
   Convolve the raw image with a symmetric 2D Gaussian kernel to suppress high-frequency noise:
   $$G_\sigma(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}$$
2. **Stage 2: Gradient Magnitude & Angle Calculation**:
   Apply Sobel kernels $G_x$ and $G_y$ to compute magnitude $M(x, y) = \sqrt{G_x^2 + G_y^2}$ and angle $\theta = \arctan(G_y/G_x)$. Round the angle $\theta$ to the nearest of **four discretized sectors**:
   - $0^\circ$ (Horizontal edge $\implies$ gradient points North-South: $90^\circ$)
   - $45^\circ$ (Diagonal)
   - $90^\circ$ (Vertical edge $\implies$ gradient points East-West: $0^\circ$)
   - $135^\circ$ (Anti-diagonal)
3. **Stage 3: Non-Maximum Suppression (NMS)**:
   Thin the smeared gradient ridges down to sharp, 1-pixel-wide lines:
   - For pixel $p(x, y)$, compare its gradient magnitude $M(p)$ with the two adjacent neighbor pixels along the gradient direction $\theta$.
   - If $M(p)$ is strictly greater than both neighbors along the gradient vector, preserve it; otherwise, suppress it (set to $0$).
4. **Stage 4: Double Thresholding**:
   Apply two thresholds $T_{\text{high}}$ and $T_{\text{low}}$ (typically $T_{\text{low}} \approx 0.4 \times T_{\text{high}}$):
   - If $M(x, y) \ge T_{\text{high}}$: Mark as **Strong Edge**.
   - If $T_{\text{low}} \le M(x, y) < T_{\text{high}}$: Mark as **Weak Edge**.
   - If $M(x, y) < T_{\text{low}}$: Suppress as **Non-Edge (Noise)**.
5. **Stage 5: Edge Tracking by Hysteresis**:
   Retain weak edge pixels **only if** they are connected to a strong edge pixel via an 8-connected digital path. Isolated weak pixels are discarded as noise.

---

### Linear Gray Level Transformation

A standard linear gray-level transformation remaps an input image $g_1(x, y)$ whose intensities occupy a dynamic range $[a, b]$ into an output image $g_2(x, y)$ spanning a new specified range $[c, d]$.

```
               Output Intensity g2
                      ▲
                    d │                    * (b, d)
                      │                   /
                      │                  /
                      │                 /
                    c │          * (a, c)
                      │          │
                      └──────────┴─────────┴─────────► Input Intensity g1
                      0          a         b
```

#### Algebraic Derivation:
We seek a linear function:
$$g_2(x, y) = \alpha \cdot g_1(x, y) + \beta$$
satisfying the boundary boundary conditions:
1. When $g_1 = a \implies g_2 = c$
2. When $g_1 = b \implies g_2 = d$

Substituting into the linear equation:
$$c = \alpha \cdot a + \beta \quad \text{--- (1)}$$
$$d = \alpha \cdot b + \beta \quad \text{--- (2)}$$

Subtracting equation (1) from equation (2):
$$d - c = \alpha(b - a) \implies \alpha = \frac{d - c}{b - a}$$

Solving for $\beta$ using equation (1):
$$\beta = c - \alpha \cdot a = c - \left(\frac{d - c}{b - a}\right) a$$

Substituting $\alpha$ and $\beta$ into the linear transformation equation:
$$g_2(x, y) = \left(\frac{d - c}{b - a}\right) g_1(x, y) + c - \left(\frac{d - c}{b - a}\right) a$$
$$g_2(x, y) = \left(\frac{d - c}{b - a}\right) \left[ g_1(x, y) - a \right] + c$$

*Application*: Used in **Contrast Stretching** when an image is underexposed ($a = 50, b = 120$) to expand its dynamic range to fill the full 8-bit monitor gamut ($c = 0, d = 255$).

---

## 2. Example: Concrete Numerical Convolution Walkthrough

Consider a $3 \times 3$ image neighborhood centered at pixel $(1, 1)$ [0-indexed]:
$$f = \begin{bmatrix} 10 & 20 & 30 \\ 15 & 25 & 35 \\ 20 & 30 & 40 \end{bmatrix}$$

---

### 1. Roberts Cross Operator Calculation (at top-left $2 \times 2$ sub-window)
$$\text{Sub-window} = \begin{bmatrix} 10 & 20 \\ 15 & 25 \end{bmatrix}$$
$$G_x = f(1, 1) - f(0, 0) = 25 - 10 = +15$$
$$G_y = f(0, 1) - f(1, 0) = 20 - 15 = +5$$
$$M_{\text{Roberts}} \approx |G_x| + |G_y| = |15| + |5| = 20$$

---

### 2. Prewitt Operator Calculation (at central pixel $(1, 1)$)
$$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix} \ast \begin{bmatrix} 10 & 20 & 30 \\ 15 & 25 & 35 \\ 20 & 30 & 40 \end{bmatrix}$$
$$G_x = (-1)(10) + (1)(30) + (-1)(15) + (1)(35) + (-1)(20) + (1)(40)$$
$$G_x = (-10 + 30) + (-15 + 35) + (-20 + 40) = 20 + 20 + 20 = +60$$

$$G_y = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix} \ast \begin{bmatrix} 10 & 20 & 30 \\ 15 & 25 & 35 \\ 20 & 30 & 40 \end{bmatrix}$$
$$G_y = (-1)(10) + (-1)(20) + (-1)(30) + (1)(20) + (1)(30) + (1)(40)$$
$$G_y = (-60) + (90) = +30$$

$$M_{\text{Prewitt}} = |G_x| + |G_y| = |60| + |30| = 90$$

---

### 3. Sobel Operator Calculation (at central pixel $(1, 1)$)
$$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix} \ast \begin{bmatrix} 10 & 20 & 30 \\ 15 & 25 & 35 \\ 20 & 30 & 40 \end{bmatrix}$$
$$G_x = (-1)(10) + (1)(30) + (-2)(15) + (2)(35) + (-1)(20) + (1)(40)$$
$$G_x = 20 + (-30 + 70) + 20 = 20 + 40 + 20 = +80$$

$$G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix} \ast \begin{bmatrix} 10 & 20 & 30 \\ 15 & 25 & 35 \\ 20 & 30 & 40 \end{bmatrix}$$
$$G_y = (-1)(10) + (-2)(20) + (-1)(30) + (1)(20) + (2)(30) + (1)(40)$$
$$G_y = (-10 - 40 - 30) + (20 + 60 + 40) = -80 + 120 = +40$$

$$M_{\text{Sobel}} = \sqrt{G_x^2 + G_y^2} = \sqrt{80^2 + 40^2} = \sqrt{6400 + 1600} = \sqrt{8000} \approx 89.44$$
$$M_{\text{Sobel, approx}} = |80| + |40| = 120$$
$$\text{Gradient Angle } \alpha = \arctan\left(\frac{40}{80}\right) = \arctan(0.5) \approx 26.57^\circ$$

---

## 3. Applications & Use Cases

1. **Autonomous Vehicle Lane Departure Systems**:
   Cameras mounted on vehicle windshields apply Sobel vertical edge detection ($G_x$) combined with Hough Transforms to detect painted highway lane boundaries in real time.
2. **Medical Radiography Bone Fracture Detection**:
   Canny edge detection isolates micro-fracture cortical bone cracks in X-ray and CT imaging where low-contrast boundaries must be traced without noise false positives.
3. **Facial Feature Landmark Tracking & Biometrics**:
   Face recognition algorithms locate eye sockets, lip contours, and jawlines by applying gradient operators across multi-scale pyramids.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Gray Level Transformation Numerical Problem [KTU Dec 2018 Q18b]
**Problem**:
An image $g_1(x, y)$ has gray levels ranging from $a = 40$ to $b = 140$. It is required to expand its contrast to cover the range $c = 0$ to $d = 255$ in the output image $g_2(x, y)$ using a linear transformation.
1. Derive the linear mapping equation.
2. Find the output gray level for an input pixel having intensity $g_1(x, y) = 80$.

**Solution**:
1. **Derivation**:
   Using the formula derived in Section 1:
   $$g_2(x, y) = \left(\frac{d - c}{b - a}\right) [g_1(x, y) - a] + c$$
   Given $a = 40, b = 140, c = 0, d = 255$:
   $$\frac{d - c}{b - a} = \frac{255 - 0}{140 - 40} = \frac{255}{100} = 2.55$$
   $$g_2(x, y) = 2.55 \cdot [g_1(x, y) - 40] + 0 = 2.55 \cdot g_1(x, y) - 102$$

2. **Compute for $g_1(x, y) = 80$**:
   $$g_2(x, y) = 2.55(80 - 40) = 2.55(40) = 102$$
   **Result**: Input intensity $80$ is mapped to output intensity $102$.

---

### Example 2: Sobel Edge Detection on Binary Edge Profile [Analytical Problem]
**Problem**:
A vertical step edge is represented in a $3 \times 3$ grid where the left column is $10$ and the center/right columns are $80$:
$$f = \begin{bmatrix} 10 & 80 & 80 \\ 10 & 80 & 80 \\ 10 & 80 & 80 \end{bmatrix}$$
Evaluate the Sobel gradient vector $\nabla f = [G_x, G_y]^T$, magnitude, and angle at the center pixel.

**Solution**:
$$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix} \ast \begin{bmatrix} 10 & 80 & 80 \\ 10 & 80 & 80 \\ 10 & 80 & 80 \end{bmatrix}$$
$$G_x = [(-1)(10) + (1)(80)] + [(-2)(10) + (2)(80)] + [(-1)(10) + (1)(80)]$$
$$G_x = 70 + 140 + 70 = +280$$

$$G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix} \ast \begin{bmatrix} 10 & 80 & 80 \\ 10 & 80 & 80 \\ 10 & 80 & 80 \end{bmatrix}$$
Because each column is vertically constant ($10, 10, 10$ and $80, 80, 80$), row 0 and row 2 are identical:
$$G_y = (-1)(10) + (-2)(80) + (-1)(80) + (1)(10) + (2)(80) + (1)(80) = -250 + 250 = 0$$

- **Gradient Vector**: $\nabla f = \begin{bmatrix} 280 & 0 \end{bmatrix}^T$.
- **Magnitude**: $M = \sqrt{280^2 + 0^2} = 280$.
- **Angle**: $\alpha = \arctan(0 / 280) = 0^\circ$ (points horizontally across the edge; true edge runs at $90^\circ$ vertically).

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [June 2024 Q10 / June 2024 Q19b / Dec 2023 Q18b / Jan 2023 Q96 — 4–8 Marks]
**Question**:
Explain the Sobel edge detector in detail. Why is it preferred over the Prewitt edge detector?

**Solution**:

The **Sobel Edge Detector** is a first-order differential spatial convolution operator that computes an approximation of the gradient of image intensity.

**1. Convolution Masks**:
The operator uses two $3 \times 3$ masks convolved with the image:
$$G_x \text{ (Horizontal Derivative / Detects Vertical Edges)} = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$
$$G_y \text{ (Vertical Derivative / Detects Horizontal Edges)} = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$

**2. Gradient Vector Computation**:
For any pixel $(x, y)$, convolution yields $G_x$ and $G_y$:
- **Gradient Magnitude (Edge Strength)**:
  $$M(x, y) = \sqrt{G_x^2 + G_y^2} \approx |G_x| + |G_y|$$
- **Gradient Orientation**:
  $$\alpha(x, y) = \arctan\left(\frac{G_y}{G_x}\right)$$

**3. Why Sobel is Preferred Over Prewitt**:
- The Prewitt operator uses uniform weights in its smoothing kernel: $\begin{bmatrix} 1 & 1 & 1 \end{bmatrix}^T$.
- The Sobel operator uses triangular/Gaussian-like weights: $\begin{bmatrix} 1 & 2 & 1 \end{bmatrix}^T$.
- **Superior Noise Suppression**: Assigning a weight of $2$ to the central row/column gives maximum influence to the pixel directly orthogonal to the edge, effectively smoothing random high-frequency noise spikes before computing differences.
- **Accurate Angle Estimation**: Sobel's weighting minimizes diagonal angular distortion, resulting in more accurate edge angle $\alpha(x, y)$ estimations.

---

### Question 2 [Dec 2019 Q19a / May 2019 Q18b / Dec 2018 Q19a — 6 Marks]
**Question**:
Explain the Roberts, Prewitt, and Sobel edge detectors.

**Solution**:

All three operators are first-order gradient approximations designed to detect spatial intensity discontinuities:

1. **Roberts Cross-Gradient Operator ($2 \times 2$)**:
   Computes diagonal differences across a $2 \times 2$ pixel window:
   $$G_x = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$
   - *Advantage*: Minimal computation; high execution speed.
   - *Limitation*: Highly sensitive to image noise due to small aperture and lack of spatial averaging.

2. **Prewitt Operator ($3 \times 3$)**:
   Combines unweighted box averaging with central differences:
   $$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$
   - *Advantage*: Smooths noise across 3 adjacent rows/columns before computing differences.

3. **Sobel Operator ($3 \times 3$)**:
   Incorporates weighted Gaussian-like smoothing ($[1, 2, 1]^T$) with central differences:
   $$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$
   - *Advantage*: Highest noise immunity and best gradient orientation accuracy among $3 \times 3$ linear difference filters.

---

### Question 3 [Dec 2018 Q18b — 4 Marks]
**Question**:
The gray levels in an image $g_1(x, y)$ range from $a$ to $b$. It is decided to change it into an image $g_2(x, y)$ in which the gray levels range from $c$ to $d$ using a linear transformation of its gray levels. Derive the equation for $g_2(x, y)$ as a function of $g_1(x, y)$ by specifying the steps.

**Solution**:

Let the linear transformation relationship between input gray level $g_1(x, y)$ and output gray level $g_2(x, y)$ be defined as:
$$g_2(x, y) = m \cdot g_1(x, y) + k \quad \text{--- (Equation 1)}$$
where $m$ is the slope (scaling factor) and $k$ is the intercept offset.

**Step 1: Formulate Boundary Conditions**:
The problem specifies that the minimum input intensity $a$ must map to the minimum output intensity $c$, and the maximum input intensity $b$ must map to the maximum output intensity $d$:
1. $g_2 = c$ when $g_1 = a \implies c = m \cdot a + k \quad \text{--- (Equation 2)}$
2. $g_2 = d$ when $g_1 = b \implies d = m \cdot b + k \quad \text{--- (Equation 3)}$

**Step 2: Solve for Slope $m$**:
Subtract Equation 2 from Equation 3:
$$d - c = (m \cdot b + k) - (m \cdot a + k)$$
$$d - c = m(b - a)$$
$$m = \frac{d - c}{b - a} \quad \text{--- (Equation 4)}$$

**Step 3: Solve for Intercept $k$**:
From Equation 2:
$$k = c - m \cdot a$$
Substituting the value of $m$ from Equation 4:
$$k = c - \left(\frac{d - c}{b - a}\right) a \quad \text{--- (Equation 5)}$$

**Step 4: Formulate Final Equation**:
Substitute $m$ and $k$ into Equation 1:
$$g_2(x, y) = \left(\frac{d - c}{b - a}\right) g_1(x, y) + c - \left(\frac{d - c}{b - a}\right) a$$
Factoring out the term $\left(\frac{d - c}{b - a}\right)$:
$$g_2(x, y) = \left(\frac{d - c}{b - a}\right) \left[ g_1(x, y) - a \right] + c$$
This is the required linear transformation formula.

---

### Question 4 [Dec 2021 Q10 — 4 Marks]
**Question**:
Explain the steps involved in edge detection.

**Solution**:

A robust edge detection system (exemplified by the Canny edge detector) executes the following sequential steps:

1. **Filtering & Noise Smoothing**:
   Raw images contain high-frequency sensor noise that causes false derivative peaks. Convolving the image with a low-pass Gaussian smoothing filter ($G_\sigma$) suppresses noise while preserving primary edge boundaries.
2. **Gradient Differentiation**:
   Spatial convolution masks (such as Sobel $G_x$ and $G_y$) compute the spatial gradient vector $\nabla f = [G_x, G_y]^T$, yielding the gradient magnitude $M(x, y) = \sqrt{G_x^2 + G_y^2}$ and gradient angle $\alpha(x, y) = \arctan(G_y/G_x)$.
3. **Non-Maximum Suppression (Edge Thinning)**:
   Gradient differentiation produces thick, blurred edge bands. Non-maximum suppression checks pixels along the gradient direction and suppresses all pixels that are not local maxima, thinning edges down to 1-pixel-wide lines.
4. **Hysteresis Thresholding**:
   Applies two thresholds ($T_{\text{high}}$ and $T_{\text{low}}$) to eliminate false edges caused by residual noise. Pixels with gradient $> T_{\text{high}}$ are marked as strong edges. Pixels between $T_{\text{low}}$ and $T_{\text{high}}$ are marked as weak edges. Weak edges are preserved only if connected to strong edges via 8-connected paths.
