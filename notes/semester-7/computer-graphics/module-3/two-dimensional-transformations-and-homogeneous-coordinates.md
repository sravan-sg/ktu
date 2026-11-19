# 2D Geometric Transformations & Homogeneous Coordinates

## 1. Explanation

Geometric transformations form the mathematical engine of computer graphics pipelines, CAD systems, digital image manipulation, and real-time animation engines. A geometric transformation is a function that maps points from an initial coordinate space to a new spatial configuration:
$$P'(x', y') = \mathcal{T}(P(x, y))$$

Affine transformations preserve:
1. **Collinearity**: Points lying on a straight line remain on a straight line after transformation.
2. **Parallelism**: Parallel lines remain parallel.
3. **Ratio of Distances**: The ratio of lengths of line segments along any line is preserved.

---

### The Fundamental 2D Transformations (Cartesian Space)

#### 1. Translation
Displaces an object by a linear directional vector $\vec{T} = \begin{bmatrix} t_x & t_y \end{bmatrix}^T$ without changing its size, orientation, or shape:
$$x' = x + t_x$$
$$y' = y + t_y$$
In standard 2D Cartesian coordinates, translation is an **algebraic addition**, not a matrix multiplication:
$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} x \\ y \end{bmatrix} + \begin{bmatrix} t_x \\ t_y \end{bmatrix}$$

#### 2. Scaling
Alters the geometric size of an object relative to the coordinate origin $(0, 0)$ by multiplying coordinates by scaling factors $s_x$ and $s_y$:
$$x' = x \cdot s_x$$
$$y' = y \cdot s_y$$
In matrix form:
$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
- **Uniform Scaling ($s_x = s_y$)**: Preserves aspect ratio, angles, and relative shape proportions.
- **Differential (Non-uniform) Scaling ($s_x \ne s_y$)**: Distorts proportions and angles.
- If $|s_x|, |s_y| > 1$: Magnification (expansion).
- If $0 < |s_x|, |s_y| < 1$: Minification (compression).
- Negative scaling factors incorporate a coordinate reflection across an axis.

#### 3. Rotation (About Origin)
Rotates an object by an angle $\theta$ counterclockwise (positive mathematical convention) about the coordinate origin $(0, 0)$.

**Derivation from Polar Coordinates**:
Let point $P(x, y)$ be located at radial distance $r = \sqrt{x^2 + y^2}$ and initial angular orientation $\phi$:
$$x = r\cos\phi, \quad y = r\sin\phi$$
When rotated by angle $\theta$ about the origin to new position $P'(x', y')$, the new angle is $\phi + \theta$:
$$x' = r\cos(\phi + \theta) = r(\cos\phi\cos\theta - \sin\phi\sin\theta) = (r\cos\phi)\cos\theta - (r\sin\phi)\sin\theta$$
$$y' = r\sin(\phi + \theta) = r(\sin\phi\cos\theta + \cos\phi\sin\theta) = (r\sin\phi)\cos\theta + (r\cos\phi)\sin\theta$$
Substituting $x = r\cos\phi$ and $y = r\sin\phi$:
$$x' = x\cos\theta - y\sin\theta$$
$$y' = x\sin\theta + y\cos\theta$$

In matrix form:
$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
The rotation matrix is **orthogonal**: $\mathbf{R}^{-1}(\theta) = \mathbf{R}^T(\theta) = \mathbf{R}(-\theta)$, and $\det(\mathbf{R}) = \cos^2\theta + \sin^2\theta = 1$.

#### 4. Reflection (Mirror Imaging)
Produces a mirror replica of an object across a designated reflection line.
- **Across the X-Axis ($y = 0$)**: $x' = x, \ y' = -y$
  $$\mathbf{M}_x = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$
- **Across the Y-Axis ($x = 0$)**: $x' = -x, \ y' = y$
  $$\mathbf{M}_y = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$$
- **Across the Coordinate Origin ($0, 0$)**: $x' = -x, \ y' = -y$ (equivalent to $180^\circ$ rotation)
  $$\mathbf{M}_{\text{origin}} = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$$
- **Across the Diagonal Line $y = x$**: Swaps coordinate axes: $x' = y, \ y' = x$
  $$\mathbf{M}_{y=x} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$
- **Across the Diagonal Line $y = -x$**: $x' = -y, \ y' = -x$
  $$\mathbf{M}_{y=-x} = \begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}$$

#### 5. Shear (Shearing Deformation)
Deforms an object along an axis such that parallel planes slide past each other like a deck of cards:
- **X-Direction Shear (shifts $x$ proportional to $y$)**:
  $$x' = x + sh_x \cdot y, \quad y' = y$$
  $$\mathbf{Sh}_x = \begin{bmatrix} 1 & sh_x \\ 0 & 1 \end{bmatrix}$$
- **Y-Direction Shear (shifts $y$ proportional to $x$)**:
  $$x' = x, \quad y' = y + sh_y \cdot x$$
  $$\mathbf{Sh}_y = \begin{bmatrix} 1 & 0 \\ sh_y & 1 \end{bmatrix}$$
