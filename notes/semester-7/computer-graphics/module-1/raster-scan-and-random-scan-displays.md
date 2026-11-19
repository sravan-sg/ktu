# Raster Scan and Random Scan (Vector) Displays

## 1. Explanation

Display architectures in computer graphics define the physical and logical mechanisms through which digital numerical geometry stored in memory is transformed into photons emitted or modulated on a display surface. Historically rooted in the physics of Cathode Ray Tubes (CRTs) and continuing into modern active-matrix liquid crystal and organic light-emitting diode panels, two foundational display philosophies govern graphics systems:
1. **Raster Scan Displays** (fixed-grid continuous periodic sampling)
2. **Random Scan Displays** (vector, calligraphic, directed-beam, or stroke-writing systems)

---

### The Cathode Ray Tube (CRT): Physical Principles & Components

At its core, a Cathode Ray Tube is an evacuated glass envelope maintaining a high vacuum ($\approx 10^{-6}\text{ to } 10^{-8}\text{ Torr}$) within which electrons are generated, concentrated into a pencil-thin stream, accelerated to relativistic velocities, and steered electrodynamically onto a luminescent phosphor target.

```
                  ┌─────────────────────────────────────────────────────────────┐
                  │                 CATHODE RAY TUBE (CRT)                      │
                  │                                                             │
   Heater Filament│    Control Grid (G1)                                        │
    ┌──┐          │       ┌─┐                                                   │
───┤  ├──────────┼───────┤ │                                                   │
    └──┘          │       └─┘       Accelerating Anode                          │
  Cathode (K)     │  Pre-accelerating  ┌──┐         Deflection Yoke             │
                  │     Anode (G2)     │  │          (Magnetic Coils)           │
                  │        ┌──┐        │  │              ┌─────┐                │
                  │        │  │        │  │            ┌─┴─────┴─┐              │
                  │        │  │        └──┘            │ ┌─────┐ │              │
                  │        └──┘      Focusing Anode    │ │     │ │              │
                  │                     (G3)           │ └─────┘ │              │
                  │                                    └─┬─────┬─┘              │
                  │                                      └─────┘                │
                  │                                                          Phosphor
                  │ ─── ─── ─── ─── ─── ─── ─── ─── ─── ─── ─── ─── ──────── Screen
                  │          Narrow High-Velocity Electron Beam              ░░░░░░░░░
                  │                                                          ░░░░░░░░░
                  │                                                          ░░░░░░░░░
                  └─────────────────────────────────────────────────────────────┘
```

#### 1. Electron Gun Structure & Operation
- **Cathode & Heater Filament**: An indirect heating element elevates an oxide-coated cathode (barium, strontium, and calcium oxides) to thermionic emission temperatures ($T \approx 1000\text{ K}$ to $1150\text{ K}$). Under thermionic emission, electrons overcome the material work function $\phi_w$ governed by the **Richardson-Dushman equation**:
  $$J = A T^2 e^{-\frac{\phi_w}{k_B T}}$$
  where $J$ is emission current density ($\text{A/m}^2$), $A$ is Richardson's constant ($\approx 1.2 \times 10^6 \text{ A}/(\text{m}^2\text{K}^2)$), and $k_B$ is the Boltzmann constant.
- **Control Grid ($G_1$)**: A metal cup enclosing the cathode with a tiny aperture ($0.5\text{ to } 1.0\text{ mm}$). Biased at a variable negative potential relative to the cathode (typically $-10\text{ V}$ to $-100\text{ V}$). Making $G_1$ more negative repels thermionic electrons, reducing the beam current; driving $G_1$ toward cutoff completely blanks the beam. Thus, video intensity modulation is achieved by voltage-biasing the control grid.
- **Pre-accelerating & Accelerating Anodes ($G_2, G_4$)**: Positively biased cylinders ($+200\text{ V}$ to $+1\text{ kV}$) that initiate axial beam velocity.
- **Focusing Anode ($G_3$)**: Situated between the accelerating elements, biased at an adjustable lower voltage ($+200\text{ V}$ to $+600\text{ V}$). The electric field curvature between $G_2, G_3,$ and $G_4$ forms an electrostatic lens (bipotential lens) that converges divergent electron paths into a focal point precisely at the phosphor plane.
- **Final High-Voltage Anode**: Operates at an ultra-high post-deflection accelerating voltage ($V_a = +15\text{ kV}$ to $+30\text{ kV}$). Electrons striking the screen have kinetic energy:
  $$E_k = q \cdot V_a = \frac{1}{2} m_e v^2 \implies v = \sqrt{\frac{2 q V_a}{m_e}} \approx 0.25c \text{ to } 0.34c$$
  where $c$ is the speed of light.

#### 2. Deflection System: Magnetic vs. Electrostatic
While laboratory oscilloscopes use electrostatic deflection plates, graphic CRT monitors universally implement **magnetic deflection yokes** (pair of orthogonal saddle coils mounted externally on the tube neck). 
- **Lorentz Force**:
  $$\vec{F} = q(\vec{v} \times \vec{B})$$
- Magnetic deflection allows much wider deflection angles ($90^\circ$ to $110^\circ$), drastically shortening the physical depth of the monitor tube, without causing beam defocusing at screen edges.

#### 3. Phosphor Physics & Persistence Categories
When energetic electrons collide with the phosphor screen, energy is transferred to lattice electrons in zinc sulfide ($\text{ZnS}$) or rare-earth crystal dopants.
- **Fluorescence**: Instantaneous light emission occurring within $10^{-8}\text{ s}$ during electron bombardment.
- **Phosphorescence**: Delayed emission caused by trapped excited electrons decaying back to ground state.
- **Persistence**: Defined as the time required for emitted luminous intensity to decay to $10\%$ of its peak initial excitation level.

Standard Phosphor Designations:
- **P1 (Green, Medium Persistence $\approx 20\text{ ms}$)**: Classic general-purpose oscilloscopes and vector displays.
- **P4 (White, Short-Medium $\approx 60\ \mu\text{s}$)**: Standard black-and-white television and monochrome raster terminals.
- **P7 (Blue-White dual-layer, Long $\approx 1\text{ to } 3\text{ seconds}$)**: Radar PPI scopes and low-refresh calligraphic displays.
- **P22 (Tricolor Red/Green/Blue, Medium-Short $\approx 1\text{ to } 2\text{ ms}$)**: Color shadow-mask CRT monitors and commercial televisions.
- **P31 (Green, High-efficiency Short $\approx 40\ \mu\text{s}$)**: Fast-response computer vector displays and radar stations.

