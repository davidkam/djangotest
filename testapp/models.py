import os

from django.db import models

class Amenity(models.Model):
    eng_name = models.CharField(
        max_length=120,
        verbose_name='English Name',
    )
    chi_name = models.CharField(
        max_length=120,
        blank=True,
        verbose_name='Chinese Name',
    )
    icon = models.ImageField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "amenity"
        verbose_name_plural = "amenities"

    def __unicode__(self):
        return u'{}'.format(
            self.eng_name
        )

class Newobj(models.Model):
    field1 = models.CharField(
        max_length=20,
    )
