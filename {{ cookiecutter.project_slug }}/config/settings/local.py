from .base import BaseConfiguration


class Local(BaseConfiguration):

    # Apps
    INSTALLED_APPS = BaseConfiguration.INSTALLED_APPS
    INSTALLED_APPS += (
        'debug_toolbar',
    )

    # Middleware
    MIDDLEWARE = BaseConfiguration.MIDDLEWARE
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    # https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    # Debug
    DEBUG = True

    # Email
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
