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
    return {'data': False, 'status': 'EROR', 'code': 501}

### use class

class BodyRead(BaseModel): 
    path: str
    skip: int
    tack: int

class File(BaseModel):
    path: str  
    data: str

class User(BaseModel):
    login: str   
    password: str

class WorkSpace(BaseModel):
    login: str
    password: str
    workspace_name: str

class ReadWorkSpace(BaseModel):
    path: str  
    limit: int
    offset: int 

class DataBase(BaseModel):
    folder: str  
    path: str
    data: str 

class DataFile(BaseModel):
    data: str

### testing 

data_base = [
    {'folder': 'media1', 'path': '/foto/test1.png', 'data': '01010100'},
    {'folder': 'media2', 'path': '/foto/test2.png', 'data': '01010101'},
    {'folder': 'media3', 'path': '/video/test3.png', 'data': '01010101'},
    {'folder': 'media4', 'path': '/foto/test4.png', 'data': '01010101'},
    {'folder': 'media5', 'path': '/foto/test5.png', 'data': '01010101'},
    {'folder': 'media6', 'path': '/video/test6.png', 'data': '01010101'},
    {'folder': 'media7', 'path': '/foto/test7.png', 'data': '01010101'},
    {'folder': 'media8', 'path': '/video/test8.png', 'data': '01010101'},
    {'folder': 'media9', 'path': '/foto/test9.png', 'data': '01010101'},
    {'folder': 'media10', 'path': '/foto/test10.png', 'data': '0101010'},
    {'folder': 'media11', 'path': '/foto/test11.png', 'data': '0101010'},
    {'folder': 'media12', 'path': '/video/test12.png', 'data': '1010101'}
]

files = [
    File(path='foto', data='01010100'),
    File(path='/foto/test4.png', data='01010100'),
    File(path='/video/test1.png', data='01010100'),
    File(path='/foto/test8.png', data='01010100')
]

all_workspace = [
    WorkSpace(login='galionme1', password=get_password_hash('123'), workspace_name='name1'),
    WorkSpace(login='galionme2', password=get_password_hash('456'), workspace_name='name2')
]

users = [
    User(login='galionme1', password=get_password_hash('123')),
    User(login='usr', password=get_password_hash('123')),
    User(login='galionme2', password=get_password_hash('456'))
]


### helpers

def authenticate_user(login: str, password: str):
    for user in users:
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

def set_answer_good(response):
    return {"status": 200, "data": response, "detail": "OK"}

### use workspace and user

# check user and set new token - no auth
@app.post('/token')
def login_for_access_token(task: User):
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

# create workspace and create user - no auth 

@app.post('/create_user')
def create_user(task: User):
    # user = authenticate_user(task.login, task.password)
    # if not user:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail='Неправильный логин или пароль',
    #         headers={'Authorization': 'Bearer'},
    #     )
    access_token = create_access_token(
        data={'sub': task.login}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': access_token, 'token_type': 'Bearer'}

@app.post('/create_workspace')
def create_workspace(workspace: WorkSpace):
    all_workspace.append(WorkSpace(login=workspace.login, password=get_password_hash(workspace.password), workspace_name=workspace.workspace_name))

    access_token = create_access_token(
        data={'sub': workspace.login}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

@app.post('/read_path')
def read_path(task: ReadWorkSpace, current_user: User = Depends(oauth2_scheme)):
    path = task.path
    offset = task.offset
    limit = task.limit - 1
    response = []
    for data in data_base:
        if (offset > limit): break
        if (data.get('path').find(path)):
            response.append(data)
            offset += 1
    return {'data': response, 'status': 'OK', 'code': 200}

### use files

@app.get('/delete_file/{path}')
def upload_file(path: str, current_user: User = Depends(oauth2_scheme)):
    for file in files:
        if file.path == path:
            files.remove(file)
            return {'data': path, 'status': 'OK', 'code': 200}
    return get_bad_answer()

@app.post('/upload_file/{path}')
def upload_file(task: DataFile, path: str, current_user: User = Depends(oauth2_scheme)):
    newFile = File(path = path, data = task.data)
    files.append(newFile)
    return {'data': path, 'status': 'OK', 'code': 200}

@app.post('/replace_file/{path}')
def replace_file(task: DataFile, path: str, current_user: User = Depends(oauth2_scheme)):
    data = task.data
    for file in files:
        if file.path == path:
            file.path = data
            return {'data': path, 'status': 'OK', 'code': 200}
    return get_bad_answer()

@app.get('/give_file/{path}')
def give_file(path: str, current_user: User = Depends(oauth2_scheme)):
    for file in files:
        if file.path == path:
            return {'data': file.data, 'status': 'OK', 'code': 200}
    return get_bad_answer()

### use folders

@app.get('/create_folder/{folder}')
def create_folder(folder: str, current_user: User = Depends(oauth2_scheme)):
    return {'data': folder, 'status': 'OK', 'code': 200}

@app.get('/delete_folder/{folder}')
def delete_folder(folder: str, current_user: User = Depends(oauth2_scheme)):
    return {'data': folder, 'status': 'OK', 'code': 200}

@app.get('/give_folder/{folder}')
def give_folder(folder: str, current_user: User = Depends(oauth2_scheme)):
    return {'data': folder, 'status': 'OK', 'code': 200}

### use grpc

# test grpc
@app.get('/test')
def test():
    with grpc.insecure_channel('localhost:8785') as channel:
        stub = grpc_pb2.TransmissionStub(channel)
        req = pb2.Path(path="go")
        responce = stub.DeleteFileOnServer(req)
        print(responce)
    pass

### logs output - logging.info()

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"), 
        logging.StreamHandler()  
    ]
)
