import numpy as np
from PIL import Image
import pytesseract
import cv2
from util import *


def ocr(image):
    recognition_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    deskewed = deskew(recognition_image)
    grayed = get_grayscale(deskewed)
    thresholded = thresholding(grayed)

    recognition_image = thresholded

    print(pytesseract.image_to_string(recognition_image))

    # https://medium.com/@jaafarbenabderrazak.info/ocr-with-tesseract-opencv-and-python-d2c4ec097866
    # for i in range(1,13):
    #     custom_config = f'--psm {i}'
    #     print(f"--------- Using psm {i}")
    #     try:
    #         print(pytesseract.image_to_string(recognition_image, config=custom_config))
    #     except:
    #         pass
    #     finally:
    #         pass



def main():
    main_page = Image.open("mainPage.png")

    startX = 30
    startY = 80
    width = 300
    height = 180
    stats_box = (startX,startY,startX + width, startY + height)
    stats = main_page.crop(box=stats_box)

    print("**** OCR the whole page in one go")
    ocr(main_page)
    print("**** OCR only stats page")
    ocr(stats)


main()
