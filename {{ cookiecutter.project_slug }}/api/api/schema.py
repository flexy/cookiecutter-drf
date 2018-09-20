from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Schema configuration
schema_view = get_schema_view(
   openapi.Info(
      title='{{ cookiecutter.project_name }}',
      default_version='{{ cookiecutter.project_version }}',
   ),
   validators=['flex', 'ssv'],
   public=False,
   permission_classes=(
       permissions.AllowAny,
   ),
)
