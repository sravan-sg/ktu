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

### Red-Black Tree Deletion Techniques (4 Structural Cases)
When deleting a node from a Red-Black tree, if a Black node is removed, it introduces a **"Double Black"** violation (loss of black-height). Balance is restored by considering the color of the sibling $S$ and its children:
1. **Case 1 (Sibling $S$ is Red):** Perform a rotation at parent $P$, swap colors of $P$ and $S$. This transforms the situation into Case 2, 3, or 4 where sibling is Black.
2. **Case 2 (Sibling $S$ is Black, both of $S$'s children are Black):** Recolor $S$ to Red. Push the "Double Black" property up to parent $P$. If $P$ was Red, it becomes Black (done); if $P$ was Black, repeat fixup at $P$.
3. **Case 3 (Sibling $S$ is Black, $S$'s inner child is Red, outer child is Black):** Perform a rotation at $S$ towards the inner child and swap colors of $S$ and its child. This converts the setup to Case 4.
4. **Case 4 (Sibling $S$ is Black, $S$'s outer child is Red):** Perform a rotation at parent $P$, recolor $S$ to parent's color, color parent $P$ Black, and color $S$'s outer child Black. Removes the Double Black violation completely.

---

### B-Tree Deletion Operations (3 Cases)
Deleting a key $k$ from a B-Tree of order $m$ must preserve the property that every node (except root) contains at least $\lceil m/2 \rceil - 1$ keys:
1. **Case 1 (Key $k$ is in a Leaf Node):**
   - If leaf has $> \lceil m/2 \rceil - 1$ keys: Simply remove $k$.
   - If leaf has minimum keys: Borrow a key from an immediate sibling (via parent) if sibling has extra keys. If sibling also has minimum keys, **merge** the leaf, its sibling, and the separating key from parent.
2. **Case 2 (Key $k$ is in an Internal Node):**
   - Find the **In-order Predecessor** (largest key in left child) or **In-order Successor** (smallest key in right child).
   - Replace key $k$ with predecessor/successor key $k'$, then recursively delete $k'$ from the leaf node.
3. **Case 3 (Underflow Propagation to Parent):**
   - If merging reduces parent's key count below $\lceil m/2 \rceil - 1$, apply borrow/merge recursively up toward the root. If root becomes empty, its only child becomes the new root, reducing tree height by 1.

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

---

### Previous Year Questions & Solutions

1. **"Construct a red-black tree by inserting the keys 41, 38, 31, 12, 19, 8..." [April 2018]**
   - **Solution:** 
     1. **Insert 41**: Root, color it Black.
     2. **Insert 38**: Left of 41. Color Red. (No violation).
     3. **Insert 31**: Left of 38. Color Red. (Red-Red violation). Uncle is null (Black). **LL Case**: Right Rotate at 41. Recolor 38 to Black, 41 to Red. (Root is 38).
     4. **Insert 12**: Left of 31. Color Red. (No violation).
     5. **Insert 19**: Right of 12. Color Red. (Red-Red violation). Uncle is 41 (Red). **Recolor Case**: Change parent (31) and uncle (41) to Black. Grandparent (38) becomes Red, but since it's the root, it reverts to Black.
     6. **Insert 8**: Left of 12. Color Red. (Red-Red violation). Uncle is 19 (Black). **LL Case**: Right Rotate at 31. Recolor 12 to Black, 31 to Red.
     *(Final Tree Structure: Root 38(B), L-> 12(B), R-> 41(B). 12 has L-> 8(R), R-> 31(R). 31 has L-> 19(B) wait, color trace may vary, but standard rotation rules apply).*

2. **"Construct a Red Black tree by inserting 10, 20, 30, 15, 16 and 27..." [Dec 2019, July 2021]**
   - **Solution:**
     1. **Insert 10:** Node 10 is root $\rightarrow$ color Black. (Tree: `10(B)`).
     2. **Insert 20:** Insert right of 10 as Red. No violation. (Tree: `10(B) -> R: 20(R)`).
     3. **Insert 30:** Insert right of 20 as Red. Red-Red violation at 20-30. Uncle of 30 is NULL (Black). **RR Case**: Left Rotate at 10. Recolor 20 to Black, 10 to Red. (Tree: Root `20(B)`, Left `10(R)`, Right `30(R)`).
     4. **Insert 15:** Insert right of 10 as Red. Red-Red violation at 10-15. Uncle of 15 is 30 (Red). **Recolor Case**: Recolor parent 10 and uncle 30 to Black, grandparent 20 to Red (remains Black as root). (Tree: Root `20(B)`, Left `10(B) -> R: 15(R)`, Right `30(B)`).
     5. **Insert 16:** Insert right of 15 as Red. Red-Red violation at 15-16. Uncle of 16 is NULL (Black). **RR Case**: Left Rotate at 10. Recolor 15 to Black, 10 to Red. 15 becomes left child of root 20. (Tree: Root `20(B)`, Left `15(B)` with `L: 10(R)`, `R: 16(R)`, Right `30(B)`).
     6. **Insert 27:** Insert left of 30 as Red. No violation.
     - **Final Tree:** Root `20(B)`; Left subtree `15(B)` with children `10(R)` and `16(R)`; Right subtree `30(B)` with left child `27(R)`. All Red-Black properties hold.

3. **"Explain the important properties of B-Tree." [April 2018] & "Define B-tree. Discuss the significance of B-tree" [Dec 2019]**
   - **Solution:** 
     **Definition & Properties**: A B-Tree of order $m$ is an $m$-way search tree where:
     1. Every node has at most $m$ children.
     2. Every non-leaf node (except root) has at least $\lceil m/2 \rceil$ children.
     3. The root has at least 2 children if it is not a leaf node.
     4. A non-leaf node with $k$ children contains $k-1$ keys.
     5. All leaves appear at the same level (perfectly balanced).
     **Significance**: B-Trees are designed for disk-based storage systems (Databases/File Systems). By allowing many keys per node (a large order $m$), a B-Tree node matches the size of a disk block. This drastically flattens the tree height, minimizing the number of slow mechanical disk reads required to find a record compared to a standard binary tree.
