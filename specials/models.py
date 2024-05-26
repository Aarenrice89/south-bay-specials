from django.db import models

from locations.models import Location
from specials.choices import DAY_CHOICES


class Special(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    limitations = models.TextField(blank=True)
    day_of_week = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    is_active = models.BooleanField(default=True)
