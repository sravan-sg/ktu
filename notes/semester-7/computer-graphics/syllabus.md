# CS401 — Computer Graphics

> 4 Credits | L-T-P: 4-0-0 | Year of Introduction: 2016 | Semester 7

---

## Grading Criteria

| Component | Details |
|-----------|---------|
| Internal Assessment | 2 Internal Exams (First Internal covers Modules I–II; Second Internal covers Modules III–IV) |
| End Semester Exam | 4 Parts (A, B, C, D) — 100 Marks total |

**Question Paper Pattern:**

| Part | Coverage | Format | Total Marks |
|------|----------|--------|-------------|
| A | All 6 modules | 10 × 4 marks (3 from Mod I&II, 3 from Mod III&IV, 4 from Mod V&VI) — all compulsory | 40 |
| B | Modules I & II | Answer 2/3 questions, 9 marks each (max 3 sub-parts) | 18 |
| C | Modules III & IV | Answer 2/3 questions, 9 marks each (max 3 sub-parts) | 18 |
| D | Modules V & VI | Answer 2/3 questions, 12 marks each (max 3 sub-parts) | 24 |
| **Total** | | | **100** |

> At least 50% of questions must be analytical/numerical type across all combinations of choices.

**Module Weightage in End-Sem Exam:**

| Module | Hours | Exam Weightage |
|--------|-------|----------------|
| Module I — Basic Concepts & Devices | 7 | 15% |
| Module II — Line/Circle Drawing & Scan Conversion | 8 | 15% |
| Module III — 2D Transformations & Clipping | 8 | 15% |
| Module IV — Polygon Clipping & 3D Objects | 8 | 15% |
| Module V — Projections & Hidden Surface Removal | 9 | 20% |
| Module VI — Image Processing | 8 | 20% |

---

## Textbooks

1. **Donald Hearn and M. Pauline Baker** — *Computer Graphics*, PHI, 2nd Edition, 1996 *(Primary — covers Modules I–V)*
2. **E. Gose, R. Johnsonbaugh and S. Jost** — *Pattern Recognition and Image Analysis*, PHI PTR, 1996 *(Module VI — Image Processing)*
3. **William M. Newman and Robert F. Sproull** — *Principles of Interactive Computer Graphics*, McGraw Hill, 2nd Edition, 1979 *(Supplementary — Modules I–IV)*
4. **Zhigang Xiang and Roy Plastock** — *Computer Graphics (Schaum's Outline Series)*, McGraw Hill, 1986 *(Problem sets and solved examples)*

**References:**
1. David F. Rogers — *Procedural Elements for Computer Graphics*, Tata McGraw Hill, 2001
2. M. Sonka, V. Hlavac, and R. Boyle — *Image Processing, Analysis, and Machine Vision*, Thomson India Edition, 2007
3. Rafael C. Gonzalez and Richard E. Woods — *Digital Image Processing*, Pearson, 2017

---

## Modules

### Module I — Basic Concepts in Computer Graphics (7 Hours | 15% Marks)

- Basic concepts in Computer Graphics
- Types of Graphic Devices
- Interactive Graphic inputs
- Raster Scan Displays
- Random Scan Displays

### Module II — Line/Circle Drawing Algorithms & Scan Conversion (8 Hours | 15% Marks)

- Line Drawing Algorithms:
  - DDA (Digital Differential Analyzer) algorithm
  - Bresenham's line drawing algorithm
- Circle Generation Algorithms:
  - Midpoint circle algorithm
  - Bresenham's circle algorithm
- Scan Conversion:
  - Frame buffers
  - Solid area scan conversion
  - Polygon filling algorithms

### Module III — 2D Transformations, Windowing & Clipping (8 Hours | 15% Marks)

- Two dimensional transformations:
  - Homogeneous coordinate systems
  - Matrix formulation of transformations
  - Concatenation of transformations
- Windowing concepts
- Window to Viewport Transformation
- Two dimensional clipping:
  - Line clipping — Cohen-Sutherland algorithm
  - Line clipping — Midpoint Subdivision algorithm

### Module IV — Polygon Clipping & 3D Object Representation (8 Hours | 15% Marks)

- Polygon clipping:
  - Sutherland-Hodgman algorithm
  - Weiler-Atherton algorithm
- Three dimensional object representation:
  - Polygon surfaces
  - Quadric surfaces
- Basic 3D transformations

### Module V — Projections & Visible Surface Detection (9 Hours | 20% Marks)

- Projections:
  - Parallel projections
  - Perspective projections
  - Vanishing points
- Visible surface detection methods:
  - Back face removal
  - Z-Buffer algorithm
  - A-Buffer algorithm
  - Depth-sorting method (Painter's algorithm)
  - Scan line algorithm

### Module VI — Image Processing (8 Hours | 20% Marks)

- Introduction to Image Processing
- Fundamental steps in image processing
- Digital image representations
- Relationship between pixels
- Gray level histogram
- Spatial convolution and correlation
- Edge detection:
  - Robert edge detector
  - Prewitt edge detector
  - Sobel edge detector

---

## Exam Focus — What to Prioritize

1. **Modules V & VI carry 44 marks (Part D — 24 marks, and 4 Part A questions worth 16 marks)** — Projections (parallel, perspective, vanishing points) and hidden surface algorithms (Z-buffer, back face removal, depth-sort) paired with image processing (edge detectors, spatial convolution, gray-level histograms) are the highest-yield exam areas. Master derivations and step-by-step algorithm traces.

2. **Bresenham's Line & Circle Algorithms (Module II)** — These are near-certain numerical questions in Parts A and B. Practice tracing pixel plots step-by-step for given slopes (e.g., draw a line from (2,3) to (12,8)). Both midpoint and Bresenham circle algorithms require explicit point-by-point computation tables.

3. **2D Transformations & Clipping (Module III)** — Matrix concatenation of translation, scaling, rotation in homogeneous coordinates is a standard 9-mark Part C question. Cohen-Sutherland line clipping with region codes is a numerical problem that appears in nearly every paper.

4. **Cohen-Sutherland & Sutherland-Hodgman (Modules III & IV)** — Both clipping algorithms involve numerical tracing (region codes, intersection computation) and are directly testable as step-by-step worked examples.

5. **Visible Surface Detection Algorithm Comparison (Module V)** — Z-buffer vs A-buffer vs scan-line vs depth-sort: comparative questions (speed, memory, accuracy, transparency handling) appear as 4-mark Part A and 12-mark Part D questions.

6. **Edge Detection Operators (Module VI)** — Robert, Prewitt, and Sobel operators require writing out the convolution masks and computing edge magnitude from a given pixel grid. Expect numerical convolution problems in Part A and Part D.

7. **DDA vs Bresenham Comparison (Module II)** — The contrast in computation steps, floating-point vs integer arithmetic, and efficiency is a high-frequency short-answer (Part A) target.

8. **3D Transformations & Polygon Clipping (Module IV)** — Weiler-Atherton and Sutherland-Hodgman polygon clipping traces are high-frequency Part C numerical questions.
