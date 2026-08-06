# Module 5 — Topic 2: BGP, Internet Multicasting (IGMP) & IPv6 Protocol Suite (Addressing, Header, Migration & ICMPv6)

> **Module 5**: Internet Control Protocols, Multicasting & IPv6  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
As global internetworks expand, specialized protocols manage inter-domain routing, multicast group delivery, and the transition to the 128-bit IPv6 architecture.

---

### 1. Internet Multicasting & IGMP Protocol
- **Multicasting**: Efficient transmission of data from 1 sender to a specific group of subscribed hosts (Class D addresses `224.0.0.0` to `239.255.255.255`).
- **Ethernet Multicast MAC Mapping**:
  - IPv4 multicast addresses are mapped to Ethernet MAC addresses with prefix `01:00:5E` followed by the low-order 23 bits of the IP multicast address.
- **IGMP (Internet Group Management Protocol)**:
  - Operates between hosts and their local multicast router to manage group memberships.
  - *Membership Query*: Router periodically sends queries to check if any host belongs to a multicast group.
  - *Membership Report*: Hosts reply specifying which multicast groups they wish to join.
  - *Leave Group*: Host informs router it is leaving a multicast group (IGMPv2/v3).
  - *IGMP Snooping*: Layer 2 switches inspect IGMP messages to forward multicast traffic only to ports with active subscribers rather than flooding.
- **Multicast Routing Protocols**: Uses **Reverse Path Forwarding (RPF)**, DVMRP, or PIM (Protocol Independent Multicast: Dense Mode PIM-DM / Sparse Mode PIM-SM with Rendezvous Points).

---

### 2. IPv6 Protocol: Addressing Architecture
IPv6 extends the address space from 32 bits to **128 bits** ($3.4 \times 10^{38}$ unique addresses), written as 8 colon-separated hexadecimal hextets (`2001:0db8:85a3:0000:0000:8a2e:0370:7334`).

#### Compression Rules (RFC 5952):
1. **Omit Leading Zeros**: `0db8` becomes `db8`; `0000` becomes `0`.
2. **Double Colon (`::`)**: Replace the longest contiguous sequence of all-zero hextets with `::` (can be used only **once** per address to prevent ambiguity).

#### IPv6 Address Scopes:
- **Global Unicast Address (`2000::/3`)**: Publicly routable internet addresses.
- **Link-Local Address (`fe80::/10`)**: Used for communication within a single local link; auto-configured using EUI-64.
- **Unique Local Address (`fc00::/7`)**: Private non-routable organizational addresses (analogous to RFC 1918 IPv4).
- **Multicast Address (`ff00::/8`)**: Replaces IPv4 broadcast; includes all-nodes (`ff02::1`) and all-routers (`ff02::2`).
- **Loopback Address (`::1/128`)**: Equivalent to IPv4 `127.0.0.1`.

#### EUI-64 Interface Identifier Generation:
Converts a 48-bit MAC address (e.g. `00:11:22:33:44:55`) into a 64-bit interface ID by inserting `FF-FE` in the middle and flipping the 7th bit (Universal/Local bit) $\implies$ `0211:22ff:fe33:4455`.

---

### 3. IPv6 Packet Format
```text
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version| Traffic Class |           Flow Label                  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Payload Length        |  Next Header  |   Hop Limit   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                         Source Address                        +
|                           (128 bits)                          |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                      Destination Address                      +
|                           (128 bits)                          |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```
- **Base Header**: Fixed **40 Bytes** (8 fields). Removed header checksum to accelerate router processing.
- **Extension Headers**: Optional headers chained between the base IPv6 header and upper-layer payload via the `Next Header` field (e.g., Hop-by-Hop Options, Routing, Fragment, ESP/AH Security).

---

### 4. IPv4-to-IPv6 Migration Issues & Strategies
- **Migration Issues**: IPv4 and IPv6 headers are incompatible. Millions of routers cannot be upgraded overnight.
- **Transition Strategies**:
  1. **Dual Stack**: Routers and hosts run both IPv4 and IPv6 protocol stacks simultaneously.
  2. **Tunneling (6to4 / 4in6)**: Encapsulating IPv6 packets inside IPv4 headers to cross IPv4-only intermediate networks.
  3. **Header Translation (NAT-PT / SIIT)**: Translates IPv6 packet headers directly into IPv4 headers at border gateways.

---

