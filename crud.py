from pymongo import MongoClient
from todo import ToDo
connection_string = "mongodb://localhost:27017/"

client = MongoClient(connection_string)
#print(client.address)

dbs = client.list_database_names()
if "lol" in dbs:
    for db in dbs:
        print(db)

db = client["todos"]
collection = db["todos"]

'''
todo = {"Name": "von Moos"}
collection.insert_one(todo)
'''
collection.delete_many({"Name": "von Moos"})
datasets = collection.find()
for data in datasets:
    print(data)



