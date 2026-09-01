# Physical Models

## Explanation
A **Physical Model** is the most explicit way to describe a distributed system. It captures the hardware composition of a system in terms of computers (nodes) and other devices, as well as their interconnecting network. It abstractly represents the physical reality of the infrastructure.

Historically, physical models have evolved through three distinct generations:
1. **Early Distributed Systems (1970s - 1980s):** Typically consisted of 10 to 100 nodes connected by a local area network (LAN) like Ethernet. These systems had limited Internet connectivity and provided basic services like shared local printers and file servers.
2. **Internet-scale Distributed Systems (1990s - 2000s):** The advent of the global Internet expanded the physical model to incorporate thousands of nodes distributed globally. This era introduced intranets (interconnected LANs within an organization) connected via firewalls to the broader Internet. Nodes included desktop computers, powerful servers, and clusters.
3. **Contemporary Distributed Systems (2010s - Present):** Characterized by massive scale, heterogeneity, and mobility. The physical model now includes millions of nodes. It encompasses everything from massive cloud datacenters containing thousands of multi-core blade servers to mobile devices (smartphones, tablets) connected via wireless networks (WiFi, 4G/5G), and embedded Internet of Things (IoT) devices.

## Example
Consider a modern university campus network as a physical model. 
- **Nodes:** Include students' laptops and smartphones (mobile nodes), faculty desktop workstations, library printer arrays, and the university's central database servers.
- **Interconnects:** Include the campus WiFi routers, wired Ethernet ports in labs, building-level switches, and the central campus gateway router that connects the entire intranet to the global Internet.
This physical model highlights the heterogeneity (different types of devices) and the varying network topologies (wireless edge, wired core) that the distributed system software must handle.

## Applications & Use Cases
1. **Cloud Computing Infrastructure**: Datacenters are physical models composed of racks of servers, top-of-rack switches, and high-speed optical cross-connects. Understanding this physical layout is essential for optimizing virtual machine placement.
2. **IoT Edge Networks**: A physical model of an agricultural IoT system includes low-power soil moisture sensors communicating via LoRaWAN to an edge gateway, which then relays aggregated data via 4G to a cloud server.
3. **Content Delivery Networks (CDNs)**: The physical deployment involves placing edge servers in strategically located internet exchange points (IXPs) worldwide to be physically closer to end-users.

## 3 Solved Numerical/Analytical Examples

**Example 1: Analyzing Network Delay in an Internet-Scale Physical Model**
*Problem:* A client in New York sends a 1 KB request to a server in London (approximate fiber distance 5500 km). The signal travels at $2 \times 10^8$ m/s in fiber. If processing at the server takes 10 ms and the response is 2 KB, calculate the total turnaround time. Assume bandwidth is 1 Gbps (negligible transmission delay for small packets).
*Solution:*
Propagation delay (one way) = Distance / Speed = $5500 \times 10^3 \text{ m} / (2 \times 10^8 \text{ m/s}) = 27.5$ ms.
Total turnaround time = (Propagation delay of request) + (Processing Time) + (Propagation delay of response)
Total turnaround time = 27.5 ms + 10 ms + 27.5 ms = 65 ms.

**Example 2: Node Failure Probability in a Cluster**
*Problem:* A modern physical model includes a compute cluster of 1000 nodes. If the Mean Time Between Failures (MTBF) for a single node is 3 years (approx 1000 days), what is the expected frequency of hardware failures in the entire cluster?
*Solution:*
Failure rate of one node, $\lambda = 1 / 1000$ failures/day.
Since there are $N = 1000$ independent nodes, the aggregate failure rate for the cluster is $N \times \lambda = 1000 \times (1 / 1000) = 1$ failure per day.
This shows that in large-scale physical models, node failure is a daily occurrence, requiring robust fault tolerance.

**Example 3: Mobile Node Bandwidth Degradation**
*Problem:* A mobile node in a contemporary physical model moves away from a WiFi access point. Its available bandwidth drops from 54 Mbps to 6 Mbps. How much longer will it take to transfer a 100 MB file at the edge of the network compared to being close to the access point?
*Solution:*
File Size = $100 \text{ MB} = 800 \text{ Mb}$ (megabits).
Time at 54 Mbps = $800 / 54 \approx 14.81$ seconds.
Time at 6 Mbps = $800 / 6 \approx 133.33$ seconds.
Difference = $133.33 - 14.81 = 118.52$ seconds longer. This illustrates the variability introduced by mobile nodes in modern physical models.

## Previous Year Questions & Solutions

**[April 2018] Q12. a) Describe the physical models of distributed systems. [5 Marks]**
*Solution:*
A **Physical Model** captures the explicit hardware composition of a distributed system, detailing the computers (nodes) and the network interconnecting them. 

The evolution of physical models can be categorized into three generations:
1. **Early Distributed Systems:** Consisted of a small number (10s to 100s) of homogeneous nodes connected by a single local area network (LAN). They were mostly isolated from the global Internet.
2. **Internet-scale Distributed Systems:** Characterized by the widespread adoption of the Internet. The model expanded to include intranets connected via firewalls, linking heterogeneous computers (desktops, servers) across vast geographical distances.
3. **Contemporary Distributed Systems:** Characterized by extreme scale, mobility, and ubiquity. The physical model now incorporates massive cloud datacenters, laptops, mobile devices (smartphones connected via wireless networks), and embedded IoT sensors, creating a highly dynamic and heterogeneous physical environment.
