# IP Security: Architecture, Protocols, and Operating Modes

## 1. Explanation
**IP Security (IPsec)** is a suite of open cryptographic protocols developed by the Internet Engineering Task Force (IETF, RFC 4301-4309) that operates at the **Network Layer (Layer 3)** of the OSI model. By securing data at Layer 3, IPsec provides transparent security services to all upper-layer applications (TCP, UDP, ICMP, HTTP, FTP) without requiring changes to client or server application code.

### Benefits of IPsec
According to William Stallings (*Cryptography and Network Security*, Chapter 19):
1. **Application Transparency**: Operates below the transport layer (TCP/UDP); individual user applications require zero modification.
2. **Universal Host & Gateway Protection**: When deployed on firewalls or routers, IPsec provides seamless perimeter security for all incoming and outgoing intranet traffic.
3. **Defense Against IP Spoofing**: Eliminates address spoofing and rogue packet injections at the network layer.
4. **Transparent Virtual Private Networks (VPNs)**: Links branch offices and remote workers securely across untrusted public Internet backbones.

### IPsec Architecture Components
1. **Security Associations (SA)**:
   - An SA is a **one-way (simplex)** logical connection between a sender and receiver that specifies the cryptographic security services, algorithms, and keys for protecting traffic.
   - For bidirectional communication, two distinct SAs are required (one inbound, one outbound).
   - An SA is uniquely identified by a 3-tuple:
     $$\text{SA} = \{\text{Security Parameter Index (SPI)}, \ \text{IP Destination Address}, \ \text{Security Protocol Identifier (AH or ESP)}\}$$
2. **Security Association Database (SAD)**:
   - A table maintained by each IPsec entity containing the cryptographic state parameters for each active SA (e.g., Sequence Number Counter, Anti-Replay Window, AH/ESP authentication algorithm and key, ESP encryption algorithm and key, SA lifetime, and Protocol Mode).
3. **Security Policy Database (SPD)**:
   - Relates IP traffic to specific security policies: Discard, Bypass IPsec (allow in clear), or Protect with IPsec (specifying which SA to use).
   - **SA Selectors**: Fields in the packet header used by the SPD to map traffic to an SA. Standard selectors include:
     - Source and Destination IP Addresses (single IP, subnet, or wildcard range)
     - Transport Layer Protocol (TCP, UDP, ICMP)
     - Source and Destination Port numbers

### The Two Core IPsec Protocols

#### 1. Authentication Header (AH - Protocol ID 51)
Provides data integrity, data origin authentication, and an optional anti-replay service for IP packets, but **does NOT provide confidentiality** (payload remains visible in cleartext).
- **Integrity Check Value (ICV)**:
  - Computed using HMAC (HMAC-SHA1 or HMAC-MD5) over the entire IP packet, including both the payload and the IP header fields.
  - **Mutable Fields Rule**: Header fields whose values may legitimately change during transit across intermediate routers (e.g., Time to Live - TTL, Header Checksum, Type of Service/DSCP) are zeroed out before computing the ICV. Non-mutable fields (Source/Destination IP addresses) are protected!

#### 2. Encapsulating Security Payload (ESP - Protocol ID 50)
Provides confidentiality, message authentication, data integrity, and anti-replay protection. ESP can be configured to provide encryption only, authentication only, or both encryption and authentication simultaneously.

#### The ESP Header and Packet Format
An ESP packet wraps the protected payload as follows:
```
  ┌──────────────────────────────────────────────────────────────┐
  │                   ESP Packet Layout                          │
  ├──────────────────────────────────────────────────────────────┤
  │ ESP Header:                                                  │
  │   - Security Parameter Index (SPI) : 32 bits                 │
  │   - Sequence Number                : 32 bits                 │
  ├──────────────────────────────────────────────────────────────┤
  │ Payload Data (Encrypted)           : Variable                │
  │   - TCP/UDP header + user data                               │
  ├──────────────────────────────────────────────────────────────┤
  │ Padding (Encrypted)                : 0 - 255 bytes           │
  │ Pad Length (Encrypted)             : 8 bits                  │
  │ Next Header (Encrypted)            : 8 bits                  │
  ├──────────────────────────────────────────────────────────────┤
  │ Integrity Check Value (ICV)        : Variable (96-128 bits)  │
  │   - Authenticates: SPI through Next Header                   │
  └──────────────────────────────────────────────────────────────┘
```
- **Fields in Detail**:
  - `Security Parameter Index (SPI)` (32 bits): Arbitrary 32-bit tag identifying the matching SA in the recipient's SAD.
  - `Sequence Number` (32 bits): Strictly increasing monotonic counter; prevents packet replay attacks.
  - `Payload Data` (Variable): The encrypted upper-layer transport packet or original IP packet.
  - `Padding` (0 to 255 bytes): Required by block ciphers to align ciphertext to multi-byte boundaries, or to conceal traffic length.
  - `Pad Length` (8 bits): Specifies the number of padding bytes preceding this field.
  - `Next Header` (8 bits): Identifies the protocol contained in the payload (e.g., 6 for TCP, 17 for UDP, 4 for IPv4).
  - `Integrity Check Value (ICV)`: Message authentication code computed over the ESP packet from the SPI field to the Next Header field.

