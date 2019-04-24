import pymongo,json,time,urllib.parse
from bson.objectid import ObjectId
from pymongo import MongoClient

class connectionobj(object):

  def __init__(self,connectionobj,dbobj,secuobj,intenobj):
        self.connection = connectionobj
        self.db = dbobj
        self.secu = secuobj
        self.inten = intenobj
        self.boolconnection = False
  
  def my_client_connection(self):
    for i in range(self.inten):
          try:
            self.myclient = pymongo.MongoClient(self.connection)
            self.mydb = self.myclient[self.db]
            self.boolconnection = True
            return True
          except Exception as e:
            print(e)
            self.boolconnection = False
            self.error= e
            time.sleep(self.secu)
        
  def validate_connection(self):
    for i in range(self.inten):
          try:
            self.mydb.command("serverStatus")
            self.boolconnection = True
            return True
          except Exception as e:
            self.boolconnection = False
            self.error = e  
            time.sleep(self.secu)

  def insert_main(self,data,col):
      typeobj = self.mydb[col].insert_one
      datastructure = [data]
      return self.mongo_called(typeobj,datastructure)
  
  def insert_many_main(self,data,col):
      typeobj = self.mydb[col].insert_many
      datastructure = [data]
      return self.mongo_called(typeobj,datastructure)

  def update_main(self,id,data,col):
      typeobj = self.mydb[col].update_one
      datastructure = [{'_id': ObjectId(id)},{'$set': data}]
      if(self.data_exist(typeobj,id) == False):
            return "Object Not Found"
      return self.mongo_called(typeobj,datastructure)

  def delete_main(self,id,col):
      typeobj = self.mydb[col].delete_one
      datastructure = [{'_id':ObjectId(id)}]
      if(self.data_exist(typeobj,id) == False):
            return "Object Not Found"
      return self.mongo_called(typeobj,datastructure)


  def find_main(self,id,col):
      typeobj = self.mydb[col].find
      datastructure = {'_id':ObjectId(id)}
      return self.data_exist(typeobj,id)

  def data_exist(self,typeobj,id):
      try: 
        for x in typeobj({'_id':ObjectId(id)}):
            return x
        return False
      except Exception as e:
        self.error = e
        return self.error
  
  def mongo_query(self,typeobj,datastructure):
      try:
        return typeobj(*datastructure)
      except Exception as e:
        self.error = e
        return self.error

  def mongo_called(self,typeobj,datastructure):
      if self.boolconnection == False:
        return self.reconnect_client_connection(typeobj,datastructure)
      else:
        if self.validate_connection:
          return self.mongo_query(typeobj,datastructure)
        else:
          return self.reconnect_client_connection(typeobj,datastructure)
  
  def reconnect_client_connection(self,typeobj,datastructure):
      if self.my_client_connection:
          return self.mongo_query(typeobj,datastructure)
      else:
          return self.error

  def close_connection(self):
    if self.validate_connection:
      self.myclient.close()
      return True