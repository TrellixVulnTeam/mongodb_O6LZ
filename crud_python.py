#import crud.crud
from crud.crud import *

connection = "mongodb://<mongoip>:<mongoport>"
db= "mydatabase"
collection = "mycollection"
test = connectionobj(connection,db,1,3)

ejemplo = test.my_client_connection()
print(ejemplo)

mydata = {'Name':"pruebaconclase"}
ejemplo = test.insert_main(mydata,collection)
print(ejemplo)

mydata = {'Name':"pruebaconclase2"}
ejemplo = test.insert_main(mydata,collection)
print(ejemplo)

with open('jsontest.json') as template:
        template_dct = json.load(template)

ejemplo = test.insert_main(template_dct,collection)



id = "5cc0cc21bc216d4a38d8f188"
mydataupd = {'name': "Carlitos tevez", 'address': "Apple st 652"}
ejemplo = test.update_main(id,mydataupd,collection)
print(ejemplo)
ejemplo = test.find_main(id,collection)
print(ejemplo)
#ejemplo = test.delete_main(id,collection)
#print(ejemplo)

test.close_connection()

''' mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
ejemplo = crud.crud.insertmult(mylist) '''
#data = { "address": 0 }
#ejemplo = crud.crud.find(id)
#print(ejemplo)