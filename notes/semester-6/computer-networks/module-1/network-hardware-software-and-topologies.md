# Module 1 — Topic 1: Network Hardware, Software & Topologies

> **Module 1**: Network Architecture & Reference Models  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
A **Computer Network** is an interconnected collection of autonomous computers capable of exchanging information. Modern computer networks are categorized by their geographical scale and architectural topologies:
- **Local Area Network (LAN)**: Privately owned networks covering a small geographic area (home, office, building up to 1 km). Characterized by high data transfer rates (100 Mbps to 10 Gbps) and low delay.
- **Metropolitan Area Network (MAN)**: Covers an entire city or town (5 km to 50 km), such as a municipal cable TV network.
- **Wide Area Network (WAN)**: Spans large geographical distances (country, continent, or entire globe). Connects subnets across leased telecommunication lines via routers.
- **Internetworks**: A collection of disparate physical networks interconnected by routers operating under a common protocol suite (TCP/IP).

**Network Topologies** define the geometric arrangement of links and nodes:
1. **Bus Topology**: Single central cable (backbone) to which all nodes connect. Simple, low cost, but vulnerable to cable failure.
2. **Star Topology**: All nodes connect to a central hub/switch. Easy to isolate faults; failure of one cable affects only that node.
3. **Ring Topology**: Nodes connected in a circular loop. Signals travel in one direction using token passing.
4. **Mesh Topology**: Every node is connected to every other node via dedicated point-to-point links. Highly redundant and reliable ($N(N-1)/2$ physical links for $N$ nodes).

### Example
Think of a computer network as a country's postal and highway system. 
- A **LAN** is like internal mail delivery inside a single company headquarters—fast, direct, and private.
- A **WAN** is like the international postal service, using hubs, delivery trucks, airports, and sorting facilities (routers) to route packages across continents.
- A **Star Topology** resembles an airport hub-and-spoke system: all flights pass through a major central airport hub. If one regional airport closes, the rest of the country's network keeps flying.

### Applications & Use Cases
- **Data Center Networks (Fat-Tree Mesh Topologies)**: Modern hyperscale data centers (AWS, Google Cloud) use leaf-spine mesh topologies to provide high bisection bandwidth between thousands of servers.
- **Enterprise Office LANs (Switched Star)**: Companies deploy Ethernet star networks using Gigabit switches for reliable, fault-isolated workstations.
- **Storage Area Networks (SANs)**: High-speed Fibre Channel ring/mesh networks dedicated to block-level data storage access.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Physical Link Calculation in Mesh vs Star Topology
**Problem:** A bank needs to connect 20 regional branch servers ($N = 20$). Compare the total number of physical duplex cables required for (a) a Fully Mesh Topology, and (b) a Central Switch Star Topology.
**Step-by-step Solution:**
1. **Fully Mesh Topology Formula:**
   $$L_{\text{mesh}} = \frac{N(N - 1)}{2}$$
   $$L_{\text{mesh}} = \frac{20 \times (20 - 1)}{2} = \frac{20 \times 19}{2} = 190 \text{ physical cables}$$
   Each node requires $N - 1 = 19$ I/O ports. Total I/O ports across all 20 nodes = $20 \times 19 = 380$ ports.

2. **Star Topology Formula:**
   $$L_{\text{star}} = N = 20 \text{ physical cables}$$
   Each node requires only 1 I/O port, and the central switch requires 20 ports.

3. **Comparison:** The Star topology requires **190 vs 20 cables** (90% reduction in cabling) and avoids port density bottlenecks on servers.

### Example 2: Bandwidth-Delay Product (BDP) & Volume Calculation
**Problem:** Calculate the Bandwidth-Delay Product (BDP) for a 1 Gbps cross-country WAN link with a Round-Trip Time (RTT) of 45 ms. How many bits are in-flight (pipe volume) at any instant?
**Step-by-step Solution:**
1. **Identify Given Values:**
   - Bandwidth ($B$) = $1 \text{ Gbps} = 10^9 \text{ bits/second}$.
   - One-way Delay ($D$) = $\frac{\text{RTT}}{2} = \frac{45 \text{ ms}}{2} = 22.5 \text{ ms} = 0.0225 \text{ seconds}$.
