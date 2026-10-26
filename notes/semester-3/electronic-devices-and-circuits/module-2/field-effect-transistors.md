# Field Effect Transistors (JFET and MOSFET)

## 1. Explanation

### Core Intuition: Voltage-Controlled Current Source

The **Field Effect Transistor (FET)** is a **majority carrier, voltage-controlled device**. This is the single most important distinction from the BJT.

In a BJT: a small **base current** IB controls a large **collector current** IC → *current-controlled current source (CCCS)*.
In a FET: a small **gate-to-source voltage** VGS controls a large **drain current** ID → *voltage-controlled current source (VCCS)*.

The gate draws essentially **zero current** (reverse-biased junction for JFET, oxide-insulated gate for MOSFET). This gives FETs an input impedance of 100 MΩ to 10¹⁵ Ω — compared to a BJT's few kΩ. This property makes FETs indispensable wherever the circuit must NOT load the signal source:

- pH sensor output (high source impedance: 100MΩ)
- Electret microphone (high source impedance)
- First-stage amplifier of oscilloscope probes

**Two main FET families:**

| Family | Mechanism | Gate isolation | VGS polarity |
|--------|-----------|---------------|-------------|
| JFET | Depletion of channel by reverse-biased junction | p-n junction | Reverse only (VGS ≤ 0 for N-ch) |
| MOSFET (E-type) | Induction of channel by electric field | SiO₂ oxide | Forward (VGS > VT) for N-ch |
| MOSFET (D-type) | Depletion or enhancement of existing channel | SiO₂ oxide | Both positive and negative |

---

### JFET — Detailed Structure and Physical Operation

**N-channel JFET physical structure:**

```
         Gate (G) ── [P+ region top]
                          ↓  (depletion region expands here)
Source (S) ─────── [N-type channel] ────── Drain (D)
                          ↑  (depletion region expands here)
         Gate (G) ── [P+ region bottom]  ← (both gates tied together internally)
```

The n-type semiconductor bar (the channel) is sandwiched between two p-type gate regions. The gate forms a **p-n junction** with the channel. Under normal operation, this junction is **always reverse biased** (VGS ≤ 0 for N-channel).

**Why reverse-biased gate?**
- Forward biasing the gate would cause gate current to flow (like a forward-biased diode) → input impedance drops dramatically.
- Reverse bias creates a depletion region with no free carriers → high impedance → zero gate current.

**Physical operation mechanism (step by step):**

1. **VGS = 0, VDS applied:** Current flows through N-channel from drain to source (conventional current, electrons flow source to drain). Channel is widest → maximum ID = IDSS.

2. **VGS = negative value (e.g., -2V) for N-channel:** The reverse bias on the gate widens the depletion region into the channel. Effective channel width narrows → increased channel resistance → reduced ID.

3. **VGS = VP (pinch-off voltage, e.g., -4V):** Depletion regions from top and bottom gates meet in the middle — channel is fully pinched off. ID → 0.

4. **VDS increases at fixed VGS:** Initially, as VDS increases, ID increases proportionally (ohmic region). As VDS approaches |VP + VGS|, the channel near the drain end pinches off. Beyond this point, ID saturates (becomes approximately constant) — this is the **saturation region**.

**Key insight on saturation:** Even though the channel is "pinched off" near the drain, electrons are still swept across the depletion region by the electric field → current continues flowing, but it's now limited by the VGS-controlled channel conductance at the source end.

### JFET Characteristic Equations

**Shockley's equation (Drain current in saturation/active region):**
```
ID = IDSS × (1 - VGS/VP)²

Where:
  IDSS = Drain-to-Source Saturation current (at VGS = 0), typically 1-20mA
  VP   = Pinch-off voltage (negative for N-ch, e.g., VP = -4V)
  VGS  = Gate-to-Source voltage (0 to VP range for N-ch)
```

