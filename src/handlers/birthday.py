import hug

@hug.get("/anewbirthday")
def home(name: str):
    return "Happy Birthday, {name}".format(name=name)