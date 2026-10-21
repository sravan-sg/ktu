# Operational Amplifiers (Op-Amps)

## 1. Explanation

### Core Intuition: The Perfect Amplifier

An **Operational Amplifier (op-amp)** is a high-gain, direct-coupled differential amplifier with extremely high input impedance and very low output impedance. The name "operational" comes from its original purpose in analog computers: performing mathematical *operations* (addition, subtraction, integration, differentiation) on electrical signals.

The key insight is that when **negative feedback** is applied around an op-amp with very high open-loop gain (A_OL ≈ 10⁵ to 10⁶), the closed-loop behavior becomes determined almost entirely by the **external feedback network**, not the op-amp internals. This is the "virtual short" principle.

### Differential Amplifier — The Core Building Block

The first stage of every op-amp is a **differential amplifier** that amplifies the *difference* between two input signals:

```
          VCC
           │
     [RC] [RC]
      │     │
      ├─────┤ ← Differential output (Vo = A(V₁ - V₂))
      │     │
   [Q1]   [Q2] ← Matched NPN transistors
      │     │
     [RE_common] or current mirror
      │
     VEE (negative supply)

V₁ → Base of Q1 (non-inverting input: +)
V₂ → Base of Q2 (inverting input: -)
```

**CMRR (Common Mode Rejection Ratio):**
```
CMRR = Ad / Ac = (Differential gain) / (Common mode gain)

In dB: CMRR(dB) = 20 log(Ad/Ac)

For IC741: CMRR_min = 70dB, typical = 90dB
```

High CMRR means the op-amp ignores noise/interference that appears equally on both inputs (common-mode), while amplifying the difference signal. Essential in noisy industrial environments.

### Op-Amp Characteristics: Ideal vs Practical (IC 741)

| Parameter | Ideal Op-Amp | IC 741 (Practical) |
|-----------|-------------|---------------------|
| Open-loop gain AOL | ∞ | 200,000 (106dB) |
| Input impedance Zin | ∞ | 2 MΩ |
| Output impedance Zout | 0 | 75 Ω |
| Bandwidth (BW) | ∞ | 1 MHz (unity gain bandwidth) |
| CMRR | ∞ | 90 dB (typ) |
| Slew rate | ∞ | 0.5 V/μs |
| Input offset voltage | 0 | ±2 mV (max 6mV) |
| Input bias current | 0 | 80 nA (typ) |
| Input offset current | 0 | 20 nA (typ) |
| Supply voltage | Any | ±5V to ±18V |

**Slew Rate (SR):** Maximum rate at which the output voltage can change, regardless of input:
```
SR = ΔVout/Δt (maximum) = 0.5 V/μs for IC 741

For a sinusoidal output Vm sin(ωt), maximum rate of change = ω × Vm:
Full-power bandwidth: f_max = SR / (2π × Vm)

For Vm = 10V with IC 741:
f_max = 0.5×10⁶ / (2π × 10) = 7.96kHz

Above f_max, the output is slew-rate limited (triangular, not sinusoidal)
```

**Input offset voltage (Vio):** The differential input voltage required to make output exactly zero. Caused by manufacturing mismatch in differential pair. Contributes to DC error in precision circuits.

**Gain-Bandwidth Product (GBW):**
```
For 741: GBW = AOL × f_3dB = 200,000 × 5Hz ≈ 1 MHz (constant)

At unity gain (Av = 1): bandwidth = 1 MHz
At gain = 10: bandwidth = 100 kHz
At gain = 100: bandwidth = 10 kHz
```

### The "Virtual Short" Principle

When negative feedback is applied to an ideal op-amp:
```
Vout = AOL × (V+ - V-)
Since AOL → ∞ and Vout is finite:
(V+ - V-) → 0 → V+ ≈ V-
```

This means the two input terminals appear to be at the same potential — a **virtual short circuit** (NOT an actual short — no current flows between them due to infinite input impedance).

