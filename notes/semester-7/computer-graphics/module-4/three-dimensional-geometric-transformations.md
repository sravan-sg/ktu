# 3D Geometric Transformations: Translation, Scaling & Rotation

## 1. Explanation
Three-dimensional geometric transformations extend 2D affine transformations into 3D Cartesian space $\mathbb{R}^3$. To unify translations with linear transformations (rotation, scaling, reflection, shear), 3D points are represented in **4D homogeneous coordinates**:
$$P(x, y, z) \implies \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$
Every affine transformation is represented by a $4 \times 4$ matrix.

---

### Basic 3D Transformations

#### 1. 3D Translation
Displaces a point $P(x, y, z)$ by translation vector $\vec{T} = \begin{bmatrix} t_x & t_y & t_z \end{bmatrix}^T$:
$$x' = x + t_x, \quad y' = y + t_y, \quad z' = z + t_z$$

In $4 \times 4$ homogeneous matrix form:
$$\mathbf{T}(t_x, t_y, t_z) = \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

#### 2. 3D Scaling
Resizes an object relative to the coordinate origin by scaling factors $(s_x, s_y, s_z)$:
$$x' = x \cdot s_x, \quad y' = y \cdot s_y, \quad z' = z \cdot s_z$$

In $4 \times 4$ homogeneous matrix form:
$$\mathbf{S}(s_x, s_y, s_z) = \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
Scaling with respect to an arbitrary fixed point $(x_f, y_f, z_f)$:
$$\mathbf{M}_{\text{fixed\_scale}} = \mathbf{T}(x_f, y_f, z_f) \cdot \mathbf{S}(s_x, s_y, s_z) \cdot \mathbf{T}(-x_f, -y_f, -z_f)$$

---

### 3D Coordinate-Axis Rotations
In 3D space, rotation requires specifying not only an angle $\theta$, but also an **axis of rotation**.
By convention in a right-handed coordinate system, positive rotation angles produce counterclockwise rotation when looking along the positive axis toward the origin (Right-Hand Rule):

#### 1. Rotation About the $Z$-Axis ($\mathbf{R}_z(\theta)$)
The $z$-coordinate remains unchanged; rotation occurs in the $xy$-plane:
$$x' = x\cos\theta - y\sin\theta$$
$$y' = x\sin\theta + y\cos\theta$$
$$z' = z$$

$$\mathbf{R}_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

#### 2. Rotation About the $X$-Axis ($\mathbf{R}_x(\theta)$)
The $x$-coordinate remains unchanged; rotation occurs in the $yz$-plane:
$$x' = x$$
$$y' = y\cos\theta - z\sin\theta$$
$$z' = y\sin\theta + z\cos\theta$$

$$\mathbf{R}_x(\theta) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta & 0 \\ 0 & \sin\theta & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

#### 3. Rotation About the $Y$-Axis ($\mathbf{R}_y(\theta)$)
The $y$-coordinate remains unchanged; rotation occurs in the $zx$-plane.
Notice the cyclic permutation of axes ($X \to Y \to Z \to X$), which introduces the sign convention:
$$x' = x\cos\theta + z\sin\theta$$
$$y' = y$$
$$z' = -x\sin\theta + z\cos\theta$$

$$\mathbf{R}_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta & 0 \\ 0 & 1 & 0 & 0 \\ -\sin\theta & 0 & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

---

### General 3D Rotation About an Arbitrary Axis in Space
When an object is to be rotated by angle $\theta$ about an arbitrary line in 3D space specified by point $P_0(x_0, y_0, z_0)$ and unit direction vector $\vec{u} = \begin{bmatrix} \alpha_x & \alpha_y & \alpha_z \end{bmatrix}^T$ ($\alpha_x^2 + \alpha_y^2 + \alpha_z^2 = 1$), a five-stage transformation sequence is executed:

#### The 5-Step Derivation:
1. **Translate the rotation axis to pass through the coordinate origin**:
   $$\mathbf{T}(-x_0, -y_0, -z_0)$$
