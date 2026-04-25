#!/bin/bash

cd /home/ubuntu/CIM_demo

echo "Pulling latest code..."
git pull origin main

echo "Stopping old containers..."
docker compose down

echo "Starting updated containers..."
docker compose up -d --build

echo "Deployment successful!"
