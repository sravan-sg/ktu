# Module 2 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 2**: Data Link Layer & Medium Access Control

---

## 🚀 Submodule 1: Framing, CRC & HDLC

- **Bit Stuffing**: Insert a `0` after 5 consecutive `1`s in data. Receiver strips `0` after 5 ones.
- **CRC Remainder**: Divide data padded with $r$ zeros by generator $G$ of length $r+1$ using XOR modulo-2 division. Remainder = CRC.
- **HDLC Control Field**: I-frame (`0...`), S-frame (`10...` for RR, REJ, RNR), U-frame (`11...` for SABM, UA, DISC).

---

## 🚀 Submodule 2: ARQ Protocols & Window Math

- **Stop-and-Wait ARQ Efficiency**: $\eta = \frac{1}{1 + 2a}$, where $a = T_p / T_t$.
- **Go-Back-N (GBN)**: $W_S = 2^m - 1$, $W_R = 1$. Discards out-of-order frames. Retransmits from lost frame onwards.
- **Selective Repeat (SR)**: $W_S = W_R = 2^{m-1}$. Buffers out-of-order frames. Retransmits *only* lost frame.

---

## 🚀 Submodule 3: MAC Protocols & Ethernet

- **CSMA/CD Condition**: $T_t \ge 2T_p \implies L_{\text{min}} = 2 T_p \times \text{Bandwidth}$.
- **Binary Exponential Backoff**: After $i$-th collision, select random $k \in [0, 2^i - 1]$, wait $k \times \text{Slot Time}$.
- **CSMA/CA & RTS/CTS**: Resolves Hidden Station Problem in Wireless LANs (IEEE 802.11).

---

## 🔢 3 Solved Numerical Micro-Examples

1. **CSMA/CD Min Frame**: $T_p = 10 \mu\text{s}$, Bandwidth $100 \text{ Mbps}$. $L_{\text{min}} = 2 \times 10 \mu\text{s} \times 10^8 \text{ bps} = 2000 \text{ bits} = 250 \text{ Bytes}$.
2. **GBN Window**: For 4-bit sequence numbers ($m=4$), $W_S = 2^4 - 1 = 15$.
3. **Pure vs Slotted ALOHA Max Efficiency**: Pure $= 18.4\%$; Slotted $= 36.8\%$.
