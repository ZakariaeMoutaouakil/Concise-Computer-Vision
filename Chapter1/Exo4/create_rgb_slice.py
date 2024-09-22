from typing import Tuple

from cv2 import imshow, createTrackbar, waitKey, destroyAllWindows, namedWindow
from numpy import sqrt, uint8, ndarray, zeros, arctan2, degrees


def create_hsi_slice(u: int, size: int = 400) -> ndarray:
    """
    Create an HSI slice for a given intensity value u.

    :param u: Intensity value (0-255)
    :param size: Size of the output image (default: 400x400)
    :return: NumPy array representing the HSI slice
    """
    hsi_slice = zeros((size, size, 3), dtype=uint8)
    center = size // 2
    max_radius = center - 1

    for y in range(size):
        for x in range(size):
            dx = x - center
            dy = y - center
            distance = sqrt(dx ** 2 + dy ** 2)

            if distance <= max_radius:
                hue = degrees(arctan2(dy, dx)) % 360
                saturation = distance / max_radius

                r, g, b = hsi_to_rgb(hue, saturation, u / 255)
                hsi_slice[y, x] = [b, g, r]  # OpenCV uses BGR format

    return hsi_slice


def hsi_to_rgb(h: float, s: float, i: float) -> Tuple[int, int, int]:
    """
    Convert HSI color values to RGB.

    :param h: Hue (0-360)
    :param s: Saturation (0-1)
    :param i: Intensity (0-1)
    :return: Tuple of RGB values (0-255)
    """
    h = h % 360
    h_sector = h / 60
    chroma = s * i
    x = chroma * (1 - abs(h_sector % 2 - 1))
    m = i - chroma

    if 0 <= h_sector < 1:
        r, g, b = chroma, x, 0
    elif 1 <= h_sector < 2:
        r, g, b = x, chroma, 0
    elif 2 <= h_sector < 3:
        r, g, b = 0, chroma, x
    elif 3 <= h_sector < 4:
        r, g, b = 0, x, chroma
    elif 4 <= h_sector < 5:
        r, g, b = x, 0, chroma
    else:
        r, g, b = chroma, 0, x

    r, g, b = r + m, g + m, b + m

    return (
        max(0, min(255, int(r * 255))),
        max(0, min(255, int(g * 255))),
        max(0, min(255, int(b * 255)))
    )


def show_hsi_slices() -> None:
    """
    Display HSI slices using a trackbar to control the intensity value.
    """
    window_name = "HSI Slice Visualization"
    namedWindow(window_name)

    def on_trackbar(value: int) -> None:
        hsi_slice = create_hsi_slice(value)
        imshow(window_name, hsi_slice)

    createTrackbar("Intensity", window_name, 0, 255, on_trackbar)
    on_trackbar(0)  # Initialize with u = 0

    while True:
        key = waitKey(1) & 0xFF
        if key == 27:  # ESC key
            break

    destroyAllWindows()


def main() -> None:
    """
    Example usage of the HSI slice visualization.
    """
    print("HSI Slice Visualization")
    print("Use the trackbar to adjust the intensity value (u).")
    print("Press ESC to exit.")

    show_hsi_slices()


if __name__ == "__main__":
    main()
