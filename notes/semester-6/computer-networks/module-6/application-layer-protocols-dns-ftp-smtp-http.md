# Module 6 — Topic 2: Application Layer Protocols: FTP, DNS, Electronic Mail (SMTP), MIME & SNMP

> **Module 6**: Transport Layer & Application Layer Protocols  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Application Layer** (Layer 7) contains protocol services consumed by network applications:

---

### 1. FTP (File Transfer Protocol)
- Dual-connection architecture operating over TCP:
  - **Control Connection (Port 21)**: Transmits commands and status responses (e.g. `USER`, `PASS`, `RETR`, `STOR`, `QUIT`). Remains open during the entire session.
  - **Data Connection (Port 20)**: Opened dynamically for transferring actual files or directory listings; closes after each file transfer completes.
- **Active Mode vs Passive Mode**:
  - *Active Mode (PORT)*: Client opens a port and tells server; server initiates connection back to client's data port (fails behind firewalls/NAT).
  - *Passive Mode (PASV)*: Client sends `PASV`; server opens a random unprivileged data port and listens for client connection (firewall-friendly).

---

### 2. DNS (Domain Name System)
- Distributed, hierarchical database mapping human-readable hostnames to IP addresses.
- **DNS Hierarchy**: Root DNS Servers (`.`) $\rightarrow$ Top-Level Domain (TLD) Servers (`.com`, `.in`) $\rightarrow$ Authoritative DNS Servers.
- **Resource Record (RR) Types**:
  - `A`: Maps IPv4 address.
  - `AAAA`: Maps IPv6 address.
  - `CNAME`: Canonical name (alias).
  - `MX`: Mail exchange server.
  - `NS`: Name server for zone.
  - `PTR`: Reverse DNS lookup (IP to domain).
