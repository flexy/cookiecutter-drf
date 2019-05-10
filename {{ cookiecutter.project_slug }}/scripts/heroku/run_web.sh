#!/bin/sh
gunicorn config.wsgi:application -b 0.0.0.0:${PORT} -k config.server.production.ProductionUvicornWorker --access-logfile -
