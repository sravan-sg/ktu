# 8279 and 8257 Interfacing

> **Senior CS Professor Notes** | Semester 5 — CS305 Microprocessors & Microcontrollers | Module IV

---

## 1. Explanation

In embedded and microprocessor-based systems, two peripheral operations consume disproportionate CPU bandwidth if managed purely via software polling:
1. **Human-Machine Interfaces (HMI)**: Scanning a matrix keypad, debouncing mechanical contacts, and multiplexing multi-digit 7-segment LED displays.
2. **Bulk Data Movement**: Transferring blocks of bytes between high-speed storage or I/O devices (disk drives, network interfaces, audio codecs) and system RAM.

The **Intel 8279** and **Intel 8257** offload these demanding tasks from the CPU into dedicated hardware coprocessing engines.

---

### Part A: Intel 8279 Programmable Keyboard/Display Controller

The **8279** is a specialized LSI peripheral designed to handle keyboard matrix scanning and multiplexed multi-digit display updating without CPU intervention.

```
                         8279 Functional Block Diagram
  +-------------------------------------------------------------------------+
  |                                                                         |
  |  +----------------+     Internal Data Bus (8-bit)     +--------------+  |
  |  | Data Bus Buffer|<=================================>| Display RAM  |==|==> A3-A0, B3-B0
  |  | (DB0 - DB7)    |          |               |        | (16 x 8-bit) |  | (Cathode data)
  |  +----------------+          |               |        +--------------+  |
  |                              |               |                          |
  |  +----------------+          |               |        +--------------+  |
  |  | I/O Control    |          |               +=======>| Display      |==|==> BD (Blank)
  |  | & Timing       |          |               |        | Address Reg  |  |
  |  | (RD#, WR#, CS#,           |               |        +--------------+  |
  |  |  A0, RESET)    |          |               |                          |
  |  +----------------+          v               v                          |
  |                       +-------------+ +-------------+ +--------------+  |
  |  +----------------+   | Scan        | | FIFO /      | | Keyboard     |  |
  |  | Clock Prescaler|-->| Counter     | | Sensor RAM  | | Debounce &   |<--|==> RL0 - RL7
  |  | (CLK / Prescale|   | (SL0 - SL3) | | (8 x 8-bit) | | Control Logic|  | (Return lines)
  |  +----------------+   +-------------+ +-------------+ +--------------+  |
  |                              |               |               ^          |
  |                              v               v               |          |
  |                         SL0 - SL3           IRQ           SHIFT, CNTL   |
  |                        (Scan Lines)     (Interrupt)     (Control pins)  |
  +-------------------------------------------------------------------------+
```

#### Four Major Functional Sections of the 8279:

1. **Keyboard Section**:
   - Interfaces to an $8 \times 8$ matrix keypad (up to **64 keys**).
   - Driven by 4 scan lines ($\text{SL}_0 - \text{SL}_3$) and 8 return lines ($\text{RL}_0 - \text{RL}_7$).
   - Contains an internal **10 ms debouncing counter** to filter out mechanical contact bounce.
   - Includes two key-depression handling modes:
     - **2-Key Lockout**: If two keys are pressed simultaneously, only the first valid key is accepted; the second is ignored until the first is released.
     - **N-Key Rollover**: Keys are continuously scanned and loaded into the FIFO buffer in the exact chronological sequence they are depressed, even during rapid typing.
   - Inputs for **SHIFT** and **CONTROL/STROBE** lines allow generating uppercase and specialized control characters.

2. **FIFO / Sensor RAM**:
   - An internal $8 \times 8$-bit (8-byte) dual-port RAM.
   - In **Keyboard Mode**, it operates as a First-In-First-Out (FIFO) buffer storing up to 8 keystrokes. When a key is validated, its 8-bit scancode (containing the 3-bit scan count, 3-bit return line code, SHIFT status, and CONTROL status) is pushed into the FIFO, and the **IRQ** output pin goes HIGH to alert the CPU.
   - In **Sensor Matrix Mode**, it stores the exact current open/closed status of all 64 matrix switches and raises IRQ whenever any sensor changes state.

