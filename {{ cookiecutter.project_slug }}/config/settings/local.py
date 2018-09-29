from .base import BaseConfiguration


class Local(BaseConfiguration):

    # Apps
    INSTALLED_APPS = BaseConfiguration.INSTALLED_APPS
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    # Debug
    DEBUG = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    # Check if we are inside a Docker container
    if BaseConfiguration.env.bool('USING_DOCKER', False):
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
