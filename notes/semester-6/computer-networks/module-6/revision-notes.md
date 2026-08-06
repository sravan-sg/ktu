# Module 6 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 6**: Transport Layer & Application Layer Protocols

---

## 🚀 Submodule 1: Transport Layer (TCP & UDP)

- **TCP Handshake**: `SYN` (Seq x) $\rightarrow$ `SYN-ACK` (Seq y, Ack x+1) $\rightarrow$ `ACK` (Seq x+1, Ack y+1).
- **TCP Congestion Control (AIMD)**: Slow Start (exponential growth to $ssthresh$), Congestion Avoidance (additive increase $+1$ per RTT), Fast Retransmit (triggered by 3 duplicate ACKs).
- **UDP vs TCP**: UDP = connectionless, 8B header, no ACKs, low delay; TCP = connection-oriented, 20B header, reliable stream.

---

## 🚀 Submodule 2: Application Layer Protocols

- **DNS**: Hierarchical resolution (Root $\rightarrow$ TLD $\rightarrow$ Authoritative). Iterative (local DNS queries each level) vs Recursive (cascading queries).
- **FTP**: Port 21 (Control connection) + Port 20 (Data connection). Out-of-band control allows terminating file transfers.
- **HTTP/1.0 vs HTTP/1.1**: HTTP/1.0 opens new TCP connection per object ($2 \text{ RTTs}$/object); HTTP/1.1 reuses persistent connection ($1 \text{ RTT}$/object).

---

## 🔢 3 Solved Numerical Micro-Examples

1. **TCP Window Throughput**: $rwnd = 64 \text{ KB} = 524,288 \text{ bits}$, $\text{RTT} = 100 \text{ ms}$. Throughput $= 524,288 / 0.1 = 5.24 \text{ Mbps}$.
2. **Persistent HTTP Load Time**: Page with 5 images. RTT = 10 ms. HTTP/1.0 $= 12 \text{ RTTs} = 120 \text{ ms}$; HTTP/1.1 $= 7 \text{ RTTs} = 70 \text{ ms}$.
3. **MIME Base64 Expansion**: 300 KB file $\rightarrow 300 \times (4/3) = 400 \text{ KB}$ (33.3% overhead).
