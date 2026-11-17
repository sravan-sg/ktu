# Module 5: 3D Projections & Visible Surface Detection — Master Detailed Notes

## Overview
Module 5 addresses two core challenges of 3D computer graphics: projecting 3D continuous geometry onto a 2D view plane (Parallel and Perspective Projections) and determining which surfaces are directly visible to the observer (Visible Surface Detection / Hidden Surface Elimination).

---

## Detailed Topic Guides

1. **[Three-Dimensional Projections: Parallel and Perspective](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-5/three-dimensional-projections.md)**
   - Theoretical taxonomy: Center of Projection (COP), Direction of Projection (DOP), Projectors
   - Parallel Projections: Orthographic (Multiview, Isometric, Dimetric, Trimetric) and Oblique (Cavalier $\alpha = 45^\circ$, Cabinet $\alpha = 63.4^\circ$)
   - Perspective Projections: Optical convergence, perspective foreshortening, and vanishing points (1-point, 2-point, 3-point)
   - Mathematical derivation of the $4 \times 4$ homogeneous perspective transformation matrix using similar triangles
   - Solved numerical problems (foreshortening calculations, Cavalier vs Cabinet coordinate traces, vanishing point convergence proofs) and KTU exam solutions

2. **[Visible Surface Detection Algorithms (Hidden Surface Elimination)](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-5/visible-surface-detection-algorithms.md)**
   - Algorithmic paradigms: Object-Space vs. Image-Space methods ($O(n^2)$ vs $O(n \cdot p)$)
   - Back-Face Removal: Surface normal dot-product test ($\vec{N} \cdot \vec{V} \le 0$) and $C \ge 0$ culling condition
   - Depth-Buffer (Z-Buffer) Algorithm: Memory buffers, algorithm pseudocode, and incremental scanline depth recurrence ($z' = z - A/C$)
   - A-Buffer Algorithm: Linked list fragment architecture, antialiasing, and transparency handling
   - Depth-Sorting Method (Painter's Algorithm): Preliminary depth sorting and the 5 disambiguation tests
   - Scan-Line visible surface detection mechanism
   - Solved numerical examples and complete KTU previous year question solutions

---

## Module Revision Guide
- For quick-reference formulas, projection matrices, culling tests, and exam summaries, refer to:
  **[Module 5 Revision Notes](file:///home/sravan/ktu/notes/semester-7/computer-graphics/module-5/revision-notes.md)**

