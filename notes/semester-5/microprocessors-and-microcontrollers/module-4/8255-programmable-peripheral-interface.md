# 8255 Programmable Peripheral Interface (PPI)

> **Senior CS Professor Notes** | Semester 5 — CS305 Microprocessors & Microcontrollers | Module IV

---

## 1. Explanation

### Role & Purpose of the 8255 PPI
The **Intel 8255A Programmable Peripheral Interface (PPI)** is a general-purpose, programmable I/O device designed to interface parallel peripheral hardware (printers, keyboards, ADC/DAC modules, stepper motors, LED displays, sensors) to the Intel microprocessor bus.

Without an interface chip like the 8255, connecting discrete peripheral devices directly to the high-speed multiplexed bus of the 8086 CPU would require dozens of external latches, tri-state buffers, address decoders, and handshake flip-flops. The 8255 integrates **24 programmable I/O pins** into a single 40-pin IC, organized into three 8-bit ports (Port A, Port B, and Port C). It allows engineers to dynamically reconfigure port directions and handshake protocols purely through software control words.

---

### Internal Architecture of the 8255A

The internal architecture consists of two programmable groups (**Group A** and **Group B**) coordinated by the system bus control logic:

```
                          8255A Internal Architecture
  +-------------------------------------------------------------------------+
  |                                                                         |
  |  +----------------+     Internal Data Bus (8-bit)     +--------------+  |
  |  | Data Bus Buffer|<=================================>| Port A (8)   |==|==> PA0 - PA7
  |  | (D0 - D7)      |          |               |        | Latch/Buffer |  |
  |  +----------------+          |               |        +--------------+  |
  |                              |               |                          |
  |  +----------------+          |               |        +--------------+  |
  |  | Read / Write   |          |               +=======>| Port B (8)   |==|==> PB0 - PB7
  |  | Control Logic  |          |               |        | Latch/Buffer |  |
  |  |                |          |               |        +--------------+  |
  |  | RD#            |          |               |                          |
  |  | WR#            |          |               |        +--------------+  |
  |  | CS#            |          v               +=======>| Port C UPPER |==|==> PC7 - PC4
  |  | A1             |   +-------------+        |        | (4-bit Latch)|  |
  |  | A0             |   | Group A     |        |        +--------------+  |
  |  | RESET          |   | Control     |        |                          |
  |  +----------------+   +-------------+        |        +--------------+  |
  |                              ^               +=======>| Port C LOWER |==|==> PC3 - PC0
  |                              |                        | (4-bit Latch)|  |
  |                       +-------------+                 +--------------+  |
  |                       | Group B     |                                   |
  |                       | Control     |                                   |
  |                       +-------------+                                   |
  +-------------------------------------------------------------------------+
```

#### Detailed Functional Blocks:

1. **Port A**:
   - One 8-bit data output latch/buffer and one 8-bit data input latch.
   - Can operate in **Mode 0 (Basic I/O)**, **Mode 1 (Strobed Handshake I/O)**, and **Mode 2 (Bidirectional Bus)**.
2. **Port B**:
   - One 8-bit data input/output latch/buffer.
   - Can operate in **Mode 0** and **Mode 1**. (Does NOT support Mode 2).
3. **Port C**:
   - One 8-bit data output latch/buffer and one 8-bit data input buffer (inputs are not latched in Mode 0).
   - Can be split into two independent 4-bit nibbles:
     - **Port C Upper ($\text{PC}_7 - \text{PC}_4$)**: Associated with Group A control.
     - **Port C Lower ($\text{PC}_3 - \text{PC}_0$)**: Associated with Group B control.
   - In Modes 1 and 2, Port C pins provide hardware handshake control signals ($\overline{\text{STB}}, \text{IBF}, \overline{\text{OBF}}, \overline{\text{ACK}}, \text{INTR}$) for Port A and Port B.
   - Every individual bit of Port C can be set or reset using the **BSR (Bit Set/Reset)** mode.
