from .base import BaseConfiguration


class Production(BaseConfiguration):

    # Apps
    INSTALLED_APPS = BaseConfiguration.INSTALLED_APPS
    INSTALLED_APPS += (
        'gunicorn',
    )

    # Middleware
    MIDDLEWARE = BaseConfiguration.MIDDLEWARE
    MIDDLEWARE += (
        # Simplified static file serving.
        # https://warehouse.python.org/project/whitenoise/
        'whitenoise.middleware.WhiteNoiseMiddleware',
    )

    # Static files config
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # noqa