**Boundary between ohmic and saturation:**
```
VDS(sat) = VGS - VP = VGS - VP

Example (VP = -4V, VGS = -1V):
VDS(sat) = -1 - (-4) = 3V  → saturation starts at VDS = 3V
```

**Transconductance (gm) — the key amplifier parameter:**
```
gm = ΔID/ΔVGS = -2×IDSS/VP × (1 - VGS/VP)   [differentiate Shockley's equation]

At VGS = 0: gm0 = 2×IDSS/|VP|   (maximum transconductance)
At any VGS: gm = gm0 × (1 - VGS/VP) = gm0 × √(ID/IDSS)

Example: IDSS = 8mA, VP = -4V
gm0 = 2 × 8mA / 4 = 4mA/V (4000 μS)
At VGS = -2V: gm = 4mA/V × (1 - (-2)/(-4)) = 4 × 0.5 = 2mA/V
```

**Channel resistance in ohmic region:**
```
rd = 1/gm (approximate)

More accurately: rds = VP / (2 × IDSS × (1 - VGS/VP))
```

### JFET Characteristic Curves

**1. Output Characteristics (ID vs VDS):**

```
ID (mA)
  ↑
8 │●── VGS = 0V (ID = IDSS = 8mA, flat line in saturation)
6 │●── VGS = -1V
4 │●── VGS = -2V
2 │●── VGS = -3V
0 │●── VGS = -4V = VP (ID ≈ 0)
  └──────────────────────────────→ VDS
        ohmic │  saturation region (flat, current controlled by VGS)
```

Each curve shows:
- **Ohmic region** (left of knee): ID rises steeply with VDS — FET acts as voltage-controlled resistor. Used as analog switch or VCR (voltage-controlled resistor).
- **Saturation region** (right of knee): ID ≈ constant at IDSS×(1-VGS/VP)². This is the amplifier region.
- **Breakdown** (far right): Avalanche breakdown if VDS exceeds BVdss rating.

**2. Transfer Characteristics (ID vs VGS):**

```
ID (mA)
  ↑
8 │●   (VGS = 0, ID = IDSS = 8mA)
6 │  ●
4 │    ●   ← Parabolic curve (from Shockley's equation)
2 │      ●
0 │────────●──── VP = -4V
  └──────────────→ VGS (V)
        -4  -3  -2  -1   0
```

The transfer characteristic is a **parabola** (quadratic in VGS). This is why small-signal analysis uses gm (derivative of the parabola at the Q-point).

---

### BJT vs JFET — Detailed Comparison

| Parameter | BJT (NPN) | N-channel JFET |
|-----------|-----------|----------------|
| Control mechanism | Base current IB | Gate voltage VGS |
| Input impedance | Low, ~1-10kΩ | Very high, ~100MΩ-1GΩ |
| Gate/Base current | IB = IC/β (significant) | IG ≈ 1nA (negligible) |
| Output current | IC = β × IB | ID = IDSS×(1-VGS/VP)² |
| Transfer characteristic | Linear (IC vs IB) | Parabolic (ID vs VGS) |
| Transconductance gm | High (gm = IC/VT = IC/26mV) | Moderate (gm = 2IDSS/|VP|) |
| Noise figure | Higher (shot noise from IB) | Lower (no base shot noise) |
| Thermal stability | Poor (ICBO doubles/10°C) | Better (ID decreases with temp) |
| Speed (fT) | Higher (for same device) | Moderate for JFET |
| Fabrication | Simpler (for discrete) | More complex |
| Analog switch performance | Moderate Rce | Excellent (low Ron, high Roff ratio) |
| VGS range | 0.7V (only forward VBE) | 0 to VP (variable reverse bias) |
| Voltage amplifier (Av) | Very high (-gm×RC, large gm) | Moderate (-gm×RD) |

**When to use FET over BJT:**
- High input impedance required (sensor amplifiers, oscilloscope probes)
- Low noise required (LNA — Low Noise Amplifier)
- Analog switch applications (FET is bidirectional, BJT is not)
- Very high input frequency with CMOS technology

