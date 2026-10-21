# Module 4 Revision Notes — Oscillators and Multivibrators

## Oscillator Frequency Formulas

| Oscillator | Frequency | Notes |
|------------|-----------|-------|
| Wien Bridge | f₀ = 1/(2πRC) | Gain must = 3, used at audio |
| Hartley | f₀ = 1/(2π√(L_total×C)) | L_total = L1+L2+2M |
| Colpitts | f₀ = 1/(2π√(L×C_total)) | C_total = C1×C2/(C1+C2) |
| Crystal | fs = 1/(2π√(LsCs)) | Highest stability, ppm drift |

## Barkhausen Criterion (MUST memorize)

1. **|Aβ| = 1** (loop gain magnitude = 1)
2. **∠Aβ = 0°** (total phase shift = 0° or 360°)

Wien network: β = 1/3, phase = 0° at f₀. So A must = 3.

## Multivibrator Timing

| Type | States | Timing | Formula |
|------|--------|--------|---------|
| Astable | 0 stable | T = 0.69(R1C1+R2C2) | f = 0.72/RC (symmetric) |
| Monostable | 1 stable | T = 0.69×R×C | Triggered once |
| Bistable | 2 stable | None (latches) | Triggered by S/R |

## Key Points

- Oscillators: distinguish **sinusoidal** (Wien, Hartley, LC) from **non-sinusoidal** (astable, multivibrators, sawtooth)
- Crystal oscillator: Q = 10,000 to 10M (vs LC Q = 50-200). Used in MCU clocks, GPS, watches.
- Barkhausen is **necessary but not sufficient** — in practice, |Aβ| is started slightly > 1 to initiate oscillation, then amplitude stabilizes via nonlinearity (saturation, thermistor).
- Astable MV: output is complementary — when Q1 saturates, Q2 cuts off.
