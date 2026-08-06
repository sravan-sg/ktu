# Module 3 — Topic 2: Distance Vector vs Link State Routing (RIP & OSPF) & Mobile IP

> **Module 3**: Network Layer & Routing Algorithms  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
Dynamic routing algorithms enable routers to continuously learn network topology changes and update forwarding tables automatically:

#### 1. Distance Vector Routing (DVR)
- Based on the **Bellman-Ford Algorithm**.
- Each router maintains a table (Vector) giving the minimum known distance to every destination and the next-hop router.
- Routers periodically exchange their entire routing table only with **immediate neighbors**.
- Vulnerable to the **Count-to-Infinity Problem** (slow convergence when a link fails). Solutions include **Split Horizon** and **Poison Reverse**.
- **RIP (Routing Information Protocol)**: Intradomain routing protocol using Distance Vector with Hop Count metric (max 15 hops; 16 = infinity).

---

#### 2. Link State Routing (LSR)
- Based on **Dijkstra's Shortest Path Algorithm**.
- Each router discovers its immediate neighbors, measures delay/cost, builds a **Link State Packet (LSP)**, and **floods** the LSP to *all routers* in the network/area.
- Every router builds a complete, identical map of the entire network topology and runs Dijkstra independently. Fast convergence, no count-to-infinity problem.
- **OSPF (Open Shortest Path First)**: Widely used intradomain Link State protocol supporting hierarchical area partitioning (Area 0 Backbone).

---

#### 3. Routing for Mobile Hosts (Mobile IP)
When a mobile node (laptop, mobile phone) moves from its **Home Network** to a **Foreign Network**, its IP address cannot change continuously without breaking active TCP connections. **Mobile IP** solves this using agents:

```
 Correspondent Node (CN)
        │ 1. IP Packet (Src: CN, Dst: Home IP)
        ▼
   Home Network ───────────► Home Agent (HA)
                              │ 2. Encapsulates PDU inside IP Tunnel
                              ▼ (Care-of Address)
   Foreign Network ────────► Foreign Agent (FA) / Mobile Node (MN)
```

- **Home Address**: Permanent IP address assigned to the mobile node on its home network.
- **Home Agent (HA)**: Router on the home network that intercepts packets destined for the mobile node when it is away.
- **Foreign Agent (FA)**: Router on the foreign network that assigns a temporary **Care-of Address (CoA)** to the mobile node.
- **Tunneling & Encapsulation**: HA encapsulates incoming packets destined for the Home Address inside an outer IP header addressed to the CoA (IP-in-IP tunneling) and forwards them to the FA.
- **Triangular Routing**: Packets from Correspondent Node (CN) to Mobile Node go via HA, but return packets from Mobile Node to CN go directly via standard IP routing.

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
   - Via $X$: $c(J,X) + D_X(A) = 3 + 12 = 15$. Existing: $18$ via $K$. $\min(18, 15) = 15 \implies$ Update $A$: **Cost 15 via $X$**.
2. **Destination B:**
   - Via $X$: $3 + 8 = 11$. Existing: $14$ via $L$. $\min(14, 11) = 11 \implies$ Update $B$: **Cost 11 via $X$**.
3. **Destination C:**
   - Via $X$: $3 + 20 = 23$. Existing: $22$ via $X$. Mandatory update $\rightarrow$ **Cost 23 via $X$**.
4. **Destination D:**
   - Via $X$: $3 + 4 = 7$. Existing: $9$ via $M$. $\min(9, 7) = 7 \implies$ Update $D$: **Cost 7 via $X$**.
5. **New Routing Table at J:**
   - $A \rightarrow 15 \text{ via } X$, $B \rightarrow 11 \text{ via } X$, $C \rightarrow 23 \text{ via } X$, $D \rightarrow 7 \text{ via } X$.

