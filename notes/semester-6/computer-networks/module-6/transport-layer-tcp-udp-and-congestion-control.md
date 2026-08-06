# Module 6 — Topic 1: Transport Layer: TCP Segment Header, Connection Management, Sliding Window & Congestion Control

> **Module 6**: Transport Layer & Application Layer Protocols  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Transport Layer** (Layer 4) provides process-to-process, end-to-end communication across networks using **Port Numbers** (16-bit identifiers).

---

### 1. UDP vs TCP Protocol Fundamentals
- **UDP (User Datagram Protocol)**:
  - Connectionless, lightweight, unreliable transport.
  - Fixed **8-byte header** (Source Port, Destination Port, Length, Checksum). No handshaking, no flow control, no congestion control.
  - Ideal for real-time applications (VoIP, DNS, Video Streaming, Online Gaming).
- **TCP (Transmission Control Protocol)**:
  - Connection-oriented, full-duplex, reliable byte stream transport.
  - Provides in-order delivery, flow control, error control, and congestion control.

---

### 2. TCP Segment Header Structure
```text
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |        Destination Port       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                     Acknowledgment Number                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Data |       |U|A|P|R|S|F|                                |
|Offset| Reserved|R|C|S|S|Y|I|           Window Size            |
| (4b) | (6b)  |G|K|H|T|N|N|                                |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Checksum           |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if any) + Padding                 |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```
- **Source & Destination Ports (16 bits each)**: Identifies sending and receiving processes.
- **Sequence Number (32 bits)**: Byte number of the first data byte in this segment.
- **Acknowledgment Number (32 bits)**: Next byte number expected from the sender (Cumulative ACK).
- **Data Offset / Header Length (4 bits)**: Number of 32-bit words in the TCP header (min = 5, i.e., 20 Bytes).
- **Control Flags (6 bits)**:
  - `URG`: Urgent Pointer field is valid.
  - `ACK`: Acknowledgment field is valid.
  - `PSH`: Receiver should push data to application immediately.
  - `RST`: Reset the connection.
  - `SYN`: Synchronize sequence numbers during connection establishment.
  - `FIN`: Finish / release connection.
- **Window Size (16 bits)**: Flow control credit advertised by receiver ($rwnd$).
- **Checksum (16 bits)**: Error detection over TCP header, payload, and IP pseudo-header.

---

### 3. TCP Connection Management & State Machine
```text
  Client (Active Open)                                Server (Passive Open)
           │                                                    │
  SYN_SENT │ 1. SYN (Seq=x)                                     │ LISTEN
           ├───────────────────────────────────────────────────►│ SYN_RCVD
           │ 2. SYN-ACK (Seq=y, Ack=x+1)                        │
 ESTABLISHED│◄───────────────────────────────────────────────────┤
           │ 3. ACK (Seq=x+1, Ack=y+1)                          │ ESTABLISHED
           ├───────────────────────────────────────────────────►│
```
- **3-Way Handshake (Establishment)**:
  1. Client sends `SYN` segment with Initial Sequence Number ($\text{ISN}_A$).
  2. Server responds with `SYN-ACK` segment ($\text{ISN}_B$, $\text{ACK} = \text{ISN}_A + 1$).
  3. Client sends `ACK` segment ($\text{ACK} = \text{ISN}_B + 1$). Connection established.
- **4-Way Teardown (Release)**:
  1. Active close party sends `FIN`.
  2. Passive party responds with `ACK`.
  3. Passive party sends its own `FIN`.
  4. Active party responds with `ACK` and enters **`TIME_WAIT`** state for $2 \times \text{MSL}$ (Maximum Segment Lifetime) to ensure final ACK reaches receiver before closing.

---

### 4. TCP Flow Control & Sliding Window
- **Bytes-Oriented Sliding Window**: Sender can transmit up to $swnd = \min(cwnd, rwnd)$ unacknowledged bytes.
- **Silly Window Syndrome**: Occurs when data is read in small increments, causing tiny 1-byte segments to be transmitted. Solved by **Nagle's Algorithm** (sender buffers data until 1 full MSS is accumulated or prior ACK arrives) and **Clark's Solution** (receiver delays advertising $rwnd$ until 1 MSS space is free).

---

### 5. TCP Congestion Control (AIMD Algorithm)
- **Slow Start**: $cwnd$ starts at 1 MSS and **doubles every RTT** ($cwnd = cwnd \times 2$) until $cwnd \ge ssthresh$.
- **Congestion Avoidance**: When $cwnd \ge ssthresh$, $cwnd$ grows **linearly by 1 MSS per RTT** ($cwnd = cwnd + 1$).
- **Fast Retransmit**: Upon receiving 3 duplicate ACKs, TCP retransmits the missing segment immediately without waiting for retransmission timer expiration.
- **Fast Recovery (TCP Reno)**: Upon 3 duplicate ACKs, sets $ssthresh = cwnd / 2$, $cwnd = ssthresh + 3$, and remains in Congestion Avoidance rather than dropping $cwnd$ to 1 MSS.

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
   - `Seq = 1000`, `Ack = 0`.
2. **Step 2 (SYN-ACK from Server):**
   - Flags: `SYN = 1`, `ACK = 1`
   - `Seq = 5000`, `Ack = 1001` (Acknowledges receipt of SYN 1000).
3. **Step 3 (ACK from Client):**
   - Flags: `SYN = 0`, `ACK = 1`
   - `Seq = 1001`, `Ack = 5001` (Connection Established!).
4. **Step 4 (First Data Segment - 100 Bytes from Client):**
   - `Seq = 1001`, `Ack = 5001`. Data byte range: 1001 to 1100.
   - Server responds with ACK: `Seq = 5001`, `Ack = 1101`.

### Example 2: TCP Congestion Window ($cwnd$) Progression Trace
**Problem:** A TCP connection has $ssthresh = 16 \text{ MSS}$. It starts in Slow Start ($cwnd = 1 \text{ MSS}$). Trace the value of $cwnd$ for 10 consecutive transmission rounds (RTTs), assuming no packet loss occurs.
**Step-by-step Solution:**
1. **Slow Start Phase ($cwnd < ssthresh$):**
   - RTT 1: $cwnd = 1 \text{ MSS}$
   - RTT 2: $cwnd = 2 \text{ MSS}$
   - RTT 3: $cwnd = 4 \text{ MSS}$
   - RTT 4: $cwnd = 8 \text{ MSS}$
   - RTT 5: $cwnd = 16 \text{ MSS}$ (Reaches $ssthresh = 16$).
2. **Congestion Avoidance Phase ($cwnd \ge ssthresh$):**
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