4. **Group A and Group B Controls**:
   - **Group A Control**: Controls Port A and Port C Upper ($\text{PC}_7 - \text{PC}_4$).
   - **Group B Control**: Controls Port B and Port C Lower ($\text{PC}_3 - \text{PC}_0$).
5. **Read/Write Control Logic**:
   - Decodes bus commands and directs data between internal registers and the CPU data bus:
     - $\overline{\text{CS}}$ (Chip Select): Enables communication when LOW.
     - $\overline{\text{RD}}$: CPU reads data or status from 8255.
     - $\overline{\text{WR}}$: CPU writes data or control words to 8255.
     - $A_1, A_0$: Port select address lines.
     - $\text{RESET}$: High level clears control register and sets all 24 I/O pins into high-impedance **Input Mode** (safety default to prevent external circuit damage).

#### Port Selection Truth Table:
| $\overline{\text{CS}}$ | $A_1$ | $A_0$ | $\overline{\text{RD}}$ | $\overline{\text{WR}}$ | Operation Selected |
|---|---|---|---|---|---|
| `0` | `0` | `0` | `0` | `1` | **Read Port A** ($\text{CPU} \leftarrow \text{Port A}$) |
| `0` | `0` | `1` | `0` | `1` | **Read Port B** ($\text{CPU} \leftarrow \text{Port B}$) |
| `0` | `1` | `0` | `0` | `1` | **Read Port C** ($\text{CPU} \leftarrow \text{Port C}$) |
| `0` | `0` | `0` | `1` | `0` | **Write Port A** ($\text{CPU} \rightarrow \text{Port A}$) |
| `0` | `0` | `1` | `1` | `0` | **Write Port B** ($\text{CPU} \rightarrow \text{Port B}$) |
| `0` | `1` | `0` | `1` | `0` | **Write Port C** ($\text{CPU} \rightarrow \text{Port C}$) |
| `0` | `1` | `1` | `1` | `0` | **Write Control Register** ($\text{Mode Set}$ or $\text{BSR}$) |
| `0` | `1` | `1` | `0` | `1` | Illegal (Control register cannot be read; data bus tri-stated) |
| `1` | $\times$ | $\times$ | $\times$ | $\times$ | 8255 Deselected (Bus in High-Z) |

---

### Operating Modes of the 8255

The 8255 provides three primary operating modes:

#### 1. Mode 0: Basic Input/Output
- Provides simple unidirectional input or output without hardware handshake lines.
- Outputs are latched. Inputs are unlatched (buffered only).
- There are 16 possible I/O configurations because Port A, Port B, Port C Upper, and Port C Lower can each be independently programmed as an Input or Output port.
- Ideal for interfacing simple devices like DIP switches, 7-segment displays, relays, and steady LED arrays.

#### 2. Mode 1: Strobed Handshake Input/Output
- Transfers data between the CPU and peripheral using hardware handshake control signals generated on Port C pins.
- **Inputs and outputs are both latched**.
- Port A and Port B function as 8-bit data ports; Port C provides handshaking.

##### (A) Mode 1 Strobed Input (e.g., Reading from an ADC or Keyboard):
- $\overline{\text{STB}}$ (**Strobe Input**, active low): Asserted by peripheral when data has been placed on the port pins.
- **IBF** (**Input Buffer Full**, active high): Asserted by 8255 to acknowledge receipt of data into the input latch; warns the peripheral not to send more data until CPU reads current byte.
- **INTR** (**Interrupt Request**, active high): Asserted by 8255 to interrupt the CPU when data is ready in the buffer. Requires interrupt enable flip-flop ($\text{INTE}$) to be set via BSR.
- Handshake Sequence:
  $$\text{Peripheral outputs data} \to \text{Pulses } \overline{\text{STB}} \to \text{IBF goes HIGH} \to \text{INTR goes HIGH} \to \text{CPU reads port} \to \text{IBF and INTR reset}$$

