# Memory and I/O Interfacing with 8086

> **Senior CS Professor Notes** | Semester 5 — CS305 Microprocessors & Microcontrollers | Module IV

---

## 1. Explanation

### Memory Banking Architecture of the 8086
The 8086 microprocessor has a 20-bit address bus ($A_{19} - A_0$), providing a physical address space of:
$$2^{20} = 1,048,576 \text{ bytes} = 1\text{ MB}$$

However, the external data bus is **16 bits wide** ($D_{15} - D_0$). To allow both 8-bit (byte) and 16-bit (word) operations to take place seamlessly, the 1 MB physical address space is split into two independent memory banks of $512\text{ KB}$ each:

```
               1 MB Physical Memory Space
      +-------------------------------------------+
      |                                           |
      v                                           v
+-----------------------+               +-----------------------+
|   EVEN (LOW) BANK     |               |    ODD (HIGH) BANK    |
|   512 KB              |               |    512 KB             |
|   Addresses: 0,2,4... |               |   Addresses: 1,3,5... |
|   Connected to D7-D0  |               |   Connected to D15-D8 |
+-----------------------+               +-----------------------+
           ^                                       ^
           |                                       |
    Selected by A0 = 0                     Selected by BHE# = 0
```

1. **Even (Low) Bank**:
   - Contains all even byte addresses: `00000H`, `00002H`, `00004H`, ..., `FFFFEH`.
   - Connected directly to the lower half of the data bus: **$D_7 - D_0$**.
   - Activated when address line **$A_0 = 0$**.
2. **Odd (High) Bank**:
   - Contains all odd byte addresses: `00001H`, `00003H`, `00005H`, ..., `FFFFFH`.
   - Connected directly to the upper half of the data bus: **$D_{15} - D_8$**.
   - Activated when **$\overline{\text{BHE}}$ (Bus High Enable)** is asserted low ($\overline{\text{BHE}} = 0$).

#### Bank Selection Control Logic
During any bus transfer, address line $A_0$ and the status signal $\overline{\text{BHE}}$ coordinate which bank(s) participate in the transfer:

| $\overline{\text{BHE}}$ | $A_0$ | Operation Type | Active Data Lines | Bus Cycles Required |
|---|---|---|---|---|
| `0` | `0` | **16-bit Word access at Even (Aligned) Address** | $D_{15} - D_0$ (Both Banks) | **1 Bus Cycle** (4 T-states) |
| `1` | `0` | **8-bit Byte access at Even Address** | $D_7 - D_0$ (Even Bank) | **1 Bus Cycle** (4 T-states) |
| `0` | `1` | **8-bit Byte access at Odd Address** | $D_{15} - D_8$ (Odd Bank) | **1 Bus Cycle** (4 T-states) |
| `1` | `1` | **No operation** (Idle Bus) | None (High-Z) | None |

#### Aligned vs. Misaligned Word Access Penalty
- **Aligned Word**: A 16-bit word whose starting address is an even number (e.g., `MOV AX, [2000H]`).
  - Both $A_0 = 0$ and $\overline{\text{BHE}} = 0$ are asserted simultaneously.
  - Byte at `2000H` is read over $D_7 - D_0$, while byte at `2001H` is read over $D_{15} - D_8$ in a single 4-clock bus cycle!
- **Misaligned Word**: A 16-bit word starting at an odd address (e.g., `MOV AX, [2001H]`).
  - Cannot be transferred in one cycle because the low byte (`2001H`) is in the Odd Bank and the high byte (`2002H`) is in the Even Bank.
  - The 8086 automatically initiates **two consecutive bus cycles**:
    1. **Cycle 1**: Access byte at odd address `2001H` ($\overline{\text{BHE}}=0, A_0=1$) using $D_{15}-D_8$.
    2. **Cycle 2**: Access byte at even address `2002H` ($\overline{\text{BHE}}=1, A_0=0$) using $D_7-D_0$.
  - **Penalty**: Execution time doubles (8 T-states instead of 4 T-states). This is why optimizing compilers align data structures to 16-bit (or 32/64-bit) boundaries.

---

