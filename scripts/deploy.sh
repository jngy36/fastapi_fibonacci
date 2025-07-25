#!/bin/bash
# deploy.sh - Deploy using docker-compose

echo "Deploying Fibonacci API with docker-compose..."
docker-compose down
docker-compose build
docker-compose up -d

echo "Deployment completed! API available at http://localhost:8000"
echo "Check logs with: docker-compose logs -f"