*Flicker Criterion*: If the refresh interval exceeds phosphor persistence, the human eye perceives disruptive luminance fluctuation (flicker). According to the **Ferry-Porter Law**, the critical flicker fusion frequency ($f_c$) increases logarithmically with retinal illuminance ($I$):
$$f_c = a \log_{10} I + b$$
For bright monitors, refresh rates must be maintained at $\ge 60\text{ Hz}$ (or $\ge 75\text{–}85\text{ Hz}$ for ergonomic flicker-free operation).

---

### Raster Scan Architecture & Video Generation Pipeline

In a **Raster Scan** system, the electron beam sweeps across the entire phosphor faceplate in a rigid, repetitive, top-to-bottom rectangular raster matrix regardless of how many or how few graphical entities occupy the scene.

```
       Scanline 0 ───────► (Active Video Display)
                  ◄┄┄┄┄┄┄ Horizontal Retrace (Blanked)
       Scanline 1 ───────►
                  ◄┄┄┄┄┄┄
                  │
                  ▼
       Scanline V-1 ─────►
                  ▲
                  │  Vertical Retrace (Blanked)
                  └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
```

#### 1. Scanning Mechanics
- **Active Horizontal Trace**: The horizontal sweep circuit applies a linear ramp current to the horizontal deflection coil, deflecting the beam from left to right at constant velocity while the video DAC modulates pixel intensities.
- **Horizontal Blanking & Retrace**: Upon reaching the right margin, the beam is cut off (grid $G_1$ pulled highly negative) and swept back to the left margin at maximum speed via a flyback pulse. The blanked flyback period is the **Horizontal Blanking Interval (HBI)**.
- **Active Vertical Sweep**: Concurrently, the vertical deflection coil drives a slower linear ramp, pulling scanlines downward sequentially.
- **Vertical Blanking & Retrace (VBI)**: When the beam finishes the bottommost scanline, it is blanked and returned diagonally to the upper-left corner ($0, 0$). The **Vertical Blanking Interval (VBI)** was historically used for closed-caption data (NTSC Line 21) and remains in modern GPU drivers as the swap-chain buffer exchange window.

#### 2. Progressive vs. Interlaced Scanning
- **Progressive (Non-interlaced)**: All scanlines ($0, 1, 2, \dots, V-1$) are drawn sequentially in a single vertical frame period ($1/60\text{ s} \approx 16.67\text{ ms}$). This avoids interline twitter and is the standard for high-resolution graphics and computer monitors.
- **Interlaced Scanning**: Each complete frame is bifurcated into two temporal fields:
  1. *Odd Field*: Paints scanlines $1, 3, 5, \dots, V-1$ in $1/60\text{ s}$.
  2. *Even Field*: Paints scanlines $0, 2, 4, \dots, V-2$ in the subsequent $1/60\text{ s}$.
  Total frame rate is $30\text{ Hz}$, but perceived flicker rate is $60\text{ Hz}$. This halved broadcast transmission bandwidth for analog television (NTSC 525 lines / PAL 625 lines) at the expense of motion comb artifacts on fast horizontal scene displacements.

#### 3. Complete Video Generation Pipeline
```
┌──────────────┐     PCIe Bus     ┌────────────────────────┐
│  Host CPU /  │ ═══════════════► │ Frame Buffer (VRAM)    │
│  Rasterizer  │                  │ Width × Height × Depth │
└──────────────┘                  └───────────┬────────────┘
                                              │ Pixel Clock Readout
                                              ▼
┌──────────────────┐  Sync Bus    ┌────────────────────────┐
│ Video Controller │ ───────────► │ Shift Register / Serializer
│ (CRTC Engine)    │              └───────────┬────────────┘
└────────┬─────────┘                          │ Index / Color
         │                                    ▼
         │ HSync, VSync           ┌────────────────────────┐
         │ Blanking Signals       │ Color Lookup Table     │
         │                        │ (LUT Palette / DAC)    │
         │                        └───────────┬────────────┘
         ▼                                    │ Analog Drive (R,G,B)
┌─────────────────────────────────────────────┴────────────┐
│ Display Screen (CRT Driver Cathodes / Flat Panel Source) │
└──────────────────────────────────────────────────────────┘
```

The **Video Controller (CRTC)** maintains:
- Horizontal Line Counter ($X$) and Vertical Line Counter ($Y$).
- Direct Memory Access (DMA) address generator: $\text{Offset} = (Y \times \text{Row\_Stride}) + X$.
- At every tick of the **Pixel Clock** ($f_{\text{pixel}}$), pixel data is loaded into a high-speed shift register, indexed through the Color Palette (LUT), converted into voltage by a triple 8-bit Video DAC, and fed to cathode amplifiers.

---

### Random Scan (Vector / Calligraphic / Stroke-Writing) Displays

In a **Random Scan** display, the electron beam is never driven across empty screen regions. Instead, the beam acts as an automated physical pen, deflected **strictly along the geometry of lines, curves, and vectors** specified in an application's display list.

```
       (X1, Y1) *
                 \
                  \   Beam ON (Drawing line segment)
                   \
                    ▼
                     * (X2, Y2)
                     .
                     . Beam Blanked (Rapid slew to new coordinate)
                     .
       (X3, Y3) * - - -
```

#### 1. Display Architecture & The Display Processing Unit (DPU)
A random scan terminal contains a dedicated vector graphics processor called the **Display Processing Unit (DPU)** or Display Controller:
1. **Display File (Display Buffer)**: A continuous block of memory containing low-level vector opcodes:
   ```asm
   MOVE_TO   X1, Y1   ; Beam blanked, rapid deflection to start point
   LINE_TO   X2, Y2   ; Beam unblanked, constant-velocity draw to endpoint
   SET_INTEN I_VAL    ; Set beam current (brightness)
   JUMP      ADDR     ; Loop back to display file origin
   ```
2. **Vector Generator (Analog Ramp Integrator)**: Unlike raster DACs that output point voltages, the vector generator outputs coordinated linear voltage ramps:
   $$V_x(t) = V_{x1} + \left(\frac{X_2 - X_1}{\Delta T}\right) t, \quad V_y(t) = V_{y1} + \left(\frac{Y_2 - Y_1}{\Delta T}\right) t$$
   These dual ramps drive wideband, linear deflection amplifiers directly connected to the deflection coils.
