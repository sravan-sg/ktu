# 2D Geometric Transformations & Homogeneous Coordinates

## 1. Explanation
Geometric transformations are mathematical operations that reposition, orient, resize, or deform geometric models in 2D or 3D space. They form the core computational engine of computer graphics pipelines, animation engines, and CAD systems.

### The Basic 2D Transformations (Affine Transformations)

#### 1. Translation
Moves an object by a linear displacement vector $\vec{T} = (t_x, t_y)$ without altering its size or angular orientation:
$$x' = x + t_x$$
$$y' = y + t_y$$
In standard Cartesian coordinates, translation is an vector addition, **not** a matrix multiplication.

#### 2. Scaling
Alters the size of an object by scaling factors $s_x$ and $s_y$ relative to the coordinate origin $(0, 0)$:
$$x' = x \cdot s_x$$
$$y' = y \cdot s_y$$
- **Uniform Scaling**: $s_x = s_y$ (preserves aspect ratio and angles).
- **Differential (Non-uniform) Scaling**: $s_x \ne s_y$ (distorts proportions).
- If $s_x, s_y > 1$: Object is enlarged. If $0 < s_x, s_y < 1$: Object is reduced.

#### 3. Rotation
Rotates an object by an angle $\theta$ counterclockwise (positive orientation) about the coordinate origin $(0, 0)$.
Let initial point $P(x, y)$ be at radial distance $r$ and angle $\phi$:
$$x = r\cos\phi, \quad y = r\sin\phi$$
After rotating by angle $\theta$, the new angle is $\phi + \theta$:
$$x' = r\cos(\phi + \theta) = r\cos\phi\cos\theta - r\sin\phi\sin\theta = x\cos\theta - y\sin\theta$$
$$y' = r\sin(\phi + \theta) = r\sin\phi\cos\theta + r\cos\phi\sin\theta = x\sin\theta + y\cos\theta$$

In matrix form:
$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$

#### 4. Reflection
Produces a mirror image of an object across a specified reflection axis:
- **Across X-Axis ($y = 0$)**: $x' = x, \ y' = -y$
  $$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
- **Across Y-Axis ($x = 0$)**: $x' = -x, \ y' = y$
  $$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
- **Across Origin**: $x' = -x, \ y' = -y$ (equivalent to $180^\circ$ rotation).
- **Across Line $y = x$**: $x' = y, \ y' = x$.

#### 5. Shear
Deforms the shape of an object such that parallel lines remain parallel, shifting coordinates proportional to the other axis:
- **X-Direction Shear (parallel to X-axis)**:
  $$x' = x + sh_x \cdot y, \quad y' = y$$
  $$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} 1 & sh_x \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
- **Y-Direction Shear (parallel to Y-axis)**:
  $$x' = x, \quad y' = y + sh_y \cdot x$$
  $$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ sh_y & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$

---

### Homogeneous Coordinates & Matrix Formulation
Notice that in 2D Cartesian space, rotation, scaling, and shear are represented by $2 \times 2$ matrix multiplications ($P' = M \cdot P$), whereas translation is an addition ($P' = P + T$).
This architectural mismatch prevents concatenating sequences of transformations into a single unified matrix.

#### The Homogeneous Coordinate Representation
To unify all affine transformations into pure matrix multiplications, we embed the 2D Cartesian plane into a 3D projective space by adding a third coordinate $w$:
$$(x, y) \implies (X_h, Y_h, w), \quad \text{where } x = \frac{X_h}{w}, \ y = \frac{Y_h}{w}$$
For standard affine graphics pipelines, we set $w = 1$:
$$(x, y) \implies \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

#### $3 \times 3$ Homogeneous Transformation Matrices:
1. **Translation Matrix $\mathbf{T}(t_x, t_y)$**:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$
2. **Rotation Matrix $\mathbf{R}(\theta)$**:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$
3. **Scaling Matrix $\mathbf{S}(s_x, s_y)$**:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$
4. **Shear Matrix $\mathbf{Sh}(sh_x, sh_y)$**:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & sh_x & 0 \\ sh_y & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

---

### Composite Transformations (Matrix Concatenation)
Because all operations are $3 \times 3$ matrices, any sequence of transformations can be multiplied (concatenated) into a single composite matrix $\mathbf{M}_{\text{composite}}$:
$$\mathbf{M}_{\text{composite}} = \mathbf{M}_n \cdot \mathbf{M}_{n-1} \dots \mathbf{M}_2 \cdot \mathbf{M}_1$$
Applying $\mathbf{M}_{\text{composite}}$ directly to thousands of vertices requires only **one vector-matrix multiplication per vertex**, saving massive computational overhead.

