# Operational Amplifiers (Op-Amps)

## 1. Explanation

### Core Intuition: The Perfect Amplifier

An **Operational Amplifier (op-amp)** is a high-gain, direct-coupled differential amplifier with extremely high input impedance and very low output impedance. The name "operational" comes from its original purpose in analog computers: performing mathematical *operations* (addition, subtraction, integration, differentiation) on electrical signals.

The key insight is that when **negative feedback** is applied around an op-amp with very high open-loop gain (A_OL ≈ 10⁵ to 10⁶), the closed-loop behavior becomes determined almost entirely by the **external feedback network**, not the op-amp internals. This is the "virtual short" principle.

---

### IC 741 — Internal Architecture and Pin Configuration

The 741 is the industry-standard op-amp. Its 8-pin DIP package:

```
         ┌───────────┐
Offset N1 ─ 1  │741│  8 ─ NC (No Connect)
Inv Input (−) ─ 2  │   │  7 ─ V+ (Positive Supply, +15V)
Non-Inv (+) ─ 3  │   │  6 ─ Output
         V− ─ 4  │   │  5 ─ Offset N2
                 └───────────┘

Pin 2: Inverting input (−)
Pin 3: Non-inverting input (+)
Pin 4: V− (Negative supply, e.g. −15V)
Pin 6: Output
Pin 7: V+ (Positive supply, e.g. +15V)
Pins 1 & 5: Offset null (connect 10kΩ pot between them, wiper to V−)
Pin 8: No connection
```

**Internal stages of IC 741:**

1. **Input differential stage:** Long-tailed pair (Q1, Q2) + active load (current mirror). This stage provides the high CMRR and sets the input impedance.
2. **Intermediate gain stage:** Common-emitter amplifier (Q16, Q17) with active load. Provides the bulk of the open-loop voltage gain.
3. **Level-shifting stage:** Shifts DC operating point so output can swing around 0V with split supply.
4. **Output stage:** Class AB complementary (NPN + PNP emitter followers). Provides low output impedance and drives the load.
5. **Compensation capacitor:** 30pF internal (between base and collector of Q16). This is what causes the single-pole rolloff (GBW = 1MHz) and sets the slew rate (SR = 0.5 V/μs).

---

### Differential Amplifier — The Core Building Block

The first stage of every op-amp is a **differential amplifier** that amplifies the *difference* between two input signals while rejecting signals common to both inputs (noise).

**Circuit:**
```
               VCC (+12V)
                │
           [RC] [RC]   ← Equal, matched collector resistors (typically 10kΩ)
            │     │
            ├─────┤ ← Differential output Vod = Ad(V₁ − V₂)
       Q1-C     Q2-C
V1──B──Q1       Q2──B──V2
       Q1-E   Q2-E
            └──┬──┘ ← Emitters tied together at a common node
             [Iee] or [RE]   ← Constant current source (or RE)
               │
              VEE (−12V)
```

**Working — Differential Mode (V1 ≠ V2):**

Let V1 = +Vd/2 and V2 = −Vd/2 (pure differential signal, Vd = V1 − V2):

- Q1 base is more positive → Q1 draws more collector current (ΔIC1 = +gm × Vd/2)
- Q2 base is less positive → Q2 draws less collector current (ΔIC2 = −gm × Vd/2)
- Q1 collector voltage drops: ΔVC1 = −RC × ΔIC1 = −gm × RC × Vd/2
- Q2 collector voltage rises: ΔVC2 = −RC × ΔIC2 = +gm × RC × Vd/2
- Differential output: Vod = VC2 − VC1 = gm × RC × Vd

```
Differential voltage gain (double-ended):
Ad = Vod/(V1−V2) = gm × RC

Single-ended gain (output from one collector to GND):
Ad(single) = gm × RC / 2   [only half the differential swing]
```

**Working — Common Mode (V1 = V2 = Vcm):**

Let V1 = V2 = Vcm (noise or interference, appears identically on both inputs):

- Both Q1 and Q2 bases rise by Vcm → both try to increase IC
- But emitter current source Iee is **fixed** → total emitter current cannot increase
- The current cannot redistribute → both IC1 and IC2 stay approximately constant
- Both VC1 and VC2 change by the same amount → differential output Vod = VC2 − VC1 ≈ 0

**Why common-mode gain is not zero (finite CMRR in practice):**

If the emitter element is a resistor RE (not an ideal current source):
```
Ac = −RC / (2RE + 1/gm) ≈ −RC/(2RE)   for RE >> 1/gm
```

For a practical constant current source with output impedance Ro:
```
Ac ≈ −RC / (2Ro)   [Ro can be 1MΩ+ → very low Ac]
```

**CMRR derivation:**
```
CMRR = |Ad/Ac|

For resistor RE:
Ad = gm × RC
Ac = RC/(2RE) → CMRR = 2 × gm × RE

For current source (Ro replaces RE):
CMRR = 2 × gm × Ro   → CMRR → ∞ as Ro → ∞

In dB: CMRR(dB) = 20 log₁₀(CMRR)

For IC 741: CMRR(min) = 70dB, CMRR(typ) = 90dB
```

**What CMRR means practically:**

In an ECG machine, the heart signal is ≈1mV differential. Mains interference (50Hz) appears as ≈100mV common-mode on both electrodes. With a differential amplifier with Ad = 1000 and CMRR = 90dB (CMRR = 31,623):
```
Ac = Ad/CMRR = 1000/31623 = 0.032

Output signal from ECG: 1mV × 1000 = 1V
Output from mains hum: 100mV × 0.032 = 3.2mV   ← easily filtered out
Signal-to-noise ratio: 1V / 3.2mV = 312 (about 50dB)
```

Without CMRR (simple single-ended amplifier): mains hum at output = 100mV × 1000 = 100V — completely overwhelming the signal.