### Address Decoding Techniques
To interface physical memory chips (e.g., $32\text{ KB}$ SRAM or $64\text{ KB}$ EPROM) to the 20-bit address bus of the 8086, address lines must be divided into:
1. **Internal Chip Address Lines**: Connected to the chip's internal address pins ($A_{k-1} - A_0$ where $2^k$ is chip capacity in bytes).
2. **Chip Select ($\overline{\text{CS}}$) Decoding Lines**: Connected to address decoder circuits (such as the 3-to-8 decoder **74LS138**) to generate unique chip-enable pulses.

#### 1. Full Address Decoding
- **Principle**: Every single address line ($A_{19} - A_0$) is strictly decoded. No address bit is left floating or unused.
- **Advantage**: Each physical memory location responds to **one and only one** unique address. No memory shadowing or address aliasing occurs.
- **Disadvantage**: Requires more complex logic gates and decoders.

#### 2. Partial Address Decoding
- **Principle**: High-order address lines are ignored or left unattached to simplify decoder circuitry.
- **Advantage**: Lower chip count and cheaper circuit board routing.
- **Disadvantage**: Causes **Address Aliasing (Shadowing)**—the same physical memory location appears at multiple distinct addresses throughout the memory map.

---

### The 74LS138 3-to-8 Decoder
The standard industrial building block for memory and I/O address decoding is the **74LS138**:

```
                 74LS138 3-to-8 Decoder
                 +--------------------+
     G1 (High) --| G1                 |
    G2A# (Low) --| G2A#            Y0#|--> Chip Select 0
    G2B# (Low) --| G2B#            Y1#|--> Chip Select 1
                 |                 Y2#|--> Chip Select 2
       A (Addr) -| A               Y3#|--> Chip Select 3
       B (Addr) -| B               Y4#|--> Chip Select 4
       C (Addr) -| C               Y5#|--> Chip Select 5
                 |                 Y6#|--> Chip Select 6
                 |                 Y7#|--> Chip Select 7
                 +--------------------+
```

- **Enable Condition**: $G_1 = 1 \land \overline{G_{2A}} = 0 \land \overline{G_{2B}} = 0$. If enabled, exactly one active-low output ($\overline{Y_0} - \overline{Y_7}$) goes low matching the binary value on inputs $C B A$.

---

### Memory-Mapped I/O vs. I/O-Mapped I/O (Isolated I/O)

Microprocessors communicate with peripheral registers using one of two fundamental architectural philosophies:

```
    Memory-Mapped I/O                      I/O-Mapped (Isolated) I/O
+-----------------------+              +-----------------------+  +-------------------+
| 00000H                |              | 00000H                |  | 0000H             |
|                       |              |                       |  |                   |
| System Memory (RAM)   |              | System Memory (RAM)   |  | Peripheral Ports  |
|                       |              |                       |  | (64 KB space)     |
+-----------------------+              |                       |  |                   |
| F0000H                |              |                       |  +-------------------+
| Peripheral Registers  |              |                       |  (Controlled by      |
+-----------------------+              +-----------------------+   M/IO# = 0)         |
| FFFFFH                |              | FFFFFH                |                      |
+-----------------------+              +-----------------------+                      |
(Shared 1 MB Space,                    (Separate 1 MB Space,                          |
 M/IO# = 1 always)                      Controlled by M/IO# = 1)                      |
```

| Architectural Feature | Memory-Mapped I/O | I/O-Mapped (Isolated) I/O |
|---|---|---|
| **Address Space** | I/O ports share the 1 MB memory address space. | Separate 64 KB I/O space ($0000\text{H} - \text{FFFF}\text{H}$). |
| **Control Signal** | $\overline{\text{MEMR}}, \overline{\text{MEMW}}$ ($M/\overline{\text{IO}} = 1$) | $\overline{\text{IOR}}, \overline{\text{IOW}}$ ($M/\overline{\text{IO}} = 0$) |
| **Instructions Used** | Any memory instruction (`MOV`, `ADD`, `TEST`, `AND`, `OR`, `CMP`). | Dedicated `IN` and `OUT` instructions only. |
| **Speed & Efficiency** | Slower; complex addressing modes consume more instruction bytes. | Faster execution; dedicated 1-byte / 2-byte opcodes. |
| **Register Flexibility**| Any general-purpose register (`AX`, `BX`, `CX`, `DX`, `SI`, `DI`) can read/write ports. | Data transfers must pass exclusively through accumulator (`AL` or `AX`). |
| **Address Bus Width** | Full 20 bits ($A_{19} - A_0$) decoded. | 8-bit direct ($A_7 - A_0$) or 16-bit indirect via `DX` ($A_{15} - A_0$). |
| **Hardware Overhead** | Complex full 20-bit decoding decoders. | Simpler decoders (decodes only 8 or 16 address lines). |

