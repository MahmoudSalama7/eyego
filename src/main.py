import cv2
from src.tracker import ObjectTracker
from src.utils import setup_webcam, process_frame

def main():
    # Initialize tracker
    tracker = ObjectTracker(tracker_type="CSRT")
    if tracker.tracker is None:
        return

    # Set up webcam
    cap = setup_webcam(device_index=0, width=640, height=480)
    if cap is None:
        return

    # Create window and set mouse callback
    cv2.namedWindow("Object Tracker")
    cv2.setMouseCallback("Object Tracker", tracker.select_object, param={"frame": None})

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Process frame
        frame = process_frame(frame)

        # Update mouse callback frame
        cv2.setMouseCallback("Object Tracker", tracker.select_object, param={"frame": frame})

        # Update tracker and get display frame
        display_frame = tracker.update(frame)

        # Display the frame
        cv2.imshow("Object Tracker", display_frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()