3. **Display Section**:
   - Contains a $16 \times 8$-bit **Display RAM** organized as dual 4-bit nibbles ($A_3 - A_0$ and $B_3 - B_0$), capable of driving up to 16 numeric 7-segment displays or 8 alphanumeric 16-segment displays.
   - Automatically and continuously refreshes the displays without CPU intervention by cycling through the Display RAM addresses in synchronism with the scan lines ($\text{SL}_0 - \text{SL}_3$).
   - Supports two display entry modes:
     - **Left Entry Mode**: Characters are entered from the left; the display pointer increments with each write ($0 \to 1 \to 2 \dots$).
     - **Right Entry Mode (Calculator Style)**: Characters enter from the rightmost digit, and existing digits shift leftward with each new keystroke.

4. **Scan Counter**:
   - Generates the time-multiplexed scanning signals on $\text{SL}_0 - \text{SL}_3$.
   - **Encoded Mode**: Outputs a 4-bit binary count ($0000_2$ to $1111_2$). Requires an external 4-to-16 decoder (e.g., 74LS154) to drive 16 display digits and an 8-to-1 decoder for 8 keypad rows.
   - **Decoded Mode**: Internal decoder drives lines $\text{SL}_0 - \text{SL}_3$ directly as 4 active-low scanning pulses (limited to 4 display digits and 4 keypad rows).

---

### Part B: Intel 8257 Programmable DMA Controller

In standard CPU-controlled I/O, every byte transferred between memory and a peripheral requires at least two bus cycles:
$$\text{Read from I/O to AL} \quad \longrightarrow \quad \text{Write AL to Memory}$$
This requires multiple instruction fetch and execution states ($10 - 20$ T-states per byte), restricting data throughput to less than $500\text{ KB/s}$.

**Direct Memory Access (DMA)** bypasses the CPU entirely. The peripheral exchanges data bytes **directly with memory** across the system bus in a single bus cycle ($2 - 4$ T-states), achieving throughputs exceeding $2 - 5\text{ MB/s}$.

The **Intel 8257** is a 4-channel dedicated DMA controller that manages bus arbitration, generates memory addresses, and issues memory/IO read-write strobes.

```
                         8257 DMA Controller Architecture
  +-------------------------------------------------------------------------+
  |                                                                         |
  |  +----------------+     Internal Data Bus (8-bit)     +--------------+  |
  |  | Data Bus Buffer|<=================================>| Channel 0    |==|==> DRQ0, DACK0#
  |  | (D0 - D7)      |          |                        | Registers    |  |
  |  +----------------+          |                        +--------------+  |
  |                              |                                          |
  |  +----------------+          |                        +--------------+  |
  |  | Control Logic  |          |                        | Channel 1    |==|==> DRQ1, DACK1#
  |  | (IOR#, IOW#,              |                        | Registers    |  |
  |  |  MEMR#, MEMW#) |          |                        +--------------+  |
  |  +----------------+          |                                          |
  |                              v                        +--------------+  |
  |  +----------------+   +-------------+                 | Channel 2    |==|==> DRQ2, DACK2#
  |  | Priority       |-->| Mode Set /  |                 | Registers    |  |
  |  | Resolver       |   | Status Reg  |                 +--------------+  |
  |  +----------------+   +-------------+                                   |
  |                              |                        +--------------+  |
  |  +----------------+          |                        | Channel 3    |==|==> DRQ3, DACK3#
  |  | Bus Request    |          |                        | Registers    |  |
  |  | (HOLD, HLDA)   |          |                        +--------------+  |
  |  +----------------+          |                                          |
  |                              v                                          |
  |                          A0 - A3 (Bidirectional), A4 - A7 (Outputs),    |
  |                          AEN, ADSTB, TC (Terminal Count), MARK          |
  +-------------------------------------------------------------------------+
```

