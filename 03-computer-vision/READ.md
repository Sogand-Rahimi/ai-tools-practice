# Real-Time Face and Eye Detection

A Computer Vision module using OpenCV to demonstrate fundamental image processing operations and real-time object detection via Haar Feature-based Cascade Classifiers.

---

## Key Features

* **Image Manipulation Concepts:** BGR to RGB color transformations, image cropping, resizing, Gaussian blurring, thresholding, and geometric drawing.
* **Haar Cascade Classifiers:** Uses pre-trained feature cascades (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) for face and eye tracking.
* **Region of Interest (ROI) Optimization:** Constrains eye detection strictly inside detected facial bounding boxes to reduce false positives.

---

## Prerequisites

```bash
pip install opencv-python matplotlib
