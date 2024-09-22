from typing import Tuple

from cv2 import meanStdDev, imshow, waitKey, calcHist, destroyAllWindows, setMouseCallback, EVENT_MOUSEMOVE, \
    FONT_HERSHEY_SIMPLEX, mean, putText, imread, rectangle, namedWindow
from matplotlib.pyplot import xlim, figure, ylabel, plot, show, xlabel, title, close
from numpy import ndarray


def analyze_image(image_path: str) -> None:
    def calculate_histogram(window: ndarray) -> Tuple[ndarray, ndarray, ndarray]:
        hist_b = calcHist([window], [0], None, [256], [0, 256])
        hist_g = calcHist([window], [1], None, [256], [0, 256])
        hist_r = calcHist([window], [2], None, [256], [0, 256])
        return hist_b, hist_g, hist_r

    def plot_histogram(hist_b: ndarray, hist_g: ndarray, hist_r: ndarray) -> None:
        figure()
        title("Color Histogram")
        xlabel("Bins")
        ylabel("# of Pixels")
        plot(hist_b, color='b')
        plot(hist_g, color='g')
        plot(hist_r, color='r')
        xlim([0, 256])
        show(block=False)

    def mouse_callback(event: int, x: int, y: int, flags: int, param: None) -> None:
        if event == EVENT_MOUSEMOVE:
            img_copy = img.copy()

            # Draw the outer border of the 11x11 window
            rectangle(img_copy, (x - 5, y - 5), (x + 5, y + 5), (128, 128, 128), 1)

            # Get RGB values at the current pixel
            b, g, r = img[y, x]

            # Calculate intensity value
            intensity = (int(r) + int(g) + int(b)) / 3

            # Calculate mean and standard deviation of the 11x11 window
            window = img[max(0, y - 5):min(img.shape[0], y + 6), max(0, x - 5):min(img.shape[1], x + 6)]
            expectation = mean(window)[:3]  # Get only BGR values
            stddev = meanStdDev(window)[1][:3]  # Get only BGR values

            # Calculate histogram of the window
            hist_b, hist_g, hist_r = calculate_histogram(window)

            # Display information
            putText(img_copy, f"Pos: ({x}, {y}) RGB: ({r}, {g}, {b})", (10, 30),
                    FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            putText(img_copy, f"Intensity: {intensity:.2f}", (10, img.shape[0] - 10),
                    FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            putText(img_copy, f"Mean: ({expectation[0]:.2f}, {expectation[1]:.2f}, {expectation[2]:.2f})",
                    (10, img.shape[0] - 40),
                    FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            putText(img_copy, f"StdDev: ({stddev[0][0]:.2f}, {stddev[1][0]:.2f}, {stddev[2][0]:.2f})",
                    (10, img.shape[0] - 70),
                    FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            # Show the image with information
            imshow("Image Analysis", img_copy)

            # Plot histogram
            plot_histogram(hist_b, hist_g, hist_r)

    # Read the image
    img = imread(image_path)
    if img is None:
        raise ValueError(f"Unable to read image from {image_path}")

    # Create a window and set the callback
    namedWindow("Image Analysis")
    setMouseCallback("Image Analysis", mouse_callback)

    # Display the image
    imshow("Image Analysis", img)

    # Wait for a key press
    waitKey(0)
    destroyAllWindows()
    close('all')


def main() -> None:
    image_path = "../../data/img.png"
    try:
        analyze_image(image_path)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
