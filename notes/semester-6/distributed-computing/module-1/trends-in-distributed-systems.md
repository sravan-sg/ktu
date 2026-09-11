# Trends in Distributed Systems

## Explanation

Distributed computing is a rapidly evolving field. The shift from isolated mainframes to global, interconnected networks has been driven by several key technological trends. Understanding these trends is crucial for anticipating the future architectural needs of software systems.

The major contemporary trends driving the evolution of distributed systems include:

1. **Pervasive Networking and the Modern Internet:**
   The internet has grown from a small academic network into a massive, pervasive global infrastructure. The adoption of IPv6 (providing virtually unlimited IP addresses) and high-speed wireless networks (5G, Wi-Fi 6) means almost any device can now be a node in a distributed system.

2. **Mobile and Ubiquitous Computing:**
   Computing is no longer confined to desktops. Mobile devices (smartphones, tablets) and ubiquitous computing devices (wearables, smart home appliances, IoT sensors) form highly dynamic distributed systems. These nodes frequently join and leave networks, demanding extreme tolerance for intermittent connectivity and mobility.

3. **Cloud, Edge, and Fog Computing:**
   - **Cloud Computing:** Centralizing massive computational and storage resources into massive data centers (e.g., AWS, Azure) to provide on-demand resources over the internet.
   - **Edge/Fog Computing:** As billions of IoT devices generate data, sending it all to the cloud causes latency and bandwidth bottlenecks. The new trend is pushing computation to the "edge" of the network (closer to the data source, like a router or local gateway) to process data in real-time.

4. **Distributed Multimedia Systems:**
   The massive demand for video streaming (Netflix, YouTube), live conferencing (Zoom, Teams), and augmented/virtual reality requires distributed systems capable of handling continuous, time-sensitive streams of data with strict Quality of Service (QoS) guarantees (minimizing latency and jitter).

5. **Distributed AI & Machine Learning (Federated Learning):**
   Training complex ML models requires massive distributed clusters. Furthermore, **Federated Learning** is a growing trend where models are trained locally on edge devices (like smartphones), and only the learned weights—not the private user data—are sent to a central server to update the global model.

## Example

**A Modern Smart City Traffic Management System**
- **IoT & Ubiquitous Computing:** Thousands of cameras and inductive loop sensors placed at intersections.
- **Edge Computing:** Instead of sending high-definition video of every car to the cloud, a local edge computer at the intersection processes the video, counts the cars, and calculates traffic density.
- **Cloud Computing:** The lightweight density data is sent to a central cloud server, which aggregates data across the entire city to adjust traffic light timings globally.
- **Mobile Computing:** The cloud server pushes real-time route updates to GPS apps on drivers' smartphones.

## Applications & Use Cases

1. **Healthcare (Wearable IoT):** Continuous monitoring of patient vitals (heart rate, blood oxygen) via smartwatches (ubiquitous computing), which alert cloud-based medical systems if anomalies are detected.
2. **Autonomous Vehicles:** Cars acting as powerful edge nodes that process sensor data locally for immediate driving decisions, while connecting to a distributed cloud network for map updates and fleet learning.
3. **Netflix (Distributed Multimedia):** Utilizing a massive global CDN (Content Delivery Network) to cache video files at the edge (in local ISP data centers) to ensure high-bandwidth, low-latency streaming.

## 3 Solved Numerical/Analytical Examples

**Example 1: Bandwidth Savings using Edge Computing**
*Problem:* A factory has 1000 IoT temperature sensors. Each sensor generates 1 MB of data per second. Sending data to the central cloud costs \$0.01 per GB. If we install an Edge gateway that aggregates and averages the data, reducing the output to 1 MB per second total for the whole factory, how much money is saved per day?
*Solution:*
1. **Cloud-only model:** Data generated = $1000 \times 1 \text{ MB/sec} = 1000 \text{ MB/sec} \approx 1 \text{ GB/sec}$.
   Data per day = $1 \text{ GB/sec} \times 60 \times 60 \times 24 = 86,400 \text{ GB/day}$.
   Cost = $86,400 \times \$0.01 = \$864 \text{ per day}$.
