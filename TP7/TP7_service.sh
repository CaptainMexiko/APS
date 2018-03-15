#!/bin/sh

PORT=10345

echo "Service listening on port $PORT..."

while :
do
  nc -lp $PORT -e "./TP7_oracle check_padding"
done
