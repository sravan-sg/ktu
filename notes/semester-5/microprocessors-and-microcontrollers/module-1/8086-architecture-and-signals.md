# 8086 Architecture and Signals

## 1. Explanation

### Why the 8086 Matters

The Intel 8086 (1978) was the world's first fully 16-bit microprocessor and the founding chip of the x86 architecture. Every Intel Core i9, AMD Ryzen 9, and server Xeon processor today is a direct architectural descendant. Understanding 8086 means understanding the DNA of modern computing.

The 8086 introduced the concept of a **pipelined CPU** at the microprocessor level — it fetches the next instruction while executing the current one. This "instruction pre-fetch queue" is the ancestor of today's 20+ stage superscalar pipelines.

---

### Internal Architecture: The BIU and EU Model

The 8086 is internally divided into two **independent, pipelined functional units** that operate concurrently:

```
┌─────────────────────────────────────────────────────────────────────┐
│                      8086 MICROPROCESSOR                            │
│                                                                     │
│  ┌────────────────────────────┐   ┌──────────────────────────────┐  │
│  │  BUS INTERFACE UNIT (BIU)  │   │    EXECUTION UNIT (EU)       │  │
│  │                            │   │                              │  │
│  │  Segment Registers:        │   │  General Purpose Registers:  │  │
│  │  ┌────┐ ┌────┐ ┌────┐     │   │  AX = AH | AL  (Accumulator) │  │
│  │  │ CS │ │ DS │ │ SS │     │   │  BX = BH | BL  (Base)        │  │
│  │  └────┘ └────┘ └────┘     │   │  CX = CH | CL  (Count)       │  │
│  │  ┌────┐                   │   │  DX = DH | DL  (Data)        │  │
│  │  │ ES │                   │   │                              │  │
│  │  └────┘                   │   │  Pointer/Index Registers:    │  │
│  │                           │   │  SP (Stack Pointer)          │  │
│  │  Instruction Pointer:     │   │  BP (Base Pointer)           │  │
│  │  ┌────────┐               │   │  SI (Source Index)           │  │
│  │  │  IP    │               │   │  DI (Destination Index)      │  │
│  │  └────────┘               │   │                              │  │
│  │                           │   │  ALU (16-bit)                │  │
│  │  6-Byte Pre-fetch Queue:  │   │  ┌──────────────────────┐    │  │
│  │  ┌──┬──┬──┬──┬──┬──┐     │   │  │  Arithmetic/Logic     │    │  │
│  │  │I6│I5│I4│I3│I2│I1│     │   │  │  Operations Unit     │    │  │
│  │  └──┴──┴──┴──┴──┴──┘     │   │  └──────────────────────┘    │  │
│  │  Bus Control Logic        │   │                              │  │
│  │                           │   │  Flags Register (F):        │  │
│  │  Address Adder (+)        │   │  CF AF PF ZF SF TF IF DF OF │  │
│  └────────────────────────┬──┘   └────────────────────────────┘  │
│                           │                │                       │
│                           │  Internal Bus  │                       │
│                           └────────────────┘                       │
│                                                                     │
│               External 20-bit Address Bus (A0–A19)                 │
│               External 16-bit Data Bus (D0–D15)                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Bus Interface Unit (BIU) — The Memory Traffic Manager

The BIU is responsible for **all interactions with external memory and I/O**. It has 4 key functions:

1. **Instruction Pre-fetching**: Fetches instruction bytes from memory into the **6-byte prefetch queue** (a FIFO buffer). The EU reads instructions from this queue — not directly from memory. This decouples fetch from execute, enabling pipelining.

2. **Physical Address Generation**: Computes the 20-bit physical memory address by combining a 16-bit segment register with the 16-bit offset address:
   $$\text{Physical Address (PA)} = (\text{Segment Register} \times 16) + \text{Offset}$$
   Multiplying by 16 is equivalent to shifting left by 4 bits, extending the 16-bit register to 20 bits and adding the offset.

3. **Bus Control**: Generates all control signals for external bus transactions (ALE, RD#, WR#, etc.).

4. **Segment Register Management**: Maintains 4 segment registers that point to 4 active memory segments simultaneously:

| Segment Register | Points To | Default Usage |
|---|---|---|
| **CS (Code Segment)** | Executable code | IP always offsets from CS: `CS:IP` |
| **DS (Data Segment)** | Program data variables | Most data instructions use DS |
| **SS (Stack Segment)** | Stack memory | PUSH/POP use SP as offset from SS |
| **ES (Extra Segment)** | Auxiliary data | String destination operations (STOS, MOVS) use ES:DI |

---

### Execution Unit (EU) — The Computation Engine

The EU **never accesses memory directly**. It:
- Receives pre-fetched instruction bytes from the BIU's queue
- Decodes instructions and executes ALU operations
- When memory access is needed, hands the **effective address** (offset) to the BIU and waits

#### General-Purpose Registers (all 16-bit, all byte-addressable)

| Register | High Byte | Low Byte | Primary Purpose |
|---|---|---|---|
| AX | AH | AL | Accumulator — arithmetic, I/O, multiply/divide |
| BX | BH | BL | Base — memory addressing, table lookup |
| CX | CH | CL | Counter — LOOP, REP, shift count |
| DX | DH | DL | Data — multiply/divide extension, I/O port address |

#### Pointer and Index Registers (16-bit only)

| Register | Purpose | Default Segment |
|---|---|---|
| SP (Stack Pointer) | Points to top of stack | SS:SP |
| BP (Base Pointer) | Stack frame access (function parameters) | SS:BP |
| SI (Source Index) | Source address in string operations | DS:SI |
| DI (Destination Index) | Destination address in string operations | ES:DI |

#### Flags Register (16-bit, 9 bits used)

| Flag | Name | Set When |
|---|---|---|
| CF | Carry Flag | Carry/borrow out of bit 15 |
| PF | Parity Flag | Low byte of result has even number of 1s |
| AF | Auxiliary Carry Flag | Carry out of bit 3 (BCD arithmetic) |
| ZF | Zero Flag | Result = 0 |
| SF | Sign Flag | Result bit 15 = 1 (negative in 2's complement) |
| TF | Trap Flag | Single-step mode (debug) |
| IF | Interrupt Flag | Maskable interrupt enable (STI/CLI) |
| DF | Direction Flag | String operation direction (CLD=forward, STD=backward) |
| OF | Overflow Flag | Signed arithmetic overflow |

---

### Physical Address Generation — The Key Formula

The 8086 has a **20-bit address bus** but only **16-bit registers**. With 20 address bits, it can address $2^{20} = 1,048,576$ bytes = **1 MB** of memory.

The BIU computes the physical address using:
$$\text{PA} = \text{Segment} \times 16 + \text{Offset} = (\text{Seg} \ll 4) + \text{Off}$$

**Example**: Code is at CS = 1000H, IP = 2345H:
$$\text{PA} = 1000H \times 10H + 2345H = 10000H + 2345H = 12345H$$

**Important**: Different segment:offset combinations can yield the **same physical address** (aliasing). For example, CS=1000H:IP=2345H and CS=1234H:IP=0005H both give PA=12345H.

---

### 8086 Signal Descriptions

The 8086 has 40 pins. Many pins are **multiplexed** (serve dual purposes depending on timing):

#### Address/Data Multiplexed Bus (Pins 2–16, 39)
- **AD0–AD15**: During the first clock cycle (T1) of a bus cycle, these carry the **lower 16 bits** of the 20-bit address. During T2–T4, they carry the **16-bit data** (read or write).
- **A16–A19**: The upper 4 address bits — present only during T1; also carry status (S3–S6) during T2–T4.
- **ALE (Address Latch Enable)**: Pulses HIGH during T1 to signal that the multiplexed address/data bus currently carries a valid address. External 74LS373 latches capture the address at this point.

#### Control Signals

| Signal | Direction | Function |
|---|---|---|
| **ALE** | Out | Address Latch Enable: demultiplexes address from data bus |
| **BHE#** | Out | Bus High Enable: selects the high byte (D8–D15) of data bus. With A0=0: word access; A0=0,BHE#=1: even byte; A0=1,BHE#=0: odd byte |
| **RD#** | Out | Read: active low, signals memory or I/O to put data on bus |
| **WR#** | Out | Write: active low, signals memory or I/O to accept data from bus |
| **M/IO#** | Out | Memory or I/O select: HIGH = memory access; LOW = I/O access |
| **DT/R#** | Out | Data Transmit/Receive: direction control for 8286 bus transceiver |
| **DEN#** | Out | Data Enable: enables data bus transceivers during data transfer phase |
| **READY** | In | Wait state input: pulled LOW by slow memory/peripherals to insert wait states (Tw) |
| **HOLD** | In | DMA request: another master requests bus control |
| **HLDA** | Out | Hold Acknowledge: 8086 relinquishes bus to DMA controller |
| **INTR** | In | Maskable Interrupt Request (checked when IF=1) |
| **NMI** | In | Non-Maskable Interrupt (Type 2, always serviced) |
| **RESET** | In | Resets CPU; CS=FFFFH, IP=0000H; starts executing at FFFF0H |
| **CLK** | In | System clock (8MHz for 8086-2, 10MHz for 8086-1) |
| **MN/MX#** | In | Minimum/Maximum mode select (tied to VCC or GND) |

---

### Minimum Mode vs Maximum Mode

| Feature | Minimum Mode (MN/MX# = VCC) | Maximum Mode (MN/MX# = GND) |
|---|---|---|
| **Control Signal Source** | 8086 itself generates all bus control signals | 8288 Bus Controller generates bus control from 8086 status lines S0#, S1#, S2# |
| **Status Signals** | S0#, S1#, S2# not present (pins used for INTA#, ALE, DEN#, DT/R#, M/IO#, WR#) | S0#, S1#, S2# issued by 8086 (decoded by 8288) |
| **Request/Grant** | HOLD/HLDA (for DMA) | RQ#/GT0#, RQ#/GT1# (bidirectional, for multi-master arbitration) |
| **Queue Status** | Not available | QS0, QS1 (allow math coprocessor 8087 to track instruction queue) |
| **Bus Arbitration** | Simple, single master | Full multi-processor bus arbitration |
| **System Complexity** | Simple, requires fewer chips | Complex, requires 8288 Bus Controller |
| **Typical Use** | Single-processor systems | Multi-processor systems (8086 + 8087 FPU) |

---

### Why Pipelining the BIU and EU?

Consider execution without pipelining:
- Fetch instruction → Execute → Fetch next → Execute next...
- The bus is idle during execution; the ALU is idle during fetch.

With BIU/EU pipeline:
- While EU **executes** instruction N, BIU **prefetches** instruction N+1 and N+2 into the 6-byte queue.
- Approximately doubles throughput for sequential code with no branches.
- On a branch instruction, the queue is **flushed** (invalidated) and refilled from the branch target. This is the branch prediction problem in modern CPUs.

---

## 2. Example

### Physical Address Calculation Examples

**Example A**: DS = 2000H, offset = 0500H
$$\text{PA} = 2000H \times 10H + 0500H = 20000H + 0500H = 20500H$$

**Example B**: SS = 5000H, SP = 00FEH
$$\text{PA (Stack)} = 5000H \times 10H + 00FEH = 50000H + 00FEH = 500FEH$$

**Example C**: Given PA = 3A4F0H. If CS = 3A00H, what is IP?
$$\text{IP} = \text{PA} - (\text{CS} \times 10H) = 3A4F0H - 3A000H = 004F0H$$

---

### Segmented Memory Map (1MB = 00000H to FFFFFH)

```
FFFFFH ┌──────────────────────────┐
       │  BIOS ROM (64KB)         │ ← Reset vector at FFFF0H (CS=FFFFH:IP=0000H)
