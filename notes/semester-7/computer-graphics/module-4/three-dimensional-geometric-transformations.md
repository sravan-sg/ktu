# 3D Geometric Transformations: Translation, Scaling, Rotation, Reflection & Shear

## 1. Explanation

Three-dimensional geometric transformations extend 2D affine mapping principles into three-dimensional Euclidean space $\mathbb{R}^3$. To unify linear transformations (rotation, scaling, reflection, shear) with non-linear translations into a single coherent computational framework, 3D points are expressed in **4D homogeneous coordinates**:
$$P(x, y, z) \implies \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$
Every affine 3D transformation is represented as a uniform $4 \times 4$ matrix.

---

### The Fundamental 3D Transformations

#### 1. 3D Translation
Displaces a point $P(x, y, z)$ by a 3D translation displacement vector $\vec{T} = \begin{bmatrix} t_x & t_y & t_z \end{bmatrix}^T$:
$$x' = x + t_x, \quad y' = y + t_y, \quad z' = z + t_z$$

In $4 \times 4$ homogeneous matrix form:
$$\mathbf{T}(t_x, t_y, t_z) = \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

The inverse translation matrix undoes the displacement:
$$\mathbf{T}^{-1}(t_x, t_y, t_z) = \mathbf{T}(-t_x, -t_y, -t_z) = \begin{bmatrix} 1 & 0 & 0 & -t_x \\ 0 & 1 & 0 & -t_y \\ 0 & 0 & 1 & -t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

#### 2. 3D Scaling (Relative to Coordinate Origin)
Multiplies the coordinates of an object by independent scaling factors $s_x, s_y, s_z$:
$$x' = x \cdot s_x, \quad y' = y \cdot s_y, \quad z' = z \cdot s_z$$

In $4 \times 4$ homogeneous matrix form:
$$\mathbf{S}(s_x, s_y, s_z) = \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
- **Uniform Scaling**: $s_x = s_y = s_z$ (preserves shape and proportions).
- **Differential Scaling**: $s_x \ne s_y$ or $s_y \ne s_z$ (distorts geometric proportions).
- Inverse scaling: $\mathbf{S}^{-1}(s_x, s_y, s_z) = \mathbf{S}(1/s_x, 1/s_y, 1/s_z)$.

#### 3. 3D Coordinate-Axis Rotations
In three-dimensional space, rotation requires defining both an **angle of rotation $\theta$** and a **spatial axis of rotation**. By convention in a standard right-handed Cartesian coordinate system ($X \times Y = Z$), a positive angle $\theta$ produces counterclockwise rotation when looking along the positive axis toward the coordinate origin.

##### A. Rotation About the Z-Axis ($\mathbf{R}_z(\theta)$)
The $z$-coordinate remains invariant; planar rotation occurs strictly in the $xy$-plane:
$$x' = x\cos\theta - y\sin\theta$$
$$y' = x\sin\theta + y\cos\theta$$
$$z' = z$$

$$\mathbf{R}_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

##### B. Rotation About the X-Axis ($\mathbf{R}_x(\theta)$)
The $x$-coordinate remains invariant; planar rotation occurs strictly in the $yz$-plane:
$$x' = x$$
$$y' = y\cos\theta - z\sin\theta$$
$$z' = y\sin\theta + z\cos\theta$$

$$\mathbf{R}_x(\theta) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta & 0 \\ 0 & \sin\theta & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

##### C. Rotation About the Y-Axis ($\mathbf{R}_y(\theta)$)
The $y$-coordinate remains invariant; planar rotation occurs in the $zx$-plane. 
Notice the cyclic permutation of axes ($X \to Y \to Z \to X$). Because rotation proceeds from the Z-axis toward the X-axis:
$$x' = x\cos\theta + z\sin\theta$$
$$y' = y$$
$$z' = -x\sin\theta + z\cos\theta$$

$$\mathbf{R}_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta & 0 \\ 0 & 1 & 0 & 0 \\ -\sin\theta & 0 & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