---

## 2. Example: Memory Interfacing Circuit

### Interfacing 64 KB RAM (Two $32\text{ KB}$ SRAMs) to 8086
- System needs $64\text{ KB}$ total RAM:
  - Banked into: $32\text{ KB}$ Even Bank SRAM + $32\text{ KB}$ Odd Bank SRAM.
  - Chip Capacity: $32\text{ KB} = 2^{15} \text{ bytes}$.
  - Internal Chip Address Lines: 15 lines ($A_{15} - A_1$). Notice that $A_0$ is **not** connected to chip address pins; it is used for bank selection!
  - Chip Select Decoding: Address lines $A_{19} - A_{16}$ and $M/\overline{\text{IO}}$ decode the address range.

```
                     +---------------------------------------+
                     |           8086 CPU BUS                |
                     +---------------------------------------+
                           | A19-A16       | A15-A1         | D15-D8       | D7-D0
                           |               |                |              |
                    +------v------+        |                |              |
                    |   74LS138   |        |                |              |
       M/IO# ------>| G1  Decoder |        |                |              |
       A19   ------>| G2A#        |        |                |              |
       A18   ------>| G2B#        |        |                |              |
       A17   ------>| C           |        |                |              |
       A16   ------>| B        Y0#|---+    |                |              |
                    +-------------+   |    |                |              |
                                      |    |                |              |
              +-----------------------+    |                |              |
              |                            |                |              |
       BHE# --|--------+                   |                |              |
              |        v                   |                |              |
              |     +-----+                |                |              |
              +---->| OR  |--- CS_ODD# ----|------------+   |              |
                    +-----+                |            |   |              |
                                           |            v   v              |
       A0 ----|--------+                   |     +------------------+      |
              |        v                   |     | 32 KB ODD SRAM   |      |
              |     +-----+                |     | (Addresses 1,3..)|<-----+
              +---->| OR  |--- CS_EVEN# ---|--+  | A14-A0 <-> A15-A1|
                    +-----+                |  |  | D7-D0  <-> D15-D8|
                                           |  |  +------------------+
                                           |  |
                                           |  v
                                           |  +------------------+
                                           |  | 32 KB EVEN SRAM  |
                                           |  | (Addresses 0,2..)|<--------+
                                           +->| A14-A0 <-> A15-A1|
                                              | D7-D0  <-> D7-D0 |
                                              +------------------+
```

---

## 3. Applications & Real-World Use Cases

1. **High-Speed Network Interface Buffers**:
   - Network controllers (e.g., Ethernet NICs) use memory-mapped I/O ring buffers mapped directly into 8086 high memory. This enables the CPU to use `REP MOVSW` string instructions to copy megabytes of network packets at raw memory-bus speeds without incurring `IN`/`OUT` loop overhead.
2. **Industrial Sensor DAQ Cards**:
   - Data Acquisition Cards with 12-bit Analog-to-Digital Converters (ADCs) interface via I/O-mapped ports using address decoders like 74LS138. The CPU reads sensor voltages with simple `IN AL, DX` instructions.
3. **Automotive Electronic Control Units (ECUs)**:
   - Microcontrollers interface to flash memory and SRAM banks using odd/even byte banking to ensure real-time engine spark timing look-up tables can be fetched in single-cycle 16-bit word bursts.

---

## 4. Solved Numerical & Analytical Examples

### Example 1: Interfacing 64 KB EPROM and 64 KB SRAM
**Problem**: Design an 8086 memory system with the following specifications:
- **$64\text{ KB}$ EPROM** mapped to the top of memory ending at `FFFFFH`.
- **$64\text{ KB}$ SRAM** mapped starting from address `00000H`.
- Available memory chips: $32\text{ KB} \times 8$ EPROM chips and $32\text{ KB} \times 8$ SRAM chips.
- Use 74LS138 decoders.