### Operational Modes: Transport Mode vs. Tunnel Mode

| Comparison Attribute | Transport Mode | Tunnel Mode |
|---|---|---|
| **Primary Deployment** | Host-to-Host (End-to-End) communication between two endpoints. | Gateway-to-Gateway (Firewall-to-Firewall) or Host-to-Gateway (VPN access). |
| **What is Protected** | Only the upper-layer payload (TCP/UDP segments). Original IP header is NOT encrypted. | The entire original IP packet (including original source and destination IP headers). |
| **IP Header Architecture** | Uses the **Original IP Header** with modified protocol field (50 for ESP, 51 for AH). | Prepends a **New Outer IP Header** containing the firewall/gateway IP addresses. |
| **Traffic Flow Confidentiality** | Low: An observer on the network can see true source and destination IP addresses. | High: True endpoint IP addresses are completely hidden inside the encrypted tunnel payload. |

```
  TRANSPORT MODE (ESP):
  [ Original IP Header ] [ ESP Header ] [ TCP Segment (Encrypted) ] [ ESP Trailer ] [ ESP ICV ]
                                        |◄──────── Encrypted ─────►|
                         |◄──────────────── Authenticated ────────────────────────►|

  TUNNEL MODE (ESP):
  [ New IP Header ] [ ESP Header ] [ Original IP Header + TCP (Encrypted) ] [ ESP Trailer ] [ ESP ICV ]
                                   |◄─────────────── Encrypted ──────────►|
                    |◄──────────────────────── Authenticated ─────────────────────────────────►|
```

---

## 2. Example: Combining Security Associations (SA Bundles)
An individual SA provides either AH or ESP, but not both in different modes. To satisfy complex security policies, SAs are concatenated into an **SA Bundle**:
- **Transport-Adjacent Bundle**: A transport-mode AH is combined with a transport-mode ESP on the same host to provide both strong authentication across the IP header and payload encryption.
- **Iterated Tunneling (VPN inside a VPN)**: A secure corporate tunnel is nested inside a commercial service-provider tunnel.

---

## 3. Applications & Use Cases
1. **Site-to-Site Enterprise VPNs**: Connecting corporate headquarters with international branch offices over the public Internet via IPsec Tunnel Mode.
2. **Remote Worker VPN Clients (Cisco AnyConnect / strongSwan)**: Enabling telecommuters to securely access internal enterprise intranets from laptops.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: ESP Packet Overhead Calculation
**Problem**:
An application sends a 100-byte UDP packet (20-byte IP header + 8-byte UDP header + 72-byte payload). Calculate the total packet size when encapsulated using AES-CBC (16-byte block size) and HMAC-SHA1 in IPsec Transport Mode.

**Step-by-step Solution**:
1. In Transport Mode, the 20-byte IP header is placed at the front.
2. The payload to be encrypted consists of:
   - UDP header: 8 bytes
   - Data payload: 72 bytes
   - Total unpadded payload = $8 + 72 = 80$ bytes.
3. AES-CBC requires padding such that:
   $$(\text{Payload} + \text{Pad Length (1)} + \text{Next Header (1)} + \text{Padding}) \equiv 0 \pmod{16}$$
   $$80 + 1 + 1 + \text{Padding} = 82 + \text{Padding}$$
   The next multiple of 16 above 82 is 96.
   $$\text{Padding} = 96 - 82 = \mathbf{14 \text{ bytes}}$$
4. Encrypted block size = $96$ bytes.
5. Add ESP Header (SPI: 4 bytes, Sequence Number: 4 bytes) = 8 bytes.
6. Add ESP Authentication ICV (HMAC-SHA1-96) = 12 bytes.
7. Add Original IP Header = 20 bytes.
8. Total packet size on the wire:
   $$\text{Total} = 20 + 8 + 96 + 12 = \mathbf{136 \text{ bytes}}$$
   Overhead = $136 - 100 = 36$ bytes.

