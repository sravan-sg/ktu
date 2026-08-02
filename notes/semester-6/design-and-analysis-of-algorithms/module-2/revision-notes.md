# Module 2: Last-Minute Revision & Submodule Guide

> **Semester**: S6 | **Subject**: Design and Analysis of Algorithms (CS302)  
> **Purpose**: Rapid revision guide for Module 2 covering Master's Theorem, Asymptotic Notations, AVL/Red-Black/B-Trees, and Disjoint Sets.

---

## Submodule 2.1: Master's Theorem & Asymptotics

### 1. Explanation
Master's Theorem provides an immediate formula to solve $T(n) = a T(n/b) + f(n)$. Compare $f(n)$ to $n^{\log_b a}$:
- Case 1: $f(n)$ smaller $\rightarrow \Theta(n^{\log_b a})$.
- Case 2: $f(n)$ equal $\rightarrow \Theta(n^{\log_b a} \log n)$.
- Case 3: $f(n)$ larger $\rightarrow \Theta(f(n))$.

### 2. Real-World Example
Determining MapReduce processing time: If splitting/combining data takes linear time ($f(n) = n$) and splits into 2 subproblems of half size ($2T(n/2)$), Case 2 immediately tells us total runtime is $O(n \log n)$.

### 3. Applications & Use Cases
- **Algorithm Analysis**: Instantaneous evaluation of recursive algorithms like Merge Sort, Binary Search, and Strassen's Matrix Multiplication.

### 4. 3 Solved Micro-Examples
- **Example 1**: $T(n) = 4T(n/2) + n \implies a=4, b=2 \implies n^{\log_2 4} = n^2$. $f(n) = n = O(n^{2-1})$. Case 1 $\implies \Theta(n^2)$.
- **Example 2**: $T(n) = 2T(n/2) + n \implies n^{\log_2 2} = n^1$. $f(n) = n = \Theta(n)$. Case 2 $\implies \Theta(n \log n)$.
- **Example 3**: $T(n) = T(n/2) + 1 \implies n^{\log_2 1} = n^0 = 1$. $f(n) = 1$. Case 2 $\implies \Theta(\log n)$.

---

## Submodule 2.2: Balanced Search Trees (AVL, Red-Black, B-Trees)

### 1. Explanation
- **AVL Tree**: Height-balanced tree keeping balance factor $|h_L - h_R| \le 1$ using rotations.
- **Red-Black Tree**: Self-balancing tree using node colors (Red/Black) ensuring no two adjacent red nodes and uniform black-height.
- **B-Tree**: Self-balancing multi-way tree optimized for reading and writing large blocks of memory on physical disk drives.

### 2. Real-World Example
- **B-Trees**: Used in database storage engines (MySQL InnoDB, PostgreSQL) and filesystem metadata (NTFS, ext4) to minimize disk head seeks.

### 3. Applications & Use Cases
- **Standard Libraries**: C++ `std::map` and Java `TreeMap` use Red-Black trees for $O(\log n)$ insertion, deletion, and search bounds.

### 4. 3 Solved Micro-Examples
- **Example 1**: Single Right Rotation (LL Imbalance) fixes an unbalance caused by insertion into left child's left subtree.
- **Example 2**: Maximum height of an AVL tree with $n$ nodes is $\approx 1.44 \log_2 n$.
- **Example 3**: A B-Tree of order 5 can hold up to 4 keys per node and up to 5 children per node.

---

## Submodule 2.3: Disjoint Sets & Union-Find

### 1. Explanation
Disjoint-set data structures track partitionings of elements into disjoint non-overlapping sets using `MAKE-SET`, `FIND-SET`, and `UNION`.

### 2. Real-World Example
Social network friend groups: Finding whether User A and User B are connected in the same network component using `FIND-SET`.

### 3. Applications & Use Cases
- **Kruskal's MST Algorithm**: Uses Union-Find to detect cycles when adding edges to minimum cost spanning trees.

### 4. 3 Solved Micro-Examples
- **Example 1**: `FIND-SET` with Path Compression points all evaluated nodes directly to root.
- **Example 2**: Union by Rank connects root of shorter tree to root of taller tree.
- **Example 3**: Amortized time per operation with both heuristics is $O(\alpha(n)) \approx O(1)$.
