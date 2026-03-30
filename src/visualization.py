import cv2
import matplotlib.pyplot as plt

def draw_result(img, location, text):
    cv2.rectangle(
        img,
        tuple(location[0][0]),
        tuple(location[2][0]),
        (0, 255, 0),
        3
    )

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
        img,
        text,
        (location[0][0][0], location[1][0][1] + 50),
        font,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )

    return img


def show_final(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Final Output")
    plt.axis('off')
    plt.show()