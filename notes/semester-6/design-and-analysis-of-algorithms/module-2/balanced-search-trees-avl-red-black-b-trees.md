# Module 2 — Topic 2: Balanced Search Trees (AVL, Red-Black, & B-Trees)

> **Module 2**: Master's Theorem, Asymptotics & Balanced Structures  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
A standard **Binary Search Tree (BST)** stores data such that everything to the left of a node is smaller, and everything to the right is larger. However, if you insert sorted data (e.g., 1, 2, 3, 4, 5), the tree degrades into a straight line, degrading search times from $O(\log n)$ to $O(n)$.
A **Balanced Search Tree** solves this by strictly monitoring its own shape. When an insertion or deletion causes the tree to become too "lopsided," it performs a **rotation**—a constant-time structural rearrangement that restores balance without breaking the BST ordering property. 
- **AVL Trees**: Strictly balanced. The height difference between left and right subtrees (Balance Factor) can never exceed 1.
- **Red-Black Trees**: Loosely balanced using color rules (Red/Black). Guarantees the longest path is no more than twice the shortest path.
- **B-Trees**: Fat, multi-way trees where nodes can have many children. Designed specifically to minimize disk reads.

### Example
Imagine organizing a physical filing cabinet. 
If you just shove folders in sequentially, you end up with one massive, deep drawer and many empty ones (an unbalanced tree). Finding a folder requires pulling out the entire massive drawer.
A **Balanced Tree** is like an office manager who strictly enforces that no drawer can contain more than 10 folders more than any other drawer. If a drawer gets too full, they immediately split and shift folders around (a rotation) so that finding any folder is always equally fast.

### Applications & Use Cases
- **Database Indexing (B-Trees)**: PostgreSQL, MySQL, and SQLite use B-Trees for their primary indices. Because disks are incredibly slow compared to RAM, B-Trees pack multiple keys into a single disk block (node) to minimize the number of mechanical disk reads.
- **Language Libraries (Red-Black Trees)**: The C++ `std::map` and `std::set`, as well as Java's `TreeMap`, are implemented using Red-Black trees because their loose balancing makes insertions/deletions faster than AVL trees.
- **In-Memory Lookups (AVL Trees)**: Used in systems where the data is entirely in RAM and read operations vastly outnumber write operations, benefiting from the strict $O(\log n)$ height guarantee.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: AVL Tree Imbalance and Rotation
**Problem:** Given an initially empty AVL Tree, insert the keys `10, 20, 30` in order. Calculate the balance factors at each step and perform the necessary rotation to maintain balance.
**Step-by-step Solution:**
1. **Insert 10:** Tree has only root `10`. Balance Factor (BF) of 10 = Height(Left) - Height(Right) = 0 - 0 = 0. (Balanced).
2. **Insert 20:** `20` > `10`, so it becomes the right child of `10`.
   - BF(20) = 0.
   - BF(10) = 0 - 1 = -1. (Balanced).
3. **Insert 30:** `30` > `10` and `30` > `20`, so it becomes the right child of `20`.
   - BF(30) = 0.
   - BF(20) = 0 - 1 = -1.
   - BF(10) = 0 - 2 = -2. (Imbalanced! The tree is right-heavy).
4. **Identify Imbalance:** The imbalance is on the Right child of the Right child (RR case).
5. **Apply Rotation:** We must perform a **Left Rotation** on the unbalanced node `10`.
   - `20` becomes the new root.
   - `10` becomes the left child of `20`.
   - `30` remains the right child of `20`.
6. **Verify Balance:**
   - BF(10) = 0.
   - BF(30) = 0.
   - BF(20) = Height(Left:10) - Height(Right:30) = 1 - 1 = 0. (Perfectly balanced).

### Example 2: Red-Black Tree Coloring Rules
**Problem:** In a valid Red-Black tree, a red node `R` has two children. What MUST be the colors of these two children and why? Prove that a Red-Black tree cannot consist of alternating Red and Black nodes from root to a leaf if there is another path that is purely Black.
**Step-by-step Solution:**
1. **Child Colors:** According to Red-Black Tree Property #4 ("No two adjacent Red nodes"), if a node is Red, both of its children *must* be **Black**. 
2. **Path Proof:** Consider a tree with Root `B` (Black). 
   - Path 1 goes down the left subtree: `B -> R -> B -> R -> B (leaf)`.
   - Path 2 goes down the right subtree: `B -> B (leaf)`.
3. Let's check Property #5 ("Black-Height"): Every path from a node to its descendant leaves must contain the exact same number of Black nodes.
4. **Black-Height of Path 1:** Contains 3 Black nodes.
5. **Black-Height of Path 2:** Contains 2 Black nodes.
6. Since $3 \neq 2$, this tree violates Property #5. Therefore, a Red-Black tree strictly enforces that the longest path (alternating Red/Black) is at most twice the length of the shortest path (all Black), guaranteeing an $O(\log n)$ search time.

### Example 3: B-Tree Order and Key Capacity
**Problem:** Given a B-Tree of Order $m = 5$, what is the minimum and maximum number of children an internal node can have? What is the minimum and maximum number of keys it can store? If the root is not a leaf, what are its constraints?
**Step-by-step Solution:**
1. **Understand B-Tree Order ($m$):** The order $m$ defines the maximum number of *children* a node can have. Here, $m = 5$.
2. **Maximum Constraints:**
   - Max children per node = $m = 5$.
   - Max keys per node = $m - 1 = 4$.
3. **Minimum Constraints (Internal Nodes):**
   - A B-Tree requires internal nodes to be at least half full to prevent the tree from becoming too stringy.
   - Min children per internal node = $\lceil m / 2 \rceil = \lceil 5 / 2 \rceil = 3$.
   - Min keys per internal node = $\lceil m / 2 \rceil - 1 = 2$.
4. **Root Constraints:**
   - The root is exempt from the strict "half-full" rule because a tree might only have 1 or 2 items total.
   - If the root is not a leaf (it has split at least once), it must have at least **2 children** (and thus at least 1 key).
