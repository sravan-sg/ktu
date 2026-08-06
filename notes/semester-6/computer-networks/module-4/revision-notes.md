# Module 4 — Rapid Revision Notes

> **Course**: CS306 Computer Networks | **Module 4**: Congestion Control, QoS & IPv4 Subnetting

---

## 🚀 Submodule 1: Congestion Control & Traffic Shaping

- **Leaky Bucket**: Smooths bursty traffic to a strictly uniform, constant output rate. Drops packets when bucket overflows.
- **Token Bucket**: Accumulates tokens up to capacity $b$. Allows bursts at maximum speed $M$ for time $S = \frac{b}{M - r}$.
- **RED (Random Early Detection)**: Proactively drops packets with probability $P$ when queue exceeds threshold, preventing TCP global synchronization.

---

## 🚀 Submodule 2: IPv4 Subnetting & CIDR

- **Subnet Mask**: Mask with $n$ prefix 1s and $h = 32 - n$ host 0s. Usable hosts per subnet $= 2^h - 2$.
- **Class Ranges**: Class A (`/8`), Class B (`/16`), Class C (`/24`), Class D (Multicast `224.0.0.0/4`).
- **CIDR Supernetting**: Aggregates $2^k$ contiguous networks into a single route by matching prefix bits.

---

## 🔢 3 Solved Numerical Micro-Examples

1. **Token Burst Duration**: $b = 40 \text{ Mb}$, $M = 50 \text{ Mbps}$, $r = 10 \text{ Mbps}$. Burst duration $S = \frac{40}{50 - 10} = 1.0 \text{ second}$.
2. **Subnet Host Count**: For `/26` prefix, host bits $h = 32 - 26 = 6$. Usable hosts $= 2^6 - 2 = 62$. Subnet mask $= 255.255.255.192$.
3. **Supernetting**: `202.10.0.0/24` and `202.10.1.0/24` aggregate into `202.10.0.0/23`.
