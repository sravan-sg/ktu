# Module 1 — Topic 4: OSI Reference Model vs TCP/IP Reference Model

> **Module 1**: Network Architecture & Reference Models  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
To standardize global communications across disparate hardware platforms, formal reference models specify layered abstractions.

```
       OSI 7-LAYER MODEL                       TCP/IP 4-LAYER MODEL
  ┌─────────────────────────┐               ┌─────────────────────────┐
  │  7. Application Layer   │               │   4. Application Layer  │
  ├─────────────────────────┤               │ (HTTP, FTP, DNS, SMTP)  │
  │  6. Presentation Layer  │ ────────────► ├─────────────────────────┤
  ├─────────────────────────┤               │   3. Transport Layer    │
  │  5. Session Layer       │               │       (TCP, UDP)        │
  ├─────────────────────────┤               ├─────────────────────────┤
  │  4. Transport Layer     │ ────────────► │   2. Internet Layer     │
  ├─────────────────────────┤               │       (IP, ICMP)        │
  │  3. Network Layer       │ ────────────► ├─────────────────────────┤
  ├─────────────────────────┤               │ 1. Network Access Layer │
  │  2. Data Link Layer     │ ────────────► │ (Ethernet, Wi-Fi, PPP)  │
  ├─────────────────────────┤               └─────────────────────────┘
  │  1. Physical Layer      │
  └─────────────────────────┘
```

---

### Detailed Functions of the OSI 7 Layers

1. **Layer 7 — Application Layer**:
   - Provides user interface services and application-level network protocols (HTTP, FTP, SMTP, DNS, Telnet).

2. **Layer 6 — Presentation Layer**:
   - Handles data syntax formatting, character encoding (ASCII, EBCDIC, Unicode), data compression (JPEG, MP3), and encryption/decryption (SSL/TLS).

3. **Layer 5 — Session Layer**:
   - Establishes, manages, and terminates dialog sessions between applications. Provides dialog control (Simplex, Half-Duplex, Full-Duplex) and checkpointing for recovery.

4. **Layer 4 — Transport Layer**:
   - Manages end-to-end, process-to-process communication. Performs segmentation, port addressing (Layer 4 ports), flow control, error control, and in-order delivery (TCP, UDP).

5. **Layer 3 — Network Layer**:
   - Handles host-to-host routing across subnets. Assigns logical addresses (IP addresses), determines shortest paths using routing algorithms, and handles packet fragmentation.

6. **Layer 2 — Data Link Layer**:
   - Provides reliable node-to-node hop transmission across a single physical link. Groups bits into **Frames**, handles physical MAC addressing, CRC error detection, and MAC medium access (CSMA/CD).

7. **Layer 1 — Physical Layer**:
   - Transmits raw, uninterpreted **Bit Streams** over physical media (copper wires, optical fibers, radio waves). Defines electrical voltage levels, pin layouts, bit rates, and signal timing.

---

### Key Structural Differences: OSI vs TCP/IP

| Feature / Metric | OSI Reference Model | TCP/IP Reference Model |
| :--- | :--- | :--- |
| **Development Approach** | Theoretical model created by ISO *before* protocols were written | Practical model created by DoD *after* TCP/IP protocols were implemented |
| **Layer Count** | 7 Layers | 4 Layers (or 5-layer hybrid model) |
| **Session & Presentation** | Separate dedicated Layers 5 & 6 | Combined into Application Layer 4 |
| **Network Layer Services** | Supports both Connectionless & Connection-Oriented | Connectionless IP Service only at Network Layer |
| **Transport Layer Services**| Connection-Oriented only | Choice of Connectionless (UDP) or Connection-Oriented (TCP) |
| **Protocol Independence** | Strictly decoupled (protocols fit hidden behind interfaces) | Protocol-dependent (protocols came first, model is a description) |

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Multi-Layer Protocol Encapsulation Overhead
**Problem:** An application sends a 1,000-byte message down the OSI 7-layer stack.
- Layer 7, 6, 5 add no headers.
- Layer 4 (Transport) adds 20 Bytes.
- Layer 3 (Network) adds 20 Bytes.
- Layer 2 (Data Link) adds 18 Bytes (14B Header + 4B Trailer).
- Layer 1 (Physical) adds 8 Bytes (Preamble + SFD).
Calculate the total transmitted frame size, header overhead percentage, and throughput efficiency on a 100 Mbps link.
**Step-by-step Solution:**
1. **Total Overhead:** $20 + 20 + 18 + 8 = 66 \text{ Bytes}$.
2. **Total Frame Size:** $1000 + 66 = 1,066 \text{ Bytes} = 8,528 \text{ bits}$.
3. **Header Overhead %:**
   $$\text{Overhead \%} = \frac{66}{1066} \times 100 = \mathbf{6.19\%}$$
