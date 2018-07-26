#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin "$REGISTRY"
docker build -t "$DEV_URL" -f Dockerfile-prod .
docker push "$DEV_URL"
