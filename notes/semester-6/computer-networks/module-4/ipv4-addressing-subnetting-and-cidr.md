# Module 4 — Topic 2: Internetworking, IPv4 Header & IP Addressing (Classful & CIDR)

> **Module 4**: Congestion Control, QoS & IPv4 Subnetting  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The Internet is a global **Internetwork**—a collection of disparate physical networks (Ethernet LANs, Wi-Fi, Optical WANs, Satellite links) connected by routers operating under a common protocol: **IPv4 (Internet Protocol Version 4)**.

---

### 1. Internetworking & Network Layer in the Internet
- **Heterogeneous Subnets**: Different networks have different frame formats, Maximum Transmission Units (MTU), physical speeds, and addressing schemes.
- **Tunneling**: When an IPv6 or specialized packet must cross an intermediate IPv4-only network, the entire packet is encapsulated inside an outer IPv4 header at the entry router and stripped at the exit router.
- **IPv4 Datagram Header Format**:
  ```text
  0                   1                   2                   3
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  |Version|  IHL  |Type of Service|          Total Length         |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  |         Identification        |Flags|     Fragment Offset     |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  |  Time to Live |    Protocol   |        Header Checksum        |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  |                       Source IP Address                       |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  |                    Destination IP Address                     |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  |                    Options (if any) + Padding                 |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  ```
  - **Version (4 bits)**: Specifies protocol version (`4` for IPv4).
  - **IHL (Internet Header Length - 4 bits)**: Specifies header length in 32-bit words (minimum = 5, i.e., 20 Bytes).
  - **Type of Service / DSCP (8 bits)**: Used for QoS traffic classification.
  - **Total Length (16 bits)**: Total datagram size including header and payload (max 65,535 Bytes).
  - **Identification, Flags (DF, MF), Fragment Offset**: Handles packet fragmentation when packet size exceeds MTU.
  - **Time to Live (TTL - 8 bits)**: Hop count limit to prevent infinite loops (decremented per hop; discarded when TTL = 0).
  - **Protocol (8 bits)**: Specifies upper-layer payload protocol (`6` for TCP, `17` for UDP, `1` for ICMP).
  - **Header Checksum (16 bits)**: Error detection checksum over the IPv4 header.

---

### 2. Classful IP Addressing
IPv4 uses a **32-bit logical address** formatted as 4 octets in dotted-decimal notation (e.g. `192.168.1.1`).
Originally partitioned into rigid Classes A, B, C, D, E based on leading bits:

| Class | Leading Bits | First Octet Range | NetID / HostID Split | Default Subnet Mask | Max Networks / Hosts |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Class A** | `0...` | `1.0.0.0` to `127.255.255.255` | 8 bits NetID / 24 bits HostID | `255.0.0.0` (`/8`) | 128 nets / $16,777,214$ hosts |
| **Class B** | `10..` | `128.0.0.0` to `191.255.255.255` | 16 bits NetID / 16 bits HostID | `255.255.0.0` (`/16`) | 16,384 nets / $65,534$ hosts |
| **Class C** | `110.` | `192.0.0.0` to `223.255.255.255` | 24 bits NetID / 8 bits HostID | `255.255.255.0` (`/24`) | $2,097,152$ nets / 254 hosts |
| **Class D** | `1110` | `224.0.0.0` to `239.255.255.255` | Multicast Addressing | N/A | Reserved for Multicasting |
| **Class E** | `1111` | `240.0.0.0` to `255.255.255.255` | Experimental / Research | N/A | Reserved for Research |

#### Special IP Addresses:
- **Loopback Address**: `127.0.0.1` (used for internal host software testing).
- **Private IP Ranges (RFC 1918)**:
  - Class A Private: `10.0.0.0/8` (`10.0.0.0` – `10.255.255.255`)
  - Class B Private: `172.16.0.0/12` (`172.16.0.0` – `172.31.255.255`)
  - Class C Private: `192.168.0.0/16` (`192.168.0.0` – `192.168.255.255`)

---

### 3. Classless IP Addressing (CIDR)
To solve the depletion of Class B addresses and routing table explosion, **CIDR (Classless Inter-Domain Routing)** was introduced:
- **Slash Notation (`/n`)**: Replaces rigid class boundaries with arbitrary prefix lengths (e.g. `200.10.20.0/22`).
- **Subnetting**: Borrowing bits from the Host portion to create smaller subnets ($2^s$ subnets, $2^h - 2$ usable hosts).
- **VLSM (Variable Length Subnet Masking)**: Allocating subnet masks of different sizes based on exact host requirements.
- **Supernetting (Route Aggregation)**: Combining multiple contiguous network prefixes into a single routing table entry (e.g., combining 4 `/24` networks into 1 `/22` supernet).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Full Subnetting Calculation Walkthrough
**Problem:** An organization is assigned the IP block `192.168.10.0/24`. The administrator needs to create **4 equal-sized subnets**. Find:
(a) Subnet Mask, (b) Number of usable hosts per subnet, (c) Network Address, Broadcast Address, and Usable Host Range for Subnet 1 and Subnet 3.
**Step-by-step Solution:**
1. **Determine Borrowed Bits:**
   To make 4 subnets ($2^s = 4 \implies s = 2$ bits borrowed).
   New prefix length $n = 24 + 2 = \mathbf{/26}$.
