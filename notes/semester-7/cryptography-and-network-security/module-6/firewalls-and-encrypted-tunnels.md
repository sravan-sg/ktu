# Firewalls and Encrypted Tunnels

## 1. Explanation
A **firewall** is an integrated collection of security components (hardware and software) placed between an organization's private, trusted internal network and an untrusted external network (such as the Internet) to enforce an access control security policy.

### Firewall Design Principles & Objectives
According to William Stallings (*Cryptography and Network Security*, Chapter 22), any firewall must satisfy three design goals:
1. **Single Choke Point (All traffic must pass through)**: All traffic from inside to outside, and vice versa, must traverse the firewall. Physical bypass routes (e.g., unauthorized modems or rogue wireless access points) must be prevented.
2. **Policy Enforcement (Only authorized traffic is allowed)**: Only traffic defined by the local security policy is permitted to pass.
3. **High Immunity (The firewall itself is immune to penetration)**: The firewall platform must be implemented on a hardened system (Bastion host) with secure operating system controls.

#### General Access Control Policies
- **Default Deny (Whitelist)**: "That which is not explicitly permitted is forbidden." Highly secure; only pre-approved protocols and ports are allowed through.
- **Default Permit (Blacklist)**: "That which is not explicitly forbidden is permitted." Convenient, but prone to zero-day vulnerabilities and unauthorized covert channels.

---

### Classification of Firewalls

#### 1. Packet Filtering Firewalls (Stateless Packet Filters)
Applies a set of administrative rules to each incoming and outgoing IP packet, forwarding or dropping the packet based on header fields:
- Source and Destination IP addresses
- IP Protocol field (TCP, UDP, ICMP)
- Source and Destination TCP/UDP Port numbers
- TCP Flags (`SYN`, `ACK`, `RST`, `FIN`)
- Network interface on which the packet arrived
- **Limitation**: Stateless. Inspects each packet in isolation without awareness of connection state. Vulnerable to IP spoofing, fragmented packet evasion, and attacks using forged `ACK` flags.

#### 2. Stateful Packet Inspection (SPI) Firewalls
Maintains an internal dynamic **state table** tracking active TCP connections and UDP pseudo-connections:
- When an internal host initiates an outbound TCP connection, the firewall records the source IP, destination IP, source port, destination port, sequence numbers, and connection state (`SYN_SENT`, `ESTABLISHED`).
- Inbound packets from the outside are only permitted if they match an entry in the active state table representing a response to a legitimate internally initiated connection.
- Drops out-of-order sequence numbers, unsolicited `SYN-ACK` packets, and anomalous flag combinations (`NULL`, `XMAS` scans).

#### 3. Application-Level Gateways (Proxy Firewalls)
Acts as a relay or proxy server at the Application Layer (Layer 7):
- Clients connect to the proxy rather than directly to the destination server.
- The proxy parses the full application protocol (HTTP, FTP, SMTP, DNS), inspecting the actual payload commands and data (e.g., examining HTTP GET/POST URLs, filtering file extensions, stripping malicious headers).
- **Strengths**: Extremely secure; completely hides internal IP addresses; full application logging.
- **Limitations**: Higher processing overhead (must reassemble TCP streams and parse protocols in user space); requires custom proxy software for every supported protocol.

#### 4. Circuit-Level Gateways
Operates at the Transport Layer (Layer 4) (e.g., SOCKS protocol - RFC 1928):
- Sets up two separate TCP connections: one between the internal client and the gateway, and one between the gateway and the external server.
- Once both connections are established, the circuit-level gateway simply relays TCP segments back and forth without inspecting the application-layer payload.
- More lightweight than an Application Gateway while still preventing direct end-to-end IP connections.

```
       Comparison of Firewall Inspection Layers
  Application Layer Gateway ──► Inspects HTTP, SMTP, FTP commands & payloads (L7)
  Circuit-Level Gateway     ──► Inspects TCP handshake & connection circuits (L4/L5)
  Stateful Inspection (SPI) ──► Inspects TCP state table & sequence numbers (L3/L4)
  Packet Filtering Firewall ──► Inspects static IP headers & port numbers (L3/L4)
```

---

### Firewall Configurations and Architectures
1. **Screened Host Firewall (Single-Homed Bastion)**:
   - Consists of a packet-filtering router and a single-homed bastion host situated on the internal network.
   - The packet filter forces all incoming traffic to route only to the bastion host. If the router's filtering is breached, the internal network is directly exposed.
