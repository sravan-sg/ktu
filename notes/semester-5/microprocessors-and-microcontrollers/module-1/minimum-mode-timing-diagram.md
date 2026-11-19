# Minimum Mode Timing Diagram — 8086 Read and Write Cycles

## 1. Explanation

### Why Timing Diagrams?
A timing diagram is the **electrical contract** between the microprocessor and external memory/peripherals. It precisely specifies which signals go high/low at which clock transition, and for how long — information essential for:
- **Memory interface design**: Does the SRAM's access time fit within the data valid window?
- **Peripheral interface**: Does the I/O device's response meet setup and hold requirements?
- **Wait state calculation**: How many Tw cycles are needed to accommodate slow memory?

The 8086 uses a **synchronous bus** — all signals are referenced to the system clock (CLK).

---

### Clock States (T-States)

A basic 8086 bus cycle consists of **4 clock states** (T1, T2, T3, T4):

| State | Duration | Function |
|---|---|---|
| **T1** | 1 CLK period | Address phase: BIU drives address on AD0–AD15, A16–A19. ALE goes HIGH then LOW to latch address. BHE# becomes valid. |
| **T2** | 1 CLK period | Data phase begins: Address/data bus transitions from address to data. M/IO# and DT/R# set. For READ: RD# goes LOW (memory asserts data). For WRITE: WR# goes LOW, 8086 drives data. |
| **T3** | 1 CLK period | Wait for READY: Processor samples READY at the beginning of T3. If READY=HIGH, proceeds to T4. If READY=LOW, inserts Tw (wait states) until READY goes HIGH. |
| **Tw** | 1+ CLK periods | Wait states inserted when READY=LOW (slow memory). Can be any number of Tw cycles. |
| **T4** | 1 CLK period | Completion: RD# or WR# de-asserted. Data is sampled (read) or bus released (write). ALE for next cycle begins. |

---

### Minimum Mode Read Cycle Timing Diagram

```
         T1      T2      T3      T4
         │       │       │       │
CLK  ─┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
      └──┘     └──┘     └──┘     └──┘     └──

ALE  ───┐  ┌─────────────────────────────────
        └──┘ ← Pulses high for first half of T1
             External 74LS373 latches address here

AD0–AD15
(addr)   ════╗ ADDR ╔════════════════════════  ← Address valid during T1
(data)       ╚══════╝ DATA from memory ══════  ← Data driven by memory in T2–T4

A16–A19  ════════ ADDR ══════════════════════  ← High address bits during T1 (status S3-S6 during T2-T4)

M/IO#    ────────────────────────────────────  HIGH (Memory access)

DT/R#    ─────────────────────────────────    LOW (Receive mode — 8086 reads data)

DEN#     ─────┐ LOW ┌─────────────────────    Enables data bus transceivers

RD#      ─────────────────────┐  ┌──────────  LOW = Memory is being read
                              └──┘

READY    ════════════════════ HIGH ═══════    HIGH = no wait states inserted
```

**Data Valid Window**: Memory must place valid data on AD0–AD15 before the **rising edge of CLK at the start of T4** (the sampling point). This is the critical timing constraint for memory selection.

---

### Minimum Mode Write Cycle Timing Diagram

```
         T1      T2      T3      T4
         │       │       │       │
CLK  ─┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
      └──┘     └──┘     └──┘     └──┘     └──

ALE  ───┐  ┌─────────────────────────────────
        └──┘

AD0–AD15
(addr)   ════╗ ADDR ╔════════════════════════
(data)       ╚══════╝ ═════ DATA from 8086 ═  ← 8086 drives write data T2–T4

M/IO#    ────────────────────────────────────  HIGH

DT/R#    ────────────────────────────────────  HIGH (Transmit mode — 8086 writes data)

DEN#     ─────┐ LOW ┌─────────────────────

WR#      ─────────────────────┐  ┌──────────  LOW = Memory write strobe
                              └──┘

READY    ════════════════════ HIGH ═══════
```

---

### Wait State (Tw) Insertion

If memory is too slow, the READY pin is pulled LOW by an **8284 Clock Generator** (via its READY logic) or the memory's WAIT logic:

```
         T1      T2      T3      Tw      T4
CLK  ─┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
      └──┘     └──┘     └──┘     └──┘     └──┘     └──

READY                            LOW     HIGH         ← Sampled at start of T3
                                 ↑SLOW MEMORY INSERTS Tw

RD#   ─────────────────────────────────────┐  ┌──────
```

