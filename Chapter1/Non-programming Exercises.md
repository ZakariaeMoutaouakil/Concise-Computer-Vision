# Exercise 1.5

See [Derivation of Computational Forumla for the Variance](https://psychology.emory.edu/clinical/mcdowell/PSYCH560/Basics/var.html).

# Exercise 1.6

## Who was Fourier?

Joseph Fourier (1768-1830) was a French mathematician and physicist. He is best known for initiating the investigation
of Fourier series and their application to problems of heat transfer and vibrations. His work laid the foundation for
what would later become known as the Fourier transform.

## When was the Fast Fourier Transform (FFT) designed for the first time?

The Fast Fourier Transform (FFT) was first published in 1965 by James Cooley and John Tukey. However, it's worth noting
that similar algorithms had been independently discovered earlier:

- Carl Friedrich Gauss described a similar algorithm in 1805, but it remained unpublished until 1866.
- Some versions were developed in the 1950s by scientists working on defense projects.

Cooley and Tukey's 1965 paper is considered the breakthrough that brought FFT into widespread use due to its efficiency
and applicability to digital computers.

## How is the Fourier transform related to optical lens systems?

The Fourier transform has significant applications in optics and lens systems:

1. **Spatial frequency analysis**: The Fourier transform can decompose an image into its spatial frequency components,
   which is crucial for understanding image formation in optical systems.

2. **Optical transfer function**: The Fourier transform of a lens's point spread function gives its optical transfer
   function, which describes how different spatial frequencies are transmitted through the optical system.

3. **Diffraction patterns**: The far-field diffraction pattern of an aperture is essentially the Fourier transform of
   the aperture's shape.

4. **Image processing**: In digital image processing, which often mimics optical processes, the Fourier transform is
   used for filtering, compression, and analysis.

5. **Holography**: The process of recording and reconstructing holograms can be described mathematically using Fourier
   transforms.

In essence, the Fourier transform provides a mathematical framework for understanding how lenses manipulate the spatial
frequency content of images, making it an indispensable tool in optical system design and analysis.

# Exercise 1.7

### Step 1: Multiply $I(x, y)$ by $(-1)^{x+y}$

Let $I'(x, y)$ be the modified image:

$$
I'(x, y) = I(x, y) \cdot (-1)^{x+y}
$$

### Step 2: Express $(-1)^{x+y}$ Using Exponentials

Recognize that:

$$
(-1)^{x+y} = e^{i\pi(x + y)}
$$

### Step 3: Compute the DFT of $I'(x, y)$

Substitute $I'(x, y)$ into the DFT formula:

$$
\begin{align*}
I'(u, v) &= \frac{1}{N^2} \sum_{x=0}^{N-1} \sum_{y=0}^{N-1} I'(x, y) \cdot e^{-i 2\pi \left( \frac{xu}{N} + \frac{yv}{N} \right)} \\
&= \frac{1}{N^2} \sum_{x=0}^{N-1} \sum_{y=0}^{N-1} I(x, y) \cdot e^{i\pi(x + y)} \cdot e^{-i 2\pi \left( \frac{xu}{N} + \frac{yv}{N} \right)}
\end{align*}
$$

### Step 4: Combine Exponential Terms

Combine the exponentials:

$$
\begin{align*}
e^{i\pi(x + y)} \cdot e^{-i 2\pi \left( \frac{xu}{N} + \frac{yv}{N} \right)} &= e^{-i 2\pi \left( \frac{xu}{N} + \frac{yv}{N} \right) + i\pi x + i\pi y} \\
&= e^{-i 2\pi \left( \frac{xu}{N} + \frac{yv}{N} \right) + i 2\pi \left( \frac{x}{2} + \frac{y}{2} \right)} \\
&= e^{-i 2\pi \left( \frac{xu}{N} - \frac{x}{2} + \frac{yv}{N} - \frac{y}{2} \right)}
\end{align*}
$$

### Step 5: Simplify the Expression

Simplify the exponent:

$$
\begin{align*}
&-i 2\pi \left( \frac{xu}{N} - \frac{x}{2} + \frac{yv}{N} - \frac{y}{2} \right) \\
&= -i 2\pi \left( x \left( \frac{u}{N} - \frac{1}{2} \right) + y \left( \frac{v}{N} - \frac{1}{2} \right) \right)
\end{align*}
$$

### Step 6: Recognize Frequency Shift Terms

Define shifted frequency variables:

$$
\begin{align*}
u' &= \left( u - \frac{N}{2} \right) \mod N \\
v' &= \left( v - \frac{N}{2} \right) \mod N
\end{align*}
$$

So:

$$
\frac{u}{N} - \frac{1}{2} = \frac{u - \frac{N}{2}}{N} = \frac{u'}{N}
$$

Similarly for $v$:

$$
\frac{v}{N} - \frac{1}{2} = \frac{v'}{N}
$$

### Step 7: Rewrite the DFT Expression

The DFT becomes:

$$
I'(u, v) = \frac{1}{N^2} \sum_{x=0}^{N-1} \sum_{y=0}^{N-1} I(x, y) \cdot e^{-i 2\pi \left( x \cdot \frac{u'}{N} + y \cdot \frac{v'}{N} \right)}
$$

### Step 8: Recognize the Shifted DFT

This expression is the DFT of $I(x, y)$ evaluated at shifted frequencies $(u', v')$:

$$
I'(u, v) = I\left( u', v' \right)
$$

Which simplifies to:

$$
I'(u, v) = I\left( (u - \frac{N}{2}) \mod N, \, (v - \frac{N}{2}) \mod N \right)
$$

# Exercise 1.8

### RGB to HSI Transformation Examples

#### Example 1: Yellow (255, 255, 0)

**Normalized RGB:**

- **R:** 1
- **G:** 1
- **B:** 0

**Intensity (I):**

- I = (1 + 1 + 0) / 3 ≈ 0.67

**Saturation (S):**

- S = 1 - min(1, 1, 0) / 0.67 = 1

**Hue (H):**

- For hue, calculate θ from the cosine formula for normalized colors. Here, θ = 60° because B ≤ G.
- H = θ = 60°

#### Example 2: Magenta (255, 0, 255)

**Normalized RGB:**

- **R:** 1
- **G:** 0
- **B:** 1

**Intensity (I):**

- I = (1 + 0 + 1) / 3 ≈ 0.67

**Saturation (S):**

- S = 1 - min(1, 0, 1) / 0.67 = 1

**Hue (H):**

- Compute θ = 60° (using cosine formula)
- Since B > G, H = 360° - θ = 300°

#### Example 3: Cyan (0, 255, 255)

**Normalized RGB:**

- **R:** 0
- **G:** 1
- **B:** 1

**Intensity (I):**

- I = (0 + 1 + 1) / 3 ≈ 0.67

**Saturation (S):**

- S = 1 - min(0, 1, 1) / 0.67 = 1

**Hue (H):**

- Compute θ = 180° (using cosine formula for hue)
- H = θ = 180°

# Exercise 1.9

## Understanding Hue (H)

In the HSI space, Hue (H) represents the color type and is modeled as an angle:

- **δ = 0 to 2π/3**: Corresponds to colors between red and green through yellow, with red starting at 0 and green at
  2π/3.
- **δ = 2π/3 to 4π/3**: Spans green to blue through cyan, with blue at 4π/3.
- **δ = 4π/3 to 2π**: Covers blue back to red through magenta.

## Saturation (S) and Intensity (M)

- **Saturation (S)** measures the vibrancy of the color. High saturation means a vivid color, while low saturation (near
  zero) means the color is nearing a grayscale equivalent.
- **Intensity (M)** represents the brightness of the color.

## Special Cases and RGB Recovery

### 1. If δ ∈ [0, 2π/3]

- **Blue (B) = (1 - S)M**: In this range, the blue component is the least dominant, so it is influenced directly by the
  saturation and intensity.
- **Computing R and G**:
    - You can compute the other two components (R and G) using the trigonometric relations in the definition of δ. In
      this range, you can use the formulas:
      ```
      R = M + 2√(M² - 3B²)
      G = 3M - (R + B)
      ```

### 2. If δ ∈ [2π/3, 4π/3]

- **Red (R) = (1 - S)M**: Here, the red component is the least dominant. This is because, within this hue range, we are
  transitioning from green to blue.
- **Computing B and G**:
    - Similar trigonometric relations can be applied here:
      ```
      G = M + 2√(M² - 3R²)
      B = 3M - (R + G)
      ```

### 3. If δ ∈ [4π/3, 2π]

- **Green (G) = (1 - S)M**: In this segment, green is the least dominant component.
- **Computing R and B**:
    - Using the position in the hue circle:
      ```
      B = M + 2√(M² - 3G²)
      R = 3M - (G + B)
      ```

# Exercise 1.10

### Overview of the HSI Model

In the HSI color space:

- **Intensity (I or M)**: Represents the brightness of the color, calculated as the average of the RGB components.

  \[
  I = M = \frac{R + G + B}{3}
  \]

- **Saturation (S)**: Measures the purity of the color, indicating how much white light is mixed with the hue. Defined
  as:

  \[
  S = 1 - \frac{3 \cdot \min\{R, G, B\}}{R + G + B}
  \]

### Deriving the Formula \( B = (1 - S)M \)

#### Step 1: Express \( \min\{R, G, B\} \) in Terms of \( S \) and \( M \)

From the saturation formula:

\[
S = 1 - \frac{3 \cdot \min\{R, G, B\}}{3M} = 1 - \frac{\min\{R, G, B\}}{M}
\]

Rearranging for \( \min\{R, G, B\} \):

\[
\min\{R, G, B\} = M(1 - S)
\]

#### Step 2: Identifying the Minimal Component Based on \( \delta \)

In the HSI model, the hue angle \( \delta \) determines which RGB component is minimal:

- **For \( \delta \in [0, \frac{2\pi}{3}] \)**: The **Blue (B)** component is minimal.
- **For \( \delta \in [\frac{2\pi}{3}, \frac{4\pi}{3}] \)**: The **Red (R)** component is minimal.
- **For \( \delta \in [\frac{4\pi}{3}, 2\pi] \)**: The **Green (G)** component is minimal.

#### Step 3: Applying to the Specific Case \( \delta \in [0, \frac{2\pi}{3}] \)

Since \( \delta \in [0, \frac{2\pi}{3}] \), the minimal component is \( B \). Therefore:

\[
B = \min\{R, G, B\} = M(1 - S)
\]

This directly gives us the formula:

\[
B = (1 - S)M
\]

## Physical Interpretation of Negative RGB Values in CIE RGB Color Space

In the CIE RGB color space, negative values for the R, G, or B components arise due to the limitations of the chosen
primary colors in spanning the entire range of human color perception. These values indicate a requirement for a
hypothetical addition of light to achieve a color match, since physically subtracting light from a spectrum is not
possible.

### Why Negative Values?

- **Colors Outside the Gamut:** Negative values suggest that the color to be matched is **outside the color gamut**
  defined by the RGB primaries. The primaries cannot reproduce these colors using only positive quantities.

- **Adding Light to the Test Source:** To match the test color perceptually, it may be necessary to **add light of a
  primary color to the test source**. This addition is represented mathematically as a negative value for that primary
  in the color matching process.

- **Quantifying Mismatch:** The magnitude of a negative value quantifies how much of a primary color would need to be
  added to the test light to bring the color within the reproducible gamut of the RGB system.

### Why Can't We Subtract Light?

- **Physical Limitations:** In real-world applications, subtracting light from a spectrum is not feasible; we can only
  add light.

- **Mathematical Convenience:** Negative values are used as a mathematical tool to represent and manage colors that fall
  outside the RGB gamut within a linear algebra framework.


