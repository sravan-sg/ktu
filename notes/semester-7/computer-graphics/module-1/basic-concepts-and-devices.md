# Module I: Basic Concepts in Computer Graphics

## 1. Explanation

### What is Computer Graphics?

**Computer Graphics** is the field of creating, manipulating, and displaying visual content using computers. At its core, it answers a deceptively simple question: *How do we turn mathematical descriptions of objects (numbers, equations, coordinates) into pixels on a screen?*

The fundamental pipeline is:
```
Mathematical Model (vertices, edges, surfaces)
        ↓
Geometric Transformations (translation, rotation, scaling)
        ↓
Projection (3D → 2D)
        ↓
Scan Conversion (continuous geometry → discrete pixels)
        ↓
Display (rasterized image on screen)
```

**Why does this matter?** Every application — from medical imaging and CAD software to video games and GIS — relies on this pipeline. The algorithms you learn in this course are embedded in every GPU manufactured today.

---

### Types of Graphic Devices

#### 1. Input Devices (Interactive Graphic Inputs)

Input devices allow a user to interact with the graphics system by providing positional, gestural, or textual input.

| Category | Device Examples | Data Produced |
|----------|----------------|---------------|
| **Locator** | Mouse, trackball, joystick, touchscreen | 2D coordinate (x, y) |
| **Pick** | Light pen, touch screen | Object identifier on screen |
| **Keyboard** | Standard keyboard | Character/command input |
| **Valuator** | Dial, slider, potentiometer | Scalar value (e.g., zoom level) |
| **Stroke** | Digitizing tablet, gesture recognition | Sequence of (x, y) coordinates |
| **String** | Keyboard | Character sequence |

**Light pen (historical):** Uses a photodetector; when pointed at the screen during the electron beam's scan, it detects the beam's position. Accurate but now obsolete due to flat panel displays.

**Digitizing tablet:** A flat electromagnetic pad + stylus. Absolute positioning (unlike mouse, which is relative). Used extensively in CAD and GIS.

**Logical input device model (Hearn & Baker Ch. 8):** PHIGS and GKS separate physical device from logical function — a program requests a "locator" and the system maps it to whatever physical device exists (mouse, trackball, touch). This abstraction is fundamental to portable graphics API design.

#### 2. Display Devices (Output Devices)

##### A. Raster Scan Display

The dominant modern display technology. The screen is divided into a **rectangular grid of pixels (picture elements)**. The image is stored in a **frame buffer** (video RAM) and the display controller reads it continuously to drive the screen.

**Raster scan principle:**
```
Electron beam sweeps LEFT→RIGHT across each scanline
After each line: horizontal retrace (beam returns to left)
After last line:  vertical retrace (beam returns to top-left)
Field rate: 60–75 Hz (to prevent flicker above CFF threshold)
```

**Key parameters:**
- **Resolution:** Width × Height (e.g., 1920 × 1080 = 2,073,600 pixels)
- **Aspect Ratio:** Ratio of width to height (16:9 for HD)
- **Refresh Rate:** 60–144 Hz. Persistence of phosphor + persistence of human vision (~1/25s) means we perceive continuous motion.
- **Frame Buffer Size:** Resolution × Bits-per-pixel. For 1920×1080 @ 24-bit color: 1920×1080×24 = 49,766,400 bits ≈ 6 MB per frame.

**Color depth:**
| Depth | Colors | Use |
|-------|--------|-----|
| 1 bpp | 2 (monochrome) | Text displays |
| 8 bpp | 256 (indexed palette) | Early VGA |
| 16 bpp | 65,536 (high color) | Mobile, older hardware |
| 24 bpp | 16,777,216 (true color) | Standard today |
| 32 bpp | 24-bit color + 8-bit alpha | With transparency |

**Color lookup table (CLUT / palette):** With 8bpp, each pixel stores an 8-bit index into a 256-entry table. Each table entry holds a 24-bit RGB value. This compresses storage but limits simultaneous colors.

