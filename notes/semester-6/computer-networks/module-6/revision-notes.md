# Module 6 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 6**: Transport Layer & Application Layer Protocols

---

## 🚀 Submodule 1: Transport Layer (UDP, TCP Header & Connection)

- **UDP vs TCP**:
  - *UDP*: Connectionless, unacknowledged, 8-byte fixed header (Src Port, Dst Port, Length, Checksum).
  - *TCP*: Connection-oriented, reliable byte stream, 20-byte base header.
- **TCP Segment Header (20B Base)**: Source Port (16b), Destination Port (16b), Sequence Number (32b), Acknowledgment Number (32b), Data Offset (4b), Flags (6b: URG, ACK, PSH, RST, SYN, FIN), Window Size (16b), Checksum (16b), Urgent Pointer (16b).
- **TCP Connection Management**:
  - *3-Way Handshake*: `SYN` ($\text{ISN}_A$) $\rightarrow$ `SYN-ACK` ($\text{ISN}_B, \text{ACK}=\text{ISN}_A+1$) $\rightarrow$ `ACK` ($\text{ACK}=\text{ISN}_B+1$).
  - *4-Way Teardown*: `FIN` $\rightarrow$ `ACK` $\rightarrow$ `FIN` $\rightarrow$ `ACK` $\rightarrow$ `TIME_WAIT` ($2 \times \text{MSL}$).

---

## 🚀 Submodule 2: TCP Flow & Congestion Control

- **Flow Control**: Sliding window where sender window $swnd = \min(cwnd, rwnd)$. Silly Window Syndrome prevented by Nagle's Algorithm (sender buffering) and Clark's Solution (receiver credit window updates).
- **Congestion Control Algorithms**:
  - *Slow Start*: $cwnd$ starts at 1 MSS and **doubles every RTT** ($cwnd = cwnd \times 2$) until $cwnd \ge ssthresh$.
  - *Congestion Avoidance*: $cwnd$ grows **linearly by 1 MSS per RTT** ($cwnd = cwnd + 1$).
  - *Fast Retransmit / Fast Recovery (TCP Reno)*: 3 duplicate ACKs trigger instant retransmit; sets $ssthresh = cwnd/2$, $cwnd = ssthresh + 3$, avoiding drop to 1 MSS.

---

## 🚀 Submodule 3: Application Protocols (FTP, DNS, SMTP, MIME, SNMP)

- **FTP (Ports 20/21)**: Out-of-band architecture; Control Connection (Port 21) vs Data Connection (Port 20). Active (`PORT`) vs Passive (`PASV`) modes.
- **DNS**: Hierarchical resolution (Root $\rightarrow$ TLD $\rightarrow$ Authoritative). Resource Records: `A` (IPv4), `AAAA` (IPv6), `CNAME` (alias), `MX` (Mail), `NS` (Nameserver), `PTR` (Reverse IP).
- **Electronic Mail (SMTP & MIME)**:
  - *SMTP*: Push protocol over TCP Port 25 sending 7-bit ASCII emails (`HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, `QUIT`).
  - *MIME Base64*: Groups 24 bits (3 bytes) into four 6-bit ASCII characters ($33.3\%$ overhead).
- **SNMP (UDP Ports 161/162)**: Architecture: Manager, Agent, SMI (ASN.1 structure), MIB (database). PDUs: `GetRequest`, `SetRequest`, `Trap` (unsolicited alarm).

---

## 🔢 3 Solved Numerical Micro-Examples

1. **TCP 3-Way Handshake Trace**: Client ISN $= 1000$, Server ISN $= 5000$.
   - SYN: `Seq = 1000`.
   - SYN-ACK: `Seq = 5000, Ack = 1001`.
   - ACK: `Seq = 1001, Ack = 5001`.
2. **MIME Base64 Overhead**: File size $= 600 \text{ KB}$. Encoded size $= 600 \times \frac{4}{3} = \mathbf{800 \text{ KB}}$.
3. **HTTP Iterative vs Persistent**: Page has 1 HTML + 4 images. RTT $= 10 \text{ ms}$.
   - Non-persistent HTTP/1.0: $2 + 4 \times 2 = 10 \text{ RTTs} = \mathbf{100 \text{ ms}}$.
   - Persistent HTTP/1.1 (no pipelining): $2 + 4 \times 1 = 6 \text{ RTTs} = \mathbf{60 \text{ ms}}$.
