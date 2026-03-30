import easyocr

def read_text(cropped_image):
    reader = easyocr.Reader(['en'], gpu=False)

    result = reader.readtext(cropped_image, detail=1, paragraph=False)

    return result


def get_text(result):
    texts = [res[-2] for res in result]
    return " ".join(texts)