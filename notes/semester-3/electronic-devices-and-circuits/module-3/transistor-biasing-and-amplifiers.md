# Transistor Biasing, Amplifiers, and Feedback

## 1. Explanation

### Why Biasing Matters — The Operating Point

A BJT transistor amplifies a signal by operating in the **active region** (emitter junction forward biased, collector junction reverse biased). To ensure the transistor stays in the active region throughout the AC signal swing, we must establish a **DC operating point (Q-point)** — the quiescent (no-signal) values of IC, VCE, and IB.

**Load line analysis:**

For a common-emitter circuit with VCC, RC:
```
KVL: VCC = IC × RC + VCE
→ IC = (VCC - VCE) / RC   [Load line equation]
```

This is a straight line on the IC-VCE plane:
- At VCE = 0: IC = VCC/RC (saturation boundary)
- At IC = 0: VCE = VCC (cutoff boundary)

The Q-point is where the DC bias sets the operating point on this load line.

**Ideal Q-point location:** Middle of the load line (VCE ≈ VCC/2) to allow maximum symmetric output swing without clipping.

**Thermal runaway:** If Q-point is not thermally stable, IC increases with temperature (ICBO doubles per 10°C) → more power dissipation → more heating → runaway destruction. The stability factor S = ΔIC/ΔICO must be minimized.

### Fixed Bias Circuit

```
        VCC
         │
        [RB]
         │
         ├──── Base
        [RC]      [BJT NPN]
         │    Collector──┤
       Vout               ├─── Emitter
         │                │
        GND              GND
```

**Analysis:**
```
IB = (VCC - VBE) / RB ≈ (VCC - 0.7) / RB
IC = β × IB
VCE = VCC - IC × RC

Stability factor: S = β + 1 ≈ β (very poor stability!)
```

**Disadvantage:** S = β (high), meaning a small change in ICBO causes large change in IC. Prone to thermal runaway. Poor for mass production (β varies widely: 50-300 for same transistor type).

### Self Bias (Emitter Bias)

```
        VCC
         │
        [RC]
         │
         Collector
        [NPN BJT]
         Emitter
         │
        [RE]  ← Emitter resistor (self-bias element)
         │
        GND

RB from VCC to Base
```

The emitter resistor RE provides **negative feedback**: if IC increases, VE = IC×RE increases, VBE = VB - VE decreases, IB decreases, IC decreases.

```
Stability factor: S = (β+1)×(RB+RE) / (β×RE + RB + RE)
If RE >> RB/β: S ≈ 1 (excellent stability)
```

### Voltage Divider Bias (Most Stable)

```
        VCC
         │
       [R1]
         │
         ├──── Base
       [R2]      [BJT NPN]
         │    Collector──┤
        GND               ├─── Emitter
                          │
                         [RE]
                          │
                         GND
```

The R1-R2 divider establishes a stable Thevenin base voltage:
```
VTH = VCC × R2/(R1+R2)
RTH = R1 || R2

Applying KVL to the base-emitter loop:
VTH = IB×RTH + VBE + IE×RE
Since IE ≈ IC = β×IB:
IB = (VTH - VBE) / (RTH + (β+1)×RE)

For a stiff voltage divider (RTH << (β+1)×RE):
VE ≈ VTH - VBE (independent of β!)
IE = VE/RE

Stability factor: S ≈ 1 + RTH/RE (approaches 1 for small RTH/RE)
```

This is the most commonly used biasing scheme — practical, stable, and β-independent.

### RC Coupled Amplifier

An RC coupled amplifier uses coupling capacitors to link stages while blocking DC.

```
                                   VCC
                                    │
        [CC1]          [RC]        [RC]         [CC2]
Vin ────||──── Base  Collector─────┤├────── Vout
              [NPN]                 │
              Emitter        [CE bypass cap]
              │
             [RE]────[CE]
              │
             GND
```

**Voltage gain in mid-frequency (Av):**
```
Av = -gm × RC' = -(IC/VT) × (RC || RL)

Where:
VT = 26mV at room temperature (thermal voltage)
gm = transconductance = IC/VT
RC' = RC || RL (effective collector resistance)
```

**Frequency response:**
```
             ↑ Gain (dB)
   0dB ──────────────────────── flat (mid-band)
             ╱        ╲
            ╱          ╲
  -3dB ───╱              ╲───
         fL              fH       → frequency (log scale)
```

