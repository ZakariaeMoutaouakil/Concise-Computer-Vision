# Data Measures for Analyzing Image Sequences

## Definitions

We define three different data measures Di(t), i = 1, 2, 3, for analyzing image sequences:

1. **D1(t): Temporal Gradient Magnitude**
   ```
   D1(t) = ||∇I(x,y,t)||₂
   ```
   Where ∇I(x,y,t) is the temporal gradient of the image intensity at position (x,y) and time t, and ||·||₂ denotes the L2 norm.

2. **D2(t): Structural Similarity Index (SSIM)**
   ```
   D2(t) = SSIM(I(t), I(t-1))
   ```
   Where SSIM is the structural similarity index between consecutive frames I(t) and I(t-1).

3. **D3(t): Optical Flow Magnitude**
   ```
   D3(t) = ||u(x,y,t)||₂
   ```
   Where u(x,y,t) is the optical flow vector at position (x,y) and time t.

## Structural Similarities

The structural similarities between these measures depend on the chosen input sequence of images:

### 1. Static Scenes

For a sequence of images with little to no motion:
- D1(t) will be close to zero, as there's minimal change between frames.
- D2(t) will be close to 1, indicating high similarity between consecutive frames.
- D3(t) will be close to zero, as there's minimal motion.

In this case, D1(t) and D3(t) show structural similarity in their near-zero values, while D2(t) differs by being close to its maximum value.

### 2. Scenes with Uniform Motion

For sequences with consistent, smooth motion:
- D1(t) will show consistent, non-zero values.
- D2(t) will show values less than 1 but relatively consistent across frames.
- D3(t) will show consistent, non-zero values.

Here, all three measures show structural similarity in their consistency, but D2(t) differs in its inverse relationship to motion (decreasing with more motion).

### 3. Scenes with Abrupt Changes

For sequences with sudden scene changes or rapid motion:
- D1(t) will show spikes at points of abrupt change.
- D2(t) will show sudden drops at points of abrupt change.
- D3(t) may show spikes or become unreliable due to the difficulty in calculating optical flow for large displacements.

In this scenario, D1(t) and D2(t) show structural similarity in their ability to detect abrupt changes, albeit with inverse relationships. D3(t) may or may not align with the others depending on the nature of the changes.

### 4. Textured vs. Uniform Regions

- D1(t) and D3(t) will be more sensitive to motion in highly textured regions.
- D2(t) may be less affected by texture and more sensitive to overall structural changes.

This demonstrates a structural difference between D2(t) and the other two measures in their sensitivity to image texture.

### 5. Illumination Changes

- D1(t) will be sensitive to both motion and illumination changes.
- D2(t) is designed to be somewhat robust to illumination changes.
- D3(t) can be affected by illumination changes but is generally more robust than D1(t).

Here, we see structural differences in how each measure responds to non-motion related changes in the image sequence.

## Conclusion

The structural similarities between these measures vary significantly depending on the nature of the input image sequence. D1(t) and D3(t) often show similar behavior, especially in scenes with consistent motion, while D2(t) frequently provides complementary information. The choice of measure(s) should depend on the specific characteristics of the image sequence and the goals of the analysis.