> **Important Sign Note**: The negative sign appears in the $(3, 1)$ element ($-\sin\theta$) rather than the $(1, 3)$ element. This is mathematically required to preserve right-handed cyclic orthogonality ($Z \times X = Y$).

---

### 3D Reflection & 3D Shear

#### 1. 3D Reflection
A 3D reflection produces a mirror replica across a designated reflection plane:
- **Across the XY-Plane ($z = 0$)**: Inverts the sign of the $z$-coordinate:
  $$\mathbf{M}_{xy} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
- **Across the XZ-Plane ($y = 0$)**: Inverts the sign of the $y$-coordinate:
  $$\mathbf{M}_{xz} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
- **Across the YZ-Plane ($x = 0$)**: Inverts the sign of the $x$-coordinate:
  $$\mathbf{M}_{yz} = \begin{bmatrix} -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

#### 2. 3D Shear
Deforms 3D geometry such that coordinate planes slide parallel to each other:
- **X-Direction Shear (shifts $x$ based on $y$ and $z$)**:
  $$x' = x + sh_{xy} \cdot y + sh_{xz} \cdot z, \quad y' = y, \quad z' = z$$
  $$\mathbf{Sh}_x(sh_{xy}, sh_{xz}) = \begin{bmatrix} 1 & sh_{xy} & sh_{xz} & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
- **Z-Direction Shear (shifts $z$ based on $x$ and $y$)**:
  $$x' = x, \quad y' = y, \quad z' = z + sh_{zx} \cdot x + sh_{zy} \cdot y$$
  $$\mathbf{Sh}_z(sh_{zx}, sh_{zy}) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ sh_{zx} & sh_{zy} & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

---

### Scaling Relative to an Arbitrary Fixed Point $(x_f, y_f, z_f)$

To scale a 3D object while keeping a specific anchor vertex $(x_f, y_f, z_f)$ fixed in space:
1. Translate the fixed point to the coordinate origin: $\mathbf{T}(-x_f, -y_f, -z_f)$
2. Apply coordinate scaling: $\mathbf{S}(s_x, s_y, s_z)$
3. Translate the origin back to the fixed point: $\mathbf{T}(x_f, y_f, z_f)$

**Composite Matrix Derivation**:
$$\mathbf{M}_{\text{fixed}} = \mathbf{T}(x_f, y_f, z_f) \cdot \mathbf{S}(s_x, s_y, s_z) \cdot \mathbf{T}(-x_f, -y_f, -z_f)$$
$$\mathbf{M}_{\text{fixed}} = \begin{bmatrix} 1 & 0 & 0 & x_f \\ 0 & 1 & 0 & y_f \\ 0 & 0 & 1 & z_f \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 & -x_f \\ 0 & 1 & 0 & -y_f \\ 0 & 0 & 1 & -z_f \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{M}_{\text{fixed}} = \begin{bmatrix} s_x & 0 & 0 & x_f(1 - s_x) \\ 0 & s_y & 0 & y_f(1 - s_y) \\ 0 & 0 & s_z & z_f(1 - s_z) \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

---

### General 3D Rotation About an Arbitrary Axis in Space

When rotating an object by angle $\theta$ about an arbitrary line in 3D space defined by two points $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$, coordinate-axis rotation matrices cannot be applied directly. We must align the arbitrary axis with one of the primary Cartesian coordinate axes (typically the Z-axis) through a systematic **7-stage geometric transformation sequence**.

```
    Arbitrary Line L                  Translate P1 to Origin            Rotate into XZ Plane
          P2                                                                     Z
         /                                  P2'                                  ▲  Axis aligned with Z
        /                                  /                                     │ /
       /                                  /                                      │/
      P1 ──────────────►                (0,0,0) ──────────►           (0,0,0) ───┴────────► X
     (World Space)                      T(-x1,-y1,-z1)                  Rx(alpha) * Ry(beta)
```

