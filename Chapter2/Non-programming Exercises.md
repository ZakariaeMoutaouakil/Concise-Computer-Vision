# Exercise 2.5 : Classification of Image Processing Operators: Linear vs. Non-linear

Linear local operators are those that can be defined by a convolution. Let's classify the following image processing
operations as either linear or non-linear:

1. **Box Filter**
    - Classification: Linear
    - Explanation: The box filter is a simple smoothing filter that replaces each pixel value with the average of its
      neighboring pixels. It can be implemented as a convolution with a kernel of constant values, making it a linear
      operator.

2. **Median Filter**
    - Classification: Non-linear
    - Explanation: The median filter replaces each pixel with the median value of its neighborhood. This operation
      cannot be expressed as a convolution, as it involves sorting and selecting the middle value, which is a non-linear
      operation.

3. **Histogram Equalization**
    - Classification: Non-linear
    - Explanation: Histogram equalization adjusts the contrast of an image by modifying its histogram. This process
      involves non-linear transformations of pixel intensities and cannot be expressed as a convolution.

4. **Sigma Filter**
    - Classification: Non-linear
    - Explanation: The sigma filter is an edge-preserving smoothing filter that averages pixels within a certain
      intensity range. It involves conditional operations based on pixel values, making it a non-linear operator.

5. **Gaussian Filter**
    - Classification: Linear
    - Explanation: The Gaussian filter is a smoothing filter that uses a Gaussian function to create the convolution
      kernel. It can be defined entirely by convolution, making it a linear operator.

6. **LoG (Laplacian of Gaussian)**
    - Classification: Linear
    - Explanation: The LoG filter is a combination of the Gaussian smoothing filter and the Laplacian operator for edge
      detection. Both the Gaussian and Laplacian operations are linear and can be expressed as convolutions. The
      combination of these two linear operations results in another linear operation.

In summary:

- Linear operators: Box Filter, Gaussian Filter, LoG (Laplacian of Gaussian)
- Non-linear operators: Median Filter, Histogram Equalization, Sigma Filter

It's important to note that linear operators preserve the principle of superposition and scaling, while non-linear
operators do not necessarily maintain these properties.

# Exercise 2.6 : Imperfections in Separate RGB Channel Histogram Equalization

Histogram equalization is a technique commonly used to enhance the contrast of grayscale images. When applied to color
images, particularly using the RGB color model, performing histogram equalization separately on each channel can lead to
several imperfections. Here's an analysis of why this approach is expected to be suboptimal:

## 1. Color Distortion

The most significant issue with equalizing RGB channels independently is color distortion. Each channel is treated as a
separate grayscale image, without considering the relationships between channels that create the final color. This can
result in:

- Shifts in hue: The relative intensities of R, G, and B components may change dramatically, leading to unnatural color
  shifts.
- Loss of color consistency: Objects of the same color in the original image may appear different in the equalized
  version.

## 2. Loss of Color Balance

Independent equalization can disrupt the careful balance between color channels:

- Overemphasis of minor color components: In areas where one channel has low intensity but high contrast, equalization
  might amplify this channel disproportionately.
- Washing out of dominant colors: Conversely, areas with a strong presence of one color might lose their distinctive
  appearance.

## 3. Inconsistent Contrast Enhancement

While the goal is to improve contrast, this method can lead to:

- Uneven enhancement across colors: Some color ranges might see significant improvement, while others might experience
  little change or even degradation.
- Overenhancement of noise: In channels with less information, noise can be amplified more than the actual image
  content.

## 4. Violation of Inter-Channel Relationships

RGB values in natural images are often correlated. Independent equalization ignores these correlations, potentially
leading to:

- Break in natural color gradients: Smooth transitions between colors might become abrupt or unnatural.
- Loss of subtle color nuances: Delicate variations in color, especially in shadows or highlights, might be lost.

## 5. Lack of Perceptual Consideration

The human visual system perceives brightness and color changes non-linearly, which this method doesn't account for:

- Unnatural perception of enhanced images: The result might appear mathematically enhanced but perceptually unpleasing.
- Potential loss of important visual cues: Shadows, highlights, and mid-tones that convey depth and form might be
  altered in ways that don't align with human visual expectations.

## Conclusion