- **Low-frequency cutoff (fL)**: Caused by coupling capacitors (CC1, CC2) and bypass capacitor CE. At low f, XC is large → capacitor blocks signal → gain drops.
  ```
  fL ≈ 1 / (2π × RC1 × CC1)   [for each stage]
  ```
- **High-frequency cutoff (fH)**: Caused by transistor's internal junction capacitances and stray capacitances. At high f, these capacitances short the signal to ground → gain drops.
- **Bandwidth (BW)** = fH - fL (mid-band range)

### Effect of Cascading (Multistage Amplifiers)

**Gain:** Cascading N stages multiplies voltage gains:
```
AV(total) = AV1 × AV2 × ... × AVN
In dB: AV(dB total) = AV1(dB) + AV2(dB) + ... + AVN(dB)
```

**Bandwidth:** Each stage's high-frequency cutoff reduces the overall bandwidth:
```
fH(N stages) ≈ fH(single) × √(2^(1/N) - 1)

For 2 identical stages: fH(2stage) ≈ 0.64 × fH(single) [bandwidth narrows by 36%]
For 3 identical stages: fH(3stage) ≈ 0.51 × fH(single)
```

**Trade-off:** More stages → higher total gain but narrower bandwidth. The gain-bandwidth product (GBW) is approximately constant for each transistor type.

### Feedback in Amplifiers — Effects of Negative Feedback

In a feedback amplifier:
```
Vout = A × (Vin - β × Vout)   [negative feedback]
Closed-loop gain: Af = A/(1 + Aβ)

Where: A = open-loop gain, β = feedback factor, Aβ = loop gain
```

**Effects of negative feedback (all beneficial at the cost of reduced gain):**

| Parameter | Effect of Negative Feedback | Formula |
|-----------|----------------------------|---------|
| Gain | Reduced | Af = A/(1+Aβ) |
| Gain stability | Improved | ΔAf/Af = (1/(1+Aβ)) × ΔA/A |
| Bandwidth | Increased | fH(f) = fH × (1+Aβ) |
| Distortion | Reduced | Df = D/(1+Aβ) |
| Noise | Reduced (if in forward path) | Nf = N/(1+Aβ) |
| Input impedance | Depends on topology: series increases Zin × (1+Aβ); shunt reduces |
| Output impedance | Depends: series reduces Zo/(1+Aβ); shunt increases |

**Four feedback topologies:**
1. Series-shunt (voltage-series): High Zin, Low Zo — voltage amplifier
2. Shunt-series (current-shunt): Low Zin, High Zo — current amplifier
3. Series-series (voltage-series current): High Zin, High Zo — transconductance amplifier
4. Shunt-shunt (current-shunt voltage): Low Zin, Low Zo — transresistance amplifier

### Common Source MOSFET Amplifier

```
        VDD
         │
        [RD]
         │
         Drain
       [N-MOSFET] ─── Gate ──── Vin (AC) through CC
         │
         Source ──── GND (with RS and CS bypass)
         │
        [RS]─[CS bypass]
         │
        GND
```

**Voltage gain:**
```
Av = -gm × (RD || RL)

Where gm = 2√(K × ID)   [MOSFET transconductance]
      K = process constant
      ID = drain current at Q-point
```

**Input impedance:** Zin = RG (gate resistance, very high since IG ≈ 0)
**Output impedance:** Zout ≈ RD

---

## 2. Example

### Voltage Divider Bias Q-Point Calculation

**Given:** VCC = 12V, R1 = 47kΩ, R2 = 10kΩ, RC = 2.2kΩ, RE = 1kΩ, β = 100

**Solution:**
```
VTH = VCC × R2/(R1+R2) = 12 × 10/(47+10) = 12 × 0.175 = 2.11V

RTH = R1 || R2 = 47k × 10k / (47k + 10k) = 470k/57k = 8.25kΩ

IE = (VTH - VBE) / (RE + RTH/(β+1))
   = (2.11 - 0.7) / (1000 + 8250/101)
   = 1.41 / (1000 + 81.7)
   = 1.41 / 1081.7
   = 1.3mA

IC ≈ IE = 1.3mA
VCE = VCC - IC(RC + RE) = 12 - 1.3mA × (2.2k + 1k) = 12 - 4.16 = 7.84V
```

Q-point: IC = 1.3mA, VCE = 7.84V — well centered in the active region. ✓

