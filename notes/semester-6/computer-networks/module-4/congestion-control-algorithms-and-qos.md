# Module 4 — Topic 1: Congestion Control Algorithms & Quality of Service (QoS)

> **Module 4**: Congestion Control, QoS & IPv4 Subnetting  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
When total network traffic exceeds the processing or forwarding capacity of intermediate routers, queues build up and **congestion** occurs. This results in packet delays, buffer overflows, dropped packets, and ultimately retransmissions that can lead to *congestion collapse*.

#### Congestion Control vs Flow Control
- **Flow Control**: Point-to-point rate matching. It prevents a single fast sender from overrunning a single slow receiver's buffer capacity (e.g., using a sliding window).
- **Congestion Control**: Global network-wide traffic management. It prevents a set of senders from overloading the intermediate routers and shared links in the network.

---

### Traffic Shaping & Congestion Control Algorithms

1. **Leaky Bucket Algorithm**:
   - Converts bursty incoming traffic into a **smooth, constant-rate outgoing stream**.
   - Modeled as a bucket with a small hole at the bottom. If input arrives faster than the leak rate, data accumulates in the bucket buffer. If the bucket overflows, incoming packets are dropped.
   - Used for strict traffic shaping where output rate must not exceed a set threshold.

2. **Token Bucket Algorithm**:
   - Tokens arrive into the bucket at a constant rate $r$. The bucket can hold up to $b$ tokens.
   - To transmit a packet, the sender must consume tokens corresponding to the packet size. This allows **controlled burstiness** up to the bucket capacity $b$.

3. **Choke Packets**:
   - When a router's queue utilization exceeds a threshold, it generates a control packet (choke packet) sent directly back to the source host commanding it to reduce its transmission rate.

4. **Random Early Detection (RED)**:
   - Proactive router queue management. The router monitors average queue length. When queue size exceeds a minimum threshold $Min_{th}$, the router randomly drops incoming packets *before* the buffer fills completely, forcing TCP senders to slow down gracefully via Fast Retransmit.

### TCP Congestion Control
TCP uses a **Congestion Window (cwnd)** to limit the amount of unacknowledged data in transit, making the effective window the minimum of the receiver's advertised window and the congestion window. It employs a self-clocking mechanism driven by ACKs.

1. **Additive Increase / Multiplicative Decrease (AIMD)**:
   - *Multiplicative Decrease*: TCP interprets packet loss (usually indicated by a timeout or triple duplicate ACKs) as a sign of congestion. When congestion occurs, TCP aggressively reduces its sending rate by halving the Congestion Window (e.g., if cwnd is 16 packets, it drops to 8).
   - *Additive Increase*: When the network is healthy and ACKs are arriving, TCP conservatively increases the Congestion Window by exactly 1 Maximum Segment Size (MSS) per Round Trip Time (RTT), resulting in a linear increase.
   - This creates a characteristic **"sawtooth"** pattern of bandwidth usage over time.

2. **Slow Start**:
   - Used when a connection initially starts or restarts after a severe timeout. Since AIMD's linear growth takes too long to reach network capacity from zero, TCP starts with a cwnd of 1 packet.
   - For every ACK received, cwnd increases by 1, effectively **doubling** the window size every RTT (exponential growth).
   - Once a threshold is reached or a packet is lost, it switches back to AIMD.

### Example
- **Flow Control vs Congestion Control Analogy**: 
  - *Flow Control* is like drinking from a firehose; you ask the person holding the hose to turn the pressure down so you don't choke. 
  - *Congestion Control* is like a freeway metering light; it restricts how many cars (packets) enter the highway to prevent a massive traffic jam (network collapse).
- **Leaky Bucket Analogy**: Pouring water into a funnel. You can dump a bucket of water in quickly (bursty traffic), but it only drips out the bottom at a steady, fixed rate (shaped traffic).

