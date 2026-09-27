import cv2
import os
import numpy as np
from sklearn import linear_model  
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 1. Load Training Dataset (Folders 1 to 9)
x = np.empty((0, 256))
y = np.array([])

for f in range(1, 10):
    folder_path = r"F:\AIO Leran\ML projects\J2\pelak\{}".format(f)
    if not os.path.exists(folder_path):
        continue
        
    files = os.listdir(folder_path)
    for file in files:
        image_path = os.path.join(folder_path, file)
        im = cv2.imread(image_path, 0) # Load directly as grayscale
        
        if im is None:
            continue
        
        ret, im_thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY_INV)
        im2 = cv2.resize(im_thresh, (8, 32))
        im4 = im2.flatten()
        
        x = np.append(x, [im4], axis=0)
        y = np.append(y, f)

# 2. Train Model
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = linear_model.LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print(f"Model Accuracy: {model.score(X_test, y_test) * 100:.2f}%")

# 3. Load & Preprocess License Plate Image
plate_im0 = cv2.imread(r"F:\AIO Leran\ML projects\J2\pelak\car-number-plate.jpg", 0)

if plate_im0 is None:
    print("Error loading license plate image!")
else:
    height, width = plate_im0.shape
    plate_im0_cropped = plate_im0[5:height-5, 5:width-5]
    crop_height, crop_width = plate_im0_cropped.shape

    # Binary Thresholding
    ret, plate_im0_thresh = cv2.threshold(plate_im0_cropped, 127, 255, cv2.THRESH_BINARY_INV)

    # Calculate Vertical Projection Profile
    s = crop_height - (np.sum(plate_im0_thresh, axis=0, keepdims=True) / 255)

    # Display Projection Plot
    plt.close()
    plt.figure(figsize=(10, 4))
    plt.plot(s[0])
    plt.title("Vertical Projection Profile")
    plt.xlabel("Column (X-axis)")
    plt.ylabel("Value")
    plt.show()

    # 4. Segment Characters and Predict
    plate_color = cv2.cvtColor(plate_im0_cropped, cv2.COLOR_GRAY2BGR)
    
    xi = 0
    xi1 = 0
    in_character = False
    x1 = np.empty((0, 256))

    for i in s[0]:
        # Values under threshold signify gap/background
        if i < 20:
            plate_color = cv2.line(plate_color, (xi, 0), (xi, crop_height), (0, 0, 255), 1)

            if in_character:
                xi2 = xi
                in_character = False
                img1 = plate_im0_thresh[:, xi1:xi2]

                # Ensure crop has valid dimension before resizing
                if img1.shape[1] > 0:
                    cv2.imshow('Cropped Character', img1)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    im2 = cv2.resize(img1, (8, 32))
                    im4 = im2.flatten()
                    single_char = np.array([im4])
                    
                    result = model.predict(single_char)
                    print("Predicted label:", int(result[0]))

                    x1 = np.append(x1, [im4], axis=0)
        else:
            if not in_character:
                xi1 = xi
                in_character = True

        xi += 1

    cv2.imshow('Divided License Plate', plate_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
