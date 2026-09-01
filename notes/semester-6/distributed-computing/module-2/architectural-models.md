# Architectural Models

## Explanation
An **Architectural Model** in a distributed system describes the system's structure in terms of its separately specified components and their interrelationships. Its primary objective is to ensure that the structure meets current and future demands on reliability, manageability, adaptability, and cost-effectiveness. 

At a conceptual level, architectural models abstract away the underlying physical network and focus on the logical placement of software components and the paradigms used for their interaction. The core idea is determining *where* the computation happens, *where* the state is stored, and *how* different entities discover and communicate with one another. 

The major architectural models are:
1. **Client-Server Model**: Processes are distinctly divided into clients (requesters of service) and servers (providers of service).
2. **Peer-to-Peer (P2P) Model**: All processes (peers) play similar roles, interacting cooperatively to perform a distributed activity without any distinction between clients and servers.
3. **Variants and Extensions**:
   - **Multiple Servers**: Services are replicated or partitioned across multiple servers to improve performance and reliability.
   - **Proxy Servers and Caches**: Intermediary nodes that store recently accessed data to reduce latency and network traffic.
   - **Mobile Code**: Code is downloaded from the server and executed locally on the client (e.g., JavaScript in browsers, Java Applets).
   - **Mobile Agents**: A running program (including both code and data) that travels from one computer to another in a network carrying out a task.

## Example
Consider a traditional Web Browsing scenario vs. a BitTorrent download. 
- In the **Client-Server** approach (Web Browsing), the browser (Client) explicitly requests a web page from an Apache web server. The server does the heavy lifting of fetching the data and sending it back. If the server goes down, the client cannot access the page.
- In the **Peer-to-Peer** approach (BitTorrent), a user wants to download a large file. Instead of hitting a single server, the user's torrent client connects to multiple other peers who already have pieces of the file. The client downloads different chunks from different peers simultaneously and also uploads the chunks it has to others. There is no central point of failure for the file transfer itself.

## Applications & Use Cases
1. **Content Delivery Networks (CDNs)**: Utilize proxy servers and caches placed at the edge of the network to serve static assets (images, videos) close to the users, minimizing latency.
2. **Blockchain & Cryptocurrency (Bitcoin, Ethereum)**: Heavily rely on the Peer-to-Peer model where all nodes maintain a copy of the distributed ledger and participate in consensus without a central authority.
3. **Modern Web Applications**: Use a multi-tier client-server model (Presentation Tier -> Application Tier -> Data Tier) to separate concerns and allow independent scaling of the backend microservices.

## 3 Solved Numerical/Analytical Examples

**Example 1: Analyzing Bottlenecks in Client-Server Architecture**
*Problem:* A single server handles requests from 1000 clients. Each client makes 10 requests per second. The server takes 2 milliseconds to process a single request. Will the server be able to handle the load?
*Solution:*
Total request rate = 1000 clients * 10 req/sec = 10,000 requests/second.
Time taken for 10,000 requests = 10,000 * 2 ms = 20,000 ms = 20 seconds.
Since the server needs 20 seconds of processing time for every 1 second of real time, the server will become a severe bottleneck. The system requires either vertical scaling (faster processor) or horizontal scaling (multiple servers behind a load balancer).

**Example 2: Caching Efficiency in Proxy Servers**
*Problem:* A proxy server cache has a hit rate of 80%. Fetching from the cache takes 10ms, while a cache miss requires fetching from the origin server, taking 200ms. Calculate the average response time.
*Solution:*
Average Response Time = (Hit Rate * Cache Fetch Time) + (Miss Rate * Origin Fetch Time)
Average Response Time = (0.80 * 10ms) + (0.20 * 200ms)
Average Response Time = 8ms + 40ms = 48ms.
The use of the proxy server significantly reduces the average latency compared to the 200ms baseline.

**Example 3: Peer-to-Peer File Distribution Time**
*Problem:* In a pure P2P network, a file of size $F$ needs to be distributed to $N$ peers. Assume the origin has upload capacity $U_s$, and each peer has download capacity $D_i$ and upload capacity $U_i$. State the theoretical minimum distribution time.
*Solution:*
The minimum distribution time $T$ must satisfy three constraints:
1. The server must upload at least one copy of the file: $T \ge F / U_s$
2. The peer with the slowest download speed must get the file: $T \ge F / D_{min}$
3. The total uploaded data ($N \cdot F$) cannot exceed the total upload capacity of the entire system over time $T$: $T \ge (N \cdot F) / (U_s + \sum U_i)$.
Thus, $T = \max \left( \frac{F}{U_s}, \frac{F}{D_{min}}, \frac{N \cdot F}{U_s + \sum_{i=1}^N U_i} \right)$.

## Previous Year Questions & Solutions

**[April 2018] Q3. What is an architectural model? (Module II) [4 Marks]**
*Solution:*
An **Architectural Model** is an abstract representation that defines the structure of a distributed system in terms of its separately specified components and their interrelationships. It focuses on the logical placement of software components and how they communicate, irrespective of the underlying physical network. 

The primary goals of defining an architectural model are to ensure reliability, adaptability, and cost-effectiveness. 

Key types of architectural models include:
1. **Client-Server Model**: Processes are divided into clients that request services and servers that provide them. Communication is typically request-reply.
2. **Peer-to-Peer Model**: All processes act as peers without a rigid client-server distinction, cooperating to achieve a shared goal (e.g., file sharing).
3. **Proxy Servers**: Intermediary nodes that cache data to reduce load on the primary server and improve client response times.
4. **Mobile Code & Mobile Agents**: Architectures where executable code (or code along with its execution state) is transferred across the network to run on different machines.
