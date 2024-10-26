from django.db import models


class Location(models.Model):
    name = models.CharField()
    address = models.CharField()
    phone_number = models.CharField(null=True)
    website = models.CharField(null=True)
    google_place_id = models.CharField()
    google_url = models.CharField(null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
