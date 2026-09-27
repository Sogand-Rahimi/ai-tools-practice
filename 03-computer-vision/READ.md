Markdown
# 👁️ Computer Vision Projects

A collection of Computer Vision modules demonstrating real-time object detection, image processing operations, and machine learning-based character recognition using OpenCV and Scikit-Learn.

---

## 📸 1. Real-Time Face and Eye Detection (`face_eye_detection.py`)

Uses OpenCV and pre-trained Haar Feature-based Cascade Classifiers for real-time tracking in video streams and images.

### Key Features
* **Image Manipulation Concepts:** BGR to RGB color transformations, image cropping, resizing, Gaussian blurring, thresholding, and geometric drawing.
* **Haar Cascade Classifiers:** Uses pre-trained feature cascades (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) for face and eye tracking.
* **Region of Interest (ROI) Optimization:** Constrains eye detection strictly inside detected facial bounding boxes to reduce false positives.

---

## 🚗 2. License Plate Character Recognition (`license_plate_recognition.py`)

An end-to-end pipeline that isolates license plate characters using image processing and classifies them with machine learning.

### Key Features
* **Dataset Processing:** Loads digit samples from folders (`1` through `9`), resizes images to `(8, 32)`, and flattens pixel matrices into feature vectors.
* **Model Training:** Trains a `LogisticRegression` classifier on grayscale pixel values.
* **Segmentation:** Applies binary inversion thresholding (`cv2.THRESH_BINARY_INV`) and vertical projection profiling to locate gaps between numbers.
* **Prediction:** Isolates each character segment and predicts its numerical value in real time.

---

## 🛠️ Prerequisites & Installation

Ensure you have Python 3.x installed along with the required dependencies:

```bash
pip install opencv-python scikit-learn matplotlib numpy
🚀 Usage
Navigate to the project directory:

Bash
cd 03-computer-vision
Run either script:

Bash
# For Face & Eye Detection
python face_eye_detection.py

# For License Plate Recognition
python license_plate_recognition.py
(Press 'q' while an image or video window is active to exit.)


---

### Steps to Update on GitHub:
1. Open **`03-computer-vision/READ.md`** on GitHub.
2. Click the **pencil icon** (Edit this file).
3. Paste the entire block above into the editor.
4. Click **"Commit changes..."** at the top right to save.
