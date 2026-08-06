# Module 1 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 1**: Network Architecture & Reference Models

---

## 🚀 Submodule 1: Network Hardware & Topologies

- **LAN vs WAN**: LAN (< 1 km, high speed 1 Gbps, low delay, private); WAN (> 100 km, country/global, moderate speed, leased lines).
- **Mesh Topology Formula**: Links $L = \frac{N(N-1)}{2}$; I/O ports per node = $N - 1$. High fault tolerance, expensive cabling.
- **Star Topology**: Central switch; $L = N$. Node cable break isolates only 1 machine; central switch failure drops network.

---

## 🚀 Submodule 2: Protocol Hierarchies & Layering

- **Protocol vs Service**: Protocol = rules governing communication between *peer entities* at Layer $N$. Service = set of primitives Layer $N$ provides to Layer $N+1$ across an *interface*.
- **Encapsulation**: Moving down stack prepends headers ($H_N$); moving up decapsulates.
- **Connection-Oriented vs Connectionless**: Connection-oriented has 3 phases (Establishment, Data Transfer, Release) guaranteeing in-order delivery; Connectionless sends independent datagrams without setup.

---

## 🚀 Submodule 3: OSI vs TCP/IP Reference Models

- **OSI 7 Layers**: **P**hysical, **D**ata Link, **N**etwork, **T**ransport, **S**ession, **P**resentation, **A**pplication (*"Please Do Not Touch Steve's Pet Alligator"*).
- **TCP/IP 4 Layers**: Host-to-Network, Internet (IP), Transport (TCP/UDP), Application (HTTP, DNS).
- **Key Difference**: OSI is a theoretical 7-layer model separating services/interfaces/protocols; TCP/IP is a practical 4-layer internet suite.

---

## 🔢 3 Solved Numerical Micro-Examples

1. **Mesh Links**: For $N = 10$ nodes, $L = \frac{10 \times 9}{2} = 45$ links.
2. **BDP Pipe Volume**: Bandwidth $100 \text{ Mbps}$, RTT $20 \text{ ms}$. One-way delay $= 10 \text{ ms}$. $\text{BDP} = 10^8 \times 0.01 = 1,000,000 \text{ bits} = 125,000 \text{ Bytes} = 125 \text{ KB}$.
3. **Encapsulation Overhead**: Payload 1000B, Headers 60B. Efficiency $\eta = \frac{1000}{1060} \times 100 = 94.34\%$.
