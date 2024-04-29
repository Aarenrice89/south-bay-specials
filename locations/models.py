from django.db import models


class Location(models.Model):
    name = models.CharField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()
    zipcode = models.CharField()
    google_link = models.URLField(null=True)