---

## 3. Applications and Use Cases

1. **Voltage Divider Bias in Audio Preamps**: All practical BJT audio preamplifiers use voltage divider bias for temperature stability and β-independence across manufacturing.

2. **RC Coupled Amplifiers in Hearing Aids**: Multi-stage RC coupled amplifiers (3-4 stages) amplify the microphone signal by 60-80dB in hearing aid circuits.

3. **Feedback in Op-Amps**: Op-amps use massive negative feedback (loop gain ~10⁵) to achieve stable, predictable gain, low distortion, and low output impedance — all the benefits of NFB.

4. **Common Source MOSFET in Low-Noise RF Amplifiers**: The first stage of a WiFi/LTE receiver uses a common-source MOSFET LNA (Low Noise Amplifier) for its high input impedance and low noise.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: RC Coupled Amplifier Design [May 2019, Q12]

**Problem:** Design an RC Coupled Amplifier with:
- VCC = 12V DC
- IC = 2mA
- hfe (β) = 125
- Lower cut-off frequency fL = 100Hz
- Upper cut-off frequency fH = 100kHz

**Solution:**

**Step 1: Choose Q-point and calculate RC**

For VCE = VCC/2 = 6V (midpoint for maximum swing):
```
VCE + IC×RC + IE×RE = VCC
With VE = 1V (typical: 10% of VCC for thermal stability):
IC × RC = VCC - VCE - VE = 12 - 6 - 1 = 5V
RC = 5V / IC = 5V / 2mA = 2.5kΩ → use 2.2kΩ (standard)

RE = VE / IE ≈ VE/IC = 1V / 2mA = 500Ω → use 470Ω
```

**Step 2: Bias resistors (voltage divider)**
```
VB = VE + VBE = 1 + 0.7 = 1.7V

Rule of thumb: IR1 = 10 × IB (make divider stiff)
IB = IC/β = 2mA/125 = 16μA
IR1 = 10 × 16 = 160μA

R1 + R2 = VCC / IR1 = 12 / 160μA = 75kΩ
R2 = VB / IR1 = 1.7 / 160μA = 10.625kΩ → use 10kΩ
R1 = 75kΩ - 10kΩ = 65kΩ → use 68kΩ (standard)
```

**Step 3: Coupling capacitor CC1 (for fL = 100Hz)**
```
The input coupling capacitor CC1 forms a high-pass filter with Rin = R1||R2||hie

hie = β/gm = β × VT/IC = 125 × 26mV/2mA = 1625Ω

Rin = R1||R2||hie = 68k||10k||1.625k ≈ 1.35kΩ

For fL = 100Hz:
CC1 = 1 / (2π × fL × Rin) = 1 / (2π × 100 × 1350) = 1.18μF → use 2.2μF (next standard value)
```

**Step 4: Bypass capacitor CE**
```
CE must bypass RE at fL. The resistance seen at emitter = RE || (1/gm + RS'/β)
Approximate: RE_eff ≈ 1/gm = VT/IC = 26/2 = 13Ω

CE = 1 / (2π × fL × 13) = 1 / (2π × 100 × 13) = 122μF → use 150μF (standard)
```

**Step 5: Voltage gain (mid-band)**
```
Av = -gm × RC' = -(IC/VT) × RC
   = -(2mA/26mV) × 2.2kΩ
   = -76.9 × 2200 / 1000
   = -169 (magnitude = 169)
   
In dB: 20 log(169) = 44.6dB
```

**Summary of designed component values:**
- RC = 2.2kΩ, RE = 470Ω
- R1 = 68kΩ, R2 = 10kΩ
- CC1 = 2.2μF, CE = 150μF
- Voltage gain ≈ 169 (44.6dB)
- fL ≈ 100Hz, fH limited by transistor fT

---

### Example 2: Effect of Cascading on Bandwidth [May 2019, Q13a]

**Problem:** What are the effects of cascading on the gain and bandwidth of transistor amplifier circuits? [3 marks]

**Solution:**

**Effect on Gain:**

For n identical stages, each with voltage gain Av:
```
Total gain: AV(total) = Av^n

Example: 3 stages × 40dB each = 120dB total (gain of 10⁶)
```

Gain INCREASES by multiplication (addition in dB) — this is the primary reason for cascading.

**Effect on Bandwidth:**

