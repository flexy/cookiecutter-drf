#!/bin/bash
docker-compose --version
docker-compose build
docker-compose run --rm web bash -c "
    flake8 . &&
    python scripts/local/wait_for_postgres.py &&
    pytest --cov=./
"
