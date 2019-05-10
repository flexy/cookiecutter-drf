#!/bin/sh
celery -A config.celery worker -l info