##### (B) Mode 1 Strobed Output (e.g., Writing to a Printer or DAC):
- $\overline{\text{OBF}}$ (**Output Buffer Full**, active low): Asserted by 8255 when CPU writes data to the output port, notifying peripheral that data is waiting.
- $\overline{\text{ACK}}$ (**Acknowledge Input**, active low): Pulled low by the peripheral after it has ingested the data byte.
- **INTR** (**Interrupt Request**, active high): Asserted when the peripheral acknowledges receipt ($\overline{\text{ACK}}$ goes high), signaling the CPU that the buffer is empty and ready for the next byte.

##### Port C Pin Assignment in Mode 1:
| Signal Role | Port A (Group A) | Port B (Group B) |
|---|---|---|
| **Mode 1 Input** | $\text{PC}_4 = \overline{\text{STB}}_A$, $\text{PC}_5 = \text{IBF}_A$, $\text{PC}_3 = \text{INTR}_A$ | $\text{PC}_2 = \overline{\text{STB}}_B$, $\text{PC}_1 = \text{IBF}_B$, $\text{PC}_0 = \text{INTR}_B$ |
| | Unused pins ($\text{PC}_6, \text{PC}_7$) available for I/O. | (All 3 Port C Lower pins consumed). |
| **Mode 1 Output** | $\text{PC}_7 = \overline{\text{OBF}}_A$, $\text{PC}_6 = \overline{\text{ACK}}_A$, $\text{PC}_3 = \text{INTR}_A$ | $\text{PC}_1 = \overline{\text{OBF}}_B$, $\text{PC}_2 = \overline{\text{ACK}}_B$, $\text{PC}_0 = \text{INTR}_B$ |
| | Unused pins ($\text{PC}_4, \text{PC}_5$) available for I/O. | (All 3 Port C Lower pins consumed). |

#### 3. Mode 2: Strobed Bidirectional Bus I/O
- Supported **only on Port A**.
- Transforms Port A ($\text{PA}_7 - \text{PA}_0$) into an 8-bit bidirectional data bus capable of both input and output with full handshaking.
- Consumes 5 pins of Port C:
  - $\text{PC}_7 = \overline{\text{OBF}}_A$ (Output Buffer Full)
  - $\text{PC}_6 = \overline{\text{ACK}}_A$ (Acknowledge)
  - $\text{PC}_5 = \text{IBF}_A$ (Input Buffer Full)
  - $\text{PC}_4 = \overline{\text{STB}}_A$ (Strobe Input)
  - $\text{PC}_3 = \text{INTR}_A$ (Interrupt Request)
- Remaining pins ($\text{PC}_2, \text{PC}_1, \text{PC}_0$) can be used as simple I/O or as handshake pins for Port B in Mode 1.
- Widely used for inter-processor communication and interfacing disk controllers.

---

### Control Word Formats

The 8255 has a single write-only Control Register at address $A_1 A_0 = 11$. It accepts two distinct formats differentiated by bit $D_7$:

#### 1. Mode Definition Control Word ($D_7 = 1$)

```
  D7   D6   D5   D4   D3   D2   D1   D0
+----+----+----+----+----+----+----+----+
| 1  |  Group A   |PA  |PC_U|Mode|PB  |PC_L|
|    |  Mode Sel  |Dir |Dir |PB  |Dir |Dir |
+----+----+----+----+----+----+----+----+
```

- **$D_7 = 1$**: Identifies byte as **Mode Definition Word**.
- **Group A Configuration**:
  - **$D_6, D_5$ (Port A Mode Selection)**:
    - `00` = Mode 0 (Basic I/O)
    - `01` = Mode 1 (Strobed I/O)
    - `1X` = Mode 2 (Bidirectional Bus, $X = 0 \text{ or } 1$)
  - **$D_4$ (Port A Direction)**:
    - $1 = \text{Input}$; $0 = \text{Output}$
  - **$D_3$ (Port C Upper Direction $\text{PC}_7 - \text{PC}_4$)**:
    - $1 = \text{Input}$; $0 = \text{Output}$
- **Group B Configuration**:
  - **$D_2$ (Port B Mode Selection)**:
    - $0 = \text{Mode 0}$; $1 = \text{Mode 1}$
  - **$D_1$ (Port B Direction)**:
    - $1 = \text{Input}$; $0 = \text{Output}$
  - **$D_0$ (Port C Lower Direction $\text{PC}_3 - \text{PC}_0$)**:
    - $1 = \text{Input}$; $0 = \text{Output}$