---

### MOSFET — Metal-Oxide-Semiconductor FET

The MOSFET gate is completely isolated from the channel by a thin layer of silicon dioxide (SiO₂), 10-100nm thick. This oxide layer acts as a capacitor between the metal gate and the semiconductor. No direct electrical connection — hence the extremely high input impedance (10¹²-10¹⁵ Ω).

#### Enhancement-Type MOSFET (E-MOSFET) — N-Channel

**Physical Structure:**
```
Gate (G) ──── Metal plate
              SiO₂ insulator (10-100nm)
              P-type substrate (body/bulk)
         ↑                     ↑
Source (S) [N+ region]   [N+ region] Drain (D)
              P-type body connects to Source (for 3-terminal device)
```

**Key characteristic: No channel exists at VGS = 0.**

The P-type body separates the two N+ regions. Without a gate voltage, the only path from source to drain is through two back-to-back p-n junctions — no current flows regardless of VDS.

**Channel induction mechanism:**

When a **positive VGS** is applied:
1. The positive gate voltage attracts electrons from the P-type body toward the gate
2. Holes are repelled away from the surface into the bulk
3. A thin **inversion layer** of electrons forms at the silicon-oxide interface
4. This inversion layer IS the N-channel, connecting Source to Drain
5. When VGS > VT (threshold voltage, typically +2V to +4V for N-channel): channel is formed → current can flow

```
Threshold voltage concept:
VGS < VT: No channel (cutoff) → ID = 0
VGS > VT: N-channel forms → ID flows (proportional to (VGS - VT)²)
```

**E-MOSFET Drain Current (Saturation Region):**
```
ID = K × (VGS - VT)²

Where:
K = process transconductance parameter (A/V²), depends on device geometry and oxide thickness
VT = threshold voltage (positive for N-channel enhancement type)
VGS must exceed VT for any drain current

Saturation condition: VDS ≥ VGS - VT
```

**E-MOSFET Symbol:**

```
      D ──┐
          │  (broken line = no channel at VGS=0)
      G ─┤  
          │
      S ──┘── B (body, usually tied to source in discrete devices)
```

The broken line in the symbol represents the induced (non-permanent) channel.

**E-MOSFET Transfer Characteristic:**
```
ID (mA)
↑
│            ●
│          ●
│        ●
│      ●
│    ●
│  ● (starts at VT, increases as (VGS-VT)²)
0───────●────────────────→ VGS
        VT  (e.g., +3V)
```

Starts at VT (not at VGS = 0 like JFET). Only conducts when VGS > VT.

#### Depletion-Type MOSFET (D-MOSFET) — N-Channel

**Physical Structure:**
```
Gate (G) ──── Metal plate
              SiO₂ insulator
              N-channel (physically exists, built-in during fabrication!)
         ↑                     ↑
Source (S) [N+ region]   [N+ region] Drain (D)
              P-type substrate
```

**Key characteristic: A physical N-channel EXISTS at VGS = 0.**

During fabrication, n-type impurities are diffused into the P-body between source and drain, creating a permanent channel. At VGS = 0, the device is **already ON**.

**Operation in two modes:**

**Depletion mode (VGS negative for N-channel):**
- Negative VGS repels electrons from the channel → channel narrows → ID decreases
- Behaves like JFET in this region
- At VGS = VP (negative pinch-off): channel depleted → ID → 0

**Enhancement mode (VGS positive for N-channel):**
- Positive VGS attracts more electrons into the channel → channel widens → ID increases beyond IDSS
- **This is unique to D-MOSFET** — JFET cannot have positive VGS (would forward-bias gate junction)!

**D-MOSFET Drain Current:**
```
Same as JFET (Shockley's equation, since built-in channel):
ID = IDSS × (1 - VGS/VP)²   [valid for VGS from VP (negative) to positive values]

At VGS = 0: ID = IDSS (same as JFET)
At VGS > 0: ID > IDSS (enhanced mode, unique to D-MOSFET)
At VGS = VP: ID = 0 (depleted mode)
```