2. **Rotate about the $X$-axis by angle $\alpha$ to swing the axis into the $xz$-plane**:
   - The projection of $\vec{u}$ onto the $yz$-plane has length $d = \sqrt{\alpha_y^2 + \alpha_z^2}$.
   - Direction cosines: $\cos\alpha = \frac{\alpha_z}{d}, \ \sin\alpha = \frac{\alpha_y}{d}$.
   $$\mathbf{R}_x(\alpha) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \frac{\alpha_z}{d} & -\frac{\alpha_y}{d} & 0 \\ 0 & \frac{\alpha_y}{d} & \frac{\alpha_z}{d} & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
3. **Rotate about the $Y$-axis by angle $\beta$ to align the axis with the positive $Z$-axis**:
   - Direction cosines: $\cos\beta = d, \ \sin\beta = \alpha_x$.
   $$\mathbf{R}_y(\beta) = \begin{bmatrix} d & 0 & -\alpha_x & 0 \\ 0 & 1 & 0 & 0 \\ \alpha_x & 0 & d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
4. **Perform the desired rotation by angle $\theta$ about the $Z$-axis**:
   $$\mathbf{R}_z(\theta)$$
5. **Apply the inverse transformations in exact reverse order**:
   - Undo rotation about $Y$: $\mathbf{R}_y^{-1}(\beta) = \mathbf{R}_y(-\beta)$.
   - Undo rotation about $X$: $\mathbf{R}_x^{-1}(\alpha) = \mathbf{R}_x(-\alpha)$.
   - Undo translation: $\mathbf{T}^{-1} = \mathbf{T}(x_0, y_0, z_0)$.

#### Master Composite Rotation Matrix:
$$\mathbf{M}_{\text{arb\_rot}} = \mathbf{T}(x_0, y_0, z_0) \cdot \mathbf{R}_x(-\alpha) \cdot \mathbf{R}_y(-\beta) \cdot \mathbf{R}_z(\theta) \cdot \mathbf{R}_y(\beta) \cdot \mathbf{R}_x(\alpha) \cdot \mathbf{T}(-x_0, -y_0, -z_0)$$

---

## 2. Example: Arbitrary Axis Rotation Alignment Geometry
```
Step 1: Translate P_0 to Origin     Step 2: Rotate around X into XZ-plane   Step 3: Rotate around Y onto Z-axis
       Z                                   Z                                       Z Axis (Aligned!)
       ▲                                   ▲                                       ▲   
       │       / Axis u                    │    / Axis u'                          │   │ Axis u''
       │      /                            │   / (In XZ plane)                     │   │
       │     * P_0                         │  /                                    │   │
       └──────────────► X                  └──────────────► X                      └──────────────► X
      /                                   /                                       /
     ▼ Y                                 ▼ Y                                     ▼ Y
```

---

## 3. Applications & Use Cases
1. **Robotic Kinematics & Manipulator Control (Denavit-Hartenberg Parameters)**: Industrial robot arms calculate end-effector tool positions by cascading 3D translation and rotation matrices along multi-link joint axes.
2. **Gimbal Lock Prevention and Quaternion Rotation**: Understanding arbitrary axis rotations provides the foundational basis for Quaternion rotations ($\mathbf{q} = [\cos(\theta/2), \vec{u}\sin(\theta/2)]$) used in aerospace avionics and 3D flight simulators.
3. **VR/AR Head Tracking (6-DOF Tracking)**: Virtual Reality headsets update camera matrices in real time by mapping 3-axis accelerometer and gyroscope readings into 3D composite rotation matrices.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: 3D Coordinate Axis Rotation Trace [KTU Dec 2021 / June 2024 - 4 Marks]
**Problem**:
A 3D point $P(2, 4, 6)$ is rotated by $90^\circ$ counterclockwise about the $Z$-axis, followed by a rotation of $90^\circ$ counterclockwise about the $X$-axis. Determine the final coordinates of the point.