Each stage's high-frequency cutoff frequency fH decreases the overall bandwidth:
```
fH(n stages) = fH(single) × √(2^(1/n) - 1)

For n=1: fH = fH (reference)
For n=2: fH ≈ 0.64 × fH (36% reduction)
For n=3: fH ≈ 0.51 × fH (49% reduction)
For n=4: fH ≈ 0.44 × fH (56% reduction)
```

Similarly, for the low-frequency end:
```
fL(n stages) = fL(single) / √(2^(1/n) - 1)

For n=2: fL ≈ 1.56 × fL (low-frequency end rises by 56%)
```

**Net effect:** Each additional stage narrows the bandwidth from both ends, while multiplying the gain. The **gain-bandwidth product (GBW)** of the transistor remains approximately constant:

```
GBW = Av × fH = constant (= fT, transition frequency of transistor)
```

**Conclusion:** Cascading is beneficial only when high gain is needed and bandwidth sacrifice is acceptable. For broadband applications (e.g., oscilloscopes, 1GHz+ amplifiers), careful design is needed to maintain bandwidth with each cascade stage.

---

### Example 3: Wien Bridge Oscillator using Transistors [May 2019, Q13b]

**Problem:** Sketch and explain a Wien Bridge Oscillator using transistors. Explain how conditions for sustained oscillations are satisfied. [6 marks]

**Solution:**

**Circuit sketch:**

```
              VCC
               │
              [RC2]
               │
    [CC1]    Collector [Q2]
Vin ──||─── Base [Q1] ── Base [Q2] ── Vout
            Emitter [Q1]   Emitter [Q2]
               │               │
             [RE1]           [RE2]
               │               │
              GND             GND

Feedback network (Wien bridge):
Vout ──┬──[R]──[C]──┬── Base of Q1
       │             │
      [C]   [2R] ─ [R]
       │             │
      GND           GND (voltage divider 2R from Vout to GND, R from node to GND)
```

**Simplified two-stage RC coupled amplifier with Wien network:**

The two-stage BJT amplifier provides positive feedback through the Wien RC network:

**Wien network frequency-selective feedback:**

The Wien network consists of:
- Series RC arm: R in series with C (from Vout to middle node)
- Parallel RC arm: R in parallel with C (from middle node to GND)

Transfer function of Wien network at the frequency of oscillation:
```
At ω₀ = 1/(RC):
Feedback fraction β = 1/3
Phase shift = 0° (the feedback is in phase with input at this frequency only)
```

**Barkhausen Criterion for Oscillation:**
1. **Loop gain |Aβ| = 1**: The amplifier must provide gain exactly equal to 3 (to compensate for β = 1/3 attenuation of Wien network)
2. **Total phase shift = 0°** (or 360°): 
   - Two-stage BJT amplifier: each stage inverts (180° each) → total 360° = 0° net phase
   - Wien network at ω₀ = 1/(RC): 0° additional phase
   - **Total: 0°** ✓ → Positive feedback → Oscillation

**Oscillation frequency:**
```
f₀ = 1 / (2π × R × C)

Example: R = 10kΩ, C = 0.01μF
f₀ = 1 / (2π × 10⁴ × 10⁻⁸) = 1 / (2π × 10⁻⁴) = 1591 Hz ≈ 1.59kHz
```

**Gain requirement:**
- Wien network attenuation = 1/3
- Amplifier must have Av ≥ 3
- The gain is set by: Av = 1 + RF/R1 (if using op-amp) or equivalent with BJT stages

**Why Wien bridge oscillator is preferred for audio frequencies:**
- Low distortion (near-sinusoidal output)
- Frequency easily tunable by changing R or C (use gang-switched capacitors or twin-gang potentiometer)
- Stable amplitude when AGC (Automatic Gain Control) is used (thermistor or FET in feedback controls gain)

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q8]: Explain thermal runaway in transistors. [3 marks]

**Complete Solution:**

**Definition:** Thermal runaway is a destructive positive feedback cycle in BJT transistors where increasing temperature leads to increasing collector current, which further increases dissipation and temperature, eventually destroying the transistor.

**Mechanism — Step by Step:**

