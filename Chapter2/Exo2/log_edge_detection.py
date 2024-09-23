from cv2 import CV_64F, imshow, waitKey, GaussianBlur, imread, IMREAD_GRAYSCALE, destroyWindow, Laplacian
from numpy import uint8, ndarray, zeros_like


def log_edge_detection(image: ndarray, kernel_size: int = 5, sigma: float = 1.0) -> ndarray:
    """
    Apply Laplacian of Gaussian (LoG) edge detection to the input image using OpenCV.

    Args:
        image (np.ndarray): Input image as a 2D numpy array (grayscale).
        kernel_size (int): Size of the Gaussian kernel. Must be odd and positive.
        sigma (float): Standard deviation of the Gaussian distribution.

    Returns:
        np.ndarray: Edge map after zero-crossing detection.
    """
    # Apply Gaussian blur
    blurred = GaussianBlur(image, (kernel_size, kernel_size), sigma)

    # Apply Laplacian
    laplacian = Laplacian(blurred, CV_64F)

    # Detect zero-crossings
    zero_crossings = detect_zero_crossings(laplacian)

    return zero_crossings


def detect_zero_crossings(laplacian: ndarray) -> ndarray:
    """
    Detect zero-crossings in the Laplacian result.

    Args:
        laplacian (np.ndarray): Result of Laplacian operation.

    Returns:
        np.ndarray: Binary edge map where edges are marked as 255.
    """
    rows, cols = laplacian.shape
    zero_crossings = zeros_like(laplacian, dtype=uint8)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            neighbors = [
                laplacian[i - 1, j], laplacian[i + 1, j],
                laplacian[i, j - 1], laplacian[i, j + 1],
                laplacian[i - 1, j - 1], laplacian[i - 1, j + 1],
                laplacian[i + 1, j - 1], laplacian[i + 1, j + 1]
            ]

            if (min(neighbors) < 0) and (max(neighbors) < 0):
                zero_crossings[i, j] = 255

    return zero_crossings


def display_image(window_name: str, image: ndarray):
    """
    Display an image in a named window and wait for a key press.

    Args:
        window_name (str): Name of the window to display the image.
        image (np.ndarray): Image to display.
    """
    imshow(window_name, image)
    waitKey(0)
    destroyWindow(window_name)


def main():
    image_path = "../../data/img.png"
    image = imread(image_path, IMREAD_GRAYSCALE)

    if image is None:
        print(f"Error: Could not read image from {image_path}")
        return

    # Apply LoG edge detection
    log_edges = log_edge_detection(image, kernel_size=5, sigma=1.4)

    log_edges = 255 - log_edges

    # Display original image and edge detection results
    display_image("Original Image", image)
    display_image("LoG Edge Detection", log_edges)

    print("Edge detection completed. All windows closed.")


if __name__ == "__main__":
    main()