- **Shear Relative to Arbitrary Reference Lines**:
  - Relative to horizontal reference line $y = y_{\text{ref}}$:
    $$x' = x + sh_x(y - y_{\text{ref}}), \quad y' = y$$
  - Relative to vertical reference line $x = x_{\text{ref}}$:
    $$x' = x, \quad y' = y + sh_y(x - x_{\text{ref}})$$

---

### Homogeneous Coordinates & Architectural Significance

#### The Incompatibility Problem
In 2D Cartesian space:
- Scaling, Rotation, Reflection, and Shear are $2 \times 2$ matrix **multiplications**: $P' = \mathbf{M} \cdot P$.
- Translation is a vector **addition**: $P' = P + T$.

Because of this architectural mismatch, a complex sequence of operations (e.g., Translate $\to$ Rotate $\to$ Scale $\to$ Translate back) cannot be concatenated into a single cumulative matrix in Cartesian coordinates. Each vertex of a $100,000$-triangle mesh would require evaluating separate additions and multiplications sequentially.

#### The Homogeneous Coordinate Representation
To unify all affine transformations into pure matrix multiplications, 2D Cartesian space $\mathbb{R}^2$ is embedded into 3D projective space $\mathbb{P}^2$ by appending a third scaling coordinate $w$:
$$(x, y) \implies (X_h, Y_h, w), \quad \text{where } x = \frac{X_h}{w}, \ y = \frac{Y_h}{w} \quad (w \ne 0)$$
In standard affine computer graphics, we set $w = 1$:
$$(x, y) \implies \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$
Points at infinity are represented naturally when $w = 0$ (directional vectors).

#### $3 \times 3$ Homogeneous Transformation Matrices

1. **Translation Matrix $\mathbf{T}(t_x, t_y)$**:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

2. **Rotation Matrix $\mathbf{R}(\theta)$**:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

3. **Scaling Matrix $\mathbf{S}(s_x, s_y)$**:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

