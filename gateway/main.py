from collections import OrderedDict
from typing import List
import logging
from jose import jwt
from typing import Annotated 
from pydantic import BaseModel, Field
from fastapi import FastAPI, status, HTTPException, Depends, UploadFile
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
import array
import grpc
import grpc_helper
import grpc_pb2 as pb2
import grpc_pb2_grpc as grpc_pb2
import gRPC_methods

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
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token') 

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"), 
        logging.StreamHandler()  
    ]
)

