#!/bin/bash

mkdir istio-setup
cd istio-setup
curl -L https://git.io/getLatestIstio | sh -
cd istio*

kubectl apply -f install/kubernetes/helm/istio/templates/crds.yaml
kubectl apply -f install/kubernetes/istio-demo.yaml

kubectl label namespace default istio-injection=enabled
