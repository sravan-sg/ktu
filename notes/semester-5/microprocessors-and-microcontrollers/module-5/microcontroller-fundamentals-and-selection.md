# Microcontroller Fundamentals and Selection Criteria

> **Senior CS Professor Notes** | Semester 5 — CS305 Microprocessors & Microcontrollers | Module V

---

## 1. Explanation

### What is a Microcontroller?
A **microcontroller (MCU)** is a complete, self-contained computer-on-a-chip. Unlike a general-purpose microprocessor (such as the Intel 8086 or Core i7) which contains only a Central Processing Unit (CPU) and requires dozens of external support chips (RAM, ROM, I/O ports, timers, interrupt controllers, clock generators) to form a functional computer, a microcontroller integrates:
1. A **CPU core** (ALU, registers, instruction decoder).
2. **On-chip Data Memory (RAM)** for variable and stack storage.
3. **On-chip Program Memory (ROM / Flash / EPROM)** for non-volatile firmware execution.
4. **General-Purpose Input/Output (GPIO) Ports** to interface with sensors, switches, and actuators.
5. **Hardware Timers and Counters** for precision event timing, pulse-width modulation (PWM), and frequency measurement.
6. **Serial Communication Interfaces** (UART, SPI, $I^2C$, CAN, USB) for digital telemetry.
7. **Analog Peripherals** (Analog-to-Digital Converters - ADC, Comparators).
8. **Interrupt Controller** and on-chip clock oscillator circuitry.

This integration reduces printed circuit board (PCB) footprint, decreases manufacturing cost, dramatically lowers power consumption, and eliminates high-frequency electromagnetic interference (EMI) radiating across external address and data buses.

---

### Architectural Divergence: Microprocessor vs. Microcontroller

The fundamental difference between microprocessors and microcontrollers stems from their design objectives:

```
     Microprocessor (e.g., 8086)                    Microcontroller (e.g., 8051)
  +-------------------------------+             +----------------------------------+
  |             CPU               |             |          Single Silicon IC       |
  |  (ALU, Registers, Pipeline)   |             |  +----------------------------+  |
  +-------------------------------+             |  |            CPU             |  |
                 |                              |  +----------------------------+  |
    External System Bus                         |        | Internal Buses       |  |
  +--------------+----------------+             |  +-----+-----+-----+----+-----+  |
  |              |                |             |  | RAM | ROM | I/O | TMR|UART |  |
+----+        +----+           +----+           |  +-----+-----+-----+----+-----+  |
|RAM |        |ROM |           |I/O |           +----------------------------------+
+----+        +----+           +----+           (Self-contained System on Chip)
(Separate external chips required)
```

| Architectural Feature | Microprocessor (e.g., Intel 8086) | Microcontroller (e.g., Intel 8051) |
|---|---|---|
| **System Architecture** | CPU only on-chip. Memory and peripherals reside on external PCB chips. | Single-chip microcomputer: CPU, RAM, ROM, I/O, timers all on one die. |
| **Memory Architecture** | Typically **Von Neumann** (unified memory space for instructions and data). | Typically **Harvard** (physically separate buses and spaces for Code and Data). |
| **Instruction Set Focus** | Optimized for complex arithmetic, string processing, and large memory array computation. | Optimized for single-bit boolean manipulation, pin toggling, and control decisions. |
| **Pin Usage** | Address/data bus pins are committed to external bus expansion. | Pins multiplex as General Purpose I/O (GPIO) lines or peripheral functions. |
| **Access Speed** | Memory access is constrained by external PCB capacitive load and bus cycles. | Internal register/RAM access occurs at high speed with low clock latency. |
| **Power Consumption** | High power consumption (typically several hundred milliwatts to tens of watts). | Low power consumption (milliwatts to microwatts; includes Idle/Power-Down modes). |
| **Typical Application** | General-purpose computing (PCs, servers, workstations, laptops). | Dedicated embedded real-time control (appliances, automobiles, robotics). |

---

### Evolution and Classification of Microcontrollers

Microcontrollers are categorized primarily by the data-bus width of their internal ALU:

1. **4-Bit Microcontrollers**:
   - Earliest MCUs (e.g., TMS1000, NEC $\mu\text{PD}7500$).
   - Ultra-low cost, optimized for simple BCD calculations.
   - Applications: Handheld electronic calculators, digital watches, toys, microwave oven keypads.
