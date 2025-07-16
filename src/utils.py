import cv2

def setup_webcam(device_index=0, width=640, height=480):
    """Set up the webcam with specified resolution."""
    cap = cv2.VideoCapture(device_index)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def process_frame(frame):
    """Ensure frame is in correct format (BGR, CV_8UC3)."""
    return cv2.convertScaleAbs(frame)