**D-MOSFET Symbol:**
```
      D ──┐
          │  (solid line = permanent channel at VGS=0)
      G ─┤  
          │
      S ──┘── B
```

The **solid line** between drain and source in D-MOSFET symbol vs. **broken line** in E-MOSFET symbol is the key visual distinction.

**D-MOSFET Transfer Characteristic:**
```
ID (mA)
↑
│
│●  ← Enhanced region (VGS > 0, ID > IDSS)
IDSS ─●── (VGS = 0)
│  ●    ← Depleted region (VGS < 0, ID < IDSS)
│    ●
│      ●
0────────●──────→ VGS
         VP (negative)
```

The curve crosses VGS = 0 at ID = IDSS, and extends BOTH directions (unlike JFET which only depletes, and E-MOSFET which only starts at VT).

---

### MOSFET Biasing

**E-MOSFET biasing:**

Since VGS must be positive (N-channel) and the device has no IDSS reference:

```
Voltage divider bias (most common):

VDD ─── R1 ──┬── Gate
             R2    │
             │  [E-MOSFET]
            GND   │
                  RD (drain)
                  RS (source)

VGS = VDD × R2/(R1+R2) [must be > VT]
ID = K(VGS - VT)²
VDS = VDD - ID(RD + RS)
```

**D-MOSFET biasing:**

Can use zero-bias (VGS = 0, simplest!) since IDSS exists:

```
VDD ─── RD ──── Drain
         │
    Gate ─ 0V (ground through RG)
         │
        Source ── RS (optional) ── GND
```

With VGS = 0: ID = IDSS directly. This is the simplest possible bias!

---

### Comparison: JFET vs E-MOSFET vs D-MOSFET

| Parameter | N-ch JFET | N-ch E-MOSFET | N-ch D-MOSFET |
|-----------|-----------|---------------|---------------|
| Channel at VGS=0 | Yes (built-in) | No (must induce) | Yes (built-in) |
| Gate input | Reverse-biased junction | Oxide-insulated | Oxide-insulated |
| Input impedance | 100MΩ-1GΩ | 10¹²-10¹⁵ Ω | 10¹²-10¹⁵ Ω |
| VGS operating range | VP to 0 (negative only) | VT to +VDD (positive) | VP to +VDD (both) |
| Current at VGS=0 | IDSS | 0 | IDSS |
| ID equation | IDSS(1-VGS/VP)² | K(VGS-VT)² | IDSS(1-VGS/VP)² |
| Zero-bias operation | At max ID = IDSS | Not possible | Yes (VGS=0, ID=IDSS) |
| Gate damage risk | Cannot forward bias | Sensitive to static | Sensitive to static |
| Typical applications | LNA, analog switch, VCR | CMOS logic, power FET | RF amplifiers |
| Symbol channel line | None (space implied) | Broken | Solid |

---

### ESD (Electrostatic Discharge) Protection

MOSFET gates (SiO₂ layer ~10nm) are extremely sensitive to static electricity. A discharge of even 100V (easily generated by walking on carpet) can permanently destroy the gate oxide, causing a short or open circuit.

**Precautions:**
- Handle MOSFETs with anti-static wrist strap and ESD mat
- Store in conductive foam or shorted shipping tubes
- IC designers include on-chip ESD protection diodes (but these limit input voltage range)

JFETs are less sensitive since the gate is a p-n junction (more robust than oxide).

---

## 2. Example

### Finding the Q-point for a JFET Circuit

**Given:** N-channel JFET with IDSS = 10mA, VP = -5V. Self-bias circuit: RS = 500Ω, RD = 1kΩ, VDD = 15V.

**Step 1: Write the self-bias equation**

In JFET self-bias: VGS = -ID × RS (no gate current)
```
VGS = -ID × RS = -ID × 500
```

