from django.db import models

from base.models import BaseModel


class Film(BaseModel):
    """Model definition for Movie."""

    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
