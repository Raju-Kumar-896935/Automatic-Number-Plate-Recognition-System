import cv2
import matplotlib.pyplot as plt

def detect_edges(bfilter):
    # Auto thresholds (better than fixed 30,200)
    v = bfilter.mean()

    lower = int(max(0, 0.66 * v))
    upper = int(min(255, 1.33 * v))

    edged = cv2.Canny(bfilter, lower, upper)
    return edged


def show_edges(edged):
    plt.figure(figsize=(6,6))   # ✅ important
    plt.imshow(edged, cmap='gray')
    plt.title("Edge Detection")
    plt.axis('off')
    plt.show()