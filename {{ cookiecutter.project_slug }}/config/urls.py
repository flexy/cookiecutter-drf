from django.conf import settings
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib import admin


urlpatterns = [
    # Redirect to API root
    path(
        '',
        RedirectView.as_view(
            url=reverse_lazy('api:schema-swagger-ui'),
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
        include(
            'api.api.urls',
            'api',
        ),
    ),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
