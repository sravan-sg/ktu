# CS306 — Computer Networks

> **Semester**: Semester 6 (S6) | **Scheme**: 2016 | **Credits**: 3 (L-T-P 3-0-0)  
> **Course Syllabus & Guide**: [syllabus.md](syllabus.md) | **Knowledge Base**: [knowledge/README.md](knowledge/README.md)

---

## Grading Criteria

**End-semester per-module weightage (sums to 100%):**

| Modules | Weightage |
|---------|-----------|
| I       | 15 % |
| II      | 15 % |
| III     | 15 % |
| IV      | 15 % |
| V       | 20 % |
| VI      | 20 % |

**Question-paper pattern (end-sem, 100 marks):**

| Part | Marks | Questions | Covers | To answer |
|------|-------|-----------|--------|-----------|
| A | 12 | 4 × 3 | Modules I & II | All 4 |
| B | 18 | 3 × 9 (≤3 subparts each) | Modules I & II | Any 2 |
| C | 12 | 4 × 3 | Modules III & IV | All 4 |
| D | 18 | 3 × 9 (≤3 subparts each) | Modules III & IV | Any 2 |
| E | 40 | 6 × 10 (≤3 subparts each) | Modules V & VI | Any 4 |

- Two internal exams: **First Internal** after Module II, **Second Internal** after Module IV.
- **At least 60 % of questions must be analytical/numerical.**

---

## Textbooks

1. Andrew S. Tanenbaum — *Computer Networks*, 4th ed., PHI. **[Modules 1, 2, 3, 6]**
2. Behrouz A. Forouzan — *Data Communications and Networking*, 4th ed., Tata McGraw Hill. **[Modules 2, 4, 5]**
3. Larry L. Peterson & Bruce S. Davie — *Computer Networks: A Systems Approach*, 5th ed., Morgan Kaufmann, 2011. **[Modules 3, 4, 5, 6]**

**References**

1. Fred Halsall — *Computer Networking and the Internet*, 5th ed.
2. James F. Kurose, Keith W. Ross — *Computer Networking: A Top-Down Approach*, 6th ed.
3. Keshav — *An Engineering Approach to Computer Networks*, Addison Wesley, 1998.
4. Request for Comments (RFC) Pages — IETF (`https://www.ietf.org/rfc.html`).
5. W. Richard Stevens — *TCP/IP Illustrated Volume 1*, Addison-Wesley, 2005.
6. William Stallings — *Computer Networking with Internet Protocols*, Prentice-Hall, 2004.

---

## Modules

### Module I — Network Architecture & Reference Models (7 hrs)
- Introduction and Uses of Computer Networks
- Network Hardware: LAN, MAN, WAN, Internetworks
- Network Software: Protocol hierarchies, Design issues for layers, Interfaces & Services, Service Primitives
- Reference Models: OSI Reference Model vs TCP/IP Reference Model

### Module II — Data Link Layer & Medium Access Control (8 hrs)
- Data Link Layer Design Issues
- Flow Control and ARQ techniques (Stop-and-Wait, Go-Back-N, Selective Repeat)
- Data Link Protocols: HDLC, DLL in Internet
- Medium Access Control (MAC) Sublayer: IEEE 802 for LANs & MANs (802.3 Ethernet, 802.4 Token Bus, 802.5 Token Ring)
- Network Interconnection Devices: Bridges, Switches
- High Speed LANs: Gigabit Ethernet
- Wireless LANs: IEEE 802.11 a/b/g/n, IEEE 802.15 (Bluetooth)
- Point-to-Point Protocol (PPP)

*(First Internal Exam covers Modules I & II.)*

### Module III — Network Layer & Routing Algorithms (7 hrs)
- Network Layer Design Issues
- Routing Algorithms: Shortest Path Routing, Flooding, Distance Vector Routing, Link State Routing
- Routing Protocols: RIP (Routing Information Protocol), OSPF (Open Shortest Path First)
- Routing for Mobile Hosts

### Module IV — Congestion Control, QoS & IPv4 Subnetting (7 hrs)
- Congestion Control Algorithms (Leaky Bucket, Token Bucket, Choke Packets)
- Quality of Service (QoS)
- Internetworking & Network Layer in the Internet
- IPv4 Protocol & Header Structure
- IP Addressing: Classful Addressing, Classless Addressing (CIDR)
- Subnetting and Supernetting Calculations

*(Second Internal Exam covers Modules III & IV.)*

### Module V — Internet Control Protocols, Multicasting & IPv6 (7 hrs)
- Internet Control Protocols: ICMP, ARP, RARP, BOOTP
- Internet Multicasting: IGMP
- Exterior Routing Protocols: BGP (Border Gateway Protocol)
- IPv6 Protocol: Addressing, Packet Format, IPv4-to-IPv6 Migration Issues, ICMPv6

### Module VI — Transport Layer & Application Layer Protocols (7 hrs)
- Transport Layer: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol)
- TCP Segment Header, Connection Management, TCP Congestion Control & Sliding Window
- Application Layer Protocols: FTP, DNS, Electronic Mail (SMTP), MIME, SNMP
- Introduction to World Wide Web (HTTP, HTML, Web Architecture)

---

## Exam Focus — What to Prioritize

- **Modules V & VI carry 40 of 100 marks in Part E alone.** Focus heavily on ICMP, ARP/RARP, BGP, IPv6 transition, TCP connection state machine, TCP vs UDP header fields, and Application protocols (DNS, FTP, SMTP, HTTP).
- **Master Numerical & Analytical Problems (≥60% of marks):**
  1. **IPv4 Subnetting & CIDR Math (Module IV):** Calculating subnet masks, network addresses, broadcast addresses, usable host ranges, and VLSM allocation.
  2. **ARQ Flow Control Calculations (Module II):** Channel efficiency $\eta = \frac{1}{1 + 2a}$ for Stop-and-Wait, Go-Back-N, and Selective Repeat; maximum window size $W \le 2^k - 1$.
  3. **Routing Table Tracing (Module III):** Distance Vector Routing step-by-step distance updates (Bellman-Ford equation) and Link State Dijkstra shortest path trees.
  4. **Leaky Bucket & Token Bucket Math (Module IV):** Maximum burst transmission rate and token bucket capacity calculations.
- **Reference Model Comparisons:** Contrast OSI (7 layers) vs TCP/IP (4/5 layers) with clear protocol mapping — a guaranteed Part A/B theory question.
- **MAC Sublayer & Wireless Standards:** IEEE 802.3 Ethernet vs 802.11 CSMA/CA collision avoidance, hidden/exposed terminal problems, and PPP frame format.
