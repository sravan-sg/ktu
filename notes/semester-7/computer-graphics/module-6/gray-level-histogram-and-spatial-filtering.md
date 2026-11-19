# Gray-Level Histogram, Histogram Equalization & Spatial Filtering

## 1. Explanation

In digital image processing, spatial domain techniques operate directly on image pixels:
$$g(x, y) = T[f(x, y)]$$
where $f(x, y)$ is the input image, $g(x, y)$ is the processed output image, and $T$ is an operator defined over a spatial neighborhood surrounding $(x, y)$.

When the neighborhood is a single pixel ($1 \times 1$), the transformation depends strictly on pixel intensity, giving rise to **point operations** and **histogram processing**. When the neighborhood encompasses surrounding pixels ($3 \times 3$, $5 \times 5$), the transformation represents **spatial filtering** (convolution).

---

### The Image Histogram: Formal Definition & Interpretation

The **histogram** of a digital image with gray levels in the range $[0, L-1]$ is a discrete frequency function:
$$h(r_k) = n_k$$
where:
- $r_k$ is the $k$-th gray level ($k \in \{0, 1, \dots, L-1\}$).
- $n_k$ is the total number of pixels in the image possessing gray level $r_k$.

#### Normalized Histogram (Probability Mass Function)
Dividing each frequency $n_k$ by the total number of pixels in the image ($M \times N$) yields the **normalized histogram**:
$$p(r_k) = \frac{n_k}{M \cdot N}, \quad k = 0, 1, \dots, L-1$$
- $p(r_k)$ represents the empirical probability of occurrence of gray level $r_k$.
- $\sum_{k=0}^{L-1} p(r_k) = 1$, and $p(r_k) \ge 0$ for all $k$.

```
    Dark Image                   Bright Image                 Low-Contrast Image           High-Contrast Image
       p(rk)                        p(rk)                        p(rk)                        p(rk)
     ▲                            ▲                            ▲                            ▲
     │ █                          │         █                  │       ███                  │ █  █   █  █  █
     │ ██                         │        ██                  │      █████                 │ █████ ███████
     │ ███                        │       ███                  │       ███                  │ █████████████
     └─────┴───────► r            └───────┴───► r              └───────┴───► r              └──────────────► r
     0           L-1              0         L-1                0         L-1                0            L-1
```

- **Dark Image**: Histogram components are concentrated toward the lower (dark) end near $0$.
- **Bright Image**: Histogram components are clustered toward the higher (bright) end near $L-1$.
- **Low-Contrast Image**: Histogram is compressed into a narrow band in the middle of the scale.
- **High-Contrast Image**: Histogram spans broadly and uniformly across the entire dynamic range from $0$ to $L-1$.

---

### Histogram Equalization (HE)

**Histogram Equalization** is an automated, non-linear transformation that flattens and stretches an image's dynamic range so that the resulting histogram approximates a **uniform probability distribution**, maximizing global image contrast.

#### 1. Continuous Mathematical Derivation
Let continuous variable $r$ represent input gray levels, normalized such that $0 \le r \le 1$.
We seek a monotonic transformation $s = T(r)$ mapping $r \in [0, 1]$ to output $s \in [0, 1]$ such that:
1. $T(r)$ is strictly monotonically increasing ($dT/dr > 0$) to preserve relative brightness ordering.
2. $0 \le T(r) \le 1$ for $0 \le r \le 1$.

From elementary probability theory, the probability density function (PDF) of the transformed variable $s$ is related to $p_r(r)$ by:
$$p_s(s) = p_r(r) \left| \frac{dr}{ds} \right| = \frac{p_r(r)}{\frac{ds}{dr}}$$

We choose the **Cumulative Distribution Function (CDF)** of $r$ as the transformation function $T(r)$:
$$s = T(r) = \int_0^r p_r(w) \, dw$$
Differentiating $s$ with respect to $r$ using the Fundamental Theorem of Calculus:
$$\frac{ds}{dr} = \frac{d}{dr} \left[ \int_0^r p_r(w) \, dw \right] = p_r(r)$$

Substituting this derivative into the PDF formula:
$$p_s(s) = \frac{p_r(r)}{p_r(r)} = 1, \quad 0 \le s \le 1$$
**Conclusion**: The output PDF $p_s(s)$ is a constant ($1.0$), proving that transforming continuous gray levels by their cumulative distribution function produces a **perfectly uniform distribution**.

---

#### 2. Discrete Histogram Equalization Formula
In discrete digital images, integrals are replaced by summations:
$$s_k = T(r_k) = \text{round}\left( (L - 1) \sum_{j=0}^k p_r(r_j) \right) = \text{round}\left( \frac{L - 1}{M \cdot N} \sum_{j=0}^k n_j \right)$$
where:
- $\sum_{j=0}^k n_j$ is the cumulative pixel count up to gray level $r_k$.
- $(L - 1)$ scales the normalized cumulative sum into the dynamic integer range $[0, L-1]$.
- $\text{round}(\cdot)$ quantizes the continuous value to the nearest integer.

