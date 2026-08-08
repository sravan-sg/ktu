# Module 4 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 4**: Congestion Control, QoS & IPv4 Subnetting

---

## 🚀 Submodule 1: Congestion Control & QoS

- **Traffic Shaping**:
  - *Leaky Bucket*: Converts variable bursty traffic into a smooth, constant bit-rate output stream using a fixed-rate queue. Drops overflowing packets.
  - *Token Bucket*: Accumulates tokens at rate $r$ up to capacity $B$. Allows short bursts at full link speed $S$ for duration $t = \frac{B}{S - r}$.
- **Congestion Prevention**:
  - *Choke Packets*: Router sends explicit warning packet back to traffic source.
  - *RED (Random Early Detection)*: Router drops/marks incoming packets randomly before buffer becomes completely full to trigger TCP slow-down.
- **Quality of Service (QoS)**:
  - *IntServ (RSVP)*: Per-flow resource reservation; hard guarantees but poor scalability.
  - *DiffServ (DSCP)*: Per-hop class-based traffic prioritization; 6-bit DSCP field in IP header; highly scalable.
  - *WFQ (Weighted Fair Queueing)*: Allocates bandwidth proportional to queue weights.

---

## 🚀 Submodule 2: IPv4 Header & Classful Addressing

- **IPv4 Header Fields (20B Base)**: Version (4b), IHL (4b), Type of Service/DSCP (8b), Total Length (16b), Identification (16b), Flags (3b - DF, MF), Fragment Offset (13b), TTL (8b), Protocol (8b), Header Checksum (16b), Source IP (32b), Destination IP (32b).
- **Classful IP Addressing Table**:
  - *Class A*: `0.0.0.0` to `127.255.255.255` (`/8` mask `255.0.0.0`). 128 networks, 16M hosts/net.
  - *Class B*: `128.0.0.0` to `191.255.255.255` (`/16` mask `255.255.0.0`). 16k networks, 65k hosts/net.
  - *Class C*: `192.0.0.0` to `223.255.255.255` (`/24` mask `255.255.255.0`). 2M networks, 254 hosts/net.
  - *Class D*: `224.0.0.0` to `239.255.255.255` (Multicast).
  - *Class E*: `240.0.0.0` to `255.255.255.255` (Experimental).
- **RFC 1918 Private Address Ranges**: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.

---

## 🚀 Submodule 3: CIDR, Subnetting & VLSM

- **Subnet Mask Math**: Borrowing $b$ host bits creates $2^b$ subnets, leaving $32 - (N + b)$ host bits, providing $2^{\text{host bits}} - 2$ usable hosts per subnet.
- **CIDR (Classless Inter-Domain Routing)**: Replaces classful masks with prefix length notation (e.g. `/26`).
- **Supernetting (Route Aggregation)**: Combines multiple contiguous smaller subnets into a single routing table entry (e.g. four `/24` subnets combined into one `/22` supernet).

---

## 🔢 3 Solved Numerical Micro-Examples

1. **Token Bucket Burst Math**: Capacity $B = 1 \text{ MB}$, Token Rate $r = 2 \text{ MB/s}$, Maximum Transmission Speed $S = 10 \text{ MB/s}$.
   $$\text{Max Burst Duration } t = \frac{1 \text{ MB}}{10 - 2} = \frac{1}{8} \text{ s} = \mathbf{125 \text{ ms}}$$
2. **Subnet Math (`/26`)**: IP `192.168.1.130/26`.
   - Subnet Mask: `255.255.255.192`.
   - Block Size $= 256 - 192 = 64$.
   - Network Address $= \mathbf{192.168.1.128}$.
   - Broadcast Address $= \mathbf{192.168.1.191}$.
   - Usable Host Range $= \mathbf{192.168.1.129 \text{ to } 192.168.1.190}$ (62 hosts).
3. **Fragment Math**: Data $= 3000 \text{ B}$, MTU $= 1000 \text{ B}$.
   - Frag 1: Payload $976 \text{ B}$ (divisible by 8) + 20B Header. Offset $= 0$, `MF = 1`.
   - Frag 2: Payload $976 \text{ B}$ + 20B Header. Offset $= 976 / 8 = \mathbf{122}$, `MF = 1`.
   - Frag 3: Payload $1048 \text{ B}$ + 20B Header. Offset $= 1952 / 8 = \mathbf{244}$, `MF = 0`.
