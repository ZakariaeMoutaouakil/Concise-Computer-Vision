from typing import Dict, List

from numpy import std, array, mean

from Chapter1.Exo2.calculate_data_measures import calculate_data_measures
from Chapter1.Exo2.read_image_sequence import read_image_sequence, process_image_sequence


def normalize_measures(measures: Dict[str, List[float]]) -> Dict[str, List[float]]:
    """
    Normalize all measures to have the same expectation and variance.

    Args:
    measures (Dict[str, List[float]]): Dictionary of original measures.

    Returns:
    Dict[str, List[float]]: Dictionary of normalized measures.
    """
    target_mean = 0
    target_std = 1

    normalized_measures = {}

    for name, values in measures.items():
        values = array(values)
        expectation = mean(values)
        deviation = std(values)

        # Avoid division by zero
        if deviation == 0:
            deviation = 1e-6

        # Normalize to zero expectation and unit variance
        normalized = (values - expectation) / deviation

        # Scale to target expectation and standard deviation
        normalized = normalized * target_std + target_mean

        normalized_measures[name] = normalized.tolist()

    return normalized_measures


def main():
    try:
        # Replace with your actual directory path
        image_sequence = read_image_sequence("../../gif", num_frames=50)
        print(f"Successfully read {len(image_sequence)} images.")

        avg_brightness, avg_contrast, avg_motion = process_image_sequence(image_sequence)
        print(f"Average Brightness: {avg_brightness:.2f}")
        print(f"Average Contrast: {avg_contrast:.2f}")
        print(f"Average Motion: {avg_motion:.2f}")

        # Calculate and print normalized data measures
        data_measures = calculate_data_measures(image_sequence)
        normalized_data_measures = normalize_measures(data_measures)
        for measure, values in normalized_data_measures.items():
            print(f"\n{measure} statistics (normalized):")
            print(f"  Min: {min(values):.4f}")
            print(f"  Max: {max(values):.4f}")
            print(f"  Mean: {mean(values):.4f}")
            print(f"  Std Dev: {std(values):.4f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
