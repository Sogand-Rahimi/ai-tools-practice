"""
Face Recognition (Photo + Webcam)
---------------------------------
Learns one known face from a reference photo, then recognizes it in a photo
or in a live webcam stream. Every detected face gets a box and a label
("Sogand" or "Unknown"). It works for any number of faces in the frame:
each face is checked separately.

Usage:
    python face_recognition_webcam.py               # live webcam
    python face_recognition_webcam.py image_test.jpg  # compare a photo
"""

import sys

import cv2
import face_recognition as fr

# --- Configuration ---
KNOWN_IMAGE_PATH = "img.jpg"
KNOWN_NAME = "Sogand"
CAMERA_INDEX = 0
FRAME_SIZE = (600, 400)  # (width, height)

COLOR_BLUE = (255, 0, 0)    # OpenCV uses BGR order
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)


def load_known_encoding(path):
    """Return the face encoding of the first face found in the reference photo."""
    image = fr.load_image_file(path)
    encodings = fr.face_encodings(image)
    if not encodings:
        raise ValueError(f"No face found in {path}")
    return encodings[0]


def label_faces(frame, known_encoding):
    """Draw a box and a name label on every face in a BGR frame."""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # face_recognition needs RGB
    locations = fr.face_locations(rgb)
    encodings = fr.face_encodings(rgb, locations)

    for (top, right, bottom, left), encoding in zip(locations, encodings):
        is_match = fr.compare_faces([known_encoding], encoding)[0]
        name = KNOWN_NAME if is_match else "Unknown"
        color = COLOR_GREEN if is_match else COLOR_RED

        cv2.rectangle(frame, (left, top), (right, bottom), COLOR_BLUE, 3)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_COMPLEX, 0.9, color, 2)
    return frame


def compare_photo(path, known_encoding):
    """Print whether each face in a photo matches the known face."""
    image = fr.load_image_file(path)
    encodings = fr.face_encodings(image)

    if not encodings:
        print("No face found in the photo.")
        return

    for number, encoding in enumerate(encodings, start=1):
        is_match = fr.compare_faces([known_encoding], encoding)[0]
        print(f"Face {number}: {'match' if is_match else 'no match'}")


def run_webcam(known_encoding):
    """Show the webcam stream with recognized faces. Press 'q' to quit."""
    webcam = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    if not webcam.isOpened():
        print("Error: could not open webcam.")
        return

    try:
        while True:
            ret, frame = webcam.read()
            if not ret:
                break

            frame = cv2.resize(frame, FRAME_SIZE)
            frame = label_faces(frame, known_encoding)
            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        webcam.release()
        cv2.destroyAllWindows()


def main():
    known_encoding = load_known_encoding(KNOWN_IMAGE_PATH)

    if len(sys.argv) > 1:
        compare_photo(sys.argv[1], known_encoding)
    else:
        run_webcam(known_encoding)


if __name__ == "__main__":
    main()
