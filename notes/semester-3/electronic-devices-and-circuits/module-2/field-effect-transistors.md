# Field Effect Transistors (JFET and MOSFET)

## 1. Explanation

### Core Intuition: Voltage-Controlled Current Source

The **Field Effect Transistor (FET)** is a voltage-controlled device, fundamentally different from the BJT (Bipolar Junction Transistor). In a BJT, a small **base current** controls a large **collector current** (current-controlled current source). In a FET, a small **gate voltage** controls a large **drain current** (voltage-controlled current source) while drawing essentially **zero gate current**.

This zero-gate-current property is revolutionary: FETs have input impedances of 10⁸ to 10¹⁵ Ω, making them ideal for amplifying signals from high-impedance sources (microphones, pH sensors, electrometer circuits) without loading the source.

**Two main categories:**
1. **JFET (Junction FET)**: Gate is a reverse-biased p-n junction; operates by depletion of channel only
2. **MOSFET (Metal-Oxide-Semiconductor FET)**: Gate is insulated by SiO₂; can operate in both depletion and enhancement modes

### JFET — Structure and Operation

**N-channel JFET structure:**
```
Gate (G) ─── [P-type gate region]
              ↓ ↓ ↓ (depletion region controlled by VGS)
Source (S) ─[N-type channel]─ Drain (D)
```

**Three terminals:**
- **Source (S)**: Where carriers (electrons for N-channel) enter
- **Drain (D)**: Where carriers exit (conventional current flows from D to S in N-channel)
- **Gate (G)**: Controls channel width via electric field (reverse biased junction)

**Physical operation mechanism:**

The P-type gate forms a p-n junction with the N-type channel. When reverse bias VGS is applied:
1. Depletion region expands into the channel
2. The depletion region contains no free carriers → effectively narrows the channel width
3. Narrower channel → higher resistance → lower drain current ID

**Key equations:**

**Drain current (active/saturation region):**
```
ID = IDSS × (1 - VGS/VP)²

Where:
- IDSS = drain-to-source saturation current (when VGS = 0)
- VP = pinch-off voltage (negative for N-channel, e.g., VP = -4V)
- VGS ranges: 0 to VP (0 to -4V for N-channel)
```

**Regions of operation:**
- **Ohmic/Linear region**: VDS < |VP| + VGS. Channel not pinched off; behaves as voltage-controlled resistor.
- **Saturation/Active region**: VDS ≥ |VP| + VGS. Channel pinched off; ID is approximately constant (controlled by VGS only). Amplifier operation uses this region.
- **Cutoff region**: VGS ≤ VP. Channel fully depleted; ID ≈ 0.

**JFET Characteristics curves:**
- **Output characteristics (ID vs VDS)**: Family of curves for different VGS values, showing linear and saturation regions
- **Transfer characteristics (ID vs VGS)**: Parabolic curve from IDSS (at VGS=0) to 0 (at VGS=VP)

### BJT vs JFET Comparison

| Parameter | BJT | JFET |
|-----------|-----|------|
| Type | Current-controlled | Voltage-controlled |
| Control signal | Base current IB | Gate voltage VGS |
| Input impedance | Low (kΩ) | Very high (100MΩ+) |
| Noise | Higher | Lower |
| Gain | High gm (transconductance) | Moderate gm |
| Frequency response | Wide bandwidth | Moderate |
| Thermal stability | Poor (ICBO doubles per 10°C) | Better (ID decreases with temp) |
| Applications | High-gain amplifiers, switching | Low-noise preamps, analog switches |
| Gate current | Yes (IB flows) | Essentially zero |
| Polarity types | NPN, PNP | N-channel, P-channel |

### MOSFET — Structure, Enhancement and Depletion Types

The MOSFET uses an oxide-insulated gate (no direct electrical contact to channel). The gate is a metal (or polysilicon) electrode separated from the semiconductor by a thin SiO₂ (silicon dioxide) layer.

**Enhancement-type MOSFET (E-MOSFET):**

No channel exists at VGS = 0. Applying a positive VGS (for N-channel) **induces** (creates) a conducting channel.

**Structure:**
```
     Gate (G) metal
         ↓
  ┌─ SiO₂ insulator ─┐
  │N+ Source  │ P-substrate │ N+ Drain │
  S                              D
```

**Operation:**
- VGS = 0: No channel → ID = 0 (device is OFF)
- VGS > VT (threshold): Positive gate voltage repels holes from surface, attracts electrons → inversion layer forms → N-channel created between N+ source and drain → current flows
- VGS >> VT: Wide channel, large ID

