from fastapi import APIRouter, Response
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
user = APIRouter()

@user.get('/users')
def findAllUser():
    return usersEntity(conn.local.user.find())#de la base de datos que va a buscar

@user.post('/users')
def createUser(user: User):
    newUser = dict(user)
    newUser["password"] = sha256_crypt.encrypt(newUser["password"])
    del newUser["id"]   #para no guardar id null

    id = conn.local.user.insert_one(newUser).inserted_id

    user = conn.local.user.find_one({"_id": id})
    
    return userEntity(user)

@user.put('/users/{id}')
def updateUser(id: str, user:User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/users/{id}')
def deleteUser(id: str):
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.get('/users/{id}')
def findUser(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))