#### The 7-Stage Alignment Algorithm:
1. **Translation to Origin**:
   Translate point $P_1$ to the coordinate origin $(0, 0, 0)$:
   $$\mathbf{T}_1 = \mathbf{T}(-x_1, -y_1, -z_1)$$
   The vector along the axis is $\vec{V} = P_2 - P_1 = \begin{bmatrix} \Delta x & \Delta y & \Delta z \end{bmatrix}^T$.
   Its normalized unit vector is:
   $$\hat{u} = \frac{\vec{V}}{|\vec{V}|} = \begin{bmatrix} a \\ b \\ c \end{bmatrix}, \quad \text{where } a^2 + b^2 + c^2 = 1$$

2. **Rotate Axis into the XZ Coordinate Plane**:
   Project $\hat{u}$ onto the YZ-plane. The length of this projection is $d = \sqrt{b^2 + c^2}$. Rotate by angle $\alpha$ about the X-axis:
   $$\cos\alpha = \frac{c}{d}, \quad \sin\alpha = \frac{b}{d}$$
   $$\mathbf{R}_x(\alpha) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & c/d & -b/d & 0 \\ 0 & b/d & c/d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

3. **Rotate Axis onto the Positive Z-Axis**:
   The vector now lies entirely in the XZ-plane with components $a$ along X and $d$ along Z. Rotate by angle $-\beta$ about the Y-axis:
   $$\cos\beta = d, \quad \sin\beta = a \quad (\text{since } a^2 + d^2 = a^2 + b^2 + c^2 = 1)$$
   $$\mathbf{R}_y(-\beta) = \begin{bmatrix} d & 0 & -a & 0 \\ 0 & 1 & 0 & 0 \\ a & 0 & d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

4. **Rotate About the Z-Axis by Angle $\theta$**:
   Now that the arbitrary axis is coincident with the Z-axis, apply the desired rotation:
   $$\mathbf{R}_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

5. **Inverse Rotation About the Y-Axis**:
   $$\mathbf{R}_y^{-1}(-\beta) = \mathbf{R}_y(\beta) = \begin{bmatrix} d & 0 & a & 0 \\ 0 & 1 & 0 & 0 \\ -a & 0 & d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

6. **Inverse Rotation About the X-Axis**:
   $$\mathbf{R}_x^{-1}(\alpha) = \mathbf{R}_x(-\alpha) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & c/d & b/d & 0 \\ 0 & -b/d & c/d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

7. **Inverse Translation Back to $P_1$**:
   $$\mathbf{T}_1^{-1} = \mathbf{T}(x_1, y_1, z_1)$$

#### Composite Transformation Matrix:
$$\mathbf{M}_{\text{composite}} = \mathbf{T}_1^{-1} \cdot \mathbf{R}_x^{-1}(\alpha) \cdot \mathbf{R}_y^{-1}(-\beta) \cdot \mathbf{R}_z(\theta) \cdot \mathbf{R}_y(-\beta) \cdot \mathbf{R}_x(\alpha) \cdot \mathbf{T}_1$$

---

## 2. Example: 3D Fixed-Point Scaling Numerical Calculation

Consider a 3D unit cube with vertices:
$$P_0(0, 0, 0), \ P_1(1, 0, 0), \ P_2(1, 1, 0), \ P_3(0, 1, 0), \ P_4(0, 0, 1), \ P_5(1, 0, 1), \ P_6(1, 1, 1), \ P_7(0, 1, 1)$$
Scale this cube by factors $s_x = 2, s_y = 3, s_z = 2$ relative to its corner vertex $P_6(1, 1, 1)$.

**Step 1: Compute Matrix Coefficients**:
Fixed point: $(x_f, y_f, z_f) = (1, 1, 1)$.
- $t_x' = x_f(1 - s_x) = 1(1 - 2) = -1$
- $t_y' = y_f(1 - s_y) = 1(1 - 3) = -2$
- $t_z' = z_f(1 - s_z) = 1(1 - 2) = -1$

$$\mathbf{M}_{\text{fixed}} = \begin{bmatrix} 2 & 0 & 0 & -1 \\ 0 & 3 & 0 & -2 \\ 0 & 0 & 2 & -1 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

**Step 2: Coordinate Transformation Formula**:
$$x' = 2x - 1, \quad y' = 3y - 2, \quad z' = 2z - 1$$

