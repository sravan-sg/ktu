# Regulated Power Supplies

## 1. Explanation

### Core Intuition: Why Do We Need Voltage Regulation?

An unregulated DC power supply (rectifier + filter capacitor) produces a DC voltage that fluctuates with:
1. **Load current changes:** More load → more voltage drop across internal resistance → output drops
2. **AC mains variations:** ±10% input voltage change → proportional output change
3. **Temperature:** Component values drift with temperature

**Quantifying the problem:**

Consider an unregulated supply with internal resistance Rint = 5Ω:
```
No load:  Vout = 12V
Full load (IL = 200mA): Vout = 12 - 0.2 × 5 = 11V  (8.3% drop!)
```

For digital circuits (which need ±5% supply tolerance), or analog circuits (where even 1% supply change affects signal quality), this is unacceptable.

**Key regulation specifications:**

**Load Regulation:**
```
Load Regulation (%) = (VNL - VFL) / VFL × 100%

Where: VNL = no-load output voltage
       VFL = full-load output voltage

Good regulator: < 0.1% load regulation
```

**Line Regulation:**
```
Line Regulation (%/V) = ΔVout / ΔVin × 100%

Good regulator: < 0.01%/V
```

**Ripple Rejection (PSRR — Power Supply Rejection Ratio):**
```
PSRR (dB) = 20 log10(ΔVin(ripple) / ΔVout(ripple))

7805 typical PSRR: 60-70dB  → for 100mV input ripple, only 0.03-0.1mV appears at output
```

**Two fundamental approaches:**
- **Linear regulators**: Dissipate excess power as heat (series or shunt resistive element). Simple, low noise, but poor efficiency.
- **Switching regulators (SMPS)**: Switch power on/off rapidly, store in L/C. Complex but 80-90% efficient.

---

### Zener Voltage Regulator (Review and Analysis)

**Operating principle:**

The zener diode in reverse breakdown maintains a nearly constant voltage VZ across itself for a wide range of reverse current IZ:

```
         Rs
Vin ─────┤├─────┬───── Vout = VZ
                │
               ─|← Zener (VZ, reverse biased)
                │
              [RL] (load)
                │
               GND
```

**Complete Circuit Analysis:**

KCL at junction: IT = IZ + IL

KVL: Vin = IT × Rs + VZ

```
IT = (Vin - VZ) / Rs   [total current supplied by Rs]
IL = Vout / RL = VZ / RL   [load current]
IZ = IT - IL = (Vin - VZ)/Rs - VZ/RL   [zener current; must stay > IZ(knee)]
```

**Design constraints:**

For proper regulation, IZ must always be ≥ IZ(knee) (typically 5mA):
```
Case 1 — Maximum load (IL = IL(max)):
IZ(min) = (Vin_min - VZ)/Rs - IL(max) ≥ IZ(knee)   → determines Rs(max)

Case 2 — Minimum/No load (IL = 0):
IZ(max) = (Vin_max - VZ)/Rs ≤ PZ(max)/VZ   → determines minimum Rs and zener power rating

Design: Rs = (Vin_min - VZ) / (IL(max) + IZ(knee))
```

**Why zener regulation is self-correcting:**

The zener's dynamic resistance rz (slope of I-V curve in breakdown) is typically 5-30Ω. If Vin changes by ΔVin:

```
ΔVout = ΔVin × rz / (Rs + rz) ≈ ΔVin × rz/Rs   (since rz << Rs)

For Rs = 330Ω, rz = 10Ω:
ΔVout/ΔVin = 10/330 = 0.03 → only 3% of input change appears at output!
```

**Limitation of zener-only regulator:**
- Poor efficiency (zener always dissipates IZ × VZ)
- Limited current capacity (PZ(max) typically 400mW-1W)
- Output resistance = rz || Rs ≈ rz (not zero)

---

### Shunt Voltage Regulator (Transistor-Assisted)

Adding a transistor in shunt (parallel) with the load increases current capacity while the zener provides a stable reference:

```
          Rs
Vin ─────┤├──────────┬──── Vout
                     │
                  [Load RL]
                     │
        Base ─── Q (NPN) ─── Collector (tied to Vout)
          │                     Emitter (tied to GND)
         ─|← Zener VZ
          │
         GND
```

**Operation:**