#### Channel Architecture:
Each of the 4 independent DMA channels ($\text{Channel } 0 - 3$) possesses two 16-bit registers:
1. **DMA Address Register (DAR)**:
   - Holds the 16-bit memory address where the next DMA transfer will take place.
   - Automatically increments (or decrements) after every transferred byte.
2. **Terminal Count Register (TCR)**:
   - Bits $13 - 0$ store the count value ($N-1$) specifying how many bytes to transfer (up to $16\text{ KB} = 16,384$ bytes).
   - Bits $15 - 14$ store the 2-bit **DMA Transfer Type**:
     - `00` = Verify DMA Cycle (no data transferred; tests memory parity).
     - `01` = Write DMA Cycle ($\text{Peripheral} \to \text{Memory}$).
     - `10` = Read DMA Cycle ($\text{Memory} \to \text{Peripheral}$).
     - `11` = Illegal / Reserved.

#### DMA Bus Arbitration Protocol (HOLD / HLDA Handshake)

```
DRQn (Peripheral)  _______/----------------------------------------------------
HOLD (8257 to CPU) ___________/------------------------------------------------
HLDA (CPU to 8257) _______________/--------------------------------------------
AEN (8257 Enable)  ___________________/----------------------------------------
DACKn# (to Periph) _______________________/----------------\___________________
MEMW# / IOR#       ___________________________/--------\_______________________
                                              ^ Single-Cycle Direct Transfer
```

1. **Request**: Peripheral asserts its DMA Request line ($\text{DRQ}_n$).
2. **Bus Request**: The 8257 Priority Resolver selects the highest channel and asserts `HOLD` to the 8086 CPU.
3. **Bus Grant**: The 8086 completes its current bus cycle, floats its address, data, and control lines into high impedance, and responds by asserting **`HLDA` (Hold Acknowledge)**.
4. **Bus Takeover**: The 8257 asserts **`AEN` (Address Enable)** to disable system CPU bus latches and enables its own address generation:
   - Outputs low address bits $A_0 - A_3$ and middle address bits $A_4 - A_7$.
   - Places high address bits $A_8 - A_{15}$ onto the data bus ($D_0 - D_7$) and asserts **`ADSTB` (Address Strobe)** to latch them into an external 74LS373 latch.
5. **Transfer Execution**:
   - The 8257 asserts **$\overline{\text{DACK}}_n$** to notify the peripheral.
   - For a DMA Write ($\text{I/O} \to \text{Memory}$): 8257 asserts both **$\overline{\text{IOR}}$** and **$\overline{\text{MEMW}}$** simultaneously. Data flows directly from peripheral output to RAM input across the data bus in **one clock pulse**!
6. **Completion**:
   - The Terminal Count Register decrements. When the count rolls over from `0000H` to `FFFFH`, the 8257 asserts the **`TC` (Terminal Count)** pin high and resets `HOLD` to relinquish bus control back to the CPU.

---

## 2. Example: 8257 DMA System Interconnection

```
                 8086 Interfaced to 8257 DMA Controller
  +------------------+                     +------------------+
  |     8086 CPU     |                     |     8257 DMA     |
  |                  |                     |                  |
  | HOLD <-----------|---------------------| HOLD             |
  | HLDA ----------->|-------------------->| HLDA             |
  |                  |                     |                  |
  | MEMR# <----------|---+                 | MEMR# ---------->| System MEMR#
  | MEMW# <----------|-+ |                 | MEMW# ---------->| System MEMW#
  | IOR#  <----------|-|-+                 | IOR#  ---------->| System IOR#
  | IOW#  <----------|-|-|-+               | IOW#  ---------->| System IOW#
  +------------------+ | | |               |                  |
                       | | |               | AEN ------------>| Disables CPU Bus Buffers
                       v v v               | ADSTB ---------->| Latches A8-A15 into 74LS373
                 [Bus Tristate Gates]      +------------------+
```

---

## 3. Applications & Real-World Use Cases

