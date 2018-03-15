#!/bin/sh

PORT=10345
while : 
do
  echo "Service listening on port $PORT..."
  nc -lp $PORT -e "./TP7_oracle check_padding"
done
