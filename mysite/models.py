import os

from django.db import models

class Amenity(models.Model):
    eng_name = models.CharField(
        max_length=120,
    )
    chi_name = models.CharField(
        max_length=120,
        blank=True,
    )
    icon = models.ImageField(
        blank=True,
        null=True,
    )
