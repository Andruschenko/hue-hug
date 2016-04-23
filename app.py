import hug
import os
from src.handlers import basic, profile, submit

@hug.extend_api('')
def api():
  return [basic, profile, submit]