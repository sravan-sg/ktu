# Transistor Biasing, Amplifiers, and Feedback

## 1. Explanation

### BJT Recap: Regions of Operation

Before biasing, understand where a BJT operates:

| Region | BE Junction | BC Junction | IB | IC | VCE | Use |
|--------|------------|------------|----|----|-----|-----|
| Cutoff | Reverse | Reverse | ≈0 | ≈0 | ≈VCC | Switch OFF |
| Active (linear) | Forward | Reverse | Small | β×IB | VCE = VCC - IC×RC | Amplifier |
| Saturation | Forward | Forward | Large | VCC/RC | ≈0.2V | Switch ON |

**For amplification:** BJT must always be in the **active region** throughout the entire AC signal swing.

### DC Load Line and Q-Point — Deep Dive

**Load line equation** (from KVL around output loop):
```
VCC = IC × RC + VCE
→ IC = VCC/RC - VCE/RC   [straight line on IC-VCE axes]
```

**Two intercepts:**
- **Saturation point (VCE = 0):** IC = VCC/RC (maximum possible IC)
- **Cutoff point (IC = 0):** VCE = VCC (maximum possible VCE)

**AC load line:** When AC signal is applied, the effective load seen by the transistor changes. The AC load line has a different (steeper) slope than the DC load line because the coupling capacitor connects the external load RL in parallel with RC for AC:

```
AC load line slope = -1/(RC || RL)
DC load line slope = -1/RC

AC load line passes through Q-point with steeper slope.
```

**Maximum output voltage swing:**

```
For symmetric clipping (Q-point at center of AC load line):
Vout(max) = ICQ × (RC || RL)   [positive peak]
         = VCEQ - VCE(sat)     [negative peak]

For maximum symmetric swing: set ICQ × (RC||RL) = VCEQ - VCE(sat)
This gives the optimum Q-point for maximum undistorted output power.
```

**Stability factor S:**
```
S = ΔIC / ΔICBO   [sensitivity of IC to reverse leakage ICBO]

S = 1: Perfect stability (IC independent of ICBO) — theoretical ideal
S = β+1: Fixed bias (worst case) — any ICBO change amplified β+1 times
```

### Fixed Bias — Analysis and Limitations

**Circuit:**
```
        VCC
         │
        [RB]──────────── Base
         │               │
                      [Q NPN]
        [RC]──── Collector─┤
         │               Emitter ── GND
        Vout               │
         │
        GND
```

**DC Analysis:**
```
Apply KVL to base-emitter loop:
VCC - IB×RB - VBE = 0
IB = (VCC - VBE) / RB = (VCC - 0.7) / RB

IC = β × IB
VCE = VCC - IC × RC

Stability factor: S = (β+1) ≈ β   [very poor!]
```

**Why is fixed bias unstable?**

