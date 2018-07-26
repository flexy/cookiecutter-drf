from django.contrib.auth.models import AbstractUser

from api.utils.models import UUIDModel


class User(AbstractUser, UUIDModel):
    pass