**Step 2: Substitute into Shockley's equation**
```
ID = 10mA × (1 - VGS/(-5))²
ID = 10mA × (1 + VGS/5)²

Substituting VGS = -500ID (ID in mA):
ID = 10 × (1 - 500ID/5000)²     [converting ID to mA so units match]

Let x = ID (mA):
x = 10(1 - x/20)²
x = 10(1 - x/10 + x²/400)

This is a quadratic — solve graphically or algebraically:
Try ID = 4mA: VGS = -0.5 × 4 = -2V → ID_check = 10(1-(-2)/(-5))² = 10(1-0.4)² = 10×0.36 = 3.6mA ≠ 4mA
Try ID = 3.5mA: VGS = -1.75V → ID_check = 10(1-0.35)² = 10×0.4225 = 4.2mA
Try ID = 3.8mA: VGS = -1.9V → ID_check = 10(0.62)² = 3.84mA ≈ 3.8mA ✓
```

**Q-point:** ID ≈ 3.8mA, VGS ≈ -1.9V

**Step 3: Find VDS**
```
VDS = VDD - ID(RD + RS) = 15 - 3.8mA×(1k+500) = 15 - 5.7 = 9.3V
```

**Q-point:** (VGS = -1.9V, ID = 3.8mA, VDS = 9.3V) — well within active region. ✓

---

## 3. Applications and Use Cases

1. **JFET as Analog Switch (Signal Multiplexer):** JFET's bidirectional conduction in the ohmic region makes it ideal as an analog switch. Unlike BJT, a JFET can pass signals of either polarity. IC CD4051 (CMOS analog mux) uses this principle with MOSFETs.

2. **E-MOSFET in CMOS Digital Logic:** CMOS (Complementary MOS) — the technology behind every microprocessor, RAM chip, and smartphone — uses N-channel and P-channel E-MOSFETs in complementary pairs. In steady state, one of them is always OFF → near-zero static power. The entire digital world runs on E-MOSFETs.

3. **Power MOSFET in Motor Drives and SMPS:** N-channel power E-MOSFETs (IRFZ44N, STP55NF06) handle 40-400A of current at 50-600V in motor drive inverters, battery chargers, and switching power supplies. Their key advantage over BJT is purely voltage-controlled switching (no base current needed) and faster switching (no minority carrier storage).

4. **JFET in Low-Noise Preamplifiers:** The first stage of a condenser microphone's built-in preamp uses a JFET (e.g., 2N5457) because of its low flicker (1/f) noise floor at audio frequencies. Guitar pedal buffers and impedance converters for passive pickups also use JFETs.

5. **D-MOSFET in RF Amplifiers:** Depletion MOSFETs can be biased at VGS = 0, making them self-biased with no external bias components at RF. The BF998 dual-gate D-MOSFET is used as an RF mixer in TV tuners and satellite receivers.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: JFET Drain Current Calculation [May 2019, Q5b — Modified]

**Problem:** A JFET has IDSS = 12mA and VP = -6V. Calculate:  
(a) ID at VGS = -2V  
(b) ID at VGS = -4V  
(c) gm at VGS = -2V  
(d) VDS(sat) at VGS = -2V

**Solution:**

**(a) ID at VGS = -2V:**
```
ID = IDSS × (1 - VGS/VP)²
   = 12 × (1 - (-2)/(-6))²
   = 12 × (1 - 1/3)²
   = 12 × (2/3)²
   = 12 × 4/9
   = 5.33mA
```

**(b) ID at VGS = -4V:**
```
ID = 12 × (1 - (-4)/(-6))²
   = 12 × (1 - 2/3)²
   = 12 × (1/3)²
   = 12 × 1/9
   = 1.33mA
```