2. **8-Bit Microcontrollers**:
   - The historic workhorses of embedded engineering (e.g., Intel 8051, Microchip PIC16/PIC18, Atmel AVR ATmega328P used in Arduino).
   - Excellent balance of mathematical capability, simplicity, rich peripheral sets, and low cost.
   - Applications: Home appliances, motor speed control, remote controls, smart energy meters.
3. **16-Bit Microcontrollers**:
   - Bridge the gap between 8-bit simplicity and 32-bit computational power (e.g., Intel 8096, TI MSP430, Microchip dsPIC).
   - Optimized for ultra-low-power sensing (MSP430) or intermediate digital signal processing.
   - Applications: Battery-operated medical implants, digital blood pressure monitors, automotive climate control.
4. **32-Bit Microcontrollers**:
   - Dominated by ARM Cortex-M cores (Cortex-M0/M3/M4/M7, e.g., STM32, NXP LPC, ESP32).
   - High clock speeds ($50\text{ MHz} - 600\text{ MHz}$), hardware floating-point units (FPUs), megabytes of flash memory, direct DMA channels.
   - Applications: Automotive Engine Control Units (ECUs), drones, modern smart IoT devices, smartwatches.

---

### Criteria for Selecting a Microcontroller

When designing a commercial embedded product, selecting the optimal microcontroller is a critical systems engineering decision. Choosing an overpowered chip inflates bill-of-materials (BOM) cost and consumes excessive battery power; choosing an underpowered chip results in missed real-time deadlines and product failure.

The selection criteria are grouped into four technical dimensions:

#### 1. Computational & Architectural Requirements
- **Word Length (Data Width)**: 8-bit for basic sensor polling and relay actuation; 16-bit or 32-bit for real-time mathematical filtering (FFT, PID loops, DSP).
- **Processing Speed (MIPS / Clock Frequency)**: Must guarantee that all real-time control loops and interrupt service routines finish well within their hard deadlines.
- **Instruction Set Architecture**: CISC (code density) vs. RISC (execution speed and deterministic pipeline).

#### 2. Memory Requirements
- **On-Chip Flash (Program Memory)**: Sized to accommodate compiled firmware, lookup tables, and future Over-the-Air (OTA) firmware upgrade margins (typically $30\%$ safety margin).
- **On-Chip SRAM (Data Memory)**: Sized to hold runtime variables, dynamic buffers, and deep nested stack frames during interrupt handling.
- **EEPROM**: Sized for non-volatile configuration parameters and calibration constants that must survive power cycles.

#### 3. Peripheral & I/O Requirements
- **Digital GPIO Pin Count**: Total number of dedicated input/output pins required for buttons, LEDs, and chip-select lines.
- **Analog Peripherals**: Resolution (10-bit, 12-bit) and sample rate (kSPS) of built-in ADCs; presence of DACs or analog comparators.
- **Communication Buses**: Required hardware peripherals for UART, SPI, $I^2C$, USB, CAN bus (mandatory in automotive), or Ethernet.
- **Hardware Timers & PWM Channels**: Necessary for driving brushless DC motors, generating precise audio tones, or measuring pulse widths.

#### 4. Physical, Electrical & Commercial Constraints
- **Power Consumption**: Current draw in active mode and quiescent current during Sleep/Deep-Sleep modes (crucial for multi-year coin-cell battery life).
- **Operating Voltage & Temperature**: Automotive qualification (AEC-Q100, $-40^\circ\text{C}$ to $+125^\circ\text{C}$) or industrial rating ($-40^\circ\text{C}$ to $+85^\circ\text{C}$).
- **Packaging**: Small surface-mount footprints (QFN, BGA) for wearables vs. easily solderable packages (DIP, TQFP) for educational or low-cost PCB assembly.
- **BOM Cost & Long-Term Availability**: Unit cost at volume and manufacturer longevity commitment (guaranteed 10 to 15-year production runs).

---

## 2. Example: System Block Diagram of an Embedded MCU Application

### Automated Green-House Climate Controller using 8051

