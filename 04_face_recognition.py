import cv2
import face_recognition as fr

# ==========================================
# Configurations & File Paths
# ==========================================
# Replace these with your local image paths before running
KNOWN_IMAGE_PATH = "reference.jpg"
TEST_IMAGE_PATH = "test.jpg"


def detect_and_display(image_path):
    """Loads an image, detects faces, and displays bounding boxes using OpenCV."""
    image = fr.load_image_file(image_path)
    locations = fr.face_locations(image)

    # Convert RGB (face_recognition format) to BGR (OpenCV format)
    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if locations:
        # Unpack coordinates for the first detected face: (Top, Right, Bottom, Left)
        top, right, bottom, left = locations[0]
        cv2.rectangle(bgr_image, (left, top), (right, bottom), (255, 0, 0), 5)

    resized_image = cv2.resize(bgr_image, (400, 600))

    cv2.imshow("Detected Face", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def match_faces(known_path, test_path, tolerance=0.6):
    """Encodes two face images and compares them for a match."""
    known_image = fr.load_image_file(known_path)
    test_image = fr.load_image_file(test_path)

    # Extract 128-d face encodings
    known_encodings = fr.face_encodings(known_image)
    test_encodings = fr.face_encodings(test_image)

    if not known_encodings or not test_encodings:
        print("[!] Warning: Could not detect a face in one of the images.")
        return False

    # Compare the extracted encodings
    results = fr.compare_faces([known_encodings[0]], test_encodings[0], tolerance=tolerance)
    return results[0]


def main():
    print("--> Step 1: Detecting and drawing face bounding box...")
    detect_and_display(KNOWN_IMAGE_PATH)

    print("--> Step 2: Comparing face encodings...")
    is_match = match_faces(KNOWN_IMAGE_PATH, TEST_IMAGE_PATH)

    if is_match:
        print("\n[+] Result: Match Found! (True)")
    else:
        print("\n[-] Result: No Match. (False)")


if __name__ == "__main__":
    main()
