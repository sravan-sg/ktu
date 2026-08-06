# Module 5 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 5**: Internet Control Protocols, Multicasting & IPv6

---

## 🚀 Submodule 1: Control Protocols (ICMP, ARP, BOOTP)

- **ARP**: Maps IP $\rightarrow$ MAC. Broadcast request (`FF:FF:FF:FF:FF:FF`), unicast reply.
- **ICMP**: Diagnostic error messages. Type 11 (TTL Exceeded used by `traceroute`), Type 8/0 (Echo Request/Reply used by `ping`).
- **BOOTP**: UDP-based protocol (Ports 67/68) to obtain IP address and boot file server at startup.

---

## 🚀 Submodule 2: BGP, IGMP & IPv6

- **BGP**: Inter-domain routing using Path Vector (AS-Path). Runs over TCP Port 179. Prevents loops by rejecting routes containing recipient's AS number.
- **IPv6 Header**: 128-bit addresses, fixed 40-byte header, 8 fields. Removes header checksum to optimize router forwarding.
- **IPv6 Transition**: Dual Stack (run both IPv4 and IPv6), Tunneling (encapsulate IPv6 in IPv4), Header Translation.

---

## 🔢 3 Solved Numerical Micro-Examples

1. **IPv6 Address Compression**: `2001:0db8:0000:0000:0000:ff00:0042:8329` $\rightarrow$ `2001:db8::ff00:42:8329`.
2. **ICMP Traceroute RTT**: TTL 1 probe takes 10 ms to Router 1, router processing 2 ms $\implies$ RTT $= 22 \text{ ms}$.
3. **BGP Loop Prevention**: AS 300 receives AS-Path `[AS 400, AS 300, AS 100]`. Contains `AS 300` $\implies$ REJECT route.