> **Crucial Rule**: Matrix multiplication is **associative** ($\mathbf{A}(\mathbf{B}\mathbf{C}) = (\mathbf{A}\mathbf{B})\mathbf{C}$), but **non-commutative** ($\mathbf{A}\mathbf{B} \ne \mathbf{B}\mathbf{A}$). The order of operations is critical!

#### 1. General 2D Rotation About an Arbitrary Pivot Point $(x_r, y_r)$
To rotate an object by angle $\theta$ about an arbitrary point $(x_r, y_r)$ instead of origin:
1. Translate pivot point to the origin: $\mathbf{T}(-x_r, -y_r)$.
2. Perform rotation about origin: $\mathbf{R}(\theta)$.
3. Translate origin back to pivot point: $\mathbf{T}(x_r, y_r)$.

$$\mathbf{M}_{\text{pivot\_rot}} = \mathbf{T}(x_r, y_r) \cdot \mathbf{R}(\theta) \cdot \mathbf{T}(-x_r, -y_r)$$

Multiplying these $3 \times 3$ matrices:
$$\mathbf{M}_{\text{pivot\_rot}} = \begin{bmatrix} 1 & 0 & x_r \\ 0 & 1 & y_r \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -x_r \\ 0 & 1 & -y_r \\ 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{M}_{\text{pivot\_rot}} = \begin{bmatrix} \cos\theta & -\sin\theta & x_r(1 - \cos\theta) + y_r\sin\theta \\ \sin\theta & \cos\theta & y_r(1 - \cos\theta) - x_r\sin\theta \\ 0 & 0 & 1 \end{bmatrix}$$

#### 2. General 2D Scaling About an Arbitrary Fixed Point $(x_f, y_f)$
$$\mathbf{M}_{\text{fixed\_scale}} = \mathbf{T}(x_f, y_f) \cdot \mathbf{S}(s_x, s_y) \cdot \mathbf{T}(-x_f, -y_f)$$
$$\mathbf{M}_{\text{fixed\_scale}} = \begin{bmatrix} s_x & 0 & x_f(1 - s_x) \\ 0 & s_y & y_f(1 - s_y) \\ 0 & 0 & 1 \end{bmatrix}$$

---

## 2. Example: Commutativity and Pivot Rotation Geometry
```
Object at P          1. Translate to origin       2. Rotate by theta        3. Translate back
     +---+                  +---+                                                  +---+
     |   |                  |   |                      /|                          |  /
     +---+                  +---+                     /_|                          |_/
       * (Pivot P_r)          * (0, 0)                  * (0, 0)                     * (Pivot P_r)
```

---

## 3. Applications & Use Cases
1. **Scene Graph Hierarchies in Game Engines (Unity, Unreal)**: Objects in 3D/2D games are arranged in transform hierarchies (e.g., character body $\to$ arm $\to$ hand $\to$ weapon). Composite matrix multiplication propagates transformations down the hierarchy automatically.
2. **Camera Panning, Zooming, and Orbiting in CAD**: Changing user viewpoint is implemented by concatenating inverse camera translation and rotation matrices against all geometric model vertices.
3. **Typography & Font Glyph Rendering**: Font rendering engines apply affine shear and scale matrices to generate italic and bold variations dynamically from standard Roman font vector outlines.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: 2D Rotation About an Arbitrary Pivot Point [KTU June 2024 / Dec 2020 - 9 Marks]
**Problem**:
A triangle has vertices at $A(2, 2)$, $B(6, 2)$, and $C(4, 6)$.
Rotate this triangle by $90^\circ$ counterclockwise about the fixed pivot point $A(2, 2)$. Determine the final coordinates of vertices $A', B', C'$.

**Step-by-step Solution**:
1. **Parameter Values**:
   $$\theta = 90^\circ \implies \cos 90^\circ = 0, \quad \sin 90^\circ = 1$$
   $$\text{Pivot Point } (x_r, y_r) = (2, 2)$$
2. **Composite Transformation Matrix**:
   $$\mathbf{M} = \mathbf{T}(2, 2) \cdot \mathbf{R}(90^\circ) \cdot \mathbf{T}(-2, -2)$$
   - Calculate third column terms:
     $$m_{13} = x_r(1 - \cos 90^\circ) + y_r\sin 90^\circ = 2(1 - 0) + 2(1) = 4$$
     $$m_{23} = y_r(1 - \cos 90^\circ) - x_r\sin 90^\circ = 2(1 - 0) - 2(1) = 0$$
   - The composite matrix is:
     $$\mathbf{M} = \begin{bmatrix} 0 & -1 & 4 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
