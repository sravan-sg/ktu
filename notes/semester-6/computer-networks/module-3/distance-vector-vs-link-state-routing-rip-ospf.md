# Module 3 — Topic 2: Distance Vector vs Link State Routing (RIP & OSPF)

> **Module 3**: Network Layer & Routing Algorithms  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
Dynamic routing algorithms enable routers to continuously learn network topology changes and update forwarding tables automatically:

1. **Distance Vector Routing (DVR)**:
   - Based on the **Bellman-Ford Algorithm**.
   - Each router maintains a table (Vector) giving the minimum known distance to every destination and the next-hop router.
   - Routers periodically exchange their entire routing table only with **immediate neighbors**.
   - Vulnerable to the **Count-to-Infinity Problem** (slow convergence when a link fails). Solutions include **Split Horizon** and **Poison Reverse**.
   - **RIP (Routing Information Protocol)**: Intradomain routing protocol using Distance Vector with Hop Count metric (max 15 hops; 16 = infinity).

2. **Link State Routing (LSR)**:
   - Based on **Dijkstra's Shortest Path Algorithm**.
   - Each router discovers its immediate neighbors, measures delay/cost, builds a **Link State Packet (LSP)**, and **floods** the LSP to *all routers* in the network.
   - Every router builds a complete, identical map of the entire network topology and runs Dijkstra independently. Fast convergence, no count-to-infinity problem.
   - **OSPF (Open Shortest Path First)**: Widely used intradomain Link State protocol supporting hierarchical area partitioning (Area 0 Backbone).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Distance Vector Routing Table Update (Bellman-Ford Math)
**Problem:** Router $J$ receives a Distance Vector update from neighbor $X$.
- Link cost from $J$ to $X$ is $c(J,X) = 3$.
- $X$'s vector to destinations $(A, B, C, D)$ is: $[A: 12, B: 8, C: 20, D: 4]$.
- $J$'s current routing table is: $[A: 18 \text{ via } K, B: 14 \text{ via } L, C: 22 \text{ via } X, D: 9 \text{ via } M]$.
Calculate $J$'s new distance vector and updated next-hop table using Bellman-Ford equation:
$$D_J(Y) = \min(D_J(Y), c(J,X) + D_X(Y))$$

**Step-by-step Solution:**
1. **Destination A:**
   - Via $X$: $c(J,X) + D_X(A) = 3 + 12 = 15$.
   - Existing: $18$ via $K$.
   - $\min(18, 15) = 15 \implies$ Update $A$: **Cost 15 via $X$**.
2. **Destination B:**
   - Via $X$: $3 + 8 = 11$.
   - Existing: $14$ via $L$.
   - $\min(14, 11) = 11 \implies$ Update $B$: **Cost 11 via $X$**.
3. **Destination C:**
   - Via $X$: $3 + 20 = 23$.
   - Existing: $22$ via $X$. Since $X$ is the next-hop, mandatory update $\rightarrow$ **Cost 23 via $X$**.
4. **Destination D:**
   - Via $X$: $3 + 4 = 7$.
   - Existing: $9$ via $M$.
   - $\min(9, 7) = 7 \implies$ Update $D$: **Cost 7 via $X$**.
5. **New Routing Table at J:**
   - $A \rightarrow 15 \text{ via } X$
   - $B \rightarrow 11 \text{ via } X$
   - $C \rightarrow 23 \text{ via } X$
   - $D \rightarrow 7 \text{ via } X$

### Example 2: Count-to-Infinity Problem & Split Horizon Walkthrough
**Problem:** Routers $A, B, C$ are connected in a line ($A - B - C$). Link costs are 1. Link $A-B$ fails. Explain how Count-to-Infinity occurs without Split Horizon and how Split Horizon prevents it.
**Step-by-step Solution:**
1. **Initial State:**
   - $B$'s distance to $A = 1$. $C$'s distance to $A = 2$ (via $B$).
2. **Link $A-B$ Fails (Without Split Horizon):**
   - $B$ sets $D_B(A) = \infty$.
   - Before $B$ can send update, $C$ sends vector to $B$ saying $D_C(A) = 2$.
   - $B$ thinks $C$ has a path to $A$ of length 2! $B$ updates $D_B(A) = 2 + 1 = 3$ via $C$.
   - In next step, $C$ updates $D_C(A) = 3 + 1 = 4$ via $B$.
   - Distance slowly counts up to $\infty$ (16 in RIP).
3. **With Split Horizon Rule:**
   - Rule: "Do not advertise a route back to the neighbor from whom you learned it."
   - Since $C$ learned its route to $A$ from $B$, $C$ **refuses to advertise $A$ to $B$**.
   - When $A-B$ fails, $B$ sees no alternative route from $C$ and correctly sets $D_B(A) = \infty$ immediately.

### Example 3: OSPF Hierarchical Area Structure
**Problem:** Explain OSPF Area partitioning. Differentiate between Backbone Router (ABR), Autonomous System Boundary Router (ASBR), and Internal Router.
**Step-by-step Solution:**
1. **OSPF Area Partitioning:**
   - Divides a large Autonomous System (AS) into smaller logical **Areas** (Area 0.0.0.0 is the **Backbone Area**).
   - Link State Packets (LSPs) are flooded *only within their local Area*, preventing global LSP flooding overhead across thousands of routers.
2. **Router Classifications:**
   - **Internal Router:** All interfaces belong to the same non-backbone area.
   - **Area Border Router (ABR):** Attached to multiple areas (at least one interface in Area 0). Summarizes routes between areas.
   - **Autonomous System Boundary Router (ASBR):** Connects OSPF network to external routing domains (e.g. BGP or RIP).

---

## 3. Previous Year Questions & Solutions

1. **"Explain Distance Vector Routing. Discuss Count-to-Infinity problem and its solutions." [April 2018, Dec 2019]**
   - **Solution:**
     **Distance Vector:** Each router maintains a table $D_i(j)$ of distances to all nodes, periodically sharing its vector with direct neighbors. Uses Bellman-Ford equation: $D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$.
     **Count-to-Infinity:** When a link fails, good news travels fast, but bad news travels slow. Two neighbors can form a routing loop, incrementing cost by 1 on each exchange until reaching infinity.
     **Solutions:**
     - **Split Horizon:** Do not report routes back to the node from which they were learned.
     - **Poison Reverse:** Report route back to node with cost $\infty$ when learned from that node.

2. **"Differentiate between Distance Vector Routing and Link State Routing." [May 2019, July 2021]**
   - **Solution:**
     | Parameter | Distance Vector Routing (RIP) | Link State Routing (OSPF) |
     | :--- | :--- | :--- |
     | **Algorithm** | Bellman-Ford Algorithm | Dijkstra's Shortest Path Algorithm |
     | **Information Shared** | Entire routing table | Only state of directly connected links (LSP) |
     | **Sharing Target** | Immediate neighbors only | Flooded to all routers in network/area |
     | **Convergence Speed** | Slow (vulnerable to Count-to-Infinity) | Fast convergence |
     | **Traffic / Overhead** | Low bandwidth, high periodic updates | High initial flooding, low periodic maintenance |
