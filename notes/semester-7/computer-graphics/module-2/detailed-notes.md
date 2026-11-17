# Module 2: Scan Conversion & Rasterization Algorithms — Master Detailed Notes

## Overview
Module 2 covers the foundational mathematical and algorithmic primitives of 2D raster graphics: converting ideal continuous geometric shapes (lines, circles, filled polygons) into discrete integer pixel rasters on a digital display grid.

---

## Detailed Topic Guides

1. **[Line Drawing Algorithms: DDA and Bresenham's Algorithm](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-2/line-drawing-algorithms.md)**
   - The fundamental raster scan conversion challenge
   - Digital Differential Analyzer (DDA): Floating-point recurrence, round-off error accumulation, slope cases ($|m| \le 1$ vs $|m| > 1$)
   - Bresenham's Integer Line Algorithm: Complete algebraic derivation, decision parameters $p_k$, initial condition $p_0 = 2\Delta y - \Delta x$, and steep line formulation
   - In-depth solved numerical problems (step-by-step trace tables) and KTU exam solutions

2. **[Circle Generation Algorithms: Midpoint Circle and Bresenham's Algorithm](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-2/circle-generation-algorithms.md)**
   - Circle functions in Cartesian and polar coordinate systems
   - Eight-way reflective symmetry of a circle centered at origin: 87.5% computation reduction
   - Midpoint Circle Algorithm: Complete derivation from midpoint $M(x_k + 1, y_k - 0.5)$, decision parameters, and integer update rules
   - Solved numerical traces for $r = 8$ and $r = 6$ with arbitrary centers, error bound proofs, and KTU solutions

3. **[Scan Conversion & Polygon Filling Algorithms](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-2/scan-conversion-and-polygon-filling.md)**
   - Inside-Outside tests: Odd-Even Parity Rule vs. Non-Zero Winding Number Rule
   - Scan-Line Polygon Fill: Edge Table (ET) and Active Edge Table (AET) data structure maintenance and vertex parity rules
   - Seed-based filling: Boundary-Fill (4-connected vs 8-connected) and Flood-Fill algorithms
   - Solved numerical examples (Edge Table construction, self-intersecting star polygons, recursion stack depth analysis)

---

## Module Revision Guide
- For high-yield formulas, decision parameter recurrences, and quick review, refer to:
  **[Module 2 Revision Notes](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-2/revision-notes.md)**

