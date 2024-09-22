# Question 1

In general, the image contributing the phase tends to be more dominant in the final result.
The phase information carries more structural and edge information, which is crucial for human perception of images.
The amplitude, on the other hand, contributes more to the overall energy distribution and contrast of the image.

# Question 2

In general, modifying the phase tends to cause more significant and noticeable changes in the image compared to
modifying the amplitude. This is because:

Phase information carries more structural and edge information, which is crucial for human perception of images.
Amplitude modification typically affects the overall contrast and energy distribution of the image, which can be less
perceptually significant.

# Question 3 : Effects of Uniform Changes in Amplitude and Phase on Image Information

When applying uniform changes to either amplitude or phase in the frequency domain of an image, we observe different
effects on the image information. This analysis helps us understand the distinct roles of amplitude and phase in
representing image content.

## 1. Uniform Changes in Amplitude

Uniformly modifying the amplitude in the frequency domain scales the magnitude of all frequency components equally.

### a) Small increases in amplitude (scaling by 1.1-1.5):

- Slightly increases overall image contrast
- May enhance subtle textures
- Generally preserves the overall structure and content of the image

### b) Large increases in amplitude (scaling by 2 or more):

- Significantly boosts contrast, potentially leading to saturation
- May cause loss of detail in very bright or dark areas
- Can make the image appear "harsher" or more "synthetic"

### c) Decreases in amplitude (scaling by 0.5-0.9):

- Reduces overall contrast
- May make the image appear "flatter" or more muted
- Can obscure fine details, especially in areas of low contrast

## 2. Uniform Changes in Phase

Modifying the phase uniformly is more complex and can lead to more dramatic changes in the image.

### a) Small changes in phase (adding or subtracting a small constant):

- Can cause slight shifts or distortions in image features
- May introduce subtle artifacts or "ripples" in the image
- Generally preserves the overall structure but can alter fine details

### b) Moderate changes in phase:

- Can significantly distort the image structure
- May cause noticeable shifts in edge positions
- Can introduce interference patterns or moire effects

### c) Large changes in phase:

- Can completely scramble the image information
- May render the original content unrecognizable
- Often results in noise-like patterns or abstract textures

## Key Observations

1. **Information Preservation**: Amplitude changes generally preserve more of the original image information compared to
   phase changes. Even with significant amplitude scaling, the main structures and features of the image often remain
   recognizable.

2. **Structural Sensitivity**: Phase information is crucial for maintaining the structural integrity of the image. Even
   small changes in phase can lead to noticeable alterations in image features and edges.

3. **Texture Effects**: Uniform amplitude changes can enhance or suppress texture details, while phase changes can
   dramatically alter the texture characteristics, potentially creating new texture patterns.

4. **Perceptual Impact**: In most cases, uniform phase modifications will cause more significant perceptual changes than
   uniform amplitude modifications of similar magnitude.

5. **Non-linearity of Effects**: The impact of these changes is not strictly linear. Very small modifications might have
   subtle effects, while slightly larger changes can sometimes lead to disproportionately large visual impacts.

To truly appreciate these effects, it's best to experiment with different scaling factors on various types of images.
Textures with different characteristics (e.g., regular patterns vs. random textures) may respond differently to these
modifications.