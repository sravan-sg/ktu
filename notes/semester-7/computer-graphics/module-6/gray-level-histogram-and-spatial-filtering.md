# Gray Level Histograms & Spatial Filtering

## 1. Explanation
In digital image processing, image enhancement techniques operate directly on pixel intensities to improve visual contrast or extract features. These operations are partitioned into **point operations** (e.g. histogram processing) and **spatial neighborhood operations** (e.g. spatial convolution and correlation).

---

### Gray Level Histograms
The gray-level histogram of a digital image with intensity levels in the range $[0, L-1]$ is a discrete mathematical function:
$$h(r_k) = n_k$$
where:
- $r_k$: The $k^{\text{th}}$ intensity level ($k = 0, 1, \dots, L-1$). For an 8-bit image, $L = 256$ and $r_k \in [0, 255]$.
- $n_k$: The total number of pixels in the image with intensity level $r_k$.

#### Normalized Histogram (Probability Distribution Function - PDF)
Dividing by the total number of pixels $MN$ in the image yields the normalized histogram $p(r_k)$:
$$p(r_k) = \frac{n_k}{MN}, \quad \text{where } \sum_{k=0}^{L-1} p(r_k) = 1$$
$p(r_k)$ represents the empirical probability of occurrence of intensity level $r_k$.

---

### Histogram Equalization (Contrast Enhancement)
Histogram equalization is an automated method that transforms an image's intensity levels so that the output image has an approximately **uniform (flat)** probability distribution across the entire range $[0, L-1]$. This stretches contrast in crowded intensity bands, revealing hidden details in underexposed or overexposed images.

#### Continuous Derivation:
Let continuous variable $r \in [0, L-1]$ represent input image intensity, and $s \in [0, L-1]$ represent output intensity under a transformation function:
$$s = T(r)$$

Requirements on transformation $T(r)$:
1. $T(r)$ must be strictly monotonically increasing on $[0, L-1]$ ($T(r_1) < T(r_2)$ for $r_1 < r_2$) to preserve the relative brightness order of pixels.
2. $0 \le T(r) \le L-1$ for $0 \le r \le L-1$.

From probability theory, the probability density function (PDF) of $s$ is:
$$p_s(s) = p_r(r) \left| \frac{dr}{ds} \right|$$
To achieve a uniform output distribution, we demand:
$$p_s(s) = \frac{1}{L-1}$$
Equating and integrating:
$$\frac{ds}{dr} = (L-1) p_r(r) \implies s = T(r) = (L-1) \int_0^r p_r(w) dw$$
This is the **Cumulative Distribution Function (CDF)** of the input image scaled by $(L-1)$!

#### Discrete Formulation:
In a digital image with discrete levels, the transformation is expressed as:
$$\mathbf{s_k = T(r_k) = \text{round}\left( (L - 1) \sum_{j=0}^k p_r(r_j) \right) = \text{round}\left( \frac{L - 1}{MN} \sum_{j=0}^k n_j \right)}$$

---

### Spatial Filtering: Convolution vs. Correlation
Spatial filtering enhances or blurs images by moving a small matrix mask (kernel / filter) of size $m \times n$ (typically $3 \times 3$ or $5 \times 5$, with odd dimensions $m = 2a+1, n = 2b+1$) across every pixel in the image.

#### 1. Spatial Correlation
Correlation computes the inner product between the kernel and the image neighborhood:
$$g(x, y) = w(x, y) \star f(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) f(x + s, \ y + t)$$

#### 2. Spatial Convolution
Convolution is mathematically identical to correlation **except that the filter mask is rotated by $180^\circ$** before sliding over the image:
$$g(x, y) = w(x, y) * f(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) f(x - s, \ y - t)$$

> **Academic Insight**:
> If a spatial filter kernel is **symmetric** ($w(-s, -t) = w(s, t)$, such as Gaussian blur, box blur, or Laplacian masks), rotating by $180^\circ$ leaves the mask unchanged. For symmetric kernels:
> $$\text{Convolution} \equiv \text{Correlation}$$

---

## 2. Example: Histogram Equalization Transformation Function
```
Input Histogram p_r(r_k)                  Transformation Function s = T(r)             Output Histogram p_s(s_k)
       ▲                                         ▲                                            ▲
       │       * * *                             │                  * *                       │   * * * * * * *
       │     *       *                           │              * *                           │   * * * * * * *
       │   *           *                         │          * *                               │   * * * * * * *
       └───────────────────► r                   └─────────────────────► r                    └───────────────────► s
       Narrow, low-contrast                      Scaled Cumulative CDF                        Uniform, high-contrast
```

---

