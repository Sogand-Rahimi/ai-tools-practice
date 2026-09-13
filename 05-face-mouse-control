"""
Face-Tracking Mouse Control
-----------------------------
Moves the mouse cursor based on face position relative to a central
"safe zone". Moving your face outside the zone nudges the mouse in
that direction — the farther out, the faster it moves.
"""

import cv2
import pyautogui

# --- Configuration ---
CAMERA_INDEX = 0
ZONE_LEFT, ZONE_TOP = 200, 80
ZONE_RIGHT, ZONE_BOTTOM = 450, 350
SPEED_DIVISOR = 2  # lower = faster mouse movement

COLOR_GREEN = (0, 250, 0)
COLOR_WHITE = (250, 250, 250)
COLOR_RED = (0, 0, 250)

FACE_CASCADE_PATH = "haarcascade_frontalface_default.xml"
EYE_CASCADE_PATH = "haarcascade_eye.xml"


def load_models():
    face_model = cv2.CascadeClassifier(FACE_CASCADE_PATH)
    eye_model = cv2.CascadeClassifier(EYE_CASCADE_PATH)
    return face_model, eye_model


def compute_mouse_position(x, y, x2, y2, mouse_x, mouse_y):
    """Adjust mouse position based on how far the face crosses the safe zone."""
    box_color = COLOR_WHITE

    if x < ZONE_LEFT:
        box_color = COLOR_RED
        mouse_x -= (ZONE_LEFT - x) // SPEED_DIVISOR

    if x2 > ZONE_RIGHT:
        box_color = COLOR_RED
        mouse_x += (x2 - ZONE_RIGHT) // SPEED_DIVISOR

    if y < ZONE_TOP:
        box_color = COLOR_RED
        mouse_y -= (ZONE_TOP - y) // SPEED_DIVISOR

    if y2 > ZONE_BOTTOM:
        box_color = COLOR_RED
        mouse_y += (y2 - ZONE_BOTTOM) // SPEED_DIVISOR

    return mouse_x, mouse_y, box_color


def process_frame(frame, face_model, eye_model):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    output = frame.copy()

    if len(faces) == 0:
        return output

    x, y, w, h = faces[0]
    x2, y2 = x + w, y + h

    cv2.rectangle(output, (x, y), (x2, y2), COLOR_GREEN, 3)

    mouse_x, mouse_y = pyautogui.position()
    mouse_x, mouse_y, box_color = compute_mouse_position(x, y, x2, y2, mouse_x, mouse_y)
    pyautogui.moveTo(mouse_x, mouse_y)

    cv2.rectangle(output, (ZONE_LEFT, ZONE_TOP), (ZONE_RIGHT, ZONE_BOTTOM), box_color, 3)

    gray_face = gray[y:y2, x:x2]
    eyes = eye_model.detectMultiScale(gray_face, scaleFactor=1.1, minNeighbors=5)
    for (xe, ye, ew, eh) in eyes:
        cv2.rectangle(output, (xe + x, ye + y), (xe + x + ew, ye + y + eh), COLOR_GREEN, 3)

    return output


def main():
    face_model, eye_model = load_models()
    webcam = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

    if not webcam.isOpened():
        print("Error: could not open webcam.")
        return

    try:
        while True:
            ret, frame = webcam.read()
            if not ret:
                continue

            frame = cv2.flip(frame, 1)
            output = process_frame(frame, face_model, eye_model)
            cv2.imshow("Face Detection", output)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        webcam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