Q's base is held at VZ by the zener. Emitter follows: VE = VZ - VBE ≈ VZ - 0.7V.

Wait — in the correct shunt regulator, the transistor's Collector-Emitter (CE) path shunts the load. Here:
- Base = VZ (stable, set by zener)
- Emitter = VZ - VBE ≈ output side — but actually for shunt regulation, collector-emitter is in PARALLEL with the load.

**Self-correcting loop:**
```
Vout ↑ → (since base = VZ = fixed) → VEB increases → IB increases → IC (shunt) increases
       → More current drawn from Rs → Voltage drop on Rs increases → Vout ↓ (corrected)
```

**Output voltage:**
```
Vout ≈ VZ - VBE ≈ VZ - 0.7V (if emitter connected to output and collector to GND)
```

OR for the transistor with emitter to GND:
```
Vout ≈ VZ + VBE(Q) (zener at emitter junction, Vout at collector side)
```

**Analysis:**
```
IQ (shunt transistor current) = β × IB
IT (total) = IQ + IL = constant (set by Rs and Vin)

As IL increases: IQ decreases (transistor shunts less) to keep IT constant
As IL decreases: IQ increases (transistor shunts more) to keep IT constant
```

**Disadvantage:** Always draws large shunt current even at no load → poor efficiency.

---

### Series Voltage Regulator — Detailed Analysis

The series regulator places a **pass transistor Q1 in series** between the unregulated input and the regulated output. Q1 acts as a variable resistance, dropping the excess (Vin - Vout) voltage.

**Full circuit with error amplifier:**

```
     VCC (unregulated)
          │
        [Q1] ← Series pass transistor (NPN, power transistor like 2N3055)
          │ Collector
          │  Emitter ──────────────────── Vout (regulated)
          │                                    │
     Base ────[R_base]──[Q2 Collector]    [R1] (voltage divider, R1 from Vout to sense)
                         Q2 Emitter ─ GND [R2] (R2 from sense to GND)
                         Q2 Base ───────────┘ (sense point: Vsense = Vout×R2/(R1+R2))
                             │
                          [Zener]
                             │
                            GND
```

**Working (step-by-step):**

1. **Zener establishes reference Vref = VZ** (e.g., 5.1V)

2. **Q2 is the error amplifier** — it compares Vsense (sampled Vout) with Vref:
   - VB(Q2) = Vsense = Vout × R2/(R1+R2)
   - VE(Q2) = VZ (held by zener)
   - Q2 base-emitter: VBE(Q2) = Vsense - VZ

3. **Negative feedback loop:**

   ```
   Vout rises → Vsense rises → VBE(Q2) increases → IC(Q2) increases
   → More voltage dropped across Q2 collector resistor → VB(Q1) drops
   → Q1 base-emitter voltage drops → Q1 less conductive → VCE(Q1) increases
   → Output side: Vout = Vin - VCE(Q1) drops → Vout is corrected ✓
   ```

4. **Output voltage derivation:**

   At equilibrium: VB(Q2) - VE(Q2) = VBE(Q2) = 0.7V constant
   ```
   VB(Q2) = Vref + VBE(Q2)   where Vref = VZ
   
   But Vsense = Vout × R2/(R1+R2) = Vref + VBE(Q2) ≈ Vref (approx, since VBE is constant)
   
   → Vout = Vref × (R1+R2)/R2 = Vref × (1 + R1/R2)
   ```

5. **Output is continuously adjusted** to maintain this ratio. Changing R1 or R2 changes Vout.

**Efficiency of series regulator:**
```
Efficiency η = Pout / Pin = (Vout × IL) / (Vin × IT)

For Vin = 15V, Vout = 12V, IL = 500mA:
η = (12 × 0.5) / (15 × 0.5) = 6/7.5 = 80%   (upper limit; actual is lower due to quiescent current)
```

**Power dissipated in pass transistor Q1:**
```
PQ1 = (Vin - Vout) × IL = (15 - 12) × 0.5 = 1.5W   (must be heatsunk!)
```

### Current Limiting and Foldback Protection

**Why current limiting?**

Without protection, a short circuit (RL = 0Ω) causes:
```
IL → ∞, VCE(Q1) → Vin - 0 = Vin (maximum), PQ1 = Vin × IL → transistor destroyed
```

**1. Simple (constant) current limiting:**

