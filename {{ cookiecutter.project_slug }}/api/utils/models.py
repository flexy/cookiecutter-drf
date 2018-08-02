import uuid

from django.db import models


class UUIDModel(models.Model):
    """
    An abstract base class model with a UUID as its primary key.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True
