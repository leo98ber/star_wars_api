from django.db import models

from base.models import BaseModel
from movies.models import Film


class Character(BaseModel):
    """Model definition for Character."""

    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    performer = models.CharField(max_length=150, blank=False, null=False)
    movies = models.ManyToManyField(Film)