4. **Reflection Matrices**:
   $$\mathbf{M}_x = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \mathbf{M}_y = \begin{bmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \mathbf{M}_{y=x} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

5. **Shear Matrix $\mathbf{Sh}(sh_x, sh_y)$**:
   $$\mathbf{Sh}(sh_x, sh_y) = \begin{bmatrix} 1 & sh_x & 0 \\ sh_y & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

---

### Composite Transformations (Matrix Concatenation)

Because all operations are expressed as uniform $3 \times 3$ matrices, any sequence of $n$ successive transformations can be multiplied (concatenated) into a single composite matrix:
$$\mathbf{M}_{\text{composite}} = \mathbf{M}_n \cdot \mathbf{M}_{n-1} \cdots \mathbf{M}_2 \cdot \mathbf{M}_1$$
For a scene with $V$ vertices, computing $\mathbf{M}_{\text{composite}}$ requires only a few matrix multiplications. Applying it to every vertex requires only **one vector-matrix multiplication per vertex**:
$$P'_i = \mathbf{M}_{\text{composite}} \cdot P_i, \quad \forall i \in \{1, \dots, V\}$$

> **Fundamental Matrix Properties**:
> - **Associative**: $\mathbf{A}(\mathbf{B}\mathbf{C}) = (\mathbf{A}\mathbf{B})\mathbf{C}$ (enables pre-concatenation of transformation pipelines).
> - **Non-Commutative**: In general, $\mathbf{A}\mathbf{B} \ne \mathbf{B}\mathbf{A}$. Translating then rotating produces a completely different result than rotating then translating!
> - **Commutative Exceptions**:
>   - Two pure translations: $\mathbf{T}_1 \mathbf{T}_2 = \mathbf{T}_2 \mathbf{T}_1$.
>   - Two pure rotations: $\mathbf{R}_1 \mathbf{R}_2 = \mathbf{R}_2 \mathbf{R}_1$.
>   - Two pure scalings: $\mathbf{S}_1 \mathbf{S}_2 = \mathbf{S}_2 \mathbf{S}_1$.
>   - Uniform scaling and rotation: $\mathbf{S}(s, s) \mathbf{R}(\theta) = \mathbf{R}(\theta) \mathbf{S}(s, s)$.

---

### Advanced Composite Derivations

#### 1. General Rotation About an Arbitrary Pivot Point $(x_r, y_r)$
To rotate an object about an arbitrary pivot point $P_r(x_r, y_r)$ rather than the origin:
1. Translate the pivot point $(x_r, y_r)$ to the coordinate origin: $\mathbf{T}(-x_r, -y_r)$
2. Perform rotation by angle $\theta$ about the origin: $\mathbf{R}(\theta)$
3. Translate the origin back to the pivot point: $\mathbf{T}(x_r, y_r)$

Composite Matrix:
$$\mathbf{M}_{\text{pivot\_rot}} = \mathbf{T}(x_r, y_r) \cdot \mathbf{R}(\theta) \cdot \mathbf{T}(-x_r, -y_r)$$

Multiplying out the $3 \times 3$ matrices:
$$\mathbf{M}_{\text{pivot\_rot}} = \begin{bmatrix} 1 & 0 & x_r \\ 0 & 1 & y_r \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -x_r \\ 0 & 1 & -y_r \\ 0 & 0 & 1 \end{bmatrix}$$
$$= \begin{bmatrix} \cos\theta & -\sin\theta & x_r(1 - \cos\theta) + y_r\sin\theta \\ \sin\theta & \cos\theta & y_r(1 - \cos\theta) - x_r\sin\theta \\ 0 & 0 & 1 \end{bmatrix}$$

#### 2. Scaling Relative to an Arbitrary Fixed Point $(x_f, y_f)$
To resize an object while keeping a specific anchor point $(x_f, y_f)$ stationary:
1. Translate $(x_f, y_f)$ to origin: $\mathbf{T}(-x_f, -y_f)$
2. Scale by $(s_x, s_y)$: $\mathbf{S}(s_x, s_y)$
3. Translate back: $\mathbf{T}(x_f, y_f)$

Composite Matrix:
$$\mathbf{M}_{\text{fixed\_scale}} = \mathbf{T}(x_f, y_f) \cdot \mathbf{S}(s_x, s_y) \cdot \mathbf{T}(-x_f, -y_f)$$
$$= \begin{bmatrix} 1 & 0 & x_f \\ 0 & 1 & y_f \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -x_f \\ 0 & 1 & -y_f \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & x_f(1 - s_x) \\ 0 & s_y & y_f(1 - s_y) \\ 0 & 0 & 1 \end{bmatrix}$$

#### 3. Reflection About an Arbitrary Line $L: y = mx + b$
Reflecting across a line that does not pass through the origin requires a 5-stage transformation sequence:
1. Translate the line vertically so its y-intercept $(0, b)$ coincides with the origin: $\mathbf{T}(0, -b)$
2. Rotate the line by angle $-\theta$ about the origin to align it with the positive X-axis (where $\theta = \arctan(m) \implies \cos\theta = \frac{1}{\sqrt{1+m^2}}, \sin\theta = \frac{m}{\sqrt{1+m^2}}$): $\mathbf{R}(-\theta)$
3. Perform standard reflection across the X-axis: $\mathbf{M}_x$
4. Apply the inverse rotation by $+\theta$: $\mathbf{R}(\theta)$
5. Apply the inverse translation back: $\mathbf{T}(0, b)$

Composite Matrix:
$$\mathbf{M}_{\text{line\_refl}} = \mathbf{T}(0, b) \cdot \mathbf{R}(\theta) \cdot \mathbf{M}_x \cdot \mathbf{R}(-\theta) \cdot \mathbf{T}(0, -b)$$

---

## 2. Example: Step-by-Step Matrix Chain Evaluation

Consider transforming point $P(2, 3)$ by:
1. Scaling by $s_x = 2, s_y = 3$
2. Rotating counterclockwise by $\theta = 90^\circ$
3. Translating by $t_x = 4, t_y = -1$

**Step 1: Write individual homogeneous matrices**:
$$\mathbf{S} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \mathbf{R} = \begin{bmatrix} \cos 90^\circ & -\sin 90^\circ & 0 \\ \sin 90^\circ & \cos 90^\circ & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \mathbf{T} = \begin{bmatrix} 1 & 0 & 4 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$

**Step 2: Compute composite matrix $\mathbf{M} = \mathbf{T} \cdot \mathbf{R} \cdot \mathbf{S}$**:
$$\mathbf{R} \cdot \mathbf{S} = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{M} = \mathbf{T} \cdot (\mathbf{R} \cdot \mathbf{S}) = \begin{bmatrix} 1 & 0 & 4 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -3 & 4 \\ 2 & 0 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$

**Step 3: Transform Point $P(2, 3)$**:
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -3 & 4 \\ 2 & 0 & -1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(2) - 3(3) + 4(1) \\ 2(2) + 0(3) - 1(1) \\ 0(2) + 0(3) + 1(1) \end{bmatrix} = \begin{bmatrix} -5 \\ 3 \\ 1 \end{bmatrix}$$
Transformed position: $P'(-5, 3)$.

---

## 3. Applications & Use Cases

1. **Hierarchical Scene Graphs in Game Engines (Unity, Unreal Engine)**:
   A character model consists of parent-child kinematic hierarchies (Torso $\to$ Upper Arm $\to$ Forearm $\to$ Hand $\to$ Fingers). Each joint stores a local transformation matrix $\mathbf{M}_{\text{local}}$. The global world-space position of a fingertip is computed by pre-multiplying parent transforms:
   $$\mathbf{M}_{\text{world}} = \mathbf{M}_{\text{torso}} \cdot \mathbf{M}_{\text{upper\_arm}} \cdot \mathbf{M}_{\text{forearm}} \cdot \mathbf{M}_{\text{hand}} \cdot \mathbf{M}_{\text{finger}}$$
2. **Computer-Aided Design (CAD / SolidWorks / AutoCAD)**:
   Parametric mechanical assemblies use composite pivot rotations and fixed-point scalings to simulate linkage kinematics (four-bar mechanisms, robotic arm inverse kinematics).
3. **GPU Vertex Shader Execution (OpenGL / Vulkan / DirectX)**:
   The core vertex shader operation collapses Model, View, and Projection transformations into a single pre-calculated $4 \times 4$ Model-View-Projection (MVP) matrix:
   $$\mathbf{gl\_Position} = \mathbf{P}_{\text{proj}} \cdot \mathbf{V}_{\text{view}} \cdot \mathbf{M}_{\text{model}} \cdot \mathbf{v}_{\text{in}}$$
   Evaluating MVP once on the CPU allows the GPU to transform millions of vertices concurrently in parallel SIMD vector units.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Formal Proof of Additivity for Successive Translations [KTU June 2022 Q16a]
**Problem**:
Show that the composition of two successive 2D translations is additive by multiplying their $3 \times 3$ homogeneous transformation matrices $\mathbf{T}(t_{x1}, t_{y1})$ and $\mathbf{T}(t_{x2}, t_{y2})$.

**Solution**:
Let $\mathbf{T}_1 = \mathbf{T}(t_{x1}, t_{y1})$ and $\mathbf{T}_2 = \mathbf{T}(t_{x2}, t_{y2})$ be two homogeneous translation matrices:
$$\mathbf{T}_1 = \begin{bmatrix} 1 & 0 & t_{x1} \\ 0 & 1 & t_{y1} \\ 0 & 0 & 1 \end{bmatrix}, \quad \mathbf{T}_2 = \begin{bmatrix} 1 & 0 & t_{x2} \\ 0 & 1 & t_{y2} \\ 0 & 0 & 1 \end{bmatrix}$$
Multiplying the two matrices $\mathbf{T}_{\text{composite}} = \mathbf{T}_2 \cdot \mathbf{T}_1$:
$$\mathbf{T}_{\text{composite}} = \begin{bmatrix} 1 & 0 & t_{x2} \\ 0 & 1 & t_{y2} \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & t_{x1} \\ 0 & 1 & t_{y1} \\ 0 & 0 & 1 \end{bmatrix}$$
Evaluating each entry via row-by-column dot products:
- Row 1:
  - $(1)(1) + (0)(0) + (t_{x2})(0) = 1$
  - $(1)(0) + (0)(1) + (t_{x2})(0) = 0$
  - $(1)(t_{x1}) + (0)(t_{y1}) + (t_{x2})(1) = t_{x1} + t_{x2}$
- Row 2:
  - $(0)(1) + (1)(0) + (t_{y2})(0) = 0$
  - $(0)(0) + (1)(1) + (t_{y2})(0) = 1$
  - $(0)(t_{x1}) + (1)(t_{y1}) + (t_{y2})(1) = t_{y1} + t_{y2}$
- Row 3:
  - $(0)(1) + (0)(0) + (1)(0) = 0$
  - $(0)(0) + (0)(1) + (1)(0) = 0$
  - $(0)(t_{x1}) + (0)(t_{y1}) + (1)(1) = 1$

Assembling the result:
$$\mathbf{T}_{\text{composite}} = \begin{bmatrix} 1 & 0 & t_{x1} + t_{x2} \\ 0 & 1 & t_{y1} + t_{y2} \\ 0 & 0 & 1 \end{bmatrix} = \mathbf{T}(t_{x1} + t_{x2}, \ t_{y1} + t_{y2})$$
Furthermore, because scalar addition is commutative ($t_{x1} + t_{x2} = t_{x2} + t_{x1}$):
$$\mathbf{T}_2 \cdot \mathbf{T}_1 = \mathbf{T}_1 \cdot \mathbf{T}_2$$
**Conclusion**: Successive translations are strictly additive and commutative. $\blacksquare$

---

### Example 2: Formal Proof of Additivity & Commutativity for Successive Rotations [KTU Dec 2023 Q5 / Sep 2020 Q5 / Dec 2019 Q15b / May 2019 Q14b]
**Problem**:
Show that the composition of two 2D rotations is additive by concatenating the matrix representation for $\mathbf{R}(\theta_1)$ and $\mathbf{R}(\theta_2)$, and prove that two successive rotations commute.

**Solution**:
Let the homogeneous rotation matrices for angles $\theta_1$ and $\theta_2$ about the origin be:
$$\mathbf{R}(\theta_1) = \begin{bmatrix} \cos\theta_1 & -\sin\theta_1 & 0 \\ \sin\theta_1 & \cos\theta_1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \mathbf{R}(\theta_2) = \begin{bmatrix} \cos\theta_2 & -\sin\theta_2 & 0 \\ \sin\theta_2 & \cos\theta_2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
Multiplying $\mathbf{R}_{\text{comp}} = \mathbf{R}(\theta_2) \cdot \mathbf{R}(\theta_1)$:
$$\mathbf{R}_{\text{comp}} = \begin{bmatrix} \cos\theta_2 & -\sin\theta_2 & 0 \\ \sin\theta_2 & \cos\theta_2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} \cos\theta_1 & -\sin\theta_1 & 0 \\ \sin\theta_1 & \cos\theta_1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
Evaluating each matrix cell:
- **Cell (1, 1)**: $\cos\theta_2\cos\theta_1 - \sin\theta_2\sin\theta_1 + 0 = \cos(\theta_1 + \theta_2)$
- **Cell (1, 2)**: $-\cos\theta_2\sin\theta_1 - \sin\theta_2\cos\theta_1 + 0 = -(\sin\theta_1\cos\theta_2 + \cos\theta_1\sin\theta_2) = -\sin(\theta_1 + \theta_2)$
- **Cell (1, 3)**: $0 + 0 + 0 = 0$
- **Cell (2, 1)**: $\sin\theta_2\cos\theta_1 + \cos\theta_2\sin\theta_1 + 0 = \sin(\theta_1 + \theta_2)$
- **Cell (2, 2)**: $-\sin\theta_2\sin\theta_1 + \cos\theta_2\cos\theta_1 + 0 = \cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2 = \cos(\theta_1 + \theta_2)$
- **Cell (2, 3)**: $0 + 0 + 0 = 0$
- **Row 3**: $\begin{bmatrix} 0 & 0 & 1 \end{bmatrix}$

