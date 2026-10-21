# Module 3 Revision Notes — Amplifiers and Feedback

## Biasing Formulas

| Circuit | Stability S | Q-point |
|---------|------------|---------|
| Fixed bias | S = β (worst) | IC = β(VCC-0.7)/RB |
| Self bias | S = (β+1)(RB+RE)/(βRE+RB+RE) | Improved |
| Voltage divider | S → 1 (best) | VE=(VB-0.7), IC=VE/RE |

**Voltage divider Q-point:**
```
VTH = VCC × R2/(R1+R2)
RTH = R1 || R2
IE = (VTH - 0.7) / (RE + RTH/(β+1))
VCE = VCC - IC(RC + RE)
```

## Amplifier Gain (Mid-band)

| Configuration | Av | Zin | Zout |
|---------------|-----|-----|------|
| Common Emitter | -gm×RC (large) | RB || hie | RC |
| Common Base | gm×RC (large, no inversion) | re | RC |
| Emitter Follower | ≈ 1 | Large | re |
| Common Source MOSFET | -gm×RD | RG (huge) | RD |

**gm = IC/VT = IC/26mV** (at room temperature)

## Negative Feedback Effects (all beneficial)

| Parameter | Effect | Magnitude change |
|-----------|--------|-----------------|
| Gain | Reduced | Af = A/(1+Aβ) |
| Bandwidth | Increased | BW_f = BW × (1+Aβ) |
| Distortion | Reduced | Df = D/(1+Aβ) |
| Gain stability | Improved | ΔAf/Af << ΔA/A |

## Cascading Effects

- Total gain: multiply individual gains (add in dB)
- Bandwidth: each stage reduces BW. For n identical stages: BW_n = BW_1 × √(2^(1/n) - 1)
- For 2 stages: BW_2 ≈ 0.64 × BW_1

## Key Points

- Thermal runaway: ICBO doubles per 10°C → IC increases → more heating → runaway destruction
- Prevention: RE provides negative feedback, heatsink, stability factor S < 10
- RC coupled amplifier: coupling capacitors block DC but pass AC signal; bypass CE shorts RE for AC
