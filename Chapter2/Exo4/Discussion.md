# Relationship Between Recursively Repeated Box Filters and Gaussian Filters

## Introduction

In image processing, smoothing filters are essential tools for noise reduction and image enhancement. Two commonly used
filters are the **box filter** and the **Gaussian filter**. While the box filter is simple and computationally
efficient, the Gaussian filter provides smoother results due to its weighting scheme. Interestingly, applying a box
filter recursively can approximate the effect of a Gaussian filter. This document discusses the general relationship
between recursively repeated box filters and Gaussian filters, and determines the corresponding radius.

## Box Filter vs. Gaussian Filter

### Box Filter

A **box filter** of size \( n \times n \) replaces each pixel value with the average of its neighboring pixels within
the kernel. The kernel for a 3×3 box filter is:

\[
H_{\text{box}} = \frac{1}{9}
\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1 \\
\end{bmatrix}
\]

### Gaussian Filter

A **Gaussian filter** applies weights to neighboring pixels according to the Gaussian (normal) distribution, giving more
emphasis to pixels closer to the center of the kernel. The Gaussian function in two dimensions is:

\[
G(x, y) = \frac{1}{2\pi \sigma^2} e^{ -\frac{x^2 + y^2}{2\sigma^2} }
\]

where \( \sigma \) is the standard deviation, controlling the spread (radius) of the Gaussian.

## Relationship Through Convolution

### Convolution and Recursion

Applying a filter to an image is a convolution operation. When a filter is applied recursively, the overall effect is
equivalent to convolving the filter with itself multiple times:

\[
H_{\text{effective}} = H \ast H \ast \cdots \ast H \quad (n \text{ times})
\]

### Central Limit Theorem (CLT)

The **Central Limit Theorem** states that the sum (or average) of a large number of independent, identically distributed
random variables tends toward a Gaussian distribution, regardless of the original distribution.

- **Implication**: Repeatedly applying a box filter (which averages pixel values) causes the overall filter to
  approximate a Gaussian distribution.

## Corresponding Radius

### Deriving the Relationship

For a one-dimensional case, convolving a box filter of width \( w \) with itself \( n \) times results in a filter
resembling a binomial distribution, which approaches a Gaussian distribution as \( n \) increases.

- **Variance of Box Filter**: The variance \( \sigma_{\text{box}}^2 \) of a single box filter of width \( w \) is:

  \[
  \sigma_{\text{box}}^2 = \frac{w^2 - 1}{12}
  \]

- **Variance After \( n \) Applications**:

  \[
  \sigma_{\text{total}}^2 = n \times \sigma_{\text{box}}^2 = n \times \frac{w^2 - 1}{12}
  \]

### Calculating the Corresponding Radius

For a 3×3 box filter (\( w = 3 \)) applied recursively \( n \) times:

\[
\sigma_{\text{total}}^2 = n \times \frac{3^2 - 1}{12} = n \times \frac{8}{12} = n \times \frac{2}{3}
\]

- **Standard Deviation**:

  \[
  \sigma_{\text{total}} = \sqrt{ \sigma_{\text{total}}^2 } = \sqrt{ \frac{2n}{3} }
  \]

- **Corresponding Radius**: The standard deviation \( \sigma_{\text{total}} \) acts as the radius of the equivalent
  Gaussian filter.

### Summary Formula

The corresponding radius \( r \) of the Gaussian filter after applying a 3×3 box filter \( n \) times is:

\[
r = \sigma = \sqrt{ \frac{2n}{3} }
\]

## Practical Examples

### Example 1: \( n = 1 \)

- **Radius**:

  \[
  r = \sqrt{ \frac{2 \times 1}{3} } \approx 0.816
  \]

### Example 2: \( n = 9 \)

- **Radius**:

  \[
  r = \sqrt{ \frac{2 \times 9}{3} } = \sqrt{6} \approx 2.45
  \]

### Example 3: \( n = 30 \)

- **Radius**:

  \[
  r = \sqrt{ \frac{2 \times 30}{3} } = \sqrt{20} \approx 4.47
  \]

## Implications in Image Processing

- **Approximating Gaussian Blur**: By applying a 3×3 box filter multiple times, one can approximate a Gaussian blur with
  a specific radius without directly computing the Gaussian kernel.

- **Computational Efficiency**: Box filters are computationally less intensive than Gaussian filters. Recursive
  application leverages this efficiency while achieving similar results.

- **Control Over Blur**: Adjusting the number of iterations \( n \) allows fine-tuning of the blur radius.

## Conclusion

The general relationship between recursively applied box filters and Gaussian filters is established through the
convergence of the box filter convolution towards a Gaussian distribution, as explained by the Central Limit Theorem.
The corresponding radius (standard deviation) of the equivalent Gaussian filter after \( n \) applications of a 3×3 box
filter is:

\[
r = \sigma = \sqrt{ \frac{2n}{3} }
\]

This relationship enables practitioners to approximate Gaussian smoothing using simple box filters, balancing
computational efficiency and desired image processing outcomes.

## References

- **Digital Image Processing** by Rafael C. Gonzalez and Richard E. Woods
- **The Central Limit Theorem in Image Processing**: Understanding the convergence of repeated averaging filters to
  Gaussian filters.
- **Signal Processing**: Fundamentals of convolution and filter design.