**Step 3: Transform Selected Vertices**:
- For $P_0(0, 0, 0)$: $x' = -1, y' = -2, z' = -1 \implies P_0'(-1, -2, -1)$.
- For $P_6(1, 1, 1)$: $x' = 2(1) - 1 = 1, y' = 3(1) - 2 = 1, z' = 2(1) - 1 = 1 \implies P_6'(1, 1, 1)$ *(Invariant anchor)*.
- For $P_1(1, 0, 0)$: $x' = 1, y' = -2, z' = -1 \implies P_1'(1, -2, -1)$.

---

## 3. Applications & Use Cases

1. **3D Character Rigging & Skeletal Animation**:
   In skeletal animation (Blender, Maya), bones are modeled as hierarchical kinematic chains. When a forearm rotates about the elbow joint, the transformation is evaluated as a 3D rotation about an arbitrary spatial axis passing through the elbow pivot.
2. **Flight Simulators & Avionics (Euler Angles & Quaternions)**:
   Aircraft orientation is specified via three sequential body-axis rotations: Yaw ($\mathbf{R}_z$), Pitch ($\mathbf{R}_y$), and Roll ($\mathbf{R}_x$).
3. **Robotics Inverse Kinematics**:
   Robotic arms with multiple revolute joints use Denavit-Hartenberg (DH) parameters, where each link's transformation relative to the previous link is evaluated using composite translations and rotations about arbitrary joint axes.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: 3D Point Rotation About Coordinate Axes [KTU Dec 2020 Pattern]
**Problem**:
A 3D point $P(2, 4, 6)$ is rotated by $90^\circ$ counterclockwise about the Y-axis, and subsequently rotated by $90^\circ$ counterclockwise about the X-axis. Find its final coordinates.

**Solution**:
1. **Rotation About Y-Axis by $90^\circ$**:
   $$\cos 90^\circ = 0, \quad \sin 90^\circ = 1$$
   $$\mathbf{R}_y(90^\circ) = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   $$\begin{bmatrix} x_1 \\ y_1 \\ z_1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 4 \\ 6 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \\ -2 \\ 1 \end{bmatrix} \implies P_1(6, 4, -2)$$

2. **Subsequent Rotation About X-Axis by $90^\circ$**:
   $$\mathbf{R}_x(90^\circ) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   $$\begin{bmatrix} x_2 \\ y_2 \\ z_2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 6 \\ 4 \\ -2 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ -(-2) \\ 4 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 2 \\ 4 \\ 1 \end{bmatrix}$$

**Final Coordinates**: $P'(6, 2, 4)$.

---

### Example 2: Arbitrary Axis Direction Cosine Derivation [KTU Analytical Pattern]
**Problem**:
An axis of rotation passes through points $P_1(1, 2, 3)$ and $P_2(4, 6, 3)$. 
1. Compute the direction vector and normalized unit direction vector $\hat{u}$.
2. Determine the rotation angles $\alpha$ (about X) and $\beta$ (about Y) needed to align this axis with the Z-axis.

**Solution**:
1. **Direction Vector**:
   $$\vec{V} = P_2 - P_1 = \begin{bmatrix} 4 - 1 \\ 6 - 2 \\ 3 - 3 \end{bmatrix} = \begin{bmatrix} 3 \\ 4 \\ 0 \end{bmatrix}$$
   Magnitude: $|\vec{V}| = \sqrt{3^2 + 4^2 + 0^2} = \sqrt{9 + 16 + 0} = \sqrt{25} = 5$.
   Normalized unit vector:
   $$\hat{u} = \begin{bmatrix} a \\ b \\ c \end{bmatrix} = \begin{bmatrix} 3/5 \\ 4/5 \\ 0 \end{bmatrix} = \begin{bmatrix} 0.6 \\ 0.8 \\ 0 \end{bmatrix}$$

