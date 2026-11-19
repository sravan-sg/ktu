# 8254 Programmable Interval Timer (PIT)

> **Senior CS Professor Notes** | Semester 5 — CS305 Microprocessors & Microcontrollers | Module VI

---

## 1. Explanation

### Role & Purpose of the 8254 PIT
In microprocessor and microcontroller-based systems, generating precise time delays via software loops (e.g., executing nested `NOP` or decrement loops) severely degrades system efficiency. Software timing loops tie up the CPU, consume $100\%$ processor bandwidth, and produce inaccurate delays whenever interrupts occur.

The **Intel 8254 Programmable Interval Timer (PIT)** (an upgraded, high-speed CMOS version of the earlier 8253) solves this problem by performing all timing, delay generation, event counting, and waveform synthesis entirely in dedicated hardware. Once initialized by the CPU with an operational mode and count value, the 8254 operates completely autonomously, freeing the CPU to execute application software.

---

### Internal Architecture of the 8254

The 8254 integrates **three independent 16-bit down-counters** into a single 24-pin dual in-line package (DIP):

```
                          8254 PIT Internal Architecture
  +-------------------------------------------------------------------------+
  |                                                                         |
  |  +----------------+     Internal Data Bus (8-bit)     +--------------+  |
  |  | Data Bus Buffer|<=================================>| Counter 0    |==|==> CLK0, GATE0, OUT0
  |  | (D0 - D7)      |          |               |        | (16-bit)     |  |
  |  +----------------+          |               |        +--------------+  |
  |                              |               |                          |
  |  +----------------+          |               |        +--------------+  |
  |  | Read / Write   |          |               +=======>| Counter 1    |==|==> CLK1, GATE1, OUT1
  |  | Control Logic  |          |               |        | (16-bit)     |  |
  |  |                |          |               |        +--------------+  |
  |  | RD#            |          |               |                          |
  |  | WR#            |          |               |        +--------------+  |
  |  | CS#            |          v               +=======>| Counter 2    |==|==> CLK2, GATE2, OUT2
  |  | A1             |   +-------------+                 | (16-bit)     |  |
  |  | A0             |   | Control Word|                 +--------------+  |
  |  +----------------+   | Register    |                                   |
  |                       +-------------+                                   |
  +-------------------------------------------------------------------------+
```

#### Detailed Functional Blocks:

1. **Three Identical 16-Bit Counters (Counter 0, Counter 1, Counter 2)**:
   - Each counter is a separate, fully independent **16-bit down-counter**.
   - Each counter can operate in binary ($0000\text{H} - \text{FFFF}\text{H}$) or BCD ($0000 - 9999$) counting format.
   - Maximum count value loaded into a counter is $2^{16} = 65,536$ in binary mode (programmed by loading `0000H`) or $10,000$ in BCD mode.
   - Maximum input clock frequency:
     - 8253: up to $2.6\text{ MHz}$.
     - 8254: up to **$8\text{ MHz}$**, with 8254-2 operating up to **$10\text{ MHz}$**.
   - Each counter has three external interface pins:
     - **`CLK` (Clock Input)**: Input square wave or event pulse driving the down-counter.
     - **`GATE` (Gate Control Input)**: Hardware control line that enables, disables, or triggers counting depending on the programmed mode.
     - **`OUT` (Counter Output)**: Emits pulses, square waves, or level changes upon count expiration.

2. **Control Word Register**:
   - Write-only register selected when address lines $A_1 A_0 = 11_2$.
   - Receives control words written by the CPU to set the operational mode, counting format, and read/write byte sequence for each counter.

3. **Read/Write Control Logic**:
   - Manages CPU access to internal counter registers and the control register.

#### Address Selection Truth Table:
| $\overline{\text{CS}}$ | $A_1$ | $A_0$ | Operation Selected |
|---|---|---|---|
| `0` | `0` | `0` | Counter 0 (Read / Write) |
| `0` | `0` | `1` | Counter 1 (Read / Write) |
| `0` | `1` | `0` | Counter 2 (Read / Write) |
| `0` | `1` | `1` | Control Word Register (Write only) |
| `1` | $\times$ | $\times$ | Chip Deselected (High-Z) |

