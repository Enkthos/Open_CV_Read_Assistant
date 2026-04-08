# Hand Gesture Control System

A real-time hand gesture recognition application that allows you to control your computer (scrolling and media playback [TODO]) using simple hand movements captured by your webcam.

Built with **MediaPipe** for hand detection and **OpenCV** for camera handling.

## Features

- Scroll Up and Scroll Down using index and middle finger gestures
- Play / Pause media with pinky finger gesture
- Global hotkey to start/stop gesture control
- Real-time hand landmark visualization with circles and lines
- Audio feedback with beeps
- Simple gesture-based control

## Tech Stack

- **MediaPipe** – Hand landmark detection
- **OpenCV** – Webcam access and image display
- **pynput** – Global hotkey support
- **keyboard** – Keyboard input simulation
- **NumPy** – Distance calculations
- **Pycaw** – System volume control (currently commented)

## Requirements

### Python Version
Python 3.9 - 3.11 (64-bit) recommended

### Required Libraries

Install all dependencies with this single command:

```bash
pip install mediapipe opencv-python pycaw comtypes keyboard pynput numpy