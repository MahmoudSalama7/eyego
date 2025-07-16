import cv2

class ObjectTracker:
    def __init__(self, tracker_type="CSRT"):
        """Initialize the tracker with the specified type (CSRT or KCF)."""
        self.tracker = None
        self.tracking = False
        self.bbox = None
        self.init_tracker(tracker_type)

    def init_tracker(self, tracker_type):
        """Initialize the tracker, with fallback to KCF if CSRT fails."""
        try:
            if tracker_type == "CSRT":
                self.tracker = cv2.legacy.TrackerCSRT_create()
            elif tracker_type == "KCF":
                self.tracker = cv2.legacy.TrackerKCF_create()
            else:
                raise ValueError("Unsupported tracker type. Use 'CSRT' or 'KCF'.")
        except AttributeError:
            if tracker_type == "CSRT":
                print("CSRT tracker not found. Falling back to KCF.")
                self.init_tracker("KCF")
            else:
                print("Error: No suitable tracker found. Ensure opencv-contrib-python is installed.")
                self.tracker = None

    def select_object(self, event, x, y, flags, param):
        """Handle mouse events for bounding box selection."""
        frame = param["frame"]
        if event == cv2.EVENT_LBUTTONDOWN:
            self.bbox = [x, y, 0, 0]
        elif event == cv2.EVENT_MOUSEMOVE and self.bbox is not None:
            self.bbox[2] = x - self.bbox[0]
            self.bbox[3] = y - self.bbox[1]
        elif event == cv2.EVENT_LBUTTONUP:
            self.bbox[2] = x - self.bbox[0]
            self.bbox[3] = y - self.bbox[1]
            if self.bbox[2] <= 0 or self.bbox[3] <= 0:
                print("Error: Invalid bounding box dimensions. Please select a valid region.")
                self.bbox = None
                return
            self.tracking = True
            try:
                self.tracker.init(frame, tuple(self.bbox))
            except Exception as e:
                print(f"Error initializing tracker: {e}")
                self.tracking = False
                self.bbox = None

    def update(self, frame):
        """Update tracker and draw bounding box on the frame."""
        display_frame = frame.copy()
        if self.tracking and self.bbox is not None:
            try:
                success, new_bbox = self.tracker.update(frame)
                if success:
                    p1 = (int(new_bbox[0]), int(new_bbox[1]))
                    p2 = (int(new_bbox[0] + new_bbox[2]), int(new_bbox[1] + new_bbox[3]))
                    if new_bbox[2] > 0 and new_bbox[3] > 0:
                        cv2.rectangle(display_frame, p1, p2, (0, 255, 0), 2)
                        cv2.putText(display_frame, "Tracking", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    else:
                        cv2.putText(display_frame, "Invalid Tracker Output", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    cv2.putText(display_frame, "Tracking Lost", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            except Exception as e:
                print(f"Error during tracking: {e}")
                self.tracking = False
                self.bbox = None
        elif self.bbox is not None:
            p1 = (self.bbox[0], self.bbox[1])
            p2 = (self.bbox[0] + self.bbox[2], self.bbox[1] + self.bbox[3])
            if self.bbox[2] > 0 and self.bbox[3] > 0:
                cv2.rectangle(display_frame, p1, p2, (0, 0, 255), 2)
                cv2.putText(display_frame, "Selecting", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        return display_frame