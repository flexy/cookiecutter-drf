#!/bin/sh
watchmedo auto-restart --patterns="*.py" -d api -- celery -A config.celery worker -l info