2. **Apply BDP Formula:**
   $$\text{BDP} = B \times D = 10^9 \text{ bits/s} \times 0.0225 \text{ s} = 22,500,000 \text{ bits}$$
3. **Convert to Bytes:**
   $$\text{Volume} = \frac{22,500,000}{8} = 2,812,500 \text{ Bytes} \approx 2.81 \text{ MB}$$
4. **Interpretation:** The transmitter can send **2.81 Megabytes of data** before the first bit reaches the destination receiver.

### Example 3: Propagation vs Transmission Delay Comparison
**Problem:** A 10 KB packet is sent over a 1,000 km fiber optic link operating at 100 Mbps. Propagation speed in fiber is $2 \times 10^8 \text{ m/s}$. Compare the Transmission Delay ($T_t$) and Propagation Delay ($T_p$).
**Step-by-step Solution:**
1. **Convert Units:**
   - Packet Size ($L$) = $10 \text{ KB} = 10 \times 8 \times 10^3 \text{ bits} = 80,000 \text{ bits}$.
   - Bandwidth ($R$) = $100 \text{ Mbps} = 10^8 \text{ bits/second}$.
   - Distance ($d$) = $1,000 \text{ km} = 10^6 \text{ meters}$.
   - Speed ($v$) = $2 \times 10^8 \text{ m/s}$.
2. **Calculate Transmission Delay ($T_t$):**
   $$T_t = \frac{L}{R} = \frac{80,000 \text{ bits}}{10^8 \text{ bits/s}} = 0.0008 \text{ seconds} = 0.8 \text{ ms}$$
3. **Calculate Propagation Delay ($T_p$):**
   $$T_p = \frac{d}{v} = \frac{10^6 \text{ m}}{2 \times 10^8 \text{ m/s}} = 0.005 \text{ seconds} = 5.0 \text{ ms}$$
4. **Conclusion:** Propagation delay ($5 \text{ ms}$) dominates transmission delay ($0.8 \text{ ms}$) by a factor of 6.25. Total Latency = $T_t + T_p = 5.8 \text{ ms}$.

---

## 3. Previous Year Questions & Solutions

1. **"Differentiate between LAN, MAN, and WAN based on scale, ownership, and data rates." [May 2019]**
   - **Solution:**
     | Parameter | Local Area Network (LAN) | Metropolitan Area Network (MAN) | Wide Area Network (WAN) |
     | :--- | :--- | :--- | :--- |
     | **Geographic Scale** | Room, building, campus (< 1 km - 10 km) | City or town (10 km - 50 km) | Country, continent, global (> 100 km) |
     | **Ownership** | Private (single individual or organization) | Private or Public (cable provider, telecom) | Public or Private Consortium (Telecoms) |
     | **Data Rates** | High (100 Mbps to 10 Gbps) | Moderate (10 Mbps to 100 Mbps) | Lower (1 Mbps to 1 Gbps per link) |
     | **Propagation Delay** | Very Low (microseconds) | Moderate (milliseconds) | High (tens to hundreds of milliseconds) |
     | **Fault Rate / Errors** | Very Low | Moderate | High |

2. **"Compare Bus, Star, and Ring topologies. Highlight fault tolerance in each." [Dec 2019]**
   - **Solution:**
     - **Bus Topology:** Single central cable. **Fault Tolerance:** Low. If the main coaxial cable breaks or a terminator is lost, the entire network drops due to signal reflection.
     - **Star Topology:** Nodes connect to central switch. **Fault Tolerance:** High for individual node cables (a broken drop cable isolates only 1 machine). Low for central switch (switch failure drops all connected nodes).
     - **Ring Topology:** Nodes connected in a circular loop. **Fault Tolerance:** Low in single ring (1 node break breaks the loop). High in Dual Ring (e.g. FDDI) which counter-rotates signals to heal broken links.
