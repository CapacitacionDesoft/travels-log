from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from fleet.models import Driver, Vehicle
# Create your models here.


class Location(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = _('Location')

    name = models.CharField(verbose_name=_('Location'), help_text=_('Location name'), max_length=64, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = _('Material')

    name = models.CharField(verbose_name=_('Material'), help_text=_('Material name'), max_length=64, unique=True)

    def __str__(self):
        return self.name


class Travel(models.Model):
    class Meta:
        ordering = ('departure_date',)
        verbose_name = _('Travel')

    departure_date = models.DateTimeField(verbose_name=_('Departure date'), default=timezone.now, )
    departure_location_id = models.ForeignKey(Location, verbose_name=_('Departure location'), on_delete=models.CASCADE,
                                              related_name="departure_location" )
    arrival_date = models.DateTimeField(verbose_name=_('Arrival date'), default=timezone.now, )
    arrival_location_id = models.ForeignKey(Location, verbose_name=_('Arrival location'), on_delete=models.CASCADE,
                                            related_name="arrival_location")
    driver_id = models.ForeignKey(Driver, verbose_name=_('Driver'), on_delete=models.CASCADE, )
    vehicle_id = models.ForeignKey(Vehicle, verbose_name=_('Vehicle'), on_delete=models.CASCADE, )
    capacity = models.FloatField(verbose_name=_('Capacity'), help_text=_('Vehicle Capacity'),)
    consumption = models.FloatField(verbose_name=_('Consumption'), help_text=_('Vehicle consumption'),)
    state = models.CharField(choices=[('loading', 'Loading'),
                                      ('inprogress', 'In progress'),
                                      ('done', 'Done')], default='loading', max_length=64)

    def __str__(self):
        return self.departure_location_id.name+"/"+self.arrival_location_id.name