import numpy as np
import cv2
from PIL import Image
import os
from resize import resize_save

def create_canny(source_path: str, target_path: str, sigma=0.53):
    image = cv2.imread(source_path, 0)
    if sigma is None:
        edges = cv2.Canny(image, 350, 350)
    else:
        blur = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
        v = np.median(blur)
        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edges = cv2.Canny(blur, lower, upper)

    image_todraw = np.array(edges)
    image_todraw = np.reshape(image_todraw, image.shape)

    image_tosave = Image.fromarray(image_todraw.astype(np.uint8))
    image_tosave.save(os.path.abspath(target_path), 'PNG')
    return target_path