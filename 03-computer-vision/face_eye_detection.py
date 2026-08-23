# face_eye_detection.py
# Real-time Face and Eye Detection using OpenCV Haar Cascades

import cv2


def main():
    # Load OpenCV's built-in Haar Cascade pre-trained models
    face_cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    eye_cascade_path = cv2.data.haarcascades + "haarcascade_eye.xml"

    face_model = cv2.CascadeClassifier(face_cascade_path)
    eye_model = cv2.CascadeClassifier(eye_cascade_path)

    # Initialize webcam stream (0 = default camera)
    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Error: Could not open camera.")
        return

    print("Starting webcam... Press 'q' in the window to quit.")

    while True:
        ret, img = webcam.read()
        if not ret:
            print("Failed to capture image frame.")
            break

        # Convert to grayscale for feature detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in frame
        faces = face_model.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            # Draw green bounding box around face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                img,
                "Face",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

            # Region of Interest (ROI) for eyes inside detected face area
            gray_face = gray[y : y + h, x : x + w]
            color_face = img[y : y + h, x : x + w]

            eyes = eye_model.detectMultiScale(
                gray_face, scaleFactor=1.1, minNeighbors=10
            )

            for (xe, ye, we, he) in eyes:
                # Draw blue bounding box around eyes
                cv2.rectangle(
                    color_face, (xe, ye), (xe + we, ye + he), (255, 0, 0), 2
                )

        # Display real-time video feed
        cv2.imshow("Real-Time Face & Eye Detector", img)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