---

### Spatial Filtering: Convolution vs. Correlation

A spatial filter consists of a neighborhood (typically a small $3 \times 3$ or $5 \times 5$ matrix of coefficients called a **filter mask**, **kernel**, or **window**) and an operation executed over that neighborhood.

```
       Image Neighborhood f(x, y)                      Filter Kernel w(s, t)
    ┌──────────┬──────────┬──────────┐              ┌──────────┬──────────┬──────────┐
    │ f(x-1,y-1│ f(x-1, y)│ f(x-1,y+1│              │ w(-1,-1) │ w(-1, 0) │ w(-1, 1) │
    ├──────────┼──────────┼──────────┤              ├──────────┼──────────┼──────────┤
    │ f(x, y-1)│ f(x, y)  │ f(x, y+1)│       *      │ w(0, -1) │ w(0, 0)  │ w(0, 1)  │
    ├──────────┼──────────┼──────────┤              ├──────────┼──────────┼──────────┤
    │ f(x+1,y-1│ f(x+1, y)│ f(x+1,y+1│              │ w(1, -1) │ w(1, 0)  │ w(1, 1)  │
    └──────────┴──────────┴──────────┘              └──────────┴──────────┴──────────┘
```

#### 1. Spatial Correlation
Correlation slides the kernel across the image and computes the sum of products directly:
$$g(x, y) = w(x, y) \circ f(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) \cdot f(x+s, y+t)$$

#### 2. Spatial Convolution
Convolution is identical to correlation, except the filter mask is **rotated by $180^\circ$** before sliding:
$$g(x, y) = w(x, y) \ast f(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) \cdot f(x-s, y-t)$$
*Note*: If the filter mask is spatially symmetric (such as Gaussian or box filters where $w(s, t) = w(-s, -t)$), correlation and convolution produce mathematically identical results.

---

### Classification of Spatial Filters

#### 1. Smoothing (Low-Pass) Linear Spatial Filters
Used for noise reduction, artifact suppression, and blurring of fine details prior to object extraction:
- **Standard Box / Mean Filter ($3 \times 3$)**:
  $$w_{\text{box}} = \frac{1}{9} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$
  Replaces each pixel with the arithmetic mean of its neighborhood.
- **Weighted Gaussian Smoothing Filter ($3 \times 3$)**:
  $$w_{\text{gauss}} = \frac{1}{16} \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$$
  Weights pixels inversely proportional to distance from the center, preserving edge sharpness better than a uniform box filter.

#### 2. Order-Statistic (Non-Linear) Spatial Filters
Order-statistic filters sort the pixels contained within the filter sub-window and replace the center pixel with a rank-ordered value:
- **Median Filter**:
  $$R = \text{median}\{f(x+s, y+t)\}$$
  - **Superlative Noise Immunity**: Highly effective at eliminating **salt-and-pepper (impulse) noise** while causing **drastically less blurring of sharp edges** than linear low-pass averaging filters.
- **Max Filter**: Replaces center with the maximum value (erodes dark spots, expands bright regions).
- **Min Filter**: Replaces center with the minimum value (erodes bright spots, expands dark regions).

#### 3. Sharpening (High-Pass) Spatial Filters
Highlight fine transitions and edge details by calculating spatial second derivatives:
- **The Laplacian Filter ($3 \times 3$)**:
  $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} \approx [f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1)] - 4f(x, y)$$
  $$w_{\text{lap4}} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \quad w_{\text{lap8}} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & -8 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$
- **Laplacian Image Enhancement**:
  $$g(x, y) = f(x, y) - \nabla^2 f(x, y) \implies w_{\text{sharp}} = \begin{bmatrix} 0 & -1 & 0 \\ -1 & 5 & -1 \\ 0 & -1 & 0 \end{bmatrix}$$

---

## 2. Example: Complete Histogram Equalization Walkthrough

**Problem**:
A $4 \times 4$ image ($M \times N = 16$ pixels) with $L = 8$ gray levels (range $[0, 7]$) has the following pixel distribution:
$$f = \begin{bmatrix} 1 & 1 & 2 & 3 \\ 1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 5 \\ 3 & 4 & 5 & 6 \end{bmatrix}$$
Perform histogram equalization. Compute the transformation table, equalized gray levels, and compare initial vs. final histograms.

---

### Step 1: Compute Frequency Table and Normalized Probabilities
Count occurrences of each gray level $r_k \in [0, 7]$:
- $r_0 = 0$: $n_0 = 0$
- $r_1 = 1$: $n_1 = 3$
- $r_2 = 2$: $n_2 = 3$
- $r_3 = 3$: $n_3 = 4$
- $r_4 = 4$: $n_4 = 3$
- $r_5 = 5$: $n_5 = 2$
- $r_6 = 6$: $n_6 = 1$
- $r_7 = 7$: $n_7 = 0$
Total pixels $M \cdot N = 16$.

