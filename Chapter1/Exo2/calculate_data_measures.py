from typing import List, Dict

from cv2 import cartToPolar, cvtColor, COLOR_BGR2GRAY, absdiff, calcOpticalFlowFarneback
from numpy import std, mean, ndarray
from skimage.metrics import structural_similarity as ssim

from Chapter1.Exo2.read_image_sequence import read_image_sequence, process_image_sequence


def calculate_data_measures(images: List[ndarray]) -> Dict[str, List[float]]:
    """
    Calculate three data measures for the image sequence:
    1. Temporal Gradient Magnitude
    2. Structural Similarity Index (SSIM)
    3. Optical Flow Magnitude

    Args:
    images (List[np.ndarray]): List of images as numpy arrays.

    Returns:
    Dict[str, List[float]]: Dictionary containing lists of measure values for each frame.
    """
    temporal_gradient = []
    structural_similarity = []
    optical_flow_magnitude = []

    prev_gray = cvtColor(images[0], COLOR_BGR2GRAY)

    for i in range(1, len(images)):
        gray = cvtColor(images[i], COLOR_BGR2GRAY)

        # Calculate Temporal Gradient Magnitude
        grad = absdiff(gray, prev_gray)
        temporal_gradient.append(mean(grad))

        # Calculate Structural Similarity Index (SSIM)
        ssim_value, _ = ssim(prev_gray, gray, full=True)
        structural_similarity.append(ssim_value)

        # Calculate Optical Flow Magnitude
        flow = calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        magnitude, _ = cartToPolar(flow[..., 0], flow[..., 1])
        optical_flow_magnitude.append(mean(magnitude))

        prev_gray = gray

    return {
        "Temporal Gradient Magnitude": temporal_gradient,
        "Structural Similarity Index": structural_similarity,
        "Optical Flow Magnitude": optical_flow_magnitude
    }


def main():
    try:
        # Replace with your actual directory path
        image_sequence = read_image_sequence("../../gif", num_frames=50)
        print(f"Successfully read {len(image_sequence)} images.")

        avg_brightness, avg_contrast, avg_motion = process_image_sequence(image_sequence)
        print(f"Average Brightness: {avg_brightness:.2f}")
        print(f"Average Contrast: {avg_contrast:.2f}")
        print(f"Average Motion: {avg_motion:.2f}")

        # Calculate and print data measures
        data_measures = calculate_data_measures(image_sequence)
        for measure, values in data_measures.items():
            print(f"\n{measure} statistics:")
            print(f"  Min: {min(values):.4f}")
            print(f"  Max: {max(values):.4f}")
            print(f"  Mean: {mean(values):.4f}")
            print(f"  Std Dev: {std(values):.4f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
