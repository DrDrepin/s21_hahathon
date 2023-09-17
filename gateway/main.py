from collections import OrderedDict
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
gRPC_ADRS = 'localhost:8785'

app = FastAPI(
    title='Gateway'
)

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

#
# JWT format
# X.X.X 
# {
#   "login": "usr",
#   "workspace_name": "name",
#   "password": "123",
#   "exp": 1694926432
# }
#
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token') 

# module OBJECT #
class File(BaseModel):
    data: bytes

class User(BaseModel):
    login: str
    password: str
 
class Person(BaseModel):
    login: str
    password: str
    workspace_name: str

class TokenData(BaseModel):
    login: str 
    workspace_name: str 
    password: str
    exp: int

# module HELP #
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_bad_answer():
    return {'data': False, 'status': 'ERROR', 'code': 501}

def create_access_token(data: dict, workspace: str, password: str, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'workspace_name': workspace})
    to_encode.update({'password': password})
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        # if 'exp' in payload and payload['exp'] < datetime.utcnow():
        #     return None
        # else:
        return OrderedDict(payload)
    except jwt.ExpiredSignatureError:
        return None

# module API #
@app.post('/token')
def login_for_access_token(task: Person):
    login = task.login
    password = task.password
    workspace_name = task.workspace_name
    user = gRPC_ReadUser(login, password, workspace_name)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неправильный логин или пароль',
            headers={'Authorization': 'Bearer'},
        )
    access_token = create_access_token(
        data={'login': login}, workspace = workspace_name, password = password, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': access_token, 'token_type': 'Bearer'}

@app.post('/create_user/{workspace_name}')
def create_user(task: User, workspace_name: str):
    status = gRPC_CreateUser(task.login, task.password, workspace_id)
    if status == True:
        access_token = create_access_token(
            data={'sub': task.login}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {'access_token': access_token, 'token_type': 'Bearer'}
    return {'access_token': False, 'token_type': 'Bearer'}
    access_token = create_access_token(
        data={'login': task.login}, workspace = workspace_name, password = task.password, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': access_token, 'token_type': 'Bearer'}

#file
@app.get('/create_workspace')
def create_workspace(current_user: TokenData = Depends(oauth2_scheme)):
    token = decode_jwt(current_user)
    workspace_name = token.get('workspace_name')
    # status = gRPC_CreateWorkspace(workspace_name)
    # message = MessageToDict(status)
    # print(message)
    if status !="":
        return {'data': True, 'status': 'OK', 'code': 200} #,"workspace_id":status["id"]
    return get_bad_answer()

@app.post('/upload_file')
def upload_file(task: File, path: str, current_user: TokenData = Depends(oauth2_scheme)):
    token = decode_jwt(current_user)
    User = gRPC_ReadUser(token.get('login'), token.get('password'), token.get('workspace_name'))
    if not User: 
        return get_bad_answer()
    File = gRPC_CreateFile(path, User.workspace_id, File.data)
    if not File:
        return get_bad_answer()
    return {'data': File, 'status': 'OK', 'code': 200}

@app.get('/give_file')
def give_file(path: str, current_user: TokenData = Depends(oauth2_scheme)):
    token = decode_jwt(current_user)
    User = gRPC_ReadUser(token.get('login'), token.get('password'), token.get('workspace_name'))
    if not User: 
        return get_bad_answer()
    File = gRPC_GetFile(User.workspace_id, path)
    if not File:
        return get_bad_answer()
    return {'data': File, 'status': 'OK', 'code': 200}

@app.get('/delete_file')
def delete_file(path: str, current_user: TokenData = Depends(oauth2_scheme)):
    token = decode_jwt(current_user)
    User = gRPC_ReadUser(token.get('login'), token.get('password'), token.get('workspace_name'))
    if not User: 
        return get_bad_answer()
    File = gRPC_DeleteFile(User.workspace_id, path)
    if not File:
        return get_bad_answer()
    return {'data': File, 'status': 'OK', 'code': 200}

#folder
@app.get('/give_folder')
def give_folder(path=str, current_user: TokenData = Depends(oauth2_scheme)):
    token = decode_jwt(current_user)
    User = gRPC_ReadUser(token.get('login'), token.get('password'), token.get('workspace_name'))
    if not User: 
        return get_bad_answer() 
    File = gRPC_GetFolder(User.workspace_id, path)
    if not File:
        return get_bad_answer()
    return {'data': File, 'status': 'OK', 'code': 200}

@app.get('/delete_folder')
def delete_folder(path=str, current_user: TokenData = Depends(oauth2_scheme)):
    token = decode_jwt(current_user)
    User = gRPC_ReadUser(token.get('login'), token.get('password'), token.get('workspace_name'))
    if not User: 
        return get_bad_answer() 
    Status = gRPC_DeleteFolder(User.workspace_id, path)
    if Status == False:
        return get_bad_answer()
    return {'data': File, 'status': 'OK', 'code': 200}

@app.get('/create_folder')
def create_folder(path=str, current_user: TokenData = Depends(oauth2_scheme)):
    token = decode_jwt(current_user)
    User = gRPC_ReadUser(token.get('login'), token.get('password'), token.get('workspace_name'))
    if not User: 
        return get_bad_answer() 
    Status = gRPC_CreateFolder(User.workspace_id, path)
    message = MessageToDict(Status)
    if message["status"] == False:
        return get_bad_answer()
    return { 'status': 'OK', 'code': 200}


# module gRPC #
#user
def gRPC_CreateUser(login: str, password: str, workspace_id: str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.User(login=login, password=password, workspace_id=workspace_id)
        responce = stub.CreateUser(req)
        logging.info(responce)
    return responce

def gRPC_ReadUser(login: str, password: str, workspace_id: str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.User(login=login, password=password, workspace_id=workspace_id)
        responce = stub.ReadUser(req)
        logging.info(responce)
    return responce

def gRPC_UpdateUser(login: str, password: str, workspace_id: str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.User(login=login, password=password, workspace_id=workspace_id)
        responce = stub.UpdateUser(req)
        logging.info(responce)
    return responce

#workspace
def gRPC_CreateWorkspace(name: str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.Workspace(name=name)
        responce = stub.CreateWorkspace(req)
        logging.info(responce)
    return responce

#file
def gRPC_CreateFile(path: str, workspace_id: str, buffer: bytes):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.File(path=path, workspace_id=workspace_id, buffer=buffer)
        responce = stub.CreateFile(req)
        logging.info(responce)
    return responce

def gRPC_DeleteFile(workspace_id: str, path:str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.WorkspaceFile(workspace_id=workspace_id, path=path)
        responce = stub.DeleteFile(req)
        logging.info(responce)
    return responce

def gRPC_GetFile(workspace_id: str, path:str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.WorkspaceFile(workspace_id=workspace_id, path=path)
        responce = stub.GetFile(req)
        logging.info(responce)
    return responce

#folder
def gRPC_GetFolder(path: str, workspace_id: str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.Folder(path=path, workspace_id=workspace_id)
        responce = stub.GetFolder(req)
        logging.info(responce)
    return responce

def gRPC_CreateFolder(path: str, workspace_id: str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.Folder(path=path, workspace_id=workspace_id)
        responce = stub.CreateFolder(req)
        logging.info(responce)
    return responce

def gRPC_DeleteFolder(path: str, workspace_id: str):
    with grpc.insecure_channel(gRPC_ADRS) as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.Folder(path=path, workspace_id=workspace_id)
        responce = stub.DeleteFolder(req)
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