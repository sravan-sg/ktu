# Module 5 — Topic 1: Internet Control Protocols (ICMP, ARP, RARP, BOOTP)

> **Module 5**: Internet Control Protocols, Multicasting & IPv6  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The Network Layer relies on auxiliary control protocols to handle IP error reporting, dynamic MAC-to-IP address resolution, and initial host bootstrapping.

---

### 1. ICMP (Internet Control Message Protocol)
- Operates directly over IP (Protocol number 1) to provide feedback about IP packet delivery failures.
- **ICMP Packet Header**:
  - `Type (8 bits)`: Specifies ICMP message category.
  - `Code (8 bits)`: Gives specific sub-reason for message.
  - `Checksum (16 bits)`: Error detection over ICMP header and payload.
  - `Payload`: Contains the IP header + first 64 bits (8 Bytes) of the original datagram that caused the error.

#### Key ICMP Message Types:
- **Type 0 (Echo Reply)** / **Type 8 (Echo Request)**: Used by `ping` utility to test end-to-end reachability.
- **Type 3 (Destination Unreachable)**:
  - Code 0: Network Unreachable.
  - Code 1: Host Unreachable.
  - Code 3: Port Unreachable (sent by transport layer when receiving packet for an unopened UDP port).
  - Code 4: Fragmentation Needed and DF Set.
- **Type 5 (Redirect)**: Sent by a router to inform a host of a better first-hop router.
- **Type 11 (Time Exceeded)**: Sent by a router when a packet's `TTL` reaches 0. Used by `traceroute` to map network paths hop-by-hop.

---

### 2. ARP (Address Resolution Protocol) & RARP
- **ARP (Address Resolution Protocol)**:
  - Maps a known 32-bit IP address to an unknown 48-bit Layer 2 MAC address within a local link.
  - *Operation*: Sender broadcasts an **ARP Request** (`"Who has IP 192.168.1.5?"`). Target host replies with a unicast **ARP Reply** (`"192.168.1.5 is at AA:BB:CC:DD:EE:FF"`). Results stored in **ARP Cache**.
  - **Proxy ARP**: A router responds to ARP requests for off-subnet hosts, acting as a gateway representative.
- **RARP (Reverse Address Resolution Protocol)**:
  - Used by diskless workstations to discover their own IP address given their hardcoded MAC address. (Obsoleted by BOOTP and DHCP).

---

### 3. BOOTP (Bootstrap Protocol)
- Client-server protocol operating over UDP (Ports 67/68) used by diskless workstations during bootup to request:
  1. Assigned IP Address.
  2. Subnet Mask.
  3. Default Gateway IP.
  4. TFTP Server IP and Boot Image Filename.
- Uses **BOOTP Relay Agents** to forward bootstrap requests across router boundaries to central BOOTP/DHCP servers.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: `traceroute` Execution & ICMP Time Exceeded Trace
**Problem:** Host A runs `traceroute` to destination Host B located 3 hops away (Routers R1, R2, R3).
Trace the TTL values, ICMP message types, and source IPs returned for each probe.
**Step-by-step Solution:**
1. **Probe 1 ($\text{TTL} = 1$):**
   - Host A sends UDP packet to Host B with $\text{TTL} = 1$.
   - R1 receives packet, decrements $\text{TTL} = 0$, discards packet, sends **ICMP Type 11 (Time Exceeded)** back to Host A (`Src IP: R1_IP`).
   - Host A logs R1's IP and RTT.
2. **Probe 2 ($\text{TTL} = 2$):**
   - Host A sends UDP packet with $\text{TTL} = 2$.
   - Passes R1 ($\text{TTL}=1$), reaches R2 where $\text{TTL}=0$.
   - R2 sends **ICMP Type 11 (Time Exceeded)** back to Host A (`Src IP: R2_IP`).
3. **Probe 3 ($\text{TTL} = 3$):**
   - Host A sends UDP packet with $\text{TTL} = 3$.
   - Passes R1, R2, arrives at destination Host B.
   - Host B sees an unused UDP port number and responds with **ICMP Type 3 Code 3 (Port Unreachable)**.
   - Host A receives Port Unreachable and terminates `traceroute`.

### Example 2: ARP Packet Resolution Trace
**Problem:** Host A (`IP: 192.168.1.10`, `MAC: 00:11:22:33:44:55`) wants to send a packet to Host B (`IP: 192.168.1.20`, `MAC: AA:BB:CC:DD:EE:FF`) on the same LAN. Host A's ARP cache is empty.
Trace the Layer 2 and Layer 3 frame fields for ARP Request and ARP Reply.
**Step-by-step Solution:**
1. **ARP Request (Broadcast):**
   - Ethernet Header: `[Src MAC: 00:11:22:33:44:55, Dst MAC: FF:FF:FF:FF:FF:FF]`
   - ARP Payload: `[Sender IP: 192.168.1.10, Sender MAC: 00:11:22:33:44:55, Target IP: 192.168.1.20, Target MAC: 00:00:00:00:00:00]`
2. **ARP Reply (Unicast):**
   - Ethernet Header: `[Src MAC: AA:BB:CC:DD:EE:FF, Dst MAC: 00:11:22:33:44:55]`
   - ARP Payload: `[Sender IP: 192.168.1.20, Sender MAC: AA:BB:CC:DD:EE:FF, Target IP: 192.168.1.10, Target MAC: 00:11:22:33:44:55]`

### Example 3: Subnet Mask & ICMP Redirect Mechanics
**Problem:** Host A (`192.168.1.50/24`) has Default Gateway R1 (`192.168.1.1`). Host A sends a packet to Host B (`192.168.1.90`). Router R1 receives the packet on interface `eth0` and finds that the best route to Host B is via Router R2 (`192.168.1.2`), which is attached to the same `eth0` network link.
Explain the ICMP Redirect sequence.
**Step-by-step Solution:**
1. R1 forwards the packet to R2 out of `eth0`.
2. R1 notices that the incoming and outgoing interfaces for the packet are identical (`eth0`).
3. R1 sends an **ICMP Type 5 (Redirect)** message to Host A containing R2's IP (`192.168.1.2`).
4. Host A updates its local routing table so future packets to `192.168.1.90` are sent directly to R2.

---

## 3. Previous Year Questions & Solutions

1. **"Explain ARP and RARP protocols with message exchange diagrams." [May 2019, July 2021]**
   - **Solution:**
     - **ARP**: Maps IP address $\rightarrow$ MAC address. Broadcast request, unicast reply. Results cached in ARP table.
     - **RARP**: Maps MAC address $\rightarrow$ IP address. Used by diskless hosts at bootup. Server maintains static MAC-to-IP table.

2. **"Explain ICMP error reporting messages and how traceroute uses ICMP." [Dec 2019]**
   - **Solution:**
     ICMP delivers error feedback for IP. Message types include Destination Unreachable (Type 3), Time Exceeded (Type 11), Redirect (Type 5). `traceroute` sends UDP probes with incrementing TTL values ($1, 2, 3 \dots$). Intermediate routers decrement TTL to 0 and return ICMP Time Exceeded messages, revealing router IPs along the path. Destination host returns ICMP Port Unreachable.
