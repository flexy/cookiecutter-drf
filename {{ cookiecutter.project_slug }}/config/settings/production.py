from .base import BaseConfiguration


class Production(BaseConfiguration):

    # Apps
    INSTALLED_APPS = BaseConfiguration.INSTALLED_APPS
    INSTALLED_APPS += [
        'gunicorn',
    ]

    # Middleware
    MIDDLEWARE = BaseConfiguration.MIDDLEWARE
    MIDDLEWARE += [
        # Simplified static file serving.
        # https://warehouse.python.org/project/whitenoise/
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    # Static files config
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # noqa

    # SSL: https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