#### 2. Bit Set/Reset (BSR) Control Word ($D_7 = 0$)

Used exclusively to set or reset **individual bits of Port C** without disturbing other Port C pins:

```
  D7   D6   D5   D4   D3   D2   D1   D0
+----+----+----+----+----+----+----+----+
| 0  | X  | X  | X  |   Bit Select |S/R |
+----+----+----+----+----+----+----+----+
```

- **$D_7 = 0$**: Identifies byte as **BSR Word**.
- **$D_6, D_5, D_4 = \times$**: Don't care (set to `000`).
- **$D_3, D_2, D_1$ (Bit Select $B_2 B_1 B_0$)**: Binary number ($000_2$ to $111_2$) specifying which Port C bit ($\text{PC}_0$ to $\text{PC}_7$) to modify.
- **$D_0$ (Set / Reset)**:
  - $1 = \text{SET}$ (drive selected bit to logic `1`).
  - $0 = \text{RESET}$ (drive selected bit to logic `0`).

---

## 2. Example: System Interconnection Diagram

```
                 8086 Interfaced to 8255A PPI
   +-------------------+                     +-------------------+
   |     8086 CPU      |                     |      8255A        |
   |                   |                     |                   |
   | D7 - D0 --------->|====================>| D7 - D0           |
   |                   |                     |                   |
   | A1 -------------->|-------------------->| A0                |
   | A2 -------------->|-------------------->| A1                |
   |                   |                     |                   |
   | RD# ------------->|-------------------->| RD#               |
   | WR# ------------->|-------------------->| WR#               |
   | RESET ----------->|-------------------->| RESET             |
   +-------------------+                     |                   |
                                             | CS#               |
   +-------------------+                     +---^---------------+
   | 74LS138 Decoder   |                         |
   | Y0# --------------|-------------------------+
   | (Decodes I/O port |
   |  addresses 80H-83H|
   +-------------------+
```
*Note on Address Pin Alignment*: Because the 8086 data bus is 16 bits wide, when connecting an 8-bit peripheral to the lower data bus ($D_7 - D_0$), CPU address line $A_1$ connects to 8255 $A_0$, and CPU line $A_2$ connects to 8255 $A_1$. This assigns consecutive even port addresses (e.g., `80H, 82H, 84H, 86H`).

---

## 3. Applications & Real-World Use Cases

1. **Centronics Parallel Printer Interface**:
   - The original IBM PC printer port implemented a Centronics interface using the 8255 in **Mode 1 Output**: 8 data bits sent over Port A, $\overline{\text{STB}}$ pulsed on $\text{PC}_7$, printer asserts $\overline{\text{ACK}}$ on $\text{PC}_6$, triggering an interrupt to send the next character.
2. **Industrial Stepper Motor Control**:
   - Four phase coils ($A, B, C, D$) of an industrial 2-phase bipolar stepper motor are wired to Port A ($\text{PA}_3 - \text{PA}_0$) through ULN2803 Darlington driver transistors. Precise microstepping sequences are output via Port A in Mode 0.
3. **Matrix Keypad Scanning**:
   - 4 row output lines driven via Port C Lower and 4 column sense lines read via Port C Upper in Mode 0 with pull-up resistors.

---

## 4. Solved Numerical & Analytical Examples

### Example 1: Calculating 8255 Control Words for Diverse Configurations
**Problem**: Determine the exact 8-bit Control Word in hexadecimal for each of the following configurations:
1. **Config A**: Port A as Mode 0 input, Port B as Mode 0 output, Port C Upper as output, Port C Lower as input.
2. **Config B**: Port A as Mode 1 strobed input, Port B as Mode 1 strobed output, Port C Upper bits $\text{PC}_7, \text{PC}_6$ as inputs.
3. **Config C**: Port A as Mode 2 bidirectional bus, Port B as Mode 0 output, Port C Lower as output.
4. **Config D**: Set bit $\text{PC}_5$ using BSR mode; then reset bit $\text{PC}_3$ using BSR mode.