**CRT raster scan (legacy but examinable):** Electron gun controlled by horizontal and vertical deflection circuits. The beam intensity is modulated (brightness = electron beam intensity) as it sweeps. Interlaced scanning (odd lines, then even lines) was used in early TV/monitors to reduce bandwidth requirements while maintaining flicker-free appearance.

##### B. Random Scan Display (Vector Display / Calligraphic Display)

Instead of scanning every pixel, a random scan display draws only the lines/curves that make up the picture. The electron beam is directed directly to only those positions needed.

```
Display file (display list): sequence of instructions
  MOVE TO (x1, y1)
  DRAW TO (x2, y2)
  MOVE TO (x3, y3)
  DRAW TO (x4, y4)
  ...
  REPEAT
```

**Key characteristics:**
- **Resolution:** Theoretically infinite — smooth, flicker-free lines (no discrete pixel grid)
- **Speed:** Proportional to **number of lines** (complex scenes = flicker because refresh rate drops below CFF)
- **Use case:** Early CAD systems (SAGE, Sketchpad), oscilloscopes, air traffic control radar
- **Cannot fill areas:** Only outlines; no solid area fill capability
- **Refresh:** Must redraw the entire scene ~30–60 times/second from the display list

**Comparison — Raster vs Random Scan:**

| Property | Raster Scan | Random Scan |
|----------|-------------|-------------|
| Image representation | Pixel grid (bitmap) | Display list (vector) |
| Line quality | Aliased (staircase effect) | Perfectly smooth |
| Area fill | Easy (bucket fill) | Not directly supported |
| Complexity handling | Fixed cost per frame | Increases with number of primitives |
| Typical resolution | Fixed (e.g., 1920×1080) | Effectively infinite |
| Modern use | All consumer displays | Oscilloscopes, laser shows |
| Color | Full color (RGB per pixel) | Limited (single beam intensity) |

---

## 2. Example

### Frame Buffer Organization

For a 4×4 pixel monochrome display (1 bpp):

```
Frame Buffer (16 bits, row-major):
Row 0: [1][0][1][1]
Row 1: [0][1][0][0]
Row 2: [1][1][1][0]
Row 3: [0][0][1][1]

Pixel (x=2, y=1) → address = y * width + x = 1 * 4 + 2 = index 6 → bit value = 0 (black)
```

For 24-bit color, each pixel occupies 3 consecutive bytes (R, G, B):
```
Pixel (x, y) → byte address = (y * width + x) * 3
Pixel (2, 1) on 4-wide display → byte 18, 19, 20 = R, G, B values
```

### Raster vs Random Scan — Drawing a Triangle

**Raster scan:** Store 3 edge points; run scan-conversion algorithm (rasterize) to fill pixels
```
Scan line y=2: find x-intersections with edges → fill pixels between them
Scan line y=3: find x-intersections → fill pixels
...
```

**Random scan:** Display list contains three DRAW commands:
```
MOVETO (100, 100); DRAWTO (200, 100)
MOVETO (200, 100); DRAWTO (150, 200)
MOVETO (150, 200); DRAWTO (100, 100)
```
No fill — only the three edges are drawn.

---

## 3. Applications & Use Cases

| Domain | Technology Used | Module I Concept Applied |
|--------|----------------|--------------------------|
| **Video Games** | GPU rasterization pipeline | Raster display + frame buffer management |
| **CAD/CAM Systems** | Vector graphics, precision plotters | Random scan principles still in plotters |
| **Medical Imaging (MRI/CT)** | 3D raster volume rendering | Frame buffer at extreme resolutions |
| **Touchscreen UIs** | Capacitive touch grid | Locator device input processing |
| **Broadcast Television** | Interlaced raster scanning | CRT raster principles |
| **Digital Oscilloscopes** | Vector LCD rendering | Random scan display architecture |
| **GIS/Mapping** | Hybrid raster-vector systems | Both display paradigms combined |

---

## 4. Solved Numerical/Analytical Examples

### Example 1: Frame Buffer Memory Calculation

