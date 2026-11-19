# 8086 Interrupts and Interrupt Handling

## 1. Explanation

An **interrupt** is an asynchronous or synchronous event that temporarily suspends the CPU's current execution thread, preserves its operational state, and diverts program flow to a specialized subprogram called an **Interrupt Service Routine (ISR)** or **Interrupt Handler**. Upon completing the service routine, the processor restores its saved state and seamlessly resumes the interrupted task.

Interrupts are essential for:
- Servicing time-critical peripheral I/O (keyboard strokes, network packet arrivals, timer ticks)
- Handling hardware runtime faults (power failure, memory parity errors, divide-by-zero exceptions)
- Supporting operating system software services (system calls via `INT 21H`)

---

### Classification of 8086 Interrupts

The 8086 supports **256 distinct interrupt types** (numbered Type 0 to Type 255), classified into three categories:

```
                              8086 INTERRUPTS (256 Types)
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
HARDWARE INTERRUPTS               SOFTWARE INTERRUPTS               INTERNAL EXCEPTIONS
(Initiated via external pins)     (Initiated via INT n opcode)      (Initiated by CPU execution faults)
 • NMI (Non-Maskable, Type 2)      • INT 0 to INT 255                • Type 0: Divide by Zero
 • INTR (Maskable, via IF flag)    • INT 21H (DOS API)               • Type 1: Single-Step (TF=1)
                                   • INT 10H (BIOS Video)            • Type 3: Breakpoint (1-byte CC)
                                   • INT 16H (BIOS Keyboard)         • Type 4: Overflow (INTO)
```

#### 1. Hardware Interrupts
Initiated by physical electrical signals asserted on the processor's input pins:
- **NMI (Non-Maskable Interrupt, Pin 17)**:
  - Rising-edge triggered; internally hardwired as **Type 2**.
  - **Cannot be disabled or masked** by software (ignores the Interrupt Flag `IF`).
  - Reserved for catastrophic hardware crises: impending power failure, memory parity errors, bus watchdog timeouts.
- **INTR (Interrupt Request, Pin 18)**:
  - Level-triggered; maskable by software via the Interrupt Enable Flag (`IF` in the Flags register).
  - If `IF = 0` (cleared via `CLI`), signals on INTR are ignored.
  - If `IF = 1` (set via `STI`), the processor acknowledges the interrupt by generating two successive active-low $\overline{\text{INTA}}$ (Interrupt Acknowledge) pulses. During the second $\overline{\text{INTA}}$ pulse, external interrupt logic (such as the 8259 PIC) places the 8-bit interrupt type number ($N \in [0, 255]$) onto the lower data bus ($\text{AD}_0\text{–}\text{AD}_7$).

#### 2. Software Interrupts
Triggered programmatically using the two-byte instruction `INT n` (where $n \in [0, 255]$).
- Unaffected by the state of `IF` (executes even if `IF = 0`).
- Used to invoke operating system functions and BIOS service routines.

#### 3. Dedicated Pre-Defined Internal Interrupts (Exceptions)
Intel reserves Types $0\text{–}4$ for internal processor events:
- **Type 0: Divide Error**: Triggered automatically when a `DIV` or `IDIV` instruction produces a quotient that overflows the destination register (or when dividing by zero).
- **Type 1: Single-Step (Trace) Interrupt**: Generated after every single instruction if the Trap Flag `TF = 1`. Used by interactive debuggers to execute instructions step-by-step.
- **Type 2: Non-Maskable Interrupt (NMI)**: Triggered by the external NMI pin.
- **Type 3: Breakpoint Interrupt**: A single-byte instruction (opcode `CCH`). Debuggers overwrite target instruction bytes with `0CCH` to pause program execution at breakpoints.
- **Type 4: Overflow (`INTO`)**: Triggered if the Overflow Flag `OF = 1` when the `INTO` (Interrupt on Overflow) instruction executes.

---

### The Interrupt Vector Table (IVT)

