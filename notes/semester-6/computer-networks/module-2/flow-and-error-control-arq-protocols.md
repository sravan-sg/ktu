# Module 2 — Topic 2: Flow Control and ARQ Techniques (Stop-and-Wait, Go-Back-N, Selective Repeat)

> **Module 2**: Data Link Layer & Medium Access Control  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
To prevent a fast sender from overflowing a slow receiver's buffer and to recover from lost/corrupted frames over noisy physical links, the Data Link Layer implements **Flow and Error Control ARQ (Automatic Repeat reQuest)** protocols.

---

### Comparison of ARQ Protocols

```
  STOP-AND-WAIT ARQ                GO-BACK-N ARQ               SELECTIVE REPEAT ARQ
  ┌───────────────┐              ┌───────────────┐              ┌───────────────┐
  │ Sender Ws = 1 │              │ Sender Ws = 2ⁿ-1             │ Sender Ws = 2ⁿ⁻¹             │
  │ Recv Wr = 1   │              │ Recv Wr = 1   │              │ Recv Wr = 2ⁿ⁻¹             │
  └───────────────┘              └───────────────┘              └───────────────┘
  • Sends 1 frame,               • Sends up to Ws               • Sends up to Ws
    waits for ACK                  frames without ACK             frames without ACK
  • Very low                     • Discards out-of-             • Buffers out-of-order
    efficiency                     order frames                   frames; NACKs only
  • Efficiency =                 • Efficiency =                 • Efficiency =
    1 / (1 + 2a)                   Ws / (1 + 2a)                  Ws / (1 + 2a)
```

#### 1. Stop-and-Wait ARQ
- **Operation**: Sender transmits 1 frame, starts a retransmission timer, and freezes until an ACK arrives. If timer expires, retransmits.
- **Window Sizes**: Sender Window $W_S = 1$, Receiver Window $W_R = 1$.
- **Sequence Numbers**: 1-bit sequence numbers ($0$ and $1$).
- **Efficiency ($\eta$)**:
  $$\eta = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2a} \quad \text{where } a = \frac{T_p}{T_t}$$
  In high Bandwidth-Delay Product (BDP) networks ($a \gg 1$), efficiency drops near $0\%$.

#### 2. Go-Back-N ARQ
- **Operation**: Sender can transmit up to $W_S$ frames without waiting for an ACK. Receiver accepts frames strictly **in sequence**; any out-of-order frame is discarded. If frame $k$ times out, sender retransmits **all unacknowledged frames from $k$ onwards** ("Go Back N").
- **Window Sizes**: $W_S = 2^m - 1$ (for $m$-bit sequence numbers), $W_R = 1$.
- **Efficiency ($\eta$)**:
  $$\eta = \frac{W_S}{1 + 2a} \quad \text{for } W_S < 1 + 2a$$
  If $W_S \ge 1 + 2a$, efficiency reaches $100\%$.

#### 3. Selective Repeat ARQ
- **Operation**: Sender transmits up to $W_S$ frames. Receiver maintains a receiver window $W_R > 1$ and **buffers out-of-order frames**. Receiver sends a **NAK (Negative ACK)** specifically for the missing frame. Sender retransmits **only the single lost frame**.
- **Window Sizes**: $W_S = W_R = 2^{m-1}$ (to prevent receiver window overlap ambivalence).
- **Efficiency ($\eta$)**:
  $$\eta = \frac{W_S}{1 + 2a} \quad (\text{Maximum link utilization with minimal retransmission overhead})$$

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Stop-and-Wait ARQ Efficiency Calculation
**Problem:** A 1,000-byte frame is transmitted over a 1,000 km optical fiber link ($2 \times 10^8 \text{ m/s}$) at a bit rate of $R = 1 \text{ Mbps}$. Calculate:
(a) Transmission time $T_t$, (b) Propagation delay $T_p$, (c) Parameter $a$, and (d) Protocol efficiency $\eta$.
**Step-by-step Solution:**
1. **Transmission Time ($T_t$):**
   $$T_t = \frac{\text{Frame Size}}{\text{Bandwidth}} = \frac{1000 \times 8 \text{ bits}}{10^6 \text{ bps}} = 8 \times 10^{-3} \text{ s} = 8 \text{ ms}$$
2. **Propagation Delay ($T_p$):**
   $$T_p = \frac{\text{Distance}}{\text{Speed}} = \frac{10^6 \text{ m}}{2 \times 10^8 \text{ m/s}} = 5 \times 10^{-3} \text{ s} = 5 \text{ ms}$$