Assembling the composite matrix:
$$\mathbf{R}(\theta_2) \cdot \mathbf{R}(\theta_1) = \begin{bmatrix} \cos(\theta_1 + \theta_2) & -\sin(\theta_1 + \theta_2) & 0 \\ \sin(\theta_1 + \theta_2) & \cos(\theta_1 + \theta_2) & 0 \\ 0 & 0 & 1 \end{bmatrix} = \mathbf{R}(\theta_1 + \theta_2)$$

**Proof of Commutativity**:
Because scalar addition is commutative ($\theta_1 + \theta_2 = \theta_2 + \theta_1$):
$$\mathbf{R}(\theta_1 + \theta_2) = \mathbf{R}(\theta_2 + \theta_1) = \mathbf{R}(\theta_1) \cdot \mathbf{R}(\theta_2)$$
Therefore:
$$\mathbf{R}(\theta_2) \cdot \mathbf{R}(\theta_1) = \mathbf{R}(\theta_1) \cdot \mathbf{R}(\theta_2)$$
**Conclusion**: Successive rotations about the same axis are strictly additive and commutative. $\blacksquare$

---

### Example 3: Pivot-Point Scaling of Triangle [KTU Sep 2020 Q4 / Jan 2023 Q48]
**Problem**:
Magnify the triangle with vertices $A(0, 0), B(1, 1), C(5, 2)$ to twice its original size while keeping vertex $C(5, 2)$ fixed. Determine the coordinates of the transformed triangle.

