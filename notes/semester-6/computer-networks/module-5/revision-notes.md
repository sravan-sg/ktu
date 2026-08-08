# Module 5 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 5**: Internet Control Protocols, Multicasting & IPv6

---

## 🚀 Submodule 1: Control Protocols (ICMP, ARP, RARP, BOOTP)

- **ICMP (IP Protocol 1)**: Error reporting feedback for IP.
  - *Type 0/8*: Echo Reply / Echo Request (`ping`).
  - *Type 3*: Destination Unreachable (Code 3: Port Unreachable).
  - *Type 5*: Redirect.
  - *Type 11*: Time Exceeded (`traceroute` TTL expiration).
- **ARP & RARP**:
  - *ARP*: Maps IP address $\rightarrow$ MAC address via broadcast request and unicast reply. Results cached in ARP table.
  - *Proxy ARP*: Router answers ARP requests on behalf of remote hosts.
  - *RARP*: Maps MAC address $\rightarrow$ IP address for diskless hosts.
- **BOOTP**: UDP Ports 67/68 bootstrap protocol using BOOTP Relay Agents to cross router boundaries.

---

## 🚀 Submodule 2: BGP & Internet Multicasting (IGMP)

- **BGP (Border Gateway Protocol)**: Path Vector inter-domain protocol over TCP Port 179. Avoids routing loops by inspecting the `AS-Path` attribute list. Rejects paths containing receiving router's own AS number.
- **IGMP Multicasting**:
  - Class D range: `224.0.0.0/4` (`224.0.0.0` to `239.255.255.255`).
  - Ethernet Multicast MAC Mapping: Prefix `01:00:5E` + 23 low-order IP bits.
  - IGMP Messages: Membership Query, Membership Report, Leave Group.
  - *IGMP Snooping*: Layer 2 switch prunes multicast traffic to subscriber ports only.
  - *Multicast Routing*: Reverse Path Forwarding (RPF), DVMRP, PIM-DM / PIM-SM.

---

## 🚀 Submodule 3: IPv6 Architecture, Header & Migration

- **IPv6 Addressing**: 128 bits (8 hextets in hex).
  - RFC 5952 Compression: Omit leading zeros; replace longest contiguous zero hextets with `::` once.
  - Scopes: Global Unicast (`2000::/3`), Link-Local (`fe80::/10`), Multicast (`ff00::/8`), Loopback (`::1`).
  - EUI-64 Math: Insert `FF-FE` into 48-bit MAC address middle, invert 7th U/L bit.
- **IPv6 Base Header**: Fixed **40 Bytes** (8 fields). Removed checksum for router speed; uses Extension Headers chain.
- **Migration Strategies**: Dual Stack, 6to4 / 4in6 Tunneling, Header Translation (NAT-PT).
- **ICMPv6 / NDP**: Replaces ARP with Neighbor Solicitation (NS) / Advertisement (NA); uses Router Solicitation (RS) / Advertisement (RA) for SLAAC autoconfiguration and Duplicate Address Detection (DAD).

---

## 🔢 3 Solved Numerical Micro-Examples

1. **IPv6 Address Compression**: `fe80:0000:0000:0000:0202:b3ff:fe1e:8329` $\implies$ **`fe80::202:b3ff:fe1e:8329`**.
2. **EUI-64 Interface ID Generation**: MAC `00:11:22:33:44:55`.
   - Insert `FF-FE`: `0011:22FF:FE33:4455`.
   - Flip 7th bit of $00_{16} \implies 02_{16}$.
   - EUI-64 ID: `0211:22ff:fe33:4455` $\implies$ Link-Local Address: **`fe80::211:22ff:fe33:4455`**.
3. **Multicast MAC Mapping**: Multicast IP `224.128.64.32`.
   - Low-order 23 bits in hex: `00:40:20`.
   - Ethernet MAC: **`01:00:5E:00:40:20`**.