If β changes from 100 to 200 (within same transistor type's manufacturing spread):
```
IB = constant (set by RB)
IC = β × IB → doubles!
VCE = VCC - 2×IC×RC → may saturate the transistor entirely
```

**Practical use:** Only in switching circuits (where saturation/cutoff is OK), never for linear amplifiers.

### Emitter Bias (Self-Bias) — RE Feedback Analysis

**Circuit:**
```
        VCC
         │
        [RC]
         │  Collector
        [NPN BJT]
         │  Emitter
        [RE] ← feedback element
         │
        GND

RB from VCC to Base
```

**Analysis:**
```
KVL (outer loop): VCC = IB×RB + VBE + IE×RE
IE ≈ (β+1)×IB

IB = (VCC - VBE) / (RB + (β+1)×RE)
IC = β × IB

Stability factor:
S = (β+1) / (1 + β×RE/(RB+RE))
  = (β+1)(RB+RE) / (β×RE + RB + RE)

If RB >> RE: S → β+1 (like fixed bias)
If RE >> RB/β: S → 1 + RB/RE ≈ 1 (excellent)
```

**Physical intuition for RE feedback:**
```
If temperature rises → ICBO rises → IC rises → VE = IC×RE rises
→ VBE = VB - VE decreases (since VB is held by RB from VCC)
→ IB decreases → IC decreases → corrects itself!
```

The emitter resistor creates **automatic gain control** for the DC bias.

**Disadvantage:** RE also appears in the AC signal path → RE reduces AC voltage gain!
```
Without bypass capacitor CE: Av = -gm×RC / (1 + gm×RE) ≈ -RC/RE (heavily reduced)
With bypass capacitor CE (XCE ≈ 0 at signal frequency): Av = -gm×RC (full gain restored)
```

### Voltage Divider Bias — The Industry Standard

**Circuit:**
```
        VCC
         │
       ┌─┤R1├─┐
       │       │ Base
       │    [NPN BJT]
       └─┤R2├─┤ Collector ──[RC]── VCC
               │ Emitter
              [RE]────[CE (bypass)]
               │
              GND
```

**Thevenin equivalent analysis:**

Replace R1-R2-VCC network seen from the base terminal with its Thevenin equivalent:
```
VTH = VCC × R2/(R1+R2)   [Thevenin voltage = open circuit base voltage]
RTH = R1 || R2            [Thevenin resistance = R1 in parallel with R2]
```

**DC Analysis with Thevenin equivalent:**
```
KVL around base-emitter Thevenin loop:
VTH = IB×RTH + VBE + IE×RE
IE = (β+1)×IB

IB = (VTH - VBE) / (RTH + (β+1)×RE)
IC ≈ β × IB

Condition for β-independent operation (stiff voltage divider):
RTH << (β+1)×RE  → typically RTH/((β+1)×RE) < 0.1

When this holds: VE ≈ VTH - VBE (determined only by R1, R2, VCC, VBE)
                 IC ≈ VE/RE   (independent of β!)
```

**Why this works so beautifully:** The base is held at a nearly constant voltage by the voltage divider. As long as IB << IR1 (which is ensured by making IR1 = 10×IB), the divider output doesn't shift even if β varies.

**Stability factor:**
```
S = (β+1)(RTH + RE) / (β×RE + RTH + RE) = 1 + RTH/RE  [for RTH/(β+1)<<RE condition]
```

For RTH = RE: S = 2 (excellent — only 2× sensitivity to ICBO)

**Design procedure (practical):**
```
Step 1: Choose VE = 10% of VCC (for stability) → IC = VE/RE
Step 2: Choose VCE = VCC/2 (for maximum symmetric swing)
Step 3: RC = (VCC - VCE - VE)/IC
Step 4: Choose IB = IC/β; set divider current IR2 = 10×IB
Step 5: R2 = VB/IR2; R1 = (VCC - VB)/IR2
        where VB = VE + VBE = VE + 0.7
```

### Classification of Amplifiers

**By biasing (operating point):**

| Class | Conduction angle | Efficiency | Distortion | Use |
|-------|-----------------|-----------|-----------|-----|
| Class A | 360° (full cycle) | 25-50% | Lowest | Hi-fi audio |
| Class B | 180° (half cycle) | Up to 78.5% | Crossover distortion | Push-pull stages |
| Class AB | Between 180-360° | ~60-70% | Low | Most audio amplifiers |
| Class C | Less than 180° | Up to 100% | High (not for audio) | RF amplifiers |
| Class D | Switching (PWM) | >90% | Filtered | Class-D audio, motor drives |

**Class A:** Q-point at center of load line. Transistor conducts for the entire 360° of the input signal cycle. Waveform is reproduced faithfully. Efficiency suffers because the transistor draws IC even with no input signal.

**Class B push-pull:** Two transistors — one handles positive half, other handles negative half. More efficient but creates **crossover distortion** near zero crossing (because each transistor needs 0.6V VBE before it starts conducting).

**Class AB:** Small forward bias applied to eliminate crossover distortion while preserving most of Class B's efficiency. Used in almost all practical audio amplifiers (integrated op-amp output stages, audio power amplifiers).

**By coupling method:**
| Method | Frequency range | Advantage | Use |
|--------|----------------|-----------|-----|
| RC coupled | AC (20Hz to few MHz) | Simple, low cost | Audio |
| Transformer coupled | Mid-band | Impedance matching, isolation | RF, power |
| Direct coupled | DC to high f | Works for DC signals | Op-amps, DC amplifiers |
| Capacitive (same as RC) | Same as RC | Standard audio | Standard |

### h-Parameter Model of BJT (Small-Signal Equivalent Circuit)

The BJT, when biased at a Q-point, can be replaced by a **linear small-signal model** for AC signal analysis. The most common model uses **hybrid parameters (h-parameters)**:

**h-parameter definitions (for common-emitter configuration):**
```
h11E = hie = VBE/IB  |  VCE=0  = input resistance (typ. 1-10kΩ)
h12E = hre = VBE/VCE |  IB=0   = reverse voltage ratio (very small, ~10⁻⁴, often neglected)
h21E = hfe = IC/IB   |  VCE=0  = forward current gain (= β, typically 50-300)
h22E = hoe = IC/VCE  |  IB=0   = output admittance (conductance, typ. 25-50μS; Zout = 1/hoe = 20-40kΩ)
```

**Simplified CE small-signal model (neglecting hre and hoe):**
```
B ──────┬─────[hie (resistor)]─────── E
        │                              │
       [hfe×IB (current source, IB from base to emitter)]
        │                              │
C ──────┴─────────────────────────── E
```

More explicitly for an amplifier analysis:

```
Vin ─── RS ─── B ──[hie]── E ── GND
               │ IB
         RC || RL
               │
        [hfe×IB] (collector current source, from C to E)
               │
        C ──── Vout
```

**Voltage gain derivation using h-parameters:**
```
Vout = -IC × (RC || RL) = -(hfe × IB) × RC'
Vin ≈ IB × hie   (neglecting RS)

Av = Vout/Vin = -(hfe × IB × RC') / (IB × hie)
   = -hfe × RC' / hie
   = -β × RC' / hie

Since hie = β/gm = β×VT/IC:
Av = -β × RC' / (β×VT/IC) = -IC × RC' / VT = -gm × RC'
```

This confirms: Av = -gm × (RC || RL) for common-emitter with bypassed RE.

**Input impedance:**
```
Zin = RS || hie ≈ hie (for RS >> hie)
    = β/gm = β × VT/IC
```

**Output impedance:**
```
Zout = RC || (1/hoe) ≈ RC   (since 1/hoe >> RC typically)
```

### Three Amplifier Configurations Comparison

**Common Emitter (CE):**
```
Input: Base, Output: Collector, Common: Emitter
Av = -gm×(RC||RL) (large, negative → inverts signal)
Zin = hie = β/gm (moderate)
Zout ≈ RC (moderate to high)
Phase: 180° inversion
Use: Voltage amplifier (most common)
```

**Common Base (CB):**
```
Input: Emitter, Output: Collector, Common: Base
Av = +gm×(RC||RL) (same magnitude as CE, no inversion)
Zin = 1/gm = re (very low, typically 10-50Ω)
Zout ≈ RC (high)
Phase: 0° (non-inverting)
Use: RF amplifiers (for its excellent high-frequency response), current buffer
```

**Common Collector (CC) — Emitter Follower:**
```
Input: Base, Output: Emitter, Common: Collector
Av ≈ 1 (slightly less than 1, non-inverting)
Zin = β × (RE || RL) (very high)
Zout = 1/gm || RE ≈ 1/gm = re (very low, typically 10-50Ω)
Phase: 0° (non-inverting)
Use: Impedance buffer (between high-Z source and low-Z load)
```

**Comparison table:**

| Parameter | CE | CB | CC (EF) |
|-----------|----|----|---------|
| Voltage gain | High (–gm·RC) | High (+gm·RC) | ≈1 |
| Current gain | β | <1 | β+1 |
| Power gain | Highest | Moderate | Moderate |
| Input impedance | Medium (β/gm) | Very low (1/gm) | Very high (β·RE) |
| Output impedance | High (RC) | High (RC) | Very low (1/gm) |
| Phase shift | 180° | 0° | 0° |
| Frequency response | Good | Best (no Miller effect) | Good |

### RC Coupled Amplifier — Complete Analysis

**Full circuit (single stage):**
```
        VCC
         │
       [RC]
         │ Collector
[CC1]  [NPN BJT] [CC2]
Vin──||──Base   Collector──||──Vout
       Emitter
         │
       [RE]──[CE (bypass)]
         │
        GND

R1, R2 voltage divider for biasing (connected to base)
```

**Three frequency regions:**

**Low-frequency response (f < fL):**

Coupling capacitors CC1, CC2 and bypass capacitor CE form high-pass filters:
```
For CC1 with Rin = R1||R2||hie:
fL1 = 1/(2π × CC1 × Rin)

For CE bypassing RE (emitter resistor becomes un-bypassed at low f):
fL(CE) = 1/(2π × CE × (RE || 1/gm))
≈ 1/(2π × CE × 1/gm)   since 1/gm << RE typically

The dominant (highest) fL determines the overall lower cutoff.
```

**Mid-frequency response (fL << f << fH):**

All capacitors act as shorts, all internal transistor capacitances negligible:
```
Av(mid) = -gm × (RC || RL)
Zin = R1 || R2 || hie
Zout = RC
```

**High-frequency response (f > fH):**

Internal transistor capacitances dominate:
- Cbe (base-emitter capacitance, typically 20-50pF)
- Cbc or Cµ (base-collector Miller capacitance — critical!)

**Miller Effect** — key concept for high-frequency rolloff:

The collector-base capacitance Cbc appears much larger at the input due to the voltage gain:
```
Miller capacitance: Cµ(Miller) = Cbc × (1 + |Av|)

For Av = -100 and Cbc = 5pF:
Cµ(Miller) = 5 × 101 = 505pF!!

This dominates the input capacitance → creates a low-pass filter with Rin:
fH ≈ 1 / (2π × Rin × Cµ(Miller))
   = 1 / (2π × 1350 × 505×10⁻¹²)
   = 234kHz   (much lower than Cbc alone would suggest!)
```

**Why Miller effect limits bandwidth:** The feedback capacitance Cbc is multiplied by (1+|Av|). For high-gain amplifiers, this creates a large effective input capacitance that rolls off the high-frequency gain. This is why:
- Common-base configuration (no Cbc feedback path) has much wider bandwidth
- Op-amp compensation capacitor deliberately uses Miller effect to set a controlled rolloff

**Gain-Bandwidth product (GBW = fT):**

For a transistor: GBW = |Av| × BW ≈ gm/(2π × Cbe + Cbc) = fT (transition frequency)

fT is a key transistor datasheet parameter (e.g., 2N2222: fT = 300MHz at IC = 20mA).

### Effect of Cascading — Mathematical Analysis

**Two-stage amplifier:**

```
Vin → [Stage 1: Av1, fH1] → [Stage 2: Av2, fH2] → Vout
        (coupling CC between stages, blocks DC, passes AC)
```

**Gain:**
```
Av(total) = Av1 × Av2   (product)
In dB: Av(dB, total) = Av1(dB) + Av2(dB)   (sum in dB)
```

**Loading effect:** Stage 2 input impedance (Zin2) loads Stage 1 output. Effective load for Stage 1 becomes RC1 || Zin2 (not just RC1). This reduces Stage 1 gain!

```
Effective Av1(loaded) = -gm1 × (RC1 || Zin2)   where Zin2 = R1'||R2'||hie2
```

**High-frequency cutoff of cascaded stages:**

Each stage contributes a pole (a -20dB/decade rolloff starting at its fH). For two identical stages:
```
|H(jf)|² = 1 / (1 + (f/fH)²)²   [product of two identical first-order responses]

At the overall -3dB point: (1 + (f₃dB/fH)²)² = 2
→ 1 + (f₃dB/fH)² = √2
→ f₃dB/fH = √(√2 - 1) = √0.4142 = 0.6436

fH(2 stages) = 0.64 × fH(single stage)
```

**For n identical stages:**
```
fH(n) = fH(1) × √(2^(1/n) - 1)

n=1: factor = 1.00
n=2: factor = 0.64
n=3: factor = 0.51
n=4: factor = 0.44
n=10: factor = 0.26   (severe bandwidth narrowing for 10 stages)
```

### Negative Feedback — Theory and Derivation

**General feedback amplifier model:**
```
Vin → [+] → [A (open-loop gain)] → Vout
       ↑ -
      [β (feedback network)]
       ↑
      Vout
```

**Closed-loop gain derivation:**
```
Error signal: Verr = Vin - β×Vout
Vout = A × Verr = A × (Vin - β×Vout)
Vout + A×β×Vout = A×Vin
Vout(1 + Aβ) = A×Vin

Af = Vout/Vin = A/(1 + Aβ)   [fundamental feedback equation]
```

**Gain desensitivity (stability improvement):**

Differentiate Af with respect to A:
```
dAf/dA = 1/(1 + Aβ)²  × ... = [1/(1+Aβ)] × [Af/A]

→ dAf/Af = (1/(1+Aβ)) × dA/A

If A changes by ΔA/A = 10% and Aβ = 100 (loop gain):
ΔAf/Af = (1/101) × 10% = 0.099% ← only 0.1% change despite 10% open-loop change!
```

This is why op-amps with massive open-loop gain (10⁵) and modest feedback produce extraordinarily stable gain.

**Effect on bandwidth:**

Open-loop response: A(jω) = A0/(1 + jω/ωH)   [single-pole rolloff]

Closed-loop: Af(jω) = A(jω)/(1 + A(jω)β) = [A0/(1+A0β)] / (1 + jω/((1+A0β)×ωH))

New bandwidth: ωH(closed-loop) = (1 + A0β) × ωH(open-loop)

```
fH(closed-loop) = (1 + Aβ) × fH(open-loop)
```

The feedback widens the bandwidth by exactly the same factor (1+Aβ) that it reduces the gain. The **gain-bandwidth product is preserved** (constant):

```
Af × fH(closed) = A0/(1+A0β) × (1+A0β)×fH = A0 × fH = GBW = constant
```

**Effect on input/output impedance (for voltage-series feedback — non-inverting amp):**
```
Zin(closed-loop) = (1 + Aβ) × Zin(open-loop)   [series input: increases Zin]
Zout(closed-loop) = Zout(open-loop) / (1 + Aβ)   [shunt output: decreases Zout]
```

**Effect on distortion:**

If open-loop generates harmonic distortion D (at output), feedback reduces it:
```
Df = D / (1 + Aβ)
```

But: if distortion is in the feedback network itself, feedback does NOT help.

**Four feedback topologies:**

| Topology | Sampled signal | Fedback signal | Effect on Zin | Effect on Zout | Ideal use |
|----------|---------------|---------------|--------------|---------------|-----------|
| Voltage-series (series-shunt) | Vout | Voltage | Increases | Decreases | Voltage amp |
| Current-shunt (shunt-series) | Iout | Current | Decreases | Increases | Current amp |
| Voltage-shunt (shunt-shunt) | Vout | Current | Decreases | Decreases | Transresistance |
| Current-series (series-series) | Iout | Voltage | Increases | Increases | Transconductance |

### Common Source MOSFET Amplifier

**Circuit:**
```
        VDD
         │
       [RD]
         │ Drain
     [N-MOSFET (enhancement)]
         │ Source
       [RS] ── [CS (bypass)]
         │
        GND

Gate bias: voltage divider R1, R2 from VDD to GND (through Gate)
Input: AC signal through coupling cap to Gate
Output: AC signal through coupling cap from Drain
```

**Small-signal model:**

Replace MOSFET with:
- Gate node: no current (Ig = 0)
- Drain-source: gm×VGS current source (gm = 2√(K×ID) for enhancement MOSFET, or IDSS/|VP/2| for JFET at VGS)
- Output resistance: rd = |VA|/ID (channel length modulation, often neglected)

**Voltage gain (mid-band, with CS bypassing RS):**
```
Vgs = Vg = Vin   (since Vs = 0 with CS bypassing RS)
Vout = -gm × Vgs × (RD || RL)

Av = Vout/Vin = -gm × (RD || RL)
```

**Input impedance:**
```
Zin = RG = R1 || R2   (gate draws no current, so only the bias resistors matter)
Typically: Zin = 1-10 MΩ (much higher than BJT CE)
```

**Output impedance:**
```
Zout = RD || rd ≈ RD   (for rd >> RD)
```

**CS vs CE comparison:**

| Parameter | CE (BJT) | CS (MOSFET) |
|-----------|---------|------------|
| Av (same RD=RC=1kΩ, IC=ID=1mA) | -gm×RC = -(1mA/26mV)×1k = -38.5 | -gm×RD = -(2×√(K×ID))×1k (lower gm) |
| Zin | hie = β/gm ≈ kΩ | RG = MΩ |
| Zout | RC | RD |
| Noise | Higher | Lower |
| Phase | 180° | 180° |

The MOSFET CS amplifier provides much higher input impedance but generally lower voltage gain than BJT CE for the same quiescent current.

---

## 2. Example

### Complete Voltage Divider Bias Q-Point Calculation

**Given:** VCC = 12V, R1 = 47kΩ, R2 = 10kΩ, RC = 2.2kΩ, RE = 1kΩ, β = 100

**Solution:**

**Step 1: Thevenin equivalent of base circuit:**
```
VTH = VCC × R2/(R1+R2) = 12 × 10/(47+10) = 12 × 10/57 = 2.105V

RTH = R1 || R2 = (47 × 10)/(47+10) = 470/57 = 8.246kΩ
```

**Step 2: Apply KVL to base-emitter Thevenin loop:**
```
VTH = IB×RTH + VBE + IE×RE
IE = (β+1)×IB = 101×IB

2.105 = IB×8246 + 0.7 + 101×IB×1000
2.105 - 0.7 = IB × (8246 + 101000) = IB × 109246
IB = 1.405 / 109246 = 12.86μA
```

**Step 3: Find IC and VCE:**
```
IC = β × IB = 100 × 12.86μA = 1.286mA
IE = 101 × 12.86μA = 1.299mA

VCE = VCC - IC×RC - IE×RE
    = 12 - 1.286×2.2 - 1.299×1
    = 12 - 2.829 - 1.299
    = 7.87V
```

**Q-point: IC = 1.29mA, VCE = 7.87V** — close to center (VCC/2 = 6V), active region. ✓

**Verify stiff voltage divider condition:**
```
RTH/(β+1)×RE = 8246/101000 = 0.082 < 0.1 ✓ (stiff divider)
```

**Step 4: Check stability factor:**
```
S = 1 + RTH/RE = 1 + 8246/1000 = 9.25
For a 1μA increase in ICBO: ΔIC = S × ΔICBO = 9.25 × 1μA = 9.25μA — acceptable
```

---

## 3. Applications and Use Cases

1. **Voltage divider bias in audio preamplifiers:** All practical BJT preamplifiers (guitar effects pedals, microphone preamps) use voltage divider bias for production-consistent performance regardless of transistor β variation.

2. **Emitter follower (CC configuration) as impedance buffer:** The output stage of headphone amplifiers uses CC (emitter follower) configuration: low output impedance (1-10Ω) to drive 32Ω headphones without losing voltage to internal resistance.

3. **Common base amplifier in RF stages:** The first amplification stage in cellular phone receivers uses CB configuration because it has no Miller capacitance → extremely high bandwidth (can amplify GHz signals). Also has a built-in cascode configuration advantage.

4. **Negative feedback in audio amplifiers:** Mackie, Crown, and QSC professional audio amplifiers use global negative feedback (Aβ = 50-100) around power amplifiers to achieve 0.001% THD (Total Harmonic Distortion) from transistors that would otherwise produce 5-10% THD open-loop.

5. **Class AB push-pull amplifiers in speaker drivers:** Every loudspeaker power amplifier uses Class AB (two transistors, one NPN + one PNP, with small forward bias) to achieve 60-70% efficiency while maintaining low distortion for music reproduction.

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Voltage Divider Bias Q-Point and Gain [May 2019, Q12 — Modified]

**Problem:** An RC coupled BJT amplifier has VCC = 12V, IC = 2mA, β = 125, fL = 100Hz, fH = 100kHz. Design the complete amplifier and find voltage gain.

**Solution:**

**Step 1: Q-point resistors**
```
Choose: VCE = VCC/2 = 6V (centered on load line)
        VE = 1V (10% of VCC for thermal stability)

RE = VE/IC = 1V / 2mA = 500Ω → use 470Ω
RC = (VCC - VCE - VE)/IC = (12 - 6 - 1)/2mA = 5/2mA = 2.5kΩ → use 2.2kΩ
```

**Step 2: Bias network**
```
VB = VE + VBE = 1 + 0.7 = 1.7V
IB = IC/β = 2mA/125 = 16μA
Make IR2 = 10×IB = 160μA (stiff divider rule)

R2 = VB/IR2 = 1.7/160μA = 10.625kΩ → use 10kΩ
R1 = (VCC - VB)/IR2 = 10.3/160μA = 64.4kΩ → use 68kΩ
```

**Step 3: hie (for capacitor calculations)**
```
gm = IC/VT = 2mA/26mV = 76.9mA/V
hie = β/gm = 125/76.9mA = 1625Ω = 1.625kΩ
```

**Step 4: Input coupling capacitor (for fL1 = 50Hz, half of total fL contribution)**
```
Zin = R1||R2||hie = 68k||10k||1.625k

R1||R2 = 68k×10k/78k = 8.7kΩ
8.7k||1.625k = 8.7×1.625/(8.7+1.625) = 14.14/10.325 = 1.37kΩ = Zin

CC1 = 1/(2π × fL × Zin) = 1/(2π × 100 × 1370) = 1.16μF → use 2.2μF
```

**Step 5: Emitter bypass capacitor (most critical for gain flatness)**
```
Resistance at emitter for CE design: re = 1/gm = 13Ω
CE = 1/(2π × fL × re) = 1/(2π × 100 × 13) = 122μF → use 150μF (47μF minimum)
```

**Step 6: Voltage gain (mid-band)**
```
Av = -gm × (RC || RL)   [assume RL = ∞ for single-stage, or RL = 10kΩ typical]
   = -76.9mA/V × 2.2kΩ   [RL = ∞]
   = -169

In dB: 20 log(169) = 44.6dB
```

**Summary:**
- RC = 2.2kΩ, RE = 470Ω, R1 = 68kΩ, R2 = 10kΩ
- CC1 = 2.2μF, CE = 150μF
- Av(mid) = -169 (44.6dB)

---

### Example 2: Effect of Cascading and Gain Calculation [May 2019, Q13a]

**Problem:** A two-stage RC coupled amplifier has each stage with Av = -40 and fH = 200kHz. Calculate the total gain and the overall fH. [3 marks]

**Solution:**

**Total gain:**
```
Av(total) = Av1 × Av2 = (-40) × (-40) = +1600   [double inversion = in-phase]
In dB: 20 log(40) + 20 log(40) = 32 + 32 = 64dB
```

(Note: The negative signs cancel for the magnitude of gain, but since both stages invert, the output is in-phase with input — same as no inversion.)

**Overall fH:**
```
fH(2 identical stages) = fH(single) × √(2^(1/2) - 1)
                        = 200kHz × √(√2 - 1)
                        = 200kHz × √(0.4142)
                        = 200kHz × 0.6436
                        = 128.7kHz ≈ 129kHz

Bandwidth reduction: (200 - 129)/200 = 35.5% reduction
```

**Summary:**
- Total gain: 1600 (64dB)
- Overall fH: ≈ 129kHz (36% lower than single-stage bandwidth)

---

### Example 3: Stability Factor and Thermal Stability Design [KTU Style]

**Problem:** Compare the stability factors S for (a) fixed bias with β = 100, (b) voltage divider bias with R1 = 47kΩ, R2 = 10kΩ, RE = 1kΩ. If ΔICBO = 1μA for a 10°C temperature rise, find ΔIC for each case.

**Solution:**

**(a) Fixed bias:**
```
S = β + 1 = 100 + 1 = 101
ΔIC = S × ΔICBO = 101 × 1μA = 101μA = 0.101mA

If ICQ = 2mA: ΔIC/ICQ = 0.101/2 = 5.05% per 10°C rise → severe!
```

**(b) Voltage divider bias:**
```
RTH = R1||R2 = 47k×10k/57k = 8.246kΩ
RE = 1kΩ

S = (β+1)(RTH + RE) / (β×RE + RTH + RE)
  = (101)(8246 + 1000) / (100×1000 + 8246 + 1000)
  = 101 × 9246 / (100000 + 9246)
  = 933846 / 109246
  = 8.55

ΔIC = 8.55 × 1μA = 8.55μA

If ICQ = 2mA: ΔIC/ICQ = 8.55/2000 = 0.43% per 10°C rise → excellent!
```

**Comparison:** Voltage divider bias is 101/8.55 ≈ 12× more stable than fixed bias. The emitter resistance RE reduced the stability factor by providing negative feedback.

---

## 5. Previous Year Questions and Solutions

### PYQ 1 [May 2019, Q8]: Explain thermal runaway in transistors. [3 marks]

**Complete Solution:**

**Definition:** Thermal runaway is a **positive feedback thermal instability** in BJT transistors where increasing temperature causes increasing collector current, which causes more power dissipation, which causes more heating, eventually destroying the device.

**Physical mechanism:**

The BJT's collector current is:
```
IC = β×IB + (β+1)×ICBO

Where ICBO = reverse saturation current of collector-base junction (thermally generated minority carriers)
```

**Temperature dependence of ICBO:** ICBO approximately **doubles for every 10°C rise** in junction temperature.

**Runaway cycle:**

```
1. Temperature rises (ambient or self-heating)
2. ICBO doubles per 10°C rise
3. IC = β×IB + (β+1)×ICBO increases
4. More IC → More power: PD = VCE × IC
5. More PD → More heat → Temperature rises further
6. Cycle repeats with increasing amplitude
7. When Tj > Tjmax (150°C for silicon): transistor fails permanently
```

**Mathematical condition for runaway:**
```
Thermal runaway occurs when: dPD/dT_J > 1/θjA

Where θjA = junction-to-ambient thermal resistance (°C/W)
      PD = VCE × IC

For runaway to NOT occur: S × VCE × ΔICBO/ΔT < 1/θjA
```

**Prevention techniques:**
1. **Emitter resistor RE**: Creates negative feedback. IC↑ → VE↑ → VBE↓ → IB↓ → IC↓
2. **Thermal design**: Heatsink reduces θjA, keeping Tj low
3. **Thermistor in bias network**: NTC thermistor reduces RB as T rises → VB drops → IB drops → IC controlled
4. **Low stability factor S**: Design with voltage divider bias, S < 10

---

### PYQ 2 [May 2019, Q14]: Explain astable multivibrator using transistors with waveforms. [9 marks]

**Complete Solution:**

**What is an Astable Multivibrator?**

An astable (free-running) multivibrator is a BJT oscillator circuit with **no stable states** — it continuously alternates between two quasi-stable states, generating a square wave output without any external trigger.

**Circuit:**
```
VCC ────┬────[RC1]────┬────[RC2]────┬──── VCC
        │             │              │
       [RB1]        Q1-C   C-Q2    [RB2]
        │       B──┤ (NPN) (NPN) ├──B     │
        └────────   E         E   ─────────┘
                    │         │
                   GND       GND

C1: coupling capacitor from Q1-Collector to Q2-Base
C2: coupling capacitor from Q2-Collector to Q1-Base
```

**Operation — State by State:**

**State 1 (Q1 saturated ON, Q2 cut off OFF):**
- Q1 Collector ≈ VCE(sat) ≈ 0.2V (LOW)
- C2 (previously charged to ~VCC) now has its left plate connected to 0.2V → right plate (Q2 Base) driven to 0.2 - VCC ≈ -11.8V (strongly negative → Q2 OFF)
- With Q2 OFF, Q2 Collector → HIGH ≈ VCC
- C2 NOW begins charging: through RB2 from VCC → right plate rises exponentially from -11.8V toward VCC
- **Duration of State 1:** t1 = time for C2's right plate to rise from -VCC to +0.7V (threshold to turn Q2 ON)
  ```
  Mathematically: V(t) = VCC - (VCC - (-VCC))×e^(-t/RB2C2)
  At t=t1: VCC - 2VCC×e^(-t1/τ) = 0.7
  e^(-t1/τ) ≈ 0.5  →  t1 = τ×ln(2) = 0.693×RB2×C2
  (using approximation that VBE threshold ≈ 0 for timing calculation)
  ```

**State 2 (Q2 saturated ON, Q1 cut off OFF):** [Mirror image of State 1]
- Q2 turns ON → Q2 Collector drops LOW → C1 drives Q1 Base negative → Q1 turns OFF
- C1 charges through RB1 from VCC
- Duration: t2 = 0.693 × RB1 × C1

**Back to State 1:** C1 charges enough to bring Q1 Base to 0.7V → Q1 turns ON → Q2 turns OFF → State 1 repeats.

**Timing equations:**
```
t1 = 0.693 × RB2 × C2   (Q1 ON period = HIGH at Q2 Collector)
t2 = 0.693 × RB1 × C1   (Q2 ON period = HIGH at Q1 Collector)

Total period: T = t1 + t2 = 0.693(RB1C1 + RB2C2)

Frequency: f = 1/T = 1 / [0.693(RB1C1 + RB2C2)]

For symmetric (RB1=RB2=R, C1=C2=C):
T = 1.386RC ≈ 1.38RC
f = 0.722/RC ≈ 0.72/RC
```

**Output waveforms:**

```
Q1 Collector (VC1):
VCC ───────┐      ┌─────────┐      ┌──── (HIGH when Q1 OFF)
           │      │         │      │
0.2V       └──────┘         └──────┘     (LOW when Q1 ON)
           ← t2 →←   t1   →← t2 →

Q2 Collector (VC2) [complementary to VC1]:
VCC       ┌──────┐         ┌──────┐
           │      │         │      │
0.2V ──────┘      └─────────┘      └────

Q2 Base Voltage (VB2) [exponential charging]:
+0.7V           .......   (turns ON at 0.7V)
           ↗         ↘ ↗
0V        ╱           ╲╱
         ╱             ← exponential charging through RB2
-VCC ───→  (driven negative when Q1 turns ON)
```

**Design equations and example:**

For f = 1kHz with equal mark-space ratio:
```
RB1 = RB2 = R, C1 = C2 = C
f = 0.72/(RC) → RC = 0.72/f = 0.72/1000 = 7.2×10⁻⁴

Choose C = 0.01μF:
R = 7.2×10⁻⁴ / 10⁻⁸ = 72kΩ → use 68kΩ

RC1 = RC2 = VCC / IC(sat) = 5V / 5mA = 1kΩ   [for VCC = 5V, IC(sat) = 5mA]
```

**Collector resistors RC1, RC2:** Must ensure deep saturation:
```
IC(sat) = VCC/RC (approximately, since VCE(sat) ≈ 0.2V ≈ 0)
IB(sat) needed = IC(sat)/hFE

Make IB >> IB(sat) by choosing RB such that IB = IC(sat)/10 (overdrive by 10×)
```