---

### Op-Amp Characteristics — Ideal vs Practical (IC 741)

| Parameter | Symbol | Ideal | IC 741 Practical | What it limits |
|-----------|--------|-------|-----------------|----------------|
| Open-loop voltage gain | AOL | ∞ | 200,000 (106dB) | Closed-loop accuracy |
| Input impedance | Zin | ∞ Ω | 2 MΩ | Input loading |
| Output impedance | Zout | 0 Ω | 75 Ω | Output current drive |
| Gain-bandwidth product | GBW | ∞ | 1 MHz | High-frequency gain |
| CMRR | — | ∞ | 90dB (typ), 70dB (min) | Noise rejection |
| Slew rate | SR | ∞ V/μs | 0.5 V/μs | Large-signal speed |
| Input offset voltage | Vio | 0 V | ±2mV (typ), ±6mV (max) | DC accuracy |
| Input bias current | IB | 0 A | 80nA (typ), 500nA (max) | DC offset |
| Input offset current | Iio | 0 A | 20nA (typ), 200nA (max) | Residual DC error |
| Output swing | — | ±∞ | ±(VCC − 1.5V) ≈ ±13.5V (at ±15V) | Dynamic range |
| Supply voltage range | — | Any | ±5V to ±18V | System design |
| Short-circuit protection | — | N/A | Yes (built-in 25mA) | Device safety |

---

#### Open-Loop Gain (AOL) and Frequency Response

The gain without feedback. For IC 741, the open-loop gain is **not flat** — it rolls off rapidly:

```
AOL(f) = AOL(DC) / (1 + jf/f1)   [first-order roll-off due to compensation capacitor]

For 741:
AOL(DC) = 200,000
f1 = 5Hz   (open-loop −3dB frequency — surprisingly low!)

At f = 5Hz:   AOL = 141,421 (−3dB point)
At f = 1kHz:  AOL = 200,000/200 = 1,000
At f = 10kHz: AOL = 200,000/2000 = 100
At f = 1MHz:  AOL = 1 (unity gain bandwidth)
```

**Gain-Bandwidth Product (GBW):**

```
GBW = AOL(DC) × f1 = 200,000 × 5Hz = 1 MHz

This is constant across all frequencies (for the single-pole model):
GBW = AOL(f) × f = 1 MHz always

For a closed-loop non-inverting amplifier with gain Af:
Closed-loop bandwidth = GBW / Af = 1MHz / Af

Af = 1 (voltage follower):  BW = 1MHz
Af = 10:                     BW = 100kHz
Af = 100:                    BW = 10kHz
Af = 1000:                   BW = 1kHz
```

**Physical insight:** The compensation capacitor (30pF in 741) intentionally creates this slow rolloff — it prevents oscillation by ensuring only one dominant pole controls the phase. Without it, multiple transistor poles would combine to create 180° phase shift within the feedback loop → spontaneous oscillation.

---

#### Slew Rate (SR)

The maximum rate at which the **output voltage can change**, regardless of input:

```
SR = |dVout/dt|_max

For IC 741: SR = 0.5 V/μs = 500,000 V/s
```

**Physical origin of SR:** The internal compensation capacitor (30pF) must be charged or discharged by the input stage bias current (≈19μA for 741):

```
SR = I_bias / C_comp = 19μA / 30pF = 0.63 V/μs   ≈ 0.5 V/μs (matches datasheet)
```

**When does SR limit the output?**

For a sinusoidal output Vm sin(2πft), the maximum slope (at zero crossing) is:
```
(dVout/dt)_max = 2π × f × Vm

For no slewing: 2π × f × Vm ≤ SR
Full-power bandwidth: fFP = SR / (2π × Vm)
```

| Output amplitude Vm | IC 741 fFP |
|--------------------|-----------:|
| 10V (peak) | 7.96 kHz |
| 5V | 15.9 kHz |
| 1V | 79.6 kHz |
| 0.1V | 796 kHz |

**SR vs GBW — the critical distinction:**

- **GBW** is a *small-signal* limit — at what frequency does the op-amp fail to amplify a tiny signal?
- **SR** is a *large-signal* limit — at what frequency does the output fail to follow a large swing?

**Example:** IC 741 as voltage follower (GBW limit = 1MHz, SR = 0.5V/μs):
- A 1mV sine wave at 900kHz: slope = 2π × 900k × 0.001 = 5.65 V/μs > 0.5 V/μs? NO: 2π × 900kHz × 0.001V = 5.65mV/μs = 0.00565 V/μs << SR. Fine.
- A 5V sine wave at 15kHz: slope = 2π × 15k × 5 = 471 kV/s = 0.471 V/μs < 0.5 V/μs. Just fine.
- A 5V sine wave at 20kHz: slope = 2π × 20k × 5 = 628 kV/s = 0.628 V/μs > 0.5 V/μs. **Slewing!** Output becomes triangular.

**Slew-rate distortion waveform:**
```
Desired output (sine, Vm=5V, f=50kHz):       ∿∿∿∿∿∿∿∿
                                                Slope > SR!
Actual output (slewing, rate = 0.5V/μs): /\/\/\/\/  ← triangular wave
```

---

#### Input Offset Voltage (Vio)

The small differential voltage that must be applied between the input terminals to make the output exactly zero. Caused by manufacturing mismatch in the differential pair (unequal VBE, unequal β, mismatched RC resistors).

```
For IC 741: Vio = ±2mV (typ), ±6mV (max)

Effect on inverting amplifier output:
Vout(error) = Vio × (1 + Rf/Rin)   [offset appears amplified by closed-loop gain]

For Rf/Rin = 100 (gain = −100):
Vout(error) = ±2mV × 101 = ±202mV DC error at output
```

**Correction (Offset Null):**