```
     VCC
      │
    [Q1] ─── RSC ─── Vout
      │              │
   [Q2 NPN]      [RSC senses IL: when IL×RSC = 0.7V → Q2 ON]
      Base ─── junction between Q1 emitter and RSC
```

When output current IL exceeds the limit:
```
IL × RSC ≥ VBE(Q2) = 0.7V
→ Q2 turns ON
→ Q2 steals Q1 base current
→ Q1 cannot conduct more current
→ IL is limited to: I_SC = 0.7V / RSC
```

Design for I_SC = 150mA: RSC = 0.7/0.15 = 4.67Ω ≈ 4.7Ω

**Problem with constant current limiting:** At short circuit (Vout = 0):
```
Power in Q1: PQ1 = Vin × I_SC = 15 × 0.15 = 2.25W
Worse than full-load power!
```

**2. Foldback current limiting:**

As Vout drops (due to overload), the maximum allowed current also decreases. The characteristic "folds back":

```
Normal: Vout = 12V, IL = 0 to 500mA (normal range)
Overload: Vout = 6V, IL_max = 250mA (reduced!)
Short: Vout = 0V, IL_max = 100mA (minimum short-circuit current)
```

**Why foldback is superior:** At short circuit with foldback:
```
PQ1 = Vin × I_SC_foldback = 15 × 0.1A = 1.5W (less than normal load power!)
```

The transistor is protected even under sustained short circuits.

**Foldback implementation:** Uses a voltage divider sensing Vout to reduce the base voltage of the current-limiting transistor as Vout decreases — the sensing voltage compensates for the output drop, reducing the current limit proportionally.

---

### 3-Pin Voltage Regulators (78XX and 79XX) — In Depth

**78XX series (positive):** Complete series regulator in TO-220 or TO-3 package.

```
               Top view (TO-220 package):
               [Tab: heatsink surface, connected to Vout in 78XX]
                ┌─────────┐
Pin 1 (Input)  ─┤         ├─  Pin 3 (Output)
                │  78XX   │
                └────┬────┘
                Pin 2 (GND)
```

**Standard application circuit:**

```
                C1                    C2
Vin(+) ─────────||──┬──[7805]──┬──────||──── Vout(+5V)
                     │   1  3  2│             │
                     ═══      ═══          [Load]
                     │          │             │
GND ────────────────────────────────────────GND
```

- **C1 = 0.33μF** (ceramic/electrolytic): Input bypass. Prevents oscillation due to lead inductance when regulator is far from the main filter capacitor.
- **C2 = 0.1μF** (ceramic, near the output pin): Improves transient response. Supplies instantaneous current demand before the regulator loop can respond.

**Internal architecture of 78XX:**

```
Vin ──── [Vbe multiplier bias] ──── Pass transistor (Darlington NPN) ──── Vout
                                              │ Base
                                    [Error amplifier]
                                              │
                              [Bandgap voltage reference ~1.25V]
                                              │
                         ┌── [Thermal shutdown comparator] (150°C)
                         ├── [Current limit circuit] (~1.5A for standard)
                         └── [Safe Operating Area protection]
                                              │
                                             GND
```

**Key specifications for 7805:**

| Parameter | Value |
|-----------|-------|
| Output voltage | 5.0V ± 4% |
| Max output current | 1.5A (with heatsink) |
| Min input voltage | 7V (2V dropout) |
| Max input voltage | 35V |
| Line regulation | 3mV (for Vin: 7-25V) |
| Load regulation | 15mV (for IL: 5mA-1.5A) |
| PSRR | 68dB typical |
| Quiescent current | ~5mA |
| Dropout voltage | ~2V |

**Adjustable output (with resistors):**

The 78XX output can be raised above its nominal voltage using an external resistor:

```
              78XX
Vin ──[Pin1]──────[Pin3]──┬── Vout_adjusted
                          R1
          [Pin2]──┬────  Vout_adjusted point
                  R2 (R1 + R2 from output to GND)
                  │
                 GND

Vout_adj = Vnominal + IQ × R1 + (Vnominal/R2) × R1
```

**79XX series (negative regulators):** Pin arrangement is different (Tab connects to input, not output). Pinout: 1=GND, 2=Input(-), 3=Output(-). Use same external capacitors.

---

### IC 723 Voltage Regulator — Complete Design Reference

The LM723 is a general-purpose precision voltage regulator with an externally adjustable output, making it the most flexible linear regulator IC.

