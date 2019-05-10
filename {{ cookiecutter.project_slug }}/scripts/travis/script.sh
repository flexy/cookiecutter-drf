#!/bin/bash
docker-compose --version
docker-compose -f docker-compose.test.yml build
docker-compose -f docker-compose.test.yml run --rm web scripts/travis/run_tests.sh