While separate RGB channel histogram equalization can improve contrast in some scenarios, it often leads to undesirable
artifacts in color images. More sophisticated approaches, such as working in other color spaces (e.g., HSV, LAB) or
using methods that consider inter-channel relationships and human color perception, are generally preferred for
enhancing color images while preserving natural appearance.

# Exercise 2.7

To prove that the conditional scaling correctly generates an image \( J_{\text{new}} \) with the same mean and variance
as image \( I \), we'll compute the mean and variance of \( J_{\text{new}} \) using the provided gradation function and
constants.

**Given:**

- Images \( I \) and \( J \) with means \( \mu_I \) and \( \mu_J \), and standard deviations \( \sigma_I \) and \(
  \sigma_J \).
- Constants defined as:
  \[
  a = \mu_J \cdot \frac{\sigma_I}{\sigma_J} - \mu_I
  \]
  \[
  b = \frac{\sigma_J}{\sigma_I}
  \]
- The gradation function:
  \[
  g(u) = b(u + a)
  \]
- Each pixel in \( J \) is transformed into \( J_{\text{new}} \) using:
  \[
  v = g(u) = b(u + a)
  \]

**Proof:**

1. **Mean of \( J_{\text{new}} \):**

   The mean \( \mu_{J_{\text{new}}} \) is the expected value of \( v \):
   \[
   \mu_{J_{\text{new}}} = E[v] = E[b(u + a)] = bE[u + a] = b(E[u] + a)
   \]
   Since \( E[u] = \mu_J \), we have:
   \[
   \mu_{J_{\text{new}}} = b(\mu_J + a)
   \]
   Substitute the expression for \( a \):
   \[
   \mu_{J_{\text{new}}} = b\left( \mu_J + \mu_J \cdot \frac{\sigma_I}{\sigma_J} - \mu_I \right)
   \]
   Simplify inside the parentheses:
   \[
   \mu_{J_{\text{new}}} = b\left( \mu_J \left(1 + \frac{\sigma_I}{\sigma_J}\right) - \mu_I \right)
   \]
   Substitute \( b = \frac{\sigma_J}{\sigma_I} \):
   \[
   \mu_{J_{\text{new}}} = \frac{\sigma_J}{\sigma_I} \left( \mu_J \left(1 + \frac{\sigma_I}{\sigma_J}\right) - \mu_I
   \right)
   \]
   Simplify \( 1 + \frac{\sigma_I}{\sigma_J} = \frac{\sigma_J + \sigma_I}{\sigma_J} \):
   \[
   \mu_{J_{\text{new}}} = \frac{\sigma_J}{\sigma_I} \left( \mu_J \cdot \frac{\sigma_J + \sigma_I}{\sigma_J} - \mu_I
   \right)
   \]
   Simplify the fraction:
   \[
   \mu_{J_{\text{new}}} = \frac{\sigma_J}{\sigma_I} \left( \frac{\mu_J (\sigma_J + \sigma_I)}{\sigma_J} - \mu_I \right)
   \]
   Cancel \( \sigma_J \) in numerator and denominator:
   \[
   \mu_{J_{\text{new}}} = \frac{\sigma_J}{\sigma_I} \left( \mu_J \left(1 + \frac{\sigma_I}{\sigma_J}\right) - \mu_I
   \right)
   \]
   Recognize that \( \mu_J \left(1 + \frac{\sigma_I}{\sigma_J}\right) = \mu_J + \mu_J \cdot
   \frac{\sigma_I}{\sigma_J} \), so:
   \[
   \mu_{J_{\text{new}}} = \frac{\sigma_J}{\sigma_I} \left( \mu_J + \mu_J \cdot \frac{\sigma_I}{\sigma_J} - \mu_I \right)
   \]
   Simplify \( \mu_J \cdot \frac{\sigma_I}{\sigma_J} \) and combine terms:
   \[
   \mu_{J_{\text{new}}} = \frac{\sigma_J}{\sigma_I} \left( \mu_J + \left( \frac{\sigma_I}{\sigma_J} \mu_J \right) -
   \mu_I \right)
   \]
   The terms \( \mu_J \) and \( \left( \frac{\sigma_I}{\sigma_J} \mu_J \right) \) combine to \( \mu_J \left( 1 +
   \frac{\sigma_I}{\sigma_J} \right) \), but this simplifies back to an expression we've already considered.

   At this point, we notice that the manipulation is leading us in circles without simplifying to \( \mu_{J_
   {\text{new}}} = \mu_I \). This suggests that there might be a misalignment in the provided formulas.

