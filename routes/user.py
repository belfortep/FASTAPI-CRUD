from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()

@user.get('/users')
def findAllUser():
    return usersEntity(conn.local.user.find())#de la base de datos que va a buscar

@user.post('/users')
def createUser(user: User):
    newUser = dict(user)

    del newUser["id"]   #para no guardar id null

    id = conn.local.user.insert_one(newUser).inserted_id

    user = conn.local.user.find_one({"_id": id})
    
    return userEntity(user)

@user.put('/users/{id}')
def updateUser():
    return "hello"

@user.delete('/users/{id}')
def deleteUser():
    return "hello"

@user.get('/users/{id}')
def findUser():
    return "hello"
