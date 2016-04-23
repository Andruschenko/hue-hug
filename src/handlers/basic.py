import hug
import os
from .. import config
from ..database.db import db

@hug.get("/")
def home():
  return "Welcome home."