### Example 2: Count-to-Infinity Problem & Split Horizon Walkthrough
**Problem:** Routers $A, B, C$ are connected in a line ($A - B - C$). Link costs are 1. Link $A-B$ fails. Explain how Count-to-Infinity occurs without Split Horizon and how Split Horizon prevents it.
**Step-by-step Solution:**
1. **Initial State:** $B$'s distance to $A = 1$. $C$'s distance to $A = 2$ (via $B$).
2. **Link $A-B$ Fails (Without Split Horizon):**
   - $B$ sets $D_B(A) = \infty$.
   - $C$ sends vector to $B$ saying $D_C(A) = 2$.
   - $B$ thinks $C$ has a path to $A$ of length 2 and updates $D_B(A) = 2 + 1 = 3$ via $C$.
   - In next step, $C$ updates $D_C(A) = 3 + 1 = 4$ via $B$. Distance counts up to $\infty$ (16 in RIP).
3. **With Split Horizon Rule:**
   - "Do not advertise a route back to the neighbor from whom you learned it."
   - Since $C$ learned its route to $A$ from $B$, $C$ **refuses to advertise $A$ to $B$**.
   - $B$ correctly sets $D_B(A) = \infty$ immediately.

### Example 3: Mobile IP Tunneling & Care-of Address Trace
**Problem:** A mobile node (Home IP: `192.168.1.50`) moves from its home network to a foreign network (`10.0.0.0/8`). 
1. Explain how the Home Agent (HA) intercepts and delivers packets sent by a Correspondent Node (CN IP: `200.1.1.1`).
2. Identify the source and destination IP addresses in the outer IP tunnel header vs inner payload header.
**Step-by-step Solution:**
1. **Agent Registration:** Upon moving to the foreign network, the Mobile Node gets a **Care-of Address (CoA)** `10.0.0.85` from the Foreign Agent (FA) and registers it with its Home Agent (HA).
2. **Packet Transmission from CN:**
   - CN sends packet: `[Src IP: 200.1.1.1, Dst IP: 192.168.1.50]`.
   - HA intercepts this packet on the Home Network via Proxy ARP.
3. **Tunneling (IP-in-IP Encapsulation):**
   - HA encapsulates original packet inside an outer IP header:
     - Outer Header: `[Src IP: HA_IP, Dst IP: 10.0.0.85 (CoA)]`
     - Inner Payload: `[Src IP: 200.1.1.1, Dst IP: 192.168.1.50]`
   - HA routes outer packet over standard Internet to the Foreign Agent (CoA).
4. **Decapsulation:** FA strips outer header and delivers original inner packet to Mobile Node.

---

## 3. Previous Year Questions & Solutions

1. **"Explain Distance Vector Routing. Discuss Count-to-Infinity problem and its solutions." [April 2018, Dec 2019]**
   - **Solution:**
     **Distance Vector:** Each router maintains a table $D_i(j)$ of distances to all nodes, periodically sharing its vector with direct neighbors. Uses Bellman-Ford equation: $D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$.
     **Count-to-Infinity:** When a link fails, good news travels fast, but bad news travels slow. Two neighbors can form a routing loop, incrementing cost by 1 on each exchange until reaching infinity.
     **Solutions:** Split Horizon and Poison Reverse.

2. **"Differentiate between Distance Vector Routing and Link State Routing." [May 2019, July 2021]**
   - **Solution:**
     | Parameter | Distance Vector Routing (RIP) | Link State Routing (OSPF) |
     | :--- | :--- | :--- |
     | **Algorithm** | Bellman-Ford Algorithm | Dijkstra's Shortest Path Algorithm |
     | **Information Shared** | Entire routing table | Only state of directly connected links (LSP) |
     | **Sharing Target** | Immediate neighbors only | Flooded to all routers in network/area |
     | **Convergence Speed** | Slow (vulnerable to Count-to-Infinity) | Fast convergence |

3. **"Explain Mobile IP routing architecture. How are Home Agent, Foreign Agent, and Care-of Address utilized?" [Dec 2019]**
   - **Solution:**
     - **Home Agent (HA)**: Intercepts packets sent to the mobile node's static Home Address when away from home.
     - **Foreign Agent (FA)**: Assigns temporary Care-of Address (CoA) and decapsulates incoming tunneled packets on foreign network.
     - **Care-of Address (CoA)**: Temporary IP address indicating mobile node's current location.
     - **Tunneling**: HA wraps incoming PDU inside an outer IP header addressed to CoA (IP-in-IP encapsulation).