---

### Example 2: Anti-Replay Sliding Window Mechanism
**Problem**:
Explain how IPsec defends against packet replay attacks using the 32-bit Sequence Number and a 64-packet Sliding Window.

**Step-by-step Solution**:
- Sender increments the Sequence Number monotonically for every packet ($1, 2, 3 \dots$). The counter never cycles back to zero; if it reaches $2^{32}-1$, the SA is renegotiated.
- Receiver maintains a sliding window of size $W = 64$ packets, anchored at the highest valid sequence number received ($N$):
  1. If incoming packet has sequence number $> N$: It is in advance of the window. The packet is authenticated; if valid, the window advances so that the new packet becomes the right edge, and its bit is marked.
  2. If incoming packet has sequence number within $[N - W + 1, N]$: The receiver checks the window bitmask. If the bit is already marked, the packet is a **replayed duplicate and is instantly discarded**. If unmarked, it is authenticated; if valid, its bit is marked.
  3. If incoming packet has sequence number $< N - W + 1$: The packet is too old (outside the window) and is **immediately dropped without cryptographic verification**, mitigating denial-of-service CPU exhaustion.

---

### Example 3: Comparison of AH vs. ESP
**Problem**:
Summarize the comparative capabilities of AH and ESP in tabular format.

**Solution**:
| Security Service | AH (Authentication Header) | ESP (Encapsulating Security Payload) |
|---|---|---|
| **Confidentiality** | NO | YES (Optional, AES/3DES) |
| **Data Origin Authentication** | YES | YES (Optional, HMAC-SHA) |
| **Data Integrity** | YES | YES |
| **Anti-Replay Protection** | YES | YES |
| **Protects Outer IP Header** | YES (Non-mutable fields) | NO (Only from SPI downward) |
| **NAT Traversal (NAT-T)** | BROKEN by NAT (NAT changes IP addresses, breaking AH ICV) | Supported via UDP encapsulation (Port 4500) |

---

## 5. Previous Year Questions & Solutions

### Question 1 [KTU May 2019, Part A, Q7 - 4 Marks]
**Question**: Give the header format of ESP in IPSec.

**Solution**:
The Encapsulating Security Payload (ESP) packet consists of an ESP Header, the encrypted Payload, the ESP Trailer, and the Integrity Check Value (ICV):

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|               Security Parameters Index (SPI)                 |  ESP Header
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  (Unencrypted)
|                      Sequence Number                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Payload Data (variable)                    |  Encrypted
~                                                               ~  Payload
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Padding (0-255 bytes)                      |  ESP Trailer
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  (Encrypted)
|          Pad Length           |          Next Header          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                 Integrity Check Value (ICV)                   |  ESP Auth
~                          (variable)                           ~  (Unencrypted)
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Description of Fields**:
1. **Security Parameters Index (SPI) (32 bits)**: An arbitrary 32-bit integer that uniquely identifies the Security Association (SA) for this packet in the receiver's Security Association Database (SAD).
2. **Sequence Number (32 bits)**: A strictly increasing counter value. Used by the receiver to provide anti-replay protection.
3. **Payload Data (Variable)**: Contains the encrypted transport-layer segment (Transport Mode) or complete encapsulated IP packet (Tunnel Mode).
4. **Padding (0-255 bytes)**: Extra bytes added to satisfy block cipher size alignment (e.g., 16-byte multiple for AES) or to conceal plaintext packet length.
5. **Pad Length (8 bits)**: Indicates the number of padding bytes immediately preceding it.
6. **Next Header (8 bits)**: Identifies the type of payload contained in the Payload Data field (e.g., 6 for TCP, 17 for UDP, 4 for IPv4 in Tunnel Mode).
7. **Integrity Check Value (ICV) (Variable, typically 96 or 128 bits)**: A message authentication code computed over the ESP packet from the SPI to the Next Header field.

---

### Question 2 [KTU May 2019, Part D, Q17(c) - 3 Marks]
**Question**: How the integrity is achieved using ICV in Authentication Header?

**Solution**:
In the IPsec Authentication Header (AH), integrity and origin authenticity are achieved through the **Integrity Check Value (ICV)**:
1. **Cryptographic Algorithm**: The ICV is calculated using a keyed Message Authentication Code (MAC) such as HMAC-SHA1-96, HMAC-MD5-96, or AES-XCBC-MAC over the packet data.
2. **Scope of Coverage**: The AH ICV covers:
   - The IP header fields that do not change in transit.
   - The entire Authentication Header (with the ICV field temporarily zeroed out).
   - The entire upper-layer protocol payload (e.g., TCP segment and user data).
