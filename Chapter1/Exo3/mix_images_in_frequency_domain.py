from cv2 import imshow, waitKey, DFT_COMPLEX_OUTPUT, destroyAllWindows, polarToCart, NORM_MINMAX, IMREAD_GRAYSCALE, dft, \
    cartToPolar, merge, normalize, idft, imread, magnitude
from numpy import float32, uint8, ndarray


def mix_images_in_frequency_domain(img1: ndarray, img2: ndarray) -> ndarray:
    """
    Transform two images into the frequency domain, mix their amplitudes and phases,
    and transform the result back to the spatial domain.

    :param img1: First input image (numpy array)
    :param img2: Second input image (numpy array)
    :return: Mixed image in spatial domain
    """
    # Check if images have the same size
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")

    # Convert images to float32
    img1_float = float32(img1)
    img2_float = float32(img2)

    # Transform images to frequency domain
    dft1 = dft(img1_float, flags=DFT_COMPLEX_OUTPUT)
    dft2 = dft(img2_float, flags=DFT_COMPLEX_OUTPUT)

    # Compute amplitude and phase of both images
    amplitude1, phase1 = cartToPolar(dft1[:, :, 0], dft1[:, :, 1])
    amplitude2, phase2 = cartToPolar(dft2[:, :, 0], dft2[:, :, 1])

    # Mix amplitude from img1 with phase from img2
    x, y = polarToCart(amplitude1, phase2)
    combined_complex = merge([x, y])

    # Transform back to spatial domain
    mixed_image = idft(combined_complex)
    mixed_image = magnitude(mixed_image[:, :, 0], mixed_image[:, :, 1])

    # Normalize the result for display
    normalize(mixed_image, mixed_image, 0, 255, NORM_MINMAX)
    return uint8(mixed_image)


def load_and_prepare_image(path: str) -> ndarray:
    """
    Load an image and convert it to grayscale.

    :param path: Path to the image file
    :return: Grayscale image as numpy array
    """
    img = imread(path, IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not load image from {path}")
    return img


def main():
    # Load and prepare images
    img1 = load_and_prepare_image('../../data/img.png')
    img2 = load_and_prepare_image('../../data/img2.jpg')

    # Mix images in frequency domain
    mixed_image = mix_images_in_frequency_domain(img1, img2)

    # Display results
    imshow('Image 1 (Amplitude)', img1)
    imshow('Image 2 (Phase)', img2)
    imshow('Mixed Image', mixed_image)
    waitKey(0)
    destroyAllWindows()


if __name__ == "__main__":
    main()