**The two golden rules of op-amp analysis:**
1. V+ = V- (virtual short)
2. I+ = I- = 0 (no current into op-amp inputs)

These two rules let you analyze almost any op-amp circuit without knowing AOL.

### Op-Amp Applications

#### 1. Scale Changer (Inverting Amplifier)

```
         Rf
    ┌────┤├────┐
    │          │
Vin─┤├────(─)──┴── Vout
    Rin    (+)
            │
           GND
```

**Analysis using virtual short:**
- V- = V+ = 0V (virtual ground)
- Current through Rin: I = Vin/Rin
- Same current through Rf (no current into -input): Vout = -I × Rf = -(Rf/Rin) × Vin

```
Av = Vout/Vin = -Rf/Rin
```

The negative sign means inversion (180° phase shift). Scale factor = Rf/Rin.

#### 2. Sign Changer (Unity-Gain Inverter)

Set Rf = Rin:
```
Av = -Rf/Rin = -1
Vout = -Vin (inverted, same amplitude)
```

#### 3. Summing Amplifier (Adder)

```
        Rf
   ┌────┤├────┐
   │          │
V1─┤├──(−)───┴── Vout
   R1   │
V2─┤├───┘ (virtual ground at -input)
   R2
V3─┤├
   R3
```

**Analysis:**
```
I1 = V1/R1, I2 = V2/R2, I3 = V3/R3
I_total = I1 + I2 + I3 (all into virtual ground)
Vout = -Rf × (V1/R1 + V2/R2 + V3/R3)

For R1 = R2 = R3 = R:
Vout = -(Rf/R) × (V1 + V2 + V3)

For Rf = R: Vout = -(V1 + V2 + V3)  [inverting adder]
```

#### 4. Subtractor (Difference Amplifier)

```
         R2
    ┌────┤├────┐
    │          │
V1──┤├───(−)──┴── Vout
    R1    (+)
           │
V2──┤├────┤├── GND
    R3    R4
```

For R1=R2=R3=R4=R:
```
Vout = V2 - V1  [differential output, rejects common mode]
CMRR depends on matching of resistors
```

#### 5. Integrator

```
         C
    ┌────||────┐
    │          │
Vin─┤├───(−)──┴── Vout
    R     (+)
           │
          GND
```

**Analysis:**
```
Virtual ground → V- = 0 → current through R: I = Vin/R
This current charges C: Vout = -(1/RC) × ∫Vin dt

Frequency domain: H(jω) = -1/(jωRC)
At ω → 0: |H| → ∞ (integrator has infinite DC gain → practical circuits need feedback resistor in parallel with C)
```

The output is proportional to the **integral** of the input. Square wave input → triangular output.

#### 6. Differentiator

```
         R
    ┌────┤├────┐
    │          │
Vin─||───(−)──┴── Vout
    C     (+)
           │
          GND
```

**Analysis:**
```
Current through C: I = C × d(Vin)/dt
Vout = -I × R = -RC × d(Vin)/dt

Frequency domain: H(jω) = -jωRC
```

Amplifies high frequencies → susceptible to noise. In practice, a small resistor RS in series with C limits high-frequency gain.

#### 7. Schmitt Trigger (Comparator with Hysteresis)

```
         Rf
    ┌────┤├────┐
    │          │
Vin─(+)  (−)──┴── Vout
    ↑     │
    │    GND (or Vref)
   Feedback to + through R1
```

**Non-inverting Schmitt trigger** with positive feedback:

```
UTP (Upper Threshold) = +Vsat × R1/(R1+Rf)
LTP (Lower Threshold) = -Vsat × R1/(R1+Rf)
Hysteresis = UTP - LTP = 2×Vsat×R1/(R1+Rf)
```

**Operation:**
- When Vin > UTP: Vout = +Vsat (snaps high)
- When Vin < LTP: Vout = -Vsat (snaps low)
- Between LTP and UTP: Vout holds current state (hysteresis prevents noise-induced chatter)

**Application:** Converts noisy sine/triangle wave to clean square wave. Used in comparators, zero-crossing detectors, Schmitt-trigger inverters (74HC14).

