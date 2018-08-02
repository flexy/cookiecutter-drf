from .base import BaseConfiguration


class Local(BaseConfiguration):

    # Debug
    DEBUG = True

    # Apps
    INSTALLED_APPS = BaseConfiguration.INSTALLED_APPS
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    # Middleware
    MIDDLEWARE = BaseConfiguration.MIDDLEWARE
    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE

    # https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    # Check if we are inside a Docker container
    if BaseConfiguration.env('USING_DOCKER') == 'true':
        import socket

        # Add the container IP to INTERNAL_IPS
        hostname, _, ips = socket.gethostbyname_ex(
            socket.gethostname()
        )
        INTERNAL_IPS += [ip[:-1] + '1' for ip in ips]

    # Email
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