**Key equation (saturation region):**
```
ID = K × (VGS - VT)²

Where:
K = (μn × Cox × W) / (2L)   [process-dependent constant]
VT = threshold voltage (typically 1-5V for N-channel enhancement MOSFET)
W = channel width, L = channel length
```

**Depletion-type MOSFET (D-MOSFET):**

A physical channel IS implanted at fabrication (doped N-type material between S and D). The device conducts at VGS = 0.

**Operation:**
- VGS = 0: Drain current IDSS flows through the implanted channel
- VGS negative (depletion mode): Repels electrons from channel → reduces ID
- VGS positive (enhancement mode): Attracts more electrons → increases ID beyond IDSS
- Acts like a JFET for negative VGS, but can also be driven positive unlike JFET

**Comparison: Enhancement vs Depletion MOSFET:**

| Feature | Enhancement MOSFET | Depletion MOSFET |
|---------|-------------------|-----------------|
| Channel at VGS=0 | No (induced only) | Yes (implanted) |
| Normal state | OFF | ON |
| VGS range | Positive only (N-ch) | Both ±VGS |
| Symbol | Arrow pointing inward (N-ch) | Arrow pointing outward |
| VT threshold | Positive (N-ch) | Negative (N-ch, ~VP) |
| Application | Digital logic (CMOS) | Analog switches, depletion-load circuits |

---

## 2. Example

### JFET Drain Current Calculation

**Given:** JFET with IDSS = 10mA, VP = -4V. Find ID at VGS = -2V.

```
ID = IDSS × (1 - VGS/VP)²
   = 10 × (1 - (-2)/(-4))²
   = 10 × (1 - 0.5)²
   = 10 × (0.5)²
   = 10 × 0.25
   = 2.5 mA
```

---

## 3. Applications and Use Cases

1. **MOSFET in CMOS Digital Logic**: Every microprocessor, memory chip, and FPGA uses complementary MOSFET (CMOS) pairs — one N-channel and one P-channel per logic gate. The CMOS inverter draws current only during switching, enabling extremely low standby power.

2. **JFET in Low-Noise Amplifiers**: Audio preamplifiers, scientific instruments, and radio front-ends use JFETs for their low noise figure. The first stage of a condenser microphone preamp is typically a JFET follower.

3. **Power MOSFETs in Motor Drivers**: N-channel enhancement MOSFETs (IRF540, IRFZ44N) in H-bridge configurations drive DC motors, stepper motors, and solenoids with high efficiency.

4. **MOSFET as Analog Switch**: For audio routing, multiplexer circuits (CD4066), JFET and MOSFET analog switches connect/disconnect signal paths without mechanical contacts.

5. **MOSFET in Power Supplies (SMPS)**: High-speed switching in SMPS uses MOSFETs (IRF840, STP20NF20) because of fast switching and low on-resistance (RDS(on) < 100mΩ).

---

## 4. Solved Numerical/Analytical Examples

### Example 1: JFET Transfer Characteristic and Bias Point [May 2019, Q5b]

**Problem:** With the help of characteristic curves, explain the principle of operation of a Junction Field Effect Transistor. Mark its regions of operation on the curve. [6 marks]

**Solution:**

**JFET (N-channel) Characteristic Curves:**

**Output Characteristic (ID vs VDS for various VGS):**

```
ID (mA)
  10 │────────────────── VGS = 0V (IDSS = 10mA)
     │    ╱─── saturation region
   8 │───╱─────────────── VGS = -1V
     │  ╱
   5 │─╱──────────────── VGS = -2V
     │╱
   2 │╱──────────────── VGS = -3V
     │
   0 ├──────────────────────────── VDS
     0     1    2     Vp(sat) ...
           ↑Linear↑ ↑Saturation region↑    ↑Breakdown
```

**Regions labeled on curve:**

1. **Ohmic/Linear Region** (VDS < VGS - VP): 
   - Left of the pinch-off locus
   - JFET acts as a voltage-controlled resistor
   - ID rises linearly with VDS
   - Used in: voltage-controlled resistor (VCR) applications

2. **Saturation/Active Region** (VDS ≥ VGS - VP):
   - Right of pinch-off locus; ID is nearly constant
   - ID controlled by VGS only, independent of VDS
   - Used for **amplification** (most important region)
   - The pinch-off occurs when: channel is fully depleted at drain end

3. **Pinch-off Voltage (VP)**: At VGS = 0, pinch-off begins at VDS = |VP|.

4. **Cutoff Region** (VGS ≤ VP):
   - Gate reverse bias exceeds pinch-off → channel fully depleted → ID ≈ 0
   - JFET is "OFF"

