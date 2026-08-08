# Module 1 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 1**: Network Architecture & Reference Models

---

## 🚀 Submodule 1: Network Classification & Topologies

- **LAN vs MAN vs WAN**:
  - *LAN*: Local link (< 1 km), high speed (1–10 Gbps), low latency (< 1 ms), private ownership.
  - *MAN*: Citywide (10–50 km), medium speed (100 Mbps–1 Gbps), e.g., cable TV networks.
  - *WAN*: Global/Countrywide (> 100 km), leased lines/routers, higher latency (20–100 ms).
- **Network Topologies**:
  - *Mesh*: Every node connected to every other. Physical Links $L = \frac{N(N-1)}{2}$; Ports per node $= N-1$. Maximum fault tolerance & security, highest cabling cost.
  - *Star*: All nodes connect to central Switch/Hub. Links $L = N$. Easy maintenance; central switch failure drops entire network.
  - *Bus*: Single shared backbone cable with terminators. Low cable cost; collisions occur; line break downs entire bus.
  - *Ring*: Token ring structure. Equal access; single link break breaks ring (unless dual ring).

---

## 🚀 Submodule 2: Protocol Hierarchies & Design Issues

- **Protocols vs Services**:
  - *Protocol*: Rules governing peer-to-peer communication between identical layers on different machines.
  - *Service*: Set of operations/primitives a lower layer provides to an upper layer across an interface on the same machine.
- **6 Core Layer Design Issues**:
  1. *Addressing*: Identifying senders and receivers.
  2. *Error Control*: Detecting and correcting corrupted bits (CRC, checksums).
  3. *Flow Control*: Preventing fast senders from swamping slow receivers.
  4. *Multiplexing/Demultiplexing*: Sharing single link among multiple applications.
  5. *Routing*: Selecting optimal paths across subnets.
  6. *Fragmentation*: Splitting large messages into fit-sized payload packets.
- **4 Service Primitives**: `REQUEST` (initiates), `INDICATION` (notifies remote), `RESPONSE` (replies), `CONFIRM` (notifies initiator).

---

## 🚀 Submodule 3: OSI vs TCP/IP Reference Models

- **OSI 7 Layers**: Physical $\rightarrow$ Data Link $\rightarrow$ Network $\rightarrow$ Transport $\rightarrow$ Session $\rightarrow$ Presentation $\rightarrow$ Application (*"Please Do Not Touch Steve's Pet Alligator"*).
- **TCP/IP 4 Layers**: Network Access $\rightarrow$ Internet (IP) $\rightarrow$ Transport (TCP/UDP) $\rightarrow$ Application (HTTP, DNS, FTP, SMTP).
- **Key Differences**:
  - OSI strictly separates Services, Interfaces, and Protocols; TCP/IP was built around existing protocols.
  - OSI supports both connectionless & connection-oriented at Network layer; TCP/IP supports *only connectionless IP* at Internet layer.

---

## 🔢 3 Solved Numerical Micro-Examples

1. **Mesh Cabling Math**: For $N = 20$ routers, links $L = \frac{20 \times 19}{2} = \mathbf{190 \text{ cables}}$, ports per router $= \mathbf{19 \text{ ports}}$.
2. **Bandwidth-Delay Product (BDP)**: Bandwidth $100 \text{ Mbps}$, RTT $40 \text{ ms}$ (one-way delay $20 \text{ ms}$). $\text{BDP} = 100 \times 10^6 \times 0.02 = 2,000,000 \text{ bits} = \mathbf{250 \text{ KB}}$.
3. **Multi-Header Efficiency ($\eta$)**: Data $= 1000 \text{ B}$. Transport Header $= 20 \text{ B}$, IP Header $= 20 \text{ B}$, MAC Header $= 18 \text{ B}$. Total $= 1058 \text{ B}$.
   $$\eta = \frac{1000}{1058} \times 100 = \mathbf{94.52\%}$$