**(c) gm at VGS = -2V:**
```
gm0 = 2×IDSS/|VP| = 2×12mA/6 = 4mA/V

gm at VGS = gm0 × (1 - VGS/VP)
           = 4 × (1 - (-2)/(-6))
           = 4 × (1 - 1/3)
           = 4 × 2/3
           = 2.67mA/V  (2667 μS)
```

Verification using derivative: gm = dID/dVGS = 2×IDSS×(1-VGS/VP)/|VP| = 2×12×(2/3)/6 = 2.67mA/V ✓

**(d) VDS(sat) at VGS = -2V:**
```
VDS(sat) = VGS - VP = -2 - (-6) = +4V
The channel pinches off at VDS = 4V; beyond this, saturation region (amplifier operation).
```

---

### Example 2: E-MOSFET Design [KTU Style]

**Problem:** An enhancement MOSFET has K = 0.4mA/V² and VT = 3V. The circuit has VDD = 15V, RD = 5kΩ. A voltage divider bias sets VGS = 7V. Find:  
(a) ID  
(b) VDS  
(c) Confirm operating region

**Solution:**

**(a) ID:**
```
ID = K × (VGS - VT)²
   = 0.4 × (7 - 3)²
   = 0.4 × 16
   = 6.4mA
```

**(b) VDS:**
```
VDS = VDD - ID × RD = 15 - 6.4mA × 5kΩ = 15 - 32 = -17V ???
```

That gives a negative VDS — impossible! This means the assumed operating region is wrong.

**Correction — MOSFET is in ohmic (triode) region:**

If VDS < VGS - VT, the MOSFET is NOT in saturation. At the limit:
```
VDS(sat) = VGS - VT = 7 - 3 = 4V

Maximum possible VDS at saturation boundary:
ID_sat_boundary × RD = VDD - VDS(sat) = 15 - 4 = 11V → ID = 11/5000 = 2.2mA

But at VGS = 7V in saturation: ID would be 6.4mA → VDD - 6.4mA×5kΩ = -17V (not physical)
```

**Re-analyze in ohmic region:**
```
In triode: ID = K[2(VGS-VT)VDS - VDS²]
KVL: VDS = VDD - ID×RD = 15 - 5000×ID

This requires iterative solution or assuming VDS is small:
If VDS ≈ 0V (deep saturation): ID ≈ VDD/RD = 15/5000 = 3mA (limited by RD)

More precisely (iterative):
Assume VDS = 1V: ID = 0.4[2(4)(1) - 1²] = 0.4×7 = 2.8mA → VDS = 15-2.8×5 = 1V ✓

Q-point: VDS = 1V, ID = 2.8mA (triode region — like a switch that's on)
```

**Lesson:** Always check if VDS(sat) = VGS - VT is satisfied. If not, the MOSFET is in triode (on) region.

---

### Example 3: Comparing JFET and BJT Gain [May 2019, Q10 — Modified]

**Problem:** A JFET common-source amplifier has IDSS = 8mA, VP = -4V, VGS = -1V, RD = 3.3kΩ. A BJT common-emitter amplifier has IC = 2mA, RC = 3.3kΩ. Compare their voltage gains.

**Solution:**

**JFET amplifier gain:**
```
gm (at VGS = -1V) = gm0 × (1 - VGS/VP)
gm0 = 2×IDSS/|VP| = 2×8/4 = 4mA/V
gm = 4 × (1-(-1)/(-4)) = 4 × (1 - 0.25) = 4 × 0.75 = 3mA/V

Av(JFET) = -gm × RD = -3mA/V × 3.3kΩ = -9.9 ≈ -10
```

**BJT amplifier gain:**
```
gm(BJT) = IC/VT = 2mA/26mV = 76.9mA/V

Av(BJT) = -gm × RC = -76.9 × 3.3kΩ = -254
```

**Comparison:**

| Parameter | JFET CS Amp | BJT CE Amp |
|-----------|------------|------------|
| Voltage Gain | -10 | -254 |
| Input Impedance | ~MΩ (RG dominates) | ~kΩ (hie) |
| Noise | Lower | Higher |
| Design simplicity | Moderate | Simple |

