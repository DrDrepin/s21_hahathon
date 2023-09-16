#!/bin/bash

protoc --go-grpc_out=../s3_service grpc.proto
python3 -m grpc_tools.protoc -I. --grpc_python_out=../gateway grpc.proto
protoc --java_out=../user_service grpc.proto