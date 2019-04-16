import pymongo
from bson.objectid import ObjectId
import json

class connectionobj(object):

  def __init__(self,connectionobj,dbobj):
        self.connection = connectionobj
        self.db = dbobj

  def connectiontes(self):
    self.myclient = pymongo.MongoClient(self.connection) 
    self.mydb = self.myclient[self.db]
    return "start connection"
  
  def coleccion(self,col):
    return self.mydb[col]        
 
  def close(self):
    self.myclient.close()

  def insert(self,data,col): 
      return self.mydb[col].insert_one(data)
  
  def insertmult(self,data,col):
      return self.mydb[col].insert_many(data)

  def update(self,id,data,col):
      if(find(id,col) == "none"):
          return "none"
      return self.mydb[col].update_one({'_id': ObjectId(id)}, {"$set": data})

  def remove_data(self,id,col):
      if(find(id,col) == "none"):
          return "none"
      return self.mydb[col].delete_one({'_id':ObjectId(id)})

  def find(self,id,col):
      for x in self.mydb[col].find({'_id':ObjectId(id)}):
          return x
      return "none"
 
#myclient = pymongo.MongoClient("mongodb+srv://juangui:Juan5157@clustertesting-yew86.azure.mongodb.net/test?retryWrites=true")
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
''' mydb = myclient["mydatabase"]
mycollection = mydb["mycollection"]

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

collist = mydb.list_collection_names()
if "mycollection" in collist:
  print("The collection exists.") '''
