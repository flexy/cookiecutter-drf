#!/bin/bash
docker-compose --version
docker-compose build
docker-compose run --rm web bash -c "
    flake8 . &&
    python wait_for_postgres.py &&
    ./manage.py test
"
