#!/bin/sh
watchmedo auto-restart --patterns="*.py" -d api -- celery -A config.celery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
