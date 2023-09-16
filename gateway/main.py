from typing import List
import logging
import jwt
from pydantic import BaseModel, Field
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
# import grpc
# import my_service_pb2
# import my_service_pb2_grpc
import http.client
import json

SECRET_KEY = 'hahathon'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(
    title='Gateway'
)

# def com_grpc():
#     channel = grpc.insecure_channel('localhost:8785')
#     client = my_service_pb2_grpc.MyServiceStub(channel)
#     request = my_service_pb2.MyRequest(name='Alice')
#     response = client.ProcessData(request)
#     logging.info(response.message)

def com_push():
    conn = http.client.HTTPSConnection("127.0.0.1", 9999)
    payload = json.dumps([
    {
        "path": "/123",
        "data": "string",
        "folder": True
    }
    ])
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnYWxpb25tZSIsImV4cCI6MTY5NDg1NDY2M30.Vf8r7Xh4XQ7mKU8WY2gX4PPiO2uvvv_OtyOgola8QC8',
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/put_files", payload, headers)
    res = conn.getresponse()
    data = res.read()
    logging.info(data.decode("utf-8"))


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"), 
        logging.StreamHandler()  
    ]
)

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token') 

class BodyRead(BaseModel): 
    path: str
    skip: int = Field(..., ge=0)   
    tack: int = Field(..., ge=0)   

class File(BaseModel):
    path: str  
    data: str = Field(..., min_length=1) 

class User(BaseModel):
    login: str = Field(..., min_length=6)    
    password: str = Field(..., min_length=3)   

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str):
    for user in users:
        if user.login == username and pwd_context.verify(password, user.password):
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

@app.post('/token')
def login_for_access_token(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неправильный логин или пароль',
            headers={'Authorization': 'Bearer'},
        )
    access_token = create_access_token(
        data={'sub': user.login}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

@app.get('/protected_route')
def protected_route(current_user: User = Depends(oauth2_scheme)):
    return {'message': 'Авторизированы успешно!'}

data_base = [
    {'path': '/foto/test1.png', 'data': '0101010'},
    {'path': '/video/test2.png', 'data': '1010101'}
]

def set_answer_good(response):
    return {"status": 200, "data": response, "detail": "OK"}

def set_answer_bad():
    return {"status": 404, "data": "EROR", "detail": "Неправильный логин или пароль"}

@app.post('/put_files')
def put_files(file: List[File],current_user: User = Depends(oauth2_scheme)):
    data_base.extend(file)
    return set_answer_good(data_base)

@app.get('/delete_file')
def delete_file(path: str, current_user: User = Depends(oauth2_scheme)):
    for file in data_base:
        if file.get('path') == path:
            data_base.remove(file)
    return set_answer_good(data_base)

@app.post('/read_files') 
def read_files(body: BodyRead, current_user: User = Depends(oauth2_scheme)):
    return set_answer_good(body)

@app.post('/create_user')
def put_files(user: User):
    users.append(User(login=user.login, password=get_password_hash(user.password)))
    access_token = create_access_token(
        data={'sub': user.login}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

users = [
    User(login='galionme', password=get_password_hash('123')),
    User(login='user_login2', password=get_password_hash('user_password2'))
]