---

### Control Word Format of the 8254

```
  D7   D6   D5   D4   D3   D2   D1   D0
+----+----+----+----+----+----+----+----+
| SC1| SC0| RW1| RW0| M2 | M1 | M0 | BCD|
+----+----+----+----+----+----+----+----+
```

#### Bit Descriptions:
1. **$D_7, D_6$ (Select Counter — SC1, SC0)**:
   - `00` = Select Counter 0
   - `01` = Select Counter 1
   - `10` = Select Counter 2
   - `11` = Read-Back Command (in 8254 only)
2. **$D_5, D_4$ (Read/Write Mode — RW1, RW0)**:
   - `00` = **Counter Latch Command** (latches current count value so CPU can read it on-the-fly without disturbing the ongoing count).
   - `01` = Read/Write **Least Significant Byte (LSB)** only.
   - `10` = Read/Write **Most Significant Byte (MSB)** only.
   - `11` = Read/Write **LSB first, then MSB** (two consecutive byte transfers).
3. **$D_3, D_2, D_1$ (Mode Selection — M2, M1, M0)**:
   - `000` = Mode 0 (Interrupt on Terminal Count)
   - `001` = Mode 1 (Hardware Retriggerable One-Shot)
   - `X10` (`010` or `110`) = Mode 2 (Rate Generator)
   - `X11` (`011` or `111`) = Mode 3 (Square Wave Generator)
   - `100` = Mode 4 (Software Triggered Strobe)
   - `101` = Mode 5 (Hardware Triggered Strobe)
4. **$D_0$ (BCD / Binary Format)**:
   - `0` = Binary Counter (16-bit, $0000\text{H} - \text{FFFF}\text{H}$)
   - `1` = Binary Coded Decimal (BCD) Counter (4-decade BCD, $0000 - 9999$)

---

### Six Operating Modes of the 8254

```
Mode 0 (Interrupt on Terminal Count)
CLK   ---|___|---|___|---|___|---|___|---|___|---|___|---|___
OUT   _______________________________________/---------------  (Count N expires)

Mode 1 (Hardware Retriggerable One-Shot)
GATE  _______/-----------------------------------------------  (Trigger edge)
OUT   -------/_______________________________/---------------  (Low for N counts)

Mode 2 (Rate Generator / Divide-by-N)
CLK   ---|___|---|___|---|___|---|___|---|___|---|___|---|___
OUT   -----------------------------------\___/---------------  (1 clock low pulse)

Mode 3 (Square Wave Generator)
CLK   ---|___|---|___|---|___|---|___|---|___|---|___|---|___
OUT   -----------------------/_______________________________  (50% duty cycle)

Mode 4 (Software Triggered Strobe)
CLK   ---|___|---|___|---|___|---|___|---|___|---|___|---|___
OUT   -----------------------------------\___/---------------  (Strobe on count=0)

Mode 5 (Hardware Triggered Strobe)
GATE  _______/-----------------------------------------------  (Trigger edge)
OUT   -----------------------------------\___/---------------  (Strobe N clocks later)
```

#### Detailed Breakdown:

1. **Mode 0: Interrupt on Terminal Count**
   - **Output Behavior**: Upon writing the control word, `OUT` immediately goes **LOW**. When the count value is loaded and decrements to zero ($N \to 0$), `OUT` transitions **HIGH** and stays HIGH until a new count or mode is loaded.
   - **GATE**: $\text{GATE} = 1$ enables counting; $\text{GATE} = 0$ suspends counting.
   - **Primary Use**: Generating hardware interrupts after a fixed elapsed time or serving as a digital event counter.