**Step-by-step Solution**:
1. **Rotation about $Z$-axis ($\theta_z = 90^\circ$)**:
   $$\cos 90^\circ = 0, \quad \sin 90^\circ = 1$$
   $$\mathbf{R}_z(90^\circ) = \begin{bmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   $$P_1 = \mathbf{R}_z(90^\circ) \cdot \begin{bmatrix} 2 \\ 4 \\ 6 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(2) - 1(4) \\ 1(2) + 0(4) \\ 6 \\ 1 \end{bmatrix} = \begin{bmatrix} -4 \\ 2 \\ 6 \\ 1 \end{bmatrix} \implies \mathbf{P_1(-4, 2, 6)}$$
2. **Rotation about $X$-axis ($\theta_x = 90^\circ$)**:
   $$\mathbf{R}_x(90^\circ) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   $$P_2 = \mathbf{R}_x(90^\circ) \cdot \begin{bmatrix} -4 \\ 2 \\ 6 \\ 1 \end{bmatrix} = \begin{bmatrix} -4 \\ 0(2) - 1(6) \\ 1(2) + 0(6) \\ 1 \end{bmatrix} = \begin{bmatrix} -4 \\ -6 \\ 2 \\ 1 \end{bmatrix} \implies \mathbf{P_2(-4, -6, 2)}$$
3. **Result**: The point transforms to $\mathbf{(-4, -6, 2)}$.

---

### Example 2: 3D Scaling About an Arbitrary Fixed Point [KTU May 2019 Pattern]
**Problem**:
A 3D pyramid with base centered at $(1, 2, 3)$ is to be scaled by factors $s_x = 2, s_y = 2, s_z = 3$ about the fixed point $(1, 2, 3)$.
Formulate the composite $4 \times 4$ transformation matrix.

**Step-by-step Solution**:
1. Fixed point $(x_f, y_f, z_f) = (1, 2, 3)$.
2. Composite formula:
   $$\mathbf{M} = \mathbf{T}(x_f, y_f, z_f) \cdot \mathbf{S}(s_x, s_y, s_z) \cdot \mathbf{T}(-x_f, -y_f, -z_f)$$
   $$\mathbf{M} = \begin{bmatrix} s_x & 0 & 0 & x_f(1 - s_x) \\ 0 & s_y & 0 & y_f(1 - s_y) \\ 0 & 0 & s_z & z_f(1 - s_z) \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
3. Substitute values:
   $$t_x' = 1(1 - 2) = -1$$
   $$t_y' = 2(1 - 2) = -2$$
   $$t_z' = 3(1 - 3) = -6$$
4. Composite Matrix:
   $$\mathbf{M} = \begin{bmatrix} 2 & 0 & 0 & -1 \\ 0 & 2 & 0 & -2 \\ 0 & 0 & 3 & -6 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

---

### Example 3: Non-Commutativity of 3D Rotations [KTU Analytical Pattern]
**Problem**:
Prove that 3D rotations about distinct coordinate axes do not commute by evaluating $\mathbf{R}_x(90^\circ) \cdot \mathbf{R}_y(90^\circ)$ versus $\mathbf{R}_y(90^\circ) \cdot \mathbf{R}_x(90^\circ)$.

**Step-by-step Solution**:
1. Matrices for $90^\circ$ rotation:
   $$\mathbf{R}_x(90^\circ) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{bmatrix}, \quad \mathbf{R}_y(90^\circ) = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{bmatrix}$$
2. **Product $\mathbf{R}_x \cdot \mathbf{R}_y$**:
   $$\mathbf{R}_x \cdot \mathbf{R}_y = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$
3. **Product $\mathbf{R}_y \cdot \mathbf{R}_x$**:
   $$\mathbf{R}_y \cdot \mathbf{R}_x = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & -1 \\ -1 & 0 & 0 \end{bmatrix}$$
4. **Conclusion**:
   $$\mathbf{R}_x(90^\circ) \cdot \mathbf{R}_y(90^\circ) \ne \mathbf{R}_y(90^\circ) \cdot \mathbf{R}_x(90^\circ)$$
   3D rotations about distinct axes are **strictly non-commutative**. Changing the execution order produces completely different spatial orientations.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019 / January 2023 - 9 Marks]
**Question**:
Derive the general composite transformation matrix for rotating an object about an arbitrary axis in space that does not pass through the origin.

**Solution**:
1. **Geometric Problem Specification**:
   Let the arbitrary axis of rotation be defined by a line passing through point $P_0(x_0, y_0, z_0)$ with direction unit vector $\vec{u} = (\alpha_x, \alpha_y, \alpha_z)$ where $\alpha_x^2 + \alpha_y^2 + \alpha_z^2 = 1$. The object is to be rotated about this line by an angle $\theta$.
