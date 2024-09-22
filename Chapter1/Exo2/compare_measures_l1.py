from itertools import combinations
from typing import List, Dict, Tuple

from numpy import std, abs, array, mean, sum

from Chapter1.Exo2.calculate_data_measures import calculate_data_measures
from Chapter1.Exo2.normalize_measures import normalize_measures
from Chapter1.Exo2.read_image_sequence import read_image_sequence, process_image_sequence


def l1_distance(x: List[float], y: List[float]) -> float:
    """
    Calculate the L1 distance between two lists of numbers.

    Args:
    x (List[float]): First list of numbers
    y (List[float]): Second list of numbers

    Returns:
    float: L1 distance between x and y
    """
    return sum(abs(array(x) - array(y)))


def compare_measures_l1(measures: Dict[str, List[float]]) -> Dict[Tuple[str, str], float]:
    """
    Compare all pairs of measures using L1 metric.

    Args:
    measures (Dict[str, List[float]]): Dictionary of normalized measures

    Returns:
    Dict[Tuple[str, str], float]: Dictionary of L1 distances between each pair of measures
    """
    comparisons = {}
    measure_names = list(measures.keys())

    for name1, name2 in combinations(measure_names, 2):
        distance = l1_distance(measures[name1], measures[name2])
        comparisons[(name1, name2)] = distance

    return comparisons


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

        # Compare measures using L1 metric
        l1_comparisons = compare_measures_l1(normalized_data_measures)
        print("\nL1 distances between normalized measures:")
        for (measure1, measure2), distance in l1_comparisons.items():
            print(f"  {measure1} vs {measure2}: {distance:.4f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
