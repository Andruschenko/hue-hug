import json

import cv2
import matplotlib.pyplot as plt
import numpy as np

from src.processor.cutter import ClairesCutter
from src.processor.image import ClairesImage


class Printer:
    __single = None
    __i = 0
    __plt = plt
    # Making printer a singleton

    def __init__(self):
        self.__plt.figure()
        if Printer.__single:
            raise Printer.__single
        Printer.__single = self

    def add(self, image, title):
        self.__i = self.__i + 1
        self.__plt.subplot(3, 2, self.__i)
        self.__plt.imshow(image)
        self.__plt.title(title)

    def show(self):
        self.__plt.show()


printer = Printer()
with open('test/one-red-hi-there.json') as dataFile:
    jsonData = json.load(dataFile)
cutter = ClairesCutter(jsonData['image'], 'base64')
printer.add(cutter.getOriginal().getOpenCV(), 'Original')
positions = cutter.getPositions()
cutter.restoreImage()
images = []
for color in positions:
    for position in positions[color]:
        printer.add(cutter.crop(position), color)

printer.show()
