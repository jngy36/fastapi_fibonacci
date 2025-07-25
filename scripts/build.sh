#!/bin/bash
# build.sh - Build the Docker image

echo "Building Fibonacci API Docker image..."
docker build -t fibonacci-api:latest .

echo "Build completed successfully!"
