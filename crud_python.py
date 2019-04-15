import crud.crud

mydata = {'Name':"pruebaconeccioncerrada"}
connection = "mongodb+srv://juangui:Juan5157@clustertesting-yew86.azure.mongodb.net/test?retryWrites=true"
db= "mydatabase"
collection = "mycollection"

ejemplo = crud.crud.insert(mydata,connection,db,collection)

#id = "5cb0e141bc216d25ac165922"
#mydataupd = { 'name': "Carlitos tevez", 'address': "Apple st 652"}
#ejemplo = crud.crud.find('5cb0bd8bbc216d283c871b20')

#ejemplo = crud.crud.remove_data(id)
#print(ejemplo)
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

print(ejemplo)


