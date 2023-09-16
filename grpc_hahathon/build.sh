#!/bin/bash

mkdir -p grpc_golang grpc_python grpc_java
protoc --go-grpc_out=grpc_golang grpc_hahathon.proto
python3 -m grpc_tools.protoc -I. --python_out=grpc_python grpc_hahathon.proto
protoc --java_out=grpc_java grpc_hahathon.proto