import hug
import os
import json
from hug.types import longer_than, text
from ..database.db import db

# image should come as a base64 string, which will be a certain length
@hug.post("/submit")
def submit(image: longer_than(100, convert=text)):
  # image will be a variable with base64 string
  
  # takes the image from a json file as base64

  # perform your image manipulation here, transform to json coords

  # cut out actual images from coordinates

  # return images as an array of base64 strings
  return json.dumps({ "bubu": "hello" })