**Internal block diagram of IC 723:**

```
               VCC (pin 12)
                 │
         ┌───────┴─────────────────────┐
         │   Reference amplifier       │
         │   (generates Vref = 7.15V)  │
         │             │               │
         │         [Vref output]─── pin 6 (Vref)
         │                             │
         │   Error amplifier           │
         │   (+) input ─── pin 5 (V+) │
         │   (-) input ─── pin 4 (V-) │
         │                             │
         │   Pass transistor (NPN)     │
         │   Collector ─── pin 11 (VC)│
         │   Emitter ─── pin 10 (Vout)│
         │                             │
         │   Current limiter           │
         │   pin 2 (CL), pin 3 (CS)  │
         │                             │
         │   VEE (pin 7, GND)          │
         └─────────────────────────────┘
```

**Pin summary:**

| Pin | Name | Function |
|-----|------|---------|
| 4 | V- | Inverting input of error amplifier (connect to voltage divider sampling Vout) |
| 5 | V+ | Non-inverting input of error amplifier (connect to Vref for low-V mode, or R divider) |
| 6 | Vref | 7.15V reference output (±0.5% stable) |
| 7 | VEE | Negative supply / Ground |
| 10 | Vout | Output terminal (emitter of pass transistor) |
| 11 | VC | Collector of pass transistor — connect to Vin (or to external pass transistor base) |
| 12 | VCC | Positive supply (max 40V) |
| 2 | CL | Current limit — connect via RSC to CS pin (0.7V/RSC = current limit) |
| 3 | CS | Current sense — connect to Vout (RSC measures IL) |

**Low Voltage Regulator (Vout < Vref = 7.15V):**

```
          VCC
           │
         [VC (11)]
         [LM723]
         [Vout (10)]─────────────────── Vout
               │                          │
         [V+ (5)]──[Vref (6)]         [R1]
         [V- (4)]──────────────────────[R2]  ← voltage divider
               │                          │
              GND                        GND

Vout = Vref × R2/(R1+R2)
```

Connect V+ to Vref (pin 6) directly. V- senses the sampled output through R1-R2 voltage divider.

```
Design for Vout = 5V:
R2/(R1+R2) = Vout/Vref = 5/7.15 = 0.699
If R1 = 1.5kΩ: R1+R2 = R1/0.301 = 1.5/0.301 = 4.98kΩ → R2 = 3.48kΩ ≈ 3.3kΩ (use 3.3kΩ + 180Ω in series for precision)
```

**High Voltage Regulator (Vout > Vref = 7.15V):**

```
          VCC
           │
         [VC (11)]
         [LM723]
         [Vout (10)]────────────────── Vout
               │                          │
         [V- (4)]──[Vref (6)]         [R1]  ← R1 from Vout to V- pin
         [V+ (5)]──────────────────────[R2]  ← R2 from V- pin to GND
               │                          │
              GND                        GND

Vout = Vref × (1 + R1/R2)
```

In high-voltage mode: V- is now the summing node. V+ is held at Vref via a resistor from Vref pin.

```
Design for Vout = 12V:
1 + R1/R2 = 12/7.15 = 1.678
R1/R2 = 0.678
Choose R2 = 7.5kΩ → R1 = 0.678 × 7.5 = 5.085kΩ ≈ 5.1kΩ

Also connect: 100pF capacitor from Vout to pin 4 (prevents HF oscillation)
```

**External pass transistor for high current (>150mA):**

IC 723's internal pass transistor handles max 150mA. For higher currents, use external NPN transistor:

```
IC 723 Vout (pin 10) → Base of external NPN (e.g., 2N3055)
IC 723 VC (pin 11) → Collector of external NPN (via heatsink)
External NPN Emitter → Actual output voltage

Current limit: IL(max) = (0.7V / RSC) × β_external
```

---

### DC-to-DC Converters — Theory and Types

Linear regulators can only step DOWN (Vout < Vin) and always waste power. Switching DC-DC converters can step up, step down, or invert.

**Buck Converter (Step-Down):**

```
     L (inductor, energy storage)
Vin ─[S]────(▶)──────┬──── Vout
     switch   │      │
            [D]  freewheeling  [C]    [Load]
             │   diode         │        │
            GND                └────────┘
```