The 8086 maintains an **Interrupt Vector Table (IVT)** occupying the absolute lowest $1\text{ KB}$ of physical memory ($00000\text{H}$ to $003\text{FF}\text{H}$):
- Accommodates all **256 interrupt types**.
- Each interrupt vector consists of **4 bytes**:
  - Bytes 0–1: 16-bit Instruction Pointer offset (`IP`) of the ISR.
  - Bytes 2–3: 16-bit Code Segment base address (`CS`) of the ISR.
  $$\text{Table Size} = 256 \text{ vectors} \times 4 \text{ bytes/vector} = 1024 \text{ bytes} = 1 \text{ KB}$$

```
Memory Address                                 Content
003FFH ┌──────────────────────────────────────────────┐
       │ Type 255 Segment (CS) (2 bytes)              │
       ├──────────────────────────────────────────────┤
       │ Type 255 Offset  (IP) (2 bytes)              │
       ├──────────────────────────────────────────────┤
       │                      ...                     │
00010H ├──────────────────────────────────────────────┤
       │ Type 4 (INTO) ISR Address (IP, CS)           │
0000CH ├──────────────────────────────────────────────┤
       │ Type 3 (Breakpoint) ISR Address (IP, CS)     │
00008H ├──────────────────────────────────────────────┤
       │ Type 2 (NMI) ISR Address (IP, CS)            │
00004H ├──────────────────────────────────────────────┤
       │ Type 1 (Single-step) ISR Address (IP, CS)    │
00000H ├──────────────────────────────────────────────┤
       │ Type 0 (Divide Error) ISR Address (IP, CS)   │
       └──────────────────────────────────────────────┘
```

#### Vector Address Calculation Formula
For any interrupt of Type $N$:
$$\text{Starting Physical Address of Vector} = N \times 4$$
- Low word at $(N \times 4)$ is loaded into `IP`.
- High word at $(N \times 4 + 2)$ is loaded into `CS`.

*Example*: For Interrupt Type $08\text{H}$ (PC Timer Tick):
$$\text{Vector Address} = 8 \times 4 = 32 = 00020\text{H}$$
- `IP` fetched from $00020\text{H}$ and $00021\text{H}$.
- `CS` fetched from $00022\text{H}$ and $00023\text{H}$.

---

### Hardware Interrupt Handling Sequence

When an interrupt request (INTR or NMI) or instruction (`INT n`) occurs:

```
        Event (INTR / NMI / INT n)
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  Complete Current Instruction Execution      │
└───────────────────┬──────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  Push Flags Register onto Stack (SP ← SP - 2)│
└───────────────────┬──────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  Clear IF and TF (Disable further interrupts)│
└───────────────────┬──────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  Push CS Register onto Stack (SP ← SP - 2)   │
└───────────────────┬──────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  Push IP Register onto Stack (SP ← SP - 2)   │
└───────────────────┬──────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  Fetch Type N: Read IP from [N*4], CS from   │
│  [N*4 + 2]; Branch to ISR                    │
└───────────────────┬──────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  Execute ISR Code; Conclude with IRET        │
└───────────────────┬──────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│  IRET: Pop IP, Pop CS, Pop Flags             │
│  Resume Interrupted Program Execution        │
└──────────────────────────────────────────────┘
```

**Step-by-Step Response**:
1. The CPU finishes executing the currently executing instruction.
2. For INTR, the CPU issues two $\overline{\text{INTA}}$ pulses and reads the interrupt type number $N$ from $\text{D}_0\text{–}\text{D}_7$.
3. The **Flags register** is pushed onto the stack: `SP ← SP - 2`.
4. The **Interrupt Flag (`IF`)** and **Trap Flag (`TF`)** are cleared to $0$, preventing re-entrant maskable interrupts during vector fetch.
5. The return code segment **`CS`** is pushed onto the stack: `SP ← SP - 2`.
6. The return offset **`IP`** is pushed onto the stack: `SP ← SP - 2`.
7. The CPU multiplies $N$ by 4, loads the low word into `IP`, loads the high word into `CS`, and begins executing the ISR.
8. The ISR terminates with the **`IRET` (Interrupt Return)** instruction, which automatically pops `IP`, pops `CS`, and pops the `Flags` register in reverse order, restoring the previous task state.

---

### Interrupt Priorities in 8086

When multiple interrupt requests occur simultaneously, the 8086 resolves them in the following rigid priority order:

