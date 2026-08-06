# Module 3 — Topic 1: Network Layer Design Issues, Shortest Path Routing & Flooding

> **Module 3**: Network Layer & Routing Algorithms  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Network Layer** (Layer 3) is responsible for end-to-end packet delivery from source to destination across multiple intermediate network hops (routers).

---

### 1. Network Layer Design Issues & Subnet Models

```
   Host A                             Router 1                           Router 2
  ┌──────┐                           ┌──────┐                           ┌──────┐
  │App/T │                           │      │                           │      │
  ├──────┤   1. Packet Transmission  ├──────┤   2. Store & Forward      ├──────┤
  │ Net  ├──────────────────────────►│ Net  ├──────────────────────────►│ Net  │
  └──────┘   (Full Frame Received)   └──────┘   (Check Checksum & Route)└──────┘
```

1. **Store-and-Forward Packet Switching**:
   - Packets travel hop-by-hop across intermediate routers.
   - When a packet arrives at a router, it is stored in a memory buffer until the entire frame is received and its checksum is verified. Only then is it processed and forwarded to the next router along the output queue.

2. **Services Provided to Transport Layer**:
   - Shielding the transport layer from the physical details and transmission technologies of intermediate subnets.
   - Providing uniform addressing mechanisms across heterogeneous networks (LANs, WANs, Satellite links).

3. **Subnet Architectures: Datagram vs Virtual-Circuit Subnets**:
   - **Connectionless (Datagram Subnet)**:
     - Each packet is treated independently and carries full 32-bit source and destination IP addresses.
     - Routers evaluate destination IP at every hop to choose the best outgoing link.
     - Resilient to router failures (packets naturally route around crashed routers), but packets may arrive out-of-order.
   - **Connection-Oriented (Virtual-Circuit Subnet)**:
     - A virtual path is established between source and destination before data transfer begins.
     - Packets carry a short **Virtual Circuit Identifier (VCI)** instead of full IP addresses.
     - All packets follow the exact same established path, guaranteeing in-order arrival, but a single router crash along the path terminates the virtual circuit.

| Parameter | Datagram Subnet | Virtual Circuit Subnet |
| :--- | :--- | :--- |
| **Circuit Setup** | Not required | Mandatory setup phase |
| **Addressing** | Each packet carries full 32-bit IP | Packets carry short 16-bit VCI |
| **Router State Info** | No connection state stored in routers | Routers store state table for each VC |
| **Routing** | Dynamic routing per packet | Path chosen during setup; all packets follow it |
| **Effect of Router Crash** | Minimal (packets rerouted automatically) | All VCs passing through crashed router terminate |
| **Quality of Service** | Difficult to guarantee | Easy to allocate bandwidth during setup |

---

### 2. Shortest Path Routing (Dijkstra's Algorithm)
- Represents the network as a weighted graph $G = (V, E)$ where vertices $V$ are routers and edges $E$ are physical links.
- Edge weights represent physical distance, propagation delay, or link cost.
- Computes the minimum-cost path from a source router $s$ to all destination routers.

---

### 3. Flooding & Its Mechanisms
- A static routing technique where every incoming packet is retransmitted on every outgoing link except the one it arrived on.
- **Flooding Variations**:
  - **Uncontrolled Flooding**: Routers forward all packets blindly, causing infinite packet duplication loops.
  - **Controlled Flooding (Hop Count / TTL)**: Each packet carries a **Time-to-Live (TTL)** counter. Each router decrements TTL by 1; when TTL reaches 0, the packet is discarded.
  - **Controlled Flooding (Sequence Numbers)**: Source router appends a sequence number to every packet. Intermediate routers log `<Source IP, Sequence No>` in a history buffer and drop duplicate packets.
  - **Selective Flooding**: Routers forward incoming packets only on links that lead approximately in the direction of the destination.

---

### Real-World Example
Think of Network Layer Routing like Google Maps GPS Navigation:
- **Datagram Subnet**: Drivers check live traffic independently at every intersection and can switch routes midway.
- **Virtual Circuit Subnet**: A train traveling along a fixed railway track system—switches are aligned during setup, and all train cars follow the exact same track sequence.
- **Flooding**: Emergency radio broadcasts sent to all local radio towers simultaneously to ensure 100% immediate coverage regardless of local tower failures.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Dijkstra's Shortest Path Algorithm Step-by-Step Trace
**Problem:** Trace Dijkstra's algorithm to find the shortest path from source node $A$ to all other nodes in the network graph:
- Edges: $(A,B)=2, (A,C)=5, (B,C)=1, (B,D)=4, (C,D)=2, (D,E)=1$.
**Step-by-step Solution:**
1. **Initialization:**
   - Set distance vector $D[V]$: $D[A]=0, D[B]=\infty, D[C]=\infty, D[D]=\infty, D[E]=\infty$.
   - Unvisited set $S = \{A, B, C, D, E\}$. Current node $u = A$.
2. **Iteration 1 (Process A):**
   - Neighbors of A: $B$ (cost $0+2=2$), $C$ (cost $0+5=5$).
   - Update: $D[B]=2$, $D[C]=5$. Mark $A$ visited. Min unvisited is $B$ ($D[B]=2$). Next $u = B$.
