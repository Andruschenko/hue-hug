import re
from io import BytesIO

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def findMax(lists, index):
    pivot = 0
    for item in lists:
        if item[0][index] > pivot:
            pivot = item[0][index]
    return pivot


def findMin(lists, index):
    pivot = 0
    for item in lists:
        if pivot == 0:
            pivot = item[0][index]
        if item[0][index] < pivot:
            pivot = item[0][index]
    return pivot


def colorToIndex(color):
    colors = {
        'red': 0,
        'green': 1,
        'blue': 2
    }
    return colors[color]


def indexToColor(index):
    colors = ['red', 'green', 'blue']
    return colors[index]


def createBlank(size, rgb=(0, 0, 0)):
    image = np.zeros((size[0], size[1], 3), np.uint8)
    color = tuple(reversed(rgb))
    image[:] = color
    image = np.uint8(image * 255)
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