A 10kΩ potentiometer connected between pins 1 and 5, with the wiper going to V− (pin 4). Adjusting the pot trims the internal current imbalance until Vout = 0 with Vin = 0. This must be redone if temperature changes significantly (Vio drifts with temperature at ≈5μV/°C for 741).

---

#### Input Bias Current (IB)

The average DC current that flows into both input terminals. In BJT op-amps, this is the base current of the differential pair transistors.

```
IB = (IB+ + IB−) / 2

For IC 741: IB = 80nA (typ), 500nA (max)
```

**Why this causes output error:**

Even with Vin = 0, IB flows through the feedback resistors, creating a voltage:
```
For inverting amplifier: V−(error) = IB × (Rin || Rf) ≈ IB × Rf/2   [approximately]
This error is amplified:
Vout(error) ≈ IB × Rf   (for Rf >> Rin, approximately)

For IB = 80nA and Rf = 100kΩ: Vout(error) = 80nA × 100k = 8mV
```

**Compensation:** Add resistor Rcomp = Rin || Rf at the non-inverting (+) input. Now IB flows through Rcomp and creates a voltage that cancels the error from IB− flowing through Rin||Rf:

```
Rcomp = Rin || Rf   ← This is the standard bias current compensation resistor

With Rcomp: only the *difference* (Iio = IB+ − IB−) causes error
Residual error: Vout(error) = Iio × Rf   [much smaller since Iio << IB]
```

---

#### Input Offset Current (Iio)

The difference between the two input bias currents, caused by transistor mismatch:

```
Iio = |IB+ − IB−|

For IC 741: Iio = 20nA (typ), 200nA (max)   [about 1/4 of IB]

After adding Rcomp: residual error = Iio × Rf
For Iio = 20nA, Rf = 100kΩ: residual error = 20nA × 100k = 2mV
```

**Note on CMOS op-amps:** Modern CMOS op-amps (e.g., TL071, LMC6482) have MOSFET input stages with IB in the femtoampere range (10⁻¹⁵ A) — bias current compensation resistors are not needed.

---

### The "Virtual Short" Principle — Complete Derivation

When an op-amp with gain AOL is connected in a negative feedback loop:

```
Error voltage: Vε = V+ − V−   [differential input]
Output: Vout = AOL × Vε

The output drives the feedback network, which forces V− toward V+:
Vε = Vout / AOL = (finite voltage) / 200,000 = extremely small

For Vout = 10V: Vε = 10/200,000 = 50μV ≈ 0
```

Therefore: V+ ≈ V− (inputs appear at the same potential) — this is the **virtual short**.

**Important: it is virtual, not real:**
- Virtual: The potentials are equal, but there is no low-resistance connection between them
- NOT real: No current flows between V+ and V− (input impedance is 2MΩ)

**The Two Golden Rules of Ideal Op-Amp Analysis:**

> 1. **V+ = V−** (virtual short — differential input ≈ 0 for negative feedback circuits)
> 2. **I+ = I− = 0** (no current into either input terminal)

Apply these two rules mechanically to derive the behavior of any op-amp circuit with negative feedback.

---

### Op-Amp Applications — Complete Analysis

#### Application 1: Inverting Amplifier (Scale Changer)

**Circuit:**
```
              Rf
    ┌─────────┤├──────────── Vout
    │                  │
Vin ─┤ Rin ──── (−) ────┘
                (+)
                 │
                GND

Optional: Rcomp = Rin||Rf connected from (+) to GND (bias compensation)
```

**Step-by-step derivation:**

1. V+ = 0V (grounded). By virtual short: **V− = 0V** ("virtual ground")
2. Current through Rin: since V− = 0, I₁ = (Vin − 0)/Rin = **Vin/Rin**
3. KCL at the V− node: I_into_op-amp = 0 → I_Rin = I_Rf = **Vin/Rin**
4. Voltage at Vout from V−: Vout = V− − I_Rf × Rf = 0 − (Vin/Rin) × Rf

```
┌───────────────────────────────┐
│  Av = Vout/Vin = −Rf/Rin     │
└───────────────────────────────┘

Input impedance:  Zin = Rin   (input "sees" Rin to virtual ground)
Output impedance: Zout ≈ 75Ω / (1 + AOL × β) ≈ 0 Ω (very low)
Phase:            180° (inverting)
```

**Design example:** Gain = −47:
- Choose Rin = 1kΩ → Rf = 47kΩ
- Bandwidth = GBW/|Av| = 1MHz/47 = 21.3kHz
- Rcomp = 1kΩ || 47kΩ = 979Ω ≈ 1kΩ

---

#### Application 2: Sign Changer (Unity-Gain Inverter)

Special case of the inverting amplifier with Rf = Rin:
```
Av = −Rf/Rin = −1

Vout = −Vin   (identical amplitude, 180° phase shift)
```

**Use:** Negate a signal in analog computation. In audio, invert phase to cancel standing waves in a room.

---

#### Application 3: Non-Inverting Amplifier

**Circuit:**
```
                        Rf
Vout ─────────────────┤├──── (−)
                              │
                             R1
                              │
                             GND

Vin ──────────────────────── (+)
```

**Step-by-step derivation:**

1. V+ = Vin (input connected directly to +)
2. By virtual short: **V− = V+ = Vin**
3. V− is the midpoint of a voltage divider (R1 from GND, Rf from Vout):
   ```
   V− = Vout × R1/(R1 + Rf)
   ```
4. Set V− = Vin and solve for Vout:
   ```
   Vin = Vout × R1/(R1 + Rf)
   Vout/Vin = (R1 + Rf)/R1 = 1 + Rf/R1
   ```