**Solution**:
Fixed point: $(x_f, y_f) = (5, 2)$.
Scaling factor: $s_x = 2, s_y = 2$.

**Step 1: Construct the Fixed-Point Scaling Composite Matrix**:
$$\mathbf{M}_{\text{fixed}} = \mathbf{T}(5, 2) \cdot \mathbf{S}(2, 2) \cdot \mathbf{T}(-5, -2)$$
$$\mathbf{M}_{\text{fixed}} = \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -5 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{S}(2, 2) \cdot \mathbf{T}(-5, -2) = \begin{bmatrix} 2 & 0 & -10 \\ 0 & 2 & -4 \\ 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{M}_{\text{fixed}} = \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 & -10 \\ 0 & 2 & -4 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 & -5 \\ 0 & 2 & -2 \\ 0 & 0 & 1 \end{bmatrix}$$
Alternatively, using the formula $x' = s_x \cdot x + x_f(1 - s_x)$ and $y' = s_y \cdot y + y_f(1 - s_y)$:
- $x' = 2x + 5(1 - 2) = 2x - 5$
- $y' = 2y + 2(1 - 2) = 2y - 2$

**Step 2: Transform Each Vertex**:
- **Vertex $A(0, 0)$**:
  $$x_A' = 2(0) - 5 = -5, \quad y_A' = 2(0) - 2 = -2 \implies A'(-5, -2)$$
- **Vertex $B(1, 1)$**:
  $$x_B' = 2(1) - 5 = -3, \quad y_B' = 2(1) - 2 = 0 \implies B'(-3, 0)$$
- **Vertex $C(5, 2)$**:
  $$x_C' = 2(5) - 5 = 5, \quad y_C' = 2(2) - 2 = 2 \implies C'(5, 2)$$
*(Vertex C remains invariant at $(5, 2)$, verifying correctness).*

**Final Transformed Coordinates**: $A'(-5, -2), B'(-3, 0), C'(5, 2)$.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [Dec 2018 Q4 — 4 Marks]
**Question**:
Given a triangle $A(20, 10), B(80, 20), C(50, 70)$. Find the coordinates of the vertices after each of the following transformations:
(a) Reflection about the line $y = x$.
(b) Rotation of the triangle $ABC$ about vertex $A$ in clockwise direction by an angle of $90^\circ$.

**Solution**:

#### Part (a): Reflection About the Line $y = x$
The transformation matrix for reflection across $y = x$ swaps the $x$ and $y$ coordinates:
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix} \implies x' = y, \ y' = x$$
Applying this to each vertex:
- $A(20, 10) \implies A'(10, 20)$
- $B(80, 20) \implies B'(20, 80)$
- $C(50, 70) \implies C'(70, 50)$

