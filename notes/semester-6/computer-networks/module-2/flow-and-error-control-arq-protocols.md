# Module 2 — Topic 2: Flow & Error Control ARQ Protocols

> **Module 2**: Data Link Layer & Medium Access Control  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
To guarantee reliable data delivery across noisy channels, the Data Link Layer uses **Automatic Repeat reQuest (ARQ)** protocols:

1. **Stop-and-Wait ARQ**:
   - Sender transmits 1 frame, starts a timer, and waits for an Acknowledgement (ACK).
   - Extremely simple, but inefficient over high Bandwidth-Delay Product (BDP) links (channel remains idle while waiting for ACK).

2. **Go-Back-N (GBN) ARQ**:
   - Sliding window protocol allowing sender to transmit up to $W_S = 2^k - 1$ frames without waiting for ACK.
   - Receiver has window size $W_R = 1$ (accepts frames strictly in-order).
   - If frame $i$ is lost/corrupted, receiver discards all subsequent frames $i+1, i+2$. Sender timer expires and **retransmits all frames from $i$ onwards** (Goes back $N$).

3. **Selective Repeat (SR) ARQ**:
   - Both sender and receiver have window sizes $W_S = W_R = 2^{k-1}$.
   - Receiver accepts out-of-order frames within its window and stores them in a buffer.
   - Sender retransmits **only the specific frame that was lost/damaged** (Selective NAK).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Efficiency Comparison (Stop-and-Wait vs Sliding Window)
**Problem:** A 1000-bit frame is transmitted over a 1 Mbps link with a one-way propagation delay of 24.5 ms. Calculate protocol efficiency $\eta$ for (a) Stop-and-Wait ARQ, and (b) Go-Back-N ARQ with window size $W_S = 15$.
**Step-by-step Solution:**
1. **Calculate Transmission Delay ($T_t$):**
   $$T_t = \frac{\text{Frame Size}}{\text{Bandwidth}} = \frac{1000 \text{ bits}}{10^6 \text{ bits/s}} = 0.001 \text{ s} = 1 \text{ ms}$$
2. **Calculate Propagation Delay ($T_p$):** $T_p = 24.5 \text{ ms}$.
3. **Calculate Parameter $a$:**
   $$a = \frac{T_p}{T_t} = \frac{24.5 \text{ ms}}{1 \text{ ms}} = 24.5$$
4. **Efficiency of Stop-and-Wait ARQ ($\eta_{\text{SW}}$):**
   $$\eta_{\text{SW}} = \frac{1}{1 + 2a} = \frac{1}{1 + 2(24.5)} = \frac{1}{50} = 0.02 = \mathbf{2\%}$$
5. **Efficiency of Go-Back-N ARQ ($\eta_{\text{GBN}}$):**
   $$\eta_{\text{GBN}} = \min\left(1, \frac{W_S}{1 + 2a}\right) = \min\left(1, \frac{15}{50}\right) = 0.30 = \mathbf{30\%}$$

### Example 2: Maximum Window Size Derivation for GBN vs SR
**Problem:** A channel uses $m = 3$ bits for sequence numbers. Calculate the maximum sender window size $W_S$ for (a) Go-Back-N ARQ, and (b) Selective Repeat ARQ to avoid sequence number ambiguity.
**Step-by-step Solution:**
1. **Total Distinct Sequence Numbers:** $2^m = 2^3 = 8$ (numbers 0 to 7).
2. **Go-Back-N Window Constraint:**
   $$W_S \le 2^m - 1 = 8 - 1 = \mathbf{7}$$
   If $W_S = 8$, receiver cannot distinguish between a new frame 0 and duplicate frame 0 if all ACKs are lost.
3. **Selective Repeat Window Constraint:**
   $$W_S + W_R \le 2^m \implies W_S = W_R \le 2^{m-1} = 2^{3-1} = \mathbf{4}$$
   If $W_S > 4$, overlapping sender/receiver windows cause old data frames to be accepted as new data.

### Example 3: Link Utilization Optimization
**Problem:** What minimum window size $W$ is required to achieve $100\%$ link utilization for a 10 Mbps satellite link ($RTT = 500 \text{ ms}$) transmitting 8,000-bit frames?
**Step-by-step Solution:**
1. **Calculate Transmission Delay ($T_t$):**
   $$T_t = \frac{8000 \text{ bits}}{10 \times 10^6 \text{ bits/s}} = 0.0008 \text{ s} = 0.8 \text{ ms}$$
2. **Calculate $1 + 2a$:**
   $$1 + 2a = \frac{T_t + RTT}{T_t} = \frac{0.8 \text{ ms} + 500 \text{ ms}}{0.8 \text{ ms}} = \frac{500.8}{0.8} = 626$$
3. **Required Window Size:**
   $$W \ge 626 \text{ frames}$$
   To achieve 100% throughput, the sender window must hold at least **626 frames**.

---

## 3. Previous Year Questions & Solutions

1. **"Explain Go-Back-N ARQ and Selective Repeat ARQ protocols with neat diagrams. Compare their performance." [April 2018, July 2021]**
   - **Solution:**
     - **Go-Back-N:** Sender window $W_S = 2^m - 1$, receiver window $W_R = 1$. Upon frame loss, receiver discards out-of-order frames. Sender retransmits all frames from lost frame onwards. Simple receiver implementation (no buffering).
     - **Selective Repeat:** Sender window $W_S = 2^{m-1}$, receiver window $W_R = 2^{m-1}$. Receiver buffers out-of-order frames and sends NAK for missing frame. Sender retransmits only lost frame. Higher throughput over noisy channels, but requires complex buffer management.

2. **"Derive the efficiency of Stop-and-Wait ARQ protocol." [Dec 2019]**
   - **Solution:**
     Total time to transmit 1 frame and receive ACK $T_{\text{total}} = T_t + T_p + T_{\text{ack}} + T_p$. Assuming $T_{\text{ack}} \approx 0$, $T_{\text{total}} = T_t + 2T_p$.
     Useful time spent = $T_t$.
     $$\text{Efficiency } \eta = \frac{\text{Useful Time}}{\text{Total Time}} = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2(T_p/T_t)} = \frac{1}{1 + 2a}$$
