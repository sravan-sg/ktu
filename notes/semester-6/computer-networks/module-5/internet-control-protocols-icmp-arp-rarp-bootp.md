# Module 5 — Topic 1: Internet Control Protocols (ICMP, ARP, RARP, BOOTP)

> **Module 5**: Internet Control Protocols, Multicasting & IPv6  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The Network Layer relies on auxiliary control protocols to handle IP error reporting, dynamic MAC-to-IP address resolution, and initial host bootstrapping.

---

### 1. ICMP (Internet Control Message Protocol)
- **Role**: Operates directly over IP (Protocol number 1) as a companion protocol to provide feedback about IP packet delivery failures and assist in network diagnostics. Although it runs *over* IP, it is considered a core part of the Network Layer.
- **Error Reporting Mechanics**: IP itself fails silently (e.g., if a router drops a packet due to an unknown route or failed reassembly). ICMP solves this by sending an error message back to the original sender.
- **ICMP Packet Header**:
  - `Type (8 bits)`: Specifies ICMP message category.
  - `Code (8 bits)`: Gives specific sub-reason for message.
  - `Checksum (16 bits)`: Error detection over ICMP header and payload.
  - `Payload`: Contains the IP header + first 64 bits (8 Bytes) of the original datagram that caused the error, allowing the sender to match the error to a specific process/socket.
- **Key ICMP Message Types**:
  - **Type 0 (Echo Reply)** / **Type 8 (Echo Request)**: Used by `ping` to test node reachability and liveness.
  - **Type 3 (Destination Unreachable)**: 
    - Code 0: Network Unreachable.
    - Code 1: Host Unreachable (e.g., link failure).
    - Code 3: Port Unreachable (sent by the destination's transport layer when receiving a packet for an unopened UDP port).
    - Code 4: Fragmentation Needed and DF (Don't Fragment) Set.
  - **Type 5 (Redirect)**: Sent by a router to a source host indicating that a better first-hop router exists for the specific destination. The host then updates its local routing table.
  - **Type 11 (Time Exceeded)**: Sent by a router when a packet's `TTL` reaches 0 to prevent routing loops. Heavily exploited by `traceroute` to map the network hop-by-hop.

---

### 2. ARP (Address Resolution Protocol) & RARP
- **ARP (Address Resolution Protocol)**:
  - **Purpose**: Maps a known 32-bit IP address to an unknown 48-bit Layer 2 physical MAC address within a single broadcast domain or local link.
  - **Operation**: 
    1. A host broadcasts an **ARP Request** containing the target IP to all nodes on the Ethernet segment (`FF:FF:FF:FF:FF:FF`).
    2. Every host receives it, but only the target host matching the IP replies. The target sends a unicast **ARP Reply** containing its MAC address back to the sender.
    3. The sender stores this mapping in its **ARP Cache** (which typically times out after ~15 minutes to handle hardware replacements).
  - **Packet Format**: Contains Hardware Type (e.g., Ethernet), Protocol Type (e.g., IP), Lengths for both, Operation (Request/Reply), and the Sender/Target MAC and IP addresses.
  - **Proxy ARP**: A router responds to ARP requests on behalf of off-subnet hosts, acting as a transparent gateway.
- **RARP (Reverse Address Resolution Protocol)**:
  - **Purpose**: Allows a diskless workstation to discover its own IP address by broadcasting its hardcoded MAC address at boot. It requires a dedicated RARP server to maintain a static MAC-to-IP table. (Largely obsoleted by BOOTP and DHCP).

---

### 3. BOOTP (Bootstrap Protocol) & DHCP
- **BOOTP**: A client-server protocol operating over UDP (Ports 67 for Server / 68 for Client) used by diskless workstations during bootup. It extends RARP by providing more than just an IP address. It supplies:
  1. Assigned IP Address.
  2. Subnet Mask.
  3. Default Gateway IP.
  4. TFTP Server IP and Boot Image Filename.
- **Relay Agents**: To avoid needing a server on every subnet, **BOOTP Relay Agents** (usually routers configured with the server's IP) listen for broadcast requests and unicast them to central servers.
- **DHCP (Dynamic Host Configuration Protocol)**:
  - Built upon BOOTP, DHCP heavily automates network management.
  - **Address Pools & Leasing**: Instead of static MAC-to-IP mappings, the DHCP server maintains a pool of available IP addresses and dynamically "leases" them to hosts for a specific duration. Hosts must periodically renew their leases.
  - **Discovery**: A new host broadcasts a `DHCPDISCOVER` message to `255.255.255.255`. A relay agent intercepts it and forwards it to the DHCP server, which responds with a `DHCPOFFER`.

---

### Example
- **ARP Cache in Action**: When you type `ping 192.168.1.100`, your computer first checks its ARP cache (viewable via `arp -a` in Windows/Linux). If the MAC address isn't there, it pauses the `ping`, broadcasts an ARP request, waits for the MAC address reply, stores it in the cache, and *then* finally constructs and sends the ICMP Echo Request frame.

### Applications & Use Cases
- **ICMP**: Network diagnostics. Tools like `ping` (testing latency and packet loss) and `traceroute` (identifying network bottlenecks or routing loops) rely entirely on ICMP.
- **ARP**: Fundamental to every local network communication. Without ARP, an IP packet cannot be encapsulated into an Ethernet frame because the destination MAC address would be unknown.
- **DHCP**: Used universally in home routers, enterprise networks, and coffee shop Wi-Fi to automatically provision connecting laptops and smartphones with valid IP configurations, avoiding catastrophic IP conflicts.

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