#### 8. Wien Bridge Oscillator using Op-Amp

Inverting op-amp with gain ≥ 3 (set by Rf = 2R1) plus Wien network:
```
f₀ = 1/(2πRC)
Gain for oscillation: Av = 1 + Rf/R1 = 3 → Rf = 2R1
```

---

## 2. Example

### Summing Amplifier Realization [May 2019 Q19a]

**Problem:** Realize Y(t) = 5V1 + 2V2 – 4V3 using op-amps.

**Solution:**

This requires multiplication of each input by different gains AND subtraction. We need:
- Stage 1: Summing amplifier for V1 and V2 with gains 5 and 2
- Stage 2: A subtractor, or use a sign changer then another summer

**Simplest approach (2 op-amps):**

**Stage 1 — Inverting Summer:**
```
-(5V1 + 2V2): Set Rf = 10kΩ
- R1 for V1: R1 = Rf/5 = 10k/5 = 2kΩ
- R2 for V2: R2 = Rf/2 = 10k/2 = 5kΩ

Output1 = -(5V1 + 2V2)
```

**Stage 2 — Inverting Summer to subtract V3 and invert Stage 1 output:**
```
Vout = -(−(5V1+2V2) × (Rf2/Rf1) − V3 × (Rf2/RV3))
     = 5V1 + 2V2 − 4V3

Set Rf2 = 4kΩ:
- For Stage 1 output: gain = 1 → R = 4kΩ
- For V3: gain = 4 → RV3 = Rf2/4 = 4k/4 = 1kΩ

Vout = -(-1×(5V1+2V2) - 4V3) = 5V1 + 2V2 - 4V3 ✓
```

---

## 3. Applications and Use Cases

1. **Summing Amplifier in Audio Mixers**: Mixing multiple audio channels (guitar, vocals, drums) into one output signal. Each channel has its own gain (volume) controlled by Rin.

2. **Integrator in Analog-to-Digital Conversion**: Dual slope ADC uses an integrator to charge a capacitor linearly, then time the discharge — this time is proportional to the analog input.

3. **Differentiator in Edge Detection**: Differentiator circuits detect the edges (rapid changes) in digital or video signals — used in image processing, servo control.

4. **Schmitt Trigger in Digital Interfaces**: RS-232, USB signal conditioning, and any interface receiving signals over long cables uses Schmitt trigger inputs to reject noise.

5. **Differential Amplifier in ECG Machines**: Electrocardiograph (ECG) amplifiers use differential amplifiers to extract the tiny heart signal (1mV) while rejecting 60Hz common-mode mains interference.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: CMRR and Slew Rate Analysis [May 2019, Q17b]

**Problem:** Explain the terms CMRR and Slew Rate of an OPAMP. Also specify the typical values for IC 741. [4 marks]

**Solution:**

**CMRR (Common Mode Rejection Ratio):**

The op-amp output due to differential signal Vd = V1 - V2 is: Vo(diff) = Ad × Vd

The op-amp output due to common-mode signal Vc = (V1+V2)/2 is: Vo(cm) = Ac × Vc

An ideal op-amp rejects Vc completely (Ac = 0, CMRR = ∞). Practical op-amps have finite CMRR.

```
CMRR = Ad / Ac

In dB: CMRR(dB) = 20 log10(Ad/Ac)

For IC 741:
- Ad (differential gain) = 200,000 (at DC)
- CMRR(min) = 70dB, CMRR(typical) = 90dB

From 90dB: Ac = Ad / 10^(90/20) = 200,000 / 31,623 = 6.3
(Common-mode signal is attenuated by factor 31,623 compared to differential signal)
```

**Slew Rate:**

The slew rate is the maximum rate of change of op-amp output voltage:
```
SR = |dVout/dt|_max

For IC 741: SR = 0.5 V/μs = 500,000 V/s

If a step input of 10V is applied:
Time to slew: Δt = ΔV/SR = 10V / 0.5V/μs = 20μs
The output takes 20μs to reach 10V, not instantaneously.
```

