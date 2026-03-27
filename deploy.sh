#!/bin/bash
set -e

cd /home/ubuntu/api-rate-limiter-gateway

git pull origin main

docker stop api-rate-limiter || true
docker rm api-rate-limiter || true

docker build -t api-rate-limiter .

docker run -d \
  --name api-rate-limiter \
  -p 8000:8000 \
  --restart unless-stopped \
  api-rate-limiter