### Step 2: Evaluate Discrete Histogram Equalization Formula
$$s_k = \text{round}\left( \frac{L - 1}{M \cdot N} \sum_{j=0}^k n_j \right) = \text{round}\left( \frac{7}{16} \sum_{j=0}^k n_j \right) = \text{round}\left( 0.4375 \sum_{j=0}^k n_j \right)$$

| $k$ | $r_k$ | $n_k$ | $p(r_k) = n_k/16$ | Cumulative Sum $\sum n_j$ | $s_k = 0.4375 \times \sum n_j$ | Output Gray Level $s_k$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0.0000 | 0 | $0.000$ | **0** |
| 1 | 1 | 3 | 0.1875 | 3 | $1.3125$ | **1** |
| 2 | 2 | 3 | 0.1875 | 6 | $2.6250$ | **3** |
| 3 | 3 | 4 | 0.2500 | 10 | $4.3750$ | **4** |
| 4 | 4 | 3 | 0.1875 | 13 | $5.6875$ | **6** |
| 5 | 5 | 2 | 0.1250 | 15 | $6.5625$ | **7** |
| 6 | 6 | 1 | 0.0625 | 16 | $7.0000$ | **7** |
| 7 | 7 | 0 | 0.0000 | 16 | $7.0000$ | **7** |

### Step 3: Mapping Mapping Function
- Gray level $1 \to 1$
- Gray level $2 \to 3$
- Gray level $3 \to 4$
- Gray level $4 \to 6$
- Gray levels $5, 6 \to 7$

### Step 4: Transformed Equalized Image Matrix
$$g = \begin{bmatrix} 1 & 1 & 3 & 4 \\ 1 & 3 & 4 & 6 \\ 3 & 4 & 6 & 7 \\ 4 & 6 & 7 & 7 \end{bmatrix}$$

Notice that original gray levels $1\text{–}6$ (compressed in middle range) are now broadly stretched across the full gamut $[1, 7]$.

---

## 3. Applications & Use Cases

1. **Medical Diagnostic Radiology (Chest X-Rays / Mammography)**:
   Soft tissue structures in raw digital radiographs exhibit extremely narrow dynamic contrast (pale gray bands). Applying adaptive histogram equalization (CLAHE) dramatically enhances lung nodule visibility without blowing out rib bone contours.
2. **Satellite & Remote Sensing Surface Analysis**:
   Optical multispectral imagery captured under atmospheric haze exhibits compressed histograms. Histogram equalization stretches thermal and vegetation reflectance bands to differentiate crop health.
3. **Low-Light Night Vision Image Enhancement**:
   Surveillance cameras operating in near-dark conditions stretch photon-starved histograms to restore visibility for human security operators.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Full Frequency Table and Histogram Generation [KTU Dec 2021 Q9]
**Problem**:
Given the simple $5 \times 5$ image:
```
2   1   2   3   2
3   2   2   4   3
1   3   5   4   3
3   4   5   6   7
2   2   6   7   5
```
Write its frequency table and draw its histogram.

**Solution**:
Total pixels: $M \times N = 5 \times 5 = 25$ pixels.
Gray levels present range from $1$ to $7$.

**Frequency Table**:
| Gray Level ($r_k$) | Pixel Occurrences ($n_k$) | Normalized Probability $p(r_k) = n_k/25$ |
|---|---|---|
| **0** | 0 | $0.00$ |
| **1** | 2 | $0.08$ |
| **2** | 7 | $0.28$ |
| **3** | 6 | $0.24$ |
| **4** | 3 | $0.12$ |
| **5** | 3 | $0.12$ |
| **6** | 2 | $0.08$ |
| **7** | 2 | $0.08$ |
| **Total** | **25** | **1.00** |

**Textual Histogram Representation**:
```
  n_k
   ▲
 7 │        █
 6 │        █    █
 5 │        █    █
 4 │        █    █
 3 │        █    █    █    █
 2 │   █    █    █    █    █    █    █
 1 │   █    █    █    █    █    █    █
 0 └───┴────┴────┴────┴────┴────┴────┴────► r_k
       1    2    3    4    5    6    7
```
The histogram exhibits a unimodal distribution with a prominent peak at gray level $2$, characteristic of a slightly dark, low-contrast image.

---