1. **Floppy Disk & Hard Drive Sector Transfers**:
   - In the IBM PC architecture, DMA Channel 2 was dedicated to the floppy disk controller. When reading a 512-byte sector, the disk controller asserted $\text{DRQ}_2$ for each byte, streaming data directly to RAM at $500\text{ kbit/s}$ without loading the 8088 CPU.
2. **Point of Sale (POS) Terminals & Electronic Weighing Scales**:
   - Point-of-sale cash registers utilize the 8279 to continuously scan an alphanumeric keypad matrix while refreshing a dual-row 16-character 7-segment customer price display.
3. **Sound Blaster & Audio Streaming**:
   - Vintage PC audio cards used 8257/8237 DMA Channel 1 to stream 8-bit PCM audio samples directly from RAM into the audio DAC, generating stutter-free sound during gameplay.

---

## 4. Solved Numerical & Analytical Examples

### Example 1: 8257 Terminal Count Register Calculation
**Problem**: An 8257 DMA Controller is to transfer a contiguous block of $4096\text{ bytes}$ from a high-speed peripheral into system RAM starting at memory address `20000H` via Channel 1.
1. Determine the 16-bit hex value to be loaded into the Channel 1 DMA Address Register (DAR).
2. Determine the 16-bit hex value to be loaded into the Channel 1 Terminal Count Register (TCR), including the transfer mode bits.
3. How many bus cycles will the transfer require, and how does the 8257 indicate that the block transfer is complete?

#### Solution:
1. **DMA Address Register (DAR)**:
   - The transfer starts at address `20000H`.
   - The 8257 provides a 16-bit address register ($A_{15} - A_0$); the upper 4 address lines ($A_{19} - A_{16} = 2\text{H}$) are generated by an external DMA page latch (e.g., 74LS670).
   - Value for 16-bit DAR = **`0000H`**.

2. **Terminal Count Register (TCR)**:
   - Transfer block length = $4096\text{ bytes} = 1000\text{H}$.
   - Terminal count value = $\text{Count} - 1 = 4096 - 1 = 4095 = \mathbf{0FFFH}$ (`0000 1111 1111 1111B`).
   - Transfer Direction: Peripheral $\to$ Memory $\implies$ **DMA Write Cycle**.
   - Mode bits ($D_{15} D_{14}$):
     - $D_{15} D_{14} = 01_2$ (DMA Write).
   - Combining mode bits with 14-bit count:
     $$\text{TCR} = (01_2 \ll 14) \lor 0\text{FFFH} = 4000\text{H} \lor 0\text{FFFH} = \mathbf{4FFFH}$$

3. **Bus Cycles & Termination**:
   - Since DMA writes occur directly between the peripheral and memory in a single cycle, each byte requires **1 DMA bus cycle**.
   - Total bus cycles required = **4096 cycles**.
   - When the counter decrements from `0000H` to `FFFFH`, the 8257 asserts the **Terminal Count (`TC`) pin HIGH**, signaling completion to the peripheral and asserting an interrupt request to the CPU.

---

### Example 2: 8279 Clock Prescaler Calculation
**Problem**: The 8086 system provides a system clock frequency of $6\text{ MHz}$ to the 8279 `CLK` pin.
- The 8279 internal keyboard scan and display refresh state machines require an internal operational clock frequency of exactly **$100\text{ kHz}$**.
- Determine the 5-bit prescaler divide value ($P$) to be programmed into the 8279 Clock Prescaler Command Word.
- Write the complete 8-bit command byte in hexadecimal.

#### Solution:
1. **Prescaler Formula**:
   $$\text{Prescaler Ratio } P = \frac{f_{\text{CLK}}}{f_{\text{internal}}} = \frac{6\text{ MHz}}{100\text{ kHz}} = \frac{6,000,000}{100,000} = \mathbf{60}$$