2. **Mode 1: Hardware-Retriggerable One-Shot**
   - **Output Behavior**: `OUT` is initially HIGH. A **low-to-high transition on the GATE pin** triggers the one-shot: `OUT` immediately drops LOW and remains LOW for exactly $N$ clock pulses, after which it returns HIGH.
   - **Retriggerable**: If another positive edge occurs on GATE while `OUT` is LOW, the counter reloads the initial count $N$ and restarts the full timing interval from that instant.
   - **Primary Use**: Generating precision monostable pulses (one-shots) in response to external sensor triggers.

3. **Mode 2: Rate Generator (Divide-by-N)**
   - **Output Behavior**: Operates as a divide-by-$N$ counter. `OUT` remains HIGH for $N-1$ clock pulses, drops LOW for **exactly one clock cycle**, and then returns HIGH. The counter automatically reloads $N$ and repeats indefinitely.
   - **Output Frequency**:
     $$f_{\text{out}} = \frac{f_{\text{CLK}}}{N}$$
   - **GATE**: $\text{GATE} = 1$ enables counting; $\text{GATE} = 0$ forces `OUT` HIGH and halts counting.
   - **Primary Use**: Generating real-time clock tick interrupts, periodic sample triggers for ADCs, and baud-rate clock inputs for UARTs.

4. **Mode 3: Square Wave Generator**
   - **Output Behavior**: Similar to Mode 2, but produces a **symmetrical square wave** with a near $50\%$ duty cycle:
     - If count $N$ is **even**: `OUT` is HIGH for $N/2$ clock cycles, and LOW for $N/2$ clock cycles.
     - If count $N$ is **odd**: `OUT` is HIGH for $(N+1)/2$ cycles, and LOW for $(N-1)/2$ cycles.
   - **Primary Use**: Generating audio tones, driving PC speakers, and synthesizing periodic clock signals.

5. **Mode 4: Software Triggered Strobe**
   - **Output Behavior**: `OUT` is initially HIGH. When the count is loaded, down-counting begins. When the count reaches zero, `OUT` goes **LOW for exactly one clock cycle**, then returns HIGH.
   - Counting does not automatically repeat; it requires a new count to be loaded by software.
   - **Primary Use**: Issuing a single delayed strobe pulse initiated by software.

6. **Mode 5: Hardware Triggered Strobe**
   - **Output Behavior**: `OUT` is initially HIGH. A **rising edge on GATE** starts the countdown. When the count reaches zero, `OUT` emits a **one-clock-wide negative strobe pulse**.
   - **Retriggerable**: A new rising edge on GATE during the countdown restarts the count.
   - **Primary Use**: Issuing a hardware-synchronized delayed strobe pulse (e.g., waiting $X$ microseconds after an optical sensor trigger before pulsing a camera flash).

---

## 2. Example: 8254 in the IBM PC/XT Architecture

In the classic IBM PC/XT/AT architectures, an 8254/8253 PIT is connected to a $1.19318\text{ MHz}$ master clock:
- **Counter 0** is programmed in **Mode 2** with a count of `0000H` ($65,536_{10}$):
  $$f_{\text{out}} = \frac{1,193,180\text{ Hz}}{65,536} \approx \mathbf{18.2\text{ Hz}}$$
  This $18.2\text{ Hz}$ output is hardwired to $\text{IRQ}_0$ of the Master 8259 PIC, creating the standard DOS system timer tick (updating the time-of-day clock 18.2 times per second).
- **Counter 1** is programmed in **Mode 2** with a count of $18_{10}$:
  $$f_{\text{out}} = \frac{1,193,180\text{ Hz}}{18} \approx 66.28\text{ kHz}$$
  This triggered DMA Channel 0 periodically to refresh dynamic RAM (DRAM).
- **Counter 2** is programmed in **Mode 3** to generate audio square waves for the built-in PC speaker.

---

## 3. Applications & Real-World Use Cases

