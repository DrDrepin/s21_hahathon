from typing import List
import logging
from jose import jwt
from pydantic import BaseModel, Field
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
import array
import grpc
import grpc_helper
import grpc_pb2 as pb2
import grpc_pb2_grpc as grpc_pb2

from google.protobuf.json_format import Parse, ParseDict,MessageToDict
import json

import http.client
import json

SECRET_KEY = 'hahathon'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(
    title='Gateway'
)

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token') 

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_bad_answer():
    return {'data': False, 'status': 'ERROR', 'code': 501}

### use class

class File(BaseModel):
    path: str  
    data: bytes

class User(BaseModel):
    login: str
    password: str

class ReadWorkSpace(BaseModel):
    path: str  
    limit: int
    offset: int 
 
class Person(BaseModel):
    login: str
    password: str

class DataFile(BaseModel):
    data: str

Users = [
    Person(login= 'usr', password=get_password_hash('123')),
    Person(login= 'adm', password=get_password_hash('123'))
]

### testing 

### helpers

def authenticate_user(login: str, password: str):
    for user in Users:
        if user.login == login and pwd_context.verify(password, user.password):
            return user
    return None

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

### use workspace and user

@app.post('/token')
def login_for_access_token(task: Person):
    login = task.login
    password = task.password
    user = authenticate_user(login, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неправильный логин или пароль',
            headers={'Authorization': 'Bearer'},
        )
    access_token = create_access_token(
        data={'sub': user.login}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': access_token, 'token_type': 'Bearer'}

@app.post('/create_user/{workspace_id}')
def create_user(task: User, workspace_id: str):
    status = gRPC_CreateUser(task.login, task.password, workspace_id)
    if status == True:
        access_token = create_access_token(
            data={'sub': task.login}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {'access_token': access_token, 'token_type': 'Bearer'}
    return {'access_token': False, 'token_type': 'Bearer'}

@app.get('/create_workspace/{workspace_name}')
def create_workspace(workspace_name: str):
    status = gRPC_CreateWorkspace(workspace_name)
    message = MessageToDict(status)
    print(message)
    if status !="":
        return {'data': True, 'status': 'OK', 'code': 200} #,"workspace_id":status["id"]
    return get_bad_answer()

@app.post('/upload_file/{workspace_id}')
def upload_file(task: File, workspace_id: str):
    status = gRPC_CreateFile(task.path, workspace_id, task.data)
    if status == True:
        return {'data': True, 'status': 'OK', 'code': 200}
    return get_bad_answer()

@app.get('/give_file/{workspace_id}/{path}')
def give_file(workspace_id: str, path: str):
    File = gRPC_GetFile(workspace_id, path)
    if not File:
        return get_bad_answer()
    return {'data': File, 'status': 'OK', 'code': 200}

@app.get('/give_folder/{workspace_id}/{path}')
def give_folder(workspace_id: str, path=str):
    File = gRPC_GetFolder(workspace_id, path)
    if not File:
        return get_bad_answer()
    return {'data': File, 'status': 'OK', 'code': 200}






# @app.post('/read_path')
# def read_path(task: ReadWorkSpace, current_user: User = Depends(oauth2_scheme)):
#     status = ()
#     if status == True:
#         return {'data': True, 'status': 'OK', 'code': 200}
#     return {'data': False, 'status': 'OK', 'code': 200}

### use folders


# @app.get('/delete_folder/{folder}')
# def delete_folder(folder: str, current_user: User = Depends(oauth2_scheme)):
#     return {'data': folder, 'status': 'OK', 'code': 200}


### use files


# @app.get('/delete_file/{path}')
# def upload_file(path: str, current_user: User = Depends(oauth2_scheme)):
#     for file in files:
#         if file.path == path:
#             files.remove(file)
#             return {'data': path, 'status': 'OK', 'code': 200}
#     return get_bad_answer()



# @app.post('/replace_file/{path}')
# def replace_file(task: DataFile, path: str, current_user: User = Depends(oauth2_scheme)):
#     data = task.data
#     for file in files:
#         if file.path == path:
#             file.path = data
#             return {'data': path, 'status': 'OK', 'code': 200}
#     return get_bad_answer()


### use grpc

# test grpc
def gRPC_CreateUser(login: str, password: str, workspace_id: str):
    with grpc.insecure_channel('localhost:8785') as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.User(login=login, password=password, workspace_id=workspace_id)
        responce = stub.CreateUser(req)
        logging.info(responce)
    return responce

def gRPC_CreateWorkspace(name: str):
    with grpc.insecure_channel('localhost:8785') as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.Workspace(name=name)
        responce = stub.CreateWorkspace(req)
        logging.info(responce)
    return responce

def gRPC_CreateFile(path: str, workspace_id: str, buffer: bytes):
    with grpc.insecure_channel('localhost:8785') as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.File(path=path, workspace_id=workspace_id, buffer=buffer)
        responce = stub.CreateFile(req)
        logging.info(responce)
    return responce

def gRPC_GetFile(workspace_id: str, path:str):
    with grpc.insecure_channel('localhost:8785') as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.WorkspaceFile(workspace_id=workspace_id, path=path)
        responce = stub.GetFile(req)
        logging.info(responce)
    return responce

def gRPC_GetFolder(path: str, workspace_id: str):
    with grpc.insecure_channel('localhost:8785') as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.Folder(path=path, workspace_id=workspace_id)
        responce = stub.GetFolder(req)
        logging.info(responce)
    return responce

### logs output - logging.info()

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"), 
        logging.StreamHandler()  
    ]
)