2. **Screened Host Firewall (Dual-Homed Bastion)**:
   - The bastion host has two physical network interfaces: one connected to the external router, and one connected to the internal network.
   - IP routing between interfaces is completely disabled in the operating system kernel, ensuring no packets can pass between networks without being processed by application proxy software on the bastion host.
3. **Screened Subnet Firewall (Demilitarized Zone - DMZ)**:
   - The most secure enterprise configuration. It utilizes **two packet-filtering routers** flanking an isolated buffer network termed the **Demilitarized Zone (DMZ)**:
     - External Router: Filters untrusted Internet traffic and directs public requests only to DMZ servers.
     - DMZ Subnet: Hosts publicly accessible enterprise servers (Web server, public DNS, Mail gateway, Bastion host).
     - Internal Router: Strictly prevents external Internet traffic from reaching the internal corporate network, and monitors DMZ-to-intranet access.
   - If an attacker compromises a public web server in the DMZ, they are still blocked from penetrating the internal corporate network by the internal firewall!

```
                    Screened Subnet (DMZ) Architecture
  Internet ──► [ External Router ] ──► [ DMZ Subnet ] ──► [ Internal Router ] ──► Internal LAN
                                              │
                              ┌───────────────┴───────────────┐
                              ▼                               ▼
                      Public Web Server               Corporate Mail Gateway
```

### Encrypted Tunnels and Virtual Private Networks (VPNs)
An **encrypted tunnel** is a secure, authenticated communications channel established across an untrusted intermediate network (the public Internet) by encapsulating encrypted packets inside standard transport packets:
- **IPsec Tunnel Mode**: The entire original IP packet (with original internal IP header) is encrypted, prepended with an ESP header, and wrapped inside a new routable outer IP header.
- **Requirements for Encrypted Tunnels**:
  1. *Tunnel Endpoint Authentication*: Cryptographic proof of gateway identities before tunnel activation.
  2. *Payload Confidentiality*: Strong symmetric encryption of all tunnel traffic.
  3. *Integrity & Anti-Replay*: Ensuring encapsulated packets cannot be modified, injected, or replayed.
  4. *Transparent Routing*: The tunnel endpoints encapsulate and decapsulate packets transparently, allowing hosts on private internal subnets (e.g., `10.0.0.0/8` and `192.168.1.0/24`) to communicate across public networks without needing public IP addresses.

### Limitations of Firewalls
Despite being vital perimeter defenses, firewalls suffer from fundamental limitations:
1. **Cannot Protect Against Internal Attacks**: Cannot defend against insider threats, disgruntled employees, or compromised machines already behind the firewall.
2. **Bypassed by Rogue Connections**: Cannot defend against traffic that bypasses the perimeter (e.g., unauthorized cellular tethering, rogue Wi-Fi hotspots, or unauthorized VPNs).
3. **Cannot Defend Against Social Engineering**: Phishing emails, malicious USB drives plugged into workstations, and credential theft easily bypass firewall filters.
4. **Limited Visibility into Encrypted Traffic**: Standard packet filters cannot inspect the contents of encrypted TLS/HTTPS streams (port 443) without specialized SSL-decryption interception proxies.

---

## 2. Example: Packet Filtering Rule Table
Enterprise rule table implementing a **Default Deny** policy:
| Rule # | Direction | Source IP | Destination IP | Protocol | Source Port | Dest Port | Action | Purpose |
|---|---|---|---|---|---|---|---|---|
| **1** | Inbound | External | `192.168.1.10` | TCP | $> 1023$ | 25 | **Permit** | Inbound SMTP to mail server |
| **2** | Inbound | External | `192.168.1.20` | TCP | $> 1023$ | 80, 443 | **Permit** | Inbound HTTP/HTTPS to web server |
| **3** | Outbound | Internal | External | TCP | $> 1023$ | 80, 443 | **Permit** | Internal users web browsing |
| **4** | Inbound | External | Internal | TCP | 80, 443 | $> 1023$ (ACK=1) | **Permit** | Web replies to internal users |
| **5** | Any | Any | Any | Any | Any | Any | **Deny & Log** | **Default Deny Catch-all** |

---

## 3. Applications & Use Cases
1. **Cloud Security Groups & VPC Firewalls (AWS / Azure / GCP)**: Enforcing stateful inbound and outbound micro-segmentation rules between web, application, and database subnets.
2. **Next-Generation Firewalls (Palo Alto Networks / Fortinet FortiGate)**: Combining stateful packet filtering, deep packet inspection (DPI), TLS decryption, and antivirus scanning at line rates.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Evaluation of IP Spoofing Attack on Stateless Packet Filter
**Problem**:
An internal corporate network has subnet `192.168.1.0/24`. A stateless packet filter has the rule:
`Permit Inbound if Source IP == 192.168.1.*` (intended for remote workers).
Show how an external attacker exploits this rule, and how the firewall must be configured to stop it.

