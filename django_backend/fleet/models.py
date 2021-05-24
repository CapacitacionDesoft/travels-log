from django.db import models
from django.utils.translation import ugettext_lazy as _


class Driver(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = _('Driver')

    name = models.CharField(verbose_name=_('Name'), help_text=_('Driver name'), max_length=64, unique=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    class Meta:
        ordering = ('plate',)
        verbose_name = _('Vehicle')

    brand = models.CharField(verbose_name=_('Brand'), help_text=_('Vehicle brand'), max_length=64,)
    model = models.CharField(verbose_name=_('Model'), help_text=_('Vehicle model'), max_length=64,)
    plate = models.CharField(verbose_name=_('Plate'), help_text=_('Vehicle plate'), max_length=64, unique=True)
    capacity = models.FloatField(verbose_name=_('Capacity'), help_text=_('Vehicle Capacity'),)
    consumption = models.FloatField(verbose_name=_('Consumption'), help_text=_('Vehicle consumption'),)

    def __str__(self):
        return self.plate