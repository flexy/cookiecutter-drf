#!/bin/sh
flake8 . &&
python scripts/local/wait_for_postgres.py &&
pytest --cov=./
