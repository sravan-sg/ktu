# Module 3 — Topic 2: Distance Vector vs Link State Routing (RIP & OSPF) & Mobile IP

> **Module 3**: Network Layer & Routing Algorithms  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
Dynamic routing protocols allow routers to dynamically discover network topologies, adapt to link failures, and compute optimal forwarding paths.

---

### 1. Distance Vector Routing (DVR) & RIP Protocol
- **Algorithm**: **Bellman-Ford Algorithm**.
- **Mechanics**:
  - Each router maintains a routing table listing destination, cost (distance), and next-hop router.
  - Every 30 seconds, routers exchange their entire routing vector only with **immediate neighbors**.
  - Bellman-Ford Equation: $D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$.
- **Count-to-Infinity Problem**: When a link breaks, routers slowly increment distances in a loop until reaching infinity.
  - *Solutions*: **Split Horizon** (do not advertise routes back to the neighbor they were learned from) and **Poison Reverse** (advertise broken routes with cost $\infty$).
- **RIP (Routing Information Protocol)**:
  - Intradomain Distance Vector protocol using **Hop Count** as cost metric.
  - Maximum metric $= 15$ hops (16 = infinity / unreachable). Uses UDP Port 520.

---

### 2. Link State Routing (LSR) & OSPF Protocol
- **Algorithm**: **Dijkstra's Shortest Path Algorithm**.
- **Mechanics**:
  1. Router discovers neighbors and measures link costs.
  2. Builds a **Link State Packet (LSP)** listing neighbor states.
  3. **Floods** the LSP to *all routers* across the network/area.
  4. Every router constructs an identical global topology map and runs Dijkstra locally.
- **OSPF (Open Shortest Path First)**:
  - Widely used interior gateway protocol (IGP) operating directly over IP (Protocol 89).
  - **Hierarchical Area Partitioning**: Divides Autonomous Systems into logical areas centered around **Area 0.0.0.0 (Backbone Area)** to prevent global LSP flooding.
  - **OSPF LSA Types**:
    - *LSA Type 1 (Router LSA)*: Originated by all routers within an area.
    - *LSA Type 2 (Network LSA)*: Originated by Designated Routers (DR) on multi-access links.
    - *LSA Type 3 (Summary LSA)*: Originated by Area Border Routers (ABR) summarizing routes between areas.
    - *LSA Type 4 (ASBR Summary)*: Advertises location of Autonomous System Boundary Routers.
    - *LSA Type 5 (AS External LSA)*: Advertises routes external to the OSPF domain.

---

### 3. Routing for Mobile Hosts (Mobile IP)
Maintains continuous IP connectivity for mobile devices moving across different network subnets without breaking active TCP sessions.

```text
 Correspondent Node (CN)
        │ 1. Native IP Packet (Dst: Home IP 192.168.1.50)
        ▼
   Home Network ───────────► Home Agent (HA)
                              │ 2. Encapsulates inside Outer IP Tunnel Header
                              │    (Dst: Care-of Address 10.0.0.85)
                              ▼
   Foreign Network ────────► Foreign Agent (FA) / Mobile Node (MN)
                              │ 3. Decapsulates and delivers to MN
```

- **Home Address**: Permanent static IP address assigned to mobile node on its home network.
- **Home Agent (HA)**: Router on home network that intercepts packets for away hosts using Proxy ARP.
- **Foreign Agent (FA)**: Router on foreign network that assigns a temporary **Care-of Address (CoA)**.
- **IP-in-IP Tunneling**: HA wraps original IP packet inside an outer IP header addressed to the CoA.
- **Triangular Routing**: Inbound packets from Correspondent Node (CN) go through HA to CoA, but outbound response packets from Mobile Node go directly to CN.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Distance Vector Bellman-Ford Matrix Update
**Problem:** Router $J$ receives a distance vector from neighbor $X$.
- Link cost $c(J,X) = 3$.
- $X$'s vector to $(A, B, C, D)$: $[A: 12, B: 8, C: 20, D: 4]$.
- $J$'s existing vector: $[A: 18 \text{ via } K, B: 14 \text{ via } L, C: 22 \text{ via } X, D: 9 \text{ via } M]$.
Calculate $J$'s new distance vector.
**Step-by-step Solution:**
1. $D_J(A) = \min(18, 3 + 12 = 15) = \mathbf{15 \text{ via } X}$.
2. $D_J(B) = \min(14, 3 + 8 = 11) = \mathbf{11 \text{ via } X}$.
3. $D_J(C) = 3 + 20 = \mathbf{23 \text{ via } X}$ (mandatory update because existing next-hop is $X$).
4. $D_J(D) = \min(9, 3 + 4 = 7) = \mathbf{7 \text{ via } X}$.

