#!/bin/bash

ENDPOINT=$1

while true; do
    curl $ENDPOINT?ds=2019-01-01%2005:00:01
done
