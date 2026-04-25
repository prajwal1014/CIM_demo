#!/bin/bash

cd /home/ubuntu/api-rate-limiter-gateway

echo "Pulling latest code..."
git pull origin main

echo "Stopping old containers..."
docker-compose down

echo "Building & starting services..."
docker-compose up -d --build

echo "Deployment complete!"