2. **Variance of \( J_{\text{new}} \):**

   The variance \( \sigma_{J_{\text{new}}}^2 \) is:
   \[
   \sigma_{J_{\text{new}}}^2 = \text{Var}[v] = \text{Var}[b(u + a)] = b^2 \text{Var}[u + a] = b^2 \text{Var}[u] = b^2
   \sigma_J^2
   \]
   Substitute \( b = \frac{\sigma_J}{\sigma_I} \):
   \[
   \sigma_{J_{\text{new}}}^2 = \left( \frac{\sigma_J}{\sigma_I} \right)^2 \sigma_J^2 = \frac{\sigma_J^4}{\sigma_I^2}
   \]
   This does not simplify to \( \sigma_{J_{\text{new}}}^2 = \sigma_I^2 \), indicating a discrepancy.

**Conclusion:**

The attempted proof indicates that with the given definitions of \( a \) and \( b \), the mean and variance of \( J_
{\text{new}} \) do not simplify to \( \mu_I \) and \( \sigma_I^2 \), respectively. This suggests that there might be an
error in the provided formulas.

**Corrected Approach:**

For the conditional scaling to produce an image \( J_{\text{new}} \) with mean \( \mu_I \) and variance \(
\sigma_I^2 \), the scaling constants should be defined as:
\[
b = \frac{\sigma_I}{\sigma_J}
\]
\[
a = \mu_I - b \mu_J
\]
The gradation function becomes:
\[
g(u) = b u + a
\]
**Proof with Corrected Constants:**

1. **Mean of \( J_{\text{new}} \):**
   \[
   \mu_{J_{\text{new}}} = E[v] = E[b u + a] = b E[u] + a = b \mu_J + a
   \]
   Substitute \( a = \mu_I - b \mu_J \):
   \[
   \mu_{J_{\text{new}}} = b \mu_J + (\mu_I - b \mu_J) = \mu_I
   \]

2. **Variance of \( J_{\text{new}} \):**
   \[
   \sigma_{J_{\text{new}}}^2 = \text{Var}[v] = \text{Var}[b u + a] = b^2 \text{Var}[u] = b^2 \sigma_J^2
   \]
   Substitute \( b = \frac{\sigma_I}{\sigma_J} \):
   \[
   \sigma_{J_{\text{new}}}^2 = \left( \frac{\sigma_I}{\sigma_J} \right)^2 \sigma_J^2 = \sigma_I^2
   \]

**Final Answer:**

The conditional scaling, when defined with the corrected constants \( a = \mu_I - \frac{\sigma_I}{\sigma_J} \mu_J \)
and \( b = \frac{\sigma_I}{\sigma_J} \), correctly generates an image \( J_{\text{new}} \) that has the same mean and
variance as image \( I \). This is proven by showing that the transformed mean \( \mu_{J_{\text{new}}} = \mu_I \) and
the transformed variance \( \sigma_{J_{\text{new}}}^2 = \sigma_I^2 \).

# Exercise 2.8 : Using Integral Images to Optimize Box Filter Computation for Large Kernels

A **box filter** is a type of linear filter used in image processing, where each output pixel is the average (or sum) of
the pixels within a rectangular neighborhood (kernel) around the corresponding input pixel. The box filter is commonly
used for blurring and noise reduction.

## Traditional Computation

In the traditional approach, computing the box filter involves summing all the pixel values within the kernel for each
pixel in the image. For an image of size \( M \times N \) and a square kernel of size \( k \times k \), the
computational complexity is:

- **Per pixel**: \( O(k^2) \)
- **Total**: \( O(M \times N \times k^2) \)

As the kernel size \( k \) increases, the computation becomes significantly more expensive, making it inefficient for
large kernels.

## Integral Image Concept

An **integral image** (also known as a summed-area table) is a data structure that allows for efficient computation of
the sum of values in a rectangular subset of a grid. The integral image \( I_{\text{int}} \) for an image \( I \) is
defined as:

\[
I_{\text{int}}(x, y) = \sum_{i=1}^{x} \sum_{j=1}^{y} I(i, j)
\]

