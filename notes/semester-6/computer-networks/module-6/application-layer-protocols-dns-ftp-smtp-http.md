# Module 6 — Topic 2: Application Layer Protocols (DNS, FTP, SMTP, POP3/IMAP, SNMP, HTTP & WWW)

> **Module 6**: Transport Layer & Application Layer Protocols  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
The **Application Layer** (Layer 7) provides high-level protocols directly consumed by user applications and network management services:

#### 1. DNS (Domain Name System)
- Distributed hierarchical database mapping human-readable domain names (e.g. `www.ktu.edu.in`) to IP addresses.
- **Hierarchy**: Root DNS Servers (`.`) $\rightarrow$ Top-Level Domain (TLD) Servers (`.in`, `.com`) $\rightarrow$ Authoritative DNS Servers.
- **Resolution Modes**: *Recursive Query* (DNS server resolves complete name on client's behalf) vs *Iterative Query* (DNS server returns referral to next server in hierarchy).

---

#### 2. FTP (File Transfer Protocol)
- Uses **two separate TCP connections**:
  - *Control Connection* (Port 21): Sends commands/responses (USER, PASS, RETR, QUIT). Remains open during session.
  - *Data Connection* (Port 20): Opened dynamically for transferring actual file content, closes after transfer completes.

---

#### 3. Electronic Mail (SMTP, MIME, POP3, IMAP4)
- **SMTP (Simple Mail Transfer Protocol)**: Push protocol using TCP Port 25 to send ASCII email between mail servers.
- **MIME (Multipurpose Internet Mail Extensions)**: Extends SMTP to support non-ASCII text, binary attachments, audio, and images using headers (`Content-Type`, `Content-Transfer-Encoding`).
- **Email Access Protocols (Pull Protocols)**:
  - **POP3 (Post Office Protocol v3)**: Downloads emails from mail server to client machine (Port 110) and deletes them from server by default. Stateless across devices.
  - **IMAP4 (Internet Message Access Protocol v4)**: Synchronizes email folders on server (Port 143). Emails remain stored on server, allowing seamless access across multiple devices.

---

#### 4. SNMP (Simple Network Management Protocol)
Framework for monitoring and managing network devices (routers, switches, servers) over UDP (Ports 161/162).
- **Structure of Management Information (SMI)**: Defines rules for naming objects and encoding data (ASN.1).
- **Management Information Base (MIB)**: Virtual database of managed objects on a device (e.g., interface packet counts, CPU temperature).
- **SNMP Operations / PDUs**:
  - `GetRequest` / `GetNextRequest`: Manager requests variable values from Agent.
  - `SetRequest`: Manager sets variable value on Agent.
  - `Trap`: Unsolicited notification sent by Agent to Manager when an alert/event occurs (e.g. link failure).

---

#### 5. HTTP (Hypertext Transfer Protocol) & WWW
- Stateless request-response protocol powering the World Wide Web (TCP Port 80 / HTTPS Port 443).
- **HTTP/1.0 (Non-Persistent)**: Opens new TCP connection for every embedded object.
- **HTTP/1.1 (Persistent)**: Reuses single TCP connection for multiple requests (Pipelining).

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
   - Total Latency $= 2 + 20 + 30 + 25 = \mathbf{77 \text{ ms}}$ (identical overall network delay, but places heavy memory load on Root/TLD servers).

### Example 2: Non-Persistent vs Persistent HTTP Web Page Fetch Time
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
3. **Speedup:** Persistent HTTP reduces total page load time by **41.7%**.

### Example 3: MIME Base64 Encoding Expansion Calculation
**Problem:** A user attaches a 300 KB binary image to an email. Calculate the size of the email after MIME Base64 encoding.
**Step-by-step Solution:**
1. **Base64 Encoding Rule:** Converts every 3 Bytes (24 bits) of raw binary data into 4 ASCII characters (32 bits).
2. **Expansion Factor:**
   $$\text{Expansion Factor} = \frac{4}{3} = 1.3333 \quad (33.33\% \text{ overhead})$$
3. **Calculate Encoded Size:**
   $$\text{Encoded Size} = 300 \text{ KB} \times \frac{4}{3} = \mathbf{400 \text{ KB}}$$
   Adding CRLF line breaks every 76 characters adds approximately 1% additional overhead ($\approx 404 \text{ KB}$).

---

## 3. Previous Year Questions & Solutions

1. **"Explain DNS architecture, hierarchy, and resolution mechanisms (Iterative vs Recursive)." [May 2019, July 2021]**
   - **Solution:**
     **Architecture:** Distributed hierarchical naming database. Root (`.`) $\rightarrow$ TLD (`.com`, `.edu`) $\rightarrow$ Authoritative.
     **Iterative Query:** Client/Local DNS contacts Root server. Root returns address of TLD server. Local DNS contacts TLD server. TLD returns address of Authoritative server. Local DNS contacts Authoritative server to get final IP.
     **Recursive Query:** Client asks Local DNS. Local DNS forwards query up the chain to Root, which queries TLD, which queries Authoritative. Result cascades back down to client.

2. **"Differentiate between POP3 and IMAP4 email access protocols." [April 2018]**
   - **Solution:**
     | Feature | POP3 (Post Office Protocol v3) | IMAP4 (Internet Message Access Protocol v4) |
     | :--- | :--- | :--- |
     | **Default Storage** | Downloads emails to local client; deletes from server | Keeps emails stored on central server |
     | **Multi-Device Support**| Poor (messages stored locally on 1 machine) | Excellent (folders synchronized across all devices) |
     | **Bandwidth** | Downloads full email content at once | Allows downloading headers only before full message |
     | **Server State** | Stateless | Stateful (maintains read/unread/flagged status) |

3. **"Explain SNMP architecture, SMI, MIB, and SNMP PDU operations." [Dec 2019]**
   - **Solution:**
     - **Architecture**: SNMP Manager (central station) manages SNMP Agents (routers/switches) over UDP (Ports 161/162).
     - **SMI**: Defines syntax and rules for naming objects using ASN.1.
     - **MIB**: Database of manageably monitored parameters (IP counters, link status).
     - **PDUs**: `GetRequest` (fetches value), `SetRequest` (modifies value), and `Trap` (unsolicited alarm sent from Agent to Manager).
