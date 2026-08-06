# Module 4 — Topic 1: Congestion Control Algorithms & Quality of Service (QoS)

> **Module 4**: Congestion Control, QoS & IPv4 Subnetting  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
When total network traffic exceeds the processing/forwarding capacity of intermediate routers, queues build up and **congestion** occurs. 

**Congestion Control vs Flow Control**:
- **Flow Control**: Point-to-point management between 1 fast sender and 1 slow receiver.
- **Congestion Control**: Global network-wide management to prevent intermediate routers/links from becoming overwhelmed.

**Traffic Shaping & Congestion Control Algorithms**:
1. **Leaky Bucket Algorithm**:
   - Converts bursty incoming traffic into a **smooth, constant-rate outgoing stream**.
   - Modeled as a bucket with a small hole at the bottom. If the bucket overflows, incoming packets are dropped.
2. **Token Bucket Algorithm**:
   - Tokens arrive into the bucket at a constant rate $r$. The bucket can hold up to $b$ tokens.
   - To send a $1$-byte packet, the sender must consume $1$ token. Allows **controlled burstiness** up to bucket capacity $b$.
3. **Choke Packets**:
   - A congested router generates a choke packet sent directly back to the source host ordering it to reduce transmission rate.
4. **Random Early Detection (RED)**:
   - Routers monitor average queue length. When queue size exceeds a threshold, the router randomly drops incoming packets *before* the queue fills completely, forcing TCP senders to slow down gracefully.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Token Bucket Burst Duration & Rate Math
**Problem:** A Token Bucket has a capacity $b = 5 \text{ MB}$ and receives tokens at a rate $r = 10 \text{ Mbps}$. The maximum transmission speed of the network interface is $M = 50 \text{ Mbps}$. Calculate the maximum duration $S$ for which the host can transmit at the maximum speed $M$.
**Step-by-step Solution:**
1. **Formulate Burst Equation:**
   In time $S$, the maximum data transmitted is $M \times S$.
   This data comes from the initial bucket capacity $b$ plus new tokens generated during time $S$ ($r \times S$):
   $$M \times S = b + r \times S$$
2. **Solve for Burst Duration $S$:**
   $$S (M - r) = b \implies S = \frac{b}{M - r}$$
3. **Convert Units:**
   - Bucket Capacity $b = 5 \text{ MB} = 5 \times 8 \times 10^6 \text{ bits} = 40 \text{ Megabits}$.
   - $M - r = 50 \text{ Mbps} - 10 \text{ Mbps} = 40 \text{ Mbps}$.
4. **Calculate $S$:**
   $$S = \frac{40 \text{ Megabits}}{40 \text{ Mbps}} = \mathbf{1.0 \text{ second}}$$
   The host can burst at 50 Mbps for exactly **1 second**.

### Example 2: Leaky Bucket vs Token Bucket Output Trace
**Problem:** An application generates 3 bursts of data: 12MB at $t=0$, 4MB at $t=1$, and 8MB at $t=2$. The interface output rate is 4 MB/s.
(a) For a Leaky Bucket of capacity 10 MB, trace output and packet drops.
(b) For a Token Bucket of capacity 8 MB initially full, trace output.
**Step-by-step Solution:**
1. **Leaky Bucket (Cap 10MB, Leak Rate 4MB/s):**
   - $t=0$: 12MB arrives. Bucket capacity is 10MB $\implies$ **2MB dropped immediately**. Bucket has 10MB. Transmits 4MB. Remaining = 6MB.
   - $t=1$: 4MB arrives. Current = $6 + 4 = 10\text{MB}$ (no drop). Transmits 4MB. Remaining = 6MB.
   - $t=2$: 8MB arrives. Current = $6 + 8 = 14\text{MB} \implies$ **4MB dropped**. Transmits 4MB. Remaining = 6MB.
   - Total Dropped = 6MB. Output rate is constant 4MB/s.
2. **Token Bucket (Cap 8MB, Token Rate 4MB/s):**
   - $t=0$: Initial tokens = 8MB. 12MB arrives. Transmits 8MB immediately in burst, remaining 4MB queued or sent at 4MB/s.

### Example 3: Jitter & Delay Variance Analysis for QoS
**Problem:** A real-time VoIP audio stream transmits packets at intervals of $20 \text{ ms}$. The arrival times at the receiver for 4 consecutive packets are $t_1 = 20 \text{ ms}$, $t_2 = 45 \text{ ms}$, $t_3 = 60 \text{ ms}$, $t_4 = 85 \text{ ms}$. Calculate the absolute delay jitter between consecutive packets.
**Step-by-step Solution:**
1. **Expected Arrival Intervals:** $\Delta t = 20 \text{ ms}$.
2. **Packet 1 to Packet 2:** Delay $= 45 - 20 = 25 \text{ ms}$. Jitter $J_1 = |25 - 20| = 5 \text{ ms}$.
3. **Packet 2 to Packet 3:** Delay $= 60 - 45 = 15 \text{ ms}$. Jitter $J_2 = |15 - 20| = 5 \text{ ms}$.
4. **Packet 3 to Packet 4:** Delay $= 85 - 60 = 25 \text{ ms}$. Jitter $J_3 = |25 - 20| = 5 \text{ ms}$.
5. **Average Jitter:** $\frac{5 + 5 + 5}{3} = \mathbf{5.0 \text{ ms}}$.

---

## 3. Previous Year Questions & Solutions

1. **"Explain Leaky Bucket and Token Bucket algorithms with neat diagrams. Compare them." [May 2019, July 2021]**
   - **Solution:**
     - **Leaky Bucket:** Discards packets when bucket overflows. Produces a rigid, strictly uniform output rate regardless of input burstiness. Ideal for smooth traffic shaping.
     - **Token Bucket:** Discards tokens (not packets) when bucket overflows. Allows hosts to transmit at full interface speed in bursts up to token capacity $b$. Flexible traffic shaping for bursty application data.

2. **"Define Congestion. Explain Choke Packets and RED mechanism for congestion prevention." [Dec 2019]**
   - **Solution:**
     **Congestion:** Occurs when load on network (number of packets sent) exceeds available capacity of routers/links, degrading throughput.
     **Choke Packets:** Router experiencing queue congestion sends feedback control packet back to source host commanding it to reduce sending rate.
     **RED (Random Early Detection):** Proactive queue management. Router calculates weighted average queue size. When queue exceeds threshold $Min_{th}$, router drops incoming packets with probability $P$, triggering TCP window reduction before buffer overflow occurs.
