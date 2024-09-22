from cv2 import imshow, createTrackbar, waitKey, destroyAllWindows, namedWindow
from numpy import sqrt, uint8, ndarray, zeros

from Chapter1.Exo4.create_rgb_slice import create_hsi_slice


def create_saturation_slice(u: int, size: int = 400) -> ndarray:
    """
    Create a saturation slice for a given intensity value u.

    :param u: Intensity value (0-255)
    :param size: Size of the output image (default: 400x400)
    :return: NumPy array representing the saturation slice
    """
    saturation_slice = zeros((size, size), dtype=uint8)
    center = size // 2
    max_radius = center - 1
    intensity = u / 255  # Normalize intensity to 0-1 range

    for y in range(size):
        for x in range(size):
            dx = x - center
            dy = y - center
            distance = sqrt(dx ** 2 + dy ** 2)

            if distance <= max_radius:
                saturation = distance / max_radius
                # Adjust saturation based on intensity
                adjusted_saturation = saturation * (1 - abs(2 * intensity - 1))
                saturation_slice[y, x] = int(adjusted_saturation * 255)

    return saturation_slice


def show_hsi_and_saturation_slices() -> None:
    """
    Display HSI and saturation slices using trackbars to control the intensity value.
    """
    rgb_window = "HSI Slice (RGB) Visualization"
    saturation_window = "Saturation Slice Visualization"
    namedWindow(rgb_window)
    namedWindow(saturation_window)

    def on_trackbar(value: int) -> None:
        hsi_slice = create_hsi_slice(value)
        saturation_slice = create_saturation_slice(value)
        imshow(rgb_window, hsi_slice)
        imshow(saturation_window, saturation_slice)

    createTrackbar("Intensity", rgb_window, 0, 255, on_trackbar)
    on_trackbar(0)  # Initialize with u = 0

    while True:
        key = waitKey(1) & 0xFF
        if key == 27:  # ESC key
            break

    destroyAllWindows()


def main() -> None:
    """
    Example usage of the HSI and saturation slice visualization.
    """
    print("HSI and Saturation Slice Visualization")
    print("Use the trackbar to adjust the intensity value (u).")
    print("Press ESC to exit.")

    show_hsi_and_saturation_slices()


if __name__ == "__main__":
    main()