3. **Handling Mutable vs. Immutable IP Header Fields**:
   - Because intermediate routers along the Internet path routinely modify certain IP header fields (e.g., Time to Live - TTL, Header Checksum, DSCP/TOS, Hop Count), including these fields would cause the ICV verification to fail at the destination.
   - Therefore, before computing the ICV, the sender **zeros out all mutable IPv4 fields** (TTL, Header Checksum, TOS, Flags/Fragment Offset).
   - **Immutable fields** (Source IP Address, Destination IP Address, Protocol, Version, Header Length) are left intact and authenticated by the ICV.
4. **Verification at Receiver**:
   The receiver extracts the packet, zeros out the mutable fields and the received ICV field, recalculates the HMAC using the shared SA key, and compares it to the received ICV. If they match, the packet is confirmed unmodified and authentic.

---

### Question 3 [KTU May 2019, Part D, Q19(a) - 4 Marks]
**Question**: Give the significance of SA selectors in IPSec.

**Solution**:
In the IPsec architecture (RFC 4301), **Security Association (SA) Selectors** are specific fields extracted from inbound and outbound network packets that are matched against the rules in the **Security Policy Database (SPD)**:
1. **Significance & Role**:
   - The SPD defines *what* security policies should be applied to network traffic (Discard, Bypass IPsec, or Protect with IPsec).
   - SA selectors act as the filtering criteria that map a packet to a specific policy entry in the SPD, and consequently to an active Security Association (SA) in the Security Association Database (SAD).
2. **Standard SA Selectors**:
   - **Source IP Address**: Single host IP, IP address range, or wildcard subnet of the sender.
   - **Destination IP Address**: Single host IP, IP address range, or wildcard subnet of the recipient.
   - **Transport Layer Protocol**: Identifies the transport protocol (e.g., TCP, UDP, ICMP, SCTP, or Any).
   - **Source and Destination Ports**: Specific TCP or UDP port numbers (e.g., Port 80 for HTTP, Port 22 for SSH, or wildcard).
   - **User Identifier / Security Label**: Optional user identity derived from an authenticated operating system context.
3. **Operational Impact**:
   SA selectors allow network administrators to apply fine-grained security policies: for instance, mandating that internal database traffic (Port 3306) must be encrypted using AES-ESP in Tunnel Mode, while public web browsing (Port 80) can bypass IPsec in the clear.

---

### Question 4 [KTU June 2022, Part A, Q7 / Part D, Q17(b) - 8 Marks]
**Question**: List out any four benefits of IPSec. Compare transport mode and tunnel mode functionalities in IPsec.

**Solution**:
1. **Four Key Benefits of IPsec**:
   - **Transparency to Applications**: IPsec functions at the Network Layer (Layer 3). Upper-layer protocols (TCP, UDP) and applications (browsers, email clients) operate without any changes or awareness of underlying encryption.
   - **Comprehensive Protection**: When implemented on a boundary firewall or router, IPsec protects all traffic traversing the perimeter, shielding entire subnets.
   - **Spoofing Prevention**: Provides origin authentication and integrity, eliminating IP address spoofing and unauthorized packet injection.
   - **Independent of User Education**: Security is enforced automatically by the network infrastructure, removing reliance on individual end-users to enable encryption.

2. **Comparison: Transport Mode vs. Tunnel Mode**:

| Feature | Transport Mode | Tunnel Mode |
|---|---|---|
| **Scope of Protection** | Protects only the transport-layer payload (TCP/UDP segments and data). | Protects the entire original IP packet (header and payload). |
| **Header Construction** | Keeps the original IP header; inserts AH/ESP header between original IP header and TCP segment. | Encapsulates original IP packet inside an AH/ESP header and prepends an entirely **New Outer IP Header**. |
| **Typical Endpoints** | Host-to-Host (client to server). | Gateway-to-Gateway (VPN firewall to firewall) or Host-to-Gateway. |
| **Traffic Flow Confidentiality** | Low: Intermediaries can see true source and destination IP addresses. | High: True source and destination addresses are concealed within the encrypted payload; observers see only gateway IPs. |
| **Packet Size Overhead** | Smaller overhead (adds only ESP/AH headers and trailers). | Larger overhead (adds ESP/AH headers plus a new 20-byte outer IP header). |