**Conclusion:** BJT gives 25× higher voltage gain for the same load resistor. JFET is chosen when input impedance or noise is the priority, not gain.

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q5b]: Explain JFET with neat sketches. Draw characteristic curves. [6 marks]

**Complete Solution:**

**JFET — Introduction:**

JFET (Junction Field Effect Transistor) is a unipolar, voltage-controlled device where drain current ID is controlled by gate-to-source voltage VGS with essentially zero gate current.

**Structure:**
```
         Gate (P+) ── Top gate contact
                    │
Source (N+) ──── [N-channel] ──── Drain (N+)
                    │
         Gate (P+) ── Bottom gate contact
                    │
              (tied together: single Gate terminal)
```

**Working:**

- Apply VDD (drain-to-source): Electrons flow from Source to Drain through N-channel (ID flows from D to S conventionally).
- Apply reverse VGS (negative for N-channel): Reverse-biased gate junction creates depletion regions on both sides of channel. Channel narrows → resistance increases → ID decreases.
- At VGS = VP (e.g., -4V): Channel fully pinched off → ID = 0.

**Two Operating Regions:**

1. **Ohmic/Linear region** (VDS < VDS(sat)): ID increases linearly with VDS — FET acts as voltage-controlled resistor. Used in analog switches, VCR (Voltage Controlled Resistor) circuits.

2. **Saturation region** (VDS ≥ VDS(sat) = VGS - VP): ID remains approximately constant, determined only by VGS. This is the **amplifier region**.

**Output Characteristics (ID vs VDS):**
```
     ID(mA)
       ↑
 8  ───●────────────────── VGS = 0
 6  ───  ●──────────────── VGS = -1V
 4  ───    ●────────────── VGS = -2V
 2  ───      ●──────────── VGS = -3V
 0  ─────────────────────── VGS = VP = -4V
       │           │
    ohmic    saturation
     region    region (active/amplifier)
            VDS →
```

**Transfer Characteristics (ID vs VGS):**
```
     ID(mA)
       ↑
  8  ──●  (VGS=0, ID=IDSS)
  6  ──  ●
  4  ──    ●
  2  ──      ●   ← Parabola: ID = IDSS(1-VGS/VP)²
  0  ──────────● VP = -4V
         VGS(V) →
        -4  -3  -2  -1   0
```

**Key parameters:**
- IDSS: Drain current at VGS = 0 (maximum current)
- VP: Pinch-off voltage (VGS at which ID = 0)
- gm: Transconductance = ΔID/ΔVGS (slope of transfer characteristic)

---

### PYQ 2 [May 2019, Q10]: Compare BJT and FET. [3 marks]

**Complete Solution:**

| Basis of Comparison | BJT | FET |
|--------------------|-----|-----|
| Type of device | Current-controlled | Voltage-controlled |
| Control parameter | Base current (IB) | Gate voltage (VGS) |
| Input impedance | Low (few kΩ) | Very high (100MΩ to 10¹⁵Ω) |
| Noise | Higher (minority carrier, shot noise) | Lower (majority carrier only) |
| Gain (voltage) | Very high (βgm product) | Moderate |
| Temperature sensitivity | High (ICBO doubles/10°C) | Lower (ID decreases with temperature) |
| Types | NPN, PNP | N-ch, P-ch (JFET, E-MOS, D-MOS) |
| Gate/base current | IB = IC/β (significant) | Virtually zero |
| Applications | High-gain amplifiers, high-speed switching | Low-noise amplifiers, CMOS digital circuits, analog switches |
| Bandwidth | Higher (for same size) | Moderate (JFET); Very high (MOSFET at RF) |

**Additional distinction:** FETs are **unipolar** (majority carrier only — electrons in N-channel, holes in P-channel). BJTs are **bipolar** (both electrons AND holes carry current, hence the name Bipolar Junction Transistor).
