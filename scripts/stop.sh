#!/bin/bash
# stop.sh - Stop and remove containers

echo "Stopping Fibonacci API..."
docker-compose down
docker container rm fibonacci-api 2>/dev/null || true

echo "Containers stopped and removed."
