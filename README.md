# Eyego Object Tracker

A modular Python application for real-time object tracking using OpenCV. Users can select an object in a live webcam feed with a bounding box and track it, with results displayed in real-time.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

### Prerequisites
- Python 3.6+ (tested with Python 3.10)
- A webcam connected to your system
- Windows, macOS, or Linux

### Setup
1. Clone the repository (if using GitHub):
   ```bash
   git clone https://github.com/MahmoudSalama7/eyego.git
   cd eyego

   Or navigate to D:\eyego if working locally.

Install dependencies:pip uninstall opencv-python
pip install -r requirements.txt



Usage

Run the application:cd D:\eyego
python -m src.main


In the "Object Tracker" window:
Select an Object: Click and drag from top-left to bottom-right to draw a red bounding box.
Start Tracking: Release the mouse to begin tracking (box turns green).
View Results: The live feed shows the tracked object with a green box and status text ("Tracking", "Tracking Lost", or "Invalid Tracker Output").
Exit: Press 'q' to quit.



Implementation Details

Modular Design:
src/tracker.py: Defines the ObjectTracker class, managing tracker initialization (CSRT or KCF), mouse-based bounding box selection, and tracking updates with error handling.
src/utils.py: Provides functions for webcam setup (setup_webcam) and frame processing (process_frame) to ensure compatibility (CV_8UC3 format).
src/main.py: Orchestrates the application, integrating webcam capture, tracker updates, and live display.


Tracking: Uses OpenCV's CSRT tracker for accuracy, with a fallback to KCF if CSRT is unavailable. The tracker is initialized with a user-selected bounding box and updated per frame.
Input/Output: Captures 640x480 video from the default webcam (index 0). Displays results in a window with a bounding box (red for selection, green for tracking) and status text.
Error Handling: Validates bounding box dimensions to prevent negative/zero sizes, handles tracker initialization/update failures, and ensures frame format compatibility to avoid OpenCV errors (e.g., cv::dft, cv::setSize).

Deployment
Local Deployment

Ensure a webcam is connected.
Follow the Installation and Usage steps.
If the webcam fails, edit src/utils.py to change device_index (e.g., setup_webcam(device_index=1)).

Packaging

Create an executable with PyInstaller:pip install pyinstaller
pyinstaller --onefile src/main.py

The executable will be in the dist folder.

Server Deployment (Optional)

Install dependencies on the target machine.
Copy the repository files.
Run python -m src.main.
For remote access, integrate with a web framework like Flask to stream the video feed (not included).

Project Structure
eyego/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── tracker.py
│   ├── utils.py
├── requirements.txt
├── README.md
├── .gitignore

License
This project is licensed under the MIT License - see the LICENSE file for details.```
