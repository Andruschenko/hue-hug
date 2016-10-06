# Burda Hackday Project

# Read README.md first :)

import base64
import math
import re
from copy import deepcopy
from io import BytesIO

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from helpers import findMax, findMin, indexToColor
from image import ClairesImage


class ClairesCutter:

    def __init__(self, inputString, type):
        # todo: validate inputs
        # inputString: The image encoded
        # type: type of encoding (only base64 atm)
        self.__sourceImage = ClairesImage(inputString, type)

    def getSourceImage(self):
        return self.__sourceImage

    def getPositions(self):
        # Array of image positions in the form:
        # {
        # 	"red": [[[x1,y1],[x2,y2]], [[x1,y1],[x2,y2]], [[x1,y1],[x2,y2]]],
        # 	"green": [[[x1,y1],[x2,y2]], [[x1,y1],[x2,y2]], [[x1,y1],[x2,y2]]],
        # 	"blue": [[[x1,y1],[x2,y2]], [[x1,y1],[x2,y2]], [[x1,y1],[x2,y2]]]
        # }
        results = {
            'red': [],
            'green': [],
            'blue': []
        }
        sourceImage = self.__sourceImage

        image = sourceImage.getOpenCV()
        original = image.copy()

        width, height = image.shape[:2]
        if width > 1000 and height > 1000:
            # todo: make divider dynamic
            sourceImage.shrinkImage(5)
            image = sourceImage.getImage()
        openCVImageBinary = sourceImage.getOpenCVBinary()

        img, contours, hierarchy = cv2.findContours(
            openCVImageBinary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < 2000:
                continue
            if len(contour) < 4:
                continue
            rect = cv2.minAreaRect(contour)
            color = self.getColor(contour)
            origin = (rect[0][0] * sourceImage.getDivider(),
                      rect[0][1] * sourceImage.getDivider())
            size = (rect[1][0] * sourceImage.getDivider(),
                    rect[1][1] * sourceImage.getDivider())
            rotationAngle = rect[2]
            transformedRect = (origin, size, rotationAngle)
            results[color].append(transformedRect)

        return results

    # Return the mean color on a path
    def getColor(self, pathArray):
        image = self.__sourceImage.getOpenCV()
        mask = np.zeros(image.shape[:2], np.uint8)
        cv2.drawContours(mask, pathArray, -1, 255, -1)
        meanValues = cv2.mean(image, mask=mask)
        maxIndex = meanValues.index(max(meanValues))
        return indexToColor(maxIndex)

    # Restore proportions of image
    def restoreImage(self):
        self.__sourceImage.restoreImage()

    # Returns copy of the source image with its original proportions
    # Here is a good place to optimize the memory footprint
    def getOriginal(self):
        sourceImage = deepcopy(self.__sourceImage)
        sourceImage.restoreImage()
        return sourceImage

    def crop(self, rect):
        sourceImage = self.getOriginal()
        image = sourceImage.getOpenCV()
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        W = rect[1][0]
        H = rect[1][1]

        Xs = [i[0] for i in box]
        Ys = [i[1] for i in box]
        x1 = min(Xs)
        x2 = max(Xs)
        y1 = min(Ys)
        y2 = max(Ys)

        angle = rect[2]
        # Center of rectangle in source image
        center = ((x1 + x2) / 2, (y1 + y2) / 2)
        # Size of the upright rectangle bounding the rotated rectangle
        size = (x2 - x1, y2 - y1)
        M = cv2.getRotationMatrix2D((size[0] / 2, size[1] / 2), angle, 1.0)
        # Cropped upright rectangle
        cropped = cv2.getRectSubPix(image, size, center)
        cropped = cv2.warpAffine(cropped, M, size)

        croppedRotated = cv2.getRectSubPix(
            cropped, (int(W), int(H)), (size[0] / 2, size[1] / 2))
        return croppedRotated
