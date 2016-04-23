import hug
import os
from src.handlers import profile, submit

@hug.extend_api('')
def api():
  return [profile, submit]