### 5. ICMPv6 & Neighbor Discovery Protocol (NDP)
**ICMPv6** combines ICMPv4, IGMP, and ARP functionality into a unified protocol.

#### Neighbor Discovery Protocol (NDP) Messages:
1. **Router Solicitation (RS) & Router Advertisement (RA)**:
   - Hosts broadcast RS; routers reply with RA containing network prefixes. Enables **SLAAC (Stateless Address Autoconfiguration)**.
2. **Neighbor Solicitation (NS) & Neighbor Advertisement (NA)**:
   - Replaces IPv4 ARP. Resolves IPv6 addresses to MAC addresses and performs **Duplicate Address Detection (DAD)**.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: IPv6 Address Compression Trace (RFC 5952)
**Problem:** Compress the following 128-bit IPv6 address: `fe80:0000:0000:0000:0202:b3ff:fe1e:8329`.
**Step-by-step Solution:**
1. **Remove Leading Zeros in Each Hextet:**
   `fe80:0:0:0:202:b3ff:fe1e:8329`
2. **Replace Longest Sequence of Zero Hextets with `::`:**
   The sequence `:0:0:0:` has 3 zero hextets.
3. **Compressed Address:** **`fe80::202:b3ff:fe1e:8329`**

### Example 2: EUI-64 Interface Identifier Generation
**Problem:** A host has MAC address `00:1A:2B:3C:4D:5E`. Generate its 64-bit EUI-64 Link-Local IPv6 address.
**Step-by-step Solution:**
1. **Split MAC into two 24-bit halves:** `00:1A:2B` and `3C:4D:5E`.
2. **Insert `FF-FE` in the middle:** `001A:2BFF:FE3C:4D5E`.
3. **Invert 7th Bit (U/L Bit) of First Byte:**
   - First byte $= 00_{16} = 00000000_2$.
   - Invert 7th bit $\implies 00000010_2 = 02_{16}$.
4. **Resulting Interface ID:** `021a:2bff:fe3c:4d5e`.
5. **Combine with Link-Local Prefix (`fe80::/64`):**
   **`fe80::21a:2bff:fe3c:4d5e`**

### Example 3: BGP Path Vector Loop Detection Trace
**Problem:** Router in AS 400 receives two BGP path advertisements for destination `1.1.1.0/24`:
- Path 1: `[AS 400 -> AS 300 -> AS 100]`
- Path 2: `[AS 500 -> AS 200 -> AS 100]`
Show how BGP detects routing loops and selects the active path.
**Step-by-step Solution:**
1. Path 1 contains `AS 400` in its AS-Path vector. Receiving router belongs to `AS 400` $\implies$ **Path 1 rejected** (loop detected).
2. Path 2 does not contain `AS 400` $\implies$ **Path 2 accepted**.

---

## 3. Previous Year Questions & Solutions

1. **"Explain IGMP protocol for multicast group management." [May 2019]**
   - **Solution:**
     **IGMP (Internet Group Management Protocol):** Manages multicast group membership between hosts and local routers over IP.
     **Messages:**
     - *Membership Query*: Router asks hosts which groups they belong to.
     - *Membership Report*: Host reports group membership (`224.0.0.0/4`).
     - *Leave Group*: Host notifies router it is leaving a multicast group.
     **IGMP Snooping:** Layer 2 switches inspect IGMP messages to forward multicast traffic only to subscriber ports.

2. **"Explain IPv6 addressing architecture and base header format. Compare IPv4 and IPv6 headers." [July 2021]**
   - **Solution:**
     **Addressing:** 128 bits (8 hextets in hex notation). Scopes: Global Unicast, Link-Local (`fe80::/10`), Multicast (`ff00::/8`), Anycast.
     **Header Format:** Fixed 40 Bytes (8 fields: Version, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, Src Address, Dst Address). Removed checksum for speed; uses extension headers.

3. **"Explain Neighbor Discovery Protocol (NDP) in ICMPv6 and IPv4-to-IPv6 transition mechanisms." [Dec 2019]**
   - **Solution:**
     **NDP:** Uses ICMPv6 messages:
     - *RS / RA*: Router Solicitation and Advertisement for Stateless Address Autoconfiguration (SLAAC).
     - *NS / NA*: Neighbor Solicitation and Advertisement for address resolution (replacing ARP) and Duplicate Address Detection (DAD).
     **Transition Strategies:** Dual Stack (running both protocols), Tunneling (encapsulating IPv6 in IPv4), and Header Translation (NAT-PT).
