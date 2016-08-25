
import base64
import re
from copy import deepcopy
from io import BytesIO

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from helpers import indexToColor


class ClairesImage():
    __divider = 1

    def __init__(self, input, type):
        if type == 'base64':
            base64String = re.sub('^data:image/.+;base64,',
                                  '', input).decode('base64')
            self.__image = Image.open(BytesIO(base64String))
            self.__backupImage = deepcopy(self.__image)
            return
        else:
            raise ValueError('Cutter: This type is not supported')

    def getImage(self):
        return self.__image

    def getDivider(self):
        return self.__divider

    # Shrinks image, divider is stored in the object. Can be blown up to
    # original proportions by restoreImage
    def shrinkImage(self, divider):
        # divider is always 5 for now
        # todo: make divider dynamic
        divider = 5
        image = self.__image
        self.__divider *= divider

        self.__image.thumbnail(
            (image.size[0] / divider, image.size[1] / divider), Image.ANTIALIAS)

    def restoreImage(self):
        self.__image = deepcopy(self.__backupImage)

    def getNumpyArray(self):
        image = self.__image
        return np.array(image.getdata()).reshape(image.size[1], image.size[0], 3) / 255.

    def getOpenCV(self):
        image = cv2.cvtColor(np.array(self.__image), cv2.COLOR_RGB2BGR)
        return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

    def getOpenCVBinary(self):
        image = self.getNumpyArray()
        image[image > 0.7] = 255
        image[image <= 0.7] = 0
        image = np.uint8(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        image = cv2.adaptiveThreshold(
            image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        # Close wholes
        kernel = np.ones((2, 2), np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=3)
        return image

    def getOpenCVBW(self):
        image = self.getOpenCV()
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def getBase64(self):
        return self.__base64

    def whiteToBlack(self):
        image = self.__image
        for i in xrange(image.shape[0]):
            for j in xrange(image.shape[1]):
                if image[i, j, 0] == image[i, j, 1] == image[i, j, 2] == 1:
                    image[i, j] = 0
        self.__image = image

    def getColor(self, pathArray):
        image = self.__image
        mask = np.zeros(image.shape[:2], np.uint8)
        cv2.drawContours(mask, pathArray, -1, 255, -1)
        meanValues = cv2.mean(image, mask=mask)
        maxIndex = meanValues.index(max(meanValues))
        return indexToColor(maxIndex)
