from django.contrib import admin

from locations.models import Location
from specials.models import Special

admin.site.register(Location)
admin.site.register(Special)