When switch S is ON (duty cycle D = ton/T):
- Energy stored in L: VL = Vin - Vout
- Diode D reverse-biased

When switch S is OFF (1-D fraction):
- L releases energy through freewheeling diode D
- Vout = L's voltage drives current into load

**Output voltage relationship:**
```
Vout = D × Vin   [for ideal buck converter, in continuous conduction mode]

Example: Vin = 12V, D = 0.5 → Vout = 6V
Efficiency can reach 95%!
```

**Boost Converter (Step-Up):**

```
Vin ─────L────┬──[D]──── Vout
              │   │
             [S]  [C]
              │    │
             GND  GND
```

When S is ON: L stores energy (current builds up in L)
When S is OFF: L's stored energy pushes current through D into output cap:

```
Vout = Vin / (1-D)   [for ideal boost converter]

Example: Vin = 5V, D = 0.6 → Vout = 5/(1-0.6) = 12.5V
```

The output is HIGHER than input — this is how phone charger bricks generate the 5V (from 9V Li-ion through a boost), or how LED flashlight drivers boost 1.5V to 3.3V for the LED.

---

### SMPS — Complete Block Diagram and Operation

**SMPS Block Diagram (detailed):**

```
230V AC ─── [EMI Filter] ─── [Bridge Rectifier] ─── [Bulk Capacitor] ─── 325V DC
                                                                              │
                                                                    [HF MOSFET Switch]
                                                                              │
                                                                    [Ferrite Transformer]
                                                                              │
                                                             ┌────────────────┘
                                                             │  Secondary side
                                                    [Schottky Rectifier]
                                                             │
                                                    [LC Output Filter]
                                                             │
                                                           Vout
                                                             │
                                         [Voltage Sense] ──────── [Optocoupler] ────────
                                                                                        │
                                                                       [PWM IC: TL494/UC3842]
                                                                                        │
                                                                         (controls MOSFET gate duty cycle)
```

**Block-by-block function:**

| Block | Function | Key components |
|-------|----------|----------------|
| EMI Filter | Suppresses conducted EMI from/to mains | X capacitors, Y capacitors, common-mode choke |
| Bridge Rectifier | Converts 230V AC → 325V DC (peak) | 4 × 1N4007 or fast diodes |
| Bulk Capacitor | Smooths 100Hz ripple, provides holdup time | 100-470μF, 400V electrolytic |
| HF MOSFET Switch | Chops DC at 20kHz-1MHz, controls energy transfer | IRFP450, STP10NK60Z, etc. |
| Ferrite Transformer | Steps down HF voltage, provides isolation | Ferrite core (not iron — iron saturates at HF) |
| Schottky Rectifier | Fast rectification (must handle HF — 1N4007 too slow) | MBR20200, SR540, etc. |
| LC Filter | Smooths output, reduces switching ripple | 50-200μH + 220-1000μF |
| Optocoupler | Feeds back Vout error signal while maintaining galvanic isolation | PC817, TLP621 |
| PWM IC | Compares feedback with internal reference, adjusts duty cycle | TL494, UC3842, NCP1200 |

**Why ferrite and not iron core transformer?**

Iron core transformers are designed for 50Hz mains. Power loss in a transformer core scales approximately as f^1.6 (Steinmetz equation). At 100kHz (SMPS frequency), an iron core would dissipate 100kHz^1.6 / 50Hz^1.6 = 200,000× more energy than at 50Hz — it would instantly overheat.

Ferrite has very low eddy current losses at HF because of its high resistivity (10⁻² to 10⁶ Ω·m vs 10⁻⁷ Ω·m for iron).

**SMPS vs Linear Regulator — Complete Comparison:**

| Aspect | Linear Regulator | SMPS |
|--------|-----------------|------|
| Efficiency | 30-60% (Vin-Vout wasted as heat) | 75-92% |
| Output voltage vs input | Always Vout < Vin (step-down only) | Step-up, step-down, or invert |
| Output noise | Very low (<0.1mV ripple) | Higher (10-100mV ripple) |
| Transient response | Fast (< 1μs) | Slower (due to L/C delays) |
| Cost/complexity | Simple, few components | Complex, more components |
| EMI generation | None | Significant (must be filtered) |
| Size/weight | Heavy (bulky transformer if AC-DC) | Very compact (HF transformer) |
| Audio circuits | Preferred (noise sensitive) | Needs good filtering |
| Computer PSU | Not used (too inefficient at 200W+) | Universal standard |