| Priority Rank | Interrupt Source |
|---|---|
| **Highest (1)** | Internal Exceptions / Software Interrupts (`DIV`, `INTO`, `INT n`) |
| **2** | Non-Maskable Interrupt (`NMI`) |
| **3** | Maskable Hardware Interrupt (`INTR`) |
| **Lowest (4)** | Single-Step Trap (`TF`) |

---

## 2. Example: Writing and Installing a Custom Interrupt Service Routine

```asm
DATA SEGMENT
    OLD_IP  DW  ?
    OLD_CS  DW  ?
    MSG     DB  "Custom Type 60H ISR Executed!", 0DH, 0AH, '$'
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
START:
    MOV AX, DATA
    MOV DS, AX
    
    ; 1. Save Old Vector for Type 60H (60H * 4 = 180H = 0180H)
    MOV AX, 0000H
    MOV ES, AX          ; ES points to IVT segment at 0000H
    
    MOV AX, ES:[0180H]  ; Save old IP
    MOV OLD_IP, AX
    MOV AX, ES:[0182H]  ; Save old CS
    MOV OLD_CS, AX
    
    ; 2. Install New Vector (CLI to prevent interrupts during write)
    CLI
    MOV WORD PTR ES:[0180H], OFFSET MY_ISR
    MOV WORD PTR ES:[0182H], CS
    STI
    
    ; 3. Trigger Software Interrupt Type 60H
    INT 60H
    
    ; 4. Restore Original Vector Before Exit
    CLI
    MOV AX, OLD_IP
    MOV ES:[0180H], AX
    MOV AX, OLD_CS
    MOV ES:[0182H], AX
    STI
    
    MOV AH, 4CH
    INT 21H

; Custom ISR Routine
MY_ISR PROC FAR
    PUSH AX             ; Preserve registers used in ISR
    PUSH DX
    PUSH DS
    
    MOV AX, DATA
    MOV DS, AX
    LEA DX, MSG
    MOV AH, 09H         ; DOS string display
    INT 21H
    
    POP DS
    POP DX
    POP AX
    IRET                ; Return from interrupt (Pops IP, CS, Flags)
MY_ISR ENDP

CODE ENDS
END START
```

---

## 3. Applications & Use Cases

1. **PC Real-Time System Clock (IRQ0 / INT 08H)**:
   An 8254 timer chip delivers a square wave at $18.2\text{ Hz}$ to the 8259 PIC's IRQ0 line, triggering INT 08H. The BIOS ISR increments a 32-bit tick counter in RAM ($0040:006C\text{H}$) used by the OS for task scheduling and sleep delays.
2. **Industrial Emergency Stop (NMI)**:
   Safety interlock switches and earthquake sensors are tied directly to the NMI pin, guaranteeing immediate power-down and motor brake activation regardless of CPU state.
3. **Debugger Breakpoints (INT 3)**:
   Debuggers (GDB, Visual Studio) insert opcode `0CCH` (`INT 3`) at the target breakpoint address, allowing the debugger to gain control and inspect registers when hit.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Physical Address of Vector Table Entries [KTU Part A — 3 Marks]
**Problem**:
Calculate the physical memory address range in the IVT occupied by the vector pointers for:
(a) Type 3 (Breakpoint)
(b) Type 21H (DOS Function Call)

**Solution**:
Vector table formula: $\text{Base Address} = N \times 4$.
Each entry occupies 4 consecutive bytes: $[N \times 4 \text{ to } N \times 4 + 3]$.

- **Part (a): Type 3**:
  $$\text{Base Address} = 3 \times 4 = 12 = 0000\text{CH}$$
  Address range: **$0000\text{CH}$ to $0000\text{FH}$** (Low byte IP at 0000CH, High byte IP at 0000DH, Low byte CS at 0000EH, High byte CS at 0000FH).

- **Part (b): Type 21H**:
  Convert hex to decimal: $21\text{H} = (2 \times 16) + 1 = 33$.
  $$\text{Base Address} = 33 \times 4 = 132 = 00084\text{H}$$
  Address range: **$00084\text{H}$ to $00087\text{H}$**.

---