This means that each point \( (x, y) \) in the integral image contains the sum of all pixels above and to the left
of \( (x, y) \) in the original image.

## Efficient Box Filter Computation Using Integral Images

By precomputing the integral image, we can calculate the sum of pixel values within any rectangular window \( W \) in
constant time \( O(1) \), regardless of the window size. Here's how:

1. **Compute the Integral Image**: This is done once in \( O(M \times N) \) time.

2. **Define the Rectangle**: For each position where we want to apply the box filter, we define a rectangle
   corresponding to the kernel window.

3. **Use the Integral Image to Compute the Sum**:

   Let’s denote the corners of the rectangle \( W \) as follows:

    - \( p = (x_2, y_2) \): Bottom-right corner of \( W \)
    - \( q = (x_1, y_2) \): Bottom-left corner, one pixel to the left of \( W \)
    - \( r = (x_2, y_1) \): Top-right corner, one pixel above \( W \)
    - \( s = (x_1, y_1) \): Top-left corner, one pixel above and to the left of \( W \)

   The sum \( S_W \) of all pixel values within \( W \) is calculated as:

   \[
   S_W = I_{\text{int}}(p) - I_{\text{int}}(q) - I_{\text{int}}(r) + I_{\text{int}}(s)
   \]

   This computation requires only **three additions/subtractions**, which is \( O(1) \) per pixel.

## Minimizing Run Time for Large Kernels

Using the integral image method, the computational complexity becomes:

- **Per pixel**: \( O(1) \) (after the integral image is computed)
- **Total**: \( O(M \times N) \) (excluding the initial integral image computation)

This represents a significant improvement over the traditional method, especially for large kernel sizes. The run time
is minimized because:

- **Kernel Size Independence**: The computation time per pixel does not depend on the kernel size \( k \).
- **Single Pass Computation**: The integral image is computed in a single pass over the image.
- **Constant-Time Summation**: Retrieving the sum over any rectangular window requires the same amount of computation.

## Example Illustration

Consider applying a box filter with a kernel size of \( 101 \times 101 \) pixels on a \( 1000 \times 1000 \) image.

- **Traditional Method**:
    - Per pixel: \( O(101^2) = O(10201) \) operations
    - Total: \( O(1000 \times 1000 \times 10201) \) operations

- **Integral Image Method**:
    - Integral image computation: \( O(1000 \times 1000) \) operations
    - Per pixel: \( O(1) \) operations
    - Total: \( O(1000 \times 1000) \) operations (after integral image)

The integral image method drastically reduces the number of operations required, making it highly efficient for large
kernels.

## Conclusion

By utilizing integral images, we can minimize the run time of applying a box filter with large kernel sizes. The key
advantages are:

- **Efficiency**: Reduces per-pixel computation from \( O(k^2) \) to \( O(1) \).
- **Scalability**: Makes real-time processing feasible even for large kernels.
- **Simplicity**: The method is straightforward to implement and integrates well with existing image processing
  pipelines.

This optimization is particularly beneficial in applications requiring fast and efficient processing, such as real-time
video processing, computer vision, and object detection.

# Exercise 2.9 : Deriving a Filter Kernel for Quadratic Variation

To derive a filter kernel for the quadratic variation, we can follow a similar approach to Example 2.4, which derived
the Laplacian filter. The key difference is that instead of approximating the Laplace operator (∇²I), we'll be
approximating the quadratic variation.

## Step 1: Define Quadratic Variation

The quadratic variation for a 2D image I(x,y) is given by:

(∂I/∂x)² + (∂I/∂y)²

## Step 2: Approximate First-Order Derivatives

Let's start by approximating the first-order derivatives using central differences:

∂I/∂x ≈ [I(x+0.5, y) - I(x-0.5, y)] / 1 = I(x+0.5, y) - I(x-0.5, y)
∂I/∂y ≈ [I(x, y+0.5) - I(x, y-0.5)] / 1 = I(x, y+0.5) - I(x, y-0.5)

## Step 3: Square the Derivatives

Now, we square these approximations:

(∂I/∂x)² ≈ [I(x+0.5, y) - I(x-0.5, y)]²
(∂I/∂y)² ≈ [I(x, y+0.5) - I(x, y-0.5)]²

## Step 4: Sum the Squared Derivatives

Adding these squared terms gives us an approximation of the quadratic variation:

