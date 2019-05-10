import environ
from configurations import Configuration


class BaseConfiguration(Configuration):
    # Path configurations
    # /config/settings/base.py - 3 = /
    ROOT_DIR = environ.Path(__file__) - 3
    APPS_DIR = ROOT_DIR.path("api")

    # Environment
    env = environ.Env()

    # Apps
    LOCAL_APPS = ["api.api", "api.users", "api.utils"]
    THIRD_PARTY_APPS = [
        "rest_framework",
        "rest_framework.authtoken",
        "djoser",
        "oauth2_provider",
        "social_django",
        "rest_framework_social_oauth2",
        "django_filters",
        "corsheaders",
        "drf_yasg",
    ]
    DJANGO_APPS = [
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.admin",
    ]

    # https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS

    # https://docs.djangoproject.com/en/dev/ref/settings/#middleware
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    # https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY = env("DJANGO_SECRET_KEY")

    # GENERAL
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = env.bool("DJANGO_DEBUG", default=False)

    # https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#append-slash
    APPEND_SLASH = True

    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])

    # CORS: https://github.com/ottoyiu/django-cors-headers
    CORS_ORIGIN_WHITELIST = env.list("DJANGO_CORS_ORIGIN_WHITELIST", default=[])

    # https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
    ROOT_URLCONF = "config.urls"

    # https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = "config.wsgi.application"

    # Redis
    redis_url = env.str("REDIS_URL", default="redis://redis:6379")

    # Caches
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": redis_url,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "COMPRESSOR": "django_redis.compressors.lz4.Lz4Compressor",
            },
        }
    }

    # Sessions
    # We are using the cache backend with Redis
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"

    # DATABASES
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        # Raises ImproperlyConfigured exception if DATABASE_URL not in
        # os.environ
        "default": env.db(default="postgres://postgres:@postgres:5432/postgres")
    }

    # Static
    # https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = str(ROOT_DIR("staticfiles"))

    # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = "/static/"

    # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = [str(APPS_DIR.path("static"))]

    # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = [
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    ]

    # Templates
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [str(APPS_DIR.path("templates"))],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "social_django.context_processors.backends",
                    "social_django.context_processors.login_redirect",
                ]
            },
        }
    ]

    # Custom authentication
    AUTH_USER_MODEL = "users.User"
    LOGIN_URL = "rest_framework:login"
    LOGOUT_URL = "rest_framework:logout"

    # Authentication
    AUTHENTICATION_BACKENDS = [
        "rest_framework_social_oauth2.backends.DjangoOAuth2",
        "django.contrib.auth.backends.ModelBackend",
    ]

    # django-oauth-toolkit
    OAUTH2_PROVIDER = {
        "OAUTH2_BACKEND_CLASS": "oauth2_provider.oauth2_backends.JSONOAuthLibCore"  # noqa
    }

    # djoser
    DJOSER = {"SERIALIZERS": {"user": "api.users.serializers.UserSerializer"}}

    # Django Rest Framework Social OAuth2
    # http://python-social-auth.readthedocs.io/en/latest/configuration/django.html#database
    SOCIAL_AUTH_POSTGRES_JSONFIELD = True
    DRFSO2_URL_NAMESPACE = "api"

    # Django Rest Framework
    REST_FRAMEWORK = {
        "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": int(env("DJANGO_PAGINATION_LIMIT", default=10)),
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
            "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
            "rest_framework_social_oauth2.authentication.SocialAuthentication",
        ],
        "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
        "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.AcceptHeaderVersioning",
        "DEFAULT_VERSION": "1.0",
    }

    def __init__(self, *args, **kwargs):
        # Initialize sentry
        SENTRY_DSN = self.env("SENTRY_DSN", default=None)
        if SENTRY_DSN:
            import sentry_sdk
            from sentry_sdk.integrations.django import DjangoIntegration

            sentry_sdk.init(SENTRY_DSN, integrations=[DjangoIntegration()])

        return super().__init__(*args, **kwargs)
