import cv2
import imutils

def find_plate_contour(edged):
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:20]

    location = None

    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # 🔥 Allow 4–6 sides (not strict 4)
        if 4 <= len(approx) <= 6:
            x, y, w, h = cv2.boundingRect(approx)

            aspect_ratio = w / float(h)

            # 🔥 Plate-like shape filter
            if 2 < aspect_ratio < 6:
                location = approx
                break

    return location, contours