2. **8279 Clock Prescaler Command Format**:
   The 8279 command byte format for Set Clock Prescaler is:
   $$\text{Command Code} = 001\text{PPPPP}_2$$
   - Bits $D_7 D_6 D_5 = 001_2$ (Opcode for Clock Prescaler Command).
   - Bits $D_4 D_3 D_2 D_1 D_0 = P = \text{5-bit Prescaler factor}$.
   - Converting $P = 60_{10}$ to 5-bit binary:
     $$60_{10} = 111100_2 \quad (\text{Note: 6 bits!})$$
   - *Crucial Engineering Limitation*: The 8279 prescaler field is only 5 bits wide ($D_4 - D_0$), meaning its maximum programmable division factor is $2^5 - 1 = 31$, or a fixed division range between 2 and 31.
   - For frequencies $> 3.1\text{ MHz}$, an external flip-flop / counter (e.g., 74LS90 divide-by-2) must first divide the $6\text{ MHz}$ CPU clock down to $3\text{ MHz}$ before feeding the 8279 `CLK` pin!
   - With an external prescaler dividing by 2 ($f_{\text{in}} = 3\text{ MHz}$):
     $$P = \frac{3\text{ MHz}}{100\text{ kHz}} = 30_{10} = 11110_2$$
   - Command byte = $0011\ 1110_2 = \mathbf{3EH}$.

---

### Example 3: Comparison of DMA Transfer Modes
**Problem**: A hard disk controller needs to transfer $64\text{ KB}$ of data to memory.
- In **Cycle Stealing (Single Byte) Mode**, the DMA controller requests the bus (`HOLD`), transfers 1 byte, and releases the bus (`HLDA` dropped) for every byte. Bus arbitration overhead is $6\text{ T-states}$ per byte, plus $4\text{ T-states}$ for the DMA transfer.
- In **Burst (Block) Mode**, the DMA controller asserts `HOLD` once, acquires the bus, and transfers all $64\text{ KB}$ continuously at $4\text{ T-states}$ per byte, paying the 6-state arbitration penalty only once at the beginning.
- Clock frequency is $10\text{ MHz}$ ($1\text{ T-state} = 100\text{ ns}$).

Calculate:
1. Total transfer time in Cycle Stealing Mode.
2. Total transfer time in Burst Mode.
3. The percentage speed improvement achieved by Burst Mode.

#### Solution:
1. **Cycle Stealing Mode**:
   $$\text{Clocks per byte} = 6 + 4 = 10\text{ T-states}$$
   $$\text{Total Clocks} = 64 \times 1024 \times 10 = 65,536 \times 10 = 655,360\text{ states}$$
   $$\text{Transfer Time } T_{\text{steal}} = 655,360 \times 100\text{ ns} = \mathbf{65.536\text{ ms}}$$

2. **Burst Mode**:
   $$\text{Total Clocks} = 6 + (65,536 \times 4) = 6 + 262,144 = 262,150\text{ states}$$
   $$\text{Transfer Time } T_{\text{burst}} = 262,150 \times 100\text{ ns} = \mathbf{26.215\text{ ms}}$$

3. **Speed Improvement**:
   $$\text{Time Saved} = 65.536\text{ ms} - 26.215\text{ ms} = 39.321\text{ ms}$$
   $$\text{Percentage Improvement} = \frac{65.536 - 26.215}{65.536} \times 100\% = \mathbf{60.00\%}$$

---

## 5. Previous Year Questions & Solutions

### Question 1 (KTU B.Tech Examination)
**Explain the architecture and working of the 8279 Keyboard and Display Controller with a block diagram. Differentiate between 2-key lockout and N-key rollover.** [9 Marks]