3. **Variable Refresh Dynamics & Flicker Limitation**:
   Because drawing time is directly proportional to cumulative drawn line length ($L_{\text{total}}$):
   $$T_{\text{frame}} = \sum_{i=1}^N \left( \frac{\text{Length}_i}{v_{\text{deflect}}} + T_{\text{position}} + T_{\text{blank}} \right)$$
   If an application attempts to render too many vectors ($N$ too large), $T_{\text{frame}}$ exceeds $1/30\text{ s}$ ($\approx 33.3\text{ ms}$), causing the refresh rate to plunge below the critical flicker frequency.

---

### Comparative Analysis: Raster Scan vs. Random Scan

| Dimension | Raster Scan Architecture | Random Scan (Vector) Architecture |
|---|---|---|
| **Deflection Principle** | Fixed periodic raster grid sweep across entire screen. | Directed coordinate-to-coordinate beam deflection along line paths only. |
| **Deflection Waveform** | Resonant sawtooth sweep (easy, cheap, high-speed resonant coils). | Arbitrary linear ramps; requires expensive, linear, wide-bandwidth push-pull power amps. |
| **Refresh Rate** | Absolutely constant ($60\text{–}240\text{ Hz}$), independent of scene complexity. | Variable; inversely proportional to total number and length of vectors. Denser scenes induce flicker. |
| **Resolution** | Discretized pixel matrix (e.g., $1920 \times 1080$, $3840 \times 2160$). Limited by grid pitch. | Continuous mathematical vector resolution (effectively infinite, limited only by beam spot diameter). |
| **Aliasing & Artifacts** | Subject to spatial quantization noise ("jaggies", staircase stepping on diagonal lines). | Zero spatial aliasing; lines are perfectly smooth continuous analog traces. |
| **Shading & Solid Areas** | Natively renders solid planar polygons, smooth gouraud/phong shading, textures, photos. | Inherent inability to fill solid areas efficiently; restricted to wireframes, outlines, and stroke text. |
| **Memory Structure** | Full Frame Buffer proportional to $\text{Width} \times \text{Height} \times \text{BitDepth}$. | Display File (Command List) proportional to number of primitives ($N_{\text{edges}}$). |
| **Primary Applications** | Modern computing, GUIs, photographic imaging, video games, CAD visualization. | Air Traffic Control (ATC) radar, analog oscilloscopes, 1980s vector arcade games (*Asteroids*, *Tempest*). |

---

### Color CRT Techniques: Beam Penetration vs. Shadow Mask

#### 1. Beam Penetration Method (Multi-Layer Phosphor CRT)
Used primarily in military vector systems and early color displays.
- **Physical Construction**: Two distinct phosphor layers coated onto the inner face of the screen without any physical mask:
  - *Outer layer (closer to gun)*: Red-emitting phosphor (e.g., $\text{Y}_2\text{O}_2\text{S:Eu}$), lower density.
  - *Inner layer (against glass)*: Green-emitting phosphor (e.g., $\text{ZnS:Cu}$), higher density with higher excitation threshold.
- **Principle of Operation**: The accelerating anode voltage determines the kinetic energy of striking electrons and thus their **depth of physical penetration** into the phosphor layers:
  - **Low Accelerating Voltage ($\approx 9\text{–}10\text{ kV}$)**: Electrons lack momentum; they stop entirely in the outer red phosphor layer $\implies$ **Red Display**.
  - **Intermediate Voltages ($\approx 12\text{–}14\text{ kV}$)**: Electrons penetrate outer layer and partially excite the inner layer $\implies$ **Orange / Yellow Display**.
  - **High Accelerating Voltage ($\approx 16\text{–}18\text{ kV}$)**: Electrons blast through the red layer and expend almost all energy exciting the deep green phosphor $\implies$ **Green Display**.
- **Severe Limitations**:
  - Only four discernible colors: Red, Orange, Yellow, Green. Cannot produce Blue or true White.
  - Switching accelerating anode voltage between $10\text{ kV}$ and $18\text{ kV}$ at high frequencies requires heavy-duty high-voltage switching circuits; changes deflection sensitivity ($\theta \propto 1/\sqrt{V_a}$), requiring dynamic deflection gain compensation.
  - Completely obsolete; replaced by shadow-mask technology.

#### 2. Shadow Mask CRT (Delta-Delta and In-Line Guns)
The universal standard for all full-color CRT monitors and televisions.

```
                  ┌───────────────────────────────┐
                  │    SHADOW MASK CRT            │
  Electron Guns   │                               │
  ┌───┐ (Red)     │                               │      Phosphor Screen
  │ R │─────────┐ │       Shadow Mask             │      (Triad of dots)
  └───┘         │ │       (Perforated sheet)      │
  ┌───┐ (Green) ┼─┼─────┐      ┌──┐               │       ┌─┐ Red Dot
  │ G │─────────┼─┼───┐ │      │  │ Aperture      │      ┌┤R├┐
  └───┘         │ │   │ │      │  │               │      │└─┘│
  ┌───┐ (Blue)  │ │   │ └──────┼──┼───────────────┼─────►│┌─┐│ Green Dot
  │ B │─────────┘ │   └────────┼──┼───────────────┼─────►││G││
  └───┘           │            │  │               │      │└─┘│
                  │            │  │               │      │┌─┐│ Blue Dot
                  │            └──┘               │      └┤B├┘
                  │                               │       └─┘
                  └───────────────────────────────┘
```

- **Electron Gun Arrangements**:
  - *Delta-Delta Triad*: Three electron guns placed at the vertices of an equilateral triangle.
  - *In-Line (Trinitron/Slotted)*: Three guns mounted horizontally in a straight line.
- **Shadow Mask Metal Grille**: A fine invar/steel sheet perforated with hundreds of thousands of microscopic apertures ($\approx 300,000\text{ to } 1,000,000$) placed $10\text{–}15\text{ mm}$ directly behind the phosphor screen.
- **Geometric Alignment**:
  - The three electron beams are emitted from three slightly separated spatial angles.
  - They converge precisely at the aperture plane of the shadow mask.
  - Due to the geometric parallax angle, the beam from the Red gun can **only** pass through the hole along an angle that strikes the Red phosphor dot. The shadow mask physically occludes (shadows) the Green and Blue dots from the Red beam.
  - Independently modulating the beam currents of the R, G, and B guns mixes light intensities additively, reproducing millions of colors across the RGB gamut.