**Wait state calculation**:
- CPU clock = 8 MHz → T-state = 1/8 MHz = 125 ns
- Memory access time = 300 ns
- Available time (without wait states): T2 + T3 ≈ 2 × 125 = 250 ns → memory is too slow!
- With 1 wait state: T2 + T3 + Tw = 3 × 125 = 375 ns > 300 ns → memory fits ✓

---

## 2. Example: Complete Bus Cycle Analysis

### Scenario
8086 at 10 MHz. DS = 3000H. Instruction `MOV AX, [5000H]` executes.

**Step-by-step bus cycle:**

1. **EU sends effective address (5000H) to BIU**
2. **BIU computes PA**: 3000H × 10H + 5000H = 35000H
3. **T1**: AD0–AD15 = 5000H (lower 16 bits), A16–A19 = 3H (upper 4 bits). ALE pulses. BHE# = 0, A0 = 0 (word access, even address).
4. **T2**: AD0–AD15 transitions to data. RD# asserts LOW. M/IO# = HIGH.
5. **T3**: READY sampled. If HIGH, proceed. Memory drives 16-bit data onto D0–D15.
6. **T4**: RD# de-asserts. BIU captures data at sampling point. Data loaded into AX register by EU.

---

## 3. Applications & Use Cases

### 1. Memory Interface Engineering
When interfacing 8086 with EPROM (27C128, 150 ns access time) or SRAM (6264, 100 ns access time), the timing diagram tells the designer exactly how many wait states are needed. The READY line can be driven by a simple RC delay circuit or a programmable wait state generator.

