from django.conf import settings
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from api.v1.routers import router as v1_router


swagger_view = get_swagger_view(title='cookiecutter-drf API')

urlpatterns = [
    # API V1
    path(
        'api/v1/',
        include(
            (
                v1_router.urls,
                'v1',
            ),
            namespace='api-v1',
        ),
    ),
    path(
        'api/swagger/',
        swagger_view,
        name='swagger',
    ),

    # Authentication
    path(
        'auth/',
        include('rest_framework.urls')
    ),

    path(
        'api/v1/auth/',
        include('djoser.urls'),
    ),
    path(
        'api/v1/auth/',
        include('djoser.urls.authtoken'),
    ),
    path(
        'api/v1/auth/oauth/',
        include('rest_framework_social_oauth2.urls'),
    ),
    path(
        'api/v1/auth/oauth/',
        include(
            'oauth2_provider.urls',
            namespace='oauth2_provider',
        ),
    ),

    # Admin
    path('admin/', admin.site.urls),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    path(
        '',
        RedirectView.as_view(
            url=reverse_lazy('api-v1:api-root'),
            permanent=False,
        ),
        name='root',
    ),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
