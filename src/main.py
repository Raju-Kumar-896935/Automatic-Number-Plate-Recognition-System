import sys
import os
import cv2
import numpy as np
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # src/
PROJECT_ROOT = os.path.dirname(BASE_DIR)

IMAGE_DIR = os.path.join(PROJECT_ROOT, "images")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

sys.path.append(BASE_DIR)

from preprocessing import preprocess_image, show_images
from edge_detection import detect_edges, show_edges
from contour_detection import find_plate_contour
from masking import extract_plate, show_plate
from ocr import read_text, get_text
from visualization import draw_result, show_final
from storage import clean_plate_text, save_to_csv

# 🎥 Start Camera
cap = cv2.VideoCapture(0)

print("📷 Press 'c' to capture | 'q' to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Camera not working")
        break

    # 🔥 Fix 4 (better frame)
    frame = cv2.resize(frame, (800, 600))
    frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=30)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    frame = cv2.filter2D(frame, -1, kernel)

    cv2.imshow("Camera - Press C to Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    # 📸 Capture
    if key == ord('c'):
        print("📸 Capturing... hold still")
        cv2.waitKey(500)

        ret, frame = cap.read()
        frame = cv2.resize(frame, (800, 600))

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = os.path.join(IMAGE_DIR, f"capture_{timestamp}.jpg")

        cv2.imwrite(image_path, frame)
        print(f"📸 Captured: {image_path}")

        # ==============================
        # 🔥 STEP-BY-STEP PIPELINE VIEW
        # ==============================

        # Step 1: Preprocessing
        img, rgb, gray, bfilter = preprocess_image(image_path)
        show_images(rgb, bfilter)

        # Step 2: Edge Detection
        edged = detect_edges(bfilter)
        show_edges(edged)

        # Step 3: Contour Detection
        location, contours = find_plate_contour(edged)
        print("📍 Plate Location:", location)

        # Step 4: Masking + OCR
        if location is not None:
            new_image, cropped_image = extract_plate(img, gray, location)
            show_plate(new_image, cropped_image)

            # Save cropped plate
            plate_path = os.path.join(OUTPUT_DIR, f"plate_{timestamp}.jpg")
            cv2.imwrite(plate_path, cropped_image)

            # OCR
            result = read_text(cropped_image)
            text = get_text(result)
            cleaned_text = clean_plate_text(text)

            print("🚗 Plate:", cleaned_text)

            # Save CSV
            save_to_csv(cleaned_text, OUTPUT_DIR)

            print("✅ Saved to CSV")

            # Step 5: Final Output
            final_img = draw_result(img.copy(), location, cleaned_text)
            show_final(final_img)

        else:
            print("❌ Plate not detected")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()