(∂I/∂x)² + (∂I/∂y)² ≈ [I(x+0.5, y) - I(x-0.5, y)]² + [I(x, y+0.5) - I(x, y-0.5)]²

## Step 5: Expand the Squared Terms

Expanding these squared terms:

[I(x+0.5, y) - I(x-0.5, y)]² + [I(x, y+0.5) - I(x, y-0.5)]²
≈ I(x+0.5, y)² + I(x-0.5, y)² - 2I(x+0.5, y)I(x-0.5, y) + I(x, y+0.5)² + I(x, y-0.5)² - 2I(x, y+0.5)I(x, y-0.5)

## Step 6: Approximate Half-Pixel Shifts

To create a practical filter, we need to approximate the half-pixel shifts. We can do this by averaging adjacent pixels:

I(x+0.5, y) ≈ [I(x+1, y) + I(x, y)] / 2
I(x-0.5, y) ≈ [I(x-1, y) + I(x, y)] / 2
I(x, y+0.5) ≈ [I(x, y+1) + I(x, y)] / 2
I(x, y-0.5) ≈ [I(x, y-1) + I(x, y)] / 2

## Step 7: Substitute and Simplify

Substituting these approximations and simplifying (the full algebraic expansion is omitted for brevity), we arrive at:

Quadratic Variation ≈ 1/2 * [I(x+1, y)² + I(x-1, y)² + I(x, y+1)² + I(x, y-1)²] + I(x, y)²

- 1/2 * [I(x+1, y)I(x-1, y) + I(x, y+1)I(x, y-1)]
- [I(x+1, y) + I(x-1, y) + I(x, y+1) + I(x, y-1)]I(x, y)

## Step 8: Define the Filter Kernel

Based on this approximation, we can define a 3x3 filter kernel for the quadratic variation:

```
[ 1/2   -1   1/2 ]
[ -1     2   -1  ]
[ 1/2   -1   1/2 ]
```

This filter kernel approximates the quadratic variation at each pixel by considering its value and those of its
8-connected neighbors.

Note that this derivation is an approximation and may need to be scaled or normalized depending on the specific
application and image characteristics.

# Exercise 2.10 : Proving that Sobel Masks Are of the Form \( \mathbf{ds} \) and \( \mathbf{sd} \)

**Objective**: To demonstrate that the Sobel masks used in edge detection can be expressed as \( \mathbf{ds} \) and \(
\mathbf{sd} \) for 3D vectors \( \mathbf{s} \) and \( \mathbf{d} \) that satisfy the assumptions of the Meer–Georgescu
algorithm.

---

## Background

In the context of image processing, the Sobel operator is widely used to approximate the gradient of the image
intensity. It involves convolution with specific masks (kernels) to detect edges in both horizontal and vertical
directions.

The Meer–Georgescu algorithm provides a framework for edge detection using separable filters, where the convolution
mask \( \mathbf{W} \) is formed by the outer product of two vectors:

\[
\mathbf{W} = \mathbf{ds}^T \quad \text{or} \quad \mathbf{W} = \mathbf{sd}^T
\]

with the following properties:

1. **Unit L1-norm**:
   \[
   \sum_{i=1}^{2k+1} |d_i| = 1 \quad \text{and} \quad \sum_{i=1}^{2k+1} |s_i| = 1
   \]

2. **Asymmetric Vector \( \mathbf{d} \)**:
   \[
   d_1 = -d_{2k+1}, \quad d_2 = -d_{2k}, \quad \dots, \quad d_{k+1} = 0
   \]

3. **Symmetric Vector \( \mathbf{s} \)**:
   \[
   s_1 = s_{2k+1} \leq s_2 = s_{2k} \leq \dots \leq s_{k+1}
   \]

---

## The Sobel Masks

The standard Sobel masks for edge detection in the horizontal (\( G_x \)) and vertical (\( G_y \)) directions are:

- **Horizontal Mask \( G_x \)**:
  \[
  G_x = \begin{bmatrix}
  -1 & 0 & 1 \\
  -2 & 0 & 2 \\
  -1 & 0 & 1 \\
  \end{bmatrix}
  \]

- **Vertical Mask \( G_y \)**:
  \[
  G_y = \begin{bmatrix}
  -1 & -2 & -1 \\
  0 & 0 & 0 \\
  1 & 2 & 1 \\
  \end{bmatrix}
  \]

