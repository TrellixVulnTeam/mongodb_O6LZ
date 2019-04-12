import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://juangui:Juan5157@clustertesting-yew86.azure.mongodb.net/test?retryWrites=true")
#mydb = myclient.pruebaseti


#client = pymongo.MongoClient("mongodb+srv://juangui:<password>@test-uy8l8.mongodb.net/test?retryWrites=true")
#db = client.test

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycollection = mydb["mycollection"]

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

collist = mydb.list_collection_names()
if "mycollection" in collist:
  print("The collection exists.")

def insert(data):
    mycollection.insert_one(data)
    return "insertado"

def insertmult(data):
    mycollection.insert_many(data)
    return "insertado multiples"

def update(id,data):
    if(find(id) == "none"):
        return "Dato no existe"
    mycollection.update_one({'_id': ObjectId(id)}, {"$set": data})
    return "Actualizado"


def remove_data(id):
    if(find(id) == "none"):
        return "Dato no existe"
    mycollection.delete_one({'_id':ObjectId(id)})
    return "eliminado"


def find(id):
    for x in mycollection.find({'_id':ObjectId(id)}):
        return x
    return "none"


myclient.close()