1. **Serial Communication Baud Rate Generation**:
   - Microcontrollers and UARTs (such as the 8251 or 8051 serial port) require clock pulses at 16 times the desired baud rate ($16 \times \text{Baud}$). An 8254 counter in Mode 3 divides the system oscillator frequency down to produce exact standard baud rates (e.g., 9600, 19200, 115200 bps).
2. **Pulse-Width Modulation (PWM) for Motor Control**:
   - By cascading two counters or combining Mode 1 and Mode 2, an 8254 synthesizes variable duty-cycle PWM waveforms to control the rotational velocity of DC motors.
3. **Automated Frequency & Pulse-Width Measurement**:
   - In frequency counter instruments, Counter 0 is configured in Mode 0 as an event counter while Counter 1 provides a precise $1.000\text{ second}$ gating window to GATE0. The count accumulated in Counter 0 directly yields the unknown frequency in Hertz.

---

## 4. Solved Numerical & Analytical Examples

### Example 1: Calculating 8254 Count and Control Word for 1 kHz Square Wave
**Problem**: An 8254 is interfaced to an 8086 with base address `40H` (I/O-mapped):
- Counter 0 address: `40H`
- Counter 1 address: `42H`
- Counter 2 address: `44H`
- Control Register address: `46H`
- Counter 0 receives an input clock frequency of **$2\text{ MHz}$**.
- Design the counter to produce a continuous **$1\text{ kHz}$ square wave** on pin `OUT0` using 16-bit binary counting.

Determine:
1. The required 16-bit count value $N$.
2. The exact Control Word in hexadecimal.
3. The complete 8086 assembly initialization sequence to program Counter 0.

#### Solution:

**Step 1: Calculate Count Value $N$**
For a square wave generator, the 8254 operates in **Mode 3**:
$$f_{\text{out}} = \frac{f_{\text{CLK}}}{N} \implies N = \frac{f_{\text{CLK}}}{f_{\text{out}}}$$
$$N = \frac{2\text{ MHz}}{1\text{ kHz}} = \frac{2,000,000}{1,000} = \mathbf{2000_{10}} = \mathbf{07D0H}$$
Since $2000 \le 65,536$, this count fits perfectly into a 16-bit counter.

**Step 2: Formulate Control Word**
- Select Counter 0 $\implies \text{SC1, SC0} = 00_2$.
- 16-bit count ($07\text{D0H}$) requires reading/writing LSB first, then MSB $\implies \text{RW1, RW0} = 11_2$.
- Square wave generator $\implies \text{Mode 3} \implies \text{M2, M1, M0} = 011_2$.
- Binary count format $\implies \text{BCD} = 0$.
- Binary Control Word:
  $$\text{Bit Pattern} = 00\ 11\ 011\ 0_2 = \mathbf{36H}$$

**Step 3: Assembly Initialization Routine**
```assembly
; 8254 Port Definitions
PORT_CNT0  EQU 40H
PORT_CTRL  EQU 46H

CODE SEGMENT
    ASSUME CS:CODE
    ORG 1000H

START:
    ; 1. Write Control Word to Control Register
    MOV AL, 36H           ; Counter 0, LSB then MSB, Mode 3, Binary
    OUT PORT_CTRL, AL

    ; 2. Write LSB of Count (D0H)
    MOV AL, 0D0H          ; Low byte of 2000 (07D0H)
    OUT PORT_CNT0, AL

    ; 3. Write MSB of Count (07H)
    MOV AL, 07H           ; High byte of 2000 (07D0H)
    OUT PORT_CNT0, AL

    HLT
CODE ENDS
END START
```

---

### Example 2: Baud Rate Generator Calculation
**Problem**: An 8254 Counter 1 is used as a baud rate clock generator for an 8251A USART.
- The input clock to Counter 1 is **$1.8432\text{ MHz}$**.
- The USART baud rate multiplier is configured for **$16\times$** clock mode.
- Determine the required count value $N$ and the control word to generate standard communication baud rates:
  1. $9600\text{ bps}$
  2. $19200\text{ bps}$

