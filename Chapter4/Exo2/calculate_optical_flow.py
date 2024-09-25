from typing import Tuple

from cv2 import add, imshow, waitKey, line, calcOpticalFlowPyrLK, destroyAllWindows, cvtColor, TERM_CRITERIA_EPS, \
    COLOR_BGR2GRAY, goodFeaturesToTrack, TERM_CRITERIA_COUNT, circle, VideoCapture
from numpy import random, ndarray, zeros_like


def calculate_optical_flow(prev_frame: ndarray, curr_frame: ndarray, prev_points: ndarray) -> Tuple[
    ndarray, ndarray, ndarray]:
    """
    Calculate optical flow using Lucas-Kanade algorithm.

    :param prev_frame: Previous grayscale frame
    :param curr_frame: Current grayscale frame
    :param prev_points: Previous points to track
    :return: Tuple of (next_points, status, error)
    """
    lk_params = dict(winSize=(15, 15),
                     maxLevel=2,
                     criteria=(TERM_CRITERIA_EPS | TERM_CRITERIA_COUNT, 10, 0.03))

    next_points, status, error = calcOpticalFlowPyrLK(prev_frame, curr_frame, prev_points, None, **lk_params)
    return next_points, status, error


def visualize_optical_flow(frame: ndarray, prev_points: ndarray, next_points: ndarray,
                           status: ndarray) -> ndarray:
    """
    Visualize optical flow by drawing arrows on the frame.

    :param frame: Current frame to draw on
    :param prev_points: Previous points
    :param next_points: Next points
    :param status: Status array from calcOpticalFlowPyrLK
    :return: Frame with optical flow visualization
    """
    mask = zeros_like(frame)

    # Filter out points where the flow wasn't found
    good_new = next_points[status == 1]
    good_old = prev_points[status == 1]

    # Draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
        frame = circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)

    img = add(frame, mask)
    return img


def main():
    cap = VideoCapture(0)  # Use default camera

    # Parameters for ShiTomasi corner detection
    feature_params = dict(maxCorners=100,
                          qualityLevel=0.3,
                          minDistance=7,
                          blockSize=7)

    # Read the first frame
    ret, old_frame = cap.read()
    old_gray = cvtColor(old_frame, COLOR_BGR2GRAY)

    # Create some random colors
    color = random.randint(0, 255, (100, 3))

    # Find initial corners
    p0 = goodFeaturesToTrack(old_gray, mask=None, **feature_params)

    # Create a mask image for drawing purposes
    mask = zeros_like(old_frame)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_gray = cvtColor(frame, COLOR_BGR2GRAY)

        # Calculate optical flow
        p1, st, err = calculate_optical_flow(old_gray, frame_gray, p0)

        # Visualize the optical flow
        img = visualize_optical_flow(frame, p0, p1, st)

        imshow('Optical Flow', img)

        # Exit if 'q' is pressed
        if waitKey(1) & 0xFF == ord('q'):
            break

        # Update the previous frame and points
        old_gray = frame_gray.copy()
        p0 = p1.reshape(-1, 1, 2)

    cap.release()
    destroyAllWindows()


if __name__ == "__main__":
    main()