---

## 2. Example

### Zener Regulator Design with Load Variation

**Given:** Vin = 15V, VZ = 9.1V, IZ(knee) = 10mA, PZ(max) = 1W, RL varies from 200Ω to ∞ (no load).

**Find Rs and check all conditions:**

**Step 1: Maximum load current**
```
IL(max) = VZ / RL(min) = 9.1 / 200 = 45.5mA
```

**Step 2: Calculate Rs for proper regulation at maximum load**
```
Rs = (Vin - VZ) / (IL(max) + IZ(knee))
   = (15 - 9.1) / (45.5 + 10) mA
   = 5.9 / 55.5 × 10⁻³
   = 106.3Ω → use standard value 100Ω
```

**Step 3: Verify no-load condition**
```
With Rs = 100Ω, no load (IL = 0):
IZ(no-load) = (Vin - VZ) / Rs = 5.9/100 = 59mA

Power in zener: PZ = VZ × IZ = 9.1 × 0.059 = 537mW < 1W ✓

IZ(max) = PZ(max)/VZ = 1W/9.1V = 110mA → 59mA < 110mA ✓
```

**Step 4: Power rating for Rs**
```
PR = (Vin - VZ)² / Rs = 5.9² / 100 = 34.81/100 = 0.35W → use 0.5W resistor
```

**Design: Rs = 100Ω (0.5W), Zener = 9.1V 1W (1N4740)**

---

## 3. Applications and Use Cases

1. **7805 in Arduino:** The Arduino Uno board uses a 7805 (or NCP1117-5.0) to regulate the 7-12V input to +5V for the ATmega328P microcontroller and peripherals.

2. **IC 723 in Laboratory Power Supplies:** Variable bench power supplies (0-30V, 0-3A) use the LM723 as their control element because its output is fully programmable by changing R1/R2 values with a potentiometer.

3. **Buck converter in laptop charger brick:** Modern laptop chargers (45W-140W) use a flyback (buck-derived) SMPS converter to convert 100-240V AC mains to 19-20V DC. Efficiency > 90%.

4. **Boost converter in UPS:** A 12V battery backup UPS converts the battery's 12V DC to 230V AC using a boost converter (12V → 400V DC bus) followed by an inverter bridge.

5. **LDO (Low Dropout) regulators in smartphones:** The power management IC (PMIC) inside every smartphone uses multiple LDO regulators (AMS1117, LP5907) to provide noise-free 1.0V-3.3V rails to the CPU, RAM, and RF circuits from the Li-ion battery's 3.7-4.2V.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Zener Regulator Design [May 2019, Q3]

**Problem:** Design a 5.1V zener regulator for IL = 20mA, Vin = 12V DC, IZ(knee) = 5mA. Find Rs and its power rating. [3 marks]

**Solution:**

**Step 1:** Total current at maximum load:
```
IT = IL + IZ(min) = 20 + 5 = 25mA
```

**Step 2:** Series resistance:
```
Rs = (Vin - VZ) / IT = (12 - 5.1) / 25×10⁻³ = 6.9 / 0.025 = 276Ω → use 270Ω
```

**Step 3:** Power in Rs:
```
PR = (Vin - VZ)² / Rs = 6.9² / 270 = 47.61/270 = 0.176W → use 0.5W resistor
```

**Step 4:** Zener power rating (worst case: no load, all current through zener):
```
IZ(no-load) = (12 - 5.1) / 270 = 25.6mA
PZ(max) = VZ × IZ = 5.1 × 25.6mA = 130mW → use IN4733 (5.1V, 1W) for safety margin
```

**Summary:** Rs = 270Ω (0.5W), Zener = IN4733 (5.1V, 1W)

---

### Example 2: IC 723 Low Voltage Regulator Design [KTU Style]

**Problem:** Design an IC 723 low voltage regulator to produce Vout = 5V regulated output. Also add current limiting for IL(max) = 100mA.

**Solution:**

**Step 1:** Voltage divider at V+ input (pins 5 and 6):

For low-voltage mode (Vout < Vref = 7.15V):
```
Vout = Vref × R2/(R1+R2)
5 = 7.15 × R2/(R1+R2)
R2/(R1+R2) = 5/7.15 = 0.699
1-0.699 = 0.301 → R1/(R1+R2) = 0.301
R1/R2 = 0.301/0.699 = 0.431

Choose R2 = 10kΩ:
R1 = 0.431 × 10kΩ = 4.31kΩ → use 4.3kΩ (standard)
```