**Step-by-step Solution**:
1. **The Attack**:
   - An external attacker on the Internet crafts an IP packet with a forged source IP: `Source IP = 192.168.1.50`, `Dest IP = 192.168.1.10` (internal server).
   - The packet arrives on the firewall's **external interface**.
   - The stateless packet filter checks only the rule: "Is Source IP == 192.168.1.*?" $\rightarrow$ YES! The packet is forwarded directly to the internal server.
2. **The Countermeasure (Ingress & Egress Filtering - RFC 2827 / BCP 38)**:
   - Configure interface-bound directional checks:
     `Deny Inbound on External Interface if Source IP == 192.168.1.0/24`
   - An internal address should *never* arrive from an external physical network link. Any packet with an internal source address arriving on the external interface is immediately dropped as spoofed.

---

### Example 2: Stateful Inspection Table Life Cycle
**Problem**:
Trace the state table entries for a client `$192.168.1.5$` establishing an HTTPS connection to server `$203.0.113.8$`.

**Step-by-step Solution**:
1. Client sends TCP SYN: `192.168.1.5:54321` $\rightarrow$ `203.0.113.8:443`, `Flags = SYN`.
   - Firewall creates dynamic table entry:
     `{Src: 192.168.1.5, Dst: 203.0.113.8, SrcPort: 54321, DstPort: 443, State: SYN_SENT, Timeout: 30s}`.
2. Server responds with TCP SYN-ACK: `203.0.113.8:443` $\rightarrow$ `192.168.1.5:54321`, `Flags = SYN-ACK`.
   - Inbound firewall matches the packet to the active state table entry. Packet is permitted! State updates to `ESTABLISHED`, timeout extended to 3600s.
3. Client sends FIN: `Flags = FIN`. State changes to `FIN_WAIT`.
4. When connection terminates, the dynamic table entry is purged from memory, automatically closing the temporary inbound hole.

---

### Example 3: Calculation of Proxy Firewall Latency Overhead
**Problem**:
A 100 Mbps packet stream passes through an Application-Level Gateway. If context switching and deep packet reconstruction introduce a 1.5 ms delay per 1500-byte packet, calculate the queuing delay and throughput degradation compared to a line-rate hardware packet filter running at 10 microseconds per packet.

**Step-by-step Solution**:
- Hardware packet filter: $10 \ \mu\text{s} = 0.01\text{ ms}$ processing time.
- Application Gateway: $1.5\text{ ms} = 1500 \ \mu\text{s}$ processing time.
- Processing delay ratio: $\frac{1.5\text{ ms}}{0.01\text{ ms}} = 150\times$ increase in packet processing latency.
- Application proxies trade throughput and latency for deep protocol inspection and granular access control.

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q10 - 4 Marks]
**Question**: What are the characteristic features of stateful inspection firewall?

**Solution**:
A **Stateful Packet Inspection (SPI) Firewall** improves upon static packet filtering by actively tracking the state of all ongoing network connections:

1. **State Table Tracking**:
   The firewall maintains a dynamic in-memory **state table** that stores session attributes for each active TCP connection and UDP pseudo-connection (Source IP, Destination IP, Source Port, Destination Port, TCP Sequence Numbers, and Connection State such as `SYN_SENT`, `ESTABLISHED`, `FIN_WAIT`).
2. **Context-Aware Inbound Filtering**:
   Inbound packets from external untrusted networks are only permitted if they correspond to an active, legitimate outbound connection recorded in the state table. Unsolicited inbound packets attempting to access internal hosts are dropped automatically without requiring manual rules.
3. **Protocol State Verification**:
   The firewall validates that packets conform to valid TCP protocol transitions. It verifies TCP sequence numbers and flags, immediately detecting and rejecting spoofed packets, out-of-sequence segments, or abnormal flag scans (`NULL`, `XMAS`, `SYN-FIN`).
4. **Dynamic Port Negotiation for Multi-Channel Protocols**:
   For complex protocols that negotiate auxiliary data ports dynamically (such as FTP, SIP, or H.323), the stateful firewall inspects control commands, automatically opens temporary dynamic pinholes for the agreed data ports, and closes them as soon as the transfer concludes.

---

### Question 2 [KTU May 2019, Part D, Q18(c) / June 2022, Part A, Q9 - 2 to 4 Marks]
**Question**: What are the requirements of Encrypted Tunnels? Explain encrypted tunnels.

