# Module 2 — Topic 3: Disjoint Sets & Union-Find Operations

> **Module 2**: Master's Theorem, Asymptotics & Balanced Structures  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
In many applications, we need to group distinct elements into non-overlapping collections. Two sets are **disjoint** if they share absolutely no elements in common. The **Disjoint-Set (or Union-Find)** data structure is specifically designed to keep track of these non-overlapping groups efficiently.
Instead of storing sets as arrays or linked lists (which make merging slow), Union-Find stores sets as a **forest of trees**. Every set has one unique "root" node acting as the representative of the entire set.
- `MAKE-SET(x)`: Creates a new set containing only $x$.
- `FIND-SET(x)`: Climbs the tree from $x$ to find and return the root.
- `UNION(x, y)`: Finds the roots of $x$ and $y$ and makes one root point to the other, merging the trees.

To keep trees flat and fast, we use two heuristics:
1. **Union by Rank**: Always attach the shorter tree to the root of the taller tree.
2. **Path Compression**: During a `FIND`, make every node visited point directly to the root, flattening the tree for future queries.

### Example
Imagine a massive high school where no one knows each other on the first day (`MAKE-SET`). 
As people meet, they form friend groups (`UNION`). If you want to know if Alice and Bob are in the same friend group, you don't ask everyone. Instead, each group designates a "Leader". You ask Alice who her leader is (`FIND-SET`), and ask Bob who his leader is. If they name the same person, they are in the same group! 
If two friend groups merge, one leader steps down and points to the other leader (Union by Rank).

### Applications & Use Cases
- **Kruskal’s Minimum Spanning Tree Algorithm**: Used heavily in networking (laying fiber-optic cables) to connect all nodes with minimal cost. Union-Find detects if adding a cable would create a redundant cycle.
- **Image Segmentation (Connected Components)**: In Computer Vision, Union-Find groups adjacent pixels of similar colors to identify discrete objects in an image.
- **Social Network Connectivity**: To rapidly determine if there is a path of connections between two users (e.g., LinkedIn degrees of connection).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Basic Union and Find Operations (Without Heuristics)
**Problem:** Start with 5 elements $\{1, 2, 3, 4, 5\}$. Perform the following operations: `UNION(1, 2)`, `UNION(2, 3)`, `UNION(4, 5)`, `UNION(3, 5)`. Trace the tree structure assuming the first argument becomes the parent of the second. Find `FIND(5)`.
**Step-by-step Solution:**
1. **Initial State:** 5 independent trees (roots): 1, 2, 3, 4, 5.
2. **`UNION(1, 2)`:** Node 1 becomes the parent of Node 2. (Tree: `1 -> 2`).
3. **`UNION(2, 3)`:** Node 2 becomes the parent of Node 3. (Tree: `1 -> 2 -> 3`).
4. **`UNION(4, 5)`:** Node 4 becomes the parent of Node 5. (Tree: `4 -> 5`).
5. **`UNION(3, 5)`:** We find the root of 3 (which is 1) and the root of 5 (which is 4). By the rule, root(3) becomes parent of root(5). So, Node 1 becomes the parent of Node 4. (Tree: `1 -> {2->3, 4->5}`).
6. **`FIND(5)`:** We trace from 5. Parent of 5 is 4. Parent of 4 is 1. Parent of 1 is 1 (Root). The answer is **1**.

### Example 2: Union by Rank
**Problem:** We have two sets. Set A is a tree with rank (height) 2, rooted at $X$. Set B is a tree with rank (height) 4, rooted at $Y$. We perform `UNION(X, Y)`. Which node becomes the root, and what is the new rank of the resulting tree?
**Step-by-step Solution:**
1. **Identify Roots and Ranks:** Root 1 is $X$ with $rank(X) = 2$. Root 2 is $Y$ with $rank(Y) = 4$.
2. **Apply Union by Rank:** The rule states that the root with the smaller rank must point to the root with the larger rank.
3. Since $rank(X) < rank(Y)$ ($2 < 4$), $X$ points to $Y$.
4. **Calculate New Rank:** Because a tree of height 2 was attached below the root of a tree of height 4, the overall maximum height of the tree does not increase. The new tree is rooted at $Y$ with $rank(Y) = 4$.
5. *(Note: The rank only increases by 1 if two trees of the exact same rank are merged).*

### Example 3: Path Compression
**Problem:** Given a stringy tree representing a set where `5 -> 4 -> 3 -> 2 -> 1` (where 1 is the root). Trace the exact pointer changes that occur when executing `FIND-SET(5)` with Path Compression enabled.
**Step-by-step Solution:**
1. **Initial Call:** `FIND(5)` is called. The algorithm looks at the parent of 5, which is 4. It recursively calls `FIND(4)`.
2. **Recursive Traversal:** 
   - `FIND(4)` calls `FIND(3)`.
   - `FIND(3)` calls `FIND(2)`.
   - `FIND(2)` calls `FIND(1)`.
3. **Base Case Reached:** `FIND(1)` sees that 1 is the root (parent of 1 is 1). It returns `1`.
4. **Unwinding and Compressing:**
   - As `FIND(2)` resolves, it updates Node 2 to point to the returned root `1`. (No change, it already did).
   - As `FIND(3)` resolves, it updates Node 3 to point directly to the returned root `1`. (Pointer changes from 2 to 1).
   - As `FIND(4)` resolves, it updates Node 4 to point directly to the returned root `1`. (Pointer changes from 3 to 1).
   - As `FIND(5)` resolves, it updates Node 5 to point directly to the returned root `1`. (Pointer changes from 4 to 1).
5. **Final Tree Structure:** The tree is completely flattened. Nodes 2, 3, 4, and 5 all point directly to the root node 1 as immediate children. Future `FIND` calls on any of these nodes will take $O(1)$ time.