**Verification:**
```
Vout = 7.15 × 10/(4.3+10) = 7.15 × 10/14.3 = 7.15 × 0.699 = 5.0V ✓
```

**Step 2:** Current limiting resistor:
```
RSC = 0.7V / IL(max) = 0.7 / 0.1 = 7Ω → use 6.8Ω (standard)
```

**Step 3:** Stability capacitor:
```
Connect 100pF from Vout (pin 10) to pin 4 (V-) for oscillation prevention
```

**Final values:**
- R1 = 4.3kΩ, R2 = 10kΩ → Vout = 5V
- RSC = 6.8Ω → IL(max) = 0.7/6.8 = 103mA ≈ 100mA ✓

---

### Example 3: 78XX Power Dissipation and Heatsink Requirement [KTU Style]

**Problem:** A 7812 regulator supplies 500mA at 12V. The input is 18V DC. Calculate: (a) Power dissipated in the IC, (b) whether a heatsink is needed if ambient temperature is 25°C and Pd(max) without heatsink = 625mW.

**Solution:**

**(a) Power dissipated:**
```
Pd = (Vin - Vout) × IL = (18 - 12) × 0.5 = 6 × 0.5 = 3W
```

**(b) Heatsink required?**

Without heatsink: Pd(max) = 625mW = 0.625W
Actual dissipation = 3W >> 0.625W → **Heatsink is absolutely required!**

Heatsink thermal resistance calculation:
```
Maximum junction temperature for 7812: Tj(max) = 125°C
Internal thermal resistance (junction to case): θjc ≈ 5°C/W (TO-220 package)

Total thermal resistance allowed:
θtotal = (Tj(max) - Tambient) / Pd = (125 - 25) / 3 = 100/3 = 33.3°C/W

Required heatsink thermal resistance:
θheatsink = θtotal - θjc = 33.3 - 5 = 28.3°C/W

Choose heatsink with θ ≤ 28°C/W
```

A standard small aluminum heatsink (e.g., Fischer SK 18 series) provides ~15°C/W — suitable for this application.

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q2]: Draw and explain 78XX IC voltage regulator. [3 marks]

**Complete Solution:**

The 78XX series are 3-terminal positive linear voltage regulators in a single IC package.

**Circuit:**
```
           C_in (0.33μF)    Pin 1 (Input)─────────────────Pin 3 (Output)
Vin(DC) ────────||─────────────[        ]──────────────────────────── Vout
                               [  78XX  ]
                               [        ]─── Pin 2 (GND) ──────────── GND
                                                │
                                            C_out (0.1μF)
                                                │
                                               GND
```

**Pinout:** Pin 1 = Input, Pin 2 = Ground, Pin 3 = Output.

**Internally it contains:**
- Temperature-stable bandgap voltage reference (1.25V)
- Differential error amplifier
- NPN Darlington pass transistor
- Thermal shutdown (activates at 150°C junction temp)
- Short-circuit current protection (~1.5A limit)
- Safe Operating Area (SOA) protection

**Why two capacitors?**
- **Cin (0.33μF):** Prevents oscillation by decoupling lead inductance from the main filter capacitor. Especially important when the main capacitor is more than 10cm away.
- **Cout (0.1μF):** Improves transient response — provides instantaneous current for fast load steps while the regulator's feedback loop responds.

**Common types:** 7805 (+5V), 7809 (+9V), 7812 (+12V), 7815 (+15V). Output current up to 1.5A with heatsink.

---

### PYQ 2 [May 2019, Q6b]: Draw and explain series voltage regulator. [5 marks]

**Complete Solution:**

**Circuit (transistor series regulator with error amplifier):**

```
   VCC (unregulated, 15V)
          │
        ┌─┴─┐
        │Q1 │ ← NPN series pass transistor (2N3055 or similar power transistor)
        └─┬─┘
          │Emitter
          ├─────────────────── Vout (regulated ~12V)
          │                          │
     Base─┴─[RC]─[Q2 Collector]   [R1] ← sampling divider
                  [Q2  NPN    ]   [R2]
                  [Q2 Emitter]─┬──┘
                               │
                             ─|← Zener (VZ = reference)
                               │
                              GND
```

