Markdown

# Face-Tracking Mouse Control

A Computer Vision automation tool using OpenCV and PyAutoGUI to move the mouse cursor based on the position of your face relative to a defined "safe zone" on screen.

---

## Key Features

* **Real-Time Face & Eye Detection:** Uses Haar Cascade Classifiers (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) to detect the user's face and eyes from a live webcam feed.
* **Directional Mouse Control:** When the detected face crosses the boundary of a central safe zone, the mouse cursor moves in that direction — the farther past the boundary, the faster the movement.
* **Visual Feedback:** The safe-zone rectangle turns red whenever the face is triggering a mouse movement, and green boxes are drawn around the detected face and eyes.

---

## Prerequisites

```bash
pip install opencv-python pyautogui

```

Usage
Bash

python mouse_control.py


Press `q` while the webcam window is focused to quit.
