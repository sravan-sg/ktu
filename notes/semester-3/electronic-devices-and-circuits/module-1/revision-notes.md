# Module 1 Revision Notes — Wave Shaping and Diode Circuits

## Quick-Reference Formulas

| Circuit | Condition | Output |
|---------|-----------|--------|
| RC Differentiator | τ = RC << T/10 | Vout = RC × d(Vin)/dt |
| RC Integrator | τ = RC >> 10T | Vout = (1/RC)∫Vin dt |
| Positive clipper | Vin > 0 | Vout = 0 |
| Negative clamper | Steady state | Bottom at 0V, range = 0 to 2Vpeak |
| Voltage doubler | - | Vout = 2 × Vpeak |
| Voltage tripler | - | Vout = 3 × Vpeak |
| Transistor sweep | τ >> T_sweep | Vout ≈ (VCC/τ) × t (linear ramp) |

## Waveform Conversion Table

| Input | Circuit | Output |
|-------|---------|--------|
| Square wave | Differentiator | Spikes (positive and negative) |
| Square wave | Integrator | Triangle wave |
| Triangle wave | Differentiator | Square wave |
| Sine wave | Clipper | Clipped/limited sine |

## Key Points

- **Differentiator = High Pass Filter**, Integrator = Low Pass Filter
- **Clamper MUST have capacitor**; clipper does NOT need capacitor
- Clamper changes DC level but NOT peak-to-peak amplitude
- Clipper changes amplitude but does NOT add DC
- Voltage multiplier: N stages → N × Vpeak DC output

## Common Exam Mistakes

1. Confusing differentiator (output across R) with integrator (output across C)
2. Forgetting to check τ vs T condition before calling circuit a "good" differentiator/integrator
3. Mixing up clamper and clipper — clamper needs C; clipper does not