**Operation:**

1. **Reference**: Zener diode sets VZ = stable reference (e.g., 5.1V). This holds Q2's emitter at VZ.

2. **Error Amplifier (Q2)**: Q2's base is driven by Vsense = Vout × R2/(R1+R2). The difference between Vsense and VZ is amplified by Q2.

3. **Pass transistor (Q1)**: Q1 acts as an emitter follower in series with the load. Its base is driven by Q2's collector. Q1 drops (Vin - Vout) volts — the "excess" voltage is absorbed as heat in Q1.

4. **Negative feedback loop**:
   ```
   Vout ↑ → Vsense ↑ → VBE(Q2) ↑ → IC(Q2) ↑ → VC(Q2) ↓ → IB(Q1) ↓ → Q1 less ON
   → VCE(Q1) ↑ → Vout ↓ (corrected back)
   ```

5. **Output voltage**:
   ```
   Vout = Vref × (1 + R1/R2) = (VZ + VBE(Q2)) × (1 + R1/R2)
   ≈ VZ × (1 + R1/R2)   [since VBE is constant and small compared to VZ]
   ```

**Advantages over zener-only regulator:**
- Much higher output current (Q1 can carry amperes; zener limited to ~mA)
- Better regulation (active error amplifier loop vs zener dynamic resistance alone)
- Adjustable output (change R1/R2 ratio)

---

### PYQ 3 [May 2019, Q7b]: Draw SMPS block diagram and explain. [5 marks]

**Complete Solution:**

**SMPS Block Diagram:**
```
         ┌────────────┐     ┌────────────┐     ┌─────────────┐     ┌──────────────┐
AC ──────►  EMI       ├────►Input        ├────►High-frequency├────►Ferrite        │
Mains    │  Filter    │     │Rectifier   │     │Switch       │     │Transformer    │
230V/50Hz└────────────┘     │+ Bulk Cap  │     │(MOSFET/IGBT)│     └──────┬───────┘
                             └────────────┘     └─────────────┘            │
                                                       ▲                    │
                                                       │             ┌──────▼────────┐
                                                 ┌─────┴──────┐     │Output Rectifier│
                                                 │PWM Control │     │+ LC Filter     │
                                                 │(Duty cycle)│     └──────┬─────────┘
                                                 └─────▲──────┘            │
                                                       │                    │Vout
                                                 ┌─────┴──────┐            │
                                                 │Optocoupler │◄───────────┘
                                                 │(isolation) │
                                                 └────────────┘
```

**Block functions:**

1. **EMI Filter**: X-capacitors across line and neutral suppress differential-mode noise; Y-capacitors from line/neutral to chassis suppress common-mode noise. Prevents SMPS switching noise from entering the AC grid.

2. **Input Rectifier + Bulk Capacitor**: Full-wave bridge rectifier + 100-470μF/400V electrolytic capacitor converts 230V AC to ~325V DC with low ripple.

3. **High-frequency Switch (MOSFET)**: N-channel power MOSFET (switching at 50-400kHz) chops the 325V DC. Duty cycle D controls energy transfer per switching cycle.

4. **Ferrite Transformer**: Operates at switching frequency. Ferrite core has low eddy current losses at HF. Steps down voltage and provides safety isolation between mains and output.

5. **Output Rectifier + LC Filter**: Schottky diodes (fast switching, low forward drop) rectify the transformer secondary. Inductor + electrolytic capacitor smooth the output to DC.

6. **Feedback via Optocoupler**: The optocoupler carries the error signal across the isolation barrier. Vout is compared to a reference (e.g., by TL431 shunt regulator on secondary); error drives the LED in the optocoupler.

7. **PWM Controller (TL494/UC3842)**: Receives feedback, compares to internal reference, adjusts duty cycle to correct Vout:
   - If Vout drops: increase duty cycle → more energy per cycle → Vout rises
   - If Vout rises: decrease duty cycle → less energy → Vout falls

**Why SMPS is preferred over linear for computers/chargers:**
- 200W computer PSU: SMPS efficiency 85% dissipates only 35W as heat; linear regulator at same power would dissipate 70-100W.
- Phone charger: SMPS with ferrite transformer fits in a 30g plug; equivalent 50Hz transformer would weigh 500g.