1. **Initial heating**: Power dissipation PD = VCE × IC heats the transistor junction.
2. **ICBO doubles per 10°C**: The reverse leakage current ICBO (minority carrier leakage through base-collector junction) approximately doubles for every 10°C rise in junction temperature.
3. **IC increases with ICBO**: IC = β×IB + (β+1)×ICBO. As ICBO increases, IC increases even with constant IB.
4. **More power dissipation**: Higher IC → more PD = VCE × IC → more heat generated.
5. **Cycle repeats**: More heat → ICBO doubles → IC increases more → more heat → **runaway**.
6. **Destruction**: Junction temperature exceeds maximum rating (150°C for silicon) → transistor destroys itself.

**Prevention strategies:**
1. **Emitter resistance RE**: Creates self-stabilizing negative feedback (voltage divider bias). As IC↑ → VE = IC×RE ↑ → VBE reduces → IB reduces → IC pulled back.
2. **Heat sink**: Keeps junction temperature low, reducing ICBO sensitivity.
3. **Thermistor biasing**: NTC thermistor in bias network compensates for temperature-related current increase.
4. **Circuit stability factor S**: Design for S < 10 to prevent runaway. S = ΔIC/ΔICO.

---

### PYQ 2 [May 2019, Q14]: With neat sketches and waveforms, explain the working of an Astable Multivibrator using transistors. [9 marks]

**Complete Solution:**

**Circuit:**
```
          VCC
           │
     [RC1] │ [RC2]
       │   │   │
  ─────┤   │   ├─────
  │C1  │   │   │  C2│
  └────┤Q1 │ Q2├────┘
       │   │   │
      [RE1]   [RE2]
       │         │
      GND       GND

Base of Q1 ←── C2 coupling ──── Collector of Q2
Base of Q2 ←── C1 coupling ──── Collector of Q1
```

**More precise circuit:**
```
VCC ─────┬───[RC1]────┬────[RC2]───┬──── VCC
         │            │            │
        [RB1]     Q1  C  Q2      [RB2]
         │     B──┤    ├──B        │
         └──────  E    E  ─────────┘
                  │    │
                 GND  GND

C1 couples Q1 Collector → Q2 Base
C2 couples Q2 Collector → Q1 Base
```

**Operation (Free-running, no input required):**

**State 1 (Q1 ON, Q2 OFF):**
- Q1 is saturated: VCE1 ≈ 0.2V (collector at near GND)
- Q1 collector low → through C2, Q2 base is driven negative → Q2 OFF
- C2 begins charging through RB2 from VCC toward +VCC
- C1 charges through RC1 and Q2's circuit

**Timing for Q2 to turn ON:**
- When C2 charges enough to bring Q2 base to +0.7V: Q2 turns ON
- Q2 ON → Q2 collector goes low → C1 now drives Q1 base negative → Q1 OFF

**State 2 (Q2 ON, Q1 OFF):** (Mirror of State 1, now timing C1 through RB1)

**Oscillation frequency:**

Time for each half cycle:
```
t1 = 0.69 × RB2 × C2   (time Q1 is ON = time C2 charges to switch Q2)
t2 = 0.69 × RB1 × C1   (time Q2 is ON = time C1 charges to switch Q1)

Total period: T = t1 + t2 = 0.69(RB1×C1 + RB2×C2)

For symmetric design (RB1 = RB2 = R, C1 = C2 = C):
T = 1.38 × R × C
f = 1/T = 0.72/(RC)
```

**Waveforms:**

```
VCE1:
  VCC ──────┐    ┌──────────┐    ┌────
            │    │          │    │
  0.2V      └────┘          └────┘
             ← t2 →← t1  →← t2 →

VCE2 (complementary):
  VCC      ┌──────────┐    ┌────────
            │          │    │
  0.2V ────┘          └────┘
             ← t2 →← t1 →← t2 →

VB2 (base of Q2):
  +0.7V               .....
            ╲         ╱
   0V        ╲       ╱    ← exponential charging toward VCC
              ╲     ╱
  -VCC  ─────────────  ← driven negative when Q1 turns on
```

**Design equations summary:**
```
f₀ = 0.72 / (R × C)   [for symmetric design R = RB1 = RB2, C = C1 = C2]
Duty cycle = t1/T = 50% (for symmetric)
For asymmetric: duty cycle = t1/(t1+t2) = RB2×C2 / (RB1×C1 + RB2×C2)
```

**Example calculation:** For f = 1kHz with C = 0.01μF:
```
R = 0.72 / (f × C) = 0.72 / (1000 × 0.01×10⁻⁶) = 72kΩ → use 68kΩ
```
