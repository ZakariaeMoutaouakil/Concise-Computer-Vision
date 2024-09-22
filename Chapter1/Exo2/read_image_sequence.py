from typing import List, Tuple

from cv2 import imread, cvtColor, COLOR_BGR2GRAY, absdiff
from numpy import std, mean, ndarray


def read_image_sequence(directory: str, num_frames: int = 50) -> List[ndarray]:
    """
    Reads an image sequence from a directory.

    Args:
    directory (str): Path to the directory containing the image sequence.
    num_frames (int): Minimum number of frames to read. Defaults to 50.

    Returns:
    List[np.ndarray]: List of images as numpy arrays.

    Raises:
    ValueError: If fewer than num_frames images are found in the directory.
    """
    import glob
    import os

    # Get list of image files in the directory
    image_files = sorted(glob.glob(os.path.join(directory, '*.png')))  # Assuming PNG format, adjust if needed

    if len(image_files) < num_frames:
        raise ValueError(
            f"Not enough images in the directory. Found {len(image_files)}, but {num_frames} are required.")

    images = []
    for i in range(num_frames):
        img = imread(image_files[i])
        if img is None:
            raise ValueError(f"Failed to read image: {image_files[i]}")
        images.append(img)

    return images


def process_image_sequence(images: List[ndarray]) -> Tuple[float, float, float]:
    """
    Process the image sequence and return some basic statistics.

    Args:
    images (List[np.ndarray]): List of images as numpy arrays.

    Returns:
    Tuple[float, float, float]: Average brightness, average contrast, average motion (using simple frame difference).
    """
    brightness = []
    contrast = []
    motion = []

    for i, img in enumerate(images):
        # Convert to grayscale
        gray = cvtColor(img, COLOR_BGR2GRAY)

        # Calculate brightness (average pixel intensity)
        brightness.append(mean(gray))

        # Calculate contrast (standard deviation of pixel intensities)
        contrast.append(std(gray))

        # Calculate motion (if not the first frame)
        if i > 0:
            prev_gray = cvtColor(images[i - 1], COLOR_BGR2GRAY)
            frame_diff = absdiff(gray, prev_gray)
            motion.append(mean(frame_diff))

    return float(mean(brightness)), float(mean(contrast)), float(mean(motion))


def main():
    # Example usage
    try:
        # Replace with your actual directory path
        image_sequence = read_image_sequence("../../gif", num_frames=50)
        print(f"Successfully read {len(image_sequence)} images.")

        avg_brightness, avg_contrast, avg_motion = process_image_sequence(image_sequence)
        print(f"Average Brightness: {avg_brightness:.2f}")
        print(f"Average Contrast: {avg_contrast:.2f}")
        print(f"Average Motion: {avg_motion:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