```
                    Automated Embedded Greenhouse Controller
  +-------------------------------------------------------------------------+
  |                           8051 Microcontroller                          |
  |                                                                         |
  |  +--------------------+                     +------------------------+  |
  |  | Port 0 (P0.0-P0.7) |                     |  Port 1 (P1.0-P1.7)    |  |
  |  +--------------------+                     +------------------------+  |
  |            | (Pull-ups)                                  |              |
  |            v                                             v              |
  |      +-----------+                                +--------------+      |
  |      | 16x2 LCD  |                                | Relays/Motor |      |
  |      | Display   |                                | Heaters,Fans |      |
  |      +-----------+                                +--------------+      |
  |                                                                         |
  |  +--------------------+                     +------------------------+  |
  |  | Port 2 (P2.0-P2.7) |                     |  Port 3 (P3.0-P3.7)    |  |
  |  +--------------------+                     +------------------------+  |
  |            ^                                       |            ^       |
  |            |                                       v            |       |
  |      +-----------+                              +-----+      +-----+    |
  |      | ADC0808   |<-----------------------------| WR# |      | INT0|    |
  |      | (Temp/Hum |                              | RD# |      | EOC |    |
  |      |  Sensors) |                              +-----+      +-----+    |
  +-------------------------------------------------------------------------+
```

---

## 3. Applications & Real-World Use Cases

1. **Automotive Electronic Control Units (ECUs)**:
   - Modern luxury automobiles contain over 80 microcontrollers networked via the Controller Area Network (CAN) bus. Microcontrollers manage anti-lock braking systems (ABS), airbag deployment accelerometers, and engine fuel injection timing.
2. **Medical Monitoring Equipment**:
   - Portable battery-powered glucose meters and pulse oximeters utilize ultra-low-power microcontrollers (e.g., MSP430) to amplify bio-potentials, perform ADC conversion, compute blood oxygen saturation ($SpO_2$), and display results on an LCD.
3. **Consumer Appliances & White Goods**:
   - Modern fully automatic washing machines use microcontrollers (like the 8051 or STM8) to monitor water level pressure switches, cycle through drum agitation cycles using triac phase control, and detect unbalanced loads via motor back-EMF sensing.

---

## 4. Solved Numerical & Analytical Examples

### Example 1: Battery Life Calculation for an IoT Node
**Problem**: A wireless soil moisture sensor node is powered by a $3.0\text{ V}$, $2400\text{ mAh}$ Lithium battery.
- The microcontroller operates with the following duty cycle:
  - **Active Mode**: The MCU wakes up once every $10\text{ minutes}$ for a duration of $200\text{ ms}$ to power the sensor, take an ADC reading, compute moisture percentage, and transmit a packet over LoRa. In Active Mode, the total system current draw is $35\text{ mA}$.
  - **Deep-Sleep Mode**: For the remaining duration of the $10\text{ minute}$ window, the MCU enters deep-sleep mode, drawing a quiescent current of $15\ \mu\text{A}$.
- Calculate:
  1. The average current consumption of the system ($I_{\text{avg}}$).
  2. The expected operational battery life in days and years (assuming $85\%$ usable battery capacity).

#### Solution:

**Step 1: Convert Time Periods to Seconds**
$$\text{Total Period } T = 10\text{ minutes} = 600\text{ seconds}$$
$$t_{\text{active}} = 200\text{ ms} = 0.2\text{ seconds}$$
$$t_{\text{sleep}} = 600 - 0.2 = 599.8\text{ seconds}$$

**Step 2: Calculate Average Current Consumption ($I_{\text{avg}}$)**
$$I_{\text{avg}} = \frac{(I_{\text{active}} \times t_{\text{active}}) + (I_{\text{sleep}} \times t_{\text{sleep}})}{T}$$
$$\begin{aligned}
I_{\text{avg}} &= \frac{(35\text{ mA} \times 0.2\text{ s}) + (0.015\text{ mA} \times 599.8\text{ s})}{600\text{ s}} \\
&= \frac{7.0\text{ mA}\cdot\text{s} + 8.997\text{ mA}\cdot\text{s}}{600\text{ s}} = \frac{15.997}{600} \approx \mathbf{0.02666\text{ mA}} = \mathbf{26.66\ \mu\text{A}}
\end{aligned}$$

**Step 3: Calculate Battery Life**
- Usable battery capacity:
  $$C_{\text{usable}} = 2400\text{ mAh} \times 0.85 = 2040\text{ mAh}$$
- Operational hours:
  $$\text{Operating Hours} = \frac{C_{\text{usable}}}{I_{\text{avg}}} = \frac{2040\text{ mAh}}{0.02666\text{ mA}} \approx 76,519\text{ hours}$$
- Operational life in days and years:
  $$\text{Life (Days)} = \frac{76,519}{24} \approx \mathbf{3,188\text{ days}}$$
  $$\text{Life (Years)} = \frac{3,188}{365} \approx \mathbf{8.73\text{ years}}$$

