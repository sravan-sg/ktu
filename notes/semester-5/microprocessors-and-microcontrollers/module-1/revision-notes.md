# Module 1: 8086 Microprocessor Architecture — Revision Notes

## 1. Core Architecture: BIU vs. EU
- **Bus Interface Unit (BIU)**: Handles all external memory and I/O communication. Contains:
  - 4 Segment Registers ($16\text{-bit}$): `CS` (Code), `DS` (Data), `SS` (Stack), `ES` (Extra).
  - Instruction Pointer (`IP`): Points to next instruction byte in `CS`.
  - 6-Byte Pre-fetch Queue: Decouples fetch from execution (1st-generation x86 pipeline).
  - 20-bit Dedicated Address Adder: Calculates physical address:
    $$\text{Physical Address (PA)} = (\text{Segment Register} \times 16) + \text{Offset}$$
- **Execution Unit (EU)**: Decodes and executes instructions. Contains:
  - 16-bit ALU.
  - General Purpose Registers ($16\text{-bit}$ / byte-addressable): `AX` (AH:AL), `BX` (BH:BL), `CX` (CH:CL), `DX` (DH:DL).
  - Pointer & Index Registers: `SP` (Stack Pointer, SS), `BP` (Base Pointer, SS), `SI` (Source Index, DS), `DI` (Destination Index, ES).
  - Flags Register ($16\text{-bit}$, 9 active flags):
    - Status Flags: `CF` (Carry), `PF` (Parity), `AF` (Auxiliary Carry), `ZF` (Zero), `SF` (Sign), `OF` (Overflow).
    - Control Flags: `TF` (Trap / Single-step), `IF` (Interrupt Enable), `DF` (Direction).

---

## 2. Memory Organization & Bank Selection
- **1 MB Memory Space** ($00000\text{H}$ to $\text{FFFFF}\text{H}$) split into two $512\text{ KB}$ interleaved memory banks:
  - **Even Bank (Lower Bank)**: Contains bytes at even addresses ($0, 2, 4, \dots$). Activated when $\text{A}_0 = 0$. Connected to lower data bus ($\text{D}_0\text{–}\text{D}_7$).
  - **Odd Bank (Higher Bank)**: Contains bytes at odd addresses ($1, 3, 5, \dots$). Activated when $\overline{\text{BHE}} = 0$. Connected to upper data bus ($\text{D}_8\text{–}\text{D}_{15}$).
- **Bank Selection Truth Table**:
  | $\overline{\text{BHE}}$ | $\text{A}_0$ | Bus Operation | Number of Bus Cycles |
  |---|---|---|---|
  | 0 | 0 | Whole 16-bit word at even address | 1 cycle |
  | 1 | 0 | 8-bit byte from even bank ($\text{D}_0\text{–}\text{D}_7$) | 1 cycle |
  | 0 | 1 | 8-bit byte from odd bank ($\text{D}_8\text{–}\text{D}_{15}$) | 1 cycle |
  | 0 | 1 (then 1, 0) | 16-bit word at odd address (misaligned) | 2 cycles |

---

## 3. Minimum Mode vs. Maximum Mode
- Selected by pin $33$ ($\text{MN}/\overline{\text{MX}}$):
  - $\text{MN}/\overline{\text{MX}} = \text{V}_{\text{CC}}$ (High) $\implies$ **Minimum Mode** (Single processor). 8086 directly outputs control strobes: $\text{ALE}, \overline{\text{RD}}, \overline{\text{WR}}, \text{M}/\overline{\text{IO}}, \text{DT}/\overline{\text{R}}, \overline{\text{DEN}}, \overline{\text{INTA}}$.
  - $\text{MN}/\overline{\text{MX}} = \text{GND}$ (Low) $\implies$ **Maximum Mode** (Multiprocessor / Coprocessor with 8087/8089). Pin functions change to status lines $\overline{\text{S}}_0, \overline{\text{S}}_1, \overline{\text{S}}_2$, queue status $\text{QS}_0, \text{QS}_1$, and bus request/grant $\overline{\text{RQ}}/\overline{\text{GT}}_0, \overline{\text{RQ}}/\overline{\text{GT}}_1$. External **8288 Bus Controller** decodes $\overline{\text{S}}_0\text{–}\overline{\text{S}}_2$ to produce bus control signals.

---

## 4. Minimum Mode Timing & 8086 vs. 8088
- **Bus Cycle**: Composed of 4 T-states ($T_1, T_2, T_3, T_4$) plus optional wait states ($T_w$).
  - $T_1$: Address output on $\text{AD}_0\text{–}\text{AD}_{15}$; $\text{ALE}$ pulses high to latch address into 74LS373.
  - $T_2$: $\text{AD}$ bus floats (read) or drives data (write); $\overline{\text{RD}}$ or $\overline{\text{WR}}$ asserted.
  - $T_3$: $\text{READY}$ line sampled; if low, inserts $T_w$ clock cycles.
  - $T_4$: Data transferred/latched; control signals deactivated.
- **8086 vs. 8088 Comparison**:
  - 8086: 16-bit external data bus ($\text{AD}_0\text{–}\text{AD}_{15}$), 6-byte queue, has $\overline{\text{BHE}}$ pin.
  - 8088: 8-bit external data bus ($\text{AD}_0\text{–}\text{AD}_7$), 4-byte queue, pin $\text{M}/\overline{\text{IO}}$ inverted to $\text{IO}/\overline{\text{M}}$, no $\overline{\text{BHE}}$ (replaced by $\text{SSO}$).