#### Solution:
In $16\times$ clock mode, the USART requires an input clock frequency of:
$$f_{\text{USART}} = 16 \times \text{Baud Rate}$$
The 8254 operates in **Mode 3 (Square Wave Generator)** or **Mode 2 (Rate Generator)**. Using Mode 3:
$$N = \frac{f_{\text{CLK}}}{f_{\text{USART}}} = \frac{f_{\text{CLK}}}{16 \times \text{Baud Rate}}$$

**Part 1: For 9600 bps**
$$f_{\text{USART}} = 16 \times 9600 = 153,600\text{ Hz}$$
$$N = \frac{1,843,200\text{ Hz}}{153,600\text{ Hz}} = \mathbf{12_{10}} = \mathbf{000CH}$$
- Because $N = 12 \le 255$, this can be loaded using **LSB only** ($\text{RW1, RW0} = 01_2$):
  - $\text{SC1, SC0} = 01_2$ (Counter 1)
  - $\text{RW1, RW0} = 01_2$ (LSB only)
  - $\text{Mode 3} = 011_2$
  - $\text{Binary} = 0$
  - Control Word = $01\ 01\ 011\ 0_2 = \mathbf{56H}$.

**Part 2: For 19200 bps**
$$f_{\text{USART}} = 16 \times 19,200 = 307,200\text{ Hz}$$
$$N = \frac{1,843,200\text{ Hz}}{307,200\text{ Hz}} = \mathbf{6_{10}} = \mathbf{0006H}$$
- Control Word: **`56H`**, Count loaded into Counter 1: **`06H`**.

---

### Example 3: On-the-Fly Counter Reading using Counter Latch Command
**Problem**: An 8254 Counter 2 is counting external events arriving on pin `CLK2` in Mode 0.
- Explain why a programmer cannot reliably read the 16-bit count using two ordinary `IN` instructions while counting is active.
- Show how the **Counter Latch Command** solves this problem and write the assembly code to read the latched count into register `BX`.

#### Solution:
1. **The Race Condition Bottleneck**:
   If the CPU executes `IN AL, PORT_CNT2` to read the low byte, the counter continues counting down. Before the CPU can execute the second `IN AL, PORT_CNT2` to read the high byte, the low byte may borrow and cause the high byte to decrement (e.g., count transitioning from `0200H` to `01FFH`). If the CPU reads the low byte as `00H` and the high byte after the borrow as `01H`, it constructs the erroneous value `0100H` instead of `0200H` or `01FFH`.
2. **Counter Latch Command Solution**:
   Writing a control word with bits $\text{RW1, RW0} = 00_2$ issues a **Counter Latch Command**. The internal control logic instantaneously latches the current 16-bit count into an internal Output Latch (OL) register without stopping or perturbing the active down-counter. The CPU can then read the stable latched count at its leisure.

**Assembly Code**:
```assembly
PORT_CNT2 EQU 44H
PORT_CTRL EQU 46H

; 1. Issue Counter Latch Command for Counter 2
; SC1, SC0 = 10 (Counter 2), RW1, RW0 = 00 (Latch Command), bits D3-D0 = 0000
MOV AL, 10000000B     ; 80H: Latch Counter 2
OUT PORT_CTRL, AL

; 2. Read LSB of latched count
IN  AL, PORT_CNT2
MOV BL, AL            ; Save LSB in BL

; 3. Read MSB of latched count
IN  AL, PORT_CNT2
MOV BH, AL            ; Save MSB in BH
; Register BX now holds the exact, uncorrupted 16-bit count!
```

---

## 5. Previous Year Questions & Solutions

### Question 1 (KTU B.Tech Examination)
**Draw and explain the internal architecture of 8254 PIT. Explain the different operating modes of 8254 with appropriate waveforms.** [10 Marks]