## 3. Applications & Use Cases
1. **Medical Diagnostic Imaging (X-Ray, Mammography)**: Raw X-ray radiograph images often suffer from narrow dynamic range due to soft-tissue absorption. Applying histogram equalization stretches bone and tissue density into visible contrast bands.
2. **Satellite Remote Sensing (Landsat, Sentinel)**: Optical multispectral sensors capture high-altitude imagery obscured by atmospheric haze. Spatial filtering (unsharp masking) and histogram equalization reveal fine ground features.
3. **Convolutional Neural Networks (CNNs)**: Modern computer vision deep learning models perform billions of 2D spatial convolution operations per second across multi-channel feature maps to extract hierarchical visual primitives.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Complete Discrete Histogram Equalization [KTU May 2019 / Jan 2023 - 9 Marks]
**Problem**:
An image with $L = 8$ gray levels ($r_k \in [0, 7]$) has size $64 \times 64$ pixels ($MN = 4096$).
The intensity distribution is given below:

| $r_k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $n_k$ | 790 | 1023 | 850 | 656 | 329 | 245 | 122 | 81 |

Perform discrete histogram equalization. Tabulate the probability distribution $p_r(r_k)$, cumulative distribution function, rounded transformation values $s_k$, and the resulting output histogram $n_{s_k}$.

**Step-by-step Solution**:
1. **Formula**:
   $$s_k = \text{round}\left( 7 \times \sum_{j=0}^k \frac{n_j}{4096} \right)$$

2. **Step-by-Step Tabulation**:

| $k$ | $r_k$ | $n_k$ | $p_r(r_k) = \frac{n_k}{4096}$ | Cumulative $\sum p_r$ | $(L-1) \times \text{CDF}$ | $s_k = \text{round}(\dots)$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 790 | $0.1929$ | $0.1929$ | $7 \times 0.1929 = 1.350$ | **1** |
| 1 | 1 | 1023 | $0.2498$ | $0.4427$ | $7 \times 0.4427 = 3.099$ | **3** |
| 2 | 2 | 850 | $0.2075$ | $0.6502$ | $7 \times 0.6502 = 4.551$ | **5** |
| 3 | 3 | 656 | $0.1602$ | $0.8104$ | $7 \times 0.8104 = 5.673$ | **6** |
| 4 | 4 | 329 | $0.0803$ | $0.8907$ | $7 \times 0.8907 = 6.235$ | **6** |
| 5 | 5 | 245 | $0.0598$ | $0.9505$ | $7 \times 0.9505 = 6.654$ | **7** |
| 6 | 6 | 122 | $0.0298$ | $0.9803$ | $7 \times 0.9803 = 6.862$ | **7** |
| 7 | 7 | 81 | $0.0197$ | $1.0000$ | $7 \times 1.0000 = 7.000$ | **7** |

3. **Output Gray Level Mapping**:
   - $r_0 = 0 \to s_0 = \mathbf{1}$ ($n = 790$)
   - $r_1 = 1 \to s_1 = \mathbf{3}$ ($n = 1023$)
   - $r_2 = 2 \to s_2 = \mathbf{5}$ ($n = 850$)
   - $r_3 = 3$ and $r_4 = 4$ both map to $s = \mathbf{6}$ ($n = 656 + 329 = 985$)
   - $r_5 = 5, r_6 = 6, r_7 = 7$ all map to $s = \mathbf{7}$ ($n = 245 + 122 + 81 = 448$)

4. **Resulting Equalized Histogram**:
   - Gray level 0: 0 pixels
   - Gray level 1: 790 pixels
   - Gray level 2: 0 pixels
   - Gray level 3: 1023 pixels
   - Gray level 4: 0 pixels
   - Gray level 5: 850 pixels
   - Gray level 6: 985 pixels
   - Gray level 7: 448 pixels
   Notice how the histogram is spread across the entire dynamic range $[0, 7]$, significantly increasing contrast.

---

### Example 2: Discrete 2D Spatial Convolution Trace [KTU Dec 2021 Pattern]
**Problem**:
Perform discrete 2D spatial convolution of the $3 \times 3$ image patch $F$ with the $3 \times 3$ filter kernel $W$ at center pixel $(2, 2)$:
$$F = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}, \quad W = \begin{bmatrix} 1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1 \end{bmatrix}$$

**Step-by-step Solution**:
1. **Rotate Kernel $W$ by $180^\circ$ for Convolution**:
   Rotating $W$ by $180^\circ$ gives $W_{\text{rot}}$:
   $$W_{\text{rot}} = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$
