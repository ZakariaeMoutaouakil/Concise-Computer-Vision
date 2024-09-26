import cv2
import numpy as np
from typing import Tuple

def segment_image_with_flood_fill(image: np.ndarray) -> np.ndarray:
    """
    Segments an image using the flood fill algorithm.

    Args:
        image: Input image as a NumPy array.

    Returns:
        Segmented image as a NumPy array.
    """
    h, w = image.shape[:2]
    # Mask for flood fill needs to be 2 pixels larger than the image
    mask = np.zeros((h + 2, w + 2), np.uint8)
    # Copy of the image to work on
    img_floodfill = image.copy()
    # Label counter
    label = 0
    # Generate a list of colors for labeling
    colors = []
    np.random.seed(0)
    for _ in range(10000):
        colors.append((
            int(np.random.randint(0, 256)),
            int(np.random.randint(0, 256)),
            int(np.random.randint(0, 256))
        ))
    # Loop over image pixels
    for y in range(h):
        for x in range(w):
            # Check if the mask at (y+1, x+1) is zero (since mask is larger)
            if mask[y + 1, x + 1] == 0:
                # Seed point
                seed_point = (x, y)
                # Color to fill
                newVal = colors[label % len(colors)]
                # Flood fill
                _, img_floodfill, mask, _ = cv2.floodFill(
                    img_floodfill, mask, seed_point, newVal=newVal,
                    loDiff=(10, 10, 10), upDiff=(10, 10, 10), flags=8
                )
                label += 1
    return img_floodfill

def main():
    # Example usage
    # Read image
    image = cv2.imread('../../data/img.png')
    # Check if image is loaded properly
    if image is None:
        print('Error: Image not found or could not be opened.')
        return
    # Segment image
    segmented_image = segment_image_with_flood_fill(image)
    # Show original and segmented images
    cv2.imshow('Original Image', image)
    cv2.imshow('Segmented Image', segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
