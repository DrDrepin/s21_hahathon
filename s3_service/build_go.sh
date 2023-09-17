#!/bin/bash

protoc --go-grpc_out=. --go_out=. grpc.proto
