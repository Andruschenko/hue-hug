import os
from pymongo import MongoClient

client = MongoClient('mongodb://{0}:27017/'.format(os.environ['DB_HOST']))
db = client.test
