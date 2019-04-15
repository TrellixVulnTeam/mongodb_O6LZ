import pymongo
from bson.objectid import ObjectId

#myclient = pymongo.MongoClient("mongodb+srv://juangui:Juan5157@clustertesting-yew86.azure.mongodb.net/test?retryWrites=true")
#mydb = myclient.pruebaseti


#client = pymongo.MongoClient("mongodb+srv://juangui:<password>@test-uy8l8.mongodb.net/test?retryWrites=true")
#db = client.test

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
''' mydb = myclient["mydatabase"]
mycollection = mydb["mycollection"]

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

collist = mydb.list_collection_names()
if "mycollection" in collist:
  print("The collection exists.") '''

def connectionobj(connection, db, collection):
  myclient = pymongo.MongoClient(connection) 
  dblist = myclient.list_database_names()
  if "mydatabase" in dblist:
    mydb = myclient[db]
  else:
    mydb = myclient[db]
  collist = mydb.list_collection_names()
  if "mycollection" in collist:
    mycollection = mydb[collection]
  else:
    mycollection = mydb[collection]
    mycollection.insert_many({'Name':"testonlytest"})
    mycollection.delete_one({'Name':"testonlytest"})
  return mycollection, myclient
      

def insert(data,connection,db,collection):
    mycollection,myclient = connectionobj(connection, db, collection)   
    mycollection.insert_one(data)
    myclient.close()
    return "insertado"
 
def insertmult(data,connection,db,collection):
    mycollection,myclient = connectionobj(connection, db, collection) 
    mycollection.insert_many(data)
    myclient.close()
    return "insertado multiples"

def update(id,data,connection,db,collection):
    mycollection,myclient = connectionobj(connection, db, collection) 
    if(find(id) == "none"):
        myclient.close()
        return "Dato no existe"
    mycollection.update_one({'_id': ObjectId(id)}, {"$set": data})
    myclient.close()
    return "Actualizado"


def remove_data(id,connection,db,collection):
    mycollection,myclient = connectionobj(connection, db, collection) 
    if(find(id) == "none"):
        myclient.close()
        return "Dato no existe"
    mycollection.delete_one({'_id':ObjectId(id)})
    myclient.close()
    return "eliminado"


def find(id,connection,db,collection):
    mycollection,myclient = connectionobj(connection, db, collection) 
    for x in mycollection.find({'_id':ObjectId(id)}):
        myclient.close()
        return x
    myclient.close()
    return "none"
 