```
┌───────────────────────────────────────┐
│  Av = 1 + Rf/R1   (always ≥ 1)       │
└───────────────────────────────────────┘

Input impedance:  Zin >> Rin of op-amp (Zin = AOL × Rin × β ≈ GΩ)
Output impedance: Zout ≈ 0 Ω
Phase:            0° (non-inverting)
Minimum gain:     1 (when Rf = 0, R1 = ∞ → voltage follower)
```

**Comparison: Inverting vs Non-Inverting:**

| Property | Inverting | Non-Inverting |
|----------|-----------|---------------|
| Gain formula | −Rf/Rin | 1 + Rf/R1 |
| Gain sign | Negative (≤ −1 possible) | Always positive (≥ 1) |
| Input impedance | Rin (moderate) | Very high (GΩ range) |
| Output impedance | ≈ 0 | ≈ 0 |
| Phase shift | 180° | 0° |
| Min gain magnitude | Any | 1 |

---

#### Application 4: Voltage Follower (Unity-Gain Buffer)

Special case: Rf = 0 (short circuit), R1 = ∞ (open circuit):

```
         ┌───────────────── Vout
         │          (−)
Vin ──── (+)
```

Derivation: V+ = Vin. V− = Vout (direct feedback). Virtual short → Vout = Vin.

```
Av = 1
Zin = AOL × Zin(open) ≈ several GΩ
Zout ≈ 0 Ω (< 1Ω in practice)
```

**Critical use case:** Prevents source loading. A pH electrode (source impedance = 10⁹ Ω) connected to a 10kΩ input amplifier without a buffer:
```
Signal attenuation = Zload/(Zsource + Zload) = 10k/(10⁹ + 10k) ≈ 10⁻⁵   (99.999% loss!)
With voltage follower buffer: signal transfers at ≈ 100% → no loss.
```

---

#### Application 5: Summing Amplifier (Inverting Adder)

**Circuit (3-input):**
```
V1 ─┤ R1 ─┐
V2 ─┤ R2 ─┤── (−) ──┬── [Op-Amp] ── Vout
V3 ─┤ R3 ─┘         └── Rf ──── (back to −)
              (+) ── GND
```

**Derivation:**

Virtual ground: V− = 0. All input currents flow into the virtual ground node independently:
```
I1 = V1/R1,   I2 = V2/R2,   I3 = V3/R3

KCL at V−: I1 + I2 + I3 = I_Rf   (since I into op-amp = 0)

Vout = −I_Rf × Rf = −(V1/R1 + V2/R2 + V3/R3) × Rf

= −(V1 × Rf/R1 + V2 × Rf/R2 + V3 × Rf/R3)
```

**Key insight:** Each input contributes independently (superposition principle), because the virtual ground node holds each input's effect isolated from the others.

**Equal resistors (R1 = R2 = R3 = R):**
```
Vout = −(Rf/R) × (V1 + V2 + V3)

For Rf = R: Vout = −(V1 + V2 + V3)   [unity-gain inverting adder]
For Rf = R/3: Vout = −(V1 + V2 + V3)/3   [averaging amplifier!]
```

**Scaling to different gains (Rf = 10kΩ):**
```
For gain on V1 = −5: R1 = Rf/5 = 2kΩ
For gain on V2 = −3: R2 = Rf/3 = 3.3kΩ
For gain on V3 = −2: R3 = Rf/2 = 5kΩ

Vout = −(5V1 + 3V2 + 2V3)
```

---

#### Application 6: Subtractor (Difference Amplifier)

**Circuit:**
```
         R2
    ┌────┤├──────────── Vout
    │          │
V1 ─┤ R1 ──(−)┘
              (+)
               │
V2 ─┤ R3 ─ ─┤├─── GND
              R4
```

**Complete derivation using superposition:**

**Step 1 — V+ (non-inverting input voltage, due to V2 only):**
```
V2 drives (+) through a voltage divider R3 and R4:
V+ = V2 × R4/(R3 + R4)
```

**Step 2 — Virtual short:** V− = V+ = V2 × R4/(R3 + R4)

**Step 3 — KCL at V− (inverting input node):**
```
(V1 − V−)/R1 = (V− − Vout)/R2

Cross-multiplying:
(V1 − V−) × R2 = (V− − Vout) × R1
V1R2 − V−R2 = V−R1 − VoutR1
VoutR1 = V−R1 + V−R2 − V1R2
Vout = V−(R1 + R2)/R1 − V1(R2/R1)
```

**Step 4 — Substitute V−:**
```
Vout = [V2 × R4/(R3+R4)] × (1 + R2/R1) − V1 × (R2/R1)
```

**For equal resistors R1 = R2 = R3 = R4 = R:**
```
V+ = V2 × R/(R+R) = V2/2
Vout = (V2/2)(1 + R/R) − V1 × (R/R)
     = (V2/2)(2) − V1
     = V2 − V1

∴ Vout = V2 − V1   [unity-gain subtractor]
```

**General case (R2/R1 = R4/R3 = K):**
```
Vout = K × (V2 − V1)
```

**Resistor matching is critical:** If R2/R1 ≠ R4/R3, the common-mode rejection degrades badly. For a subtractor with 60dB CMRR, resistors must match to better than 0.1%.

---

#### Application 7: Integrator (Miller Integrator)

**Circuit:**
```
              C  (feedback capacitor)
    ┌─────────||──────────────── Vout
    │                    │
Vin ─┤ R ──── (−) ────────┘
               (+)
                │
               GND
```

**Step-by-step derivation:**

1. V− = virtual ground = 0V
2. Current through R: I = (Vin − 0)/R = Vin/R
3. This current charges capacitor C (no current into op-amp):
   ```
   IC = C × d(VC)/dt = C × d(Vout − V−)/dt = C × d(Vout)/dt
   ```
   But IC = −I (current flows FROM V− INTO Rf direction, so into the capacitor from the left):
   ```
   Vin/R = −C × d(Vout)/dt
   d(Vout)/dt = −Vin/(RC)
   ```