2. **Five-Step Transformation Decomposition**:
   - **Step 1: Translation to Origin**:
     Translate point $P_0$ to the origin:
     $$\mathbf{T}(-x_0, -y_0, -z_0) = \begin{bmatrix} 1 & 0 & 0 & -x_0 \\ 0 & 1 & 0 & -y_0 \\ 0 & 0 & 1 & -z_0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   - **Step 2: Rotate about X-axis to align into XZ-plane**:
     Project $\vec{u}$ onto the $yz$-plane. Its length is $d = \sqrt{\alpha_y^2 + \alpha_z^2}$.
     Rotate about $X$ by angle $\alpha$ where $\cos\alpha = \frac{\alpha_z}{d}$ and $\sin\alpha = \frac{\alpha_y}{d}$:
     $$\mathbf{R}_x(\alpha) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \alpha_z/d & -\alpha_y/d & 0 \\ 0 & \alpha_y/d & \alpha_z/d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   - **Step 3: Rotate about Y-axis to align with Z-axis**:
     Rotate about $Y$ by angle $\beta$ where $\cos\beta = d$ and $\sin\beta = \alpha_x$:
     $$\mathbf{R}_y(\beta) = \begin{bmatrix} d & 0 & -\alpha_x & 0 \\ 0 & 1 & 0 & 0 \\ \alpha_x & 0 & d & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   - **Step 4: Rotate by $\theta$ about the Z-axis**:
     $$\mathbf{R}_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
   - **Step 5: Apply Inverse Transformations**:
     Undo the rotations and translation in exact inverse sequence:
     $$\mathbf{R}_y^{-1}(\beta) = \mathbf{R}_y(-\beta), \quad \mathbf{R}_x^{-1}(\alpha) = \mathbf{R}_x(-\alpha), \quad \mathbf{T}^{-1} = \mathbf{T}(x_0, y_0, z_0)$$
3. **Master Concatenated Transformation Matrix**:
   $$\mathbf{M}_{\text{composite}} = \mathbf{T}(x_0, y_0, z_0) \cdot \mathbf{R}_x(-\alpha) \cdot \mathbf{R}_y(-\beta) \cdot \mathbf{R}_z(\theta) \cdot \mathbf{R}_y(\beta) \cdot \mathbf{R}_x(\alpha) \cdot \mathbf{T}(-x_0, -y_0, -z_0)$$
   Evaluating this matrix product provides the final $4 \times 4$ transformation matrix for rotating any 3D coordinate about the specified arbitrary spatial axis.

---

### Question 2 [KTU December 2020 / December 2023 - 4 Marks]
**Question**:
Write down the $4 \times 4$ transformation matrix for 3D scaling with respect to an arbitrary fixed point.

**Solution**:
1. **Transformation Steps**:
   Scaling an object with scaling factors $(s_x, s_y, s_z)$ about an arbitrary fixed point $P_f(x_f, y_f, z_f)$ requires:
   1. Translate the fixed point $P_f$ to the coordinate origin: $\mathbf{T}(-x_f, -y_f, -z_f)$.
   2. Apply scaling with respect to the origin: $\mathbf{S}(s_x, s_y, s_z)$.
   3. Translate the origin back to the fixed point $P_f$: $\mathbf{T}(x_f, y_f, z_f)$.
2. **Matrix Derivation**:
   $$\mathbf{M} = \mathbf{T}(x_f, y_f, z_f) \cdot \mathbf{S}(s_x, s_y, s_z) \cdot \mathbf{T}(-x_f, -y_f, -z_f)$$
   $$\mathbf{M} = \begin{bmatrix} 1 & 0 & 0 & x_f \\ 0 & 1 & 0 & y_f \\ 0 & 0 & 1 & z_f \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 & -x_f \\ 0 & 1 & 0 & -y_f \\ 0 & 0 & 1 & -z_f \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
3. **Resulting $4 \times 4$ Matrix**:
   $$\mathbf{M} = \begin{bmatrix} s_x & 0 & 0 & x_f(1 - s_x) \\ 0 & s_y & 0 & y_f(1 - s_y) \\ 0 & 0 & s_z & z_f(1 - s_z) \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