F0000H ├──────────────────────────┤
       │  Expansion ROM area       │
C0000H ├──────────────────────────┤
       │  Video BIOS/Buffer       │ ← CGA/MDA video memory
A0000H ├──────────────────────────┤
       │  User Program + Data     │ ← Application code and data
       │  (up to 640 KB usable)   │
       │                          │
00400H ├──────────────────────────┤
       │  BIOS Data Area (256 B)  │
00300H ├──────────────────────────┤
       │  Interrupt Vector Table  │ ← 1 KB: 256 vectors × 4 bytes (IP:CS)
00000H └──────────────────────────┘
```

---

## 3. Applications & Use Cases

### 1. Embedded Industrial Controllers
The 8086 and its variants (80C86, 80186) are still used in some industrial PLCs (Programmable Logic Controllers) because of their deterministic timing behavior and massive ecosystem of assembly-level software. SCADA systems in chemical plants ran on 8086-based hardware for decades.

### 2. PC/XT Historical Systems & Legacy Emulation
IBM PC XT (1983) used the 8088 (8-bit data bus variant of 8086). Understanding the 8086 is essential for maintaining or emulating legacy industrial PC-based systems still in production environments.

### 3. Architecture Education
x86 assembly on the 8086 is the standard foundation for teaching computer organization worldwide. The segment:offset addressing scheme directly teaches memory hierarchy concepts that apply to modern virtual memory management.

### 4. Modern x86 Real-Mode Boot
Modern x86 CPUs still boot in **8086 Real Mode** (16-bit) for the first few instructions after power-on RESET. UEFI firmware switches the CPU from Real Mode → Protected Mode → Long Mode during the boot sequence. Understanding 8086 mode is mandatory for bootloader developers and OS kernel engineers.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Physical Address Calculation [Standard KTU Part A — 3 marks]

**Problem**: Compute the physical address if DS = 1234H and the effective address (offset) = 5678H.

**Solution**:
$$\text{PA} = \text{DS} \times 16 + \text{Offset} = 1234H \times 10H + 5678H$$
$$= 12340H + 5678H = 179B8H$$

**Verification**: PA = 179B8H is a valid 20-bit address within the 8086's 1MB address space (00000H to FFFFFH). ✓

---

### Example 2: BHE# and A0 Bank Selection [KTU Part B pattern]

**Problem**: For the following 8086 bus operations, determine which bank (even/odd) is accessed and the value of BHE# and A0:
(a) Read byte at address 2000H  
(b) Read byte at address 2001H  
(c) Read word at address 2000H  
(d) Read word at address 2001H

**Solution**:

The 8086 has two 8-bit memory banks:
- **Even Bank**: A0 = 0, provides data on D0–D7
- **Odd Bank**: BHE# = 0, provides data on D8–D15

| Operation | Address | A0 | BHE# | Banks Accessed | Comments |
|---|---|---|---|---|---|
| (a) Read byte | 2000H (even) | 0 | 1 | Even only | Single-cycle, 8-bit |
| (b) Read byte | 2001H (odd) | 1 | 0 | Odd only | Single-cycle, 8-bit |
| (c) Read word | 2000H (even) | 0 | 0 | Both banks | Single-cycle, 16-bit (aligned) |
| (d) Read word | 2001H (odd) | 1 | 0 | Odd + Even(next) | **Two bus cycles** required (misaligned) — odd byte first, then even byte of next word |

---

### Example 3: Queue Efficiency Calculation [KTU Part B analytical]

**Problem**: The 8086 BIU prefetch queue holds 6 bytes. The EU takes 4 T-states (clock cycles) to execute an average instruction that is 2 bytes long. The bus cycle (instruction fetch) takes 4 T-states. Calculate:
(a) The throughput improvement from pipelining.
(b) The queue flush penalty when a branch instruction is taken (assume 6 bytes must be refilled).

**Solution**:

(a) **Non-pipelined throughput**: Each instruction requires 4T (fetch) + 4T (execute) = 8T. Rate = 1 instruction / 8T.

**Pipelined throughput**: While EU executes in 4T, BIU fetches 2 bytes of next instruction. After warmup, rate approaches 1 instruction / 4T (limited by EU execution).

**Improvement factor** ≈ 8T / 4T = **2×** throughput.

(b) **Branch penalty**: After a branch, the 6-byte queue must be invalidated and refilled from the branch target. At 2 bytes per bus cycle (4T each):
$$\text{Refill time} = \frac{6 \text{ bytes}}{2 \text{ bytes/cycle}} \times 4T = 12T \text{ wasted cycles}$$

This is why **branch prediction** in modern CPUs is so critical — a 20-stage pipeline that mispredicts a branch wastes 20 cycles.

---

## 5. Previous Year Questions & Solutions

---

### Q1 [KTU May 2019 / Dec 2018 / June 2022 — 9 marks (Part B)]
**Question**: Draw the internal architecture of the 8086 microprocessor and explain its functional units.

**Solution**:

The 8086 microprocessor is internally organized into two cooperating units:

**A. Bus Interface Unit (BIU)**

The BIU is the interface between the 8086 CPU and the external system bus. Its components and functions:

1. **Four Segment Registers (CS, DS, SS, ES)**: Each holds the 16-bit base address of a 64KB memory segment. The BIU uses whichever segment register is appropriate for the current operation (e.g., CS for instruction fetch, DS for data read, SS for stack operations).

2. **Instruction Pointer (IP)**: A 16-bit register that always points to the **offset address** of the next instruction within the current code segment (CS). The BIU uses CS:IP to generate the physical address for instruction pre-fetching. The EU never directly manipulates IP — the BIU updates it automatically as bytes are fetched.

3. **6-Byte Instruction Pre-fetch Queue**: A FIFO buffer that holds the next 6 bytes of code fetched from memory. The BIU continuously tries to keep this queue full — whenever it has 2 empty bytes and the external bus is idle, it initiates a fetch. The EU reads instructions from the head of this queue, decoupling execution from the memory fetch rate.

4. **Physical Address Adder**: A 20-bit adder that computes: `PA = (Segment Register << 4) + Offset`. The result is driven onto the 20-pin address bus.

5. **Bus Control Logic**: Generates ALE, RD#, WR#, DT/R#, DEN# and monitors READY, HOLD inputs.

**B. Execution Unit (EU)**

The EU decodes and executes all instructions. Its components:

1. **General-Purpose Registers (AX, BX, CX, DX)**: Each 16-bit register is split into independently addressable 8-bit halves (AH:AL, BH:BL, CH:CL, DH:DL). Special usages:
   - AX: Accumulator (all arithmetic, I/O, multiply/divide)
   - BX: Base (memory offset address computation)
   - CX: Counter (REP prefix loop count, LOOP instruction)
   - DX: Data (MUL/DIV extension word, I/O port address for IN/OUT dx,al)

2. **Pointer & Index Registers (SP, BP, SI, DI)**: 16-bit only (not byte-accessible).

3. **Flags Register**: 16-bit with 9 active flags: CF, PF, AF, ZF, SF, TF, IF, DF, OF.

4. **ALU (16-bit)**: Performs all arithmetic (ADD, SUB, MUL, DIV) and logical (AND, OR, XOR, NOT) operations on 8-bit or 16-bit operands.

**Pipelined Operation:**
The BIU and EU operate concurrently — while the EU executes instruction N, the BIU fetches bytes of instruction N+1 and N+2 into the queue. This pipeline doubles the effective throughput for sequential code (no branches). On a branch, the queue is flushed and the BIU refills it from the branch target address.

**[Architecture Block Diagram: See Section 1 above]**

---

### Q2 [KTU June 2022 / May 2019 / Dec 2018 — 9 marks (Part B)]
**Question**: Explain the minimum and maximum modes of operation of the 8086. What is the role of the 8288 Bus Controller?

**Solution**:

The 8086 has a single pin **MN/MX#** (Minimum/Maximum mode select) that determines the entire bus control configuration:

**Minimum Mode (MN/MX# = VCC = logic 1)**:
- The 8086 itself generates **all bus control signals** directly on its output pins.
- Control signals directly available: ALE, DEN#, DT/R#, M/IO#, WR#, INTA#.
- Bus arbitration: simple HOLD/HLDA handshake for DMA operations.
- Suitable for **single-processor systems** with one master on the bus.
- Simple design, requires fewer support chips.
- Example: A single 8086 CPU with 8255 I/O, SRAM, and EPROM — no other bus masters.

**Maximum Mode (MN/MX# = GND = logic 0)**:
- Pins 24–31 that produced control signals in min mode are **repurposed** as status outputs (S0#, S1#, S2#), queue status (QS0, QS1), and request/grant signals (RQ#/GT0#, RQ#/GT1#).
- The **8288 Bus Controller chip** receives S0#, S1#, S2# and generates the actual bus control signals: MRDC#, MWTC#, AMWC#, IORC#, IOWC#, AIOWC#, INTA#, ALE, DEN#, DT/R#.
- Bus arbitration: RQ#/GT0# and RQ#/GT1# (bidirectional, priority-based) allow multiple bus masters to arbitrate.
- QS0, QS1 (queue status): allows the 8087 Numeric Data Processor (Math Coprocessor) to monitor the 8086's instruction queue and know exactly which opcode is being executed (necessary for the ESC instruction handoff to the 8087).
- Suitable for **multi-processor systems**: 8086 + 8087 FPU, or 8086 + 8089 I/O Processor.

**8086 Status Lines (S0#, S1#, S2#) decoded by 8288:**

| S2# | S1# | S0# | Bus Cycle Type |
|---|---|---|---|
| 0 | 0 | 0 | INTA (Interrupt Acknowledge) |
| 0 | 0 | 1 | I/O Read |
| 0 | 1 | 0 | I/O Write |
| 0 | 1 | 1 | Halt |
| 1 | 0 | 0 | Instruction Fetch |
| 1 | 0 | 1 | Memory Read |
| 1 | 1 | 0 | Memory Write |
| 1 | 1 | 1 | Passive (no bus cycle) |

---

### Q3 [KTU Dec 2018 / May 2019 / June 2022 — 3 marks (Part A)]
**Question**: What is the significance of the ALE and BHE# signals in the 8086?

**Solution**:

**ALE (Address Latch Enable)**:
- The 8086 uses a **multiplexed address/data bus**: pins AD0–AD15 carry the address during T1 (the first clock state of a bus cycle) and data during T2–T4.
- ALE is pulsed HIGH only during T1 to signal that the address is currently valid on the multiplexed pins.
- An external **latch (74LS373 or 74ALS373)** captures and holds the address when ALE goes LOW, making the address available throughout the entire bus cycle even after the data phase begins.
- Without ALE, the address would be lost as soon as T2 begins (when the bus switches to data).

**BHE# (Bus High Enable)**:
- The 8086 has a 16-bit data bus split into an **even bank (D0–D7)** and an **odd bank (D8–D15)**.
- BHE# (active LOW) selects the **odd memory bank** (high byte), while A0 (active LOW) selects the **even memory bank** (low byte).
- Byte access to even address: BHE#=1, A0=0 (only D0–D7 valid).
- Byte access to odd address: BHE#=0, A0=1 (only D8–D15 valid).
- Word access at even address: BHE#=0, A0=0 (both banks selected simultaneously — single bus cycle).
- Word access at odd address: BHE#=0, A0=1 first cycle, then BHE#=1, A0=0 second cycle (misaligned — two bus cycles needed).

---

### Q4 [KTU All Papers — 3 marks (Part A)]
**Question**: What is the significance of CS:IP pair in the 8086? How is the first instruction fetched after RESET?

**Solution**:

The **CS:IP pair** specifies the absolute memory address of the next instruction to be fetched:
- **CS (Code Segment)**: Points to the base of the current code segment (64KB region).
- **IP (Instruction Pointer)**: Contains the offset within CS of the next byte to be fetched.
- Physical Address of next instruction = CS × 16 + IP.

The EU **never directly modifies IP** — the BIU automatically increments IP as bytes are removed from the prefetch queue.

**After RESET**:
- 8086 RESET forces: CS = **FFFFH**, IP = **0000H**, DS = 0000H, SS = 0000H, ES = 0000H, Flags = 0000H.
- Physical reset address: PA = FFFFH × 10H + 0000H = **FFFF0H**.
- This address is in the **ROM BIOS** region (the last 16 bytes of the 1MB address space).
- The first instruction at FFFF0H is typically a FAR JMP to the actual BIOS initialization code (e.g., JMP F000:E000H).

This hardware reset mechanism ensures the CPU always starts executing from a known, predictable location — the same principle applies to every modern x86 CPU.

---

### Q5 [KTU June 2022 / Dec 2018 — Part A, 3 marks]
**Question**: Briefly explain the 8086 flags and their significance.

**Solution**:

The 8086 Flags Register is 16 bits wide with 9 active flags grouped as **Status Flags** (set by ALU results) and **Control Flags** (set by software for mode control):

**Status Flags** (set automatically by arithmetic/logic operations):
- **CF (Carry Flag)**: Set when an addition produces a carry out of bit 15, or subtraction produces a borrow. Used in multi-byte arithmetic (ADC, SBB, RCL, RCR).
- **ZF (Zero Flag)**: Set when the result of an operation is zero. Used in conditional jumps (JZ/JE, JNZ/JNE).
- **SF (Sign Flag)**: Set when result bit 15 is 1 (interpreted as negative in signed arithmetic). Used in JNS, JS jumps.
- **OF (Overflow Flag)**: Set when signed arithmetic produces a result outside the representable range. Detects signed overflow (e.g., adding two large positive numbers gives a negative result).
- **PF (Parity Flag)**: Set when the number of 1-bits in the low byte of the result is even. Used in serial communication for error detection (historical).
- **AF (Auxiliary Carry Flag)**: Carry from bit 3 to bit 4. Used by DAA, DAS instructions for BCD (packed decimal) arithmetic.

**Control Flags** (set/cleared by explicit software instructions):
- **IF (Interrupt Flag)**: When set (STI instruction), the 8086 acknowledges maskable interrupts on the INTR pin. When cleared (CLI instruction), maskable interrupts are ignored. NMI always works regardless of IF.
- **DF (Direction Flag)**: Controls string operation direction. CLD clears DF → SI and DI auto-increment (forward). STD sets DF → SI and DI auto-decrement (backward).
- **TF (Trap Flag)**: When set, the 8086 enters **single-step mode** — it generates a Type 1 interrupt after every instruction. Used by debuggers (DEBUG.COM, software breakpoints).

