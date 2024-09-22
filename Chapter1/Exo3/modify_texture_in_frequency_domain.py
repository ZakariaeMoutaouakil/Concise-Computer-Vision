from typing import Callable

from cv2 import imshow, waitKey, DFT_COMPLEX_OUTPUT, destroyAllWindows, polarToCart, NORM_MINMAX, IMREAD_GRAYSCALE, dft, \
    cartToPolar, merge, normalize, idft, imread, magnitude
from numpy import float32, uint8, ndarray
from numpy.fft import fftshift, ifftshift


def modify_texture_in_frequency_domain(
        img: ndarray,
        modification_func: Callable[[ndarray], ndarray],
        modify_amplitude: bool = True
) -> ndarray:
    """
    Modify a texture image in the frequency domain.

    :param img: Input grayscale image
    :param modification_func: Function to apply to amplitude or phase
    :param modify_amplitude: If True, modify amplitude; if False, modify phase
    :return: Modified image
    """
    # Convert to float32
    float_img = float32(img)

    # Apply DFT
    dft_res = dft(float_img, flags=DFT_COMPLEX_OUTPUT)
    dft_shift = fftshift(dft_res)

    # Split into magnitude and phase
    magnitude_res, phase = cartToPolar(dft_shift[:, :, 0], dft_shift[:, :, 1])

    # Apply modification
    if modify_amplitude:
        magnitude_res = modification_func(magnitude_res)
    else:
        phase = modification_func(phase)

    # Combine magnitude and phase
    real, imag = polarToCart(magnitude_res, phase)
    combined = merge([real, imag])

    # Inverse DFT
    idft_shift = ifftshift(combined)
    idft_res = idft(idft_shift)

    # Magnitude spectrum
    modified_img = magnitude(idft_res[:, :, 0], idft_res[:, :, 1])

    # Normalize for display
    normalize(modified_img, modified_img, 0, 255, NORM_MINMAX)
    return uint8(modified_img)


def uniform_scale(arr: ndarray, scale: float) -> ndarray:
    """
    Scale an array uniformly.

    :param arr: Input array
    :param scale: Scaling factor
    :return: Scaled array
    """
    return arr * scale


def load_grayscale_image(path: str) -> ndarray:
    """
    Load a grayscale image from file.

    :param path: Path to the image file
    :return: Grayscale image as numpy array
    """
    img = imread(path, IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not load image from {path}")
    return img


def main():
    # Load a texture image
    img_path = "../../data/face.jpg"
    original_img = load_grayscale_image(img_path)

    # Define modification functions
    amplitude_scale = lambda x: uniform_scale(x, 1.5)  # Increase amplitude by 50%
    phase_scale = lambda x: uniform_scale(x, 1.2)  # Increase phase by 20%

    # Modify amplitude
    amplitude_modified = modify_texture_in_frequency_domain(original_img, amplitude_scale, modify_amplitude=True)

    # Modify phase
    phase_modified = modify_texture_in_frequency_domain(original_img, phase_scale, modify_amplitude=False)

    # Display results
    imshow("Original", original_img)
    imshow("Amplitude Modified", amplitude_modified)
    imshow("Phase Modified", phase_modified)
    waitKey(0)
    destroyAllWindows()


if __name__ == "__main__":
    main()