### Applications & Use Cases
- **Leaky/Token Bucket**: Used in ISP bandwidth throttling, API rate limiting, and policing Quality of Service (QoS) Service Level Agreements (SLAs).
- **TCP Congestion Control (AIMD/Slow Start)**: Used universally by web browsers, file transfers, and streaming services to dynamically share the global Internet bandwidth without causing congestive collapse.
- **Random Early Detection (RED)**: Configured on high-speed internet backbone routers to prevent "global synchronization" (where all TCP streams back off simultaneously when a router buffer overflows).

---

### Quality of Service (QoS) Architecture

**Quality of Service (QoS)** refers to network mechanisms used to guarantee performance requirements (throughput, delay, jitter, packet loss) for specific applications.

```
                             ┌────────────────────────────────────────┐
                             │       QUALITY OF SERVICE METRICS       │
                             └───────────────────┬────────────────────┘
                                                 │
        ┌──────────────────────┬─────────────────┴──────┬──────────────────────┐
        ▼                      ▼                        ▼                      ▼
┌──────────────┐       ┌──────────────┐         ┌──────────────┐       ┌──────────────┐
│  BANDWIDTH   │       │    DELAY     │         │    JITTER    │       │ PACKET LOSS  │
├──────────────┤       ├──────────────┤         ├──────────────┤       ├──────────────┤
│ Data rate in │       │ Time from    │         │ Variation in │       │ % of dropped │
│ bps or Mbps  │       │ Src to Dst   │         │ packet delay │       │ buffer frames│
└──────────────┘       └──────────────┘         └──────────────┘       └──────────────┘
```

#### 1. Techniques for Improving QoS
- **Overprovisioning**: Building excess link bandwidth so congestion rarely occurs.
- **Buffering**: Receiver buffers audio/video packets to smooth out delay variations (Jitter).
- **Packet Scheduling Algorithms**:
  - *FIFO (First-In, First-Out)*: Serves packets in arrival order.
  - *Fair Queueing (FQ)*: Maintains separate queues per flow, serving them round-robin.
  - *Weighted Fair Queueing (WFQ)*: Assigns priority weights to queues so high-priority flows (VoIP) receive a higher fraction of bandwidth.

#### 2. Differentiated Services (DiffServ) vs Integrated Services (IntServ)
- **Integrated Services (IntServ / RSVP)**:
  - Flow-based QoS model. Applications use **RSVP (Resource Reservation Protocol)** to reserve explicit bandwidth across all intermediate routers before transmitting. High state overhead per router (does not scale globally).
- **Differentiated Services (DiffServ / DSCP)**:
  - Class-based QoS model. Edge routers classify packets and tag the 6-bit **DSCP (Differentiated Services Code Point)** field in the IPv4 header. Core routers treat packets based on Per-Hop Behaviors (**EF - Expedited Forwarding** for low latency, **AF - Assured Forwarding** for guaranteed delivery).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Token Bucket Burst Duration & Rate Math
**Problem:** A Token Bucket has a capacity $b = 5 \text{ MB}$ and receives tokens at a rate $r = 10 \text{ Mbps}$. The maximum transmission speed of the network interface is $M = 50 \text{ Mbps}$. Calculate the maximum duration $S$ for which the host can transmit at the maximum speed $M$.
**Step-by-step Solution:**
1. **Formulate Burst Equation:**
   In time $S$, the maximum data transmitted is $M \times S$.
   This data comes from initial capacity $b$ plus new tokens generated during time $S$ ($r \times S$):
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
   - $t=0$: Initial tokens = 8MB. 12MB arrives. Transmits 8MB immediately in burst, remaining 4MB sent at 4MB/s.

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

2. **"Define Quality of Service (QoS). Explain IntServ (RSVP) vs DiffServ (DSCP)." [Dec 2019]**
   - **Solution:**
     - **QoS Metrics**: Bandwidth, Delay, Jitter, Packet Loss.
     - **IntServ (Integrated Services)**: Uses RSVP to make explicit end-to-end bandwidth reservations per flow. High state overhead on core routers.
     - **DiffServ (Differentiated Services)**: Classifies traffic at edge routers using 6-bit DSCP headers. Core routers prioritize packets based on Per-Hop Behaviors (EF / AF) without maintaining per-flow state.
