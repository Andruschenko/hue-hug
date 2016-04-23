import hug
import os
from hug.types import longer_than, text
from ..database.db import db

# image should come as a base64 string, which will be a certain length
@hug.post("/submit")
def submit(image: longer_than(100, convert=text)):
    return "We just submitted your image"