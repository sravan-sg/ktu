# Module 3 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 3**: Network Layer & Routing Algorithms

---

## 🚀 Submodule 1: Network Layer & Routing Fundamentals

- **Store-and-Forward Packet Switching**: Packets buffered at intermediate routers until fully received before forwarding.
- **Datagram vs Virtual Circuit Subnets**:
  - *Datagram*: Connectionless; each packet contains full destination IP and routed independently. Fast setup, robust to failures.
  - *Virtual Circuit (VC)*: Connection-oriented; setup phase creates virtual circuit ID (VCID). Packets use VCID; predictable QoS, vulnerable to router failures.
- **Dijkstra's Shortest Path**: Computes single-source shortest path tree using non-negative link weights. $O(V^2)$ or $O(E \log V)$ with priority queue.

---

## 🚀 Submodule 2: Distance Vector vs Link State Routing

- **Distance Vector Routing (RIP)**:
  - Bellman-Ford equation: $D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$.
  - Routers share FULL routing tables periodically with IMMEDIATE neighbors only.
  - *Count-to-Infinity Problem*: Slow convergence on link failure. Solved using **Split Horizon** (don't advertise route back to source) and **Poison Reverse** (advertise infinity cost).
  - *RIP*: Max hop count $= 15$ hops ($16 = \infty$). Updates every 30s over UDP 520.
- **Link State Routing (OSPF)**:
  - Routers flood **Link State Packets (LSPs)** to ALL routers; each router builds identical global map and runs Dijkstra locally.
  - *OSPF*: Interior Gateway Protocol over IP (Protocol 89). Hierarchical structure centered around **Area 0 (Backbone)**. LSA Types 1–5 (Router, Network, Summary, ASBR Summary, External).

---

## 🚀 Submodule 3: Mobile IP Routing Architecture

- **Home Address**: Permanent IP assigned to mobile node on home network.
- **Home Agent (HA)**: Router on home network that intercepts packets using Proxy ARP.
- **Care-of Address (CoA)**: Temporary IP assigned by Foreign Agent (FA) on visited network.
- **IP-in-IP Tunneling**: HA wraps original IP packet inside outer IP header addressed to CoA.
- **Triangular Routing**: Packets from Correspondent Node go through HA to CoA, while outbound response packets from Mobile Node go directly to CN.

---

## 🔢 3 Solved Numerical Micro-Examples

1. **Distance Vector Update**: Link cost $c(J,X) = 3$. Neighbor $X$ advertises distance to node $D = 4$. Node $J$'s new distance to $D$ via $X = 3 + 4 = \mathbf{7}$.
2. **OSPF Cost Math**: Reference bandwidth $= 100 \text{ Mbps}$. Link $= 10 \text{ Mbps}$. $\text{Cost} = \frac{100}{10} = \mathbf{10}$.
3. **Flooding Packet Copies**: Node degree $= 4$. Controlled flooding with sequence number table suppresses duplicates $\implies$ exactly $\mathbf{3 \text{ copies}}$ sent out per new packet.
