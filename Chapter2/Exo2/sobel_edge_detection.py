from typing import Tuple

from cv2 import CV_64F, CV_8U, imshow, waitKey, normalize, Sobel, imread, NORM_MINMAX, IMREAD_GRAYSCALE, destroyWindow
from numpy import sqrt, ndarray


def sobel_edge_detection(image: ndarray, kernel_size: int = 3) -> Tuple[ndarray, ndarray, ndarray]:
    """
    Apply Sobel edge detection to the input image using OpenCV.

    Args:
        image (np.ndarray): Input image as a 2D numpy array (grayscale).
        kernel_size (int): Size of the Sobel kernel. Must be 1, 3, 5, or 7.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing:
            - Gradient magnitude
            - Gradient in X direction
            - Gradient in Y direction
    """
    if kernel_size not in (1, 3, 5, 7):
        raise ValueError("Kernel size must be 1, 3, 5, or 7")

    grad_x = Sobel(image, CV_64F, 1, 0, ksize=kernel_size)
    grad_y = Sobel(image, CV_64F, 0, 1, ksize=kernel_size)

    magnitude = sqrt(grad_x ** 2 + grad_y ** 2)
    magnitude = normalize(magnitude, None, 0, 255, NORM_MINMAX, dtype=CV_8U)

    return magnitude, grad_x, grad_y


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

    edge_magnitude, grad_x, grad_y = sobel_edge_detection(image)

    # Display original image
    display_image("Original Image", image)

    # Display edge detection results
    display_image("Edge Magnitude", edge_magnitude)
    display_image("Edges in X direction", normalize(grad_x, None, 0, 255, NORM_MINMAX, dtype=CV_8U))
    display_image("Edges in Y direction", normalize(grad_y, None, 0, 255, NORM_MINMAX, dtype=CV_8U))

    print("Edge detection completed. All windows closed.")


if __name__ == "__main__":
    main()
