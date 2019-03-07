"""
WSGI config for viral project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
"""

import os


# Configure environments
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")


# This is imported here to allow the environment variables to be set
from configurations.wsgi import get_wsgi_application  # noqa


# Initialize Django
application = get_wsgi_application()
