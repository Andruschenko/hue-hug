import hug
from hug.types import longer_than, text

@hug.post("/submit")
# image should come as a base64 string, which will be a certain length
def submit(image: longer_than(100, convert=text)):
    return "We just submitted your image"