#### Solution:

**1. Config A**:
- Mode Set bit $D_7 = 1$.
- Port A Mode 0 $\implies D_6 D_5 = 00_2$.
- Port A Input $\implies D_4 = 1$.
- Port C Upper Output $\implies D_3 = 0$.
- Port B Mode 0 $\implies D_2 = 0$.
- Port B Output $\implies D_1 = 0$.
- Port C Lower Input $\implies D_0 = 1$.
- Binary: `1001 0001B` = **`91H`**.

**2. Config B**:
- $D_7 = 1$ (Mode Set).
- Group A Mode 1 $\implies D_6 D_5 = 01_2$.
- Port A Input $\implies D_4 = 1$.
- Port C Upper ($\text{PC}_7, \text{PC}_6$) Input $\implies D_3 = 1$.
- Group B Mode 1 $\implies D_2 = 1$.
- Port B Output $\implies D_1 = 0$.
- In Mode 1 Output for Port B, Port C Lower pins are consumed by handshaking; $D_0$ is don't care, conventionally set to `0`.
- Binary: `1011 1100B` = **`BCH`**.

**3. Config C**:
- $D_7 = 1$ (Mode Set).
- Group A Mode 2 $\implies D_6 D_5 = 1X_2$ (set $D_6 = 1, D_5 = 0$).
- Port A direction $D_4$ is don't care in Mode 2 (bidirectional), set to `1`.
- Port C Upper pins are consumed by Mode 2 handshake, $D_3$ set to `0`.
- Port B Mode 0 $\implies D_2 = 0$.
- Port B Output $\implies D_1 = 0$.
- Port C Lower Output $\implies D_0 = 0$.
- Binary: `1101 0000B` = **`D0H`**.

**4. Config D (BSR Commands)**:
- To SET $\text{PC}_5$:
  - $D_7 = 0$ (BSR indicator).
  - $D_6 D_5 D_4 = 000_2$.
  - Bit number 5 $\implies D_3 D_2 D_1 = 101_2$.
  - SET $\implies D_0 = 1$.
  - Binary: `0000 1011B` = **`0BH`**.
- To RESET $\text{PC}_3$:
  - $D_7 = 0$.
  - $D_6 D_5 D_4 = 000_2$.
  - Bit number 3 $\implies D_3 D_2 D_1 = 011_2$.
  - RESET $\implies D_0 = 0$.
  - Binary: `0000 0110B` = **`06H`**.

---

### Example 2: Interfacing DIP Switches and LEDs with 8086 via 8255
**Problem**: An 8255 is interfaced to an 8086 with base address `0060H` (I/O-mapped).
- Port A address is `60H`.
- Port B address is `62H`.
- Port C address is `64H`.
- Control Register address is `66H`.
- **Hardware Connection**: An 8-bit DIP switch bank is connected to Port A (inputs, pulled high via $10\text{ k}\Omega$ resistor network, switch closure grounds the pin). An 8-LED active-high bar display is connected to Port B (outputs via $330\Omega$ current limiting resistors).
- Write an 8086 assembly language program that continuously reads the switch pattern from Port A and displays it immediately on the LEDs of Port B. If switch 7 ($\text{PA}_7$) is pressed (logic 0), invert all bits before displaying them on Port B.

#### Solution:

**Step 1: Control Word Calculation**
- Port A = Mode 0 Input $\implies D_6 D_5 = 00, D_4 = 1$.
- Port B = Mode 0 Output $\implies D_2 = 0, D_1 = 0$.
- Port C Upper = Output $\implies D_3 = 0$.
- Port C Lower = Output $\implies D_0 = 0$.
- Control Word: `1001 0000B` = **`90H`**.