**Result (a)**: $A'(10, 20), B'(20, 80), C'(70, 50)$.

---

#### Part (b): Clockwise Rotation by $90^\circ$ About Vertex $A(20, 10)$
Clockwise rotation by $90^\circ$ corresponds to mathematical angle $\theta = -90^\circ$:
$$\cos(-90^\circ) = 0, \quad \sin(-90^\circ) = -1$$
Pivot point: $(x_r, y_r) = (20, 10)$.

**Transformation Equations**:
$$x' = x_r + (x - x_r)\cos\theta - (y - y_r)\sin\theta = 20 + (x - 20)(0) - (y - 10)(-1) = 20 + (y - 10) = y + 10$$
$$y' = y_r + (x - x_r)\sin\theta + (y - y_r)\cos\theta = 10 + (x - 20)(-1) + (y - 10)(0) = 10 - x + 20 = 30 - x$$

Applying to each vertex:
- **Vertex $A(20, 10)$**:
  $$x_A' = 10 + 10 = 20, \quad y_A' = 30 - 20 = 10 \implies A'(20, 10) \quad \text{(invariant pivot)}$$
- **Vertex $B(80, 20)$**:
  $$x_B' = 20 + 10 = 30, \quad y_B' = 30 - 80 = -50 \implies B'(30, -50)$$
- **Vertex $C(50, 70)$**:
  $$x_C' = 70 + 10 = 80, \quad y_C' = 30 - 50 = -20 \implies C'(80, -20)$$

**Result (b)**: $A'(20, 10), B'(30, -50), C'(80, -20)$.

---

### Question 2 [June 2022 Q5 — 4 Marks]
**Question**:
Shear a square with vertices $A(0, 0), B(1, 0), C(1, 1), D(0, 1)$ with shear parameter $sh_x = 0.5$ relative to the line $Y = -1$.

**Solution**:

The general equation for X-direction shear relative to a horizontal reference line $y = y_{\text{ref}}$ is:
$$x' = x + sh_x(y - y_{\text{ref}})$$
$$y' = y$$
Given $sh_x = 0.5$ and $y_{\text{ref}} = -1$:
$$x' = x + 0.5(y - (-1)) = x + 0.5(y + 1) = x + 0.5y + 0.5$$
$$y' = y$$

In matrix form:
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0.5 & 0.5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

**Transforming Each Vertex**:
1. **Vertex $A(0, 0)$**:
   $$x_A' = 0 + 0.5(0) + 0.5 = 0.5, \quad y_A' = 0 \implies A'(0.5, 0)$$
2. **Vertex $B(1, 0)$**:
   $$x_B' = 1 + 0.5(0) + 0.5 = 1.5, \quad y_B' = 0 \implies B'(1.5, 0)$$
3. **Vertex $C(1, 1)$**:
   $$x_C' = 1 + 0.5(1) + 0.5 = 2.0, \quad y_C' = 1 \implies C'(2.0, 1)$$
4. **Vertex $D(0, 1)$**:
   $$x_D' = 0 + 0.5(1) + 0.5 = 1.0, \quad y_D' = 1 \implies D'(1.0, 1)$$

**Final Coordinates**: $A'(0.5, 0), B'(1.5, 0), C'(2.0, 1), D'(1.0, 1)$. (The square is sheared into a parallelogram of equal height and base width).

---

### Question 3 [Dec 2021 Q14a — 5 Marks]
**Question**:
Perform the following transformations on a line segment with endpoints $A(10, 20)$ and $B(40, 30)$:
(i) Scale the object two times in x-direction and three times in y-direction.
(ii) Rotate the object by $90^\circ$ counterclockwise about origin.
(iii) Translate one unit in x-direction and two units in y-direction.
Apply the second transformation on the result of the first, and the third on the result of the second.

**Solution**:

Let the initial point be $P = \begin{bmatrix} x & y & 1 \end{bmatrix}^T$.

**Step 1: Individual Transformation Matrices**:
1. Scaling: $s_x = 2, s_y = 3$:
   $$\mathbf{S} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
2. Rotation: $\theta = 90^\circ$ ($\cos 90^\circ = 0, \sin 90^\circ = 1$):
   $$\mathbf{R} = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
3. Translation: $t_x = 1, t_y = 2$:
   $$\mathbf{T} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}$$

**Step 2: Construct Composite Transformation Matrix $\mathbf{M} = \mathbf{T} \cdot \mathbf{R} \cdot \mathbf{S}$**:
$$\mathbf{R} \cdot \mathbf{S} = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{M} = \mathbf{T} \cdot (\mathbf{R} \cdot \mathbf{S}) = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -3 & 1 \\ 2 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix}$$

**Step 3: Transform Endpoint $A(10, 20)$**:
$$\begin{bmatrix} x_A' \\ y_A' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -3 & 1 \\ 2 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 10 \\ 20 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(10) - 3(20) + 1(1) \\ 2(10) + 0(20) + 2(1) \\ 1 \end{bmatrix} = \begin{bmatrix} -59 \\ 22 \\ 1 \end{bmatrix} \implies A'(-59, 22)$$

