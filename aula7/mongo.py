#!/usr/bin/python3

from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from bson import ObjectId

try:
    con = MongoClient()
    db = con['aulamongo']
except Exception as e:
    print('Erro: {}'.format(e))

#trazer o primeiro registro
# print(db.usuarios.find_one())


# usuarios = []

# for usuario in db.usuarios.find():
#     usuarios.append(usuario)
#     #print(usuario)

# print(usuarios)

# usuarios = [x for x in db.usuarios.find()]

# print(usuarios)

#db.usuarios.remove({ "_id": 1}) 
#db.usuarios.update({"_id": 2}, {"$set":{"name": "pedro"}})
# db.usuarios.insert({"_id":1, "nome":'bruno', "sobrenome":'lima'})
#inserindo
# d = datetime.now()
# date = {
#     "_id": 4,
#     "nome": "tales",
#     "sobrenome": "ferrer",
#     "hora": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
# }
# db.usuarios.insert(date)

# usuarios = [x for x in db.usuarios.find()]
# print(usuarios)



db.usuarios.remove({"_id": ObjectId("5bd8fb8746af7c614a0662f4")})

usuarios = [x for x in db.usuarios.find()]
print(usuarios)