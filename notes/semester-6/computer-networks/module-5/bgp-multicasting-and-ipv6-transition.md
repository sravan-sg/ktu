# Module 5 — Topic 2: BGP, Internet Multicasting & IPv6 Transition

> **Module 5**: Internet Control Protocols, Multicasting & IPv6  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
As internetworks scale globally across different administrative domains, specialized protocols manage inter-domain routing, multicasting, and address extension:

1. **Exterior Routing Protocol — BGP (Border Gateway Protocol)**:
   - Inter-domain routing protocol used between different **Autonomous Systems (AS)**.
   - Uses **Path Vector Routing**: Advertises the complete sequence of Autonomous System numbers (AS-Path) to reach a destination prefix, preventing routing loops.
   - Operates over reliable TCP connections (Port 179). Policy-driven routing (routing decisions based on business rules rather than shortest path).

2. **Internet Multicasting (IGMP)**:
   - Transmission from 1 sender to a specific group of subscribed hosts (Class D addresses `224.0.0.0/4`).
   - **IGMP (Internet Group Management Protocol)**: Used by hosts to inform local routers of their group membership. Routers use DVMRP or PIM to prune multicast trees.

3. **IPv6 Protocol & Transition Mechanisms**:
   - Designed to replace IPv4, providing **128-bit addresses** ($3.4 \times 10^{38}$ unique IPs).
   - **Simplified Header**: Fixed 40-byte header (8 fields instead of 14 in IPv4). Removes header checksum to speed up router processing.
   - **Transition Mechanisms**:
     - *Dual Stack*: Devices run both IPv4 and IPv6 protocol stacks simultaneously.
     - *Tunneling*: Encapsulating IPv6 packets inside IPv4 headers to cross IPv4-only networks (6to4 tunneling).
     - *Header Translation (NAT-PT)*: Translating IPv6 headers into IPv4 headers at border gateways.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: BGP Path Vector Loop Detection Trace
**Problem:** Router in AS 400 receives two BGP path advertisements for destination prefix `1.1.1.0/24`:
- Path 1: `[AS 400 -> AS 300 -> AS 100]`
- Path 2: `[AS 500 -> AS 200 -> AS 100]`
Show how BGP detects routing loops and selects the active path.
**Step-by-step Solution:**
1. **Loop Detection Check:**
   - Path 1 contains `AS 400` in its AS-Path vector. Since the receiving router belongs to `AS 400`, accepting Path 1 would create a routing loop! **Path 1 is rejected immediately**.
   - Path 2 does not contain `AS 400`. **Path 2 is accepted**.
2. **Result:** Loop-free path vector routing guarantees stability across complex ISP mesh topologies.

### Example 2: IPv6 Header Simplification & Field Comparison
**Problem:** Compare the header size and field efficiency between an IPv4 header (without options) and a base IPv6 header.
**Step-by-step Solution:**
| Feature | IPv4 Base Header | IPv6 Base Header |
| :--- | :--- | :--- |
| **Address Length** | 32 bits (4 Bytes) | 128 bits (16 Bytes) |
| **Header Size** | 20 Bytes (Variable with options) | 40 Bytes (Fixed size) |
| **Field Count** | 14 Fields | 8 Fields |
| **Header Checksum** | Present (Recalculated at every hop) | **Removed** (L2/L4 handle errors) |
| **Fragmentation** | Handled by routers & senders | **Handled ONLY by sender** (PMTU) |
| **Flow Label** | None | 20-bit Flow Label for QoS |

### Example 3: IPv6 Address Colon-Hexadecimal Compression
**Problem:** Compress the uncompressed 128-bit IPv6 address `2001:0db8:0000:0000:0000:ff00:0042:8329` according to standard RFC 5952 rules.
**Step-by-step Solution:**
1. **Remove Leading Zeros in each Hextet:**
   `2001:db8:0:0:0:ff00:42:8329`
2. **Replace Longest Contiguous Run of Zero Hextets with `::`:**
   The run `:0:0:0:` has 3 zero hextets.
3. **Compressed Address:** **`2001:db8::ff00:42:8329`**

---

## 3. Previous Year Questions & Solutions

1. **"Explain the features of IPv6. Compare IPv4 and IPv6 headers." [May 2019, July 2021]**
   - **Solution:**
     **Features:** 128-bit address space, fixed 40-byte header, autoconfiguration (SLAAC), built-in IPsec security, simplified routing without router fragmentation.
     **Comparison:**
     - Address size: 32 bits (IPv4) vs 128 bits (IPv6).
     - Checksum: IPv4 has header checksum; IPv6 removes checksum for processing speed.
     - Fragmentation: Routers fragment in IPv4; only sender fragments in IPv6.
     - Multicast/Broadcast: IPv4 uses broadcast; IPv6 eliminates broadcast, using multicast & anycast.

2. **"Explain BGP protocol and Path Vector routing." [Dec 2019]**
   - **Solution:**
     **BGP (Border Gateway Protocol):** De-facto inter-domain routing protocol of the Internet. Uses Path Vector routing to advertise destination network prefixes along with the sequence of Autonomous Systems (AS-Path) traversed.
     **Path Vector Advantage:** Prevents routing loops because an AS rejects any route listing its own AS number in the path. Allows ISPs to enforce complex commercial and security routing policies.
