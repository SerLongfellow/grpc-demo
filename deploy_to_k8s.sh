#!/bin/bash

kubectl apply -f client/kubernetes/epoch-conversion-client.yaml
kubectl apply -f server/kubernetes/epoch-conversion-server.yaml
