#import librarys
import json
import re
import base64
import numpy as np

#Plt is only needed to plot and "debug" the image.
import matplotlib.pyplot as plt
import cv2

from io import BytesIO
from PIL import Image

from helpers import *

class Imageloader(object):
	def load(self, path = 'Testimages/image1.jpg'):
		return plt.imread(path)/255.

	def show(self, image):
		"""
		Displays the image as it is loaded.
		"""
		plt.figure(1)
		plt.imshow(image)
		plt.colorbar()
		plt.show()

class Preprocessor(Imageloader):
	# def __init__(self):
	#     self.image = np.empty

	def getGrayThreshold(self, image):
		#select red/green/blue channel
		red = image[:, :, 0]
		green = image[:, :, 1]
		blue = image[:, :, 2]
		plt.figure(1)
		plt.gray()
		plt.subplot(2, 2, 1)
		plt.imshow(image)
		plt.title('color')
		plt.subplot(2, 2, 2)
		plt.imshow(red)
		plt.title('red channel')
		plt.subplot(2 ,2, 3)
		plt.imshow(green)
		plt.title('green channel')
		plt.subplot(2, 2, 4)
		plt.imshow(blue)
		plt.title('blue channel')

		# Create the histograms of the three color channels separately
		# using the np.histogram function. Use 50 bis and a range of (0, 1)
		# Afterwards plot them into one histogram line plot. 
		red_histogram = np.histogram(red, bins=50, range=(0,1))
		green_histogram = np.histogram(green, bins=50, range=(0,1))
		blue_histogram = np.histogram(blue, bins=50, range=(0,1))
		red_bins = red_histogram[1]
		central_bins = (red_bins[1:] + red_bins[:-1]) / 2.

		plt.figure(2)
		plt.title('histograms of 3 color channels')
		plt.plot(central_bins, blue_histogram[0], label='blue')
		plt.plot(central_bins, green_histogram[0], label='green')
		plt.plot(central_bins, red_histogram[0], label='red')
		plt.grid()
		plt.legend()

	#enhance Colors, so e.g. .8red =>1.0red
	def enhanceColors(self, image):
		image[image > config['threshold']] = 1
		image[image <= config['threshold']] = 0
		return image
		

	#make all white pixels to black pisels
	#This takes ages to run...
	def blackOutWhitePixels(self, image):
		for i in xrange(image.shape[0]):
			for j in xrange(image.shape[1]):
				if image[i,j,0] == image[i,j,1] == image[i,j,2]:
					image[i,j] = 0
		return image

	def morpholocicalOperations(self.image)




image = Imageloader().load()
# Imageloader().show(image)

enhanced_image = Preprocessor().enhanceColors(image)
black_image = Preprocessor().blackOutWhitePixels(enhanced_image)
Imageloader().show(black_image)








# image = Imageloader().load()
# Imageloader().showImage()

# image = im_container.loadImage()
# im_container.showImage()




# im_pre_process = Preprocessor()
# im_pre_process.image = im_container.image
# im_pre_process.enhanceColors()
# im_pre_process.whiteToBlack()




plt.show()