**Impact of slew rate on sinusoidal signals:**

Maximum slope of Vm sin(ωt) = ω × Vm (at zero crossing)
For output to follow without slewing: ω × Vm ≤ SR

Full-power bandwidth:
```
f_max = SR / (2π × Vm)

For IC 741 with Vm = 10V:
f_max = 0.5×10⁶ / (2π × 10) = 7.96kHz ≈ 8kHz

Above 8kHz with 10V amplitude: output is triangular (slew-rate limited), not sinusoidal.
```

---

### Example 2: Inverting Amplifier Gain Derivation [May 2019, Q17a]

**Problem:** Derive an expression for voltage gain of an inverting and non-inverting operational amplifier. [6 marks]

**Solution:**

**Inverting Amplifier:**

Circuit: Input Vin through Rin to inverting (-) input. Feedback resistor Rf from output to (-) input. Non-inverting (+) input grounded.

Using **virtual short principle** (V+ = V- = 0 → inverting input is at virtual ground):

KCL at inverting input node:
```
I_Rin = I_Rf + I_in(op-amp)

Since I_in(op-amp) = 0 (ideal op-amp):
I_Rin = I_Rf

Vin/Rin = -Vout/Rf    (note: Vout appears negative because current flows INTO virtual ground through Rf FROM output)

Vout/Vin = -Rf/Rin

Av(inverting) = -Rf/Rin
```

The negative sign indicates 180° phase inversion.

**Non-Inverting Amplifier:**

Circuit: Input Vin connected to non-inverting (+) input. Feedback divider R1 (from output to -) and R2 (from - to ground).

Using virtual short (V- = V+ = Vin):

KCL at inverting input node:
```
I through R2: I = V-/R2 = Vin/R2
I through R1: I = (Vout - V-)/R1 = (Vout - Vin)/R1

Since same current (no current into op-amp):
Vin/R2 = (Vout - Vin)/R1

Vin × R1 = Vout × R2 - Vin × R2
Vin(R1 + R2) = Vout × R2
Vout/Vin = (R1 + R2)/R2 = 1 + R1/R2

Av(non-inverting) = 1 + Rf/R1 (where Rf is the top feedback resistor and R1 is the bottom resistor to ground)
```

Always positive → non-inverting. Minimum gain = 1 (voltage follower when Rf = 0, R1 = ∞).

**Summary:**

| Configuration | Gain | Phase | Input impedance |
|---------------|------|-------|----------------|
| Inverting | -Rf/Rin | 180° | Rin (finite) |
| Non-inverting | 1 + Rf/R1 | 0° | Very high (Zin of op-amp × AOL) |
| Voltage follower | 1 | 0° | Maximum (entire AOL × Zin) |

---

### Example 3: Schmitt Trigger Design [May 2019, Q18a]

**Problem:** Draw and explain the circuit of a Schmitt Trigger using OPAMPS. Explain the terms UTP and LTP. [6 marks]

**Solution:**

**Non-Inverting Schmitt Trigger Circuit:**
```
                          Vout
                           │
         ┌─────[Rf]────────┘
         │
Vin ──(+)────── Vout
       │
      (−)
       │
      GND (or Vref for shifted thresholds)
```

**Wait — Non-inverting Schmitt uses positive feedback to + input:**

```
Vin ──(+)── 
       (−)── GND
              
Feedback: Vout──[Rf]──(+)
          GND──[R1]──(+)

Vout connects through Rf to + input; R1 from + input to GND forms voltage divider
```

**Correct circuit:**
```
          ┌──[Rf]──┐
          │        │
Vin ─── (+)      Vout ──── (to load)
         (−)
          │
         GND

Positive feedback: Vout fed back through R1-R2 divider to (+) input:
         (+) input voltage = Vout × R1/(R1+R2)
```

**Threshold calculation:**