#### Complete Self-Contained Solution:
1. **8279 Internal Architecture**:
   The 8279 is divided into four functional sections:
   - **Keyboard Section**: Scans an $8 \times 8$ matrix (64 switches) using lines $\text{SL}_0 - \text{SL}_3$ and $\text{RL}_0 - \text{RL}_7$. Includes internal 10 ms debouncing circuitry to reject contact bounce.
   - **Display Section**: Contains a $16 \times 8$-bit Display RAM configured as two 4-bit banks ($A_3 - A_0$ and $B_3 - B_0$). It continuously refreshes 7-segment or alphanumeric displays via cathode data pins and scan lines $\text{SL}_0 - \text{SL}_3$.
   - **FIFO / Sensor RAM**: Operates as an 8-byte FIFO in keyboard mode. Stores scancodes of depressed keys along with SHIFT and CONTROL line states, asserting `IRQ` when non-empty.
   - **Scan Counter & Timing Logic**: Generates multiplexing timing in encoded mode (binary $0 - 15$) or decoded mode (4 active low pulses).
   *(Include the functional block diagram from Section 1).*

2. **2-Key Lockout vs N-Key Rollover**:
   - **2-Key Lockout**:
     - Designed to prevent erroneous multi-key inputs.
     - If two keys are pressed simultaneously within the same debouncing scan window, neither key is accepted.
     - If a second key is pressed while the first is held down, the 8279 waits. If the first key is released while the second is still held down, the second key is registered. It only accepts one key at a time.
   - **N-Key Rollover**:
     - Designed for high-speed touch-typists.
     - Treats each key closure independently.
     - Each key depressed is debounced and entered into the 8-byte FIFO in the exact chronological sequence it was pressed, regardless of whether prior keys have been released. If the FIFO fills to capacity (8 bytes), an overrun error flag is set.

---

### Question 2 (KTU B.Tech Examination)
**What is DMA? Explain the operational sequence of the 8257 DMA Controller during a memory-to-device transfer.** [9 Marks]

#### Complete Self-Contained Solution:
1. **Concept of Direct Memory Access (DMA)**:
   Direct Memory Access (DMA) is a specialized hardware data-transfer technique where peripheral devices transfer data blocks directly to or from system memory without passing bytes through CPU internal registers. By eliminating the instruction-fetch and decode overhead of software polling or interrupt loops, DMA maximizes bus bandwidth and achieves data transfer rates bounded only by RAM access speed.

2. **Operational Sequence of 8257 during Memory-to-Device (DMA Read) Transfer**:
   - **Step 1 (Request)**: The peripheral asserts its DMA request line ($\text{DRQ}_n$).
   - **Step 2 (Bus Arbitration)**: The 8257 prioritizes the request and drives its **`HOLD` output pin HIGH** to the 8086 CPU.
   - **Step 3 (Bus Release)**: The 8086 finishes executing its current bus cycle, floats its address, data, and control lines into high impedance, and asserts **`HLDA` (Hold Acknowledge)** back to the 8257.
   - **Step 4 (Bus Mastership & Address Output)**: Upon sampling `HLDA` HIGH, the 8257 becomes the system bus master. It asserts **`AEN` (Address Enable)** to isolate CPU bus drivers. It drives address bits $A_0 - A_7$ on its address pins and outputs high address bits $A_8 - A_{15}$ onto the data bus ($D_0 - D_7$) accompanied by an **`ADSTB` (Address Strobe)** pulse to latch them into an external 74LS373 latch.
   - **Step 5 (Handshake & Transfer)**: The 8257 asserts **$\overline{\text{DACK}}_n$** to acknowledge the peripheral and simultaneously asserts **$\overline{\text{MEMR}}$** (Memory Read) and **$\overline{\text{IOW}}$** (I/O Write).
   - **Step 6 (Data Flow)**: The RAM chip places the addressed byte onto the data bus in response to $\overline{\text{MEMR}}$, and the peripheral latches the byte directly off the data bus in response to $\overline{\text{IOW}}$ in a **single clock cycle**.
   - **Step 7 (Update Registers)**: The 8257 increments the DMA Address Register (DAR) and decrements the Terminal Count Register (TCR).
   - **Step 8 (Termination)**: When the terminal count decrements past zero, the 8257 pulses **`TC` (Terminal Count)** HIGH, drops `HOLD` LOW to return bus control to the 8086 CPU, and de-asserts $\overline{\text{DACK}}_n$.

