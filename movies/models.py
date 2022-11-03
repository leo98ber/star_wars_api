from django.db import models

from base.models import BaseModel


class Planet(BaseModel):
    """Model definition for Planet."""

    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    location = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name


class Film(BaseModel):
    """Model definition for Movie."""

    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    open_text = models.CharField(max_length=5000, blank=False, null=False, default='')
    productor = models.CharField(max_length=150, blank=False, null=False, default='')
    director = models.CharField(max_length=150, blank=False, null=False, default='')
    company_producer = models.CharField(max_length=150, blank=True, null=True, default='')
    release_date = models.CharField(max_length=150, blank=True, null=True, default='')
    planets = models.ManyToManyField(Planet)

    def __str__(self):
        return self.name
