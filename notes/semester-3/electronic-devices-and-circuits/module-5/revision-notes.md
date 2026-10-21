# Module 5 Revision Notes — Operational Amplifiers

## IC 741 Specifications (Memorize for Exams)

| Parameter | IC 741 Value |
|-----------|-------------|
| Open-loop gain AOL | 200,000 (106dB) |
| Input impedance Rin | 2 MΩ |
| Output impedance Rout | 75 Ω |
| CMRR | 90 dB (typical) |
| Slew rate | 0.5 V/μs |
| Gain-bandwidth product | 1 MHz |
| Input offset voltage | ±2 mV (max 6mV) |
| Input bias current | 80 nA |
| Supply voltage | ±15V (max ±18V) |

## Op-Amp Application Gain Formulas

| Circuit | Output | Gain |
|---------|--------|------|
| Inverting amp | -(Rf/Rin)×Vin | Av = -Rf/Rin |
| Non-inverting amp | (1+Rf/R1)×Vin | Av = 1+Rf/R1 |
| Voltage follower | Vin | Av = 1 |
| Summing amp | -(Rf/R)×(V1+V2+V3) | Each channel: -Rf/Ri |
| Subtractor | V2 - V1 | Av = R2/R1 |
| Integrator | -(1/RC)∫Vin dt | H(ω) = -1/(jωRC) |
| Differentiator | -RC×d(Vin)/dt | H(ω) = -jωRC |
| Schmitt trigger | ±Vsat | UTP = +Vsat×R1/(R1+Rf) |

## Golden Rules

1. **V+ = V-** (virtual short — inputs at same potential when feedback present)
2. **I+ = I- = 0** (no current into op-amp input terminals)

## Slew Rate Impact

Full power bandwidth: f_max = SR/(2π×Vm)

For IC 741 with Vm = 10V: f_max = 0.5×10⁶/(2π×10) = 7.96 kHz

## Key Points

- Differentiator vs Integrator: same components, swap R and C positions
- Schmitt trigger uses POSITIVE feedback — provides hysteresis (noise immunity)
- CMRR: Good op-amp rejects common-mode noise (60Hz EMI on both wires) while amplifying differential signal