**Problem:** A workstation has a display with resolution 1280 × 1024 pixels and supports 24-bit true color. Calculate:
(a) The total size of the frame buffer in bytes and megabytes
(b) The memory address of pixel (640, 512) in the frame buffer
(c) The size of a double-buffered frame buffer

**Solution:**

(a) **Frame buffer size:**
```
Total pixels = 1280 × 1024 = 1,310,720 pixels
Bits per pixel = 24 (8 bits each for R, G, B)
Total bits = 1,310,720 × 24 = 31,457,280 bits
Total bytes = 31,457,280 / 8 = 3,932,160 bytes
In megabytes = 3,932,160 / (1024×1024) = 3.75 MB
```

(b) **Memory address of pixel (640, 512):**
```
Pixel address = (y × width + x) × bytes_per_pixel
             = (512 × 1280 + 640) × 3
             = (655,360 + 640) × 3
             = 656,000 × 3
             = 1,968,000 bytes from start of frame buffer
```
The R component is at byte 1,968,000, G at 1,968,001, B at 1,968,002.

(c) **Double-buffered:**
```
Double-buffer size = 2 × single buffer = 2 × 3.75 MB = 7.5 MB
```
(Double buffering eliminates screen tearing by rendering to back buffer while displaying front buffer.)

---

### Example 2: Refresh Rate and Flicker Analysis

**Problem:** A raster CRT display with 800×600 resolution uses interlaced scanning (2 fields per frame). 
(a) If the beam draws 800 pixels per line at 30 ns/pixel, calculate the time for one complete scanline (including horizontal retrace of 20% extra time).
(b) What is the maximum number of complete frames per second possible with this timing?
(c) Is the refresh rate above the Critical Fusion Frequency (CFF ≈ 46 Hz for a bright display)?

**Solution:**

(a) **Scanline time:**
```
Active drawing time per line = 800 pixels × 30 ns/pixel = 24,000 ns = 24 µs
Horizontal retrace time = 20% × 24 µs = 4.8 µs
Total scanline time = 24 µs + 4.8 µs = 28.8 µs
```

(b) **Frames per second:**
```
Total scanlines per frame = 600 (for interlaced: 300 lines/field × 2 fields)
Time per field = 300 lines × 28.8 µs/line = 8,640 µs = 8.64 ms
Time per frame = 2 × 8.64 ms = 17.28 ms (plus vertical retrace)
Max frame rate ≈ 1 / 0.01728 ≈ 57.9 frames/second
```

(c) **Flicker analysis:**
```
Field rate = 2 × 57.9 = 115.8 Hz (each field refreshes half the screen)
Since field rate (115.8 Hz) >> CFF (46 Hz), no flicker is perceived. ✓
```
Note: Interlaced scanning effectively doubles the perceived refresh rate vs. the actual frame rate, which is why interlaced was used in early broadcast TV to reduce bandwidth while avoiding flicker.

---

### Example 3: Random Scan Display Complexity Limit

**Problem:** A random-scan display refreshes its display list at 60 Hz. It takes 2 µs to draw each line segment (vector). 
(a) What is the maximum number of line segments that can be displayed without flicker?
(b) A scene has 2,000 line segments. What refresh rate would this scene achieve, and would flicker occur?

**Solution:**

(a) **Maximum segments at 60 Hz:**
```
Time for one frame = 1/60 s = 16,667 µs
Max segments = 16,667 µs / 2 µs per segment = 8,333 segments
```
As long as the display list has ≤ 8,333 segments, the system can refresh at ≥ 60 Hz.

(b) **Refresh rate for 2,000 segments:**
```
Frame time = 2,000 × 2 µs = 4,000 µs
Refresh rate = 1 / 0.004 s = 250 Hz
```
250 Hz >> CFF (46 Hz), so no flicker. The scene is simple enough that the display refreshes far above the flicker threshold. ✓

---

## 5. Previous Year Questions & Solutions

**Q1 [May 2019, Part A, 4 marks]: Compare raster scan and random scan display systems.**

