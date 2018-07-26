from .base import BaseConfiguration


class Test(BaseConfiguration):

    # Debug
    DEBUG = True

    # Email
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