Determine:
1. The memory map and starting/ending addresses for each bank.
2. The number of address pins required per chip.
3. The decoding logic and connections for the 74LS138 decoder.

#### Solution:

**Step 1: Address Space & Chip Allocation**
- Total EPROM = $64\text{ KB}$. Ending address is `FFFFFH`.
  - Starting address = $\text{FFFFFH} - 64\text{ KB} + 1 = \text{FFFFFH} - 0FFFF\text{H} = \mathbf{F0000H}$.
  - Range: `F0000H` to `FFFFFH`.
  - Implemented using two $32\text{ KB} \times 8$ chips:
    - **Even EPROM Bank**: Addresses `F0000H, F0002H, ..., FFFFEH` (Data bus $D_7 - D_0$).
    - **Odd EPROM Bank**: Addresses `F0001H, F0003H, ..., FFFFFH` (Data bus $D_{15} - D_8$).
- Total SRAM = $64\text{ KB}$. Starting address is `00000H`.
  - Ending address = $00000\text{H} + 64\text{ KB} - 1 = \mathbf{0FFFFH}$.
  - Range: `00000H` to `0FFFFH`.
  - Implemented using two $32\text{ KB} \times 8$ chips:
    - **Even SRAM Bank**: Addresses `00000H, 00002H, ..., 0FFFEH` (Data bus $D_7 - D_0$).
    - **Odd SRAM Bank**: Addresses `00001H, 00003H, ..., 0FFFFH` (Data bus $D_{15} - D_8$).

**Step 2: Internal Address Line Connections**
- Each chip has capacity $32\text{ KB} = 2^{15} \text{ bytes}$.
- Each chip requires **15 address lines**: internal pins $A_{14} - A_0$.
- These are connected to CPU address lines **$A_{15} - A_1$** (since CPU $A_0$ is dedicated to bank selection).

**Step 3: Decoder Logic ($A_{19} - A_{16}$)**
Let us analyze address lines $A_{19}, A_{18}, A_{17}, A_{16}$:
- For SRAM (`00000H` to `0FFFFH`):
  - $A_{19} A_{18} A_{17} A_{16} = 0000_2$.
- For EPROM (`F0000H` to `FFFFFH`):
  - $A_{19} A_{18} A_{17} A_{16} = 1111_2$.

Using a 74LS138 decoder:
- Connect CPU $M/\overline{\text{IO}}$ to enable input $G_1$ (ensuring decoder is active only during memory cycles).
- Connect $A_{19}, A_{18}, A_{17}$ to decoder select inputs $C, B, A$.
- Decoder output $\overline{Y_0}$ is active low when $A_{19} A_{18} A_{17} = 000_2$ (selects SRAM block).
- Decoder output $\overline{Y_7}$ is active low when $A_{19} A_{18} A_{17} = 111_2$ (selects EPROM block).

**Step 4: Bank Enable Gating**
To generate individual chip selects:
- **Even SRAM $\overline{\text{CS}}$**: $\overline{Y_0} \text{ OR } A_0$
- **Odd SRAM $\overline{\text{CS}}$**: $\overline{Y_0} \text{ OR } \overline{\text{BHE}}$
- **Even EPROM $\overline{\text{CS}}$**: $\overline{Y_7} \text{ OR } A_0$
- **Odd EPROM $\overline{\text{CS}}$**: $\overline{Y_7} \text{ OR } \overline{\text{BHE}}$

---

### Example 2: Calculating Wait States for Slow Memory
**Problem**: An 8086 microprocessor runs at a clock frequency of $8\text{ MHz}$.
- The CPU is interfaced to an EPROM having an address access time ($t_{\text{ACC}}$) of $420\text{ ns}$.
- The address propagation delay through the bus latch (74LS373) is $25\text{ ns}$.
- The decoder propagation delay (74LS138) is $20\text{ ns}$.
- Data setup time required by the 8086 prior to clock edge is $t_{\text{DS}} = 30\text{ ns}$.
- In an 8086 bus cycle, address is valid from $T_1$, and data is sampled at the end of $T_3$.

Determine:
1. The available memory access time in a standard 4-clock cycle without wait states.
2. The number of Wait States ($T_W$) that must be inserted into each read cycle to ensure reliable data reading.