4. Integrate:
   ```
   Vout(t) = −(1/RC) × ∫₀ᵗ Vin(τ) dτ + Vout(0)
   ```

**Transfer function (frequency domain):**
```
H(jω) = Vout/Vin = −1/(jωRC) = −Xc/R

|H(ω)| = 1/(ωRC)   [gain decreases with frequency — low-pass nature]

At ω = 1/RC: |H| = 1 (0dB) — the integration time constant frequency
At ω → 0 (DC): |H| → ∞ — infinite DC gain → DC offset saturates output!
```

**Waveform analysis for square wave input (amplitude ±V, period T):**

```
During Vin = +V (positive half, 0 < t < T/2):
Vout(t) = −(+V)/(RC) × t = −Vt/RC   [linearly falling ramp]

During Vin = −V (negative half, T/2 < t < T):
Vout(t) = −(−V)/(RC) × (t−T/2) + Vout(T/2)   [linearly rising ramp]

Peak-to-peak triangular wave amplitude:
ΔVpeak = V × (T/2) / RC   [amplitude of triangle per half-cycle]
```

**Input → Output for common waveforms:**

| Input waveform | Output waveform | Formula |
|---------------|----------------|---------|
| Square wave ±V | Triangular wave | ΔV = V×T/(2RC) p-p |
| Sine Vm sin(ωt) | Cosine: −Vm/(ωRC) × cos(ωt) | Gain = −1/(ωRC), 90° phase lead |
| Triangle wave | Parabola | Quadratic |
| DC step V | Linear ramp | dVout/dt = −V/RC |
| Impulse | Step | Discontinuous jump in Vout |

**Practical integrator — the DC saturation problem and fix:**

An ideal integrator saturates due to any DC offset (Vio × 1/jωRC → ∞ as ω → 0). **Fix:** Add large resistor RF in parallel with C:

```
New transfer function:
H(jω) = −RF/R × 1/(1 + jωRFC)   [low-pass filter with DC gain = −RF/R]

For f >> fL = 1/(2πRFC): acts as ideal integrator (C dominates)
For f << fL: DC gain = −RF/R (finite, prevents saturation)

Choose RF = 10R minimum, typically RF = 100R:
- RF = 10R: integrates correctly for f > 10×fL
- RF = 100R: integrates correctly for f > 100×fL (wider integration range)
```

---

#### Application 8: Differentiator

**Circuit:**
```
              R  (feedback resistor)
    ┌─────────┤├──────────────── Vout
    │                    │
Vin ─┤ C ──── (−) ────────┘
     ||        (+)
               │
              GND
```

**Step-by-step derivation:**

1. V− = virtual ground = 0V
2. Current through C: IC = C × d(Vin − V−)/dt = C × d(Vin)/dt
3. This current flows through R (no current into op-amp):
   ```
   Vout = 0 − IC × R = −RC × d(Vin)/dt
   ```

```
┌─────────────────────────────────┐
│  Vout = −RC × d(Vin)/dt        │
└─────────────────────────────────┘
```

**Transfer function:**
```
H(jω) = −jωRC

|H(ω)| = ωRC   [gain increases linearly with frequency]

At ω = 1/RC: |H| = 1
At high frequencies: |H| → ∞ → noise amplified without limit!
```

**Waveform analysis for square wave input:**

```
Vin: square wave (transitions between +V and −V with finite rise time Tr)

At each transition:
dVin/dt ≈ 2V/Tr   (average slope during transition)

Vout = −RC × 2V/Tr   [spike amplitude]
Spike duration ≈ Tr

For ideal (infinitely fast) transitions: output is impulse (δ function) spikes.
```

**Input → Output:**

| Input | Output |
|-------|--------|
| Square wave | Positive/negative spikes at edges |
| Triangle wave | Square wave (derivative of ramp = constant) |
| Sine Vm sin(ωt) | ωRC × Vm × cos(ωt) (90° phase lag, amplitude increases with ω) |
| Parabola | Triangle |

**Practical differentiator — the noise problem and fix:**

An ideal differentiator amplifies high-frequency noise (gain → ∞ with frequency). **Fix:** Add series resistor Rs with C:

```
Modified circuit: C in series with Rs, then to V−; R remains as feedback

Transfer function:
H(jω) = −jωRC / (1 + jωRsC)

At low frequencies (ω << 1/(RsC)): H ≈ −jωRC   [ideal differentiation]
At high frequencies (ω >> 1/(RsC)): H ≈ −R/Rs   [gain limited to R/Rs]

Two design frequencies:
fd = 1/(2πRC):   frequency above which integration would occur in ideal
fs = 1/(2πRsC):  frequency where gain limiting kicks in

For good differentiation: choose fd << signal frequencies << fs
Rule of thumb: Rs = R/10, so fs = 10 × fd
```

---

#### Application 9: Schmitt Trigger (Comparator with Hysteresis)

**Core concept:** A comparator with **positive feedback** creates hysteresis — different threshold voltages for rising vs falling input. This creates a "dead zone" that prevents noise from causing false triggering.

**Inverting Schmitt Trigger — Most common form:**

**Circuit:**
```
Vin ──────────────────── (−)
                           [Op-Amp] ─────────── Vout
                          (+)
                           │
            ┌──────────────┘
            │
           [R1]
            │
           GND

Positive feedback: Vout ──[R2]──(+)──[R1]── GND
                         V(+) = Vout × R1/(R1+R2)
```

**Threshold derivation:**

**Case 1: Output at +Vsat (positive saturation, ≈+13V for ±15V supply):**
```
V(+) = +Vsat × R1/(R1+R2)   ← this is the current threshold

Output will switch LOW when Vin rises above V(+):
UTP (Upper Threshold Point) = +Vsat × R1/(R1+R2)
```

