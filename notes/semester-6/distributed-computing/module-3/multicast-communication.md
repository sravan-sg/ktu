# Multicast Communication

## Explanation

Multicast communication is the process of disseminating information from a single sender to multiple specific receivers. According to **Tanenbaum**, while this historically belonged to the domain of network protocols (IP Multicast), the sheer management effort and reluctance of ISPs to support it led to the rise of **Application-Level Multicasting**. 

In application-level multicasting, the participating nodes self-organize into a logical overlay network. The underlying physical network routers are entirely unaware of group membership. Tanenbaum details two primary approaches:

1. **Application-Level Tree-Based Multicasting**:
   - Nodes form a logical spanning tree. A message is sent from the root down the branches, duplicated only at the application layer of branching nodes.
   - The quality of these overlay trees is measured by three metrics:
     - **Link Stress**: Counts how many times the same packet traverses the identical physical network link. (Optimal is 1).
     - **Stretch (Relative Delay Penalty)**: The ratio of the delay between two nodes in the overlay network compared to the delay if they had communicated directly over the underlying network.
     - **Tree Cost**: A global metric aggregating the delay of all links in the tree to minimize overall bandwidth consumption.
   - Tanenbaum highlights that dynamic **Switch-Trees** are often used to continually optimize these metrics by allowing nodes to dynamically change their parent node to find lower-latency routes.

2. **Flooding-Based Multicasting**:
   - Instead of maintaining complex trees, a node simply forwards a message to all its overlay neighbors. 
   - While robust, pure flooding is inefficient (messages traverse the network multiple times). Therefore, **Probabilistic Flooding (Gossiping)** is used, where a node forwards a message with a certain probability $p$, combining simplicity with efficiency.

## Example

Consider a distributed application with 5 nodes participating in an application-level tree-based multicast. Node A is the sender (root). 
Nodes B and C are connected to A via the internet. Node D is connected to B.

- **Tree Routing**: Node A wants to send a video frame. It sends one copy over a TCP socket to Node B, and one copy to Node C. Node B's application receives the frame, processes it, and then explicitly opens a socket to send a copy to Node D.
- **Link Stress Issue**: If Node B and C happen to sit behind the exact same physical ISP router, Node A's outgoing physical link will see *two* copies of the exact same packet traversing it, resulting in a Link Stress of 2 for that specific ISP uplink.

## Applications & Use Cases

- **Peer-to-Peer Streaming**: Applications like historically older versions of Skype or Spotify use application-level tree multicasting to disseminate audio/video streams without requiring dedicated central servers or relying on ISP-level IP Multicast.
- **Overlay Management (Chord/Pastry)**: DHT-based peer-to-peer networks build implicit multicast trees (like Scribe) to route queries and updates across massive global networks.
- **Blockchain Networks**: Bitcoin and Ethereum utilize flooding-based multicasting (gossip protocols) to rapidly disseminate new blocks and transactions to all nodes without needing a rigid tree structure.

## 3 Solved Numerical/Analytical Examples

**Example 1: Calculating Link Stress**
*Problem:* In an application-level multicast tree, a root node R in New York sends a message to children A and B, both located in London. Both messages physically traverse the transatlantic fiber optic cable. What is the link stress on that cable?
*Solution:*
1. Link stress is defined as how often a packet crosses the same physical link.
2. The application layer at R sends two distinct unicast packets (one to A, one to B).
3. Both packets cross the transatlantic cable.
4. Link Stress = 2.
*Conclusion:* Application-level multicasting can lead to high link stress (inefficiency) if the logical tree is not optimized to match physical topology.

**Example 2: Calculating Stretch (Relative Delay Penalty)**
*Problem:* Node S (Source) sends a message to Node D via an overlay intermediary node I. The direct physical network latency from S to D is 20 ms. The physical latency from S to I is 15 ms, and from I to D is 25 ms. What is the stretch for the path S -> D?
*Solution:*
1. Stretch = (Delay in Overlay) / (Delay in Direct Physical Network).
2. Delay in Overlay = $S \rightarrow I + I \rightarrow D = 15 \text{ ms} + 25 \text{ ms} = 40 \text{ ms}$.
3. Direct Delay = 20 ms.
4. Stretch = $40 / 20 = 2.0$.
*Conclusion:* The message takes twice as long to arrive due to overlay routing. Algorithms aim to keep stretch close to 1.0.

**Example 3: Flooding Efficiency**
*Problem:* In a pure flooding overlay of 100 nodes and 300 logical links, a message is broadcast. How many total messages are transmitted across the overlay if duplicate tracking is perfect?
*Solution:*
1. In pure flooding, every node forwards the message to every neighbor except the one it received it from.
2. This results in exactly one message traversing every link in both directions, minus the spanning tree edges.
3. Approximately, the number of messages sent is twice the number of links.
4. Total messages = $2 \times 300 = 600$ messages.
*Conclusion:* Pure flooding is highly robust but extremely inefficient compared to a minimal spanning tree (which would require exactly 99 messages).

## Previous Year Questions & Solutions

**[April 2018] PART A - Q5) How is a multicast communication different from a broadcast? (4 marks)**
*Solution:*
Based on Tanenbaum's principles of communication:
1. **Target Audience**: 
   - **Broadcasting** strictly refers to sending a message to *every single node* in the network (or overlay network).
   - **Multicasting** refers to sending a message to a *specific subset* of nodes (a specific group).
2. **Efficiency and Routing**: 
   - Broadcasting in overlays is often implemented via naive **flooding**, meaning every node forwards the message. This causes massive redundancy and wastes resources.
   - Multicasting avoids this inefficiency by constructing **Application-Level Trees** (where data flows only down branches containing interested members) or by using **Probabilistic Gossiping** to selectively limit dissemination.
3. **Hardware vs Application Level**: True hardware broadcasting is limited to local physical subnets (LANs). In distributed systems spanning the WAN, both broadcasting and multicasting must be simulated at the Application Layer using overlay networks and peer-to-peer routing.