#### Solution:

**Step 1: Clock Period Calculation**
$$T = \frac{1}{f} = \frac{1}{8\text{ MHz}} = 125\text{ ns}$$

**Step 2: Total Memory Access Time Required ($t_{\text{REQ}}$)**
$$\begin{aligned}
t_{\text{REQ}} &= t_{\text{latch}} + t_{\text{decoder}} + t_{\text{ACC}} + t_{\text{DS}} \\
&= 25\text{ ns} + 20\text{ ns} + 420\text{ ns} + 30\text{ ns} = \mathbf{495\text{ ns}}
\end{aligned}$$

**Step 3: Available Time in Normal 4-Clock Bus Cycle**
In an 8086 read cycle, the address is output in $T_1$, and data is latched at the falling edge of clock in $T_3$.
The time window between address valid and data latching is approximately 3 clock periods minus internal delays (typically $3T - t_{\text{CLAV}}$).
Taking the nominal 3 clock periods:
$$t_{\text{AVAIL}} = 3 \times T = 3 \times 125\text{ ns} = 375\text{ ns}$$

Since $t_{\text{REQ}} (495\text{ ns}) > t_{\text{AVAIL}} (375\text{ ns})$, the memory is **too slow** and will cause data corruption without wait states!
$$\text{Deficit} = 495\text{ ns} - 375\text{ ns} = 120\text{ ns}$$

**Step 4: Calculating Number of Wait States**
Each inserted wait state ($T_W$) adds exactly one clock cycle ($125\text{ ns}$) between $T_3$ and $T_4$:
$$\text{Time with 1 Wait State} = 375\text{ ns} + 125\text{ ns} = 500\text{ ns}$$
Since $500\text{ ns} \ge 495\text{ ns}$, **exactly ONE wait state ($N = 1$)** must be inserted by asserting the 8086 `READY` line low during $T_3$.

---

### Example 3: Decoding I/O Port Addresses
**Problem**: An 8-bit output port (8-bit latch 74LS374) is interfaced to an 8086 microprocessor using isolated I/O.
- The port must respond to the 8-bit port address `F8H`.
- Show how a 74LS138 decoder and basic gates are used to generate the clock pulse ($\text{CLK}$) for the latch.
- Write the assembly language instruction sequence to output data `55H` to this port.

#### Solution:

**Step 1: Address Bit Analysis for Port `F8H`**
- Port address `F8H` in binary:
  $$\text{F8H} = 1111\ 1000_2$$
  $$A_7 A_6 A_5 A_4 A_3 A_2 A_1 A_0 = 1\ 1\ 1\ 1\ 1\ 0\ 0\ 0$$

**Step 2: Decoding Circuit Design**
- For Isolated I/O write operations, the 8086 asserts:
  $$M/\overline{\text{IO}} = 0 \quad \text{and} \quad \overline{\text{WR}} = 0 \implies \overline{\text{IOW}} = 0$$
- Connect upper address bits $A_7, A_6, A_5, A_4, A_3$ to a 5-input AND gate to verify that $A_7 A_6 A_5 A_4 A_3 = 11111_2$. Output = $HIGH$.
- Connect this output to the active-high enable $G_1$ of the 74LS138 decoder.
- Connect CPU $M/\overline{\text{IO}}$ to active-low enable $\overline{G_{2A}}$.
- Connect CPU $\overline{\text{IOW}}$ to active-low enable $\overline{G_{2B}}$.
- Connect lower address lines $A_2, A_1, A_0$ to decoder select inputs $C, B, A$.
- When $A_2 A_1 A_0 = 000_2$, output $\mathbf{\overline{Y_0}}$ of the 74LS138 goes LOW.
- Inverting $\overline{Y_0}$ with a 74LS04 NOT gate produces the active-high clock pulse required by the 74LS374 output latch.

**Step 3: Assembly Language Code**
```assembly
MOV AL, 55H       ; Load byte 55H into accumulator AL
OUT 0F8H, AL      ; Output byte to 8-bit port address F8H
```

---

## 5. Previous Year Questions & Solutions

### Question 1 (KTU B.Tech Examination)
**Explain the memory banking scheme in 8086 microprocessor with a neat diagram. Why is memory banked in 8086? What happens during aligned and misaligned word access?** [9 Marks]

