import cv2
import matplotlib.pyplot as plt

import cv2

def preprocess_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError(f"❌ Image not found at path: {image_path}")

    print("✅ Image loaded successfully")

    # Resize (VERY IMPORTANT for webcam)
    img = cv2.resize(img, (800, 600))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 🔥 Stronger noise reduction
    bfilter = cv2.bilateralFilter(gray, 13, 20, 20)

    # 🔥 Improve contrast
    gray = cv2.equalizeHist(gray)

    return img, img, gray, bfilter


def show_images(rgb, bfilter):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(rgb)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(bfilter, cmap='gray')
    plt.title("Processed Image")
    plt.axis('off')

    plt.tight_layout()
    plt.show()