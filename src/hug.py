import hug
from handlers import pics, submit

@hug.extend_api('')
def api():
    return [pics, submit]