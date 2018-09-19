from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Extend this router with your own routes
# E.g.: router.registry.extend(your_router.registry)
router = DefaultRouter()


# API URL configuration
app_urls = [
    # API
    path(
        '',
        include(router.urls),
    ),

    # API Authentication
    path(
        'auth/',
        include('djoser.urls'),
    ),
    path(
        'auth/',
        include('djoser.urls.authtoken'),
    ),
    path(
        'auth/oauth/',
        include('rest_framework_social_oauth2.urls'),
    ),
    path(
        'auth/oauth/',
        include('oauth2_provider.urls'),
    ),
]


# Schema configuration
schema_view = get_schema_view(
   openapi.Info(
      title='{{ cookiecutter.project_name }}',
      default_version='{{ cookiecutter.project_version }}',
   ),
   validators=['flex', 'ssv'],
   public=False,
   patterns=app_urls,
)
schema_urls = [
    # Swagger
    re_path(
        r'swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]


# Final URL configuration
app_name = 'api'
urlpatterns = app_urls + schema_urls
