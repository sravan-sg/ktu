# Module 1 — Topic 1: Introduction & Uses of Computer Networks

> **Module 1**: Network Architecture & Reference Models  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
A **Computer Network** is an interconnected collection of autonomous computing devices capable of exchanging data and sharing resources over communication links. 
- **Autonomous**: Each node possesses its own local CPU, memory, and operating system. No single computer can forcibly halt or control another node.
- **Interconnected**: Devices communicate via physical transmission media (optical fiber, twisted pair copper cables, radio frequencies).

#### Primary Motivations & Uses of Computer Networks

```
                           ┌─────────────────────────────────────────┐
                           │       USES OF COMPUTER NETWORKS         │
                           └────────────────────┬────────────────────┘
                                                │
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                      ▼                                      ▼
┌─────────────────┐                    ┌─────────────────┐                    ┌─────────────────┐
│    BUSINESS     │                    │    CONSUMER     │                    │  MOBILE & IOT   │
│  APPLICATIONS   │                    │  APPLICATIONS   │                    │ COMMUNICATIONS  │
├─────────────────┤                    ├─────────────────┤                    ├─────────────────┤
│• Resource Share │                    │• Web Browsing   │                    │• Mobile Data    │
│• High Reliablty │                    │• E-Commerce     │                    │• Smart Home     │
│• Client-Server  │                    │• Social Media   │                    │• Autonomous     │
│• Cost Reduction │                    │• P2P Sharing    │                    │  Vehicles       │
└─────────────────┘                    └─────────────────┘                    └─────────────────┘
```

#### 1. Business Applications
- **Resource Sharing**: Making physical hardware (storage arrays, high-speed printers, compute clusters) and software resources (databases, shared repositories) accessible to any employee regardless of physical location.
- **High Reliability**: Duplicating critical data across multiple geographically distributed servers (e.g., AWS S3 replicas). If one data center experiences a blackout or hardware crash, replica nodes seamlessly take over.
- **Cost Reduction**: Linking networks of inexpensive microcomputers (desktop PCs) via a Local Area Network (LAN) delivers greater aggregate computing power at a lower cost than legacy centralized mainframes.
- **Client-Server Model**: Centralizing data storage and administrative management on high-capacity **Server** machines while employees interact via **Client** workstations over local or wide-area networks.

#### 2. Consumer & Home Applications
- **Access to Remote Information**: Searching digital archives, web browsing (HTTP/HTTPS), cloud storage access (Google Drive, iCloud), and streaming media.
- **Person-to-Person Communication**: Instant messaging, email (SMTP/IMAP), video conferencing (Zoom, Teams), and social networks.
- **Electronic Commerce (E-Commerce)**: Secure online banking, digital payments (UPI), and e-retail transactions using encryption protocols (TLS/SSL).
- **Peer-to-Peer (P2P) Networks**: Decentralized file sharing (BitTorrent) where nodes act as both clients and servers simultaneously.

#### 3. Mobile & IoT Communications
- Wireless connectivity for mobile devices across 4G LTE/5G cellular networks and Wi-Fi access points.
- **Internet of Things (IoT)**: Connecting embedded sensors, smart home appliances, wearable devices, and smart power grids using low-energy wireless protocols (IEEE 802.15.4, LoRaWAN, Zigbee).

### Example
Consider an enterprise healthcare system:
- **Without a Network**: Doctors must manually carry paper medical charts and physical X-ray films between buildings. If a single folder is misplaced, critical medical history is lost.
- **With a Computer Network**: Scanners upload high-resolution DICOM imagery directly to a central **PACS (Picture Archiving and Communication System) Server**. Doctors view electronic health records instantaneously from any networked tablet or workstation. High-availability cloud replicas ensure zero data loss during power outages.

### Applications & Use Cases
- **Enterprise Distributed Databases**: Financial institutions use multi-region database networks to process millions of transactions per second with real-time replication.
- **Content Delivery Networks (CDNs)**: Edge servers cache web content close to end-users to minimize latency and reduce backbone network traffic.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Availability & Reliability Calculation in Distributed Networks
**Problem:** A company stores a database on a single server with an individual uptime availability of $p = 0.95$ (95% uptime). If the company deploys a network cluster with $N = 3$ independent redundant replica servers, calculate the total system availability $A_{\text{system}}$.
**Step-by-step Solution:**
1. **Single Server Failure Probability:**
   $$P(\text{fail}) = 1 - p = 1 - 0.95 = 0.05 \quad (5\% \text{ downtime})$$