### Example 2: Stack Content Analysis During Interrupt Entry [Analytical]
**Problem**:
Before servicing an `INT 40H` instruction, the 8086 registers have values:
$\text{CS} = 2000\text{H}, \text{IP} = 1500\text{H}, \text{SP} = 0100\text{H}, \text{Flags} = 0246\text{H}$.
What are the contents of the stack and the value of `SP` immediately after the interrupt sequence completes and before the first instruction of the ISR executes?

**Solution**:
During interrupt processing, the 8086 pushes Flags, CS, and IP:
1. `Flags` ($0246\text{H}$) pushed: `SP` becomes $0100\text{H} - 2 = 00\text{FE}\text{H}$.
   - Memory at $[00\text{FE}\text{H}] = 46\text{H}$, $[00\text{FF}\text{H}] = 02\text{H}$.
2. `CS` ($2000\text{H}$) pushed: `SP` becomes $00\text{FE}\text{H} - 2 = 00\text{FC}\text{H}$.
   - Memory at $[00\text{FC}\text{H}] = 00\text{H}$, $[00\text{FD}\text{H}] = 20\text{H}$.
3. `IP` of next instruction ($1502\text{H}$ — since `INT 40H` is 2 bytes long) pushed: `SP` becomes $00\text{FC}\text{H} - 2 = 00\text{FA}\text{H}$.
   - Memory at $[00\text{FA}\text{H}] = 02\text{H}$, $[00\text{FB}\text{H}] = 15\text{H}$.

**Final Stack Pointer**: `SP = 00FAH`.
**Bytes Consumed on Stack**: $6\text{ bytes}$.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [KTU All Papers — 9 Marks]
**Question**:
Explain the interrupt structure of the 8086 microprocessor. Describe the organization of the Interrupt Vector Table. How does the 8086 handle external hardware interrupts?

**Solution**:

#### Part (a): Interrupt Structure & Classification
The 8086 supports 256 interrupts partitioned into Hardware Interrupts (`NMI`, `INTR`), Software Interrupts (`INT n`), and Internal Processor Exceptions (`Type 0` Divide error, `Type 1` Single-step, `Type 3` Breakpoint, `Type 4` Overflow).

#### Part (b): Interrupt Vector Table (IVT)
The IVT occupies physical memory addresses $00000\text{H}$ to $003\text{FF}\text{H}$ ($1\text{ KB}$). Each of the 256 interrupt types has a 4-byte entry:
- First two bytes: 16-bit offset address (`IP`) of the ISR.
- Next two bytes: 16-bit segment address (`CS`) of the ISR.
- Vector starting address for Type $N$: $\text{Address} = N \times 4$.

#### Part (c): Hardware Interrupt Handling Sequence
1. Peripheral device asserts `INTR` high.
2. If `IF = 1`, the CPU completes current instruction and outputs two active-low $\overline{\text{INTA}}$ pulses.
3. During the second $\overline{\text{INTA}}$, the peripheral puts the 8-bit interrupt type number $N$ on data lines $\text{D}_0\text{–}\text{D}_7$.
4. The CPU pushes the Flags register onto the stack, then clears `IF = 0` and `TF = 0` to prevent nested interrupts.
5. The CPU pushes `CS`, then pushes `IP` onto the stack.
6. The CPU reads `IP` from memory location $N \times 4$ and `CS` from $N \times 4 + 2$, branching to the ISR.
7. The ISR concludes with `IRET`, which pops `IP`, `CS`, and Flags, returning to the pre-interrupt state.

---

### Question 2 [KTU May 2019 / Dec 2018 — 3 Marks]
**Question**:
What is the difference between `RET` and `IRET` instructions?

**Solution**:

| Feature | `RET` (Return from Procedure) | `IRET` (Interrupt Return) |
|---|---|---|
| **Used In** | Regular subroutines / procedures (`PROC`). | Interrupt Service Routines (`ISR`). |
| **Stack Operations** | Pops return `IP` (for NEAR call) or pops return `IP` and `CS` (for FAR call). | Pops return `IP`, pops return `CS`, AND pops the saved `Flags` register. |
| **Bytes Restored** | 2 bytes (Near) or 4 bytes (Far). | **6 bytes** (`IP`, `CS`, `Flags`). |
| **Flags Restoration** | Flags register is **not restored**; flags set inside procedure remain modified. | Restores original pre-interrupt flag states (including original `IF` and `TF` bits). |

