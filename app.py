import hug
import os
from src.handlers import pics, submit

@hug.extend_api('')
def api():
  print(os.environ['DB_HOST'])
  return [pics, submit]