- **Dot Pitch**: The center-to-center distance between adjacent triad phosphor dots of the same color (typically $0.22\text{ mm}$ to $0.28\text{ mm}$). Finer dot pitch yields higher spatial resolution.

---

### Alternative Display Technologies

#### 1. Direct View Storage Tube (DVST)
Developed by Tektronix to eliminate the need for expensive refresh buffer memory in vector systems:
- **Architecture**: Employs two completely separate sets of electron guns within one envelope:
  1. *Writing Gun*: High-energy, focused electron beam that traces vectors once across a dielectric **Storage Mesh** situated behind the screen. The high velocity knocks off secondary electrons, leaving a positively charged electrostatic pattern.
  2. *Flood Guns (pair of low-velocity continuous emitters)*: Emit a wide, unfocused cloud of low-energy electrons across the entire screen area. Where the storage mesh is positively charged, flood electrons pass through and keep the phosphor continuously illuminated; where uncharged, flood electrons are repelled.
- **Advantages**: Completely flicker-free image display without needing a frame buffer; infinite persistence; ultra-high line capacity (thousands of vectors without degradation).
- **Disadvantages**: Cannot selectively erase a single line (erasing requires discharging the entire storage mesh with an eye-straining green flash); no animation; low contrast; no dynamic color.

#### 2. Flat Panel Displays: Emissive vs. Non-Emissive
Flat panel displays are structurally partitioned by whether pixels generate their own luminescence or modulate external illumination:

```
                          FLAT PANEL DISPLAYS
                                   │
         ┌─────────────────────────┴────────────────────────┐
         ▼                                                  ▼
   EMISSIVE DISPLAYS                              NON-EMISSIVE DISPLAYS
   (Generate own light)                           (Modulate external light)
   • Plasma Display Panels (PDP)                  • Liquid Crystal Displays (LCD)
   • Organic LEDs (OLED / AMOLED)                   - Twisted Nematic (TN)
   • Inorganic LEDs / Micro-LED                     - In-Plane Switching (IPS)
   • Electroluminescent Displays (ELD)              - Vertical Alignment (VA)
```

| Parameter | Emissive Displays (e.g., OLED, PDP) | Non-Emissive Displays (e.g., TFT-LCD) |
|---|---|---|
| **Light Source** | Each sub-pixel is a self-luminous emitter (electroluminescence or gas discharge). | Requires continuous external backlight unit (CCFL or White LED array). |
| **Black Level & Contrast** | Infinite contrast ratio. True blacks achieved by turning individual pixels completely OFF ($0\text{ cd/m}^2$). | Poor black levels; liquid crystals cannot completely block $100\%$ of backlight leakage ($0.1\text{ to } 0.5\text{ cd/m}^2$). |
| **Response Time** | Ultra-fast ($\approx 0.01\text{ to } 0.1\text{ ms}$). No molecular physical realignment needed. | Slower ($1\text{ to } 5\text{ ms}$). Molecular twist/rotation exhibits fluid viscoelastic lag. |
| **Power Consumption** | Variable: proportional to average picture level (APL). Pure black consumes near-zero power. | Fixed: backlight runs at full power regardless of whether screen displays white or black. |
| **Lifespan & Burn-In** | Organic compounds degrade differentially over time (blue sub-pixel degradation); susceptible to burn-in. | Extremely stable inorganic crystals; zero risk of permanent burn-in. |

#### 3. Active-Matrix Liquid Crystal Display (TFT-LCD) Architecture
A modern LCD functions as an electrically controlled light valve modulating polarized light:
1. **Backlight Unit**: Edge-lit or direct-array white LEDs produce uniform unpolarized illumination.
2. **Polarizer 1**: Linearly polarizes incident light along a primary axis (e.g., vertical).
3. **Thin-Film Transistor (TFT) Glass Substrate**: An active matrix of amorphous silicon (a-Si) or IGZO transistors providing individual voltage control to each sub-pixel capacitor without crosstalk.
4. **Liquid Crystal Layer (Nematic Phase)**:
   - *Zero Applied Voltage (Normally White TN cell)*: The alignment layers are rubbed at $90^\circ$ relative angles. The elongated nematic liquid crystal molecules form a continuous $90^\circ$ helical twist. Polarized light entering the cell has its polarization plane rotated $90^\circ$ by optical waveguiding.
   - *With Applied Electric Field*: An electric field applied across the cell forces the dipole liquid crystal molecules to untwist and align parallel to the field lines.
5. **Color Filter Matrix**: Microscopic red, green, and blue dyed resin filters aligned over respective sub-pixel cells.
6. **Polarizer 2 (Analyzer)**: Polarizing axis oriented at $90^\circ$ (perpendicular) to Polarizer 1.
   - In unenergized state: The light's $90^\circ$ rotated polarization matches Polarizer 2 $\implies$ **Sub-pixel transmits light (Bright)**.
   - In energized state: Un-twisted light encounters crossed Polarizer 2 and is absorbed $\implies$ **Sub-pixel blocked (Dark)**.

---

## 2. Example: System Architecture Diagrams

### A. Complete Raster-Scan Display Subsystem
```
+-------------------------------------------------------------------------+
|                              HOST COMPUTER                              |
|   +-----------------------+                 +-----------------------+   |
|   |   Application CPU     | <=============> |  System RAM (DDR5)    |   |
|   +-----------------------+                 +-----------------------+   |
+-----------------------------------┬────────────────────────────────-----+
                                    │ PCIe Bus (16 GB/s)
                                    ▼
+-------------------------------------------------------------------------+
|                          GRAPHICS CARD (GPU)                            |
|                                                                         |
|   +────────────────────────┐                 +──────────────────────┐   |
|   │ 3D Geometry Core &     │ ══════════════► │ Frame Buffer (VRAM)  │   |
|   │ Rasterizer Pipelines   │                 │ GDDR6 / HBM3 Memory  │   |
|   +────────────────────────┘                 +──────────┬───────────┘   |
|                                                         │               |
|                                                         │ 60-144 Hz     |
|                                                         │ Read Scanout  |
|                                                         ▼               |
|   +────────────────────────┐                 +──────────────────────┐   |
|   │ Display Timing Engine  │                 │ Scanout Controller / │   |
|   │  • HSync Generator     │ ──────────────► │ Pixel FIFO Buffer    │   |
|   │  • VSync Generator     │                 +──────────┬───────────┘   |
|   │  • Blanking Logic      │                            │               |
|   +───────────┬────────────┘                            ▼               |
|               │ HSync, VSync                 +──────────────────────┐   |
|               │                              │ Triple Video DAC /   │   |
|               │                              │ TMDS HDMI Encoder    │   |
|               │                              +──────────┬───────────┘   |
+───────────────┼─────────────────────────────────────────┼───────────────+
                │                                         │ Pixel Stream
                ▼                                         ▼
+─────────────────────────────────────────────────────────────────────────+
|                             DISPLAY MONITOR                             |
|   +-----------------------------------------------------------------+   |
|   | Deflection Yoke Coils / Source-Gate Row Drivers                 |   |
|   | CRT Phosphor Surface / Active Matrix LCD / OLED Panel           |   |
|   +-----------------------------------------------------------------+   |
+-------------------------------------------------------------------------+
```