### Example 2: OSPF Cost Calculation & Path Selection
**Problem:** OSPF calculates link cost as $\text{Cost} = \frac{\text{Reference Bandwidth}}{\text{Link Bandwidth}}$, where Reference Bandwidth $= 10^8 \text{ bps}$ ($100 \text{ Mbps}$).
Calculate OSPF cost for: (a) 10 Mbps Ethernet, (b) 100 Mbps Fast Ethernet, (c) 1 Gbps Gigabit Ethernet.
**Step-by-step Solution:**
1. **10 Mbps Ethernet:** $\text{Cost} = \frac{100 \text{ Mbps}}{10 \text{ Mbps}} = \mathbf{10}$.
2. **100 Mbps Fast Ethernet:** $\text{Cost} = \frac{100 \text{ Mbps}}{100 \text{ Mbps}} = \mathbf{1}$.
3. **1 Gbps Gigabit Ethernet:** $\text{Cost} = \frac{100 \text{ Mbps}}{1000 \text{ Mbps}} = 0.1 \implies \mathbf{1}$ (minimum OSPF cost is 1; requires adjusting reference bandwidth to 10 Gbps in modern networks).

### Example 3: Mobile IP Registration & Tunneling Trace
**Problem:** Mobile Node `MN` (Home IP `192.168.1.50`) moves to a foreign network (`10.0.0.0/8`).
Trace the outer and inner IP packet headers during data transfer from `CN` (`200.1.1.1`).
**Step-by-step Solution:**
1. `MN` acquires Care-of Address `CoA = 10.0.0.85` from Foreign Agent `FA`.
2. `MN` registers `CoA` with Home Agent `HA` (`192.168.1.1`).
3. `CN` sends packet: `[Src IP: 200.1.1.1, Dst IP: 192.168.1.50]`.
4. `HA` intercepts packet on home network and tunnels it to `CoA`:
   - Outer Tunnel Header: `[Src IP: 192.168.1.1, Dst IP: 10.0.0.85]`
   - Inner Payload Header: `[Src IP: 200.1.1.1, Dst IP: 192.168.1.50]`
5. `FA` receives outer packet, strips outer header, and delivers inner payload to `MN`.

---

## 3. Previous Year Questions & Solutions

1. **"Explain Distance Vector Routing and Count-to-Infinity problem." [April 2018, Dec 2019]**
   - **Solution:**
     Distance Vector uses Bellman-Ford algorithm where routers exchange full routing tables periodically with neighbors. Count-to-Infinity occurs when link failure bad news propagates slowly, causing routers to update costs in a loop until reaching infinity. Prevented using Split Horizon and Poison Reverse.

2. **"Explain OSPF hierarchical area structure and LSA types." [Dec 2019]**
   - **Solution:**
     OSPF partitions Autonomous Systems into Areas centered around Area 0 (Backbone) to scope Link State Packet flooding. Routers include Internal Routers, Area Border Routers (ABR), and AS Boundary Routers (ASBR). LSA Types: Type 1 (Router LSA), Type 2 (Network LSA), Type 3 (Summary LSA), Type 4 (ASBR Summary), Type 5 (AS External).

3. **"Explain Mobile IP routing architecture (HA, FA, CoA, Tunneling)." [Dec 2019]**
   - **Solution:**
     Mobile IP enables host mobility without changing IP addresses. Home Agent (HA) intercepts packets sent to static Home Address and forwards them via IP-in-IP tunneling to a Care-of Address (CoA) assigned by the Foreign Agent (FA) on the visited network.
