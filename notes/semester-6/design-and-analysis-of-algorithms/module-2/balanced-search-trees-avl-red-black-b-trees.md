# Module 2 — Topic 2: Balanced Search Trees (AVL, Red-Black, & B-Trees)

> **Module 2**: Master's Theorem, Asymptotics & Balanced Structures  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. AVL Trees (Height-Balanced Trees)

An **AVL Tree** is a self-balancing binary search tree where the balance factor of every node is in $\{-1, 0, +1\}$.
$$\text{Balance Factor } BF(node) = \text{Height}(\text{Left Subtree}) - \text{Height}(\text{Right Subtree})$$

### Rotations:
1. **Left-Left (LL) Imbalance** $\rightarrow$ Right Rotation at node.
2. **Right-Right (RR) Imbalance** $\rightarrow$ Left Rotation at node.
3. **Left-Right (LR) Imbalance** $\rightarrow$ Left Rotation on child, then Right Rotation on node.
4. **Right-Left (RL) Imbalance** $\rightarrow$ Right Rotation on child, then Left Rotation on node.

---

## 2. Red-Black Trees

A **Red-Black Tree** is a self-balancing BST with node color properties:
1. Every node is either **Red** or **Black**.
2. The root is always **Black**.
3. Every leaf (`NIL` node) is **Black**.
4. If a node is **Red**, both its children must be **Black** (No two adjacent Red nodes).
5. For each node, all simple paths from the node to descendant leaves contain the same number of Black nodes (**Black-Height**).

---

## 3. B-Trees (Multi-Way Search Trees)

A **B-Tree** of order $m$ is a self-balancing search tree designed for disk storage:
1. Every node has at most $m$ children.
2. Every internal node (except root) has at least $\lceil m/2 \rceil$ children.
3. The root has at least 2 children if it is not a leaf.
4. All leaves appear on the same level.