**Case 2: Output at −Vsat:**
```
V(+) = −Vsat × R1/(R1+R2)   ← threshold drops to negative value

Output will switch HIGH when Vin falls below V(+):
LTP (Lower Threshold Point) = −Vsat × R1/(R1+R2)
```

**Hysteresis window:**
```
Hysteresis = UTP − LTP = 2 × Vsat × R1/(R1+R2)
```

**Operation step-by-step (for a rising then falling Vin):**

```
1. Start: Vout = +Vsat → V(+) = UTP (positive)
2. Vin rises. While Vin < UTP: output stays at +Vsat
3. Vin reaches UTP: Vin > V(+) → output snaps to −Vsat
4. V(+) now drops to LTP (negative) — threshold jumps!
5. Vin falls. While Vin > LTP: output stays at −Vsat
6. Vin falls to LTP: Vin < V(+) → output snaps back to +Vsat
7. V(+) returns to UTP — cycle restarts
```

**Transfer characteristic (hysteresis loop):**
```
Vout
      ↑
+Vsat │     ─────────────────────────────────────────→ (stays HIGH until UTP)
      │                                    ↑ (UTP, snaps LOW)
      │                              ┌─────┘
      │                              │
      │           ┌──────────────────┘ (LTP, snaps HIGH)
      │           ↓ (LTP)
−Vsat │ ──────────────────────────────────────────────→ (stays LOW until LTP)
      │
      └────────────────────────────────────────────→ Vin
            LTP                    UTP
```

**Design example:**

Requirements: ±15V supply (Vsat = 13V), hysteresis = 3V (symmetric: UTP = +1.5V, LTP = −1.5V):
```
UTP = Vsat × R1/(R1+R2)
1.5 = 13 × R1/(R1+R2)
R1/(R1+R2) = 1.5/13 = 0.1154
R2/R1 = (1 − 0.1154)/0.1154 = 7.67

Choose R1 = 10kΩ → R2 = 76.7kΩ ≈ 75kΩ (standard)

Verify: UTP = 13 × 10k/(10k+75k) = 13 × 0.118 = 1.53V ✓
```

**Non-Inverting Schmitt Trigger:**

Vin applied to (+) input; (−) input grounded; positive feedback through R1-R2 from Vout back to (+):

```
V(+) = Vin × R2/(R1+R2) + Vout × R1/(R1+R2)   [superposition at + input]

Threshold (output switches):
When Vout = +Vsat: UTP = −Vsat × R1/R2   [switches when Vin drops below LTP]
When Vout = −Vsat: LTP = +Vsat × R1/R2   ← non-inverting has thresholds flipped!

Actually for non-inverting (Vin at +, GND at −, feedback from Vout to +):
UTP = Vsat × R1/R2   [output switches when Vin rises above this]
LTP = −Vsat × R1/R2
```

---

#### Application 10: Wien Bridge Oscillator using Op-Amp

**Circuit:**
```
                    Rf (= 2R1)
       ┌────────────┤├──────────────────────────────────┐
       │                                                  │
      (−)                                                 │
  [Op-Amp] ──── Vout ──────────────────────────── (+) ──┘
      (+)               │             │
                     [R]     [R parallel C]
                         │             │
                        [C]          GND
                         │
                        GND

Wien feedback network between Vout and (+):
Series arm: R + 1/(jωC)   → high-pass section
Parallel arm: R || 1/(jωC) → low-pass section
```

**Transfer function of Wien network (β):**

At exactly ω₀ = 1/(RC):
```
β = Z_parallel / (Z_series + Z_parallel)

Z_series = R + 1/(jω₀C) = R + R×j/(j²) ...

Let x = ωRC. At x = 1 (ω = ω₀):
β = (R||C) / (R + 1/jωC + R||C)

After algebra (shown in Module 4 notes):
β = 1/3  ∠ 0°   at ω = 1/(RC)
```

**Barkhausen condition:**

- Non-inverting amp gain: Av = 1 + Rf/R1. For oscillation: Av × β = 1
- Av × (1/3) = 1 → Av = 3 → Rf/R1 = 2 → **Rf = 2R1**

**Oscillation frequency:** f₀ = 1/(2πRC)

**Design (f₀ = 5kHz):**
```
Choose C = 0.01μF:
R = 1/(2π × 5000 × 0.01×10⁻⁶) = 1/(3.14×10⁻⁴) = 3.18kΩ ≈ 3.3kΩ

Choose R1 = 10kΩ → Rf = 20kΩ (or 22kΩ with thermistor for amplitude control)
```

**Amplitude stabilization (thermistor method):**

Set Rf slightly > 2R1 (e.g., Rf = 22kΩ) so startup gain = 2.2. As amplitude builds, the thermistor NTC (in series with R1) warms due to power dissipation → resistance drops → effective R1 increases → gain drops → stabilizes at gain = 3.

---

## 2. Example — Solved Design Problem

### Summing Amplifier Realization [May 2019, Q19a]

**Problem:** Realize Y(t) = 5V1 + 2V2 – 4V3 using op-amps.

**Analysis:** All terms are positive for V1 and V2 but negative for V3. Since an inverting summer always inverts, we need two stages (double inversion gives positive sign for V1, V2):

**Stage 1 — Inverting Summing Amplifier:**
```
Vout1 = −(5V1 + 2V2)

Choose Rf = 10kΩ:
R(V1) = Rf/5 = 10k/5 = 2kΩ   [Vout1 gain on V1 = −Rf/R(V1) = −5]
R(V2) = Rf/2 = 10k/2 = 5kΩ   [Vout1 gain on V2 = −Rf/R(V2) = −2]
```

