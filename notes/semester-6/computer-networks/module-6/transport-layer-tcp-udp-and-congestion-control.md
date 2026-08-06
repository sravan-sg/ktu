# Module 6 — Topic 1: Transport Layer (TCP, UDP & TCP Congestion Control)

> **Module 6**: Transport Layer & Application Layer Protocols  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Transport Layer** (Layer 4) provides end-to-end process-to-process communication between software applications using **Port Numbers**:

1. **UDP (User Datagram Protocol)**:
   - Connectionless, lightweight, unreliable transport.
   - Fixed 8-byte header (Source Port, Destination Port, Length, Checksum). No handshaking, no flow/congestion control.
   - Ideal for real-time applications (VoIP, DNS, Video Streaming, Gaming).

2. **TCP (Transmission Control Protocol)**:
   - Connection-oriented, full-duplex, reliable byte stream transport.
   - 20-byte base header (Sequence Number, ACK Number, Flags: SYN, ACK, FIN, RST, PSH, URG, Window Size, Checksum).
   - **3-Way Handshake**: (1) `SYN` $\rightarrow$ (2) `SYN-ACK` $\rightarrow$ (3) `ACK`.
   - **4-Way Connection Teardown**: `FIN` $\rightarrow$ `ACK` $\rightarrow$ `FIN` $\rightarrow$ `ACK`.

3. **TCP Congestion Control (AIMD Algorithm)**:
   - **Slow Start**: Congestion Window ($cwnd$) starts at 1 MSS and **doubles every RTT** (exponential growth) until reaching $ssthresh$.
   - **Congestion Avoidance**: $cwnd$ grows **linearly by 1 MSS per RTT** (Additive Increase).
   - **Fast Retransmit / Fast Recovery**: Upon receiving 3 duplicate ACKs, TCP retransmits missing segment without waiting for timeout, sets $ssthresh = cwnd / 2$, and enters Fast Recovery.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: TCP 3-Way Handshake & Sequence Number Math
**Problem:** Client A initiates a TCP connection to Server B (Port 80).
- Client A chooses Initial Sequence Number $\text{ISN}_A = 1000$.
- Server B chooses Initial Sequence Number $\text{ISN}_B = 5000$.
Trace sequence and ACK numbers for the 3-way handshake and the first data segment (100 Bytes) sent by Client A.
**Step-by-step Solution:**
1. **Step 1 (SYN from Client):**
   - Flags: `SYN = 1`, `ACK = 0`
   - `Seq = 1000`, `Ack = 0`. (Consumes 1 sequence number space).
2. **Step 2 (SYN-ACK from Server):**
   - Flags: `SYN = 1`, `ACK = 1`
   - `Seq = 5000`, `Ack = 1001` (Acknowledges receipt of SYN 1000).
3. **Step 3 (ACK from Client):**
   - Flags: `SYN = 0`, `ACK = 1`
   - `Seq = 1001`, `Ack = 5001` (Connection Established!).
4. **Step 4 (First Data Segment - 100 Bytes from Client):**
   - `Seq = 1001`, `Ack = 5001`. Data range: byte 1001 to byte 1100.
   - Server responds with ACK: `Seq = 5001`, `Ack = 1101` (Expects byte 1101 next).

### Example 2: TCP Congestion Window ($cwnd$) Progression Trace
**Problem:** A TCP connection has $ssthresh = 16 \text{ MSS}$. It starts in Slow Start ($cwnd = 1 \text{ MSS}$). Trace the value of $cwnd$ for 10 consecutive transmission rounds (RTTs), assuming no packet loss occurs.
**Step-by-step Solution:**
1. **Slow Start Phase ($cwnd < ssthresh$):** Doubles every RTT.
   - RTT 1: $cwnd = 1 \text{ MSS}$
   - RTT 2: $cwnd = 2 \text{ MSS}$
   - RTT 3: $cwnd = 4 \text{ MSS}$
   - RTT 4: $cwnd = 8 \text{ MSS}$
   - RTT 5: $cwnd = 16 \text{ MSS}$ (Reaches $ssthresh = 16$).
2. **Congestion Avoidance Phase ($cwnd \ge ssthresh$):** Increases by 1 MSS per RTT.
   - RTT 6: $cwnd = 17 \text{ MSS}$
   - RTT 7: $cwnd = 18 \text{ MSS}$
   - RTT 8: $cwnd = 19 \text{ MSS}$
   - RTT 9: $cwnd = 20 \text{ MSS}$
   - RTT 10: $cwnd = 21 \text{ MSS}$

### Example 3: TCP Maximum Throughput & Buffer Sizing
**Problem:** Calculate the maximum achievable TCP throughput over a path with $\text{RTT} = 100 \text{ ms}$ if the TCP Receiver Window Size ($rwnd$) is capped at $64 \text{ KB}$ ($65,536 \text{ Bytes}$).
**Step-by-step Solution:**
1. **Throughput Formula:**
   $$\text{Max Throughput} = \frac{\text{Receiver Window Size } (rwnd)}{\text{RTT}}$$
2. **Convert Values:**
   - $rwnd = 65,536 \text{ Bytes} = 65,536 \times 8 = 524,288 \text{ bits}$.
   - $\text{RTT} = 0.1 \text{ seconds}$.
3. **Calculate Throughput:**
   $$\text{Max Throughput} = \frac{524,288 \text{ bits}}{0.1 \text{ s}} = 5,242,880 \text{ bps} \approx \mathbf{5.24 \text{ Mbps}}$$
4. **Insight:** Even on a 1 Gbps physical link, TCP throughput is bottlenecked at 5.24 Mbps due to the 64 KB window limit unless TCP Window Scaling (RFC 1323) is enabled.

---

## 3. Previous Year Questions & Solutions

1. **"Explain TCP 3-Way Handshake for connection establishment and 4-way teardown." [May 2019, July 2021]**
   - **Solution:**
     **Handshake:** Client sends `SYN` (Seq x). Server responds with `SYN-ACK` (Seq y, Ack x+1). Client sends `ACK` (Seq x+1, Ack y+1). Connection is established.
     **Teardown:** Active party sends `FIN` (Seq a). Passive party sends `ACK` (Ack a+1). Passive party then sends `FIN` (Seq b). Active party responds with `ACK` (Ack b+1) and waits for TIME_WAIT duration (2 MSL) before closing socket.

2. **"Explain TCP Congestion Control mechanism (Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery)." [Dec 2019]**
   - **Solution:**
     - **Slow Start:** $cwnd$ starts at 1 MSS and doubles every RTT ($cwnd = cwnd \times 2$) until $cwnd = ssthresh$.
     - **Congestion Avoidance:** When $cwnd \ge ssthresh$, $cwnd$ increases linearly by 1 MSS per RTT ($cwnd = cwnd + 1$).
     - **Timeout Event:** $ssthresh$ set to $cwnd/2$, $cwnd$ reset to 1 MSS, restarts in Slow Start.
     - **Fast Retransmit / Fast Recovery:** Upon 3 duplicate ACKs, retransmits lost segment, sets $ssthresh = cwnd/2$, $cwnd = ssthresh + 3$, enters Fast Recovery without dropping to 1 MSS.
