from django.conf import settings
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from api.v1.routers import router as v1_router


schema_view = get_swagger_view(title='cookiecutter-drf API')

urlpatterns = [
    # API
    path(
        'api/v1/',
        include(v1_router.urls),
    ),
    path(
        'api/swagger/',
        schema_view
    ),

    # Authentication
    path(
        'api/v1/api-auth/',
        include('rest_auth.urls'),
    ),
    path(
        'api/v1/api-auth/registration/',
        include('rest_auth.registration.urls'),
    ),
    path(
        'api/v1/oauth/',
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
            url=reverse_lazy('api-root'),
            permanent=False,
        ),
    ),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