**Stage 2 — Inverting Summing Amplifier (inverts Stage 1, scales V3):**
```
Vout = −(Vout1 × a + V3 × b)
     = −(−(5V1+2V2) × 1 + V3 × 4)
     = 5V1 + 2V2 − 4V3 ✓

Choose Rf2 = 4kΩ:
R(Stage1) = Rf2/1 = 4kΩ   [gain on Stage 1 output = −1, cancels the inversion]
R(V3) = Rf2/4 = 1kΩ       [gain on V3 = −4, gives −4V3 term]
```

**Final circuit values:**
| Component | Value | Purpose |
|-----------|-------|---------|
| Stage 1 Rf | 10kΩ | Feedback |
| Stage 1 R(V1) | 2kΩ | Gain 5 for V1 |
| Stage 1 R(V2) | 5kΩ | Gain 2 for V2 |
| Stage 2 Rf | 4kΩ | Feedback |
| Stage 2 R(Vout1) | 4kΩ | Gain 1 for Stage 1 (re-invert) |
| Stage 2 R(V3) | 1kΩ | Gain 4 for V3 |

---

## 3. Applications and Use Cases

1. **Summing amplifier in audio mixing consoles:** A 32-channel mixing console uses a 32-input summing amplifier to combine all mic/line channels into stereo outputs. Each fader changes its input resistor (gain), independently controlling that channel's contribution.

2. **Integrator in dual-slope ADC:** The heart of a voltmeter. Charge a capacitor for a fixed time using the unknown voltage (Vx), then discharge with a known reference (Vref) and measure the discharge time — proportional to Vx. Accuracy depends only on timing and Vref, not on RC (self-calibrating).

3. **Differentiator in velocity measurement:** A tachometer measures angular velocity by differentiating shaft position (from an encoder). A differentiator circuit converts the position voltage to a velocity voltage in real-time.

4. **Schmitt trigger in digital communication receivers:** UART/SPI/I²C receiver input pins have Schmitt trigger hysteresis (e.g., 74HC14 has VIH = 3.15V, VIL = 1.35V, hysteresis = 1.8V at VCC = 5V) to reject glitches on noisy PCB lines.

5. **Differential amplifier in strain gauge (Wheatstone bridge):** A load cell uses a Wheatstone bridge that produces millivolt differential signals from a balanced bridge. A differential amplifier (or instrumentation amp) with 80dB+ CMRR extracts this tiny signal from the large common-mode offset.

6. **Non-inverting amplifier in sensor conditioning:** Thermistor or thermocouple signal conditioning chains use non-inverting amplifiers (high Zin = no loading on sensor) to scale mV signals to 0–5V ADC input range.

7. **Wien bridge in function generator ICs:** The Maxim ICL8038 and XR2206 function generator ICs implement Wien-bridge-like oscillators internally to produce sine waves with < 1% THD, tunable from 0.001Hz to 300kHz.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Slew Rate and Full-Power Bandwidth [May 2019, Q17b]

**Problem:** Explain CMRR and Slew Rate with typical values for IC 741. [4 marks]

**CMRR:**

```
CMRR = Ad/Ac   (dimensionless or in dB: 20 log(Ad/Ac))

For IC 741: CMRR(typ) = 90dB → Ac = Ad/31,623

At closed-loop gain Af = 1000:
Ad (closed-loop differential) ≈ 1000
Ac = 1000/31,623 = 0.0316

A 10mV common-mode signal (noise) appears at output as:
Vout(cm) = 0.0316 × 10mV = 0.316mV   (vs 1V output for 1mV differential signal)
CMRR significance: the op-amp ignores noise 31,623× more than the desired signal.
```

**Slew Rate:**

```
SR = 0.5 V/μs for IC 741

Full-power bandwidth:
fFP = SR/(2π × Vm)

At Vm = 10V: fFP = 0.5×10⁶/(2π × 10) = 7.96kHz ≈ 8kHz
At Vm = 1V:  fFP = 79.6kHz

Slew test: If a 1V step is applied to the input of a unity-gain 741:
Output risetime = ΔV/SR = 1/0.5×10⁶ = 2μs   (linear ramp, not exponential)
```

---

### Example 2: Complete Inverting Amplifier Design

**Problem:** Design an inverting amplifier using IC 741 with gain = −20 and bandwidth = 50kHz. Find all resistor values and verify the design.

**Step 1: Check GBW constraint:**
```
GBW = 1MHz → BW at gain = 1MHz/20 = 50kHz ✓ (exactly meets requirement)
Note: gain ≥ 20 is needed; actual gain of 20 gives BW = 50kHz — just feasible.
```

**Step 2: Choose resistor values:**
```
Av = −Rf/Rin = −20

Choose Rin = 5kΩ:
Rf = 20 × 5k = 100kΩ

Bias compensation resistor: Rcomp = Rin || Rf = 5k || 100k = 4.76kΩ ≈ 4.7kΩ
```

**Step 3: Check DC accuracy:**
```
Output offset from Vio: ΔVout = Vio × (1 + Rf/Rin) = 2mV × 21 = 42mV
Output offset from IB:  ΔVout = Iio × Rf = 20nA × 100k = 2mV (with Rcomp)
Total DC error: ≈ 44mV   (acceptable for most applications)
```

**Step 4: Summary:**
- Rin = 5kΩ, Rf = 100kΩ, Rcomp = 4.7kΩ
- Gain = −20, BW = 50kHz, Zin = 5kΩ

---

### Example 3: Schmitt Trigger Design and Threshold Calculation [May 2019, Q18a]

**Problem:** Design a Schmitt trigger using IC 741 to give UTP = +2V and LTP = −2V with ±15V supply. [6 marks]

**Solution:**

**Step 1: Find Vsat:**
```
IC 741 output swing ≈ ±(VCC − 1.5V) = ±(15 − 1.5) = ±13.5V
Vsat ≈ 13.5V (use 13V as conservative estimate)
```

