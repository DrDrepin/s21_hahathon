#!/bin/bash

protoc --go-grpc_out=../s3_service --go_out=../s3_service grpc.proto
python3 -m grpc_tools.protoc -I. --python_out=../gateway --grpc_python_out=../gateway grpc.proto
protoc --java_out=../user_service grpc.proto