UTP (Upper Threshold Point) — level at which output switches from LOW to HIGH:
```
When Vout = +Vsat:
V(+) = +Vsat × R1/(R1+R2)
UTP = Vsat × R1/(R1+R2)
```

LTP (Lower Threshold Point) — level at which output switches from HIGH to LOW:
```
When Vout = -Vsat:
V(+) = -Vsat × R1/(R1+R2)
LTP = -Vsat × R1/(R1+R2)
```

**Hysteresis = UTP - LTP = 2 × Vsat × R1/(R1+R2)**

**Operation:**
1. Initially Vout = +Vsat → V(+) = UTP (high)
2. As Vin rises toward UTP: When Vin > UTP → output snaps to -Vsat → V(+) drops to LTP
3. As Vin falls toward LTP: When Vin < LTP → output snaps to +Vsat → V(+) rises to UTP

**Hysteresis prevents noise-induced false triggering** — a noise spike must be large enough to cross the full hysteresis window to cause a false output change.

**Design example:** Vsat = 13V, R1 = 10kΩ, R2 = 100kΩ:
```
UTP = 13 × 10/(10+100) = 13 × 0.0909 = 1.18V
LTP = -1.18V
Hysteresis = 2.36V
```

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q15a]: Draw and explain the circuit of a differential amplifier. [5 marks]

**Complete Solution:**

**Circuit:**
```
               VCC (+12V)
                │
           [RC] [RC]    ← equal collector resistors (matched)
            │     │
            ├─────┤ ← differential output Vo = A(V1 - V2)
       Q1-C   Q2-C
V1──B──Q1     Q2──B──V2
       Q1-E   Q2-E
            └──┬──┘ ← emitters tied together
             [Iee] or RE
               │
              VEE (-12V)
```

(In practical op-amps, RE is replaced by a **constant current source** for maximum CMRR)

**Working — Differential Mode:**

When V1 ≠ V2 (differential signal):
- V1 > V2 → Q1 draws more current → VCE1 drops → Vc1 drops
- Q2 draws less current → VCE2 rises → Vc2 rises
- Differential output: Vod = Vc2 - Vc1 = Ad(V1 - V2)
- Ad = gm × RC (differential gain)

**Working — Common Mode:**

When V1 = V2 = Vcm (common noise):
- Both Q1, Q2 receive identical signals
- By symmetry: ΔVc1 = ΔVc2 (both change by same amount)
- Differential output: Vod = Vc2 - Vc1 = 0 (ideally)
- Common-mode gain Ac → 0 for perfectly matched transistors and large emitter resistance

**CMRR depends on:**
1. Matching of Q1 and Q2 (hfe, VBE)
2. Matching of RC resistors
3. Value of emitter resistance (or constant current source IEE)
4. Temperature symmetry

**Typical single-ended output (Vc2 referenced to GND):**
```
Vout = -gm × RC × (V1 - V2) / 2   [from one collector, single-ended]
Ad_single = -gm × RC / 2
```

---

### PYQ 2 [May 2019, Q16a]: Derive voltage gain of inverting and non-inverting op-amp. [6 marks]

**Complete Solution:** *(Full derivation provided in Solved Example 2 above — restated here for self-containment)*

**Golden rules used:**
1. V+ = V- (virtual short — because AOL → ∞ and feedback keeps differential input ≈ 0)
2. I+ = I- = 0 (infinite input impedance — no current flows into either terminal)

**Inverting amplifier: Av = -Rf/Rin**

Proof: V- = V+ = 0 (GND). Current through Rin = Vin/Rin. Same current (by KCL at V- node) flows through Rf. Vout = 0 - I×Rf = -(Rf/Rin)×Vin.

**Non-inverting amplifier: Av = 1 + Rf/R1**

Proof: V- = V+ = Vin. Voltage divider at output: V- = Vout × R1/(R1+Rf). Since V- = Vin: Vin = Vout × R1/(R1+Rf) → Vout = Vin × (R1+Rf)/R1 = Vin × (1 + Rf/R1).
