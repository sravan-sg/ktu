# Module 6: Transport Layer & Application Layer Protocols — Detailed Notes Index

> **Course**: CS306 Computer Networks | **Semester**: Semester 6 (S6)

---

## 📖 Module Overview

Module 6 covers Transport Layer services (UDP datagrams, TCP segment header format, 3-way handshake & 4-way teardown connection management, TCP state machine, sliding window flow control, and AIMD congestion control), as well as Application Layer protocols (FTP dual-port architecture, DNS hierarchy & resolution, Electronic Mail SMTP & MIME Base64 encoding, SNMP network management framework, and HTTP/WWW).

---

## 📑 Detailed Topic Guides

1. **[Topic 1: Transport Layer: TCP Segment Header, Connection Management, Sliding Window & Congestion Control](transport-layer-tcp-udp-and-congestion-control.md)**
   - UDP vs TCP comparison.
   - Complete 20-byte TCP Segment Header format ASCII diagram & field descriptions.
   - Connection Management: 3-Way Handshake, 4-Way Teardown, and TCP State Machine.
   - TCP Flow Control & Bytes-Oriented Sliding Window (Silly Window Syndrome & Nagle's Algorithm).
   - TCP Congestion Control: Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery (Tahoe vs Reno).

2. **[Topic 2: Application Layer Protocols: FTP, DNS, Electronic Mail (SMTP), MIME & SNMP](application-layer-protocols-dns-ftp-smtp-http.md)**
   - FTP: Control Connection (Port 21) vs Data Connection (Port 20), Active vs Passive modes.
   - DNS: Hierarchy (Root, TLD, Authoritative), Resource Records (A, AAAA, CNAME, MX, NS), Iterative vs Recursive resolution.
   - Electronic Mail (SMTP): Push protocol over TCP Port 25, Mail Transfer Agent (MTA) & Mail User Agent (MUA), SMTP command sequence.
   - MIME: Multipurpose Internet Mail Extensions headers, Base64 encoding math (33.3% overhead).
   - SNMP: Architecture (Manager, Agent, SMI, MIB), PDU Types (`GetRequest`, `SetRequest`, `Trap`), UDP Ports 161/162.
   - HTTP & WWW: Non-persistent HTTP/1.0 vs Persistent HTTP/1.1.

---

## ⚡ Last-Minute Revision Summary

- **[Module 6 Revision Notes](revision-notes.md)**
