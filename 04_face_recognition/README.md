Markdown
# AI Tools Practice

A collection of lightweight Python tools and scripts for experimenting with computer vision, machine learning, and AI libraries.

---

## 📁 Projects & Tools

### 1. Face Detection & Recognition Tool
A computer vision script built using `face_recognition` and `OpenCV` to detect face boundaries and compare facial encodings between images.

#### Features
* **Face Detection:** Identifies facial bounding box coordinates and renders them using OpenCV (`(Left, Top)` to `(Right, Bottom)` mapping).
* **Face Encoding & Matching:** Generates 128-dimensional facial embeddings to compute feature similarity and verify identity across test images.
* **Safe Configuration:** Uses placeholder local paths to prevent private assets from being tracked in version control.

---

## 🛠️ Environment & Prerequisites

* **Python:** 3.12
* **OS:** Windows / Linux / macOS
* **Dependencies:** `dlib` (requires Visual Studio C++ Build Tools on Windows), `cmake`, `opencv-python`, `face_recognition`, `numpy`

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai-tools-practice.git](https://github.com/YOUR_USERNAME/ai-tools-practice.git)
   cd ai-tools-practice
Install required packages:

Bash
pip install cmake
pip install opencv-python numpy face_recognition
🚀 Usage
Running 04_face_recognition
Navigate to the project directory:

Bash
cd 04_face_recognition
Open main.py and set your local image paths:

Python
KNOWN_IMAGE_PATH = "reference.jpg"
TEST_IMAGE_PATH = "test.jpg"
Run the script:

Bash
python main.py
