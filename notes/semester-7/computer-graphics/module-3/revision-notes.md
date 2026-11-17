# Module 3: Revision Notes — Quick Review Guide

## 1. High-Yield Summary
- **Homogeneous Coordinates**: Add third coordinate $w=1$ ($[x, y, 1]^T$) so translation can be expressed as a $3 \times 3$ matrix multiplication. Enables concatenating multiple transformations into one composite matrix.
- **Matrix Concatenation Rule**: Matrix multiplication is **associative** but **NOT commutative** ($\mathbf{A}\mathbf{B} \ne \mathbf{B}\mathbf{A}$). Order matters!
- **Rotation about Pivot $(x_r, y_r)$**: $\mathbf{T}(x_r, y_r) \cdot \mathbf{R}(\theta) \cdot \mathbf{T}(-x_r, -y_r)$.
- **Scaling about Fixed Point $(x_f, y_f)$**: $\mathbf{T}(x_f, y_f) \cdot \mathbf{S}(s_x, s_y) \cdot \mathbf{T}(-x_f, -y_f)$.
- **Window-to-Viewport Mapping**: Maps world coordinates $[x_{w\min}, x_{w\max}] \times [y_{w\min}, y_{w\max}]$ to device viewport $[x_{v\min}, x_{v\max}] \times [y_{v\min}, y_{v\max}]$. Preserves relative proportions.
- **Cohen-Sutherland Line Clipping**: Uses 4-bit outcode `[Top Bottom Right Left]`.
  - Trivial Accept: $C_1 \mid C_2 == 0000$.
  - Trivial Reject: $C_1 \ \& \ C_2 \ne 0000$.
  - Otherwise: Intersect with boundary of non-zero bit.

---

## 2. Master Matrix Reference Table ($3 \times 3$ Homogeneous)

| Transformation | Matrix Representation |
|---|---|
| **Translation** $\mathbf{T}(t_x, t_y)$ | $\begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix}$ |
| **Rotation** $\mathbf{R}(\theta)$ (CCW) | $\begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
| **Scaling** $\mathbf{S}(s_x, s_y)$ | $\begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
| **Reflection across X-axis** | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
| **Reflection across Y-axis** | $\begin{bmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
| **Reflection across line $y = x$** | $\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
| **X-Shear** $\mathbf{Sh}_x(sh_x)$ | $\begin{bmatrix} 1 & sh_x & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
| **Y-Shear** $\mathbf{Sh}_y(sh_y)$ | $\begin{bmatrix} 1 & 0 & 0 \\ sh_y & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
| **Viewing Transformation** $\mathbf{M}_{\text{view}}$ | $\begin{bmatrix} s_x & 0 & x_{v\min} - s_x x_{w\min} \\ 0 & s_y & y_{v\min} - s_y y_{w\min} \\ 0 & 0 & 1 \end{bmatrix}$ |

---

## 3. Cohen-Sutherland 4-Bit Outcode Mapping

$$\text{Bit 4: Top } (y > y_{w\max}) \quad | \quad \text{Bit 3: Bottom } (y < y_{w\min}) \quad | \quad \text{Bit 2: Right } (x > x_{w\max}) \quad | \quad \text{Bit 1: Left } (x < x_{w\min})$$

```
   1001 (TL)  |  1000 (T)  |  1010 (TR)
  ────────────┼────────────┼─────────── y_wmax
   0001 (L)   |  0000 (IN) |  0010 (R)
  ────────────┼────────────┼─────────── y_wmin
   0101 (BL)  |  0100 (B)  |  0110 (BR)
              |            |
            x_wmin       x_wmax
```

### Boundary Intersection Formulas:
- Top ($y = y_{w\max}$): $x = x_1 + \frac{1}{m}(y_{w\max} - y_1)$
- Bottom ($y = y_{w\min}$): $x = x_1 + \frac{1}{m}(y_{w\min} - y_1)$
- Right ($x = x_{w\max}$): $y = y_1 + m(x_{w\max} - x_1)$
- Left ($x = x_{w\min}$): $y = y_1 + m(x_{w\min} - x_1)$

---

## 4. Top 3 Exam Traps & Tips
1. **Pivot Rotation Order**: Always remember the sandwich principle: translate pivot to origin **FIRST** ($\mathbf{T}(-x_r, -y_r)$), rotate ($\mathbf{R}(\theta)$), then translate origin back to pivot **LAST** ($\mathbf{T}(x_r, y_r)$). Writing $\mathbf{T}(x_r, y_r) \cdot \mathbf{R} \cdot \mathbf{T}(-x_r, -y_r)$ evaluated from right-to-left is correct.
2. **Bitwise AND vs. Bitwise OR**: Trivial acceptance requires $C_1 \mid C_2 == 0000$. Trivial rejection requires $C_1 \ \& \ C_2 \ne 0000$. If $(C_1 \ \& \ C_2) == 0000$, the line is **NOT** necessarily accepted—it might still intersect!
3. **Window-to-Viewport Units**: When calculating $s_x$ and $s_y$, always place viewport dimension in the **numerator** and window dimension in the **denominator**: $s_x = \frac{\Delta x_v}{\Delta x_w}$. Inverting this ratio is a classic student mistake.

