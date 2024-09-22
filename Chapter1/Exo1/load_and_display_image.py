from typing import Tuple

from numpy import uint8
from cv2 import imshow, waitKey, destroyAllWindows, imread, cvtColor, COLOR_BGR2RGB, IMREAD_UNCHANGED


def load_and_display_image(file_path: str) -> Tuple[bool, str]:
    """
    Load a color image from a file and display it on the screen using OpenCV.

    Args:
    file_path (str): The path to the image file.

    Returns:
    Tuple[bool, str]: A tuple containing a boolean indicating success (True) or failure (False),
                      and a string message describing the result.
    """
    try:
        # Read the image file
        img = imread(file_path, IMREAD_UNCHANGED)

        if img is None:
            return False, (f"Error: Unable to read the file '{file_path}'. "
                           f"Please check if the file exists and is in a supported format.")

        # Check if the image is in a lossless format (assuming 8-bit per channel for lossy formats)
        if img.dtype != uint8 or img.shape[2] == 3:  # 3 channels indicate color image
            # Convert BGR to RGB color space
            img_rgb = cvtColor(img, COLOR_BGR2RGB)

            # Display the image
            imshow("Image", img_rgb)
            waitKey(0)  # Wait for a key press
            destroyAllWindows()  # Close the window

            return True, "Image displayed successfully."
        else:
            return False, "Error: The image may not be in a lossless format. Please use PNG, BMP, or TIFF."

    except Exception as e:
        return False, f"Error: An unexpected error occurred: {str(e)}"


def main():
    # Example usage
    image_path = "../../data/img.png"
    success, message = load_and_display_image(image_path)
    print(message)


if __name__ == "__main__":
    main()
