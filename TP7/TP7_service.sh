#!/bin/sh

PORT=9999

echo "Service listening on port $PORT..."
nc -lp $PORT -e "./TP7_oracle check_padding"
