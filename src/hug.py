import hug
from handlers import hello, submit

@hug.extend_api('')
def api():
    return [hello, submit]