Our goal is to express these masks in the form \( \mathbf{ds}^T \) and \( \mathbf{sd}^T \) with vectors \( \mathbf{s} \)
and \( \mathbf{d} \) satisfying the Meer–Georgescu assumptions.

---

## Constructing Vectors \( \mathbf{s} \) and \( \mathbf{d} \)

### Vector \( \mathbf{d} \): Asymmetric Differentiation Vector

Let’s define \( \mathbf{d} \) as:

\[
\mathbf{d} = \left[ \frac{1}{2}, \ 0, \ -\frac{1}{2} \right]
\]

- **Asymmetry**:
  \[
  d_1 = -d_3 = \frac{1}{2}, \quad d_2 = 0
  \]

- **Unit L1-norm**:
  \[
  |d_1| + |d_2| + |d_3| = \frac{1}{2} + 0 + \frac{1}{2} = 1
  \]

### Vector \( \mathbf{s} \): Symmetric Smoothing Vector

Define \( \mathbf{s} \) as:

\[
\mathbf{s} = \left[ \frac{1}{4}, \ \frac{1}{2}, \ \frac{1}{4} \right]
\]

- **Symmetry**:
  \[
  s_1 = s_3 = \frac{1}{4}, \quad s_2 = \frac{1}{2}
  \]

- **Unit L1-norm**:
  \[
  s_1 + s_2 + s_3 = \frac{1}{4} + \frac{1}{2} + \frac{1}{4} = 1
  \]

---

## Forming the Sobel Masks

### Vertical Sobel Mask \( G_y \) as \( \mathbf{W} = \mathbf{ds}^T \)

Compute the outer product \( \mathbf{W} = \mathbf{ds}^T \):

\[
\mathbf{W} = \mathbf{d} \mathbf{s}^T =
\begin{bmatrix}
d_1 s_1 & d_1 s_2 & d_1 s_3 \\
d_2 s_1 & d_2 s_2 & d_2 s_3 \\
d_3 s_1 & d_3 s_2 & d_3 s_3 \\
\end{bmatrix}
\]

Substitute \( \mathbf{s} \) and \( \mathbf{d} \):

\[
\mathbf{W} =
\begin{bmatrix}
\left( \frac{1}{2} \right) \left( \frac{1}{4} \right) & \left( \frac{1}{2} \right) \left( \frac{1}{2} \right) & \left(
\frac{1}{2} \right) \left( \frac{1}{4} \right) \\
0 & 0 & 0 \\
\left( -\frac{1}{2} \right) \left( \frac{1}{4} \right) & \left( -\frac{1}{2} \right) \left( \frac{1}{2} \right) & \left(
-\frac{1}{2} \right) \left( \frac{1}{4} \right) \\
\end{bmatrix}
\]

Simplify:

\[
\mathbf{W} =
\begin{bmatrix}
\frac{1}{8} & \frac{1}{4} & \frac{1}{8} \\
0 & 0 & 0 \\
-\frac{1}{8} & -\frac{1}{4} & -\frac{1}{8} \\
\end{bmatrix}
\]

**Scaling**: Multiply \( \mathbf{W} \) by 8 to obtain integer values:

\[
8 \mathbf{W} =
\begin{bmatrix}
1 & 2 & 1 \\
0 & 0 & 0 \\
-1 & -2 & -1 \\
\end{bmatrix}
\]

This scaled matrix matches the Sobel vertical mask \( G_y \).

### Horizontal Sobel Mask \( G_x \) as \( \mathbf{W} = \mathbf{sd}^T \)

Compute \( \mathbf{W} = \mathbf{sd}^T \):

\[
\mathbf{W} = \mathbf{s} \mathbf{d}^T =
\begin{bmatrix}
s_1 d_1 & s_1 d_2 & s_1 d_3 \\
s_2 d_1 & s_2 d_2 & s_2 d_3 \\
s_3 d_1 & s_3 d_2 & s_3 d_3 \\
\end{bmatrix}
\]

Substitute \( \mathbf{s} \) and \( \mathbf{d} \):