2. **Edge model:** Data sent = $1 \text{ MB/sec} = 0.001 \text{ GB/sec}$.
   Data per day = $0.001 \times 86,400 = 86.4 \text{ GB/day}$.
   Cost = $86.4 \times \$0.01 = \$0.86 \text{ per day}$.
3. **Savings:** $\$864 - \$0.86 = \$863.14 \text{ saved per day}$.
This illustrates why Edge computing is a dominant trend in distributed IoT systems.

**Example 2: Analyzing Jitter in Distributed Multimedia**
*Problem:* A VoIP distributed system sends voice packets every 20ms. The acceptable jitter (variation in delay) is $\pm 5$ms. Packet 1 arrives at $t=100$ms. Packet 2 arrives at $t=124$ms. Packet 3 arrives at $t=140$ms. Is the QoS maintained?
*Solution:*
1. Expected arrival of Packet 2 = $100 + 20 = 120$ms.
   Actual arrival = $124$ms. Jitter = $+4$ms. (Within $\pm 5$ms limit).
2. Expected arrival of Packet 3 = $120 + 20 = 140$ms.
   Actual arrival = $140$ms. Jitter = $0$ms. (Within limit).
3. Yes, the QoS is maintained. Handling this jitter requires distributed synchronization and buffering protocols (like RTP/RTCP).

**Example 3: Availability in Mobile Computing**
*Problem:* A mobile node frequently disconnects from the cellular network. It has an average uptime (Mean Time To Failure - MTTF) of 45 minutes before dropping the connection, and takes an average of 5 minutes to reconnect (Mean Time To Repair - MTTR). What is the steady-state availability of this mobile node to the distributed system?
*Solution:*
1. $\text{Availability} (A) = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}}$.
2. $A = \frac{45}{45 + 5} = \frac{45}{50} = 0.90$.
3. The node is available 90% of the time. Distributed algorithms in mobile computing environments must be designed to tolerate this 10% disconnection rate gracefully (e.g., using offline caching and eventual consistency).

## Previous Year Questions & Solutions

**[April 2021] Explain the major trends in distributed systems with suitable examples.**
*Solution:*
The design and deployment of distributed systems are heavily influenced by the following major trends:
1. **Pervasive Networking:** The global expansion of the internet and high-speed wireless networks (5G) allows diverse devices to communicate constantly.
2. **Ubiquitous and Mobile Computing:** Computing is integrated into everyday objects (wearables, smart home devices, smartphones). These systems must handle high mobility and intermittent network connections. *Example: A smartwatch syncing health data to a cloud server when connected to Wi-Fi.*
3. **Cloud and Edge Computing:** The shift towards centralized data centers providing compute-as-a-service (Cloud), and the counter-trend of pushing processing closer to the data source (Edge) to reduce latency and bandwidth usage. *Example: An autonomous car processing video locally (Edge) rather than sending it to the cloud.*
4. **Distributed Multimedia:** The massive growth of streaming platforms requiring systems that can deliver continuous time-based data (video/audio) with strict Quality of Service guarantees regarding bandwidth and latency. *Example: Netflix's global Content Delivery Network.*

**[December 2018] Differentiate between Cloud Computing and Edge Computing in the context of distributed systems. Why is Edge Computing becoming essential?**
*Solution:*
**Differences:**
- **Cloud Computing** centralizes massive computational and storage resources in a few massive data centers. Data from clients is sent over the internet to these servers for processing, and results are sent back.
- **Edge Computing** decentralizes processing by placing computational resources at the "edge" of the network, as close to the data source (like IoT sensors or users) as possible, such as on a local gateway router or the device itself.

**Why Edge Computing is Essential:**
1. **Latency Reduction:** For real-time applications like autonomous driving or industrial robotics, the round-trip time to a remote cloud server is too slow. Edge computing provides immediate, local processing.
2. **Bandwidth Conservation:** Sending raw, high-volume data (like 4K video feeds from hundreds of security cameras) to the cloud overwhelms internet bandwidth. Edge nodes filter and aggregate this data, sending only crucial summaries to the cloud.
3. **Privacy and Security:** Processing sensitive data locally reduces the risk of it being intercepted over the public internet.
