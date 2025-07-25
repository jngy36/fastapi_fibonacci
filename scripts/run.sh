#!/bin/bash
# run.sh - Run the container

echo "Starting Fibonacci API container..."
docker run -d \
  --name fibonacci-api \
  -p 8000:8000 \
  --restart unless-stopped \
  fibonacci-api:latest

echo "Container started! API available at http://localhost:8000"
