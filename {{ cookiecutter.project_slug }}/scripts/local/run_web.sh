#!/bin/sh
python scripts/local/wait_for_postgres.py
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
