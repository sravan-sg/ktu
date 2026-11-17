# Module 6: Digital Image Processing Fundamentals & Edge Detection — Master Detailed Notes

## Overview
Module 6 covers the foundational concepts of digital image processing, discrete mathematical pixel relationships, intensity histogram manipulation, spatial filtering, and optimal edge detection operators.

---

## Detailed Topic Guides

1. **[Digital Image Processing Fundamentals & Relationships Between Pixels](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-6/digital-image-processing-fundamentals-and-pixel-relationships.md)**
   - The complete 10-stage digital image processing system pipeline (Gonzalez & Woods model)
   - Continuous 2D optical functions $f(x, y)$, spatial sampling, and amplitude quantization ($L = 2^k$)
   - Neighborhood relationships: 4-Neighbors ($N_4$), Diagonal Neighbors ($N_D$), and 8-Neighbors ($N_8$)
   - Adjacency and connectivity: 4-adjacency, 8-adjacency, and $m$-adjacency (resolution of ambiguous multi-paths)
   - Distance Metrics: Euclidean ($D_e$), City-Block ($D_4$), and Chessboard ($D_8$) distance functions and equidistant geometric contours
   - Solved numerical examples and KTU university exam solutions

2. **[Gray Level Histograms & Spatial Filtering](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-6/gray-level-histogram-and-spatial-filtering.md)**
   - Mathematical definition of gray-level histograms $h(r_k) = n_k$ and normalized probability density $p(r_k)$
   - Theoretical derivation of continuous histogram equalization: Cumulative Distribution Function (CDF) mapping
   - Discrete histogram equalization implementation and step-by-step contrast enhancement tables
   - Spatial filtering mechanics: Difference between spatial correlation and spatial convolution ($180^\circ$ rotation)
   - Solved numerical problems (complete 8-level histogram equalization trace, 2D convolution trace) and KTU exam solutions

3. **[Edge Detection Operators: Roberts, Prewitt, Sobel & Canny](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-6/edge-detection-operators.md)**
   - First-order derivative gradient vector ($\nabla f$), magnitude ($M$), and direction ($\theta$)
   - First-order edge detection kernels: Roberts Cross ($2 \times 2$), Prewitt ($3 \times 3$), and Sobel ($3 \times 3$)
   - Why the Sobel operator is preferred over Prewitt for real-world noisy imagery (central smoothing weight of 2)
   - The Canny Edge Detector: Canny's three optimal criteria and the 5-stage processing pipeline (Gaussian smoothing, gradient calculation, Non-Maximum Suppression, double thresholding, hysteresis tracking)
   - Solved numerical walkthroughs (Sobel convolution traces, Canny threshold classification) and KTU exam questions

---

## Module Revision Guide
- For quick-reference formulas, convolution masks, distance metrics, and exam review, refer to:
  **[Module 6 Revision Notes](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-6/revision-notes.md)**

