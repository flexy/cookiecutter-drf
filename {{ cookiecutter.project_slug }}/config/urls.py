from django.conf import settings
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from api.api.routers import router


swagger_view = get_swagger_view(title='{{ cookiecutter.project_name }} API')

urlpatterns = [
    # Redirect to API root
    path(
        '',
        RedirectView.as_view(
            url=reverse_lazy('api:api-root'),
            permanent=False,
        ),
        name='root',
    ),

    # Site Authentication
    path(
        'auth/',
        include('rest_framework.urls')
    ),

    # Admin
    path('admin/', admin.site.urls),

    # API
    path(
        'api/',
        include((router.urls, 'api')),
    ),

    # API Authentication
    path(
        'api/auth/',
        include('djoser.urls'),
    ),
    path(
        'api/auth/',
        include('djoser.urls.authtoken'),
    ),
    path(
        'api/auth/oauth/',
        include('rest_framework_social_oauth2.urls'),
    ),
    path(
        'api/auth/oauth/',
        include(
            'oauth2_provider.urls',
            namespace='oauth2_provider',
        ),
    ),

    # Swagger
    path(
        'api/swagger/',
        swagger_view,
        name='swagger',
    ),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