**Solution**:
1. **Definition of Encrypted Tunnels**:
   An **encrypted tunnel** is a secure, authenticated point-to-point communication channel established across an insecure public network (such as the Internet) by encapsulating encrypted packets inside standard routable IP packets. Encrypted tunnels form the technical foundation of Virtual Private Networks (VPNs).

2. **Core Requirements of Encrypted Tunnels**:
   - **Tunnel Endpoint Authentication**: Both tunnel endpoints (routers, firewalls, or VPN clients) must mutually authenticate their identities using certificates, digital signatures, or pre-shared keys before bringing up the tunnel.
   - **Data Confidentiality (Payload Encryption)**: All data flowing through the tunnel must be encrypted with strong symmetric ciphers (e.g., AES-GCM, AES-CBC) so that intermediate eavesdroppers cannot inspect the traffic.
   - **Data Integrity & Source Authentication**: The tunnel must calculate cryptographic checksums (e.g., HMAC-SHA256) over every encapsulated packet to ensure packets are not modified or forged in transit.
   - **Anti-Replay Defense**: Monotonic sequence numbers and sliding windows must be enforced to prevent adversaries from intercepting and re-injecting valid tunnel packets.
   - **Transparent Protocol Encapsulation**: Must allow private non-routable IP addresses (RFC 1918) to traverse public networks transparently by encapsulating internal headers inside new routable outer IP headers.

---

### Question 3 [KTU May 2019, Part D, Q19(c) - 6 Marks]
**Question**: Discuss different Firewall configurations.

**Solution**:
Firewalls are deployed in three standard configurations:

1. **Screened Host Firewall (Single-Homed Bastion)**:
   - Consists of a packet-filtering router connected to the Internet and a single-homed bastion host residing on the internal corporate network.
   - The packet filter is configured so that all incoming external traffic is forced to terminate only on the bastion host.
   - *Limitation*: Because the bastion host sits directly on the internal network, if an attacker compromises the router's filtering table, they gain direct, unfettered access to internal hosts.

2. **Screened Host Firewall (Dual-Homed Bastion)**:
   - The bastion host is equipped with two separate network interface cards (NICs): one connects directly to the external router, and the other connects to the internal network.
   - IP packet forwarding (routing) between the two interfaces is completely disabled in the operating system kernel.
   - All external traffic must terminate at an application proxy on the bastion host, which inspects the data before generating a new connection to the internal network. Highly secure, but creates a single point of failure and performance bottleneck.

3. **Screened Subnet Firewall (Demilitarized Zone - DMZ)**:
   - The most secure and widely deployed enterprise architecture. It creates an isolated network segment called the **Demilitarized Zone (DMZ)** positioned between two packet-filtering routers:
     - **External Router**: Connects to the Internet. Forwards incoming traffic only to public-facing servers in the DMZ (Web, DNS, Mail).
     - **DMZ Network**: Contains public bastion hosts and servers.
     - **Internal Router**: Connects the DMZ to the private internal corporate network.
   - *Security Advantage*: Provides defense-in-depth through two distinct layers of filtering. An attacker who compromises a public web server in the DMZ remains isolated from the internal network by the internal firewall.

---

### Question 4 [KTU January 2023, Part A, Q10 - 4 Marks]
**Question**: Describe the limitations of Firewalls.

**Solution**:
While firewalls are indispensable perimeter security controls, they have significant inherent limitations:
1. **Inability to Defend Against Insider Threats**:
   Firewalls monitor only traffic crossing the network perimeter. They cannot detect or prevent malicious actions, data theft, or malware propagation originating from internal employees or compromised devices already located behind the firewall.
2. **Bypass via Alternative Transmission Paths**:
   Firewalls can be completely circumvented if internal devices establish rogue connections that bypass the perimeter firewall (e.g., dial-up modems, unauthorized 4G/5G mobile cellular hotspots, or rogue personal Wi-Fi access points).
3. **Vulnerability to Social Engineering & Phishing**:
   A firewall cannot prevent an internal user from clicking on a phishing link inside an authorized web session or opening a malicious trojan attachment received over legitimate email ports.
4. **Blindness to Encrypted Malicious Payloads**:
   Modern network traffic is overwhelmingly encrypted using TLS/HTTPS (Port 443). Unless the firewall is equipped with active TLS-decryption interception capabilities, it cannot inspect encrypted application payloads for malware or data exfiltration.
5. **Software Vulnerabilities and Configuration Errors**:
   Firewalls are complex software systems. Misconfigured access control lists (ACLs) or unpatched software bugs in the firewall operating system can leave the entire organization vulnerable to penetration.
