import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_plate(img, gray, location):
    mask = np.zeros(gray.shape, np.uint8)

    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    (x, y) = np.where(mask == 255)

    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))

    cropped_image = gray[x1:x2+1, y1:y2+1]

    # 🔥 IMPROVEMENTS FOR OCR
    cropped_image = cv2.resize(cropped_image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cropped_image = cv2.GaussianBlur(cropped_image, (5,5), 0)
    _, cropped_image = cv2.threshold(cropped_image, 120, 255, cv2.THRESH_BINARY)

    return new_image, cropped_image


def show_plate(new_image, cropped_image):
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    plt.title("Masked Image")
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(cropped_image, cmap='gray')
    plt.title("Cropped Plate (Enhanced)")
    plt.axis('off')

    plt.show()