---

## 3. Applications & Use Cases

1. **Air Traffic Control (ATC) En-Route Radars**:
   Standardized on vector displays (such as the Sony DDL-2800 calligraphic monitor) because radar targets are discrete point coordinates, velocity vectors, flight level numerals, and beacon transponder codes. Calligraphic rendering maintains needle-sharp vector clarity at all zoom levels without aliasing or pixelation.
2. **Modern Real-Time Gaming & High-Refresh Displays**:
   Modern raster displays operating at $144\text{ Hz}$ to $360\text{ Hz}$ with Adaptive Sync (NVIDIA G-Sync / VESA FreeSync) dynamically synchronize the vertical blanking interval to GPU render completion, eliminating raster screen tearing.
3. **Medical Imaging Diagnostic Workstations**:
   High-luminance monochrome diagnostic raster monitors ($5\text{ MP}$ to $12\text{ MP}$) utilize $10\text{–}12\text{ bit}$ grayscale LUTs conforming strictly to the DICOM Part 14 Grayscale Standard Display Function (GSDF) for detecting microcalcifications in mammography.

---

## 4. Solved Numerical / Analytical Examples

### Example 1: Display File Capacity vs. Refresh Rate in Calligraphic Displays [KTU May 2019 / Dec 2018]
**Problem**:
A calligraphic (random scan) vector monitor has an electron beam deflection velocity of $v_{\text{deflect}} = 0.8\text{ mm}/\mu\text{s}$. The beam requires $T_{\text{pos}} = 2.5\ \mu\text{s}$ for unilluminated repositioning between segment endpoints and $T_{\text{switch}} = 0.5\ \mu\text{s}$ to turn the beam on and off.
1. Compute the time required to trace an average line segment of physical length $40\text{ mm}$.
2. If the display must refresh at $\ge 50\text{ Hz}$ to prevent noticeable phosphor flicker, calculate the maximum number of line segments that can be drawn in the display list.

**Solution**:
1. **Time per Line Segment**:
   - Deflection drawing time:
     $$T_{\text{draw}} = \frac{\text{Distance}}{v_{\text{deflect}}} = \frac{40\text{ mm}}{0.8\text{ mm}/\mu\text{s}} = 50.0\ \mu\text{s}$$
   - Total overhead time:
     $$T_{\text{overhead}} = T_{\text{pos}} + T_{\text{switch}} = 2.5\ \mu\text{s} + 0.5\ \mu\text{s} = 3.0\ \mu\text{s}$$
   - Total duration per line:
     $$T_{\text{line}} = T_{\text{draw}} + T_{\text{overhead}} = 50.0 + 3.0 = 53.0\ \mu\text{s}$$
2. **Maximum Vector Count at $50\text{ Hz}$**:
   - Refresh frame interval:
     $$T_{\text{frame}} = \frac{1}{50\text{ Hz}} = 0.02\text{ s} = 20,000\ \mu\text{s}$$
   - Maximum line capacity:
     $$N_{\max} = \left\lfloor \frac{T_{\text{frame}}}{T_{\text{line}}} \right\rfloor = \left\lfloor \frac{20,000\ \mu\text{s}}{53.0\ \mu\text{s}} \right\rfloor = \lfloor 377.35 \rfloor = 377 \text{ lines}$$
   If the scene contains $> 377$ lines, the frame duration exceeds $20\text{ ms}$, dropping the refresh rate below $50\text{ Hz}$ and introducing visible flicker.

---

### Example 2: Bandwidth and Memory Transfer Rate in High-Resolution Raster Systems [KTU Dec 2023]
**Problem**:
A $4\text{K}$ UHD monitor ($3840 \times 2160$ resolution) operates at $120\text{ Hz}$ progressive scan with $30\text{-bit}$ Deep Color ($10\text{ bits}$ per RGB channel, stored as $32\text{ bits}$ per pixel in memory).
1. Assuming a combined horizontal and vertical blanking overhead of $18\%$, calculate the required pixel clock frequency in MHz.
2. Calculate the required continuous memory bandwidth from the frame buffer in Gigabytes per second ($\text{GB/s}$) and the digital transmission bit rate in Gigabits per second ($\text{Gbps}$).

**Solution**:
1. **Total Clocked Pixels per Frame**:
   $$\text{Active Pixels} = 3840 \times 2160 = 8,294,400\text{ pixels}$$
   $$\text{Total Pixels (with 18% blanking)} = \frac{8,294,400}{1 - 0.18} = \frac{8,294,400}{0.82} \approx 10,115,122\text{ pixels/frame}$$
2. **Pixel Clock Frequency**:
   $$f_{\text{pixel}} = \text{Total Pixels} \times \text{Refresh Rate} = 10,115,122 \times 120 \approx 1,213,814,640\text{ Hz} \approx 1.214\text{ GHz (1213.8 MHz)}$$
3. **Data Bandwidth & Transmission Rate**:
   - Bit rate across digital link (active video + blanking payload at 32 bpp):
     $$\text{Bit Rate} = f_{\text{pixel}} \times 32\text{ bits} = 1.2138 \times 10^9 \times 32 \approx 38.84\text{ Gbps}$$
     *(This requires DisplayPort 2.0 UHBR 10 or HDMI 2.1 Fixed Rate Link 48G)*.
   - Frame buffer memory read bandwidth (scanning active video):
     $$\text{VRAM Bandwidth} = 3840 \times 2160 \times 4\text{ bytes} \times 120\text{ s}^{-1} \approx 3.981 \times 10^9\text{ B/s} \approx 3.98\text{ GB/s}$$

