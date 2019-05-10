#!/bin/sh
flake8 . &&
black --check &&
python scripts/local/wait_for_postgres.py &&
pytest --cov=./
