# Module 3 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 3**: Network Layer & Routing Algorithms

---

## 🚀 Submodule 1: Datagram vs VC Subnets & Dijkstra

- **Datagram Subnet**: Connectionless; independent packet routing; full IP address per packet; resilient to router failure.
- **Virtual Circuit Subnet**: Connection-oriented; 3-phase setup; short VC identifier per packet; in-order delivery.
- **Dijkstra's Algorithm**: $O(V^2)$ algorithm finding minimum cost path from source node to all destinations using tentative distance vector $D[u]$.

---

## 🚀 Submodule 2: Distance Vector vs Link State Routing

- **Distance Vector (RIP)**: Bellman-Ford equation $D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$; exchanges entire table with immediate neighbors. Max hop count = 15.
- **Count-to-Infinity Solutions**: **Split Horizon** (don't advertise route back to source node) and **Poison Reverse** (advertise route with $\infty$ cost).
- **Link State (OSPF)**: Floods Link State Packets (LSP) to all routers; every router runs Dijkstra independently. Uses hierarchical areas (Area 0 Backbone).

---

## 🔢 3 Solved Numerical Micro-Examples

1. **Dijkstra Relaxation**: If $D[B] = 2$ and $c(B,C) = 1$, updated $D[C] = \min(\infty, 2+1) = 3$.
2. **Bellman-Ford Update**: Neighbor $X$ reports $D_X(A) = 12$. Link $c(J,X) = 3$. Updated cost $D_J(A) = 3 + 12 = 15$.
3. **Flooding Packets**: Node degree $k = 4$, $\text{TTL} = 2$. Total packets $= 4 + (4 \times 3) = 16$.
