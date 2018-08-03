#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin "$DEPLOY_PROD_REGISTRY_URL"
docker build -t "$DEPLOY_PROD_APP_URL" -f Dockerfile-prod .
docker push "$DEPLOY_PROD_APP_URL"