### Example 2: Median vs. Mean Filtering on Impulse Noise [Analytical Problem]
**Problem**:
A $3 \times 3$ image neighborhood contains a single salt-and-pepper noise spike of intensity $255$ surrounded by dark background pixels:
$$f = \begin{bmatrix} 12 & 14 & 13 \\ 11 & 255 & 15 \\ 14 & 13 & 12 \end{bmatrix}$$
Evaluate the response of:
(a) A $3 \times 3$ arithmetic mean filter.
(b) A $3 \times 3$ median filter.

**Solution**:
1. **Arithmetic Mean Filter**:
   $$\text{Sum} = 12 + 14 + 13 + 11 + 255 + 15 + 14 + 13 + 12 = 359$$
   $$\text{Output} = \text{round}\left(\frac{359}{9}\right) = 40$$
   *Analysis*: The noise spike $255$ corrupts the entire neighborhood, pulling the dark pixel from $\approx 13$ up to $40$, creating a visible blurred halo.

2. **Median Filter**:
   Sort the $9$ pixel values in ascending order:
   $$\text{Sorted} = [11, \ 12, \ 12, \ 13, \ \mathbf{13}, \ 14, \ 14, \ 15, \ 255]$$
   The median (5th element) is $\mathbf{13}$.
   $$\text{Output} = 13$$
   *Analysis*: The impulse noise spike $255$ is **completely eradicated**, restoring the true background intensity of $13$ perfectly without any blurring!

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [Dec 2023 Q19b / Jan 2023 Q94b / June 2022 Q19b / Dec 2020 Q18a / May 2019 Q19b / Dec 2018 Q18b — 6–8 Marks]
**Question**:
What do you understand by histogram equalization of an image? Illustrate with a suitable example.

**Solution**:

**Definition**:
**Histogram Equalization** is a spatial-domain point transformation method that dynamically remaps the gray levels of an image such that the resulting output image exhibits a nearly **uniform probability distribution** across its full dynamic range. It automatically enhances contrast in images with clustered or narrow histograms.

**Mathematical Formulation**:
For a digital image of size $M \times N$ with $L$ gray levels, the equalized gray level $s_k$ corresponding to input level $r_k$ is computed using the discrete Cumulative Distribution Function (CDF):
$$s_k = \text{round}\left( \frac{L - 1}{M \cdot N} \sum_{j=0}^k n_j \right)$$
where $n_j$ is the frequency of gray level $r_j$.

**Worked Example**:
Consider an $8 \times 8$ image ($M \cdot N = 64$ pixels) with $L = 8$ gray levels:

| $k$ | Gray Level $r_k$ | Pixel Count $n_k$ | Cumulative $\sum n_j$ | $s_k = \text{round}\left(\frac{7}{64} \sum n_j\right)$ | Final Level $s_k$ |
|---|---|---|---|---|---|
| 0 | 0 | 8 | 8 | $\text{round}(0.875)$ | **1** |
| 1 | 1 | 10 | 18 | $\text{round}(1.968)$ | **2** |
| 2 | 2 | 16 | 34 | $\text{round}(3.718)$ | **4** |
| 3 | 3 | 12 | 46 | $\text{round}(5.031)$ | **5** |
| 4 | 4 | 8 | 54 | $\text{round}(5.906)$ | **6** |
| 5 | 5 | 6 | 60 | $\text{round}(6.562)$ | **7** |
| 6 | 6 | 4 | 64 | $\text{round}(7.000)$ | **7** |
| 7 | 7 | 0 | 64 | $\text{round}(7.000)$ | **7** |

**Conclusion**: The clustered gray levels $0\text{–}6$ are redistributed across levels $1\text{–}7$, dramatically increasing visual contrast.

---

### Question 2 [Dec 2023 Q9 / Dec 2018 Q8 — 4 Marks]
**Question**:
What do you understand by correlation and convolution operations in case of image processing?

**Solution**:

Both correlation and convolution are fundamental neighborhood spatial filtering operations that slide a filter mask (kernel) across an image to compute sum-of-product responses.

1. **Spatial Correlation**:
   The process of displacing a filter mask $w(s, t)$ of size $m \times n$ across an image $f(x, y)$ and computing the linear inner product at each coordinate:
   $$g(x, y) = w(x, y) \circ f(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) \cdot f(x+s, y+t)$$
   - *Application*: **Template Matching** (measuring structural similarity between an image region and a reference template).

2. **Spatial Convolution**:
   Identical to correlation, except that the filter mask is **rotated by $180^\circ$** before performing multiplication and summation:
   $$g(x, y) = w(x, y) \ast f(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) \cdot f(x-s, y-t)$$
   - *Application*: Linear Time-Invariant (LTI) system response, Gaussian blurring, edge differentiation.

**Key Difference**:
- Correlation does not rotate the kernel ($w(s, t)$ applied directly).
- Convolution rotates the kernel by $180^\circ$ ($w(-s, -t)$ applied).
- For spatially symmetric kernels (e.g., Gaussian, box filters, Laplacian), **correlation and convolution yield identical numerical results**.
