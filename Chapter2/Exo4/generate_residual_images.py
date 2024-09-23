from os import makedirs
from os.path import exists

from cv2 import GaussianBlur, normalize, imread, blur, NORM_MINMAX, imwrite, IMREAD_GRAYSCALE
from numpy import abs, mean, float32, uint8, ndarray


def recursive_box_filter(image: ndarray, n: int) -> ndarray:
    """Applies a 3x3 box filter recursively n times and returns the residual image.

    Args:
        image (np.ndarray): Input image.
        n (int): Number of iterations.

    Returns:
        np.ndarray: Residual image after applying the recursive box filter.
    """
    # Convert image to float32 to prevent data loss
    smooth = image.astype(float32)

    # Apply the box filter n times
    for _ in range(n):
        smooth = blur(smooth, (3, 3))

    # Compute the residual image
    residual = image.astype(float32) - smooth

    return residual


def gaussian_filter_residual(image: ndarray, k: int) -> ndarray:
    """Applies a Gaussian filter with size (2k+1)x(2k+1) and returns the residual image.

    Args:
        image (np.ndarray): Input image.
        k (int): Kernel size parameter.

    Returns:
        np.ndarray: Residual image after applying the Gaussian filter.
    """
    # Convert image to float32
    image_float = image.astype(float32)

    # Apply Gaussian filter
    kernel_size = (2 * k + 1, 2 * k + 1)
    smooth = GaussianBlur(image_float, kernel_size, 0)

    # Compute the residual image
    residual = image_float - smooth

    return residual


def main():
    """Example usage of recursive_box_filter and gaussian_filter_residual."""
    # Create a results directory if it doesn't exist
    if not exists('results'):
        makedirs('results')

    # Load an example image
    image = imread('../../data/img.png', IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Image not found.")
        return

    # Apply recursive box filter and Gaussian filter, compare residuals
    for n in range(1, 31):
        residual_box = recursive_box_filter(image, n)
        residual_gauss = gaussian_filter_residual(image, n + 1 if n <= 15 else 15)

        # Normalize residuals for saving
        residual_box_norm = normalize(residual_box, None, 0, 255, NORM_MINMAX)
        residual_box_norm = residual_box_norm.astype(uint8)
        imwrite(f'results/residual_box_n{n}.png', residual_box_norm)

        if n <= 15:
            residual_gauss_norm = normalize(residual_gauss, None, 0, 255, NORM_MINMAX)
            residual_gauss_norm = residual_gauss_norm.astype(uint8)
            imwrite(f'results/residual_gauss_k{n + 1}.png', residual_gauss_norm)

            # Compute the difference between the two residuals
            diff = abs(residual_box - residual_gauss)
            mean_abs_diff = mean(diff)
            print(f'For n = {n}, Mean Absolute Difference between residuals: {mean_abs_diff}')

            # Save difference image
            diff_norm = normalize(diff, None, 0, 255, NORM_MINMAX)
            diff_norm = diff_norm.astype(uint8)
            imwrite(f'results/residual_difference_n{n}.png', diff_norm)


if __name__ == '__main__':
    main()