4. **Throughput Efficiency ($\eta$):**
   $$\eta = \frac{1000}{1066} \times 100 = \mathbf{93.81\%}$$

### Example 2: Bandwidth-Delay Product (BDP) Calculation
**Problem:** A satellite link operates at $R = 10 \text{ Mbps}$ with a Round-Trip Time $\text{RTT} = 500 \text{ ms}$.
(a) Calculate the Bandwidth-Delay Product (BDP) in bits and bytes.
(b) How many 1,000-byte TCP segments can be "in flight" on the wire simultaneously?
**Step-by-step Solution:**
1. **Calculate BDP:**
   $$\text{BDP} = R \times \text{RTT} = 10 \times 10^6 \text{ bps} \times 0.5 \text{ s} = 5,000,000 \text{ bits}$$
   $$\text{BDP in Bytes} = \frac{5,000,000}{8} = \mathbf{625,000 \text{ Bytes} \approx 625 \text{ KB}}$$
2. **Calculate In-Flight Segments:**
   $$\text{Segments} = \frac{625,000 \text{ Bytes}}{1,000 \text{ Bytes/segment}} = \mathbf{625 \text{ segments}}$$

### Example 3: Layer Address Mapping Trace
**Problem:** Trace the destination address changes as a packet travels from Host A (IP `10.0.0.2`, MAC `AA:AA:AA:AA:AA:AA`) through Router R (Port 1 MAC `RR:RR:RR:RR:RR:01`, Port 2 MAC `RR:RR:RR:RR:RR:02`) to Host B (IP `192.168.1.5`, MAC `BB:BB:BB:BB:BB:BB`).
**Step-by-step Solution:**
1. **Hop 1: Host A to Router R (Port 1):**
   - Layer 3 IP Header: `[Src IP: 10.0.0.2, Dst IP: 192.168.1.5]` (Unchanged)
   - Layer 2 Frame Header: `[Src MAC: AA:AA:AA:AA:AA:AA, Dst MAC: RR:RR:RR:RR:RR:01]`
2. **Hop 2: Router R (Port 2) to Host B:**
   - Layer 3 IP Header: `[Src IP: 10.0.0.2, Dst IP: 192.168.1.5]` (Unchanged)
   - Layer 2 Frame Header: `[Src MAC: RR:RR:RR:RR:RR:02, Dst MAC: BB:BB:BB:BB:BB:BB]`
3. **Key Finding:** Layer 3 IP addresses remain end-to-end constant; Layer 2 MAC addresses change at every router hop.

---

## 3. Previous Year Questions & Solutions

1. **"Compare OSI 7-layer model and TCP/IP 4-layer model. List main functions of each OSI layer." [May 2019, July 2021]**
   - **Solution:**
     **OSI Functions:** Physical (bits), Data Link (frames, MAC), Network (packets, routing), Transport (end-to-end reliability), Session (dialog control), Presentation (formatting/encryption), Application (user UI).
     **Comparison:** OSI is theoretical with 7 layers created before protocols; TCP/IP is practical with 4 layers created after protocols. OSI supports connectionless/connection-oriented at Network layer; TCP/IP supports only connectionless IP at Internet layer.

2. **"Explain protocol encapsulation and decapsulation with a diagram." [April 2018]**
   - **Solution:**
     As application data moves down the stack, each layer prepends a header ($H_4, H_3, H_2$) containing addressing and control data (Encapsulation). At the receiving host, as bits ascend, each layer strips its corresponding header before passing payload up (Decapsulation).
