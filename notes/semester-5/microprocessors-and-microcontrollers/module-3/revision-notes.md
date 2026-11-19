# Module III: Interrupts & 8259 PIC — Revision Notes

> **Quick Revision Guide for Internal & University Exams** | CS305 Semester 5

---

## 1. High-Yield Core Concepts & Formulae

### 1. 8086 Interrupt Vector Table (IVT) Architecture
- **Location**: Starts at physical address `00000H` and spans 1 KB up to `003FFH` ($256 \text{ vectors} \times 4 \text{ bytes/vector} = 1024 \text{ bytes}$).
- **Entry Structure**:
  - Bytes 0 & 1: 16-bit Instruction Pointer (`IP_L`, `IP_H`).
  - Bytes 2 & 3: 16-bit Code Segment (`CS_L`, `CS_H`).
- **Address Formula for Interrupt Type $N$**:
  $$\text{Starting Physical Address} = N \times 4$$
  $$\text{Memory Span} = [4N, 4N + 3]$$

### 2. Dedicated Hardware & Software Interrupts (Types 0 to 4)
- **Type 0 (Divide Error)**: Triggered automatically by hardware when `DIV` or `IDIV` produces a quotient exceeding destination register capacity or divisor is zero.
- **Type 1 (Single Step / Trap)**: Invoked after every instruction when Trap Flag ($\text{TF}=1$) for debugging.
- **Type 2 (NMI)**: Non-maskable, positive edge-triggered pin on 8086; used for emergency power loss or parity errors.
- **Type 3 (Breakpoint)**: 1-byte opcode `0CCH` (`INT 3`) for software breakpoints.
- **Type 4 (Overflow)**: Executed by `INTO` instruction if Overflow Flag ($\text{OF}=1$).

### 3. Hardware Interrupt Acknowledgment Protocol
- 8086 finishes current instruction $\to$ asserts **Pulse 1** on $\overline{\text{INTA}}$ (freezes IRR, sets ISR) $\to$ asserts **Pulse 2** on $\overline{\text{INTA}}$ (8259 places 8-bit vector type $N$ on $D_0 - D_7$) $\to$ CPU reads $N$, pushes FLAGS, clears `IF` and `TF`, pushes `CS`, pushes `IP`, and vectors to $4N$.
- **IRET**: Restores `IP`, `CS`, and `FLAGS` from the stack in reverse order.

### 4. 8259 Internal Registers
- **IRR (Interrupt Request Register)**: Latches unserviced incoming requests ($\text{IR}_0 - \text{IR}_7$).
- **ISR (In-Service Register)**: Stores interrupt level currently being executed.
- **IMR (Interrupt Mask Register)**: 8-bit mask programmed via OCW1 ($1 = \text{masked/disabled}$, $0 = \text{enabled}$).
- **Priority Resolver**: Evaluates $(\text{IRR} \land \neg\text{IMR})$ against ISR to assert `INT`.

### 5. 8259 Command Words Summary
- **ICW1 ($A_0 = 0, D_4 = 1$)**: Sets Edge/Level trigger ($D_3$), Single/Cascade ($D_1$), ICW4 needed ($D_0=1$ for 8086).
- **ICW2 ($A_0 = 1$)**: Sets upper 5 bits ($T_7 - T_3$) of base vector type.
- **ICW3 ($A_0 = 1$, Cascaded only)**: Master uses 8-bit bitmap of slave pins ($S_7 - S_0$); Slave uses 3-bit ID ($000_2 - 111_2$).
- **ICW4 ($A_0 = 1$)**: $\mu\text{PM}=1$ (8086 mode), AEOI bit, Master/Slave buffered bit, Special Fully Nested Mode (SFNM).
- **OCW1 ($A_0 = 1$)**: Reads/writes Interrupt Mask Register.
- **OCW2 ($A_0 = 0, D_4 D_3 = 00$)**: EOI commands (Non-specific = `20H`, Specific = `60H` + Level), Priority Rotation.
- **OCW3 ($A_0 = 0, D_4 D_3 = 01$)**: Read IRR (`0AH`) or Read ISR (`0BH`), Special Mask Mode.

---

## 2. Frequently Asked Exam Questions & Diagram Pitfalls

1. **8086 Interrupt Processing Sequence**: Always draw the stack growth showing:
   $$\text{SP} \leftarrow \text{SP}-2; \quad [\text{SP}] \leftarrow \text{FLAGS}$$
   $$\text{SP} \leftarrow \text{SP}-2; \quad [\text{SP}] \leftarrow \text{CS}$$
   $$\text{SP} \leftarrow \text{SP}-2; \quad [\text{SP}] \leftarrow \text{IP}$$
   *Common Mistake*: Forgetting that `IF` and `TF` are cleared automatically before jumping to the ISR to prevent re-entrant interrupts and debugger loops.

2. **8259 Block Diagram**: Include all 8 blocks: Data Bus Buffer, R/W Control Logic, Cascade Buffer/Comparator, Control Logic, IRR, Priority Resolver, ISR, and IMR. Clearly label lines $\text{IR}_0 - \text{IR}_7$, `INT`, $\overline{\text{INTA}}$, and $\text{CAS}_0 - \text{CAS}_2$.

3. **Cascading Diagram**: Show the Master's $\text{CAS}_0 - \text{CAS}_2$ lines connected to Slaves, Slave `INT` connected to Master $\text{IR}_k$, and the shared $\overline{\text{INTA}}$ signal from the CPU.

---

## 3. Comparison Cheat Sheets

### Hardware vs Software Interrupts

| Feature | Hardware Interrupts | Software Interrupts |
|---|---|---|
| **Initiation** | External pin excitation (NMI, INTR) | CPU executing `INT n` or `INTO` |
| **Maskability** | INTR is maskable (`CLI`); NMI is non-maskable | Non-maskable (cannot be masked by IF) |
| **Handshake** | Requires two $\overline{\text{INTA}}$ bus cycles | No $\overline{\text{INTA}}$ bus cycles; type $n$ is part of opcode |
| **Deterministic Timing** | Asynchronous to program execution | Synchronous to instruction stream |
| **Priority** | Lower than software interrupts | Higher priority than hardware interrupts |

---

## 4. 10-Minute Rapid Revision Checklist

- [ ] Can you calculate the IVT physical address for Type $32\text{H}$? ($32\text{H} \times 4 = 000C8\text{H}$ to $000CB\text{H}$).
- [ ] Do you remember why `ICW4` is mandatory in an 8086 system? (To set $D_0 = 1$ for 8086 8-bit vector mode instead of 8085 3-byte `CALL`).
- [ ] What is the difference between Non-Specific EOI (`20H`) and Specific EOI (`60H` + level)?
- [ ] Why is Special Fully Nested Mode (SFNM) used in a Master 8259? (To allow higher-priority interrupts on the same Slave to interrupt a lower routine from that Slave).
- [ ] What is the function of the `IRET` instruction? (Pops IP, CS, and FLAGS to return to interrupted code).

