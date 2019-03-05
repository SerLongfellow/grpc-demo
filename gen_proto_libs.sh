#!/bin/bash

python -m grpc_tools.protoc -Iproto --python_out=proto/lib --grpc_python_out=proto/lib epoch_converter_service.proto

python -m grpc_tools.protoc -Iproto --python_out=proto/lib --grpc_python_out=proto/lib health_check.proto
