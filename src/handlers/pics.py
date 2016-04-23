import hug
import os
from .. import config
from ..database.db import db

@hug.get("/pics")
def pics(user: hug.types.text):
    return {
      'data': 'These are the pictures for {0}'.format(user)
    }