2. **Compute Alignment Angles**:
   - Length of projection in YZ-plane:
     $$d = \sqrt{b^2 + c^2} = \sqrt{(0.8)^2 + 0^2} = 0.8$$
   - Angle $\alpha$ (rotation about X-axis to align with XZ plane):
     $$\cos\alpha = \frac{c}{d} = \frac{0}{0.8} = 0, \quad \sin\alpha = \frac{b}{d} = \frac{0.8}{0.8} = 1 \implies \alpha = 90^\circ$$
   - Angle $\beta$ (rotation about Y-axis to align with Z axis):
     $$\cos\beta = d = 0.8, \quad \sin\beta = a = 0.6 \implies \beta = \arcsin(0.6) \approx 36.87^\circ$$

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [Dec 2018 Q15a — 9 Marks]
**Question**:
What are the steps for general 3D rotation if the rotation axis is not parallel to any of the principal axes? The rotation axis is defined by points $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$. Write down the composite matrix representation.

**Solution**:

Rotating an object by an angle $\theta$ about an arbitrary axis specified by two spatial coordinates $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ is achieved through the following **7-step geometric transformation sequence**:

```
Arbitrary Axis L                 Translate P1 to Origin           Rotate into XZ Plane
       P2                                                                    Z
      /                                 P2'                                  ▲  Axis aligned with Z
     /                                 /                                     │ /
    /                                 /                                      │/
   P1 ──────────────►               (0,0,0) ──────────►          (0,0,0) ────┴────────► X
  (World Space)                     T(-x1,-y1,-z1)                 Rx(alpha) * Ry(beta)
```

1. **Step 1: Translate the rotation axis to the coordinate origin**:
   Translate $P_1$ to $(0, 0, 0)$ so that the rotation axis passes through the origin:
   $$\mathbf{T}_1 = \mathbf{T}(-x_1, -y_1, -z_1) = \begin{bmatrix} 1 & 0 & 0 & -x_1 \\ 0 & 1 & 0 & -y_1 \\ 0 & 0 & 1 & -z_1 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   The direction vector of the line is $\vec{V} = P_2 - P_1 = \begin{bmatrix} \Delta x & \Delta y & \Delta z \end{bmatrix}^T$.
   Its normalized unit direction vector is:
   $$\hat{u} = \frac{\vec{V}}{|\vec{V}|} = \begin{bmatrix} a \\ b \\ c \end{bmatrix}, \quad \text{where } a^2 + b^2 + c^2 = 1$$

2. **Step 2: Rotate the axis into the XZ coordinate plane (Rotation about X-axis)**:
   Project $\hat{u}$ onto the YZ-plane, which has length $d = \sqrt{b^2 + c^2}$. Rotate by angle $\alpha$ about the X-axis:
   $$\cos\alpha = \frac{c}{d}, \quad \sin\alpha = \frac{b}{d}$$
   $$\mathbf{R}_x(\alpha) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & c/d & -b/d & 0 \\ 0 & b/d & c/d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

3. **Step 3: Rotate the axis onto the positive Z-axis (Rotation about Y-axis)**:
   The axis now lies in the XZ plane with coordinates $(a, 0, d)$. Rotate by angle $-\beta$ about the Y-axis:
   $$\cos\beta = d, \quad \sin\beta = a \quad (\text{since } a^2 + d^2 = a^2 + b^2 + c^2 = 1)$$
   $$\mathbf{R}_y(-\beta) = \begin{bmatrix} d & 0 & -a & 0 \\ 0 & 1 & 0 & 0 \\ a & 0 & d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

4. **Step 4: Rotate about the Z-axis by angle $\theta$**:
   Now that the axis coincides with the Z-axis, apply the primary rotation:
   $$\mathbf{R}_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

5. **Step 5: Apply inverse rotation about Y-axis**:
   $$\mathbf{R}_y^{-1}(-\beta) = \mathbf{R}_y(\beta) = \begin{bmatrix} d & 0 & a & 0 \\ 0 & 1 & 0 & 0 \\ -a & 0 & d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

6. **Step 6: Apply inverse rotation about X-axis**:
   $$\mathbf{R}_x^{-1}(\alpha) = \mathbf{R}_x(-\alpha) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & c/d & b/d & 0 \\ 0 & -b/d & c/d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