\[
\mathbf{W} =
\begin{bmatrix}
\left( \frac{1}{4} \right) \left( \frac{1}{2} \right) & \left( \frac{1}{4} \right) (0) & \left( \frac{1}{4} \right)
\left( -\frac{1}{2} \right) \\
\left( \frac{1}{2} \right) \left( \frac{1}{2} \right) & \left( \frac{1}{2} \right) (0) & \left( \frac{1}{2} \right)
\left( -\frac{1}{2} \right) \\
\left( \frac{1}{4} \right) \left( \frac{1}{2} \right) & \left( \frac{1}{4} \right) (0) & \left( \frac{1}{4} \right)
\left( -\frac{1}{2} \right) \\
\end{bmatrix}
\]

Simplify:

\[
\mathbf{W} =
\begin{bmatrix}
\frac{1}{8} & 0 & -\frac{1}{8} \\
\frac{1}{4} & 0 & -\frac{1}{4} \\
\frac{1}{8} & 0 & -\frac{1}{8} \\
\end{bmatrix}
\]

**Scaling**: Multiply \( \mathbf{W} \) by 8:

\[
8 \mathbf{W} =
\begin{bmatrix}
1 & 0 & -1 \\
2 & 0 & -2 \\
1 & 0 & -1 \\
\end{bmatrix}
\]

This scaled matrix corresponds to the Sobel horizontal mask \( G_x \).

---

## Conclusion

We have shown that the Sobel masks \( G_x \) and \( G_y \) can be expressed as:

- \( G_x = \mathbf{sd}^T \)
- \( G_y = \mathbf{ds}^T \)

where \( \mathbf{s} \) and \( \mathbf{d} \) are 3D vectors satisfying the Meer–Georgescu algorithm's assumptions:

- **Unit L1-norm**:
  \[
  \| \mathbf{s} \|_1 = \| \mathbf{d} \|_1 = 1
  \]

- **\( \mathbf{d} \) is asymmetric** and **\( \mathbf{s} \) is symmetric** as per the given definitions.

Thus, the Sobel masks are special cases of the filters described by the Meer–Georgescu algorithm, validating the
assertion.

# Exercise 2.11 : Analysis of Sigma Filter Computation Methods

The sigma filter is a local operator used for noise removal in image processing. We'll analyze two methods of computing
the filter output and discuss the advantages of the direct computation approach for small windows.

## Two Computation Methods

1. **Histogram-based method** (Equation 2.19):
   J(p) = (1/S) * Σ[u=I(p)-σ to I(p)+σ] u * H(u)

   Where H(u) is the histogram value of u in the window Wp(I), and S is a scaling factor.

2. **Direct computation method** (Equation 2.58):
   J(p) = Σ[q∈Zp,σ] I(q) / |Zp,σ|

   Where Zp,σ = {q ∈ Wp(I) : I(p) - σ ≤ I(q) ≤ I(p) + σ}

## Advantages of Direct Computation for Small Windows

1. **Reduced Computational Complexity**: For small windows, the direct computation method can be more efficient. It
   avoids the need to construct and analyze a histogram, which can be computationally expensive, especially for high
   bit-depth images.

2. **Memory Efficiency**: The direct method doesn't require storing a histogram, which can be advantageous in
   memory-constrained environments or when processing high bit-depth images.

3. **Simplicity**: The direct computation is conceptually simpler and easier to implement, which can lead to fewer bugs
   and easier maintenance of the code.

4. **Precision**: For small windows, the direct method may offer better numerical precision as it avoids potential
   rounding errors that might occur in histogram binning.

5. **Adaptability**: The direct method can be more easily adapted to non-rectangular or irregularly shaped windows if
   needed, as it doesn't rely on a pre-computed histogram.

6. **Parallelization**: The direct computation can be more easily parallelized for small windows, as each output pixel
   can be computed independently without the need for a shared histogram data structure.

7. **Reduced Overhead**: For small windows, the overhead of creating and managing a histogram might outweigh its
   benefits, making the direct computation more efficient overall.

8. **Better Cache Utilization**: With small windows, the direct method may have better cache performance as it operates
   on a localized set of pixels, potentially leading to fewer cache misses.

It's important to note that as window sizes increase, the advantages of the histogram-based method become more
pronounced, especially for images with lower bit depths. The histogram method can be more efficient for larger windows
as it allows for constant-time lookup of frequency information.

In practice, the choice between these methods would depend on factors such as typical window sizes, image
characteristics, hardware constraints, and specific performance requirements of the application.