---

### Example 3: Shadow-Mask Moiré Aliasing and Triad Geometry [KTU June 2022]
**Problem**:
A color shadow-mask CRT has a physical horizontal display width of $360\text{ mm}$ and a mask aperture pitch of $a = 0.24\text{ mm}$.
1. Compute the maximum number of color pixel triads that can be resolved along a single horizontal scanline.
2. Explain mathematically why driving this monitor at a video resolution of $1920 \times 1080$ produces optical moiré fringing artifacts.

**Solution**:
1. **Horizontal Triad Count**:
   $$N_{\text{triad}} = \frac{\text{Display Width}}{\text{Aperture Pitch}} = \frac{360\text{ mm}}{0.24\text{ mm}} = 1500\text{ triads}$$
   The physical mask can resolve at most $1500$ discrete color triads horizontally.
2. **Moiré Fringing Explanation**:
   - The spatial sampling frequency of the physical shadow mask is:
     $$f_{\text{mask}} = \frac{1}{a} = \frac{1}{0.24\text{ mm}} \approx 4.167\text{ cycles/mm}$$
   - The spatial Nyquist limit of the mask is:
     $$f_{\text{Nyquist}} = \frac{f_{\text{mask}}}{2} \approx 2.083\text{ cycles/mm}$$
   - When a video signal of $1920$ pixels is driven across $360\text{ mm}$:
     $$f_{\text{signal}} = \frac{1920\text{ pixels}}{360\text{ mm}} \approx 5.333\text{ pixels/mm}$$
   - Because $f_{\text{signal}} > 2 \cdot f_{\text{Nyquist}}$, the electron beam spots fall irregularly across adjacent aperture holes. The non-linear multiplication of the two spatial patterns produces low-frequency beat frequencies:
     $$f_{\text{beat}} = |f_{\text{signal}} - f_{\text{mask}}| = |5.333 - 4.167| = 1.166\text{ cycles/mm}$$
   - This low spatial frequency ($1.166\text{ cycles/mm} \implies \lambda_{\text{beat}} \approx 0.86\text{ mm}$) manifests as visible dark-and-bright wavy interference bands across the screen known as **moiré patterns**.

---

## 5. Previous Year Questions & Solutions

---

### Question 1 [June 2024 Q1 / Dec 2023 Q11a / Jan 2023 Q11a / June 2022 Q11a / Dec 2021 Q11a / Dec 2020 Q11a / Dec 2019 Q11b / May 2019 Q11b / Dec 2018 Q11a — 4–5 Marks]
**Question**: Describe the working of Refresh Cathode-Ray Tubes with a neat diagram.

**Solution**:

A **Refresh Cathode Ray Tube (CRT)** operates by emitting a continuous stream of electrons, focusing and accelerating them through an electron gun assembly, electrodynamically deflecting the beam using magnetic coils, and exciting a luminescent phosphor screen to produce visible light.

```
       ┌─────────────────────────────────────────────────────────────┐
       │                 REFRESH CRT ARCHITECTURE                    │
       │                                                             │
Heater │  Control Grid (G1)                                          │
 ┌──┐  │     ┌─┐                                                     │
─┤  ├──┼─────┤ │  Pre-accelerating  Focusing  Accelerating            │
 └──┘  │     └─┘      Anode          Anode       Anode               │
Cathode│               ┌──┐           ┌──┐       ┌──┐     Deflection │
  (K)  │               │  │           │  │       │  │        Yoke    │
       │               │  │           │  │       │  │       ┌──┐     │  Phosphor
       │               └──┘           └──┘       └──┘       │  │     │   Screen
       │                                                    └──┘     │   ░░░░░░
       │ ─── ─── ─── ─── ─── ─── ─── ─── ─── ─── ─── ─── ─── ───────┼──►░░░░░░
       │                       Electron Beam                         │   ░░░░░░
       └─────────────────────────────────────────────────────────────┘
```

**Working Mechanism**:
1. **Thermionic Emission**: An indirect heating coil heats an oxide-coated cathode to $\approx 1000\text{ K}$, causing electrons to boil off from the surface into the vacuum.
2. **Beam Current & Intensity Modulation**: The control grid ($G_1$) surrounds the cathode and is biased with a negative voltage. Adjusting this negative bias varies the number of electrons passing through its aperture, controlling pixel brightness. Driving $G_1$ highly negative turns the beam completely off (blanking).
3. **Focusing and Acceleration**: Electrostatic fields generated between the pre-accelerating, focusing, and high-voltage accelerating anodes ($+15\text{ kV}$ to $+30\text{ kV}$) converge the divergent electrons into a fine beam and accelerate them to roughly one-third the speed of light.
4. **Deflection System**: Orthogonal magnetic coils in the deflection yoke generate horizontal and vertical magnetic fields, deflecting electrons by Lorentz force: $\vec{F} = q(\vec{v} \times \vec{B})$.
5. **Phosphor Excitation & Need for Refresh**: When high-velocity electrons impact the zinc-sulfide phosphor coating, kinetic energy is converted into visible light (fluorescence). Once the beam moves away, the light decays exponentially (phosphorescence). Because phosphor luminescence drops below visible levels within milliseconds ($1\text{–}100\text{ ms}$), the image must be **redrawn (refreshed) at least 60 times per second** to maintain a persistent, flicker-free picture to the human eye.

---

### Question 2 [June 2024 Q11a / June 2022 Q11b / Dec 2018 Q11b — 5 Marks]
**Question**: Explain the working of the Beam Penetration method for producing color in CRT displays.

**Solution**:

The **Beam Penetration Method** is a technique used primarily in random-scan (vector) displays to generate multiple colors without using an aperture mask.

**Physical Construction**:
- A single electron gun is used.
- The inner face of the CRT is coated with **two distinct concentric phosphor layers**:
  1. An outer layer (facing the electron gun) of **Red phosphor**.
  2. An inner layer (adhering directly to the glass faceplate) of **Green phosphor**, separated by a thin dielectric barrier.

