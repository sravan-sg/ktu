# Module 2 — Topic 3: MAC Sublayer, IEEE 802 Standards & Devices

> **Module 2**: Data Link Layer & Medium Access Control  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
In broadcast networks, multiple hosts share a single transmission channel. The **Medium Access Control (MAC)** sublayer resolves channel contention:

1. **Random Access Protocols**:
   - **ALOHA**: Pure ALOHA allows stations to transmit immediately (vulnerable time $2T_t$, max efficiency $18.4\%$). Slotted ALOHA synchronizes time slots ($1T_t$, max efficiency $36.8\%$).
   - **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**: Used in Ethernet (IEEE 802.3). Station listens before speaking ("Carrier Sense"), transmits, and listens while transmitting to detect collisions ("Collision Detection"). Upon collision, aborts and executes **Binary Exponential Backoff**.
   - **CSMA/CA (Collision Avoidance)**: Used in Wi-Fi (IEEE 802.11). Avoids collisions using Inter-Frame Spaces (IFS), Random Backoff timers, and **RTS/CTS (Request-to-Send / Clear-to-Send)** handshakes to solve the **Hidden Station Problem**.

2. **IEEE 802 LAN Standards**:
   - **IEEE 802.3**: Ethernet (CSMA/CD, 10 Mbps to 10 Gbps+).
   - **IEEE 802.4**: Token Bus.
   - **IEEE 802.5**: Token Ring (Token passing protocol).
   - **IEEE 802.11**: Wireless LANs (802.11a/b/g/n/ac).
   - **IEEE 802.15**: Wireless Personal Area Networks (Bluetooth).

3. **Interconnection Devices**:
   - **Bridge / Switch (Layer 2)**: Learns MAC addresses dynamically, maintains MAC forwarding tables, isolates collision domains.
   - **Router (Layer 3)**: Routes packets between subnets based on IP addresses, isolates broadcast domains.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: CSMA/CD Minimum Frame Size Formula Derivation
**Problem:** What is the minimum frame size required for a 1 Gbps Ethernet LAN with a maximum cable length of 1 km? Signal speed in cable is $2 \times 10^8 \text{ m/s}$.
**Step-by-step Solution:**
1. **Rule for Collision Detection:** Transmission time $T_t$ must be at least twice the propagation delay $T_p$ ($T_t \ge 2T_p$).
2. **Calculate $T_p$:**
   $$T_p = \frac{1000 \text{ m}}{2 \times 10^8 \text{ m/s}} = 5 \times 10^{-6} \text{ s} = 5 \mu\text{s}$$
3. **Calculate Minimum $T_t$:**
   $$T_t = 2 \times T_p = 2 \times 5 \mu\text{s} = 10 \mu\text{s}$$
4. **Calculate Minimum Frame Size ($L_{\text{min}}$):**
   $$L_{\text{min}} = T_t \times \text{Bandwidth} = 10 \times 10^{-6} \text{ s} \times 10^9 \text{ bits/s} = 10,000 \text{ bits} = \mathbf{1,250 \text{ Bytes}}$$

### Example 2: Binary Exponential Backoff Trace
**Problem:** Two stations collide on an Ethernet network. Trace the backoff time options for both stations after their 3rd consecutive collision. If slot time is $51.2 \mu\text{s}$, what are the possible backoff delays?
**Step-by-step Solution:**
1. **Formula:** After $i$-th collision, station chooses random integer $k$ from range $[0, 2^i - 1]$.
2. **For 3rd Collision ($i = 3$):**
   $$k \in [0, 2^3 - 1] = [0, 7]$$
3. **Possible Backoff Times:**
   $$\text{Delay} = k \times \text{Slot Time} = k \times 51.2 \mu\text{s}$$
   Options: $0, 51.2, 102.4, 153.6, 204.8, 256.0, 307.2, 358.4 \mu\text{s}$.
4. **Collision Probability:** Probability that both choose same $k = 1/8 = 12.5\%$.

### Example 3: Pure ALOHA vs Slotted ALOHA Throughput
**Problem:** A channel of 56 kbps is shared by multiple stations using Pure ALOHA. Each station transmits 1,000-bit frames. What is the maximum channel throughput in frames/sec?
**Step-by-step Solution:**
1. **Pure ALOHA Throughput Formula:** $S = G e^{-2G}$.
2. **Maximum Throughput occurs at $G = 0.5$:**
   $$S_{\text{max}} = 0.5 \times e^{-1} \approx 0.184 \text{ (18.4\%)}$$
3. **Calculate Maximum Bits/sec:**
   $$\text{Rate} = 0.184 \times 56,000 \text{ bps} = 10,304 \text{ bps}$$
4. **Calculate Throughput in Frames/sec:**
   $$\text{Frames/sec} = \frac{10,304 \text{ bps}}{1000 \text{ bits/frame}} = \mathbf{10.3 \text{ frames/sec}}$$

---

## 3. Previous Year Questions & Solutions

1. **"Explain CSMA/CD protocol. How does it handle collisions?" [May 2019, Sept 2020]**
   - **Solution:**
     **CSMA/CD Steps:**
     1. Station listens to medium (Carrier Sense). If busy, waits; if idle, starts transmitting.
     2. While transmitting, listens for voltage spikes (Collision Detection).
     3. If collision detected, transmits a 32-bit **Jam Signal** to notify all nodes, aborts transmission.
     4. Executes **Binary Exponential Backoff**: Picks random $k \in [0, 2^i - 1]$, waits $k \times \text{Slot Time}$, then retries up to 16 attempts.

2. **"Explain Hidden and Exposed Station problems in Wireless LANs. How does RTS/CTS resolve it?" [Dec 2019]**
   - **Solution:**
     - **Hidden Station Problem:** Station A and C cannot hear each other, but both can hear B. If A and C transmit to B simultaneously, collisions occur at B.
     - **Exposed Station Problem:** Station B transmits to A. Station C wants to transmit to D. C hears B and wrongly assumes medium is busy, unnecessarily delaying transmission.
     - **RTS/CTS Solution:** A sends Request-to-Send (RTS) to B. B replies with Clear-to-Send (CTS) broadcast. C hears CTS and defers transmission, preventing collisions at B.