#### Complete Self-Contained Solution:
1. **Why Memory is Banked**:
   The 8086 is a 16-bit processor with a 16-bit data bus ($D_{15} - D_0$), but byte-level addressability is mandatory to support 8-bit character manipulation, legacy software, and compact data structures. If memory were organized as a monolithic $1\text{ MB} \times 16$ block, reading or writing a single 8-bit byte would overwrite or corrupt the adjacent byte in that 16-bit word. By splitting the 1 MB memory space into two $512\text{ KB}$ byte-wide banks (Even Bank and Odd Bank), the CPU can independently activate either bank for 8-bit byte operations or activate both banks simultaneously for 16-bit word operations.

2. **Memory Bank Organization**:
   - **Even Bank ($512\text{ KB}$)**: Contains bytes at even addresses (`00000H, 00002H, ...`). Wired to data bus lines $D_7 - D_0$. Enabled when $A_0 = 0$.
   - **Odd Bank ($512\text{ KB}$)**: Contains bytes at odd addresses (`00001H, 00003H, ...`). Wired to data bus lines $D_{15} - D_8$. Enabled when $\overline{\text{BHE}} = 0$.
   - *(Include the block diagram and bank selection table given in Section 1).*

3. **Aligned vs Misaligned Word Access**:
   - **Aligned Word Access**:
     When a 16-bit word is stored at an even starting address (e.g., `MOV AX, [1000H]`), the low byte resides at `1000H` (Even Bank) and the high byte resides at `1001H` (Odd Bank). The 8086 asserts $A_0 = 0$ and $\overline{\text{BHE}} = 0$ simultaneously. Both banks are enabled in the same bus cycle, transferring all 16 bits across $D_{15} - D_0$ in **a single bus cycle (4 T-states)**.
   - **Misaligned Word Access**:
     When a 16-bit word is stored at an odd starting address (e.g., `MOV AX, [1001H]`), the low byte is at `1001H` (Odd Bank) and the high byte is at `1002H` (Even Bank). The CPU cannot read both simultaneously. It executes **two consecutive bus cycles**:
       - *Cycle 1*: Reads low byte at `1001H` over $D_{15} - D_8$ ($A_0 = 1, \overline{\text{BHE}} = 0$).
       - *Cycle 2*: Reads high byte at `1002H` over $D_7 - D_0$ ($A_0 = 0, \overline{\text{BHE}} = 1$).
     The internal Execution Unit automatically swaps the bytes to assemble the correct 16-bit word in register `AX`. Misaligned access incurs a performance penalty of **8 T-states instead of 4 T-states**.

---

### Question 2 (KTU B.Tech Examination)
**Compare Memory-Mapped I/O and I/O-Mapped I/O. Under what circumstances would an engineer choose one over the other?** [9 Marks]

#### Complete Self-Contained Solution:
1. **Comparative Analysis Table**:
   *(Include the comprehensive comparison table contrasting Address Space, Control Signals, Instructions, Speed, Register Flexibility, and Hardware Overhead from Section 1).*

2. **Engineering Selection Criteria**:
   - **When to Choose Memory-Mapped I/O**:
     - *High-Throughput Buffer Access*: High-speed devices (graphic frame buffers, high-speed network interfaces, DSP memory buffers) benefit from the rich set of memory instructions (`MOV`, `TEST`, `CMP`, `REP MOVSW`). The CPU can manipulate peripheral registers and buffer memory directly without first moving data through the accumulator.
     - *Large Number of Ports*: Embedded systems with thousands of control/status registers that easily exceed the 64 KB limit of isolated I/O.
   - **When to Choose I/O-Mapped (Isolated) I/O**:
     - *Preserving Main Memory Space*: Small systems where the entire 1 MB address space must be preserved for program code (ROM) and data storage (RAM) rather than being consumed by peripheral registers.
     - *Simpler Decoding Hardware*: Microcontroller/embedded applications where decoding only an 8-bit port address reduces the cost and pin count of decoders.
     - *Strict Separation of Code and Peripherals*: Enhances system reliability by preventing wild pointer bugs in user code from accidentally overwriting critical peripheral control registers.

