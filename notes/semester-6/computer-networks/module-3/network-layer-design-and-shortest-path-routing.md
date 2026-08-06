# Module 3 — Topic 1: Network Layer Design & Shortest Path Routing

> **Module 3**: Network Layer & Routing Algorithms  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Network Layer** (Layer 3) is responsible for routing packets from source to destination across multiple intermediate network hops (routers):

1. **Network Layer Services**:
   - **Connectionless Service (Datagram Subnet)**: Each packet is routed independently using the destination IP address. Fast, resilient to router crashes, but packets may arrive out-of-order.
   - **Connection-Oriented Service (Virtual-Circuit Subnet)**: A path is established before sending data. All packets follow the same path (virtual circuit ID), ensuring in-order arrival.

2. **Shortest Path Routing (Dijkstra's Algorithm)**:
   - Represents the network as a weighted graph where vertices are routers and edges are physical communication links.
   - Computes the minimum-cost path from a source router to all other routers using edge weights (distance, delay, or cost).

3. **Flooding**:
   - Every incoming packet is retransmitted on every outgoing link except the one it arrived on.
   - Generates duplicate packets, but guarantees delivery over the shortest path without requiring routing tables. Used in military applications and routing protocol initialization (LSA flooding).

### Example
Think of Network Layer Routing like Google Maps GPS Navigation:
- **Datagram Routing**: Each driver evaluates traffic conditions at every intersection (router) independently.
- **Dijkstra's Shortest Path**: The GPS server analyzes road distances and speed limits (link costs) to compute the single optimal route before you start driving.

### Applications & Use Cases
- **Enterprise Network Edge**: Routers build forwarding tables to send internet traffic to local ISP gateways.
- **CDN Global Traffic Steering**: Content Delivery Networks (Cloudflare, Akamai) use shortest-path latency metrics to route users to the nearest edge server.

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
