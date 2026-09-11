# Name Service

## Explanation
In a distributed system, resources like computers, services, and files are fundamentally identified by machine-readable identifiers (like IP addresses, MAC addresses, or UFIDs). A **Name Service** provides a mechanism to map human-readable names (like `www.google.com`) to these machine-readable identifiers. 

According to **Tanenbaum (Chapter 5 on Naming)**, the primary goal of a name service is to provide **location transparency**—allowing a resource to move to a new physical address or endpoint without requiring users to change how they refer to it.

### Core Concepts
1. **Name Space:** The collection of all valid names recognized by the name service. To scale globally, namespaces are typically structured hierarchically (e.g., a tree) to allow for distributed management and to prevent name collisions.
2. **Name Resolution:** The process of translating a given name into its corresponding underlying attribute (e.g., an IP address or access point).
3. **Name Servers:** The physical machines that store partitions of the naming database and process resolution requests. No single server holds the entire global database.
4. **Resolution Strategies (Tanenbaum's Models):**
   - **Iterative Resolution:** The client contacts a root name server, which replies with the address of the next-level server. The client then contacts the next server itself, repeating this iteratively until the name is fully resolved.
   - **Recursive Resolution:** The client contacts a local name server. If that server doesn't know the answer, it contacts the next server on behalf of the client, acting as a middleman. The final answer is passed back up the chain to the client. This allows name servers to aggressively cache results for future clients.

## Example
**DNS Recursive Resolution Example:**
A user types `www.example.com` into their browser.
1. The browser asks the local OS resolver.
2. The OS resolver asks the ISP's local DNS server (acting recursively).
3. The local DNS server asks a Root Server: "Where is `.com`?" -> Returns `.com` TLD server IP.
4. The local DNS server asks the `.com` TLD Server: "Where is `example.com`?" -> Returns `example.com` Authoritative Name Server IP.
5. The local DNS server asks the Authoritative server: "What is the IP of `www.example.com`?" -> Returns `192.0.2.1`.
6. The local DNS server caches this result and returns `192.0.2.1` to the client's OS.

## Applications & Use Cases
- **Domain Name System (DNS):** The backbone of the internet, operating as a massive, globally distributed name service mapping URLs to IP addresses.
- **Active Directory / LDAP:** Used in enterprise corporate networks to map usernames to user profiles, permissions, and network locations.
- **Service Discovery (e.g., Consul, ZooKeeper):** In modern microservices architectures, services dynamically register their ephemeral IP and port with a name service so other services can find them without hardcoded IP addresses.

## 3 Solved Numerical/Analytical Examples

**Example 1: Iterative Resolution Message Overhead**
*Problem:* In an iterative resolution process, a name consists of 4 parts (e.g., `a.b.c.d`). Assuming the client's cache is completely empty, how many messages are exchanged over the network to resolve this name?
*Solution:*
The client must send a request and receive a response for each part:
1. Query Root -> Response (points to `.d` server)
2. Query `.d` server -> Response (points to `.c` server)
3. Query `.c.d` server -> Response (points to `.b` server)
4. Query `.b.c.d` server -> Response (returns IP of `a.b.c.d`)
*Conclusion:* Total messages exchanged = 4 queries + 4 responses = 8 messages.

**Example 2: Caching and Time-To-Live (TTL)**
*Problem:* If a DNS record has a Time-To-Live (TTL) of 3600 seconds. A client resolves it at T=0. At T=1800, the authoritative server changes the IP address. If the client queries the name again at T=2000, which IP will it get?
*Solution:*
1. The local DNS cache retains the record for exactly 3600 seconds. 
2. Since T=2000 is less than 3600, the cache has not expired.
3. The local server will serve the stale cached entry instead of querying the authoritative server.
*Conclusion:* The client will receive the *old* IP address until T=3601.

**Example 3: Namespace Scalability**
*Problem:* A naming system uses a flat tree structure of depth 3 and a branching factor of 100. How many total names can this namespace accommodate at the leaf level?
*Solution:*
1. Level 0: 1 node (Root)
2. Level 1: 100 nodes
3. Level 2: $100 \times 100 = 10,000$ nodes
4. Level 3 (leaves): $10,000 \times 100 = 1,000,000$ nodes. 
*Conclusion:* The system can accommodate exactly 1,000,000 distinct names at the leaf level.

## Previous Year Questions & Solutions

**[April 2018] What is the role of a Name Service in a distributed system? (4 marks)**
*Solution:*
The role of a Name Service in a distributed system is to provide a unified mechanism for naming and locating resources. Its key roles include:
1. **Abstraction (Access Transparency):** It hides the low-level machine identifiers (like IP addresses, ports, or MAC addresses) from human users and applications, allowing them to use human-readable names.
2. **Location Transparency:** Users do not need to know the physical location of a resource to access it. If a resource moves to a new machine and gets a new IP address, the Name Service is updated, but the name remains identically the same.
3. **Scalability and Partitioning:** By structuring the name space hierarchically, the name service database can be partitioned and distributed across multiple servers globally, preventing a single point of failure and bottleneck (as seen in DNS).
4. **Resource Sharing:** It allows multiple disparate systems and users to discover and share resources easily by querying a common registry.