2. **Probability that ALL 3 Independent Replicas Fail Simultaneously:**
   $$P(\text{all fail}) = (P(\text{fail}))^N = (0.05)^3 = 0.000125$$
3. **Calculate Overall System Availability ($A_{\text{system}}$):**
   $$A_{\text{system}} = 1 - P(\text{all fail}) = 1 - 0.000125 = 0.999875 \quad (\mathbf{99.9875\% \text{ Availability}})$$
4. **Conclusion:** Networking 3 redundant servers improves uptime from 95% (18.25 days downtime/year) to 99.9875% (only 1.1 hours downtime/year).

### Example 2: Client-Server vs P2P Bandwidth Scaling Comparison
**Problem:** A 100 MB video file is distributed to $N = 1000$ users. 
(a) Calculate total server egress bandwidth required in a traditional Client-Server architecture.
(b) Calculate total server egress bandwidth required in a P2P network where the server uploads only 1 original copy to the network.
**Step-by-step Solution:**
1. **Client-Server Architecture:**
   The central server must transmit a full copy to every client individually:
   $$\text{Total Bandwidth} = N \times \text{File Size} = 1000 \times 100 \text{ MB} = \mathbf{100,000 \text{ MB} = 100 \text{ GB}}$$
2. **Peer-to-Peer (P2P) Architecture:**
   The server uploads 1 copy ($100 \text{ MB}$), and peers download/upload fragments among each other:
   $$\text{Server Egress Bandwidth} = 1 \times 100 \text{ MB} = \mathbf{100 \text{ MB}}$$
3. **Savings:** P2P reduces central server bandwidth consumption by a factor of 1,000.

### Example 3: Network Delay Impact on E-Commerce Transaction Rate
**Problem:** An e-commerce database requires 4 sequential network round-trips (RTTs) to process 1 order. Compare total transaction processing time over (a) a Fiber LAN ($\text{RTT} = 0.5 \text{ ms}$), and (b) a Satellite WAN ($\text{RTT} = 250 \text{ ms}$).
**Step-by-step Solution:**
1. **Fiber LAN Processing Time:**
   $$T_{\text{LAN}} = 4 \times \text{RTT}_{\text{LAN}} = 4 \times 0.5 \text{ ms} = \mathbf{2.0 \text{ ms}}$$
   $$\text{Max Throughput} = \frac{1000 \text{ ms}}{2.0 \text{ ms}} = 500 \text{ transactions/sec per thread}$$
2. **Satellite WAN Processing Time:**
   $$T_{\text{satellite}} = 4 \times \text{RTT}_{\text{satellite}} = 4 \times 250 \text{ ms} = 1,000 \text{ ms} = \mathbf{1.0 \text{ second}}$$
   $$\text{Max Throughput} = \frac{1 \text{ s}}{1.0 \text{ s}} = 1 \text{ transaction/sec per thread}$$

---

## 3. Previous Year Questions & Solutions

1. **"List and explain the main uses of computer networks in business and home applications." [May 2019, July 2021]**
   - **Solution:**
     **Business Applications:**
     1. *Resource Sharing*: Shares hardware (printers, NVMe storage) and software databases across hosts.
     2. *High Reliability*: Replicates data across redundant nodes to ensure zero single-point-of-failure.
     3. *Client-Server Model*: Centralizes database management on servers while users work on lightweight workstations.
     4. *Communication*: Instant corporate messaging, IP telephony, and collaborative workspaces.
     **Home Applications:**
     1. *Access to Remote Information*: Web browsing, streaming services, and online digital libraries.
     2. *Person-to-Person Communication*: Social networks, email, instant messaging, and video calls.
     3. *E-Commerce*: Online banking, shopping, and digital financial transactions.

2. **"Explain the Client-Server model. How does it differ from Peer-to-Peer (P2P) architecture?" [Dec 2019]**
   - **Solution:**
     - **Client-Server Model**: Dedicated high-capacity Server holds centralized resources. Clients send requests; server processes and returns responses. Asymmetrical architecture (Server has public IP, high uptime).
     - **P2P Model**: No dedicated central server. All nodes (Peers) are equal and act as both clients (downloaders) and servers (uploaders) simultaneously. Highly scalable as each new user adds download and upload capacity to the network.
