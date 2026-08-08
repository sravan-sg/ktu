# Module 2 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 2**: Data Link Layer & Medium Access Control

---

## 🚀 Submodule 1: Framing, CRC & HDLC Protocol

- **Framing Methods**:
  - *Character Count*: Uses count byte (fragile to error).
  - *Byte Stuffing*: Prepends `DLE` byte before payload control bytes (`DLE STX`, `DLE ETX`).
  - *Bit Stuffing*: Inserts `0` bit after any 5 consecutive `1`s in payload to avoid flag `01111110` collision.
- **CRC Error Detection**: Generator polynomial $G(x)$ of degree $r$. Appends $r$ zeros, divides by $G(x)$ modulo-2 (XOR). Remainder $R$ is appended to data. Remainder 0 at receiver = clean frame.
- **HDLC Frames**: Bit-oriented. 3 frame types:
  - *I-frame*: Information transmission + piggybacked ACKs ($N(S), N(R)$).
  - *S-frame*: Supervisory controls (`RR`, `RNR`, `REJ`, `SREJ`).
  - *U-frame*: Unnumbered link control (`SABM`, `DISC`, `UA`).

---

## 🚀 Submodule 2: Flow Control ARQ Protocols

- **Stop-and-Wait ARQ**: $W_S = 1, W_R = 1$. Sends 1 frame, waits for ACK. Efficiency $\eta = \frac{1}{1 + 2a}$ where $a = T_p / T_t$.
- **Go-Back-N ARQ**: $W_S = 2^m - 1, W_R = 1$. Transmits up to $W_S$ frames without ACK. Discards out-of-order frames. On timeout, retransmits ALL unacknowledged frames from lost frame onward. Efficiency $\eta = \frac{W_S}{1 + 2a}$.
- **Selective Repeat ARQ**: $W_S = W_R = 2^{m-1}$. Transmits up to $W_S$ frames. Buffers out-of-order frames. Retransmits ONLY the single lost frame via NAK.

---

## 🚀 Submodule 3: MAC Standards & Interconnection Devices

- **IEEE 802 Standards**:
  - *802.3 Ethernet*: CSMA/CD 1-persistent binary exponential backoff ($2^k - 1$).
  - *802.4 Token Bus*: Physical bus, logical token ring.
  - *802.5 Token Ring*: Physical ring, token passing protocol.
  - *802.11 Wi-Fi*: CSMA/CA (Collision Avoidance) with RTS/CTS to solve Hidden/Exposed Terminal problems.
  - *802.15 Bluetooth*: WPAN 2.4 GHz FHSS. Piconet (1 Master + up to 7 active Slaves), Scatternet (interconnected Piconets).
- **Layer 2 Switches**: Connect LAN segments. Uses Backward Learning to populate MAC table and Spanning Tree Protocol (STP IEEE 802.1D) to break Layer 2 loops.

---

## 🔢 3 Solved Numerical Micro-Examples

1. **Bit Stuffing**: Data `01111110` $\rightarrow$ After 5 ones, insert `0` $\rightarrow$ Stuffed data: `011111010`.
2. **Stop-and-Wait Efficiency**: Frame size $1000 \text{ B}$ ($8000 \text{ b}$), $R = 1 \text{ Mbps} \implies T_t = 8 \text{ ms}$. Propagation delay $T_p = 4 \text{ ms}$. $a = 4/8 = 0.5$.
   $$\eta = \frac{1}{1 + 2(0.5)} = \frac{1}{2} = \mathbf{50\%}$$
3. **Selective Repeat Max Window**: Sequence bits $m = 4$. $W_S = W_R = 2^{4-1} = 2^3 = \mathbf{8 \text{ frames}}$.
