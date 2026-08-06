# Module 2 — Topic 3: MAC Sublayer, IEEE 802 Standards & Devices

> **Module 2**: Data Link Layer & Medium Access Control  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
In broadcast networks, multiple hosts share a single transmission channel. The **Medium Access Control (MAC)** sublayer resolves channel contention:

#### 1. Random Access Protocols
- **ALOHA**: Pure ALOHA transmits immediately (vulnerable time $2T_t$, max efficiency $18.4\%$). Slotted ALOHA synchronizes time slots ($1T_t$, max efficiency $36.8\%$).
- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**: Used in wired Ethernet (IEEE 802.3). Station listens before speaking ("Carrier Sense"), transmits, and listens while transmitting to detect collisions. Upon collision, aborts, transmits jam signal, and executes **Binary Exponential Backoff**.
- **CSMA/CA (Collision Avoidance)**: Used in Wireless LANs (IEEE 802.11). Avoids collisions using Inter-Frame Spaces (IFS), Random Backoff timers, and **RTS/CTS (Request-to-Send / Clear-to-Send)** handshakes to solve the **Hidden Station Problem** and **Exposed Station Problem**.

---

#### 2. IEEE 802 LAN/MAN Standards & Wireless Protocols
- **IEEE 802.3**: Ethernet (CSMA/CD, 10 Mbps Fast/Gigabit/10GbE).
- **IEEE 802.4 & 802.5**: Token Bus and Token Ring (Token passing deterministic protocol).
- **IEEE 802.11**: Wireless LANs (802.11a/b/g/n/ac/ax Wi-Fi).
- **IEEE 802.15 (Bluetooth / WPAN)**: Wireless Personal Area Networks. Operates in 2.4 GHz ISM band using Frequency Hopping Spread Spectrum (FHSS). 
  - **Piconet**: Consists of 1 Master node and up to 7 Active Slave nodes.
  - **Scatternet**: Interconnected Piconets sharing bridge nodes.
- **Point-to-Point Protocol (PPP)**: Data link protocol used over direct serial links.
  - **LCP (Link Control Protocol)**: Negotiates link options, authentication (PAP/CHAP), and compression.
  - **NCP (Network Control Protocol)**: Negotiates network-layer configurations (IP address assignment).

---

#### 3. Interconnection Devices & Spanning Tree Protocol
- **Bridge / Switch (Layer 2)**:
  - **Backward Learning Algorithm**: Inspects source MAC address of incoming frames to build MAC address forwarding table automatically.
  - **Forwarding & Filtering**: If destination MAC is in table on same port, frame is dropped (filtered). If on different port, forwarded. If unknown MAC, flooded to all ports except source.
  - **Spanning Tree Protocol (STP / IEEE 802.1D)**: Prevents broadcast storms and infinite loops in redundant switch topologies by disabling redundant links to form a logical loop-free tree.
- **Router (Layer 3)**: Routes packets between subnets based on IP addresses, isolates broadcast domains.

---

### Real-World Example
Think of a switch like a smart mailroom clerk:
- When a new letter arrives from Room 101 signed by "Alice", the clerk writes down: `Alice -> Room 101` (Backward Learning).
- When a letter arrives addressed to "Bob", the clerk checks the lookup table. If Bob's room is known (`Bob -> Room 105`), the letter goes straight to Room 105 (Filtering & Forwarding). If Bob is unknown, the clerk shouts down every hallway asking for Bob (Flooding).

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

### Example 3: Backward Learning Algorithm Trace for Layer 2 Switch
**Problem:** A 4-port switch with an empty MAC table receives the following sequence of Ethernet frames:
1. Frame from MAC `A` on Port 1 to MAC `B`.
2. Frame from MAC `C` on Port 3 to MAC `A`.
3. Frame from MAC `B` on Port 2 to MAC `C`.
Trace the MAC table after each step and state which ports receive forwarded frames.
**Step-by-step Solution:**
1. **Frame 1 (`A` -> `B` on Port 1):**
   - *Learns:* `A` is on Port 1. MAC Table: `{A: Port 1}`.
   - *Destination `B` is unknown:* Floods frame to Ports 2, 3, and 4.
2. **Frame 2 (`C` -> `A` on Port 3):**
   - *Learns:* `C` is on Port 3. MAC Table: `{A: Port 1, C: Port 3}`.
   - *Destination `A` is known (Port 1):* Forwards frame **only** to Port 1 (Filtered on Ports 2 & 4).
3. **Frame 3 (`B` -> `C` on Port 2):**
   - *Learns:* `B` is on Port 2. MAC Table: `{A: Port 1, C: Port 3, B: Port 2}`.
   - *Destination `C` is known (Port 3):* Forwards frame **only** to Port 3.

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

3. **"Explain Point-to-Point Protocol (PPP) and LCP/NCP negotiation." [April 2018]**
   - **Solution:**
     - **PPP**: Data link protocol for point-to-point connections over serial lines. Provides byte-oriented framing, error detection, and link management.
     - **LCP (Link Control Protocol)**: Establishes, configures, and tests the data link connection. Negotiates maximum payload size (MRU) and authentication protocols (PAP or CHAP).
     - **NCP (Network Control Protocol)**: Establishes and configures network layer protocols (e.g. IP Control Protocol IPCP to assign IP addresses dynamically).
