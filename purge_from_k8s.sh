#!/bin/bash

kubectl delete -f client/kubernetes/epoch-conversion-client.yaml
kubectl delete -f server/kubernetes/epoch-conversion-server.yaml