**Step 2: Calculate R1, R2:**
```
UTP = Vsat × R1/(R1+R2) = 2V
R1/(R1+R2) = 2/13 = 0.1538

R2/R1 = (1/0.1538) − 1 = 6.5 − 1 = 5.5

Choose R1 = 10kΩ → R2 = 55kΩ ≈ 56kΩ (standard)
```

**Step 3: Verify:**
```
UTP = 13 × 10/(10+56) = 13 × 10/66 = 1.97V ≈ 2V ✓
LTP = −1.97V ≈ −2V ✓
Hysteresis = UTP − LTP = 3.94V ≈ 4V
```

**Step 4: Operation description:**
- Vin rising: output stays at +13V until Vin reaches +1.97V → snaps to −13V
- Vin falling: output stays at −13V until Vin falls to −1.97V → snaps to +13V
- Any noise within the ±2V window causes NO false triggering

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q15a]: Draw and explain the circuit of a differential amplifier. [5 marks]

**Complete Solution:**

**Circuit:**
```
            VCC (+12V)
             │
        [RC] [RC]   ← Matched (≈10kΩ each)
         │     │
    Q1-C─┴─────┴─Q2-C   ← Differential output taken here
V1 ─B─Q1(NPN)   (NPN)Q2─B─ V2
      Q1-E         Q2-E
         └────┬────┘
           [Iee = 2mA]   ← Constant current source
              │
            VEE (−12V)
```

**Operation:**

*Differential mode (V1 ≠ V2):*

Let V1 = +0.5mV, V2 = −0.5mV (Vd = 1mV):
- Q1: ΔIC1 = gm × Vd/2 (increases)
- Q2: ΔIC2 = −gm × Vd/2 (decreases)
- VC1 drops, VC2 rises → differential output = Ad × Vd

*Common-mode (V1 = V2 = Vcm):*

- Both bases rise by Vcm → both IC try to increase
- Iee = constant → cannot change → zero net change
- ΔVC1 = ΔVC2 → differential output ≈ 0

**Key equations:**
```
Ad = gm × RC   (double-ended)
Ac = RC / (2Ro)   where Ro = impedance of current source
CMRR = Ad/Ac = 2 × gm × Ro

For gm = 40mA/V (at IC = 1mA) and Ro = 1MΩ:
CMRR = 2 × 0.04 × 10⁶ = 80,000 = 98dB
```

---

### PYQ 2 [May 2019, Q16a]: Derive voltage gain of inverting and non-inverting op-amp. [6 marks]

**Complete Solution:**

**Basis — Virtual short principle:**

Since AOL = 200,000 and output is bounded:
Vd = V+ − V− = Vout/AOL ≈ 0 → V+ = V−

**Two golden rules:**
1. V+ = V− (virtual short)
2. I+, I− = 0 (no current into inputs)

**Inverting Amplifier:**
```
V+ = 0 → V− = 0 (virtual ground at − input)
I = Vin/Rin flows from Vin through Rin to virtual ground
Same I flows through Rf (no current into −): I = (0 − Vout)/Rf
→ (Vin/Rin) = −Vout/Rf
→ Av = Vout/Vin = −Rf/Rin
```

**Non-Inverting Amplifier:**
```
V+ = Vin → V− = Vin (virtual short)
Voltage divider at output: V− = Vout × R1/(R1+Rf)
Set V− = Vin: Vin = Vout × R1/(R1+Rf)
→ Av = Vout/Vin = (R1+Rf)/R1 = 1 + Rf/R1
```

**Comparison:**

| | Inverting | Non-Inverting |
|---|---|---|
| Gain | −Rf/Rin | 1 + Rf/R1 |
| Phase | 180° | 0° |
| Min gain | < −1 | ≥ 1 |
| Zin | Rin | Very high (GΩ) |

---

### PYQ 3 [May 2019, Q19b]: Integrator and Differentiator with square wave waveforms. [6 marks]

**Complete Solution:**

**Integrator:**

```
Circuit:
Vin ─┤R├──(−)──┬── Vout
               │
              [C] (feedback)
     GND─────(+)

Output: Vout = −(1/RC) × ∫Vin dt
```

*Square wave input (±V, period T) → Triangular wave output:*

- During Vin = +V: Vout ramps DOWN at rate = V/RC (slope = −V/RC)
- During Vin = −V: Vout ramps UP at rate = V/RC (slope = +V/RC)

```
Waveforms:
Vin:    +V  ─────┐        ┌─────
                 │        │
        −V       └────────┘

Vout:   ╲      ╱╲      ╱╲
         ╲    ╱  ╲    ╱  ╲
          ╲  ╱    ╲  ╱
           ╲╱      ╲╱

Triangular wave amplitude (one slope) = V × (T/2)/RC
```

**Differentiator:**

```
Circuit:
Vin ─┤C├──(−)──┬── Vout
               │
              [R] (feedback)
     GND─────(+)

Output: Vout = −RC × d(Vin)/dt
```

*Square wave input → spikes at transitions:*

- At rising edge (Vin: −V → +V): d(Vin)/dt = +∞ (impulse) → Vout = −RC × ∞ → large positive spike
- At falling edge (Vin: +V → −V): d(Vin)/dt = −∞ → large negative spike
- Between edges: d(Vin)/dt = 0 → Vout = 0

```
Waveforms:
Vin:    +V  ─────┐        ┌─────
                 │        │
        −V       └────────┘

Vout:   ↑        ↓        ↑        ↓
        │        │        │        │
       (spike   (spike   (spike   (spike
       +ve)     −ve)     +ve)     −ve)
    0V ─────────────────────────────
```

Spike amplitude = −RC × (2V/Tr), where Tr = rise time of the input square wave.
