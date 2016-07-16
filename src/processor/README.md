# The ClaireCut Algorithm

The algorithm to detect circular shapes in images to "clairecut" out information related to the colors r=red, g=green and b=blue.

## Basic schema of the algorithm

#### 1. Image Preparation: Enhance colors and blackout grey parts
The image is converted into a numpy array and all 3 color channels are enhanced, such that r-g-b values are set to one, whist whilst all white (grey) colors are set to zero. The resulting image will be binary and mainly black, apart from the colored circles. The image is then cleaned and refined by using morphological expand and contract operations to delete remaining dots.

#### 2. Convert image for OpenCV
The image is converted from base64 string to OpenCVBinary so it can be manipulated with OpenCV (creating a binary image). 

#### 3. Extract contours from image
Using openCV´s cv2.findContours option, coordinates of the circle contours are extracted. The max and min coordinates (top left and bottom right) are then stored into an array and associated to the corresponding color.



## Filestructure

The script is run in getpositions.py, wich is also the main script, containing the logical structure. 

#### crop.py
Contains functions to:
- crop detected circular shapes
- transform images to different data formats
- contains a debugging script to look at image parts (commented out)
- send images to Microsofts Oxford project Optical Character Recognition API (currently not implemented)
- image conversion to json

#### helpers.py
Contains functions to:
- transform images to different data formats


#### getpositions.py
In here, the image is preprocessed and circular shapes are detected and stored. It is the script where the logic is implemented and helpers and crop functions are called. The image processing (see "Basic schema of the algorithm") takes place here. 
It contains the functions to:
- enhance colors
- blackout grey pixels
- clean the image
- run the openCV findContours option



## ToDos:
- the code is not yet functional, for example the preprocessing is not called anywhere
- the code needs cleaning, throw out stuff that is not important
- the getPositions function is messy

## Issues:
- dynamic thresholding
