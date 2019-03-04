#!/bin/bash

python -m grpc_tools.protoc -Iserver/proto --python_out=server/proto/lib --grpc_python_out=server/proto/lib epoch_converter_service.proto
