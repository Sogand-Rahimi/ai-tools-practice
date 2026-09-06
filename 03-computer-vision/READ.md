Markdown
# Real-Time Face and Eye Detection

A Computer Vision module using OpenCV to demonstrate fundamental image processing operations and real-time object detection via Haar Feature-based Cascade Classifiers.

---

## Key Features

* **Image Manipulation Concepts:** BGR to RGB color transformations, image cropping, resizing, Gaussian blurring, thresholding, and geometric drawing.
* **Haar Cascade Classifiers:** Uses pre-trained feature cascades (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) for face and eye tracking.
* **Region of Interest (ROI) Optimization:** Constrains eye detection strictly inside detected facial bounding boxes to reduce false positives.

---

## Prerequisites & Installation

Make sure you have Python 3.x installed along with the required libraries:

```bash
pip install opencv-python matplotlib
🚀 Usage
Navigate to the project directory:

Bash
cd 03_face_eye_detection
Run the detection script:

Bash
python main.py
Press 'q' on your keyboard while the video window is active to exit the stream.

💡 How It Works
Grayscale Conversion: Input frames are converted to grayscale to optimize detection speed.

Face Detection: The Haar Cascade algorithm scans the frame for facial structures and draws a primary bounding box around each detected face.

ROI Extraction: The area inside the face bounding box is extracted as a Region of Interest (ROI).

Eye Tracking: Eye classifiers run exclusively within the ROI, preventing false triggers from background noise.


<FollowUp label="Would you like to check or complete the READMEs for folders 01 or 02 as well?" query="Can you help me check and complete the README files for my 01 and 02 practice folders?"/>