2. **Subnet Mask:**
   `/26` $\implies 11111111.11111111.11111111.11000000_2 = \mathbf{255.255.255.192}$.
3. **Usable Hosts per Subnet:**
   Host bits $h = 32 - 26 = 6$.
   $$\text{Usable Hosts} = 2^h - 2 = 2^6 - 2 = 64 - 2 = \mathbf{62 \text{ hosts/subnet}}$$
   Block size $= 2^h = 64$.
4. **Subnet Breakdowns:**
   - **Subnet 0:** `192.168.10.0` to `192.168.10.63` (Usable: `.1` to `.62`, Broadcast: `.63`)
   - **Subnet 1:** `192.168.10.64` to `192.168.10.127` (Usable: `.65` to `.126`, Broadcast: `.127`)
   - **Subnet 2:** `192.168.10.128` to `192.168.10.191` (Usable: `.129` to `.190`, Broadcast: `.191`)
   - **Subnet 3:** `192.168.10.192` to `192.168.10.255` (Usable: `.193` to `.254`, Broadcast: `.255`)

### Example 2: VLSM (Variable Length Subnet Masking) Allocation
**Problem:** An ISP has block `200.20.30.0/24`. Allocate subnets for 3 departments: Dept A (100 hosts), Dept B (50 hosts), Dept C (25 hosts).
**Step-by-step Solution:**
1. **Dept A (100 hosts):**
   - Need $2^h - 2 \ge 100 \implies h = 7$ bits ($2^7 - 2 = 126$ hosts).
   - Prefix length $= 32 - 7 = \mathbf{/25}$. Mask: `255.255.255.128`.
   - Allocation: `200.20.30.0/25` (Range: `200.20.30.0` to `200.20.30.127`).
2. **Dept B (50 hosts):**
   - Need $2^h - 2 \ge 50 \implies h = 6$ bits ($2^6 - 2 = 62$ hosts).
   - Prefix length $= 32 - 6 = \mathbf{/26}$. Mask: `255.255.255.192`.
   - Allocation starts at next available address: `200.20.30.128/26` (Range: `200.20.30.128` to `200.20.30.191`).
3. **Dept C (25 hosts):**
   - Need $2^h - 2 \ge 25 \implies h = 5$ bits ($2^5 - 2 = 30$ hosts).
   - Prefix length $= 32 - 5 = \mathbf{/27}$. Mask: `255.255.255.224`.
   - Allocation starts at next available address: `200.20.30.192/27` (Range: `200.20.30.192` to `200.20.30.223`).

### Example 3: CIDR Route Aggregation (Supernetting)
**Problem:** A router has 4 contiguous Class C routes: `202.10.0.0/24`, `202.10.1.0/24`, `202.10.2.0/24`, `202.10.3.0/24`. Aggregate these into a single CIDR supernet block.
**Step-by-step Solution:**
1. **Convert 3rd Octet to Binary:**
   - $0 = 00000000_2$, $1 = 00000001_2$, $2 = 00000010_2$, $3 = 00000011_2$.
2. **Find Matching Prefix Bits:**
   - First 2 octets (`202.10`) match completely (16 bits).
   - In 3rd octet, the first 6 bits (`000000`) are identical across all 4 networks.
   - Total matching bits $= 16 + 6 = 22$ bits.
3. **Supernet Result:** **`202.10.0.0/22`** (Mask: `255.255.252.0`).

---

## 3. Previous Year Questions & Solutions

1. **"Explain Classful IP Addressing scheme (Classes A, B, C, D, E) with network and host bit split." [May 2019, July 2021]**
   - **Solution:**
     - **Class A**: Leading bit `0`. 8-bit NetID, 24-bit HostID (`1.0.0.0` to `127.255.255.255`). Default mask `/8`.
     - **Class B**: Leading bits `10`. 16-bit NetID, 16-bit HostID (`128.0.0.0` to `191.255.255.255`). Default mask `/16`.
     - **Class C**: Leading bits `110`. 24-bit NetID, 8-bit HostID (`192.0.0.0` to `223.255.255.255`). Default mask `/24`.
     - **Class D**: Leading bits `1110`. Multicast reserved (`224.0.0.0` to `239.255.255.255`).
     - **Class E**: Leading bits `1111`. Experimental reserved (`240.0.0.0` to `255.255.255.255`).

2. **"Explain IPv4 datagram header fields in detail." [Dec 2019]**
   - **Solution:**
     Version (4b), IHL (4b), Type of Service/DSCP (8b), Total Length (16b), Identification (16b), Flags (DF, MF - 3b), Fragment Offset (13b), TTL (8b), Protocol (8b), Header Checksum (16b), Source IP (32b), Destination IP (32b).