7. **Step 7: Apply inverse translation back to $P_1$**:
   $$\mathbf{T}_1^{-1} = \mathbf{T}(x_1, y_1, z_1) = \begin{bmatrix} 1 & 0 & 0 & x_1 \\ 0 & 1 & 0 & y_1 \\ 0 & 0 & 1 & z_1 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

**Composite Transformation Matrix**:
$$\mathbf{M}_{\text{composite}} = \mathbf{T}_1^{-1} \cdot \mathbf{R}_x^{-1}(\alpha) \cdot \mathbf{R}_y^{-1}(-\beta) \cdot \mathbf{R}_z(\theta) \cdot \mathbf{R}_y(-\beta) \cdot \mathbf{R}_x(\alpha) \cdot \mathbf{T}_1$$

---

### Question 2 [Dec 2021 Q16a — 5 Marks]
**Question**:
Describe the steps involved in scaling a 3D object with respect to a fixed point $(x_f, y_f, z_f)$. Write the composite transformation matrix.

**Solution**:

To scale a 3D object by scaling factors $(s_x, s_y, s_z)$ while maintaining a specific point $P_f(x_f, y_f, z_f)$ stationary in space, we follow a 3-step transformation sequence:

1. **Step 1: Translate the fixed point to the coordinate origin**:
   $$\mathbf{T}(-x_f, -y_f, -z_f) = \begin{bmatrix} 1 & 0 & 0 & -x_f \\ 0 & 1 & 0 & -y_f \\ 0 & 0 & 1 & -z_f \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

2. **Step 2: Scale the object with respect to the origin**:
   $$\mathbf{S}(s_x, s_y, s_z) = \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

3. **Step 3: Translate the origin back to the fixed point**:
   $$\mathbf{T}(x_f, y_f, z_f) = \begin{bmatrix} 1 & 0 & 0 & x_f \\ 0 & 1 & 0 & y_f \\ 0 & 0 & 1 & z_f \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

**Matrix Concatenation**:
$$\mathbf{M}_{\text{fixed}} = \mathbf{T}(x_f, y_f, z_f) \cdot \mathbf{S}(s_x, s_y, s_z) \cdot \mathbf{T}(-x_f, -y_f, -z_f)$$
$$\mathbf{M}_{\text{fixed}} = \begin{bmatrix} 1 & 0 & 0 & x_f \\ 0 & 1 & 0 & y_f \\ 0 & 0 & 1 & z_f \\ 0 & 0 & 0 & 1 \end{bmatrix} \left( \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 & -x_f \\ 0 & 1 & 0 & -y_f \\ 0 & 0 & 1 & -z_f \\ 0 & 0 & 0 & 1 \end{bmatrix} \right)$$
$$\mathbf{M}_{\text{fixed}} = \begin{bmatrix} 1 & 0 & 0 & x_f \\ 0 & 1 & 0 & y_f \\ 0 & 0 & 1 & z_f \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} s_x & 0 & 0 & -s_x \cdot x_f \\ 0 & s_y & 0 & -s_y \cdot y_f \\ 0 & 0 & s_z & -s_z \cdot z_f \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
$$\mathbf{M}_{\text{fixed}} = \begin{bmatrix} s_x & 0 & 0 & x_f(1 - s_x) \\ 0 & s_y & 0 & y_f(1 - s_y) \\ 0 & 0 & s_z & z_f(1 - s_z) \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

Multiplying $\mathbf{M}_{\text{fixed}}$ by an arbitrary point $\begin{bmatrix} x & y & z & 1 \end{bmatrix}^T$ yields the transformation equations:
$$x' = s_x \cdot x + x_f(1 - s_x)$$
$$y' = s_y \cdot y + y_f(1 - s_y)$$
$$z' = s_z \cdot z + z_f(1 - s_z)$$
Notice that when $(x, y, z) = (x_f, y_f, z_f)$, we get $(x', y', z') = (x_f, y_f, z_f)$, confirming the fixed point remains stationary.