**Step 2: Assembly Program**
```assembly
; 8255 Port Definitions
PORT_A      EQU 60H
PORT_B      EQU 62H
PORT_C      EQU 64H
CTRL_REG    EQU 66H

CODE SEGMENT
    ASSUME CS:CODE
    ORG 1000H

START:
    ; 1. Initialize 8255 Control Register
    MOV AL, 90H           ; Load Control Word (PA: In, PB: Out, Mode 0)
    OUT CTRL_REG, AL      ; Configure 8255

POLL_LOOP:
    ; 2. Read DIP Switch bank from Port A
    IN  AL, PORT_A        ; Read 8-bit switch input into AL

    ; 3. Test MSB (Bit 7)
    TEST AL, 80H          ; Check bit 7 (Switch 7)
    JNZ DISPLAY_DIRECT    ; If Bit 7 = 1 (switch open/unpressed), branch

    ; If Switch 7 is closed (Bit 7 = 0), invert all bits
    NOT AL

DISPLAY_DIRECT:
    ; 4. Output pattern to LED bar at Port B
    OUT PORT_B, AL        ; Write AL to LEDs

    ; 5. Loop infinitely
    JMP POLL_LOOP

CODE ENDS
END START
```

---

### Example 3: Stepper Motor Interfacing and Step Sequence Generation
**Problem**: A 2-phase permanent magnet stepper motor with 4 stator windings ($A, B, C, D$) is interfaced to Port A pins $\text{PA}_3, \text{PA}_2, \text{PA}_1, \text{PA}_0$ of an 8255 at port address `80H`.
- Control Register is at port `86H`.
- The motor requires a 4-step sequence to rotate clockwise:
  - Step 1: `09H` (`1001B` — Coils A and D energized)
  - Step 2: `0CH` (`1100B` — Coils A and B energized)
  - Step 3: `06H` (`0110B` — Coils B and C energized)
  - Step 4: `03H` (`0011B` — Coils C and D energized)
- Write an 8086 assembly procedure that rotates the motor clockwise for 100 complete revolutions. The motor has a step angle of $1.8^\circ$ (200 steps per revolution). Insert an appropriate software delay between steps.

#### Solution:

**Step 1: Calculations**
- Step angle $\theta = 1.8^\circ$.
- Steps per revolution = $\frac{360^\circ}{1.8^\circ} = 200 \text{ steps}$.
- Total steps for 100 revolutions = $100 \times 200 = \mathbf{20,000 \text{ steps}}$.
- Port A configured as Mode 0 Output $\implies$ Control Word = `80H` (All ports Mode 0 output).

**Step 2: Assembly Language Program**
```assembly
PORT_A   EQU 80H
CTRL_REG EQU 86H

DATA SEGMENT
    ; Step sequence table for 2-phase excitation
    STEP_SEQ DB 09H, 0CH, 06H, 03H
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
START:
    MOV AX, DATA
    MOV DS, AX

    ; Initialize 8255: All ports Mode 0 Output
    MOV AL, 80H
    OUT CTRL_REG, AL

    ; Total steps to execute = 20,000 steps
    MOV CX, 20000         ; CX acts as outer step counter

STEP_LOOP:
    LEA SI, STEP_SEQ      ; Pointer to step sequence table
    MOV BX, 4             ; 4 steps per excitation cycle

CYCLE_4STEP:
    MOV AL, [SI]          ; Fetch excitation pattern
    OUT PORT_A, AL        ; Output to stepper motor coils
    CALL DELAY            ; Wait for motor rotor to settle

    INC SI                ; Point to next step pattern
    DEC CX                ; Decrement total remaining steps
    JZ  FINISHED          ; If all 20,000 steps complete, exit

    DEC BX                ; Decrement cycle counter
    JNZ CYCLE_4STEP       ; Repeat for all 4 patterns
    JMP STEP_LOOP         ; Reload table pointer and repeat

FINISHED:
    MOV AL, 00H
    OUT PORT_A, AL        ; De-energize coils to prevent overheating
    HLT

; Software Delay Subroutine (~10 ms delay at 5 MHz clock)
DELAY PROC
    PUSH DX
    MOV DX, 2500
D1: DEC DX
    JNZ D1
    POP DX
    RET
DELAY ENDP

CODE ENDS
END START
```

---

