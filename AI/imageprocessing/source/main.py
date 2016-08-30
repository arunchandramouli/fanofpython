# import all th required libraries for processing

import cv2
import numpy as np
from matplotlib import pyplot as plt
import logging


logging.basicConfig(level=logging.INFO)

def image_processing(parentImage,featureImage):

    img = cv2.imread(parentImage,0)
    img2 = img.copy()
    template = cv2.imread(featureImage,0)
    w, h = template.shape[::-1]

    # All the 6 methods for comparison in a list
    '''methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']'''

    methods = ['cv2.TM_CCOEFF']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        try:

            res = cv2.matchTemplate(img,template,method)
            
        except Exception:
            #raise Exception(" No match found on comparison with the parent image!")
            return False

    return True