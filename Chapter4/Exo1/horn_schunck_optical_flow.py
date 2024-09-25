from typing import Tuple

from cv2 import imshow, waitKey, line, destroyAllWindows, cvtColor, filter2D, blur, COLOR_BGR2GRAY, COLOR_GRAY2BGR, \
    circle, VideoCapture
from numpy import mgrid, vstack, array, int32, ones, float32, ndarray, zeros_like


def calculate_derivatives(frame1: ndarray, frame2: ndarray) -> Tuple[ndarray, ndarray, ndarray]:
    """
    Calculate spatial and temporal image derivatives.

    :param frame1: First frame
    :param frame2: Second frame
    :return: Tuple of (Ix, Iy, It) derivatives
    """
    kernel_x = array([[-1, 1], [-1, 1]]) * 0.25
    kernel_y = array([[-1, -1], [1, 1]]) * 0.25
    kernel_t = ones((2, 2)) * 0.25

    Ix = filter2D(frame1, -1, kernel_x) + filter2D(frame2, -1, kernel_x)
    Iy = filter2D(frame1, -1, kernel_y) + filter2D(frame2, -1, kernel_y)
    It = filter2D(frame2, -1, kernel_t) - filter2D(frame1, -1, kernel_t)

    return Ix, Iy, It


def horn_schunck_optical_flow(frame1: ndarray, frame2: ndarray, alpha: float = 0.1, iterations: int = 100) -> \
        Tuple[ndarray, ndarray]:
    """
    Calculate optical flow using Horn-Schunck algorithm.

    :param frame1: First frame
    :param frame2: Second frame
    :param alpha: Regularization parameter
    :param iterations: Number of iterations
    :return: Tuple of (u, v) optical flow components
    """
    Ix, Iy, It = calculate_derivatives(frame1, frame2)

    u = zeros_like(frame1, dtype=float32)
    v = zeros_like(frame1, dtype=float32)

    for _ in range(iterations):
        u_avg = blur(u, (3, 3))
        v_avg = blur(v, (3, 3))

        numerator = Ix * u_avg + Iy * v_avg + It
        denominator = alpha ** 2 + Ix ** 2 + Iy ** 2

        u = u_avg - Ix * (numerator / denominator)
        v = v_avg - Iy * (numerator / denominator)

    return u, v


def visualize_optical_flow(frame: ndarray, u: ndarray, v: ndarray, step: int = 16) -> ndarray:
    """
    Visualize optical flow by drawing arrows on the frame.

    :param frame: Original frame
    :param u: Horizontal component of optical flow
    :param v: Vertical component of optical flow
    :param step: Step size for arrow grid
    :return: Frame with optical flow visualization
    """
    h, w = frame.shape[:2]
    y, x = mgrid[step / 2:h:step, step / 2:w:step].reshape(2, -1).astype(int)
    fx, fy = u[y, x], v[y, x]
    lines = vstack([x, y, x + fx, y + fy]).T.reshape(-1, 2, 2)
    lines = int32(lines)

    vis = cvtColor(frame, COLOR_GRAY2BGR)
    for (x1, y1), (x2, y2) in lines:
        line(vis, (x1, y1), (x2, y2), (0, 255, 0), 1)
        circle(vis, (x1, y1), 1, (0, 255, 0), -1)
    return vis


def main():
    cap = VideoCapture(0)  # Use default camera

    ret, prev_frame = cap.read()
    prev_gray = cvtColor(prev_frame, COLOR_BGR2GRAY)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cvtColor(frame, COLOR_BGR2GRAY)

        # Calculate optical flow
        u, v = horn_schunck_optical_flow(prev_gray, gray)

        # Visualize the optical flow
        vis = visualize_optical_flow(gray, u, v)

        imshow('Horn-Schunck Optical Flow', vis)

        # Exit if 'q' is pressed
        if waitKey(1) & 0xFF == ord('q'):
            break

        prev_gray = gray

    cap.release()
    destroyAllWindows()


if __name__ == "__main__":
    main()