3. **Calculate Parameter $a$:**
   $$a = \frac{T_p}{T_t} = \frac{5 \text{ ms}}{8 \text{ ms}} = 0.625$$
4. **Calculate Efficiency ($\eta$):**
   $$\eta = \frac{1}{1 + 2a} = \frac{1}{1 + 2(0.625)} = \frac{1}{1 + 1.25} = \frac{1}{2.25} = 0.4444 \quad (\mathbf{44.44\%})$$

### Example 2: Go-Back-N Window Size Optimization
**Problem:** A satellite channel has a bandwidth of $R = 10 \text{ Mbps}$ and a Round-Trip Time $\text{RTT} = 500 \text{ ms}$. Frame size is 2,000 Bytes ($16,000 \text{ bits}$).
(a) Calculate $T_t$ and parameter $a$.
(b) Determine the minimum sender window size $W_S$ required to achieve 100% link utilization.
(c) How many sequence number bits $m$ are required for Go-Back-N ARQ?
**Step-by-step Solution:**
1. **Calculate $T_t$ and $a$:**
   $$T_t = \frac{16,000 \text{ bits}}{10 \times 10^6 \text{ bps}} = 1.6 \text{ ms}$$
   $$T_p = \frac{\text{RTT}}{2} = \frac{500 \text{ ms}}{2} = 250 \text{ ms}$$
   $$a = \frac{T_p}{T_t} = \frac{250}{1.6} = 156.25$$
2. **Minimum Window Size for 100% Utilization:**
   $$W_S \ge 1 + 2a = 1 + 2(156.25) = 1 + 312.5 = \mathbf{314 \text{ frames}}$$
3. **Sequence Number Bits ($m$):**
   For Go-Back-N, $W_S = 2^m - 1 \ge 314 \implies 2^m \ge 315 \implies m = \mathbf{9 \text{ bits}} \quad (2^9 = 512)$.

### Example 3: Selective Repeat Window Ambiguity Proof
**Problem:** Why must the maximum window size in Selective Repeat ARQ satisfy $W_S \le 2^{m-1}$ for $m$-bit sequence numbers? Show what happens if $W_S = 7$ for $m = 3$ bits.
**Step-by-step Solution:**
1. Sequence number space for $m=3$ is $0$ to $7$ (size $8$).
2. If $W_S = 7$ and $W_R = 7$:
   - Sender transmits frames $0, 1, 2, 3, 4, 5, 6$.
   - Receiver receives all 7 frames, sends ACKs $0-6$, and slides its window to expect frames $7, 0, 1, 2, 3, 4, 5$.
   - If ALL 7 ACKs are lost in transit, sender times out and retransmits frame $0$.
3. **Ambiguity at Receiver:**
   - Receiver receives retransmitted frame $0$. Receiver cannot distinguish whether frame $0$ is a **retransmission of old frame 0** or a **brand new frame 0**!
4. **Conclusion:** Setting $W_S = W_R = 2^{m-1} = 4$ ensures no overlap between old and new window spaces.

---

## 3. Previous Year Questions & Solutions

1. **"Derive the efficiency formula for Stop-and-Wait ARQ." [April 2018]**
   - **Solution:**
     Useful time $= T_t$. Total cycle time $= T_t + 2T_p + T_{\text{proc}} + T_{\text{ack}}$.
     Assuming negligible processing and ACK transmission times:
     $$\eta = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2(T_p / T_t)} = \frac{1}{1 + 2a}$$

2. **"Differentiate between Go-Back-N ARQ and Selective Repeat ARQ." [May 2019, July 2021]**
   - **Solution:**
     | Feature | Go-Back-N ARQ | Selective Repeat ARQ |
     | :--- | :--- | :--- |
     | **Sender Window ($W_S$)** | $2^m - 1$ | $2^{m-1}$ |
     | **Receiver Window ($W_R$)** | 1 (Discards out-of-order frames) | $2^{m-1}$ (Buffers out-of-order frames) |
     | **Retransmission Scope** | Retransmits lost frame AND all subsequent frames | Retransmits ONLY the single lost frame |
     | **ACK Types** | Cumulative ACKs | Cumulative ACKs & Selective NAKs |
     | **Buffer Overhead** | Low (Receiver needs 1 frame buffer) | High (Receiver needs $W_R$ frame buffers) |
