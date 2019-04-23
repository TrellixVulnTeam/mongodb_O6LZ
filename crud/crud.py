import pymongo
from bson.objectid import ObjectId
import json
from pymongo.errors import ConnectionFailure
import urllib.parse
from pymongo import MongoClient
import time

class connectionobj(object):

  def __init__(self,userobj,passwobj,uriobj,connectionobj,dbobj,secuobj,intenobj):
        self.user = userobj
        self.passw = passwobj
        self.uri = uriobj
        self.connection = connectionobj
        self.db = dbobj
        self.secu = secuobj
        self.inten = intenobj
        self.boole = False

  def connectiontes(self):
    self.myclientconnection()
  
  def coleccion(self,col):
        return self.mydb[col]   
  
  def myclientconnection(self):
    username = urllib.parse.quote_plus('user')
    username = self.user
    password = urllib.parse.quote_plus('pass/word')
    password = self.passw
    uricon = urllib.parse.quote_plus('uri')
    uricon = self.uri
    for i in range(self.inten):
          try:
            #self.myclient = pymongo.MongoClient(self.connection)
            self.myclient = pymongo.MongoClient('mongodb+srv://%s:%s@%s' % (username, password, uricon))
            self.mydb = self.myclient[self.db]
            self.boole = True
            return True
          except Exception as e:
            self.boole = False
            self.error= e
            time.sleep(self.secu)
        
  def testdbconnection(self):
    for i in range(self.inten):
          try:
            self.mydb.command("serverStatus")
            self.boole = True
            return True
          except Exception as e:
            self.boole = False
            self.error = e  
            time.sleep(self.secu)
        
  def insert(self,data,col):
      if(self.boole == False):
        if (self.myclientconnection() == True):
            try:
              return self.mydb[col].insert_one(data)
            except Exception as e:
              self.error = e
              return self.error
        else:
          return self.error
      else:
        if(self.testdbconnection() == True):
          try:
            return self.mydb[col].insert_one(data)
          except Exception as e:
            self.error = e
            return self.error
        else:
          if (self.myclientconnection() == True):
                try:
                  return self.mydb[col].insert_one(data)
                except Exception as e:
                  self.error = e
                  return self.error
          else:
            return self.error
              
  def insertmult(self,data,col):
      if(self.boole == False):
            if (self.myclientconnection() == True):
              try:
                return self.mydb[col].insert_many(data)
              except Exception as e:
                self.error = e
                return self.error
            else:
              return self.error
      else:
        if(self.testdbconnection() == True):
          try:
            return self.mydb[col].insert_many(data)
          except Exception as e:
            self.error = e
            return self.error
        else:
          if (self.myclientconnection() == True):
                try:
                  return self.mydb[col].insert_many(data)
                except Exception as e:
                  self.error = e
                  return self.error
          else:
            return self.error
      

  def update(self,id,data,col):
      if(find(id,col) == False):
          return "Object Not Found"
      if(self.boole == False):
            if (self.myclientconnection() == True):
              try:
                return self.mydb[col].update_one({'_id': ObjectId(id)}, {"$set": data})
              except Exception as e:
                self.error = e
                return self.error
            else:
              return self.error
      else:
        if(self.testdbconnection() == True):
          try:
            return self.mydb[col].update_one({'_id': ObjectId(id)}, {"$set": data})
          except Exception as e:
            self.error = e
            return self.error
        else:
          if (self.myclientconnection() == True):
                try:
                  return self.mydb[col].update_one({'_id': ObjectId(id)}, {"$set": data})
                except Exception as e:
                  self.error = e
                  return self.error
          else:
            return self.error

  def remove_data(self,id,col):
      if(self.boole == False):
            if (self.myclientconnection() == True):
              try:
                if(find(id,col) == False):
                  return "Object Not Found"
                return self.mydb[col].delete_one({'_id':ObjectId(id)})
              except Exception as e:
                self.error = e
                return self.error
            else:
              return self.error
      else:
          if(self.testdbconnection() == True):
            try:
              if(find(id,col) == False):
                return "Object Not Found"
              return self.mydb[col].delete_one({'_id':ObjectId(id)})
            except Exception as e:
              self.error = e
              return self.error
          else:
            if (self.myclientconnection() == True):
                  try:
                    if(find(id,col) == False):
                      return "Object Not Found"
                    return self.mydb[col].delete_one({'_id':ObjectId(id)})
                  except Exception as e:
                    self.error = e
                    return self.error
            else:
              return self.error  

  def find(self,id,col):
      if(self.boole == False):
            if (self.myclientconnection() == True):
              try:
                for x in self.mydb[col].find({'_id':ObjectId(id)}):
                  return x
                return False
              except Exception as e:
                self.error = e
                return self.error
            else:
              return self.error
      else:
        if(self.testdbconnection() == True):
          try:
            for x in self.mydb[col].find({'_id':ObjectId(id)}):
              return x
            return False
          except Exception as e:
            self.error = e
            return self.error
        else:
          if (self.myclientconnection() == True):
                try:
                  for x in self.mydb[col].find({'_id':ObjectId(id)}):
                    return x
                  return False
                except Exception as e:
                  self.error = e
                  return self.error
          else:
            return self.error

  def findall(self,col):
      if(self.boole == False):
            if (self.myclientconnection() == True):
              try:
                return self.mydb[col].find()
              except Exception as e:
                self.error = e
                return self.error
            else:
              return self.error
      else:
          if(self.testdbconnection() == True):
            try:
              return self.mydb[col].find()
            except Exception as e:
              self.error = e
              return self.error
          else:
            if (self.myclientconnection() == True):
              try:
                return self.mydb[col].find()   
              except Exception as e:
                self.error = e
                return self.error
              else:
                return self.error

  def close(self):
    if(self.testdbconnection == True):
      self.myclient.close()
      return True