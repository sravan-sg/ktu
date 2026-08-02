# Module 2 — Topic 3: Disjoint Sets & Union-Find Operations

> **Module 2**: Master's Theorem, Asymptotics & Balanced Structures  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Disjoint-Set Data Structure (Union-Find)

A **Disjoint-Set Data Structure** maintains a collection of non-overlapping sets.

### Core Operations:
1. **`MAKE-SET(x)`**: Creates a new set containing single element $x$.
2. **`FIND-SET(x)`**: Returns a representative pointer to the set containing element $x$.
3. **`UNION(x, y)`**: Merges the sets containing $x$ and $y$ into a single set.

---

## 2. Optimization Heuristics

1. **Union by Rank**: Always attach the root of the smaller tree to the root of the larger tree.
2. **Path Compression**: During `FIND-SET(x)`, flatten the tree by making every visited node point directly to the root.

---

## 3. Time Complexity
Using both Union by Rank and Path Compression, $m$ operations on $n$ elements run in $O(m \cdot \alpha(n))$ time, where $\alpha(n)$ is the extremely slow-growing **Inverse Ackermann Function** ($\alpha(n) \le 4$ for all practical universe sizes).