- **Resolution Modes**: *Recursive Query* (DNS server resolves complete name on client's behalf) vs *Iterative Query* (DNS server returns referral to next server in hierarchy).

---

### 3. Electronic Mail: SMTP & MIME
- **SMTP (Simple Mail Transfer Protocol)**:
  - Push protocol using TCP Port 25 to send 7-bit ASCII email between Mail Transfer Agents (MTAs).
  - Command Sequence: `HELO/EHLO` $\rightarrow$ `MAIL FROM:` $\rightarrow$ `RCPT TO:` $\rightarrow$ `DATA` $\rightarrow$ `QUIT`.
- **MIME (Multipurpose Internet Mail Extensions)**:
  - Extends 7-bit ASCII SMTP to support non-ASCII character sets, binary attachments (images, PDFs), and audio.
  - *Headers*: `MIME-Version`, `Content-Type`, `Content-Transfer-Encoding`.
  - *Base64 Encoding*: Groups binary data into 24-bit blocks (3 bytes) and converts them into four 6-bit ASCII characters ($33.3\%$ size overhead).

---

### 4. SNMP (Simple Network Management Protocol)
Framework for monitoring and managing network hardware (routers, switches, servers) over UDP (Ports 161/162).
- **Architecture**:
  - **SNMP Manager**: Central management station running monitoring software.
  - **SNMP Agent**: Software running on managed network devices.
  - **SMI (Structure of Management Information)**: Defines rules for naming objects and encoding data types using ASN.1.
  - **MIB (Management Information Base)**: Virtual database on each device holding monitored parameters (e.g. interface byte counters, CPU temperature).
- **SNMP PDU Operations**:
  - `GetRequest` / `GetNextRequest` / `GetBulkRequest`: Manager retrieves variable values from Agent.
  - `SetRequest`: Manager modifies variable value on Agent (e.g. disables an interface).
  - `Trap` / `InformRequest`: Unsolicited notification sent by Agent to Manager when an alert/event occurs (e.g. link failure).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: DNS Iterative vs Recursive Query Latency Calculation
**Problem:** A client queries its Local DNS Server (RTT = 2 ms) for `www.example.com`.
- Root DNS Server RTT = 20 ms.
- TLD DNS Server (`.com`) RTT = 30 ms.
- Authoritative DNS Server RTT = 25 ms.
Calculate total latency for (a) Iterative DNS Resolution, and (b) Recursive DNS Resolution (assuming all servers process instantly).
**Step-by-step Solution:**
1. **Iterative DNS Resolution:**
   - Client $\rightarrow$ Local DNS: $2 \text{ ms}$.
   - Local DNS $\rightarrow$ Root DNS (returns TLD IP): $20 \text{ ms}$.
   - Local DNS $\rightarrow$ TLD DNS (returns Auth IP): $30 \text{ ms}$.
   - Local DNS $\rightarrow$ Auth DNS (returns final IP): $25 \text{ ms}$.
   - Total Latency $= 2 + 20 + 30 + 25 = \mathbf{77 \text{ ms}}$.
2. **Recursive DNS Resolution:**
   - Chain: Client $\rightarrow$ Local DNS $\rightarrow$ Root DNS $\rightarrow$ TLD DNS $\rightarrow$ Auth DNS $\rightarrow$ return path.
   - Total Latency $= 2 + 20 + 30 + 25 = \mathbf{77 \text{ ms}}$.

### Example 2: MIME Base64 Encoding Expansion Calculation
**Problem:** A user attaches a 300 KB binary image to an email. Calculate the size of the email after MIME Base64 encoding.
**Step-by-step Solution:**
1. **Base64 Encoding Rule:** Converts every 3 Bytes (24 bits) of raw binary data into 4 ASCII characters (32 bits).
2. **Expansion Factor:**
   $$\text{Expansion Factor} = \frac{4}{3} = 1.3333 \quad (33.33\% \text{ overhead})$$
3. **Calculate Encoded Size:**
   $$\text{Encoded Size} = 300 \text{ KB} \times \frac{4}{3} = \mathbf{400 \text{ KB}}$$
   Adding CRLF line breaks every 76 characters adds approximately 1% additional overhead ($\approx 404 \text{ KB}$).

### Example 3: Non-Persistent vs Persistent HTTP Web Page Fetch Time
**Problem:** A web page contains 1 HTML file and 5 embedded JPEG images. RTT between client and server is $10 \text{ ms}$. TCP handshake takes 1 RTT. Calculate total page download time for:
(a) Non-persistent HTTP/1.0 (sequential connections).
(b) Persistent HTTP/1.1 without pipelining.
**Step-by-step Solution:**
1. **Non-Persistent HTTP/1.0:**
   - HTML File: 1 RTT (TCP Handshake) + 1 RTT (HTTP Request/Response) $= 2 \text{ RTTs}$.
   - 5 Images: Each image requires a new TCP handshake ($2 \text{ RTTs}$ per image).
   - Total Time $= 2 + 5 \times 2 = 12 \text{ RTTs} = 12 \times 10 \text{ ms} = \mathbf{120 \text{ ms}}$.
2. **Persistent HTTP/1.1 (Without Pipelining):**
   - HTML File: 1 RTT (TCP Handshake) + 1 RTT (HTTP Request/Response) $= 2 \text{ RTTs}$.
   - 5 Images: Reuses open TCP connection (1 RTT per image).
   - Total Time $= 2 + 5 \times 1 = 7 \text{ RTTs} = 7 \times 10 \text{ ms} = \mathbf{70 \text{ ms}}$.

---

## 3. Previous Year Questions & Solutions

1. **"Explain FTP dual-connection architecture (Control vs Data connections)." [Dec 2019]**
   - **Solution:**
     **Control Connection (Port 21):** Transmits text commands (`USER`, `PASS`, `RETR`) and server status responses. Remains open throughout user session.
     **Data Connection (Port 20):** Opened dynamically when a file transfer command is issued. Transfers raw data bytes and closes upon completion. Out-of-band control allows sending abort signals (`ABOR`) during transfers.

2. **"Explain MIME and Base64 encoding for email attachments." [April 2018]**
   - **Solution:**
     **MIME:** Extends 7-bit ASCII SMTP to support binary attachments and rich media using headers (`MIME-Version`, `Content-Type`, `Content-Transfer-Encoding`).
     **Base64 Encoding:** Takes 24-bit binary blocks (3 bytes), splits into four 6-bit values, and maps each to a 64-character ASCII alphabet (`A-Z`, `a-z`, `0-9`, `+`, `/`), resulting in 33.3% overhead.

3. **"Explain SNMP architecture, SMI, MIB, and PDU operations." [Dec 2019]**
   - **Solution:**
     - **Architecture**: SNMP Manager manages SNMP Agents on network devices over UDP (Ports 161/162).
     - **SMI**: Rules for defining and naming managed objects (ASN.1 syntax).
     - **MIB**: Virtual database of monitored parameters (packet counts, link status).
     - **PDUs**: `GetRequest` (retrieves value), `SetRequest` (modifies value), `Trap` (unsolicited alarm sent by Agent).
