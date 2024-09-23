from typing import Tuple

from cv2 import imshow, waitKey, Canny, normalize, destroyAllWindows, imread, NORM_MINMAX, threshold, THRESH_BINARY, \
    IMREAD_GRAYSCALE
from numpy import arange, float32, sum, zeros, meshgrid, pad, abs, count_nonzero, fft, sqrt, ones, uint8, ndarray


def compute_amplitude_phase_images(
        I: ndarray, k: int, T: float, epsilon: float = 0.01
) -> Tuple[ndarray, ndarray]:
    """
    Compute amplitude image M and phase congruency image P from input image I.

    Parameters:
        I (np.ndarray): Input grayscale image of shape (H, W), values in [0, 1].
        k (int): Half window size. Window size is (2k + 1) x (2k + 1).
        T (float): Sum of noise responses over all AC components.
        epsilon (float): Small positive number to avoid division by zero.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Amplitude image M and phase congruency image P.
    """
    H, W = I.shape
    N = 2 * k + 1  # Window size
    padded_I = pad(I, pad_width=k, mode='reflect')

    # Initialize M and P images
    M = zeros((H, W), dtype=float32)
    P = zeros((H, W), dtype=float32)

    # Precompute frequency grids
    u = arange(N)
    v = arange(N)
    u_grid, v_grid = meshgrid(u, v)

    # Shift zero frequency to center
    u_grid_shifted = fft.ifftshift(u_grid - k)
    v_grid_shifted = fft.ifftshift(v_grid - k)

    # Compute frequency magnitudes
    f_grid = sqrt(u_grid_shifted ** 2 + v_grid_shifted ** 2)

    # Define high-frequency threshold
    f_max = sqrt(2) * k
    f_thresh = 0.7 * f_max
    HFmask = f_grid >= f_thresh

    # Create AC mask (exclude DC component)
    ACmask = ones((N, N), dtype=bool)
    ACmask[k, k] = False  # Exclude DC component
    HF_AC_mask = HFmask & ACmask

    for i in range(H):
        for j in range(W):
            # Extract window
            W_patch = padded_I[i:i + N, j:j + N]

            # Perform DFT
            DFT_W = fft.fft2(W_patch)

            # Shift zero frequency to center
            DFT_W_shifted = fft.fftshift(DFT_W)

            # Exclude DC component
            DFT_AC = DFT_W_shifted.copy()
            DFT_AC[k, k] = 0

            # AC coefficients
            z_h = DFT_AC[ACmask]

            # Amplitudes
            r_h = abs(z_h)

            # Sum over AC coefficients
            z = sum(z_h)
            z_abs_squared = abs(z) ** 2
            sum_rh = sum(r_h)

            # Phase congruency measure P(p)
            P_p = max(z_abs_squared - T, 0) / (sum_rh + epsilon) if sum_rh + epsilon != 0 else 0
            P[i, j] = P_p

            # Amplitude measure M(p)
            r_h_HF = abs(DFT_AC[HF_AC_mask])
            sum_rh_HF = sum(r_h_HF)
            M_p = sum_rh_HF / sum_rh if sum_rh != 0 else 0
            M[i, j] = M_p

    return M, P


def main():
    """
    Main function to demonstrate the computation of amplitude and phase images.
    """
    # Read the image
    image_path = '../../data/img.png'  # Replace with your image path
    I = imread(image_path, IMREAD_GRAYSCALE)
    if I is None:
        print('Error: Image not found or unable to read.')
        return

    # Normalize image to [0, 1]
    I = I.astype(float32) / 255.0

    # Set parameters
    k = 1  # Half window size (e.g., k=1 for 3x3 window)
    T = 0.1  # Noise threshold (adjust as needed)
    epsilon = 0.01  # Small positive number

    # Compute amplitude and phase images
    M, P = compute_amplitude_phase_images(I, k, T, epsilon)

    # Normalize M and P for display
    M_display = normalize(M, None, 0, 255, NORM_MINMAX).astype(uint8)
    P_display = normalize(P, None, 0, 255, NORM_MINMAX).astype(uint8)

    # Edge detection using Canny
    edges = Canny((I * 255).astype(uint8), 100, 200)

    # Threshold M and P images
    _, M_thresh = threshold(M_display, 128, 255, THRESH_BINARY)
    _, P_thresh = threshold(P_display, 128, 255, THRESH_BINARY)

    # Quantify numbers of pixels
    edge_pixels = count_nonzero(edges)
    edge_and_M_pixels = count_nonzero(edges & M_thresh)
    edge_and_P_pixels = count_nonzero(edges & P_thresh)

    # Compute ratios
    ratio_M = edge_and_M_pixels / edge_pixels if edge_pixels > 0 else 0
    ratio_P = edge_and_P_pixels / edge_pixels if edge_pixels > 0 else 0

    print(f'Number of edge pixels: {edge_pixels}')
    print(f'Number of edge and M pixels: {edge_and_M_pixels}')
    print(f'Number of edge and P pixels: {edge_and_P_pixels}')
    print(f'Ratio of edge pixels in M image: {ratio_M:.2f}')
    print(f'Ratio of edge pixels in P image: {ratio_P:.2f}')

    # Display images
    imshow('Input Image', (I * 255).astype(uint8))
    imshow('Amplitude Image M', M_display)
    imshow('Phase Congruency Image P', P_display)
    imshow('Edges', edges)
    imshow('Thresholded M Image', M_thresh)
    imshow('Thresholded P Image', P_thresh)
    waitKey(0)
    destroyAllWindows()


if __name__ == '__main__':
    main()
