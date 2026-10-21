# Module 5 — Operational Amplifiers: Detailed Notes Index

## Topics

| # | Topic | File | Key Concepts |
|---|-------|------|-------------|
| 1 | Operational Amplifiers | [operational-amplifiers.md](operational-amplifiers.md) | Differential amp, CMRR, slew rate, IC741 specs, inverting/non-inverting/summing/subtractor/integrator/differentiator/Schmitt trigger/Wien oscillator |

## Module Summary

Module 5 is the **highest-mark module** (20%, 40 marks in Part E):

- **Differential amplifier**: Core building block of op-amp — amplifies (V1-V2)
- **IC 741 key specs**: AOL=200,000, Rin=2MΩ, Rout=75Ω, SR=0.5V/μs, CMRR=90dB
- **Virtual short principle**: V+ ≈ V-, I+ = I- = 0 (golden rules for analysis)
- **8 op-amp applications** are exam staples — all with derivations:
  1. Inverting amp: Av = -Rf/Rin
  2. Non-inverting amp: Av = 1 + Rf/R1
  3. Voltage follower (unity gain buffer)
  4. Summing amplifier: Vout = -Rf(V1/R1 + V2/R2 + ...)
  5. Subtractor: Vout = V2 - V1 (for matched resistors)
  6. Integrator: Vout = -(1/RC)∫Vin dt
  7. Differentiator: Vout = -RC × d(Vin)/dt
  8. Schmitt trigger: UTP/LTP = ±Vsat×R1/(R1+Rf)

## Previous Year Questions (May 2019)

- Q15a (Part E): Differential amplifier circuit [5 marks]
- Q15b (Part E): First order HPF for fc=1kHz, gain=2 [5 marks]
- Q16a (Part E): Inverting + non-inverting op-amp gain derivation [6 marks]
- Q16b (Part E): Compare active and passive filters [4 marks]
- Q17a (Part E): Sample and hold circuit [6 marks]
- Q17b (Part E): CMRR and Slew Rate — IC 741 values [4 marks]
- Q18a (Part E): Schmitt trigger — UTP, LTP [6 marks]
- Q19a (Part E): Summing amplifier — realize Y(t) = 5V1+2V2-4V3 [5 marks]
- Q20a (Part E): Wien bridge oscillator using op-amp [5 marks]