## 5. Previous Year Questions & Solutions

### Question 1 (KTU B.Tech Examination)
**Explain the different operating modes of 8255 PPI with neat diagrams. What is the significance of the BSR mode?** [9 Marks]

#### Complete Self-Contained Solution:
1. **Operating Modes Overview**:
   The Intel 8255A Programmable Peripheral Interface operates in two fundamental operational regimes: **I/O Mode** ($D_7 = 1$) and **Bit Set/Reset (BSR) Mode** ($D_7 = 0$). I/O mode is subdivided into three distinct configurations:
   - **Mode 0 (Basic I/O)**:
     - Unidirectional, simple I/O for Ports A, B, and C.
     - No handshake signals are utilized.
     - Outputs are latched, while inputs are unlatched (buffered).
     - Provides 16 independent input/output permutations across Port A, Port B, Port C Upper, and Port C Lower.
   - **Mode 1 (Strobed / Handshake I/O)**:
     - Data transfers are coordinated using hardware handshaking lines on Port C pins.
     - Both input and output data are fully latched.
     - For strobed input: $\overline{\text{STB}}$ (Strobe) from peripheral latches data into 8255; 8255 asserts $\text{IBF}$ (Input Buffer Full) to inhibit further data until CPU reads; asserts $\text{INTR}$ to interrupt CPU.
     - For strobed output: CPU writes to port, 8255 asserts $\overline{\text{OBF}}$ (Output Buffer Full); peripheral consumes data and pulses $\overline{\text{ACK}}$ (Acknowledge); 8255 raises $\text{INTR}$ to request the next byte.
   - **Mode 2 (Strobed Bidirectional Bus I/O)**:
     - Implemented **exclusively on Port A**.
     - Provides a full 8-bit bidirectional data highway with handshaking using 5 pins of Port C: $\overline{\text{STB}}_A, \text{IBF}_A, \overline{\text{OBF}}_A, \overline{\text{ACK}}_A, \text{INTR}_A$.
     - Used for high-speed inter-processor bus communication.

2. **Significance of BSR (Bit Set/Reset) Mode**:
   - In real-time industrial control, engineers frequently need to pulse or toggle an individual control line (e.g., triggering a relay, pulsing a clock line on a serial ADC, or resetting a peripheral) without corrupting or modifying the states of the other 7 pins on that port.
   - Using standard I/O writes requires a read-modify-write software sequence (`IN AL, PORT_C` $\to$ `OR/AND` $\to$ `OUT PORT_C, AL`), which is non-atomic and susceptible to race conditions if interrupts occur.
   - **BSR mode allows the CPU to set or reset ANY individual bit of Port C with a single write to the Control Register ($A_1 A_0 = 11$)** by setting $D_7 = 0$, selecting the bit with $D_3 D_2 D_1$, and specifying the value with $D_0$. It executes atomically in hardware in a single bus cycle.

---

### Question 2 (KTU B.Tech Examination)
**Draw the internal block diagram of 8255 PPI and explain the control word format for Mode Set and BSR mode.** [9 Marks]

#### Complete Self-Contained Solution:
1. **Architecture Block Diagram**:
   *(Draw the functional block diagram illustrating Data Bus Buffer, Read/Write Control Logic, Group A Control, Group B Control, Port A, Port B, Port C Upper, and Port C Lower from Section 1).*
2. **Mode Set Control Word Format ($D_7 = 1$)**:
   *(Draw the 8-bit register layout showing $D_7=1$, $D_6 D_5$ for Mode A, $D_4$ for Port A direction, $D_3$ for Port C Upper direction, $D_2$ for Mode B, $D_1$ for Port B direction, and $D_0$ for Port C Lower direction as detailed in Section 1).*
3. **BSR Control Word Format ($D_7 = 0$)**:
   *(Draw the 8-bit layout showing $D_7=0$, $D_6 - D_4 = 000$, $D_3 D_2 D_1$ for 3-bit bit selection from $\text{PC}_0$ to $\text{PC}_7$, and $D_0 = 1$ for Set and $0$ for Reset).*

