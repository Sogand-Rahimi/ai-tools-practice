# Face Recognition (Photo + Webcam)

A face recognition tool built with the `face_recognition` library and OpenCV. It learns one known face from a reference photo, then recognizes it in a photo or in a live webcam stream.

---

## Key Features

* **Face Encoding:** Converts a reference photo into a 128-number face encoding that is used to compare faces.
* **Multi-Face Recognition:** Works with any number of faces in the frame. Each face is detected and checked separately, and gets its own box and label.
* **Live Webcam Mode:** Draws a box around every face and labels it with the known name (green) or "Unknown" (red).
* **Photo Mode:** Compares the faces in a photo with the known face, without needing a webcam.

---

## Prerequisites

```bash
pip install face_recognition opencv-python "setuptools<81"
```

Note: `face_recognition` depends on `dlib`, which can be hard to build on Windows. On newer Python versions, `setuptools<81` is needed because the library still uses `pkg_resources`.

## Setup

Put a clear photo of the person you want to recognize in the same folder and name it `img.jpg` (or change `KNOWN_IMAGE_PATH` at the top of the script). Change `KNOWN_NAME` to the person's name.

## Usage

Live webcam (press `q` to quit):

```bash
python face_recognition_webcam.py
```

Compare a photo:

```bash
python face_recognition_webcam.py image_test.jpg
```

## Example Output (photo mode)

```
Face 1: match
Face 2: no match
```
