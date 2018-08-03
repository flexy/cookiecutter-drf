#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin "$DEPLOY_DEV_REGISTRY_URL"
docker build -t "$DEPLOY_DEV_APP_URL" -f Dockerfile-prod .
docker push "$DEPLOY_DEV_APP_URL"