---

### Example 2: Selecting Microcontroller Memory Size
**Problem**: An embedded software engineer is sizing a microcontroller for an industrial digital thermostat:
- Compiled machine code for system initialization, PID control algorithm, and LCD driver requires $14.5\text{ KB}$.
- A lookup table storing temperature sensor calibration curves requires $6\text{ KB}$ of non-volatile read-only storage.
- Runtime variables, display buffers, and control state variables require $380\text{ bytes}$.
- Subroutine call depth is at most 6 levels, and interrupt service routines can nest up to 2 levels. Each call or interrupt pushes 4 bytes onto the stack.
- The client mandates a minimum $25\%$ headroom for future firmware features.

Evaluate whether an 8051 derivative with $32\text{ KB}$ Flash ROM and $512\text{ bytes}$ on-chip RAM satisfies these engineering requirements.

#### Solution:

**Step 1: Program Memory (ROM / Flash) Evaluation**
$$\text{Firmware Code} = 14.5\text{ KB}$$
$$\text{Lookup Table} = 6.0\text{ KB}$$
$$\text{Total Base ROM Required} = 14.5 + 6.0 = 20.5\text{ KB}$$
Applying the required $25\%$ engineering safety headroom:
$$\text{Required Flash Capacity} = 20.5\text{ KB} \times 1.25 = \mathbf{25.625\text{ KB}}$$
Since the candidate MCU provides **$32\text{ KB}$ Flash**, it comfortably exceeds the $25.625\text{ KB}$ threshold ($32\text{ KB} \ge 25.625\text{ KB}$). **PASSED**.

**Step 2: Data Memory (RAM) Evaluation**
- Variable storage: $380\text{ bytes}$.
- Stack Depth calculation:
  - Max nested calls: 6 calls $\times 4\text{ bytes/call} = 24\text{ bytes}$.
  - Max nested interrupts: 2 ISRs $\times 4\text{ bytes/ISR} = 8\text{ bytes}$.
  - Register scratchpad saving inside ISRs: 2 ISRs $\times 8\text{ bytes} = 16\text{ bytes}$.
  - Total Maximum Stack Size = $24 + 8 + 16 = \mathbf{48\text{ bytes}}$.
- Total RAM required:
  $$\text{Total RAM} = 380\text{ bytes (Variables)} + 48\text{ bytes (Stack)} = \mathbf{428\text{ bytes}}$$
Since the candidate MCU provides **$512\text{ bytes}$ on-chip RAM**, the required 428 bytes leaves $84\text{ bytes}$ of margin ($16.4\%$ headroom). **PASSED**.

---

### Example 3: Microprocessor vs. Microcontroller Board-Level Cost Trade-Off
**Problem**: A startup is manufacturing 50,000 units of an electronic motor controller. They are comparing two hardware architectures:
- **Design A (Microprocessor-Based)**: Uses an 8086 CPU (\$2.20), external 64 KB Flash ROM (\$1.10), external 32 KB SRAM (\$0.90), 8255 PPI (\$1.50), clock generator 8284 (\$0.80), and address latches/buffers (\$0.60). Additional PCB area and 4-layer routing adds \$1.80 per board.
- **Design B (Microcontroller-Based)**: Uses a single 8051-compatible microcontroller chip integrating CPU, 64 KB Flash, 1 KB RAM, and 32 I/O lines (\$2.10). A compact 2-layer PCB costs \$0.70.

Calculate the total Bill of Materials (BOM) cost savings achieved across the entire production run of 50,000 units by selecting the microcontroller design.

#### Solution:

**Step 1: Cost per Unit for Design A (Microprocessor)**
$$\begin{aligned}
\text{Cost}_A &= \text{CPU} + \text{ROM} + \text{RAM} + \text{PPI} + \text{Clock} + \text{Latches} + \text{PCB} \\
&= \$2.20 + \$1.10 + \$0.90 + \$1.50 + \$0.80 + \$0.60 + \$1.80 = \mathbf{\$8.90 \text{ per unit}}
\end{aligned}$$

**Step 2: Cost per Unit for Design B (Microcontroller)**
$$\begin{aligned}
\text{Cost}_B &= \text{MCU} + \text{PCB} \\
&= \$2.10 + \$0.70 = \mathbf{\$2.80 \text{ per unit}}
\end{aligned}$$

