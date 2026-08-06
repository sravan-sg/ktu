# Module 4 — Topic 2: IPv4 Addressing, Subnetting & CIDR

> **Module 4**: Congestion Control, QoS & IPv4 Subnetting  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The IPv4 protocol uses a **32-bit logical address** formatted in dotted-decimal notation (e.g. `192.168.1.1`):

1. **Classful IP Addressing**:
   - **Class A**: Range `0.0.0.0` to `127.255.255.255`. Leading bits `0`. Network bits = 8, Host bits = 24.
   - **Class B**: Range `128.0.0.0` to `191.255.255.255`. Leading bits `10`. Network bits = 16, Host bits = 16.
   - **Class C**: Range `192.0.0.0` to `223.255.255.255`. Leading bits `110`. Network bits = 24, Host bits = 8.
   - **Class D**: Range `224.0.0.0` to `239.255.255.255` (Multicast). Leading bits `1110`.
   - **Class E**: Range `240.0.0.0` to `255.255.255.255` (Experimental).

2. **Subnetting**:
   - Borrowing bits from the Host portion to create sub-networks (Subnets).
   - **Subnet Mask**: 32-bit mask where network/subnet bits are 1s and host bits are 0s (e.g. `255.255.255.192` for `/26`).

3. **CIDR (Classless Inter-Domain Routing)**:
   - Eliminates rigid A/B/C class boundaries using prefix length notation `/n` (e.g. `200.10.20.0/22`).
   - Allows **Supernetting (Route Aggregation)** to collapse multiple routing table entries into a single prefix.

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
   - **Subnet 0:** `192.168.10.0` to `192.168.10.63`
     - Network ID: `192.168.10.0`
     - Usable Range: `192.168.10.1` – `192.168.10.62`
     - Broadcast ID: `192.168.10.63`
   - **Subnet 1:** `192.168.10.64` to `192.168.10.127`
     - Network ID: `192.168.10.64`
     - Usable Range: `192.168.10.65` – `192.168.10.126`
     - Broadcast ID: `192.168.10.127`
   - **Subnet 2:** `192.168.10.128` to `192.168.10.191`
     - Network ID: `192.168.10.128`
     - Usable Range: `192.168.10.129` – `192.168.10.190`
     - Broadcast ID: `192.168.10.191`
   - **Subnet 3:** `192.168.10.192` to `192.168.10.255`
     - Network ID: `192.168.10.192`
     - Usable Range: `192.168.10.193` – `192.168.10.254`
     - Broadcast ID: `192.168.10.255`

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
   - $0 = 00000000_2$
   - $1 = 00000001_2$
   - $2 = 00000010_2$
   - $3 = 00000011_2$
2. **Find Matching Prefix Bits:**
   - First 2 octets (`202.10`) match completely (16 bits).
   - In 3rd octet, the first 6 bits (`000000`) are identical across all 4 networks.
   - Total matching bits $= 16 + 6 = 22$ bits.
3. **Supernet Result:** **`202.10.0.0/22`** (Mask: `255.255.252.0`).

---

## 3. Previous Year Questions & Solutions

1. **"An organization is granted the block 190.100.0.0/16. Design a subnetting scheme to create 8 equal subnets. Find subnet mask, first and last address of each subnet." [April 2018, Dec 2019]**
   - **Solution:**
     - 8 subnets $\implies 2^3 = 8 \implies 3$ bits borrowed. New prefix $= 16 + 3 = \mathbf{/19}$.
     - Subnet Mask: `255.255.224.0`.
     - Block size in 3rd octet $= 256 / 8 = 32$.
     - Subnet 0: `190.100.0.0` to `190.100.31.255` (Usable: `.0.1` to `.31.254`).
     - Subnet 1: `190.100.32.0` to `190.100.63.255` (Usable: `.32.1` to `.63.254`).
     - ... up to Subnet 7: `190.100.224.0` to `190.100.255.255`.

2. **"Explain IPv4 header format with a neat diagram." [May 2019, July 2021]**
   - **Solution:**
     **Fields:** Version (4b), IHL (4b), Type of Service (8b), Total Length (16b), Identification (16b), Flags (3b: DF, MF), Fragment Offset (13b), TTL (8b), Protocol (8b), Header Checksum (16b), Source IP Address (32b), Destination IP Address (32b), Options (Variable).