#### Complete Self-Contained Solution:
1. **8254 Internal Architecture**:
   The 8254 Programmable Interval Timer comprises:
   - **Data Bus Buffer**: An 8-bit bidirectional buffer connecting internal registers to system data bus $D_0 - D_7$.
   - **Read/Write Control Logic**: Decodes $\overline{\text{RD}}, \overline{\text{WR}}, \overline{\text{CS}}, A_1, A_0$ to address Counter 0, Counter 1, Counter 2, or the Control Word Register.
   - **Control Word Register**: Stores mode selection and format commands written with $A_1 A_0 = 11$.
   - **Three Independent 16-Bit Down-Counters (Counter 0, 1, 2)**: Each counter has a 16-bit Count Register (CR), a 16-bit Down-Counter (CE), and a 16-bit Output Latch (OL). Each has pins `CLK`, `GATE`, and `OUT`.
   *(Include the architecture diagram from Section 1).*

2. **Six Operating Modes with Waveforms**:
   *(Include the waveforms and detailed explanations for Modes 0 through 5 from Section 1)*:
   - **Mode 0 (Interrupt on Terminal Count)**: `OUT` drops low upon mode load; transitions high when count expires.
   - **Mode 1 (Hardware Retriggerable One-Shot)**: Low-to-high transition on GATE pulls `OUT` low for $N$ clock cycles.
   - **Mode 2 (Rate Generator)**: Divide-by-$N$ counter; `OUT` stays high for $N-1$ clocks, low for 1 clock cycle.
   - **Mode 3 (Square Wave Generator)**: Symmetrical $50\%$ duty cycle square wave ($N/2$ high, $N/2$ low).
   - **Mode 4 (Software Triggered Strobe)**: `OUT` stays high until count decrements to 0, emitting a 1-clock negative strobe.
   - **Mode 5 (Hardware Triggered Strobe)**: GATE rising edge triggers down-count; emits 1-clock negative strobe when count reaches 0.

---

### Question 2 (KTU B.Tech Examination)
**Explain the Control Word format of 8254. Write an assembly language program to initialize Counter 1 in Mode 2 to generate a rate with a count of 5000 using binary counting.** [10 Marks]

#### Complete Self-Contained Solution:
1. **Control Word Format**:
   *(Include the bit diagram and field explanations from Section 1)*:
   - $D_7 D_6$ ($\text{SC1, SC0}$): Counter Select (`00`=Counter 0, `01`=Counter 1, `10`=Counter 2, `11`=Read-Back).
   - $D_5 D_4$ ($\text{RW1, RW0}$): Read/Write format (`00`=Latch, `01`=LSB, `10`=MSB, `11`=LSB then MSB).
   - $D_3 D_2 D_1$ ($\text{M2, M1, M0}$): Mode 0 to 5 (`010` for Mode 2).
   - $D_0$ ($\text{BCD}$): $0 = \text{Binary}$ (16-bit), $1 = \text{BCD}$.

2. **Control Word Calculation**:
   - Counter 1 $\implies D_7 D_6 = 01_2$.
   - Count is $5000_{10} = 1388\text{H}$ (16-bit word) $\implies$ Write LSB then MSB $\implies D_5 D_4 = 11_2$.
   - Mode 2 (Rate Generator) $\implies D_3 D_2 D_1 = 010_2$.
   - Binary counting $\implies D_0 = 0$.
   - Control Word = $01\ 11\ 010\ 0_2 = \mathbf{74H}$.

3. **8086 Assembly Program**:
```assembly
CNT1_PORT EQU 42H
CTRL_PORT EQU 46H

CODE SEGMENT
    ASSUME CS:CODE
    ORG 1000H

START:
    ; 1. Write Control Word 74H to Control Register
    MOV AL, 74H
    OUT CTRL_PORT, AL

    ; 2. Write LSB of count 5000 (1388H -> LSB = 88H)
    MOV AL, 88H
    OUT CNT1_PORT, AL

    ; 3. Write MSB of count 5000 (1388H -> MSB = 13H)
    MOV AL, 13H
    OUT CNT1_PORT, AL

    HLT
CODE ENDS
END START
```

