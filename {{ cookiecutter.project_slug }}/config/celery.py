from celery import Celery
from configurations import importer


# Initialize Django Configurations and Django
importer.install()

# Setup Celery
app = Celery("api")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