3. **Transforming the Vertices**:
   - **Vertex $A(2, 2)$**:
     $$\begin{bmatrix} x_A' \\ y_A' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 4 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(2) - 1(2) + 4 \\ 1(2) + 0(2) + 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix} \implies \mathbf{A'(2, 2)}$$
     *(As expected, the pivot point remains invariant).*
   - **Vertex $B(6, 2)$**:
     $$\begin{bmatrix} x_B' \\ y_B' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 4 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 6 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(6) - 1(2) + 4 \\ 1(6) + 0(2) + 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 6 \\ 1 \end{bmatrix} \implies \mathbf{B'(2, 6)}$$
   - **Vertex $C(4, 6)$**:
     $$\begin{bmatrix} x_C' \\ y_C' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 4 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 4 \\ 6 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(4) - 1(6) + 4 \\ 1(4) + 0(6) + 0 \\ 1 \end{bmatrix} = \begin{bmatrix} -2 \\ 4 \\ 1 \end{bmatrix} \implies \mathbf{C'(-2, 4)}$$
4. **Final Coordinates**:
   $$\mathbf{A'(2, 2), \quad B'(2, 6), \quad C'(-2, 4)}$$

---

### Example 2: Reflection Across an Arbitrary Line $y = mx + c$ [KTU Jan 2023 / May 2019 Pattern]
**Problem**:
Derive the composite transformation matrix to reflect an object across the line $y = x + 2$. Using this matrix, find the reflection of point $P(3, 1)$.

**Step-by-step Solution**:
1. **Line Parameters**:
   $$y = mx + c \implies m = 1, \ c = 2$$
   $$\text{Slope angle } \theta = \tan^{-1}(1) = 45^\circ$$
2. **Decomposition Steps**:
   1. Translate line so its $y$-intercept passes through origin: $\mathbf{T}(0, -c) = \mathbf{T}(0, -2)$.
   2. Rotate line by $-\theta = -45^\circ$ to align it with the $X$-axis: $\mathbf{R}(-45^\circ)$.
   3. Reflect across the $X$-axis: $\mathbf{Ref}_x$.
   4. Inverse rotate by $+45^\circ$: $\mathbf{R}(45^\circ)$.
   5. Inverse translate back by $+c$: $\mathbf{T}(0, 2)$.
3. **Composite Matrix**:
   $$\mathbf{M} = \mathbf{T}(0, 2) \cdot \mathbf{R}(45^\circ) \cdot \mathbf{Ref}_x \cdot \mathbf{R}(-45^\circ) \cdot \mathbf{T}(0, -2)$$
   - Notice that reflection across a line inclined at $45^\circ$ through origin simply swaps $x$ and $y$: $\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$.
   - Combining with translation:
     $$\mathbf{M} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & -2 \\ 1 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix}$$
4. **Transforming Point $P(3, 1)$**:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & -2 \\ 1 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(3) + 1(1) - 2 \\ 1(3) + 0(1) + 2 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ 5 \\ 1 \end{bmatrix} \implies \mathbf{P'(-1, 5)}$$

---

### Example 3: Scaling and Shear Sequence [KTU Dec 2021 Pattern]
**Problem**:
A square has vertices $A(0, 0), B(2, 0), C(2, 2), D(0, 2)$.
Apply an $x$-shear of $sh_x = 2$ followed by scaling $s_x = 2, s_y = 3$. Find the new coordinates of vertex $C(2, 2)$.

**Step-by-step Solution**:
1. **Transformation Matrices**:
   $$\mathbf{Sh}_x(2) = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \mathbf{S}(2, 3) = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
2. **Composite Matrix $\mathbf{M} = \mathbf{S} \cdot \mathbf{Sh}_x$**:
   $$\mathbf{M} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 4 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
3. **Transforming Vertex $C(2, 2)$**:
   $$\begin{bmatrix} x_C' \\ y_C' \\ 1 \end{bmatrix} = \begin{bmatrix} 2 & 4 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 2(2) + 4(2) \\ 0(2) + 3(2) \\ 1 \end{bmatrix} = \begin{bmatrix} 12 \\ 6 \\ 1 \end{bmatrix} \implies \mathbf{C'(12, 6)}$$

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / January 2023 - 4 Marks]
**Question**:
What do you mean by homogeneous coordinate system? What is its significance?

**Solution**:
1. **Definition of Homogeneous Coordinates**:
   A homogeneous coordinate representation expresses an $n$-dimensional point as an $(n+1)$-dimensional vector. In 2D graphics, a point $P(x, y)$ is represented by the 3D homogeneous coordinate triple $(X_h, Y_h, w)$ such that:
   $$x = \frac{X_h}{w}, \quad y = \frac{Y_h}{w} \quad (w \ne 0)$$
   By standard convention for affine transformations, the scaling factor $w$ is chosen as $1$, representing Cartesian point $(x, y)$ as the column vector $\begin{bmatrix} x & y & 1 \end{bmatrix}^T$.
2. **Significance in Computer Graphics**:
   - **Unification of Affine Transformations**: In standard 2D Cartesian coordinates, rotation and scaling are matrix multiplications, whereas translation is a vector addition. Homogeneous coordinates allow **translation to be expressed as a $3 \times 3$ matrix multiplication**, unifying all affine transformations into a single consistent mathematical form.
   - **Concatenation of Operations**: Arbitrary combinations of translation, rotation, scaling, reflection, and shear can be pre-multiplied into a single $3 \times 3$ composite matrix $\mathbf{M}_{\text{composite}}$. Vertices of complex models are transformed by evaluating a single matrix-vector product rather than applying sequential steps individually.
   - **Perspective Projections**: Homogeneous coordinates naturally support projective geometry, where the parameter $w$ represents perspective depth ($w = z/d$). Perspective division by $w$ automatically implements perspective foreshortening.

---

### Question 2 [KTU December 2018 / December 2021 - 9 Marks]
**Question**:
Derive the composite transformation matrix for rotating an object by an angle $\theta$ counterclockwise about an arbitrary pivot point $(x_r, y_r)$.

**Solution**:
1. **Objective**:
   Standard rotation formulas rotate an object about the coordinate origin $(0, 0)$. To rotate an object about an arbitrary pivot point $(x_r, y_r)$, we must execute a three-stage transformation sequence.
2. **Three-Stage Sequence**:
   - **Step 1**: Translate the object so that the pivot point $(x_r, y_r)$ moves to the origin:
     $$\mathbf{T}(-x_r, -y_r) = \begin{bmatrix} 1 & 0 & -x_r \\ 0 & 1 & -y_r \\ 0 & 0 & 1 \end{bmatrix}$$
   - **Step 2**: Perform the counterclockwise rotation by angle $\theta$ about the origin:
     $$\mathbf{R}(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
   - **Step 3**: Translate the object back so that the origin returns to the pivot point $(x_r, y_r)$:
     $$\mathbf{T}(x_r, y_r) = \begin{bmatrix} 1 & 0 & x_r \\ 0 & 1 & y_r \\ 0 & 0 & 1 \end{bmatrix}$$
3. **Matrix Multiplication Derivation**:
   The composite transformation matrix $\mathbf{M}$ is given by:
   $$\mathbf{M} = \mathbf{T}(x_r, y_r) \cdot \mathbf{R}(\theta) \cdot \mathbf{T}(-x_r, -y_r)$$
   
   First, multiply $\mathbf{R}(\theta)$ by $\mathbf{T}(-x_r, -y_r)$:
   $$\mathbf{R}(\theta) \cdot \mathbf{T}(-x_r, -y_r) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -x_r \\ 0 & 1 & -y_r \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta & -x_r\cos\theta + y_r\sin\theta \\ \sin\theta & \cos\theta & -x_r\sin\theta - y_r\cos\theta \\ 0 & 0 & 1 \end{bmatrix}$$
   
   Next, pre-multiply the result by $\mathbf{T}(x_r, y_r)$:
   $$\mathbf{M} = \begin{bmatrix} 1 & 0 & x_r \\ 0 & 1 & y_r \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} \cos\theta & -\sin\theta & -x_r\cos\theta + y_r\sin\theta \\ \sin\theta & \cos\theta & -x_r\sin\theta - y_r\cos\theta \\ 0 & 0 & 1 \end{bmatrix}$$
   $$\mathbf{M} = \begin{bmatrix} \cos\theta & -\sin\theta & x_r(1 - \cos\theta) + y_r\sin\theta \\ \sin\theta & \cos\theta & y_r(1 - \cos\theta) - x_r\sin\theta \\ 0 & 0 & 1 \end{bmatrix}$$
   This final $3 \times 3$ matrix directly maps any point $(x, y, 1)$ to its rotated position about pivot $(x_r, y_r)$ in a single matrix-vector multiplication.