2. **Element-wise Multiplication and Summation**:
   $$G(2, 2) = \sum_{s=-1}^1 \sum_{t=-1}^1 W_{\text{rot}}(s, t) F(2+s, 2+t)$$
   $$\begin{aligned}
   G(2, 2) &= (-1 \times 1) + (0 \times 2) + (1 \times 3) \\
           &+ (-2 \times 4) + (0 \times 5) + (2 \times 6) \\
           &+ (-1 \times 7) + (0 \times 8) + (1 \times 9)
   \end{aligned}$$
   $$G(2, 2) = (-1 + 0 + 3) + (-8 + 0 + 12) + (-7 + 0 + 9)$$
   $$G(2, 2) = 2 + 4 + 2 = \mathbf{8}$$
3. Convolved output response at center pixel $= \mathbf{8}$.

---

### Example 3: Spatial Averaging and Noise Reduction [KTU Analytical Pattern]
**Problem**:
Explain how a $3 \times 3$ box filter (moving average filter) attenuates additive Gaussian zero-mean noise with variance $\sigma^2$. What is the noise variance in the filtered image?

**Step-by-step Solution**:
1. A $3 \times 3$ box filter mask is:
   $$W = \frac{1}{9} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$
2. The filtered pixel $g(x, y)$ is the average of 9 independent random variables:
   $$g(x, y) = \frac{1}{9} \sum_{i=1}^9 f_i$$
3. By probability theory, for independent identically distributed (i.i.d.) random variables, the variance of the average of $N$ variables is:
   $$\sigma_g^2 = \text{Var}\left(\frac{1}{N} \sum_{i=1}^N f_i\right) = \frac{1}{N^2} \sum_{i=1}^N \text{Var}(f_i) = \frac{N \sigma^2}{N^2} = \frac{\sigma^2}{N}$$
4. For $N = 9$:
   $$\sigma_g^2 = \frac{\sigma^2}{9}$$
   The filter reduces the noise variance by a factor of **9** (standard deviation is reduced by a factor of 3), effectively smoothing out random grain noise at the cost of blurring sharp edges.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / January 2023 - 6 Marks]
**Question**:
What is a gray level histogram? Explain the theoretical basis of histogram equalization.

**Solution**:
1. **Definition of Gray Level Histogram**:
   The gray-level histogram of an image with intensity levels in the range $[0, L-1]$ is a discrete function $h(r_k) = n_k$, where $r_k$ is the $k^{\text{th}}$ gray level and $n_k$ is the total count of pixels in the image with intensity $r_k$.
   The normalized histogram gives the probability density of intensities:
   $$p_r(r_k) = \frac{n_k}{MN}$$
2. **Theoretical Basis of Histogram Equalization**:
   - The goal is to construct an intensity transformation $s = T(r)$ such that the output probability distribution $p_s(s)$ is uniformly distributed across the full dynamic range $[0, L-1]$:
     $$p_s(s) = \frac{1}{L - 1} \quad \text{for } 0 \le s \le L-1$$
   - From probability transformation theory for continuous random variables:
     $$p_s(s) = p_r(r) \left| \frac{dr}{ds} \right|$$
   - Equating $p_s(s) = \frac{1}{L - 1}$:
     $$\frac{ds}{dr} = (L - 1) p_r(r)$$
   - Integrating both sides from 0 to $r$:
     $$s = T(r) = (L - 1) \int_0^r p_r(w) dw$$
   - This proves that **the ideal transformation function is directly proportional to the Cumulative Distribution Function (CDF)** of the input image. In discrete images, this is implemented as:
     $$s_k = \text{round}\left( (L - 1) \sum_{j=0}^k \frac{n_j}{MN} \right)$$

---

### Question 2 [KTU December 2020 / June 2024 - 4 Marks]
**Question**:
Distinguish between spatial convolution and spatial correlation in digital image processing.

**Solution**:
1. **Mathematical Distinction**:
   - **Spatial Correlation**: Slides a filter mask $w(s, t)$ over image $f(x, y)$ computing element-wise products directly:
     $$(w \star f)(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) f(x + s, \ y + t)$$
   - **Spatial Convolution**: First rotates the filter mask $w(s, t)$ by **$180^\circ$** before sliding over the image:
     $$(w * f)(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) f(x - s, \ y - t)$$
2. **Symmetric Filters**:
   If the kernel is symmetric across both axes ($w(-s, -t) = w(s, t)$, such as Gaussian or averaging filters), rotating by $180^\circ$ leaves the mask unchanged. In this case, convolution and correlation yield identical results.
3. **Application Distinction**:
   - Correlation is primarily used for **template matching** (finding where a target feature matches a subregion of an image).
   - Convolution is the fundamental operation of **linear shift-invariant (LSI) systems** and spatial filtering (e.g. edge detection, Gaussian blurring).

