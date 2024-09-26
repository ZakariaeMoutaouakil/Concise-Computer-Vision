from cv2 import IMREAD_COLOR, imshow, waitKey, destroyAllWindows, imread, pyrMeanShiftFiltering
from numpy import ndarray


def mean_shift_segmentation(
        image_path: str,
        spatial_radius: int = 21,
        color_radius: int = 51,
        max_level: int = 1
) -> ndarray:
    """
    Segments an image using mean shift filtering.

    Parameters:
        image_path (str): Path to the input image.
        spatial_radius (int): The spatial window radius.
        color_radius (int): The color window radius.
        max_level (int): Maximum level of the pyramid for the segmentation.

    Returns:
        np.ndarray: The segmented image.
    """
    # Read the image
    img = imread(image_path, IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")

    # Apply mean shift filtering
    segmented = pyrMeanShiftFiltering(
        img, spatial_radius, color_radius, maxLevel=max_level
    )
    return segmented


def main():
    # Example usage
    image_path = '../../data/img.png'  # Replace with your image path
    segmented_image = mean_shift_segmentation(image_path)

    # Display the original and segmented images
    img = imread(image_path)
    imshow('Original Image', img)
    imshow('Segmented Image', segmented_image)

    # Wait until any key is pressed, then close windows
    waitKey(0)
    destroyAllWindows()


if __name__ == '__main__':
    main()
