import uuid
from django.db import models


class AuditedModel(models.Model):
    """
    Base abstraite.

    - id en UUID (clé primaire)
    - created_at / updated_at
    - is_active : pour un soft-delete simple
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