**Solution:**

A **raster scan display** works by sweeping an electron beam (or addressing LCD pixels) row by row across the entire screen area, 60–75 times per second. The image is stored as a matrix of pixel values in a frame buffer. Every pixel is updated every frame, regardless of whether it is part of the image or not. The time cost is therefore **fixed** — proportional only to resolution, not scene complexity. Modern LCD, OLED, and plasma panels are all raster devices.

A **random scan display** (also called a vector display or calligraphic display) stores the picture as a **display list** — a sequence of MOVETO and DRAWTO commands. The electron beam is steered directly to only those positions that form part of the picture, tracing lines without filling the background. Refresh time is **variable** — it grows with scene complexity. Complex scenes (many line segments) cause the refresh rate to drop, leading to visible flicker.

| Property | Raster Scan | Random Scan |
|----------|-------------|-------------|
| Storage | Frame buffer (pixel array) | Display list (vector commands) |
| Line quality | Aliased (jagged diagonal lines) | Perfectly smooth and continuous |
| Solid fill | Easily supported (scan-line fill) | Not supported |
| Scene complexity | Constant refresh rate | Refresh rate degrades with complexity |
| Color support | Full 24-bit color per pixel | Limited (beam intensity only) |
| Applications | LCD, OLED monitors, TVs | Oscilloscopes, laser shows, CAD plotters |

Raster displays dominate modern computing because they easily support photorealistic color, texture, and area fill. Random scan survives only in specialized instruments (oscilloscopes) where infinite resolution of waveforms is required.

---

**Q2 [Dec 2018, Part B, 9 marks]: Explain the different types of input devices used in interactive computer graphics. How does a digitizing tablet differ from a mouse?**

**Solution:**

**Types of Input Devices in Interactive Computer Graphics:**

Interactive graphics systems use the following logical input device classes (following the PHIGS/GKS model):

**1. Locator Device:** Provides a 2D position (x, y) in the world coordinate system. Examples:
- *Mouse:* Detects relative displacement via optical sensor. Reports Δx, Δy movement. Cannot report absolute position.
- *Trackball:* Stationary ball rotated by hand; encoder measures rotation. Good for constrained spaces.
- *Touch screen:* Capacitive or resistive grid senses finger contact position. Provides absolute position.
- *Digitizing tablet:* Electromagnetic grid + stylus detects absolute stylus position. High precision (up to 5080 LPI resolution).

**2. Pick Device:** Used to select displayed objects. Implemented as a bounding-box intersection test — user clicks or points to an area, system checks which display element falls within that area.

**3. Keyboard (String Device):** Enters text strings. In graphics, used for naming objects, entering dimensions, issuing commands.

**4. Valuator Device:** Provides a scalar value. Dials, sliders, and potentiometers used to control parameters like zoom level, rotation angle, opacity.

**5. Stroke Device:** Provides a sequence of (x, y) coordinates, representing a path. Used in gesture recognition, handwriting input, and path tracing.

**Digitizing Tablet vs Mouse:**

| Property | Digitizing Tablet | Mouse |
|----------|-------------------|-------|
| Position reporting | **Absolute** — each stylus position maps to a unique screen coordinate | **Relative** — only reports changes in position (Δx, Δy) |
| Precision | Very high (5080 LPI typical in professional models) | Lower (800–16000 DPI typical) |
| Workspace | Must match tablet to screen mapping; moving stylus off tablet = off screen | Can be lifted and repositioned freely |
| Use case | CAD drafting, digital illustration, GIS point entry | General computing, gaming |
| Input modality | Stylus pressure sensing (wacom tablets sense 8192 pressure levels) | Only x-y displacement + buttons |

The key engineering distinction is **absolute vs. relative positioning**. A digitizing tablet guarantees that moving the stylus to position (X, Y) on the physical tablet always corresponds to the same point on the screen. A mouse only reports movement direction and distance — it has no knowledge of where on the screen the cursor currently is; the OS maintains a cursor state updated by accumulated deltas.