### 2. Logic Analyzer Debugging
When debugging embedded 8086 systems, a logic analyzer captures all address, data, and control signals in real time. The timing diagram is the reference against which the captured waveforms are validated. Violations (address not stable, RD# glitches) identify hardware problems.

### 3. FPGA Soft-Core Implementation
Engineers implementing an 8086 soft-core in FPGA (e.g., Xilinx FLEX 8086 clone) use the timing diagram as the precise behavioral specification. The FSM controlling bus cycles directly implements the T1–T4 state transitions.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Minimum Number of Wait States Calculation [KTU Part B analytical — 9 marks]

**Problem**: An 8086 system operates at 8 MHz. The memory read cycle uses a data valid window that is available from the beginning of T2 to the end of T3.
- Memory access time (from address valid to data valid) = 350 ns.
- Address valid occurs at the beginning of T2 (after ALE latches it).
Determine the minimum number of wait states required.

**Solution**:

Clock period at 8 MHz:
$$T_{CLK} = \frac{1}{8 \times 10^6} = 125 \text{ ns}$$

Address becomes valid when ALE goes LOW (end of T1 / start of T2):
$$t_{addr\_valid} = 1 \times T_{CLK} = 125 \text{ ns from bus cycle start}$$

Data must be valid before the CPU samples at the end of T3 (start of T4):
$$t_{sample} = 3 \times T_{CLK} = 375 \text{ ns from bus cycle start}$$

Time available for memory access:
$$t_{available} = t_{sample} - t_{addr\_valid} = 375 - 125 = 250 \text{ ns}$$

Since memory access time (350 ns) > available time (250 ns):
$$\text{Wait states needed} = \left\lceil \frac{350 - 250}{125} \right\rceil = \left\lceil \frac{100}{125} \right\rceil = \lceil 0.8 \rceil = 1 \text{ wait state}$$

With 1 wait state: available time = 250 + 125 = 375 ns > 350 ns ✓

**Answer: 1 wait state required.**

---

### Example 2: Physical Address from Timing Diagram [KTU Part A — 3 marks]

**Problem**: During a bus cycle, the signals at T1 are measured:
- A16=1, A17=0, A18=0, A19=0 (upper nibble = 0001H → upper 4 bits of 20-bit address)
- AD15–AD0 = 2345H

What is the full 20-bit physical address being accessed?

**Solution**:
$$\text{PA} = \{A19, A18, A17, A16\} \| \{AD15...AD0\} = 0001 \| 0010001101000101_2$$
$$\text{PA} = 12345H$$

---

### Example 3: Comparison of 8086 and 8088 [KTU Part A — 3 marks]

**Problem**: List the key differences between the 8086 and 8088 microprocessors.

**Solution**:

| Feature | 8086 | 8088 |
|---|---|---|
| **External Data Bus** | 16-bit (D0–D15) | 8-bit (D0–D7 only) |
| **Internal Data Bus** | 16-bit | 16-bit |
| **Pre-fetch Queue** | 6 bytes | 4 bytes |
| **Memory Banks** | 2 banks (even + odd) | Single 8-bit bank |
| **BHE# Signal** | Present (selects odd bank) | Not present |
| **Bus Cycles for 16-bit** | 1 bus cycle (aligned) | 2 bus cycles always |
| **Historical Use** | IBM PC AT, industrial systems | IBM PC XT (Intel 8088 cheaper) |
| **Cost** | Slightly higher | Lower (8-bit bus simpler) |

Both have the identical **internal architecture** (same ALU, same registers, same instruction set, same BIU/EU organization). Only the external data bus width differs.

---

## 5. Previous Year Questions & Solutions

---

### Q1 [KTU All papers — 9 marks (Part B)]
**Question**: Draw and explain the minimum mode read and write cycle timing diagrams of the 8086.

**Solution**:

The 8086 minimum mode bus cycle consists of 4 clock states (T1–T4). The timing diagrams are shown in Section 1 above. Here is the complete explanation:

**Read Cycle (Memory Read Operation):**

**T1 (Address Phase)**:
- 8086 drives the 20-bit address: lower 16 bits appear on AD0–AD15 (multiplexed), upper 4 bits on A16–A19.
- ALE (Address Latch Enable) goes HIGH briefly then LOW. The external 74LS373 latch captures the address when ALE goes LOW.
- BHE# and M/IO# become valid. M/IO# = HIGH for memory access.
- DT/R# = LOW (8286 transceiver set to receive mode — 8086 will read data).

**T2 (Cycle Initiation)**:
- AD0–AD15 transitions from address to Hi-Z (floating), releasing the bus for memory to drive data.
- RD# goes LOW — this is the memory read strobe. It signals memory: "put your data on the bus."
- DEN# goes LOW — enables the 8286 data bus transceiver.

**T3 (Wait/Sample)**:
- READY is sampled at the beginning of T3.
  - If READY = HIGH: proceed to T4.
  - If READY = LOW: insert wait states (Tw) until READY goes HIGH.
- Memory continues to drive data on the bus.

**T4 (Completion)**:
- RD# de-asserts (goes HIGH).
- 8086 samples the data on AD0–AD15 at the beginning of T4 and latches it into the destination register.
- DEN# de-asserts.
- ALE goes HIGH again for the next bus cycle.

**Write Cycle (Memory Write Operation):**

**T1**: Same as read — address phase, ALE pulse, latching.

**T2**: 8086 drives **write data** on AD0–AD15 (instead of going Hi-Z). DT/R# = HIGH (transceiver transmit mode). WR# goes LOW.

**T3**: READY sampled. Memory captures data while WR# is LOW.

**T4**: WR# de-asserts. Memory completes the write operation. Data bus released.

**Key difference: READ vs WRITE**:
- READ: AD0–AD15 goes Hi-Z in T2 so memory can drive data.
- WRITE: AD0–AD15 is driven by 8086 from T2 onward — memory samples this data.

---

### Q2 [KTU Dec 2018 / May 2019 — Part A, 3 marks]
**Question**: What are wait states? When are they inserted in a bus cycle?

**Solution**:

**Wait states (Tw)** are additional clock periods inserted into a bus cycle to extend the time available for slow memory or slow I/O peripherals to respond.

**When inserted**: The 8086 samples the READY input at the beginning of state T3. If a memory or I/O device cannot provide valid data within the standard T2+T3 window (before T4 sampling point), it drives READY LOW. This causes the 8086 to repeat T3 (insert a Tw = one additional CLK period) each cycle until READY goes HIGH. The number of wait states can be any non-negative integer.

**Practical example**: 
- 8086 at 8 MHz: standard data valid window ≈ 250 ns (from T2 to T4 sampling point).
- 150 ns SRAM: 0 wait states (fits in 250 ns).
- 450 ns EPROM: 2 wait states needed (250 + 2×125 = 500 ns available).

The 8284A Clock Generator chip includes READY synchronization logic to ensure the READY signal is synchronized to the CPU clock before being sampled.