**Step 4: Transform Endpoint $B(40, 30)$**:
$$\begin{bmatrix} x_B' \\ y_B' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -3 & 1 \\ 2 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 40 \\ 30 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(40) - 3(30) + 1(1) \\ 2(40) + 0(30) + 2(1) \\ 1 \end{bmatrix} = \begin{bmatrix} -89 \\ 82 \\ 1 \end{bmatrix} \implies B'(-89, 82)$$

**Final Transformed Endpoints**: $A'(-59, 22)$ and $B'(-89, 82)$.

---

### Question 4 [Dec 2020 Q15a — 4 Marks]
**Question**:
Rotate the point $P(4, 3)$ by $45^\circ$ counterclockwise about the origin.

**Solution**:

Angle $\theta = 45^\circ$:
$$\cos 45^\circ = \frac{1}{\sqrt{2}} \approx 0.7071, \quad \sin 45^\circ = \frac{1}{\sqrt{2}} \approx 0.7071$$

Transformation Equations:
$$x' = x\cos\theta - y\sin\theta = 4(0.7071) - 3(0.7071) = 0.7071(4 - 3) = 0.7071 = \frac{1}{\sqrt{2}}$$
$$y' = x\sin\theta + y\cos\theta = 4(0.7071) + 3(0.7071) = 0.7071(4 + 3) = 7(0.7071) = 4.9497 = \frac{7}{\sqrt{2}}$$

In exact radical form:
$$P'\left(\frac{1}{\sqrt{2}}, \ \frac{7}{\sqrt{2}}\right) \approx P'(0.7071, \ 4.9497)$$

---

### Question 5 [May 2019 Q14a — 5 Marks]
**Question**:
Transform the point $P(6, 4)$ by the following sequence:
(i) Translate by $t_x = -2, t_y = 4$
(ii) Scale by $s_x = 2, s_y = 1$
(iii) Rotate by $90^\circ$ clockwise about the origin.

**Solution**:

Let initial point be $P = \begin{bmatrix} 6 & 4 & 1 \end{bmatrix}^T$.

1. **Translation $\mathbf{T}(-2, 4)$**:
   $$\mathbf{T} = \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{bmatrix}$$
2. **Scaling $\mathbf{S}(2, 1)$**:
   $$\mathbf{S} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
3. **Clockwise Rotation by $90^\circ$ ($\theta = -90^\circ \implies \cos(-90^\circ) = 0, \sin(-90^\circ) = -1$)**:
   $$\mathbf{R} = \begin{bmatrix} \cos(-90^\circ) & -\sin(-90^\circ) & 0 \\ \sin(-90^\circ) & \cos(-90^\circ) & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

**Construct Composite Matrix $\mathbf{M} = \mathbf{R} \cdot \mathbf{S} \cdot \mathbf{T}$**:
$$\mathbf{S} \cdot \mathbf{T} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 & -4 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{M} = \mathbf{R} \cdot (\mathbf{S} \cdot \mathbf{T}) = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 & -4 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 4 \\ -2 & 0 & 4 \\ 0 & 0 & 1 \end{bmatrix}$$

**Apply to $P(6, 4)$**:
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 4 \\ -2 & 0 & 4 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 6 \\ 4 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(6) + 1(4) + 4(1) \\ -2(6) + 0(4) + 4(1) \\ 1 \end{bmatrix} = \begin{bmatrix} 8 \\ -8 \\ 1 \end{bmatrix}$$
**Final Coordinates**: $P'(8, -8)$.

---

### Question 6 [Dec 2021 Q4 / May 2019 Q4 / Dec 2018 Q4 — 4 Marks]
**Question**:
What do you understand by the homogeneous coordinate system? What is its significance in computer graphics?

**Solution**:

**Definition**:
A homogeneous coordinate system represents an $n$-dimensional point as an $(n+1)$-dimensional vector by introducing an extra projection coordinate $w$:
$$(x, y) \in \mathbb{R}^2 \implies (X_h, Y_h, w) \in \mathbb{P}^2$$
where Cartesian coordinates are recovered via perspective division:
$$x = \frac{X_h}{w}, \quad y = \frac{Y_h}{w} \quad (w \ne 0)$$
In standard 2D affine graphics transformations, $w$ is normalized to $1$, yielding the triple $\begin{bmatrix} x & y & 1 \end{bmatrix}^T$.

**Significance & Architectural Necessity**:
1. **Unification of Translation with Linear Transformations**:
   In standard 2D Cartesian coordinates, rotation, reflection, and scaling are represented as matrix multiplications ($P' = \mathbf{M} P$), while translation is an addition ($P' = P + T$). In homogeneous coordinates, translation is expressed as a standard matrix multiplication:
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$
2. **Matrix Concatenation (Pipelining Efficiency)**:
   Because all affine transformations are $3 \times 3$ matrices, any arbitrary sequence of translations, rotations, and scalings can be multiplied into a single composite matrix $\mathbf{M}_{\text{composite}}$. Instead of applying multiple operations sequentially to every vertex, modern graphics hardware computes $\mathbf{M}_{\text{composite}}$ once and transforms millions of vertices with a single matrix multiplication per vertex.
