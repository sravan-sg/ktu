# Module 6 Revision Notes — ICs, Filters, DAC/ADC, Timer 555

## Active Filter Cutoff Frequencies

| Filter | Order | Cutoff fc | Roll-off |
|--------|-------|-----------|---------|
| 1st order LPF | 1 | 1/(2πRC) | -20dB/dec |
| 2nd order LPF | 2 | 1/(2π√(R1R2C1C2)) | -40dB/dec |
| 1st order HPF | 1 | 1/(2πRC) | -20dB/dec (attenuates below) |
| 2nd order HPF | 2 | Same formula | -40dB/dec (attenuates below) |

Passband gain (non-inverting): A0 = 1 + Rf/R1

## ADC Comparison

| ADC | Speed | Accuracy | Comparators | Applications |
|-----|-------|----------|-------------|--------------|
| Flash | 1 cycle | Low | 2ⁿ-1 | Oscilloscopes, >1Gsps |
| SAR | n cycles | High | 1 | MCUs, sensors, audio |
| Dual slope | Slow | Very high | 1 | DMMs, precision |
| Sigma-Delta | Slow (oversampled) | Very high | 1 | Audio DACs/ADCs |

## IC 555 Timer Formulas

**Astable:**
```
t_HIGH = 0.693(RA + RB)C
t_LOW  = 0.693 × RB × C
T = t_HIGH + t_LOW = 0.693(RA + 2RB)C
f = 1.44 / [(RA + 2RB)C]
Duty = (RA+RB)/(RA+2RB) [always > 50%]
```

**Monostable:**
```
T = 1.1 × RA × C
```

## DAC Comparison

| DAC | Resistors needed | Precision | Best for |
|-----|-----------------|-----------|----------|
| Binary weighted | n different values (R, 2R, 4R...) | Difficult (wide range) | ≤8 bits |
| R-2R Ladder | Only R and 2R | Easy (only 2 values) | 8-16 bits |

## Key Points

- Shannon sampling theorem: fs ≥ 2×f_max to avoid aliasing
- Sample and Hold: Use low-leakage capacitor; droop rate = I_leakage/C
- Dual slope ADC: independent of R and C values (they cancel) — very accurate
- SAR ADC: binary search, n-bit conversion in n clock cycles
- 555 can oscillate with VCC from 5V to 15V; timing independent of VCC!
