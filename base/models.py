from django.db import models


class BaseModel(models.Model):
    """Model definition for BaseModel."""

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
