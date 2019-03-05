#!/bin/bash

docker build --tag epoch-conversion-client -f client/docker/Dockerfile .
docker build --tag epoch-conversion-server -f server/docker/Dockerfile .
