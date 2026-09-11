# Minicomputer Model in Distributed Systems

## Explanation

The **Minicomputer Model** is an early and fundamental architectural model in the evolution of distributed systems. It acts as an intermediate step between the traditional, monolithic centralized mainframe and the modern workstation-client-server models. 

In this architecture, a distributed computing system consists of several minicomputers (mid-range computers, smaller than mainframes but larger than personal microcomputers) interconnected by a communication network. 

**Key Characteristics:**
1. **Multi-user Support:** Each minicomputer is a time-sharing system capable of supporting multiple users simultaneously.
2. **Dumb Terminals:** Users interact with the minicomputers via simple display terminals (consisting only of a screen and keyboard with no local processing or storage capabilities).
3. **Resource Sharing:** A user logged into one minicomputer can potentially access resources (like databases or specialized software) residing on a different minicomputer via the communication network.
4. **Decentralization of Power:** Instead of a single massive mainframe handling an entire organization, computing power is decentralized across different departments, each owning its minicomputer.

**Block Diagram of Minicomputer Model:**

```mermaid
graph TD
    subgraph "Department A"
        T11[Terminal 1] --> M1((Minicomputer 1))
        T12[Terminal 2] --> M1
        T13[Terminal 3] --> M1
    end

    subgraph "Network"
        Net{Communication Network}
    end

    subgraph "Department B"
        M2((Minicomputer 2)) <-- --> T21[Terminal 1]
        M2 <-- --> T22[Terminal 2]
    end

    subgraph "Department C"
        M3((Minicomputer 3)) <-- --> T31[Terminal 1]
        M3 <-- --> T32[Terminal 2]
    end

    M1 <--> Net
    M2 <--> Net
    M3 <--> Net
```

The underlying intuition is **cost-effectiveness and localized control**. Mainframes were prohibitively expensive. Minicomputers allowed individual departments (e.g., Computer Science, Physics, Administration) to buy their own machines tailored to their workloads, while still allowing inter-departmental communication when necessary.

## Example

**A University Campus Network (1980s style)**
Imagine a university where the Engineering department has a DEC VAX minicomputer and the Science department has its own PDP-11 minicomputer.
- Students in Engineering sit at dumb terminals in a lab, entirely powered by the VAX machine.
- If an Engineering student needs to run a specialized chemistry simulation hosted on the Science department's PDP-11, they use a network login protocol (like Telnet) over the campus communication network to execute the program remotely. The processing happens on the Science minicomputer, and only the display output is sent back to the student's terminal in the Engineering lab.

## Applications & Use Cases

1. **Departmental Computing:** Large organizations splitting their workloads geographically or logically (e.g., HR, Finance, Engineering each having their own minicomputer but sharing a company-wide network).
2. **Early Resource Sharing:** Sharing expensive peripherals like line printers or large disk drives across different departments before modern LANs and NAS devices existed.
3. **Database Partitioning:** Storing local data locally on departmental minicomputers (faster access) while allowing remote queries for cross-departmental data.

## 3 Solved Numerical/Analytical Examples

**Example 1: Analyzing Cost-Performance Ratio**
*Problem:* A centralized mainframe costs \$1,000,000 and can process 500 Transactions Per Second (TPS). A minicomputer costs \$150,000 and can process 100 TPS. If an organization requires 400 TPS, analyze the cost difference between a centralized model and a minicomputer model.
*Solution:*
1. **Centralized Model:** Requires 1 Mainframe.
   - Cost = \$1,000,000.
   - Capacity = 500 TPS (Sufficient).
2. **Minicomputer Model:** Requires $\lceil 400 / 100 \rceil = 4$ minicomputers.
   - Cost = $4 \times \$150,000 = \$600,000$.
   - Capacity = $4 \times 100 = 400$ TPS.
3. **Conclusion:** The minicomputer model saves the organization \$400,000. This demonstrates Grosh's law breaking down (which originally stated computing power is proportional to the square of cost). Distributed minicomputers offer a better price/performance ratio for highly parallelizable transactional workloads.

**Example 2: Network Bandwidth vs. Local Processing**
*Problem:* A user on Minicomputer A (MA) requests a database query on Minicomputer B (MB). The raw database table is 50 MB. If MB processes the query locally, the result is 1 MB. The network bandwidth between MA and MB is 10 Mbps (Megabits per second). Calculate the time saved by processing the query remotely on MB rather than transferring the raw data to MA to process. (Ignore query execution time).
*Solution:*
1. Note: 1 Byte = 8 bits.
2. **Scenario 1 (Transfer Raw Data):**
   - Size = $50 \text{ MB} = 50 \times 8 = 400 \text{ Megabits (Mb)}$.
   - Transfer Time = $\frac{400 \text{ Mb}}{10 \text{ Mbps}} = 40$ seconds.
3. **Scenario 2 (Process Remotely on MB):**
   - Size of Result = $1 \text{ MB} = 1 \times 8 = 8 \text{ Megabits (Mb)}$.
   - Transfer Time = $\frac{8 \text{ Mb}}{10 \text{ Mbps}} = 0.8$ seconds.
4. **Time Saved:** $40 - 0.8 = 39.2$ seconds.
This illustrates the principle of moving computation to the data (a core tenet of distributed computing) rather than moving data to the computation.

**Example 3: Terminal Response Time (M/M/1 Queueing)**
*Problem:* A minicomputer serves 20 dumb terminals. The average time a user takes to "think" and type a command is 10 seconds. The minicomputer takes an average of 0.4 seconds to process a command. Using basic queuing principles, what is the maximum throughput (commands/sec) the minicomputer can handle before the system saturates?
*Solution:*
1. Let processing time $S = 0.4$ seconds.
2. Service rate $\mu = \frac{1}{S} = \frac{1}{0.4} = 2.5$ commands per second.
3. The minicomputer can process a theoretical maximum of 2.5 commands per second. If the arrival rate $\lambda$ from the terminals exceeds 2.5, the queue will grow infinitely.
4. Therefore, the maximum sustainable throughput is **2.5 commands/second**. In a time-sharing minicomputer model, adding too many active dumb terminals directly degrades the response time for everyone.

## Previous Year Questions & Solutions

**[December 2018] Describe the Minicomputer model of a distributed computing system with the help of a block diagram. What are its primary advantages?**
*Solution:*
**Minicomputer Model:**
In the minicomputer model, the distributed system is composed of several minicomputers connected via a communication network. Each minicomputer is a multi-user time-sharing system. Users interact with the system using dumb terminals (display screens and keyboards) connected directly to a specific minicomputer. 

If a user needs computing power or data not available on their local minicomputer, they can log into a remote minicomputer over the network. The remote minicomputer performs the processing and sends the display results back over the network to the user's terminal.

**Block Diagram:**
*(Refer to the Mermaid diagram in the Explanation section above, showing multiple Terminals connected to their respective Minicomputers, which are all joined by a central Communication Network).*

**Primary Advantages:**
1. **Better Price/Performance Ratio:** A cluster of minicomputers was significantly cheaper than a single monolithic mainframe with equivalent computing power.
2. **Localized Control & Autonomy:** Different departments could own, manage, and configure their own minicomputer according to their specific needs, rather than relying on a centralized IT department.
3. **Resource Sharing:** Departments could share specialized hardware (like high-speed printers) or software accessible over the network.
4. **Improved Reliability:** If one minicomputer fails, only the users connected directly to that minicomputer are affected. The rest of the organization using other minicomputers can continue working seamlessly, providing partial fault tolerance compared to a mainframe where a crash halts the entire organization.