**Transfer Characteristic (ID vs VGS at constant VDS in saturation):**
```
ID (mA)
  10 ●  (IDSS at VGS = 0)
     │ ╲ (parabolic curve)
   5 │   ╲
     │     ╲
   0 └─────●──────── VGS (V)
    -4  -3  -2  -1   0
      ↑VP=-4V
```

Equation: ID = 10 × (1 - VGS/(-4))² = 10 × (1 + VGS/4)²

At VGS = -2V: ID = 10 × (1 - 2/4)² = 10 × 0.25 = 2.5mA

---

### Example 2: Enhancement MOSFET Drain Current

**Problem:** An N-channel E-MOSFET has VT = 2V and K = 0.5mA/V². Find ID at VGS = 5V and VGS = 3V.

**Solution:**

At VGS = 5V (saturation, assuming VDS > VGS - VT = 3V):
```
ID = K × (VGS - VT)² = 0.5 × (5 - 2)² = 0.5 × 9 = 4.5mA
```

At VGS = 3V:
```
ID = 0.5 × (3 - 2)² = 0.5 × 1 = 0.5mA
```

At VGS = 2V (= VT):
```
ID = 0.5 × (2 - 2)² = 0  (device just at threshold)
```

---

### Example 3: BJT vs JFET Comparison Analysis [May 2019, Q10]

**Problem:** Compare BJT and FET. [3 marks]

**Complete Answer:**

| Parameter | BJT | FET (JFET/MOSFET) |
|-----------|-----|---------------------|
| Control mechanism | Current (IB controls IC) | Voltage (VGS controls ID) |
| Input impedance | Low: 1kΩ-100kΩ | Very high: 10⁷-10¹⁵ Ω |
| Gate/base current | IB required (typically μA-mA) | IG ≈ 0 (MOSFET) or nA (JFET) |
| Noise | Higher (shot noise in junctions) | Lower (no minority carriers in gate) |
| Temperature stability | Less stable (ICBO doubles per 10°C) | More stable (ID decreases with temperature) |
| Fabrication density | Lower (larger die area per device) | Higher (MOSFET allows smallest geometry: <5nm!) |
| Applications | High-gain amplifiers, BJT logic | CMOS logic, LNA, power switching |
| Transconductance gm | High | Moderate |
| Power switching speed | Slower (due to charge storage) | Faster (majority carrier, no storage time) |

**Key conclusion:** FETs are the preferred choice in modern VLSI (billion transistors on a chip) due to their voltage-control, negligible gate current, and superior scalability. BJTs excel in discrete high-frequency RF amplifiers and precision analog circuits.

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q5b]: With the help of characteristic curves, explain the principle of operation of a JFET. Mark its regions of operation. [6 marks]

**Complete Solution:** *(Full solution with curves provided in Solved Example 1 above, restated here for self-containment)*

**N-channel JFET Principle:**

A JFET uses a reverse-biased gate junction to **deplete** the conducting channel, controlling drain current. The P-gate forms a p-n junction with the N-channel. Increasing reverse bias (more negative VGS for N-channel) widens the depletion region into the channel, reducing current-carrying cross-section.

**Operating principle step-by-step:**
1. With VGS = 0, VDS applied: N-channel conducts freely. ID = IDSS.
2. As VGS decreases (becomes more negative): Gate depletion region expands → channel narrows → resistance increases → ID decreases following ID = IDSS(1 - VGS/VP)².
3. At VGS = VP (pinch-off voltage, e.g., -4V): Channel fully depleted → ID → 0.
4. For fixed VGS in saturation: Increasing VDS beyond the saturation voltage (VDS,sat = VGS - VP) does NOT significantly increase ID — the channel is pinched off at the drain end, and the device acts as a current source.

**Regions on ID-VDS curves:**

| Region | Condition | Behavior |
|--------|-----------|----------|
| Linear/Ohmic | VDS < VGS - VP | Controlled resistor, ID rises with VDS |
| Pinch-off/Saturation | VDS ≥ VGS - VP | ID nearly constant, amplifier operates here |
| Cutoff | VGS ≤ VP | ID ≈ 0, switch OFF |
| Breakdown | VDS > BVDSS | Avalanche breakdown, avoid |

### PYQ 2 [May 2019, Q10]: Compare BJT and FET. [3 marks]

**Complete Solution:** *(See Solved Example 3 above — fully self-contained answer)*

The key comparisons are:
- BJT: current-controlled, low input Z, higher noise
- FET: voltage-controlled, very high input Z (especially MOSFET with SiO₂ gate insulation), lower noise, better for VLSI
- FETs are majority-carrier devices (faster switching, no minority carrier storage delay)
- BJTs have higher transconductance per unit area in discrete form