**Step 3: Total Cost Savings for 50,000 Units**
$$\text{Savings per Unit} = \$8.90 - \$2.80 = \mathbf{\$6.10}$$
$$\text{Total Production Savings} = 50,000 \times \$6.10 = \mathbf{\$305,000}$$
Choosing the microcontroller architecture saves **\$305,000** ($68.5\%$ cost reduction), demonstrating why microcontrollers dominate dedicated embedded product designs.

---

## 5. Previous Year Questions & Solutions

### Question 1 (KTU B.Tech Examination)
**Differentiate between a microprocessor and a microcontroller. Explain the criteria to be considered while selecting a microcontroller for an embedded application.** [9 Marks]

#### Complete Self-Contained Solution:
1. **Microprocessor vs Microcontroller Architectural Comparison**:
   - A **Microprocessor** is an IC containing solely the central processing unit (ALU, registers, control logic). It relies completely on external chips connected via a system bus for program memory (ROM), data memory (RAM), and input/output interfaces. It is designed for computationally intensive, general-purpose computer applications where software requirements dynamically expand.
   - A **Microcontroller** is an entire microcomputer fabricated on a single monolithic silicon chip. It integrates CPU, RAM, ROM/Flash, general-purpose I/O ports, hardware timers, interrupt logic, and communication peripherals (UART, SPI, ADC) onto the same substrate. It is optimized for dedicated, real-time control applications with tight cost, space, and power budgets.
   *(Include the comparative analysis table from Section 1 detailing system architecture, Harvard vs Von Neumann, instruction focus, pin usage, power, and applications).*

2. **Microcontroller Selection Criteria**:
   When selecting a microcontroller for a commercial embedded design, an engineer must evaluate:
   - **Word Length & Speed**: Determining whether an 8-bit, 16-bit, or 32-bit architecture is required to satisfy processing speed (MIPS) and meet control loop real-time deadlines.
   - **On-Chip Memory Capacity**: Sizing internal Flash/ROM for firmware code and internal SRAM for variables and stack space, ensuring adequate headroom ($20-30\%$) for future revisions.
   - **I/O Capability**: Verifying that the MCU has sufficient digital I/O pins, high-current drive outputs, and dedicated analog peripherals (ADCs, DACs).
   - **Communication Peripherals**: Ensuring native hardware support for required communication protocols (UART, SPI, $I^2C$, CAN, USB).
   - **Power Consumption**: Analyzing active operating current and sleep/power-down modes to satisfy battery operational lifetime targets.
   - **Cost and Long-Term Availability**: Balancing unit BOM cost against packaging requirements and manufacturer production longevity.

---

### Question 2 (KTU B.Tech Examination)
**Classify microcontrollers based on bit width and architectural features. Give two commercial examples and typical applications for each category.** [9 Marks]

#### Complete Self-Contained Solution:
1. **Classification of Microcontrollers**:
   Microcontrollers are categorized based on their internal data bus width:
   - **4-Bit Microcontrollers**:
     - *Architecture*: 4-bit ALU and data bus, highly compact instruction sets optimized for BCD arithmetic.
     - *Examples*: TMS1000, NEC $\mu\text{PD}7500$.
     - *Applications*: Electronic handheld calculators, simple digital clocks, electronic toys.
   - **8-Bit Microcontrollers**:
     - *Architecture*: 8-bit ALU, Harvard architecture, extensive bit-manipulation instructions, rich on-chip peripherals.
     - *Examples*: Intel 8051 (AT89C51), Atmel AVR (ATmega328P), Microchip PIC16F877A.
     - *Applications*: Home automation controllers, automotive wiper/lighting controls, washing machine controllers.
   - **16-Bit Microcontrollers**:
     - *Architecture*: 16-bit ALU and register set, extended 16-bit to 24-bit addressing, ultra-low-power sleep modes.
     - *Examples*: Texas Instruments MSP430, Intel 8096, Microchip dsPIC33.
     - *Applications*: Battery-operated medical diagnostic devices (glucose meters), precision industrial telemetry sensors.
   - **32-Bit Microcontrollers**:
     - *Architecture*: 32-bit RISC cores (primarily ARM Cortex-M0/M3/M4/M7), hardware floating-point units (FPU), multi-channel DMA controllers, high-speed clocking ($50 - 500\text{ MHz}$).
     - *Examples*: STMicroelectronics STM32F4 series, Espressif ESP32, NXP LPC1768.
     - *Applications*: Automotive Engine Control Units (ECUs), drones and quadcopter flight stabilization, smart IoT gateways, robotics.