```
Low Voltage (9-10 kV)              Medium Voltage (12-14 kV)            High Voltage (16-18 kV)
   Electron Beam                      Electron Beam                       Electron Beam
        │                                  │                                   │
        ▼                                  ▼                                   ▼
┌──────────────────┐               ┌──────────────────┐                ┌──────────────────┐
│  Red Phosphor    │◄──Stops       │  Red Phosphor    │◄──Partial      │  Red Phosphor    │◄──Punches
├──────────────────┤               ├──────────────────┤                ├──────────────────┤   through
│  Green Phosphor  │               │  Green Phosphor  │◄──Partial      │  Green Phosphor  │◄──Fully
├──────────────────┤               ├──────────────────┤                ├──────────────────┤   Excites
│   Glass Face     │               │   Glass Face     │                │   Glass Face     │
└──────────────────┘               └──────────────────┘                └──────────────────┘
    Output: RED                        Output: ORANGE/YELLOW               Output: GREEN
```

**Operating Principle**:
Color reproduction is controlled by varying the **accelerating anode voltage** ($V_a$):
1. **Low Potential ($\approx 9\text{–}10\text{ kV}$)**: Electrons possess low kinetic energy. They penetrate only the outer red phosphor layer, generating **Red light**.
2. **Intermediate Potentials ($\approx 12\text{–}14\text{ kV}$)**: Electrons penetrate deeper, exciting both layers simultaneously. The additive combination of red and green emissions produces **Orange** or **Yellow**.
3. **High Potential ($\approx 16\text{–}18\text{ kV}$)**: Electrons penetrate completely through the outer red layer into the dense green phosphor layer, where the vast majority of kinetic energy is discharged, generating **Green light**.

**Advantages**:
- Simple physical tube construction; no fragile shadow mask required.
- Capable of extremely high vector resolution because there is no aperture grid to limit dot pitch.

**Limitations**:
- Limited color gamut: Only 4 colors (Red, Orange, Yellow, Green). Cannot generate Blue, Cyan, Magenta, or White.
- Rapid switching of multi-kilovolt power supplies requires expensive, complex switching electronics.
- Deflection sensitivity varies inversely with the square root of accelerating voltage ($\theta \propto 1/\sqrt{V_a}$), causing image size distortion unless compensated dynamically by deflection gain circuitry.

---

### Question 3 [Dec 2023 Q11b / Dec 2018 Q11a — 5 Marks]
**Question**: Explain the working of a random scan display system with a suitable diagram.

**Solution**:

In a **Random Scan Display System** (also known as a Vector, Calligraphic, or Directed-Beam system), the electron beam is directed **only to the specific coordinates on the screen where graphics primitives (lines and curves) are to be drawn**. The beam does not sweep systematically across empty background regions.

```
+--------------------+        System Bus        +--------------------+
|   Application CPU  | <======================> |    System RAM      |
+--------------------+                          +--------------------+
                                                           │
                                                           │ Display List DMA
                                                           ▼
+--------------------+                          +--------------------+
| Display Processor  | <─────────────────────── | Display Buffer     |
| Unit (DPU)         |                          | (Display File)     |
+─────────┬──────────+                          +--------------------+
          │
          ├─────────────────────────────────┐
          │ Digital Coordinate Vectors      │ Intensity On/Off
          ▼                                 ▼
+--------------------+            +--------------------+
| Vector Generator / |            | Beam Intensity /   |
| DAC Integrator     |            | Blanking Circuit   |
+─────────┬──────────+            +─────────┬──────────+
          │ Linear X, Y Ramps               │ Z-Modulation
          ▼                                 ▼
+--------------------+            +--------------------+
| X, Y Linear        |            | Vector CRT Monitor |
| Deflection Amps    | ─────────► | (Deflection Coils) |
+--------------------+            +--------------------+
```

**Operational Steps**:
1. **Display File Execution**: The application processor converts geometric entities into a sequence of drawing commands stored in the **Display Buffer** (Display File). Instructions include `MOVE_TO(X, Y)`, `LINE_TO(X, Y)`, and `SET_INTENSITY(I)`.
2. **Display Processing Unit (DPU)**: The DPU functions as a specialized coprocessor that fetches instructions sequentially from the display file.
3. **Vector Generator**: Converts endpoint digital coordinate pairs into coordinated analog voltage ramps for the horizontal and vertical deflection amplifiers, sweeping the beam at a constant linear speed from start point to end point.
4. **Blanking Control**: During a `MOVE_TO` operation, the beam is blanked (turned off) while deflecting rapidly to the new starting coordinate. During a `LINE_TO`, the beam is unblanked at the desired intensity.
5. **Periodic Refresh**: After executing the entire display list, a jump command resets execution to the start of the file. The entire file is re-executed $30\text{ to } 60\text{ times per second}$ to prevent phosphor decay flicker.
6. **Flicker Trade-off**: If the display file contains too many line segments, total cycle time exceeds the phosphor persistence period ($> 33\text{ ms}$), causing visible screen flicker.

---

### Question 4 [May 2019 Q11b / Dec 2021 Q11a / Dec 2019 Q11a — 5 Marks]
**Question**: With the help of a neat diagram, explain the working of a Direct View Storage Tube (DVST) display.

**Solution**:

The **Direct View Storage Tube (DVST)** is a CRT-based vector display technology that stores visual patterns as an electrostatic charge distribution directly on a dielectric mesh located inside the tube face, eliminating the need for periodic image refreshing and dedicated frame buffer memory.

```
      ┌─────────────────────────────────────────────────────────────┐
      │             DIRECT VIEW STORAGE TUBE (DVST)                 │
      │                                                             │
Writing Gun                                                         │
  ┌──┐                                                              │
  │  │─── ─── High-Velocity Electron Beam ─── ─── ───┐              │
  └──┘                                               │              │
                                                     ▼              │
Flood Guns (Continuous)                          Storage Mesh       │
  ┌──┐                                           (Dielectric)       │
  │  │===                                             ┌──┐ Phosphor │
  └──┘   === Low-Velocity Flood Electrons             │  │ Screen   │
  ┌──┐   === ════════════════════════════════════════►│  │ ░░░░░░░  │
  │  │===                                             │  │ ░░░░░░░  │
  └──┘                                                │  │ ░░░░░░░  │
                                                Collector │  │ Glass │
                                                  Mesh    └──┘      │
      └─────────────────────────────────────────────────────────────┘
```

