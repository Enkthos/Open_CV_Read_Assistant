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

# Gesture Control Application

## Deployment / Installation

1. Clone or download this repository
2. Open Command Prompt or Terminal as Administrator
3. Install the required libraries using the command above
4. Save the main code as `gesture_control.py` in the project folder
5. Run the application:

```bash
python gesture_control.py
```

## Usage Instructions

After running the script, the program starts in waiting mode and prints `"waiting.."`.

1. Press the hotkey **Ctrl + Alt + Cmd** (Ctrl + Alt + Windows key) to activate gesture control
2. The camera window titled "Image" will open
3. Show your right or left hand clearly to the webcam

### Available Gestures

- **Scroll Down**: Move index finger down while thumb is close to index finger
- **Scroll Up**: Move middle finger up while thumb is close to index finger
- **Play / Pause**: Spread pinky finger far from thumb (triggers toggle with beep sound)

### Exit Controls

- Press **Ctrl + Alt + Cmd** again to stop gesture mode (cmd is the win button in windows)
- Press **Spacebar** in the camera window to completely exit

## Tips for Best Performance

- Ensure good lighting on your hand
- Keep your hand 30–60 cm away from the webcam
- Avoid very fast movements for more accurate detection
- If the hotkey doesn't work, try changing it in the code to `<ctrl>+<alt>+h`

## Known Issues & Notes

- Hotkey using `<cmd>` (Windows key) can sometimes be unstable with pynput. Use `<ctrl>+<alt>+h` as backup if needed.
- Pinky detection uses landmark 18 (not the tip). This may be improved later.
- Volume control code is commented out and can be enabled easily.
- Zoom gestures are detected but not implemented yet.

## Future Enhancements

- Enable volume control using thumb-index distance
- Add actual zoom functionality
- Implement mouse cursor control
- Improve gesture smoothness and add filtering

## License

This project is open-source under the **MIT License**.
Built with [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/).