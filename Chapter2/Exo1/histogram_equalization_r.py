from typing import Tuple, Dict, List

from cv2 import imshow, waitKey, destroyAllWindows, imread, IMREAD_GRAYSCALE
from numpy import histogram, cumsum, array, mean, arange, sum, uint8, ndarray, clip, linspace, meshgrid


def sigma_filter(img: ndarray, window_size: int, sigma: float) -> ndarray:
    """
    Apply sigma filter to a grayscale image.

    Parameters:
    img: np.ndarray
        Input grayscale image.
    window_size: int
        Size of the window (must be odd).
    sigma: float
        Standard deviation threshold.

    Returns:
    np.ndarray
        Filtered image.
    """
    from scipy.ndimage import generic_filter

    def filter_func(values):
        center_value = values[len(values) // 2]
        lower_bound = center_value - sigma
        upper_bound = center_value + sigma
        valid_values = values[(values >= lower_bound) & (values <= upper_bound)]
        if len(valid_values) == 0:
            return center_value
        else:
            return mean(valid_values)

    filtered_img = generic_filter(
        img,
        function=filter_func,
        size=window_size,
        mode='reflect'
    )

    return filtered_img


def histogram_equalization_with_r(img: ndarray, r_values: List[float], Gmax: int = 255) -> Tuple[
    Dict[float, ndarray], Dict[float, ndarray]]:
    """
    Apply histogram equalization with varying r.

    Parameters:
    img: np.ndarray
        Input grayscale image.
    r_values: List[float]
        List of r values.
    Gmax: int
        Maximum grey level (default is 255).

    Returns:
    Tuple[Dict[float, np.ndarray], Dict[float, np.ndarray]]
        A tuple of dictionaries mapping r to equalized images and histograms.
    """
    images = {}
    histograms = {}

    # Compute the histogram hI(u)
    hI, bins = histogram(img.flatten(), bins=Gmax + 1, range=(0, Gmax), density=False)
    hI = hI / img.size  # Convert to relative frequencies

    for r in r_values:
        # Compute hI(w)^r
        hI_r = hI ** r
        Q = sum(hI_r)
        cI_r = cumsum(hI_r)
        g = (Gmax / Q) * cI_r
        g = clip(g, 0, Gmax).astype(uint8)

        # Map the image
        img_equalized = g[img.astype(int)]

        images[r] = img_equalized
        histograms[r] = histogram(img_equalized.flatten(), bins=Gmax + 1, range=(0, Gmax), density=False)[0]

    return images, histograms


def visualize_histograms(histograms: Dict[float, ndarray], Gmax: int = 255):
    """
    Visualize histograms as a 2D image or 3D surface plot.

    Parameters:
    histograms: Dict[float, np.ndarray]
        Dictionary mapping r to histogram counts.
    Gmax: int
        Maximum grey level (default is 255).
    """
    import matplotlib.pyplot as plt

    r_values = sorted(histograms.keys())
    grey_levels = arange(Gmax + 1)

    # Create a 2D array where rows are r values, columns are grey levels
    histogram_array = array([histograms[r] for r in r_values])

    # Normalize the histograms for visualization
    histogram_array = histogram_array / histogram_array.max()

    # Plot as 2D image
    plt.figure(figsize=(10, 6))
    plt.imshow(histogram_array, aspect='auto', extent=[0, Gmax, r_values[0], r_values[-1]], origin='lower')
    plt.colorbar(label='Normalized Histogram Count')
    plt.xlabel('Grey Level')
    plt.ylabel('r Value')
    plt.title('2D Histogram of Equalized Images for Varying r')
    plt.show()

    # Plot as 3D surface plot
    X, Y = meshgrid(grey_levels, r_values)
    Z = histogram_array

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_xlabel('Grey Level')
    ax.set_ylabel('r Value')
    ax.set_zlabel('Normalized Histogram Count')
    plt.title('3D Surface Plot of Histograms for Varying r')
    plt.show()


def main():
    """
    Main function to demonstrate the sigma filter and histogram equalization.
    """
    # Read a grayscale image
    img = imread('../../data/noise.png', IMREAD_GRAYSCALE)

    if img is None:
        print('Error: Could not open or find the image.')
        return

    # Parameters
    window_size = 5  # Must be odd
    sigma = 15.0  # Adjust as needed

    # Apply sigma filter
    filtered_img = sigma_filter(img, window_size, sigma)
    filtered_img_uint8 = clip(filtered_img, 0, 255).astype(uint8)

    # Define r values
    r_values = linspace(0.5, 2.0, num=16)  # For example, from 0.5 to 2.0

    # Apply histogram equalization with varying r
    images, histograms = histogram_equalization_with_r(filtered_img_uint8, r_values.tolist())

    # Visualize histograms
    visualize_histograms(histograms)

    # Display the original and filtered images
    imshow('Original Image', img)
    imshow('Sigma Filtered Image', filtered_img_uint8)
    waitKey(0)
    destroyAllWindows()

    # Display equalized images for selected r values
    for r in [0.5, 1.0, 1.5, 2.0]:
        img_eq = images[r]
        imshow(f'Equalized Image r={r:.2f}', img_eq)
        waitKey(0)
        destroyAllWindows()


if __name__ == '__main__':
    main()
