from cv2 import split, imshow, waitKey, calcHist, destroyAllWindows, imread
from matplotlib.pyplot import tight_layout, show, subplots
from numpy import ndarray


def display_color_histograms(image: ndarray) -> None:
    """
    Display histograms of all three color channels of an image.

    Args:
        image (np.ndarray): Input image in BGR format.
    """
    # Split the image into its color channels
    blue, green, red = split(image)

    # Create a figure with 3 subplots
    fig, axs = subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Color Channel Histograms')

    # List of colors, channel names, and corresponding image channels
    colors = ['b', 'g', 'r']
    channel_names = ['Blue', 'Green', 'Red']
    channels = [blue, green, red]

    # Calculate and plot histogram for each channel
    for i, (color, name, channel) in enumerate(zip(colors, channel_names, channels)):
        hist = calcHist([channel], [0], None, [256], [0, 256])
        axs[i].plot(hist, color=color)
        axs[i].set_title(f'{name} Channel')
        axs[i].set_xlabel('Pixel Value')
        axs[i].set_ylabel('Frequency')

    tight_layout()
    show()


def main() -> None:
    # Load an example image
    image_path = "../../data/img.png"
    image: ndarray = imread(image_path)

    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Display the original image
    imshow("Original Image", image)
    waitKey(1)  # Wait for a key event

    # Display color histograms
    display_color_histograms(image)

    # Close all OpenCV windows
    destroyAllWindows()


if __name__ == "__main__":
    main()