**Internal Components**:
1. **Writing Gun**: A focused electron gun producing high-velocity electrons directed by deflection plates to trace vector lines.
2. **Flood Guns (pair)**: Low-voltage electron guns continuously generating an unfocused, wide-angle cloud of low-velocity electrons across the entire screen area.
3. **Collector Mesh**: A conductive wire grid biased at a positive potential ($+100\text{ to }+200\text{ V}$) to collect secondary electrons.
4. **Storage Mesh**: A fine metal screen coated with a dielectric material (such as magnesium fluoride) mounted immediately behind the phosphor target.

**Working Principle**:
1. **Writing Phase**: The writing gun traces vectors across the storage mesh. High-velocity electrons strike the dielectric, causing **secondary electron emission** (ratio $> 1$). Emitted secondary electrons are attracted to the positively charged collector mesh. This leaves the targeted regions of the dielectric with a net **positive electrostatic charge**.
2. **Storage and Continuous Display (Flood Phase)**: The flood guns continuously emit a cloud of low-energy electrons toward the screen:
   - In unwritten (negatively/neutrally charged) areas of the storage mesh, flood electrons are electrostatically repelled back toward the collector mesh $\implies$ **Phosphor remains unlit**.
   - In written (positively charged) areas, the local positive potential accelerates flood electrons through the mesh pores, causing them to strike the phosphor screen continuously $\implies$ **Vector lines glow continuously without flicker**.
3. **Erasing**: Because charges are held on the dielectric mesh, individual vectors cannot be selectively deleted. To erase, a positive voltage pulse is applied to the storage mesh to equalize charges across the surface, followed by a negative pulse. This produces a characteristic bright flash across the entire screen before clearing the image.

---

### Question 5 [Sep 2020 Q2 / June 2022 Q11b / Dec 2021 Q11b / Dec 2019 Q11a — 4 Marks]
**Question**: Differentiate between emissive and non-emissive flat panel displays with suitable examples.

**Solution**:

Flat panel displays are divided into two fundamental physical classes depending on how light is produced and presented:

| Parameter | Emissive Flat Panel Displays | Non-Emissive Flat Panel Displays |
|---|---|---|
| **Operating Principle** | Pixels are independent, active light-emitting transducers (convert electrical energy directly into light via electroluminescence or gas ionization). | Pixels do not emit light; they act as spatial light valves that modulate, transmit, or reflect light from an external source. |
| **Primary Examples** | Organic Light-Emitting Diodes (OLED / AMOLED), Plasma Display Panels (PDP), Inorganic Micro-LED, Electroluminescent Displays (ELD). | Thin-Film Transistor Liquid Crystal Displays (TFT-LCD), Electronic Paper Displays (E-Ink). |
| **Backlight Requirement** | **No backlight required**. Each sub-pixel generates its own photons independently. | **Requires an external backlight unit** (LED or CCFL edge-lit/direct array) or ambient incident light. |
| **Contrast Ratio & Black Levels** | **Infinite contrast ratio**. Deep, absolute blacks are achieved by turning off sub-pixels ($0\text{ nits}$). | **Limited contrast ratio** ($1000:1$ to $3000:1$). Residual light leaks through unaligned liquid crystals, resulting in grayish blacks. |
| **Viewing Angles** | Extremely wide ($> 178^\circ$) with minimal color distortion or brightness degradation. | Narrower viewing angles; contrast and color saturation degrade off-axis due to liquid crystal phase retardation. |
| **Response Time** | Nearly instantaneous ($\approx 0.01\text{ ms}$ to $0.1\text{ ms}$); ideal for high-motion fidelity. | Slower ($1\text{ ms}$ to $10\text{ ms}$) due to the physical viscoelastic viscosity of rotating liquid crystal molecules. |
| **Power Consumption** | Content-dependent: displays with dark backgrounds consume minimal power; full-white screens consume high power. | Constant: backlight power remains constant regardless of whether the displayed scene is completely black or bright white. |

---

### Question 6 [Sep 2020 Q12a / Dec 2020 Q13b — 5 Marks]
**Question**: Explain the working of a Shadow Mask color CRT display.

**Solution**:

The **Shadow Mask CRT** is the primary display technology used to produce full-color imagery in television and computer monitors.

```
       Electron Guns
         ┌───┐ (Red)
         │ R │─────────┐
         └───┘         │
         ┌───┐ (Green) ┼─────────┐
         │ G │─────────┼───────┐ │
         └───┘         │       │ │      Shadow Mask           Phosphor Screen
         ┌───┐ (Blue)  │       │ └────► ┌──┐ Aperture           ┌───┐ Red Dot
         │ B │─────────┘       └──────► │  │                  ┌─┤ R ├─┐
         └───┘                 ───────► │  │ ────────────────►│ └───┘ │ Green Dot
                                        └──┘                  │ ┌───┐ │
                                                              └─┤ G ├─┘
                                                                └───┘   Blue Dot
```

**Key Components**:
1. **Three Electron Guns**: Dedicated Red ($R$), Green ($G$), and Blue ($B$) electron guns arranged either in a delta configuration (equilateral triangle) or an in-line horizontal strip.
2. **Deflection Yoke & Convergence Coils**: Deflects all three beams simultaneously across the screen while dynamic convergence magnets ensure the three beams converge exactly at the plane of the shadow mask.
3. **Shadow Mask**: A perforated invar or steel sheet containing roughly $300,000\text{ to } 1,000,000$ microscopic circular apertures or vertical slots positioned $\approx 15\text{ mm}$ behind the phosphor faceplate.
4. **Phosphor Dot Triads**: The inner glass faceplate is coated with alternating triads of Red, Green, and Blue phosphor dots (or vertical phosphor stripes in Trinitron/aperture grille designs).

**Principle of Color Generation**:
- The three electron guns are aligned at slightly different spatial angles relative to the shadow mask holes.
- As the converged beams pass through an aperture, they diverge at precise angular trajectories:
  - The beam from the **Red gun** strikes **only the Red phosphor dot**.
  - The beam from the **Green gun** strikes **only the Green phosphor dot**.
  - The beam from the **Blue gun** strikes **only the Blue phosphor dot**.
- The shadow mask physically blocks (shadows) the incorrect phosphor dots from each respective beam.
- By independently modulating the current in each electron gun, the emitted Red, Green, and Blue light intensities vary from $0$ to maximum. Because the phosphor dots in each triad are situated closer than the eye's angular resolving limit ($\approx 1\text{ arcminute}$), the human visual system fuses the three stimulus spots into a single perceived intermediate color from the additive RGB color gamut.
