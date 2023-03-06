from typing import Union
import numpy as np
import cv2
from PIL import Image
import os

def resize_save(path: Union[str, np.array], output_path: str, scale=512):
    if isinstance(path, str):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    else:
        img = path
    shape = img.shape
    w = shape[0]
    h = shape[1]
    img_resize = cv2.resize(img, (256, 256), interpolation = cv2.INTER_NEAREST)
    cv2.imwrite(output_path, img_resize)
    #image_tosave = Image.fromarray(img_resize[:,:, [2, 1, 0]].astype(np.uint8))
    #image_tosave.save(os.path.abspath(output_path), 'PNG')

    return output_path
