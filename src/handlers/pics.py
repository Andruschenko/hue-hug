import hug
import os
import config
# import pydocumentdb.document_client as document_client

# client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})

# db = client.CreateDatabase({ 'id': config.DOCUMENTDB_DATABASE })
# collection = client.CreateCollection(db['_self'],{ 'id': config.DOCUMENTDB_COLLECTION }, { 'offerType': 'S1' })
# document = client.CreateDocument(collection['_self'],
#         { 'id': config.DOCUMENTDB_DOCUMENT,
#           'Web Site': 0,
#           'Cloud Service': 0,
#           'Virtual Machine': 0,
#           'name': config.DOCUMENTDB_DOCUMENT 
#         })

@hug.get("/pics")
def pics(user: hug.types.text):
    return {
      'data': 'These are the pictures for {0}'.format(user)
    }