3. **Iteration 2 (Process B):**
   - Neighbors of B: $C$ ($2+1=3 < 5 \implies D[C]=3$), $D$ ($2+4=6 \implies D[D]=6$).
   - Update: $D[C]=3$, $D[D]=6$. Mark $B$ visited. Min unvisited is $C$ ($D[C]=3$). Next $u = C$.
4. **Iteration 3 (Process C):**
   - Neighbors of C: $D$ ($3+2=5 < 6 \implies D[D]=5$).
   - Update: $D[D]=5$. Mark $C$ visited. Min unvisited is $D$ ($D[D]=5$). Next $u = D$.
5. **Iteration 4 (Process D):**
   - Neighbors of D: $E$ ($5+1=6 \implies D[E]=6$). Mark $D$ visited. Next $u = E$.
6. **Final Shortest Paths from A:**
   - $A \rightarrow B$: Cost **2** (Path: $A-B$)
   - $A \rightarrow C$: Cost **3** (Path: $A-B-C$)
   - $A \rightarrow D$: Cost **5** (Path: $A-B-C-D$)
   - $A \rightarrow E$: Cost **6** (Path: $A-B-C-D-E$)

### Example 2: Datagram Subnet vs Virtual Circuit Overhead Analysis
**Problem:** A 1,000-byte message is split into 10 packets of 100 bytes each. Compare total bandwidth overhead for (a) Datagram subnet (32-byte header per packet), and (b) Virtual Circuit subnet (150-byte setup packet, 4-byte VC header per packet, 50-byte teardown packet).
**Step-by-step Solution:**
1. **Datagram Subnet Overhead:**
   $$\text{Total Header Bytes} = 10 \text{ packets} \times 32 \text{ Bytes} = 320 \text{ Bytes}$$
   $$\text{Total Transmitted Bytes} = 1000 + 320 = 1,320 \text{ Bytes}$$
2. **Virtual Circuit Subnet Overhead:**
   $$\text{Setup + Teardown} = 150 + 50 = 200 \text{ Bytes}$$
   $$\text{Packet Headers} = 10 \text{ packets} \times 4 \text{ Bytes} = 40 \text{ Bytes}$$
   $$\text{Total Transmitted Bytes} = 1000 + 200 + 40 = 1,240 \text{ Bytes}$$
3. **Conclusion:** For long streams (10+ packets), Virtual Circuit overhead ($240 \text{ Bytes}$) is lower than Datagram overhead ($320 \text{ Bytes}$).

### Example 3: Flooding Packet Generation Count
**Problem:** In a network with average node degree $k = 4$, a host initiates a flooded packet with Time-to-Live $\text{TTL} = 3$. Assuming no duplicate packet suppression, how many packets are generated in total?
**Step-by-step Solution:**
1. **Hop 1 ($\text{TTL}=3$):** Source sends to $k=4$ neighbors. Packets generated = $4$.
2. **Hop 2 ($\text{TTL}=2$):** Each of the 4 neighbors forwards to $k-1=3$ other links. Packets generated = $4 \times 3 = 12$.
3. **Hop 3 ($\text{TTL}=1$):** Each of the 12 nodes forwards to $3$ other links. Packets generated = $12 \times 3 = 36$.
4. **Total Packets Generated:** $4 + 12 + 36 = \mathbf{52 \text{ packets}}$.

---

## 3. Previous Year Questions & Solutions

1. **"Explain Dijkstra's shortest path algorithm with an example." [May 2019, July 2021]**
   - **Solution:**
     **Algorithm:** Maintains a set $S$ of nodes with finalized shortest distance from source $v_0$. At each step, selects unvisited node $u$ with minimum tentative distance $D[u]$, adds $u$ to $S$, and updates distance to all unvisited neighbors $w$:
     $$D[w] = \min(D[w], D[u] + c(u, w))$$
     **Complexity:** $O(V^2)$ with array implementation, $O((E + V) \log V)$ with min-heap.

2. **"Compare Datagram subnets and Virtual Circuit subnets." [Dec 2019]**
   - **Solution:**
     - **Datagram Subnet:** Connectionless. Each packet routed independently using full 32-bit IP destination address. No setup phase. Resilient to router failures. Out-of-order arrival possible.
     - **Virtual Circuit Subnet:** Connection-oriented. 3-phase setup (Setup, Data, Teardown). Packets carry short Virtual Circuit Identifier (VCI). In-order delivery guaranteed. Router failure breaks connection.

3. **"Explain Flooding routing algorithm. Differentiate between Controlled and Uncontrolled flooding." [April 2018]**
   - **Solution:**
     - **Flooding**: Packet is retransmitted on every outgoing link except the arriving link.
     - **Uncontrolled Flooding**: Routers forward indefinitely $\rightarrow$ packet storms.
     - **Controlled Flooding**: Uses TTL field (decremented per hop until 0) or Sequence Number buffers (drops seen packets) to prevent infinite loops.