3. **Unified Perspective Projections**:
   In 3D viewing pipelines, perspective foreshortening requires dividing $x$ and $y$ by depth $z$. Homogeneous coordinates achieve this division naturally by placing $-z/d$ into the $w$-coordinate, deferring division to a single hardware-level perspective divide stage ($x = X_h/w$).
4. **Representation of Points at Infinity**:
   Setting $w = 0$ provides a mathematically rigorous representation for directional vectors and vanishing points at infinity without causing division-by-zero exceptions.

---

### Question 7 [Dec 2018 Q15a — 9 Marks]
**Question**:
What are the steps for general 3D rotation if the rotation axis is not parallel to any of the principal coordinate axes? The rotation axis is defined by endpoints $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$. Write down the composite matrix representation.

**Solution**:

When an arbitrary rotation axis in 3D space is specified by two points $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$, the rotation by angle $\theta$ cannot be executed directly by coordinate-axis rotation matrices ($\mathbf{R}_x, \mathbf{R}_y, \mathbf{R}_z$). The procedure requires a **7-step geometric alignment sequence**:

```
Arbitrary Axis L                 Translate P1 to Origin           Rotate into XZ Plane
       P2                                                                    Z
      /                                 P2'                                  ▲  Axis aligned with Z
     /                                 /                                     │ /
    /                                 /                                      │/
   P1 ──────────────►               (0,0,0) ──────────►          (0,0,0) ────┴────────► X
  (World Space)                     T(-x1,-y1,-z1)                 Rx(alpha) * Ry(beta)
```

**The 7-Step Algorithm**:
1. **Translate the rotation axis to the coordinate origin**:
   Translate point $P_1$ to the origin $(0, 0, 0)$ so the axis passes through the origin:
   $$\mathbf{T}_1 = \mathbf{T}(-x_1, -y_1, -z_1) = \begin{bmatrix} 1 & 0 & 0 & -x_1 \\ 0 & 1 & 0 & -y_1 \\ 0 & 0 & 1 & -z_1 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   The direction vector of the axis is $\vec{V} = P_2 - P_1 = \begin{bmatrix} \Delta x & \Delta y & \Delta z \end{bmatrix}^T$.
   Its unit direction vector is $\vec{u} = \frac{\vec{V}}{|\vec{V}|} = \begin{bmatrix} a & b & c \end{bmatrix}^T$, where $a^2 + b^2 + c^2 = 1$.

2. **Rotate the axis into the XZ coordinate plane (Rotation about X-axis)**:
   Project $\vec{u}$ onto the YZ-plane: the projection has length $d = \sqrt{b^2 + c^2}$. Rotate by angle $\alpha$ about the X-axis so the vector falls onto the XZ-plane:
   $$\cos\alpha = \frac{c}{d}, \quad \sin\alpha = \frac{b}{d}$$
   $$\mathbf{R}_x(\alpha) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & c/d & -b/d & 0 \\ 0 & b/d & c/d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

3. **Rotate the axis to coincide with the positive Z-axis (Rotation about Y-axis)**:
   In the XZ-plane, the vector has components $a$ along X and $d$ along Z. Rotate by angle $-\beta$ about the Y-axis to align the vector with the Z-axis:
   $$\cos\beta = d, \quad \sin\beta = a \quad (\text{since } a^2 + d^2 = a^2 + b^2 + c^2 = 1)$$
   $$\mathbf{R}_y(-\beta) = \begin{bmatrix} d & 0 & -a & 0 \\ 0 & 1 & 0 & 0 \\ a & 0 & d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

4. **Perform the desired rotation by angle $\theta$ about the Z-axis**:
   $$\mathbf{R}_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

5. **Apply the inverse rotation about the Y-axis**:
   $$\mathbf{R}_y^{-1}(-\beta) = \mathbf{R}_y(\beta) = \begin{bmatrix} d & 0 & a & 0 \\ 0 & 1 & 0 & 0 \\ -a & 0 & d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

6. **Apply the inverse rotation about the X-axis**:
   $$\mathbf{R}_x^{-1}(\alpha) = \mathbf{R}_x(-\alpha) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & c/d & b/d & 0 \\ 0 & -b/d & c/d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

7. **Apply the inverse translation back to $P_1$**:
   $$\mathbf{T}_1^{-1} = \mathbf{T}(x_1, y_1, z_1) = \begin{bmatrix} 1 & 0 & 0 & x_1 \\ 0 & 1 & 0 & y_1 \\ 0 & 0 & 1 & z_1 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

**Composite Transformation Matrix**:
$$\mathbf{M}_{\text{composite}} = \mathbf{T}_1^{-1} \cdot \mathbf{R}_x^{-1}(\alpha) \cdot \mathbf{R}_y^{-1}(-\beta) \cdot \mathbf{R}_z(\theta) \cdot \mathbf{R}_y(-\beta) \cdot \mathbf{R}_x(\alpha) \cdot \mathbf{T}_1$$
This $4 \times 4$ matrix achieves pure rotation by angle $\theta$ about the arbitrary line passing through $P_1$ and $P_2$.
