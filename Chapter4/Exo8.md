# Analysis of Horn-Schunck Algorithm Initialization

## Question

An initialization by zero in the Horn-Schunck algorithm would not be possible if the resulting initial u- and v-values
would also be zero. Verify that this is not happening in general (i.e., if there exists motion) at the start of the
iteration of this algorithm.

## Analysis

To verify that the initialization by zero in the Horn-Schunck algorithm does not result in zero u- and v-values when
motion exists, let's examine the update equations of the algorithm.

### Horn-Schunck Update Equations

The Horn-Schunck algorithm uses the following update equations:

```
u = u_avg - Ix * (Ix * u_avg + Iy * v_avg + It) / (α^2 + Ix^2 + Iy^2)
v = v_avg - Iy * (Ix * u_avg + Iy * v_avg + It) / (α^2 + Ix^2 + Iy^2)
```

Where:

- u and v are the horizontal and vertical components of the optical flow
- u_avg and v_avg are the local averages of u and v
- Ix, Iy, and It are the spatial and temporal image derivatives
- α is the regularization parameter

### Initial Iteration

At the start of the iteration:

1. We initialize u and v to zero: u = 0, v = 0
2. Consequently, u_avg and v_avg are also zero: u_avg = 0, v_avg = 0

Substituting these into the update equations:

```
u = 0 - Ix * (Ix * 0 + Iy * 0 + It) / (α^2 + Ix^2 + Iy^2)
  = -Ix * It / (α^2 + Ix^2 + Iy^2)

v = 0 - Iy * (Ix * 0 + Iy * 0 + It) / (α^2 + Ix^2 + Iy^2)
  = -Iy * It / (α^2 + Ix^2 + Iy^2)
```

### Verification

For u and v to be non-zero after the first iteration, we need:

1. It ≠ 0 (temporal derivative is non-zero, indicating motion)
2. Ix ≠ 0 and/or Iy ≠ 0 (spatial derivatives are non-zero, indicating image texture)

When motion exists:

- It will be non-zero in regions where pixel intensities change over time.
- In most real-world scenarios, Ix and Iy will be non-zero in textured regions of the image.

Therefore, as long as there is motion and the image isn't perfectly uniform, u and v will become non-zero after the
first iteration.

## Conclusion

The initialization by zero in the Horn-Schunck algorithm does not result in zero u- and v-values when motion exists.
After the first iteration:

1. If there's motion (It ≠ 0) and image texture (Ix ≠ 0 and/or Iy ≠ 0), both u and v will become non-zero.
2. If there's no motion (It = 0), u and v will remain zero, correctly indicating no optical flow.
3. If the image is perfectly uniform (Ix = Iy = 0), u and v will be undefined (0/0), but this is an edge case that
   doesn't occur in practice with real images.

Thus, the Horn-Schunck algorithm can indeed start with an initialization of zero for u and v, and it will still detect
motion when it exists.